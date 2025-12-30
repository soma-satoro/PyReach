"""
Werewolf Gifts (Facets) for Chronicles of Darkness 2nd Edition.

Gifts in Werewolf: The Forsaken 2e are called "Facets" and are organized by:
- Gift category (e.g., Gift of Agony, Gift of Blood)
- Renown type (Cunning, Glory, Honor, Purity, Wisdom)
- Rank (1-5 dots)

Based on Werewolf: The Forsaken 2nd Edition.
"""

# ==================== MOON GIFTS ====================
# Gifts associated with Auspices

# Crescent Moon's Gift (Ithaeur - Spirit Master)
CRESCENT_MOON_GIFT = {
    "shadow_gaze": {
        "name": "Shadow Gaze",
        "gift_type": "crescent_moon",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Occult + Wisdom vs. Resistance",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Boosts interaction with spirits & ridden. Reveals bane or ban.",
        "book": "WTF 2e p.115"
    },
    "spirit_whispers": {
        "name": "Spirit Whispers",
        "gift_type": "crescent_moon",
        "renown": "wisdom",
        "rank": 2,
        "cost": "*",
        "dice_pool": "Presence + Persuasion + Wisdom",
        "action": "Instant",
        "duration": "-",
        "description": "Ask spirit a question.",
        "book": "WTF 2e p.115"
    },
    "shadow_hunter": {
        "name": "Shadow Hunter",
        "gift_type": "crescent_moon",
        "renown": "wisdom",
        "rank": 3,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "Sacred Hunt",
        "description": "Boosts specific rolls while in Shadow.",
        "book": "WTF 2e p.116"
    },
    "shadow_masquerade": {
        "name": "Shadow Masquerade",
        "gift_type": "crescent_moon",
        "renown": "wisdom",
        "rank": 4,
        "cost": "**",
        "dice_pool": "Manipulation + Occult + Wisdom vs. Resistance",
        "action": "Instant",
        "duration": "1 hour per success",
        "description": "Mimic target spirit.",
        "book": "WTF 2e p.116"
    },
    "panopticon": {
        "name": "Panopticon",
        "gift_type": "crescent_moon",
        "renown": "wisdom",
        "rank": 5,
        "cost": "*+",
        "dice_pool": "Intelligence + Occult + Wisdom",
        "action": "Extended (10, minute per roll)",
        "duration": "1 scene",
        "description": "Gains awareness of spirits. Use spirit's senses.",
        "book": "WTF 2e p.117"
    }
}

# Full Moon's Gift (Rahu - Warrior)
FULL_MOON_GIFT = {
    "killer_instinct": {
        "name": "Killer Instinct",
        "gift_type": "full_moon",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 scene",
        "description": "8-again on Brawl and Weaponry.",
        "book": "WTF 2e p.117"
    },
    "warriors_hide": {
        "name": "Warrior's Hide",
        "gift_type": "full_moon",
        "renown": "glory",
        "rank": 2,
        "cost": "-",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Boosts Health.",
        "book": "WTF 2e p.117"
    },
    "bloody_handed_hunter": {
        "name": "Bloody-Handed Hunter",
        "gift_type": "full_moon",
        "renown": "glory",
        "rank": 3,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "Sacred Hunt",
        "description": "Boosts attack rolls vs obstacles to the Hunt.",
        "book": "WTF 2e p.117"
    },
    "butchery": {
        "name": "Butchery",
        "gift_type": "full_moon",
        "renown": "glory",
        "rank": 4,
        "cost": "**",
        "dice_pool": "Wits + Brawl + Purity",
        "action": "Reflexive",
        "duration": "1 turn per success",
        "description": "Adds tilts to opponents that meet criteria.",
        "book": "WTF 2e p.117"
    },
    "crimson_spasm": {
        "name": "Crimson Spasm",
        "gift_type": "full_moon",
        "renown": "glory",
        "rank": 5,
        "cost": "● per turn",
        "dice_pool": "Stamina + Survival + Purity",
        "action": "Instant",
        "duration": "-",
        "description": "Use successes to boost Strength, Stamina, armor, damage.",
        "book": "WTF 2e p.118"
    }
}

# Gibbous Moon's Gift (Cahalith - Visionary)
GIBBOUS_MOON_GIFT = {
    "war_howl": {
        "name": "War Howl",
        "gift_type": "gibbous_moon",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Presence + Expression + Glory",
        "action": "Instant",
        "duration": "1 turn per success",
        "description": "Boosts pack's Brawl and Weaponry.",
        "book": "WTF 2e p.118"
    },
    "voice_of_glory": {
        "name": "Voice of Glory",
        "gift_type": "gibbous_moon",
        "renown": "glory",
        "rank": 2,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Adds to Expression, Persuasion and First Impression.",
        "book": "WTF 2e p.118"
    },
    "dream_hunter": {
        "name": "Dream Hunter",
        "gift_type": "gibbous_moon",
        "renown": "glory",
        "rank": 3,
        "cost": "*",
        "dice_pool": "Manipulation + Empathy + Glory vs. Composure + Primal Urge",
        "action": "Instant",
        "duration": "Sacred Hunt",
        "description": "Invades prey's dreams.",
        "book": "WTF 2e p.118"
    },
    "thousand_throat_howl": {
        "name": "Thousand Throat Howl",
        "gift_type": "gibbous_moon",
        "renown": "glory",
        "rank": 4,
        "cost": "**",
        "dice_pool": "Presence + Intimidate + Glory vs. Resolve + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Howl to apply Demoralized Condition.",
        "book": "WTF 2e p.118"
    },
    "end_of_story": {
        "name": "End of Story",
        "gift_type": "gibbous_moon",
        "renown": "glory",
        "rank": 5,
        "cost": "***",
        "dice_pool": "Presence + Persuasion + Glory vs. prey's Composure + Primal Urge",
        "action": "Instant",
        "duration": "1 day",
        "description": "Story of prey's impending fate adds penalties to prey.",
        "book": "WTF 2e p.119"
    }
}

# Half Moon's Gift (Elodoth - Judge/Mediator)
HALF_MOON_GIFT = {
    "scent_beneath_the_surface": {
        "name": "Scent Beneath the Surface",
        "gift_type": "half_moon",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Empathy + Honor vs. Composure + Primal Urge",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Detect Lies.",
        "book": "WTF 2e p.119"
    },
    "binding_oath": {
        "name": "Binding Oath",
        "gift_type": "half_moon",
        "renown": "honor",
        "rank": 2,
        "cost": "*",
        "dice_pool": "Resolve + Persuasion + Honor vs. Resolve + Primal Urge",
        "action": "Instant",
        "duration": "1 month",
        "description": "Bind oaths.",
        "book": "WTF 2e p.119"
    },
    "sly_hunter": {
        "name": "Sly Hunter",
        "gift_type": "half_moon",
        "renown": "honor",
        "rank": 3,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "Sacred Hunt",
        "description": "Boosts dice pools while pursuing Hunt.",
        "book": "WTF 2e p.119"
    },
    "ties_of_word_and_promise": {
        "name": "Ties of Word and Promise",
        "gift_type": "half_moon",
        "renown": "honor",
        "rank": 4,
        "cost": "● per dot",
        "dice_pool": "Manipulation + Persuasion + Honor",
        "action": "Extended (10, minute per roll)",
        "duration": "1 day",
        "description": "Acquire temporary access to Allies, Contacts, etc.",
        "book": "WTF 2e p.120"
    },
    "ties_of_blood_and_bone": {
        "name": "Ties of Blood and Bone",
        "gift_type": "half_moon",
        "renown": "honor",
        "rank": 5,
        "cost": "***",
        "dice_pool": "Stamina + Empathy + Honor vs. Stamina + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Switch location with packmate.",
        "book": "WTF 2e p.120"
    }
}

