"""
Geist: The Sin-Eaters - Power Data
Haunts, Keys, and Ceremonies for Sin-Eaters.
This file contains all the detailed information about Geist powers.
"""


# Valid geist burdens (how they died)
GEIST_BURDENS = [
    "abiding", "bereaved", "hungry", "kindly", "vengeful"
]

# Valid krewe types
GEIST_KREWE_TYPES = [
    "family", "industrial", "network", "military", "academic"
]

# Primary powers (rated 1-5 dots) - Haunts
GEIST_PRIMARY_POWERS = [
    "boneyard", "caul", "curse", "dirge", "marionette", "memoria", "oracle", "rage", "shroud", "tomb"
]

# Secondary powers (individual abilities) - Keys and Ceremonies
GEIST_SECONDARY_POWERS = [
    # Keys (individual abilities)
    "beasts", "blood", "chance", "cold wind", "deep waters", "disease", "grave dirt", "pyre flame", "stillness",
    # Ceremonies (individual rituals)
    # Level 1 Ceremonies
    "dead man's camera", "death watch", "diviner's jawbone", "lovers' telephone", "ishtar's perfume",
    # Level 2 Ceremonies
    "crow girl kiss", "gifts of persephone", "ghost trap", "skeleton key",
    # Level 3 Ceremonies
    "bestow regalia", "krewe binding", "speaker for the dead", "black cat's crossing", "bloody codex", "dumb supper",
    # Level 4 Ceremonies
    "forge anchor", "maggot homonculus",
    # Level 5 Ceremonies
    "pass on", "ghost binding", "persephone's return"
]

# All geist powers combined
GEIST_ALL_POWERS = GEIST_PRIMARY_POWERS + GEIST_SECONDARY_POWERS

# Backwards compatibility aliases
GEIST_HAUNTS = GEIST_PRIMARY_POWERS
GEIST_KEYS = ["beasts", "blood", "chance", "cold wind", "deep waters", "disease", "grave dirt", "pyre flame", "stillness"]
GEIST_CEREMONIES = [
    "dead man's camera", "death watch", "diviner's jawbone", "lovers' telephone", "ishtar's perfume",
    "crow girl kiss", "gifts of persephone", "ghost trap", "skeleton key",
    "bestow regalia", "krewe binding", "speaker for the dead", "black cat's crossing", "bloody codex", "dumb supper",
    "forge anchor", "maggot homonculus",
    "pass on", "ghost binding", "persephone's return"
]

# Valid crisis point triggers for geists
GEIST_CRISIS_TRIGGERS = [
    "betrayal", "abandonment", "mortality", "innocence", "loss", "helplessness", "failure", "isolation"
]

# Valid remembrance trait types (skills or merits ≤3 dots)
GEIST_REMEMBRANCE_SKILLS = [
    "athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry",
    "animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge",
    "crafts", "investigation", "medicine", "occult", "politics", "science"
]

GEIST_REMEMBRANCE_MERITS = [
    "contacts", "allies", "resources", "safe_place", "library", "mentor", "retainer", "status"
]

# ==================== HAUNT DETAILS ====================

# The Boneyard
HAUNT_BONEYARD = {
    "raise_the_boneyard": {
        "name": "Raise the Boneyard",
        "rank": 1,
        "cost": "*+",
        "description": "Spread Plasm to haunt a Boneyard, which becomes Open to ghosts. Understand the Boneyard's layout and defeat attempts to hide from you in it.",
        "book": "GTS 2e p.102"
    },
    "eyes_in_the_paintings": {
        "name": "Eyes in the Paintings",
        "rank": 2,
        "cost": "*",
        "description": "See and sense through places in the Boneyard.",
        "book": "GTS 2e p.102"
    },
    "no_escape": {
        "name": "No Escape",
        "rank": 3,
        "cost": "--",
        "description": "Raise larger Boneyards.",
        "book": "GTS 2e p.102",
        "additional": "●/die to penalize attempts to leave the Boneyard by any means."
    },
    "earthquake_weather": {
        "name": "Earthquake Weather",
        "rank": 4,
        "cost": "***",
        "description": "Conjure Environmental Tilts within the Boneyard.",
        "book": "GTS 2e p.103"
    },
    "the_new_law": {
        "name": "The New Law",
        "rank": 5,
        "cost": "**",
        "description": "Impose an Old Law upon the Boneyard, penalizing actions to break it.",
        "book": "GTS 2e p.103",
        "additional": "●● to punish violators with the rote quality and as a ghostly bane."
    }
}

