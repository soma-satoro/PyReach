"""
Promethean: The Created - Detailed Alembic Data
Complete alembic information including dice pools, Pyros costs, and descriptions.
Based on Promethean: The Created 2nd Edition.
"""

# ==================== ALCHEMICUS ====================

# Stone Distillation
ALEMBIC_STONE = {
    "name": "Stone",
    "transmutation": "Alchemicus",
    "distillation": "Stone",
    "rank": 1,
    "charge": "--",
    "dice_pool": "Wits + Science + Azoth",
    "action": "Instant",
    "description": "Roll to scrutinize the composition of an object.",
    "book": "PTC 2e p.119"
}

ALEMBIC_PURIFICATION = {
    "name": "Purification",
    "transmutation": "Alchemicus",
    "distillation": "Stone",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Intelligence + Occult + Azoth",
    "action": "Instant",
    "description": "Temporarily improve an object's functionality.",
    "book": "PTC 2e p.119"
}

ALEMBIC_FORTIFICATION = {
    "name": "Fortification",
    "transmutation": "Alchemicus",
    "distillation": "Stone",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Stamina + Science + Azoth",
    "action": "Reflexive",
    "description": "Temporarily reinforce an object's Durability.",
    "book": "PTC 2e p.119"
}

ALEMBIC_TRANSFORMATION = {
    "name": "Transformation",
    "transmutation": "Alchemicus",
    "distillation": "Stone",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Intelligence + Occult + Azoth",
    "action": "Instant",
    "description": "Temporarily transmute one inorganic material into another.",
    "book": "PTC 2e p.119"
}

# Aqua Regia Distillation
ALEMBIC_AQUA_REGIA = {
    "name": "Aqua Regia",
    "transmutation": "Alchemicus",
    "distillation": "Aqua Regia",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "Reflexive",
    "description": "Ignore bashing damage from caustics, and reduce lethal damage from them by your Azoth.",
    "book": "PTC 2e p.120"
}

ALEMBIC_DECAY = {
    "name": "Decay",
    "transmutation": "Alchemicus",
    "distillation": "Aqua Regia",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Stamina + Occult + Azoth",
    "action": "Reflexive",
    "description": "Temporarily weaken an object's functionality.",
    "book": "PTC 2e p.120"
}

ALEMBIC_DEGRADATION = {
    "name": "Degradation",
    "transmutation": "Alchemicus",
    "distillation": "Aqua Regia",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Stamina + Occult + Azoth",
    "action": "Reflexive",
    "description": "Temporarily buckle an object's Durability.",
    "book": "PTC 2e p.120"
}

ALEMBIC_DISSOLUTION = {
    "name": "Dissolution",
    "transmutation": "Alchemicus",
    "distillation": "Aqua Regia",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Stamina + Occult + Azoth",
    "action": "Reflexive",
    "description": "Secrete an acid to deal lethal damage.",
    "book": "PTC 2e p.120"
}

# Spagyria Distillation
ALEMBIC_SPAGYRIA = {
    "name": "Spagyria",
    "transmutation": "Alchemicus",
    "distillation": "Spagyria",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "Instant",
    "description": "Extend an Alchemicus Distillation to last 24 hours for one Pyros.",
    "book": "PTC 2e p.120"
}

ALEMBIC_TEMPERATURE_MODIFICATION = {
    "name": "Temperature Modification",
    "transmutation": "Alchemicus",
    "distillation": "Spagyria",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Intelligence + Science + Azoth",
    "action": "Instant",
    "description": "Temporarily heat or cool an object.",
    "book": "PTC 2e p.120"
}

ALEMBIC_ALTERATION = {
    "name": "Alteration",
    "transmutation": "Alchemicus",
    "distillation": "Spagyria",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Strength + Crafts + Azoth",
    "action": "Extended",
    "description": "Temporarily resculpt an object.",
    "book": "PTC 2e p.120"
}

ALEMBIC_RESIZE = {
    "name": "Resize",
    "transmutation": "Alchemicus",
    "distillation": "Spagyria",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Manipulation + Occult + Azoth",
    "action": "Instant",
    "description": "Shrink or enlarge an object.",
    "book": "PTC 2e p.120"
}

# Elixir Distillation
ALEMBIC_ELIXIR = {
    "name": "Elixir",
    "transmutation": "Alchemicus",
    "distillation": "Elixir",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Roll exceptional successes with Occult at a threshold of three.",
    "book": "PTC 2e p.122"
}

ALEMBIC_APPRENTICES_BROOMS = {
    "name": "Apprentice's Brooms",
    "transmutation": "Alchemicus",
    "distillation": "Elixir",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Intelligence + Occult + Azoth",
    "action": "Instant",
    "description": "Temporarily charge Azothic Objects, enhancing an object's functionality.",
    "book": "PTC 2e p.122"
}

ALEMBIC_SPARK_OF_LIFE = {
    "name": "Spark of Life",
    "transmutation": "Alchemicus",
    "distillation": "Elixir",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Occult + Azoth",
    "action": "Instant",
    "description": "Temporarily raise a corpse as an undead servant.",
    "book": "PTC 2e p.122"
}

ALEMBIC_FLESH_TO_STONE = {
    "name": "Flesh to Stone",
    "transmutation": "Alchemicus",
    "distillation": "Elixir",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Intelligence + Crafts - Stamina",
    "action": "Instant",
    "description": "Temporarily petrify a target, immobilizing them.",
    "book": "PTC 2e p.122"
}

# ==================== BENEFICE ====================

# Command Distillation
ALEMBIC_COMMAND = {
    "name": "Command",
    "transmutation": "Benefice",
    "distillation": "Command",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Add +1 to teamwork rolls with your throng.",
    "book": "PTC 2e p.123"
}

ALEMBIC_MANY_HANDS_MAKE_LIGHT_WORK = {
    "name": "Many Hands Make Light Work",
    "transmutation": "Benefice",
    "distillation": "Command",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "All members of your throng may contribute to a non-combat effort with teamwork.",
    "book": "PTC 2e p.123"
}

ALEMBIC_ABLE_WORKER = {
    "name": "Able Worker",
    "transmutation": "Benefice",
    "distillation": "Command",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Sharpen the resolve of a throngmate.",
    "book": "PTC 2e p.123"
}

ALEMBIC_THE_COMMUNITY_OF_POWER = {
    "name": "The Community of Power",
    "transmutation": "Benefice",
    "distillation": "Command",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Intelligence + Occult + Azoth",
    "action": "Reflexive",
    "description": "You may use teamwork to support the use of Bestowments and Distillations within the throng.",
    "book": "PTC 2e p.123"
}

# Consortium Distillation
ALEMBIC_CONSORTIUM = {
    "name": "Consortium",
    "transmutation": "Benefice",
    "distillation": "Consortium",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "Reflexive",
    "description": "Once per turn, two throng members may swap Initiative.",
    "book": "PTC 2e p.124"
}

ALEMBIC_THE_FORTIFIED_COMPACT = {
    "name": "The Fortified Compact",
    "transmutation": "Benefice",
    "distillation": "Consortium",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Strengthens the effects of the throng's brand.",
    "book": "PTC 2e p.124"
}

ALEMBIC_COMMON_PERCEPTION = {
    "name": "Common Perception",
    "transmutation": "Benefice",
    "distillation": "Consortium",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Share your senses with a throngmate, who may at will use your senses, use their own, or split their attention between both.",
    "book": "PTC 2e p.124"
}

ALEMBIC_UNSPOKEN_WORDS = {
    "name": "Unspoken Words",
    "transmutation": "Benefice",
    "distillation": "Consortium",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Members of the throng may communicate telepathically, and gain +3 Initiative.",
    "book": "PTC 2e p.124"
}

# Control Distillation
ALEMBIC_CONTROL = {
    "name": "Control",
    "transmutation": "Benefice",
    "distillation": "Control",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "+1 Defense when fighting alongside a throngmate.",
    "book": "PTC 2e p.124"
}

ALEMBIC_PROTECTIVE_BOON = {
    "name": "Protective Boon",
    "transmutation": "Benefice",
    "distillation": "Control",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Enhance the Defense of a chosen throngmate, even against ranged attacks.",
    "book": "PTC 2e p.124"
}

ALEMBIC_INVIOLABLE_UNITY = {
    "name": "Inviolable Unity",
    "transmutation": "Benefice",
    "distillation": "Control",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Occult + Azoth",
    "action": "Instant",
    "description": "Distribute the alchemical brand as points of Armor among the throng.",
    "book": "PTC 2e p.124"
}

ALEMBIC_BULWARK = {
    "name": "Bulwark",
    "transmutation": "Benefice",
    "distillation": "Control",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Sharpen the resolve of a throngmate.",
    "book": "PTC 2e p.125"
}

# Community Distillation
ALEMBIC_COMMUNITY = {
    "name": "Community",
    "transmutation": "Benefice",
    "distillation": "Community",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "Reflexive",
    "description": "Share Pyros with your throng more freely, once per turn.",
    "book": "PTC 2e p.125"
}

ALEMBIC_COMMUNAL_FONT = {
    "name": "Communal Font",
    "transmutation": "Benefice",
    "distillation": "Community",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Become a conduit for your entire throng to share Pyros on a per-turn basis.",
    "book": "PTC 2e p.125"
}

ALEMBIC_WE_ARE_AS_ONE = {
    "name": "We Are As One",
    "transmutation": "Benefice",
    "distillation": "Community",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Target nearby throngmates with Distillations that normally require touch.",
    "book": "PTC 2e p.125"
}

ALEMBIC_WHATS_MINE_IS_YOURS = {
    "name": "What's Mine Is Yours",
    "transmutation": "Benefice",
    "distillation": "Community",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Wits + Occult + Azoth",
    "action": "Instant",
    "description": "Share a Bestowment or calcified Alembic with a throngmate for a scene.",
    "book": "PTC 2e p.125"
}

# ==================== CONTAMINATION ====================

# Indulgence Distillation
ALEMBIC_INDULGENCE = {
    "name": "Indulgence",
    "transmutation": "Contamination",
    "distillation": "Indulgence",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Sense Vices and benefit from a better impression when appealing to them.",
    "book": "PTC 2e p.125"
}

ALEMBIC_ENCOURAGE_IMPULSE = {
    "name": "Encourage Impulse",
    "transmutation": "Contamination",
    "distillation": "Indulgence",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Manipulation + Empathy + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Provoke impulsive action from the target's Vice.",
    "book": "PTC 2e p.125"
}

ALEMBIC_REMOVE_INHIBITIONS = {
    "name": "Remove Inhibitions",
    "transmutation": "Contamination",
    "distillation": "Indulgence",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Persuasion + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Temporarily enslave the target to his Vice.",
    "book": "PTC 2e p.125"
}

ALEMBIC_PLAGUE_OF_DESIRE = {
    "name": "Plague of Desire",
    "transmutation": "Contamination",
    "distillation": "Indulgence",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Persuasion + Azoth",
    "action": "Instant",
    "description": "Evoke mob mentality centering around strong personalities in a crowd.",
    "book": "PTC 2e p.125"
}

# Leverage Distillation
ALEMBIC_LEVERAGE = {
    "name": "Leverage",
    "transmutation": "Contamination",
    "distillation": "Leverage",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Ignore one Door when maneuvering to uncover secrets.",
    "book": "PTC 2e p.126"
}

ALEMBIC_CONFESSION = {
    "name": "Confession",
    "transmutation": "Contamination",
    "distillation": "Leverage",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Manipulation + Persuasion + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Prompt an honest answer to a leading question.",
    "book": "PTC 2e p.126"
}

ALEMBIC_GUILT_TRIP = {
    "name": "Guilt Trip",
    "transmutation": "Contamination",
    "distillation": "Leverage",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Wits + Empathy + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Draw out the subject's worst memory of herself.",
    "book": "PTC 2e p.126"
}

ALEMBIC_SCANDAL = {
    "name": "Scandal",
    "transmutation": "Contamination",
    "distillation": "Leverage",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Resolve + Subterfuge + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Contagiously spread intuitive knowledge of the subject's worst deed by touch for a day.",
    "book": "PTC 2e p.126"
}

# Madness Distillation
ALEMBIC_MADNESS = {
    "name": "Madness",
    "transmutation": "Contamination",
    "distillation": "Madness",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Sense Persistent Conditions relating to mental ailment and trauma.",
    "book": "PTC 2e p.127"
}

ALEMBIC_PSYCHOTIC_FLASH = {
    "name": "Psychotic Flash",
    "transmutation": "Contamination",
    "distillation": "Madness",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Presence + Intimidation + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Stun the target with a brief traumatic psychic break.",
    "book": "PTC 2e p.127"
}

ALEMBIC_ONSET_OF_MADNESS = {
    "name": "Onset of Madness",
    "transmutation": "Contamination",
    "distillation": "Madness",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Subterfuge + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Inflict mental instability for a matter of days, like an undirected Disquiet.",
    "book": "PTC 2e p.127"
}

