"""
Mage Spells for Chronicles of Darkness 2nd Edition
Complete spell list from Codex of Darkness
Source: https://codexofdarkness.com/wiki/Spells,_All

Spells are organized by Arcana and dot level.
Available to: Mages, Sleepwalkers (limited), and Proximus (limited)
"""

# Spell data structure
# Each spell is a dictionary with the following keys:
# - arcana: Primary arcana
# - level: Dot level (1-5)
# - secondary_arcana: Secondary required arcana (if any)
# - practice: Type of practice
# - primary_factor: Primary factor for casting
# - withstand: What the spell must overcome
# - rote_skills: Suggested rote skills
# - description: Brief description
# - source: Book source

DEATH_SPELLS = {
    # Death 1
    "ectoplasmic_shaping": {
        "name": "Ectoplasmic Shaping",
        "arcana": "death",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Crafts", "Occult", "Larceny"],
        "description": "Shape and mold ectoplasm, or create Open Condition on an object or location for a ghost to Manifest",
        "source": "MtAw2 p128"
    },
    "deepen_shadows": {
        "name": "Deepen Shadows",
        "arcana": "death",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Intimidation", "Expression"],
        "description": "Apply Poor Light Tilt in area. +1 Reach: Apply Blinded Tilt in an area",
        "source": "MtAw2 p128"
    },
    "forensic_gaze": {
        "name": "Forensic Gaze",
        "arcana": "death",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Potency",
        "rote_skills": ["Medicine", "Investigation", "Expression"],
        "description": "Learn how a subject died. +1 Reach: Witness final moments of a corpse's life",
        "source": "MtAw2 p128"
    },
    "shadow_sculpting": {
        "name": "Shadow Sculpting",
        "arcana": "death",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Science", "Expression"],
        "description": "Shape shadows to your liking. +1 Reach: Both shape and animate shadows",
        "source": "MtAw2 p128"
    },
    "soul_marks": {
        "name": "Soul Marks",
        "arcana": "death",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Medicine", "Occult", "Empathy"],
        "description": "Learn about a subjects soul. +1 Reach: Can use spell on unattached souls",
        "source": "MtAw2 p128"
    },
    "speak_with_the_dead": {
        "name": "Speak with the Dead",
        "arcana": "death",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Socialize", "Expression", "Investigation"],
        "description": "Sense and communicate with ghosts in Twilight. Sense anchors and determine a ghosts rank",
        "source": "MtAw2 p128"
    },
    
    # Death 2
    "corpse_mask": {
        "name": "Corpse Mask",
        "arcana": "death",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Subterfuge", "Crafts", "Medicine"],
        "description": "Alter a corpse's apparent time and cause of death",
        "source": "MtAw2 p129"
    },
    "decay": {
        "name": "Decay",
        "arcana": "death",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Subterfuge", "Science", "Occult"],
        "description": "Age an object, lowering durability. +1 Reach: Decrease structure instead",
        "source": "MtAw2 p129"
    },
    "ectoplasm": {
        "name": "Ectoplasm",
        "arcana": "death",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Expression", "Academics"],
        "description": "Create ectoplasm from your own orifices or that of a corpse",
        "source": "MtAw2 p129"
    },
    "ghost_shield": {
        "name": "Ghost Shield",
        "arcana": "death",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Potency",
        "rote_skills": ["Occult", "Expression", "Academics"],
        "description": "Protects subject from ghostly Numina, Influences and Manifestations",
        "source": "MtAw2 p129"
    },
    "shape_ephemera": {
        "name": "Shape Ephemera",
        "arcana": "death",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Crafts", "Expression", "Science"],
        "description": "Shape ephemera into objects, weapons or armor",
        "source": "MtAw2 p129"
    },
    "soul_armor": {
        "name": "Soul Armor",
        "arcana": "death",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Occult", "Survival"],
        "description": "Protect soul against hostile spells",
        "source": "MtAw2 p129"
    },
    "soul_jar": {
        "name": "Soul Jar",
        "arcana": "death",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Crafts", "Occult", "Persuasion"],
        "description": "Trap unattached soul into container",
        "source": "MtAw2 p129"
    },
    "suppress_aura": {
        "name": "Suppress Aura",
        "arcana": "death",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Subterfuge", "Intimidation", "Medicine"],
        "description": "Suppress Nimbus to appear as a sleeper to Mage Sight",
        "source": "MtAw2 p129"
    },
    "suppress_life": {
        "name": "Suppress Life",
        "arcana": "death",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Subterfuge", "Medicine", "Academics"],
        "description": "Appear to be a corpse",
        "source": "MtAw2 p130"
    },
    "touch_of_the_grave": {
        "name": "Touch of the Grave",
        "arcana": "death",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Survival", "Crafts", "Persuasion"],
        "description": "Interact with ghosts and other things in Death-attuned Twilight",
        "source": "MtAw2 p130"
    },
    "without_a_trace": {
        "name": "Without a Trace",
        "arcana": "death",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Science", "Stealth", "Subterfuge"],
        "description": "Leave no forensic evidence like fingerprints",
        "source": "MtAw2 p130"
    },
    
    # Death 3
    "cold_snap": {
        "name": "Cold Snap",
        "arcana": "death",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Survival", "Intimidation", "Science"],
        "description": "Apply Ice Tilt to area. +1 Reach: Also apply Extreme Cold Tilt",
        "source": "MtAw2 p130"
    },
    "damage_ghost": {
        "name": "Damage Ghost",
        "arcana": "death",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "rote_skills": ["Occult", "Intimidation", "Brawl"],
        "description": "Deal bashing damage to ghost",
        "source": "MtAw2 p130"
    },
    "devouring_the_slain": {
        "name": "Devouring the Slain",
        "arcana": "death",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Intimidation", "Medicine", "Persuasion"],
        "description": "Can take Willpower or Scour the pattern of an injured person",
        "source": "MtAw2 p130"
    },
    "ghost_gate": {
        "name": "Ghost Gate",
        "arcana": "death",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Occult", "Persuasion"],
        "description": "Create a gateway to the Underworld",
        "source": "MtAw2 p130"
    },
    "ghost_summons": {
        "name": "Ghost Summons",
        "arcana": "death",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "withstand": "Rank",
        "rote_skills": ["Intimidation", "Occult", "Persuasion"],
        "description": "Summon a ghost to your location",
        "source": "MtAw2 p131"
    },
    "quicken_corpse": {
        "name": "Quicken Corpse",
        "arcana": "death",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Medicine", "Occult", "Intimidation"],
        "description": "Animate a corpse as a zombie servant",
        "source": "MtAw2 p131"
    },
    "quicken_ghost": {
        "name": "Quicken Ghost",
        "arcana": "death",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "withstand": "Rank",
        "rote_skills": ["Intimidation", "Occult", "Persuasion"],
        "description": "Compel a ghost to serve you",
        "source": "MtAw2 p131"
    },
    "rotting_flesh": {
        "name": "Rotting Flesh",
        "arcana": "death",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "withstand": "Stamina",
        "rote_skills": ["Intimidation", "Medicine", "Science"],
        "description": "Deal lethal damage by accelerating decay",
        "source": "MtAw2 p131"
    },
    "sever_soul": {
        "name": "Sever Soul",
        "arcana": "death",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Intimidation", "Medicine", "Occult"],
        "description": "Separate a soul from a body",
        "source": "MtAw2 p131"
    },
    
    # Death 4
    "enervation": {
        "name": "Enervation",
        "arcana": "death",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "withstand": "Stamina",
        "rote_skills": ["Intimidation", "Medicine", "Occult"],
        "description": "Drain the subject's life force, imposing negative modifiers",
        "source": "MtAw2 p131"
    },
    "exorcism": {
        "name": "Exorcism",
        "arcana": "death",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "withstand": "Rank",
        "rote_skills": ["Intimidation", "Occult", "Persuasion"],
        "description": "Banish a ghost from the material world",
        "source": "MtAw2 p132"
    },
    "revenant": {
        "name": "Revenant",
        "arcana": "death",
        "level": 4,
        "secondary_arcana": "spirit 4",
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Rank",
        "rote_skills": ["Medicine", "Occult", "Persuasion"],
        "description": "Bind a ghost into a corpse, creating an intelligent undead",
        "source": "MtAw2 p132"
    },
    "shadow_crafting": {
        "name": "Shadow Crafting",
        "arcana": "death",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Create solid objects from shadow",
        "source": "MtAw2 p132"
    },
    
    # Death 5
    "create_anchor": {
        "name": "Create Anchor",
        "arcana": "death",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Occult", "Persuasion"],
        "description": "Create a permanent anchor for a ghost",
        "source": "MtAw2 p132"
    },
    "create_ghost": {
        "name": "Create Ghost",
        "arcana": "death",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Occult", "Persuasion"],
        "description": "Create a ghost from nothing",
        "source": "MtAw2 p132"
    },
    "empty_presence": {
        "name": "Empty Presence",
        "arcana": "death",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Duration",
        "rote_skills": ["Intimidation", "Medicine", "Stealth"],
        "description": "Become completely undetectable by any supernatural means",
        "source": "MtAw2 p133"
    },
    "sever_the_awakened_soul": {
        "name": "Sever the Awakened Soul",
        "arcana": "death",
        "level": 5,
        "secondary_arcana": "prime 5",
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Intimidation", "Medicine", "Occult"],
        "description": "Separate a mage's Avatar from their body",
        "source": "MtAw2 p133"
    }
}

TIME_SPELLS = {
    # Time 1
    "divination": {
        "name": "Divination",
        "arcana": "time",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Investigation", "Occult"],
        "description": "Ask questions about the past, present, or future",
        "source": "MtAw2ed p187"
    },
    "momentary_flux": {
        "name": "Momentary Flux",
        "arcana": "time",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Firearms", "Stealth"],
        "description": "Reroll a single instant action that just occurred",
        "source": "MtAw2ed p187"
    },
    "perfect_timing": {
        "name": "Perfect Timing",
        "arcana": "time",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Crafts", "Socialize"],
        "description": "Know the perfect moment to act, gain bonus to actions",
        "source": "MtAw2ed p187"
    },
    "postdiction": {
        "name": "Postdiction",
        "arcana": "time",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Investigation", "Medicine"],
        "description": "View the past of a subject or location",
        "source": "MtAw2ed p188"
    },
    
    # Time 2
    "choose_the_thread": {
        "name": "Choose the Thread",
        "arcana": "time",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Investigation", "Occult"],
        "description": "View multiple possible futures and choose the best outcome",
        "source": "MtAw2ed p188"
    },
    "constant_presence": {
        "name": "Constant Presence",
        "arcana": "time",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Stealth", "Survival"],
        "description": "Protect against temporal manipulation",
        "source": "MtAw2ed p188"
    },
    "hung_spell": {
        "name": "Hung Spell",
        "arcana": "time",
        "level": 2,
        "secondary_arcana": "fate 2",
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Occult", "Expression"],
        "description": "Delay a spell's effect until a specific condition is met",
        "source": "MtAw2ed p188"
    },
    "shield_of_chronos": {
        "name": "Shield of Chronos",
        "arcana": "time",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Occult", "Survival"],
        "description": "Protect subject from Time-based attacks",
        "source": "MtAw2ed p188"
    },
    "tipping_the_hourglass": {
        "name": "Tipping the Hourglass",
        "arcana": "time",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Investigation", "Medicine", "Occult"],
        "description": "Advance or reverse time's effects on an object",
        "source": "MtAw2ed p188"
    },
    "veil_of_moments": {
        "name": "Veil of Moments",
        "arcana": "time",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Medicine", "Investigation", "Subterfuge"],
        "description": "Protect a subject from Time's effects - no aging, bleeding out stalled, etc",
        "source": "MtAw2ed p188"
    },
    
    # Time 3
    "acceleration": {
        "name": "Acceleration",
        "arcana": "time",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Drive", "Stealth"],
        "description": "Speed up a subject's movements, multiply speed by Potency",
        "source": "MtAw2ed p189"
    },
    "chronos_curse": {
        "name": "Chronos' Curse",
        "arcana": "time",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "withstand": "Stamina",
        "rote_skills": ["Academics", "Occult", "Intimidation"],
        "description": "Slow a subject down, reduces Defense and Speed",
        "source": "MtAw2ed p190"
    },
    "shifting_sands": {
        "name": "Shifting Sands",
        "arcana": "time",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Occult", "Survival"],
        "description": "Subject goes back in time a number of turns equal to Potency",
        "source": "MtAw2ed p190"
    },
    "temporal_summoning": {
        "name": "Temporal Summoning",
        "arcana": "time",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Investigation", "Persuasion"],
        "description": "Return the subject to a younger version of itself",
        "source": "MtAw2ed p190"
    },
    "weight_of_years": {
        "name": "Weight of Years",
        "arcana": "time",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Intimidation", "Medicine"],
        "description": "Attack spell dealing Bashing damage equal to Potency",
        "source": "MtAw2ed p191"
    },
    
    # Time 4
    "present_as_past": {
        "name": "Present as Past",
        "arcana": "time",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Investigation", "Streetwise"],
        "description": "See the future, declare actions first in combat",
        "source": "MtAw2ed p191"
    },
    "prophecy": {
        "name": "Prophecy",
        "arcana": "time",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Expression", "Investigation"],
        "description": "Ask 'what if?' questions about possible futures",
        "source": "MtAw2ed p191"
    },
    "rend_lifespan": {
        "name": "Rend Lifespan",
        "arcana": "time",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Medicine", "Intimidation"],
        "description": "Attack spell dealing Lethal damage equal to Potency",
        "source": "MtAw2ed p191"
    },
    "rewrite_history": {
        "name": "Rewrite History",
        "arcana": "time",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Expression", "Investigation", "Persuasion"],
        "description": "Change the subject's timeline as though different choices were made",
        "source": "MtAw2ed p191"
    },
    "temporal_stutter": {
        "name": "Temporal Stutter",
        "arcana": "time",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Stamina",
        "rote_skills": ["Intimidation", "Science", "Survival"],
        "description": "Throw a subject forward in time",
        "source": "MtAw2ed p192"
    },
    
    # Time 5
    "blink_of_an_eye": {
        "name": "Blink of an Eye",
        "arcana": "time",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Crafts", "Occult"],
        "description": "Turn next extended action into an instant action",
        "source": "MtAw2ed p192"
    },
    "corridors_of_time": {
        "name": "Corridors of Time",
        "arcana": "time",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Investigation", "Persuasion"],
        "description": "Subject inhabits their past self and can change history",
        "source": "MtAw2ed p192"
    },
    "temporal_pocket": {
        "name": "Temporal Pocket",
        "arcana": "time",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Science", "Stealth"],
        "description": "Grant the subject extra time - the world around them freezes",
        "source": "MtAw2ed p192"
    }
}

