"""Views and API hooks for asynchronous web-based play."""

import json
import random
from collections.abc import Mapping
from urllib.parse import quote

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.utils import timezone
from django.views.decorators.http import require_GET, require_http_methods
from evennia.utils.ansi import strip_ansi
from evennia.utils.utils import class_from_module

from .models import AsyncAction, AsyncScene, AsyncScenePost
from .utils import build_character_sheet_payload


def _is_admin(account) -> bool:
    """Check whether an account has elevated access."""
    return bool(account.is_superuser or account.check_permstring("Admin"))


def _owned_characters(account):
    """Return approved characters belonging to this account."""
    Character = class_from_module("typeclasses.characters.Character")
    characters = Character.objects.all()
    return [
        char
        for char in characters
        if char.account == account and getattr(char.db, "approved", False)
    ]


def _approved_characters():
    """Return all approved characters for invitation lists."""
    Character = class_from_module("typeclasses.characters.Character")
    return [char for char in Character.objects.all() if getattr(char.db, "approved", False)]


def _character_by_id(character_id: int):
    """Load a Character typeclass instance by id."""
    Character = class_from_module("typeclasses.characters.Character")
    return get_object_or_404(Character, id=character_id)


def _can_access_character(account, character) -> bool:
    """Enforce owner-or-admin access to character async data."""
    if _is_admin(account):
        return True
    return character.account == account


def _scene_member_characters(scene, account):
    """Return participant characters in scene owned by this account."""
    return [char for char in scene.participants.all() if char.account == account]


def _can_view_scene(scene, account) -> bool:
    """Determine if account can view this scene."""
    if _is_admin(account) or scene.creator == account:
        return True
    if scene.privacy == AsyncScene.PRIVACY_OPEN:
        return True
    return bool(_scene_member_characters(scene, account))


def _can_post_to_scene(scene, account) -> bool:
    """Determine if account may add posts to this scene."""
    if _is_admin(account) or scene.creator == account:
        return True
    return bool(_scene_member_characters(scene, account))


def _can_manage_scene(scene, account) -> bool:
    """Only creator/admin can change scene metadata or completion."""
    return _is_admin(account) or scene.creator == account


def _dots(value: int, max_value: int = 5) -> str:
    """Render UTF-8 dot rating."""
    try:
        numeric = int(value or 0)
    except (TypeError, ValueError):
        numeric = 0
    safe_value = max(0, min(numeric, max_value))
    return ("●" * safe_value) + ("○" * (max_value - safe_value))


def _as_mapping(value):
    """Return dict-like values as a plain dict, otherwise empty dict."""
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _format_name(value: str) -> str:
    """Humanize a stat key."""
    return str(value).replace("_", " ").title()


def _format_merits(merits: dict) -> list[dict]:
    """Normalize merit data for display."""
    if not isinstance(merits, Mapping):
        return []
    rows = []
    for merit_name, merit_value in (merits or {}).items():
        if isinstance(merit_value, Mapping):
            dots = merit_value.get("dots", merit_value.get("perm", merit_value.get("value", 0)))
        else:
            dots = merit_value
        try:
            dots_num = int(dots or 0)
        except (TypeError, ValueError):
            dots_num = 0
        base_name = merit_name
        if ":" in merit_name:
            base_name, instance = merit_name.split(":", 1)
            label = f"{_format_name(base_name)} ({_format_name(instance)})"
        else:
            label = _format_name(base_name)
        rows.append({"label": label, "dots": _dots(dots_num), "value": dots_num})
    rows.sort(key=lambda item: item["label"])
    return rows


def _flatten_powers(value, prefix: str = "") -> list[tuple[str, object]]:
    """Flatten nested power structures into key/value entries."""
    entries = []
    if isinstance(value, Mapping):
        for key, subvalue in value.items():
            key_str = str(key)
            full_key = f"{prefix}:{key_str}" if prefix else key_str
            if isinstance(subvalue, Mapping):
                entries.extend(_flatten_powers(subvalue, full_key))
            elif isinstance(subvalue, list):
                if not subvalue:
                    entries.append((full_key, "known"))
                for item in subvalue:
                    entries.append((f"{full_key}:{item}", "known"))
            else:
                entries.append((full_key, subvalue))
    elif isinstance(value, list):
        for item in value:
            entries.append((str(item), "known"))
    return entries


def _normalize_stat_key(value: str) -> str:
    """Normalize data keys for robust comparisons."""
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_").replace("'", "")


def _contract_category_and_tier(contract_type: str) -> tuple[str, str]:
    """Map changeling contract type to display category and tier."""
    normalized = _normalize_stat_key(contract_type)
    tier = "Royal" if normalized.endswith("_royal") or normalized.endswith("royal") else "Common"
    base = normalized.replace("_royal", "").replace("_common", "")

    court_buckets = {"spring", "summer", "autumn", "winter", "high_tide", "low_tide", "flood_tide", "ebb_tide"}
    regalia_map = {
        "crown": "Crown",
        "jewels": "Jewels",
        "mirror": "Mirror",
        "shield": "Shield",
        "steed": "Steed",
        "sword": "Sword",
        "chalice": "Chalice",
        "coin": "Coin",
        "stars": "Stars",
        "thorn": "Thorn",
        "goblin": "Goblin",
        "independent": "Independent",
    }
    if base in court_buckets:
        return "Court", tier
    return regalia_map.get(base, _format_name(base)), tier


def _format_contract_power_label(contract_key: str, contract_data: Mapping) -> str:
    """Format a changeling contract with category and tier metadata."""
    contract_name = str(contract_data.get("name") or _format_name(contract_key))
    category, tier = _contract_category_and_tier(str(contract_data.get("contract_type", "")))
    return f"{contract_name} ({category}, {tier})"


