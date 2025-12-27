"""
Power management utilities for supernatural abilities.
Handles semantic power syntax and power validation.
"""

from world.cofd.powers.promethean_powers import ALL_ALEMBICS, PROMETHEAN_BESTOWMENTS
from world.cofd.powers.hunter_endowments import ALL_ENDOWMENT_POWERS
from world.cofd.powers.mage_spells import ALL_MAGE_SPELLS, get_spell
from world.cofd.powers.vampire_disciplines import (
    ALL_DISCIPLINE_POWERS, ALL_DEVOTIONS
)
from world.cofd.powers.vampire_rituals import (
    ALL_SCALES, ALL_THEBAN, ALL_CRUAC
)
from world.cofd.powers.werewolf_gifts import ALL_WEREWOLF_GIFTS
from world.cofd.powers.changeling_contracts import ALL_CHANGELING_CONTRACTS
from world.cofd.powers.demon_powers import ALL_EMBEDS, DEMON_EXPLOITS, ALL_EMBED_NAMES, ALL_EXPLOIT_NAMES
from world.cofd.powers.deviant_data import DEVIANT_ADAPTATIONS


def get_valid_semantic_powers(power_type):
    """
    Get list of valid powers for a semantic power type.
    
    Args:
        power_type (str): Type of power (key, ceremony, rite, ritual, contract, spell, alembic, bestowment, endowment, adaptation)
        
    Returns:
        list: List of valid power names for that type
    """
    valid_powers = {
        "key": ["beasts", "blood", "chance", "cold_wind", "deep_waters", "disease", "grave_dirt", "pyre_flame", "stillness"],
        "ceremony": [
            "dead_mans_camera", "death_watch", "diviners_jawbone", "lovers_telephone", "ishtars_perfume",
            "crow_girl_kiss", "gifts_of_persephone", "ghost_trap", "skeleton_key", "bestow_regalia", 
            "krewe_binding", "speaker_for_the_dead", "black_cats_crossing", "bloody_codex", "dumb_supper",
            "forge_anchor", "maggot_homonculus", "pass_on", "ghost_binding", "persephones_return"
        ],
        "rite": [
            "chain_rage", "messenger", "banish", "harness_the_cycle", "totemic_empowerment",
            "bottle_spirit", "infest_locus", "rite_of_the_shroud", "sacred_hunt", "hunting_ground", "moons_mad_love",
            "shackled_lightning", "sigrblot", "wellspring", "carrion_feast", "flay_auspice", "kindle_fury", 
            "rite_of_absolution", "shadowbind", "the_thorn_pursuit", "banshee_howl", "raiment_of_the_storm", 
            "shadowcall", "supplication", "between_worlds", "fetish", "shadow_bridge", "twilight_purge", 
            "hidden_path", "expel", "heal_old_wounds", "lupus_venandi", "devour", "forge_alliance", 
            "urfarahs_bane", "veil", "great_hunt", "shadow_distortion", "unleash_shadow"
        ],
        "ritual": [
            # Legacy keyword - kept for backward compatibility, but specific keywords preferred
            "ban_of_the_spiteful_bastard", "mantle_of_amorous_fire", "pangs_of_proserpina", 
            "pool_of_forbidden_truths", "rigor_mortis", "cheval", "mantle_of_the_beasts_breath", 
            "the_hydras_vitae", "shed_the_virulent_bowels", "curse_of_aphrodites_favor", 
            "curse_of_the_beloved_toy", "deflection_of_wooden_doom", "donning_the_beasts_flesh", 
            "mantle_of_the_glorious_dervish", "touch_of_the_morrigan", "blood_price", "willful_vitae", 
            "blood_blight", "feeding_the_crone", "bounty_of_the_storm", "gorgons_gaze", 
            "manananggals_working", "mantle_of_the_predator_goddess", "quicken_the_withered_womb", 
            "the_red_blossoms", "birthing_the_god", "denying_hades", "gwydions_curse", 
            "mantle_of_the_crone", "scapegoat", "apple_of_eden", "blandishment_of_sin", 
            "blood_scourge", "marian_apparition", "revelatory_shroud", "vitae_reliquary", 
            "apparition_of_the_host", "bloody_icon", "curse_of_babel", "liars_plague", 
            "the_walls_of_jericho", "aarons_rod", "baptism_of_damnation", "blessing_the_legion", 
            "the_guiding_star", "malediction_of_despair", "miracle_of_the_dead_sun", 
            "pledge_to_the_worthless_one", "the_rite_of_ascending_blood", "blandishment_of_sin_advanced", 
            "curse_of_isolation", "gift_of_lazarus", "great_prophecy", "stigmata", "trials_of_job", 
            "apocalypse", "the_judgment_fast", "orison_of_voices", "sins_of_the_ancestors", "transubstatiation"
        ],
        "discipline_power": list(ALL_DISCIPLINE_POWERS.keys()),
        "devotion": list(ALL_DEVOTIONS.keys()),
        "coil": list(ALL_DISCIPLINE_POWERS.keys()),  # Coils are in ALL_DISCIPLINE_POWERS
        "scale": list(ALL_SCALES.keys()),
        "theban": list(ALL_THEBAN.keys()),
        "cruac": list(ALL_CRUAC.keys()),
        "gift": list(ALL_WEREWOLF_GIFTS.keys()),
        "contract": list(ALL_CHANGELING_CONTRACTS.keys()),
        "spell": list(ALL_MAGE_SPELLS.keys()),
        "alembic": [a.lower().replace(" ", "_").replace("'", "") for a in ALL_ALEMBICS],
        "bestowment": [b.lower().replace(" ", "_").replace("'", "") for b in PROMETHEAN_BESTOWMENTS],
        "endowment": ALL_ENDOWMENT_POWERS,
        "embed": ALL_EMBED_NAMES,
        "exploit": ALL_EXPLOIT_NAMES,
        "adaptation": list(DEVIANT_ADAPTATIONS.keys())
    }
    
    return valid_powers.get(power_type, [])