FATE_SPELLS = {
    # Fate 1
    "interconnections": {
        "name": "Interconnections",
        "arcana": "fate",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Empathy", "Investigation", "Medicine"],
        "description": "Reveal sympathetic connections, who has violated an oath or geas and spells with conditional duration",
        "source": "MtAw2 p134"
    },
    "oaths_fulfilled": {
        "name": "Oaths Fulfilled",
        "arcana": "fate",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Politics", "Investigation"],
        "description": "Know when the subject breaks or fulfills an oath",
        "source": "MtAw2 p135"
    },
    "quantum_flux": {
        "name": "Quantum Flux",
        "arcana": "fate",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Firearms", "Occult"],
        "description": "Negate penalties to Mundane actions or wait a turn to receive bonus to next mundane action",
        "source": "MtAw2 p135"
    },
    "reading_the_outmost_eddies": {
        "name": "Reading the Outmost Eddies",
        "arcana": "fate",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Computer", "Persuasion", "Subterfuge"],
        "description": "Subject receives a minor twist of fate positive or negative in 24 hours",
        "source": "MtAw2 p135"
    },
    "serendipity": {
        "name": "Serendipity",
        "arcana": "fate",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Crafts", "Survival"],
        "description": "Reveal what course of action will bring you closer to your goal",
        "source": "MtAw2 p135"
    },
    
    # Fate 2
    "exceptional_luck": {
        "name": "Exceptional Luck",
        "arcana": "fate",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Intimidation", "Occult", "Socialize"],
        "description": "Subject receives a boon or hex. A hex may be withstood",
        "source": "MtAw2 p136"
    },
    "fabricate_fortune": {
        "name": "Fabricate Fortune",
        "arcana": "fate",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Larceny", "Occult", "Subterfuge"],
        "description": "Conceal and falsify a subject's fate or Destiny",
        "source": "MtAw2 p136"
    },
    "fools_rush_in": {
        "name": "Fools Rush In",
        "arcana": "fate",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Socialize", "Streetwise"],
        "description": "Suffer no untrained skill penalties when facing a situation unprepared",
        "source": "MtAw2 p136"
    },
    "lucky_number": {
        "name": "Lucky Number",
        "arcana": "fate",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Investigation", "Larceny", "Science"],
        "description": "Guess the right password, phone number, etc. on the first try",
        "source": "MtAw2 p136"
    },
    "malleable_thorns": {
        "name": "Malleable Thorns",
        "arcana": "fate",
        "level": 2,
        "secondary_arcana": "mind 2",
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Empathy", "Survival"],
        "description": "Mage states a goal and the Hedge alters itself to fulfill that goal",
        "source": "DE2 p377"
    },
    "shifting_the_odds": {
        "name": "Shifting the Odds",
        "arcana": "fate",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Investigation", "Politics", "Subterfuge"],
        "description": "Find a particular kind of person, place or thing within 24 hours",
        "source": "MtAw2 p136"
    },
    "warding_gesture": {
        "name": "Warding Gesture",
        "arcana": "fate",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Brawl", "Occult", "Subterfuge"],
        "description": "Protect a subject against supernatural effect that would alter her fate",
        "source": "MtAw2 p136"
    },
    
    # Fate 3
    "grave_misfortune": {
        "name": "Grave Misfortune",
        "arcana": "fate",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Intimidation", "Occult", "Weaponry"],
        "description": "The next time the subject suffers damage, increase the damage",
        "source": "MtAw2 p137"
    },
    "monkeys_paw": {
        "name": "Monkey's Paw",
        "arcana": "fate",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Drive", "Crafts", "Science"],
        "description": "Bless or curse an object altering its equipment bonus",
        "source": "MtAw2 p137"
    },
    "shared_fate": {
        "name": "Shared Fate",
        "arcana": "fate",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Medicine", "Persuasion", "Politics"],
        "description": "Two or more subjects are bound together. Any damage, Tilt or Condition suffered by one will also affect the other",
        "source": "MtAw2 p137"
    },
    "superlative_luck": {
        "name": "Superlative Luck",
        "arcana": "fate",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Crafts", "Occult"],
        "description": "Cost: 1 Mana, Gain the rote quality",
        "source": "MtAw2 p137"
    },
    "sworn_oaths": {
        "name": "Sworn Oaths",
        "arcana": "fate",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Occult", "Politics"],
        "description": "Supernaturally enforce a vow. Adhere to the oath and the subject receives a boon, break it and she suffers a hex",
        "source": "MtAw2 p137"
    },
    "the_right_tool": {
        "name": "The Right Tool",
        "arcana": "fate",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Stealth", "Expression"],
        "description": "Turn an ordinary object into the object needed to get the job done",
        "source": "SoS 64"
    },
    "wyrdbound_oaths": {
        "name": "Wyrdbound Oaths",
        "arcana": "fate",
        "level": 3,
        "secondary_arcana": "mind 2",
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Politics", "Socialize"],
        "description": "Allow Mages to be valid participants in Wyrd-backed oaths",
        "source": "DE2 p379"
    },
    
    # Fate 4
    "atonement": {
        "name": "Atonement",
        "arcana": "fate",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "withstand": "Countered effect's Potency",
        "rote_skills": ["Academics", "Occult", "Subterfuge"],
        "description": "If a subject is cursed, grant them a quest that if fulfilled will lift the curse",
        "source": "MtAw2 p137"
    },
    "chaos_mastery": {
        "name": "Chaos Mastery",
        "arcana": "fate",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Occult", "Science"],
        "description": "Manipulate complex probabilities within subject or area, dictating any physically possible outcome",
        "source": "MtAw2 p138"
    },
    "divine_intervention": {
        "name": "Divine Intervention",
        "arcana": "fate",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Intimidation", "Occult", "Subterfuge"],
        "description": "Replace one of the subject's Aspirations with a stated goal",
        "source": "MtAw2 p138"
    },
    "masking_the_false_fae": {
        "name": "Masking the False Fae",
        "arcana": "fate",
        "level": 4,
        "secondary_arcana": "mind 1",
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Empathy", "Larceny", "Socialize"],
        "description": "Allow Changelings to make Goblin Contracts with supernal entities",
        "source": "DE2 p376"
    },
    "scribe_daimonomikon": {
        "name": "Scribe Daimonomikon",
        "arcana": "fate",
        "level": 4,
        "secondary_arcana": "prime 1",
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Rank of Attainment + (10 - Caster's Gnosis)",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Cost 1 Mana. Scribe a Daimonomikon for the Mage's Legacy",
        "source": "SoS 87"
    },
    "strings_of_fate": {
        "name": "Strings of Fate",
        "arcana": "fate",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Academics", "Persuasion", "Stealth"],
        "description": "Encourage a specific event to befall the subject",
        "source": "MtAw2 p138"
    },
    "sever_oaths": {
        "name": "Sever Oaths",
        "arcana": "fate",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Occult", "Subterfuge", "Weaponry"],
        "description": "Free a bound ephemeral entity or dispel a conditional trigger",
        "source": "MtAw2 p138"
    },
    
    # Fate 5
    "forge_destiny": {
        "name": "Forge Destiny",
        "arcana": "fate",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Intimidation", "Occult", "Persuasion"],
        "description": "Grant the subject a supernatural merit or increase/decrease an existing one. Impose Aspirations, Obsessions or a Doom",
        "source": "MtAw2 p139"
    },
    "miracle": {
        "name": "Miracle",
        "arcana": "fate",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Persuasion", "Subterfuge"],
        "description": "Mage gains Intercessions that can be spent reflexively to increase/decrease dice pools or cause likely events",
        "source": "MtAw2 p140"
    },
    "pariah": {
        "name": "Pariah",
        "arcana": "fate",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Investigation", "Medicine", "Politics"],
        "description": "Turns the whole world against the subject",
        "source": "MtAw2 p139"
    },
    "swarm_of_locusts": {
        "name": "Swarm of Locusts",
        "arcana": "fate",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Intimidation", "Occult", "Science"],
        "description": "Create chaotic conditions that cause Environmental Tilts of player's choosing on the area",
        "source": "MtAw2 p140"
    }
}

FORCES_SPELLS = {
    # Forces 1
    "influence_electricity": {
        "name": "Influence Electricity",
        "arcana": "forces",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Computers", "Crafts", "Science"],
        "description": "Operate or shut down electrical devices",
        "source": "MtAw2 p140"
    },
    "influence_fire": {
        "name": "Influence Fire",
        "arcana": "forces",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Science", "Survival"],
        "description": "Guide flames along a particular path. +1 Reach: Increase or decrease the size of a flame",
        "source": "MtAw2 p140"
    },
    "kinetic_efficiency": {
        "name": "Kinetic Efficiency",
        "arcana": "forces",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Science", "Survival"],
        "description": "Run faster, jump further or lift more",
        "source": "MtAw2 p141"
    },
    "influence_heat": {
        "name": "Influence Heat",
        "arcana": "forces",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Science", "Survival"],
        "description": "Control the flow of heat in an area. Can protect against heat- or cold-related Environments up to level 2",
        "source": "MtAw2 p141"
    },
    "nightvision": {
        "name": "Nightvision",
        "arcana": "forces",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Investigation", "Science", "Stealth"],
        "description": "Suffer no penalty from dim to no light. Bright lights can inflict the Blind Condition. +1 Reach: No longer risk the Blind Condition from sudden bright lights",
        "source": "MtAw2 p141"
    },
    "receiver": {
        "name": "Receiver",
        "arcana": "forces",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Empathy", "Investigation", "Science"],
        "description": "Hear sounds outside normal human frequency",
        "source": "MtAw2 p141"
    },
    "tune_in": {
        "name": "Tune In",
        "arcana": "forces",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Duration",
        "rote_skills": ["Computers", "Empathy", "Science"],
        "description": "Become able to see and listen to data transmission",
        "source": "MtAw2 p141"
    },
    
    # Forces 2
    "control_electricity": {
        "name": "Control Electricity",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Computers", "Science"],
        "description": "Alter the flow of a current or decrease it, but you cannot increase it. Direct a buildings electricity to one outlet, or divide the power from one outlet to many other sources",
        "source": "MtAw2 p142"
    },
    "control_fire": {
        "name": "Control Fire",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Science", "Survival"],
        "description": "Increase or decrease the heat or size of a fire",
        "source": "MtAw2 p142"
    },
    "control_gravity": {
        "name": "Control Gravity",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Occult", "Science"],
        "description": "Cause gravity to pull upwards or horizontally",
        "source": "MtAw2 p142"
    },
    "control_heat": {
        "name": "Control Heat",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Science", "Survival"],
        "description": "Increase or decrease the temperature of an area this may cause an Extreme Environment",
        "source": "MtAw2 p142"
    },
    "control_light": {
        "name": "Control Light",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Investigation", "Science"],
        "description": "Can focus or disperse light, and alter its wavelength on the spectrum. +1 Reach: Can create a mirroring effect or a complete black-out which causes the Blinded Tilt or provides substantial cover",
        "source": "MtAw2 p142"
    },
    "control_sound": {
        "name": "Control Sound",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Stealth", "Science"],
        "description": "Amplify or dampen sound, can also influence the direction of sound. Loud sounds can cause the Deafened Tilt in combat",
        "source": "MtAw2 p142"
    },
    "control_weather": {
        "name": "Control Weather",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Science", "Survival"],
        "description": "Make changes to the weather may create an Extreme Environments up to level 4. +1 Reach: Weather changes are more gradual. +2 Reach: Required for more drastic changes",
        "source": "MtAw2 p143"
    },
    "environmental_shield": {
        "name": "Environmental Shield",
        "arcana": "forces",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Science", "Survival"],
        "description": "This spell gives resistance to any Conditions and Tilts caused by the environment",
        "source": "MtAw2 p143"
    },
    "invisibility": {
        "name": "Invisibility",
        "arcana": "forces",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Larceny", "Science", "Stealth"],
        "description": "Make a subject invisible",
        "source": "MtAw2 p143"
    },
    "kinetic_blow": {
        "name": "Kinetic Blow",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Brawl", "Science"],
        "description": "Unarmed attacks gain a bonus. +1 Reach: Apply the Knocked Down Tilt. +1 Reach: Apply the Stunned Tilt. +1 Reach: Spell can affect held weapons. +2 Reach: Spell affects thrown weapons but can also grant bullets Armor Piercing",
        "source": "MtAw2 p143"
    },
    "transmission": {
        "name": "Transmission",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Expression", "Science"],
        "description": "Hijack existing signals and change the transmitted data or its destination. +1 Reach: The signal becomes encrypted only specific actions will allow somebody to read them",
        "source": "MtAw2 p144"
    },
    "zoom_in": {
        "name": "Zoom In",
        "arcana": "forces",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Investigation", "Science", "Survival"],
        "description": "See distant objects or better examine small ones. +1 Reach: See clearly for miles. +1 Reach: Clearly examine dust-sized particles. +1 Reach: No longer suffer penalties from atmospheric conditions. +2 Reach: Clearly see microscopic particles, even molecular bonds",
        "source": "MtAw2 p144"
    },
    
    # Forces 3
    "call_lightning": {
        "name": "Call Lightning",
        "arcana": "forces",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Firearms", "Science"],
        "description": "Can call lightning from an existing storm which may be created with Control Weather",
        "source": "MtAw2 p144"
    },
    "data_hog": {
        "name": "Data Hog",
        "arcana": "forces",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Computer", "Larceny", "Persuasion"],
        "description": "Increase or decrease a computer device's capability to process, accept and transfer data by Potency",
        "source": "SoS 65"
    },
    "energize_object": {
        "name": "Energize Object",
        "arcana": "forces",
        "level": 3,
        "secondary_arcana": "prime 2",
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Larceny", "Science"],
        "description": "Cost 1 Mana. Primes an object with the potential for activation to hold a spell. Once the object is primed a mage may spend a Mana to cast any other spell on the object which doesn't activate until appropriate force is applied to the object",
        "source": "SoS 69"
    },
    "gravitic_supremacy": {
        "name": "Gravitic Supremacy",
        "arcana": "forces",
        "level": 3,
        "practice": "Fraying/Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Science", "Survival"],
        "description": "Increase or decrease gravity",
        "source": "MtAw2 p144"
    },
    "perpetual_motion": {
        "name": "Perpetual Motion",
        "arcana": "forces",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Science", "Survival"],
        "description": "The subject no longer requires an energy input for the duration of the spell",
        "source": "SoS 65"
    },
    "rapid_access_memory": {
        "name": "Rapid Access Memory",
        "arcana": "forces",
        "level": 3,
        "secondary_arcana": "prime 3",
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Larceny", "Science"],
        "description": "Allows the Subject to use the attainment Imbue Item on computer Software which can later be activated on a computer",
        "source": "SoS 69"
    },
    "telekinesis": {
        "name": "Telekinesis",
        "arcana": "forces",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Brawl", "Science"],
        "description": "Use telekinetic force to lift or manipulate an object remotely. Potency is applied to either Strength or Dexterity the remaining stat becomes 1. +1 Reach: Divide Potency between Two of the Three Physical Attributes. +2 Reach: Divide Potency between any of the Three Physical Attributes",
        "source": "MtAw2 p144"
    },
    "telekinetic_strike": {
        "name": "Telekinetic Strike",
        "arcana": "forces",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Firearms", "Science"],
        "description": "Deal bashing damage. +1 Reach: Apply the Knocked Down or Stunned Tilt",
        "source": "MtAw2 p145"
    },
    "turn_momentum": {
        "name": "Turn Momentum",
        "arcana": "forces",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Firearms", "Science"],
        "description": "When applying defense against an object this spell may be used, causing the object to be deflected in an uncontrolled direction though it never reverses direction. +1 Reach: Spell can be used as an reflexive action. +1 Reach: Mage has control over where the object is deflected",
        "source": "MtAw2 p145"
    },
    "velocity_control": {
        "name": "Velocity Control",
        "arcana": "forces",
        "level": 3,
        "practice": "Fraying or Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Firearms", "Science"],
        "description": "Increase or decrease an objects speed",
        "source": "MtAw2 p145"
    },
    
    # Forces 4
    "electromagnetic_pulse": {
        "name": "Electromagnetic Pulse",
        "arcana": "forces",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Computers", "Science"],
        "description": "By Unraveling electricity in the Subject this Creates an EMP that snuffs out powered devices in the affected area. Military devices may be shielded. Magical devices require a Clash of Wills. If used on a Living being this acts as an attack spell",
        "source": "MtAw2 p145"
    },
    "levitation": {
        "name": "Levitation",
        "arcana": "forces",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Athletics", "Science", "Survival"],
        "description": "Levitate a subject, if unwilling the spell is withstood. You may direct the levitation each turn as an instant action. +1 Reach: Subject retains momentum from turn to turn. +1 Reach: Subject can fly freely",
        "source": "MtAw2 p145"
    },
    "rend_friction": {
        "name": "Rend Friction",
        "arcana": "forces",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Drive", "Science"],
        "description": "Increase or decrease friction. Increases can cause lethal damage. Decreases cause objects to move after they normally would have stopped",
        "source": "MtAw2 p145"
    },
    "thunderbolt": {
        "name": "Thunderbolt",
        "arcana": "forces",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Firearms", "Science"],
        "description": "Deal lethal damage. +1 Reach: Spend one Mana, spell deals aggravated damage",
        "source": "MtAw2 p146"
    },
    "transform_energy": {
        "name": "Transform Energy",
        "arcana": "forces",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Occult", "Science"],
        "description": "Transform one type of energy into another of the same level. +1 Reach: May decrease the level of transformed energy by one. +1 Reach: Split one type of energy into two others. +1 Reach: Spend one Mana, increase the level of transformed energy by one",
        "source": "MtAw2 p146"
    },
    
    # Forces 5
    "adverse_weather": {
        "name": "Adverse Weather",
        "arcana": "forces",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Occult", "Science"],
        "description": "Create Extreme Environments of nearly any kind up to level 4. +1 Reach: Can create weather drastically different from the local conditions",
        "source": "MtAw2 p146"
    },
    "create_energy": {
        "name": "Create Energy",
        "arcana": "forces",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Occult", "Science"],
        "description": "Create any type of energy from nothing, including sunlight and radiation",
        "source": "MtAw2 p146"
    },
    "eradicate_energy": {
        "name": "Eradicate Energy",
        "arcana": "forces",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "rote_skills": ["Intimidation", "Science", "Survival"],
        "description": "Explosively destroy energy, if used on a creature the spell is instantly fatal",
        "source": "MtAw2 p146"
    },
    "earthquake": {
        "name": "Earthquake",
        "arcana": "forces",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Science", "Survival"],
        "description": "Apply damage to all structures within the affected area. Buildings made to withstand earthquakes subtract their Durability",
        "source": "MtAw2 p147"
    }
}