# The Caul
HAUNT_CAUL = {
    "extrude_the_caul": {
        "name": "Extrude the Caul",
        "rank": 1,
        "cost": "* to *****",
        "description": "Take on a geistly flesh charged by Plasm. Spend a charge to ignore wound penalties, substitute your geist's Attribute for yours, or reduce the exceptional success threshold from five to three on an action making use of your plasmic form.",
        "book": "GTS 2e p.104"
    },
    "cold_flesh": {
        "name": "Cold Flesh",
        "rank": 2,
        "cost": "***",
        "description": "For each dot of Caul, gain +1/+½ Armor.",
        "book": "GTS 2e p.104"
    },
    "vitiate": {
        "name": "Vitiate",
        "rank": 3,
        "cost": "--",
        "description": "Extrude the Caul generates twice the charges.",
        "book": "GTS 2e p.105",
        "additional": "Various Plasm costs for: Swell in Size (+2 Size per Strength dot), Contort into skittering shape (●), Inflict lethal unarmed (●), Grow wings (●●), Explode into swarm (●●●●)"
    },
    "disarticulation": {
        "name": "Disarticulation",
        "rank": 4,
        "cost": "* to *****",
        "description": "Disgorge an obedient homunculus with Plasm as Health and twice Plasm as a Physical dice pool.",
        "book": "GTS 2e p.105"
    },
    "the_hungry_dead": {
        "name": "The Hungry Dead",
        "rank": 5,
        "cost": "●/Size",
        "description": "Devour a fresh corpse or incapacitated ghost. You may spend remaining charges to take the victim's shape or substitute their traits for your own.",
        "book": "GTS 2e p.105"
    }
}

# The Curse
HAUNT_CURSE = {
    "lay_the_curse": {
        "name": "Lay the Curse",
        "rank": 1,
        "cost": "* to ****",
        "description": "Mark a subject with a Plasm-charged curse. Spend a charge to impose a -2 penalty on an action.",
        "book": "GTS 2e p.106"
    },
    "gremlin": {
        "name": "Gremlin",
        "rank": 2,
        "cost": "**",
        "description": "Spend a charge to invert equipment bonuses into penalties, or two charges to cause tools to deal their bonus as damage on use.",
        "book": "GTS 2e p.106",
        "additional": "●● to spend a charge to extinguish all fires set by the subject for a scene."
    },
    "malady": {
        "name": "Malady",
        "rank": 3,
        "cost": "--",
        "description": "Lay the Curse generates twice the charges.",
        "book": "GTS 2e p.107",
        "additional": "●● to spend a charge to inflict an injurious Personal Tilt for a scene through dangerous misfortune. ●● to spend the Curse to deal three lethal damage through misfortune."
    },
    "exhaustion": {
        "name": "Exhaustion",
        "rank": 4,
        "cost": "**",
        "description": "Spend a charge to reduce a Social roll to a chance die.",
        "book": "GTS 2e p.107",
        "additional": "●● to spend a charge to deny Willpower recovery."
    },
    "forgotten": {
        "name": "Forgotten",
        "rank": 5,
        "cost": "***",
        "description": "Spend a charge to force the subject to spend Willpower to be noticed.",
        "book": "GTS 2e p.107",
        "additional": "●●● to spend a charge to block the use of a Social Merit. ●●● to spend a charge to bring the subject in contact with ghostly Twilight."
    }
}

# The Dirge
HAUNT_DIRGE = {
    "sing_the_dirge": {
        "name": "Sing the Dirge",
        "rank": 1,
        "cost": "* to *****",
        "description": "Sing the wordless Dirge to evoke a feeling or simple response. While you sing, (Plasm) subjects gain a +2 bonus to obey, but must spend Willpower to act in contradiction.",
        "book": "GTS 2e p.108"
    },
    "exaltation": {
        "name": "Exaltation",
        "rank": 2,
        "cost": "*/Essence",
        "description": "Share your Plasm as Essence with ghostly subjects.",
        "book": "GTS 2e p.108",
        "additional": "●● to render a living subject Inspired."
    },
    "communion": {
        "name": "Communion",
        "rank": 3,
        "cost": "--",
        "description": "Sing the Dirge to entire areas.",
        "book": "GTS 2e p.108",
        "additional": "●● to give a perfect impression to subjects. You may roll Synergy + Dirge to open their Doors."
    },
    "exaltation_greater": {
        "name": "Exaltation (Greater)",
        "rank": 4,
        "cost": "**",
        "description": "Lift a negative mental Condition from a subject, or suppress a Persistent Condition while you sing.",
        "book": "GTS 2e p.108",
        "additional": "●●● to inflict a negative mental Condition on a subject."
    },
    "visitation": {
        "name": "Visitation",
        "rank": 5,
        "cost": "*/Rank",
        "description": "Impose a Manifestation Condition on a ghostly subject.",
        "book": "GTS 2e p.109"
    }
}

