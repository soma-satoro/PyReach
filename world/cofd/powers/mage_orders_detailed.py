"""
Mage: The Awakening Orders
Detailed order information for Chronicles of Darkness 2nd Edition.
Based on Mage: The Awakening 2nd Edition and supplements.
"""

# ============================================================================
# CONTEMPORARY ORDERS
# ============================================================================

CONTEMPORARY_ORDERS = {
    "adamantine_arrow": {
        "name": "Adamantine Arrow",
        "nickname": "Arrows",
        "creed": "Challenge is magical",
        "symbolism": "Attack and Defense",
        "rote_skills": ["Athletics", "Intimidation", "Medicine"],
        "description": "Warrior-mages who believe that conflict and struggle refine the soul and sharpen magical will",
        "book": "MTA 2e 36"
    },
    "guardians_of_the_veil": {
        "name": "Guardians of the Veil",
        "nickname": "Guardians",
        "creed": "Magic is fragile",
        "symbolism": "Concealing Identity",
        "rote_skills": ["Investigation", "Stealth", "Subterfuge"],
        "description": "Spies and protectors who guard the Mysteries from those who would exploit or expose them",
        "book": "MTA 2e 39"
    },
    "mysterium": {
        "name": "Mysterium",
        "nickname": "Mystagogues",
        "creed": "Magic is alive",
        "symbolism": "Knowledge",
        "rote_skills": ["Investigation", "Occult", "Survival"],
        "description": "Scholars and researchers dedicated to preserving and studying magical knowledge",
        "book": "MTA 2e 43"
    },
    "silver_ladder": {
        "name": "Silver Ladder",
        "nickname": "Thearchs",
        "creed": "Magic is humanity's birthright",
        "symbolism": "Authority",
        "rote_skills": ["Expression", "Persuasion", "Subterfuge"],
        "description": "Leaders who believe mages should guide humanity to Awakening and rule with enlightened authority",
        "book": "MTA 2e 46"
    },
    "council_of_free_assemblies": {
        "name": "Council of Free Assemblies",
        "nickname": "Libertines",
        "creed": "Humanity is magical",
        "symbolism": "Culture",
        "rote_skills": ["Crafts", "Persuasion", "Science"],
        "description": "Democratic mages who believe magic should serve and celebrate human diversity",
        "book": "MTA 2e 49"
    },
    "seers_of_the_throne": {
        "name": "Seers of the Throne",
        "nickname": "Seers",
        "creed": "Magic is payment",
        "symbolism": "Words of the Tyrants",
        "rote_skills": ["Investigation", "Occult", "Persuasion"],
        "description": "Servants of the Exarchs who enforce the Lie and maintain the sleeping world",
        "book": "MTA 2e 52"
    },
    "tremere": {
        "name": "Tremere",
        "nickname": "Hollowed",
        "creed": "Magic hungers",
        "symbolism": "Ephemeral and Physical Unity",
        "rote_skills": ["Empathy", "Occult", "Subterfuge"],
        "description": "Lich-mages who consume souls to sustain their immortal existence",
        "book": "NH-NA 126"
    },
}

# ============================================================================
# MINISTRY (SEERS OF THE THRONE)
# ============================================================================

MINISTRY_ORDERS = {
    "hegemony": {
        "name": "Hegemony",
        "crown": "Obligation",
        "creed": "The State is the soul",
        "iron_seal": "The Unity",
        "rote_skills": ["Empathy", "Persuasion", "Politics"],
        "description": "Seer ministry focused on social control and collective obligation",
        "book": "MTA 2e 72, 82"
    },
    "horologian": {
        "name": "Horologian",
        "crown": "Agency",
        "creed": "Routine is the opiate of the masses",
        "iron_seal": "The Prophet",
        "rote_skills": ["Intimidation", "Politics", "Socialize"],
        "description": "Seer ministry that disrupts patterns and routines",
        "book": "NH-NA 38"
    },
    "panopticon": {
        "name": "Panopticon",
        "crown": "Vision",
        "creed": "Vision is power",
        "iron_seal": "The Eye",
        "rote_skills": ["Investigation", "Stealth", "Subterfuge"],
        "description": "Seer ministry of surveillance and information gathering",
        "book": "MTA 2e 72, 82"
    },
    "paternoster": {
        "name": "Paternoster",
        "crown": "Doctrine",
        "creed": "Faith is an unbreakable chain",
        "iron_seal": "The Father",
        "rote_skills": ["Academics", "Expression", "Occult"],
        "description": "Seer ministry of religious control and ideological dominance",
        "book": "MTA 2e 72, 82"
    },
    "praetorian": {
        "name": "Praetorian",
        "crown": "Fury",
        "creed": "The weak fear the strong",
        "iron_seal": "The General",
        "rote_skills": ["Athletics", "Intimidation", "Larceny"],
        "description": "Seer ministry of military might and intimidation",
        "book": "MTA 2e 72, 82"
    },
    "geryon": {
        "name": "Geryon",
        "crown": "Secrecy",
        "creed": "Faceless powers rule unopposed",
        "iron_seal": "The Nemesis",
        "rote_skills": ["Larceny", "Socialize", "Subterfuge"],
        "description": "Seer ministry that operates in shadows and anonymity",
        "book": "DE2 301"
    },
}

