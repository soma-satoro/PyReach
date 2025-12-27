"""
Vampire Disciplines and Powers for Chronicles of Darkness 2nd Edition.

This module contains detailed information about vampire disciplines and their individual powers.
Based on Vampire: The Requiem 2nd Edition.
"""

# Animalism Powers
ANIMALISM_POWERS = {
    "feral_whispers": {
        "name": "Feral Whispers",
        "discipline": "animalism",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Speak with and command animals.",
        "dice_pool": "Manipulation + Animal Ken + Animalism",
        "book": "VTR 2e Corebook p.126"
    },
    "raise_the_familiar": {
        "name": "Raise the Familiar",
        "discipline": "animalism",
        "level": 2,
        "cost": "●",
        "prerequisite": "",
        "description": "Turn dead animal into a loyal proto-vampire.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.126"
    },
    "summon_the_hunt": {
        "name": "Summon the Hunt",
        "discipline": "animalism",
        "level": 3,
        "cost": "●●",
        "prerequisite": "",
        "description": "Call animals to a location or target with spilled blood.",
        "dice_pool": "Presence + Animal Ken + Animalism",
        "book": "VTR 2e Corebook p.126"
    },
    "feral_infection": {
        "name": "Feral Infection",
        "discipline": "animalism",
        "level": 4,
        "cost": "●●",
        "prerequisite": "",
        "description": "Drives animals, humans and vampires into a frenzy.",
        "dice_pool": "Presence + Intimidation + Animalism",
        "book": "VTR 2e Corebook p.126"
    },
    "lord_of_the_land": {
        "name": "Lord of the Land",
        "discipline": "animalism",
        "level": 5,
        "cost": "●●●○ to ●●●●●●●●●○",
        "prerequisite": "",
        "description": "Mark territory as own, intruders take penalties.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.126"
    }
}

# Auspex Powers
AUSPEX_POWERS = {
    "beasts_hackles": {
        "name": "Beast's Hackles",
        "discipline": "auspex",
        "level": 1,
        "cost": "- to ●",
        "prerequisite": "",
        "description": "Answer questions about weaknesses and danger.",
        "dice_pool": "Wits + Empathy + Auspex",
        "book": "VTR 2e Corebook p.128"
    },
    "uncanny_perception": {
        "name": "Uncanny Perception",
        "discipline": "auspex",
        "level": 2,
        "cost": "- to ●",
        "prerequisite": "",
        "description": "Answer questions about the targeted characters secrets.",
        "dice_pool": "Intelligence + Empathy + Auspex",
        "book": "VTR 2e Corebook p.128"
    },
    "spirits_touch": {
        "name": "Spirit's Touch",
        "discipline": "auspex",
        "level": 3,
        "cost": "-",
        "prerequisite": "",
        "description": "Answer questions about the targeted objects secrets.",
        "dice_pool": "Wits + Occult + Auspex",
        "book": "VTR 2e Corebook p.128"
    },
    "lay_open_the_mind": {
        "name": "Lay Open the Mind",
        "discipline": "auspex",
        "level": 4,
        "cost": "●",
        "prerequisite": "",
        "description": "Telepathy and mind-reading. Invoke conditions.",
        "dice_pool": "Intelligence + Socialize + Auspex vs. Resolve + Blood Potency",
        "book": "VTR 2e Corebook p.128"
    },
    "twilight_projection": {
        "name": "Twilight Projection",
        "discipline": "auspex",
        "level": 5,
        "cost": "●●",
        "prerequisite": "",
        "description": "Project own senses into twilight.",
        "dice_pool": "Intelligence + Occult + Auspex",
        "book": "VTR 2e Corebook p.128"
    }
}

# Celerity Powers (Amalgamated Discipline)
CELERITY_POWERS = {
    "celerity": {
        "name": "Celerity",
        "discipline": "celerity",
        "level": "1-5",
        "cost": "(●)",
        "prerequisite": "",
        "description": "Persistent improved defense or dodge. Activate for supernatural speed benefits.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.130",
        "note": "Rated discipline (1-5 dots). Each dot provides passive benefits, can spend Vitae to activate."
    }
}

# Dominate Powers
DOMINATE_POWERS = {
    "mesmerize": {
        "name": "Mesmerize",
        "discipline": "dominate",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Imposes 'Mesmerized' Condition. Control with short commands.",
        "dice_pool": "Intelligence + Expression + Dominate vs. Resolve + Blood Potency",
        "book": "VTR 2e Corebook p.131"
    },
    "iron_edict": {
        "name": "Iron Edict",
        "discipline": "dominate",
        "level": 2,
        "cost": "(●)",
        "prerequisite": "Mesmerized",
        "description": "Imposes 'Dominated' condition. Give long, detailed commands.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.131"
    },
    "entombed_command": {
        "name": "Entombed Command",
        "discipline": "dominate",
        "level": 3,
        "cost": "-",
        "prerequisite": "Mesmerized",
        "description": "Establish triggers for other dominate powers.",
        "dice_pool": "Intelligence + Subterfuge + Dominate - victim's Resolve",
        "book": "VTR 2e Corebook p.131"
    },
    "the_lying_mind": {
        "name": "The Lying Mind",
        "discipline": "dominate",
        "level": 4,
        "cost": "●●",
        "prerequisite": "Mesmerized",
        "description": "Imposes 'Amnesia' or 'False Memories' condition.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.131"
    },
    "possession": {
        "name": "Possession",
        "discipline": "dominate",
        "level": 5,
        "cost": "●○",
        "prerequisite": "Mesmerized",
        "description": "Control victims body.",
        "dice_pool": "Intelligence + Intimidation + Dominate - victim's Resolve",
        "book": "VTR 2e Corebook p.131"
    }
}

# Majesty Powers
MAJESTY_POWERS = {
    "awe": {
        "name": "Awe",
        "discipline": "majesty",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Become center of attention. Subjects become 'Awed'.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.133"
    },
    "confidant": {
        "name": "Confidant",
        "discipline": "majesty",
        "level": 2,
        "cost": "-",
        "prerequisite": "Awed",
        "description": "Imposes 'Charmed' condition.",
        "dice_pool": "Presence + Empathy + Majesty vs. Resolve + Blood Potency",
        "book": "VTR 2e Corebook p.133"
    },
    "green_eyes": {
        "name": "Green Eyes",
        "discipline": "majesty",
        "level": 3,
        "cost": "●",
        "prerequisite": "Charmed or Enthralled",
        "description": "Shift emotions by spending Vitae. Subjects will perform requests.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.133"
    },
    "loyalty": {
        "name": "Loyalty",
        "discipline": "majesty",
        "level": 4,
        "cost": "●●",
        "prerequisite": "Charmed",
        "description": "Imposes 'Enthralled' condition.",
        "dice_pool": "Manipulation + Empathy + Majesty vs. Resolve + Blood Potency",
        "book": "VTR 2e Corebook p.133"
    },
    "idol": {
        "name": "Idol",
        "discipline": "majesty",
        "level": 5,
        "cost": "(●●○)",
        "prerequisite": "Awed",
        "description": "Enhances Awe's effect (free) or immediately (at cost). Cannot be harmed.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.133"
    }
}

# Nightmare Powers
NIGHTMARE_POWERS = {
    "dread_presence": {
        "name": "Dread Presence",
        "discipline": "nightmare",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Conjure brief illusions. Improves intimidation. Prevents foes spending willpower.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.135"
    },
    "face_of_the_beast": {
        "name": "Face of the Beast",
        "discipline": "nightmare",
        "level": 2,
        "cost": "●",
        "prerequisite": "",
        "description": "Imposes 'Frightened' condition. Causes fleeing.",
        "dice_pool": "Presence + Empathy + Nightmare vs. Composure + Blood Potency",
        "book": "VTR 2e Corebook p.135"
    },
    "grand_delusion": {
        "name": "Grand Delusion",
        "discipline": "nightmare",
        "level": 3,
        "cost": "●●",
        "prerequisite": "",
        "description": "Imposes 'Delusional' condition.",
        "dice_pool": "Manipulation + Empathy + Nightmare vs. Composure + Blood Potency",
        "book": "VTR 2e Corebook p.135"
    },
    "waking_nightmare": {
        "name": "Waking Nightmare",
        "discipline": "nightmare",
        "level": 4,
        "cost": "●",
        "prerequisite": "",
        "description": "Create and control hallucinations.",
        "dice_pool": "Presence + Empathy + Nightmare vs. highest Composure + Blood Potency in group",
        "book": "VTR 2e Corebook p.135"
    },
    "mortal_terror": {
        "name": "Mortal Terror",
        "discipline": "nightmare",
        "level": 5,
        "cost": "●○",
        "prerequisite": "Frightened or Delusional",
        "description": "Imposes 'Broken' condition. Do lethal damage with fear.",
        "dice_pool": "Presence + Intimidation + Nightmare - victim's Composure",
        "book": "VTR 2e Corebook p.135"
    }
}