# New Moon's Gift (Irraka - Scout/Trickster)
NEW_MOON_GIFT = {
    "eviscerate": {
        "name": "Eviscerate",
        "gift_type": "new_moon",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Brawl or Weaponry attack vs. unaware target becomes rote action.",
        "book": "WTF 2e p.120"
    },
    "slip_away": {
        "name": "Slip Away",
        "gift_type": "new_moon",
        "renown": "cunning",
        "rank": 2,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Blurs observers memories.",
        "book": "WTF 2e p.120"
    },
    "relentless_hunter": {
        "name": "Relentless Hunter",
        "gift_type": "new_moon",
        "renown": "cunning",
        "rank": 3,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "Sacred Hunt",
        "description": "Boosts dice pools while pursuing prey.",
        "book": "WTF 2e p.120"
    },
    "divide_and_conquer": {
        "name": "Divide and Conquer",
        "gift_type": "new_moon",
        "renown": "cunning",
        "rank": 4,
        "cost": "*",
        "dice_pool": "Manipulation + Subterfuge + Cunning vs. Composure + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Lure prey away from their companions.",
        "book": "WTF 2e p.121"
    },
    "breach": {
        "name": "Breach",
        "gift_type": "new_moon",
        "renown": "cunning",
        "rank": 5,
        "cost": "***",
        "dice_pool": "Wits + Stealth + Cunning",
        "action": "Instant",
        "duration": "-",
        "description": "Cross the Gauntlet.",
        "book": "WTF 2e p.121"
    }
}

# All Moon Gifts combined
ALL_MOON_GIFTS = {
    **CRESCENT_MOON_GIFT,
    **FULL_MOON_GIFT,
    **GIBBOUS_MOON_GIFT,
    **HALF_MOON_GIFT,
    **NEW_MOON_GIFT
}

# Moon gifts by auspice
MOON_GIFTS_BY_AUSPICE = {
    "ithaeur": CRESCENT_MOON_GIFT,
    "crescent_moon": CRESCENT_MOON_GIFT,
    "rahu": FULL_MOON_GIFT,
    "full_moon": FULL_MOON_GIFT,
    "cahalith": GIBBOUS_MOON_GIFT,
    "gibbous_moon": GIBBOUS_MOON_GIFT,
    "elodoth": HALF_MOON_GIFT,
    "half_moon": HALF_MOON_GIFT,
    "irraka": NEW_MOON_GIFT,
    "new_moon": NEW_MOON_GIFT
}

# ==================== SHADOW GIFTS ====================
# Gifts organized by category and renown

# Gift of Agony
GIFT_OF_AGONY = {
    "wrack": {
        "name": "Wrack",
        "gift_type": "agony",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 day",
        "description": "Penalise a touched targets attempts at tracking and foot-chases.",
        "book": "Night Horrors: Shunned by the Moon p.15"
    },
    "stoicism": {
        "name": "Stoicism",
        "gift_type": "agony",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 + Glory turns",
        "description": "Ignore dice penalties from physical sources.",
        "book": "Night Horrors: Shunned by the Moon p.15"
    },
    "pain_mirror": {
        "name": "Pain Mirror",
        "gift_type": "agony",
        "renown": "honor",
        "rank": 2,
        "cost": "**",
        "dice_pool": "Composure + Empathy + Honor",
        "action": "Instant; Reflexive on exceptional success",
        "duration": "1 scene",
        "description": "Cause opponents to take 1 bashing for every lethal or aggravated damage received, and copy a Physical Tilt to one linked opponent for (Honor) turns.",
        "book": "Night Horrors: Shunned by the Moon p.15"
    },
    "catharsis": {
        "name": "Catharsis",
        "gift_type": "agony",
        "renown": "purity",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "When spending Willpower in the same turn as suffering lethal or aggravated damage, increase the Willpower bonus by (Purity).",
        "book": "Night Horrors: Shunned by the Moon p.15"
    },
    "scourge": {
        "name": "Scourge",
        "gift_type": "agony",
        "renown": "wisdom",
        "rank": 2,
        "cost": "**",
        "dice_pool": "-",
        "action": "None",
        "duration": "-",
        "description": "Suppress the effects of a Condition or Tilt that affects the user's mind or soul for (Wisdom) days.",
        "book": "Night Horrors: Shunned by the Moon p.15"
    }
}

# Gift of Blood
GIFT_OF_BLOOD = {
    "seep": {
        "name": "Seep",
        "gift_type": "blood",
        "renown": "cunning",
        "rank": 3,
        "cost": "**",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Cause blood to seep from everything in an area of (Cunning x 25) yards, inflicting (Cunning) penalty to Athletics rolls and increasing time needed to interact with objects. Also overpowers all other smells in area.",
        "book": "Night Horrors: Shunned by the Moon p.16"
    },
    "purge": {
        "name": "Purge",
        "gift_type": "blood",
        "renown": "glory",
        "rank": 2,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Reduce Toxicity of disease or poison by (Glory), ending if reduced to 0. Mundane addictions instantly purged, Clash against supernatural addictions with rote quality; suppress Poisoned and Sick Tilts; expel foreign bodies and parasites.",
        "book": "Night Horrors: Shunned by the Moon p.16"
    },
    "bind": {
        "name": "Bind",
        "gift_type": "blood",
        "renown": "honor",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Ignore a Facet's requirement to perceive, touch or strike an opponent by consuming the opponent's blood or of a close relative, which must be fresh.",
        "book": "Night Horrors: Shunned by the Moon p.16"
    },
    "bleed": {
        "name": "Bleed",
        "gift_type": "blood",
        "renown": "purity",
        "rank": 2,
        "cost": "*",
        "dice_pool": "Strength + Brawl + Purity vs. Stamina + Primal Urge",
        "action": "Reflexive",
        "duration": "1 day",
        "description": "Opponents suffer 1 extra lethal in a turn where they are dealt lethal or aggravated damage, and penalizes all Medicine rolls to treat injuries by (Purity).",
        "book": "Night Horrors: Shunned by the Moon p.16"
    },
    "clot": {
        "name": "Clot",
        "gift_type": "blood",
        "renown": "wisdom",
        "rank": 2,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 day",
        "description": "Long-term lethal and aggravated healing is increased. Does not affect turn-to-turn regeneration.",
        "book": "Night Horrors: Shunned by the Moon p.16"
    }
}

