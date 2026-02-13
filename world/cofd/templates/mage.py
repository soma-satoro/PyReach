"""
Mage Template Definition for Chronicles of Darkness.
Mage: The Awakening template with Path and Order validations.
"""

from . import register_template

# Valid paths for Mage characters
MAGE_PATHS = [
    "acanthus", "mastigos", "moros", "obrimos", "thyrsus"
]

# Valid orders for Mage characters
MAGE_ORDERS = [
    # Contemporary Orders
    "adamantine_arrow", "guardians_of_the_veil", "mysterium", 
    "silver_ladder", "council_of_free_assemblies", "seers_of_the_throne", "tremere", "unaligned",
    # Ministry (Seers)
    "hegemony", "horologian", "panopticon", "paternoster", "praetorian", "geryon",
    # Historical Orders
    "jnanashakti", "mahanizrayani", "samashti", "vajrastra", "ajivaki",
    "bay_city_marshals", "company_of_the_codex",
    # Legacy compatibility
    "abyssal"
]

# Valid arcana for Mage characters (prefix conflicting names only)
MAGE_ARCANA = [
    "arcanum_death", "fate", "forces", "life", "matter", "mind", "prime", "space", "spirit", "time"
]

# Legacy mappings - legacies accessible by Path
LEGACIES_BY_PATH = {
    "acanthus": [
        "chronologue", "house of ariadne", "awakening gambit", "blank badge", 
        "carnival melancholy", "pygmalion society", "sisterhood of the blessed", 
        "storm keepers", "walkers in mists"
    ],
    "mastigos": [
        "intendants of the building", "logophages", "nagaraja", "reality stalkers",
        "bearers of the eternal voice", "bene ashmedai", "brotherhood of the demon wind",
        "clavicularius", "cryptologos", "parliament of the needle", "subtle ones"
    ],
    "moros": [
        "eleventh question", "kitchen alchemists", "nighthawks", "stone scribes",
        "bokor", "forge masters", "uncrowned kings", "votaries of the ordained", "legion"
    ],
    "obrimos": [
        "illumined path", "perfected adepts", "shapers of the invisible", "tyrian archons",
        "daksha", "echowalkers", "tamers of fire", "thrice-great", "transhuman engineers"
    ],
    "thyrsus": [
        "engineers of the system", "keepers of the covenant", "chrysalides", "dreamspeakers",
        "gilgamesh's lions", "orphans of proteus", "tamers of blood"
    ]
}

# Legacy mappings - legacies accessible by Order
LEGACIES_BY_ORDER = {
    "adamantine arrow": [
        "perfected adepts", "awakening gambit", "brotherhood of the demon wind",
        "devourers of the flesh", "hunters of the golden wing", "votaries of the ordained"
    ],
    "free council": [
        "blank badge", "cryptologos", "dreamspeakers", "parliament of the needle",
        "transhuman engineers"
    ],
    "guardians of the veil": [
        "eleventh question", "house of ariadne", "bearers of the eternal voice",
        "subtle ones", "votaries of the ordained", "legion"
    ],
    "mysterium": [
        "eleventh question", "logophages", "reality stalkers", "stone scribes",
        "cryptologos", "daksha", "walkers in mists"
    ],
    "silver ladder": [
        "illumined path", "keepers of the covenant", "logophages", "nighthawks",
        "bene ashmedai", "carnival melancholy", "clavicularius", "sisterhood of the blessed",
        "thrice-great"
    ],
    "seers of the throne": [
        "chronologue", "engineers of the system", "house of ariadne", "tyrian archons",
        "architects of the future", "bene ashmedai", "chrysalides", "clavicularius",
        "cryptologos", "secret order of the gate"
    ],
    "tremere": [
        "house nagaraja", "house seo hel", "house thrax", "house vedmak"
    ],
    "abyssal": [
        "hand of destiny", "keepers of the chrysalis"
    ]
}

# Unlinked legacies - accessible to anyone
UNLINKED_LEGACIES = [
    "archimandrite", "aurora auricalcinae", "bull's children", "celestial masters",
    "emergent", "fallen pillar", "filiae philosopharum", "hollow keepers",
    "lords of mars", "singers in silence", "skalds", "sphinxes", "tamers of the cave",
    "tamers of the winds", "tephra", "thread-cutters", "timori", "torches of artemis",
    "wind-singers"
]

