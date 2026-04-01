"""
Changeling Template Definition for Chronicles of Darkness.
Changeling: The Lost template with Seeming, Court, and Kith validations.
"""

from . import register_template
from world.cofd.powers.changeling_contracts import get_all_contracts

# Valid seemings for Changeling characters
CHANGELING_SEEMINGS = [
    "beast", "darkling", "elemental", "fairest", "ogre", "wizened"
]

# Valid courts for Changeling characters  
CHANGELING_COURTS = [
    "spring", "summer", "autumn", "winter", "courtless",
    "morning", "day", "night", "barter", "coins", "favors", "shady_deals",
    "high_tide", "low_tide", "flood_tide", "ebb_tide"
]

# Valid kiths for Changeling characters (2nd Edition)
CHANGELING_KITHS = [
    # Base Changeling: The Lost 2nd Edition kiths
    "artist", "bright_one", "chatelaine", "gristlegrinder", "helldiver", "hunterheart", 
    "leechfinger", "mirrorskin", "nightsinger", "notary", "playmate", "snowskin",
    
    # Kith & Kin - Crown kiths
    "absinthial", "climacteric", "concubus", "draconic", "flowering", "ghostheart", 
    "moonborn", "uttervoice",
    
    # Kith & Kin - Jewels kiths
    "delver", "glimmerwisp", "manikin", "oculus", "polychromatic", "veneficus", "witchtooth",
    
    # Kith & Kin - Mirror kiths
    "bricoleur", "cloakskin", "doppelganger", "lethipomp", "lullescent", "riddleseeker", 
    "sideromancer", "spiegelbild",
    
    # Kith & Kin - Shield kiths
    "asclepian", "bridgeguard", "librorum", "liminal", "reborn", "stoneflesh", "wisewitch",
    
    # Kith & Kin - Steed kiths
    "airtouched", "chalomot", "chevalier", "farwalker", "flickerflash", "levinquick", 
    "swarmflight", "swimmerskin",
    
    # Kith & Kin - Sword kiths
    "bearskin", "beastcaller", "cyclopean", "plaguesmith", "razorhand", "sandharrowed", 
    "valkyrie", "venombite",
    
    # Kith & Kin - Additional kiths
    "apoptosome", "becquerel", "blightbent", "enkrateia", "gravewight", "shadowsoul", 
    "telluric", "whisperwisp",
    
    # Dark Eras 2 kiths
    "nymph", "dryad", "cleverquick"
]

# Valid entitlements for Changeling characters
CHANGELING_ENTITLEMENTS = [ 
    "Baron of the Lesser Ones", "Dauphines of Wayward Children", "Master of Keys", "Modiste of Elfhame", "Thorn Dancer", "Sibylline Fishers", "Spiderborn Riders"
]

# Valid changeling contracts (2e + project homebrew extensions).
# Keep this synced automatically with the authoritative contracts registry.
CHANGELING_CONTRACTS = sorted(get_all_contracts().keys())

# Changeling template definition
CHANGELING_TEMPLATE = {
    "name": "changeling",
    "display_name": "Changeling", 
    "description": ("Changelings are humans who were taken to the realm of the True Fae and "
                   "transformed, eventually escaping back to the mortal world. They are organized "
                   "by their Seemings (what they became) and Courts (seasonal affiliations)."),
    "bio_fields": ["needle", "thread", "seeming", "court", "kith", "keeper", "motley", "entitlement"],
    "integrity_name": "Clarity",
    "starting_integrity": 7,
    "supernatural_power_stat": "wyrd",
    "starting_power_stat": 1,
    "resource_pool": "glamour",
    "power_systems": CHANGELING_CONTRACTS,
    "anchors": ["needle", "thread"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "changeling"],
    "field_validations": {
        "seeming": {
            "valid_values": CHANGELING_SEEMINGS
        },
        "court": {
            "valid_values": CHANGELING_COURTS
        },
        "kith": {
            "valid_values": CHANGELING_KITHS
        },
        "entitlement": {
            "valid_values": CHANGELING_ENTITLEMENTS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Changeling: The Lost",
    "notes": "Enhanced Changeling template with Wyrd, Contracts, and Glamour pool"
}

# Register the template
register_template(CHANGELING_TEMPLATE)


# Power list helper functions
def get_primary_powers():
    """Get list of primary changeling powers (contracts - individual abilities)."""
    return CHANGELING_CONTRACTS.copy()


def get_secondary_powers():
    """Get list of secondary changeling powers (none - all powers are contracts)."""
    return []


def get_all_powers():
    """Get all changeling powers for validation."""
    return CHANGELING_CONTRACTS.copy() 