ALEMBIC_CATHARSIS = {
    "name": "Catharsis",
    "transmutation": "Contamination",
    "distillation": "Madness",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Wits + Empathy + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Join a target in his own mind for an internal symbolic harrowing, which may either heal or worsen mental wounds.",
    "book": "PTC 2e p.127"
}

# Suffering Distillation
ALEMBIC_SUFFERING = {
    "name": "Suffering",
    "transmutation": "Contamination",
    "distillation": "Suffering",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "Instant",
    "description": "Scrutinize an opponent as an instant action for weaknesses to exploit as a 1L weapon rating.",
    "book": "PTC 2e p.128"
}

ALEMBIC_PURGE = {
    "name": "Purge",
    "transmutation": "Contamination",
    "distillation": "Suffering",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Resolve + Medicine + Azoth - Toxicity",
    "action": "Instant",
    "description": "Remove a disease or poison by drawing it out of the subject's body.",
    "book": "PTC 2e p.128"
}

ALEMBIC_AFFLICTION = {
    "name": "Affliction",
    "transmutation": "Contamination",
    "distillation": "Suffering",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Intelligence + Medicine + Azoth vs Stamina + Tolerance",
    "action": "Instant",
    "description": "Double pain debilities such as wound penalties for a scene.",
    "book": "PTC 2e p.128"
}

ALEMBIC_PAIN = {
    "name": "Pain",
    "transmutation": "Contamination",
    "distillation": "Suffering",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Cause incapacitating pain with a touch or close-combat attack.",
    "book": "PTC 2e p.128"
}

# ==================== CORPOREUM ====================

# Charites Distillation
ALEMBIC_CHARITES = {
    "name": "Charites",
    "transmutation": "Corporeum",
    "distillation": "Charites",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Roll exceptional successes with Athletics at a threshold of three.",
    "book": "PTC 2e p.129"
}

ALEMBIC_ATHLETIC_GRACE = {
    "name": "Athletic Grace",
    "transmutation": "Corporeum",
    "distillation": "Charites",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Temporarily increase Dexterity.",
    "book": "PTC 2e p.129"
}

ALEMBIC_UNCANNY_DEXTERITY = {
    "name": "Uncanny Dexterity",
    "transmutation": "Corporeum",
    "distillation": "Charites",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Dexterity rolls take 9-Again, and may be rerolled by spending Pyros.",
    "book": "PTC 2e p.129"
}

ALEMBIC_RARIFIED_GRACE = {
    "name": "Rarified Grace",
    "transmutation": "Corporeum",
    "distillation": "Charites",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Up to (Azoth) Dexterity and Dodge rolls take the rote quality. Spend Willpower to restock.",
    "book": "PTC 2e p.129"
}

# Zephyrus Distillation
ALEMBIC_ZEPHYRUS = {
    "name": "Zephyrus",
    "transmutation": "Corporeum",
    "distillation": "Zephyrus",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Add Azoth to rolls against surprise, and keep half your Defense on failure.",
    "book": "PTC 2e p.129"
}

ALEMBIC_SWIFT_FEET = {
    "name": "Swift Feet",
    "transmutation": "Corporeum",
    "distillation": "Zephyrus",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Double your Speed.",
    "book": "PTC 2e p.129"
}

ALEMBIC_SERPENT_STRIKE = {
    "name": "Serpent Strike",
    "transmutation": "Corporeum",
    "distillation": "Zephyrus",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Add Azoth to Initiative. Spend Pyros to ignore a weapon's Initiative penalty.",
    "book": "PTC 2e p.129"
}

ALEMBIC_PERFECTED_REFLEXES = {
    "name": "Perfected Reflexes",
    "transmutation": "Corporeum",
    "distillation": "Zephyrus",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "+3 Defense, Dodge with 8-Again. Apply Defense against ranged attacks.",
    "book": "PTC 2e p.129"
}

# Hygeius Distillation
ALEMBIC_HYGEIUS = {
    "name": "Hygeius",
    "transmutation": "Corporeum",
    "distillation": "Hygeius",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Benefit from inverted wound 'penalties.'",
    "book": "PTC 2e p.130"
}

ALEMBIC_HUMAN_FLESH = {
    "name": "Human Flesh",
    "transmutation": "Corporeum",
    "distillation": "Hygeius",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Assume a human biology. Do not show disfigurements.",
    "book": "PTC 2e p.130"
}

ALEMBIC_IMPOSSIBLE_FLESH = {
    "name": "Impossible Flesh",
    "transmutation": "Corporeum",
    "distillation": "Hygeius",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Ignore Physical Tilts, even dismemberment.",
    "book": "PTC 2e p.130"
}

ALEMBIC_RESILIENT_FLESH = {
    "name": "Resilient Flesh",
    "transmutation": "Corporeum",
    "distillation": "Hygeius",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Reduce all damage suffered by two points.",
    "book": "PTC 2e p.130"
}

# Motus Distillation
ALEMBIC_MOTUS = {
    "name": "Motus",
    "transmutation": "Corporeum",
    "distillation": "Motus",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "While moving, ignore fatigue and tiring.",
    "book": "PTC 2e p.130"
}

ALEMBIC_UNCANNY_ATHLETICISM = {
    "name": "Uncanny Athleticism",
    "transmutation": "Corporeum",
    "distillation": "Motus",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Strength + Athletics + Azoth",
    "action": "Reflexive",
    "description": "Increase Strength or Stamina as applied to athletics and endurance.",
    "book": "PTC 2e p.130"
}

ALEMBIC_MIGHTY_BOUND = {
    "name": "Mighty Bound",
    "transmutation": "Corporeum",
    "distillation": "Motus",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Triple horizontal jump distance. Double vertical jump distance.",
    "book": "PTC 2e p.130"
}

ALEMBIC_EXEMPLARY_ATHLETICISM = {
    "name": "Exemplary Athleticism",
    "transmutation": "Corporeum",
    "distillation": "Motus",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Double your Speed. Increase all Physical Attributes. Take the rote quality on rolls that benefit from Uncanny Athleticism.",
    "book": "PTC 2e p.130"
}

# ==================== DECEPTION ====================

# Anonymity Distillation
ALEMBIC_ANONYMITY = {
    "name": "Anonymity",
    "transmutation": "Deception",
    "distillation": "Anonymity",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Inflict a -2 penalty to pick you out in a crowd.",
    "book": "PTC 2e p.132"
}

ALEMBIC_NAMELESS = {
    "name": "Nameless",
    "transmutation": "Deception",
    "distillation": "Anonymity",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Presence + Stealth + Azoth",
    "action": "Instant",
    "description": "Become unremarkable and unmemorable for a scene.",
    "book": "PTC 2e p.132"
}

ALEMBIC_TRACELESS = {
    "name": "Traceless",
    "transmutation": "Deception",
    "distillation": "Anonymity",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Wits + Stealth + Azoth",
    "action": "Instant",
    "description": "Leave no evidence of your passing, and trigger no alarms, for a scene.",
    "book": "PTC 2e p.132"
}

ALEMBIC_FORGOTTEN = {
    "name": "Forgotten",
    "transmutation": "Deception",
    "distillation": "Anonymity",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Extend the charge of Anonymity for a point of Pyros every 24 hours, at the cost of risking Torment afterward.",
    "book": "PTC 2e p.132"
}

# Assimilation Distillation
ALEMBIC_ASSIMILATION = {
    "name": "Assimilation",
    "transmutation": "Deception",
    "distillation": "Assimilation",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Make a better social impression in group settings.",
    "book": "PTC 2e p.132"
}

ALEMBIC_CONFORMITY = {
    "name": "Conformity",
    "transmutation": "Deception",
    "distillation": "Assimilation",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Stamina + Subterfuge + Azoth",
    "action": "Instant",
    "description": "Adopt physical features to blend into a crowd. Add Azoth as a bonus to hide.",
    "book": "PTC 2e p.132"
}

ALEMBIC_TONGUES = {
    "name": "Tongues",
    "transmutation": "Deception",
    "distillation": "Assimilation",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Intelligence + Academics + Azoth",
    "action": "Instant",
    "description": "Gain fluency, but not literacy, in a host group's language for a scene.",
    "book": "PTC 2e p.132"
}

ALEMBIC_HIVE_MIND = {
    "name": "Hive Mind",
    "transmutation": "Deception",
    "distillation": "Assimilation",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Wits + Empathy + Azoth",
    "action": "Instant",
    "description": "Reproduce the mannerisms of your host group, granting a bonus to social rolls within the group.",
    "book": "PTC 2e p.132"
}

# Doppelganger Distillation
ALEMBIC_DOPPELGANGER = {
    "name": "Doppelganger",
    "transmutation": "Deception",
    "distillation": "Doppelganger",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Perfectly imitate voices you have heard.",
    "book": "PTC 2e p.133"
}

ALEMBIC_INCRIMINATE = {
    "name": "Incriminate",
    "transmutation": "Deception",
    "distillation": "Doppelganger",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Wits + Empathy + Azoth vs Stamina + Tolerance",
    "action": "Instant",
    "description": "Evidence of your passing instead points toward a subject you have touched.",
    "book": "PTC 2e p.133"
}

ALEMBIC_IMPERSONATE = {
    "name": "Impersonate",
    "transmutation": "Deception",
    "distillation": "Doppelganger",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Subterfuge + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Transform bodily to duplicate a subject you have touched this scene.",
    "book": "PTC 2e p.133"
}

ALEMBIC_DEEP_COVER = {
    "name": "Deep Cover",
    "transmutation": "Deception",
    "distillation": "Doppelganger",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Extend the charge of Impersonate for a point of Pyros every 24 hours, at the cost of risking amnesia afterward.",
    "book": "PTC 2e p.133"
}

# Stalker Distillation
ALEMBIC_STALKER = {
    "name": "Stalker",
    "transmutation": "Deception",
    "distillation": "Stalker",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Add Azoth as a bonus to Stealth rolls.",
    "book": "PTC 2e p.134"
}

ALEMBIC_SHADOW = {
    "name": "Shadow",
    "transmutation": "Deception",
    "distillation": "Stalker",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Wits + Stealth + Azoth vs Wits + Tolerance",
    "action": "Instant",
    "description": "+3 to hide from, shadow or ambush the subject for a scene.",
    "book": "PTC 2e p.134"
}

ALEMBIC_LURKER = {
    "name": "Lurker",
    "transmutation": "Deception",
    "distillation": "Stalker",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Wits + Stealth + Azoth vs Wits + Tolerance",
    "action": "Instant",
    "description": "Escape the subject's notice for a scene.",
    "book": "PTC 2e p.134"
}

ALEMBIC_PHANTOM = {
    "name": "Phantom",
    "transmutation": "Deception",
    "distillation": "Stalker",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Composure + Stealth + Azoth",
    "action": "Instant",
    "description": "Escape notice within a particular building for a scene.",
    "book": "PTC 2e p.134"
}

# ==================== DISQUIETISM ====================

# Externalize Distillation
ALEMBIC_EXTERNALIZE = {
    "name": "Externalize",
    "transmutation": "Disquietism",
    "distillation": "Externalize",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Immunity to extreme environment effects in Wastelands.",
    "book": "PTC 2e p.134"
}

ALEMBIC_SAFE_SOJOURN = {
    "name": "Safe Sojourn",
    "transmutation": "Disquietism",
    "distillation": "Externalize",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Stamina + Survival + Azoth - Wasteland",
    "action": "Instant",
    "description": "Share your environmental immunity with your throng or others.",
    "book": "PTC 2e p.134"
}

ALEMBIC_MAELSTROM = {
    "name": "Maelstrom",
    "transmutation": "Disquietism",
    "distillation": "Externalize",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Strength + Occult + Azoth - Wasteland",
    "action": "Instant",
    "description": "Cause a heavy storm as a Tilt to which you're immune.",
    "book": "PTC 2e p.134"
}

ALEMBIC_ASSAULT = {
    "name": "Assault",
    "transmutation": "Disquietism",
    "distillation": "Externalize",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Dexterity + Athletics + Azoth - Defense",
    "action": "Instant",
    "description": "Project a bolt of Flux, dealing lethal damage that ignores artificial Armor.",
    "book": "PTC 2e p.134"
}

# Internalize Distillation
ALEMBIC_INTERNALIZE = {
    "name": "Internalize",
    "transmutation": "Disquietism",
    "distillation": "Internalize",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Identify the progression of Disquiet on sight.",
    "book": "PTC 2e p.135"
}

ALEMBIC_TEMPER = {
    "name": "Temper",
    "transmutation": "Disquietism",
    "distillation": "Internalize",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Composure + Empathy + Azoth",
    "action": "Reflexive",
    "description": "Confer a bonus to resist your Disquiet for a scene.",
    "book": "PTC 2e p.135"
}

ALEMBIC_SOOTHE = {
    "name": "Soothe",
    "transmutation": "Disquietism",
    "distillation": "Internalize",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Empathy + Azoth",
    "action": "Reflexive",
    "description": "Briefly lift the effects of Disquiet.",
    "book": "PTC 2e p.135"
}

