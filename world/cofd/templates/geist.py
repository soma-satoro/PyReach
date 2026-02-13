"""
Geist: The Sin-Eaters Template Definition for Chronicles of Darkness.
Sin-Eaters are those who have died and returned, bound to powerful ghosts called geists.
"""

from . import register_template, get_template_definition
from world.cofd.powers.geist_powers import (
    GEIST_BURDENS, GEIST_KREWE_TYPES,
    GEIST_PRIMARY_POWERS, GEIST_SECONDARY_POWERS, GEIST_ALL_POWERS,
    GEIST_HAUNTS, GEIST_KEYS, GEIST_CEREMONIES,
    GEIST_CRISIS_TRIGGERS, GEIST_REMEMBRANCE_SKILLS, GEIST_REMEMBRANCE_MERITS,
    ALL_HAUNTS, GEIST_KEY_DETAILS
)


# Geist template definition
GEIST_TEMPLATE = {
    "name": "geist",
    "display_name": "Geist",
    "description": "Sin-Eaters are those who have died and returned to life, bound to powerful ghosts called geists who saved them from true death.",
    "bio_fields": ["root", "bloom",  "burden", "geist_name", "krewe"],
    "integrity_name": "Synergy",
    "starting_integrity": 7,
    "supernatural_power_stat": "psyche",
    "starting_power_stat": 1,
    "resource_pool": "plasm",
    "power_systems": GEIST_ALL_POWERS,
    "anchors": ["root", "bloom"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "geist"],
    "field_validations": {
        "burden": {
            "valid_values": GEIST_BURDENS
        },
        "krewe": {
            "valid_values": GEIST_KREWE_TYPES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Geist: The Sin-Eaters",
    "notes": "Enhanced Geist template with Psyche, Manifestations, Keys, and Plasm pool",
    
    # Geist-specific secondary character sheet configuration
    "geist_config": {
        "rank": 3,
        "size": 5,
        "base_attributes": {
            "power": 1,
            "finesse": 1, 
            "resistance": 1
        },
        "attribute_dots_to_assign": 12,
        "max_attribute": 9,
        "crisis_triggers": GEIST_CRISIS_TRIGGERS,
        "remembrance_skills": GEIST_REMEMBRANCE_SKILLS,
        "remembrance_merits": GEIST_REMEMBRANCE_MERITS,
        "remembrance_max_dots": 3,
        "innate_keys": GEIST_KEYS,
        "bio_fields": ["concept", "remembrance_description", "virtue", "vice", "crisis_trigger", "ban", "bane", "innate_key"]
    }
}

# Register the template
register_template(GEIST_TEMPLATE)


# Sheet Rendering Functions
def render_geist_sheet(character, caller, force_ascii=False):
    """
    Render the Geist character sheet for a Sin-Eater.
    
    Args:
        character: The character object with geist_stats
        caller: The caller (for messaging)
        force_ascii: If True, use ASCII dots instead of Unicode
        
    Returns:
        list: Lines of formatted output for the geist sheet
    """
    from evennia.utils import ansi
    
    # Check if geist stats exist
    if not hasattr(character.db, 'geist_stats') or not character.db.geist_stats:
        return None  # Signal that no geist sheet exists
    
    geist_stats = character.db.geist_stats
    
    # Determine dot characters
    if force_ascii:
        filled_char, empty_char = "*", "-"
    else:
        filled_char, empty_char = "●", "○"
    
    def format_dots(value, max_value):
        """Format dots for display"""
        filled = filled_char * value
        empty = empty_char * (max_value - value)
        return filled + empty
    
    from world.utils.formatting import sheet_section_header, footer

    def format_section_header(section_name):
        return sheet_section_header(section_name)

    # Build the geist sheet display (theme colors for borders)
    output = []
    output.append(footer(78, char="="))
    geist_concept = geist_stats.get("bio", {}).get("concept", f"{character.name}'s Geist")
    output.append(f"|y{geist_concept.center(78)}|n")
    output.append(f"|y{'GEIST CHARACTER SHEET'.center(78)}|n")
    output.append(footer(78, char="="))
    
    # Bio Section
    output.append(format_section_header("|wBIO|n"))
    
    bio = geist_stats.get("bio", {})
    other = geist_stats.get("other", {})
    
    # Bio data with defaults
    concept = bio.get("concept", "<not set>")
    virtue = bio.get("virtue", "<not set>")
    vice = bio.get("vice", "<not set>")
    crisis_trigger = bio.get("crisis_trigger", "<not set>")
    ban = bio.get("ban", "<not set>")
    bane = bio.get("bane", "<not set>")
    innate_key = bio.get("innate_key", "<not set>")
    rank = other.get("rank", 3)
    
    # Remembrance section
    remembrance = geist_stats.get("remembrance", {})
    remembrance_desc = bio.get("remembrance_description", "<not set>")
    remembrance_trait = remembrance.get("trait", "<not set>")
    remembrance_dots = remembrance.get("dots", 0)
    remembrance_type = remembrance.get("trait_type", "")
    
    if remembrance_trait != "<not set>":
        # Show trait even if dots aren't set
        if remembrance_dots > 0:
            trait_display = f"{remembrance_trait.replace('_', ' ').title()} ({remembrance_type}) {format_dots(remembrance_dots, 3)}"
        else:
            trait_display = f"{remembrance_trait.replace('_', ' ').title()} ({remembrance_type})"
    else:
        trait_display = "<not set>"
    
    # Create bio items list for display
    short_bio_items = [
        ("Concept", concept),
        ("Rank", f"{rank}"),
        ("Virtue", virtue),
        ("Vice", vice),
        ("Crisis Trigger", crisis_trigger.title() if crisis_trigger != "<not set>" else crisis_trigger),
        ("Bane", bane),
        ("Innate Key", innate_key.title() if innate_key != "<not set>" else innate_key),
        ("Trait", trait_display)
    ]

    # long fields that need their own lines
    long_bio_items = [
        ("Ban", ban),
        ("Remembrance", remembrance_desc)
    ]
    
    # Display short bio items in two-column format
    for i in range(0, len(short_bio_items), 2):
        left_label, left_value = short_bio_items[i]
        left_text = f"{left_label:<15}: {left_value}"
        
        if i + 1 < len(short_bio_items):
            right_label, right_value = short_bio_items[i + 1]
            # Use less padding for right column labels to prevent overflow
            right_text = f"{right_label:<12}: {right_value}"
        else:
            right_text = ""
        
        left_formatted = left_text.ljust(39)
        output.append(f"{left_formatted} {right_text}")
    
    # Add newline before long bio items
    output.append("")
    
    # Display long bio items on their own lines
    for label, value in long_bio_items:
        if value != "<not set>":
            output.append(f"{label:<15}: {value}")

    
    # Geist Attributes (simplified - Power, Finesse, Resistance)
    attrs = geist_stats.get("attributes", {"power": 1, "finesse": 1, "resistance": 1})
    if attrs:
        output.append(format_section_header("|wATTRIBUTES|n"))
        
        # Format geist attributes
        power_val = attrs.get("power", 1)
        finesse_val = attrs.get("finesse", 1)
        resistance_val = attrs.get("resistance", 1)
        
        power_dots = format_dots(power_val, 9)
        finesse_dots = format_dots(finesse_val, 9)
        resistance_dots = format_dots(resistance_val, 9)
        
        output.append(f"Power          {power_dots} ({power_val})")
        output.append(f"Finesse        {finesse_dots} ({finesse_val})")
        output.append(f"Resistance     {resistance_dots} ({resistance_val})")
    
    # Keys Section
    keys = geist_stats.get("keys", {})
    output.append(format_section_header("|wKEYS|n"))
    
    if keys:
        key_list = []
        for key_name, has_key in keys.items():
            if has_key:
                key_lookup = key_name  # Keep as stored (with spaces)
                key_details = GEIST_KEY_DETAILS.get(key_lookup, {})
                full_name = key_details.get("full_name", key_name.replace("_", " ").title())
                unlock_attr = key_details.get("attribute", "")
                
                key_display = f"|c{full_name}|n"
                if unlock_attr:
                    key_display += f" (Unlock: {unlock_attr})"
                key_list.append(key_display)
        
        if key_list:
            for i, key_display in enumerate(key_list):
                output.append(f"  {key_display}")
                
                clean_key_name = key_display.split(" (")[0]
                # Remove color codes from the key name
                clean_key_name = clean_key_name.replace("|c", "").replace("|n", "").lower()
                for key_code, details in GEIST_KEY_DETAILS.items():
                    if details["full_name"].lower() == clean_key_name:
                        output.append(f"    |cDescription:|n {details['description']}")
                        output.append(f"    |rDoom:|n {details['doom']}")
                        output.append("")
                        break
        else:
            output.append("  No keys unlocked yet.")
    else:
        output.append("  No keys unlocked yet.")
    
    # Derived Stats for Geist
    advantages = geist_stats.get("advantages", {})
    output.append(format_section_header("|wADVANTAGES|n"))
    
    # Calculate derived stats if not already calculated
    if not advantages:
        defense = min(attrs.get("power", 1), attrs.get("finesse", 1))
        initiative = attrs.get("finesse", 1) + attrs.get("resistance", 1)
        speed = attrs.get("power", 1) + attrs.get("finesse", 1) + 5
        size = other.get("size", 5)
    else:
        defense = advantages.get("defense", 0)
        initiative = advantages.get("initiative", 0) 
        speed = advantages.get("speed", 0)
        size = other.get("size", 5)
    
    geist_advantages = [
        ("Defense", defense),
        ("Size", size),
        ("Initiative", initiative),
        ("Speed", speed)
    ]
    
    # Display advantages in rows of 2 columns
    for i in range(0, len(geist_advantages), 2):
        row_parts = []
        for j in range(2):
            if i + j < len(geist_advantages):
                name, value = geist_advantages[i + j]
                part = f"{name:<16} : {value}"
                row_parts.append(part.ljust(39))
            else:
                row_parts.append(" " * 39)
        output.append("".join(row_parts))
    output.append(footer(78, char="="))
    
    # Add encoding info to bottom if ASCII mode is being used
    if force_ascii:
        output.append("|g(ASCII mode active - use +sheet/geist without /ascii for Unicode)|n")
    
    return output


# Power list helper functions
def get_primary_powers():
    """Get list of primary geist powers (haunts rated 1-5)."""
    return GEIST_PRIMARY_POWERS.copy()


def get_secondary_powers():
    """Get list of secondary geist powers (keys and ceremonies - individual abilities)."""
    return GEIST_SECONDARY_POWERS.copy()


def get_all_powers():
    """Get all geist powers for validation."""
    return GEIST_ALL_POWERS.copy()


# Geist Stat Management Utilities
def initialize_geist_stats(character):
    """
    Initialize the geist stats structure for a Sin-Eater.
    
    Args:
        character: The character object
    """
    if not hasattr(character.db, 'geist_stats') or not character.db.geist_stats:
        character.db.geist_stats = {
            "attributes": {"power": 1, "finesse": 1, "resistance": 1},
            "bio": {},
            "remembrance": {},
            "keys": {},
            "haunts": {},
            "advantages": {},
            "other": {"rank": 3, "size": 5}
        }


def set_geist_stat_value(character, stat, value, caller):
    """
    Set a geist stat value with validation.
    
    Args:
        character: The character object
        stat: The stat name to set
        value: The value to set (string or int)
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    # Initialize geist_stats if needed
    initialize_geist_stats(character)
    
    geist_stats = character.db.geist_stats
    
    # Get template config for validation
    template_def = get_template_definition("geist")
    geist_config = template_def.get("geist_config", {}) if template_def else {}
    
    # Try to convert value to int for numeric stats
    original_value = value
    try:
        value = int(value)
    except ValueError:
        # Keep as string for non-numeric stats
        pass
    
    # Handle different stat categories
    if stat in ["power", "finesse", "resistance"]:
        # Geist attributes
        if not isinstance(value, int):
            return False, "Geist attributes must be numbers."
        
        max_attr = geist_config.get("max_attribute", 9)
        if not 1 <= value <= max_attr:
            return False, f"Geist attributes must be between 1 and {max_attr}."
        
        # Check total attribute dots (base 3 + 12 to assign = 15 total)
        current_total = sum(geist_stats["attributes"].values())
        current_value = geist_stats["attributes"].get(stat, 1)
        new_total = current_total - current_value + value
        max_total = 3 + geist_config.get("attribute_dots_to_assign", 12)
        
        if new_total > max_total:
            error_msg = f"Cannot set {stat} to {value}. Total attribute dots would be {new_total}, maximum is {max_total}.\n"
            error_msg += f"Current totals: Power {geist_stats['attributes']['power']}, Finesse {geist_stats['attributes']['finesse']}, Resistance {geist_stats['attributes']['resistance']}"
            return False, error_msg
        
        geist_stats["attributes"][stat] = value
        return True, f"Set geist's {stat} to {value}."
    
    elif stat in ["concept", "remembrance_description", "virtue", "vice", "crisis_trigger", "ban", "bane"]:
        # Bio fields (string values)
        if isinstance(value, int):
            value = original_value  # Use original string value
        
        if len(str(value)) > 100:
            return False, "Geist bio fields cannot exceed 100 characters."
        
        # Validate specific fields
        if stat == "virtue":
            geist_stats["bio"][stat] = str(value).title()
            return True, f"Set geist's virtue to {value}."
        elif stat == "vice":
            geist_stats["bio"][stat] = str(value).title()
            return True, f"Set geist's vice to {value}."
        elif stat == "crisis_trigger":
            valid_triggers = geist_config.get("crisis_triggers", [])
            if valid_triggers and value.lower() not in valid_triggers:
                return False, f"Invalid crisis trigger. Valid options: {', '.join(valid_triggers)}"
            geist_stats["bio"][stat] = str(value).lower()
            return True, f"Set geist's crisis trigger to {value}."
        else:
            geist_stats["bio"][stat] = str(value)
            return True, f"Set geist's {stat.replace('_', ' ')} to {value}."
    
    elif stat == "innate_key":
        # Innate key selection
        valid_keys = geist_config.get("innate_keys", [])
        if valid_keys and value.lower() not in valid_keys:
            return False, f"Invalid innate key. Valid options: {', '.join(valid_keys)}"
        geist_stats["bio"]["innate_key"] = str(value).lower()
        return True, f"Set geist's innate key to {value}."
    
    elif stat == "remembrance_trait":
        # Remembrance trait (skill or merit)
        if not isinstance(value, str):
            return False, "Remembrance trait must be a skill or merit name."
            
        value_lower = value.lower().replace(" ", "_")
        valid_skills = geist_config.get("remembrance_skills", [])
        valid_merits = geist_config.get("remembrance_merits", [])
        
        if value_lower not in valid_skills + valid_merits:
            error_msg = f"Invalid remembrance trait. Must be a valid skill or merit (≤3 dots).\n"
            error_msg += f"Valid skills: {', '.join(valid_skills)}\n"
            error_msg += f"Valid merits: {', '.join(valid_merits)}"
            return False, error_msg
        
        geist_stats["remembrance"]["trait"] = value_lower
        geist_stats["remembrance"]["trait_type"] = "skill" if value_lower in valid_skills else "merit"
        return True, f"Set geist's remembrance trait to {value}."
    
    elif stat == "remembrance_dots":
        # Remembrance trait dots
        if not isinstance(value, int):
            return False, "Remembrance dots must be a number."
            
        max_dots = geist_config.get("remembrance_max_dots", 3)
        if not 1 <= value <= max_dots:
            return False, f"Remembrance trait dots must be between 1 and {max_dots}."
        
        geist_stats["remembrance"]["dots"] = value
        return True, f"Set geist's remembrance dots to {value}."
    
    else:
        # Unknown stat
        error_msg = f"Unknown geist stat: {stat}\n"
        error_msg += "Valid geist stats:\n"
        error_msg += "  Attributes: power, finesse, resistance\n"
        error_msg += "  Bio: concept, remembrance_description, virtue, vice, crisis_trigger, ban, bane, innate_key\n"
        error_msg += "  Remembrance: remembrance_trait, remembrance_dots\n"
        error_msg += "  Note: For keys, use the semantic syntax: +stat key=beasts\n"
        error_msg += "  Note: For haunts, use regular numeric syntax: +stat boneyard=3"
        return False, error_msg


def calculate_geist_derived_stats(character, caller):
    """
    Calculate derived stats for a geist.
    
    Args:
        character: The character object
        caller: The caller object (for messages)
        
    Returns:
        dict: Calculated advantages
    """
    if not hasattr(character.db, 'geist_stats') or not character.db.geist_stats:
        return {}
    
    geist_stats = character.db.geist_stats
    attrs = geist_stats.get("attributes", {})
    
    # Calculate derived stats per Geist rules
    defense = min(attrs.get("power", 1), attrs.get("finesse", 1))
    initiative = attrs.get("finesse", 1) + attrs.get("resistance", 1)
    speed = attrs.get("power", 1) + attrs.get("finesse", 1) + 5
    size = geist_stats.get("other", {}).get("size", 5)
    
    # Store derived stats
    geist_stats["advantages"] = {
        "defense": defense,
        "initiative": initiative,
        "speed": speed
    }
    
    if caller:
        caller.msg(f"Recalculated geist derived stats: Defense {defense}, Initiative {initiative}, Speed {speed}")
    
    return geist_stats["advantages"]

