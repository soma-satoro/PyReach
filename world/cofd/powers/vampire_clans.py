"""
Vampire: The Requiem Clans and Bloodlines
Detailed clan and bloodline information for Chronicles of Darkness 2nd Edition.
Based on Vampire: The Requiem 2nd Edition and supplemental materials.
"""

# ============================================================================
# MAJOR CLANS
# ============================================================================

MAJOR_CLANS = {
    "daeva": {
        "name": "Daeva",
        "nickname": "Serpents",
        "disciplines": ["Celerity", "Majesty", "Vigor"],
        "bonus_trait": "Dexterity or Manipulation",
        "weakness": "Feeding again on a previous vessel rolls Humanity to avoid compulsive dependence.",
        "description": "The Serpents are creatures of passion and vice, moving through mortal society like predatory aristocrats",
        "book": "VTR 2e 15, 103"
    },
    "gangrel": {
        "name": "Gangrel",
        "nickname": "Savages",
        "disciplines": ["Animalism", "Protean", "Resilience"],
        "bonus_trait": "Composure or Stamina",
        "weakness": "Cap rolls to resist frenzy by your Humanity.",
        "description": "The Savages are feral hunters who embrace their bestial nature",
        "book": "VTR 2e 19, 103"
    },
    "mekhet": {
        "name": "Mekhet",
        "nickname": "Shadows",
        "disciplines": ["Auspex", "Celerity", "Obfuscate"],
        "bonus_trait": "Intelligence or Wits",
        "weakness": "Choose a permanent bane. Banes treat Humanity as one dot lower.",
        "description": "The Shadows are information brokers and occult scholars who thrive in darkness",
        "book": "VTR 2e 22, 103"
    },
    "nosferatu": {
        "name": "Nosferatu",
        "nickname": "Haunts",
        "disciplines": ["Nightmare", "Obfuscate", "Vigor"],
        "bonus_trait": "Composure or Strength",
        "weakness": "Social penalties with non-Touchstone humans treat Humanity as one dot lower, and such rolls, when failed, become dramatic failures.",
        "description": "The Haunts are twisted monsters who inspire terror and dread",
        "book": "VTR 2e 24, 103"
    },
    "ventrue": {
        "name": "Ventrue",
        "nickname": "Lords",
        "disciplines": ["Animalism", "Dominate", "Resilience"],
        "bonus_trait": "Presence or Resolve",
        "weakness": "Touchstones proceed down from Humanity 7, not 6.",
        "description": "The Lords are regal predators who rule through dominance and control",
        "book": "VTR 2e 28, 103"
    },
}

# ============================================================================
# UNCOMMON AND LOST CLANS
# ============================================================================

