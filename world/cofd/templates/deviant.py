"""
Deviant: The Renegades Template Definition for Chronicles of Darkness.
Deviants are people transformed by conspiracies, escaped from laboratories and secret programs.
"""

from . import register_template
from world.cofd.powers.deviant_data import (
    ALL_VARIATIONS, ALL_SCARS, DEVIANT_FORMS,
    VARIATION_CATEGORIES, SCAR_ACTIVATION_TYPES, SCAR_ATTRIBUTES,
    DEVIANT_ORIGINS_DETAILED, DEVIANT_CLADES_DETAILED, DEVIANT_ADAPTATIONS,
    DEVIANT_ORIGIN_NAMES, DEVIANT_CLADE_NAMES, DEVIANT_ADAPTATION_NAMES,
    ADAPTATION_CATEGORIES
)

# Valid deviant origins
DEVIANT_ORIGINS = DEVIANT_ORIGIN_NAMES

# Valid deviant clades
DEVIANT_CLADES = DEVIANT_CLADE_NAMES

# Extract of variation and scar names for validation
DEVIANT_VARIATIONS = list(ALL_VARIATIONS.keys())
DEVIANT_SCARS = list(ALL_SCARS.keys())

# Deviant template definition
DEVIANT_TEMPLATE = {
    "name": "deviant",
    "display_name": "Deviant",
    "description": "Deviants are people who have been transformed by conspiracies and secret organizations, then escaped or been discarded.",
    "bio_fields": ["origin", "loyalty", "conviction", "clade", "forms", "conspiracy", "touchstone"],
    "integrity_name": "Stability",
    "starting_integrity": 7,
    "supernatural_power_stat": "acclimation",
    "starting_power_stat": 1,
    "resource_pool": "willpower",
    "power_systems": DEVIANT_VARIATIONS + DEVIANT_ADAPTATION_NAMES + DEVIANT_SCARS,
    "anchors": ["loyalty", "conviction"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "deviant"],
    "field_validations": {
        "origin": {
            "valid_values": DEVIANT_ORIGINS
        },
        "clade": {
            "valid_values": DEVIANT_CLADES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Deviant: The Renegades",
    "notes": "Deviant template with Deviation, Variations, Adaptations, and specialized mechanics"
}

# Register the template
register_template(DEVIANT_TEMPLATE)


# Sheet Rendering Functions
def render_deviant_sheet(character, caller, force_ascii=False):
    """
    Render the Deviant-specific sheet showing Variations and Scars.
    
    Args:
        character: The character object
        caller: The caller requesting the sheet
        force_ascii: Whether to force ASCII display
        
    Returns:
        List of formatted output lines or None if no deviant data
    """
    # Determine dot style
    filled_char = "*" if force_ascii else "●"
    empty_char = "-" if force_ascii else "○"
    
    output = []
    
    # Header
    output.append("|g" + "=" * 78 + "|n")
    output.append(f"|w{character.name}'s DEVIANT POWERS|n".center(78))
    output.append("|g" + "=" * 78 + "|n")
    output.append("")
    
    # Get deviant stats
    if not hasattr(character.db, 'stats'):
        return None
        
    stats = character.db.stats
    bio = stats.get("bio", {})
    other = stats.get("other", {})
    powers = stats.get("powers", {})
    
    # Deviant bio info
    clade = bio.get("clade", "<not set>")
    origin = bio.get("origin", "<not set>")
    
    # Get detailed info
    clade_data = DEVIANT_CLADES_DETAILED.get(clade.lower().replace(" ", "_"), {})
    origin_data = DEVIANT_ORIGINS_DETAILED.get(origin.lower().replace(" ", "_"), {})
    
    # Display Origin
    if origin_data:
        formal = origin_data.get("formal_name", origin.title())
        informal = origin_data.get("informal_name", "")
        anchor = origin_data.get("anchor", "")
        var_type = origin_data.get("variation_type", "")
        output.append(f"|wOrigin:|n {formal} ({informal}) - |cAnchor:|n {anchor}, |cVariations:|n {var_type}")
    else:
        output.append(f"|wOrigin:|n {origin.title()}")
    
    # Display Clade
    if clade_data:
        formal = clade_data.get("formal_name", clade.title())
        informal = clade_data.get("informal_name", "")
        output.append(f"|wClade:|n {formal} ({informal})")
    else:
        output.append(f"|wClade:|n {clade.title()}")
    
    output.append("")
    
    # Deviant power stats
    acclimation = other.get("acclimation", 0)
    loyalty = other.get("loyalty", 0)
    conviction = other.get("conviction", 0)
    
    output.append(f"|wAcclimation:|n {filled_char * acclimation}{empty_char * (5 - acclimation)}")
    output.append(f"|wLoyalty:|n {filled_char * loyalty}{empty_char * (10 - loyalty)}")
    output.append(f"|wConviction:|n {filled_char * conviction}{empty_char * (10 - conviction)}")
    output.append("")
    
    # Forms (if any)
    forms = bio.get("forms", [])
    if forms:
        output.append(_format_section_header("|wFORMS|n"))
        if isinstance(forms, list):
            for form in forms:
                form_data = DEVIANT_FORMS.get(form.lower().replace(" ", "_"), {})
                if form_data:
                    output.append(f"|c{form_data['name']}|n - {form_data['description']}")
                else:
                    output.append(f"|c{form.title()}|n")
        else:
            output.append(forms)
        output.append("")
    
    # Variations Section
    output.append(_format_section_header("|wVARIATIONS|n"))
    
    # Check both nested structure and flat structure for variations
    variations_nested = powers.get("variations", {})
    
    # Group by category
    universal_vars = []
    clade_vars = []
    found_variations = False
    
    # First check nested structure
    if variations_nested:
        for var_name, magnitude in variations_nested.items():
            if magnitude > 0:
                found_variations = True
                var_data = ALL_VARIATIONS.get(var_name.lower().replace(" ", "_"), {})
                category = var_data.get("category", "Unknown")
                
                # Format the variation display
                var_display = f"|c{var_data.get('name', var_name.replace('_', ' ').title())}|n"
                var_dots = filled_char * magnitude
                keywords = ", ".join(var_data.get("keywords", [])) if var_data else ""
                
                var_line = f"  {var_display:40} {var_dots:10} |w({keywords})|n"
                
                # Show ALL magnitude effects from 1 to current magnitude
                magnitude_effects = var_data.get("magnitude_effects", {})
                if magnitude_effects:
                    for mag_level in range(1, magnitude + 1):
                        if mag_level in magnitude_effects:
                            mag_dots = filled_char * mag_level + empty_char * (5 - mag_level)
                            var_line += f"\n    |y{mag_dots}|n {magnitude_effects[mag_level]}"
                
                if category == "Universal":
                    universal_vars.append(var_line)
                else:
                    clade_vars.append(var_line)
    
    # Then check flat structure in powers dict
    for power_name, power_value in powers.items():
        if power_name in ["variations", "scars", "adaptations"]:
            continue  # Skip the nested containers
        
        # Check if this is a variation
        var_data = ALL_VARIATIONS.get(power_name.lower().replace(" ", "_"), None)
        if var_data and isinstance(power_value, int) and power_value > 0:
            found_variations = True
            category = var_data.get("category", "Unknown")
            magnitude = power_value
            
            # Format the variation display
            var_display = f"|c{var_data.get('name', power_name.replace('_', ' ').title())}|n"
            var_dots = filled_char * magnitude
            keywords = ", ".join(var_data.get("keywords", [])) if var_data else ""
            
            var_line = f"  {var_display:40} {var_dots:10} |w({keywords})|n"
            
            # Show ALL magnitude effects from 1 to current magnitude
            magnitude_effects = var_data.get("magnitude_effects", {})
            if magnitude_effects:
                for mag_level in range(1, magnitude + 1):
                    if mag_level in magnitude_effects:
                        mag_dots = filled_char * mag_level + empty_char * (5 - mag_level)
                        var_line += f"\n    |y{mag_dots}|n {magnitude_effects[mag_level]}"
            
            if category == "Universal":
                universal_vars.append(var_line)
            else:
                clade_vars.append(var_line)
    
    if universal_vars:
        output.append("|yUniversal Variations:|n")
        output.extend(universal_vars)
        output.append("")
    
    if clade_vars:
        output.append(f"|y{clade.title()} Clade Variations:|n")
        output.extend(clade_vars)
        output.append("")
    
    if not found_variations:
        output.append("No variations purchased yet.")
        output.append("")
    
    # Scars Section
    output.append(_format_section_header("|wSCARS|n"))
    
    # Check both nested structure and flat structure for scars
    scars_nested = powers.get("scars", {})
    
    # Group by activation type
    controlled_scars = []
    involuntary_scars = []
    persistent_scars = []
    found_scars = False
    
    # First check nested structure
    if scars_nested:
        for scar_name, magnitude in scars_nested.items():
            if magnitude > 0:
                found_scars = True
                scar_data = ALL_SCARS.get(scar_name.lower().replace(" ", "_"), {})
                activation = scar_data.get("activation", "Unknown")
                
                # Format the scar display
                scar_display = f"|r{scar_data.get('name', scar_name.replace('_', ' ').title())}|n"
                scar_dots = filled_char * magnitude
                keywords = ", ".join(scar_data.get("keywords", [])) if scar_data else ""
                
                scar_line = f"  {scar_display:40} {scar_dots:10} |w({keywords})|n"
                
                # Show ALL magnitude effects from 1 to current magnitude
                magnitude_effects = scar_data.get("magnitude_effects", {})
                if magnitude_effects:
                    for mag_level in range(1, magnitude + 1):
                        if mag_level in magnitude_effects:
                            mag_dots = filled_char * mag_level + empty_char * (5 - mag_level)
                            scar_line += f"\n    |r{mag_dots}|n {magnitude_effects[mag_level]}"
                
                # Get entangled variations
                entangled_key = f"{scar_name}_entangled"
                entangled = powers.get(entangled_key, [])
                if entangled:
                    if isinstance(entangled, list):
                        entangled_str = ", ".join([v.replace("_", " ").title() for v in entangled])
                    else:
                        entangled_str = entangled.replace("_", " ").title()
                    scar_line += f"\n    |xEntangled with: {entangled_str}|n"
                
                if activation == "Controlled":
                    controlled_scars.append(scar_line)
                elif activation == "Involuntary":
                    involuntary_scars.append(scar_line)
                elif activation == "Persistent":
                    persistent_scars.append(scar_line)
    
    # Check flat structure in powers dict
    for power_name, power_value in powers.items():
        if power_name in ["variations", "scars", "adaptations"] or power_name.endswith("_entangled"):
            continue  # Skip the nested containers and entanglement markers
        
        # Check if this is a scar
        scar_data = ALL_SCARS.get(power_name.lower().replace(" ", "_"), None)
        if scar_data and isinstance(power_value, int) and power_value > 0:
            found_scars = True
            activation = scar_data.get("activation", "Unknown")
            magnitude = power_value
            
            # Format the scar display
            scar_display = f"|r{scar_data.get('name', power_name.replace('_', ' ').title())}|n"
            scar_dots = filled_char * magnitude
            keywords = ", ".join(scar_data.get("keywords", [])) if scar_data else ""
            
            scar_line = f"  {scar_display:40} {scar_dots:10} |w({keywords})|n"
            
            # Show ALL magnitude effects from 1 to current magnitude
            magnitude_effects = scar_data.get("magnitude_effects", {})
            if magnitude_effects:
                for mag_level in range(1, magnitude + 1):
                    if mag_level in magnitude_effects:
                        mag_dots = filled_char * mag_level + empty_char * (5 - mag_level)
                        scar_line += f"\n    |r{mag_dots}|n {magnitude_effects[mag_level]}"
            
            # Get entangled variations
            entangled_key = f"{power_name}_entangled"
            entangled = powers.get(entangled_key, [])
            if entangled:
                if isinstance(entangled, list):
                    entangled_str = ", ".join([v.replace("_", " ").title() for v in entangled])
                else:
                    entangled_str = entangled.replace("_", " ").title()
                scar_line += f"\n    |xEntangled with: {entangled_str}|n"
            
            if activation == "Controlled":
                controlled_scars.append(scar_line)
            elif activation == "Involuntary":
                involuntary_scars.append(scar_line)
            elif activation == "Persistent":
                persistent_scars.append(scar_line)
    
    # Also check 'other' dict for scars (legacy storage location)
    for stat_name, stat_value in other.items():
        if stat_name in ["template", "acclimation", "loyalty", "conviction", "size", "beats", "experience", "integrity"]:
            continue  # Skip known non-scar stats
        
        # Check if this might be a scar (look for underscore + common scar suffixes)
        potential_scar_name = stat_name.replace("_variation", "").replace("_scar", "")
        scar_data = ALL_SCARS.get(potential_scar_name.lower().replace(" ", "_"), None)
        
        if scar_data and isinstance(stat_value, int) and stat_value > 0:
            found_scars = True
            activation = scar_data.get("activation", "Unknown")
            magnitude = stat_value
            
            # Format the scar display
            scar_display = f"|r{scar_data.get('name', potential_scar_name.replace('_', ' ').title())}|n"
            scar_dots = filled_char * magnitude
            keywords = ", ".join(scar_data.get("keywords", [])) if scar_data else ""
            
            scar_line = f"  {scar_display:40} {scar_dots:10} |w({keywords})|n"
            
            # Show ALL magnitude effects from 1 to current magnitude
            magnitude_effects = scar_data.get("magnitude_effects", {})
            if magnitude_effects:
                for mag_level in range(1, magnitude + 1):
                    if mag_level in magnitude_effects:
                        mag_dots = filled_char * mag_level + empty_char * (5 - mag_level)
                        scar_line += f"\n    |r{mag_dots}|n {magnitude_effects[mag_level]}"
            
            # Get entangled variations
            entangled_key = f"{potential_scar_name}_entangled"
            entangled = powers.get(entangled_key, []) or other.get(entangled_key, [])
            if entangled:
                if isinstance(entangled, list):
                    entangled_str = ", ".join([v.replace("_", " ").title() for v in entangled])
                else:
                    entangled_str = entangled.replace("_", " ").title()
                scar_line += f"\n    |xEntangled with: {entangled_str}|n"
            
            if activation == "Controlled":
                controlled_scars.append(scar_line)
            elif activation == "Involuntary":
                involuntary_scars.append(scar_line)
            elif activation == "Persistent":
                persistent_scars.append(scar_line)
    
    if controlled_scars:
        output.append("|yControlled Scars:|n")
        output.extend(controlled_scars)
        output.append("")
    
    if involuntary_scars:
        output.append("|yInvoluntary Scars:|n")
        output.extend(involuntary_scars)
        output.append("")
    
    if persistent_scars:
        output.append("|yPersistent Scars:|n")
        output.extend(persistent_scars)
        output.append("")
    
    if not found_scars:
        output.append("No scars yet.")
        output.append("")
    
    # Adaptations Section
    output.append(_format_section_header("|wADAPTATIONS|n"))
    
    # Check both nested structure and flat structure for adaptations
    adaptations_nested = powers.get("adaptations", {})
    
    # Group by category
    universal_adaptations = []
    clade_adaptations = []
    found_adaptations = False
    adaptation_names = set()  # Track which adaptations we've already processed
    
    # First check nested structure (dictionary of adaptations)
    if adaptations_nested:
        for adapt_name in adaptations_nested:
            adaptation_names.add(adapt_name.lower().replace(" ", "_"))
            found_adaptations = True
            adapt_data = DEVIANT_ADAPTATIONS.get(adapt_name.lower().replace(" ", "_"), {})
            category = adapt_data.get("category", "Unknown")
            
            # Format the adaptation display
            adapt_display = f"|y{adapt_data.get('name', adapt_name.replace('_', ' ').title())}|n"
            description = adapt_data.get("description", "")
            frequency = adapt_data.get("frequency", "")
            cost = adapt_data.get("cost", "")
            
            cost_str = f" |r(Cost: {cost})|n" if cost else ""
            adapt_line = f"  {adapt_display} - {frequency}{cost_str}\n    {description}"
            
            if category == "Universal":
                universal_adaptations.append(adapt_line)
            else:
                clade_adaptations.append(adapt_line)
    
    # Check flat structure in powers dict
    for power_name, power_value in powers.items():
        if power_name in ["variations", "scars", "adaptations"] or power_name.endswith("_entangled"):
            continue  # Skip the nested containers and entanglement markers
        
        # Skip if already processed
        power_key = power_name.lower().replace(" ", "_")
        if power_key in adaptation_names:
            continue
        
        # Check if this is an adaptation
        adapt_data = DEVIANT_ADAPTATIONS.get(power_key, None)
        if adapt_data:
            adaptation_names.add(power_key)
            found_adaptations = True
            category = adapt_data.get("category", "Unknown")
            
            # Format the adaptation display
            adapt_display = f"|y{adapt_data.get('name', power_name.replace('_', ' ').title())}|n"
            description = adapt_data.get("description", "")
            frequency = adapt_data.get("frequency", "")
            cost = adapt_data.get("cost", "")
            
            cost_str = f" |r(Cost: {cost})|n" if cost else ""
            adapt_line = f"  {adapt_display} - {frequency}{cost_str}\n    {description}"
            
            if category == "Universal":
                universal_adaptations.append(adapt_line)
            else:
                clade_adaptations.append(adapt_line)
    
    # Also check 'other' dict for adaptations (legacy storage location)
    for stat_name, stat_value in other.items():
        if stat_name in ["template", "acclimation", "loyalty", "conviction", "size", "beats", "experience", "integrity"]:
            continue  # Skip known non-adaptation stats
        
        # Special case: if the key is literally "adaptation", the value is the adaptation name
        if stat_name.lower() == "adaptation" and isinstance(stat_value, str):
            adapt_name = stat_value.lower().replace(" ", "_")
            if adapt_name in adaptation_names:
                continue  # Already processed
            
            adapt_data = DEVIANT_ADAPTATIONS.get(adapt_name, None)
            if adapt_data:
                adaptation_names.add(adapt_name)
                found_adaptations = True
                category = adapt_data.get("category", "Unknown")
                
                # Format the adaptation display
                adapt_display = f"|y{adapt_data.get('name', stat_value.title())}|n"
                description = adapt_data.get("description", "")
                frequency = adapt_data.get("frequency", "")
                cost = adapt_data.get("cost", "")
                
                cost_str = f" |r(Cost: {cost})|n" if cost else ""
                adapt_line = f"  {adapt_display} - {frequency}{cost_str}\n    {description}"
                
                if category == "Universal":
                    universal_adaptations.append(adapt_line)
                else:
                    clade_adaptations.append(adapt_line)
            continue
        
        # Skip if already processed
        stat_key = stat_name.lower().replace(" ", "_")
        if stat_key in adaptation_names:
            continue
        
        # Check if this might be an adaptation
        adapt_data = DEVIANT_ADAPTATIONS.get(stat_key, None)
        
        if adapt_data:
            adaptation_names.add(stat_key)
            found_adaptations = True
            category = adapt_data.get("category", "Unknown")
            
            # Format the adaptation display
            adapt_display = f"|y{adapt_data.get('name', stat_name.replace('_', ' ').title())}|n"
            description = adapt_data.get("description", "")
            frequency = adapt_data.get("frequency", "")
            cost = adapt_data.get("cost", "")
            
            cost_str = f" |r(Cost: {cost})|n" if cost else ""
            adapt_line = f"  {adapt_display} - {frequency}{cost_str}\n    {description}"
            
            if category == "Universal":
                universal_adaptations.append(adapt_line)
            else:
                clade_adaptations.append(adapt_line)
    
    if universal_adaptations:
        output.append("|yUniversal Adaptations:|n")
        output.extend(universal_adaptations)
        output.append("")
    
    if clade_adaptations:
        output.append(f"|y{clade.title()} Clade Adaptations:|n")
        output.extend(clade_adaptations)
        output.append("")
    
    if not found_adaptations:
        output.append("No adaptations purchased yet.")
        output.append("")
    
    # Scar Power/Finesse/Resistance calculation hint
    output.append("|gScar Traits are calculated from associated Attributes:|n")
    output.append("|xMental:|n Intelligence (Power), Wits (Finesse), Resolve (Resistance)")
    output.append("|xPhysical:|n Strength (Power), Dexterity (Finesse), Stamina (Resistance)")
    output.append("|xSocial:|n Presence (Power), Manipulation (Finesse), Composure (Resistance)")
    output.append("")
    
    output.append("|gUse +lookup variation=<name> or +lookup scar=<name> for details|n")
    output.append("|g" + "=" * 78 + "|n")
    
    return output


def _format_section_header(section_name):
    """Create an arrow-style section header"""
    total_width = 78
    name_length = len(section_name) - 6  # Account for ANSI codes
    available_dash_space = total_width - name_length - 4
    
    left_dashes = available_dash_space // 2
    right_dashes = available_dash_space - left_dashes
    
    return f"|g<{'-' * left_dashes}|n {section_name} |g{'-' * right_dashes}>|n" 