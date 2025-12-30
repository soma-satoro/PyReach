"""
Mortal+ Template Definition for Chronicles of Darkness 2nd Edition.
Mortals with supernatural abilities - comprehensive list of all minor templates.
Based on Codex of Darkness: https://codexofdarkness.com/wiki/Mortals_and_Lesser_Templates
"""

from . import register_template

# Core Chronicles of Darkness 2e mortal+ types (General Character Types)
CORE_MORTAL_PLUS = [
    "Atariya",           # Spirit-touched with connection to the Shadow
    "Changing Breeds",   # Minor shapeshifters (not Uratha)
    "Dreamer",           # Those who walk in dreams
    "Infected",          # Carriers of supernatural diseases
    "Lost Boy",          # Children who never grew up
    "Plain",             # Seemingly normal but with hidden depths
    "Psychic",           # Humans with psychic abilities
    "Psychic Vampire",   # Those who feed on life force
    "Skinthief",         # Shapeshifters who steal skins
]

# Vampire: The Requiem related (Associated Character Types)
VAMPIRE_MORTAL_PLUS = [
    "Ghoul",    # Blood-bound servants with Disciplines
    "Dhampir"   # Half-vampire offspring
]

# Werewolf: The Forsaken related (Associated Character Types)
WEREWOLF_MORTAL_PLUS = [
    "Wolf-Blooded",  # Descendants of werewolves with Tells
    "Host"           # Possessed by spirits with Dread Powers
]

# Mage: The Awakening related (Associated Character Types)
MAGE_MORTAL_PLUS = [
    "Sleepwalker",  # Mortals who can witness magic
    "Proximus"      # Bloodlines with innate magical abilities
]

# Changeling: The Lost related (Associated Character Types)
CHANGELING_MORTAL_PLUS = [
    "Fae-Touched"  # Mortals touched by the Fae
]

# Mummy: The Curse related (Associated Character Types)
MUMMY_MORTAL_PLUS = [
    "Immortal"  # Humans who achieved immortality through various means
]

# Demon: The Descent related (Associated Character Types)
DEMON_MORTAL_PLUS = [
    "Demon-Blooded",  # Offspring or touched by demons
    "Stigmatic"       # Marked by the God-Machine
]

# All mortal+ types combined (2nd Edition only)
ALL_MORTAL_PLUS_TYPES = (
    CORE_MORTAL_PLUS + 
    VAMPIRE_MORTAL_PLUS + 
    WEREWOLF_MORTAL_PLUS + 
    MAGE_MORTAL_PLUS + 
    CHANGELING_MORTAL_PLUS + 
    MUMMY_MORTAL_PLUS + 
    DEMON_MORTAL_PLUS
)

# Psychic power types (for Psychics - 2e Supernatural Merits)
# Based on Chronicles of Darkness 2e core book
PSYCHIC_POWERS = [
    "aura_reading",      # See supernatural auras
    "clairvoyance",      # Remote viewing
    "mind_reading",      # Read surface thoughts
    "psychokinesis",     # Move objects with mind
    "psychometry",       # Read object histories
    "telepathy",         # Mental communication
    "precognition",      # See future events
    "medium",            # Communicate with ghosts
    "biokinesis",        # Control biological functions
    "telekinesis"        # Advanced psychokinesis
]

# Demon-blooded levels (2e)
DEMON_BLOODED_LEVELS = [
    "latent",      # Dormant abilities
    "offspring",   # Direct demon parentage
    "fractal"      # God-Machine touched
]

# Wolf-Blooded Tell categories (2e)
WOLF_BLOODED_TELLS = [
    "moon_gift",         # Powers tied to moon phases
    "pack_awareness",    # Sense other Wolf-Blooded
    "territorial",       # Enhanced in claimed territory
    "spirit_sight",      # See into Shadow
    "primal"            # Enhanced physical traits
]

PROXIMUS_FAMILIES = [
    "benedetto",    # Mastigos, Provincial Italian occultists bonded with something in the land.
    "essers",       # Thyrsus, Specialists in harnessing the soul, with loosened souls of their own.
    "myrmidons",    # Obrimos, Muscular warrior slaves concealing insectile mutations.
    "sisters of the mountain" # Thyrsus, Appalachian folk witches with faint signs of plant life beneath the skin.
]

# Game line heritage (for tracking mortal+ origin)
GAME_LINE_HERITAGE = [
    "vampire", "werewolf", "mage", "changeling", "hunter", "promethean",
    "geist", "mummy", "demon", "deviant", "core", "none"
]

# Get mage spells for Sleepwalkers/Proximus
try:
    from world.cofd.powers.mage_spells import SLEEPWALKER_SPELLS, PROXIMUS_SPELLS
    MORTAL_PLUS_SPELL_ACCESS = PROXIMUS_SPELLS  # Use Proximus list (1-3 dot) for validation
except ImportError:
    MORTAL_PLUS_SPELL_ACCESS = []

# Get Wolf-Blooded Tells (detailed list)
try:
    from world.cofd.powers.mortalplus_abilities import ALL_TELLS as DETAILED_TELLS
except ImportError:
    DETAILED_TELLS = []

# Combine old generic categories with new detailed tells for validation
ALL_WOLF_BLOODED_TELLS = WOLF_BLOODED_TELLS + DETAILED_TELLS

# Mortal+ template definition (2nd Edition)
MORTAL_PLUS_TEMPLATE = {
    "name": "mortal_plus",
    "display_name": "Mortal+",
    "description": ("Mortals with supernatural abilities - psychics, witches, wolf-blooded, sleepwalkers, ghouls, "
                   "and many other minor supernatural templates from Chronicles of Darkness 2nd Edition. "
                   "See: https://codexofdarkness.com/wiki/Mortals_and_Lesser_Templates"),
    "bio_fields": ["virtue", "vice", "template_type", "subtype", "organization", "profession"],
    "integrity_name": "Integrity",
    "starting_integrity": 7,
    "supernatural_power_stat": None,
    "starting_power_stat": None,
    "resource_pool": "willpower",
    "power_systems": PSYCHIC_POWERS + MORTAL_PLUS_SPELL_ACCESS,  # 2e: Psychic, and Spells
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "minor_template"],
    "field_validations": {
        "template_type": {
            "valid_values": ALL_MORTAL_PLUS_TYPES,
            "description": "Primary mortal+ template type"
        },
        "subtype": {
            "valid_values": ALL_WOLF_BLOODED_TELLS + DEMON_BLOODED_LEVELS + PROXIMUS_FAMILIES,
            "description": "Specific variant or subtype (optional)"
        },
        "game_line": {
            "valid_values": GAME_LINE_HERITAGE,
            "description": "Associated game line or origin"
        },
    },
    "version": "2.0",
    "author": "Chronicles of Darkness 2nd Edition",
    "game_line": "Chronicles of Darkness Core",
    "notes": ("2nd Edition Mortal+ template. Includes psychic powers and spells. ")
}

# Register the template
register_template(MORTAL_PLUS_TEMPLATE) 