ALEMBIC_QUELL = {
    "name": "Quell",
    "transmutation": "Disquietism",
    "distillation": "Internalize",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Socialize + Azoth",
    "action": "Instant",
    "description": "Shield subjects from your Disquiet for one scene.",
    "book": "PTC 2e p.135"
}

# Redirect Distillation
ALEMBIC_REDIRECT = {
    "name": "Redirect",
    "transmutation": "Disquietism",
    "distillation": "Redirect",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Roll exceptional successes with Subterfuge at a threshold of three.",
    "book": "PTC 2e p.135"
}

ALEMBIC_SCAPEGOAT = {
    "name": "Scapegoat",
    "transmutation": "Disquietism",
    "distillation": "Redirect",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Manipulation + Persuasion + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "For one scene, evoke Disquiet directed at a touched subject instead of yourself.",
    "book": "PTC 2e p.135"
}

ALEMBIC_RABID_RAGE = {
    "name": "Rabid Rage",
    "transmutation": "Disquietism",
    "distillation": "Redirect",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Animal Ken + Azoth vs Resolve",
    "action": "Instant",
    "description": "Sic a Disquieted animal on the scapegoat.",
    "book": "PTC 2e p.135"
}

ALEMBIC_IAGOS_WHISPER = {
    "name": "Iago's Whisper",
    "transmutation": "Disquietism",
    "distillation": "Redirect",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Manipulation + Subterfuge + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Incite violence against the scapegoat.",
    "book": "PTC 2e p.135"
}

# Weaponize Distillation
ALEMBIC_WEAPONIZE = {
    "name": "Weaponize",
    "transmutation": "Disquietism",
    "distillation": "Weaponize",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "+2 to Intimidation rolls within a day of evoking Disquiet.",
    "book": "PTC 2e p.137"
}

ALEMBIC_TENSION = {
    "name": "Tension",
    "transmutation": "Disquietism",
    "distillation": "Weaponize",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Presence + Intimidation + Azoth",
    "action": "Instant",
    "description": "Evoke Disquiet progress and inflict proportional action penalties.",
    "book": "PTC 2e p.137"
}

ALEMBIC_VANQUISH = {
    "name": "Vanquish",
    "transmutation": "Disquietism",
    "distillation": "Weaponize",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "When you strike a Disquieted target, they are Beaten Down.",
    "book": "PTC 2e p.137"
}

ALEMBIC_RAMPAGE = {
    "name": "Rampage",
    "transmutation": "Disquietism",
    "distillation": "Weaponize",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Unarmed attacks gain a weapon rating proportional to the victim's Disquiet.",
    "book": "PTC 2e p.137"
}

# ==================== ELECTRIFICATION ====================

# Machinus Distillation
ALEMBIC_MACHINUS = {
    "name": "Machinus",
    "transmutation": "Electrification",
    "distillation": "Machinus",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Sense electrical activity and anticipate lightning strikes.",
    "book": "PTC 2e p.137"
}

ALEMBIC_JOLT = {
    "name": "Jolt",
    "transmutation": "Electrification",
    "distillation": "Machinus",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Power electrical devices by handling them.",
    "book": "PTC 2e p.137"
}

ALEMBIC_GENERATOR = {
    "name": "Generator",
    "transmutation": "Electrification",
    "distillation": "Machinus",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Power electrical devices at a distance.",
    "book": "PTC 2e p.137"
}

ALEMBIC_GHOST_IN_THE_MACHINE = {
    "name": "Ghost in the Machine",
    "transmutation": "Electrification",
    "distillation": "Machinus",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Manipulation + Crafts or Computer + Azoth",
    "action": "Instant",
    "description": "Exert fine operation over electronics at a distance.",
    "book": "PTC 2e p.137"
}

# Arc Distillation
ALEMBIC_ARC = {
    "name": "Arc",
    "transmutation": "Electrification",
    "distillation": "Arc",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Generate a weak electric burn by touch.",
    "book": "PTC 2e p.138"
}

ALEMBIC_SPARK = {
    "name": "Spark",
    "transmutation": "Electrification",
    "distillation": "Arc",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Dexterity + Athletics + Azoth",
    "action": "Instant",
    "description": "Throw a bolt of lightning, which ignores an amount of Armor and has a weapon rating proportional to Pyros charged.",
    "book": "PTC 2e p.138"
}

ALEMBIC_SHOCK = {
    "name": "Shock",
    "transmutation": "Electrification",
    "distillation": "Arc",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Target multiple opponents around you with Spark.",
    "book": "PTC 2e p.138"
}

ALEMBIC_DIVINE_LIGHTNING = {
    "name": "Divine Lightning",
    "transmutation": "Electrification",
    "distillation": "Arc",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Extra damage lingers per turn from Spark. You may spend Pyros to throw a Spark with an aggravated weapon rating.",
    "book": "PTC 2e p.138"
}

# Oscillitus Distillation
ALEMBIC_OSCILLITUS = {
    "name": "Oscillitus",
    "transmutation": "Electrification",
    "distillation": "Oscillitus",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Short small electrical devices at will, and gain 2 Armor or +2 to contest dangerous electrical effects.",
    "book": "PTC 2e p.139"
}

ALEMBIC_INSULATION = {
    "name": "Insulation",
    "transmutation": "Electrification",
    "distillation": "Oscillitus",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Intelligence + Science + Azoth vs Resolve",
    "action": "Instant",
    "description": "Strip the benefits of electric charge from a target.",
    "book": "PTC 2e p.139"
}

ALEMBIC_BLACKOUT = {
    "name": "Blackout",
    "transmutation": "Electrification",
    "distillation": "Oscillitus",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Science + Azoth vs Stamina",
    "action": "Instant",
    "description": "Produce a disruptive pulse that inhibits sight and blows out artificial lights.",
    "book": "PTC 2e p.139"
}

ALEMBIC_AZOTHIC_DETONATION = {
    "name": "Azothic Detonation",
    "transmutation": "Electrification",
    "distillation": "Oscillitus",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Manipulation + Science + Azoth vs Stamina",
    "action": "Instant",
    "description": "Discharge a destructive electromagnetic pulse, frying electronics and injuring people within the radius.",
    "book": "PTC 2e p.139"
}

# Imperatus Distillation
ALEMBIC_IMPERATUS = {
    "name": "Imperatus",
    "transmutation": "Electrification",
    "distillation": "Imperatus",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Maintain a static electric charge that halves healing times.",
    "book": "PTC 2e p.140"
}

ALEMBIC_LIGHTNING_THERAPY = {
    "name": "Lightning Therapy",
    "transmutation": "Electrification",
    "distillation": "Imperatus",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Heal Prometheans or Pandorans by spending Pyros.",
    "book": "PTC 2e p.140"
}

ALEMBIC_REMOTE_ABSORPTION = {
    "name": "Remote Absorption",
    "transmutation": "Electrification",
    "distillation": "Imperatus",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Electrocute yourself at a distance from a source of power, as if the source were dampened.",
    "book": "PTC 2e p.140"
}

ALEMBIC_POWER_SINK = {
    "name": "Power Sink",
    "transmutation": "Electrification",
    "distillation": "Imperatus",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Stamina + Survival + Azoth",
    "action": "Reflexive",
    "description": "Derive Willpower and temporary Health from electrocution.",
    "book": "PTC 2e p.140"
}

# ==================== FLUX ====================

# Blight Distillation
ALEMBIC_BLIGHT = {
    "name": "Blight",
    "transmutation": "Flux",
    "distillation": "Blight",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Immunity to extreme environments conjured by Wastelands or Firestorms.",
    "book": "PTC 2e p.252"
}

ALEMBIC_INVOKE_DISQUIET = {
    "name": "Invoke Disquiet",
    "transmutation": "Flux",
    "distillation": "Blight",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Manipulation + Empathy + Azoth vs Resolve",
    "action": "Instant",
    "description": "Inflict Disquiet focused on a chosen Promethean.",
    "book": "PTC 2e p.252"
}

ALEMBIC_AGGRAVATE_WASTELAND = {
    "name": "Aggravate Wasteland",
    "transmutation": "Flux",
    "distillation": "Blight",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Occult + Azoth",
    "action": "Instant",
    "description": "Fester a Wasteland.",
    "book": "PTC 2e p.252"
}

ALEMBIC_SUMMON_FIRESTORM = {
    "name": "Summon Firestorm",
    "transmutation": "Flux",
    "distillation": "Blight",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Resolve + Occult + Azoth",
    "action": "Instant",
    "description": "Conjure a Firestorm.",
    "book": "PTC 2e p.252"
}

# Cannibalize Distillation
ALEMBIC_CANNIBALIZE = {
    "name": "Cannibalize",
    "transmutation": "Flux",
    "distillation": "Cannibalize",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Your bite attacks inflict +1 damage.",
    "book": "NH-TT p.44"
}

ALEMBIC_APTITUDE = {
    "name": "Aptitude",
    "transmutation": "Flux",
    "distillation": "Cannibalize",
    "rank": 2,
    "charge": "●+",
    "dice_pool": "Resolve + Stamina - Merit",
    "action": "Instant",
    "description": "Consume a victim to manifest a Physical or Mental Merit for (Azoth) hours.",
    "book": "NH-TT p.44"
}

ALEMBIC_ACUMEN = {
    "name": "Acumen",
    "transmutation": "Flux",
    "distillation": "Cannibalize",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Resolve + Stamina + Azoth - Skill",
    "action": "Instant",
    "description": "Consume a victim to manifest a Skill dot for (Azoth) days.",
    "book": "NH-TT p.44"
}

ALEMBIC_ENDOWMENT = {
    "name": "Endowment",
    "transmutation": "Flux",
    "distillation": "Cannibalize",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Resolve + Stamina + Azoth - Attribute",
    "action": "Instant",
    "description": "Consume a victim to manifest an Attribute dot for (Azoth) hours.",
    "book": "NH-TT p.44"
}

# Lordship Distillation
ALEMBIC_LORDSHIP = {
    "name": "Lordship",
    "transmutation": "Flux",
    "distillation": "Lordship",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Pandorans do not aggress you.",
    "book": "PTC 2e p.252"
}

ALEMBIC_LORDSHIP_COMMAND = {
    "name": "Lordship (Command)",
    "transmutation": "Flux",
    "distillation": "Lordship",
    "rank": 2,
    "charge": "●+",
    "dice_pool": "Presence + Animal Ken + Azoth vs Resolve",
    "action": "Instant",
    "description": "Command Pandorans for a scene. Feed them to maintain control, at the cost of Pyros and lethal damage every 24 hours.",
    "book": "PTC 2e p.252"
}

# Mutation Distillation
ALEMBIC_MUTATION = {
    "name": "Mutation",
    "transmutation": "Flux",
    "distillation": "Mutation",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Calcify Dread Powers as a step backwards.",
    "book": "PTC 2e p.253"
}

ALEMBIC_DREAD_POWER = {
    "name": "Dread Power",
    "transmutation": "Flux",
    "distillation": "Mutation",
    "rank": 2,
    "charge": "●+",
    "dice_pool": "Resolve + Stamina + Azoth - Dread Power",
    "action": "Instant",
    "description": "Manifest a Dread Power.",
    "book": "PTC 2e p.253"
}

# Solvent Distillation
ALEMBIC_SOLVENT = {
    "name": "Solvent",
    "transmutation": "Flux",
    "distillation": "Solvent",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Sense Alembic charges.",
    "book": "PTC 2e p.253"
}

ALEMBIC_DISRUPTION = {
    "name": "Disruption",
    "transmutation": "Flux",
    "distillation": "Solvent",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Resolve + Occult + Azoth - Resolve + Azoth",
    "action": "Instant",
    "description": "Disrupt the charge of an Alembic.",
    "book": "PTC 2e p.253"
}

ALEMBIC_DISASTER = {
    "name": "Disaster",
    "transmutation": "Flux",
    "distillation": "Solvent",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Wits + Occult + Azoth vs Wits + Azoth",
    "action": "Reflexive",
    "description": "Block the use of a Distillation.",
    "book": "PTC 2e p.253"
}

ALEMBIC_DETONATION = {
    "name": "Detonation",
    "transmutation": "Flux",
    "distillation": "Solvent",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Intelligence + Occult + Azoth vs Stamina + Azoth",
    "action": "Instant",
    "description": "Discharge an Alembic, dealing proportional lethal damage.",
    "book": "PTC 2e p.253"
}

# Unleash Distillation
ALEMBIC_UNLEASH = {
    "name": "Unleash",
    "transmutation": "Flux",
    "distillation": "Unleash",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Transhuman Potential lasts for a scene, but you may not Dampen the Fire.",
    "book": "NH-TT p.45"
}

ALEMBIC_INVIGORATE = {
    "name": "Invigorate",
    "transmutation": "Flux",
    "distillation": "Unleash",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Resolve + Stamina + Azoth",
    "action": "Instant",
    "description": "Ignore wound penalties.",
    "book": "NH-TT p.45"
}