# Gift of Death
GIFT_OF_DEATH = {
    "cold_embrace": {
        "name": "Cold Embrace",
        "gift_type": "death",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Stamina + Medicine + Cunning",
        "action": "Instant",
        "duration": "1 hour per success",
        "description": "Suppress vital signs and appear dead.",
        "book": "WTF 2e p.121"
    },
    "barghest": {
        "name": "Barghest",
        "gift_type": "death",
        "renown": "glory",
        "rank": 1,
        "cost": "- / *",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Perceive and interact with ghosts.",
        "book": "WTF 2e p.121"
    },
    "memento_mori": {
        "name": "Memento Mori",
        "gift_type": "death",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 scene",
        "description": "Awareness of packmates injuries. Transfer packmates injuries to self.",
        "book": "WTF 2e p.121"
    },
    "bone_gnaw": {
        "name": "Bone Gnaw",
        "gift_type": "death",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Gain knowledge from bones of deceased.",
        "book": "WTF 2e p.121"
    },
    "eyes_of_the_dead": {
        "name": "Eyes of the Dead",
        "gift_type": "death",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Occult + Wisdom",
        "action": "Instant",
        "duration": "-",
        "description": "View last thing seen by the deceased.",
        "book": "WTF 2e p.122"
    }
}

# Gift of Disease
GIFT_OF_DISEASE = {
    "festering_bite": {
        "name": "Festering Bite",
        "gift_type": "disease",
        "renown": "cunning",
        "rank": 2,
        "cost": "*",
        "dice_pool": "Strength + Survival + Cunning vs. Stamina + Primal Urge",
        "action": "Reflexive",
        "duration": "1 week",
        "description": "Double the time for opponents to regenerate damage. Does not affect Gauru opponents. Other supernatural methods of healing must win Clash or become dramatic failure.",
        "book": "Night Horrors: Shunned by the Moon p.16-17"
    },
    "rancid_maw": {
        "name": "Rancid Maw",
        "gift_type": "disease",
        "renown": "glory",
        "rank": 2,
        "cost": "**",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Attempt to inflict the moderate Poisoned Tilt from up to 20 yards range via 1L autofire cloud of disease; roll Dexterity + Athletics for attack roll and ignore Defense. For 1 turn, ranged attacks against user suffer a -2 penalty.",
        "book": "Night Horrors: Shunned by the Moon p.17"
    },
    "lepers_bell": {
        "name": "Leper's Bell",
        "gift_type": "disease",
        "renown": "honor",
        "rank": 2,
        "cost": "*",
        "dice_pool": "Manipulation + Medicine + Honor vs. Stamina + Primal Urge",
        "action": "Instant",
        "duration": "1 week",
        "description": "Severity of diseases the opponent suffers are increased; Opponent suffers a penalty to social rolls.",
        "book": "Night Horrors: Shunned by the Moon p.17"
    },
    "rabid_fever": {
        "name": "Rabid Fever",
        "gift_type": "disease",
        "renown": "purity",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Increase resistance to disease; Increase Initiative modifier by (Purity).",
        "book": "Night Horrors: Shunned by the Moon p.18"
    },
    "pox_cauldron": {
        "name": "Pox Cauldron",
        "gift_type": "disease",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Become infected with a disease that can be transmitted to a target.",
        "book": "Night Horrors: Shunned by the Moon p.18"
    }
}

# Gift of Dominance
GIFT_OF_DOMINANCE = {
    "primal_allure": {
        "name": "Primal Allure",
        "gift_type": "dominance",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Manipulation + Subterfuge + Cunning vs. Resolve + Primal Urge",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Perfect impression with target.",
        "book": "WTF 2e p.122"
    },
    "glorious_lunacy": {
        "name": "Glorious Lunacy",
        "gift_type": "dominance",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 scene",
        "description": "When inflicting Lunacy, apply Awestruck Condition.",
        "book": "WTF 2e p.122"
    },
    "lay_low_the_challenger": {
        "name": "Lay Low the Challenger",
        "gift_type": "dominance",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Presence + Intimidate + Honor vs. Composure + Primal Urge",
        "action": "Reflexive",
        "duration": "-",
        "description": "Inflicts the Cowed Condition on a struck opponent.",
        "book": "WTF 2e p.122"
    },
    "snarl_of_the_predator": {
        "name": "Snarl of the Predator",
        "gift_type": "dominance",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Reduces penalty when forcing Doors.",
        "book": "WTF 2e p.123"
    },
    "lead_the_lesser_pack": {
        "name": "Lead the Lesser Pack",
        "gift_type": "dominance",
        "renown": "wisdom",
        "rank": 1,
        "cost": "* per ally",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 day",
        "description": "Adds temporary pack member.",
        "book": "WTF 2e p.123"
    }
}

# Gift of the Elementals
GIFT_OF_THE_ELEMENTALS = {
    "breath_of_air": {
        "name": "Breath of Air",
        "gift_type": "elementals",
        "renown": "cunning",
        "rank": 1,
        "cost": "*+",
        "dice_pool": "Wits + Athletics + Cunning",
        "action": "Instant",
        "duration": "-",
        "description": "Use the Air Influence at the same Essence cost as a spirit with (Cunning) dots.",
        "book": "WTF 2e p.123"
    },
    "catastrophe": {
        "name": "Catastrophe",
        "gift_type": "elementals",
        "renown": "glory",
        "rank": 5,
        "cost": "***** per dot",
        "dice_pool": "Presence + Survival + Glory",
        "action": "Extended (15, hour per roll)",
        "duration": "-",
        "description": "Boosts influence gained from Elemental Facets; grants immunity to catastrophe boosted Influences.",
        "book": "WTF 2e p.123"
    },
    "flesh_of_earth": {
        "name": "Flesh of Earth",
        "gift_type": "elementals",
        "renown": "honor",
        "rank": 1,
        "cost": "*+",
        "dice_pool": "Strength + Survival + Honor",
        "action": "Instant",
        "duration": "-",
        "description": "Use the Earth Influence at the same Essence cost as a spirit with (Honor) dots.",
        "book": "WTF 2e p.123"
    },
    "tongue_of_flame": {
        "name": "Tongue of Flame",
        "gift_type": "elementals",
        "renown": "purity",
        "rank": 1,
        "cost": "*+",
        "dice_pool": "Presence + Empathy + Purity",
        "action": "Instant",
        "duration": "-",
        "description": "Use the Fire Influence at the same Essence cost as a spirit with (Purity) dots.",
        "book": "WTF 2e p.123"
    },
    "heart_of_water": {
        "name": "Heart of Water",
        "gift_type": "elementals",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*+",
        "dice_pool": "Manipulation + Occult + Wisdom",
        "action": "Instant",
        "duration": "-",
        "description": "Use the Water Influence at the same Essence cost as a spirit with (Wisdom) dots.",
        "book": "WTF 2e p.123"
    }
}