UNCOMMON_CLANS = {
    "akhud": {
        "name": "Akhud",
        "nickname": "Ahranites",
        "disciplines": ["Celerity", "Praestantia", "Obfuscate"],
        "bonus_trait": "Strength or Wits",
        "weakness": "Half of (10-Humanity) as penalty to actions that harm fellow Akhud and others with blood ties/Vincula.",
        "description": "Ancient Persian vampires bound by blood and honor",
        "book": "TY 28"
    },
    "amari": {
        "name": "Amari",
        "nickname": "Winter Kings",
        "disciplines": ["Obfuscate", "Protean", "Resilience"],
        "bonus_trait": "Manipulation or Stamina",
        "weakness": "(10 - Humanity) penalty to resist frenzy due to fire and sunlight.",
        "description": "Siberian vampires adapted to the frozen wastes",
        "book": "NH:SB 77"
    },
    "bekaak": {
        "name": "Bekaak",
        "nickname": "Prophets",
        "disciplines": ["Animalism", "Obfuscate", "Vitiate"],
        "bonus_trait": "Composure or Presence",
        "weakness": "Base rolls to lie to mortals of higher Integrity are capped by Humanity unless character spends Willpower.",
        "description": "North African vampires bound by truth",
        "book": "NH:SB 86"
    },
    "dukhan": {
        "name": "Dukhan",
        "nickname": "Incubi",
        "disciplines": ["Auspex", "Obfuscate", "Protean"],
        "bonus_trait": "Stamina or Wits",
        "weakness": "Grow Languid after (Humanity) nights without dwelling within the Dream.",
        "description": "Dream-dwelling vampires from Central Asia",
        "book": "DE2 141"
    },
    "hypatians": {
        "name": "Hypatians",
        "nickname": "Blights",
        "disciplines": ["Animalism", "Nightmare", "Resilience"],
        "bonus_trait": "Resolve or Stamina",
        "weakness": "Humans become increasingly distrustful after failed (Humanity - Composure) rolls.",
        "description": "Scholarly vampires cursed with distrust",
        "book": "NH:SB 90"
    },
    "jiang_shi": {
        "name": "Jiang Shi",
        "nickname": "Phantoms",
        "disciplines": ["Animalism", "Celerity", "Obfuscate"],
        "bonus_trait": "Dexterity or Intelligence",
        "weakness": "Can't inflict Conditions through the Kiss.",
        "description": "Hopping corpses from East Asia",
        "book": "VTR 2e 255"
    },
    "julii": {
        "name": "Julii",
        "nickname": "--",
        "disciplines": ["Dominate", "Resilience", "Vigor"],
        "bonus_trait": "Composure or Presence",
        "weakness": "Supernatural resistance against Strix and ephemera is capped by Humanity.",
        "description": "Roman vampires vulnerable to spirits",
        "book": "TY 30"
    },
    "mekhet_hollow": {
        "name": "Mekhet (Hollow)",
        "nickname": "Shadows",
        "disciplines": ["Auspex", "Celerity", "Obfuscate"],
        "bonus_trait": "Intelligence or Wits",
        "weakness": "Haunted by your own resentful ghost.",
        "description": "Mekhet haunted by their own ghosts",
        "book": "TY 29"
    },
    "mikhaili": {
        "name": "Mikhaili",
        "nickname": "Winter Kings",
        "disciplines": ["Animalism", "Bereschligost", "Resilience"],
        "bonus_trait": "Manipulation or Stamina",
        "weakness": "Fall torpid each summer. Embrace produces revenants.",
        "description": "Slavic vampires tied to winter",
        "book": "HD 53"
    },
    "nhang": {
        "name": "Nhang",
        "nickname": "Water Serpents",
        "disciplines": ["Celerity", "Protean", "Resilience"],
        "bonus_trait": "Stamina or Wits",
        "weakness": "Bodies become brittle on dry land if not enough Vitae in system.",
        "description": "Aquatic vampires from Southeast Asia",
        "book": "NH:SB 94"
    },
    "pijavica": {
        "name": "Pijavica",
        "nickname": "--",
        "disciplines": ["Animalism", "Protean", "Resilience"],
        "bonus_trait": "Stamina or Wits",
        "weakness": "Physical Attributes wither with Blood Potency above 7, and Mental and Social Attributes wither below 4.",
        "description": "Balkan vampires cursed with withering",
        "book": "TY 30"
    },
    "twice_cursed": {
        "name": "Twice-Cursed",
        "nickname": "Stalkers",
        "disciplines": ["Celerity", "Obfuscate", "Vigor"],
        "bonus_trait": "Dexterity and Strength",
        "weakness": "Gain both Daeva and Nosferatu banes.",
        "description": "Doubly cursed vampires bearing two clan weaknesses",
        "book": "NH:SB 102"
    },
}

# ============================================================================
# BLOODLINES
# ============================================================================