ALEMBIC_INFUSE = {
    "name": "Infuse",
    "transmutation": "Flux",
    "distillation": "Unleash",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Brawl attacks apply Azoth as a weapon rating and strip Willpower.",
    "book": "NH-TT p.45"
}

ALEMBIC_AZOTHIC_MANTLE = {
    "name": "Azothic Mantle",
    "transmutation": "Flux",
    "distillation": "Unleash",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Resolve + Occult + Azoth",
    "action": "Instant",
    "description": "Project Pyretic fire for (Azoth) feet for an action, inflicting lethal damage and action penalties, and stripping Pyros. Spend Pyros to extend duration.",
    "book": "NH-TT p.45"
}

# ==================== LUCIFERUS ====================

# Solar Flare Distillation
ALEMBIC_SOLAR_FLARE = {
    "name": "Solar Flare",
    "transmutation": "Luciferus",
    "distillation": "Solar Flare",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Glow at will.",
    "book": "PTC 2e p.141"
}

ALEMBIC_DAZZLING_CORONA = {
    "name": "Dazzling Corona",
    "transmutation": "Luciferus",
    "distillation": "Solar Flare",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Presence + Intimidation + Azoth",
    "action": "Instant",
    "description": "Temporarily blind those who oppose you physically.",
    "book": "PTC 2e p.141"
}

ALEMBIC_SEARING_CORONA = {
    "name": "Searing Corona",
    "transmutation": "Luciferus",
    "distillation": "Solar Flare",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Rapidly call up the Extreme Heat Tilt, to which you are immune.",
    "book": "PTC 2e p.141"
}

ALEMBIC_VOLATILE_CORONA = {
    "name": "Volatile Corona",
    "transmutation": "Luciferus",
    "distillation": "Solar Flare",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Others around you must roll Stamina + Athletics each turn to avoid damaging flares.",
    "book": "PTC 2e p.141"
}

# Morning Star Distillation
ALEMBIC_MORNING_STAR = {
    "name": "Morning Star",
    "transmutation": "Luciferus",
    "distillation": "Morning Star",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Once a scene, regain Willpower by inspiring others to impulsive action.",
    "book": "PTC 2e p.141"
}

ALEMBIC_IGNUS_FATUUS = {
    "name": "Ignis Fatuus",
    "transmutation": "Luciferus",
    "distillation": "Morning Star",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Presence + Persuasion + Azoth vs Composure + Tolerance",
    "action": "Reflexive",
    "description": "Project a fascinating aura, issuing good impressions and +2 to social rolls.",
    "book": "PTC 2e p.141"
}

ALEMBIC_BECKON = {
    "name": "Beckon",
    "transmutation": "Luciferus",
    "distillation": "Morning Star",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Empathy + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Compel a subject to follow you until they catch you, after which they are Disquieted.",
    "book": "PTC 2e p.141"
}

ALEMBIC_RINGLEADER = {
    "name": "Ringleader",
    "transmutation": "Luciferus",
    "distillation": "Morning Star",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Socialize + Azoth",
    "action": "Extended",
    "description": "Sway the behavior of a crowd.",
    "book": "PTC 2e p.141"
}

# Blaze of Glory Distillation
ALEMBIC_BLAZE_OF_GLORY = {
    "name": "Blaze of Glory",
    "transmutation": "Luciferus",
    "distillation": "Blaze of Glory",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Gain Willpower when you empty your supply of Pyros.",
    "book": "PTC 2e p.142"
}

ALEMBIC_OUTSHINING_THE_SUN = {
    "name": "Outshining the Sun",
    "transmutation": "Luciferus",
    "distillation": "Blaze of Glory",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Resolve + Expression + Azoth",
    "action": "Instant",
    "description": "Temporarily stoke the efficacy and Tolerance of your Azoth.",
    "book": "PTC 2e p.142"
}

ALEMBIC_ROMAN_CANDLE = {
    "name": "Roman Candle",
    "transmutation": "Luciferus",
    "distillation": "Blaze of Glory",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "+3 to your next contesting roll. Spend Pyros to restock this bonus by +2 dice.",
    "book": "PTC 2e p.142"
}

ALEMBIC_ALL_OR_NOTHING = {
    "name": "All or Nothing",
    "transmutation": "Luciferus",
    "distillation": "Blaze of Glory",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Ignore limitations on Pyros spent per turn.",
    "book": "PTC 2e p.142"
}

# Beacon of Helios Distillation
ALEMBIC_BEACON_OF_HELIOS = {
    "name": "Beacon of Helios",
    "transmutation": "Luciferus",
    "distillation": "Beacon of Helios",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Your presence grants +1 to withstand breaking points and steps backward to those around you.",
    "book": "PTC 2e p.143"
}

ALEMBIC_DAYBREAK = {
    "name": "Daybreak",
    "transmutation": "Luciferus",
    "distillation": "Beacon of Helios",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "When social maneuvering, draw on a character's Virtue or Elpis as per drawing on their Vice.",
    "book": "PTC 2e p.143"
}

ALEMBIC_GUIDEPOST = {
    "name": "Guidepost",
    "transmutation": "Luciferus",
    "distillation": "Beacon of Helios",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Persuasion + Azoth - Resolve",
    "action": "Reflexive",
    "description": "Benefit from a greater impression. Your next few leadership rolls gain the rote quality.",
    "book": "PTC 2e p.143"
}

ALEMBIC_LIGHTHOUSE_FOR_THE_DEAD = {
    "name": "Lighthouse for the Dead",
    "transmutation": "Luciferus",
    "distillation": "Beacon of Helios",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Stamina + Occult + Azoth",
    "action": "Instant",
    "description": "Evoke a vision of hope that pulls a dying Promethean back from the brink of death.",
    "book": "PTC 2e p.143"
}

# ==================== METAMORPHOSIS ====================

# Aptare Distillation
ALEMBIC_APTARE = {
    "name": "Aptare",
    "transmutation": "Metamorphosis",
    "distillation": "Aptare",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Ignore one Environmental Tilt per scene.",
    "book": "PTC 2e p.144"
}

ALEMBIC_BLESSING_OF_TETHYS = {
    "name": "Blessing of Tethys",
    "transmutation": "Metamorphosis",
    "distillation": "Aptare",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Breathe water.",
    "book": "PTC 2e p.144"
}

ALEMBIC_SCUTTLING_SPIDER = {
    "name": "Scuttling Spider",
    "transmutation": "Metamorphosis",
    "distillation": "Aptare",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Adhesive fibers allow you to scale surfaces at full Speed without climbing rolls, or even walk across ceilings.",
    "book": "PTC 2e p.144"
}

ALEMBIC_PROCRUSTEAN_SHAPE = {
    "name": "Procrustean Shape",
    "transmutation": "Metamorphosis",
    "distillation": "Aptare",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Resolve + Medicine + Azoth",
    "action": "Instant",
    "description": "Alter the body's shape so as to extend limbs, contort into small spaces, or otherwise adapt through distortion.",
    "book": "PTC 2e p.144"
}

# Bestiae Facies Distillation
ALEMBIC_BESTIAE_FACIES = {
    "name": "Bestiae Facies",
    "transmutation": "Metamorphosis",
    "distillation": "Bestiae Facies",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Use the higher of Wits or Dexterity to calculate Defense.",
    "book": "PTC 2e p.145"
}

ALEMBIC_NATURAL_WEAPONRY = {
    "name": "Natural Weaponry",
    "transmutation": "Metamorphosis",
    "distillation": "Bestiae Facies",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Grow claws or fangs with a 1L weapon rating.",
    "book": "PTC 2e p.145"
}

ALEMBIC_FORM_OF_THE_BARGHEST = {
    "name": "Form of the Barghest",
    "transmutation": "Metamorphosis",
    "distillation": "Bestiae Facies",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Adopt a large, only vaguely canid quadripedal form, with greater Size, Speed, and Strength.",
    "book": "PTC 2e p.145"
}

ALEMBIC_CHIMERA = {
    "name": "Chimera",
    "transmutation": "Metamorphosis",
    "distillation": "Bestiae Facies",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Stamina + Animal Ken + Azoth",
    "action": "Instant",
    "description": "Take the shape of an animal which you have previously touched.",
    "book": "PTC 2e p.145"
}

# Tegere Distillation
ALEMBIC_TEGERE = {
    "name": "Tegere",
    "transmutation": "Metamorphosis",
    "distillation": "Tegere",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "Instant",
    "description": "Transform the skin as an instant action, providing 2 General Armor against bashing damage.",
    "book": "PTC 2e p.146"
}

ALEMBIC_IMPERMEABLE_SHELL = {
    "name": "Impermeable Shell",
    "transmutation": "Metamorphosis",
    "distillation": "Tegere",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Stamina + Survival + Azoth",
    "action": "Reflexive",
    "description": "Temporarily harden the flesh, taking -1 Defense but gaining 2/4 Armor.",
    "book": "PTC 2e p.146"
}

ALEMBIC_RETRIBUTIVE_PROTECTION = {
    "name": "Retributive Protection",
    "transmutation": "Metamorphosis",
    "distillation": "Tegere",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Stamina + Weaponry + Azoth",
    "action": "Reflexive",
    "description": "Flesh temporarily becomes jagged or abrasive, dealing lethal damage to an attacker's body or weapon.",
    "book": "PTC 2e p.146"
}

ALEMBIC_QUILL_ASSAULT = {
    "name": "Quill Assault",
    "transmutation": "Metamorphosis",
    "distillation": "Tegere",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Carapace evolves into 4/4 Armor, which suffers from -2 Defense and Speed. Take lethal damage to propel fragments as a 1L thrown weapon.",
    "book": "PTC 2e p.146"
}

# Verto Distillation
ALEMBIC_VERTO = {
    "name": "Verto",
    "transmutation": "Metamorphosis",
    "distillation": "Verto",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Shapeshift minor bodily details, such as eye color or hair length.",
    "book": "PTC 2e p.146"
}

ALEMBIC_MEDUSAS_VISAGE = {
    "name": "Medusa's Visage",
    "transmutation": "Metamorphosis",
    "distillation": "Verto",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Stamina + Intimidation + Azoth",
    "action": "Instant",
    "description": "Contort your expression hatefully, granting an Intimidation bonus.",
    "book": "PTC 2e p.146"
}

ALEMBIC_EVERYMAN = {
    "name": "Everyman",
    "transmutation": "Metamorphosis",
    "distillation": "Verto",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Subterfuge + Azoth",
    "action": "Instant",
    "description": "Lose all identifying features, becoming plain and faceless.",
    "book": "PTC 2e p.146"
}

ALEMBIC_BODY_LIKE_CLAY = {
    "name": "Body Like Clay",
    "transmutation": "Metamorphosis",
    "distillation": "Verto",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Dexterity + Medicine + Azoth",
    "action": "Instant",
    "description": "Briefly take any shape within the natural human form. You may roll to extend the change without spending Pyros.",
    "book": "PTC 2e p.146"
}

# ==================== MESMERISM ====================

# Phobos Distillation
ALEMBIC_PHOBOS = {
    "name": "Phobos",
    "transmutation": "Mesmerism",
    "distillation": "Phobos",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Roll exceptional successes with Intimidation at a threshold of three.",
    "book": "PTC 2e p.147"
}

ALEMBIC_RATTLE = {
    "name": "Rattle",
    "transmutation": "Mesmerism",
    "distillation": "Phobos",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Presence + Intimidation + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Unnerve the subject, counting as Hard Leverage and motivating the subject to expedite and end your interaction.",
    "book": "PTC 2e p.147"
}

ALEMBIC_TERRIFY = {
    "name": "Terrify",
    "transmutation": "Mesmerism",
    "distillation": "Phobos",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Intimidation + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Frighten the subject enough to drive them to retreat and escape.",
    "book": "PTC 2e p.147"
}

ALEMBIC_SWOON = {
    "name": "Swoon",
    "transmutation": "Mesmerism",
    "distillation": "Phobos",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Intimidation + Azoth - Stamina",
    "action": "Instant",
    "description": "A fear attack inflicts bashing damage, a breaking point, and fainting.",
    "book": "PTC 2e p.147"
}

# Eros Distillation
ALEMBIC_EROS = {
    "name": "Eros",
    "transmutation": "Mesmerism",
    "distillation": "Eros",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Roll exceptional successes with Persuasion at a threshold of three.",
    "book": "PTC 2e p.148"
}

ALEMBIC_LURE = {
    "name": "Lure",
    "transmutation": "Mesmerism",
    "distillation": "Eros",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Manipulation + Persuasion + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Evoke an excellent impression from a subject, granting +2 to social rolls and inclining them to aid and please you.",
    "book": "PTC 2e p.148"
}

ALEMBIC_SEDUCE = {
    "name": "Seduce",
    "transmutation": "Mesmerism",
    "distillation": "Eros",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Persuasion + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Overwhelms the subject long enough to make them obey one request.",
    "book": "PTC 2e p.148"
}

