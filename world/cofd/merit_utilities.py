"""
Merit management utilities.
Handles merit instances, validation, and setting.

Prerequisite authoring shorthand (validated by Character prerequisite checks):
    stat:value                -> e.g. "resolve:3"
                                 Stat lookup includes attributes, skills,
                                 and advantages (e.g. wyrd, blood_potency,
                                 primal_urge, gnosis, etc.)
    [a:x,b:y]                 -> OR group
    category_skill:value      -> e.g. "social_skill:2"
    category_attribute:value  -> e.g. "mental_attribute:3"
    specialty:value           -> any specialty count
    <skill>_specialty:value   -> e.g. "brawl_specialty:1"
    weapon_specialty:value    -> brawl/firearms/weaponry specialties
    merit_instance:value      -> e.g. "mantle:autumn:3"
    stat:@dots                -> dynamic threshold tied to merit dots
"""


def parse_merit_instance(stat):
    """
    Parse merit name and instance from stat string.
    
    Args:
        stat (str): Stat string (e.g., "unseen_sense:ghosts" or "resources")
        
    Returns:
        tuple: (base_merit_name, instance_name) - instance_name is None if no instance
    """
    if ":" in stat:
        base_merit, instance = stat.split(":", 1)
        return base_merit.strip(), instance.strip()
    return stat, None


def validate_merit(character, merit_obj, dots, caller):
    """
    Validate merit purchase/setting.
    
    Args:
        character: The character object
        merit_obj: The merit object from merits_dict
        dots (int): Number of dots to set
        caller: The caller object (for messages)
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Validate dots
    if dots < merit_obj.min_value or dots > merit_obj.max_value:
        return False, f"{merit_obj.name} must be between {merit_obj.min_value} and {merit_obj.max_value} dots."
    
    # Check prerequisites if they exist
    if merit_obj.prerequisite:
        unmet = character.get_unmet_merit_prerequisites(
            merit_obj.prerequisite, merit_dots=dots
        )
        if unmet:
            return (
                False,
                f"Prerequisites not met for {merit_obj.name}: "
                f"{', '.join(unmet)}"
            )
    
    return True, None


def set_merit(character, merit_key, merit_obj, dots, caller):
    """
    Set a merit value with validation and proper storage.
    
    Args:
        character: The character object
        merit_key (str): Full merit key including instance if present (e.g., "unseen_sense:ghosts")
        merit_obj: The merit object from merits_dict
        dots (int): Number of dots to set
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    # Validate merit
    is_valid, error_msg = validate_merit(character, merit_obj, dots, caller)
    if not is_valid:
        return False, error_msg
    
    # Parse instance if present
    base_merit_name, instance_name = parse_merit_instance(merit_key)
    
    # Ensure merits category exists
    if "merits" not in character.db.stats:
        character.db.stats["merits"] = {}
    
    # Store merit data with full key (including instance if present)
    character.db.stats["merits"][merit_key] = {
        "dots": dots,
        "max_dots": merit_obj.max_value,
        "merit_type": merit_obj.merit_type,
        "base_merit": base_merit_name
    }
    
    # If this is an instanced merit, also store the instance name
    if instance_name:
        character.db.stats["merits"][merit_key]["instance"] = instance_name
    
    # Format success message
    merit_display = merit_obj.name
    if instance_name:
        merit_display += f" ({instance_name.replace('_', ' ').title()})"
    
    message = f"Set {character.name}'s {merit_display} merit to {dots} dots."
    
    # Recalculate derived stats in case merit affects them
    if hasattr(character, 'calculate_derived_stats'):
        character.calculate_derived_stats()
    
    return True, message


def check_merit_approved_status(character, merit_key, caller):
    """
    Check if a merit can be modified based on character approval status.
    
    Args:
        character: The character object
        merit_key (str): The merit key (may include instance)
        caller: The caller object
        
    Returns:
        tuple: (can_modify, error_message)
    """
    # Check if character is approved and not an NPC
    is_npc = hasattr(character, 'db') and character.db.is_npc
    
    if character.db.approved and not is_npc:
        error_msg = "Character is approved. Merits must be purchased with experience points."
        if ":" in merit_key:
            error_msg += f"\nUse '+xp/buy {merit_key}=[dots]' to purchase merits with experience points."
        else:
            error_msg += f"\nUse '+xp/buy {merit_key}=[dots]' to purchase merits with experience points."
        
        # Parse base merit name
        base_merit, _ = parse_merit_instance(merit_key)
        error_msg += f"\nUse '+xp/info {base_merit}' to see merit details and prerequisites."
        
        return False, error_msg
    
    return True, None

