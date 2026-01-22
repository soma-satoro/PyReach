"""
Reality Systems for Chronicles of Darkness

This module handles the various reality perception systems in the game:
- Fae Reality (Mask/Mien for Changelings and Fae-Touched)
- Shadow/Hisil (Spirit world for Werewolves and Mages)
- Hedge (Changeling-specific reality)
- Gauntlet mechanics for crossing between worlds

These systems control what characters can see and experience based on
their supernatural nature and current reality state.
"""

from evennia.utils import logger
from datetime import datetime, timedelta
from django.utils import timezone


# =============================================================================
# FAE REALITY SYSTEM
# =============================================================================

def can_see_mien(viewer, target):
    """
    Check if a viewer can see a target's Mien (true fae form).
    
    Args:
        viewer (Character): The character trying to see
        target (Character): The character being viewed
        
    Returns:
        bool: True if viewer can see target's Mien
    """
    if not viewer or not target:
        return False
    
    # Safety check: ensure both characters have been saved to database (have IDs)
    if not hasattr(viewer, 'id') or viewer.id is None:
        return False
    if not hasattr(target, 'id') or target.id is None:
        return False
    
    # Get character templates
    viewer_template = get_template(viewer)
    target_template = get_template(target)
    
    # Changelings can always see Miens (unless target has strengthened their Mask)
    if viewer_template == "Changeling":
        # Check if target has strengthened their Mask
        if hasattr(target.db, 'mask_strengthened') and target.db.mask_strengthened:
            return False
        return True
    
    # Fae-Touched can see Miens (unless target has strengthened their Mask)
    if is_fae_touched(viewer):
        if hasattr(target.db, 'mask_strengthened') and target.db.mask_strengthened:
            return False
        return True
    
    # Characters enchanted by pledges can see Miens
    if hasattr(viewer.db, 'pledge_enchanted') and viewer.db.pledge_enchanted:
        if hasattr(target.db, 'mask_strengthened') and target.db.mask_strengthened:
            return False
        return True
    
    # If target has shed their Mask, everyone can see their Mien
    if hasattr(target.db, 'mask_shed') and target.db.mask_shed:
        return True
    
    return False


def is_fae_touched(character):
    """
    Check if a character is Fae-Touched (Mortal+ with fae connection).
    
    Fae-Touched characters can see Changeling Miens and Hedge Gates.
    
    Args:
        character (Character): The character to check
        
    Returns:
        bool: True if character is Fae-Touched
    """
    if not character:
        return False
    
    # Safety check: ensure character has been saved to database (has ID)
    # This prevents errors when checking tags on unsaved/deleted objects
    if not hasattr(character, 'id') or character.id is None:
        return False
    
    # Check for Fae-Touched tag (manually set by staff)
    if character.tags.get("fae_touched", category="supernatural"):
        return True
    
    # Check for Mortal+ template with Fae-Touched type
    template = get_template(character)
    if template in ["Mortal+", "Mortal Plus"]:
        bio = character.db.stats.get("bio", {})
        template_type = bio.get("template_type", "")
        if template_type and "fae" in template_type.lower():
            return True
    
    return False


def has_mien(character):
    """
    Check if a character should have a Mien description.
    
    Args:
        character (Character): The character to check
        
    Returns:
        bool: True if character should have a Mien
    """
    if not character:
        return False
    
    # Safety check: ensure character has been saved to database (has ID)
    # This prevents errors when checking tags on unsaved/deleted objects
    if not hasattr(character, 'id') or character.id is None:
        return False
    
    template = get_template(character)
    return template == "Changeling" or is_fae_touched(character)


def get_mien_description(character):
    """
    Get a character's Mien description.
    
    Args:
        character (Character): The character
        
    Returns:
        str: The Mien description, or None if not set
    """
    if not hasattr(character.db, 'mien_desc'):
        return None
    return character.db.mien_desc


def set_mien_description(character, description):
    """
    Set a character's Mien description.
    
    Args:
        character (Character): The character
        description (str): The Mien description
    """
    character.db.mien_desc = description


# =============================================================================
# SHADOW/HISIL SYSTEM
# =============================================================================

def can_cross_gauntlet(character):
    """
    Check if a character has the ability to cross the Gauntlet.
    
    Args:
        character (Character): The character to check
        
    Returns:
        bool: True if character can cross the Gauntlet
    """
    template = get_template(character)
    
    # Werewolves can always cross
    if template == "Werewolf":
        return True
    
    # Mages with Spirit 3+ can cross
    if template == "Mage":
        powers = character.db.stats.get("powers", {})
        arcana = powers.get("arcana", {})
        spirit_level = arcana.get("spirit", 0)
        if isinstance(spirit_level, dict):
            spirit_level = spirit_level.get("dots", 0)
        if spirit_level >= 3:
            return True
    
    return False