# Gift of Evasion
GIFT_OF_EVASION = {
    "feet_of_mist": {
        "name": "Feet of Mist",
        "gift_type": "evasion",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 hour",
        "description": "All attempts to track or locate the user fail.",
        "book": "WTF 2e p.123"
    },
    "fog_of_war": {
        "name": "Fog of War",
        "gift_type": "evasion",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Subterfuge + Glory vs. Composure + Primal Urge",
        "action": "Reflexive",
        "duration": "-",
        "description": "Something specific (bullet, package, etc.) reaches the wrong target.",
        "book": "WTF 2e p.124"
    },
    "deny_everything": {
        "name": "Deny Everything",
        "gift_type": "evasion",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Use Honor to resist Social/Manipulation actions.",
        "book": "WTF 2e p.124"
    },
    "hit_and_run": {
        "name": "Hit and Run",
        "gift_type": "evasion",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Dexterity + Stealth + Purity vs. Composure + Primal Urge",
        "action": "Reflexive",
        "duration": "-",
        "description": "Interrupt attack and disengage; Can inflict Shadow Paranoia Condition.",
        "book": "WTF 2e p.124"
    },
    "exit_strategy": {
        "name": "Exit Strategy",
        "gift_type": "evasion",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Streetwise + Wisdom",
        "action": "Instant",
        "duration": "-",
        "description": "Gain immediate knowledge of escape routes or boltholes.",
        "book": "WTF 2e p.124"
    }
}

# Gift of Fervor
GIFT_OF_FERVOR = {
    "crisis_of_faith": {
        "name": "Crisis of Faith",
        "gift_type": "fervor",
        "renown": "cunning",
        "rank": 2,
        "cost": "*",
        "dice_pool": "Manipulation + Subterfuge + Cunning vs. Resolve + Primal Urge",
        "action": "Instant",
        "duration": "1 day per success",
        "description": "Prevent an opponent from regaining Willpower from rest; Gain (Cunning) bonus to social rolls against them. Opponent also takes equal penalty to participate in or lead formalized expressions of ideology.",
        "book": "Night Horrors: Shunned by the Moon p.18"
    },
    "fanaticism": {
        "name": "Fanaticism",
        "gift_type": "fervor",
        "renown": "glory",
        "rank": 2,
        "cost": "*",
        "dice_pool": "Presence + Socialize + Glory vs. Resolve",
        "action": "Instant",
        "duration": "1 day per success",
        "description": "Cause a human community to become more insular and despise outsiders.",
        "book": "Night Horrors: Shunned by the Moon p.18"
    },
    "affirmation": {
        "name": "Affirmation",
        "gift_type": "fervor",
        "renown": "honor",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "Permanent",
        "description": "Grant a point of Willpower to a target; Gain Willpower when they indulge in their morality traits.",
        "book": "Night Horrors: Shunned by the Moon p.18"
    },
    "zeal": {
        "name": "Zeal",
        "gift_type": "fervor",
        "renown": "purity",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Increase Willpower, potentially exceeding 10.",
        "book": "Night Horrors: Shunned by the Moon p.19"
    },
    "fervid_mission": {
        "name": "Fervid Mission",
        "gift_type": "fervor",
        "renown": "wisdom",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "Manipulation + Persuasion + Wisdom - Resolve",
        "action": "Instant",
        "duration": "1 month",
        "description": "Human or Wolf-Blooded target gains the Obsession Condition. Resolving the Condition ends the facet.",
        "book": "Night Horrors: Shunned by the Moon p.19"
    }
}

# Gift of Hunger
GIFT_OF_HUNGER = {
    "eater_of_names": {
        "name": "Eater of Names",
        "gift_type": "hunger",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 day",
        "description": "Prevent the target from using social merits or rites, or inflict a penalty on human attempts to remember and supernatural attempts to gain knowledge of a dead target for 1 year.",
        "book": "Night Horrors: Shunned by the Moon p.19"
    },
    "famine_howl": {
        "name": "Famine Howl",
        "gift_type": "hunger",
        "renown": "glory",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "Presence + Survival + Glory",
        "action": "Instant",
        "duration": "1 week",
        "description": "Cause all physical food sources to wither, spoil and be infested; Attempts to gain Essence or similar resources are penalised.",
        "book": "Night Horrors: Shunned by the Moon p.19"
    },
    "gluttony": {
        "name": "Gluttony",
        "gift_type": "hunger",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Strength + Persuasion + Honor - Composure",
        "action": "Instant",
        "duration": "1 day",
        "description": "Cause a living target or object to require to consume multiple times the normal requirement.",
        "book": "Night Horrors: Shunned by the Moon p.19-20"
    },
    "wolf_hunger": {
        "name": "Wolf Hunger",
        "gift_type": "hunger",
        "renown": "purity",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Gain bonus Essence from flesh or spirit consumption during the Sacred Hunt.",
        "book": "Night Horrors: Shunned by the Moon p.20"
    },
    "ravenous_maw": {
        "name": "Ravenous Maw",
        "gift_type": "hunger",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Initiate a Grapple at a range of (5 x Wisdom) yards, and can drag target closer if successful.",
        "book": "Night Horrors: Shunned by the Moon p.20"
    }
}

# Gift of Insight
GIFT_OF_INSIGHT = {
    "prey_on_weakness": {
        "name": "Prey on Weakness",
        "gift_type": "insight",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Presence + Empathy + Cunning vs. Composure + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Gains awareness prey's weaknesses and conditions.",
        "book": "WTF 2e p.125"
    },
    "read_the_worlds_loom": {
        "name": "Read the World's Loom",
        "gift_type": "insight",
        "renown": "glory",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "Wits + Streetwise + Glory",
        "action": "Instant",
        "duration": "-",
        "description": "Gains insight; Learns of an event, threat or circumstance of meaningful relevence.",
        "book": "WTF 2e p.125"
    },
    "echo_dream": {
        "name": "Echo Dream",
        "gift_type": "insight",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Investigation + Honor",
        "action": "Instant",
        "duration": "-",
        "description": "Gain information about an object or location.",
        "book": "WTF 2e p.125"
    },
    "scent_the_unnatural": {
        "name": "Scent the Unnatural",
        "gift_type": "insight",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Occult + Purity",
        "action": "Instant",
        "duration": "-",
        "description": "Detect supernatural creatures and effects.",
        "book": "WTF 2e p.126"
    },
    "one_step_ahead": {
        "name": "One Step Ahead",
        "gift_type": "insight",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Detect the way in which prey will flee.",
        "book": "WTF 2e p.126"
    }
}