def _format_powers(powers: dict) -> list[str]:
    """Format powers for display."""
    labels = set()
    try:
        from world.cofd.powers.changeling_contracts import get_contract
    except Exception:
        get_contract = None

    for power_name, power_value in _flatten_powers(powers):
        status = str(power_value or "").strip().lower()
        if status in {"", "0", "false", "none"}:
            continue

        if ":" in power_name:
            power_type, short_name = power_name.split(":", 1)
        else:
            power_type, short_name = "", power_name

        contract_data = None
        if get_contract:
            contract_data = get_contract(_normalize_stat_key(short_name))
            if not contract_data:
                contract_data = get_contract(_normalize_stat_key(power_name))

        if contract_data:
            labels.add(_format_contract_power_label(short_name, contract_data))
        elif power_type:
            labels.add(f"{_format_name(short_name)} ({_format_name(power_type)})")
        else:
            labels.add(_format_name(power_name))
    return sorted(labels)


def _build_sheet_display(character) -> dict:
    """Build a CoD-friendly sheet display payload."""
    stats = _as_mapping(getattr(character.db, "stats", {}) or {})
    attributes = _as_mapping(stats.get("attributes", {}))
    skills = _as_mapping(stats.get("skills", {}))
    advantages = _as_mapping(stats.get("advantages", {}))
    bio = _as_mapping(stats.get("bio", {}))
    merits = stats.get("merits", {})
    powers = stats.get("powers", {})
    if not powers:
        powers = getattr(character.db, "powers", {}) or {}
    other = _as_mapping(stats.get("other", {}))

    section_map = {
        "mental": ("intelligence", "wits", "resolve"),
        "physical": ("strength", "dexterity", "stamina"),
        "social": ("presence", "manipulation", "composure"),
    }

    attributes_display = {
        section: [
            {"label": _format_name(attr), "dots": _dots(attributes.get(attr, 0))}
            for attr in attrs
        ]
        for section, attrs in section_map.items()
    }

    skill_groups = {
        "mental": ("academics", "computer", "crafts", "investigation", "medicine", "occult", "politics", "science"),
        "physical": ("athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry"),
        "social": ("animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"),
    }
    skills_display = {
        section: [
            {"label": _format_name(skill), "dots": _dots(skills.get(skill, 0))}
            for skill in skill_names
        ]
        for section, skill_names in skill_groups.items()
    }

    advantages_display = []
    for name, value in advantages.items():
        if isinstance(value, Mapping):
            value_display = ", ".join(f"{_format_name(k)}: {v}" for k, v in value.items()) or "-"
        elif isinstance(value, list):
            value_display = ", ".join(str(item) for item in value) or "-"
        else:
            value_display = value
        advantages_display.append({"label": _format_name(name), "value": value_display})
    advantages_display.sort(key=lambda item: item["label"])

    pools_display = []
    template = str(other.get("template", "")).strip().lower()
    resource_pools = {
        "geist": ("Plasm", "plasm"),
        "changeling": ("Glamour", "glamour"),
        "werewolf": ("Essence", "essence"),
        "mage": ("Mana", "mana"),
        "demon": ("Aether", "aether"),
        "promethean": ("Pyros", "pyros"),
    }
    if template in resource_pools:
        pool_name, pool_key = resource_pools[template]
        pool_max = int(other.get(pool_key, 0) or 0)
        pool_current = getattr(character.db, f"{pool_key}_current", None)
        if pool_current is None:
            pool_current = pool_max
        pools_display.append({"label": pool_name, "value": f"{pool_current}/{pool_max}"})

    extra_pools = _as_mapping(getattr(character.db, "pools", {}) or {})
    for pool_name, pool_value in sorted(extra_pools.items(), key=lambda item: str(item[0])):
        if isinstance(pool_value, Mapping):
            current = pool_value.get("current", pool_value.get("value", 0))
            maximum = pool_value.get("max", pool_value.get("maximum", current))
            value_display = f"{current}/{maximum}"
        else:
            value_display = str(pool_value)
        pools_display.append({"label": _format_name(pool_name), "value": value_display})

    try:
        from world.utils.health_utils import get_health_track

        health_max = int(advantages.get("health", 0) or 0)
        health_track = get_health_track(character)
        bashing = sum(1 for damage in health_track if damage == "bashing")
        lethal = sum(1 for damage in health_track if damage == "lethal")
        aggravated = sum(1 for damage in health_track if damage == "aggravated")
        total_damage = bashing + lethal + aggravated
        current_health = max(0, health_max - total_damage)
        damage_parts = [part for part in [f"B:{bashing}" if bashing else "", f"L:{lethal}" if lethal else "", f"A:{aggravated}" if aggravated else ""] if part]
        health_display = f"{current_health}/{health_max}" if health_max else "-"
        if damage_parts:
            health_display = f"{health_display} ({', '.join(damage_parts)})"
    except Exception:
        health_display = str(advantages.get("health", "-"))

    aspirations_display = []
    raw_aspirations = getattr(character.db, "aspirations", []) or []
    for aspiration in raw_aspirations:
        if isinstance(aspiration, Mapping):
            description = str(aspiration.get("description", "")).strip()
            if not description:
                continue
            asp_type = str(aspiration.get("type", "short-term")).strip().lower()
            if asp_type in {"short", "short-term"}:
                label = "Short-Term"
            elif asp_type in {"long", "long-term"}:
                label = "Long-Term"
            else:
                label = _format_name(asp_type)
            aspirations_display.append({"label": label, "value": description})
        elif isinstance(aspiration, str) and aspiration.strip():
            aspirations_display.append({"label": "Aspiration", "value": aspiration.strip()})

    return {
        "header": {
            "name": character.key,
            "template": other.get("template", "Mortal"),
            "concept": bio.get("concept", ""),
            "seeming": bio.get("seeming", ""),
            "kith": bio.get("kith", ""),
        },
        "bio": bio,
        "attributes": attributes_display,
        "skills": skills_display,
        "advantages": advantages_display,
        "health": health_display,
        "pools": pools_display,
        "aspirations": aspirations_display,
        "merits": _format_merits(merits),
        "powers": _format_powers(powers),
    }