def can_peek_across_gauntlet(character):
    """
    Check if a character can see across the Gauntlet into the Shadow.
    
    Args:
        character (Character): The character to check
        
    Returns:
        bool: True if character can peek across
    """
    template = get_template(character)
    
    # Werewolves can always peek
    if template == "Werewolf":
        return True
    
    # Mages with Spirit 1+ can peek using Exorcist's Eye
    if template == "Mage":
        powers = character.db.stats.get("powers", {})
        arcana = powers.get("arcana", {})
        spirit_level = arcana.get("spirit", 0)
        if isinstance(spirit_level, dict):
            spirit_level = spirit_level.get("dots", 0)
        if spirit_level >= 1:
            return True
    
    return False


def is_in_shadow(character):
    """
    Check if a character is currently in the Shadow/Hisil.
    
    Args:
        character (Character): The character to check
        
    Returns:
        bool: True if character is in the Shadow
    """
    if not character:
        return False
    
    # Safety check: ensure character has been saved to database (has ID)
    if not hasattr(character, 'id') or character.id is None:
        return False
    
    return character.tags.get("in_shadow", category="reality")


def is_peeking_shadow(character):
    """
    Check if a character is currently peeking into the Shadow.
    
    Args:
        character (Character): The character to check
        
    Returns:
        bool: True if character is peeking
    """
    return character.tags.get("peeking_shadow", category="reality")


def set_shadow_state(character, in_shadow):
    """
    Set whether a character is in the Shadow.
    
    Args:
        character (Character): The character
        in_shadow (bool): True to put them in Shadow, False to remove
    """
    if in_shadow:
        character.tags.add("in_shadow", category="reality")
    else:
        character.tags.remove("in_shadow", category="reality")


def set_peeking_state(character, peeking):
    """
    Set whether a character is peeking into the Shadow.
    
    Args:
        character (Character): The character
        peeking (bool): True to set peeking, False to remove
    """
    if peeking:
        character.tags.add("peeking_shadow", category="reality")
    else:
        character.tags.remove("peeking_shadow", category="reality")


def get_gauntlet_rating(location):
    """
    Get the Gauntlet rating for a location.
    
    Returns a tuple of (strength, dice_modifier).
    
    Args:
        location (Room): The room to check
        
    Returns:
        tuple: (strength, dice_modifier) where strength is 0-5 and 
               dice_modifier is -3 to +2
    """
    if not location:
        return (3, -1)  # Default: Small towns
    
    # Check for explicit Gauntlet setting
    if hasattr(location.db, 'gauntlet_strength'):
        strength = location.db.gauntlet_strength
        # Calculate dice modifier based on strength
        modifier_map = {
            0: None,  # Verge - no gauntlet
            1: 2,     # Locus
            2: 0,     # Wilderness
            3: -1,    # Small towns
            4: -2,    # City suburbs
            5: -3     # Dense urban
        }
        return (strength, modifier_map.get(strength, -1))
    
    # Default based on area type
    return (3, -1)


def set_gauntlet_rating(location, strength):
    """
    Set the Gauntlet rating for a location.
    
    Args:
        location (Room): The room to set
        strength (int): Gauntlet strength (0-5)
    """
    if strength < 0:
        strength = 0
    if strength > 5:
        strength = 5
    location.db.gauntlet_strength = strength


def is_locus(location):
    """
    Check if a location is a Locus (place of spiritual power).
    
    Args:
        location (Room): The room to check
        
    Returns:
        bool: True if location is a Locus
    """
    if not location:
        return False
    return location.tags.get("locus", category="supernatural")


def get_locus_data(location):
    """
    Get Locus data for a location.
    
    Args:
        location (Room): The room to check
        
    Returns:
        dict: Locus data with keys 'level', 'resonance', 'essence_current', 'essence_max', 'last_refresh'
              Returns None if not a Locus
    """
    if not is_locus(location):
        return None
    
    if not hasattr(location.db, 'locus_data'):
        return None
    
    return location.db.locus_data


