"""
Clarity damage tracking system for Changelings in Chronicles of Darkness.
Similar to health tracking but for Clarity (Changeling integrity stat).
"""

# Clarity-specific Conditions
# These are conditions that can be gained from Clarity damage
CLARITY_CONDITIONS = {
    "broken": {"name": "Broken", "persistent": True},
    "comatose": {"name": "Comatose", "persistent": False},
    "confused": {"name": "Confused", "persistent": False},
    "delusional": {"name": "Delusional", "persistent": True},
    "dissociation": {"name": "Dissociation", "persistent": False},
    "distracted": {"name": "Distracted", "persistent": False},
    "fugue": {"name": "Fugue", "persistent": True},
    "numb": {"name": "Numb", "persistent": True},
    "shaken": {"name": "Shaken", "persistent": False},
    "sleepwalking": {"name": "Sleepwalking", "persistent": True},
    "spooked": {"name": "Spooked", "persistent": False},
}

# Separate lists for menu display
CLARITY_CONDITIONS_REGULAR = [
    "comatose", "confused", "dissociation", "distracted", "shaken", "spooked"
]

CLARITY_CONDITIONS_PERSISTENT = [
    "broken", "delusional", "fugue", "numb", "sleepwalking"
]

def get_clarity_track(character):
    """
    Get Clarity track as an array where index 0 is leftmost.
    Returns array of damage types ('mild' or 'severe') or None for empty boxes.
    
    Clarity track size equals the character's Clarity rating.
    """
    try:
        clarity_max = character.db.stats['other'].get('integrity', 7)
    except (KeyError, TypeError, AttributeError):
        clarity_max = 7
    
    clarity_damage = character.db.clarity_damage or {}
    
    # Convert dictionary format to array format
    track = [None] * clarity_max
    for position, damage_type in clarity_damage.items():
        if 1 <= position <= clarity_max:
            track[position - 1] = damage_type  # Convert to 0-based indexing
    
    return track


def set_clarity_track(character, track):
    """
    Set Clarity track from array format back to dictionary format.
    """
    clarity_damage = {}
    for i, damage_type in enumerate(track):
        if damage_type:
            clarity_damage[i + 1] = damage_type  # Convert to 1-based indexing
    
    character.db.clarity_damage = clarity_damage


def get_clarity_display(character):
    """Get a visual representation of current Clarity damage."""
    try:
        clarity_max = character.db.stats['other'].get('integrity', 7)
    except (KeyError, TypeError, AttributeError):
        clarity_max = 7
    
    clarity_track = get_clarity_track(character)
    
    # Create Clarity boxes
    clarity_boxes = []
    for i in range(clarity_max):
        damage_type = clarity_track[i]
        if damage_type == "mild":
            clarity_boxes.append("[|c/|n]")  # Cyan for mild
        elif damage_type == "severe":
            clarity_boxes.append("[|rX|n]")  # Red for severe
        else:
            clarity_boxes.append("[ ]")
    
    return "  " + "".join(clarity_boxes)


def get_clarity_display_with_info(character):
    """Get Clarity display with additional information."""
    try:
        clarity_max = character.db.stats['other'].get('integrity', 7)
    except (KeyError, TypeError, AttributeError):
        clarity_max = 7
    
    clarity_track = get_clarity_track(character)
    display = get_clarity_display(character)
    
    # Count damage
    mild_count = sum(1 for d in clarity_track if d == "mild")
    severe_count = sum(1 for d in clarity_track if d == "severe")
    total_damage = mild_count + severe_count
    
    # Check if damage is in rightmost 3 boxes (triggers Conditions)
    rightmost_damage = False
    if clarity_max >= 3:
        for i in range(clarity_max - 3, clarity_max):
            if clarity_track[i] is not None:
                rightmost_damage = True
                break
    
    info_lines = [display]
    
    if total_damage > 0:
        damage_info = f"|xMild: {mild_count}  Severe: {severe_count}  Total: {total_damage}/{clarity_max}|n"
        info_lines.append("  " + damage_info)
        
        if rightmost_damage:
            info_lines.append("  |yDamage in rightmost boxes - Clarity Condition active!|n")
    
    # Show perception modifier
    undamaged_clarity = clarity_max - total_damage
    if undamaged_clarity >= 5:
        info_lines.append("  |gPerception: +2 dice|n")
    elif undamaged_clarity >= 3:
        info_lines.append("  |yPerception: -1 die|n")
    elif undamaged_clarity >= 1:
        info_lines.append("  |rPerception: -2 dice (hallucinations on dramatic failure)|n")
    else:
        info_lines.append("  |RClarityFULL - COMATOSE RISK!|n")
    
    return "\n".join(info_lines)


