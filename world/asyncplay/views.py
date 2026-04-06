"""Views and API hooks for asynchronous web-based play."""

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_http_methods
from evennia.utils.utils import class_from_module

from .models import AsyncAction
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


def _can_access_character(account, character) -> bool:
    """Enforce owner-or-admin access to character async data."""
    if _is_admin(account):
        return True
    return character.account == account


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
def api_character_sheet(request, character_id: int):
    """Return the full sheet payload for one character."""
    Character = class_from_module("typeclasses.characters.Character")
    character = get_object_or_404(Character, id=character_id)

    if not _can_access_character(request.user, character):
        return JsonResponse({"error": "You do not have access to this character."}, status=403)

    return JsonResponse(build_character_sheet_payload(character))


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
    try:
        body = json.loads(request.body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
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