# Obfuscate Powers
OBFUSCATE_POWERS = {
    "face_in_the_crowd": {
        "name": "Face in the Crowd",
        "discipline": "obfuscate",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Blend into surroundings, visible but unnoticeable. Hides predatory aura.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.137"
    },
    "touch_of_shadow": {
        "name": "Touch of Shadow",
        "discipline": "obfuscate",
        "level": 2,
        "cost": "●",
        "prerequisite": "",
        "description": "Cast Face in the Crowd on object or person.",
        "dice_pool": "Wits + Larceny + Obfuscate",
        "book": "VTR 2e Corebook p.137"
    },
    "cloak_of_the_night": {
        "name": "Cloak of the Night",
        "discipline": "obfuscate",
        "level": 3,
        "cost": "●",
        "prerequisite": "",
        "description": "Become invisible.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.137"
    },
    "the_familiar_stranger": {
        "name": "The Familiar Stranger",
        "discipline": "obfuscate",
        "level": 4,
        "cost": "●●",
        "prerequisite": "",
        "description": "Disguise self or other as a desired person.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.137"
    },
    "oubliette": {
        "name": "Oubliette",
        "discipline": "obfuscate",
        "level": 5,
        "cost": "●●●○ to ●●●●●●●●●○",
        "prerequisite": "",
        "description": "Designate an area. May use obfuscate at a distance on anything in the area at discount.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.137"
    }
}

# Protean Powers
PROTEAN_POWERS = {
    "unmarked_grave": {
        "name": "Unmarked Grave",
        "discipline": "protean",
        "level": 1,
        "cost": "Varies",
        "prerequisite": "",
        "description": "Merge with soil.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.139"
    },
    "predatory_aspect": {
        "name": "Predatory Aspect",
        "discipline": "protean",
        "level": 2,
        "cost": "●",
        "prerequisite": "",
        "description": "Take on animal traits.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.139"
    },
    "beasts_skin": {
        "name": "Beast's Skin",
        "discipline": "protean",
        "level": 3,
        "cost": "●●",
        "prerequisite": "",
        "description": "Transform into predatory animal.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.139"
    },
    "unnatural_aspect": {
        "name": "Unnatural Aspect",
        "discipline": "protean",
        "level": 4,
        "cost": "●",
        "prerequisite": "",
        "description": "Take on a horrific trait.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.139"
    },
    "primeval_miasma": {
        "name": "Primeval Miasma",
        "discipline": "protean",
        "level": 5,
        "cost": "●●●",
        "prerequisite": "",
        "description": "Transform into smoke.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.139"
    }
}

# Resilience Powers (Amalgamated Discipline)
RESILIENCE_POWERS = {
    "resilience": {
        "name": "Resilience",
        "discipline": "resilience",
        "level": "1-5",
        "cost": "(●)",
        "prerequisite": "",
        "description": "Downgrade damage and increase stamina. Improves armor and defenses.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.141",
        "note": "Rated discipline (1-5 dots). Each dot provides passive benefits, can spend Vitae to activate."
    }
}

# Vigor Powers (Amalgamated Discipline)
VIGOR_POWERS = {
    "vigor": {
        "name": "Vigor",
        "discipline": "vigor",
        "level": "1-5",
        "cost": "(●)",
        "prerequisite": "",
        "description": "Improve strength.",
        "dice_pool": "-",
        "book": "VTR 2e Corebook p.141",
        "note": "Rated discipline (1-5 dots). Each dot provides passive benefits, can spend Vitae to activate."
    }
}

# ==================== COILS OF THE DRAGON ====================
# Ordo Dracul unique disciplines organized by Mystery

# Coils of the Dragon - Mystery of the Ascendant
COILS_ASCENDANT = {
    "surmounting_the_daysleep": {
        "name": "Surmounting the Daysleep",
        "discipline": "coils_of_the_dragon",
        "mystery": "ascendant",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Ignore the call of daysleep when the Blush of Life is active.",
        "dice_pool": "-",
        "book": "VTR 2e p.155"
    },
    "the_warm_face": {
        "name": "The Warm Face",
        "discipline": "coils_of_the_dragon",
        "mystery": "ascendant",
        "level": 2,
        "cost": "-",
        "prerequisite": "",
        "description": "The Blush of Life lasts a full day.",
        "dice_pool": "-",
        "book": "VTR 2e p.156"
    },
    "conquer_the_red_fear": {
        "name": "Conquer the Red Fear",
        "discipline": "coils_of_the_dragon",
        "mystery": "ascendant",
        "level": 3,
        "cost": "-",
        "prerequisite": "",
        "description": "Fire and sunlight don't provoke frenzy.",
        "dice_pool": "-",
        "book": "VTR 2e p.156"
    },
    "peace_with_the_flame": {
        "name": "Peace with the Flame",
        "discipline": "coils_of_the_dragon",
        "mystery": "ascendant",
        "level": 4,
        "cost": "-",
        "prerequisite": "",
        "description": "Take lethal damage from fire when the Blush of Life is active. Resilience reduces this damage to bashing.",
        "dice_pool": "-",
        "book": "VTR 2e p.156"
    },
    "suns_forgotten_kiss": {
        "name": "Sun's Forgotten Kiss",
        "discipline": "coils_of_the_dragon",
        "mystery": "ascendant",
        "level": 5,
        "cost": "●",
        "prerequisite": "",
        "description": "Feed the Blush of Life with Vitae to pass under sunlight as if your Blood Potency were reduced.",
        "dice_pool": "-",
        "book": "VTR 2e p.156"
    }
}

# Coils of the Dragon - Mystery of the Quintessence
COILS_QUINTESSENCE = {
    "forever_mine": {
        "name": "Forever Mine",
        "discipline": "coils_of_the_dragon",
        "mystery": "quintessence",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Claim a domain you've been a presence in for a hundred years. Sense Kindred feeding or killing in your domain without permission. You may lash out at them remotely with the Predatory Aura.",
        "dice_pool": "-",
        "book": "Thousand Years p.81"
    },
    "home_turf": {
        "name": "Home Turf",
        "discipline": "coils_of_the_dragon",
        "mystery": "quintessence",
        "level": 2,
        "cost": "-",
        "prerequisite": "",
        "description": "Residents of your domain must spend Willpower to resist your feeding.",
        "dice_pool": "-",
        "book": "Thousand Years p.81"
    },
    "smother": {
        "name": "Smother",
        "discipline": "coils_of_the_dragon",
        "mystery": "quintessence",
        "level": 3,
        "cost": "●●●",
        "prerequisite": "",
        "description": "Suppress the natural ignition of fires in your domain. +1 to resist or contest supernatural flames there, and spend three Vitae to exert a Clash of Wills to extinguish them.",
        "dice_pool": "-",
        "book": "Thousand Years p.82"
    },
    "in_the_motherlands_arms": {
        "name": "In the Motherland's Arms",
        "discipline": "coils_of_the_dragon",
        "mystery": "quintessence",
        "level": 4,
        "cost": "-",
        "prerequisite": "",
        "description": "Apply half your Blood Potency as a supernatural Safe Place and Haven effect when sleeping within your domain. In a Haven, add +1 each to the effective Merit ratings.",
        "dice_pool": "-",
        "book": "Thousand Years p.82"
    },
    "fingers_on_a_dead_pulse": {
        "name": "Fingers on a Dead Pulse",
        "discipline": "coils_of_the_dragon",
        "mystery": "quintessence",
        "level": 5,
        "cost": "●",
        "prerequisite": "",
        "description": "Spend Vitae to intuit a domain resident's Vice and ignominious Conditions. Experience blood sympathy visions tied to your domain as a whole.",
        "dice_pool": "-",
        "book": "Thousand Years p.82"
    }
}

