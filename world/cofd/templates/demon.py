"""
Demon: The Descent Template Definition for Chronicles of Darkness.
Demons are fallen angels who have escaped from the God-Machine's control.
"""

from . import register_template
from world.cofd.powers.demon_form import (
    DEMON_MODIFICATIONS, DEMON_TECHNOLOGIES, DEMON_PROPULSIONS, DEMON_PROCESSES,
    ALL_DEMON_MODIFICATIONS, ALL_DEMON_TECHNOLOGIES, ALL_DEMON_PROPULSIONS, ALL_DEMON_PROCESSES
)
from world.cofd.powers.demon_powers import (
    ALL_EMBEDS, DEMON_EXPLOITS,
    EMBEDS_BY_INCARNATION, EMBEDS_CACOPHONY, EMBEDS_INSTRUMENTAL, EMBEDS_MUNDANE, EMBEDS_VOCAL,
    ALL_EMBED_NAMES, ALL_EXPLOIT_NAMES
)

# Valid demon incarnations
DEMON_INCARNATIONS = [
    "destroyer", "guardian", "messenger", "psychopomp"
]

# Valid demon agendas
DEMON_AGENDAS = [
    "inquisitor", "integrator", "saboteur", "tempter",
    "inquisitor-integrator", "inquisitor-saboteur", "inquisitor-tempter",
    "integrator-saboteur", "integrator-tempter",
    "saboteur-tempter"
]

# Valid demon catalysts
DEMON_CATALYSTS = [
    "abandonment", "betrayal", "destruction", "fear", "guilt", "memory", "withdrawal"
]

# Valid demon embeds (all embeds from all incarnations)
DEMON_EMBEDS = ALL_EMBED_NAMES

# Valid demon exploits (all exploits)
DEMON_EXPLOITS_LIST = ALL_EXPLOIT_NAMES