# The Marionette
HAUNT_MARIONETTE = {
    "string_the_marionette": {
        "name": "String the Marionette",
        "rank": 1,
        "cost": "* to ***",
        "description": "Cast strings of Plasm upon a subject of (Plasm) Size. You may take the marionette's actions as it could normally move, or swing it about as an improvised throwing weapon.",
        "book": "GTS 2e p.109"
    },
    "swarm": {
        "name": "Swarm",
        "rank": 2,
        "cost": "**",
        "description": "You may simultaneously string a number of marionettes equal to your Haunt rating.",
        "book": "GTS 2e p.110"
    },
    "phantom_strength": {
        "name": "Phantom Strength",
        "rank": 3,
        "cost": "* to ***",
        "description": "String marionettes of (Marionette + 2 × Plasm) Size.",
        "book": "GTS 2e p.110",
        "additional": "●● to impose a -3 penalty to contest your control."
    },
    "servant": {
        "name": "Servant",
        "rank": 4,
        "cost": "**",
        "description": "Sink your strings into a marionette to render it an obedient servant, which will follow orders without direct manipulation.",
        "book": "GTS 2e p.110",
        "additional": "●●●● to extend the Servant Condition for 24 hours."
    },
    "traitor_flesh": {
        "name": "Traitor Flesh",
        "rank": 5,
        "cost": "**",
        "description": "Retain control of a marionette through lethal damage or a breaking point.",
        "book": "GTS 2e p.110",
        "additional": "●●● to inflict two lethal damage to a marionette contesting your control."
    }
}

# The Memoria
HAUNT_MEMORIA = {
    "recall_the_memoria": {
        "name": "Recall the Memoria",
        "rank": 1,
        "cost": "* to *****",
        "description": "Witness a place or Anchor's memories of a particular death. Spend a Plasm charge for 8-Again to investigate the death or put it to rest, or to store memories as soft leverage that opens a Door.",
        "book": "GTS 2e p.112"
    },
    "denouement": {
        "name": "Dénouement",
        "rank": 2,
        "cost": "* to *****",
        "description": "Weave Plasm into a phantasm of the witnessed memories across an area, visible but not tangible to others.",
        "book": "GTS 2e p.112"
    },
    "memory_in_a_bottle": {
        "name": "Memory in a Bottle",
        "rank": 3,
        "cost": "--",
        "description": "Recall the Memoria generates twice the charges.",
        "book": "GTS 2e p.112",
        "additional": "●●● to seal the Memoria in a container to be released later, taking the memory with it."
    },
    "mystery_play": {
        "name": "Mystery Play",
        "rank": 4,
        "cost": "* to *****",
        "description": "Cast Plasm upon witnesses to draft them into roles in the memory.",
        "book": "GTS 2e p.112"
    },
    "break_the_cycle": {
        "name": "Break the Cycle",
        "rank": 5,
        "cost": "**",
        "description": "Actors in a Mystery Play can roll Resolve + Synergy to play out other actions in the memory. At the conclusion of the memory, Actors can resolve a Condition related to the memory, and ghostly Actors can resolve an Anchor and gain Rank 2.",
        "book": "GTS 2e p.113"
    }
}

# The Oracle
HAUNT_ORACLE = {
    "consult_the_oracle": {
        "name": "Consult the Oracle",
        "rank": 1,
        "cost": "* to ****",
        "description": "Release your ghost from your body into the ether. Spend a Plasm charge for your body to answer a question put to it about the touch of death, desires, and the hidden.",
        "book": "GTS 2e p.114"
    },
    "wandering_shade": {
        "name": "Wandering Shade",
        "rank": 2,
        "cost": "*",
        "description": "Your ghost wanders farther. You may spend a charge to answer a question about finding threats, the needy, the lost, and crimes against the dead.",
        "book": "GTS 2e p.114"
    },
    "spirit_reading": {
        "name": "Spirit Reading",
        "rank": 3,
        "cost": "--",
        "description": "Consult the Oracle generates twice the charges.",
        "book": "GTS 2e p.115",
        "additional": "●● to spend a charge to answer a question about ghostly bans, banes, and attachments to life."
    },
    "descent": {
        "name": "Descent",
        "rank": 4,
        "cost": "***",
        "description": "Your ghost roams the Underworld. Answer one question about ferrymen, the Old Laws, or Irkalla's Gates.",
        "book": "GTS 2e p.115"
    },
    "nekyia": {
        "name": "Nekyia",
        "rank": 5,
        "cost": "****",
        "description": "Answer one question about future betrayal, opportunities, brushes with death, or Underworld trials.",
        "book": "GTS 2e p.115"
    }
}