def create_locus(location, level, resonance):
    """
    Create a Locus at a location.
    
    Args:
        location (Room): The room to make into a Locus
        level (int): Locus level (1-5)
        resonance (str): Type of essence/resonance
        
    Returns:
        bool: True if successful
    """
    if level < 1:
        level = 1
    if level > 5:
        level = 5
    
    # Set locus tag
    location.tags.add("locus", category="supernatural")
    
    # Set Gauntlet to 1 (Loci have Gauntlet strength 1)
    set_gauntlet_rating(location, 1)
    
    # Calculate max essence (level * 3)
    max_essence = level * 3
    
    # Initialize locus data
    location.db.locus_data = {
        'level': level,
        'resonance': resonance,
        'essence_current': max_essence,
        'essence_max': max_essence,
        'last_refresh': timezone.now()
    }
    
    return True


def refresh_locus_essence(location):
    """
    Refresh essence for a Locus (called daily).
    
    Args:
        location (Room): The Locus room
        
    Returns:
        int: Amount of essence refreshed, or 0 if not refreshed
    """
    locus_data = get_locus_data(location)
    if not locus_data:
        return 0
    
    last_refresh = locus_data.get('last_refresh')
    if not last_refresh:
        last_refresh = timezone.now() - timedelta(days=1)
    
    # Check if 24 hours have passed
    now = timezone.now()
    if (now - last_refresh).total_seconds() < 86400:  # 24 hours
        return 0
    
    # Calculate days since last refresh
    days_passed = int((now - last_refresh).total_seconds() / 86400)
    
    # Regenerate essence
    level = locus_data['level']
    essence_per_day = level * 3
    essence_to_add = essence_per_day * days_passed
    
    current = locus_data['essence_current']
    max_essence = locus_data['essence_max']
    
    new_current = min(current + essence_to_add, max_essence)
    actual_refreshed = new_current - current
    
    # Update locus data
    locus_data['essence_current'] = new_current
    locus_data['last_refresh'] = now
    location.db.locus_data = locus_data
    
    return actual_refreshed


def draw_from_locus(location, character, amount):
    """
    Draw essence/mana from a Locus.
    
    Args:
        location (Room): The Locus room
        character (Character): The character drawing essence
        amount (int): Amount to draw
        
    Returns:
        tuple: (success, message)
    """
    locus_data = get_locus_data(location)
    if not locus_data:
        return (False, "This is not a Locus.")
    
    template = get_template(character)
    if template not in ["Werewolf", "Mage"]:
        return (False, "Only Werewolves and Mages can draw from Loci.")
    
    # Check if character is in Shadow (required to draw from Locus)
    if not is_in_shadow(character):
        return (False, "You must be in the Shadow to draw from this Locus.")
    
    current = locus_data['essence_current']
    if amount > current:
        return (False, f"This Locus only has {current} essence available.")
    
    # Deduct from Locus
    locus_data['essence_current'] = current - amount
    location.db.locus_data = locus_data
    
    # Add to character's pool
    if template == "Werewolf":
        pool_name = "essence"
    elif template == "Mage":
        pool_name = "mana"
    else:
        return (False, "Unknown power pool for your template.")
    
    # Get current pool value
    current_pool = character.db.stats.get(pool_name + "_current", 0)
    max_pool = character.db.stats.get("advantages", {}).get(pool_name, 10)
    
    new_pool = min(current_pool + amount, max_pool)
    actual_gained = new_pool - current_pool
    
    character.db.stats[pool_name + "_current"] = new_pool
    
    return (True, f"You draw {actual_gained} {pool_name} from the Locus.")


# =============================================================================
# HEDGE SYSTEM
# =============================================================================

def can_enter_hedge(character):
    """
    Check if a character can enter the Hedge.
    
    Args:
        character (Character): The character to check
        
    Returns:
        bool: True if character can enter the Hedge
    """
    return get_template(character) == "Changeling"


def is_in_hedge(character):
    """
    Check if a character is currently in the Hedge.
    
    Args:
        character (Character): The character to check
        
    Returns:
        bool: True if character is in the Hedge
    """
    # Check if character's location has hedge tag
    location = character.location
    if location:
        return location.tags.get("hedge", category="reality")
    return False


def is_hedge_gate(exit_obj):
    """
    Check if an exit is a Hedge Gate.
    
    Args:
        exit_obj (Exit): The exit to check
        
    Returns:
        bool: True if exit is a Hedge Gate
    """
    if not exit_obj:
        return False
    return exit_obj.tags.get("hedge_gate", category="supernatural")