# ============================================================================
# HISTORICAL ORDERS
# ============================================================================

HISTORICAL_ORDERS = {
    # Darshana (India) / Greek equivalent
    "jnanashakti": {
        "name": "Jnanashakti",
        "greek_name": "Gnostikon",
        "ethos": "The Wise study and preserve eternal truth",
        "symbolism": "Writing",
        "rote_skills": ["Crafts", "Occult", "Science"],
        "region": "India/Greece",
        "description": "Ancient order dedicated to preserving magical knowledge",
        "book": "DE 86"
    },
    "mahanizrayani": {
        "name": "Mahanizrayani",
        "greek_name": "Omphalos",
        "ethos": "The Wise shepherd souls spiritually",
        "symbolism": "Ceremony",
        "rote_skills": ["Academics", "Expression", "Persuasion"],
        "region": "India/Greece",
        "description": "Spiritual guides and ceremonial mages",
        "book": "DE 87"
    },
    "samashti": {
        "name": "Samashti",
        "greek_name": "Phulakeion",
        "ethos": "The Wise protect a fallen world",
        "symbolism": "Secrecy",
        "rote_skills": ["Investigation", "Stealth", "Subterfuge"],
        "region": "India/Greece",
        "description": "Protectors who guard the world through secrecy",
        "book": "DE 88"
    },
    "vajrastra": {
        "name": "Vajrastra",
        "greek_name": "Adamantine Arrow",
        "ethos": "The Wise pursue heroic achievements",
        "symbolism": "Weaponry",
        "rote_skills": ["Athletics", "Weaponry", "Intimidation"],
        "region": "India/Greece",
        "description": "Ancient precursor to the Adamantine Arrow",
        "book": "DE 88"
    },
    "ajivaki": {
        "name": "Ajivaki",
        "greek_name": "Living Sects",
        "ethos": "The Wise are not separate from the people",
        "symbolism": "Belief",
        "rote_skills": ["Expression + two others"],
        "region": "India/Greece",
        "description": "Populist mages who live among the people",
        "book": "DE 89"
    },
    "bay_city_marshals": {
        "name": "Bay City Marshals",
        "nickname": "Marshals",
        "creed": "Justice is magical",
        "symbolism": "Retaliation",
        "rote_skills": ["Empathy", "Firearms", "Investigation"],
        "era": "Historical",
        "description": "Law enforcement mages seeking magical justice",
        "book": "DE2 384"
    },
    "company_of_the_codex": {
        "name": "Company of the Codex",
        "nickname": "Picaroons",
        "creed": "Freedom is magical",
        "symbolism": "Discipline",
        "rote_skills": ["Firearms", "Intimidation", "Survival"],
        "era": "Historical",
        "description": "Freedom fighters and mercenaries",
        "book": "DE2 311"
    },
}

# ============================================================================
# COMBINED ORDER DATA
# ============================================================================

ALL_ORDERS_DETAILED = {
    **CONTEMPORARY_ORDERS,
    **MINISTRY_ORDERS,
    **HISTORICAL_ORDERS
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_order(order_name):
    """Get a specific order by name."""
    order_key = order_name.lower().replace(" ", "_")
    return ALL_ORDERS_DETAILED.get(order_key)

def get_all_orders_detailed():
    """Get all order data."""
    return ALL_ORDERS_DETAILED.copy()

def get_contemporary_orders():
    """Get contemporary Diamond orders."""
    return CONTEMPORARY_ORDERS.copy()

def get_ministry_orders():
    """Get Seer ministry orders."""
    return MINISTRY_ORDERS.copy()

def get_historical_orders():
    """Get historical orders."""
    return HISTORICAL_ORDERS.copy()