# Gift of Inspiration
GIFT_OF_INSPIRATION = {
    "lunatic_inspiration": {
        "name": "Lunatic Inspiration",
        "gift_type": "inspiration",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Manipulation + Empathy + Cunning vs Composure",
        "action": "Instant",
        "duration": "1 lunar cycle",
        "description": "Infects a human or Wolf-Blooded with ongoing Inspired and Madness Conditions, driving towards resolution through a prophetic or revelatory work.",
        "book": "WTF 2e p.127"
    },
    "fearless_hunter": {
        "name": "Fearless Hunter",
        "gift_type": "inspiration",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Share contests and resistance against mental influence and fear with present packmates, and add Glory as a bonus to do so.",
        "book": "WTF 2e p.127"
    },
    "pack_triumphs_together": {
        "name": "Pack Triumphs Together",
        "gift_type": "inspiration",
        "renown": "honor",
        "rank": 1,
        "cost": "* per target",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 scene",
        "description": "Allows packmates to share Initiative values, and grants them 8-Again on teamwork actions.",
        "book": "WTF 2e p.127"
    },
    "unity": {
        "name": "Unity",
        "gift_type": "inspiration",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Intervene in Social Maneuvering to grant a packmate your Purity in additional Doors.",
        "book": "WTF 2e p.127"
    },
    "still_small_voice": {
        "name": "Still Small Voice",
        "gift_type": "inspiration",
        "renown": "wisdom",
        "rank": 1,
        "cost": "* per target",
        "dice_pool": "Presence + Persuasion + Wisdom vs Resolve + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Talk werewolves down from the Soft Rage.",
        "book": "WTF 2e p.127"
    }
}

# Gift of Knowledge
GIFT_OF_KNOWLEDGE = {
    "needle": {
        "name": "Needle",
        "gift_type": "knowledge",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Manipulation + Subterfuge + Cunning vs Composure + Primal Urge",
        "action": "Instant",
        "duration": "1 month",
        "description": "Hides an item of knowledge in all forms from a target.",
        "book": "WTF 2e p.127-128"
    },
    "this_story_is_true": {
        "name": "This Story Is True",
        "gift_type": "knowledge",
        "renown": "glory",
        "rank": 2,
        "cost": "**",
        "dice_pool": "Presence + Academics + Glory",
        "action": "Instant",
        "duration": "1 hour per success",
        "description": "Tells a tale whose lesson grants temporary bonus dots in a particular Skill to one listener.",
        "book": "WTF 2e p.128"
    },
    "know_thy_prey": {
        "name": "Know Thy Prey",
        "gift_type": "knowledge",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Socialize + Honor",
        "action": "Instant",
        "duration": "-",
        "description": "Intuits a target's names and aliases, alternate identities, sources of fame and social connections.",
        "book": "WTF 2e p.128"
    },
    "lore_of_the_land": {
        "name": "Lore of the Land",
        "gift_type": "knowledge",
        "renown": "purity",
        "rank": 2,
        "cost": "**",
        "dice_pool": "Intelligence + Survival + Purity",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Identifies supernatural effects lain upon a territory. Locates material creatures and dangers within your pack's territory.",
        "book": "WTF 2e p.128"
    },
    "sift_the_sands": {
        "name": "Sift the Sands",
        "gift_type": "knowledge",
        "renown": "wisdom",
        "rank": 2,
        "cost": "* / **",
        "dice_pool": "Intelligence + Academics + Wisdom",
        "action": "Extended (10, minute per roll)",
        "duration": "-",
        "description": "Spirit hauntings aid research, and can optionally copy the sought knowledge to a new medium.",
        "book": "WTF 2e p.128-129"
    }
}

# Gift of Nature
GIFT_OF_NATURE = {
    "natures_lure": {
        "name": "Nature's Lure",
        "gift_type": "nature",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Manipulation + Survival + Cunning vs Composure + Primal Urge",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Lures an isolated group of up to (Cunning) non-werewolves into the heart of wilderness, and penalizes their Initiative by your Cunning.",
        "book": "WTF 2e p.129"
    },
    "black_earth_red_hunger": {
        "name": "Black Earth, Red Hunger",
        "gift_type": "nature",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Spurs guided plant overgrowth across a radius of (Glory × 10) yards, which consumes corpses. Until the next sunrise, sense any heartbeat or bloodshed within the overgrowth, and regenerate lethal damage when it soaks in blood.",
        "book": "WTF 2e p.129"
    },
    "knotted_paths": {
        "name": "Knotted Paths",
        "gift_type": "nature",
        "renown": "honor",
        "rank": 1,
        "cost": "* per target",
        "dice_pool": "Wits + Survival + Honor vs Composure + Primal Urge",
        "action": "Instant",
        "duration": "1 day",
        "description": "Prevents any path from leading prey out of the wilderness.",
        "book": "WTF 2e p.129"
    },
    "pack_kin": {
        "name": "Pack Kin",
        "gift_type": "nature",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Presence + Animal Ken + Purity",
        "action": "Extended (5, half-hour per roll)",
        "duration": "Indefinite",
        "description": "Inducts a predatory animal as a loyal member of the pack, which can understand commands from packmates and resists mental influence from without at a +3 bonus. Each werewolf with this Gift may induct up to (Purity) animals.",
        "book": "WTF 2e p.129-130"
    },
    "beast_ride": {
        "name": "Beast Ride",
        "gift_type": "nature",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Animal Ken + Wisdom - Resolve",
        "action": "Instant",
        "duration": "Indefinite",
        "description": "Enter a trance to ride an animal spiritually, receiving its senses and controlling its behavior.",
        "book": "WTF 2e p.130"
    }
}

# Gift of Rage
GIFT_OF_RAGE = {
    "incite_fury": {
        "name": "Incite Fury",
        "gift_type": "rage",
        "renown": "cunning",
        "rank": 2,
        "cost": "**",
        "dice_pool": "Manipulation + Subterfuge + Cunning vs Composure + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Snarl to incite Death Rage in a werewolf or the Berserk Condition otherwise.",
        "book": "WTF 2e p.130"
    },
    "berserkers_might": {
        "name": "Berserker's Might",
        "gift_type": "rage",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "While in a form that causes Lunacy, reduce damage from one attack by (Glory) points, or shrug off a physical injury Tilt. Use freely at no cost in Hard Rage.",
        "book": "WTF 2e p.130"
    },
    "perfected_rage": {
        "name": "Perfected Rage",
        "gift_type": "rage",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Increase controlled time in Gauru by (Honor) turns.",
        "book": "WTF 2e p.130"
    },
    "slaughterer": {
        "name": "Slaughterer",
        "gift_type": "rage",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Use in Gauru to add (Purity) damage to a Brawl attack. Use freely at no cost in Hard Rage.",
        "book": "WTF 2e p.130"
    },
    "raging_lunacy": {
        "name": "Raging Lunacy",
        "gift_type": "rage",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 scene",
        "description": "Inflict the Berserk Condition instead of normal Lunacy Conditions.",
        "book": "WTF 2e p.131"
    }
}