LIFE_SPELLS = {
    # Life 1
    "analyze_life": {
        "name": "Analyze Life",
        "arcana": "life",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Duration",
        "rote_skills": ["Animal Ken", "Medicine", "Survival"],
        "description": "Observe a creature and learn information like species, age, sex and overall health. Can discern amount of dots in physical attributes and any illnesses, injuries, Personal Tilts and Condition on target. +1 Reach: May learn a specific Physical Attribute level",
        "source": "MtAw2 p148"
    },
    "cleanse_the_body": {
        "name": "Cleanse the Body",
        "arcana": "life",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Medicine", "Survival"],
        "description": "Help subject resist any toxins in her system. +1 Reach: The subject may make a resistance roll immediately, in addition to the normal ones from regular intervals",
        "source": "MtAw2 p148"
    },
    "heightened_senses": {
        "name": "Heightened Senses",
        "arcana": "life",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Empathy", "Investigation", "Survival"],
        "description": "Heighten desired senses. Grants bonus to perception roles. +1 Reach: You can track by scent",
        "source": "MtAw2 p149"
    },
    "speak_with_beasts": {
        "name": "Speak With Beasts",
        "arcana": "life",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Animal Ken", "Empathy", "Survival"],
        "description": "Magically speak with a specific species of animal. Animals have limited ability to understand things around them. +1 Reach: May communicate with all animals rather than only a single species",
        "source": "MtAw2 p148"
    },
    "web_of_life": {
        "name": "Web of Life",
        "arcana": "life",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Duration",
        "rote_skills": ["Investigation", "Medicine", "Survival"],
        "description": "Detect all forms of specified life in the spells area of effect",
        "source": "MtAw2 p148"
    },
    
    # Life 2
    "body_control": {
        "name": "Body Control",
        "arcana": "life",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Medicine", "Survival"],
        "description": "Slow Breathing, Heartbeat and/or Metabolism. Up your Initiative, eliminate or increase body odors and halve healing time for bashing damage. +1 Reach: Gain 1/0 armor. +2 reach: Half healing time for lethal damage",
        "source": "MtAw2 p148"
    },
    "control_instincts": {
        "name": "Control Instincts",
        "arcana": "life",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Animal Ken", "Intimidation", "Persuasion"],
        "description": "Trigger a specific instinctual response in animals (includes humans). Subject suffers a Condition related to the desired instinct. +1 Reach: Control instincts of living supernatural creatures",
        "source": "MtAw2 p149"
    },
    "lure_and_repel": {
        "name": "Lure and Repel",
        "arcana": "life",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Animal Ken", "Persuasion", "Survival"],
        "description": "Create a lure or repellent that works on a specific organism. Plant and bacteria have 0 resolve for the purposes of this spell. +1 Reach: Lured creatures may offer food or small favors",
        "source": "MtAw2 p149"
    },
    "mutable_mask": {
        "name": "Mutable Mask",
        "arcana": "life",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Medicine", "Stealth", "Subterfuge"],
        "description": "Change a subjects appearance, apparent sex, voice, smell, etc. Changes are illusionary, bio-metric devices will still pick up the truth. Cannot imitate specific people. +2 Reach: Can duplicate the appearance of a specific person",
        "source": "MtAw2 p149"
    },
    "purge_illness": {
        "name": "Purge Illness",
        "arcana": "life",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Medicine", "Survival"],
        "description": "Cure yourself of an illness. Compare Potency to the illness' rating if less, reduce the illness by the difference if more, eliminate the illness",
        "source": "MtAw2 p149"
    },
    
    # Life 3
    "bruise_flesh": {
        "name": "Bruise Flesh",
        "arcana": "life",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "rote_skills": ["Brawl", "Intimidation", "Medicine"],
        "description": "Deal bashing damage. +1 Reach: Inflict an additional -1 penalty to any wound penalties the target might have",
        "source": "MtAw2 p150"
    },
    "contact_high": {
        "name": "Contact High",
        "arcana": "life",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Medicine", "Occult", "Science"],
        "description": "Creates a drug that targets the nervous system. Anyone who comes into contact with the Subject is affected by this drug for one scene. The Caster determines if it increases Initiative equal to Potency or penalizes Initiative equal to Potency",
        "source": "SoS 65"
    },
    "degrading_the_form": {
        "name": "Degrading the Form",
        "arcana": "life",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Brawl", "Medicine", "Survival"],
        "description": "Reduce a targets Physical Attributes, but only one. +1 Reach: Spell may effect two different Physical Attributes",
        "source": "MtAw2 p150"
    },
    "honing_the_form": {
        "name": "Honing the Form",
        "arcana": "life",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Medicine", "Survival"],
        "description": "Raise Strength, Dexterity or Stamina, but no higher than a subjects max for these stats. +1 Reach: Spell may effect two different Physical. +1 Reach: Spend a point of Mana, may increase stats beyond the allowed maximum",
        "source": "MtAw2 p150"
    },
    "knit": {
        "name": "Knit",
        "arcana": "life",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Medicine", "Survival"],
        "description": "Heal 2 bashing damage per Potency. +1 Reach: You can heal Personal Tilts such as Arm Wrack. +1 Reach: Can heal damage done by deprivation. +1 Reach: Reproduce the effect of night's rest. +1 Reach: Heal one lethal per Potency instead of 2 Bashing",
        "source": "MtAw2 p150"
    },
    "living_vessel": {
        "name": "Living Vessel",
        "arcana": "life",
        "level": 3,
        "secondary_arcana": "prime 3",
        "practice": "Weaving",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Academics", "Medicine", "Persuasion"],
        "description": "Prepare a subject under the purview of Life for the Imbue Item Attainment. The mage can use the Attainment to imbue any living subject",
        "source": "SoS 69"
    },
    "many_faces": {
        "name": "Many Faces",
        "arcana": "life",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Medicine", "Stealth", "Subterfuge"],
        "description": "Like Mutable Mask only the changes are real rather than an illusion. Poor vision or other senses can be restored. Missing organs and limbs can not be restored however. You may also rearrange the subjects Physical Attributes. Add Time 3: You can change physical age as well",
        "source": "MtAw2 p150"
    },
    "steal_life_force": {
        "name": "Steal Life Force",
        "arcana": "life",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Crafts", "Medicine", "Persuasion"],
        "description": "This spell is cast on a mage to alter his imbument process causing the item to damage the user. The item appears to function as normal but requires Life force to function. This item deals 1 point of Lethal damage for each point of Mana spent",
        "source": "SoS 72"
    },
    "transform_life": {
        "name": "Transform Life",
        "arcana": "life",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "withstand": "Stamina",
        "rote_skills": ["Animal Ken", "Science", "Survival"],
        "description": "Give life features normally belonging to other organisms. Gills, Claws, Senses, Etc. +2 Reach: The bestowed feature, if permanent, can be passed on to a creatures descendants",
        "source": "MtAw2 p150"
    },
    
    # Life 4
    "accelerate_growth": {
        "name": "Accelerate Growth",
        "arcana": "life",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Animal Ken", "Medicine", "Science"],
        "description": "Cause a lifeform to rapidly grow, at the end of the duration the subject will return to their actual age. If the subject exceeds its natural lifespan, it will die of old age. +1 Reach: When the spell ends the subject will rapidly de-age",
        "source": "MtAw2 p151"
    },
    "animal_minion": {
        "name": "Animal Minion",
        "arcana": "life",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Animal Ken", "Science", "Survival"],
        "description": "The mage takes complete bodily control of a subject. Difference in gait may be noticeable to those familiar with the subject. The mage's body will be inert while this spell is active. +1 Reach: Target behaves more normally",
        "source": "MtAw2 p151"
    },
    "life_force_assault": {
        "name": "Life-Force Assault",
        "arcana": "life",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "rote_skills": ["Brawl", "Intimidation", "Medicine"],
        "description": "Deal lethal damage. +1 Reach: Inflict an additional -2 penalty to any wound penalties the target might have. +1 Reach: Spend a point of Mana, deal aggravated damage",
        "source": "MtAw2 p152"
    },
    "living_grimoire": {
        "name": "Living Grimoire",
        "arcana": "life",
        "level": 4,
        "secondary_arcana": "prime 4",
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Total Arcanum dots used in the Rote + Stamina",
        "rote_skills": ["Crafts", "Medicine", "Occult"],
        "description": "The Mage scribes a single rote per casting of this spell onto a living being. Casting this spell constitutes as an act of Hubris against Understanding Wisdom",
        "source": "SoS 85"
    },
    "mend": {
        "name": "Mend",
        "arcana": "life",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Medicine", "Survival"],
        "description": "Heal 2 lethal wounds per Potency. +1 Reach: Can erase scars. +1 Reach: Can heal damage done by deprivation. +1 Reach: Reproduce the effect of night's rest. +1 Reach: Spend a point of Mana, can heal aggravated damage",
        "source": "MtAw2 p152"
    },
    "regeneration": {
        "name": "Regeneration",
        "arcana": "life",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Medicine", "Survival"],
        "description": "Cost: 1 Mana, restore lost organs or limbs",
        "source": "MtAw2 p152"
    },
    "shapechanging": {
        "name": "Shapechanging",
        "arcana": "life",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Stamina",
        "rote_skills": ["Animal Ken", "Science", "Survival"],
        "description": "Take on the form of another creature. Clothes and gear do not change with you. Instincts of the new form may need to be resisted with a Composure + Resolve roll. Add Matter 4: Gear changes with you to fit the new form. +1 Reach: Turn into a swarm of tiny creatures",
        "source": "MtAw2 p152"
    },
    
    # Life 5
    "create_life": {
        "name": "Create Life",
        "arcana": "life",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Medicine", "Science", "Survival"],
        "description": "Design and create any form of life you desire. If cast with finite duration life will disappear at the end of the spell, this may count as an Act of Hubris. Add Mind 5: Give your organism a true mind as appropriate to type",
        "source": "MtAw2 p153"
    },
    "contagion": {
        "name": "Contagion",
        "arcana": "life",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "rote_skills": ["Medicine", "Occult", "Science"],
        "description": "Create minor or life-threatening diseases. +1 Reach: Create a never before seen disease. This is likely to be an Act of Hubris as no creature in the world could have developed any defenses against it",
        "source": "MtAw2 p153"
    },
    "salt_the_earth": {
        "name": "Salt the Earth",
        "arcana": "life",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Duration",
        "rote_skills": ["Medicine", "Science", "Survival"],
        "description": "Destroy life-force in an area. This Creates an Extreme Environment equal to Potency. +1 Reach: Individual living things that survive, will still suffer an additional -1 to any wound penalties they might have",
        "source": "MtAw2 p153"
    }
}