ALL_BLOODLINES = {
    # Cross-Clan Bloodlines
    "neglatu": {
        "name": "Neglatu",
        "parent_clan": "Any",
        "description": "Uplifted revenants with an affinity for their former kind.",
        "disciplines": "As uplifted clan",
        "gifts": "Agah",
        "bane": "Cannot use the blood bond",
        "book": "Onyx Path blog"
    },
    "parliamentarians": {
        "name": "Parliamentarians",
        "parent_clan": "Carthian",
        "description": "Tedious, browbeating Carthians who religiously adhere to the party line.",
        "disciplines": ["Animalism", "Auspex", "Celerity", "Majesty"],
        "gifts": "Bloodline Merits",
        "bane": "Cap Social dice pools by Humanity when conventional order is broken",
        "book": "NH-SB 33"
    },
    "penumbrae": {
        "name": "Penumbrae",
        "parent_clan": "Circle of the Crone",
        "description": "Acolyte psychonauts who read visions in the skein of the Blood.",
        "disciplines": ["Auspex", "Celerity", "Crúac", "Vigor"],
        "gifts": "Crúac Rites",
        "bane": "Dots of Crúac deepen states of torpor",
        "book": "NH-SB 37"
    },
    "scions_of_the_first_city": {
        "name": "Scions of the First City",
        "parent_clan": "Various",
        "description": "Urban mystics who see through the eyes of their city.",
        "disciplines": ["Animalism", "Auspex", "Obfuscate", "Resilience"],
        "gifts": "Bloodline Devotions",
        "bane": "Cap all dice pools by Humanity outside your city",
        "book": "NH-SB 41"
    },
    
    # Daeva Bloodlines
    "jharana": {
        "name": "Jharana",
        "parent_clan": "Daeva",
        "description": "Obsessive technomystics chosen from those touched by the God-Machine.",
        "disciplines": ["Auspex", "Dead Signal", "Celerity", "Vigor"],
        "gifts": "Bloodline Discipline",
        "bane": "Risk Persistent Obsession from the Wanton Curse",
        "book": "NH-SB 20"
    },
    "liderc": {
        "name": "Liderc",
        "parent_clan": "Daeva",
        "description": "Passionate lovers who drink from the ardor they incite.",
        "disciplines": ["Celerity", "Majesty", "Obfuscate", "Vigor"],
        "gifts": "Siphon Devotions",
        "bane": "The Wanton Curse also disrupts Touchstones",
        "book": "NH-SB 24"
    },
    "vilseduire": {
        "name": "Vilseduire",
        "parent_clan": "Daeva/Nosferatu",
        "description": "Narcissistic rebels who revel in glamorous transgression",
        "disciplines": ["Majesty", "Nightmare", "Obfuscate", "Resilience"],
        "gifts": "None",
        "bane": "Only one Touchstone, and risk detachment at lower Humanity",
        "book": "NH-SB 50"
    },
    
    # Gangrel Bloodlines
    "kerberos": {
        "name": "Kerberos",
        "parent_clan": "Gangrel",
        "description": "Self-reinventing social predators who excel at projecting the Beast.",
        "disciplines": ["Animalism", "Majesty", "Protean", "Resilience"],
        "gifts": "Hounds of Hell",
        "bane": "Lose 10-again to oppose characters without the Predatory Aura",
        "book": "Onyx Path blog"
    },
    "nosoi": {
        "name": "Nosoi",
        "parent_clan": "Gangrel",
        "description": "Plague farmers who cultivate blood-borne disease in the herd.",
        "disciplines": ["Dominate", "Obfuscate", "Protean", "Resilience"],
        "gifts": "Bloodline Devotions",
        "bane": "Imbibed Vitae untainted by your disease is capped nightly by Humanity",
        "book": "NH-SB 29"
    },
    
    # Mekhet Bloodlines
    "ankou": {
        "name": "Ankou",
        "parent_clan": "Mekhet",
        "description": "Killers who keep the living separate from the dead for the greater good.",
        "disciplines": ["Auspex", "Celerity", "Obfuscate", "Vigor"],
        "gifts": "None",
        "bane": "Must roll Humanity to recover Willpower from Mask",
        "book": "NH-SB 12"
    },
    "icelus": {
        "name": "Icelus",
        "parent_clan": "Mekhet/Ventrue",
        "description": "Manipulators disguised as hypnotherapists plumbing the collective unconscious.",
        "disciplines": ["Auspex", "Dominate", "Obfuscate", "Resilience"],
        "gifts": "Psychognosis Merit",
        "bane": "Detachment inflicts a Mesmerized state",
        "book": "NH-SB 15"
    },
    "khaibit": {
        "name": "Khaibit",
        "parent_clan": "Mekhet",
        "description": "An ancient line of soldiers who fight darkness by embracing it.",
        "disciplines": ["Auspex", "Celerity", "Obfuscate", "Vigor"],
        "gifts": "Obtenebration Devotions",
        "bane": "Temporarily blinded by any light bright enough to inhibit normal vision",
        "book": "Onyx Path blog"
    },
    "morbus": {
        "name": "Morbus",
        "parent_clan": "Mekhet",
        "description": "Outcast plague angels who feed on diseased vessels.",
        "disciplines": ["Auspex", "Celerity", "Cachexy", "Obfuscate"],
        "gifts": "Bloodline Discipline",
        "bane": "Can't feed on the living free of disease",
        "book": "DEC 94"
    },
    
    # Ventrue Bloodlines
    "bron": {
        "name": "Bron",
        "parent_clan": "Ventrue",
        "description": "Knights errant and bravos who live by blood, quest, and oath.",
        "disciplines": ["Animalism", "Crochan", "Dominate", "Resilience"],
        "gifts": "Bloodline Discipline",
        "bane": "Touchstones are vulnerable to detaching and changing by the whims of fate",
        "book": "DE2 117"
    },
    "vardyvle": {
        "name": "Vardyvle",
        "parent_clan": "Ventrue",
        "description": "Jealous dreamers who yearn for what they are not and lose themselves in others' lives.",
        "disciplines": ["Dominate", "Obfuscate", "Protean", "Resilience"],
        "gifts": "Shapeshifting Devotion",
        "bane": "Feeding from those living your dreams risks False Memories",
        "book": "NH-SB 45"
    },
}

# ============================================================================
# COMBINED CLAN DATA
# ============================================================================

ALL_CLANS_DETAILED = {
    **MAJOR_CLANS,
    **UNCOMMON_CLANS
}

ALL_BLOODLINES_DETAILED = ALL_BLOODLINES.copy()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_clan(clan_name):
    """Get a specific clan by name."""
    clan_key = clan_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
    return ALL_CLANS_DETAILED.get(clan_key)

def get_bloodline(bloodline_name):
    """Get a specific bloodline by name."""
    bloodline_key = bloodline_name.lower().replace(" ", "_")
    return ALL_BLOODLINES_DETAILED.get(bloodline_key)

def get_all_clans():
    """Get all clan data."""
    return ALL_CLANS_DETAILED.copy()

def get_all_bloodlines():
    """Get all bloodline data."""
    return ALL_BLOODLINES_DETAILED.copy()

def get_major_clans():
    """Get only the five major clans."""
    return MAJOR_CLANS.copy()

def get_uncommon_clans():
    """Get uncommon and lost clans."""
    return UNCOMMON_CLANS.copy()

