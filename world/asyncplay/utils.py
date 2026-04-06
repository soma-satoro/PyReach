"""Helpers for safe async web payload generation."""

from collections.abc import Mapping
from typing import Any


def to_json_compatible(value: Any) -> Any:
    """Convert nested values into JSON-safe primitives."""
    if isinstance(value, Mapping):
        return {str(key): to_json_compatible(item) for key, item in value.items()}
    if isinstance(value, list):
        return [to_json_compatible(item) for item in value]
    if isinstance(value, tuple):
        return [to_json_compatible(item) for item in value]
    if isinstance(value, set):
        return [to_json_compatible(item) for item in sorted(value, key=str)]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def build_character_sheet_payload(character) -> dict[str, Any]:
    """
    Build a normalized payload for a character sheet web hook.

    This intentionally mirrors how sheet data is stored on the Character
    typeclass (`db.stats`, `db.powers`, `db.pools`) so browser clients can
    consume one stable structure regardless of game template.
    """

    stats = to_json_compatible(getattr(character.db, "stats", {}) or {})
    powers = to_json_compatible(getattr(character.db, "powers", {}) or {})
    pools = to_json_compatible(getattr(character.db, "pools", {}) or {})

    other_stats = stats.get("other", {}) if isinstance(stats, dict) else {}
    bio = stats.get("bio", {}) if isinstance(stats, dict) else {}

    return {
        "character": {
            "id": character.id,
            "name": character.key,
            "template": other_stats.get("template", "Mortal"),
            "approved": bool(getattr(character.db, "approved", False)),
            "description": getattr(character.db, "desc", "") or "",
            "owner": getattr(getattr(character, "account", None), "username", None),
        },
        "sheet": {
            "bio": bio,
            "stats": stats,
            "powers": powers,
            "pools": pools,
        },
    }
