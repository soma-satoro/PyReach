"""
Sandbox configuration utilities.

These helpers centralize server-config driven sandbox behavior so commands can
share a consistent source of truth.
"""

from evennia.server.models import ServerConfig


SANDBOX_MODE_KEY = "sandbox_mode_enabled"
SANDBOX_AUTO_APPROVE_KEY = "sandbox_auto_approve_on_submit"
SANDBOX_STARTING_XP_KEY = "sandbox_starting_xp"
SANDBOX_UNLIMITED_PURCHASES_KEY = "sandbox_unlimited_xp_purchases"

SANDBOX_XP_GRANTED_MARKER = "sandbox_starting_xp_granted"
SANDBOX_XP_GRANTED_AMOUNT_MARKER = "sandbox_starting_xp_amount_granted"


def is_sandbox_mode_enabled():
    """Return True when sandbox mode is globally enabled."""
    return bool(ServerConfig.objects.conf(SANDBOX_MODE_KEY, default=False))


def should_auto_approve_on_submit():
    """Return True when sandbox submit should auto-approve characters."""
    if not is_sandbox_mode_enabled():
        return False
    # In sandbox mode, auto-approval is enabled by default. Config can override.
    return bool(ServerConfig.objects.conf(SANDBOX_AUTO_APPROVE_KEY, default=True))


def get_sandbox_starting_xp():
    """Return configured sandbox starting XP (non-negative int)."""
    raw_value = ServerConfig.objects.conf(SANDBOX_STARTING_XP_KEY, default=0)
    try:
        value = int(raw_value)
    except (TypeError, ValueError):
        return 0
    return max(0, value)


def has_unlimited_xp_purchases():
    """Return True when sandbox should ignore XP purchase dot caps."""
    if not is_sandbox_mode_enabled():
        return False
    # In sandbox mode, unlimited XP purchase caps are enabled by default.
    # Config can override to disable if needed.
    return bool(ServerConfig.objects.conf(SANDBOX_UNLIMITED_PURCHASES_KEY, default=True))


def grant_sandbox_starting_xp(character):
    """
    Grant configured sandbox starting XP once per character.

    Returns:
        tuple[bool, int]: (granted, amount)
    """
    amount = get_sandbox_starting_xp()
    if amount <= 0:
        return False, 0

    if bool(character.attributes.get(SANDBOX_XP_GRANTED_MARKER, default=False)):
        return False, 0

    exp_handler = character.experience
    exp_handler.add_experience(amount)
    character.attributes.add(SANDBOX_XP_GRANTED_MARKER, True)
    character.attributes.add(SANDBOX_XP_GRANTED_AMOUNT_MARKER, amount)
    return True, amount