# Coils of the Dragon - Mystery of the Voivode
COILS_VOIVODE = {
    "taste_of_fealty": {
        "name": "Taste of Fealty",
        "discipline": "coils_of_the_dragon",
        "mystery": "voivode",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Your blood becomes the focus of an addiction twice as powerful as normal.",
        "dice_pool": "-",
        "book": "VTR 2e p.158"
    },
    "into_the_fold": {
        "name": "Into the Fold",
        "discipline": "coils_of_the_dragon",
        "mystery": "voivode",
        "level": 2,
        "cost": "-",
        "prerequisite": "",
        "description": "Form blood sympathy through the Vinculum.",
        "dice_pool": "-",
        "book": "VTR 2e p.158"
    },
    "call_to_serve": {
        "name": "Call to Serve",
        "discipline": "coils_of_the_dragon",
        "mystery": "voivode",
        "level": 3,
        "cost": "-",
        "prerequisite": "",
        "description": "Share more Vitae to advance the Vinculum multiple steps at once.",
        "dice_pool": "-",
        "book": "VTR 2e p.158"
    },
    "voivode_undisputed": {
        "name": "Voivode Undisputed",
        "discipline": "coils_of_the_dragon",
        "mystery": "voivode",
        "level": 4,
        "cost": "-",
        "prerequisite": "",
        "description": "Deny blood sympathy bonuses to target you with Disciplines, and add them to contest bonding and your thralls' Predatory Auras.",
        "dice_pool": "-",
        "book": "VTR 2e p.158"
    },
    "the_vast_dynasty": {
        "name": "The Vast Dynasty",
        "discipline": "coils_of_the_dragon",
        "mystery": "voivode",
        "level": 5,
        "cost": "-",
        "prerequisite": "",
        "description": "The Embrace risks but no longer guarantees detachment.",
        "dice_pool": "-",
        "book": "VTR 2e p.158"
    }
}

# Coils of the Dragon - Mystery of the Wyrm
COILS_WYRM = {
    "stir_the_beast": {
        "name": "Stir the Beast",
        "discipline": "coils_of_the_dragon",
        "mystery": "wyrm",
        "level": 1,
        "cost": "○",
        "prerequisite": "",
        "description": "Spend Willpower to enter a directed frenzy.",
        "dice_pool": "-",
        "book": "VTR 2e p.157"
    },
    "beasts_hunger": {
        "name": "Beast's Hunger",
        "discipline": "coils_of_the_dragon",
        "mystery": "wyrm",
        "level": 2,
        "cost": "-",
        "prerequisite": "",
        "description": "During frenzy, use Kindred Senses and the Predatory Aura as if your Blood Potency were increased by your dots in this Coil.",
        "dice_pool": "-",
        "book": "VTR 2e p.157"
    },
    "leash_the_beast": {
        "name": "Leash the Beast",
        "discipline": "coils_of_the_dragon",
        "mystery": "wyrm",
        "level": 3,
        "cost": "-",
        "prerequisite": "",
        "description": "Ride the wave without spending Willpower, with a bonus from dots in this Coil.",
        "dice_pool": "-",
        "book": "VTR 2e p.157"
    },
    "beasts_power": {
        "name": "Beast's Power",
        "discipline": "coils_of_the_dragon",
        "mystery": "wyrm",
        "level": 4,
        "cost": "-",
        "prerequisite": "",
        "description": "Lock an oncoming frenzy to last until its goal is complete to add Blood Potency to your Defense, Health, and Speed during the frenzy.",
        "dice_pool": "-",
        "book": "VTR 2e p.157"
    },
    "eternal_frenzy": {
        "name": "Eternal Frenzy",
        "discipline": "coils_of_the_dragon",
        "mystery": "wyrm",
        "level": 5,
        "cost": "-",
        "prerequisite": "",
        "description": "During frenzy, don't fall torpid from damage. When you end a scene in a frenzy, choose whether to extend it into the next.",
        "dice_pool": "-",
        "book": "VTR 2e p.157"
    }
}

# Coils of the Dragon - Mystery of Zirnitra
COILS_ZIRNITRA = {
    "opening_the_third_eye": {
        "name": "Opening the Third Eye",
        "discipline": "coils_of_the_dragon",
        "mystery": "zirnitra",
        "level": 1,
        "cost": "●",
        "prerequisite": "",
        "description": "Each dot in this Coil unlocks access to a mortal Supernatural Merit, which must be fed with Vitae and risk dramatic failure.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.200"
    },
    "unleash_the_mind": {
        "name": "Unleash the Mind",
        "discipline": "coils_of_the_dragon",
        "mystery": "zirnitra",
        "level": 2,
        "cost": "-",
        "prerequisite": "",
        "description": "Willpower costs for Supernatural Merits don't count for your per-turn Willpower use.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.200"
    },
    "embolden_potential": {
        "name": "Embolden Potential",
        "discipline": "coils_of_the_dragon",
        "mystery": "zirnitra",
        "level": 3,
        "cost": "-",
        "prerequisite": "",
        "description": "Supernatural Merits cost fewer experiences and no Vitae, and may be enhanced with Physical Intensity.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.200"
    },
    "the_dragons_breath": {
        "name": "The Dragon's Breath",
        "discipline": "coils_of_the_dragon",
        "mystery": "zirnitra",
        "level": 4,
        "cost": "○",
        "prerequisite": "",
        "description": "Supernatural Merits no longer court dramatic failure, and Willpower can be spent for extra bonus dice.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.200"
    },
    "ascendancy": {
        "name": "Ascendancy",
        "discipline": "coils_of_the_dragon",
        "mystery": "zirnitra",
        "level": 5,
        "cost": "Aggravated",
        "prerequisite": "",
        "description": "Suffer aggravated damage to grant the rote quality to a Supernatural Merit. Supernatural Merits no longer need to be unlocked by Coil dots.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.200"
    }
}

# Coils of the Dragon - Mystery of Ziva
COILS_ZIVA = {
    "denying_the_bane": {
        "name": "Denying the Bane",
        "discipline": "coils_of_the_dragon",
        "mystery": "ziva",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Banes aside from fire and sunlight treat your Humanity as increased by dots in this Coil.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.201"
    },
    "buttress_the_soul": {
        "name": "Buttress the Soul",
        "discipline": "coils_of_the_dragon",
        "mystery": "ziva",
        "level": 2,
        "cost": "●",
        "prerequisite": "",
        "description": "Spend Vitae for a bonus against detachment.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.201"
    },
    "enliven_the_anima": {
        "name": "Enliven the Anima",
        "discipline": "coils_of_the_dragon",
        "mystery": "ziva",
        "level": 3,
        "cost": "○",
        "prerequisite": "",
        "description": "Spend Willpower to take Raptured instead of a detachment Condition.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.201"
    },
    "embracing_the_banes": {
        "name": "Embracing the Banes",
        "discipline": "coils_of_the_dragon",
        "mystery": "ziva",
        "level": 4,
        "cost": "-",
        "prerequisite": "",
        "description": "Callous your Humanity with up to your Willpower in banes.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.201"
    },
    "shedding_the_beasts_skin": {
        "name": "Shedding the Beast's Skin",
        "discipline": "coils_of_the_dragon",
        "mystery": "ziva",
        "level": 5,
        "cost": "○",
        "prerequisite": "",
        "description": "Spend Willpower to shed your vampiric skin, temporarily becoming a living mortal.",
        "dice_pool": "-",
        "book": "Secrets of the Covenants p.201"
    }
}

# All Coils combined
ALL_COILS = {
    **COILS_ASCENDANT,
    **COILS_QUINTESSENCE,
    **COILS_VOIVODE,
    **COILS_WYRM,
    **COILS_ZIRNITRA,
    **COILS_ZIVA
}

# ==================== BLOODLINE DISCIPLINES ====================

# Cachexy (Morbus bloodline)
CACHEXY_POWERS = {
    "diagnose": {
        "name": "Diagnose",
        "discipline": "cachexy",
        "bloodline": "morbus",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Sense carriers of disease.",
        "dice_pool": "Intelligence + Medicine + Cachexy",
        "book": "Danse Macabre p.112"
    },
    "contaminate": {
        "name": "Contaminate",
        "discipline": "cachexy",
        "bloodline": "morbus",
        "level": 2,
        "cost": "●",
        "prerequisite": "",
        "description": "Render a space a contagion vector for a given disease.",
        "dice_pool": "-",
        "book": "Danse Macabre p.112"
    },
    "inflame": {
        "name": "Inflame",
        "discipline": "cachexy",
        "bloodline": "morbus",
        "level": 3,
        "cost": "●",
        "prerequisite": "",
        "description": "Inflict penalties by exacerbating a disease's symptoms.",
        "dice_pool": "Wits + Survival + Cachexy - Stamina",
        "book": "Danse Macabre p.112"
    },
    "plague_bearer": {
        "name": "Plague-Bearer",
        "discipline": "cachexy",
        "bloodline": "morbus",
        "level": 4,
        "cost": "●/turn",
        "prerequisite": "",
        "description": "Quickly infect nearby victims with a given disease.",
        "dice_pool": "Intelligence + Medicine + Cachexy",
        "book": "Danse Macabre p.112"
    },
    "accelerate_disease": {
        "name": "Accelerate Disease",
        "discipline": "cachexy",
        "bloodline": "morbus",
        "level": 5,
        "cost": "○",
        "prerequisite": "",
        "description": "Inflict lethal damage by worsening even a mild sickness.",
        "dice_pool": "Wits + Survival + Cachexy - Stamina",
        "book": "Danse Macabre p.112"
    }
}