# Import detailed legacy names for validation
from world.cofd.powers.mage_legacies_detailed import ALL_LEGACIES as DETAILED_LEGACY_DICT

# All valid legacies (for validation) - combine old list format with new detailed keys
ALL_LEGACIES = list(set(
    [legacy for legacies in LEGACIES_BY_PATH.values() for legacy in legacies] +
    [legacy for legacies in LEGACIES_BY_ORDER.values() for legacy in legacies] +
    UNLINKED_LEGACIES +
    list(DETAILED_LEGACY_DICT.keys())  # Add all keys from detailed legacies
))

# Mage template definition
MAGE_TEMPLATE = {
    "name": "mage",
    "display_name": "Mage",
    "description": ("Mages are awakened humans who can perceive and manipulate the underlying "
                   "structure of reality through magic. They are organized into Paths based on "
                   "their approach to magic and Orders based on their philosophical beliefs."),
    "bio_fields": ["virtue", "vice", "path", "order", "shadow_name", "cabal", "legacy"],
    "integrity_name": "Wisdom",
    "starting_integrity": 7,
    "supernatural_power_stat": "gnosis",
    "starting_power_stat": 1,
    "resource_pool": "mana",
    "power_systems": MAGE_ARCANA,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "mage"],
    "field_validations": {
        "path": {
            "valid_values": MAGE_PATHS
        },
        "order": {
            "valid_values": MAGE_ORDERS
        },
        "legacy": {
            "valid_values": ALL_LEGACIES,
            "custom_validation": "legacy"  # Flag for custom validation logic
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Mage: The Awakening",
    "notes": "Enhanced Mage template with Gnosis, Arcana, Mana pool, and Legacy system"
}

# Register the template
register_template(MAGE_TEMPLATE)


# Power list helper functions
def get_primary_powers():
    """Get list of primary mage powers (arcana rated 1-5)."""
    return MAGE_ARCANA.copy()


def get_secondary_powers():
    """Get list of secondary mage powers (none - mages only have arcana)."""
    return []


def get_all_powers():
    """Get all mage powers for validation."""
    return MAGE_ARCANA.copy()


# Mage Sheet Rendering Functions
def render_mage_sheet(character, caller, force_ascii=False):
    """
    Render the Mage-specific character sheet.
    
    Args:
        character: The character object with mage_stats
        caller: The calling object (for dot style detection)
        force_ascii: Whether to force ASCII display
        
    Returns:
        list: Lines of output for the mage sheet
    """
    # Helper function to format dots
    def format_dots(value, max_value=5):
        if force_ascii:
            filled = "*" * value
            empty = "-" * (max_value - value)
        else:
            filled = "●" * value
            empty = "○" * (max_value - value)
        return filled + empty
    
    from world.utils.formatting import sheet_section_header, footer

    def format_section_header(section_name):
        return sheet_section_header(section_name)

    # Initialize mage stats if needed (using shared function)
    initialize_mage_stats(character)
    
    mage_stats = character.db.mage_stats
    bio = character.db.stats.get("bio", {})
    other = character.db.stats.get("other", {})
    advantages = character.db.stats.get("advantages", {})
    
    # Build output (theme colors for borders)
    output = []
    output.append(footer(78, char="="))
    output.append(f"|y{character.name} - Mage Details|n".center(88))
    output.append(footer(78, char="="))
    
    # Basic Mage Info
    output.append(format_section_header("|wMAGE IDENTITY|n"))
    
    path = bio.get("path", "<not set>")
    order = bio.get("order", "<not set>")
    shadow_name = bio.get("shadow_name", "<not set>")
    cabal = bio.get("cabal", "<not set>")
    legacy = bio.get("legacy", "<not set>")
    gnosis = advantages.get("gnosis", 1)
    
    info_items = [
        ("Shadow Name", shadow_name),
        ("Path", path),
        ("Order", order),
        ("Legacy", legacy),
        ("Cabal", cabal),
        ("Gnosis", f"{gnosis} {format_dots(gnosis, gnosis)}")
    ]
    
    for i in range(0, len(info_items), 2):
        left_label, left_value = info_items[i]
        left_text = f"{left_label:<15}: {left_value}"
        
        if i + 1 < len(info_items):
            right_label, right_value = info_items[i + 1]
            right_text = f"{right_label:<15}: {right_value}"
        else:
            right_text = ""
        
        left_formatted = left_text.ljust(39)
        output.append(f"{left_formatted} {right_text}")
    
    # Dedicated Tool
    output.append(format_section_header("|wDEDICATED TOOL|n"))
    dedicated_tool = mage_stats.get("dedicated_tool", "<not set>")
    output.append(f"  {dedicated_tool}")
    
    # Only show help if not set
    if dedicated_tool == "<not set>":
        output.append("")
        output.append("|gYour dedicated magical tool synchronizes with your Nimbus.|n")
        output.append("|gSet with:|n +stat/mage dedicated_tool=<description>")
    
    # Nimbus
    output.append(format_section_header("|wNIMBUS|n"))
    
    immediate = mage_stats.get("immediate_nimbus", "<not set>")
    long_term = mage_stats.get("long_term_nimbus", "<not set>")
    signature = mage_stats.get("signature_nimbus", "<not set>")
    
    output.append("|cImmediate Nimbus:|n")
    output.append(f"  {immediate}")
    if immediate == "<not set>":
        output.append("|g  (Visible when casting spells, causes Nimbus Tilt based on Potency)|n")
    output.append("")
    
    output.append("|cLong-Term Nimbus:|n")
    output.append(f"  {long_term}")
    if long_term == "<not set>":
        output.append("|g  (Subtle coincidences around you based on your Path)|n")
    output.append("")
    
    output.append("|cSignature Nimbus:|n")
    output.append(f"  {signature}")
    if signature == "<not set>":
        output.append("|g  (Your magical signature left on spells, visible to Mage Sight, reflects a portion of what immediate nimbus looks like.)|n")
    
    # Only show command help if any nimbus is not set
    if immediate == "<not set>" or long_term == "<not set>" or signature == "<not set>":
        output.append("")
        if immediate == "<not set>":
            output.append("|gSet with:|n +stat/mage immediate_nimbus=<description>")
        if long_term == "<not set>":
            output.append("|gSet with:|n +stat/mage long_term_nimbus=<description>")
        if signature == "<not set>":
            output.append("|gSet with:|n +stat/mage signature_nimbus=<description>")
    
    # Obsessions
    output.append(format_section_header("|wOBSESSIONS|n"))
    
    obsessions = mage_stats.get("obsessions", [])
    if obsessions:
        for i, obsession in enumerate(obsessions, 1):
            if obsession:
                output.append(f"{i}. {obsession}")
    else:
        output.append("No obsessions set yet.")
    
    # Only show help if no obsessions or less than max (3)
    if len(obsessions) < 3:
        output.append("")
        output.append("|gObsessions are mage-specific goals tied to your magical practice.|n")
        output.append("|gMages can have up to 3 obsessions (1 short-term, 2 long-term).|n")
        output.append("|gSet with:|n +stat/mage obsession=<description>")
    
    # Praxes
    output.append(format_section_header("|wPRAXES|n"))
    
    praxes = mage_stats.get("praxes", [])
    if praxes:
        # Import spell data for display
        from world.cofd.powers.mage_spells import get_spell
        
        for praxis_key in sorted(praxes):
            spell_data = get_spell(praxis_key)
            if spell_data:
                spell_level = spell_data['level']
                arcana_dots = format_dots(spell_level, 5)
                arcana_name = spell_data['arcana'].title()
                output.append(f"  {spell_data['name']} ({arcana_name} {arcana_dots})")
            else:
                output.append(f"  {praxis_key.replace('_', ' ').title()} (Unknown Spell)")
    else:
        output.append("No praxes learned yet.")
    
    # Only show help if they have room for more praxes (or have none)
    if not praxes or len(praxes) < gnosis:
        output.append("")
        output.append(f"|gPraxes are spells you've mastered (exceptional success on 3 successes).|n")
        output.append(f"|gYou gain 1 free praxis per Gnosis dot, plus extras for 1 Arcane XP each.|n")
        output.append(f"|gCurrent Gnosis: {gnosis} = {gnosis} free praxis|n")
        output.append(f"|gSet with:|n +stat/mage praxis=<spell_name>")
    
    output.append(footer(78, char="="))
    
    return output


def initialize_mage_stats(character):
    """
    Initialize the mage stats structure for a Mage character.
    
    Args:
        character: The character object
    """
    if not hasattr(character.db, 'mage_stats') or not character.db.mage_stats:
        character.db.mage_stats = {
            "immediate_nimbus": "<not set>",
            "long_term_nimbus": "<not set>",
            "signature_nimbus": "<not set>",
            "obsessions": [],
            "praxes": [],
            "dedicated_tool": "<not set>"
        }


def set_mage_stat_value(character, stat, value, caller):
    """
    Set a mage stat value with validation.
    
    Args:
        character: The character object
        stat (str): The stat to set
        value: The value to set
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    # Initialize mage_stats if needed (like geist does)
    initialize_mage_stats(character)
    
    # Get reference to mage_stats for modification (like geist does)
    mage_stats = character.db.mage_stats
    
    # Handle different mage stats
    if stat in ["immediate_nimbus", "long_term_nimbus", "signature_nimbus", "dedicated_tool"]:
        # Text descriptions
        if len(value) > 200:
            return False, "Nimbus and tool descriptions cannot exceed 200 characters."
        
        # Modify through the reference (like geist does)
        mage_stats[stat] = value
        
        display_name = stat.replace('_', ' ').title()
        return True, f"Set {character.name}'s {display_name} to: {value}"
        
    elif stat == "obsession":
        # Add to obsessions list (max 3)
        current_obsessions = mage_stats.get("obsessions", [])
        
        if len(current_obsessions) >= 3:
            return False, "Mages can only have up to 3 obsessions (1 short-term, 2 long-term).\nRemove an obsession first or use +aspiration for general aspirations."
        
        # Modify through the reference (like geist does)
        mage_stats["obsessions"].append(value)
        
        return True, f"Added obsession {len(current_obsessions) + 1}: {value}"
        
    elif stat == "praxis":
        # Add a praxis (validate it's a real spell)
        from world.cofd.powers.mage_spells import get_spell
        
        spell_key = value.lower().replace(" ", "_")
        spell_data = get_spell(spell_key)
        
        if not spell_data:
            return False, f"'{value}' is not a valid spell.\nUse +lookup spells to browse available spells."
        
        current_praxes = mage_stats.get("praxes", [])
        
        # Check if already have this praxis
        if spell_key in current_praxes:
            return False, f"You already have {spell_data['name']} as a praxis."
        
        # Check gnosis limit and cost
        gnosis = character.db.stats.get("advantages", {}).get("gnosis", 1)
        free_praxes = gnosis
        
        # If buying beyond free praxes, need to spend 1 Arcane XP
        if len(current_praxes) >= free_praxes:
            # Check if character is approved
            if character.db.approved:
                # Need to spend Arcane XP
                exp_handler = character.experience
                if exp_handler.arcane_experience < 1:
                    return False, f"|rInsufficient Arcane Experience.|n\nYou have {len(current_praxes)} praxes and Gnosis {gnosis} (which gives {free_praxes} free praxes).\nAdditional praxes cost 1 Arcane XP each.\nYou have {exp_handler.arcane_experience} Arcane XP."
                
                # Spend the Arcane XP
                exp_handler.spend_arcane_experience(1)
                xp_message = f"\n|gSpent 1 Arcane XP.|n Remaining: {exp_handler.arcane_experience} Arcane XP"
            else:
                # Character not approved, just warn them
                xp_message = f"\n|yNote:|n You have {len(current_praxes)} praxes with Gnosis {gnosis}. You get {free_praxes} free praxes.\nOnce approved, additional praxes cost 1 Arcane Experience each."
        else:
            # Free praxis
            xp_message = f"\n|gFree praxis ({len(current_praxes) + 1}/{free_praxes} from Gnosis {gnosis})|n"
        
        # Modify through the reference (like geist does)
        mage_stats["praxes"].append(spell_key)
        
        spell_level = spell_data['level']
        arcana_name = spell_data['arcana'].title()
        dots_str = "●" * spell_level
        return True, f"Added praxis: {spell_data['name']} ({arcana_name} {dots_str}){xp_message}"
        
    else:
        return False, f"Unknown mage stat: {stat}\nValid stats: immediate_nimbus, long_term_nimbus, signature_nimbus, dedicated_tool, obsession, praxis" 