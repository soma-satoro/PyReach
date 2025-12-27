"""
Stat management utilities for character statistics.
Handles stat removal, validation, and permissions.
"""


def check_stat_permissions(caller, target, is_removal=False):
    """
    Check if caller has permission to modify target's stats.
    
    Args:
        caller: The caller object
        target: The target character object
        is_removal (bool): Whether this is a removal operation
        
    Returns:
        tuple: (has_permission, error_message)
    """
    # Check if target is an NPC
    is_npc = hasattr(target, 'db') and target.db.is_npc
    
    if target == caller:
        # Modifying own stats
        if not is_npc and target.db.approved:
            return False, "Your character is approved. Only staff can modify your stats."
        return True, None
    
    # Modifying someone else's stats
    if is_npc:
        # For NPCs, check if caller can control them
        if hasattr(target, 'can_control') and target.can_control(caller):
            return True, None
        return False, "You don't have permission to modify that NPC's stats."
    else:
        # For player characters, requires staff
        if caller.check_permstring("Builder"):
            return True, None
        action = "remove stats from" if is_removal else "set stats for"
        return False, f"Only staff can {action} other player characters."


def remove_stat_from_character(character, stat, caller):
    """
    Remove a stat from a character.
    
    Args:
        character: The character object
        stat (str): The stat to remove
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    if not character.db.stats:
        return False, f"{character.name} has no stats set."
    
    # Check if removing a specialty
    if stat.startswith("specialty/"):
        return _remove_specialty(character, stat, caller)
    
    # Check if removing an adaptation (format: "adaptation <name>")
    if stat.startswith("adaptation "):
        adaptation_name = stat[11:]  # Remove "adaptation " prefix
        return _remove_adaptation(character, adaptation_name, caller)
    
    # Check if trying to remove a merit (including instanced merits)
    base_merit_name = stat
    if ":" in stat:
        base_merit_name, _ = stat.split(":", 1)
    
    try:
        from world.cofd.merits.general_merits import merits_dict
        
        if base_merit_name in merits_dict:
            # Check if character is approved and not an NPC
            is_npc = hasattr(character, 'db') and character.db.is_npc
            if character.db.approved and not is_npc:
                error_msg = f"Character is approved. Merits cannot be removed directly with +stat."
                if caller.check_permstring("Builder"):
                    error_msg += f"\nUse '+xp/refund {stat}' to refund the merit and return experience points."
                else:
                    error_msg += f"\nOnly staff can refund merits. Contact staff for assistance."
                return False, error_msg
            # For unapproved characters and NPCs, allow direct removal (handled below)
    except ImportError:
        # If merit system not available, continue with normal removal
        pass
    
    # Special handling for mage arcana: map "death" to "arcanum_death"
    character_template = character.db.stats.get("other", {}).get("template", "Mortal")
    if character_template.lower() in ["mage", "legacy_mage"]:
        if stat == "death":
            stat = "arcanum_death"
    
    # Try to find stat in all categories
    for category in ["attributes", "skills", "advantages", "bio", "anchors", "merits", "powers", "other"]:
        if stat in character.db.stats.get(category, {}):
            # Special handling for template (staff only)
            if stat == "template" and category == "other":
                if not caller.check_permstring("Builder"):
                    return False, "Only staff can modify template."
            
            # Special handling for template-specific bio fields
            if stat in ["path", "order", "mask", "dirge", "clan", "covenant", "bone", "blood", 
                       "auspice", "tribe", "seeming", "court", "kith", "burden", "archetype", 
                       "krewe", "lineage", "refinement", "profession", "organization", "creed", 
                       "incarnation", "agenda", "agency", "hunger", "family", "inheritance", 
                       "origin", "clade", "divergence", "needle", "thread", "legend", "life",
                       "entitlement", "bloodline", "keeper", "motley", "pack", "lodge", "legacy",
                       "cabal", "lineage", "refinement", "athanor", "conspiracy", "cell", "threshold",
                       "decree", "guild", "judge", "incarnation", "agenda", "origin", "clade", "form",
                       "keeper", "sire", "progenitor"] and category == "bio":
                character_template = character.db.stats.get("other", {}).get("template", "Mortal")
                valid_fields = character.get_template_bio_fields(character_template)
                
                if stat not in valid_fields:
                    return False, f"{stat.title()} is not a valid field for {character_template} characters."
            
            # Special handling for virtue/vice (remove from both bio and anchors)
            if stat in ["virtue", "vice"]:
                character.db.stats.get("bio", {}).pop(stat, None)
                character.db.stats.get("anchors", {}).pop(stat, None)
            else:
                del character.db.stats[category][stat]
            
            # Recalculate derived stats if merit was removed
            if category == "merits" and hasattr(character, 'calculate_derived_stats'):
                character.calculate_derived_stats()
            
            # Format display for instanced merits and semantic powers with colons
            display_stat = stat
            if ":" in stat:
                base_name, instance = stat.split(":", 1)
                # Check if this is a semantic power (devotion, discipline_power, etc.) or an instanced merit
                semantic_power_types = ["devotion", "discipline_power", "coil", "scale", "theban", "cruac", "gift", 
                                       "contract", "spell", "alembic", "bestowment", "endowment", "embed", "exploit",
                                       "adaptation", "key", "ceremony", "rite"]
                if base_name in semantic_power_types:
                    # This is a semantic power like devotion:in_vitae_veritas
                    # Try to get the actual power name for better display
                    try:
                        if base_name == "devotion":
                            from world.cofd.powers.vampire_disciplines import ALL_DEVOTIONS
                            if instance in ALL_DEVOTIONS:
                                display_stat = ALL_DEVOTIONS[instance].get('name', instance.replace('_', ' ').title())
                            else:
                                display_stat = f"{base_name.replace('_', ' ').title()}: {instance.replace('_', ' ').title()}"
                        else:
                            # Generic semantic power format
                            display_stat = f"{base_name.replace('_', ' ').title()}: {instance.replace('_', ' ').title()}"
                    except ImportError:
                        display_stat = f"{base_name.replace('_', ' ').title()}: {instance.replace('_', ' ').title()}"
                else:
                    # This is an instanced merit
                    display_stat = f"{base_name.replace('_', ' ').title()} ({instance.replace('_', ' ').title()})"
            else:
                # Clean up power prefixes for better display
                if stat.startswith('discipline_'):
                    display_stat = stat[11:]  # Remove 'discipline_'
                elif stat.startswith('arcanum_'):
                    display_stat = stat[8:]   # Remove 'arcanum_'
                elif stat.startswith('gift_'):
                    display_stat = stat[5:]   # Remove 'gift_'
                
                display_stat = display_stat.replace('_', ' ').title()
            
            return True, f"Removed {display_stat} from {character.name}."
    
    return False, f"{character.name} doesn't have a stat called {stat}."


def _remove_specialty(character, stat, caller):
    """
    Remove all specialties for a skill.
    
    Args:
        character: The character object
        stat (str): The specialty stat (format: "specialty/skill_name")
        caller: The caller object
        
    Returns:
        tuple: (success, message)
    """
    skill_name = stat[10:]  # Remove "specialty/" prefix
    specialties = character.db.stats.get("specialties", {})
    
    if skill_name in specialties and specialties[skill_name]:
        # Remove all specialties for this skill
        del specialties[skill_name]
        skill_display = skill_name.replace('_', ' ').title()
        return True, f"Removed all specialties for {character.name}'s {skill_display}."
    else:
        skill_display = skill_name.replace('_', ' ').title()
        return False, f"{character.name} has no specialties for {skill_display}."


def _remove_adaptation(character, adaptation_name, caller):
    """
    Remove a specific adaptation from a Deviant character.
    
    Args:
        character: The character object
        adaptation_name (str): The adaptation name to remove
        caller: The caller object
        
    Returns:
        tuple: (success, message)
    """
    from world.cofd.powers.deviant_data import DEVIANT_ADAPTATIONS
    
    # Normalize adaptation name
    adaptation_key = adaptation_name.lower().replace(" ", "_")
    
    # Validate it's a real adaptation
    if adaptation_key not in DEVIANT_ADAPTATIONS:
        return False, f"'{adaptation_name}' is not a valid adaptation. Use +lookup adaptations to see available adaptations."
    
    # Check nested structure first
    powers = character.db.stats.get("powers", {})
    adaptations_dict = powers.get("adaptations", {})
    
    if adaptation_key in adaptations_dict:
        # Remove from nested structure
        del adaptations_dict[adaptation_key]
        character.db.stats = character.db.stats  # Trigger persistence
        adaptation_display = DEVIANT_ADAPTATIONS[adaptation_key]['name']
        return True, f"Removed adaptation: {adaptation_display}"
    
    # Check legacy storage in 'other' dict
    other = character.db.stats.get("other", {})
    if "adaptation" in other:
        # Single adaptation stored as string value
        if other["adaptation"].lower().replace(" ", "_") == adaptation_key:
            del other["adaptation"]
            character.db.stats = character.db.stats  # Trigger persistence
            adaptation_display = DEVIANT_ADAPTATIONS[adaptation_key]['name']
            return True, f"Removed adaptation: {adaptation_display}"
    
    # Check if stored with "adaptations" plural in 'other'
    if "adaptations" in other:
        if isinstance(other["adaptations"], list):
            # List format
            for i, adapt in enumerate(other["adaptations"]):
                if adapt.lower().replace(" ", "_") == adaptation_key:
                    del other["adaptations"][i]
                    character.db.stats = character.db.stats  # Trigger persistence
                    adaptation_display = DEVIANT_ADAPTATIONS[adaptation_key]['name']
                    return True, f"Removed adaptation: {adaptation_display}"
        elif isinstance(other["adaptations"], dict):
            # Dict format
            if adaptation_key in other["adaptations"]:
                del other["adaptations"][adaptation_key]
                character.db.stats = character.db.stats  # Trigger persistence
                adaptation_display = DEVIANT_ADAPTATIONS[adaptation_key]['name']
                return True, f"Removed adaptation: {adaptation_display}"
    
    adaptation_display = DEVIANT_ADAPTATIONS[adaptation_key]['name']
    return False, f"{character.name} doesn't have the {adaptation_display} adaptation."