def get_template_requirements(power_type):
    """
    Get template requirements for a power type.
    
    Args:
        power_type (str): Type of power
        
    Returns:
        list: List of templates that can use this power type
    """
    template_requirements = {
        "key": ["geist"],
        "ceremony": ["geist"],
        "rite": ["werewolf"],
        "ritual": ["vampire"],  # Legacy keyword for backward compatibility
        "discipline_power": ["vampire"],
        "devotion": ["vampire"],
        "coil": ["vampire"],
        "scale": ["vampire"],
        "theban": ["vampire"],
        "cruac": ["vampire"],
        "gift": ["werewolf"],
        "contract": ["changeling"],
        "spell": ["mage", "legacy_mage"],
        "alembic": ["promethean"],
        "bestowment": ["promethean"],
        "endowment": ["hunter"],
        "embed": ["demon"],
        "exploit": ["demon"],
        "adaptation": ["deviant"]
    }
    
    return template_requirements.get(power_type, [])


def check_devotion_prerequisites(character, devotion_data):
    """
    Check if a character meets the prerequisites for a devotion.
    
    Args:
        character: The character object
        devotion_data (dict): The devotion data dictionary with prerequisites and covenant fields
        
    Returns:
        tuple: (meets_prerequisites (bool), error_message (str or None))
    """
    stats = character.db.stats or {}
    powers = stats.get("powers", {})
    bio = stats.get("bio", {})
    
    # Check covenant requirement if present
    if "covenant" in devotion_data:
        required_covenant = devotion_data["covenant"].lower().replace(" ", "_")
        character_covenant = bio.get("covenant", "").lower().replace(" ", "_")
        
        if character_covenant != required_covenant:
            covenant_display = devotion_data["covenant"].title()
            character_covenant_display = bio.get("covenant", "None")
            return False, f"This devotion requires membership in the {covenant_display} covenant. Your covenant is: {character_covenant_display}"
    
    # Check bloodline requirement if present
    if "bloodline" in devotion_data:
        required_bloodline = devotion_data["bloodline"].lower().replace(" ", "_")
        character_bloodline = bio.get("bloodline", "").lower().replace(" ", "_")
        
        if character_bloodline != required_bloodline:
            bloodline_display = devotion_data["bloodline"].title()
            character_bloodline_display = bio.get("bloodline", "None")
            return False, f"This devotion requires the {bloodline_display} bloodline. Your bloodline is: {character_bloodline_display}"
    
    # Check prerequisites
    prerequisites_str = devotion_data.get("prerequisites", "")
    if not prerequisites_str:
        return True, None
    
    # Parse prerequisites - handle comma-separated AND requirements, brackets for OR requirements
    prereqs = _parse_devotion_prerequisites(prerequisites_str)
    
    for prereq in prereqs:
        prereq = prereq.strip()
        
        # Handle OR requirements [option1,option2]
        if prereq.startswith("[") and prereq.endswith("]"):
            or_options = prereq[1:-1].split(",")
            or_met = False
            for option in or_options:
                if _check_single_devotion_prerequisite(character, option.strip(), powers):
                    or_met = True
                    break
            if not or_met:
                # Build helpful error message
                or_list = ", ".join([opt.strip() for opt in or_options])
                return False, f"You must have one of: {or_list}"
        else:
            if not _check_single_devotion_prerequisite(character, prereq, powers):
                return False, f"You must have: {prereq}"
    
    return True, None