def add_clarity_damage(character, damage_type="mild", amount=1):
    """
    Add Clarity damage to a character.
    
    Args:
        character: The character object
        damage_type: 'mild' or 'severe'
        amount: Number of damage to add
        
    Returns:
        tuple: (success, message, condition_triggered)
    """
    try:
        clarity_max = character.db.stats['other'].get('integrity', 7)
    except (KeyError, TypeError, AttributeError):
        clarity_max = 7
    
    clarity_track = get_clarity_track(character)
    
    # Count current damage
    total_damage = sum(1 for d in clarity_track if d is not None)
    
    if total_damage >= clarity_max:
        return (False, "|rYour Clarity track is already full!|n", False)
    
    condition_triggered = False
    rightmost_start = max(0, clarity_max - 3)
    
    for _ in range(amount):
        if damage_type == "mild":
            # Find leftmost empty box
            for i in range(clarity_max):
                if clarity_track[i] is None:
                    clarity_track[i] = "mild"
                    if i >= rightmost_start:
                        condition_triggered = True
                    break
        else:  # severe
            # Find leftmost empty box or mild damage box
            placed = False
            for i in range(clarity_max):
                if clarity_track[i] is None or clarity_track[i] == "mild":
                    clarity_track[i] = "severe"
                    if i >= rightmost_start:
                        condition_triggered = True
                    placed = True
                    break
            
            if not placed:
                # Track is full
                set_clarity_track(character, clarity_track)
                return (False, "|rClarity track is full! Character risks Comatose Condition!|n", True)
    
    # Save the updated track
    set_clarity_track(character, clarity_track)
    
    # Build message
    damage_word = "mild" if damage_type == "mild" else "severe"
    msg = f"|rYou take {amount} {damage_word} Clarity damage!|n\n"
    msg += get_clarity_display_with_info(character)
    
    if condition_triggered:
        msg += "\n|yDamage in rightmost boxes - gain a Clarity Condition!|n"
    
    return (True, msg, condition_triggered)


def heal_clarity_damage(character, amount=1, heal_severe=False):
    """
    Heal Clarity damage.
    
    Args:
        character: The character object
        amount: Number of boxes to heal
        heal_severe: If True, heals severe damage; if False, heals mild
        
    Returns:
        tuple: (success, message)
    """
    clarity_track = get_clarity_track(character)
    
    healed = 0
    target_type = "severe" if heal_severe else "mild"
    
    # Heal from right to left
    for i in range(len(clarity_track) - 1, -1, -1):
        if healed >= amount:
            break
        
        if clarity_track[i] == target_type:
            clarity_track[i] = None
            healed += 1
        elif not heal_severe and clarity_track[i] is not None:
            # When healing mild, can heal any damage
            clarity_track[i] = None
            healed += 1
    
    if healed == 0:
        return (False, f"|yNo {target_type} Clarity damage to heal.|n")
    
    # Save the updated track
    set_clarity_track(character, clarity_track)
    
    damage_word = "severe" if heal_severe else "mild"
    msg = f"|gYou heal {healed} box{'es' if healed != 1 else ''} of {damage_word} Clarity damage!|n\n"
    msg += get_clarity_display_with_info(character)
    
    return (True, msg)


def get_clarity_perception_modifier(character):
    """
    Get the perception modifier based on current Clarity.
    
    Returns:
        int: Dice pool modifier for perception rolls
    """
    try:
        clarity_max = character.db.stats['other'].get('integrity', 7)
    except (KeyError, TypeError, AttributeError):
        clarity_max = 7
    
    clarity_track = get_clarity_track(character)
    total_damage = sum(1 for d in clarity_track if d is not None)
    undamaged_clarity = clarity_max - total_damage
    
    if undamaged_clarity >= 5:
        return 2
    elif undamaged_clarity >= 3:
        return -1
    elif undamaged_clarity >= 1:
        return -2
    else:
        return -2  # Full track, severe penalties