# Gift of Shaping
GIFT_OF_SHAPING = {
    "moldywarp": {
        "name": "Moldywarp",
        "gift_type": "shaping",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Dalu form's claws spread and harden, able to tunnel through stone and concrete at a Speed equal to Strength + Cunning.",
        "book": "WTF 2e p.131"
    },
    "shield_breaker": {
        "name": "Shield-Breaker",
        "gift_type": "shaping",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Add (Glory) Armor-Piercing to a Brawl or Weaponry attack.",
        "book": "WTF 2e p.131"
    },
    "entropys_toll": {
        "name": "Entropy's Toll",
        "gift_type": "shaping",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Presence + Expression + Honor",
        "action": "Instant",
        "duration": "-",
        "description": "Damage an object by twice your successes, ignoring Durability, with a shrieking howl.",
        "book": "WTF 2e p.131"
    },
    "perfection_of_form": {
        "name": "Perfection of Form",
        "gift_type": "shaping",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Crafts + Purity",
        "action": "1 day",
        "duration": "-",
        "description": "Whisper your successes into an object as a bonus to its equipment rating, which dissipates after use. Repair an equal amount of Structure damage.",
        "book": "WTF 2e p.131"
    },
    "sculpt": {
        "name": "Sculpt",
        "gift_type": "shaping",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Intelligence + Crafts + Wisdom",
        "action": "Instant",
        "duration": "30 minutes",
        "description": "Render up to your Wisdom in Size's worth of material malleable like clay. You may spend Essence to extend the duration.",
        "book": "WTF 2e p.131"
    }
}

# Gift of Stealth
GIFT_OF_STEALTH = {
    "shadow_pelt": {
        "name": "Shadow Pelt",
        "gift_type": "stealth",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Take the rote quality on your next (Cunning) Stealth rolls.",
        "book": "WTF 2e p.131-132"
    },
    "predators_shadow": {
        "name": "Predator's Shadow",
        "gift_type": "stealth",
        "renown": "glory",
        "rank": 1,
        "cost": "* per target",
        "dice_pool": "Presence + Intimidation + Glory vs Composure + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Inflict the Shadow Paranoia Condition, evoking panic on failed Perception actions.",
        "book": "WTF 2e p.132"
    },
    "pack_stalks_the_prey": {
        "name": "Pack Stalks the Prey",
        "gift_type": "stealth",
        "renown": "honor",
        "rank": 1,
        "cost": "* per ally",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Allow packmates to share your success on a Stealth roll.",
        "book": "WTF 2e p.132"
    },
    "the_hunter_waits": {
        "name": "The Hunter Waits",
        "gift_type": "stealth",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "While you remain still and unobtrusive, penalize Perception actions and supernatural powers to spot you by your Purity. Add Purity to your Initiative on an ambush.",
        "book": "WTF 2e p.132"
    },
    "running_silent": {
        "name": "Running Silent",
        "gift_type": "stealth",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Moving at high speeds doesn't deter Stealth actions. Reduce terrain penalties and fall damage by your Wisdom.",
        "book": "WTF 2e p.132"
    }
}

# Gift of Strength
GIFT_OF_STRENGTH = {
    "unchained": {
        "name": "Unchained",
        "gift_type": "strength",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Add (Cunning) to a grappling roll, or shatter any restraint or binding. Use freely at no cost in Hard Rage.",
        "book": "WTF 2e p.132"
    },
    "predators_unmatched_pursuit": {
        "name": "Predator's Unmatched Pursuit",
        "gift_type": "strength",
        "renown": "glory",
        "rank": 1,
        "cost": "* (*)",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Add Glory to Urshul and Urhan Speed. Extend jump distances by (Glory) times over. Double Speed for a turn with Essence. Use freely at no cost in Hard Rage.",
        "book": "WTF 2e p.132"
    },
    "crushing_blow": {
        "name": "Crushing Blow",
        "gift_type": "strength",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Inflict Honor as a temporary Defense penalty with a Brawl strike. The strike deals lethal damage even in Hishu.",
        "book": "WTF 2e p.132"
    },
    "primal_strength": {
        "name": "Primal Strength",
        "gift_type": "strength",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 scene",
        "description": "Add Purity to Strength. Use freely at no cost in Hard Rage.",
        "book": "WTF 2e p.132"
    },
    "rending_claws": {
        "name": "Rending Claws",
        "gift_type": "strength",
        "renown": "wisdom",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Gauru and Urshul forms ignore up to (Wisdom) Durability, and add (Wisdom) Structure damage.",
        "book": "WTF 2e p.133"
    }
}

# Gift of Technology
GIFT_OF_TECHNOLOGY = {
    "garble": {
        "name": "Garble",
        "gift_type": "technology",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Intelligence + Science + Cunning - Composure",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Technology betrays and confounds the target at every turn.",
        "book": "WTF 2e p.133"
    },
    "unmake": {
        "name": "Unmake",
        "gift_type": "technology",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Crafts + Glory vs Resolve + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Dismantles an object up to (Glory × 5) Size.",
        "book": "WTF 2e p.133-134"
    },
    "command_artifice": {
        "name": "Command Artifice",
        "gift_type": "technology",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Intelligence + Science + Honor",
        "action": "Instant",
        "duration": "(Honor) hours",
        "description": "Issues a one-sentence command a device is capable of obeying.",
        "book": "WTF 2e p.134"
    },
    "shutdown": {
        "name": "Shutdown",
        "gift_type": "technology",
        "renown": "purity",
        "rank": 2,
        "cost": "**",
        "dice_pool": "Presence + Intimidate + Purity",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Extinguishes artificial lights, recording and communication devices, and security systems.",
        "book": "WTF 2e p.134"
    },
    "iron_slave": {
        "name": "Iron Slave",
        "gift_type": "technology",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Crafts + Wisdom",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Enter a trance to ride a machine spiritually, perceiving its surroundings and controlling its functions.",
        "book": "WTF 2e p.134"
    }
}

# Gift of Technology (Historical - Dark Eras)
GIFT_OF_TECHNOLOGY_HISTORICAL = {
    "hush": {
        "name": "Hush",
        "gift_type": "technology_historical",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Composure + Stealth + Cunning",
        "action": "Instant",
        "duration": "1 scene",
        "description": "All technological warning signals are silenced.",
        "book": "Dark Eras p.165"
    },
    "unmake_historical": {
        "name": "Unmake (Historical)",
        "gift_type": "technology_historical",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Crafts + Glory vs Resolve + Primal Urge",
        "action": "Instant",
        "duration": "-",
        "description": "Destroys an object up to (Glory × 5) Size.",
        "book": "Dark Eras p.166"
    },
    "balance_the_scales": {
        "name": "Balance the Scales",
        "gift_type": "technology_historical",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Resolve + Craft + Honor vs Resolve + Primal Urge",
        "action": "Instant",
        "duration": "(Honor) hours",
        "description": "A broken item works perfectly.",
        "book": "Dark Eras p.166"
    },
    "gutter": {
        "name": "Gutter",
        "gift_type": "technology_historical",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Presence + Survival + Purity",
        "action": "Instant",
        "duration": "1 scene",
        "description": "All flames within (Purity × 100) yards are reduced to embers.",
        "book": "Dark Eras p.166"
    },
    "iron_minions": {
        "name": "Iron Minions",
        "gift_type": "technology_historical",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Wits + Politics + Wisdom",
        "action": "Instant",
        "duration": "1 week",
        "description": "Be aware of an object's movements and see its surroundings.",
        "book": "Dark Eras p.166"
    }
}