# Crochan (Bron bloodline)
CROCHAN_POWERS = {
    "swift_flows_the_blood": {
        "name": "Swift Flows the Blood",
        "discipline": "crochan",
        "bloodline": "bron",
        "level": 1,
        "cost": "●",
        "prerequisite": "",
        "description": "Spend up to your successes in additional Vitae this turn on healing.",
        "dice_pool": "Intelligence + Medicine + Crochan",
        "book": "Dark Eras 2 p.119"
    },
    "blooding_the_hunter": {
        "name": "Blooding the Hunter",
        "discipline": "crochan",
        "bloodline": "bron",
        "level": 2,
        "cost": "●",
        "prerequisite": "",
        "description": "Sample your quarry's blood to apply successes as a bonus for the night to track and pursue them.",
        "dice_pool": "Wits + Survival + Crochan",
        "book": "Dark Eras 2 p.119"
    },
    "sealing_the_covenant": {
        "name": "Sealing the Covenant",
        "discipline": "crochan",
        "bloodline": "bron",
        "level": 3,
        "cost": "○, ●/oathmate",
        "prerequisite": "",
        "description": "Mix blood to swear a shared oath of loyalty, taking a symbol or focus as an added Touchstone.",
        "dice_pool": "-",
        "book": "Dark Eras 2 p.119"
    },
    "blood_of_my_blood": {
        "name": "Blood of My Blood",
        "discipline": "crochan",
        "bloodline": "bron",
        "level": 4,
        "cost": "●+ (○)",
        "prerequisite": "",
        "description": "Touch blood to a subject to spend Vitae to heal them immediately.",
        "dice_pool": "-",
        "book": "Dark Eras 2 p.119"
    },
    "conquering_the_challenge_of_the_axe": {
        "name": "Conquering the Challenge of the Axe",
        "discipline": "crochan",
        "bloodline": "bron",
        "level": 5,
        "cost": "●●○",
        "prerequisite": "",
        "description": "Swear not to be moved, and suffer no damage for the scene so long as you take no aggressive action.",
        "dice_pool": "-",
        "book": "Dark Eras 2 p.119"
    }
}

# Dead Signal (Jharana bloodline)
DEAD_SIGNAL_POWERS = {
    "analyze_signal": {
        "name": "Analyze Signal",
        "discipline": "dead_signal",
        "bloodline": "jharana",
        "level": 1,
        "cost": "-",
        "prerequisite": "",
        "description": "Diagnose Radio Sickness and stigmata.",
        "dice_pool": "Wits + Composure + Dead Signal",
        "book": "Night Horrors: Shunned by the Moon p.23"
    },
    "minor_repairs": {
        "name": "Minor Repairs",
        "discipline": "dead_signal",
        "bloodline": "jharana",
        "level": 2,
        "cost": "●+",
        "prerequisite": "",
        "description": "Heal a subject's non-Persistent Condition or bashing damage per Vitae.",
        "dice_pool": "Wits + Medicine + Dead Signal",
        "book": "Night Horrors: Shunned by the Moon p.23"
    },
    "receive_transmission": {
        "name": "Receive Transmission",
        "discipline": "dead_signal",
        "bloodline": "jharana",
        "level": 3,
        "cost": "○",
        "prerequisite": "",
        "description": "Shoulder another vampire's Radio Sickness for a night.",
        "dice_pool": "Intelligence + Occult + Dead Signal",
        "book": "Night Horrors: Shunned by the Moon p.23"
    },
    "configure_receiver": {
        "name": "Configure Receiver",
        "discipline": "dead_signal",
        "bloodline": "jharana",
        "level": 4,
        "cost": "●●/dot, ○",
        "prerequisite": "",
        "description": "Anoint a subject with blood to enhance their Skills for a night.",
        "dice_pool": "Intelligence + Medicine + Dead Signal",
        "book": "Night Horrors: Shunned by the Moon p.23"
    },
    "broadcast": {
        "name": "Broadcast",
        "discipline": "dead_signal",
        "bloodline": "jharana",
        "level": 5,
        "cost": "●",
        "prerequisite": "",
        "description": "Issue a friendly summons to beings touched by the God-Machine.",
        "dice_pool": "Manipulation + Persuasion + Dead Signal",
        "book": "Night Horrors: Shunned by the Moon p.23"
    }
}

# All Bloodline Disciplines combined
ALL_BLOODLINE_DISCIPLINES = {
    **CACHEXY_POWERS,
    **CROCHAN_POWERS,
    **DEAD_SIGNAL_POWERS
}

# ==================== DEVOTIONS ====================
# Devotions are combination discipline powers