# The Rage
HAUNT_RAGE = {
    "vent_the_rage": {
        "name": "Vent the Rage",
        "rank": 1,
        "cost": "* to ****",
        "description": "Channel ghostly assaults for a scene, applying Plasm as a weapon rating and dealing lethal damage to ghosts. Roll the higher of your Brawl or Rage in your unarmed dice pool, ignoring unskilled penalties.",
        "book": "GTS 2e p.116"
    },
    "black_iron_blade": {
        "name": "Black-Iron Blade",
        "rank": 2,
        "cost": "**",
        "description": "Your strike inflicts a disabling or poisonous Personal Tilt.",
        "book": "GTS 2e p.116"
    },
    "maelstrom": {
        "name": "Maelstrom",
        "rank": 3,
        "cost": "--",
        "description": "Make unarmed ranged attacks out to 30 yards.",
        "book": "GTS 2e p.117",
        "additional": "●● to unleash an unarmed autofire medium burst."
    },
    "shatter": {
        "name": "Shatter",
        "rank": 4,
        "cost": "***",
        "description": "Deal aggravated damage with an unarmed attack.",
        "book": "GTS 2e p.117",
        "additional": "●● to traumatize a victim who suffers a breaking point from the Rage, inflicting Fugue."
    },
    "breaking_the_world": {
        "name": "Breaking the World",
        "rank": 5,
        "cost": "****",
        "description": "Lash out with an Environmental Tilt to which you remain immune.",
        "book": "GTS 2e p.117"
    }
}

# The Shroud
HAUNT_SHROUD = {
    "don_the_shroud": {
        "name": "Don the Shroud",
        "rank": 1,
        "cost": "* to ****",
        "description": "Wear your geist as a ghostly apparition. Ignore physiological needs and mundane disabling, and spend a Plasm charge to pass into Twilight for (Shroud) turns.",
        "book": "GTS 2e p.118"
    },
    "vision_of_mist": {
        "name": "Vision of Mist",
        "rank": 2,
        "cost": "*",
        "description": "Exude no body heat and pass through motion and laser sensors unnoticed.",
        "book": "GTS 2e p.118",
        "additional": "●● to fly at half Speed."
    },
    "haunting_presence": {
        "name": "Haunting Presence",
        "rank": 3,
        "cost": "--",
        "description": "Spend charges to enter Twilight for minutes instead of turns.",
        "book": "GTS 2e p.118",
        "additional": "●●● to choose a Manifestation (Discorporate, Fetter, Image, or Possess) or Numen (Sign or Hallucination) to use while Twilit."
    },
    "harrow": {
        "name": "Harrow",
        "rank": 4,
        "cost": "**",
        "description": "You may spend a charge to pull another person with you into Twilight.",
        "book": "GTS 2e p.119"
    },
    "descent_shroud": {
        "name": "Descent",
        "rank": 5,
        "cost": "***",
        "description": "You may spend a charge to cross directly into or out of the Upper Reaches, guided by emotional ties. You may spend another charge to pull another person with you into the Underworld.",
        "book": "GTS 2e p.119"
    }
}

# The Tomb
HAUNT_TOMB = {
    "open_the_tomb": {
        "name": "Open the Tomb",
        "rank": 1,
        "cost": "* to ****",
        "description": "Reassemble part of a corpse or destroyed object of (Tomb + Plasm) Size into a completed inanimate replica for (Tomb) days. The replica is also tangible to Twilit ghosts.",
        "book": "GTS 2e p.120"
    },
    "headstone": {
        "name": "Headstone",
        "rank": 2,
        "cost": "**",
        "description": "Open the Tomb using an item depicting or strongly tied to the object or creature.",
        "book": "GTS 2e p.120"
    },
    "empty_graves": {
        "name": "Empty Graves",
        "rank": 3,
        "cost": "--",
        "description": "Double the Size capability of Open the Tomb, and extend its duration indefinitely.",
        "book": "GTS 2e p.120",
        "additional": "— to Open the Tomb may produce obedient undead replicas of creatures. ●●● for the replica to become Open to ghosts, and can be Possessed by the ghost of its model."
    },
    "stygian_treasures": {
        "name": "Stygian Treasures",
        "rank": 4,
        "cost": "**",
        "description": "The replica's user can either see, hear, or communicate with the dead or the Underworld.",
        "book": "GTS 2e p.120"
    },
    "terra_cotta_soldiers": {
        "name": "Terra Cotta Soldiers",
        "rank": 5,
        "cost": "* to *****",
        "description": "Open the Tomb can reproduce notional objects from representations, producing Merits or services by their rating in Plasm.",
        "book": "GTS 2e p.120"
    }
}

