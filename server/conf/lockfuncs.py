"""

Lockfuncs

Lock functions are functions available when defining lock strings,
which in turn limits access to various game systems.

All functions defined globally in this module are assumed to be
available for use in lockstrings to determine access. See the
Evennia documentation for more info on locks.

A lock function is always called with two arguments, accessing_obj and
accessed_obj, followed by any number of arguments. All possible
arguments should be handled with *args, **kwargs. The lock function
should handle all eventual tracebacks by logging the error and
returning False.

Lock functions in this module extend (and will overload same-named)
lock functions from evennia.locks.lockfuncs.

"""

from evennia.utils import logger
from world.cofd.models import Group, GroupMembership
from typeclasses.groups import get_group_by_id
from world.utils.permission_utils import check_staff_permission

def group_member(accessing_obj, accessed_obj, *args, **kwargs):
    """
    Lock function to check if accessing_obj is a member of a specific group.
    
    This function is used in group channel locks to restrict access to group members.
    Usage in locks: "group_member(group_id)"
    
    Args:
        accessing_obj: The object trying to access (usually a Character)
        accessed_obj: The object being accessed (usually a Channel)
        *args: Should contain the group_id as the first argument
        
    Returns:
        bool: True if accessing_obj is a member of the specified group
    """
    if not args:
        return False
    
    try:
        group_id = int(args[0])
    except (ValueError, IndexError):
        return False
    
    # Get the group by ID
    group = get_group_by_id(group_id)
    if not group:
        return False
    
    # Check if the accessing object is a member
    return group.is_member(accessing_obj)


def _normalize_id(value):
    """
    Normalize values for robust lock comparisons.
    """
    return str(value or "").strip().lower().replace("-", "_").replace(" ", "_")


def _normalize_template(value):
    """
    Normalize template/group names used by visibility locks.
    """
    normalized = _normalize_id(value)
    alias_map = {
        "sin_eater": "geist",
        "sin_eaters": "geist",
        "sineater": "geist",
        "sineaters": "geist",
        "hunters": "hunter",
        "mummies": "mummy",
        "mortalplus": "mortal_plus",
        "mortal_plus": "mortal_plus",
        "mortal+": "mortal_plus",
        "promixus": "proximus",
        "demonblooded": "demon_blooded",
    }
    return alias_map.get(normalized, normalized)


ASSOCIATED_MORTALPLUS_BY_TEMPLATE = {
    "changeling": {"fae_touched"},
    "werewolf": {"wolf_blooded"},
    "vampire": {"ghoul", "dhampir"},
    "mage": {"proximus", "sleepwalker"},
    "demon": {"stigmatic", "demon_blooded"},
    "mummy": {"immortal"},
}


def _get_character(accessing_obj):
    """
    Resolve the traversing object to a Character when possible.
    """
    if not accessing_obj:
        return None

    # Most in-game traversals come from Character objects.
    if getattr(accessing_obj, "has_account", False):
        return accessing_obj

    # Account callers may be routed here in edge cases.
    if hasattr(accessing_obj, "sessions") and hasattr(accessing_obj, "get_puppet"):
        sessions = list(accessing_obj.sessions.all())
        if sessions:
            try:
                return accessing_obj.get_puppet(sessions[0])
            except Exception:
                return None

    return None


def _compare_skill(actual, operator, required):
    if operator == ">=":
        return actual >= required
    if operator == "<=":
        return actual <= required
    if operator == ">":
        return actual > required
    if operator == "<":
        return actual < required
    if operator in ("=", "=="):
        return actual == required
    return False


def _get_merit_dots(stats, merit_name):
    """
    Robust merit dot lookup from stats['merits'].
    """
    merits = (stats or {}).get("merits", {}) or {}
    key = _normalize_id(merit_name)
    merit_data = merits.get(key, 0)
    if isinstance(merit_data, dict):
        return int(merit_data.get("dots", 0) or 0)
    try:
        return int(merit_data or 0)
    except (TypeError, ValueError):
        return 0