# Gift of Warding
GIFT_OF_WARDING = {
    "maze_ward": {
        "name": "Maze Ward",
        "gift_type": "warding",
        "renown": "cunning",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 month",
        "description": "Penalizes attempts by intruders to navigate a warded area by Cunning through rebelling geometry, expelling on failure.",
        "book": "WTF 2e p.134"
    },
    "ward_the_wolfs_den": {
        "name": "Ward the Wolf's Den",
        "gift_type": "warding",
        "renown": "glory",
        "rank": 5,
        "cost": "●●●●● (●)",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 month",
        "description": "Penalizes attempts to cross worlds or scry through a warded area by Glory, and alerts the werewolf. Seals loci for (Glory) hours.",
        "book": "WTF 2e p.134-135"
    },
    "all_doors_locked": {
        "name": "All Doors Locked",
        "gift_type": "warding",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Senses doors and windows in a structure. The werewolf may open, close, or lock them at will.",
        "book": "WTF 2e p.135"
    },
    "predators_claim": {
        "name": "Predator's Claim",
        "gift_type": "warding",
        "renown": "purity",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 month",
        "description": "Increases the werewolf's honorary Rank by 2 within the warded area.",
        "book": "WTF 2e p.135"
    },
    "boundary_ward": {
        "name": "Boundary Ward",
        "gift_type": "warding",
        "renown": "wisdom",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 month",
        "description": "Senses when a given type of being crosses the threshold of the warded area.",
        "book": "WTF 2e p.135"
    }
}

# Gift of Weather
GIFT_OF_WEATHER = {
    "cloak_of_mist_and_haze": {
        "name": "Cloak of Mist and Haze",
        "gift_type": "weather",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "Dexterity + Stealth + Cunning",
        "action": "Extended (5, minute per roll)",
        "duration": "1 hour per success",
        "description": "Conjures a haze to penalize sight, hearing, and ranged attacks by Cunning.",
        "book": "WTF 2e p.135"
    },
    "heavens_unleashed": {
        "name": "Heavens Unleashed",
        "gift_type": "weather",
        "renown": "glory",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "Presence + Survival + Glory",
        "action": "Extended (10, minute per roll)",
        "duration": "1 hour per success",
        "description": "Conjures a flooding storm to penalize Speed and Initiative by Glory.",
        "book": "WTF 2e p.135"
    },
    "hunt_under_iron_skies": {
        "name": "Hunt Under Iron Skies",
        "gift_type": "weather",
        "renown": "honor",
        "rank": 1,
        "cost": "- (* per ally)",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Ignore negative effects conjured by your Weather Facets, and shield allies with Essence. Ignore up to your Honor in other environmental penalties.",
        "book": "WTF 2e p.136"
    },
    "grasp_of_howling_winds": {
        "name": "Grasp of Howling Winds",
        "gift_type": "weather",
        "renown": "purity",
        "rank": 2,
        "cost": "**",
        "dice_pool": "Manipulation + Survival + Purity - Stamina",
        "action": "Instant",
        "duration": "1 turn per success",
        "description": "Howl a fierce gust that penalizes one target's Speed and Physical actions by your Purity.",
        "book": "WTF 2e p.136"
    },
    "hunt_of_fire_and_ice": {
        "name": "Hunt of Fire and Ice",
        "gift_type": "weather",
        "renown": "wisdom",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "Intelligence + Occult + Wisdom",
        "action": "Extended (10, minute per success)",
        "duration": "1 hour per success",
        "description": "Conjure either the Extreme Cold or Extreme Heat Tilt.",
        "book": "WTF 2e p.136"
    }
}

# Gift of Change
GIFT_OF_CHANGE = {
    "skin_thief": {
        "name": "Skin Thief",
        "gift_type": "change",
        "renown": "cunning",
        "rank": 5,
        "cost": "●●●●● (○)",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Skin and don the hide of a human or predatory animal at least as large as a wolf to take its appearance, except for eyes, in Hishu or Urhan respectively.",
        "book": "WTF 2e p.136"
    },
    "gaze_of_the_moon": {
        "name": "Gaze of the Moon",
        "gift_type": "change",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "-",
        "description": "Inflict Lunacy with a look.",
        "book": "WTF 2e p.136"
    },
    "lunas_embrace": {
        "name": "Luna's Embrace",
        "gift_type": "change",
        "renown": "honor",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "Indefinite",
        "description": "Change sex.",
        "book": "WTF 2e p.136-137"
    },
    "the_fathers_form": {
        "name": "The Father's Form",
        "gift_type": "change",
        "renown": "purity",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "-",
        "duration": "-",
        "description": "You can adopt a modified Gauru that is less unstoppable, but which doesn't have to attack to hold back Death Rage. This is a breaking point towards flesh.",
        "book": "WTF 2e p.137"
    },
    "quicksilver_flesh": {
        "name": "Quicksilver Flesh",
        "gift_type": "change",
        "renown": "wisdom",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 scene",
        "description": "Manifest a partially shapeshifted aspect while in a different form, such as manipulative hands, human vocal cords, claws, or lupine striding legs.",
        "book": "WTF 2e p.137"
    }
}

# Gift of Hunting
GIFT_OF_HUNTING = {
    "honed_senses": {
        "name": "Honed Senses",
        "gift_type": "hunting",
        "renown": "cunning",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Perception rolls achieve exceptional success on a threshold of three instead of five.",
        "book": "WTF 2e p.137"
    },
    "cow_the_prey": {
        "name": "Cow the Prey",
        "gift_type": "hunting",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Wield the Hunter's Aspect as a Persistent Condition.",
        "book": "WTF 2e p.137"
    },
    "beast_talker": {
        "name": "Beast Talker",
        "gift_type": "hunting",
        "renown": "honor",
        "rank": 1,
        "cost": "-",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Communicate with animals.",
        "book": "WTF 2e p.137"
    },
    "tireless_hunter": {
        "name": "Tireless Hunter",
        "gift_type": "hunting",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Instant",
        "duration": "1 day",
        "description": "While pursuing the Sacred Hunt, ignore the need to eat or drink, the inability to spend Willpower, and up to your Purity in fatigue penalties.",
        "book": "WTF 2e p.137"
    },
    "impossible_spoor": {
        "name": "Impossible Spoor",
        "gift_type": "hunting",
        "renown": "wisdom",
        "rank": 1,
        "cost": "(*+)",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "1 scene",
        "description": "Track infinitesimal traces, adding two successes to any successful tracking roll. Spend Essence to ignore penalties from old trails or from environmental degredation.",
        "book": "WTF 2e p.137-138"
    }
}