MATTER_SPELLS = {
    # Matter 1
    "craftsmens_eye": {
        "name": "Craftsmen's Eye",
        "arcana": "matter",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Investigation", "Science"],
        "description": "Study an object for one turn to learn its intended function. +1 Reach: Learn how to use the studied object. This grants the 8-Again when using the object. +2 Reach: Learn all possible uses for an object. Add Fate 1: Name a task while casting the spell",
        "source": "MtAw2 p154"
    },
    "detect_substance": {
        "name": "Detect Substance",
        "arcana": "matter",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Investigation", "Science"],
        "description": "Become aware of a chosen type of substance in the area. Iron, A knife and My hunting Knife are all valid choices. Add Time 1: Determine if an object has been in the area. Add Forces 1: Search for a specific type of electronic information",
        "source": "MtAw2 p154"
    },
    "discern_composition": {
        "name": "Discern Composition",
        "arcana": "matter",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Investigation", "Science"],
        "description": "Become aware of an objects weight, density and the precise elements in its makeup. +1 Reach: Also become aware of any objects hidden within the studied object. +1 Reach: You know an object's structural weak points. Reduce Durability by spell Potency",
        "source": "MtAw2 p154"
    },
    "lodestone": {
        "name": "Lodestone",
        "arcana": "matter",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Larceny", "Science"],
        "description": "Choose a substance or type of object. Those objects will be drawn toward you or repelled away from you",
        "source": "MtAw2 p154"
    },
    "remote_control": {
        "name": "Remote Control",
        "arcana": "matter",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Drive", "Intimidation"],
        "description": "Control a mechanical object, to make it fulfill its function. +1 Reach: Perform more complex task while controlling the object",
        "source": "MtAw2 p155"
    },
    
    # Matter 2
    "alchemists_touch": {
        "name": "Alchemist's Touch",
        "arcana": "matter",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Survival", "Persuasion"],
        "description": "Choose a material, you become largely immune to its deleterious effects. The material cannot inflict bashing damage and lethal damage is reduced by spell Potency. +1 Reach: Choose an additional material to be protected against. +2 Reach: Your immune to both the bashing and lethal",
        "source": "MtAw2 p155"
    },
    "find_the_balance": {
        "name": "Find the Balance",
        "arcana": "matter",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Persuasion", "Science"],
        "description": "Improve the balance and heft of an item. This grants it the 9-Again quality. +1 Reach: Grant a tool the 8-Again quality instead",
        "source": "MtAw2 p155"
    },
    "hidden_hoard": {
        "name": "Hidden Hoard",
        "arcana": "matter",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Larceny", "Occult", "Subterfuge"],
        "description": "Make matter difficult to detect. Mundane attempts to locate automatically fail. Supernatural power enters a Clash of Wills",
        "source": "MtAw2 p156"
    },
    "machine_invisibility": {
        "name": "Machine Invisibility",
        "arcana": "matter",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Larceny", "Science", "Stealth"],
        "description": "Become invisible to mechanical sensors. Supernatural items enter a Clash of Wills. +1 Reach: This spell now also works on constructs animated with magic, like zombies and golems. This triggers a Clash of Wills",
        "source": "MtAw2 p156"
    },
    "shaping": {
        "name": "Shaping",
        "arcana": "matter",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Expression", "Persuasion"],
        "description": "Shape liquids and gases in any form you desire in defiance of gravity. +1 Reach: Can alter solids as well. +1 Reach: If creating or repairing an object in an extended action reduce its required successes by this spell's Potency. +2 Reach: The shaping can create an appropriate Environmental Tilt",
        "source": "MtAw2 p156"
    },
    
    # Matter 3
    "aegis": {
        "name": "Aegis",
        "arcana": "matter",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Crafts", "Science"],
        "description": "For each level of Potency grant an object one of the following: Raise/lower ballistic Armor by 1, raise/lower general Armor by 1, raise/lower Defense penalty by 1. +1 Reach: The armor becomes immune to the Armor-Piercing effect",
        "source": "MtAw2 p156"
    },
    "alter_conductivity": {
        "name": "Alter Conductivity",
        "arcana": "matter",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Computer", "Science", "Subterfuge"],
        "description": "Make an object more or less conductive to electricity. +1 Reach: Alter an objects conductivity to other forms of energy. Each additional type is an extra Reach",
        "source": "MtAw2 p156"
    },
    "alter_integrity": {
        "name": "Alter Integrity",
        "arcana": "matter",
        "level": 3,
        "practice": "Fraying or Perfecting",
        "primary_factor": "Potency",
        "withstand": "Durability",
        "rote_skills": ["Crafts", "Medicine", "Subterfuge"],
        "description": "Increase or decrease an objects Durability. +1 Reach: Instead of increasing Durability by 1 increase structure by 2. +2 Reach: The effect is lasting",
        "source": "MtAw2 p156"
    },
    "crucible": {
        "name": "Crucible",
        "arcana": "matter",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Occult", "Science"],
        "description": "Grant a tool the 8-Again for a number of turns. Valuable objects will have their Availability rating increased, this rating cannot become more than double the original rating. +1 Reach: Spend one point of Mana, The object gains the rote quality for a number of rolls",
        "source": "MtAw2 p157"
    },
    "hone_the_perfected_form": {
        "name": "Hone the Perfected Form",
        "arcana": "matter",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Persuasion", "Science"],
        "description": "Cost 1 Mana. The mage takes an ordinary metal (iron, gold, silver, mercury, copper, tin or lead) and transmutes it into its perfected metal. +2 Reach: The spell may Perfect another substance like Glass or Gemstones. Forces 3: May perfect fire",
        "source": "SoS 61"
    },
    "nigredo_and_albedo": {
        "name": "Nigredo and Albedo",
        "arcana": "matter",
        "level": 3,
        "practice": "Fraying or Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Brawl", "Medicine"],
        "description": "Repair or damage an objects Structure. +1 Reach: When damaging ignore durability",
        "source": "MtAw2 p157"
    },
    "shrink_and_grow": {
        "name": "Shrink and Grow",
        "arcana": "matter",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "withstand": "Durability",
        "rote_skills": ["Crafts", "Expression", "Science"],
        "description": "Increase or decrease an objects size. Add Life 3: Can be cast on living subjects, unwilling subjects may Withstand with Stamina",
        "source": "MtAw2 p157"
    },
    "spell_potion": {
        "name": "Spell Potion",
        "arcana": "matter",
        "level": 3,
        "secondary_arcana": "prime 2",
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Medicine", "Subterfuge"],
        "description": "Costs 1 Mana. Magically alters an ingested item, making it act as a storage vessel for another spell. Once the Ingested item has been primed for holding a mage may spend a Mana to cast any other spell on the item if it uses touch/self range",
        "source": "SoS 70"
    },
    "state_change": {
        "name": "State Change",
        "arcana": "matter",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "withstand": "Durability",
        "rote_skills": ["Crafts", "Persuasion", "Science"],
        "description": "Change material one step along the path from solid to liquid to gas. This does not cause any temperature change. +1 Reach: You may transform solids directly into gas and vice versa. Add Forces 3: You may transmute matter into plasma",
        "source": "MtAw2 p157"
    },
    "windstrike": {
        "name": "Windstrike",
        "arcana": "matter",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Brawl", "Crafts"],
        "description": "Deal bashing damage. +1 Reach: Create an appropriate Environmental Tilt",
        "source": "MtAw2 p157"
    },
    "wonderful_machine": {
        "name": "Wonderful Machine",
        "arcana": "matter",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Politics", "Science"],
        "description": "Integrate multiple machines into one another. Add Life 3: Machine properties can be grafted onto a living thing or vice versa",
        "source": "MtAw2 p157"
    },
    
    # Matter 4
    "endless_bounty": {
        "name": "Endless Bounty",
        "arcana": "matter",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Science", "Streetwise"],
        "description": "Never run out of small expendable items. Enchant a single item that contains a smaller expendable item. For the duration of the spell the expendable item never runs out. E.g.: Money in wallet, Bullets in magazine, Gas in car tank",
        "source": "SoS 66"
    },
    "forge_dumanium": {
        "name": "Forge Dumanium",
        "arcana": "matter",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Expression", "Persuasion"],
        "description": "Costs 1 Mana. Combine perfected metals into a single metal called Dumanium. The object is Durability 1 and holds 1 point of Mana. Weapons made from Dumanium can spend Mana to deal aggravated Damage for a single attack. +2 Reach: The Spell is Lasting",
        "source": "SoS 62"
    },
    "forge_sophis": {
        "name": "Forge Sophis",
        "arcana": "matter",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Occult", "Science"],
        "description": "Costs 1 Mana. Combine perfected metals into a single metal that scavenges Mana called Sophis. The object is Durability 1 and can hold 1 Mana. Potency increases this 1 for 1 for Durability and Mana. +2 Reach: The Spell is Lasting",
        "source": "SoS 62"
    },
    "forge_thaumium": {
        "name": "Forge Thaumium",
        "arcana": "matter",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Occult", "Survival"],
        "description": "Costs 1 Mana. Combine perfected metals to create Thaumium. The object is Durability 1 and holds 1 point of Mana which it spends to shield against Magic. +2 Reach: The Spell is Lasting. Other Arcanum 2: Thaumium can protect against other types of Magic",
        "source": "SoS 62"
    },
    "ghostwall": {
        "name": "Ghostwall",
        "arcana": "matter",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Occult", "Stealth"],
        "description": "Turn objects intangible. Add Death 3, Mind 3 or Spirit 3: The object may be shifted into the Twilight, attuned to the used Arcanum",
        "source": "MtAw2 p158"
    },
    "golem": {
        "name": "Golem",
        "arcana": "matter",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Animate a statue or other object. Add Death 4 or Spirit 4: A ghost or spirit may serve as the intelligence of the golem. Add Mind 5: Grant true intelligence see Psychic Genesis",
        "source": "MtAw2 p158"
    },
    "piercing_earth": {
        "name": "Piercing Earth",
        "arcana": "matter",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Brawl", "Crafts"],
        "description": "Deal lethal damage. +1 Reach: Create an appropriate Environmental Tilt. +1 Reach: Spend a point of Mana, deal aggravated damage",
        "source": "MtAw2 p158"
    },
    "transubstantiation": {
        "name": "Transubstantiation",
        "arcana": "matter",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Empathy", "Science"],
        "description": "Transform any type of matter into another type. +1 Reach: Transmute multiple substance into a single substance or vice versa. Add Life 4: Transform matter into living things or vice versa",
        "source": "MtAw2 p158"
    },
    
    # Matter 5
    "annihilate_matter": {
        "name": "Annihilate Matter",
        "arcana": "matter",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "withstand": "Durability",
        "rote_skills": ["Athletics", "Intimidation", "Science"],
        "description": "Destroy matter completely. +1 Reach: Spend a point of Mana, can now destroy magical objects as well",
        "source": "MtAw2 p158"
    },
    "ex_nihilo": {
        "name": "Ex Nihilo",
        "arcana": "matter",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Expression", "Science"],
        "description": "Create an object or relatively uncomplicated tool out of nothing. +1 Reach: Create a complex machine or electronic device, like a car or smartphone",
        "source": "MtAw2 p158"
    },
    "self_repairing_machine": {
        "name": "Self-Repairing Machine",
        "arcana": "matter",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Medicine", "Occult"],
        "description": "Cause a machine to repair Potency in Structure per day. +1 Reach: The machine heals every hour. +2 Reach: The machine heals every 15 minutes",
        "source": "MtAw2 p159"
    }
}