ALEMBIC_INFLAME = {
    "name": "Inflame",
    "transmutation": "Mesmerism",
    "distillation": "Eros",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Intimidation + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Obsesses the subject with aiding the Promethean for a scene, leaving them Disquieted afterward.",
    "book": "PTC 2e p.148"
}

# Eris Distillation
ALEMBIC_ERIS = {
    "name": "Eris",
    "transmutation": "Mesmerism",
    "distillation": "Eris",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Roll exceptional successes with Subterfuge at a threshold of three.",
    "book": "PTC 2e p.149"
}

ALEMBIC_MISDIRECT = {
    "name": "Misdirect",
    "transmutation": "Mesmerism",
    "distillation": "Eris",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Manipulation + Subterfuge + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Distract and addle a subject, causing a -3 mental penalty.",
    "book": "PTC 2e p.149"
}

ALEMBIC_BAFFLE = {
    "name": "Baffle",
    "transmutation": "Mesmerism",
    "distillation": "Eris",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Resolve + Subterfuge + Azoth - Resolve",
    "action": "Instant",
    "description": "Glaze and stun the target briefly.",
    "book": "PTC 2e p.149"
}

ALEMBIC_FOG = {
    "name": "Fog",
    "transmutation": "Mesmerism",
    "distillation": "Eris",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Subterfuge + Azoth - Resolve",
    "action": "Instant",
    "description": "Causes a temporary catatonic seizure, after which it takes a matter of days to recall what happened during the scene, inflicting Disquiet and a breaking point.",
    "book": "PTC 2e p.149"
}

# Penthos Distillation
ALEMBIC_PENTHOS = {
    "name": "Penthos",
    "transmutation": "Mesmerism",
    "distillation": "Penthos",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Roll exceptional successes with Empathy at a threshold of three.",
    "book": "PTC 2e p.150"
}

ALEMBIC_UNDERMINE = {
    "name": "Undermine",
    "transmutation": "Mesmerism",
    "distillation": "Penthos",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Manipulation + Empathy + Azoth vs Resolve + Tolerance",
    "action": "Reflexive",
    "description": "Discourages the subject, disrupting their use of Willpower.",
    "book": "PTC 2e p.150"
}

ALEMBIC_DEFEAT = {
    "name": "Defeat",
    "transmutation": "Mesmerism",
    "distillation": "Penthos",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Empathy + Azoth vs Resolve + Tolerance",
    "action": "Reflexive",
    "description": "Leaves the subject Beaten Down.",
    "book": "PTC 2e p.150"
}

ALEMBIC_DEPRESS = {
    "name": "Depress",
    "transmutation": "Mesmerism",
    "distillation": "Penthos",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Manipulation + Empathy + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Shatters the subject, leaving them temporarily Broken and unable to act without mustering Willpower.",
    "book": "PTC 2e p.150"
}

# ==================== SATURNINUS ====================

# Heed the Call Distillation
ALEMBIC_HEED_THE_CALL = {
    "name": "Heed the Call",
    "transmutation": "Saturninus",
    "distillation": "Heed the Call",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Sense Azothic radiance as if it were one dot stronger, and judge the direction and distance to its source.",
    "book": "PTC 2e p.150"
}

ALEMBIC_INSCRIBED_IN_FLAME = {
    "name": "Inscribed in Flame",
    "transmutation": "Saturninus",
    "distillation": "Heed the Call",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Wits + Empathy + Azoth",
    "action": "Instant",
    "description": "Sense the Azothic radiance of pilgrim's marks and of Torment. Analyze the Measure for details about Azothic traits.",
    "book": "PTC 2e p.150"
}

ALEMBIC_CONTROLLED_BURN = {
    "name": "Controlled Burn",
    "transmutation": "Saturninus",
    "distillation": "Heed the Call",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Composure + Expression + Azoth",
    "action": "Instant",
    "description": "Alter the strength of your Azothic radiance. Appear human to supernatural senses if you dampen it to nothing.",
    "book": "PTC 2e p.150"
}

ALEMBIC_SUBLIMATION_BY_FIRE = {
    "name": "Sublimation by Fire",
    "transmutation": "Saturninus",
    "distillation": "Heed the Call",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Manipulation + Expression + Azoth vs Resolve + Azoth",
    "action": "Extended",
    "description": "Salve another Promethean's Torment.",
    "book": "PTC 2e p.150"
}

# Plumb the Fathoms Distillation
ALEMBIC_PLUMB_THE_FATHOMS = {
    "name": "Plumb the Fathoms",
    "transmutation": "Saturninus",
    "distillation": "Plumb the Fathoms",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Retain detailed memory of a Ramble long enough to record it. +1 to resist or Tolerate mental influence powers.",
    "book": "PTC 2e p.152"
}

ALEMBIC_PILGRIMS_LANDMARKS = {
    "name": "Pilgrim's Landmarks",
    "transmutation": "Saturninus",
    "distillation": "Plumb the Fathoms",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Intelligence + Occult + Azoth",
    "action": "Instant",
    "description": "Consult the Azothic memory about experiences in a place.",
    "book": "PTC 2e p.152"
}

ALEMBIC_WISDOM_OF_AGES = {
    "name": "Wisdom of Ages",
    "transmutation": "Saturninus",
    "distillation": "Plumb the Fathoms",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Intelligence + Occult + Azoth",
    "action": "Reflexive",
    "description": "Gain the rote quality on certain Skills by experiencing flashes of shared memories.",
    "book": "PTC 2e p.152"
}

ALEMBIC_GLIMPSING_THE_CRASIS = {
    "name": "Glimpsing the Crasis",
    "transmutation": "Saturninus",
    "distillation": "Plumb the Fathoms",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Secrete your ruling humour from a wound. When consumed, it evokes visions that draw prophetic truth out of your personal experiences.",
    "book": "PTC 2e p.152"
}

# Stoke the Furnace Distillation
ALEMBIC_STOKE_THE_FURNACE = {
    "name": "Stoke the Furnace",
    "transmutation": "Saturninus",
    "distillation": "Stoke the Furnace",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Transhuman Potential lasts another turn.",
    "book": "PTC 2e p.153"
}

ALEMBIC_CATALYTIC_AFFIRMATION = {
    "name": "Catalytic Affirmation",
    "transmutation": "Saturninus",
    "distillation": "Stoke the Furnace",
    "rank": 2,
    "charge": "--",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "When awarded a beat through your efforts in your current Role, boost an Attribute by one for a session.",
    "book": "PTC 2e p.153"
}

ALEMBIC_CHASING_HOPE = {
    "name": "Chasing Hope",
    "transmutation": "Saturninus",
    "distillation": "Stoke the Furnace",
    "rank": 3,
    "charge": "--",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Recover Pyros as well as Willpower from your Elpis Anchor.",
    "book": "PTC 2e p.153"
}

ALEMBIC_TRANSHUMAN_ADAPTATION = {
    "name": "Transhuman Adaptation",
    "transmutation": "Saturninus",
    "distillation": "Stoke the Furnace",
    "rank": 4,
    "charge": "--",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Spend Pyros to manifest a Merit for a scene through alchemical catalysis.",
    "book": "PTC 2e p.153"
}

# Prime the Vessel Distillation
ALEMBIC_PRIME_THE_VESSEL = {
    "name": "Prime the Vessel",
    "transmutation": "Saturninus",
    "distillation": "Prime the Vessel",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Choose a Skill category. Reduce its unskilled penalty by one.",
    "book": "PTC 2e p.153"
}

ALEMBIC_SHIELDING_POD = {
    "name": "Shielding Pod",
    "transmutation": "Saturninus",
    "distillation": "Prime the Vessel",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Stamina + Occult + Azoth",
    "action": "Instant",
    "description": "Grow a resilient sac to protect stored Vitriol.",
    "book": "PTC 2e p.153"
}

ALEMBIC_HUMOUR_ELECTROLYSIS = {
    "name": "Humour Electrolysis",
    "transmutation": "Saturninus",
    "distillation": "Prime the Vessel",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Your flesh and viscera become poisonous, causing bashing damage when directly ingested, or lethal damage when extracted and concentrated.",
    "book": "PTC 2e p.153"
}

ALEMBIC_PYROS_BRANDING = {
    "name": "Pyros Branding",
    "transmutation": "Saturninus",
    "distillation": "Prime the Vessel",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Occult + Azoth",
    "action": "Instant",
    "description": "Brand a throng.",
    "book": "PTC 2e p.153"
}

# ==================== SENSORIUM ====================

# Vitreous Humour Distillation
ALEMBIC_VITREOUS_HUMOUR = {
    "name": "Vitreous Humour",
    "transmutation": "Sensorium",
    "distillation": "Vitreous Humour",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "See in complete darkness. Immunity to blinding light.",
    "book": "PTC 2e p.154"
}

ALEMBIC_FIRE_SIGHT = {
    "name": "Fire Sight",
    "transmutation": "Sensorium",
    "distillation": "Vitreous Humour",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Overlay thermal vision.",
    "book": "PTC 2e p.154"
}

ALEMBIC_PIERCING_SIGHT = {
    "name": "Piercing Sight",
    "transmutation": "Sensorium",
    "distillation": "Vitreous Humour",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Wits + Composure + Azoth",
    "action": "Instant",
    "description": "See through opaque matter.",
    "book": "PTC 2e p.154"
}

ALEMBIC_EPHEMERAL_SIGHT = {
    "name": "Ephemeral Sight",
    "transmutation": "Sensorium",
    "distillation": "Vitreous Humour",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Wits + Composure + Azoth",
    "action": "Instant",
    "description": "Perceive Twilit ephemera and incorporeal qashmallim.",
    "book": "PTC 2e p.154"
}

# Receptive Humour Distillation
ALEMBIC_RECEPTIVE_HUMOUR = {
    "name": "Receptive Humour",
    "transmutation": "Sensorium",
    "distillation": "Receptive Humour",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Add Azoth as bonus dice to perception rolls.",
    "book": "PTC 2e p.155"
}

ALEMBIC_TRANSLATORS_MEMORY = {
    "name": "Translator's Memory",
    "transmutation": "Sensorium",
    "distillation": "Receptive Humour",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Intelligence + Academics + Azoth",
    "action": "Extended",
    "description": "Draw on Azothic memory to interpret written messages.",
    "book": "PTC 2e p.155"
}

ALEMBIC_RARIFIED_SENSES = {
    "name": "Rarified Senses",
    "transmutation": "Sensorium",
    "distillation": "Receptive Humour",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Perception rolls take the rote quality.",
    "book": "PTC 2e p.155"
}

ALEMBIC_CIRCLE_OF_PERCEPTION = {
    "name": "Circle of Perception",
    "transmutation": "Sensorium",
    "distillation": "Receptive Humour",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Wits + Composure + Azoth",
    "action": "Reflexive",
    "description": "Senses apply in every direction. +2 Defense, which may be applied against surprise attacks.",
    "book": "PTC 2e p.155"
}

# Stereo Humour Distillation
ALEMBIC_STEREO_HUMOUR = {
    "name": "Stereo Humour",
    "transmutation": "Sensorium",
    "distillation": "Stereo Humour",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "+2 to read a person's feelings or motivations.",
    "book": "PTC 2e p.156"
}

ALEMBIC_AURA_SIGHT = {
    "name": "Aura Sight",
    "transmutation": "Sensorium",
    "distillation": "Stereo Humour",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Wits + Empathy + Azoth - Composure",
    "action": "Instant",
    "description": "Interpret details of a character's psychic aura.",
    "book": "PTC 2e p.156"
}

ALEMBIC_HEARING_THE_INNER_VOICE = {
    "name": "Hearing the Inner Voice",
    "transmutation": "Sensorium",
    "distillation": "Stereo Humour",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Wits + Composure + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Listen in on a subject's thought process.",
    "book": "PTC 2e p.156"
}

ALEMBIC_CLAIRVOYANCE = {
    "name": "Clairvoyance",
    "transmutation": "Sensorium",
    "distillation": "Stereo Humour",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Wits + Investigation + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Use a sample of a subject to perceive them from afar.",
    "book": "PTC 2e p.156"
}

# Somatic Humour Distillation
ALEMBIC_SOMATIC_HUMOUR = {
    "name": "Somatic Humour",
    "transmutation": "Sensorium",
    "distillation": "Somatic Humour",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Roll exceptional successes with Survival on a threshold of three.",
    "book": "PTC 2e p.157"
}

ALEMBIC_BLOODHOUNDS_NOSE = {
    "name": "Bloodhound's Nose",
    "transmutation": "Sensorium",
    "distillation": "Somatic Humour",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Enhanced sense of smell, which may be used to track subjects at +2.",
    "book": "PTC 2e p.157"
}

ALEMBIC_DISCRIMINATING_TONGUE = {
    "name": "Discriminating Tongue",
    "transmutation": "Sensorium",
    "distillation": "Somatic Humour",
    "rank": 3,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Make Intelligence rolls to quickly identify chemical natures by taste.",
    "book": "PTC 2e p.157"
}