# General Devotions (available to all)
GENERAL_DEVOTIONS = {
    "aerial_cocoon": {
        "name": "Aerial Cocoon",
        "type": "devotion",
        "prerequisites": "protean:1",
        "xp_cost": 1,
        "cost": "N/A",
        "dice_pool": "N/A",
        "description": "Use Unmarked Grave between walls of concrete or metal, turning it into a protective cocoon.",
        "book": "Gods and Monsters p.133"
    },
    "annals_of_death": {
        "name": "Annals of Death",
        "type": "devotion",
        "prerequisites": "auspex:4",
        "xp_cost": 1,
        "cost": "N/A",
        "dice_pool": "Intelligence + Occult + Auspex",
        "description": "Answer questions about death in a location. Can foresee deaths.",
        "book": "Thousand Years p.72"
    },
    "bend_space": {
        "name": "Bend Space",
        "type": "devotion",
        "prerequisites": "auspex:2, celerity:4",
        "xp_cost": 4,
        "cost": "2 blood, 1 willpower",
        "dice_pool": "N/A",
        "description": "Teleport anywhere you can see directly. With willpower, anywhere you have visited or seen before.",
        "book": "Gods and Monsters p.134"
    },
    "best_served_cold": {
        "name": "Best Served Cold",
        "type": "devotion",
        "prerequisites": "vigor:3",
        "xp_cost": 1,
        "cost": "2 blood",
        "dice_pool": "Stamina + Athletics + Vigor",
        "description": "Until the end of the chapter or the person who harmed you is defeated, +3 to attack them. Can only have one target at a time.",
        "book": "Gods and Monsters p.135"
    },
    "between_the_walls": {
        "name": "Between the Walls",
        "type": "devotion",
        "prerequisites": "protean:3, resilience:1",
        "xp_cost": 2,
        "cost": "-",
        "dice_pool": "N/A",
        "description": "Fit into spaces down to size 2, moving at your normal speed. Add Protean to ambush rolls.",
        "book": "Gods and Monsters p.134"
    },
    "blood_scenting": {
        "name": "Blood Scenting",
        "type": "devotion",
        "prerequisites": "auspex:3",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "Wits + Composure + Auspex",
        "description": "Identify the target's clan, blood potency and disciplines.",
        "book": "Gods and Monsters p.136"
    },
    "blood_scenting_crown_games": {
        "name": "Blood Scenting (Crown Games)",
        "type": "devotion",
        "prerequisites": "auspex:2",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "Wits + Composure + Auspex",
        "description": "Crown Games variant. Identify if the target's blood is divine.",
        "book": "Gods and Monsters p.133"
    },
    "body_of_will": {
        "name": "Body of Will",
        "type": "devotion",
        "prerequisites": "resilience:3, vigor:1",
        "xp_cost": 2,
        "cost": "2 blood",
        "dice_pool": "Stamina + Survival + Resilience",
        "description": "Ignore wound penalties, free Vigor effects.",
        "book": "VTR 2e p.142"
    },
    "bones_of_the_mountain": {
        "name": "Bones of the Mountain",
        "type": "devotion",
        "prerequisites": "protean:4, resilience:3, vigor:2",
        "xp_cost": 5,
        "cost": "3 blood",
        "dice_pool": "Stamina + Survival + Protean",
        "description": "Become living stone for a turn, adding Protean to Resilience, dealing lethal unarmed, and activating Resilience and Vigor for free.",
        "book": "Thousand Years p.73"
    },
    "celebrity": {
        "name": "Celebrity",
        "type": "devotion",
        "prerequisites": "majesty:2",
        "xp_cost": 2,
        "cost": "3 blood",
        "dice_pool": "Presence + Empathy + Majesty vs Resolve + Tolerance",
        "description": "Have a fan talk about you, giving you a temporary dot of Allies, Fame, Herd, Retainer, Staff or Status.",
        "book": "Thousand Years p.73"
    },
    "chain_of_command": {
        "name": "Chain of Command",
        "type": "devotion",
        "prerequisites": "dominate:3, vigor:1",
        "xp_cost": 2,
        "cost": "2 blood",
        "dice_pool": "Intelligence + Persuasion + Dominate vs Resolve + Tolerance",
        "description": "Dominate effects activate later.",
        "book": "VTR 2e p.142"
    },
    "cloak_the_gathering": {
        "name": "Cloak the Gathering",
        "type": "devotion",
        "prerequisites": "obfuscate:4",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Make a group disappear.",
        "book": "VTR 2e p.142"
    },
    "conditioning": {
        "name": "Conditioning",
        "type": "devotion",
        "prerequisites": "dominate:4",
        "xp_cost": 2,
        "cost": "2 blood",
        "dice_pool": "Wits + Subterfuge + Dominate vs Resolve + Tolerance",
        "description": "Suppress the target's will, commanding them even without Dominate active.",
        "book": "VTR 2e p.143"
    },
    "consumption": {
        "name": "Consumption",
        "type": "devotion",
        "prerequisites": "dominate:5",
        "xp_cost": 4,
        "cost": "1 blood, 1 willpower",
        "dice_pool": "Intelligence + Intimidation + Dominate vs Resolve",
        "description": "Possess victim over any distance with just your voice.",
        "book": "Thousand Years p.74"
    },
    "cross_contamination": {
        "name": "Cross-Contamination",
        "type": "devotion",
        "prerequisites": "majesty:1, nightmare:1",
        "xp_cost": 1,
        "cost": "N/A",
        "dice_pool": "Presence + Empathy + lower Discipline",
        "description": "Spread an unsettling fascination that commands attention and lowers social defenses.",
        "book": "VTR 2e p.143"
    },
    "crush_of_years": {
        "name": "Crush of Years",
        "type": "devotion",
        "prerequisites": "nightmare:4, majesty:2",
        "xp_cost": 3,
        "cost": "3 blood, 1 willpower",
        "dice_pool": "Presence + Expression + Nightmare vs Composure + Tolerance",
        "description": "Press the weight of existing for centuries upon the target.",
        "book": "Thousand Years p.74"
    },
    "cult_of_personality": {
        "name": "Cult of Personality",
        "type": "devotion",
        "prerequisites": "majesty:4, vigor:2",
        "xp_cost": 4,
        "cost": "10 blood",
        "dice_pool": "Presence + Socialize + Majesty",
        "description": "Enthrall a crowd in a mass display of Majesty.",
        "book": "VTR 2e p.143"
    },
    "cybernetic_mimic": {
        "name": "Cybernetic Mimic",
        "type": "devotion",
        "prerequisites": "protean:2, vigor:2",
        "xp_cost": 2,
        "cost": "1 blood to 3 blood",
        "dice_pool": "N/A",
        "description": "Ascendancy. Spend a scene studying a cybernetic individual. Afterwards copy its abilities by paying Vitae based on the level of enhancements.",
        "book": "Gods and Monsters p.134"
    },
    "dead_mans_reprieve": {
        "name": "Dead Man's Reprieve",
        "type": "devotion",
        "prerequisites": "obfuscate:1",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Occult + Obfuscate",
        "description": "Brews a precious reagent into a ritual bath which cloaks the presence of bathers.",
        "book": "Thousand Years p.128"
    },
    "distant_control": {
        "name": "Distant Control",
        "type": "devotion",
        "prerequisites": "dominate:4, vigor:2",
        "xp_cost": 3,
        "cost": "2 blood",
        "dice_pool": "N/A",
        "description": "As long as you know of the target's location, you can issue commands or make social rolls by speaking into their mind for a scene.",
        "book": "Gods and Monsters p.135"
    },
    "enchantment": {
        "name": "Enchantment",
        "type": "devotion",
        "prerequisites": "majesty:4, obfuscate:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Empathy + Majesty vs Composure + Tolerance",
        "description": "Enthrall the target with another subject instead of yourself.",
        "book": "VTR 2e p.143"
    },
    "enfeebling_aura": {
        "name": "Enfeebling Aura",
        "type": "devotion",
        "prerequisites": "majesty:1, resilience:1",
        "xp_cost": 3,
        "cost": "1 blood",
        "dice_pool": "Presence + Intimidation + Majesty vs Composure + Tolerance",
        "description": "Temporarily sacrifice Majesty dots to suppress a target's dots of Celerity, Resilience or Vigor.",
        "book": "VTR 2e p.143"
    },
    "flesh_form": {
        "name": "Flesh Form",
        "type": "devotion",
        "prerequisites": "protean:2, resilience:1",
        "xp_cost": 1,
        "cost": "3 blood/day",
        "dice_pool": "N/A",
        "description": "Consume the body of a human to imitate their look and voice, aging at a rate of a decade a week.",
        "book": "Night Horrors: Shunned by the Moon p.97"
    },
    "flush_out": {
        "name": "Flush Out",
        "type": "devotion",
        "prerequisites": "dominate:1, nightmare:3",
        "xp_cost": 2,
        "cost": "2 blood",
        "dice_pool": "Presence + Subterfuge + Nightmare vs highest Composure + Tolerance",
        "description": "Target gains Frightened and flees their hiding space to a location you want.",
        "book": "Gods and Monsters p.136"
    },
    "foul_grave": {
        "name": "Foul Grave",
        "type": "devotion",
        "prerequisites": "protean:1, nightmare:1",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Exert the Predatory Aura while in your Unmarked Grave.",
        "book": "VTR 2e p.144"
    },
    "force_of_nature": {
        "name": "Force of Nature",
        "type": "devotion",
        "prerequisites": "protean:4, resilience:4, vigor:2",
        "xp_cost": 5,
        "cost": "8 blood",
        "dice_pool": "N/A",
        "description": "Make use of Beast's Skin and Protean Aspects freely. Shift Physical Attributes.",
        "book": "VTR 2e p.144"
    },
    "gargoyles_vigilance": {
        "name": "Gargoyle's Vigilance",
        "type": "devotion",
        "prerequisites": "resilience:2, auspex:1",
        "xp_cost": 1,
        "cost": "1 blood, 1 willpower",
        "dice_pool": "N/A",
        "description": "Remain static within your Haven to monitor it with Auspex, taking bonuses to defend from intruders. With Willpower, monitor while asleep.",
        "book": "VTR 2e p.144"
    },
    "gargoyles_vigilance_advanced": {
        "name": "Gargoyle's Vigilance (Advanced)",
        "type": "devotion",
        "prerequisites": "protean:5, resilience:2, auspex:1",
        "xp_cost": 4,
        "cost": "1 blood, 1 willpower",
        "dice_pool": "N/A",
        "description": "As Gargoyle's Vigilance, but you may become a stone statue, immune to fire and sunlight.",
        "book": "VTR 2e p.144"
    },
    "ghost_skin": {
        "name": "Ghost Skin",
        "type": "devotion",
        "prerequisites": "auspex:5",
        "xp_cost": 2,
        "cost": "1 willpower",
        "dice_pool": "N/A",
        "description": "Perceive and interact with ghosts while using Twilight Projection.",
        "book": "Night Horrors: Shunned by the Moon p.85"
    },
    "hint_of_fear": {
        "name": "Hint of Fear",
        "type": "devotion",
        "prerequisites": "celerity:2, nightmare:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Use Face of the Beast reflexively.",
        "book": "VTR 2e p.145"
    },
    "juggernauts_gait": {
        "name": "Juggernaut's Gait",
        "type": "devotion",
        "prerequisites": "resilience:5, vigor:2",
        "xp_cost": 4,
        "cost": "5 blood",
        "dice_pool": "N/A",
        "description": "Negate all damage for a turn.",
        "book": "VTR 2e p.145"
    },
    "kin_maker": {
        "name": "Kin Maker",
        "type": "devotion",
        "prerequisites": "dominate:5, protean:2",
        "xp_cost": 4,
        "cost": "10 blood, 1 willpower",
        "dice_pool": "N/A",
        "description": "Used by the Pijavica to infect vampires with a gestating childe.",
        "book": "Thousand Years p.120"
    },
    "legion": {
        "name": "Legion",
        "type": "devotion",
        "prerequisites": "animalism:5, auspex:2",
        "xp_cost": 4,
        "cost": "1 blood, 1 willpower",
        "dice_pool": "Composure + Animal Ken + Animalism",
        "description": "Use the senses of all animals of a certain type within (Blood Potency) miles, can spend extra vitae to focus on the senses of individual animals.",
        "book": "Thousand Years p.74"
    },
    "malignant_smog": {
        "name": "Malignant Smog",
        "type": "devotion",
        "prerequisites": "protean:5",
        "xp_cost": 3,
        "cost": "2 blood",
        "dice_pool": "-",
        "description": "Enhance the effect of Primeval Miasma, transforming the vampire from a cloud of hungry smoke to a cloud of toxic gas that inflicts tilts.",
        "book": "Thousand Years p.75"
    },
    "memetic_menace": {
        "name": "Memetic Menace",
        "type": "devotion",
        "prerequisites": "majesty:2, nightmare:2",
        "xp_cost": 2,
        "cost": "2 blood",
        "dice_pool": "Presence + Expression + Nightmare or Majesty vs Resolve + Blood Potency",
        "description": "When caught on camera, shift the image of you to cause the Swooning or Frightening condition.",
        "book": "Gods and Monsters p.134"
    },
    "nightmare_journey": {
        "name": "Nightmare Journey",
        "type": "devotion",
        "prerequisites": "auspex:5",
        "xp_cost": 3,
        "cost": "1 blood, 1 willpower",
        "dice_pool": "-",
        "description": "Astrally project into the Primordial Dream, and feed from dream forms there.",
        "book": "Dark Eras 2 p.143"
    },
    "not_so_special": {
        "name": "Not So Special",
        "type": "devotion",
        "prerequisites": "obfuscate:2, vigor:2",
        "xp_cost": 2,
        "cost": "2 blood",
        "dice_pool": "Resolve + Occult + Vigor vs Blood Potency + Stamina",
        "description": "Suppress another vampire's Clan-specific Disciplines.",
        "book": "Night Horrors: Shunned by the Moon p.105"
    },
    "null_space": {
        "name": "Null Space",
        "type": "devotion",
        "prerequisites": "[animalism:5,obfuscate:5], vitiate:2",
        "xp_cost": 4,
        "cost": "See Description",
        "dice_pool": "N/A",
        "description": "Pay half again the Vitae (rounded up) spent on Lord Of The Land or Oubliette, gain the ability to use Vitiate without touch.",
        "book": "Night Horrors: Shunned by the Moon p.89"
    },
    "pass_into_yesteryear": {
        "name": "Pass Into Yesteryear",
        "type": "devotion",
        "prerequisites": "obfuscate:3, nightmare:1",
        "xp_cost": 2,
        "cost": "2 blood, 1 willpower",
        "dice_pool": "-",
        "description": "Cause those under Vinculum towards you to be forgotten by others.",
        "book": "Thousand Years p.76"
    },
    "pierce_the_veil": {
        "name": "Pierce The Veil",
        "type": "devotion",
        "prerequisites": "auspex:1",
        "xp_cost": 1,
        "cost": "0 to 1 willpower",
        "dice_pool": "N/A",
        "description": "Use Auspex to perceive ghosts, and with Willpower affect them with other Disciplines.",
        "book": "Night Horrors: Shunned by the Moon p.85"
    },
    "preternatural_instinct": {
        "name": "Preternatural Instinct",
        "type": "devotion",
        "prerequisites": "auspex:4, celerity:1",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Be alerted to danger before it happens and pick up traces of intent from your opponents mind.",
        "book": "Thousand Years p.76"
    },
    "quicken_sight": {
        "name": "Quicken Sight",
        "type": "devotion",
        "prerequisites": "auspex:1, celerity:1",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "See the world in bullet time.",
        "book": "VTR 2e p.145"
    },
    "reasons_salon": {
        "name": "Reason's Salon",
        "type": "devotion",
        "prerequisites": "animalism:4, resilience:2",
        "xp_cost": 3,
        "cost": "5 blood",
        "dice_pool": "N/A",
        "description": "Dampen the Predatory Aura and frenzy rolls in an area.",
        "book": "VTR 2e p.146"
    },
    "riot": {
        "name": "Riot",
        "type": "devotion",
        "prerequisites": "majesty:5, animalism:4",
        "xp_cost": 5,
        "cost": "10 blood",
        "dice_pool": "Presence + Animal Ken + Majesty",
        "description": "Spread the aspects of the Beast everywhere for half a mile.",
        "book": "VTR 2e p.146"
    },
    "seance": {
        "name": "Seance",
        "type": "devotion",
        "prerequisites": "auspex:3, vigor:2",
        "xp_cost": 2,
        "cost": "1 willpower",
        "dice_pool": "Resolve + Occult + Auspex vs Resistance + Rank",
        "description": "Force a ghost to Materialize by their Anchor.",
        "book": "Night Horrors: Shunned by the Moon p.85"
    },
    "shared_sight": {
        "name": "Shared Sight",
        "type": "devotion",
        "prerequisites": "auspex:4, dominate:1",
        "xp_cost": 2,
        "cost": "2 blood",
        "dice_pool": "Intelligence + Empathy + Auspex",
        "description": "Lend your Auspex to another.",
        "book": "VTR 2e p.146"
    },
    "shatter_the_shroud": {
        "name": "Shatter the Shroud",
        "type": "devotion",
        "prerequisites": "auspex:2, vigor:1",
        "xp_cost": 2,
        "cost": "2 blood",
        "dice_pool": "N/A",
        "description": "Shut down Obfuscate with a Clash of Wills.",
        "book": "VTR 2e p.146"
    },
    "spontaneous_ignition": {
        "name": "Spontaneous Ignition",
        "type": "devotion",
        "prerequisites": "celerity:5, resilience:1",
        "xp_cost": 4,
        "cost": "6 blood",
        "dice_pool": "Dexterity + Athletics + Celerity - Stamina",
        "description": "Set fire to a touched target.",
        "book": "Thousand Years p.76"
    },
    "stalwart_servant": {
        "name": "Stalwart Servant",
        "type": "devotion",
        "prerequisites": "dominate:3, resilience:1",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Lend your Resilience through your Vitae.",
        "book": "VTR 2e p.146"
    },
    "subsume_the_lesser_beast": {
        "name": "Subsume the Lesser Beast",
        "type": "devotion",
        "prerequisites": "animalism:4, dominate:2",
        "xp_cost": 3,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Animal Ken + Animalism - Resolve",
        "description": "Take control of an animal's body.",
        "book": "VTR 2e p.147"
    },
    "summoning": {
        "name": "Summoning",
        "type": "devotion",
        "prerequisites": "[dominate:4,majesty:4]",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Persuasion + Discipline vs Composure + Tolerance",
        "description": "Force subject to come to you.",
        "book": "VTR 2e p.147"
    },
    "suns_brutal_dreamscape": {
        "name": "Sun's Brutal Dreamscape",
        "type": "devotion",
        "prerequisites": "nightmare:5, resilience:2",
        "xp_cost": 4,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Empathy + Nightmare vs Composure + Tolerance",
        "description": "Victim takes sunlight damage for you.",
        "book": "VTR 2e p.148"
    },
    "touch_of_deprivation": {
        "name": "Touch of Deprivation",
        "type": "devotion",
        "prerequisites": "obfuscate:4, dominate:2",
        "xp_cost": 3,
        "cost": "1 blood",
        "dice_pool": "Intelligence + Medicine + Auspex vs Resolve + Tolerance",
        "description": "Removes a sense with a touch.",
        "book": "VTR 2e p.148"
    },
    "unbridled_force": {
        "name": "Unbridled Force",
        "type": "devotion",
        "prerequisites": "vigor:5, dominate:2",
        "xp_cost": 4,
        "cost": "5 blood",
        "dice_pool": "N/A",
        "description": "Perform feats of raw strength at a distance.",
        "book": "Thousand Years p.76"
    },
    "undying_familiar": {
        "name": "Undying Familiar",
        "type": "devotion",
        "prerequisites": "animalism:2, resilience:2",
        "xp_cost": 1,
        "cost": "2 blood",
        "dice_pool": "N/A",
        "description": "Animal ghoul rises from death as an undead familiar.",
        "book": "VTR 2e p.148"
    },
    "vermin_flood": {
        "name": "Vermin Flood",
        "type": "devotion",
        "prerequisites": "animalism:3, celerity:2, vigor:2",
        "xp_cost": 4,
        "cost": "10 blood",
        "dice_pool": "Presence + Animal Ken + Animalism",
        "description": "Massive swarms of vermin deal lethal damage en masse.",
        "book": "VTR 2e p.149"
    },
    "vile_blood": {
        "name": "Vile Blood",
        "type": "devotion",
        "prerequisites": "protean:3, resilience:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Stamina + Medicine + Protean",
        "description": "Damages the vampire feeding on you by 1L instead of Vitae they would gain. Attacks inflict the Poisoned tilt during combat after taking any damage.",
        "book": "Gods and Monsters p.136"
    },
    "water_hibernation": {
        "name": "Water Hibernation",
        "type": "devotion",
        "prerequisites": "protean:1",
        "xp_cost": 1,
        "cost": "N/A",
        "dice_pool": "N/A",
        "description": "Used like Unmarked Grave, except fully submerged in water.",
        "book": "Night Horrors: Shunned by the Moon p.97"
    },
    "wet_dream": {
        "name": "Wet Dream",
        "type": "devotion",
        "prerequisites": "majesty:2, nightmare:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Empathy + Majesty vs Composure + Tolerance",
        "description": "Inflict ambiguous dreams that eerily fascinate and entice.",
        "book": "VTR 2e p.148"
    },
    "whip_sharp_tongue": {
        "name": "Whip-Sharp Tongue",
        "type": "devotion",
        "prerequisites": "majesty:1, celerity:2",
        "xp_cost": 1,
        "cost": "2 blood",
        "dice_pool": "N/A",
        "description": "Lingua Bellum. At the end of the turn, activate this devotion to make a maneuver not used this turn.",
        "book": "Gods and Monsters p.137"
    },
    "the_wish": {
        "name": "The Wish",
        "type": "devotion",
        "prerequisites": "majesty:4, celerity:2, vigor:2",
        "xp_cost": 2,
        "cost": "5 blood",
        "dice_pool": "Manipulation + Persuasion + Majesty",
        "description": "Gift vampiric strength and power to a subject for three days, then enthrall them to serve you.",
        "book": "VTR 2e p.148"
    },
    "wrack_the_mind": {
        "name": "Wrack the Mind",
        "type": "devotion",
        "prerequisites": "dominate:4, majesty:3",
        "xp_cost": 3,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Intimidation + Dominate vs Resolve + Blood Potency",
        "description": "Inflict the Agonized condition.",
        "book": "Gods and Monsters p.135"
    },
    "wraiths_presence": {
        "name": "Wraith's Presence",
        "type": "devotion",
        "prerequisites": "obfuscate:3, nightmare:1",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Wits + Subterfuge + Obfuscate",
        "description": "Conceal a subject's presence and conjure an illusion of them elsewhere.",
        "book": "VTR 2e p.149"
    }
}

