"""
Health system utilities for Chronicles of Darkness.
Shared functions for managing health tracks, damage, and healing.
"""

def get_health_track(character):
    """
    Get health track as an array where index 0 is leftmost (most severe).
    Returns array of damage types or None for empty boxes.
    """
    advantages = character.db.stats.get("advantages", {})
    health_max = advantages.get("health", 7)
    health_damage = character.db.health_damage or {}
    
    # Convert the old dictionary format to array format
    track = [None] * health_max
    for position, damage_type in health_damage.items():
        if 1 <= position <= health_max:
            track[position - 1] = damage_type  # Convert to 0-based indexing
    
    # Compact the track to ensure proper left-justified display
    compact_track(track)
    
    return track

def compact_track(track):
    """
    Compact the health track by moving all damage to the left with no gaps.
    Maintains severity order: aggravated, then lethal, then bashing.
    """
    # Collect all damage in severity order
    aggravated_count = sum(1 for d in track if d == "aggravated")
    lethal_count = sum(1 for d in track if d == "lethal")
    bashing_count = sum(1 for d in track if d == "bashing")
    
    # Clear the track
    for i in range(len(track)):
        track[i] = None
    
    # Place damage back in order: aggravated first, then lethal, then bashing
    pos = 0
    
    # Place aggravated damage
    for i in range(aggravated_count):
        track[pos] = "aggravated"
        pos += 1
    
    # Place lethal damage
    for i in range(lethal_count):
        track[pos] = "lethal"
        pos += 1
    
    # Place bashing damage
    for i in range(bashing_count):
        track[pos] = "bashing"
        pos += 1

def set_health_track(character, track):
    """
    Set health track from array format back to dictionary format.
    """
    health_damage = {}
    for i, damage_type in enumerate(track):
        if damage_type:
            health_damage[i + 1] = damage_type  # Convert to 1-based indexing
    
    character.db.health_damage = health_damage

def get_health_display(character, force_ascii=False):
    """Get a visual representation of current health"""
    advantages = character.db.stats.get("advantages", {})
    health_max = advantages.get("health", 7)
    health_track = get_health_track(character)
    
    # Save the compacted track back to ensure consistency
    set_health_track(character, health_track)
    
    # Create health boxes
    health_boxes = []
    for i in range(health_max):
        damage_type = health_track[i]
        if damage_type == "bashing":
            health_boxes.append("[|c/|n]")  # Cyan for bashing
        elif damage_type == "lethal":
            health_boxes.append("[|rX|n]")  # Red for lethal
        elif damage_type == "aggravated":
            health_boxes.append("[|R*|n]")  # Bright red for aggravated
        else:
            health_boxes.append("[ ]")
    
    return "  " + "".join(health_boxes)

def parse_damage_type(type_str):
    """Parse damage type from string"""
    if not type_str:
        return "bashing"
    
    type_str = type_str.lower()
    if type_str in ["bashing", "bash", "b"]:
        return "bashing"
    elif type_str in ["lethal", "l"]:
        return "lethal"
    elif type_str in ["aggravated", "agg", "a"]:
        return "aggravated"
    else:
        return "bashing"  # Default

def damage_severity(damage_type):
    """Return numeric severity for damage comparison"""
    severity = {"bashing": 1, "lethal": 2, "aggravated": 3}
    return severity.get(damage_type, 1)

def calculate_wound_penalty(character):
    """
    Calculate wound penalties based on Chronicles of Darkness rules.
    
    Wound Penalties:
    - If damage reaches the third-to-last health box: -1 penalty
    - If damage reaches the second-to-last health box: -2 penalty  
    - If damage reaches the last health box: -3 penalty
    
    Iron Stamina merit reduces wound penalties by 1 per dot.
    
    Args:
        character: The character object to calculate wound penalties for
        
    Returns:
        int: The wound penalty (0, -1, -2, or -3)
    """
    advantages = character.db.stats.get("advantages", {})
    merits = character.db.stats.get("merits", {})
    health_max = advantages.get("health", 7)
    health_track = get_health_track(character)
    
    # Count total damage taken
    total_damage = sum(1 for box in health_track if box is not None)
    
    # If no damage, no penalty
    if total_damage == 0:
        return 0
    
    # Calculate base penalty based on how much damage has been taken
    # If damage reaches the third-to-last box or beyond: penalty applies
    # For a health track of size N:
    # - Third-to-last box is at position N-3 (0-indexed: N-3)
    # - Second-to-last box is at position N-2 (0-indexed: N-2) 
    # - Last box is at position N-1 (0-indexed: N-1)
    
    # Since damage fills from left to right, we check if damage has reached these positions
    if total_damage >= health_max:  # Last box filled (incapacitated)
        base_penalty = -3
    elif total_damage >= health_max - 1:  # Second-to-last box filled
        base_penalty = -2
    elif total_damage >= health_max - 2:  # Third-to-last box filled
        base_penalty = -1
    else:
        base_penalty = 0
    
    # Apply Iron Stamina merit reduction
    iron_stamina = merits.get("iron_stamina", {})
    if iron_stamina and "dots" in iron_stamina:
        # Iron Stamina reduces penalty by 1 per dot (makes it less negative)
        base_penalty += iron_stamina["dots"]
        # Penalty cannot be positive
        if base_penalty > 0:
            base_penalty = 0
    
    return base_penalty

def get_health_display_with_penalty(character, force_ascii=False):
    """Get a visual representation of current health with wound penalty indicator"""
    display = get_health_display(character, force_ascii)
    wound_penalty = calculate_wound_penalty(character)
    
    if wound_penalty < 0:
        penalty_text = f" |r(Wound Penalty: {wound_penalty})|n"
        display += penalty_text
    
    return display