MIND_SPELLS = {
    # Mind 1
    "know_nature": {
        "name": "Know Nature",
        "arcana": "mind",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Science", "Subterfuge"],
        "description": "Determine a subject's Virtue, Vice and Mental and Social Attribute levels. +1 Reach: Also determine Aspirations and Obsessions",
        "source": "MtAw2 p159"
    },
    "mental_scan": {
        "name": "Mental Scan",
        "arcana": "mind",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Empathy", "Investigation", "Occult"],
        "description": "Ask storyteller questions about a subject's mental or emotional state. +1 Reach: Read surface thoughts for snippets of a subject's current ideas or words and phrases before they are actually spoken",
        "source": "MtAw2 p159"
    },
    "one_mind_two_thoughts": {
        "name": "One Mind, Two Thoughts",
        "arcana": "mind",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Expression", "Science"],
        "description": "Perform two Mental or Social extended tasks at the same time. Neither can be a purely Physical task. +1 Reach: May perform two Mental instant tasks at the same time. +2 Reach: If in the Astral Realms one of the actions may be Physical",
        "source": "MtAw2 p159"
    },
    "perfect_recall": {
        "name": "Perfect Recall",
        "arcana": "mind",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Expression", "Investigation"],
        "description": "Recall old memories with perfect accuracy",
        "source": "MtAw2 p160"
    },
    
    # Mind 2
    "alter_mental_pattern": {
        "name": "Alter Mental Pattern",
        "arcana": "mind",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Potency",
        "rote_skills": ["Science", "Stealth", "Subterfuge"],
        "description": "Add to subterfuge rolls. Supernatural powers that read surface thoughts or emotions provoke a Clash of Wills",
        "source": "MtAw2 p160"
    },
    "dream_reaching": {
        "name": "Dream Reaching",
        "arcana": "mind",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Empathy", "Medicine", "Persuasion"],
        "description": "Enter a subject's dream. You can influence but not take part in the dream. Cast on self to be able to remember your own dreams. +1 Reach: You can become an active part of the dream. Cast on self induces lucid dreaming",
        "source": "MtAw2 p160"
    },
    "emotional_urging": {
        "name": "Emotional Urging",
        "arcana": "mind",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Empathy", "Intimidation", "Subterfuge"],
        "description": "Open or close a subject's doors",
        "source": "MtAw2 p160"
    },
    "first_impressions": {
        "name": "First Impressions",
        "arcana": "mind",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Crafts", "Socialize", "Subterfuge"],
        "description": "Raise or lower the first impression",
        "source": "MtAw2 p160"
    },
    "incognito_presence": {
        "name": "Incognito Presence",
        "arcana": "mind",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Empathy", "Stealth", "Subterfuge"],
        "description": "Costs 1 Mana. The Mage hides the Subject's Psychic Presence which Prevents people from remembering their presence or looking their way. Active attempts to do so with supernatural abilities provoke a Clash of Wills",
        "source": "MtAw2 p160"
    },
    "memory_hole": {
        "name": "Memory Hole",
        "arcana": "mind",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Medicine", "Subterfuge"],
        "description": "Hide a specific memory forgetting it completely for the duration of the spell. One memory per Potency",
        "source": "MtAw2 p160"
    },
    "mental_shield": {
        "name": "Mental Shield",
        "arcana": "mind",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Intimidation", "Survival"],
        "description": "Protects the Subject from Mental Attacks, Goetia Powers, Influences or Manifestations that target them. +1 Reach: Also Protects from Physical attacks of Goetia",
        "source": "MtAw2 p160"
    },
    "narcissus_mirror": {
        "name": "Narcissus' Mirror",
        "arcana": "mind",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Intimidation", "Occult", "Subterfuge"],
        "description": "The mage can reflect the mental and emotional effects of a Nimbus tilt back onto its source. Whenever the Mage is subjected to a tilt that affects a Mental or Social trait this spell provokes a Clash of Wills. Substitute Life 2: This Spell affects Nimbus Tilts relating to Physical Traits",
        "source": "SoS 94"
    },
    "psychic_domination": {
        "name": "Psychic Domination",
        "arcana": "mind",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Expression", "Intimidation", "Subterfuge"],
        "description": "Send one word commands to a subject that they are compelled to act upon, even against their will. +1 Reach: take control of a subject, forcing him to take actions against their will. +1 Reach: Force the subject to take an additional task",
        "source": "MtAw2 p161"
    },
    "ritual_focus": {
        "name": "Ritual Focus",
        "arcana": "mind",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Empathy", "Leadership", "Persuasion"],
        "description": "A Variant on Telepathy linking a Mage and his Subjects allowing him to guide them as they work in unison on a particular spell. Must have Scale to affect every other Awakened participant in Ritual. Secondary Actors in ritual add Potency to dice pool",
        "source": "SoS 55"
    },
    "soul_windows": {
        "name": "Soul Windows",
        "arcana": "mind",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Empathy", "Investigation", "Stealth"],
        "description": "By Splitting their senses a mage may view whats happening around their Soul Stone 360 degrees or hears the sounds in its vicinity. This doesn't require sympathetic range. Add Forces 2: The mage may project their voice through the stone. +1 Reach: The mage experiences the Stone's surroundings with all their Senses",
        "source": "SoS 90"
    },
    "telepathy": {
        "name": "Telepathy",
        "arcana": "mind",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Crafts", "Empathy", "Socialize"],
        "description": "Surface thoughts of the subjects play out in the each others minds. This may grant a bonus or penalty between the subjects. A deliberate message may be send along the link. +1 Reach: Only thoughts that the originating subject wants to share are shared. +1 Reach: All subjects have the ability to send and receive thoughts",
        "source": "MtAw2 p161"
    },
    
    # Mind 3
    "astral_grimoire": {
        "name": "Astral Grimoire",
        "arcana": "mind",
        "level": 3,
        "secondary_arcana": "prime 1",
        "practice": "Weaving",
        "primary_factor": "Potency",
        "withstand": "Total Arcanum dots used in rote",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Costs 1 Mana. Scribe a Rote within ones own Oneiros, these can be cast from the Grimoire without needing to meditate to the Astral. +1 Reach: The Mage can scribe the grimoire within the Temenos. +1 Reach: For 1 point of Mana the Spell's duration is lasting",
        "source": "SoS 85"
    },
    "augment_mind": {
        "name": "Augment Mind",
        "arcana": "mind",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Expression", "Survival"],
        "description": "Increase a Mental or Social Attribute by Potency, up to normal limits. +1 Reach: Divide increase between an additional Attribute. +2 Reach: for 1 Mana, go above normal limits",
        "source": "MtAw2 p161"
    },
    "befuddle": {
        "name": "Befuddle",
        "arcana": "mind",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "withstand": "Composure or Resolve",
        "rote_skills": ["Intimidation", "Persuasion", "Science"],
        "description": "Lower a Mental or Social Attributes. One Potency equal one dot to a minimum of one. +1 Reach: May lower an additional Attribute per reach, dividing Potency among the options",
        "source": "MtAw2 p163"
    },
    "broken_relinquishment": {
        "name": "Broken Relinquishment",
        "arcana": "mind",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Intimidation", "Occult", "Subterfuge"],
        "description": "This spell creates a breaking point for the subject as a way to relinquish spells without spending a willpower dot. The next act of hubris, breaking point or genre equivalent by a subject of this spell suffers penalty by Potency. +1 Reach: The Subject of this spell immediately suffers a breaking point",
        "source": "SoS 73"
    },
    "clear_thoughts": {
        "name": "Clear Thoughts",
        "arcana": "mind",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Empathy", "Intimidation", "Persuasion"],
        "description": "Suppress a Mental Condition or Tilt per Potency, for the Duration. Can't affect Paradox Conditions; those cause by the supernatural provoke a Clash of Wills. +1 Reach: subject gains 1 Willpower. +2 Reach: effect is lasting",
        "source": "MtAw2 p161"
    },
    "enhance_skill": {
        "name": "Enhance Skill",
        "arcana": "mind",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Expression", "Survival"],
        "description": "Increase a Skill with already at least one rank by Potency, for the Duration, up to their normal limits. +1 Reach: Divide increase between an additional Skill. +2 Reach: for 1 Mana, go above normal limits",
        "source": "MtAw2 p161"
    },
    "give_me_that": {
        "name": "Give Me That",
        "arcana": "mind",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Crafts", "Empathy", "Persuasion"],
        "description": "The subject item evokes a concept of ownership. Those who do not Withstand the spell gain the Persistent Condition: Obsession with the object as their focus. Space 3: Individuals with the Obsessed Condition to the object also gain a Strong sympathetic link to it",
        "source": "SoS 66"
    },
    "goetic_summons": {
        "name": "Goetic Summons",
        "arcana": "mind",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "withstand": "Rank",
        "rote_skills": ["Persuasion", "Socialize", "Occult"],
        "description": "Call the nearest Goetia; one personally known, specified by type of Resonance, or the nearest generally. Add Spirit or Death 2: it gains the Materialized Condition for the duration. +1 Reach: Also creates the Open Condition. +1 Reach: May give it a one-word command",
        "source": "MtAw2 p162"
    },
    "imposter": {
        "name": "Imposter",
        "arcana": "mind",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Persuasion", "Stealth", "Subterfuge"],
        "description": "Cause the subject to believe the caster is someone else. Manipulation + Subterfuge every minute if mimicking a specific person. Can't replicate Social Merits; any Doors opened benefit the assumed identity",
        "source": "MtAw2 p162"
    },
    "psychic_assault": {
        "name": "Psychic Assault",
        "arcana": "mind",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Intimidation", "Medicine"],
        "description": "Deal Bashing equal to Potency, mimicking a stroke. +1 Reach: give target -1 to Mental rolls (may stack 3 times)",
        "source": "MtAw2 p162"
    },
    "sleep_of_the_just": {
        "name": "Sleep of the Just",
        "arcana": "mind",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Academics", "Athletics", "Occult"],
        "description": "Control sleep cycle and dreams. Anything else entering or influencing dreams provokes Clash of Wills",
        "source": "MtAw2 p162"
    },
    "supernal_translation": {
        "name": "Supernal Translation",
        "arcana": "mind",
        "level": 3,
        "secondary_arcana": "prime 3",
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Empathy", "Expression", "Occult"],
        "description": "Allows the subject to comprehend and translate High Speech as they hear or read it as if they had up Mage Sight. Does not allow them to Speak or Write it back and is still subject to Dissonance and Quiescence",
        "source": "SoS 28"
    },
    "read_the_depths": {
        "name": "Read the Depths",
        "arcana": "mind",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Empathy", "Investigation", "Medicine"],
        "description": "Read memories and ideas from target's subconscious. +1 Reach: modify one of the memories read, for the Duration",
        "source": "MtAw2 p162"
    },
    "universal_language": {
        "name": "Universal Language",
        "arcana": "mind",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Investigation", "Persuasion"],
        "description": "Target can understand and translate any language they are able to perceive: spoken, written, symbols, encoded signals, body language, hand symbols, or thoughts. Does not allow non-Awakened to understand High Speech",
        "source": "MtAw2 p162"
    },
    
    # Mind 4
    "haunted_grimoire": {
        "name": "Haunted Grimoire",
        "arcana": "mind",
        "level": 4,
        "secondary_arcana": "prime 1",
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Total Arcanum dots of Rote + Rank",
        "rote_skills": ["Crafts", "Intimidation", "Occult"],
        "description": "Costs 1 Mana. The Mage binds a Goetia to a grimoire, writing its essence into the vessel's pattern. The Grimoire gains the Open and Resonant Conditions. When cast the spell is increased by the Goetia Rank for Primary Factor. This spell is a Wisdom Sin against Understanding",
        "source": "SoS 86"
    },
    "possession": {
        "name": "Possession",
        "arcana": "mind",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Medicine", "Persuasion", "Subterfuge"],
        "description": "Can possess the subject inflicting the Possessed Condition",
        "source": "MtAw2 p165"
    },
    "gain_skill": {
        "name": "Gain Skill",
        "arcana": "mind",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Expression", "Science"],
        "description": "Increase a Skill by Potency. This cannot go above the normal maximum. +1 Reach: Divide the increase between an additional Skill. +1 Reach: for 1 Mana, go above normal limits",
        "source": "MtAw2 p163"
    },
    "goetic_evocation": {
        "name": "Goetic Evocation",
        "arcana": "mind",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Rank of Entity",
        "rote_skills": ["Intimidation", "Occult", "Persuasion"],
        "description": "May convert pieces of a persons Psyche from a soul stone into a Goetia. +2 Reach: The Mage may extract the Goetia directly into his own Oneiros",
        "source": "SoS 90"
    },
    "hallucination": {
        "name": "Hallucination",
        "arcana": "mind",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Academics", "Persuasion", "Subterfuge"],
        "description": "Create an illusion that affects all senses but touch. +1 Reach: The illusion can now be touched by the subject. It cannot harm or attack",
        "source": "MtAw2 p163"
    },
    "mind_flay": {
        "name": "Mind Flay",
        "arcana": "mind",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "rote_skills": ["Expression", "Intimidation", "Science"],
        "description": "Deal lethal damage. +1 Reach: Cause Insane Tilt. +2 Reach: Spend a point of Mana, deal aggravated damage",
        "source": "MtAw2 p164"
    },
    "psychic_projection": {
        "name": "Psychic Projection",
        "arcana": "mind",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Academics", "Occult", "Socialize"],
        "description": "Astral project into Twilight or into somebody's dreams. Add Spirit 2: May project into the Shadow. Withstand is Gauntlet rating",
        "source": "MtAw2 p164"
    },
    "psychic_reprogramming": {
        "name": "Psychic Reprogramming",
        "arcana": "mind",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Intimidation", "Medicine", "Persuasion"],
        "description": "For each point of Potency change one of the following: Virtue, Vice, Short-Term Aspiration, Long-Term Aspiration, Obsession, a non-Physical Persistent Condition, or may move one dot between two Social Skills, or between two Mental Skills. +1 Reach: May also move between two Social Attributes, or two Mental Attributes",
        "source": "MtAw2 p164"
    },
    "scribe_daimonomikon": {
        "name": "Scribe Daimonomikon",
        "arcana": "mind",
        "level": 4,
        "secondary_arcana": "prime 1",
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Rank of Attainment + (10 - Caster's Gnosis)",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Cost 1 Mana. Scribe a Daimonomikon for the Mage's Legacy. A Mage must be of Gnosis 2 or above to cast this. Anyone initiated into a Legacy via a Daimonomikon must spend 1 Arcane Experience. These serve as a sympathetic Yantra worth +2 Dice for members of the inscribed Legacy",
        "source": "SoS 87"
    },
    "terrorize": {
        "name": "Terrorize",
        "arcana": "mind",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Expression", "Intimidation", "Medicine"],
        "description": "Cause the Insensate Tilt for the duration or until it's resolved. +1 Reach: Inflict Broken Condition instead",
        "source": "MtAw2 p164"
    },
    
    # Mind 5
    "amorality": {
        "name": "Amorality",
        "arcana": "mind",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Crafts", "Empathy", "Expression"],
        "description": "Remove Virtue or Vice. Without Virtue the subject regains two Willpower for indulging Vice. Without Vice the subject cannot engage in any activity that would be a breaking point or Act of Hubris",
        "source": "MtAw2 p164"
    },
    "no_exit": {
        "name": "No Exit",
        "arcana": "mind",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Expression", "Persuasion", "Science"],
        "description": "For the duration of the spell the subject is in a catatonic state. Reading of the subjects mind or memory reveals this spell",
        "source": "MtAw2 p164"
    },
    "mind_wipe": {
        "name": "Mind Wipe",
        "arcana": "mind",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "withstand": "Resolve",
        "rote_skills": ["Academics", "Intimidation", "Occult"],
        "description": "Remove large portions of the subjects memories, inflicts the Amnesia Tilt for the duration of the spell. You can affect one month of time per level Potency. You can specify what portions are forgotten. +1 Reach: May specify what memories are erased. +2 Reach: The effect is Lasting",
        "source": "MtAw2 p164"
    },
    "psychic_genesis": {
        "name": "Psychic Genesis",
        "arcana": "mind",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Expression", "Science"],
        "description": "Create a self-aware intelligence. This is a Rank 1 Goetia in Twilight. +1 Reach: The entity works as a sleepwalker for the purposes of assisting ritual casting. +1 Reach: For one Mana, the rank is 2",
        "source": "MtAw2 p165"
    },
    "social_networking": {
        "name": "Social Networking",
        "arcana": "mind",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "rote_skills": ["Persuasion", "Politics", "Socialize"],
        "description": "For every level of Potency, gain one dot in one of the following Merits: Allies, Contacts or Status",
        "source": "MtAw2 p165"
    }
}

PRIME_SPELLS = {
    # Prime 1
    "dispel_magic": {
        "name": "Dispel Magic",
        "arcana": "prime",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "withstand": "Arcanum rating of the subject spell's caster",
        "rote_skills": ["Athletics", "Intimidation", "Occult"],
        "description": "Temporarily suppress or destroy an active spell. Add Fate 1: Selectively suppress spell. +2 Reach: Make the effect Lasting",
        "source": "MtAw2 p165"
    },
    "nimbus_tuning": {
        "name": "Nimbus Tuning",
        "arcana": "prime",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Investigation", "Occult"],
        "description": "The mage can tune in more attentively to any Signature Nimbus he scrutinizes with Focused Mage sight. For Each potency learn one of the following: Gnosis, Wisdom, Virtue/Vice, An Act of Hubris resulting from cast magic, An Obsession related to the remaining Magic, Whether the Magic resulted in Paradox",
        "source": "SoS 94"
    },
    "pierce_deception": {
        "name": "Pierce Deception",
        "arcana": "prime",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Investigation", "Medicine", "Occult"],
        "description": "See through falsehoods magical and mundane. +1 Reach: Get a sense of the actual truth",
        "source": "MtAw2 p165"
    },
    "sacred_geometry": {
        "name": "Sacred Geometry",
        "arcana": "prime",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Occult", "Survival"],
        "description": "Reveal ley lines and nodes. +1 Reach: Reveal Hallows. Add Death 1 or Spirit 1: See Avernian Gates or Loci as well",
        "source": "MtAw2 p166"
    },
    "scribe_grimoire": {
        "name": "Scribe Grimoire",
        "arcana": "prime",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "withstand": "Total Arcanum dots of all Arcana used in the spell being scribed",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Create a Grimoire full of Rotes or transcribe it from one medium to another. +1 Reach: Make the Grimoire Lasting. Add Forces 2: Transcribe the grimoire without needed equipment",
        "source": "MtAw2 p166, SoS p83"
    },
    "shared_mage_sight": {
        "name": "Shared Mage Sight",
        "arcana": "prime",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Expression", "Investigation", "Occult"],
        "description": "Cost 1+ Mana per Arcanum per subject. Share your Mage sight with another Mage. Prime 4: Can be used on a Sleepwalker under the effects of Apocalypse. Other Arcanum 1: 1 Mana per Arcanum May add or substitute Prime for another Arcanum",
        "source": "SoS 28"
    },
    "supernal_signature": {
        "name": "Supernal Signature",
        "arcana": "prime",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "rote_skills": ["Expression", "Intimidation", "Politics"],
        "description": "The Mage flares her Immediate Nimbus to imprint her signature on a subject. The signature reflects her Shadow Name and lasts for the Duration of the spell. Anyone who Studies the nimbus under focused mage sight can sense the details of the Nimbus and the Casters Supernal Identity",
        "source": "SoS 93"
    },
    "supernal_vision": {
        "name": "Supernal Vision",
        "arcana": "prime",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Occult", "Survival"],
        "description": "Perceive the Supernal properties of a subject. +1 Reach: Perceive the non-Supernal magical properties of a subject",
        "source": "MtAw2 p166"
    },
    "word_of_command": {
        "name": "Word of Command",
        "arcana": "prime",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "rote_skills": ["Craft", "Occult", "Persuasion"],
        "description": "Bypass triggers to activate magical effects. Add Any Other Arcanum 1: Add another Arcanum to activate magical effects and objects created by other sources of power",
        "source": "MtAw2 p166"
    },
    
    # Prime 2
    "as_above_so_below": {
        "name": "As Above, So Below",
        "arcana": "prime",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Occult", "Politics"],
        "description": "Empower Yantras with 9-Again on spellcasting rolls. +1 Reach: Make it 8-again",
        "source": "MtAw2 p166"
    },
    "cloak_nimbus": {
        "name": "Cloak Nimbus",
        "arcana": "prime",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Politics", "Stealth", "Subterfuge"],
        "description": "Veil Nimbus and emotional state of auras. Attempts to see are subject to a Clash of Wills. Immediate Nimbus does not flare unless the caster chooses to. Signature Nimbus viewed by Mage Sight provokes Clash of Wills. +1 Reach: Make your Nimbus appear lesser",
        "source": "MtAw2 p167"
    },
    "fractured_grimoire": {
        "name": "Fractured Grimoire",
        "arcana": "prime",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Investigation", "Occult"],
        "description": "Costs 1 Mana. The mage copies one whole grimoire into two or more disparate parts that individually mean nothing. Only someone with all parts may use the rotes within the Grimoire. +1 Reach: The mage may fracture the Grimoire into as many pieces as she wants",
        "source": "SoS 84"
    },
    "invisible_runes": {
        "name": "Invisible Runes",
        "arcana": "prime",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Intimidation", "Persuasion"],
        "description": "Leave message in High Speech only visible to Mage Sight. Alteration or overwriting of these messages provokes a Clash of Wills",
        "source": "MtAw2 p167"
    },
    "light_under_a_bushel": {
        "name": "Light Under a Bushel",
        "arcana": "prime",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Investigation", "Subterfuge"],
        "description": "Adds Mages Potency to the number of rolls before Mages Nimbus leaks into a mystery",
        "source": "SoS 28"
    },
    "nimbus_forgery": {
        "name": "Nimbus Forgery",
        "arcana": "prime",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Larceny", "Subterfuge"],
        "description": "Once a Mage has scrutinized an Immediate or Signature Nimbus with Focused mage sight she may cast this spell to disguise her own Nimbus as the Scrutinized one. Any attempt to pierce the deception results with a Clash of Wills. +1 Reach: The Mage Forges all three types of nimbus with one casting",
        "source": "SoS 94"
    },
    "path_to_jerusalem": {
        "name": "Path to Jerusalem",
        "arcana": "prime",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Potency",
        "withstand": "Opacity",
        "rote_skills": ["Expression", "Larceny", "Subterfuge"],
        "description": "Add Spell's Potency to the Opacity of the Subject Mystery. +1 Reach: Every Reach spent allows mage to plant 1 falsehood of Surface or Deep information. Recognizing this is a Clash of Wills when focused on with Focused Mage Sight",
        "source": "SoS 28"
    },
    "supernal_veil": {
        "name": "Supernal Veil",
        "arcana": "prime",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Subterfuge", "Survival"],
        "description": "Veil supernatural phenomenon including spells. Peripheral Mage Sight will fail to detect, active attempts cause a Clash of Wills",
        "source": "MtAw2 p168"
    },
    "sustain_nimbus": {
        "name": "Sustain Nimbus",
        "arcana": "prime",
        "level": 2,
        "secondary_arcana": "time 1",
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Investigation", "Survival"],
        "description": "The mage casts this on a Signature Nimbus she's studied under Focused Mage Sight. Rather than fading like normal the Nimbus persists for the Duration of the spell. Once the Duration expires it fades at its usual rate. +2 Reach: Duration is Lasting",
        "source": "SoS 93"
    },
    "wards_and_signs": {
        "name": "Wards and Signs",
        "arcana": "prime",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Intimidation", "Occult", "Survival"],
        "description": "When subject is target of a spell apply Potency as Withstand rating. Spells used near but not directly at the target are not Withstood by this spell",
        "source": "MtAw2 p168"
    },
    "words_of_truth": {
        "name": "Words of Truth",
        "arcana": "prime",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Expression", "Intimidation", "Persuasion"],
        "description": "All subjects of the spell can hear and understand the caster regardless of distance, noise or language barriers. Subjects feel what the mage says is true, but this effect only works on statements the mage knows are true. May remove one Door or improve impression level by one per Potency",
        "source": "MtAw2 p168"
    },
    
    # Prime 3
    "aetheric_winds": {
        "name": "Aetheric Winds",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Expression", "Occult"],
        "description": "Attack with shrieking aetheric wind. +1 Reach: Create Heavy Winds Environmental Tilt. +1 Reach: Destroy target's Mana instead of dealing damage",
        "source": "MtAw2 p168"
    },
    "camera_obscura": {
        "name": "Camera Obscura",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Craft", "Expression", "Science"],
        "description": "Cost 1 Mana. This spell enchants a Camera, video recorder or similar device and allows it to record Supernal Energies allowing a mage to study the recordings using Active and Focused mage sight. +2 Reach: 1 Mana to make the recordings Lasting",
        "source": "SoS 28"
    },
    "channel_mana": {
        "name": "Channel Mana",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Occult", "Politics", "Socialize"],
        "description": "Move Mana equal to Potency between vessels (mages, Hallows, etc). This cannot exceed Gnosis-derived the Mana per turn limit though. +1 Reach: Ignore Mana per turn limit for this spell",
        "source": "MtAw2 p168"
    },
    "cleanse_pattern": {
        "name": "Cleanse Pattern",
        "arcana": "prime",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "rote_skills": ["Investigation", "Occult", "Stealth"],
        "description": "Remove the dramatic failure of a focused Mage Sight Revelation. This spell will also remove a mage's Signature Nimbus from the subject",
        "source": "MtAw2 p168"
    },
    "display_of_power": {
        "name": "Display of Power",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Brawl", "Occult", "Socialize"],
        "description": "Imagos become visible to all forms of Active Mage Sight. +2 Reach: For one Mana all attempts to Counterspell gain the Rote Quality. Add Fate 1: Make clauses of fae Contracts visible",
        "source": "MtAw2 p168, DE2 379"
    },
    "ephemeral_enchantment": {
        "name": "Ephemeral Enchantment",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Occult", "Weaponry"],
        "description": "Subject becomes solid to any and all Twilight entities. +2 Reach: For one Mana, if the subject is a weapon it will inflict aggravated damage to one specified Twilight entity. Every additional entity costs one Mana",
        "source": "MtAw2 p169"
    },
    "geomancy": {
        "name": "Geomancy",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Expression", "Occult"],
        "description": "Move ley lines within the area of effect. May also change the Resonance Keyword of a Node",
        "source": "MtAw2 p169"
    },
    "imbue_room": {
        "name": "Imbue Room",
        "arcana": "prime",
        "level": 3,
        "secondary_arcana": "space 3",
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Larceny", "Occult", "Science"],
        "description": "Allows a Mage to prepare a room or space for the Imbue Item attainment. Unlike an object the room does not have Mana storage so all Mana must be spent by the user of the Imbued room",
        "source": "SoS 69"
    },
    "mana_battery": {
        "name": "Mana Battery",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Occult", "Subterfuge"],
        "description": "Allows a Mage to prime an item to store Mana. The mage casts the spell on a subject prior to using the Attainment Imbue Item. The subject is Primed to accept a Mana pool but not a spell. An Item created this way can be used to cast spells without using a Mages own Mana",
        "source": "SoS 70"
    },
    "platonic_form": {
        "name": "Platonic Form",
        "arcana": "prime",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Crafts", "Expression"],
        "description": "Cost 1+ Mana. Create a simple Tass object or tool of Size 5 or less from Mana. Durability is 1 and contains one Mana. Potency may be allocated to increase Durability, increase Mana capacity, or if a tool add equipment bonus. Add Forces 3: The construct is not obviously magical",
        "source": "MtAw2 p169"
    },
    "primary_subject": {
        "name": "Primary Subject",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Intimidation", "Occult", "Subterfuge"],
        "description": "Cost 1+ Mana. This spell alters the imbument process, creating an item that will always target the user. The subject of the spell must be a mage",
        "source": "SoS 72"
    },
    "reveal_marks": {
        "name": "Reveal Marks",
        "arcana": "prime",
        "level": 3,
        "secondary_arcana": "time 2",
        "practice": "Weaving",
        "primary_factor": "Potency",
        "rote_skills": ["Crafts", "Expression", "Investigation"],
        "description": "You may discern all signature Nimbuses associated with the Subject. This spell reduces the difficulty to Focused Mage Sight to scrutinize the subject for a signature Nimbus and reveals all Nimbuses associated with the subject. Add Potency as bonus die to reveal them",
        "source": "SoS 74"
    },
    "scribe_palimpsest": {
        "name": "Scribe Palimpsest",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Potency",
        "withstand": "Rotes Total Arcanum dots +1",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Costs 1 Mana. Like Scribe Grimoire this spell gives physical form to a single rote's symbols using a Grimoire that has had its contents erased. The Storyteller chooses one Arcanum when the character casts this spell. +1 Reach: For 1 point of Mana, the spell's Duration is Lasting",
        "source": "SoS 84"
    },
    "spirit_vessel": {
        "name": "Spirit Vessel",
        "arcana": "prime",
        "level": 3,
        "secondary_arcana": "spirit 3",
        "practice": "Weaving",
        "primary_factor": "Duration",
        "withstand": "Resistance",
        "rote_skills": ["Academics", "Intimidation", "Occult"],
        "description": "Prepare a Spirit for the Imbue Item Attainment. The mage must either cast the spell through the Gauntlet or the spirit must be Manifested. The subject automatically withstands the casting",
        "source": "SoS 69"
    },
    "steal_mana": {
        "name": "Steal Mana",
        "arcana": "prime",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Duration",
        "withstand": "Stamina",
        "rote_skills": ["Expression", "Occult", "Subterfuge"],
        "description": "Costs 1 Mana. This spell alters the imbument process resulting in an item that siphons its users Mana. When under this spell when Imbuing an item you may set a Mana capacity to the item, instead of imbuing it with that much Mana it steals it from its user",
        "source": "SoS 72"
    },
    "stealing_fire": {
        "name": "Stealing Fire",
        "arcana": "prime",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Expression", "Larceny", "Persuasion"],
        "description": "Temporarily turn Sleeper into a Sleepwalker. Breaking points from magic will hit only when the spell expires",
        "source": "MtAw2 p168"
    },
    "stored_spell": {
        "name": "Stored Spell",
        "arcana": "prime",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Occult", "Subterfuge"],
        "description": "A Mage may make an item capable of holding a spell until later activation similar to the Attainment Imbue Item. Once this spell is in effect a mage may spend a Mana to cast any other spell on the item that uses touch/self range, which is contained and unactivated",
        "source": "SoS 70"
    },
    
    # Prime 4
    "apocalypse": {
        "name": "Apocalypse",
        "arcana": "prime",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Occult", "Persuasion", "Socialize"],
        "description": "Grant a Sleeper the ability to see what a Mage sees. +1 Reach and Add Any Other Arcanum 1: Add the Arcanum to the granted Sight",
        "source": "MtAw2 p169"
    },
    "celestial_fire": {
        "name": "Celestial Fire",
        "arcana": "prime",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Expression", "Occult"],
        "description": "Attack spell inflict Lethal equal to Potency. +1 Reach: Spell ignites flammable object in the scene. +1 Reach: For one Mana, spell deals aggravated damage. +1 Reach: May destroy target's Mana instead of dealing damage",
        "source": "MtAw2 p170"
    },
    "destroy_tass": {
        "name": "Destroy Tass",
        "arcana": "prime",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "withstand": "Durability",
        "rote_skills": ["Brawl", "Intimidation", "Occult"],
        "description": "Successful casting destroys Tass. Mana from the tass is not destroyed but released into the world likely to the nearest Hallow",
        "source": "MtAw2 p170"
    },
    "hallow_dance": {
        "name": "Hallow Dance",
        "arcana": "prime",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Hallow Rating",
        "rote_skills": ["Expression", "Occult", "Survival"],
        "description": "Suppress an active Hallow or awaken a dormant one. Rousing requires Potency equal to the Hallow's rating. Dampening reduces the Hallow's dot rating by Potency, if it falls to zero or less the Hallow is rendered dormant. +2 Reach: For one point of Mana the effect is Lasting",
        "source": "MtAw2 p170"
    },
    "primal_transfer": {
        "name": "Primal Transfer",
        "arcana": "prime",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Crafts", "Empathy", "Subterfuge"],
        "description": "This allows a Mage to transfer spell control of a spell they've cast to another mage. The spell transfers Spells up to Potency from Caster to Subject. Once the Duration ends control returns to the Caster. +2 Reach: If Primal Transfer is Imbued into an item with this effect spell control is passed to the user",
        "source": "SoS 71"
    },
    "scribe_daimonomikon_prime": {
        "name": "Scribe Daimonomikon",
        "arcana": "prime",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Rank of Attainment + (10 - Caster's Gnosis)",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Cost 1 Mana. Scribe a Daimonomikon for the Mage's Legacy. A Mage must be of Gnosis 2 or above to cast this. Anyone initiated into a Legacy via a Daimonomikon must spend 1 Arcane Experience. These serve as a sympathetic Yantra worth +2 Dice for members of the inscribed Legacy. +1 Reach: For 1 Mana, the Spell's Duration is Lasting",
        "source": "SoS 87"
    },
    "supernal_dispellation": {
        "name": "Supernal Dispellation",
        "arcana": "prime",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "withstand": "Arcanum rating of the subject spell's caster",
        "rote_skills": ["Athletics", "Intimidation", "Occult"],
        "description": "Success suppresses target spell for Supernal Dispellations Duration. Add Fate 1: Selectively suppress spell. +2 Reach: Make the effect Lasting",
        "source": "MtAw2 p170"
    },
    "transfer_soul_stone": {
        "name": "Transfer Soul Stone",
        "arcana": "prime",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Occult", "Persuasion"],
        "description": "May transfer a Soul Stone from one object to another of size 2 or below. +2 Reach: This spell is Lasting",
        "source": "SoS 91"
    },
    
    # Prime 5
    "blasphemy": {
        "name": "Blasphemy",
        "arcana": "prime",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "withstand": "Hallow Rating, if applicable",
        "rote_skills": ["Athletics", "Occult", "Survival"],
        "description": "Sever the connection to the Supernal in an area. +2 Reach: Make the effect Lasting",
        "source": "MtAw2 p170"
    },
    "create_truth": {
        "name": "Create Truth",
        "arcana": "prime",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "withstand": "Hallow Rating",
        "rote_skills": ["Expression", "Occult", "Persuasion"],
        "description": "Cost 5 Mana per Potency. Create Hallow with rating equal to Potency, Hallows cannot have a rating above 5. +2 Reach: For 5 Mana the effect is Lasting",
        "source": "MtAw2 p170"
    },
    "eidolon": {
        "name": "Eidolon",
        "arcana": "prime",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Crafts", "Occult"],
        "description": "Like Platonic Form but can create animate Tass. May spend Potency on an additional effect: grant the mage a dot of the Retainer Merit. Construct will obey its owner's command. Add Forces 3: The construct is not obviously magical. Add Mind 5: The construct may be given a mind of its own",
        "source": "MtAw2 p171"
    },
    "forge_purpose": {
        "name": "Forge Purpose",
        "arcana": "prime",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Empathy", "Expression", "Medicine"],
        "description": "Subject gains one of the caster's Obsessions. If subject is a mage already possessing the maximum number of Obsessions this spell causes a Clash of Wills. If successful replace one of these Obsessions. +1 Reach: Can grant a wholly new Obsession",
        "source": "MtAw2 p171"
    },
    "word_of_unmaking": {
        "name": "Word of Unmaking",
        "arcana": "prime",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "withstand": "Merit rating or Durability",
        "rote_skills": ["Intimidation", "Occult", "Weaponry"],
        "description": "Destroy a magical item, but not artifacts. +2 Reach: Item explodes violently, roll the item Merit rating or Durability. Anyone within 1 yard per dot suffers lethal damage per success",
        "source": "MtAw2 p171"
    }
}

SPACE_SPELLS = {
    # Space 1
    "correspondence": {
        "name": "Correspondence",
        "arcana": "space",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Empathy", "Medicine"],
        "description": "Learn one of subjects sympathetic links per Potency. The oldest and strongest are revealed first. If the link is nearby you will learn its exact location too. +1 Reach: You can follow a link to its other end. +1 Reach: Learn the emotional aspect of the connection",
        "source": "MtAw2 p172"
    },
    "ground_eater": {
        "name": "Ground Eater",
        "arcana": "space",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "withstand": "Stamina",
        "rote_skills": ["Athletics", "Science", "Survival"],
        "description": "Add or reduce Speed by Potency. Speed cannot go below 1",
        "source": "MtAw2 p173"
    },
    "isolation": {
        "name": "Isolation",
        "arcana": "space",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "withstand": "Composure",
        "rote_skills": ["Academics", "Intimidation", "Subterfuge"],
        "description": "Any attempt to interact with other people costs a Willpower point. Even then, dice pools are penalized by Potency. Prolonged exposure to spell (a day per point of subject's Composure) may cause breaking points or Conditions like Shaken or Spooked",
        "source": "MtAw2 p173"
    },
    "locate_object": {
        "name": "Locate Object",
        "arcana": "space",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Duration",
        "rote_skills": ["Empathy", "Occult", "Science"],
        "description": "Can find the subject in spell area. +1 Reach: Can track the subject even if it leaves the area",
        "source": "MtAw2 p173"
    },
    "the_outward_and_inward_eye": {
        "name": "The Outward and Inward Eye",
        "arcana": "space",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Firearms", "Investigation", "Occult"],
        "description": "Gain 360 degree vision and hearing. All attempts to ambush the character fail, or in the case of exceptional camouflage or distraction a chance die. Finally all penalties due to range, cover or concealment are reduced by Potency. +2 Reach: Can see through warps or shortcuts in Space",
        "source": "MtAw2 p174"
    },
    
    # Space 2
    "borrow_threads": {
        "name": "Borrow Threads",
        "arcana": "space",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Sympathy",
        "rote_skills": ["Larceny", "Occult", "Subterfuge"],
        "description": "Allows the transfer of a number of sympathetic connections between the caster and the subject(s) of the spell equal to potency. The caster must be aware of the links, either through other magic or knowledge of the subject. +1 Reach: The caster may copy connections instead of transferring them",
        "source": "MtAw2 p174"
    },
    "break_boundary": {
        "name": "Break Boundary",
        "arcana": "space",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Larceny", "Persuasion"],
        "description": "Allows the subject to slip past an obstacle that is obstructing a path or similar restriction of movement. +1 Reach: The subject can fit through narrow or restrictive passageways they couldn't normally fit through. +2 Reach: Subjects unable to move can pass through obstructions",
        "source": "MtAw2 p174"
    },
    "lying_maps": {
        "name": "Lying Maps",
        "arcana": "space",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "withstand": "Resolve",
        "rote_skills": ["Academics", "Politics", "Survival"],
        "description": "Makes a subject certain that a path of the caster's choosing is the correct path to a destination",
        "source": "MtAw2 p174"
    },
    "scrying": {
        "name": "Scrying",
        "arcana": "space",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Computers", "Occult", "Subterfuge"],
        "description": "Allows the caster to remotely view a distant location, with varying effects depending on the type of Sympathetic connection. Spells can also be cast on subjects as if one were viewing them remotely. The scrying window may be invisible or visible to everyone in the vicinity. Add Fate 2: The caster can select specific people who can see the scrying window",
        "source": "MtAw2 p174"
    },
    "secret_door": {
        "name": "Secret Door",
        "arcana": "space",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Stealth", "Subterfuge"],
        "description": "Allows the caster to hide a passageway from mundane perception, invoking Clash of Wills against magical perception. +1 Reach: A Key may be specified to allow entry",
        "source": "MtAw2 p175"
    },
    "veil_sympathy": {
        "name": "Veil Sympathy",
        "arcana": "space",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "withstand": "Sympathy",
        "rote_skills": ["Politics", "Subterfuge", "Survival"],
        "description": "Conceals one of the subject's sympathetic connections. +1 Reach: May make the subject appear to have a nonexistent connection. +1 Reach: Prevents the connection from being used as a Sympathetic Yantra. +2 Reach: The caster may suppress all of the subject's connections",
        "source": "MtAw2 p175"
    },
    "ward": {
        "name": "Ward",
        "arcana": "space",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Subterfuge", "Weaponry"],
        "description": "Prevents space from being manipulated in an area. +1 Reach: The caster may specify a Key that can allow the manipulation of space. +2 Reach: The caster may ward an Iris",
        "source": "MtAw2 p176"
    },
    
    # Space 3
    "ban": {
        "name": "Ban",
        "arcana": "space",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "rote_skills": ["Intimidation", "Science", "Stealth"],
        "description": "Cuts an area off from the outside world, including light, sound, and air. Add Any Arcanum 2: Exclude phenomena under that Arcanum, or only Ban phenomena of that Arcanum",
        "source": "MtAw2 p176"
    },
    "co_location": {
        "name": "Co-Location",
        "arcana": "space",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Firearms", "Science"],
        "description": "Allows the overlapping of multiple locations. Individuals who can perceive this overlap may switch between locations reflexively once a turn. +1 Reach: Anything in the overlapped locations may be made visible to the naked eye. +1 Reach: The caster may make the Co-Location a two-dimensional plane, creating a portal",
        "source": "MtAw2 p176"
    },
    "forced_sympathy": {
        "name": "Forced Sympathy",
        "arcana": "space",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Empathy", "Stealth", "Subterfuge"],
        "description": "Must be cast on a Mage to alter his imbument process. Whenever a user casts the item's spell it always targets the subject with the closest sympathy to the user. Closest sympathy is determined by the best sympathetic Yantra on the user at the time of Casting",
        "source": "SoS 73"
    },
    "optimal_container": {
        "name": "Optimal Container",
        "arcana": "space",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Larceny", "Science", "Subterfuge"],
        "description": "Expand the dimensions within a container to allow it to hold larger objects than usual. Enhance the sized item a container can hold by its base size + Potency",
        "source": "SoS 66"
    },
    "perfect_sympathy": {
        "name": "Perfect Sympathy",
        "arcana": "space",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Empathy", "Larceny"],
        "description": "Allows the subject to gain 8-Again when taking an action on a subject that is one of their Strong sympathies. +1 Reach: Can redirect spells at Sympathetic Range to a Strong connection instead. +1 Reach: For one Mana, the subject gains (Potency) rote actions",
        "source": "MtAw2 p176"
    },
    "warp": {
        "name": "Warp",
        "arcana": "space",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "rote_skills": ["Athletics", "Brawl", "Medicine"],
        "description": "Deals bashing damage equal to Potency by twisting the space the subject occupies. +1 Reach: The pain inflicts the Arm Wrack or Leg Wrack Tilt",
        "source": "MtAw2 p177"
    },
    "web_weaver": {
        "name": "Web-Weaver",
        "arcana": "space",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Crafts", "Empathy", "Persuasion"],
        "description": "Allows bolstering of a sympathetic connection. Add Time 2: The caster may use temporal sympathy to anything the subject touched in the target time",
        "source": "MtAw2 p177"
    },
    
    # Space 4
    "alter_direction": {
        "name": "Alter Direction",
        "arcana": "space",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Firearms", "Persuasion"],
        "description": "Allows the caster to change (Potency) absolute directions (e.g. north, south, up, down) in an area, or change directions relative to a chosen subject. +1 Reach: The caster can redefine directions in curves rather than just straight lines",
        "source": "MtAw2 p177"
    },
    "collapse": {
        "name": "Collapse",
        "arcana": "space",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "rote_skills": ["Academics", "Firearms", "Intimidation"],
        "description": "Forces a subject and a chosen object to occupy the same space, dealing (Potency) lethal damage. +1 Reach: For 1 Mana, damage inflicted becomes Aggravated. +1 Reach: The co-located object remains inside the subject",
        "source": "MtAw2 p177"
    },
    "cut_threads": {
        "name": "Cut Threads",
        "arcana": "space",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "withstand": "Sympathy (Connection)",
        "rote_skills": ["Persuasion", "Politics", "Weaponry"],
        "description": "Destroy a sympathetic connection, effect is lasting, but connection can be restored in time. +2 Reach: Remove the subject's sympathetic name. This is not lasting and only last until the spell expires",
        "source": "MtAw2 p177"
    },
    "secret_room": {
        "name": "Secret Room",
        "arcana": "space",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Expression", "Science", "Survival"],
        "description": "Enlarge or shrink a space. Making a box bigger on the inside than on the outside, for example. Scale has to encompass the targets current size. And goes up or down equal to Potency in steps along the Area Scale Factor",
        "source": "MtAw2 p178"
    },
    "teleportation": {
        "name": "Teleportation",
        "arcana": "space",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "rote_skills": ["Larceny", "Persuasion", "Science"],
        "description": "Teleport a subject to another location. You may use the Sympathetic Range Attainment on either the subject or the location but not both. +1 Reach: You may swap the location of two subjects with no more a point of Size difference. +2 Reach: You may now use two separate Sympathetic Ranges",
        "source": "MtAw2 p178"
    },
    
    # Space 5
    "create_sympathy": {
        "name": "Create Sympathy",
        "arcana": "space",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "withstand": "Desired Sympathy",
        "rote_skills": ["Empathy", "Persuasion", "Politics"],
        "description": "Create a new sympathetic connection for the subject. This is Lasting, but may fade with time. +1 Reach: The created connection is Lasting and never fades. Only magic can sever it now. +2 Reach: Give a subject a new sympathetic name",
        "source": "MtAw2 p178"
    },
    "forge_no_chains": {
        "name": "Forge No Chains",
        "arcana": "space",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Subterfuge", "Survival"],
        "description": "For the Duration of the spell the subjects cannot create new sympathetic connection. blood, hair, etc shed during the Duration of the spell do not link back to the subject. This also has an effect on any Space spells you leave behind. Any attempt to scrutinize your spells with Mage Sight has the spell's Potency added to the Opacity",
        "source": "MtAw2 p178"
    },
    "pocket_dimension": {
        "name": "Pocket Dimension",
        "arcana": "space",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Expression", "Survival"],
        "description": "Create a space. By default this space is devoid of the other arcana. Spells cast within never cause Paradox unless they sympathetic range is used to affect something outside of the space. +1 Reach: Create an Iris to the Pocket Dimension in the physical world. Add Time 2: Time flows normally within the space",
        "source": "MtAw2 p178"
    },
    "quarantine": {
        "name": "Quarantine",
        "arcana": "space",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Duration",
        "rote_skills": ["Academics", "Larceny", "Socialize"],
        "description": "Remove a subject from space altogether. The world adjusts for the missing space. A Quarantined house doesn't leave behind an empty space, instead the neighboring house would now find themselves adjacent. +1 Reach: Specify a Key that allows access to and from the removed area",
        "source": "MtAw2 p179"
    },
    "unnaming": {
        "name": "Unnaming",
        "arcana": "space",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Duration",
        "withstand": "Composure",
        "rote_skills": ["Empathy", "Expression", "Occult"],
        "description": "The Mage Erases a subject's sympathetic name from existence, the excised name is immediately replaced with one that matches whatever most sleepers would use to refer to her as. Any Sympathetic connections to the old name cease to exist as well. Add Prime 5: The Spell can be used on an Awakened Subject's Shadow Name",
        "source": "SoS 94"
    }
}

SPIRIT_SPELLS = {
    # Spirit 1
    "coaxing_the_spirits": {
        "name": "Coaxing the Spirits",
        "arcana": "spirit",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "withstand": "Composure or Rank",
        "rote_skills": ["Politics", "Athletics", "Expression"],
        "description": "Compel a Spirit or its physical representation to take a single instant action that is in accordance to its nature",
        "source": "MtAw2 p180"
    },
    "exorcists_eye": {
        "name": "Exorcist's Eye",
        "arcana": "spirit",
        "level": 1,
        "practice": "Unveiling",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Survival", "Socialize"],
        "description": "See and speak with any Spirit, be they in Twilight, slumbering in an object or possessing somebody. Can also see the conduit of any Spirit with the Reaching Manifestation. +1 Reach: Can see across the Gauntlet, Withstood by Gauntlet Strength. Add Death 1 or Mind 1: These benefits extend to ghost or Goetia",
        "source": "MtAw2 p180"
    },
    "gremlins": {
        "name": "Gremlins",
        "arcana": "spirit",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Potency",
        "rote_skills": ["Larceny", "Politics", "Subterfuge"],
        "description": "Cause Spirit of object to hinder its user. Each level of Potency causes one failure with the item to become a dramatic failure. A player's character can earn a Beat from this as per normal. +1 Reach: As long as the object is within sensory range, can decide what failure become dramatic failures",
        "source": "MtAw2 p180"
    },
    "invoke_bane": {
        "name": "Invoke Bane",
        "arcana": "spirit",
        "level": 1,
        "practice": "Compelling",
        "primary_factor": "Duration",
        "withstand": "Rank",
        "rote_skills": ["Brawl", "Intimidation", "Occult"],
        "description": "Force a Spirit to avoid its Bane even more then normal. Spirit needs to spend a Willpower to come within the area of its bane and cannot touch it. Spirits above Rank 5 are unaffected by this spell",
        "source": "MtAw2 p180"
    },
    "know_spirit": {
        "name": "Know Spirit",
        "arcana": "spirit",
        "level": 1,
        "practice": "Knowing",
        "primary_factor": "Potency",
        "withstand": "Rank",
        "rote_skills": ["Academics", "Brawl", "Socialize"],
        "description": "Learn a number of facts about the Spirit equal to Potency: Spirit's name, Rank, Manifestations, Numina, Influences and roughly how strong these are, Ban, Bane",
        "source": "MtAw2 p180"
    },
    
    # Spirit 2
    "cap_the_well": {
        "name": "Cap the Well",
        "arcana": "spirit",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Politics", "Survival", "Persuasion"],
        "description": "Any attempt to feed from a source of Essence affected by this spell provokes a Clash of Wills",
        "source": "MtAw2 p180"
    },
    "channel_essence": {
        "name": "Channel Essence",
        "arcana": "spirit",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "rote_skills": ["Occult", "Persuasion", "Survival"],
        "description": "Move Essence equal to Potency but no higher than the Gnosis-derived Mana per turn, from a Resonant Condition or suitable receptacle to a Spirit. You can store Essence into your own Pattern which stays even after the spell has expired. Add Death 2 or Mind 2: Spell may be cast on ghosts or Goetia. +1 Reach: Can siphon Essence directly from a Spirit",
        "source": "MtAw2 p180"
    },
    "command_spirit": {
        "name": "Command Spirit",
        "arcana": "spirit",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Potency",
        "withstand": "Rank",
        "rote_skills": ["Medicine", "Athletics", "Persuasion"],
        "description": "Force a Spirit to undertake a number of actions equal to Potency. Spirit may/will abandon incomplete task if the spell Duration expires. No effect on Spirits above Rank 5",
        "source": "MtAw2 p181"
    },
    "ephemeral_shield": {
        "name": "Ephemeral Shield",
        "arcana": "spirit",
        "level": 2,
        "practice": "Shielding",
        "primary_factor": "Duration",
        "rote_skills": ["Animal Ken", "Medicine", "Stealth"],
        "description": "Any Spirit Numina, Influences and Manifestations, Spirit Spells and werewolf Gifts aimed at subject provoke a Clash of Wills. +1 Reach: A Spirits physical attacks are likewise affected. Add Death 2 or Mind 2: Shield affects ghosts or Goetia respectively",
        "source": "MtAw2 p181"
    },
    "gossamer_touch": {
        "name": "Gossamer Touch",
        "arcana": "spirit",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Brawl", "Crafts", "Intimidation"],
        "description": "Can interact physically with Spirits in Twilight. Add Death 2 or Mind 2: Affects ghosts or Goetia respectively. +1 Reach: Object you carry are likewise physical to Spirits. +1 Reach: Unarmed attacks against Spirits deal Potency extra damage",
        "source": "MtAw2 p181"
    },
    "opener_of_the_way": {
        "name": "Opener of the Way",
        "arcana": "spirit",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Computers", "Socialize"],
        "description": "Shift Resonant Condition to Open Condition or vice versa",
        "source": "MtAw2 p181"
    },
    "shadow_walk": {
        "name": "Shadow Walk",
        "arcana": "spirit",
        "level": 2,
        "practice": "Veiling",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Stealth", "Streetwise"],
        "description": "Subject becomes shrouded from Spirit and Spirit magics notice. Supernatural effects to detect provoke a Clash of Wills",
        "source": "MtAw2 p181"
    },
    "slumber": {
        "name": "Slumber",
        "arcana": "spirit",
        "level": 2,
        "practice": "Ruling",
        "primary_factor": "Duration",
        "withstand": "Rank",
        "rote_skills": ["Expression", "Occult", "Weaponry"],
        "description": "Reduce the rate at which a hibernating Spirit regains Essence. Instead of one Essence per day the Spirit only regains one Essence per Potency days",
        "source": "MtAw2 p181"
    },
    
    # Spirit 3
    "bolster_spirit": {
        "name": "Bolster Spirit",
        "arcana": "spirit",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "rote_skills": ["Medicine", "Occult", "Expression"],
        "description": "Heal a Spirit. Each level of Potency heals two bashing damage. +1 Reach: Instead of healing, each level of Potency can increase one of the Spirit's Attributes by one for the duration of the spell. +2 Reach: Spend one Mana to increase the Spirit's Rank by one",
        "source": "MtAw2 p181"
    },
    "erode_resonance": {
        "name": "Erode Resonance",
        "arcana": "spirit",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Brawl", "Intimidation"],
        "description": "Remove a subject's Open or Resonant condition. This effect is Lasting. +1 Reach: Any future attempts to create the Conditions suffers a penalty equal to Potency",
        "source": "MtAw2 p181"
    },
    "howl_from_beyond": {
        "name": "Howl From Beyond",
        "arcana": "spirit",
        "level": 3,
        "practice": "Fraying",
        "primary_factor": "Potency",
        "rote_skills": ["Expression", "Firearms", "Medicine"],
        "description": "Attack spell deal bashing damage equal to Potency. +1 Reach: the subject gains the Open Condition. +1 Reach: Can target beings on the other side of the Gauntlet, but is Withstood by Gauntlet Strength",
        "source": "MtAw2 p182"
    },
    "place_of_power": {
        "name": "Place of Power",
        "arcana": "spirit",
        "level": 3,
        "practice": "Fraying or Perfecting",
        "primary_factor": "Potency",
        "withstand": "Gauntlet Strength",
        "rote_skills": ["Academics", "Expression", "Survival"],
        "description": "Raise or lower Gauntlet Strength in spell Area by Potency. +1 Reach: Alter Gauntlet independently on either side. For example making it easier to enter the Shadow but harder to leave or vice versa",
        "source": "MtAw2 p182"
    },
    "reaching": {
        "name": "Reaching",
        "arcana": "spirit",
        "level": 3,
        "practice": "Weaving",
        "primary_factor": "Duration",
        "withstand": "Gauntlet Strength",
        "rote_skills": ["Athletics", "Medicine", "Socialize"],
        "description": "Interact physically and magically with things on the other side of the Gauntlet. +1 Reach: Open an Iris between the physical world and the Shadow, which anybody can pass through. For another Reach may specify a Key",
        "source": "MtAw2 p182"
    },
    "rouse_spirit": {
        "name": "Rouse Spirit",
        "arcana": "spirit",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Potency",
        "withstand": "Rank",
        "rote_skills": ["Athletics", "Expression", "Investigation"],
        "description": "Awaken a Spirit early Potency required is equal to the difference between the Spirit's current Essence and total Corpus. +1 Reach: For each additional Reach, the Spirit wakes with an additional Corpus box cleared",
        "source": "MtAw2 p182"
    },
    "spirit_summons": {
        "name": "Spirit Summons",
        "arcana": "spirit",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "withstand": "Rank",
        "rote_skills": ["Persuasion", "Socialize", "Occult"],
        "description": "Call a Spirit in the local area to you. +1 Reach: Spell also creates the Open Condition. +1 Reach: Can give the Spirit a single word command to follow. +1 Reach: Can call a Spirit from the Shadow instead. +2 Reach: Can give Spirit a complex command to follow",
        "source": "MtAw2 p182"
    },
    "spiritual_tool": {
        "name": "Spiritual Tool",
        "arcana": "spirit",
        "level": 3,
        "practice": "Perfecting",
        "primary_factor": "Duration",
        "rote_skills": ["Empathy", "Occult", "Survival"],
        "description": "Enhance an item to be more in-tune with the Shadow and Spirits in general. The object becomes both an item of the material world and the shadow and is able to interact with spirits both within Twilight and the Shadow. If the item is carried into either other realm it retains its material form when it returns to the material world",
        "source": "SoS 66"
    },
    
    # Spirit 4
    "banishment": {
        "name": "Banishment",
        "arcana": "spirit",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "withstand": "Rank",
        "rote_skills": ["Brawl", "Expression", "Occult"],
        "description": "Strip a number of Manifestation Conditions equal to Potency. Effect is Lasting, but Conditions may be reestablished as normal. No effect on Spirits above Rank 5. Add Mind 4: affect Goetia. Add Death 4: affect Ghosts. +1 Reach: Conditions cannot be reestablished until spell duration has expired",
        "source": "MtAw2 p182"
    },
    "bind_spirit": {
        "name": "Bind Spirit",
        "arcana": "spirit",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Rank",
        "rote_skills": ["Crafts", "Brawl", "Intimidation"],
        "description": "Grant a number of Manifestation Conditions equal to Potency. No effect on Spirits above Rank 5. Add Mind 4: effect Goetia. Add Death 4: effect Ghosts",
        "source": "MtAw2 p183"
    },
    "craft_fetish": {
        "name": "Craft Fetish",
        "arcana": "spirit",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "withstand": "Rank",
        "rote_skills": ["Crafts", "Occult", "Persuasion"],
        "description": "Create a Fetish an item that contains a Spirit. And can be used to call upon a number of one of the Spirit's Influence dots and Numina equal to Potency. These abilities cost Essence and the item has the Spirit's Essence pool. Triggering the bound Spirit's Ban or Bane destroys the fetish. A fetish without a Spirit may also be created and can hold 10+Potency Essence",
        "source": "MtAw2 p183"
    },
    "familiar": {
        "name": "Familiar",
        "arcana": "spirit",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Athletics", "Expression", "Intimidate"],
        "description": "Gain the Familiar Merit for the duration of the spell. Both parties must be willing. Cannot effect Spirits above Rank 2. Substitute Death 4 or Mind 4: Bind a Ghost or Goetia respectively",
        "source": "MtAw2 p183"
    },
    "haunted_grimoire_spirit": {
        "name": "Haunted Grimoire",
        "arcana": "spirit",
        "level": 4,
        "secondary_arcana": "prime 1",
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Total Arcanum dots of Rote + Rank",
        "rote_skills": ["Crafts", "Intimidation", "Occult"],
        "description": "Costs 1 Mana. The Mage binds a spirit to a grimoire, writing its essence into the vessel's pattern. The Grimoire gains the Open and Resonant Conditions. When cast the spell is increased by the Spirits Rank for Primary Factor. This spell is a Wisdom Sin against Understanding",
        "source": "SoS 86"
    },
    "scribe_daimonomikon_spirit": {
        "name": "Scribe Daimonomikon",
        "arcana": "spirit",
        "level": 4,
        "secondary_arcana": "prime 1",
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Rank of Attainment + (10 - Caster's Gnosis)",
        "rote_skills": ["Crafts", "Expression", "Occult"],
        "description": "Cost 1 Mana. Scribe a Daimonomikon for the Mage's Legacy. A Mage must be of Gnosis 2 or above to cast this. Anyone initiated into a Legacy via a Daimonomikon must spend 1 Arcane Experience. These serve as a sympathetic Yantra worth +2 Dice for members of the inscribed Legacy. +1 Reach: For 1 Mana, the Spell's Duration is Lasting",
        "source": "SoS 87"
    },
    "shadow_scream": {
        "name": "Shadow Scream",
        "arcana": "spirit",
        "level": 4,
        "practice": "Unraveling",
        "primary_factor": "Potency",
        "rote_skills": ["Expression", "Firearms", "Medicine"],
        "description": "Deal Lethal damage equal to Potency. Can hit targets in Twilight. +1 Reach: For one point of Mana damage is aggravated. +1 Reach: Can destroy Essence divide Potency between regular and Essence damage. +1 Reach: Target gains Open Condition. +1 Reach: Can hit target on the other side of the Gauntlet",
        "source": "MtAw2 p183"
    },
    "shape_spirit": {
        "name": "Shape Spirit",
        "arcana": "spirit",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Rank",
        "rote_skills": ["Crafts", "Medicine", "Persuasion"],
        "description": "Change a Spirit with a number of effects equal to Potency: Change nature, Redistribute Attribute dots, Heal one Lethal corpus, Redefine and redistribute Influences, Add/remove/replace one Manifestation, Add/remove/replace one Numen, Rewrite Ban or Bane. Traits must stay within Rank-derived maximums. Change revert at the end of spell duration. +1 Reach: For one Mana heal aggravated damage",
        "source": "MtAw2 p184"
    },
    "twilit_body": {
        "name": "Twilit Body",
        "arcana": "spirit",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Duration",
        "rote_skills": ["Occult", "Subterfuge", "Survival"],
        "description": "Turn yourself (and whatever you're wearing) into Spirit-attuned ephemera, and thus in Twilight. +1 Reach: can become immaterial even in realms where Twilight doesn't normally exist",
        "source": "MtAw2 p184"
    },
    "world_walker": {
        "name": "World Walker",
        "arcana": "spirit",
        "level": 4,
        "practice": "Patterning",
        "primary_factor": "Potency",
        "withstand": "Gauntlet Strength",
        "rote_skills": ["Athletics", "Persuasion", "Survival"],
        "description": "Bring subject across the Gauntlet, no portal necessary. +1 Reach: Give conjured Spirit Materialized Condition",
        "source": "MtAw2 p184"
    },
    
    # Spirit 5
    "annihilate_spirit": {
        "name": "Annihilate Spirit",
        "arcana": "spirit",
        "level": 5,
        "practice": "Unmaking",
        "primary_factor": "Potency",
        "withstand": "Rank",
        "rote_skills": ["Intimidation", "Science", "Weaponry"],
        "description": "Utterly destroy a Spirit. The Spirit may spend an Essence to roll Power + Finesse in a Clash of Wills to prevent this. But if the spell succeeds the Spirit is destroyed even if it still has Essence it won't go into hibernation the Spirit is simply gone. Cannot affect Spirits above Rank 5",
        "source": "MtAw2 p184"
    },
    "birth_spirit": {
        "name": "Birth Spirit",
        "arcana": "spirit",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Medicine", "Expression"],
        "description": "Create a Rank 1 Spirit. +1 Reach: For one Mana, create a Rank 2 Spirit",
        "source": "MtAw2 p184"
    },
    "create_locus": {
        "name": "Create Locus",
        "arcana": "spirit",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "withstand": "Gauntlet Strength",
        "rote_skills": ["Crafts", "Empathy", "Survival"],
        "description": "Create a Locus at a location with the Resonant Condition. +1 Reach: The Locus generates Essence equal to Potency per day",
        "source": "MtAw2 p184"
    },
    "essence_fountain": {
        "name": "Essence Fountain",
        "arcana": "spirit",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Potency",
        "rote_skills": ["Empathy", "Expression", "Occult"],
        "description": "Create Essence equal to Potency. The Essence has a Resonance of your choosing, as long as you have encountered it before. +1 Reach: Flavor the Essence with multiple Resonances",
        "source": "MtAw2 p185"
    },
    "spirit_manse": {
        "name": "Spirit Manse",
        "arcana": "spirit",
        "level": 5,
        "practice": "Making",
        "primary_factor": "Duration",
        "rote_skills": ["Crafts", "Expression", "Survival"],
        "description": "Create a place in the Shadow for yourself and gain the Safe Place Merit with rating equal to Potency. +1 Reach: You may create an Iris between this place and the material world and may give it a key. But the spell becomes Withstood by Gauntlet Strength",
        "source": "MtAw2 p185"
    }
}

# NOTE: The Codex of Darkness contains spells for all 10 Arcana
# This file now includes ALL SPELLS from Death, Time, Fate, Forces, Life, Matter, Mind, Prime, Space, and Spirit!


# All spells dictionary combining all arcana
ALL_MAGE_SPELLS = {}
ALL_MAGE_SPELLS.update(DEATH_SPELLS)
ALL_MAGE_SPELLS.update(TIME_SPELLS)
ALL_MAGE_SPELLS.update(FATE_SPELLS)
ALL_MAGE_SPELLS.update(FORCES_SPELLS)
ALL_MAGE_SPELLS.update(LIFE_SPELLS)
ALL_MAGE_SPELLS.update(MATTER_SPELLS)
ALL_MAGE_SPELLS.update(MIND_SPELLS)
ALL_MAGE_SPELLS.update(PRIME_SPELLS)
ALL_MAGE_SPELLS.update(SPACE_SPELLS)
ALL_MAGE_SPELLS.update(SPIRIT_SPELLS)

# Spell lists by level for easy access
SPELLS_BY_LEVEL = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

# Populate spell lists by level
for spell_key, spell_data in ALL_MAGE_SPELLS.items():
    level = spell_data['level']
    SPELLS_BY_LEVEL[level].append(spell_key)

# Spells available to Sleepwalkers (typically 1-2 dot spells)
SLEEPWALKER_SPELLS = SPELLS_BY_LEVEL[1] + SPELLS_BY_LEVEL[2]

# Spells available to Proximus (typically 1-3 dot spells from their bloodline arcana)
PROXIMUS_SPELLS = SPELLS_BY_LEVEL[1] + SPELLS_BY_LEVEL[2] + SPELLS_BY_LEVEL[3]

def get_spell(spell_key):
    """Get spell data by key."""
    return ALL_MAGE_SPELLS.get(spell_key)

def get_spells_by_arcana(arcana):
    """Get all spells for a specific arcana."""
    return {k: v for k, v in ALL_MAGE_SPELLS.items() if v['arcana'] == arcana.lower()}

def get_spells_by_level(level):
    """Get all spells of a specific level."""
    return {k: v for k, v in ALL_MAGE_SPELLS.items() if v['level'] == level}