def _parse_json_body(request):
    """Parse JSON body or return None."""
    try:
        return json.loads(request.body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return None


def _parse_int_list(value):
    """Parse list of ints from list or comma-separated string."""
    if not value:
        return []
    if isinstance(value, list):
        candidates = value
    else:
        candidates = [chunk.strip() for chunk in str(value).split(",")]
    output = []
    for item in candidates:
        try:
            output.append(int(item))
        except (TypeError, ValueError):
            continue
    return output


def _scene_wiki_url(scene) -> str:
    """Build external wiki URL for a published scene log."""
    if not scene.wiki_log_slug:
        return ""
    base_url = getattr(settings, "ASYNC_WIKI_LOG_BASE_URL", "").strip()
    if not base_url:
        return ""
    encoded_title = quote(scene.wiki_log_slug, safe="/:")
    if "title=" in base_url:
        return f"{base_url}{encoded_title}"
    return f"{base_url.rstrip('/')}/{encoded_title}"


def _serialize_scene(scene, include_posts: bool = False, account=None):
    """Serialize scene for API output."""
    payload = {
        "id": scene.id,
        "title": scene.title,
        "privacy": scene.privacy,
        "scene_type": scene.scene_type,
        "pacing": scene.pacing,
        "is_completed": scene.is_completed,
        "is_public_log": scene.is_public_log,
        "wiki_log_slug": scene.wiki_log_slug,
        "wiki_log_url": _scene_wiki_url(scene),
        "location": scene.location,
        "ic_date": str(scene.ic_date),
        "plot": scene.plot,
        "tags": scene.tags,
        "notes": scene.notes,
        "summary": scene.summary,
        "creator": scene.creator.username,
        "participants": [
            {
                "id": char.id,
                "name": char.key,
                "owner": char.account.username if char.account else None,
                "description": (getattr(char.db, "desc", "") or "").strip(),
            }
            for char in scene.participants.all()
        ],
        "related_scene_ids": list(scene.related_scenes.values_list("id", flat=True)),
        "created_at": scene.created_at.isoformat(),
        "updated_at": scene.updated_at.isoformat(),
        "last_activity_at": scene.last_activity_at.isoformat(),
    }
    if account is not None:
        payload["can_manage"] = _can_manage_scene(scene, account)
        payload["can_post"] = _can_post_to_scene(scene, account)
        payload["can_reopen"] = (
            scene.is_completed and (
                _can_manage_scene(scene, account) or bool(_scene_member_characters(scene, account))
            )
        )
    if include_posts:
        payload["posts"] = [
            {
                "id": post.id,
                "post_type": post.post_type,
                "content": post.content,
                "account": post.account.username,
                "character_name": post.character.db_key if post.character else None,
                "created_at": post.created_at.isoformat(),
            }
            for post in scene.posts.select_related("account", "character").all()
        ]
    return payload


def _format_room_label(room) -> str:
    """Format room location as `Room Name -- Hierarchy1 -- Hierarchy2`."""
    hierarchy = getattr(room.db, "location_hierarchy", []) or []
    if isinstance(hierarchy, str):
        hierarchy = [hierarchy]
    clean = [str(item).strip() for item in hierarchy if str(item).strip()]
    if len(clean) < 2:
        clean += ["Unknown"] * (2 - len(clean))
    parts = [room.key] + clean[:2]
    return " -- ".join(parts)


def _has_ooc_db_tag(room) -> bool:
    """Check room.db.tags for explicit OOC markers."""
    raw_tags = getattr(room.db, "tags", None)
    if not raw_tags:
        return False
    if isinstance(raw_tags, str):
        tokens = [raw_tags.strip().lower()]
    elif isinstance(raw_tags, dict):
        tokens = [str(key).strip().lower() for key in raw_tags.keys()]
    else:
        try:
            tokens = [str(tag).strip().lower() for tag in raw_tags]
        except TypeError:
            tokens = [str(raw_tags).strip().lower()]
    return any(token in {"ooc", "ooc area"} for token in tokens if token)


def _is_chargen_room(room) -> bool:
    """Identify chargen rooms by typeclass, key, or db tag."""
    try:
        if room.is_typeclass("typeclasses.rooms.ChargenRoom", exact=False):
            return True
    except Exception:
        pass

    key = (room.key or "").strip().lower()
    if "chargen" in key:
        return True

    raw_tags = getattr(room.db, "tags", None)
    if not raw_tags:
        return False
    if isinstance(raw_tags, str):
        tokens = [raw_tags.strip().lower()]
    elif isinstance(raw_tags, dict):
        tokens = [str(key).strip().lower() for key in raw_tags.keys()]
    else:
        try:
            tokens = [str(tag).strip().lower() for tag in raw_tags]
        except TypeError:
            tokens = [str(raw_tags).strip().lower()]
    return "chargen" in tokens


def _available_room_locations():
    """Return all rooms with hierarchy labels for scene creation."""
    Room = class_from_module("typeclasses.rooms.Room")
    rooms = Room.objects.all().order_by("db_key")
    output = []
    for room in rooms:
        if _is_chargen_room(room):
            continue
        if _has_ooc_db_tag(room):
            continue
        output.append({"id": room.id, "label": _format_room_label(room), "name": room.key})
    return output


def _publish_scene_log_to_wiki(scene) -> tuple[bool, str]:
    """
    Publish scene log to MediaWiki API and return status/message.

    This uses bot/service account credentials from settings (preferably in
    `secret_settings.py`) and writes a page using the Log template format.
    """
    api_url = getattr(settings, "ASYNC_MEDIAWIKI_API_URL", "").strip()
    base_url = getattr(settings, "ASYNC_WIKI_LOG_BASE_URL", "").strip()
    bot_username = getattr(settings, "ASYNC_MEDIAWIKI_USERNAME", "").strip()
    bot_password = getattr(settings, "ASYNC_MEDIAWIKI_PASSWORD", "").strip()
    storyteller_name = getattr(settings, "ASYNC_WIKI_LOG_USERNAME", "").strip() or bot_username or "AsyncSystem"
    title_prefix = getattr(settings, "ASYNC_MEDIAWIKI_TITLE_PREFIX", "scene-log").strip()

    if not api_url or not base_url or not bot_username or not bot_password:
        return False, "MediaWiki API settings are incomplete."

    participants = sorted({char.key for char in scene.participants.all()})
    participants_markup = " ".join(f"[[{name}]]" for name in participants) if participants else ""
    page_title = f"{title_prefix}-{scene.id}-{slugify(scene.title) or 'log'}".strip("-")
    date_text = str(scene.ic_date)

    header_lines = [
        "{{Log",
        f"| title={scene.title}",
        f"| participants={participants_markup}",
        f"| storyteller=[[{storyteller_name}]]",
        f"| location={scene.location or 'Unknown'}",
        f"| dateandtime={date_text}",
        f"| summary={scene.summary or 'No summary provided.'}",
        "}}",
        "",
    ]

    transcript_lines = []
    for post in scene.posts.select_related("account", "character").all():
        speaker = post.character.db_key if post.character else post.account.username
        cleaned_content = str(post.content).replace("\r", "")
        transcript_lines.extend(
            [
                f"'''{speaker}''' ({post.post_type}):",
                cleaned_content,
                "",
            ]
        )

    category_lines = ["", "[[Category:Logs]]"]
    page_text = "\n".join(header_lines + transcript_lines + category_lines).strip()
    edit_summary = f"Async scene log generated from scene #{scene.id}."

    session = requests.Session()
    timeout_seconds = 15

    try:
        login_token_resp = session.get(
            api_url,
            params={
                "action": "query",
                "meta": "tokens",
                "type": "login",
                "format": "json",
            },
            timeout=timeout_seconds,
        )
        login_token_resp.raise_for_status()
        login_token = login_token_resp.json()["query"]["tokens"]["logintoken"]

        login_resp = session.post(
            api_url,
            data={
                "action": "login",
                "lgname": bot_username,
                "lgpassword": bot_password,
                "lgtoken": login_token,
                "format": "json",
            },
            timeout=timeout_seconds,
        )
        login_resp.raise_for_status()
        login_result = login_resp.json().get("login", {}).get("result")
        if login_result != "Success":
            return False, f"MediaWiki login failed ({login_result})."

        csrf_resp = session.get(
            api_url,
            params={"action": "query", "meta": "tokens", "format": "json"},
            timeout=timeout_seconds,
        )
        csrf_resp.raise_for_status()
        csrf_token = csrf_resp.json()["query"]["tokens"]["csrftoken"]

        edit_resp = session.post(
            api_url,
            data={
                "action": "edit",
                "title": page_title,
                "text": page_text,
                "summary": edit_summary,
                "token": csrf_token,
                "format": "json",
            },
            timeout=timeout_seconds,
        )
        edit_resp.raise_for_status()
        edit_data = edit_resp.json()
        if "error" in edit_data:
            return False, f"MediaWiki edit error: {edit_data['error'].get('info', 'unknown error')}"
        if edit_data.get("edit", {}).get("result") != "Success":
            return False, "MediaWiki edit did not return success."
    except requests.RequestException as err:
        return False, f"MediaWiki request failed: {err}"
    except (KeyError, ValueError, TypeError) as err:
        return False, f"MediaWiki response parse failed: {err}"

    scene.wiki_log_slug = page_title
    scene.is_public_log = True
    scene.save(update_fields=["wiki_log_slug", "is_public_log", "updated_at"])
    return True, page_title


def _validate_choice(value: str, choices: tuple[tuple[str, str], ...], field_name: str):
    """Validate a choice value and raise JSON error payload."""
    valid = {choice[0] for choice in choices}
    if value not in valid:
        return JsonResponse({"error": f"Invalid {field_name}."}, status=400)
    return None


_WEB_COMMAND_PREFIXES = (
    "+xp",
    "+vote",
    "+jobs",
    "+requests",
    "+roll",
    "roll",
    "+tilt",
    "+tilts",
    "+condition",
    "+conditions",
    "+cond",
    "+aspiration",
    "+aspirations",
    "+asp",
    "initiative",
    "init",
)


def _is_allowed_web_command(command: str) -> bool:
    """Allow only explicitly approved command families for web execution."""
    lowered = command.strip().lower()
    return any(lowered == prefix or lowered.startswith(f"{prefix}/") or lowered.startswith(f"{prefix} ") for prefix in _WEB_COMMAND_PREFIXES)


def _execute_web_command(character, command: str) -> list[str]:
    """Execute command as character and capture caller-facing output."""
    output = []
    account = getattr(character, "account", None)

    original_char_msg = character.msg
    original_account_msg = getattr(account, "msg", None) if account else None

    def _capture_message(text=None, **kwargs):
        if text is None:
            return
        cleaned = strip_ansi(str(text))
        if cleaned:
            output.append(cleaned)

    character.msg = _capture_message
    if account and original_account_msg:
        account.msg = _capture_message

    try:
        character.execute_cmd(command)
    finally:
        character.msg = original_char_msg
        if account and original_account_msg:
            account.msg = original_account_msg

    return output


def _is_initiative_command(command: str) -> bool:
    """Check if a command is initiative-related."""
    lowered = command.strip().lower()
    return (
        lowered == "initiative"
        or lowered == "init"
        or lowered.startswith("initiative/")
        or lowered.startswith("init/")
        or lowered.startswith("initiative ")
        or lowered.startswith("init ")
    )


def _get_scene_initiative_state(scene) -> dict:
    """Get normalized initiative state for one scene."""
    raw = scene.initiative_state if isinstance(scene.initiative_state, dict) else {}
    participants = raw.get("participants", {})
    order = raw.get("order", [])
    current_actor_id = raw.get("current_actor_id")
    return {
        "participants": participants if isinstance(participants, dict) else {},
        "order": order if isinstance(order, list) else [],
        "current_actor_id": int(current_actor_id) if str(current_actor_id).isdigit() else None,
    }


def _save_scene_initiative_state(scene, state: dict):
    """Persist initiative state and activity timestamp."""
    scene.initiative_state = state
    scene.last_activity_at = timezone.now()
    scene.save(update_fields=["initiative_state", "last_activity_at", "updated_at"])


def _sort_scene_initiative_order(state: dict):
    """Sort initiative order by score (descending)."""
    participants = state.get("participants", {})
    order = [str(char_id) for char_id in state.get("order", []) if str(char_id) in participants]
    order.sort(key=lambda char_id: int(participants.get(char_id, {}).get("initiative", 0) or 0), reverse=True)
    state["order"] = order
    if order and str(state.get("current_actor_id")) not in order:
        state["current_actor_id"] = int(order[0])
    if not order:
        state["current_actor_id"] = None


def _format_scene_initiative_status_lines(scene, state: dict) -> list[str]:
    """Return readable initiative status for output."""
    order = state.get("order", [])
    if not order:
        return ["No active initiative order in this scene."]

    Character = class_from_module("typeclasses.characters.Character")
    ids = [int(char_id) for char_id in order if str(char_id).isdigit()]
    by_id = {char.id: char for char in Character.objects.filter(id__in=ids)}
    current_actor_id = state.get("current_actor_id")

    lines = ["Initiative Order:"]
    for idx, char_id in enumerate(order, start=1):
        char_int = int(char_id)
        pdata = state["participants"].get(char_id, {})
        name = by_id.get(char_int).key if by_id.get(char_int) else f"Character #{char_int}"
        initiative_value = pdata.get("initiative", 0)
        team = pdata.get("team", "Solo")
        marker = "->" if current_actor_id == char_int else "  "
        lines.append(f"{marker} {idx}. {name} | Team: {team} | Init: {initiative_value}")
    return lines


def _find_scene_character_by_name(scene, name: str):
    """Find a participant character in scene by name."""
    needle = (name or "").strip().lower()
    if not needle:
        return None
    for participant in scene.participants.all():
        if participant.key.lower() == needle:
            return participant
    return None


def _execute_scene_initiative_command(scene, character, account, command: str) -> tuple[list[str], bool]:
    """Run initiative command scoped to one scene."""
    lowered = command.strip().lower()
    state = _get_scene_initiative_state(scene)
    participants = state["participants"]
    order = state["order"]
    char_id = str(character.id)
    should_post = False

    if lowered in {"initiative", "init"}:
        # Status if already in initiative, otherwise roll into this scene only.
        if char_id in order:
            return _format_scene_initiative_status_lines(scene, state), False

        init_attr = int(_as_mapping(getattr(character.db, "stats", {}) or {}).get("advantages", {}).get("initiative", 0) or 0)
        roll = random.randint(1, 10)
        total = roll + init_attr
        existing = participants.get(char_id, {})
        existing["initiative"] = total
        existing.setdefault("team", "Solo")
        participants[char_id] = existing
        if char_id not in order:
            order.append(char_id)
        _sort_scene_initiative_order(state)
        _save_scene_initiative_state(scene, state)
        should_post = True

        lines = [f"Initiative Roll: {character.key} enters at {total} ({roll} + {init_attr})"]
        lines.extend(_format_scene_initiative_status_lines(scene, state))
        return lines, should_post

    if lowered.startswith("init/team ") or lowered.startswith("initiative/team "):
        target_name = command.split(" ", 1)[1].strip() if " " in command else ""
        target = _find_scene_character_by_name(scene, target_name)
        if not target:
            return [f"Character '{target_name}' not found in this scene."], False

        target_id = str(target.id)
        target_data = participants.get(target_id)
        if not target_data:
            return [f"{target.key} is not in initiative order for this scene yet."], False

        target_team = target_data.get("team", "Solo")
        caller_data = participants.get(char_id, {})
        caller_data["team"] = target_team
        participants[char_id] = caller_data
        if char_id not in order:
            init_attr = int(_as_mapping(getattr(character.db, "stats", {}) or {}).get("advantages", {}).get("initiative", 0) or 0)
            roll = random.randint(1, 10)
            caller_data["initiative"] = roll + init_attr
            order.append(char_id)

        _sort_scene_initiative_order(state)
        _save_scene_initiative_state(scene, state)
        should_post = True
        lines = [f"{character.key} joins team {target_team} with {target.key}."]
        lines.extend(_format_scene_initiative_status_lines(scene, state))
        return lines, should_post

    if lowered in {"init/turn", "initiative/turn"}:
        if not order:
            return ["No active initiative order in this scene."], False
        current_actor_id = state.get("current_actor_id")
        is_manager = _can_manage_scene(scene, account)
        if not is_manager and current_actor_id != int(char_id):
            return ["Only the current actor can advance the turn."], False

        current_idx = order.index(str(current_actor_id)) if str(current_actor_id) in order else -1
        next_idx = (current_idx + 1) % len(order)
        state["current_actor_id"] = int(order[next_idx])
        _save_scene_initiative_state(scene, state)
        should_post = True
        lines = ["Turn advanced."]
        lines.extend(_format_scene_initiative_status_lines(scene, state))
        return lines, should_post

    if lowered in {"init/end", "initiative/end"}:
        if not _can_manage_scene(scene, account):
            return ["Only scene managers can end combat."], False
        state = {"participants": {}, "order": [], "current_actor_id": None}
        _save_scene_initiative_state(scene, state)
        should_post = True
        return ["Combat ended for this scene. Initiative order cleared."], should_post

    return ["Unsupported initiative command. Use initiative, init/team <name>, init/turn, or init/end."], False


@login_required
def dashboard(request):
    """Render the async-play dashboard page."""
    return render(request, "asyncplay/dashboard.html")


@login_required
@require_GET
def api_my_characters(request):
    """List characters owned by the authenticated account."""
    data = []
    for char in _owned_characters(request.user):
        template = (getattr(char.db, "stats", {}) or {}).get("other", {}).get("template", "Mortal")
        data.append(
            {
                "id": char.id,
                "name": char.key,
                "template": template,
                "approved": bool(getattr(char.db, "approved", False)),
            }
        )
    return JsonResponse({"characters": data})


@login_required
@require_GET
def api_scene_invite_candidates(request):
    """List approved characters that can be invited to scenes."""
    candidates = []
    for char in _approved_characters():
        owner_name = getattr(getattr(char, "account", None), "username", None)
        candidates.append(
            {
                "id": char.id,
                "name": char.key,
                "owner": owner_name,
                "template": _as_mapping(
                    _as_mapping(getattr(char.db, "stats", {}) or {}).get("other", {})
                ).get("template", "Mortal"),
            }
        )
    return JsonResponse({"candidates": sorted(candidates, key=lambda item: (item["owner"] or "", item["name"]))})


@login_required
@require_GET
def api_character_sheet(request, character_id: int):
    """Return the full sheet payload for one character."""
    Character = class_from_module("typeclasses.characters.Character")
    character = get_object_or_404(Character, id=character_id)

    if not _can_access_character(request.user, character):
        return JsonResponse({"error": "You do not have access to this character."}, status=403)

    payload = build_character_sheet_payload(character)
    payload["sheet_display"] = _build_sheet_display(character)
    return JsonResponse(payload)


@login_required
@require_http_methods(["POST"])
def api_command_execute(request):
    """Run a restricted set of in-game commands from the async web client."""
    body = _parse_json_body(request)
    if body is None:
        return HttpResponseBadRequest("Invalid JSON body.")

    character_id = body.get("character_id")
    if not character_id:
        return JsonResponse({"error": "character_id is required."}, status=400)
    command = (body.get("command") or "").strip()
    if not command:
        return JsonResponse({"error": "command is required."}, status=400)
    if not _is_allowed_web_command(command):
        return JsonResponse({"error": "Command not allowed in async web tools."}, status=400)

    try:
        character = _character_by_id(int(character_id))
    except (TypeError, ValueError):
        return JsonResponse({"error": "character_id must be an integer."}, status=400)
    if not _can_access_character(request.user, character):
        return JsonResponse({"error": "You do not have access to this character."}, status=403)

    scene_id = body.get("scene_id")
    post_to_scene = bool(body.get("post_to_scene"))
    initiative_command = _is_initiative_command(command)
    scene = None
    if scene_id:
        try:
            scene = get_object_or_404(AsyncScene, id=int(scene_id))
        except (TypeError, ValueError):
            return JsonResponse({"error": "scene_id must be an integer."}, status=400)
        if not _can_view_scene(scene, request.user):
            return JsonResponse({"error": "You do not have access to this scene."}, status=403)
        if initiative_command and scene.is_completed:
            return JsonResponse({"error": "Scene is stopped. Restart it before using initiative."}, status=400)

    # Initiative is scene-scoped when scene_id is provided.
    initiative_should_post = False
    if scene and initiative_command:
        lines, initiative_should_post = _execute_scene_initiative_command(scene, character, request.user, command)
    else:
        lines = _execute_web_command(character, command)

    did_post = False
    if post_to_scene and scene:
        if scene.is_completed:
            return JsonResponse({"error": "Scene is stopped. Restart it to post rolls."}, status=400)
        if not _can_post_to_scene(scene, request.user):
            return JsonResponse({"error": "You do not have posting access to this scene."}, status=403)

        lowered = command.lower().strip()
        should_post = initiative_should_post
        post_header = f"Command: {command}"

        if not should_post and (lowered.startswith("+roll") or lowered.startswith("roll")):
            should_post = True
        if initiative_should_post:
            post_header = f"Initiative: {command}"

        if should_post:
            content_lines = [f"Command: {command}"]
            if post_header != f"Command: {command}":
                content_lines = [post_header]
            content_lines.extend(lines or ["(Roll executed with no direct output.)"])
            AsyncScenePost.objects.create(
                scene=scene,
                account=request.user,
                character=character,
                post_type=AsyncScenePost.TYPE_OOC,
                content="\n".join(content_lines).strip(),
            )
            scene.participants.add(character)
            scene.last_activity_at = timezone.now()
            scene.save(update_fields=["last_activity_at", "updated_at"])
            did_post = True

    return JsonResponse({"ok": True, "lines": lines, "command": command, "posted_to_scene": did_post})


@login_required
@require_GET
def api_my_actions(request):
    """Return async actions submitted by this account."""
    actions = AsyncAction.objects.filter(account=request.user).select_related("character")
    payload = [
        {
            "id": action.id,
            "character_id": action.character_id,
            "character_name": action.character.db_key,
            "title": action.title,
            "content": action.content,
            "status": action.status,
            "staff_response": action.staff_response,
            "created_at": action.created_at.isoformat(),
            "updated_at": action.updated_at.isoformat(),
        }
        for action in actions
    ]
    return JsonResponse({"actions": payload})


@login_required
@require_http_methods(["POST"])
def api_submit_action(request):
    """Submit a new async action from the web portal."""
    body = _parse_json_body(request)
    if body is None:
        return HttpResponseBadRequest("Invalid JSON body.")

    character_id = body.get("character_id")
    title = (body.get("title") or "").strip()
    content = (body.get("content") or "").strip()

    if not character_id:
        return JsonResponse({"error": "character_id is required."}, status=400)
    if not title:
        return JsonResponse({"error": "title is required."}, status=400)
    if not content:
        return JsonResponse({"error": "content is required."}, status=400)

    Character = class_from_module("typeclasses.characters.Character")
    character = get_object_or_404(Character, id=character_id)

    if not _can_access_character(request.user, character):
        return JsonResponse({"error": "You do not have access to this character."}, status=403)

    action = AsyncAction.objects.create(
        account=request.user,
        character=character,
        title=title,
        content=content,
    )

    return JsonResponse(
        {
            "ok": True,
            "action": {
                "id": action.id,
                "status": action.status,
            },
        },
        status=201,
    )


@login_required
@require_GET
def api_scene_list(request):
    """List scenes split by public ongoing/completed and personal access."""
    scenes = AsyncScene.objects.prefetch_related("participants").all()
    visible = [scene for scene in scenes if _can_view_scene(scene, request.user)]

    public_ongoing = [
        _serialize_scene(scene, account=request.user)
        for scene in visible
        if scene.privacy == AsyncScene.PRIVACY_OPEN and not scene.is_completed
    ]
    public_completed = [
        _serialize_scene(scene, account=request.user)
        for scene in visible
        if scene.privacy == AsyncScene.PRIVACY_OPEN and scene.is_completed and scene.is_public_log
    ]
    my_scenes = [
        _serialize_scene(scene, account=request.user)
        for scene in visible
        if scene.creator == request.user or _scene_member_characters(scene, request.user)
    ]

    return JsonResponse(
        {
            "public_ongoing": public_ongoing,
            "public_completed": public_completed,
            "my_scenes": my_scenes,
        }
    )


@login_required
@require_GET
def api_scene_detail(request, scene_id: int):
    """Get a single scene with posts."""
    scene = get_object_or_404(
        AsyncScene.objects.prefetch_related("participants", "posts__account", "posts__character"),
        id=scene_id,
    )
    if not _can_view_scene(scene, request.user):
        return JsonResponse({"error": "You do not have access to this scene."}, status=403)
    return JsonResponse({"scene": _serialize_scene(scene, include_posts=True, account=request.user)})


@login_required
@require_http_methods(["POST"])
def api_scene_create(request):
    """Create a new async scene."""
    body = _parse_json_body(request)
    if body is None:
        return HttpResponseBadRequest("Invalid JSON body.")

    title = (body.get("title") or "").strip()
    if not title:
        return JsonResponse({"error": "title is required."}, status=400)

    character_id = body.get("character_id")
    if not character_id:
        return JsonResponse({"error": "character_id is required."}, status=400)

    try:
        character = _character_by_id(int(character_id))
    except (TypeError, ValueError):
        return JsonResponse({"error": "character_id must be an integer."}, status=400)
    if not _can_access_character(request.user, character):
        return JsonResponse({"error": "You do not own this character."}, status=403)

    ic_date_raw = (body.get("ic_date") or "").strip()
    ic_date = timezone.localdate()
    if ic_date_raw:
        try:
            ic_date = timezone.datetime.fromisoformat(ic_date_raw).date()
        except ValueError:
            return JsonResponse({"error": "ic_date must be YYYY-MM-DD."}, status=400)

    scene_type = (body.get("scene_type") or AsyncScene.TYPE_SOCIAL).strip()
    pacing = (body.get("pacing") or AsyncScene.PACING_TRADITIONAL).strip()
    privacy = (body.get("privacy") or AsyncScene.PRIVACY_PRIVATE).strip()

    choice_error = _validate_choice(scene_type, AsyncScene.TYPE_CHOICES, "scene_type")
    if choice_error:
        return choice_error
    choice_error = _validate_choice(pacing, AsyncScene.PACING_CHOICES, "pacing")
    if choice_error:
        return choice_error
    choice_error = _validate_choice(privacy, AsyncScene.PRIVACY_CHOICES, "privacy")
    if choice_error:
        return choice_error

    location = (body.get("location") or "").strip()
    room_id = body.get("room_id")
    if room_id:
        try:
            selected_room_id = int(room_id)
        except (TypeError, ValueError):
            selected_room_id = 0
        room_options = {opt["id"]: opt["label"] for opt in _available_room_locations()}
        location = room_options.get(selected_room_id, location)

    scene = AsyncScene.objects.create(
        creator=request.user,
        title=title,
        notes=(body.get("notes") or "").strip(),
        location=location,
        ic_date=ic_date,
        scene_type=scene_type,
        pacing=pacing,
        privacy=privacy,
        is_completed=bool(body.get("is_completed", False)),
        plot=(body.get("plot") or "").strip(),
        tags=(body.get("tags") or "").strip(),
        summary=(body.get("summary") or "").strip(),
    )
    scene.participants.add(character)

    invite_ids = _parse_int_list(body.get("invite_character_ids"))
    if invite_ids:
        for invited in _approved_characters():
            if invited.id in invite_ids:
                scene.participants.add(invited)

    related_ids = _parse_int_list(body.get("related_scene_ids"))
    if related_ids:
        scene.related_scenes.add(*AsyncScene.objects.filter(id__in=related_ids))

    scene.last_activity_at = timezone.now()
    scene.save(update_fields=["last_activity_at", "updated_at"])

    summary_text = (scene.summary or "").strip()
    if summary_text:
        AsyncScenePost.objects.create(
            scene=scene,
            account=request.user,
            character=character,
            post_type=AsyncScenePost.TYPE_SCENE_SET,
            content=summary_text,
        )
        scene.last_activity_at = timezone.now()
        scene.save(update_fields=["last_activity_at", "updated_at"])

    return JsonResponse({"ok": True, "scene": _serialize_scene(scene, account=request.user)}, status=201)


@login_required
@require_GET
def api_scene_locations(request):
    """List all room locations in hierarchy format."""
    return JsonResponse({"locations": _available_room_locations()})


@login_required
@require_http_methods(["POST"])
def api_scene_join(request, scene_id: int):
    """Join scene as one of your characters."""
    body = _parse_json_body(request)
    if body is None:
        return HttpResponseBadRequest("Invalid JSON body.")

    scene = get_object_or_404(AsyncScene, id=scene_id)
    if scene.is_completed:
        return JsonResponse({"error": "Scene is stopped. Restart it to join."}, status=400)
    if not _can_view_scene(scene, request.user):
        return JsonResponse({"error": "You do not have access to this scene."}, status=403)

    character_id = body.get("character_id")
    if not character_id:
        return JsonResponse({"error": "character_id is required."}, status=400)
    character = _character_by_id(int(character_id))
    if not _can_access_character(request.user, character):
        return JsonResponse({"error": "You do not own this character."}, status=403)

    scene.participants.add(character)
    scene.last_activity_at = timezone.now()
    scene.save(update_fields=["last_activity_at", "updated_at"])
    return JsonResponse({"ok": True})


@login_required
@require_http_methods(["POST"])
def api_scene_update(request, scene_id: int):
    """Update scene metadata (creator/admin)."""
    body = _parse_json_body(request)
    if body is None:
        return HttpResponseBadRequest("Invalid JSON body.")

    scene = get_object_or_404(AsyncScene, id=scene_id)
    if not _can_manage_scene(scene, request.user):
        return JsonResponse({"error": "You do not have permission to edit this scene."}, status=403)

    if "title" in body:
        scene.title = (body.get("title") or "").strip() or scene.title
    if "notes" in body:
        scene.notes = (body.get("notes") or "").strip()
    if "location" in body:
        scene.location = (body.get("location") or "").strip()
    if "plot" in body:
        scene.plot = (body.get("plot") or "").strip()
    if "tags" in body:
        scene.tags = (body.get("tags") or "").strip()
    if "summary" in body:
        return JsonResponse({"error": "Scene set/summary cannot be edited after scene creation."}, status=400)
    if "privacy" in body:
        privacy = (body.get("privacy") or "").strip()
        choice_error = _validate_choice(privacy, AsyncScene.PRIVACY_CHOICES, "privacy")
        if choice_error:
            return choice_error
        scene.privacy = privacy
    if "scene_type" in body:
        scene_type = (body.get("scene_type") or "").strip()
        choice_error = _validate_choice(scene_type, AsyncScene.TYPE_CHOICES, "scene_type")
        if choice_error:
            return choice_error
        scene.scene_type = scene_type
    if "pacing" in body:
        pacing = (body.get("pacing") or "").strip()
        choice_error = _validate_choice(pacing, AsyncScene.PACING_CHOICES, "pacing")
        if choice_error:
            return choice_error
        scene.pacing = pacing

    ic_date_raw = (body.get("ic_date") or "").strip()
    if ic_date_raw:
        try:
            scene.ic_date = timezone.datetime.fromisoformat(ic_date_raw).date()
        except ValueError:
            return JsonResponse({"error": "ic_date must be YYYY-MM-DD."}, status=400)

    scene.last_activity_at = timezone.now()
    scene.save()
    return JsonResponse({"ok": True, "scene": _serialize_scene(scene, account=request.user)})


@login_required
@require_http_methods(["POST"])
def api_scene_invite(request, scene_id: int):
    """Invite an approved character into a scene (creator/admin)."""
    body = _parse_json_body(request)
    if body is None:
        return HttpResponseBadRequest("Invalid JSON body.")

    scene = get_object_or_404(AsyncScene, id=scene_id)
    if not _can_manage_scene(scene, request.user):
        return JsonResponse({"error": "You do not have permission to invite to this scene."}, status=403)

    character_id = body.get("character_id")
    if not character_id:
        return JsonResponse({"error": "character_id is required."}, status=400)

    character = _character_by_id(int(character_id))
    if not getattr(character.db, "approved", False):
        return JsonResponse({"error": "Only approved characters can be invited."}, status=400)
    if scene.participants.filter(id=character.id).exists():
        return JsonResponse({"error": "Character is already in this scene."}, status=400)

    scene.participants.add(character)
    scene.last_activity_at = timezone.now()
    scene.save(update_fields=["last_activity_at", "updated_at"])
    return JsonResponse({"ok": True, "scene": _serialize_scene(scene, account=request.user)})


@login_required
@require_http_methods(["POST"])
def api_scene_complete(request, scene_id: int):
    """Stop/complete scene and optionally publish a public wiki log."""
    body = _parse_json_body(request)
    if body is None:
        return HttpResponseBadRequest("Invalid JSON body.")

    scene = get_object_or_404(AsyncScene, id=scene_id)
    if not _can_manage_scene(scene, request.user):
        return JsonResponse({"error": "You do not have permission to complete this scene."}, status=403)

    if scene.is_completed:
        return JsonResponse({"error": "Scene is already stopped."}, status=400)

    scene.is_completed = True
    if "summary" in body:
        scene.summary = (body.get("summary") or "").strip()
    scene.last_activity_at = timezone.now()
    scene.save(update_fields=["is_completed", "summary", "last_activity_at", "updated_at"])

    publish_log = bool(body.get("publish_public_log", False))
    if publish_log:
        if scene.is_public_log:
            return JsonResponse({"error": "A public log has already been published for this scene."}, status=400)
        scene.privacy = AsyncScene.PRIVACY_OPEN
        scene.save(update_fields=["privacy", "updated_at"])
        ok, message = _publish_scene_log_to_wiki(scene)
        if not ok:
            return JsonResponse(
                {
                    "ok": False,
                    "error": f"Scene completed but wiki log publishing failed: {message}",
                    "scene": _serialize_scene(scene, account=request.user),
                },
                status=500,
            )

    return JsonResponse({"ok": True, "scene": _serialize_scene(scene, account=request.user)})


@login_required
@require_http_methods(["POST"])
def api_scene_reopen(request, scene_id: int):
    """Restart a stopped scene for creator/admin or prior participants."""
    scene = get_object_or_404(AsyncScene, id=scene_id)
    if not scene.is_completed:
        return JsonResponse({"error": "Scene is already active."}, status=400)

    can_reopen = _can_manage_scene(scene, request.user) or bool(_scene_member_characters(scene, request.user))
    if not can_reopen:
        return JsonResponse({"error": "You do not have permission to restart this scene."}, status=403)

    scene.is_completed = False
    scene.last_activity_at = timezone.now()
    scene.save(update_fields=["is_completed", "last_activity_at", "updated_at"])
    return JsonResponse({"ok": True, "scene": _serialize_scene(scene, account=request.user)})


@login_required
@require_http_methods(["POST"])
def api_scene_post(request, scene_id: int):
    """Add a new post to a scene."""
    body = _parse_json_body(request)
    if body is None:
        return HttpResponseBadRequest("Invalid JSON body.")

    scene = get_object_or_404(AsyncScene, id=scene_id)
    if scene.is_completed:
        return JsonResponse({"error": "Scene is stopped. Restart it to post again."}, status=400)
    if not _can_post_to_scene(scene, request.user):
        return JsonResponse({"error": "You do not have posting access to this scene."}, status=403)

    content = (body.get("content") or "").strip()
    if not content:
        return JsonResponse({"error": "content is required."}, status=400)

    character = None
    character_id = body.get("character_id")
    if character_id:
        character = _character_by_id(int(character_id))
        if not _can_access_character(request.user, character):
            return JsonResponse({"error": "You do not own this character."}, status=403)
        scene.participants.add(character)

    post_type = (body.get("post_type") or AsyncScenePost.TYPE_POSE).strip()
    valid_post_types = {choice[0] for choice in AsyncScenePost.TYPE_CHOICES}
    if post_type not in valid_post_types:
        return JsonResponse({"error": "Invalid post_type."}, status=400)
    if post_type == AsyncScenePost.TYPE_SCENE_SET:
        return JsonResponse({"error": "Scene Set can only be created when starting the scene."}, status=400)

    post = AsyncScenePost.objects.create(
        scene=scene,
        account=request.user,
        character=character,
        post_type=post_type,
        content=content,
    )
    scene.last_activity_at = timezone.now()
    scene.save(update_fields=["last_activity_at", "updated_at"])
    return JsonResponse(
        {
            "ok": True,
            "post": {
                "id": post.id,
                "created_at": post.created_at.isoformat(),
            },
        },
        status=201,
    )