ALEMBIC_SENSITIVE_EARS = {
    "name": "Sensitive Ears",
    "transmutation": "Sensorium",
    "distillation": "Somatic Humour",
    "rank": 4,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Extend beyond the human range of hearing. Roll Wits + Survival to narrow the focus of hearing. May blindfight by hearing.",
    "book": "PTC 2e p.157"
}

# ==================== SPIRITUS ====================

# Clades Distillation
ALEMBIC_CLADES = {
    "name": "Clades",
    "transmutation": "Spiritus",
    "distillation": "Clades",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "Instant",
    "description": "Focus Clades on a type of supernatural being as an instant action. +2 Defense against those beings.",
    "book": "PTC 2e p.158"
}

ALEMBIC_STRIKE_THE_HEART = {
    "name": "Strike the Heart",
    "transmutation": "Spiritus",
    "distillation": "Clades",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Focus on one opponent of the chosen type. Briefly reduce called shot penalties against them by two.",
    "book": "PTC 2e p.158"
}

ALEMBIC_BITING_AURA = {
    "name": "Biting Aura",
    "transmutation": "Spiritus",
    "distillation": "Clades",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Azoth",
    "action": "Instant",
    "description": "Your Azothic radiance deals lethal damage to beings of the chosen type.",
    "book": "PTC 2e p.158"
}

ALEMBIC_BURNING_STRIKE = {
    "name": "Burning Strike",
    "transmutation": "Spiritus",
    "distillation": "Clades",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Azoth",
    "action": "Reflexive",
    "description": "Briefly deal aggravated damage unarmed against beings of the chosen type.",
    "book": "PTC 2e p.158"
}

# Clupeum Distillation
ALEMBIC_CLUPEUM = {
    "name": "Clupeum",
    "transmutation": "Spiritus",
    "distillation": "Clupeum",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "-2 to sense the Promethean with supernatural powers.",
    "book": "PTC 2e p.158"
}

ALEMBIC_PERSONAL_SHIELD = {
    "name": "Personal Shield",
    "transmutation": "Spiritus",
    "distillation": "Clupeum",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Apply twice your Azoth as Supernatural Tolerance.",
    "book": "PTC 2e p.158"
}

ALEMBIC_INTERPOSING_SHIELD = {
    "name": "Interposing Shield",
    "transmutation": "Spiritus",
    "distillation": "Clupeum",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Stamina + Survival + Azoth",
    "action": "Reflexive",
    "description": "Grant beneficiaries your Azoth as a bonus to contest, and half Azoth as a bonus to resist.",
    "book": "PTC 2e p.158"
}

ALEMBIC_MYSTIC_FORTRESS = {
    "name": "Mystic Fortress",
    "transmutation": "Spiritus",
    "distillation": "Clupeum",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Intelligence + Occult + Azoth",
    "action": "Instant",
    "description": "Extend a ward which resists hostile supernatural powers, and grants a bonus to your allies to unveil illusions and the hidden.",
    "book": "PTC 2e p.158"
}

# Veritas Distillation
ALEMBIC_VERITAS = {
    "name": "Veritas",
    "transmutation": "Spiritus",
    "distillation": "Veritas",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Sense the use of supernatural powers nearby.",
    "book": "PTC 2e p.160"
}

ALEMBIC_FINDING_THE_WELLSPRING = {
    "name": "Finding the Wellspring",
    "transmutation": "Spiritus",
    "distillation": "Veritas",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Wits + Occult + Azoth vs Composure + Tolerance",
    "action": "Instant",
    "description": "Assess the origin of a supernatural effect.",
    "book": "PTC 2e p.160"
}

ALEMBIC_WALKING_THE_PATH_OF_MEMORY = {
    "name": "Walking the Path of Memory",
    "transmutation": "Spiritus",
    "distillation": "Veritas",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Wits + Manipulation + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Touch a supernatural being and gain insight by witnessing one of its memories.",
    "book": "PTC 2e p.160"
}

ALEMBIC_DISRUPTING_THE_VITAL_HUMOURS = {
    "name": "Disrupting the Vital Humours",
    "transmutation": "Spiritus",
    "distillation": "Veritas",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Presence + Occult + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Temporarily obstruct targets' use of their corresponding supernatural fuel.",
    "book": "PTC 2e p.160"
}

# Laruae Distillation
ALEMBIC_LARUAE = {
    "name": "Laruae",
    "transmutation": "Spiritus",
    "distillation": "Laruae",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Focus Laruae on a type of supernatural being. Those beings take -2 to identify you as a Promethean; failure registers you as human.",
    "book": "PTC 2e p.160"
}

ALEMBIC_PLUMB_AZOTHIC_MEMORY = {
    "name": "Plumb Azothic Memory",
    "transmutation": "Spiritus",
    "distillation": "Laruae",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Intelligence + Occult + Azoth",
    "action": "Instant",
    "description": "Glean information about a particular supernatural being or event through the Azothic memory.",
    "book": "PTC 2e p.160"
}

ALEMBIC_ONE_OF_THE_TRIBE = {
    "name": "One of the Tribe",
    "transmutation": "Spiritus",
    "distillation": "Laruae",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Manipulation + Socialize + Azoth",
    "action": "Instant",
    "description": "Azoth grants bonus dice to fit in among the chosen type of being, and resists attempts to discern you as different.",
    "book": "PTC 2e p.160"
}

ALEMBIC_PYROS_DECOY = {
    "name": "Pyros Decoy",
    "transmutation": "Spiritus",
    "distillation": "Laruae",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Intelligence + Crafts",
    "action": "Instant",
    "description": "Destroy a small object to release invisible pyretic energy. Those who perceive it with supernatural senses suffer a penalty to notice you.",
    "book": "PTC 2e p.160"
}

# ==================== VITALITY ====================

# Unbowed Distillation
ALEMBIC_UNBOWED = {
    "name": "Unbowed",
    "transmutation": "Vitality",
    "distillation": "Unbowed",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Increase Resolve by Azoth.",
    "book": "PTC 2e p.161"
}

ALEMBIC_RESOLUTION_OF_STEEL = {
    "name": "Resolution of Steel",
    "transmutation": "Vitality",
    "distillation": "Unbowed",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Sharpen your resolve.",
    "book": "PTC 2e p.161"
}

ALEMBIC_CRUCIBLE_OF_WILL = {
    "name": "Crucible of Will",
    "transmutation": "Vitality",
    "distillation": "Unbowed",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Recover Willpower.",
    "book": "PTC 2e p.161"
}

ALEMBIC_ROAR_OF_THE_DEFIANT = {
    "name": "Roar of the Defiant",
    "transmutation": "Vitality",
    "distillation": "Unbowed",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Resolve + Composure + Azoth",
    "action": "Reflexive",
    "description": "Substitute to contest supernatural mind control.",
    "book": "PTC 2e p.161"
}

# Unbroken Distillation
ALEMBIC_UNBROKEN = {
    "name": "Unbroken",
    "transmutation": "Vitality",
    "distillation": "Unbroken",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Increase Stamina by Azoth.",
    "book": "PTC 2e p.162"
}

ALEMBIC_ARMOR_OF_WILL = {
    "name": "Armor of Will",
    "transmutation": "Vitality",
    "distillation": "Unbroken",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Double the effect of Willpower spent defensively.",
    "book": "PTC 2e p.162"
}

ALEMBIC_DRIVE_ON = {
    "name": "Drive On",
    "transmutation": "Vitality",
    "distillation": "Unbroken",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Stamina + Athletics + Azoth",
    "action": "Reflexive",
    "description": "Temporarily ignore the effects of physical Conditions or Tilts.",
    "book": "PTC 2e p.162"
}

ALEMBIC_REBUKE_THE_SHROUD = {
    "name": "Rebuke the Shroud",
    "transmutation": "Vitality",
    "distillation": "Unbroken",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Survive any amount of damage for one scene, after which if too much damage still remains, you die.",
    "book": "PTC 2e p.162"
}

# Unconquered Distillation
ALEMBIC_UNCONQUERED = {
    "name": "Unconquered",
    "transmutation": "Vitality",
    "distillation": "Unconquered",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Increase Strength by Azoth.",
    "book": "PTC 2e p.163"
}

ALEMBIC_CYCLOPEAN_MIGHT = {
    "name": "Cyclopean Might",
    "transmutation": "Vitality",
    "distillation": "Unconquered",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Reflexive",
    "description": "Deal lethal damage unarmed, and ignore a point of Durability when striking objects.",
    "book": "PTC 2e p.163"
}

ALEMBIC_TITANS_THROW = {
    "name": "Titan's Throw",
    "transmutation": "Vitality",
    "distillation": "Unconquered",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Strength + Athletics + Azoth",
    "action": "Reflexive",
    "description": "Multiply your lifting and hurling Strength.",
    "book": "PTC 2e p.163"
}

ALEMBIC_WRATH_OF_THE_GODS = {
    "name": "Wrath of the Gods",
    "transmutation": "Vitality",
    "distillation": "Unconquered",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Strength + Athletics + Azoth",
    "action": "Instant",
    "description": "Cause the environment itself to quake.",
    "book": "PTC 2e p.163"
}

# Unfettered Distillation
ALEMBIC_UNFETTERED = {
    "name": "Unfettered",
    "transmutation": "Vitality",
    "distillation": "Unfettered",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Add Azoth as a bonus to break free of restraint.",
    "book": "PTC 2e p.163"
}

ALEMBIC_CLOSE_COMBAT_DEFENSE = {
    "name": "Close Combat Defense",
    "transmutation": "Vitality",
    "distillation": "Unfettered",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Strength + Athletics + Azoth",
    "action": "Reflexive",
    "description": "Instantly escape a grapple.",
    "book": "PTC 2e p.163"
}

ALEMBIC_SHATTERED_CHAINS = {
    "name": "Shattered Chains",
    "transmutation": "Vitality",
    "distillation": "Unfettered",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Strength + Crafts + Azoth",
    "action": "Reflexive",
    "description": "Ignore the Durability of restraints when busting free.",
    "book": "PTC 2e p.163"
}

ALEMBIC_NO_WALLS_MAY_HOLD_ME = {
    "name": "No Walls May Hold Me",
    "transmutation": "Vitality",
    "distillation": "Unfettered",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Strength + Crafts + Azoth",
    "action": "Instant",
    "description": "Ignore three points of Durability when striking a cage or imprisoning wall, and take no damage from pounding it down.",
    "book": "PTC 2e p.163"
}

# ==================== VULCANUS ====================

# Cauterio Distillation
ALEMBIC_CAUTERIO = {
    "name": "Cauterio",
    "transmutation": "Vulcanus",
    "distillation": "Cauterio",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Mark an invisible brand by touch, and intuit the direction to it.",
    "book": "PTC 2e p.164"
}

ALEMBIC_ALTER_FIRETOUCHED = {
    "name": "Alter Firetouched",
    "transmutation": "Vulcanus",
    "distillation": "Cauterio",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Temporarily alter physical aspects of a branded target.",
    "book": "PTC 2e p.164"
}

ALEMBIC_ANIMATE_FIRETOUCHED = {
    "name": "Animate Firetouched",
    "transmutation": "Vulcanus",
    "distillation": "Cauterio",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Animate a branded object and puppet its movements for a scene.",
    "book": "PTC 2e p.164"
}

ALEMBIC_EVOLVE_FIRETOUCHED = {
    "name": "Evolve Firetouched",
    "transmutation": "Vulcanus",
    "distillation": "Cauterio",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Imbue an animated object with a simple loyal intelligence of its own.",
    "book": "PTC 2e p.164"
}

# Ignus Aspiratus Distillation
ALEMBIC_IGNUS_ASPIRATUS = {
    "name": "Ignus Aspiratus",
    "transmutation": "Vulcanus",
    "distillation": "Ignus Aspiratus",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Ignite kindling at will.",
    "book": "PTC 2e p.165"
}

ALEMBIC_DIRECT_FIRE = {
    "name": "Direct Fire",
    "transmutation": "Vulcanus",
    "distillation": "Ignus Aspiratus",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Shape a fire, or lash out with it as a 1L weapon.",
    "book": "PTC 2e p.165"
}

ALEMBIC_FIRE_GRASP = {
    "name": "Fire Grasp",
    "transmutation": "Vulcanus",
    "distillation": "Ignus Aspiratus",
    "rank": 3,
    "charge": "**",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Ignite your hand, suffering no injury from its burning, and spread the fire by touch.",
    "book": "PTC 2e p.165"
}

ALEMBIC_DIVINE_GUIDANCE = {
    "name": "Divine Guidance",
    "transmutation": "Vulcanus",
    "distillation": "Ignus Aspiratus",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Stamina + Occult + Azoth",
    "action": "Instant",
    "description": "Stoke the Divine Fire to achieve automatic success on your next few actions.",
    "book": "PTC 2e p.165"
}