# Carthian Devotions (Carthian Movement covenant)
CARTHIAN_DEVOTIONS = {
    "twentytwo_solid": {
        "name": ".22 Solid",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "protean:2, resilience:1",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Increase the downgrading power of Resilience.",
        "book": "Post/Pastebin"
    },
    "aegis_of_defiance": {
        "name": "Aegis of Defiance",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "dominate:3, resilience:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Resolve + Intimidation + Dominate",
        "description": "Shrug off mind-altering effects by forcing yourself to act contrary.",
        "book": "Post/Pastebin"
    },
    "aura_of_cursive_seduction": {
        "name": "Aura of Cursive Seduction",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "majesty:3, vigor:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Presence + Subterfuge + Majesty",
        "description": "Inflict Enthralled and Quelled Conditions when someone lashes out at you.",
        "book": "Post/Pastebin"
    },
    "bffs": {
        "name": "BFFs",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "majesty:2, dominate:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Empathy + Majesty vs Composure + Tolerance",
        "description": "Offer a facade of a long-term friendship and meaningful acquaintance.",
        "book": "Post/Pastebin"
    },
    "call_me_maybe": {
        "name": "Call Me Maybe",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "majesty:2, resilience:1",
        "xp_cost": 1,
        "cost": "N/A",
        "dice_pool": "Manipulation + Socialize + Majesty",
        "description": "Make temporary Herd that lasts for some time.",
        "book": "Post/Pastebin"
    },
    "hekireki": {
        "name": "Hekireki",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "celerity:1, vigor:1",
        "xp_cost": 2,
        "cost": "1 willpower",
        "dice_pool": "-",
        "description": "Lets you spend blood on multiple turns before unleashing the benefiting attack.",
        "book": "Post/Pastebin"
    },
    "holdout": {
        "name": "Holdout",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "protean:1, resilience:1",
        "xp_cost": 1,
        "cost": "1 blood/Size",
        "dice_pool": "N/A",
        "description": "Meld objects within yourself.",
        "book": "Post/Pastebin"
    },
    "if_you_cant_duck_it": {
        "name": "If You Can't Duck It",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "[celerity:4, resilience:4, vigor:4]",
        "xp_cost": 2,
        "cost": "1 blood, 1 willpower",
        "dice_pool": "N/A",
        "description": "Bless an object with some of your own physical power.",
        "book": "Post/Pastebin"
    },
    "manic_depression": {
        "name": "Manic Depression",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "majesty:2, nightmare:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Empathy + Nightmare vs Composure + Tolerance",
        "description": "Force a victim into a rapidly shifting state of mental extremes.",
        "book": "Post/Pastebin"
    },
    "natural_born_killer": {
        "name": "Natural Born Killer",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "celerity:3, auspex:2",
        "xp_cost": 3,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Let you intuitively sense opponents and answer with powerful gunfire.",
        "book": "Post/Pastebin"
    },
    "preserved_blood": {
        "name": "Preserved Blood",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "resilience:3, protean:1",
        "xp_cost": 2,
        "cost": "2 blood to 6 blood",
        "dice_pool": "Stamina + Occult + Protean",
        "description": "Store your Vitae for later use.",
        "book": "Post/Pastebin"
    },
    "psycho_mantle": {
        "name": "Psycho Mantle",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "nightmare:2, resilience:1",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Retaliate with a terrifying Predatory Aura.",
        "book": "Post/Pastebin"
    },
    "punching_and_fucking": {
        "name": "Punching and Fucking",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "majesty:2, vigor:1",
        "xp_cost": 2,
        "cost": "1 willpower, optionally 2 blood",
        "dice_pool": "-",
        "description": "Exert Majesty through an unarmed attack.",
        "book": "Post/Pastebin"
    },
    "sudden_strength": {
        "name": "Sudden Strength",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "celerity:2, vigor:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "If Celerity is activated, let you add your Celerity to your Strength.",
        "book": "Post/Pastebin"
    },
    "rapidity": {
        "name": "Rapidity",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "celerity:1",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Modify another Devotion, letting you activate it reflexively.",
        "book": "Post/Pastebin"
    },
    "rock_is_dead": {
        "name": "Rock Is Dead",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "vigor:2, majesty:1",
        "xp_cost": 1,
        "cost": "1 willpower",
        "dice_pool": "N/A",
        "description": "Improve your Awe, dulling other powerful presences.",
        "book": "Post/Pastebin"
    },
    "slow_and_steady": {
        "name": "Slow and Steady",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "resilience:1",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Modify a Devotion or Discipline power, slowing its activation to convert the dice pool's Attribute from dice to successes.",
        "book": "Post/Pastebin"
    },
    "straight_up_fucking_murderer": {
        "name": "Straight Up Fucking Murderer",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "celerity:2, resilience:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Use a maneuver that would normally sacrifice your Defense without doing so.",
        "book": "Post/Pastebin"
    },
    "talking_circles": {
        "name": "Talking Circles",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "celerity:3, majesty:1",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Speed up a conversation and shut down an opponent before he speaks.",
        "book": "Post/Pastebin"
    },
    "the_gun_show": {
        "name": "The Gun Show",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "vigor:3, majesty:1",
        "xp_cost": 2,
        "cost": "1 blood, 1 willpower",
        "dice_pool": "N/A",
        "description": "Improve your next use of Majesty after performing a feat of strength.",
        "book": "Post/Pastebin"
    },
    "tune_in_tune_out": {
        "name": "Tune In, Tune Out",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "auspex:2, obfuscate:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Turn off all senses but one to hyperextend the remaining sense.",
        "book": "Post/Pastebin"
    },
    "under_my_skin": {
        "name": "Under My Skin",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "protean:3, majesty:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Empathy + Protean",
        "description": "Take the appearance of someone who is under your Majesty.",
        "book": "Post/Pastebin"
    },
    "under_my_skin_advanced": {
        "name": "Under My Skin (Advanced)",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "protean:4, majesty:3",
        "xp_cost": 3,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Empathy + Protean",
        "description": "As Under My Skin, but your subject may instead take your appearance.",
        "book": "Post/Pastebin"
    },
    "violent_coercion": {
        "name": "Violent Coercion",
        "type": "devotion",
        "covenant": "carthian",
        "prerequisites": "majesty:2, vigor:1",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "Presence + Intimidation + Majesty vs Composure + Tolerance",
        "description": "Hang the threat of violence over a subject to coerce them into a task.",
        "book": "Post/Pastebin"
    }
}