def _parse_devotion_prerequisites(prereq_string):
    """
    Parse prerequisite string, respecting bracket groups for OR requirements.
    Similar to merit prerequisite parsing.
    """
    prereqs = []
    current = ""
    bracket_depth = 0
    
    for char in prereq_string:
        if char == '[':
            bracket_depth += 1
            current += char
        elif char == ']':
            bracket_depth -= 1
            current += char
        elif char == ',' and bracket_depth == 0:
            # Only split on commas outside of brackets
            if current.strip():
                prereqs.append(current.strip())
            current = ""
        else:
            current += char
    
    # Add the last prerequisite
    if current.strip():
        prereqs.append(current.strip())
    
    return prereqs


def _check_single_devotion_prerequisite(character, prereq, powers):
    """
    Check a single devotion prerequisite requirement.
    Format: discipline:level (e.g., "vigor:5", "majesty:3")
    """
    prereq = prereq.strip()
    
    # Parse discipline:level
    if ":" not in prereq:
        return False
    
    discipline_name, required_level = prereq.split(":", 1)
    discipline_name = discipline_name.strip().lower()
    
    try:
        required_level = int(required_level.strip())
    except ValueError:
        return False
    
    # Get character's discipline level
    current_level = powers.get(discipline_name, 0)
    
    return current_level >= required_level


