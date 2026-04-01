"""
Utilities for checking Changeling kith data.
"""


def normalize_kith_name(value):
    """Normalize kith input/storage values to snake_case keys."""
    if not value:
        return ""
    return str(value).strip().lower().replace("-", "_").replace(" ", "_")


def get_character_kith(character):
    """
    Return a character's normalized kith key, or an empty string.
    """
    try:
        stats = character.db.stats or {}
        bio = stats.get("bio", {}) or {}
        return normalize_kith_name(bio.get("kith", ""))
    except Exception:
        return ""


def has_kith(character, kith_name):
    """True if character has the provided kith."""
    return get_character_kith(character) == normalize_kith_name(kith_name)