# Invictus Devotions (Invictus covenant)
INVICTUS_DEVOTIONS = {
    "colossus": {
        "name": "Colossus",
        "type": "devotion",
        "covenant": "invictus",
        "prerequisites": "vigor:5, resilience:4",
        "xp_cost": 5,
        "cost": "6 blood",
        "dice_pool": "Stamina + Athletics + Resilience",
        "description": "Massively increase the power of your strikes.",
        "book": "Post/Pastebin"
    },
    "in_vitae_veritas": {
        "name": "In Vitae Veritas",
        "type": "devotion",
        "covenant": "invictus",
        "prerequisites": "majesty:5, [dominate:4, nightmare:4]",
        "xp_cost": 5,
        "cost": "10 blood",
        "dice_pool": "N/A",
        "description": "Send ripples of your Disciplines through Kindred lineages.",
        "book": "Post/Pastebin"
    },
    "kissing_cousins": {
        "name": "Kissing Cousins",
        "type": "devotion",
        "covenant": "invictus",
        "prerequisites": "majesty:2, vigor:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Manipulation + Occult + Majesty vs Composure + Tolerance",
        "description": "Makes two vampires become like relatives.",
        "book": "Post/Pastebin"
    },
    "knight_commander": {
        "name": "Knight Commander",
        "type": "devotion",
        "covenant": "invictus",
        "prerequisites": "majesty:2, vigor:2",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Presence + Brawl or Weaponry + Majesty",
        "description": "Inspire the charmed to utter greatness.",
        "book": "Post/Pastebin"
    },
    "strength_of_empire": {
        "name": "Strength of Empire",
        "type": "devotion",
        "covenant": "invictus",
        "prerequisites": "dominate:4, majesty:3, [vigor:2,resilience:2]",
        "xp_cost": 4,
        "cost": "1 willpower",
        "dice_pool": "Intelligence + Occult + Dominate - Resolve",
        "description": "Temporarily steal dots of Celerity, Resilience or Vigor from a thrall to your Vinculum.",
        "book": "Post/Pastebin"
    }
}

