"""
Animal and mythical form definitions for the Chrysalis contract.

These entries only provide physical form data used by +shift:
- Physical Attributes (Strength, Dexterity, Stamina)
- Size, Speed, Health
- Movement modes and mundane senses notes
"""

CHRYSALIS_FORMS = {
    # Canon-style and grounded animals.
    "bat": {"display_name": "Bat", "size": 1, "strength": 1, "dexterity": 4, "stamina": 1, "speed": 15, "health": 2, "movement": "flight", "senses": "echolocation"},
    "badger": {"display_name": "Badger", "size": 3, "strength": 2, "dexterity": 3, "stamina": 5, "speed": 9, "health": 9, "movement": "land, burrow", "senses": "keen smell"},
    "bear": {"display_name": "Bear", "size": 7, "strength": 6, "dexterity": 2, "stamina": 4, "speed": 13, "health": 11, "movement": "land, climb, swim", "senses": "keen smell"},
    "cat": {"display_name": "House Cat", "size": 2, "strength": 1, "dexterity": 5, "stamina": 3, "speed": 13, "health": 5, "movement": "land, climb", "senses": "low-light vision"},
    "great_cat": {"display_name": "Great Cat", "size": 5, "strength": 5, "dexterity": 4, "stamina": 3, "speed": 16, "health": 8, "movement": "land, climb", "senses": "low-light vision"},
    "chimpanzee": {"display_name": "Chimpanzee", "size": 4, "strength": 5, "dexterity": 4, "stamina": 3, "speed": 13, "health": 7, "movement": "land, climb", "senses": "keen vision"},
    "coyote": {"display_name": "Coyote", "size": 3, "strength": 3, "dexterity": 3, "stamina": 3, "speed": 13, "health": 6, "movement": "land", "senses": "keen smell"},
    "crocodile": {"display_name": "Crocodile", "size": 4, "strength": 4, "dexterity": 1, "stamina": 4, "speed": 10, "health": 9, "movement": "land, swim", "senses": "water ambush"},
    "deer": {"display_name": "Deer (Buck)", "size": 6, "strength": 3, "dexterity": 3, "stamina": 3, "speed": 14, "health": 9, "movement": "land", "senses": "keen hearing"},
    "large_dog": {"display_name": "Large Dog", "size": 4, "strength": 4, "dexterity": 3, "stamina": 3, "speed": 14, "health": 7, "movement": "land", "senses": "keen smell"},
    "small_dog": {"display_name": "Small Dog", "size": 2, "strength": 2, "dexterity": 3, "stamina": 3, "speed": 11, "health": 5, "movement": "land", "senses": "keen smell"},
    "fox": {"display_name": "Fox", "size": 2, "strength": 1, "dexterity": 4, "stamina": 3, "speed": 13, "health": 5, "movement": "land", "senses": "keen hearing"},
    "horse": {"display_name": "Horse", "size": 7, "strength": 5, "dexterity": 3, "stamina": 5, "speed": 19, "health": 12, "movement": "land", "senses": "wide field vision"},
    "owl": {"display_name": "Owl", "size": 2, "strength": 1, "dexterity": 3, "stamina": 2, "speed": 14, "health": 4, "movement": "flight", "senses": "night vision, keen hearing"},
    "rat": {"display_name": "Rat", "size": 1, "strength": 1, "dexterity": 4, "stamina": 2, "speed": 6, "health": 3, "movement": "land, climb", "senses": "tight spaces"},
    "raven": {"display_name": "Raven", "size": 2, "strength": 1, "dexterity": 3, "stamina": 2, "speed": 14, "health": 4, "movement": "flight", "senses": "keen sight"},
    "snake": {"display_name": "Snake", "size": 2, "strength": 1, "dexterity": 3, "stamina": 1, "speed": 6, "health": 3, "movement": "land, swim", "senses": "vibration sensing"},
    "toad": {"display_name": "Toad", "size": 1, "strength": 1, "dexterity": 3, "stamina": 1, "speed": 6, "health": 2, "movement": "land, swim", "senses": "amphibious"},
    "weasel": {"display_name": "Weasel/Ferret", "size": 2, "strength": 1, "dexterity": 3, "stamina": 2, "speed": 11, "health": 4, "movement": "land", "senses": "keen smell"},
    "wolf": {"display_name": "Wolf", "size": 4, "strength": 4, "dexterity": 3, "stamina": 3, "speed": 14, "health": 7, "movement": "land", "senses": "keen smell"},
    "shark": {"display_name": "Shark", "size": 7, "strength": 6, "dexterity": 3, "stamina": 4, "speed": 16, "health": 10, "movement": "swim", "senses": "electroreception, blood scent", "aquatic": True},
    "orca": {"display_name": "Orca", "size": 10, "strength": 8, "dexterity": 3, "stamina": 6, "speed": 18, "health": 16, "movement": "swim", "senses": "echolocation", "aquatic": True},
    "dolphin": {"display_name": "Dolphin", "size": 6, "strength": 4, "dexterity": 4, "stamina": 4, "speed": 17, "health": 10, "movement": "swim", "senses": "echolocation", "aquatic": True},
    "octopus": {"display_name": "Octopus", "size": 2, "strength": 2, "dexterity": 5, "stamina": 3, "speed": 8, "health": 5, "movement": "swim, crawl", "senses": "camouflage, tactile", "aquatic": True},
    "squid": {"display_name": "Squid", "size": 4, "strength": 3, "dexterity": 4, "stamina": 3, "speed": 12, "health": 7, "movement": "swim", "senses": "low-light ocean vision", "aquatic": True},
    "giant_squid": {"display_name": "Giant Squid", "size": 12, "strength": 8, "dexterity": 3, "stamina": 7, "speed": 13, "health": 19, "movement": "swim", "senses": "deep-sea low-light vision", "aquatic": True},
    "anglerfish": {"display_name": "Anglerfish", "size": 1, "strength": 1, "dexterity": 2, "stamina": 3, "speed": 6, "health": 4, "movement": "swim", "senses": "bioluminescent lure", "aquatic": True},
    "fish": {"display_name": "Fish (Generic)", "size": 1, "strength": 1, "dexterity": 3, "stamina": 2, "speed": 7, "health": 3, "movement": "swim", "senses": "water vibration sensing", "aquatic": True},
    "eel": {"display_name": "Eel", "size": 1, "strength": 1, "dexterity": 4, "stamina": 2, "speed": 8, "health": 3, "movement": "swim", "senses": "water vibration sensing", "aquatic": True},
    "jellyfish": {"display_name": "Jellyfish", "size": 1, "strength": 1, "dexterity": 2, "stamina": 2, "speed": 5, "health": 3, "movement": "swim", "senses": "water pressure sensing", "aquatic": True},
    "seal": {"display_name": "Seal", "size": 4, "strength": 3, "dexterity": 3, "stamina": 4, "speed": 12, "health": 8, "movement": "swim, land", "senses": "underwater hearing", "aquatic": True},
    "manatee": {"display_name": "Manatee", "size": 7, "strength": 5, "dexterity": 1, "stamina": 6, "speed": 9, "health": 13, "movement": "swim", "senses": "water pressure sensing", "aquatic": True},
    "whale": {"display_name": "Whale", "size": 15, "strength": 10, "dexterity": 2, "stamina": 8, "speed": 16, "health": 23, "movement": "swim", "senses": "echolocation", "aquatic": True},
    "piranha": {"display_name": "Piranha", "size": 1, "strength": 1, "dexterity": 3, "stamina": 1, "speed": 7, "health": 2, "movement": "swim", "senses": "blood scent", "aquatic": True},
    # Larger animals enabled by ogre benefit.
    "elephant": {"display_name": "Elephant", "size": 15, "strength": 9, "dexterity": 2, "stamina": 7, "speed": 15, "health": 22, "movement": "land", "senses": "keen smell"},
    "hippopotamus": {"display_name": "Hippopotamus", "size": 12, "strength": 8, "dexterity": 2, "stamina": 7, "speed": 14, "health": 19, "movement": "land, swim", "senses": "amphibious"},
    "rhino": {"display_name": "Rhinoceros", "size": 12, "strength": 9, "dexterity": 2, "stamina": 6, "speed": 14, "health": 18, "movement": "land", "senses": "thick hide"},
    # Mythical forms (physical body only; no supernatural powers).
    "dragon": {"display_name": "Dragon", "size": 15, "strength": 10, "dexterity": 3, "stamina": 8, "speed": 20, "health": 23, "movement": "land, flight", "senses": "keen smell and sight", "mythical": True},
    "pegasus": {"display_name": "Pegasus", "size": 8, "strength": 6, "dexterity": 4, "stamina": 5, "speed": 21, "health": 13, "movement": "land, flight", "senses": "keen sight", "mythical": True},
    "manticore": {"display_name": "Manticore", "size": 10, "strength": 8, "dexterity": 4, "stamina": 6, "speed": 18, "health": 16, "movement": "land, flight", "senses": "predator scent", "mythical": True},
    "griffin": {"display_name": "Griffin", "size": 9, "strength": 7, "dexterity": 4, "stamina": 5, "speed": 20, "health": 14, "movement": "land, flight", "senses": "raptor sight", "mythical": True},
    "kraken": {"display_name": "Kraken", "size": 15, "strength": 10, "dexterity": 3, "stamina": 8, "speed": 14, "health": 23, "movement": "swim", "senses": "deep-ocean vibration sensing", "aquatic": True, "mythical": True},
}


def normalize_chrysalis_form_name(name):
    """Normalize user-facing form text into a key."""
    return str(name or "").strip().lower().replace("-", "_").replace(" ", "_")