# The Void
HAUNT_VOID = {
    "awaken_the_void": {
        "name": "Awaken the Void",
        "rank": 1,
        "cost": "* to ****",
        "description": "Welcome a blinding darkness. Within the darkness, your attacks ignore (Void) Durability and Armor, and the attacks of others ignore half that.",
        "book": "Mem p.24"
    },
    "annihilation_of_form": {
        "name": "Annihilation of Form",
        "rank": 2,
        "cost": "***",
        "description": "Make ranged attacks within the darkness, dealing lethal damage unarmed.",
        "book": "Mem p.25",
        "additional": "●+ to destroy objects, terrain, or immobilized creatures, paying extra for Size greater than Synergy."
    },
    "feasting_on_infinity": {
        "name": "Feasting on Infinity",
        "rank": 3,
        "cost": "--",
        "description": "Recover Plasm for every 10 points of Health, Corpus, or Structure you devour.",
        "book": "Mem p.25",
        "additional": "●● to remain unblinded by Awakening the Void. ●● to consume material without adverse effects, and deal aggravated damage with a grappling bite."
    },
    "the_end_of_all_things": {
        "name": "The End of All Things",
        "rank": 4,
        "cost": "*+",
        "description": "Open an annihilatory vacuum from within the darkness, which deals aggravated damage for each turn of contact, and pulls in anything without Size greater than Plasm spent. If that Plasm exceeds your Synergy, the vacuum threatens to persist as long as it can feed.",
        "book": "Mem p.25"
    },
    "the_wrong_way_door": {
        "name": "The Wrong-Way Door",
        "rank": 5,
        "cost": "*****+",
        "description": "Tear open a wound that directly connects the material realm to the Underworld for a day. Spend Plasm to open larger or more persistent wounds.",
        "book": "Mem p.25"
    }
}

# The Well
HAUNT_WELL = {
    "submerge_the_self": {
        "name": "Submerge the Self",
        "rank": 1,
        "cost": "*+",
        "description": "Your identity runs deep and fluid, allowing you to trade and use Memories like a ghost, treating Plasm as a maximum applicable Memory Skill bonus.",
        "book": "Mem p.27"
    },
    "awash_in_unknown_tides": {
        "name": "Awash in Unknown Tides",
        "rank": 2,
        "cost": "* to *****",
        "description": "Summon a wellspring from one of the Underworld's Rivers, causing an Environmental Tilt or Extreme Environment proportionate to Plasm spent. Rivers may produce other effects at the Storyteller's discretion.",
        "book": "Mem p.27"
    },
    "lightless_depths": {
        "name": "Lightless Depths",
        "rank": 3,
        "cost": "**",
        "description": "Dissolve all memories formed in your presence while the self is submerged, inflicting Amnesia.",
        "book": "Mem p.28",
        "additional": "●●● to steal a Memory with skin to skin contact, but suffer a crisis point."
    },
    "vortices_of_self_and_memory": {
        "name": "Vortices of Self and Memory",
        "rank": 4,
        "cost": "*+",
        "description": "Fuse two Memories into a new Memory that synthesizes their themes, paying additional Plasm to carry over dots of Memory Skills.",
        "book": "Mem p.28",
        "additional": "●/Resolve to infuse a Memory into a third party, living or dead."
    },
    "remade_in_the_oceans_womb": {
        "name": "Remade in the Ocean's Womb",
        "rank": 5,
        "cost": "●/feature",
        "description": "Take intrinsic features such as Memories, physical characteristics, or dots of Attributes or Merits from a subject submerged in water into yourself.",
        "book": "Mem p.29",
        "additional": "●/feature to graft such an intrinsic feature into a subject submerged in water."
    }
}