def entrycheck(accessing_obj, accessed_obj, *args, **kwargs):
    """
    Evaluate dynamic room-entry requirements stored on an Exit.

    Intended usage in lockstrings:
      traverse:entrycheck()
    """
    try:
        char = _get_character(accessing_obj)
        if not char:
            return False

        # Staff always bypass entry restrictions.
        if check_staff_permission(char):
            return True

        requirements = getattr(accessed_obj.db, "room_entry_requirements", None) or {}
        if not requirements:
            return True

        # Hard lock against non-staff characters.
        if bool(requirements.get("staff_only", False)):
            return False

        stats = getattr(char.db, "stats", None) or {}
        bio = stats.get("bio", {}) or {}
        other = stats.get("other", {}) or {}
        skills = stats.get("skills", {}) or {}
        attributes = stats.get("attributes", {}) or {}

        # Template checks (e.g. Mage, Changeling, Werewolf).
        allowed_templates = {_normalize_id(t) for t in requirements.get("templates", []) if str(t).strip()}
        if allowed_templates:
            template = _normalize_id(other.get("template", ""))
            if template not in allowed_templates:
                return False

        # Mortal+ subtype checks (e.g. fae_touched).
        allowed_mortalplus = {
            _normalize_id(t) for t in requirements.get("mortalplus", []) if str(t).strip()
        }
        if allowed_mortalplus:
            template = _normalize_id(other.get("template", ""))
            template_type = _normalize_id(bio.get("template_type", ""))
            if template not in {"mortal+", "mortal_plus"} or template_type not in allowed_mortalplus:
                return False

        # Legacy skill checks (supports >=, <=, >, <, =).
        for req in requirements.get("skills", []) or []:
            skill_name = _normalize_id(req.get("name", ""))
            # Skill requirements are minimum-threshold by default.
            operator = str(req.get("op", ">=")).strip() or ">="
            required = int(req.get("value", 0))
            actual = int(skills.get(skill_name, 0) or 0)
            if not _compare_skill(actual, operator, required):
                return False

        # Unified stat checks (attributes or skills): streetwise:3, presence:4, etc.
        for req in requirements.get("stats", []) or []:
            stat_name = _normalize_id(req.get("name", ""))
            operator = str(req.get("op", ">=")).strip() or ">="
            required = int(req.get("value", 0))
            if stat_name in attributes:
                actual = int(attributes.get(stat_name, 0) or 0)
            else:
                actual = int(skills.get(stat_name, 0) or 0)
            if not _compare_skill(actual, operator, required):
                return False

        # Bio/identity checks (court, seeming, kith, tribe, auspice, clan, order, path, etc).
        bio_reqs = requirements.get("bio", {}) or {}
        for field, allowed_values in bio_reqs.items():
            allowed = {_normalize_id(v) for v in (allowed_values or []) if str(v).strip()}
            if not allowed:
                continue
            current = _normalize_id(bio.get(field, ""))
            if current not in allowed:
                return False

        return True
    except Exception as err:
        logger.log_err(f"entrycheck lockfunc error: {err}")
        return False


def exitviewcheck(accessing_obj, accessed_obj, *args, **kwargs):
    """
    Determine if a hidden exit should be visible to the accessor.

    Intended usage in lockstrings:
      view:exitviewcheck()
    """
    try:
        char = _get_character(accessing_obj)
        if not char:
            return False

        if check_staff_permission(char):
            return True

        if not bool(getattr(accessed_obj.db, "exit_hidden", False)):
            return True

        requirements = getattr(accessed_obj.db, "exit_view_requirements", None) or {}
        allowed_templates = {
            _normalize_template(t)
            for t in (
                requirements.get("templates")
                or getattr(accessed_obj.db, "exit_view_templates", None)
                or []
            )
            if str(t).strip()
        }
        allowed_mortalplus = {
            _normalize_template(t)
            for t in (requirements.get("mortalplus", []) or [])
            if str(t).strip()
        }
        stat_requirements = requirements.get("stats", []) or []
        merit_requirements = requirements.get("merits", []) or []

        if not (allowed_templates or allowed_mortalplus or stat_requirements or merit_requirements):
            return False

        stats = getattr(char.db, "stats", None) or {}
        bio = stats.get("bio", {}) or {}
        other = stats.get("other", {}) or {}
        skills = stats.get("skills", {}) or {}
        attributes = stats.get("attributes", {}) or {}
        template = _normalize_template(other.get("template", ""))
        template_type = _normalize_template(bio.get("template_type", ""))

        # Template visibility, including associated Mortal+ subtypes.
        if allowed_templates:
            template_ok = template in allowed_templates
            if not template_ok and template in {"mortal_plus"}:
                for major_template in allowed_templates:
                    associated = ASSOCIATED_MORTALPLUS_BY_TEMPLATE.get(major_template, set())
                    if template_type in associated:
                        template_ok = True
                        break
            if not template_ok:
                return False

        # Direct Mortal+ subtype visibility.
        if allowed_mortalplus:
            if template != "mortal_plus" or template_type not in allowed_mortalplus:
                return False

        # Stat visibility requirements (streetwise:3, presence:4, etc).
        for req in stat_requirements:
            stat_name = _normalize_id(req.get("name", ""))
            operator = str(req.get("op", ">=")).strip() or ">="
            required = int(req.get("value", 0))
            if stat_name in attributes:
                actual = int(attributes.get(stat_name, 0) or 0)
            else:
                actual = int(skills.get(stat_name, 0) or 0)
            if not _compare_skill(actual, operator, required):
                return False

        # Merit visibility requirements (merit:status=2 etc).
        for req in merit_requirements:
            merit_name = _normalize_id(req.get("name", ""))
            operator = str(req.get("op", ">=")).strip() or ">="
            required = int(req.get("value", 1))
            actual = _get_merit_dots(stats, merit_name)
            if not _compare_skill(actual, operator, required):
                return False

        return True
    except Exception as err:
        logger.log_err(f"exitviewcheck lockfunc error: {err}")
        return False


# def myfalse(accessing_obj, accessed_obj, *args, **kwargs):
#    """
#    called in lockstring with myfalse().
#    A simple logger that always returns false. Prints to stdout
#    for simplicity, should use utils.logger for real operation.
#    """
#    print "%s tried to access %s. Access denied." % (accessing_obj, accessed_obj)
#    return False