# Demon template definition
DEMON_TEMPLATE = {
    "name": "demon",
    "display_name": "Demon",
    "description": "Demons are fallen angels who have escaped from the God-Machine's control and now struggle to maintain their human identities.",
    "bio_fields": ["virtue", "vice", "incarnation", "agenda", "catalyst", "ring", "first_key"],
    "integrity_name": "Cover",
    "starting_integrity": 7,
    "multiple_integrity": True,  # Demons have multiple covers
    "supernatural_power_stat": "primum",
    "starting_power_stat": 1,
    "resource_pool": "aether",
    "power_systems": DEMON_EMBEDS + DEMON_EXPLOITS_LIST,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "demon"],
    "field_validations": {
        "incarnation": {
            "valid_values": DEMON_INCARNATIONS
        },
        "agenda": {
            "valid_values": DEMON_AGENDAS
        },
        "catalyst": {
            "valid_values": DEMON_CATALYSTS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Demon: The Descent",
    "notes": "Enhanced Demon template with Primum, Embeds, Exploits, and Aether pool"
}

# Register the template
register_template(DEMON_TEMPLATE)


# Power list helper functions
def get_primary_powers():
    """Get list of primary demon powers (embeds - known/unknown)."""
    # Return embed names with semantic prefix for storage
    return [f"embed:{embed}" for embed in DEMON_EMBEDS]


def get_secondary_powers():
    """Get list of secondary demon powers (exploits - known/unknown)."""
    # Return exploit names with semantic prefix for storage
    return [f"exploit:{exploit}" for exploit in DEMON_EXPLOITS_LIST]


# Sheet Rendering Functions
def render_demon_form_sheet(character, caller, force_ascii=False):
    """
    Render the Demon demonic form character sheet.
    
    Args:
        character: The character object with demon_form_stats
        caller: The caller (for messaging)
        force_ascii: If True, use ASCII dots instead of Unicode
        
    Returns:
        list: Lines of formatted output for the demon form sheet
    """
    from evennia.utils import ansi
    
    # Check if demon form stats exist
    if not hasattr(character.db, 'demon_form_stats') or not character.db.demon_form_stats:
        return None  # Signal that no demon form sheet exists
    
    demon_form_stats = character.db.demon_form_stats
    
    # Determine dot characters
    if force_ascii:
        filled_char, empty_char = "*", "-"
    else:
        filled_char, empty_char = "●", "○"
    
    from world.utils.formatting import sheet_section_header, footer

    def format_section_header(section_name):
        return sheet_section_header(section_name)

    # Build the demon form sheet display (theme colors for borders)
    output = []
    output.append(footer(78, char="="))
    form_concept = demon_form_stats.get("bio", {}).get("concept", f"{character.name}'s Apocalyptic Form")
    output.append(f"|y{form_concept.center(78)}|n")
    output.append(f"|y{'DEMONIC FORM'.center(78)}|n")
    output.append(footer(78, char="="))
    
    # Bio Section
    output.append(format_section_header("|wBIO|n"))
    
    bio = demon_form_stats.get("bio", {})
    
    # Bio data with defaults
    concept = bio.get("concept", "<not set>")
    description = bio.get("description", "<not set>")
    
    output.append(f"{'Concept':<15}: {concept}")
    if description != "<not set>":
        output.append(f"{'Description':<15}: {description}")
    output.append("")
    
    # Modifications Section (3 total at character creation)
    modifications = demon_form_stats.get("modifications", {})
    output.append(format_section_header("|wMODIFICATIONS|n"))
    output.append("|g(Permanent alterations - 3 at character creation)|n")
    
    modification_list = []
    for mod_key, mod_selected in modifications.items():
        if mod_selected:
            mod_data = DEMON_MODIFICATIONS.get(mod_key, {})
            if mod_data:
                modification_list.append({
                    'name': mod_data['name'],
                    'appearance': mod_data.get('appearance', ''),
                    'system': mod_data.get('system', ''),
                    'source': mod_data.get('source', '')
                })
    
    if modification_list:
        for i, mod in enumerate(modification_list, 1):
            output.append(f"|c{i}. {mod['name']}|n")
            output.append(f"   |yAppearance:|n {mod['appearance']}")
            output.append(f"   |ySystem:|n {mod['system']}")
            output.append(f"   |xSource:|n {mod['source']}")
            output.append("")
    else:
        output.append("  No modifications selected yet.")
        output.append("")
    
    # Technologies Section (2 total at character creation)
    technologies = demon_form_stats.get("technologies", {})
    output.append(format_section_header("|wTECHNOLOGIES|n"))
    output.append("|g(Must be activated - 2 at character creation)|n")
    
    technology_list = []
    for tech_key, tech_selected in technologies.items():
        if tech_selected:
            tech_data = DEMON_TECHNOLOGIES.get(tech_key, {})
            if tech_data:
                technology_list.append({
                    'name': tech_data['name'],
                    'appearance': tech_data.get('appearance', ''),
                    'system': tech_data.get('system', ''),
                    'source': tech_data.get('source', '')
                })
    
    if technology_list:
        for i, tech in enumerate(technology_list, 1):
            output.append(f"|c{i}. {tech['name']}|n")
            output.append(f"   |yAppearance:|n {tech['appearance']}")
            output.append(f"   |ySystem:|n {tech['system']}")
            output.append(f"   |xSource:|n {tech['source']}")
            output.append("")
    else:
        output.append("  No technologies selected yet.")
        output.append("")
    
    # Propulsion Section (1 total at character creation)
    propulsions = demon_form_stats.get("propulsions", {})
    output.append(format_section_header("|wPROPULSION|n"))
    output.append("|g(Movement ability - 1 at character creation)|n")
    
    propulsion_list = []
    for prop_key, prop_selected in propulsions.items():
        if prop_selected:
            prop_data = DEMON_PROPULSIONS.get(prop_key, {})
            if prop_data:
                propulsion_list.append({
                    'name': prop_data['name'],
                    'appearance': prop_data.get('appearance', ''),
                    'system': prop_data.get('system', ''),
                    'source': prop_data.get('source', '')
                })
    
    if propulsion_list:
        for i, prop in enumerate(propulsion_list, 1):
            output.append(f"|c{prop['name']}|n")
            output.append(f"   |yAppearance:|n {prop['appearance']}")
            output.append(f"   |ySystem:|n {prop['system']}")
            output.append(f"   |xSource:|n {prop['source']}")
            output.append("")
    else:
        output.append("  No propulsion selected yet.")
        output.append("")
    
    # Process Section (1 total at character creation)
    processes = demon_form_stats.get("processes", {})
    output.append(format_section_header("|wPROCESS|n"))
    output.append("|g(Complex activated ability - 1 at character creation)|n")
    
    process_list = []
    for proc_key, proc_selected in processes.items():
        if proc_selected:
            proc_data = DEMON_PROCESSES.get(proc_key, {})
            if proc_data:
                process_list.append({
                    'name': proc_data['name'],
                    'appearance': proc_data.get('appearance', ''),
                    'system': proc_data.get('system', ''),
                    'source': proc_data.get('source', '')
                })
    
    if process_list:
        for i, proc in enumerate(process_list, 1):
            output.append(f"|c{proc['name']}|n")
            output.append(f"   |yAppearance:|n {proc['appearance']}")
            output.append(f"   |ySystem:|n {proc['system']}")
            output.append(f"   |xSource:|n {proc['source']}")
            output.append("")
    else:
        output.append("  No process selected yet.")
        output.append("")
    
    output.append(footer(78, char="="))
    
    # Add encoding info to bottom if ASCII mode is being used
    if force_ascii:
        output.append("|g(ASCII mode active - use +sheet/demon without /ascii for Unicode)|n")
    
    return output


# Demon Form Stat Management Utilities
def initialize_demon_form_stats(character):
    """
    Initialize the demon form stats structure for a Demon character.
    
    Args:
        character: The character object
    """
    if not hasattr(character.db, 'demon_form_stats') or not character.db.demon_form_stats:
        character.db.demon_form_stats = {
            "bio": {},
            "modifications": {},
            "technologies": {},
            "propulsions": {},
            "processes": {}
        }


def set_demon_form_stat_value(character, stat, value, caller):
    """
    Set a demon form stat value with validation.
    
    Args:
        character: The character object
        stat: The stat name to set (modification, technology, propulsion, process, or bio field)
        value: The value to set (trait name or description)
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    # Initialize demon_form_stats if needed
    initialize_demon_form_stats(character)
    
    demon_form_stats = character.db.demon_form_stats
    
    # Handle different stat categories
    if stat == "modification":
        # Add a modification
        value_lower = value.lower().replace(" ", "_")
        
        # Check if it's a valid modification
        if value_lower not in DEMON_MODIFICATIONS:
            return False, f"Invalid modification: {value}. Use +lookup demon_modification to see available modifications."
        
        # Check if already at max (3 modifications)
        current_count = sum(1 for v in demon_form_stats["modifications"].values() if v)
        if current_count >= 3 and not demon_form_stats["modifications"].get(value_lower):
            return False, f"Cannot add modification. Already have 3 modifications (max at character creation)."
        
        # Add the modification
        demon_form_stats["modifications"][value_lower] = True
        mod_name = DEMON_MODIFICATIONS[value_lower]['name']
        return True, f"Added demonic form modification: {mod_name}"
    
    elif stat == "technology":
        # Add a technology
        value_lower = value.lower().replace(" ", "_")
        
        # Check if it's a valid technology
        if value_lower not in DEMON_TECHNOLOGIES:
            return False, f"Invalid technology: {value}. Use +lookup demon_technology to see available technologies."
        
        # Check if already at max (2 technologies)
        current_count = sum(1 for v in demon_form_stats["technologies"].values() if v)
        if current_count >= 2 and not demon_form_stats["technologies"].get(value_lower):
            return False, f"Cannot add technology. Already have 2 technologies (max at character creation)."
        
        # Add the technology
        demon_form_stats["technologies"][value_lower] = True
        tech_name = DEMON_TECHNOLOGIES[value_lower]['name']
        return True, f"Added demonic form technology: {tech_name}"
    
    elif stat == "propulsion":
        # Add a propulsion
        value_lower = value.lower().replace(" ", "_")
        
        # Check if it's a valid propulsion
        if value_lower not in DEMON_PROPULSIONS:
            return False, f"Invalid propulsion: {value}. Use +lookup demon_propulsion to see available propulsions."
        
        # Check if already have one (1 propulsion max)
        current_propulsions = [k for k, v in demon_form_stats["propulsions"].items() if v]
        if current_propulsions and value_lower not in current_propulsions:
            current_name = DEMON_PROPULSIONS[current_propulsions[0]]['name']
            return False, f"Cannot add propulsion. Already have {current_name} (max 1 at character creation). Remove it first with +stat/demon/remove propulsion={current_name}"
        
        # Add the propulsion
        demon_form_stats["propulsions"][value_lower] = True
        prop_name = DEMON_PROPULSIONS[value_lower]['name']
        return True, f"Added demonic form propulsion: {prop_name}"
    
    elif stat == "process":
        # Add a process
        value_lower = value.lower().replace(" ", "_")
        
        # Check if it's a valid process
        if value_lower not in DEMON_PROCESSES:
            return False, f"Invalid process: {value}. Use +lookup demon_process to see available processes."
        
        # Check if already have one (1 process max)
        current_processes = [k for k, v in demon_form_stats["processes"].items() if v]
        if current_processes and value_lower not in current_processes:
            current_name = DEMON_PROCESSES[current_processes[0]]['name']
            return False, f"Cannot add process. Already have {current_name} (max 1 at character creation). Remove it first with +stat/demon/remove process={current_name}"
        
        # Add the process
        demon_form_stats["processes"][value_lower] = True
        proc_name = DEMON_PROCESSES[value_lower]['name']
        return True, f"Added demonic form process: {proc_name}"
    
    elif stat in ["concept", "description"]:
        # Bio fields (string values)
        if len(str(value)) > 200:
            return False, "Demonic form bio fields cannot exceed 200 characters."
        
        demon_form_stats["bio"][stat] = str(value)
        return True, f"Set demonic form {stat} to: {value}"
    
    else:
        # Unknown stat
        error_msg = f"Unknown demon form stat: {stat}\n"
        error_msg += "Valid demon form stats:\n"
        error_msg += "  modification=<name> - Add a modification (max 3)\n"
        error_msg += "  technology=<name> - Add a technology (max 2)\n"
        error_msg += "  propulsion=<name> - Add a propulsion (max 1)\n"
        error_msg += "  process=<name> - Add a process (max 1)\n"
        error_msg += "  concept=<text> - Set form concept\n"
        error_msg += "  description=<text> - Set form description"
        return False, error_msg


def remove_demon_form_trait(character, trait_type, trait_name, caller):
    """
    Remove a demonic form trait.
    
    Args:
        character: The character object
        trait_type: The type of trait (modification, technology, propulsion, process)
        trait_name: The name of the trait to remove
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    # Initialize demon_form_stats if needed
    initialize_demon_form_stats(character)
    
    demon_form_stats = character.db.demon_form_stats
    trait_name_lower = trait_name.lower().replace(" ", "_")
    
    # Map trait types to their dictionaries and lookup sources
    trait_maps = {
        "modification": (demon_form_stats["modifications"], DEMON_MODIFICATIONS),
        "technology": (demon_form_stats["technologies"], DEMON_TECHNOLOGIES),
        "propulsion": (demon_form_stats["propulsions"], DEMON_PROPULSIONS),
        "process": (demon_form_stats["processes"], DEMON_PROCESSES)
    }
    
    if trait_type not in trait_maps:
        return False, f"Invalid trait type: {trait_type}. Valid types: modification, technology, propulsion, process"
    
    trait_dict, lookup_dict = trait_maps[trait_type]
    
    # Check if trait exists in lookup
    if trait_name_lower not in lookup_dict:
        return False, f"Invalid {trait_type}: {trait_name}"
    
    # Check if character has this trait
    if trait_name_lower not in trait_dict or not trait_dict[trait_name_lower]:
        return False, f"You don't have the {trait_type}: {lookup_dict[trait_name_lower]['name']}"
    
    # Remove the trait
    trait_dict[trait_name_lower] = False
    display_name = lookup_dict[trait_name_lower]['name']
    return True, f"Removed demonic form {trait_type}: {display_name}"


def get_demon_form_summary(character):
    """
    Get a summary of the character's demonic form.
    
    Args:
        character: The character object
        
    Returns:
        dict: Summary with counts and trait names
    """
    if not hasattr(character.db, 'demon_form_stats') or not character.db.demon_form_stats:
        return None
    
    demon_form_stats = character.db.demon_form_stats
    
    summary = {
        'modifications': [],
        'technologies': [],
        'propulsions': [],
        'processes': [],
        'counts': {
            'modifications': 0,
            'technologies': 0,
            'propulsions': 0,
            'processes': 0
        }
    }
    
    # Count and collect modifications
    for mod_key, selected in demon_form_stats.get("modifications", {}).items():
        if selected:
            summary['modifications'].append(DEMON_MODIFICATIONS[mod_key]['name'])
            summary['counts']['modifications'] += 1
    
    # Count and collect technologies
    for tech_key, selected in demon_form_stats.get("technologies", {}).items():
        if selected:
            summary['technologies'].append(DEMON_TECHNOLOGIES[tech_key]['name'])
            summary['counts']['technologies'] += 1
    
    # Count and collect propulsions
    for prop_key, selected in demon_form_stats.get("propulsions", {}).items():
        if selected:
            summary['propulsions'].append(DEMON_PROPULSIONS[prop_key]['name'])
            summary['counts']['propulsions'] += 1
    
    # Count and collect processes
    for proc_key, selected in demon_form_stats.get("processes", {}).items():
        if selected:
            summary['processes'].append(DEMON_PROCESSES[proc_key]['name'])
            summary['counts']['processes'] += 1
    
    return summary 