# Gift of Pack
GIFT_OF_PACK = {
    "reflected_facets": {
        "name": "Reflected Facets",
        "gift_type": "pack",
        "renown": "cunning",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Use one of your Facets through a werewolf packmate within (Cunning) miles.",
        "book": "WTF 2e p.138"
    },
    "down_the_prey": {
        "name": "Down the Prey",
        "gift_type": "pack",
        "renown": "glory",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "When striking an enemy wounded by a packmate, either inflict a temporary -2 penalty, gain a temporary +2 Defense against them, or if their Defense was reduced to zero, knock them down.",
        "book": "WTF 2e p.138"
    },
    "totems_wrath": {
        "name": "Totem's Wrath",
        "gift_type": "pack",
        "renown": "honor",
        "rank": 5,
        "cost": "*****",
        "dice_pool": "Presence + Occult + Honor vs Power + Finesse + Resistance",
        "action": "Instant",
        "duration": "-",
        "description": "Materialize your totem spirit in a body-shell like a lesser Gauru, anchored by the Death Rage and bleeding Essence each turn. The raging totem will not strike allies with the Totem Merit.",
        "book": "WTF 2e p.138"
    },
    "maw_of_madness": {
        "name": "Maw of Madness",
        "gift_type": "pack",
        "renown": "purity",
        "rank": 1,
        "cost": "*",
        "dice_pool": "-",
        "action": "Reflexive",
        "duration": "-",
        "description": "Infect a human with the Moon Taint Condition through your bite, threatening to unleash them for one night as a raging lesser werewolf.",
        "book": "WTF 2e p.138"
    },
    "pack_awareness": {
        "name": "Pack Awareness",
        "gift_type": "pack",
        "renown": "wisdom",
        "rank": 1,
        "cost": "(*)",
        "dice_pool": "-",
        "action": "None",
        "duration": "Permanent",
        "description": "Sense the location and state of packmates within (Wisdom) miles. Spend Essence to communicate with them spiritually for a scene.",
        "book": "WTF 2e p.138"
    }
}

ALL_SHADOW_GIFTS = {
    **GIFT_OF_AGONY,
    **GIFT_OF_BLOOD,
    **GIFT_OF_DEATH,
    **GIFT_OF_DISEASE,
    **GIFT_OF_DOMINANCE,
    **GIFT_OF_THE_ELEMENTALS,
    **GIFT_OF_EVASION,
    **GIFT_OF_FERVOR,
    **GIFT_OF_HUNGER,
    **GIFT_OF_INSIGHT,
    **GIFT_OF_INSPIRATION,
    **GIFT_OF_KNOWLEDGE,
    **GIFT_OF_NATURE,
    **GIFT_OF_RAGE,
    **GIFT_OF_SHAPING,
    **GIFT_OF_STEALTH,
    **GIFT_OF_STRENGTH,
    **GIFT_OF_TECHNOLOGY,
    **GIFT_OF_TECHNOLOGY_HISTORICAL,
    **GIFT_OF_WARDING,
    **GIFT_OF_WEATHER,
    **GIFT_OF_CHANGE,
    **GIFT_OF_HUNTING,
    **GIFT_OF_PACK
}

# Consolidated all gifts
ALL_WEREWOLF_GIFTS = {
    **ALL_MOON_GIFTS,
    **ALL_SHADOW_GIFTS
}

# Gift categories for organization
GIFT_CATEGORIES = {
    # Moon Gifts (Auspice)
    "crescent_moon": CRESCENT_MOON_GIFT,
    "full_moon": FULL_MOON_GIFT,
    "gibbous_moon": GIBBOUS_MOON_GIFT,
    "half_moon": HALF_MOON_GIFT,
    "new_moon": NEW_MOON_GIFT,
    # Shadow Gifts
    "agony": GIFT_OF_AGONY,
    "blood": GIFT_OF_BLOOD,
    "death": GIFT_OF_DEATH,
    "disease": GIFT_OF_DISEASE,
    "dominance": GIFT_OF_DOMINANCE,
    "elementals": GIFT_OF_THE_ELEMENTALS,
    "evasion": GIFT_OF_EVASION,
    "fervor": GIFT_OF_FERVOR,
    "hunger": GIFT_OF_HUNGER,
    "insight": GIFT_OF_INSIGHT,
    "inspiration": GIFT_OF_INSPIRATION,
    "knowledge": GIFT_OF_KNOWLEDGE,
    "nature": GIFT_OF_NATURE,
    "rage": GIFT_OF_RAGE,
    "shaping": GIFT_OF_SHAPING,
    "stealth": GIFT_OF_STEALTH,
    "strength": GIFT_OF_STRENGTH,
    "technology": GIFT_OF_TECHNOLOGY,
    "technology_historical": GIFT_OF_TECHNOLOGY_HISTORICAL,
    "warding": GIFT_OF_WARDING,
    "weather": GIFT_OF_WEATHER,
    "change": GIFT_OF_CHANGE,
    "hunting": GIFT_OF_HUNTING,
    "pack": GIFT_OF_PACK
}

# Gifts organized by renown
GIFTS_BY_RENOWN = {
    "cunning": {},
    "glory": {},
    "honor": {},
    "purity": {},
    "wisdom": {}
}

# Populate renown dictionary
for gift_key, gift_data in ALL_WEREWOLF_GIFTS.items():
    renown = gift_data.get('renown')
    if renown:
        GIFTS_BY_RENOWN[renown][gift_key] = gift_data

# Helper functions
def get_gift(gift_key):
    """Get a specific gift by key."""
    return ALL_WEREWOLF_GIFTS.get(gift_key.lower().replace(" ", "_"))


def get_gifts_by_type(gift_type):
    """Get all gifts of a specific type (e.g., 'agony', 'blood', 'crescent_moon')."""
    gift_type = gift_type.lower().replace(" ", "_")
    return GIFT_CATEGORIES.get(gift_type, {})


def get_gifts_by_renown(renown):
    """Get all gifts of a specific renown."""
    return GIFTS_BY_RENOWN.get(renown.lower(), {})


def get_gifts_by_rank(rank):
    """Get all gifts at a specific rank."""
    gifts = {}
    for key, data in ALL_WEREWOLF_GIFTS.items():
        if data.get('rank') == rank:
            gifts[key] = data
    return gifts


def get_moon_gift_by_auspice(auspice):
    """Get moon gifts for a specific auspice."""
    auspice = auspice.lower().replace(" ", "_")
    return MOON_GIFTS_BY_AUSPICE.get(auspice, {})


def get_all_gifts():
    """Get all werewolf gifts."""
    return ALL_WEREWOLF_GIFTS


def get_all_moon_gifts():
    """Get all moon gifts (auspice gifts)."""
    return ALL_MOON_GIFTS


def get_all_shadow_gifts():
    """Get all shadow gifts."""
    return ALL_SHADOW_GIFTS