# Mutatus Aspiratus Distillation
ALEMBIC_MUTATUS_ASPIRATUS = {
    "name": "Mutatus Aspiratus",
    "transmutation": "Vulcanus",
    "distillation": "Mutatus Aspiratus",
    "rank": 1,
    "charge": "--",
    "dice_pool": "Wits + Azoth",
    "action": "Instant",
    "description": "Roll as an instant action to sense Flux activity.",
    "book": "PTC 2e p.166"
}

ALEMBIC_CONTAIN_FLUX = {
    "name": "Contain Flux",
    "transmutation": "Vulcanus",
    "distillation": "Mutatus Aspiratus",
    "rank": 2,
    "charge": "*",
    "dice_pool": "Presence + Athletics + Azoth",
    "action": "Instant",
    "description": "Gain effective Armor against beings or powers of Flux for a scene.",
    "book": "PTC 2e p.166"
}

ALEMBIC_DRAWING_FLUX = {
    "name": "Drawing Flux",
    "transmutation": "Vulcanus",
    "distillation": "Mutatus Aspiratus",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Presence + Intimidation + Azoth vs Composure + Rank",
    "action": "Instant",
    "description": "Weaken the efficiency of Pyros used by Pandorans or to charge Flux.",
    "book": "PTC 2e p.166"
}

ALEMBIC_EXPEL_PYROS = {
    "name": "Expel Pyros",
    "transmutation": "Vulcanus",
    "distillation": "Mutatus Aspiratus",
    "rank": 4,
    "charge": "***",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Inflict fleeting Dormancy on Pandorans in your presence.",
    "book": "PTC 2e p.166"
}

# Sanctus Aspiratus Distillation
ALEMBIC_SANCTUS_ASPIRATUS = {
    "name": "Sanctus Aspiratus",
    "transmutation": "Vulcanus",
    "distillation": "Sanctus Aspiratus",
    "rank": 1,
    "charge": "--",
    "dice_pool": "Wits + Occult",
    "action": "Instant",
    "description": "Roll as an instant action to sense sources of Pyros.",
    "book": "PTC 2e p.167"
}

ALEMBIC_REFINE_PYROS = {
    "name": "Refine Pyros",
    "transmutation": "Vulcanus",
    "distillation": "Sanctus Aspiratus",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Briefly double the efficacy of spent Pyros.",
    "book": "PTC 2e p.167"
}

ALEMBIC_STEAL_PYROS = {
    "name": "Steal Pyros",
    "transmutation": "Vulcanus",
    "distillation": "Sanctus Aspiratus",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Strength + Occult + Azoth - Resolve",
    "action": "Reflexive",
    "description": "With a touch, steal Pyros from beings who store it, or vampirize living things for Pyros.",
    "book": "PTC 2e p.167"
}

ALEMBIC_DRAIN_PYROS = {
    "name": "Drain Pyros",
    "transmutation": "Vulcanus",
    "distillation": "Sanctus Aspiratus",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Dexterity + Occult + Azoth - Stamina",
    "action": "Instant",
    "description": "Steal Pyros or vampirize for Pyros at a distance, drawing it into yourself or throngmates.",
    "book": "PTC 2e p.167"
}

# The Tsar's Gift Distillation (Zeka-specific)
ALEMBIC_THE_TSARS_GIFT = {
    "name": "The Tsar's Gift",
    "transmutation": "Vulcanus",
    "distillation": "The Tsar's Gift",
    "rank": 1,
    "charge": "--",
    "dice_pool": "--",
    "action": "--",
    "description": "Sense the approach of weaponry. Spend Pyros to reduce damage from an explosion to bashing, or spend two to ignore it entirely.",
    "book": "NH-TT p.146"
}

ALEMBIC_THE_FIRST_STONE = {
    "name": "The First Stone",
    "transmutation": "Vulcanus",
    "distillation": "The Tsar's Gift",
    "rank": 2,
    "charge": "*",
    "dice_pool": "None",
    "action": "Instant",
    "description": "Render guns, explosives and similar inert for the scene.",
    "book": "NH-TT p.146"
}

ALEMBIC_THE_HAND_THAT_FEEDS = {
    "name": "The Hand that Feeds",
    "transmutation": "Vulcanus",
    "distillation": "The Tsar's Gift",
    "rank": 3,
    "charge": "**",
    "dice_pool": "Strength + Weapon Rating + Azoth",
    "action": "Instant",
    "description": "Make something explode.",
    "book": "NH-TT p.146"
}

ALEMBIC_SEVENFOLD = {
    "name": "Sevenfold",
    "transmutation": "Vulcanus",
    "distillation": "The Tsar's Gift",
    "rank": 4,
    "charge": "***",
    "dice_pool": "Stamina + Survival + Azoth vs Resolve + Tolerance",
    "action": "Instant",
    "description": "Target takes damage equal to the damage the Zeka has taken.",
    "book": "NH-TT p.146"
}