# All Haunts dictionary
ALL_HAUNTS = {
    "boneyard": HAUNT_BONEYARD,
    "caul": HAUNT_CAUL,
    "curse": HAUNT_CURSE,
    "dirge": HAUNT_DIRGE,
    "marionette": HAUNT_MARIONETTE,
    "memoria": HAUNT_MEMORIA,
    "oracle": HAUNT_ORACLE,
    "rage": HAUNT_RAGE,
    "shroud": HAUNT_SHROUD,
    "tomb": HAUNT_TOMB,
    "void": HAUNT_VOID,
    "well": HAUNT_WELL
}

# ==================== KEY DETAILS ====================

# Key descriptions with unlock attributes and mechanics
GEIST_KEY_DETAILS = {
    "beasts": {
        "name": "Beasts",
        "full_name": "The Key of Beasts",
        "alternate_names": "The Primeval Key, the Key of Tooth and Claw",
        "attribute": "Wits",
        "description": "The Primeval Key of Tooth and Claw rules all beasts and haunts places hidden or reclaimed from mankind.",
        "doom": "Fail an action due to animal interference.",
        "book": "GTS 2e p.122"
    },
    "blood": {
        "name": "Blood",
        "full_name": "The Key of Blood", 
        "alternate_names": "The Stigmatic Key, the Key of Crimson Agony",
        "attribute": "Presence",
        "description": "The Stigmatic Key of Crimson Agony turns when danger creeps unexpected and inevitable.",
        "doom": "Dramatically fail an action to avoid violence.",
        "book": "GTS 2e p.122"
    },
    "chance": {
        "name": "Chance",
        "full_name": "The Key of Chance",
        "alternate_names": "The Bastard's Key, the Key of Jinx and Hex", 
        "attribute": "Dexterity",
        "description": "The Bastard's Key of Jinx and Hex rules foolhardy gambles, improbable misfortune and dangerous machinery.",
        "doom": "Invert a roll with a +3 bonus into a chance die.",
        "book": "GTS 2e p.122"
    },
    "cold wind": {
        "name": "Cold Wind",
        "full_name": "The Key of Cold Wind",
        "alternate_names": "The Breathless Key, the Key of Gale and Garrote",
        "attribute": "Resolve", 
        "description": "The Breathless Key of Gale and Garrote unlocks conditions of exposure and howling noise.",
        "doom": "Confess a dark secret or suffer Extreme Cold.",
        "book": "GTS 2e p.122"
    },
    "deep waters": {
        "name": "Deep Waters",
        "full_name": "The Key of Deep Waters",
        "alternate_names": "The Tear-Stained Key, the Key of Azure Futility",
        "attribute": "Manipulation",
        "description": "The Tear-Stained Key of Azure Futility haunts through enclosure, submergence and suffocation.",
        "doom": "Reduce a full Willpower refresh to only one point.",
        "book": "GTS 2e p.123"
    },
    "disease": {
        "name": "Disease",
        "full_name": "The Key of Disease",
        "alternate_names": "The Wasting Key, the Key of Plague and Pestilence",
        "attribute": "Stamina",
        "description": "The Wasting Key of Plague and Pestilence turns wherever sickness and poison can be found.",
        "doom": "Suffer the Sick Tilt for a full scene.",
        "book": "GTS 2e p.123"
    },
    "grave dirt": {
        "name": "Grave Dirt",
        "full_name": "The Key of Grave Dirt", 
        "alternate_names": "The Crushing Key, the Key of Slate Bereavement",
        "attribute": "Strength",
        "description": "The Crushing Key of Slate Bereavement haunts subterranean hollows and anything dominated by the past.",
        "doom": "Extended actions cost Willpower unless fed by sacrifice.",
        "book": "GTS 2e p.123"
    },
    "pyre flame": {
        "name": "Pyre Flame",
        "full_name": "The Key of Pyre Flame",
        "alternate_names": "The Burning Key, the Key of Ash and Brand", 
        "attribute": "Intelligence",
        "description": "The Burning Key of Ash and Brand rules fire and extreme heat.",
        "doom": "Destroy a possession of value or suffer Extreme Heat.",
        "book": "GTS 2e p.123"
    },
    "stillness": {
        "name": "Stillness",
        "full_name": "The Key of Stillness",
        "alternate_names": "The Silent Key, the Key of Shroud and Shadow",
        "attribute": "Composure", 
        "description": "The Silent Key of Shroud and Shadow haunts those who are helpless, cornered, or caught unaware.",
        "doom": "You may not speak, dispelling your Haunt if you do.",
        "book": "GTS 2e p.124"
    }
}

