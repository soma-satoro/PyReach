"""
Changing Breeds data for Legacy Mode (World of Darkness 1st Edition).

This module contains form definitions and breed information for all Changing Breeds,
including the pre-defined breeds and support for custom breeds using Aspects and Favors.

Based on: Changing Breeds (1st Edition)
Reference: https://codexofdarkness.com/wiki/Changing_Breed_Aspects_and_Favors
"""

# =============================================================================
# CHANGING BREEDS REGISTRY
# =============================================================================

CHANGING_BREEDS = {
    # WERECATS (Bastet)
    "rajanya": {
        "display_name": "Rajanya",
        "description": "Tiger-shifters of incredible power and majesty",
        "animal_type": "tiger",
        "breed_favors": ["Fang and Claw 2 (L)", "Keen Senses (all)", "Size 7"],
        "breed_bonus": "All Rajanya have the Striking Looks Merit (not free), in addition to excellent Physical Attributes. Weretigers pay one dot less for the Durga's Blessing Aspect.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form - natural camouflage among humanity",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive tiger-beast of legend",
                "strength": 5,
                "dexterity": 2,
                "stamina": 5,
                "manipulation": 0,
                "size": 8,
                "health_mod": 8,
                "speed_mod": 7,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Massive tiger form",
                "strength": 3,
                "dexterity": 2,
                "stamina": 3,
                "manipulation": 0,
                "size": 2,
                "health_mod": 5,
                "speed_mod": 8,
                "speed_factor": 8,
                "perception_bonus": 3
            }
        }
    },
    
    "bubasti": {
        "display_name": "Bubasti",
        "description": "Mystical cat-people with powerful magic",
        "animal_type": "cat",
        "breed_favors": ["Beast Magic (five dots of spells)", "Clever Monkey", "Fang and Claw 1 (L)"],
        "breed_bonus": "All Bubasti share the Striking Looks Merit (not free). They get three free Specialties in Academics. Instead of a War-Beast form, Bubasti have an eerie Throwback shape.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with an otherworldly beauty",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "throwback": {
                "display_name": "Throwback",
                "description": "Eerie humanoid-feline hybrid",
                "strength": 1,
                "dexterity": 3,
                "stamina": 1,
                "manipulation": 0,
                "size": 4,
                "health_mod": 1,
                "speed_mod": 4,
                "speed_factor": 5,
                "perception_bonus": 5
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Small, swift cat form",
                "strength": -1,
                "dexterity": 3,
                "stamina": -1,
                "manipulation": 0,
                "size": 4,
                "health_mod": -2,
                "speed_mod": 6,
                "speed_factor": 9,
                "perception_bonus": 4
            }
        }
    },
    
    "hatara": {
        "display_name": "Hatara",
        "description": "Lion-shifters with pride and majesty",
        "animal_type": "lion",
        "breed_favors": ["Fang (bite) 3 (L)", "Claw 2 (L)", "Keen Senses (all)", "Size 6"],
        "breed_bonus": "All Hatara get a free Specialty in a Social Skill. They subtract -1 from dice pools to spot a con job, lie or illusion.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with regal bearing",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive lion-beast form",
                "strength": 4,
                "dexterity": 1,
                "stamina": 5,
                "manipulation": 0,
                "size": 8,
                "health_mod": 8,
                "speed_mod": 5,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Powerful lion form",
                "strength": 2,
                "dexterity": 2,
                "stamina": 2,
                "manipulation": 0,
                "size": 1,
                "health_mod": 3,
                "speed_mod": 7,
                "speed_factor": 8,
                "perception_bonus": 3
            }
        }
    },
    
    "bahgrasha": {
        "display_name": "Bahgrasha",
        "description": "Panther-shifters with spiritual connections",
        "animal_type": "panther",
        "breed_favors": ["Catwalk", "Fang and Claw 2 (L)", "Keen Senses (all)"],
        "breed_bonus": "Bahgrasha characters begin with one free point of Harmony. They may have Spirit-based Aspects.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with feline grace",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive panther-beast form",
                "strength": 3,
                "dexterity": 5,
                "stamina": 3,
                "manipulation": 0,
                "size": 7,
                "health_mod": 5,
                "speed_mod": 8,
                "speed_factor": 5,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift panther form",
                "strength": 2,
                "dexterity": 3,
                "stamina": 2,
                "manipulation": 0,
                "size": 5,
                "health_mod": 2,
                "speed_mod": 8,
                "speed_factor": 8,
                "perception_bonus": 2
            }
        }
    },
    
    "balam": {
        "display_name": "Balam",
        "description": "Jaguar-shifters with bone-crushing jaws",
        "animal_type": "jaguar",
        "breed_favors": ["Fang and Claw 2 (L)", "Keen Senses (all)", "Needleteeth"],
        "breed_bonus": "Balam characters get one free Skill Specialty each with Stealth and Survival.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with jungle cunning",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Powerful jaguar-beast form",
                "strength": 3,
                "dexterity": 2,
                "stamina": 3,
                "manipulation": 0,
                "size": 6,
                "health_mod": 4,
                "speed_mod": 5,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Sleek jaguar form",
                "strength": 2,
                "dexterity": 2,
                "stamina": 3,
                "manipulation": 0,
                "size": 0,
                "health_mod": 3,
                "speed_mod": 6,
                "speed_factor": 9,
                "perception_bonus": 4
            }
        }
    },
    
    "cait_sith": {
        "display_name": "Cait Sith",
        "description": "Magical fairy cat-shifters with mystical tricks",
        "animal_type": "fairy cat",
        "breed_favors": ["Fang and Claw 1 (L)", "Keen Senses (all)", "Sweet-Voiced Fiend"],
        "breed_bonus": "Cait Sith receive four free Specialties in Social Skills. All have Expression and Subterfuge. They have no War-Beast form but assume a Throwback form instead.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with fey charm",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "throwback": {
                "display_name": "Throwback",
                "description": "Fey humanoid-feline form",
                "strength": 1,
                "dexterity": 5,
                "stamina": 1,
                "manipulation": 0,
                "size": 4,
                "health_mod": 0,
                "speed_mod": 6,
                "speed_factor": 5,
                "perception_bonus": 3
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Tiny magical cat form",
                "strength_absolute": 2,
                "dexterity": 3,
                "stamina_absolute": 3,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 6,
                "speed_mod": 4,
                "speed_factor": 7,
                "perception_bonus": 3
            }
        }
    },
    
    "qualmi": {
        "display_name": "Qualmi",
        "description": "Lynx-shifters bonded with the elements",
        "animal_type": "lynx",
        "breed_favors": ["Clever Monkey", "Earthbond", "Fang and Claw 2 (L)"],
        "breed_bonus": "Qualm'a ni have strong Physical and Social Attributes, and receive two free Specialties in each. They add +1 to dice pools involving Earthbond or Territory Bond.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with elemental connection",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Powerful lynx-beast form",
                "strength": 2,
                "dexterity": 3,
                "stamina": 2,
                "manipulation": 0,
                "size": 0,
                "health_mod": 2,
                "speed_mod": 5,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift lynx form",
                "strength": 1,
                "dexterity": 3,
                "stamina": 3,
                "manipulation": 0,
                "size": 0,
                "health_mod": 3,
                "speed_mod": 7,
                "speed_factor": 8,
                "perception_bonus": 2
            }
        }
    },
    
    "klinerash": {
        "display_name": "Klinerash",
        "description": "Dark version of the Bubasti, prone to witchcraft",
        "animal_type": "black cat",
        "breed_favors": ["Beast Magic (five dots of spells)", "Fang and Claw 1 (L)", "Keen Senses (all)"],
        "breed_bonus": "Klinerash affinity for magic grants two free Skill Specialties in Occult. In Primal form, the small black cats gain +2 bonus to hide from characters of Size 5 or larger.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with dark mystique",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "dire_beast": {
                "display_name": "Dire Beast",
                "description": "Large black cat form",
                "strength": 2,
                "dexterity": 4,
                "stamina": 2,
                "manipulation": 0,
                "size": 4,
                "health_mod": 1,
                "speed_mod": 9,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Small black cat form",
                "strength_absolute": 2,
                "dexterity_absolute": 5,
                "stamina_absolute": 3,
                "manipulation": 0,
                "size_absolute": 2,
                "health_absolute": 5,
                "speed_mod": 12,
                "speed_factor": 7,
                "perception_bonus": 4
            }
        }
    },
    
    # MEGAFAUNA
    "azubuike": {
        "display_name": "Azubuike",
        "description": "Rhino-shifters of immense power",
        "animal_type": "rhinoceros",
        "breed_favors": ["Fang and Claw (horn) 3 (L)", "Natural Armor 3/2", "Size 12"],
        "breed_bonus": "Huge size, horn and strength",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with powerful build",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive rhino-beast form",
                "strength": 5,
                "dexterity": 0,
                "stamina": 5,
                "manipulation": -4,
                "size": 10,
                "health_mod": 15,
                "speed_mod": 7,
                "speed_factor": 7,
                "perception_bonus": 0
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Enormous rhinoceros form",
                "strength": 6,
                "dexterity": 0,
                "stamina": 5,
                "manipulation": -5,
                "size": 12,
                "health_mod": 17,
                "speed_mod": 8,
                "speed_factor": 7,
                "perception_bonus": 0
            }
        }
    },
    
    "jhaa": {
        "display_name": "Jhaa",
        "description": "Elephant-shifters with enormous power",
        "animal_type": "elephant",
        "breed_favors": ["Extra Limb (trunk)", "Fang and Claw (tusks) 2 (L)", "Size 13"],
        "breed_bonus": "Enormous strength and power",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with tremendous presence",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive elephant-beast form",
                "strength": 4,
                "dexterity": 1,
                "stamina": 3,
                "manipulation": -3,
                "size": 8,
                "health_mod": 11,
                "speed_mod": 7,
                "speed_factor": 6,
                "perception_bonus": 0
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Enormous elephant form",
                "strength": 4,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": -1,
                "size": 13,
                "health_mod": 17,
                "speed_mod": 5,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    "mhole_rho": {
        "display_name": "Mhole-Rho",
        "description": "African elephant-shifters of legendary size",
        "animal_type": "african elephant",
        "breed_favors": ["Extra Limb (trunk)", "Fang and Claw (tusks) 3 (L)", "Size 15"],
        "breed_bonus": "Enormous size and strength",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with imposing stature",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive elephant-beast form",
                "strength": 4,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": -3,
                "size": 8,
                "health_mod": 12,
                "speed_mod": 5,
                "speed_factor": 6,
                "perception_bonus": 0
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Gigantic African elephant form",
                "strength": 5,
                "dexterity": 0,
                "stamina": 5,
                "manipulation": -1,
                "size": 15,
                "health_mod": 20,
                "speed_mod": 6,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    "iravati": {
        "display_name": "Iravati",
        "description": "Southeast Asian elephant-shifters",
        "animal_type": "asian elephant",
        "breed_favors": ["Extra Limb (trunk)", "Fang and Claw (tusks) 2 (L)", "Size 14"],
        "breed_bonus": "Enormous size and strength",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with spiritual depth",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive elephant-beast form",
                "strength": 4,
                "dexterity": 1,
                "stamina": 4,
                "manipulation": -4,
                "size": 8,
                "health_mod": 12,
                "speed_mod": 5,
                "speed_factor": 6,
                "perception_bonus": 0
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Enormous Asian elephant form",
                "strength": 5,
                "dexterity": 0,
                "stamina": 5,
                "manipulation": -4,
                "size": 14,
                "health_mod": 19,
                "speed_mod": 6,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    # SMALL SHIFTERS - RODENTS AND SCAVENGERS
    "minjur": {
        "display_name": "Minjur",
        "description": "Rat-shifters with cunning and adaptability",
        "animal_type": "rat",
        "breed_favors": ["Darksight", "Fang and Claw (bite) 1 (L)", "Needleteeth"],
        "breed_bonus": "Rats duck into small places, but aren't physically tough. In return, Minjur receive nine dots for Aspects instead of the usual seven. Minjur also gain a +2 bonus when trying to hide from Size 5 or larger creatures.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with sharp features",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_form": {
                "display_name": "War-Form",
                "description": "Hunched rat-beast hybrid",
                "strength": 1,
                "dexterity": 2,
                "stamina": 1,
                "manipulation": -5,
                "size": 5,
                "health_mod": 1,
                "speed_mod": 2,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift rat form",
                "strength_absolute": 2,
                "dexterity": 3,
                "stamina_absolute": 2,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 5,
                "speed_mod": 15,
                "speed_factor": 10,
                "perception_bonus": 4
            }
        }
    },
    
    "baitu": {
        "display_name": "Baitu",
        "description": "Hare-shifters blessed with speed and fortune",
        "animal_type": "hare",
        "breed_favors": ["Keen Senses (all)", "Nine Lives", "Speed 10"],
        "breed_bonus": "Hares are fast, but they're not fighters. In Primal form, these ferals lose a good deal of their human constitution. However, they gain speed, perception and a vast bag of tricks. Lucks begin play with nine dots, not seven, to spend on Aspects. They also gain a +2 bonus when trying to hide from Size 5 or larger creatures.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with quick movements",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_form": {
                "display_name": "War-Form",
                "description": "Powerful hare-human hybrid",
                "strength": 1,
                "dexterity": 4,
                "stamina": 1,
                "manipulation": -2,
                "size": 5,
                "health_mod": 1,
                "speed_mod": 2,
                "speed_factor": 5,
                "perception_bonus": 4
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift hare form",
                "strength_absolute": 2,
                "dexterity": 5,
                "stamina_absolute": 2,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 5,
                "speed_mod": 15,
                "speed_factor": 10,
                "perception_bonus": 4
            }
        }
    },
    
    "archunen": {
        "display_name": "Archunen",
        "description": "Raccoon-shifters with clever hands and minds",
        "animal_type": "raccoon",
        "breed_favors": ["Fang and Claw (bite) 1 (L)", "Size 3", "Nine Lives"],
        "breed_bonus": "These ferals shrink to smaller forms, lowering certain Physical Attributes in the process. In exchange, the raccoon-folk begin play with nine dots, not seven, to spend on Aspects. They also gain a +2 bonus when trying to hide from creatures of Size 5 or larger.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with dexterous hands",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_form": {
                "display_name": "War-Form",
                "description": "Hunched raccoon-beast",
                "strength": 1,
                "dexterity": 2,
                "stamina": 1,
                "manipulation": -2,
                "size": 5,
                "health_mod": 3,
                "speed_mod": 2,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Clever raccoon form",
                "strength_absolute": 3,
                "dexterity": 2,
                "stamina_absolute": 2,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 5,
                "speed_mod": 7,
                "speed_factor": 6,
                "perception_bonus": 2
            }
        }
    },
    
    "reynardi": {
        "display_name": "Reynardi",
        "description": "Fox-shifters known as cunning tricksters",
        "animal_type": "fox",
        "breed_favors": ["Fang and Claw (bite) 1 (L)", "Nine Lives", "Speed 9"],
        "breed_bonus": "Similar to most small werefolk, these ferals lose some physical hardiness as they shrink. In exchange, these fox-tricksters begin play with nine dots, not seven, to spend on Aspects. Reynardi also gain a +2 bonus when trying to hide from larger creatures, and have the Tell Aspect (distinctive eyes) for no cost.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with distinctive eyes",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_form": {
                "display_name": "War Form",
                "description": "Fox-beast hybrid",
                "strength": 1,
                "dexterity": 2,
                "stamina": 1,
                "manipulation": -2,
                "size": 5,
                "health_mod": 1,
                "speed_mod": 2,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift fox form",
                "strength_absolute": 3,
                "dexterity": 3,
                "stamina_absolute": 3,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 6,
                "speed_mod": 7,
                "speed_factor": 9,
                "perception_bonus": 2
            }
        }
    },
    
    "mistai": {
        "display_name": "Mistai",
        "description": "Coyote-shifters walking as Laughing Strangers",
        "animal_type": "coyote",
        "breed_favors": ["Alarming Alacrity", "Fang and Claw (bite) 1 (L)"],
        "breed_bonus": "Mistai have no War-Beast form; instead, they have a Throwback coyote-human guise that walks with quiet confidence. Similar to other Laughing Strangers, Coyote's children begin play with nine dots, not seven, to spend on Aspects.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with coyote's cunning",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "throwback": {
                "display_name": "Throwback",
                "description": "Coyote-human hybrid with quiet confidence",
                "strength": 1,
                "dexterity": 2,
                "stamina": 0,
                "manipulation": -2,
                "size": 6,
                "health_mod": 1,
                "speed_mod": 2,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift coyote form",
                "strength": -1,
                "dexterity": 4,
                "stamina_absolute": 3,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 6,
                "speed_mod": 7,
                "speed_factor": 8,
                "perception_bonus": 2
            }
        }
    },
    
    "wapathemwa": {
        "display_name": "Wapathemwa",
        "description": "Possum-shifters known as White Beasts",
        "animal_type": "possum",
        "breed_favors": ["Extra Limb (Tail)", "Fang and Claw (Bite) 1 (L)", "Nine Lives"],
        "breed_bonus": "All Wapathemwa have at least one dot in Survival, and receive a free Skill Specialty in that trait. Similar to other Laughing Strangers, White Beasts begin play with nine dots, not seven, to spend on Aspects.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with survivor's instinct",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Possum-beast with prehensile tail",
                "strength": 1,
                "dexterity": 2,
                "stamina": 1,
                "manipulation": -4,
                "size": 5,
                "health_mod": 1,
                "speed_mod": 2,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Possum form with grasping tail",
                "strength_absolute": 3,
                "dexterity": 3,
                "stamina_absolute": 2,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 5,
                "speed_mod": 4,
                "speed_factor": 6,
                "perception_bonus": 2
            }
        }
    },
    
    # CANINES
    "maerans": {
        "display_name": "Maerans",
        "description": "Dog-shifters with unwavering loyalty",
        "animal_type": "dog",
        "breed_favors": ["Fang and Claw (bite) 2 (L)", "Keen Senses", "Speed 8"],
        "breed_bonus": "Dog-bloods have sight, hearing and smell as a single free Keen Sense Aspect. Of all feral breeds (save perhaps for cats), these shapeshifters have the easiest time getting along in Man's world while in their Primal form.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with loyal nature",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Powerful dog-beast hybrid",
                "strength": 2,
                "dexterity": 1,
                "stamina": 1,
                "manipulation": 0,
                "size": 6,
                "health_mod": 2,
                "speed_mod": 3,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Loyal dog form",
                "strength": 0,
                "dexterity": 1,
                "stamina": 1,
                "manipulation": 0,
                "size": 4,
                "health_mod": 0,
                "speed_mod": 4,
                "speed_factor": 8,
                "perception_bonus": 4
            }
        }
    },
    
    "riantes": {
        "display_name": "Riantes",
        "description": "Hyena-shifters with pack mentality",
        "animal_type": "hyena",
        "breed_favors": ["Fang and Claw (bite) 2 (L)", "Keen Senses", "Speed 8"],
        "breed_bonus": "Riantes have sight, hearing and smell as a single free Keen Sense Aspect. A typical Riante has other hyenas nearby, and often consorts with at least one other shapechanger of her breed. Many Riantes also have at least one dot in Crafts.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with pack instincts",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Powerful hyena-beast",
                "strength": 2,
                "dexterity": 1,
                "stamina": 3,
                "manipulation": 0,
                "size": 6,
                "health_mod": 4,
                "speed_mod": 3,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Cackling hyena form",
                "strength": 1,
                "dexterity": 1,
                "stamina": 2,
                "manipulation": 0,
                "size": 4,
                "health_mod": 1,
                "speed_mod": 4,
                "speed_factor": 8,
                "perception_bonus": 3
            }
        }
    },
    
    "warrigal": {
        "display_name": "Warrigal",
        "description": "Dingo-shifters from the Australian wilderness",
        "animal_type": "dingo",
        "breed_favors": ["Fang and Claw (bite) 2 (L)", "Keen Senses", "Speed 8"],
        "breed_bonus": "Dog-bloods have sight, hearing and smell as a single free Keen Sense Aspect. Warrigal characters also have at least one dot in Survival, and often more.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with wilderness knowledge",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Dingo-beast hybrid",
                "strength": 1,
                "dexterity": 1,
                "stamina": 1,
                "manipulation": 0,
                "size": 5,
                "health_mod": 2,
                "speed_mod": 3,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Wild dingo form",
                "strength": 0,
                "dexterity": 1,
                "stamina": 1,
                "manipulation": 0,
                "size": 3,
                "health_mod": 0,
                "speed_mod": 4,
                "speed_factor": 8,
                "perception_bonus": 4
            }
        }
    },
    
    # PRIMATES
    "hanumani_brahmin": {
        "display_name": "Hanumani Brahmin",
        "description": "Indian monkey/ape shifters blessed by Hanuman",
        "animal_type": "monkey",
        "breed_favors": ["Clamber", "Size 4", "Speed 6"],
        "breed_bonus": "All Hanumani Brahmans also have the Magnificence Aspect for free.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with graceful bearing",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Powerful monkey-beast hybrid",
                "strength": 2,
                "dexterity": 3,
                "stamina": 2,
                "manipulation": -1,
                "size": 5,
                "health_mod": 7,
                "speed_mod": 6,
                "speed_factor": 6,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Agile monkey form",
                "strength": 1,
                "dexterity": 3,
                "stamina": 1,
                "manipulation": -2,
                "size": 4,
                "health_mod": 0,
                "speed_mod": 5,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    "sun_wukong": {
        "display_name": "Sun Wukong",
        "description": "Chinese monkey shifters of the Wukong Order",
        "animal_type": "monkey",
        "breed_favors": ["Clamber", "Fang and Claw 1 (L)", "Speed 6"],
        "breed_bonus": "Members of the Wukong Order can use the Fighting Style: Kung Fu Merit in their beast forms -- something no other feral shapechanger can do.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with martial grace",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Fierce monkey warrior form",
                "strength": 2,
                "dexterity": 3,
                "stamina": 2,
                "manipulation": -1,
                "size": 5,
                "health_mod": 7,
                "speed_mod": 6,
                "speed_factor": 6,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift monkey form",
                "strength": 1,
                "dexterity": 3,
                "stamina": 1,
                "manipulation": -2,
                "size": 4,
                "health_mod": 0,
                "speed_mod": 5,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    "abathaki": {
        "display_name": "Abathaki",
        "description": "African monkey/ape shifters with Beast Magic",
        "animal_type": "monkey",
        "breed_favors": ["Clamber", "Darksight", "Fang and Claw 1 (L)"],
        "breed_bonus": "Although the player must pay points for it, all members of this breed have an innate faculty for Beast Magic.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with magical potential",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Swift monkey-beast warrior",
                "strength": 2,
                "dexterity": 4,
                "stamina": 2,
                "manipulation": 2,
                "size": 5,
                "health_mod": 7,
                "speed_mod": 7,
                "speed_factor": 6,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Agile monkey form",
                "strength": 1,
                "dexterity": 3,
                "stamina": 1,
                "manipulation": -1,
                "size": 4,
                "health_mod": 0,
                "speed_mod": 5,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    "tothian": {
        "display_name": "Tothian",
        "description": "Baboon shifters with Beast Magic and spiritual connections",
        "animal_type": "baboon",
        "breed_favors": ["Clamber", "Darksight", "Fang and Claw 1 (L)"],
        "breed_bonus": "These breeds have innate talents for Beast Magic or Spirit Gifts. Both species can buy the Shadow Bond Aspect, and have other Aspect tricks as well.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with spiritual awareness",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Fierce baboon-beast hybrid",
                "strength": 2,
                "dexterity": 3,
                "stamina": 2,
                "manipulation": -2,
                "size": 5,
                "health_mod": 7,
                "speed_mod": 6,
                "speed_factor": 6,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Cunning baboon form",
                "strength": 1,
                "dexterity": 3,
                "stamina": 1,
                "manipulation": -1,
                "size": 4,
                "health_mod": 0,
                "speed_mod": 5,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    "babi_ahsh": {
        "display_name": "Babi-Ahsh",
        "description": "Baboon shifters with Spirit Gifts and shadow magic",
        "animal_type": "baboon",
        "breed_favors": ["Clamber", "Darksight", "Fang and Claw 1 (L)"],
        "breed_bonus": "These breeds have innate talents for Beast Magic or Spirit Gifts. Both species can buy the Shadow Bond Aspect, and have other Aspect tricks as well.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with shadow affinity",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Shadow-touched baboon-beast",
                "strength": 2,
                "dexterity": 3,
                "stamina": 2,
                "manipulation": -2,
                "size": 5,
                "health_mod": 7,
                "speed_mod": 6,
                "speed_factor": 6,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift baboon form",
                "strength": 1,
                "dexterity": 3,
                "stamina": 1,
                "manipulation": -1,
                "size": 4,
                "health_mod": 0,
                "speed_mod": 5,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    "hugranjah": {
        "display_name": "Hugranjah",
        "description": "Mythic ape shifters - the legendary Sasquatch",
        "animal_type": "sasquatch",
        "breed_favors": ["Darksight", "Fang and Claw 1 (L)", "Size 7"],
        "breed_bonus": "These folk are adept at Stealth, and receive an extra two successes to any attempt at hiding, moving silently or otherwise evading detection. Their Primal form is the ape-like Sasquatch, which triggers the Delusion unless the witness makes a normal Resolve + Composure roll.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with mysterious presence",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive Sasquatch with glowing eyes and misty hide",
                "strength": 4,
                "dexterity": 0,
                "stamina": 3,
                "manipulation": -2,
                "size": 8,
                "health_mod": 6,
                "speed_mod": 4,
                "speed_factor": 5,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Legendary Sasquatch form",
                "strength": 3,
                "dexterity": 0,
                "stamina": 2,
                "manipulation": -2,
                "size": 7,
                "health_mod": 4,
                "speed_mod": 3,
                "speed_factor": 5,
                "perception_bonus": 1
            }
        }
    },
    
    # ARACHNIDS (SPIDERS)
    "nanekisu": {
        "display_name": "Nanekisu",
        "description": "Hive-minded spider collective - many become one",
        "animal_type": "spider swarm",
        "breed_favors": ["Fang and Claw", "Many-Legged (+4 Speed)", "Nine Lives"],
        "breed_bonus": "Nanekisu surrender their individuality to join a hive-minded collective. A single mind guides them and a single human flesh-bag holds their souls, but each one is truly many. This breed has NO Primal form, just Man-Guise and War-Form (millions of spiders united into a giant arachnid). When 'killed', component spiders scurry off and resurrect via Nine Lives Aspect.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form hosting the hive mind",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Giant arachnid formed from millions of spiders",
                "strength": 3,
                "dexterity": 4,
                "stamina": 3,
                "manipulation": -5,
                "size": 6,
                "health_mod": 4,
                "speed_mod": 13,
                "speed_factor": 9,
                "perception_bonus": 2
            }
        }
    },
    
    "carapache": {
        "display_name": "Carapache",
        "description": "South American spider shifters with jungle cunning",
        "animal_type": "spider",
        "breed_favors": ["Many-Legged (+4 Speed)", "Venomous", "Webbing"],
        "breed_bonus": "As for most small shapechangers, the Carapache Primal form has set Health, Size and Speed traits. This gives +2 bonus when hiding from larger creatures. All Carapache have Survival and Stealth, with free Skill Specialties in Hiding and Jungle Survival.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with jungle wisdom",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Large spider-beast hybrid",
                "strength": 2,
                "dexterity": 4,
                "stamina": 2,
                "manipulation": -3,
                "size": 5,
                "health_mod": 3,
                "speed_mod": 8,
                "speed_factor": 9,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift spider form",
                "strength_absolute": 2,
                "dexterity": 4,
                "stamina_absolute": 2,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 5,
                "speed_mod": 12,
                "speed_factor": 9,
                "perception_bonus": 2
            }
        }
    },
    
    "chi_hsu": {
        "display_name": "C'hi Hsu",
        "description": "Asian spider shifters with corporate connections",
        "animal_type": "spider",
        "breed_favors": ["Many-Legged (+4 Speed)", "Venomous", "Webbing"],
        "breed_bonus": "C'hi Hsu have NO War-Beast forms, only a single large spider (Dire Beast) and small human. Both shapes are the same Size. All C'hi Hsu have Occult Skill, and have Allies and Contacts among corporations and criminal syndicates.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with underworld connections",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "dire_beast": {
                "display_name": "Dire Beast",
                "description": "Large venomous spider",
                "strength": 0,
                "dexterity": 3,
                "stamina": 0,
                "manipulation": -5,
                "size": 4,
                "health_mod": 0,
                "speed_mod": 16,
                "speed_factor": 5,
                "perception_bonus": 2
            }
        }
    },
    
    "sicarius": {
        "display_name": "Sicarius",
        "description": "Black widow shifters with deadly venom",
        "animal_type": "black widow spider",
        "breed_favors": ["Many-Legged (+4 Speed)", "Venomous", "Webbing"],
        "breed_bonus": "Sicarians are too well tempered for war. Instead, they have a single vast spider-form, a 'Dire Beast' that spans more than eight feet from tip to tip. All Sicarians have Science with free Skill Specialty in Toxicology. Their venom is the most virulent sort.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with scientific knowledge",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "dire_beast": {
                "display_name": "Dire Beast",
                "description": "Massive black widow spanning 8+ feet",
                "strength": 0,
                "dexterity": 4,
                "stamina": 0,
                "manipulation": -5,
                "size": 6,
                "health_mod": 0,
                "speed_mod": 8,
                "speed_factor": 5,
                "perception_bonus": 2
            }
        }
    },
    
    # URSINES (BEARS)
    "yonah": {
        "display_name": "Yonah",
        "description": "Black bear shifters, most personable of bears",
        "animal_type": "black bear",
        "breed_favors": ["Fang (bite) 3 (L) and Claw 2 (L)", "Natural Armor 2/1", "Size 6"],
        "breed_bonus": "The most personable of the breed, Yonah get one free Specialty with a Social Skill.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with personable nature",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Powerful black bear-beast",
                "strength": 4,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": 0,
                "size": 7,
                "health_mod": 6,
                "speed_mod": 7,
                "speed_factor": 5,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Black bear form",
                "strength": 2,
                "dexterity": 0,
                "stamina": 2,
                "manipulation": 0,
                "size": 1,
                "health_mod": 3,
                "speed_mod": 3,
                "speed_factor": 6,
                "perception_bonus": 2
            }
        }
    },
    
    "nanuq": {
        "display_name": "Nanuq",
        "description": "Polar bear shifters of the frozen north",
        "animal_type": "polar bear",
        "breed_favors": ["Fang (bite) 3 (L) and Claw 1 (L)", "Natural Armor 2/1", "Size 7"],
        "breed_bonus": "Nanuq get a free Survival Specialty in Arctic Surroundings.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form adapted to arctic life",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive polar bear-beast",
                "strength": 5,
                "dexterity": 0,
                "stamina": 5,
                "manipulation": 0,
                "size": 8,
                "health_mod": 8,
                "speed_mod": 6,
                "speed_factor": 5,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Polar bear form",
                "strength": 4,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": 0,
                "size": 2,
                "health_mod": 6,
                "speed_mod": 6,
                "speed_factor": 6,
                "perception_bonus": 1
            }
        }
    },
    
    "storm_bear": {
        "display_name": "Storm Bear",
        "description": "Russian bear shifters of legendary power",
        "animal_type": "russian bear",
        "breed_favors": ["Fang (Bite) 3 (L) and Claw 2 (L)", "Natural Armor 3/2", "Size 8"],
        "breed_bonus": "Does he really need one? (Massive and terrifying)",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form, burly and surly",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Legendary bear-beast of immense power",
                "strength": 6,
                "dexterity": 0,
                "stamina": 5,
                "manipulation": 0,
                "size": 8,
                "health_mod": 8,
                "speed_mod": 6,
                "speed_factor": 5,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Massive Russian bear",
                "strength": 4,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": 0,
                "size": 2,
                "health_mod": 6,
                "speed_mod": 6,
                "speed_factor": 6,
                "perception_bonus": 2
            }
        }
    },
    
    # UNGULATES (HOOFED ANIMALS)
    "uchchaihshravi": {
        "display_name": "Uchchaihshravi",
        "description": "Horse shifters with divine speed",
        "animal_type": "horse",
        "breed_favors": ["Fang and Claw (bite) 1 (L)", "Size 7", "Speed 12"],
        "breed_bonus": "Hooves inflict three bashing damage and can knock down opponents. Speed species factor is based on four-legged War-Beast, not two-legged human norm.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with equine grace",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Powerful horse-beast hybrid",
                "strength": 3,
                "dexterity": 1,
                "stamina": 3,
                "manipulation": -1,
                "size": 8,
                "health_mod": 6,
                "speed_mod": 11,
                "speed_factor": 12,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift horse form",
                "strength": 2,
                "dexterity": 0,
                "stamina": 3,
                "manipulation": -1,
                "size": 7,
                "health_mod": 5,
                "speed_mod": 9,
                "speed_factor": 12,
                "perception_bonus": 1
            }
        }
    },
    
    "alces": {
        "display_name": "Alces",
        "description": "Elk shifters of astonishing size",
        "animal_type": "elk",
        "breed_favors": ["Fang and Claw (antlers) 3 (L)", "Size 10", "Speed 10"],
        "breed_bonus": "Astonishing size and speed, plus affinity for spirit world. Hooves inflict three bashing damage and can knock down opponents. Speed species factor based on four-legged War-Beast.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with spiritual connection",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive elk-beast",
                "strength": 4,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": -2,
                "size": 10,
                "health_mod": 9,
                "speed_mod": 9,
                "speed_factor": 10,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Enormous elk form",
                "strength": 3,
                "dexterity": 0,
                "stamina": 3,
                "manipulation": -3,
                "size": 10,
                "health_mod": 8,
                "speed_mod": 8,
                "speed_factor": 10,
                "perception_bonus": 1
            }
        }
    },
    
    "flidaisin": {
        "display_name": "Flidaisin",
        "description": "Deer shifters with fey beauty",
        "animal_type": "deer",
        "breed_favors": ["Keen Sense 2", "Size 6", "Speed 10"],
        "breed_bonus": "Males only have Fang and Claw (Antlers) 3 (L). All Flidaisins have Striking Looks Merit in human form. Hooves inflict two bashing damage and can knock down opponents.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with striking beauty",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Graceful deer-beast",
                "strength": 2,
                "dexterity": 3,
                "stamina": 2,
                "manipulation": -1,
                "size": 6,
                "health_mod": 3,
                "speed_mod": 5,
                "speed_factor": 5,
                "perception_bonus": 3
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift deer form",
                "strength": 2,
                "dexterity": 3,
                "stamina": 3,
                "manipulation": -1,
                "size": 6,
                "health_mod": 4,
                "speed_mod": 10,
                "speed_factor": 10,
                "perception_bonus": 3
            }
        }
    },
    
    "takuskansa": {
        "display_name": "Takuskansa",
        "description": "Native American horse shifters with deep empathy",
        "animal_type": "horse",
        "breed_favors": ["Fang and Claw (bite) 1 (L)", "Size 7", "Speed 12"],
        "breed_bonus": "All Takuskansa have Empathy 3+. Hooves inflict three bashing damage and can knock down opponents. Speed species factor based on four-legged War-Beast.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with deep empathy",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Powerful horse-beast warrior",
                "strength": 3,
                "dexterity": 2,
                "stamina": 3,
                "manipulation": -1,
                "size": 8,
                "health_mod": 6,
                "speed_mod": 12,
                "speed_factor": 12,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift and graceful horse",
                "strength": 2,
                "dexterity": 3,
                "stamina": 3,
                "manipulation": -1,
                "size": 7,
                "health_mod": 5,
                "speed_mod": 12,
                "speed_factor": 12,
                "perception_bonus": 1
            }
        }
    },
    
    # AVIANS (BIRDS AND BATS)
    "gente_alada": {
        "display_name": "Gente Alada",
        "description": "Quetzal bird shifters with Aztec heritage",
        "animal_type": "quetzal",
        "breed_favors": ["Fang and Claw (beak) 1 (L) (talons) 2 (L)", "Speed 10", "Wings"],
        "breed_bonus": "All ferals have Brawl, Weaponry and Academics Skills with free Specialties in Close Combat, Silent Kills and Aztec History. Primal form has specific Size and Health (smaller). +2 bonus to hiding.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with bright coloration",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Fierce quetzal-beast warrior",
                "strength": 2,
                "dexterity": 4,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 7,
                "speed_factor": 8,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Beautiful quetzal bird",
                "strength": 0,
                "dexterity": 5,
                "stamina": 0,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 4,
                "speed_mod": 12,
                "speed_factor": 5,
                "perception_bonus": 2
            }
        }
    },
    
    "corvians": {
        "display_name": "Corvians",
        "description": "Crow/raven shifters, supreme tricksters",
        "animal_type": "crow/raven",
        "breed_favors": ["Fang and Claw (beak and talons) 1 (L)", "Speed 10", "Wings"],
        "breed_bonus": "Corvians do NOT have War-Beast form; instead they have modified Throwback with talons, beak and wings. Some can assume Dire Beast (seven-foot wingspan) OR Flock form, but not both. Supreme tricksters with 'bag of tricks' Aspects. +2 bonus to hide in Primal form.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with trickster nature",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "throwback": {
                "display_name": "Throwback",
                "description": "Human with beak, talons and wings",
                "strength": 1,
                "dexterity": 2,
                "stamina": 1,
                "manipulation": -2,
                "size": 0,
                "health_mod": 1,
                "speed_mod": 8,
                "speed_factor": 10,
                "perception_bonus": 2
            },
            "dire_beast": {
                "display_name": "Dire Beast",
                "description": "Giant crow with seven-foot wingspan",
                "strength": 0,
                "dexterity": 1,
                "stamina": 1,
                "manipulation": 0,
                "size": 6,
                "health_mod": 2,
                "speed_mod": 6,
                "speed_factor": 10,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift crow/raven form",
                "strength_absolute": 2,
                "dexterity": 1,
                "stamina_absolute": 2,
                "manipulation": 0,
                "size_absolute": 2,
                "health_absolute": 4,
                "speed_mod": 14,
                "speed_factor": 10,
                "perception_bonus": 2
            }
        }
    },
    
    "chevalier_rapace": {
        "display_name": "Chevalier Rapace",
        "description": "Falcon shifters with martial prowess",
        "animal_type": "falcon",
        "breed_favors": ["Fang and Claw (beak) 1 (L) (talons) 2 (L)", "Speed 15", "Wings"],
        "breed_bonus": "All raptor-people have Academics with free Specialty in Military History, plus Brawl and Weaponry Skills, and Fighting Finesse Merit (Dive and Claw).",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with martial bearing",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Fierce raptor-beast warrior",
                "strength": 4,
                "dexterity": 1,
                "stamina": 5,
                "manipulation": 0,
                "size": 6,
                "health_mod": 6,
                "speed_mod": 11,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift falcon form",
                "strength_absolute": 4,
                "dexterity": 1,
                "stamina_absolute": 5,
                "manipulation": 0,
                "size_absolute": 4,
                "health_absolute": 8,
                "speed_mod": 20,
                "speed_factor": 15,
                "perception_bonus": 2
            }
        }
    },
    
    "vagahuir": {
        "display_name": "Vagahuir",
        "description": "Bat shifters with haunting songs",
        "animal_type": "bat",
        "breed_favors": ["Echolocation", "Speed 10", "Wings"],
        "breed_bonus": "Most Vagahuir have Expression with free Specialty in Song. Primal form has specific Size and Health (smaller). +2 bonus to hiding.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with musical talent",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Large bat-beast",
                "strength": 3,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": 0,
                "size": 6,
                "health_mod": 5,
                "speed_mod": 10,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift bat form",
                "strength": 0,
                "dexterity": 0,
                "stamina": 1,
                "manipulation": 0,
                "size_absolute": 3,
                "health_absolute": 5,
                "speed_mod": 5,
                "speed_factor": 10,
                "perception_bonus": 2
            }
        }
    },
    
    "strigoi": {
        "display_name": "Strigoi",
        "description": "Owl shifters specializing in information and death magic",
        "animal_type": "owl",
        "breed_favors": ["Darksight", "Fang and Claw (beak) 2 (L) (wings) 3 (B)", "Wings"],
        "breed_bonus": "These ferals specialize in information, and receive two free Skill Specialties in Academics, Investigation or Occult.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with keen intelligence",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Fierce owl-beast",
                "strength": 2,
                "dexterity": 3,
                "stamina": 0,
                "manipulation": -4,
                "size": 6,
                "health_mod": 1,
                "speed_mod": 3,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Silent owl form",
                "strength": 0,
                "dexterity": 4,
                "stamina": 0,
                "manipulation": 0,
                "size_absolute": 4,
                "health_absolute": 5,
                "speed_mod": 7,
                "speed_factor": 8,
                "perception_bonus": 2
            }
        }
    },
    
    "brythian": {
        "display_name": "Brythian",
        "description": "Mythic bird shifters with prophetic powers",
        "animal_type": "mythic bird",
        "breed_favors": ["Fang and Claw (beak) 1 (L) (wings) 3 (B)", "Speed 13", "Wings"],
        "breed_bonus": "Mythic bird shifters with spiritual connections and foretelling abilities.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with prophetic insight",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Majestic mythic bird-beast",
                "strength": 2,
                "dexterity": 1,
                "stamina": 5,
                "manipulation": 0,
                "size": 7,
                "health_mod": 6,
                "speed_mod": 15,
                "speed_factor": 5,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Legendary bird form",
                "strength": 2,
                "dexterity": 1,
                "stamina": 3,
                "manipulation": 0,
                "size": 5,
                "health_mod": 2,
                "speed_mod": 11,
                "speed_factor": 15,
                "perception_bonus": 2
            }
        }
    },
    
    # SHADOW BREEDS (UNUSUAL AND MYSTICAL)
    "whiskey_croc": {
        "display_name": "Whiskey Croc",
        "description": "Crocodile shifters reeking of alcohol and sewage",
        "animal_type": "crocodile",
        "breed_favors": ["Darksight", "Fang and Claw (bite) 3 (L) / (rake) 1 (L)", "Natural Armor 4/3"],
        "breed_bonus": "These ferals receive the Eidetic Memory Merit during character creation. In all forms, they stink heavily of alcohol and sewage.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with alcohol stench",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive crocodile-beast with razor hide",
                "strength": 4,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": -4,
                "size": 7,
                "health_mod": 6,
                "speed_mod": 3,
                "speed_factor": 4,
                "perception_bonus": 0
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Armored crocodile form",
                "strength": 3,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": -4,
                "size": 6,
                "health_mod": 5,
                "speed_mod": 3,
                "speed_factor": 4,
                "perception_bonus": 0
            }
        }
    },
    
    "mendeans": {
        "display_name": "Mendeans",
        "description": "Satyr-like goat people with mystical powers",
        "animal_type": "goat",
        "breed_favors": ["Darksight", "Fang and Claw (horns) 3 (L)", "Territory Bond"],
        "breed_bonus": "Mendeans all have several dots in Occult with three free Skill Specialties. All known Mendeans have been hermaphrodites. This breed has NO War-Beast form; instead, they become goat-headed people and huge, shaggy black goats.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with goatish smell",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "throwback": {
                "display_name": "Throwback",
                "description": "Goat-headed humanoid satyr",
                "strength": 1,
                "dexterity": 0,
                "stamina": 3,
                "manipulation": 0,
                "size": 0,
                "health_mod": 3,
                "speed_mod": 1,
                "speed_factor": 5,
                "perception_bonus": 0
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Huge shaggy black goat",
                "strength": 2,
                "dexterity": 0,
                "stamina": 3,
                "manipulation": -2,
                "size": 5,
                "health_mod": 3,
                "speed_mod": 4,
                "speed_factor": 7,
                "perception_bonus": 0
            }
        }
    },
    
    "olutakami": {
        "display_name": "Olutakami",
        "description": "Dolphin shifters with echolocation and water mastery",
        "animal_type": "dolphin",
        "breed_favors": ["Aquatic", "Echolocation", "Fang and Claw (Bite) 1 (L)", "Waterbreath"],
        "breed_bonus": "Dolphins can ram opponents, inflicting additional three bashing damage. This breed also has the Limbless Aspect (worth no points).",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with dolphin intelligence",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive dolphin-beast hybrid",
                "strength": 3,
                "dexterity": 0,
                "stamina": 3,
                "manipulation": -2,
                "size": 7,
                "health_mod": 5,
                "speed_mod": 6,
                "speed_factor": 8,
                "perception_bonus": 2
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift dolphin form",
                "strength": 2,
                "dexterity": 0,
                "stamina": 2,
                "manipulation": -1,
                "size": 6,
                "health_mod": 3,
                "speed_mod": 5,
                "speed_factor": 8,
                "perception_bonus": 2
            }
        }
    },
    
    "kinno_balo": {
        "display_name": "Kinno'balo",
        "description": "Tiny arrow frog shifters with deadly venom",
        "animal_type": "poison dart frog",
        "breed_favors": ["Size 2", "Venomous", "Truthsight"],
        "breed_bonus": "These tiny creatures receive an additional +4 bonus to dice pools when hiding from enemies of Size 4 or larger.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Small human form with bright coloration",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Larger frog-beast hybrid",
                "strength": 0,
                "dexterity": 2,
                "stamina": 1,
                "manipulation": -5,
                "size": 5,
                "health_mod": 1,
                "speed_mod": 1,
                "speed_factor": 4,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Tiny poison dart frog",
                "strength": -2,
                "dexterity": 0,
                "stamina": -2,
                "manipulation": -2,
                "size_absolute": 2,
                "health_absolute": 4,
                "speed_mod": -2,
                "speed_factor": 3,
                "perception_bonus": 2
            }
        }
    },
    
    "melusinae": {
        "display_name": "Melusinae",
        "description": "Snake shifters with hypnotic song",
        "animal_type": "snake",
        "breed_favors": ["Alarming Alacrity", "Fang and Claw (bite) 2 (L)", "Hypnotic Allure"],
        "breed_bonus": "All Melusinae must buy at least two dots in Expression but receive free Skill Specialty in song. In beast-form, this breed has the Limbless Aspect (worth no points).",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with mesmerizing presence",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Serpentine humanoid hybrid",
                "strength": 2,
                "dexterity": 3,
                "stamina": 0,
                "manipulation": -4,
                "size": 6,
                "health_mod": 1,
                "speed_mod": 5,
                "speed_factor": 5,
                "perception_bonus": 1
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Swift serpent form",
                "strength": 2,
                "dexterity": 4,
                "stamina": 0,
                "manipulation": -5,
                "size": 6,
                "health_mod": 1,
                "speed_mod": 9,
                "speed_factor": 8,
                "perception_bonus": 2
            }
        }
    },
    
    "mimma_lemnua": {
        "display_name": "Mimma Lemnua",
        "description": "Bee shifters with hive-mind swarm form",
        "animal_type": "bee swarm",
        "breed_favors": ["Fang and Claw", "Pack Bond", "Swarm Form"],
        "breed_bonus": "In Primal form, this feral is smaller than Size 1 and can scatter yet stay connected through hive-mind. Swarm ignores Defense when attacking. Inflicts one lethal Health per turn once in place until shapechanger retreats or is harmed by fire/electricity.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form hosting the swarm consciousness",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "primal_beast": {
                "display_name": "Primal Beast (Swarm)",
                "description": "Bee swarm with hive-mind connection",
                "strength_absolute": 1,
                "dexterity_absolute": 5,
                "stamina_absolute": 4,
                "manipulation_absolute": 0,
                "size_absolute": 5,
                "health_absolute": 8,
                "speed_mod": 9,
                "speed_factor": 4,
                "perception_bonus": 0
            }
        }
    },
    
    "yumni": {
        "display_name": "Yumni",
        "description": "Sacred bison shifters with mystical aura",
        "animal_type": "bison",
        "breed_favors": ["Fang and Claw (horns) 3 (L) / (trample) 3 (B)", "Natural Armor 3/2"],
        "breed_bonus": "Yumni project a sacred aura; breeze and mist seem to follow them. With American mystics (especially Native), they receive two automatic successes with Social rolls. Most Yumni have hybrid forms.",
        "forms": {
            "human": {
                "display_name": "Human",
                "description": "Human form with sacred aura",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "health_mod": 0,
                "speed_mod": 0,
                "perception_bonus": 0
            },
            "war_beast": {
                "display_name": "War-Beast",
                "description": "Massive bison-beast warrior",
                "strength": 3,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": -2,
                "size": 6,
                "health_mod": 5,
                "speed_mod": 3,
                "speed_factor": 5,
                "perception_bonus": 0
            },
            "primal_beast": {
                "display_name": "Primal Beast",
                "description": "Sacred white bison form",
                "strength": 3,
                "dexterity": 0,
                "stamina": 4,
                "manipulation": 0,
                "size": 10,
                "health_mod": 9,
                "speed_mod": 6,
                "speed_factor": 8,
                "perception_bonus": 0
            }
        }
    }
}