# Export all alembics
ALL_ALEMBICS_DETAILED = {
    # Alchemicus - Stone
    "stone": ALEMBIC_STONE,
    "purification": ALEMBIC_PURIFICATION,
    "fortification": ALEMBIC_FORTIFICATION,
    "transformation": ALEMBIC_TRANSFORMATION,
    
    # Alchemicus - Aqua Regia
    "aqua_regia": ALEMBIC_AQUA_REGIA,
    "decay": ALEMBIC_DECAY,
    "degradation": ALEMBIC_DEGRADATION,
    "dissolution": ALEMBIC_DISSOLUTION,
    
    # Alchemicus - Spagyria
    "spagyria": ALEMBIC_SPAGYRIA,
    "temperature_modification": ALEMBIC_TEMPERATURE_MODIFICATION,
    "alteration": ALEMBIC_ALTERATION,
    "resize": ALEMBIC_RESIZE,
    
    # Alchemicus - Elixir
    "elixir": ALEMBIC_ELIXIR,
    "apprentices_brooms": ALEMBIC_APPRENTICES_BROOMS,
    "spark_of_life": ALEMBIC_SPARK_OF_LIFE,
    "flesh_to_stone": ALEMBIC_FLESH_TO_STONE,
    
    # Benefice - Command
    "command": ALEMBIC_COMMAND,
    "many_hands_make_light_work": ALEMBIC_MANY_HANDS_MAKE_LIGHT_WORK,
    "able_worker": ALEMBIC_ABLE_WORKER,
    "the_community_of_power": ALEMBIC_THE_COMMUNITY_OF_POWER,
    
    # Benefice - Consortium
    "consortium": ALEMBIC_CONSORTIUM,
    "the_fortified_compact": ALEMBIC_THE_FORTIFIED_COMPACT,
    "common_perception": ALEMBIC_COMMON_PERCEPTION,
    "unspoken_words": ALEMBIC_UNSPOKEN_WORDS,
    
    # Benefice - Control
    "control": ALEMBIC_CONTROL,
    "protective_boon": ALEMBIC_PROTECTIVE_BOON,
    "inviolable_unity": ALEMBIC_INVIOLABLE_UNITY,
    "bulwark": ALEMBIC_BULWARK,
    
    # Benefice - Community
    "community": ALEMBIC_COMMUNITY,
    "communal_font": ALEMBIC_COMMUNAL_FONT,
    "we_are_as_one": ALEMBIC_WE_ARE_AS_ONE,
    "whats_mine_is_yours": ALEMBIC_WHATS_MINE_IS_YOURS,
    
    # Contamination - Indulgence
    "indulgence": ALEMBIC_INDULGENCE,
    "encourage_impulse": ALEMBIC_ENCOURAGE_IMPULSE,
    "remove_inhibitions": ALEMBIC_REMOVE_INHIBITIONS,
    "plague_of_desire": ALEMBIC_PLAGUE_OF_DESIRE,
    
    # Contamination - Leverage
    "leverage": ALEMBIC_LEVERAGE,
    "confession": ALEMBIC_CONFESSION,
    "guilt_trip": ALEMBIC_GUILT_TRIP,
    "scandal": ALEMBIC_SCANDAL,
    
    # Contamination - Madness
    "madness": ALEMBIC_MADNESS,
    "psychotic_flash": ALEMBIC_PSYCHOTIC_FLASH,
    "onset_of_madness": ALEMBIC_ONSET_OF_MADNESS,
    "catharsis": ALEMBIC_CATHARSIS,
    
    # Contamination - Suffering
    "suffering": ALEMBIC_SUFFERING,
    "purge": ALEMBIC_PURGE,
    "affliction": ALEMBIC_AFFLICTION,
    "pain": ALEMBIC_PAIN,
    
    # Corporeum - Charites
    "charites": ALEMBIC_CHARITES,
    "athletic_grace": ALEMBIC_ATHLETIC_GRACE,
    "uncanny_dexterity": ALEMBIC_UNCANNY_DEXTERITY,
    "rarified_grace": ALEMBIC_RARIFIED_GRACE,
    
    # Corporeum - Zephyrus
    "zephyrus": ALEMBIC_ZEPHYRUS,
    "swift_feet": ALEMBIC_SWIFT_FEET,
    "serpent_strike": ALEMBIC_SERPENT_STRIKE,
    "perfected_reflexes": ALEMBIC_PERFECTED_REFLEXES,
    
    # Corporeum - Hygeius
    "hygeius": ALEMBIC_HYGEIUS,
    "human_flesh": ALEMBIC_HUMAN_FLESH,
    "impossible_flesh": ALEMBIC_IMPOSSIBLE_FLESH,
    "resilient_flesh": ALEMBIC_RESILIENT_FLESH,
    
    # Corporeum - Motus
    "motus": ALEMBIC_MOTUS,
    "uncanny_athleticism": ALEMBIC_UNCANNY_ATHLETICISM,
    "mighty_bound": ALEMBIC_MIGHTY_BOUND,
    "exemplary_athleticism": ALEMBIC_EXEMPLARY_ATHLETICISM,
    
    # Deception - Anonymity
    "anonymity": ALEMBIC_ANONYMITY,
    "nameless": ALEMBIC_NAMELESS,
    "traceless": ALEMBIC_TRACELESS,
    "forgotten": ALEMBIC_FORGOTTEN,
    
    # Deception - Assimilation
    "assimilation": ALEMBIC_ASSIMILATION,
    "conformity": ALEMBIC_CONFORMITY,
    "tongues": ALEMBIC_TONGUES,
    "hive_mind": ALEMBIC_HIVE_MIND,
    
    # Deception - Doppelganger
    "doppelganger": ALEMBIC_DOPPELGANGER,
    "incriminate": ALEMBIC_INCRIMINATE,
    "impersonate": ALEMBIC_IMPERSONATE,
    "deep_cover": ALEMBIC_DEEP_COVER,
    
    # Deception - Stalker
    "stalker": ALEMBIC_STALKER,
    "shadow": ALEMBIC_SHADOW,
    "lurker": ALEMBIC_LURKER,
    "phantom": ALEMBIC_PHANTOM,
    
    # Disquietism - Externalize
    "externalize": ALEMBIC_EXTERNALIZE,
    "safe_sojourn": ALEMBIC_SAFE_SOJOURN,
    "maelstrom": ALEMBIC_MAELSTROM,
    "assault": ALEMBIC_ASSAULT,
    
    # Disquietism - Internalize
    "internalize": ALEMBIC_INTERNALIZE,
    "temper": ALEMBIC_TEMPER,
    "soothe": ALEMBIC_SOOTHE,
    "quell": ALEMBIC_QUELL,
    
    # Disquietism - Redirect
    "redirect": ALEMBIC_REDIRECT,
    "scapegoat": ALEMBIC_SCAPEGOAT,
    "rabid_rage": ALEMBIC_RABID_RAGE,
    "iagos_whisper": ALEMBIC_IAGOS_WHISPER,
    
    # Disquietism - Weaponize
    "weaponize": ALEMBIC_WEAPONIZE,
    "tension": ALEMBIC_TENSION,
    "vanquish": ALEMBIC_VANQUISH,
    "rampage": ALEMBIC_RAMPAGE,
    
    # Electrification - Machinus
    "machinus": ALEMBIC_MACHINUS,
    "jolt": ALEMBIC_JOLT,
    "generator": ALEMBIC_GENERATOR,
    "ghost_in_the_machine": ALEMBIC_GHOST_IN_THE_MACHINE,
    
    # Electrification - Arc
    "arc": ALEMBIC_ARC,
    "spark": ALEMBIC_SPARK,
    "shock": ALEMBIC_SHOCK,
    "divine_lightning": ALEMBIC_DIVINE_LIGHTNING,
    
    # Electrification - Oscillitus
    "oscillitus": ALEMBIC_OSCILLITUS,
    "insulation": ALEMBIC_INSULATION,
    "blackout": ALEMBIC_BLACKOUT,
    "azothic_detonation": ALEMBIC_AZOTHIC_DETONATION,
    
    # Electrification - Imperatus
    "imperatus": ALEMBIC_IMPERATUS,
    "lightning_therapy": ALEMBIC_LIGHTNING_THERAPY,
    "remote_absorption": ALEMBIC_REMOTE_ABSORPTION,
    "power_sink": ALEMBIC_POWER_SINK,
    
    # Flux - Blight
    "blight": ALEMBIC_BLIGHT,
    "invoke_disquiet": ALEMBIC_INVOKE_DISQUIET,
    "aggravate_wasteland": ALEMBIC_AGGRAVATE_WASTELAND,
    "summon_firestorm": ALEMBIC_SUMMON_FIRESTORM,
    
    # Flux - Cannibalize
    "cannibalize": ALEMBIC_CANNIBALIZE,
    "aptitude": ALEMBIC_APTITUDE,
    "acumen": ALEMBIC_ACUMEN,
    "endowment": ALEMBIC_ENDOWMENT,
    
    # Flux - Lordship
    "lordship": ALEMBIC_LORDSHIP,
    "lordship_command": ALEMBIC_LORDSHIP_COMMAND,
    
    # Flux - Mutation
    "mutation": ALEMBIC_MUTATION,
    "dread_power": ALEMBIC_DREAD_POWER,
    
    # Flux - Solvent
    "solvent": ALEMBIC_SOLVENT,
    "disruption": ALEMBIC_DISRUPTION,
    "disaster": ALEMBIC_DISASTER,
    "detonation": ALEMBIC_DETONATION,
    
    # Flux - Unleash
    "unleash": ALEMBIC_UNLEASH,
    "invigorate": ALEMBIC_INVIGORATE,
    "infuse": ALEMBIC_INFUSE,
    "azothic_mantle": ALEMBIC_AZOTHIC_MANTLE,
    
    # Luciferus - Solar Flare
    "solar_flare": ALEMBIC_SOLAR_FLARE,
    "dazzling_corona": ALEMBIC_DAZZLING_CORONA,
    "searing_corona": ALEMBIC_SEARING_CORONA,
    "volatile_corona": ALEMBIC_VOLATILE_CORONA,
    
    # Luciferus - Morning Star
    "morning_star": ALEMBIC_MORNING_STAR,
    "ignus_fatuus": ALEMBIC_IGNUS_FATUUS,
    "beckon": ALEMBIC_BECKON,
    "ringleader": ALEMBIC_RINGLEADER,
    
    # Luciferus - Blaze of Glory
    "blaze_of_glory": ALEMBIC_BLAZE_OF_GLORY,
    "outshining_the_sun": ALEMBIC_OUTSHINING_THE_SUN,
    "roman_candle": ALEMBIC_ROMAN_CANDLE,
    "all_or_nothing": ALEMBIC_ALL_OR_NOTHING,
    
    # Luciferus - Beacon of Helios
    "beacon_of_helios": ALEMBIC_BEACON_OF_HELIOS,
    "daybreak": ALEMBIC_DAYBREAK,
    "guidepost": ALEMBIC_GUIDEPOST,
    "lighthouse_for_the_dead": ALEMBIC_LIGHTHOUSE_FOR_THE_DEAD,
    
    # Metamorphosis - Aptare
    "aptare": ALEMBIC_APTARE,
    "blessing_of_tethys": ALEMBIC_BLESSING_OF_TETHYS,
    "scuttling_spider": ALEMBIC_SCUTTLING_SPIDER,
    "procrustean_shape": ALEMBIC_PROCRUSTEAN_SHAPE,
    
    # Metamorphosis - Bestiae Facies
    "bestiae_facies": ALEMBIC_BESTIAE_FACIES,
    "natural_weaponry": ALEMBIC_NATURAL_WEAPONRY,
    "form_of_the_barghest": ALEMBIC_FORM_OF_THE_BARGHEST,
    "chimera": ALEMBIC_CHIMERA,
    
    # Metamorphosis - Tegere
    "tegere": ALEMBIC_TEGERE,
    "impermeable_shell": ALEMBIC_IMPERMEABLE_SHELL,
    "retributive_protection": ALEMBIC_RETRIBUTIVE_PROTECTION,
    "quill_assault": ALEMBIC_QUILL_ASSAULT,
    
    # Metamorphosis - Verto
    "verto": ALEMBIC_VERTO,
    "medusas_visage": ALEMBIC_MEDUSAS_VISAGE,
    "everyman": ALEMBIC_EVERYMAN,
    "body_like_clay": ALEMBIC_BODY_LIKE_CLAY,
    
    # Mesmerism - Phobos
    "phobos": ALEMBIC_PHOBOS,
    "rattle": ALEMBIC_RATTLE,
    "terrify": ALEMBIC_TERRIFY,
    "swoon": ALEMBIC_SWOON,
    
    # Mesmerism - Eros
    "eros": ALEMBIC_EROS,
    "lure": ALEMBIC_LURE,
    "seduce": ALEMBIC_SEDUCE,
    "inflame": ALEMBIC_INFLAME,
    
    # Mesmerism - Eris
    "eris": ALEMBIC_ERIS,
    "misdirect": ALEMBIC_MISDIRECT,
    "baffle": ALEMBIC_BAFFLE,
    "fog": ALEMBIC_FOG,
    
    # Mesmerism - Penthos
    "penthos": ALEMBIC_PENTHOS,
    "undermine": ALEMBIC_UNDERMINE,
    "defeat": ALEMBIC_DEFEAT,
    "depress": ALEMBIC_DEPRESS,
    
    # Saturninus - Heed the Call
    "heed_the_call": ALEMBIC_HEED_THE_CALL,
    "inscribed_in_flame": ALEMBIC_INSCRIBED_IN_FLAME,
    "controlled_burn": ALEMBIC_CONTROLLED_BURN,
    "sublimation_by_fire": ALEMBIC_SUBLIMATION_BY_FIRE,
    
    # Saturninus - Plumb the Fathoms
    "plumb_the_fathoms": ALEMBIC_PLUMB_THE_FATHOMS,
    "pilgrims_landmarks": ALEMBIC_PILGRIMS_LANDMARKS,
    "wisdom_of_ages": ALEMBIC_WISDOM_OF_AGES,
    "glimpsing_the_crasis": ALEMBIC_GLIMPSING_THE_CRASIS,
    
    # Saturninus - Stoke the Furnace
    "stoke_the_furnace": ALEMBIC_STOKE_THE_FURNACE,
    "catalytic_affirmation": ALEMBIC_CATALYTIC_AFFIRMATION,
    "chasing_hope": ALEMBIC_CHASING_HOPE,
    "transhuman_adaptation": ALEMBIC_TRANSHUMAN_ADAPTATION,
    
    # Saturninus - Prime the Vessel
    "prime_the_vessel": ALEMBIC_PRIME_THE_VESSEL,
    "shielding_pod": ALEMBIC_SHIELDING_POD,
    "humour_electrolysis": ALEMBIC_HUMOUR_ELECTROLYSIS,
    "pyros_branding": ALEMBIC_PYROS_BRANDING,
    
    # Sensorium - Vitreous Humour
    "vitreous_humour": ALEMBIC_VITREOUS_HUMOUR,
    "fire_sight": ALEMBIC_FIRE_SIGHT,
    "piercing_sight": ALEMBIC_PIERCING_SIGHT,
    "ephemeral_sight": ALEMBIC_EPHEMERAL_SIGHT,
    
    # Sensorium - Receptive Humour
    "receptive_humour": ALEMBIC_RECEPTIVE_HUMOUR,
    "translators_memory": ALEMBIC_TRANSLATORS_MEMORY,
    "rarified_senses": ALEMBIC_RARIFIED_SENSES,
    "circle_of_perception": ALEMBIC_CIRCLE_OF_PERCEPTION,
    
    # Sensorium - Stereo Humour
    "stereo_humour": ALEMBIC_STEREO_HUMOUR,
    "aura_sight": ALEMBIC_AURA_SIGHT,
    "hearing_the_inner_voice": ALEMBIC_HEARING_THE_INNER_VOICE,
    "clairvoyance": ALEMBIC_CLAIRVOYANCE,
    
    # Sensorium - Somatic Humour
    "somatic_humour": ALEMBIC_SOMATIC_HUMOUR,
    "bloodhounds_nose": ALEMBIC_BLOODHOUNDS_NOSE,
    "discriminating_tongue": ALEMBIC_DISCRIMINATING_TONGUE,
    "sensitive_ears": ALEMBIC_SENSITIVE_EARS,
    
    # Spiritus - Clades
    "clades": ALEMBIC_CLADES,
    "strike_the_heart": ALEMBIC_STRIKE_THE_HEART,
    "biting_aura": ALEMBIC_BITING_AURA,
    "burning_strike": ALEMBIC_BURNING_STRIKE,
    
    # Spiritus - Clupeum
    "clupeum": ALEMBIC_CLUPEUM,
    "personal_shield": ALEMBIC_PERSONAL_SHIELD,
    "interposing_shield": ALEMBIC_INTERPOSING_SHIELD,
    "mystic_fortress": ALEMBIC_MYSTIC_FORTRESS,
    
    # Spiritus - Veritas
    "veritas": ALEMBIC_VERITAS,
    "finding_the_wellspring": ALEMBIC_FINDING_THE_WELLSPRING,
    "walking_the_path_of_memory": ALEMBIC_WALKING_THE_PATH_OF_MEMORY,
    "disrupting_the_vital_humours": ALEMBIC_DISRUPTING_THE_VITAL_HUMOURS,
    
    # Spiritus - Laruae
    "laruae": ALEMBIC_LARUAE,
    "plumb_azothic_memory": ALEMBIC_PLUMB_AZOTHIC_MEMORY,
    "one_of_the_tribe": ALEMBIC_ONE_OF_THE_TRIBE,
    "pyros_decoy": ALEMBIC_PYROS_DECOY,
    
    # Vitality - Unbowed
    "unbowed": ALEMBIC_UNBOWED,
    "resolution_of_steel": ALEMBIC_RESOLUTION_OF_STEEL,
    "crucible_of_will": ALEMBIC_CRUCIBLE_OF_WILL,
    "roar_of_the_defiant": ALEMBIC_ROAR_OF_THE_DEFIANT,
    
    # Vitality - Unbroken
    "unbroken": ALEMBIC_UNBROKEN,
    "armor_of_will": ALEMBIC_ARMOR_OF_WILL,
    "drive_on": ALEMBIC_DRIVE_ON,
    "rebuke_the_shroud": ALEMBIC_REBUKE_THE_SHROUD,
    
    # Vitality - Unconquered
    "unconquered": ALEMBIC_UNCONQUERED,
    "cyclopean_might": ALEMBIC_CYCLOPEAN_MIGHT,
    "titans_throw": ALEMBIC_TITANS_THROW,
    "wrath_of_the_gods": ALEMBIC_WRATH_OF_THE_GODS,
    
    # Vitality - Unfettered
    "unfettered": ALEMBIC_UNFETTERED,
    "close_combat_defense": ALEMBIC_CLOSE_COMBAT_DEFENSE,
    "shattered_chains": ALEMBIC_SHATTERED_CHAINS,
    "no_walls_may_hold_me": ALEMBIC_NO_WALLS_MAY_HOLD_ME,
    
    # Vulcanus - Cauterio
    "cauterio": ALEMBIC_CAUTERIO,
    "alter_firetouched": ALEMBIC_ALTER_FIRETOUCHED,
    "animate_firetouched": ALEMBIC_ANIMATE_FIRETOUCHED,
    "evolve_firetouched": ALEMBIC_EVOLVE_FIRETOUCHED,
    
    # Vulcanus - Ignus Aspiratus
    "ignus_aspiratus": ALEMBIC_IGNUS_ASPIRATUS,
    "direct_fire": ALEMBIC_DIRECT_FIRE,
    "fire_grasp": ALEMBIC_FIRE_GRASP,
    "divine_guidance": ALEMBIC_DIVINE_GUIDANCE,
    
    # Vulcanus - Mutatus Aspiratus
    "mutatus_aspiratus": ALEMBIC_MUTATUS_ASPIRATUS,
    "contain_flux": ALEMBIC_CONTAIN_FLUX,
    "drawing_flux": ALEMBIC_DRAWING_FLUX,
    "expel_pyros": ALEMBIC_EXPEL_PYROS,
    
    # Vulcanus - Sanctus Aspiratus
    "sanctus_aspiratus": ALEMBIC_SANCTUS_ASPIRATUS,
    "refine_pyros": ALEMBIC_REFINE_PYROS,
    "steal_pyros": ALEMBIC_STEAL_PYROS,
    "drain_pyros": ALEMBIC_DRAIN_PYROS,
    
    # Vulcanus - The Tsar's Gift
    "the_tsars_gift": ALEMBIC_THE_TSARS_GIFT,
    "the_first_stone": ALEMBIC_THE_FIRST_STONE,
    "the_hand_that_feeds": ALEMBIC_THE_HAND_THAT_FEEDS,
    "sevenfold": ALEMBIC_SEVENFOLD
}

def get_alembic_info(alembic_name):
    """Get detailed information about a specific alembic."""
    return ALL_ALEMBICS_DETAILED.get(alembic_name.lower().replace(" ", "_"))