# Nereid Devotions (Nereid bloodline)
NEREID_DEVOTIONS = {
    "sea_witchs_gift": {
        "name": "Sea Witch's Gift",
        "type": "devotion",
        "bloodline": "nereid",
        "prerequisites": "protean:2",
        "xp_cost": 1,
        "cost": "1 blood",
        "dice_pool": "N/A",
        "description": "Regain your legs for an hour, while ignoring your Bane.",
        "book": "Night Horrors: Shunned by the Moon p.139"
    },
    "sirens_sweet_visage": {
        "name": "Siren's Sweet Visage",
        "type": "devotion",
        "bloodline": "nereid",
        "prerequisites": "obfuscate:4, majesty:1",
        "xp_cost": 2,
        "cost": "1 blood",
        "dice_pool": "Presence + Empathy + Majesty - Composure",
        "description": "Conceal your abnormalities and inflict a penalty equal to successes on rolls to resist your persuasion or intimidation rolls.",
        "book": "Night Horrors: Shunned by the Moon p.140"
    }
}

# All Devotions combined
ALL_DEVOTIONS = {
    **GENERAL_DEVOTIONS,
    **CARTHIAN_DEVOTIONS,
    **INVICTUS_DEVOTIONS,
    **NEREID_DEVOTIONS
}

# Consolidated dictionary of all discipline powers
ALL_DISCIPLINE_POWERS = {
    **ANIMALISM_POWERS,
    **AUSPEX_POWERS,
    **CELERITY_POWERS,
    **DOMINATE_POWERS,
    **MAJESTY_POWERS,
    **NIGHTMARE_POWERS,
    **OBFUSCATE_POWERS,
    **PROTEAN_POWERS,
    **RESILIENCE_POWERS,
    **VIGOR_POWERS,
    **ALL_COILS,
    **ALL_BLOODLINE_DISCIPLINES,
    **ALL_DEVOTIONS
}

# Discipline categories for easy lookup
DISCIPLINE_POWER_CATEGORIES = {
    "animalism": ANIMALISM_POWERS,
    "auspex": AUSPEX_POWERS,
    "celerity": CELERITY_POWERS,
    "dominate": DOMINATE_POWERS,
    "majesty": MAJESTY_POWERS,
    "nightmare": NIGHTMARE_POWERS,
    "obfuscate": OBFUSCATE_POWERS,
    "protean": PROTEAN_POWERS,
    "resilience": RESILIENCE_POWERS,
    "vigor": VIGOR_POWERS,
    "coils_of_the_dragon": ALL_COILS,
    "cachexy": CACHEXY_POWERS,
    "crochan": CROCHAN_POWERS,
    "dead_signal": DEAD_SIGNAL_POWERS,
    "devotions": ALL_DEVOTIONS
}

# Devotions organized by type
DEVOTIONS_BY_TYPE = {
    "general": GENERAL_DEVOTIONS,
    "carthian": CARTHIAN_DEVOTIONS,
    "invictus": INVICTUS_DEVOTIONS,
    "nereid": NEREID_DEVOTIONS
}

# Coils organized by Mystery
COILS_BY_MYSTERY = {
    "ascendant": COILS_ASCENDANT,
    "quintessence": COILS_QUINTESSENCE,
    "voivode": COILS_VOIVODE,
    "wyrm": COILS_WYRM,
    "zirnitra": COILS_ZIRNITRA,
    "ziva": COILS_ZIVA
}

# Bloodline disciplines organized by bloodline
BLOODLINE_DISCIPLINES_BY_BLOODLINE = {
    "morbus": CACHEXY_POWERS,
    "bron": CROCHAN_POWERS,
    "jharana": DEAD_SIGNAL_POWERS
}


def get_discipline_power(power_key):
    """Get a specific discipline power by key."""
    return ALL_DISCIPLINE_POWERS.get(power_key.lower().replace(" ", "_"))


def get_powers_by_discipline(discipline_name):
    """Get all powers for a specific discipline."""
    discipline_name = discipline_name.lower().replace(" ", "_")
    return DISCIPLINE_POWER_CATEGORIES.get(discipline_name, {})


def get_powers_by_level(level):
    """Get all discipline powers at a specific level (1-5)."""
    powers = {}
    for power_key, power_data in ALL_DISCIPLINE_POWERS.items():
        if power_data['level'] == level:
            powers[power_key] = power_data
    return powers


def get_all_discipline_powers():
    """Get all discipline powers."""
    return ALL_DISCIPLINE_POWERS


def get_coils_by_mystery(mystery_name):
    """Get all coils for a specific mystery."""
    mystery_name = mystery_name.lower().replace(" ", "_")
    return COILS_BY_MYSTERY.get(mystery_name, {})


def get_all_coils():
    """Get all Coils of the Dragon powers."""
    return ALL_COILS


def get_bloodline_discipline(bloodline_name):
    """Get all powers for a specific bloodline discipline."""
    bloodline_name = bloodline_name.lower().replace(" ", "_")
    return BLOODLINE_DISCIPLINES_BY_BLOODLINE.get(bloodline_name, {})


def get_devotions_by_type(devotion_type=None):
    """Get devotions by type (general, carthian, invictus, nereid)."""
    if devotion_type:
        devotion_type = devotion_type.lower().replace(" ", "_")
        return DEVOTIONS_BY_TYPE.get(devotion_type, {})
    return ALL_DEVOTIONS


def get_all_devotions():
    """Get all devotions."""
    return ALL_DEVOTIONS