def handle_semantic_power(character, power_type, power_name, value, caller):
    """
    Handle semantic power syntax like key=beasts, ceremony=pass_on, spell=telekinesis, etc.
    
    Args:
        character: The character object
        power_type (str): Type of power (key, ceremony, rite, ritual, contract, spell, alembic, bestowment, endowment,
                                          discipline_power, devotion, coil, scale, theban, cruac)
        power_name (str): Name of the specific power
        value: The value to set (usually "known" or 1)
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    character_template = character.db.stats.get("other", {}).get("template", "Mortal")
    
    # Get valid powers for this type
    valid_powers = get_valid_semantic_powers(power_type)
    
    # Validate power type
    if not valid_powers:
        return False, f"Invalid power type: {power_type}\nValid types: key, ceremony, rite, ritual, contract, spell, alembic, bestowment, endowment, discipline_power, devotion, coil, scale, theban, cruac, embed, exploit, adaptation"
    
    # Validate power name
    if power_name not in valid_powers:
        if power_type == "spell":
            return False, f"Invalid spell: {power_name}\nUse +lookup spells to browse spells or +lookup <spell_name> for details. There are {len(valid_powers)} spells available."
        elif power_type == "endowment":
            return False, f"Invalid endowment: {power_name}\nUse +lookup endowments to browse endowments or +lookup <endowment_name> for details. There are {len(valid_powers)} endowments available."
        elif power_type in ["discipline_power", "devotion", "coil"]:
            return False, f"Invalid {power_type.replace('_', ' ')}: {power_name}\nUse +lookup {power_type.split('_')[0]}s to browse or +lookup <power_name> for details. There are {len(valid_powers)} available."
        elif power_type in ["scale", "theban", "cruac"]:
            return False, f"Invalid {power_type}: {power_name}\nUse +lookup {power_type} to browse or +lookup <power_name> for details. There are {len(valid_powers)} available."
        elif power_type == "embed":
            return False, f"Invalid embed: {power_name}\nUse +lookup embeds to browse embeds or +lookup <embed_name> for details. There are {len(valid_powers)} embeds available."
        elif power_type == "exploit":
            return False, f"Invalid exploit: {power_name}\nUse +lookup exploits to browse exploits or +lookup <exploit_name> for details. There are {len(valid_powers)} exploits available."
        elif power_type == "adaptation":
            return False, f"Invalid adaptation: {power_name}\nUse +lookup adaptations to browse adaptations or +lookup adaptations <name> for details. There are {len(valid_powers)} adaptations available."
        else:
            return False, f"Invalid {power_type}: {power_name}\nValid {power_type}s: {', '.join(sorted(valid_powers)[:10])}..."
    
    # Check template compatibility
    required_templates = get_template_requirements(power_type)
    if required_templates and character_template.lower() not in required_templates:
        return False, f"{power_type.title().replace('_', ' ')}s are only available to {', '.join(required_templates).title()} characters.\nYour template is: {character_template}"
    
    # Handle different power types
    if power_type == "key":
        # Keys go to geist stats for Sin-Eaters
        from world.cofd.templates.geist import initialize_geist_stats
        initialize_geist_stats(character)
        
        # Keys are known/unknown - semantic syntax means they have the key
        character.db.geist_stats["keys"][power_name.replace("_", " ")] = True
        return True, f"Set {character.name} to have the {power_name.replace('_', ' ').title()} key."
    
    elif power_type == "spell":
        # Spells are stored in powers with spell: prefix as "known"
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][f"spell:{power_name}"] = "known"
        
        # Get spell data to show more info
        spell_data = get_spell(power_name)
        if spell_data:
            arcana_name = spell_data['arcana'].title()
            spell_level = spell_data['level']
            dots_str = "●" * spell_level
            return True, f"Set {character.name} to know {spell_data['name']} ({arcana_name} {dots_str})."
        else:
            return True, f"Set {character.name} to know {power_name.replace('_', ' ').title()} (spell)."
    
    elif power_type == "endowment":
        # Endowments are stored in powers with endowment: prefix as "known"
        # Endowment keys use spaces, not underscores
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][f"endowment:{power_name}"] = "known"
        
        # Get endowment data to show more info
        from world.cofd.powers.hunter_endowments import get_endowment
        power_data = get_endowment(power_name)
        if power_data:
            cost_info = f" (Cost: {power_data['cost']})" if power_data.get('cost') else ""
            return True, f"Set {character.name} to know {power_data['name']} ({power_data['endowment_type'].replace('_', ' ').title()}){cost_info}."
        else:
            return True, f"Set {character.name} to know {power_name.title()} (endowment)."
    
    elif power_type in ["discipline_power", "devotion", "coil", "scale", "theban", "cruac", "gift", "contract"]:
        # Vampire-specific and werewolf-specific powers - store with prefixes for organization
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][f"{power_type}:{power_name}"] = "known"
        
        # Get power data for detailed feedback
        power_data = None
        display_type = ""
        
        if power_type == "discipline_power":
            from world.cofd.powers.vampire_disciplines import get_discipline_power
            power_data = get_discipline_power(power_name)
            display_type = "Discipline Power"
        elif power_type == "devotion":
            if power_name in ALL_DEVOTIONS:
                power_data = ALL_DEVOTIONS[power_name]
                display_type = "Devotion"
                
                # Check prerequisites for devotions
                meets_prereqs, error_msg = check_devotion_prerequisites(character, power_data)
                if not meets_prereqs:
                    return False, f"|rCannot learn {power_data.get('name', power_name)}:|n {error_msg}"
            else:
                display_type = "Devotion"
        elif power_type == "coil":
            if power_name in ALL_DISCIPLINE_POWERS:
                power_data = ALL_DISCIPLINE_POWERS[power_name]
            display_type = "Coil of the Dragon"
        elif power_type == "scale":
            if power_name in ALL_SCALES:
                power_data = ALL_SCALES[power_name]
            display_type = "Scale of the Dragon"
        elif power_type == "theban":
            if power_name in ALL_THEBAN:
                power_data = ALL_THEBAN[power_name]
            display_type = "Theban Sorcery"
        elif power_type == "cruac":
            if power_name in ALL_CRUAC:
                power_data = ALL_CRUAC[power_name]
            display_type = "Cruac Rite"
        elif power_type == "gift":
            if power_name in ALL_WEREWOLF_GIFTS:
                power_data = ALL_WEREWOLF_GIFTS[power_name]
            display_type = "Werewolf Gift"
        elif power_type == "contract":
            if power_name in ALL_CHANGELING_CONTRACTS:
                power_data = ALL_CHANGELING_CONTRACTS[power_name]
            display_type = "Changeling Contract"
        
        if power_data and 'name' in power_data:
            # Add renown info for gifts
            if power_type == "gift" and 'renown' in power_data:
                renown = power_data['renown'].title()
                return True, f"Set {character.name} to know {power_data['name']} ({renown} {display_type})."
            return True, f"Set {character.name} to know {power_data['name']} ({display_type})."
        else:
            return True, f"Set {character.name} to know {power_name.replace('_', ' ').title()} ({display_type})."
    
    elif power_type == "embed":
        # Embeds are stored in powers with embed: prefix as "known"
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][f"embed:{power_name}"] = "known"
        
        # Get embed data to show more info
        if power_name in ALL_EMBEDS:
            embed_data = ALL_EMBEDS[power_name]
            # Determine incarnation by checking which dict it's in
            from world.cofd.powers.demon_powers import EMBEDS_CACOPHONY, EMBEDS_INSTRUMENTAL, EMBEDS_MUNDANE, EMBEDS_VOCAL
            incarnation = "Unknown"
            if power_name in EMBEDS_CACOPHONY:
                incarnation = "Destroyer/Cacophony"
            elif power_name in EMBEDS_INSTRUMENTAL:
                incarnation = "Guardian/Instrumental"
            elif power_name in EMBEDS_MUNDANE:
                incarnation = "Psychopomp/Mundane"
            elif power_name in EMBEDS_VOCAL:
                incarnation = "Messenger/Vocal"
            return True, f"Set {character.name} to know {embed_data['name']} ({incarnation} Embed)."
        else:
            return True, f"Set {character.name} to know {power_name.replace('_', ' ').title()} (Embed)."
    
    elif power_type == "exploit":
        # Exploits are stored in powers with exploit: prefix as "known"
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][f"exploit:{power_name}"] = "known"
        
        # Get exploit data to show more info
        if power_name in DEMON_EXPLOITS:
            exploit_data = DEMON_EXPLOITS[power_name]
            prereq_info = f" (Prerequisite: {exploit_data['prerequisite']})" if exploit_data.get('prerequisite') else ""
            return True, f"Set {character.name} to know {exploit_data['name']} (Exploit){prereq_info}."
        else:
            return True, f"Set {character.name} to know {power_name.replace('_', ' ').title()} (Exploit)."
    
    elif power_type == "adaptation":
        # Adaptations are stored in powers as a dictionary to allow multiple adaptations
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        # Initialize adaptations dict if needed
        if "adaptations" not in character.db.stats["powers"]:
            character.db.stats["powers"]["adaptations"] = {}
        
        # Check if character already has this adaptation
        if power_name in character.db.stats["powers"]["adaptations"]:
            return False, f"{character.name} already has the {power_name.replace('_', ' ').title()} adaptation."
        
        # Add the adaptation
        character.db.stats["powers"]["adaptations"][power_name] = True
        
        # Get adaptation data to show more info
        adaptation_data = DEVIANT_ADAPTATIONS.get(power_name)
        if adaptation_data:
            category = adaptation_data.get('category', '')
            category_str = f" ({category})" if category else ""
            frequency = adaptation_data.get('frequency', '')
            freq_str = f" - {frequency}" if frequency else ""
            return True, f"Added {adaptation_data['name']}{category_str} to {character.name}{freq_str}."
        else:
            return True, f"Added {power_name.replace('_', ' ').title()} adaptation to {character.name}."
    
    elif power_type == "alembic":
        # Alembics are stored in powers with alembic: prefix as "known"
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][f"alembic:{power_name}"] = "known"
        power_display_name = power_name.replace('_', ' ').title()
        
        return True, f"Set {character.name} to know {power_display_name} (Alembic)."
    
    elif power_type == "bestowment":
        # Bestowments are stored in powers with bestowment: prefix as "known"
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][f"bestowment:{power_name}"] = "known"
        power_display_name = power_name.replace('_', ' ').title()
        
        return True, f"Set {character.name} to know {power_display_name} (Bestowment)."
    
    else:
        # Ceremonies, rites, rituals (legacy), contracts go to regular powers as known abilities (stored as 1)
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][power_name] = 1
        power_display_name = power_name.replace('_', ' ').title()
        
        return True, f"Set {character.name} to know {power_display_name} ({power_type})."