def get_breed_forms(breed_name):
    """
    Get the forms dictionary for a specific breed.
    
    Args:
        breed_name (str): Name of the breed (case-insensitive)
        
    Returns:
        dict: Forms dictionary, or None if breed not found
    """
    breed_key = breed_name.lower().replace(" ", "_").replace("-", "_")
    breed_data = CHANGING_BREEDS.get(breed_key)
    
    if breed_data:
        return breed_data["forms"]
    return None


def get_breed_info(breed_name):
    """
    Get complete information about a breed.
    
    Args:
        breed_name (str): Name of the breed (case-insensitive)
        
    Returns:
        dict: Breed information, or None if not found
    """
    breed_key = breed_name.lower().replace(" ", "_").replace("-", "_")
    return CHANGING_BREEDS.get(breed_key)


def list_all_breeds():
    """
    Get a list of all available changing breed names.
    
    Returns:
        list: List of breed names
    """
    return [breed["display_name"] for breed in CHANGING_BREEDS.values()]


def get_form_list(breed_name):
    """
    Get a list of available form names for a breed.
    
    Args:
        breed_name (str): Name of the breed
        
    Returns:
        list: List of form names (e.g., ['human', 'war_beast', 'primal_beast'])
    """
    forms = get_breed_forms(breed_name)
    if forms:
        return list(forms.keys())
    return []