def can_see_hedge_gate(character, exit_obj):
    """
    Check if a character can see a Hedge Gate.
    
    Args:
        character (Character): The character
        exit_obj (Exit): The Hedge Gate exit
        
    Returns:
        bool: True if character can see the gate
    """
    if not is_hedge_gate(exit_obj):
        return True  # Regular exits are always visible
    
    template = get_template(character)
    if template == "Changeling":
        return True
    
    if is_fae_touched(character):
        return True
    
    return False


def is_hedge_gate_closed(exit_obj):
    """
    Check if a Hedge Gate is closed (used for 3 IC months).
    
    Args:
        exit_obj (Exit): The Hedge Gate exit
        
    Returns:
        bool: True if gate is closed
    """
    if not is_hedge_gate(exit_obj):
        return False
    
    if hasattr(exit_obj.db, 'gate_closed_until'):
        closed_until = exit_obj.db.gate_closed_until
        if closed_until and timezone.now() < closed_until:
            return True
    
    return False


def open_hedge_gate(exit_obj):
    """
    Open a Hedge Gate (closes it for 3 IC months after use).
    
    Args:
        exit_obj (Exit): The Hedge Gate exit
        
    Returns:
        tuple: (success, message)
    """
    if not is_hedge_gate(exit_obj):
        return (False, "This is not a Hedge Gate.")
    
    if is_hedge_gate_closed(exit_obj):
        closed_until = exit_obj.db.gate_closed_until
        time_left = closed_until - timezone.now()
        days_left = time_left.days
        return (False, f"This gate is closed and will remain so for {days_left} more days.")
    
    # Close the gate for 3 IC months (90 days)
    exit_obj.db.gate_closed_until = timezone.now() + timedelta(days=90)
    
    return (True, "The Hedge Gate opens before you.")


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def get_template(character):
    """
    Get a character's supernatural template.
    
    Args:
        character (Character): The character to check
        
    Returns:
        str: Template name (e.g., "Changeling", "Werewolf", "Mage", "Mortal")
    """
    if not character or not hasattr(character, 'db'):
        return "Mortal"
    
    stats = character.db.stats
    if not stats:
        return "Mortal"
    
    other = stats.get("other", {})
    template = other.get("template", "Mortal")
    
    # Normalize template name
    if isinstance(template, str):
        template = template.title().replace("_", " ")
    
    return template


def get_harmony(character):
    """
    Get a Werewolf's Harmony rating.
    
    For Werewolves, Harmony is stored as 'integrity' in the 'other' section of stats.
    
    Args:
        character (Character): The character (must be Werewolf)
        
    Returns:
        int: Harmony rating (1-10), or None if not a Werewolf
    """
    if get_template(character) != "Werewolf":
        return None
    
    # Harmony is stored as 'integrity' in the 'other' section for Werewolves
    other = character.db.stats.get("other", {})
    harmony = other.get("integrity", 5)
    
    if isinstance(harmony, dict):
        harmony = harmony.get("dots", 5)
    
    return harmony


def calculate_gauntlet_pool(character, location, entering_shadow=True):
    """
    Calculate the dice pool for crossing the Gauntlet.
    
    For Werewolves:
      - Entering Shadow: 10 - Harmony + Gauntlet modifier
      - Entering Flesh: Harmony + Gauntlet modifier
      
    Args:
        character (Character): The character attempting to cross
        location (Room): The location they're crossing from
        entering_shadow (bool): True if entering Shadow, False if entering Flesh
        
    Returns:
        tuple: (dice_pool, modifiers_text)
    """
    template = get_template(character)
    
    if template != "Werewolf":
        return (0, "Only Werewolves can use this calculation.")
    
    harmony = get_harmony(character)
    gauntlet_strength, gauntlet_mod = get_gauntlet_rating(location)
    
    # Base pool
    if entering_shadow:
        base_pool = 10 - harmony
    else:
        base_pool = harmony
    
    # Apply Gauntlet modifier
    total_pool = base_pool + gauntlet_mod
    
    # Build modifier text
    modifiers = []
    if entering_shadow:
        modifiers.append(f"Base: 10 - Harmony ({harmony}) = {base_pool}")
    else:
        modifiers.append(f"Base: Harmony ({harmony}) = {base_pool}")
    
    modifiers.append(f"Gauntlet modifier: {gauntlet_mod:+d}")
    
    # Check for special modifiers
    # TODO: Add checks for reflective surface, time of day, etc.
    
    modifiers.append(f"Total pool: {total_pool}")
    
    return (max(0, total_pool), "\n".join(modifiers))
