"""
Changeling Contracts for Chronicles of Darkness 2nd Edition.

Contracts in Changeling: The Lost 2e are magical bargains and agreements.
Organized by:
- Contract type (Crown, Jewels, Mirror, Shield, etc.)
- Royal vs Common contracts
- Seasonal contracts (Spring, Summer, Autumn, Winter)
- Goblin contracts

Based on Changeling: The Lost 2nd Edition.
"""

# ==================== ARCADIAN CONTRACTS ====================

# Contracts of the Crown
CONTRACTS_OF_THE_CROWN = {
    "hostile_takeover": {
        "name": "Hostile Takeover",
        "contract_type": "crown",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "One of the owner's possessions",
        "description": "Declare yourself, and up to your Presence in allies beside you, a rightful guest, unharried by protection from intruders.",
        "seeming_benefits": {
            "beast": "Guard animals obey you.",
            "fairest": "+2 to Clash of Wills against owners of supernatural locations."
        },
        "book": "CTL 2e p.128"
    },
    "mask_of_superiority": {
        "name": "Mask of Superiority",
        "contract_type": "crown",
        "cost": "1 glamour",
        "dice_pool": "Presence + Subterfuge + Wyrd",
        "loopholes": "Match the dress code",
        "description": "Apply your Presence as false Status, convincing others you rank in their organization.",
        "seeming_benefits": {
            "fairest": "Bypass a Door in Social Maneuvering.",
            "ogre": "Apply successes as an Intimidation bonus."
        },
        "book": "CTL 2e p.128"
    },
    "paralyzing_presence": {
        "name": "Paralyzing Presence",
        "contract_type": "crown",
        "cost": "2 glamour",
        "dice_pool": "Presence + Intimidation + Wyrd vs Composure + Tolerance",
        "loopholes": "Touch a lone target",
        "description": "Overwhelm a target with your presence, rendering them Insensate.",
        "seeming_benefits": {
            "darkling": "You may substitute Manipulation for Presence.",
            "fairest": "+3 bonus to activate."
        },
        "book": "CTL 2e p.129"
    },
    "summon_the_loyal_servant": {
        "name": "Summon the Loyal Servant",
        "contract_type": "crown",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "A favor for the source element",
        "description": "Conjure a loyal servant from the elements for a scene, like a weak Hedge ghost.",
        "seeming_benefits": {
            "elemental": "Add Glamour and Willpower to merge with the elemental servant and assume its properties.",
            "fairest": "Add Willpower to bind the servant to guard a Hollow indefinitely."
        },
        "book": "CTL 2e p.129"
    },
    "tumult": {
        "name": "Tumult",
        "contract_type": "crown",
        "cost": "2 glamour",
        "dice_pool": "Presence + Empathy + Wyrd - Resolve",
        "loopholes": "Plant folding paper on the subject",
        "description": "Fold a subject's name to read her weaknesses and spend successes on inflicting disorienting Conditions or specifying conditional triggers.",
        "seeming_benefits": {
            "fairest": "Read and inflict Inspired, Swooned, and Wanton.",
            "ogre": "Read and inflict Bestial, Cowed, and Frightened."
        },
        "book": "CTL 2e p.129"
    }
}

# Royal Contracts of the Crown
ROYAL_CONTRACTS_OF_THE_CROWN = {
    "discreet_summons": {
        "name": "Discreet Summons",
        "contract_type": "crown_royal",
        "cost": "1 or 2 glamour",
        "dice_pool": "Manipulation + Persuasion + Wyrd vs Composure + Tolerance",
        "loopholes": "From an enemy's holdings, or for good payment",
        "description": "For one scene, draw out a desired Size 1 object or, with two Glamour, invite a hobgoblin to perform a task.",
        "seeming_benefits": {
            "darkling": "Draw the summons out of shadows.",
            "fairest": "Hobs serve until the next sunrise or sunset."
        },
        "book": "CTL 2e p.130"
    },
    "masterminds_gambit": {
        "name": "Mastermind's Gambit",
        "contract_type": "crown_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Using 50 year old paper",
        "description": "Dramatically monologue a +5 plan into existence for a session.",
        "seeming_benefits": {
            "elemental": "Add Willpower to preserve the plan for a story and expand its bonus to a Mental Specialty.",
            "fairest": "You may conjure an organization instead of a plan."
        },
        "book": "CTL 2e p.130"
    },
    "pipes_of_the_beastcaller": {
        "name": "Pipes of the Beastcaller",
        "contract_type": "crown_royal",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Animal Ken + Wyrd vs Resolve + Composure",
        "loopholes": "A fluting dance",
        "description": "Summon and command animals of a given species with a silver flute.",
        "seeming_benefits": {
            "beast": "Monitor and command the animals from a distance.",
            "fairest": "Add Glamour to affect a second species."
        },
        "book": "CTL 2e p.131"
    },
    "the_royal_court": {
        "name": "The Royal Court",
        "contract_type": "crown_royal",
        "cost": "3 glamour, 1 willpower",
        "dice_pool": "None",
        "loopholes": "A five-minute speech",
        "description": "Forbid violence from breaking out in a mediated gathering.",
        "seeming_benefits": {
            "fairest": "Social violence is also forbidden.",
            "wizened": "Mental violence is also forbidden."
        },
        "book": "CTL 2e p.131"
    },
    "spinning_wheel": {
        "name": "Spinning Wheel",
        "contract_type": "crown_royal",
        "cost": "3 glamour, 1 willpower",
        "dice_pool": "Intelligence + Occult + Wyrd - Resolve",
        "loopholes": "Prick and draw blood",
        "description": "Destine a subject for a certain circumstance or encounter, applying successes as bonuses to approach that destiny or penalties to avoid it.",
        "seeming_benefits": {
            "fairest": "Take +3 and Inspired to destine positive circumstances.",
            "ogre": "Take +3 and Steadfast to destine negative circumstances."
        },
        "book": "CTL 2e p.132"
    }
}

# Contracts of Jewels
CONTRACTS_OF_JEWELS = {
    "blessing_of_perfection": {
        "name": "Blessing of Perfection",
        "contract_type": "jewels",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Bury charged payment",
        "description": "Bless and encourage an object or a Computer, Crafts or Medicine task, substituting your Wyrd as the equipment or Skill dice.",
        "seeming_benefits": {
            "fairest": "Bless an Expression, Persuasion or Socialize task.",
            "wizened": "Blessing lasts for a scene."
        },
        "book": "CTL 2e p.132"
    },
    "changing_fortunes": {
        "name": "Changing Fortunes",
        "contract_type": "jewels",
        "cost": "2 glamour",
        "dice_pool": "Wits + Occult + Wyrd - Resolve",
        "loopholes": "Dramatic failure",
        "description": "Whisper tales to curse or bless a subject's next action, by a two-dice modifier or one-success exceptional threshold shift per success. May target a given subject once per session.",
        "seeming_benefits": {
            "ogre": "Curses inflict Shaken when the same dice pool is rolled, until next sunrise or sunset.",
            "wizened": "You may choose to force a reroll."
        },
        "book": "CTL 2e p.132"
    },
    "light_shy": {
        "name": "Light-Shy",
        "contract_type": "jewels",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "A minute still in darkness",
        "description": "Fade from conscious notice while your actions remain subtle and you inflict no harm or magic.",
        "seeming_benefits": {
            "darkling": "Fade from even inanimate detection.",
            "wizened": "You may target an object."
        },
        "book": "CTL 2e p.133"
    },
    "murkblur": {
        "name": "Murkblur",
        "contract_type": "jewels",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Subterfuge + Wyrd vs Wits + Tolerance",
        "loopholes": "Eat an eye",
        "description": "Blind a target with fantastic distractions for a turn.",
        "seeming_benefits": {
            "elemental": "You may instead convince the target they are immersed in a chosen element, suffering any appropriate Tilt.",
            "wizened": "Also inflict Disoriented."
        },
        "book": "CTL 2e p.133"
    },
    "trivial_reworking": {
        "name": "Trivial Reworking",
        "contract_type": "jewels",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Touch something similar to your chosen Mask",
        "description": "Mask an object up to Size 3.",
        "seeming_benefits": {
            "darkling": "Penalize attempts to detect forgery by your Manipulation.",
            "wizened": "Mask an object of any Size."
        },
        "book": "CTL 2e p.133"
    }
}

# Royal Contracts of Jewels
ROYAL_CONTRACTS_OF_JEWELS = {
    "changeling_hours": {
        "name": "Changeling Hours",
        "contract_type": "jewels_royal",
        "cost": "1 glamour, + 1 glamour per 5 Size",
        "dice_pool": "None",
        "loopholes": "Name a past owner of the object",
        "description": "Grasp and push an object's time, reversing or accelerating its aging or freezing it in place.",
        "seeming_benefits": {
            "elemental": "Push your associated element's time.",
            "wizened": "Spend Willpower to freeze permanently."
        },
        "book": "CTL 2e p.134"
    },
    "dance_of_the_toys": {
        "name": "Dance of the Toys",
        "contract_type": "jewels_royal",
        "cost": "2 glamour",
        "dice_pool": "Manipulation + Crafts + Wyrd",
        "loopholes": "Command the device by name",
        "description": "Operate a mechanical device at will.",
        "seeming_benefits": {
            "beast": "Gift the device with basic intelligence.",
            "wizened": "Cause the device to move beyond its own power, at your Wyrd in Speed."
        },
        "book": "CTL 2e p.134"
    },
    "hidden_reality": {
        "name": "Hidden Reality",
        "contract_type": "jewels_royal",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "A show of searching and finding the feature",
        "description": "Temporarily realize possible imagined features of your surroundings.",
        "seeming_benefits": {
            "fairest": "Contest Manipulation + Subterfuge + Wyrd vs Resolve + Tolerance to reimagine a person's Anchors instead.",
            "wizened": "Add Glamour to instead discover possible objects present."
        },
        "book": "CTL 2e p.134"
    },
    "stealing_the_solid_reflection": {
        "name": "Stealing the Solid Reflection",
        "contract_type": "jewels_royal",
        "cost": "1 glamour, 1 willpower",
        "dice_pool": "Strength + Larceny + Wyrd",
        "loopholes": "A remark of indebtedness from the owner",
        "description": "Pull an object's mundane reflection out of a reflective surface.",
        "seeming_benefits": {
            "fairest": "Pull a person's reflection out as a friendly duplicate with some strange telltale mark.",
            "wizened": "Add Glamour to retain supernatural qualities in the reflection."
        },
        "book": "CTL 2e p.135"
    },
    "tatterdemalions_workshop": {
        "name": "Tatterdemalion's Workshop",
        "contract_type": "jewels_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Glasses and archaic tools",
        "description": "Jury-rig anything up to Size 5 with no tools and only vaguely associated materials, applying half Wyrd (rounded up) as a crafting bonus.",
        "seeming_benefits": {
            "ogre": "Hammer even inappropriate materials into shape.",
            "wizened": "Jury-rig projects of any Size."
        },
        "book": "CTL 2e p.135"
    }
}

# Contracts of the Mirror
CONTRACTS_OF_THE_MIRROR = {
    "glimpse_of_a_distant_mirror": {
        "name": "Glimpse of a Distant Mirror",
        "contract_type": "mirror",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Using an enemy's mirror",
        "description": "Use a reflective surface as a window to look out another surface that has reflected your face",
        "seeming_benefits": {
            "beast": "Look out surfaces reflecting someone who has sworn a promise to you or invoked your name",
            "darkling": "Hear through the window, and you may choose to make it two-way."
        },
        "book": "CTL 2e p.136"
    },
    "know_the_competition": {
        "name": "Know the Competition",
        "contract_type": "mirror",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Socialize + Wyrd vs Composure + Tolerance",
        "loopholes": "Challenged by the subject",
        "description": "Play a game to observe a competitor's Anchors and one Aspiration",
        "seeming_benefits": {
            "beast": "Until dawn, reflect on the competitor as an instant action once to know where he is, what he's doing, and when he plans to leave.",
            "darkling": "Observe up to your Wyrd in competitors."
        },
        "book": "CTL 2e p.136"
    },
    "portents_and_visions": {
        "name": "Portents and Visions",
        "contract_type": "mirror",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Occult + Wyrd vs Composure + Tolerance",
        "loopholes": "Tear up their picture",
        "description": "Enter a glossolalic trance to glimpse an important event in the past or present of a visible subject.",
        "seeming_benefits": {
            "darkling": "You may choose to witness a past transgression and inflict Guilty.",
            "elemental": "You may choose to predict a violent event and confer the benefits of the Giant Merit should it play out."
        },
        "book": "CTL 2e p.137"
    },
    "read_lucidity": {
        "name": "Read Lucidity",
        "contract_type": "mirror",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Empathy + Wyrd vs Composure + Tolerance",
        "loopholes": "Skin contact",
        "description": "Intuit a character's Clarity and any Clarity Conditions.",
        "seeming_benefits": {
            "beast": "You may use an exceptional success as a dice pool to attack Clarity.",
            "darkling": "You may use an exceptional success to confer your Wits as Defense against the subject's next suffered Clarity attack this session."
        },
        "book": "CTL 2e p.137"
    },
    "walls_have_ears": {
        "name": "Walls Have Ears",
        "contract_type": "mirror",
        "cost": "1 glamour per secret",
        "dice_pool": "None",
        "loopholes": "Mortal witnesses hear your secret",
        "description": "Share secrets with an object to learn how it was constructed and how to repair or destroy it, how to best use it, or what was happening when it was last touched.",
        "seeming_benefits": {
            "darkling": "Become Informed about the object's owner, or last owner besides you.",
            "wizened": "Add Glamour to glimpse particular other circumstances around the object."
        },
        "book": "CTL 2e p.138"
    }
}

# Royal Contracts of the Mirror
ROYAL_CONTRACTS_OF_THE_MIRROR = {
    "props_and_scenery": {
        "name": "Props and Scenery",
        "contract_type": "mirror_royal",
        "cost": "1 glamour, 1 willpower",
        "dice_pool": "Manipulation + Persuasion + Wyrd",
        "loopholes": "Within plain sight of others, but no one sees you at the moment.",
        "description": "Copy the form of a present object up to your Size, adding extra bonuses with successes.",
        "seeming_benefits": {
            "darkling": "Remain transformed until the next sunrise or sunset.",
            "ogre": "Copy objects up to twice your Size."
        },
        "book": "CTL 2e p.138"
    },
    "reflections_of_the_past": {
        "name": "Reflections of the Past",
        "contract_type": "mirror_royal",
        "cost": "1 to 5 glamour",
        "dice_pool": "Intelligence + Occult + Wyrd",
        "loopholes": "Spill blood from lethal damage",
        "description": "Rewind a reflective surface to watch a reflected scene from a specified time, ranging in Glamour cost from a week ago to a decade ago.",
        "seeming_benefits": {
            "darkling": "You may ken the reflected past event.",
            "fairest": "You may inflict Leveraged upon one of the reflected characters."
        },
        "book": "CTL 2e p.138"
    },
    "riddle_kith": {
        "name": "Riddle-Kith",
        "contract_type": "mirror_royal",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Larceny + Wyrd vs Composure + Tolerance",
        "loopholes": "Give a gift to someone of the imitated kith",
        "description": "Remold a changeling's fae mien into that of another kith. Face a breaking point with 3 dice upon an unwilling subject.",
        "seeming_benefits": {
            "darkling": "You may replace the subject's kith blessing.",
            "elemental": "You may also alter the subject's apparent seeming."
        },
        "book": "CTL 2e p.139"
    },
    "skinmask": {
        "name": "Skinmask",
        "contract_type": "mirror_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "One of the model's possessions",
        "description": "Recite three details about a mortal or Masked being to copy their appearance with your Mask (and your mien if appropriate).",
        "seeming_benefits": {
            "darkling": "You may purchase the Alternate Identity Merit for one guise, and adopt it reflexively for one Glamour.",
            "fairest": "+3 to mimic the subject by intuition about their ways."
        },
        "book": "CTL 2e p.139"
    },
    "unravel_the_tapestry": {
        "name": "Unravel the Tapestry",
        "contract_type": "mirror_royal",
        "cost": "2 glamour, 1 willpower",
        "dice_pool": "Wits + Occult + Wyrd",
        "loopholes": "A new debt unpaid",
        "description": "Replay the last ten seconds or combat round, with the actions of others unchanged. Once per story, reflexively activate when killed.",
        "seeming_benefits": {
            "darkling": "Move up to your Stealth in yards before time resumes.",
            "wizened": "You may make a surprise attack against one character."
        },
        "book": "CTL 2e p.139"
    }
}

# Contracts of the Shield
CONTRACTS_OF_THE_SHIELD = {
    "cloak_of_night": {
        "name": "Cloak of Night",
        "contract_type": "shield",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Wear black",
        "description": "While sneaking in dim light without drawing attention actively, add half Wyrd (rounded up) to Stealth rolls. You and up to your Dexterity in allies may take a reflexive Stealth action each turn, and your Stealth actions conceal your allies.",
        "seeming_benefits": {
            "darkling": "You may act and draw attention without ending the Contract.",
            "ogre": "You may substitute Stamina for Dexterity."
        },
        "book": "CTL 2e p.140"
    },
    "fae_cunning": {
        "name": "Fae Cunning",
        "contract_type": "shield",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Challenge to a duel",
        "description": "Retain Defense against Firearms and surprise attacks. Successful Dodges may redirect attacks, automatically succeeding by your Presence.",
        "seeming_benefits": {
            "elemental": "Add Resolve as an Initiative and Speed bonus.",
            "ogre": "Damage mundane weapons that strike you by your Stamina."
        },
        "book": "CTL 2e p.140"
    },
    "shared_burden": {
        "name": "Shared Burden",
        "contract_type": "shield",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Skin from the assailant",
        "description": "Shed blood on a subject, suffering resistant lethal damage to heal them at a 1:2 point ratio, healing bashing before lethal.",
        "seeming_benefits": {
            "ogre": "Heal at a 1:3 point ratio.",
            "wizened": "Heal lethal damage before bashing."
        },
        "book": "CTL 2e p.140"
    },
    "thorns_and_brambles": {
        "name": "Thorns and Brambles",
        "contract_type": "shield",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Strew Hedge thorns behind you",
        "description": "Thorns emerge around you, either draining Glamour from those who move quickly through them, forcing a Dexterity + Athletics roll to avoid being Immobilized, or attacking with your Wyrd as a dice pool.",
        "seeming_benefits": {
            "darkling": "Absorb drained Glamour.",
            "ogre": "Penalize Athletics rolls by your Strength."
        },
        "book": "CTL 2e p.141"
    },
    "trapdoor_spiders_trick": {
        "name": "Trapdoor Spider's Trick",
        "contract_type": "shield",
        "cost": "1 glamour, optionally 1 willpower",
        "dice_pool": "None",
        "loopholes": "Lure an enemy through the passage",
        "description": "Cause an open passage to appear sealed for a scene, or with Willpower, until dawn or dusk.",
        "seeming_benefits": {
            "ogre": "Allies may see through the illusion.",
            "wizened": "Force a Clash of Wills to breach the illusion with supernatural senses."
        },
        "book": "CTL 2e p.142"
    }
}

# Royal Contracts of the Shield
ROYAL_CONTRACTS_OF_THE_SHIELD = {
    "fortifying_presence": {
        "name": "Fortifying Presence",
        "contract_type": "shield_royal",
        "cost": "2 glamour",
        "dice_pool": "Presence + Empathy + Wyrd vs Resolve + Tolerance",
        "loopholes": "Profess friendship",
        "description": "Heal two mild Clarity damage, or one severe, through one-on-one interaction with a subject.",
        "seeming_benefits": {
            "fairest": "Confer your Presence as bonus Defense against the subject's next Clarity attack suffered in the story.",
            "ogre": "You may instead make a Clarity attack with Empathy, preventing you from ever healing the subject with this Contract."
        },
        "book": "CTL 2e p.142"
    },
    "hedgewall": {
        "name": "Hedgewall",
        "contract_type": "shield_royal",
        "cost": "2 glamour, 1 willpower",
        "dice_pool": "Intelligence + Survival + Wyrd",
        "loopholes": "Plant a seed from the Hedge",
        "description": "Surround yourself with a fortress of thorns for (10 x Wyrd) yards, conferring substantial concealment from ranged attacks and inflicting lethal damage when climbed.",
        "seeming_benefits": {
            "beast": "Enemies in the fort take -2 to Resolve.",
            "ogre": "Lasts until next sunrise or sunset."
        },
        "book": "CTL 2e p.142"
    },
    "pure_clarity": {
        "name": "Pure Clarity",
        "contract_type": "shield_royal",
        "cost": "2 glamour, 1 willpower",
        "dice_pool": "Resolve + Composure + Wyrd",
        "loopholes": "Wear a gauntlet and silk glove",
        "description": "Steel yourself to shrug off one breaking point caused by your actions within a scene.",
        "seeming_benefits": {
            "fairest": "You may shrug off breaking points independent of your actions.",
            "ogre": "You may instead shield an ally from a breaking point."
        },
        "book": "CTL 2e p.143"
    },
    "vow_of_no_compromise": {
        "name": "Vow of No Compromise",
        "contract_type": "shield_royal",
        "cost": "1 glamour, 1 willpower",
        "dice_pool": "None",
        "loopholes": "Destroy a symbol of the Gentry",
        "description": "Touch a subject and become Stoic to downgrade a point of aggravated damage.",
        "seeming_benefits": {
            "ogre": "Become Inspired to seek vengeance.",
            "elemental": "Treat the immersion of your associated element as a touch."
        },
        "book": "CTL 2e p.143"
    },
    "whispers_of_morning": {
        "name": "Whispers of Morning",
        "contract_type": "shield_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Unarmed and unarmored",
        "description": "Become insubstantial like a Hedge ghost.",
        "seeming_benefits": {
            "ogre": "Carry a subject with you. If unwilling, contest Presence + Occult + Wyrd vs Stamina + Tolerance.",
            "wizened": "Pick Size 1 objects up to dissolve them with you. You may choose to materialize them when setting them down."
        },
        "book": "CTL 2e p.143"
    }
}

# Contracts of the Steed
CONTRACTS_OF_THE_STEED = {
    "boon_of_the_scuttling_spider": {
        "name": "Boon of the Scuttling Spider",
        "contract_type": "steed",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Swallow a spider",
        "description": "Cross walls, ceilings, and treacherous terrain freely.",
        "seeming_benefits": {
            "beast": "Successful grapples may restrain like exceptional successes.",
            "darkling": "+2 to Stealth when crossing."
        },
        "book": "CTL 2e p.144"
    },
    "dreamsteps": {
        "name": "Dreamsteps",
        "contract_type": "steed",
        "cost": "1 glamour",
        "dice_pool": "Intelligence + Empathy + Wyrd vs Fortification",
        "loopholes": "A childhood comfort of yours or your Touchstone's",
        "description": "Touch a sleeper and enter their dream in Dream Form.",
        "seeming_benefits": {
            "beast": "Adopt an observed nightmare as your mien and inflict Spooked on the dreamer within the chapter.",
            "fairest": "Become Informed about the dreamer's inner life."
        },
        "book": "CTL 2e p.144"
    },
    "nevertread": {
        "name": "Nevertread",
        "contract_type": "steed",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Leave a calling card somewhere",
        "description": "Supernaturally conceal your tracks.",
        "seeming_benefits": {
            "beast": "Also conceal the tracks of allies up to twice your Stealth.",
            "wizened": "Trap your hidden tracks like a Safe Place with a rating of your Dexterity."
        },
        "book": "CTL 2e p.144"
    },
    "pathfinder": {
        "name": "Pathfinder",
        "contract_type": "steed",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Prick yourself on the thorns",
        "description": "Dowse your way to a given feature of the Hedge.",
        "seeming_benefits": {
            "beast": "Intuit the presence and hostility of Hedge locals.",
            "wizened": "Identify found goblin fruit and whether they are safe to eat."
        },
        "book": "CTL 2e p.144"
    },
    "seven_league_leap": {
        "name": "Seven-League Leap",
        "contract_type": "steed",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Boots newly stolen from an enemy",
        "description": "Clear (10 x Wyrd) yards with a Strength + Athletics leap.",
        "seeming_benefits": {
            "beast": "+10 Speed for a scene, and in a foot chase, take the Edge.",
            "ogre": "Leap as an unarmed attack at +2, inflicting Knocked Down."
        },
        "book": "CTL 2e p.145"
    }
}

# Royal Contracts of the Steed
ROYAL_CONTRACTS_OF_THE_STEED = {
    "chrysalis": {
        "name": "Chrysalis",
        "contract_type": "steed_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Near the chosen animal in its habitat",
        "description": "Transform into one of two Size 1-7 animals chosen when you buy this Contract, able to communicate with fellow such animals.",
        "seeming_benefits": {
            "beast": "Choose another two animal forms.",
            "ogre": "Choose animals up to Size 15."
        },
        "book": "CTL 2e p.145"
    },
    "flickering_hours": {
        "name": "Flickering Hours",
        "contract_type": "steed_royal",
        "cost": "1 glamour, optionally 1 willpower",
        "dice_pool": "Wits + Occult + Wyrd vs Resolve + Tolerance",
        "loopholes": "Smash an antique timepiece",
        "description": "Individually half or double the rate of time through the Hedge for yourself, or with Willpower, fellow travellers or pursuers. Until next sunrise or sunset, confer the Edge and the Fleet of Foot Merit with a rating of your Wyrd on quickened beneficiaries. Roll only if contested.",
        "seeming_benefits": {
            "beast": "When you spend Willpower, you may include subjects later encountered along the way.",
            "elemental": "Inflict the effects of the Ice Tilt to traverse your wake, reskinned for your appropriate element."
        },
        "book": "CTL 2e p.146"
    },
    "leaping_toward_nightfall": {
        "name": "Leaping Toward Nightfall",
        "contract_type": "steed_royal",
        "cost": "3 glamour, 1 willpower",
        "dice_pool": "Intelligence + Occult + Wyrd vs Resolve + Tolerance",
        "loopholes": "A piece of the Hedge",
        "description": "Push a character or object up to Size 10 forward in time with a riddle for a set duration up to your successes in days.",
        "seeming_benefits": {
            "beast": "You may inflict Disoriented for a scene when the target reappears.",
            "darkling": "Erase the scene from which the target was pushed from their memory."
        },
        "book": "CTL 2e p.146"
    },
    "mirror_walk": {
        "name": "Mirror Walk",
        "contract_type": "steed_royal",
        "cost": "1 glamour, 1 willpower",
        "dice_pool": "Wits + Survival + Wyrd",
        "loopholes": "The name of someone reflected on the other side",
        "description": "Reach or travel through reflective surfaces, into one nearby and out one you have touched before.",
        "seeming_benefits": {
            "beast": "You may remain in the reflected world without exiting, at +2 to navigate.",
            "elemental": "Exit invisible for your successes in minutes."
        },
        "book": "CTL 2e p.146"
    },
    "talon_and_wing": {
        "name": "Talon and Wing",
        "contract_type": "steed_royal",
        "cost": "1 glamour per effect",
        "dice_pool": "None",
        "loopholes": "Eat a piece of the chosen animal",
        "description": "Gain the +10 Speed, the +3 perception senses, and/or the upgraded unarmed damage of a chosen animal.",
        "seeming_benefits": {
            "beast": "Ignore fatigue.",
            "darkling": "Add Glamour to develop a grave Poison with your Wyrd in Toxicity."
        },
        "book": "CTL 2e p.147"
    }
}

# Contracts of the Sword
CONTRACTS_OF_THE_SWORD = {
    "elemental_weapon": {
        "name": "Elemental Weapon",
        "contract_type": "sword",
        "cost": "2 glamour",
        "dice_pool": "Presence + Survival + Wyrd",
        "loopholes": "Perform a trick with the element",
        "description": "Fashion an archaic weapon from the elements, applying successes to increase weapon rating or range or reduce Initiative penalty.",
        "seeming_benefits": {
            "darkling": "Shadow weapons may blind instead of damaging.",
            "elemental": "Wield a weapon of the appropriate element and contest Presence + Intimidation vs Stamina + Tolerance to stun a foe."
        },
        "book": "CTL 2e p.147"
    },
    "might_of_the_terrible_brute": {
        "name": "Might of the Terrible Brute",
        "contract_type": "sword",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Fight multiple opponents at once",
        "description": "Add a grapple maneuver to steal the opponent's Strength, immobilizing them when emptied.",
        "seeming_benefits": {
            "beast": "The maneuver may steal Dexterity instead.",
            "elemental": "Gain the benefits of the Giant Merit."
        },
        "book": "CTL 2e p.148"
    },
    "overpowering_dread": {
        "name": "Overpowering Dread",
        "contract_type": "sword",
        "cost": "1 glamour",
        "dice_pool": "Presence + Intimidation + Wyrd vs Composure + Tolerance",
        "loopholes": "In shadow",
        "description": "Frighten a subject into fleeing.",
        "seeming_benefits": {
            "elemental": "Contest two subjects at once.",
            "fairest": "Console and take advantage of the subject's fear to instead inflict Swooned."
        },
        "book": "CTL 2e p.148"
    },
    "primal_glory": {
        "name": "Primal Glory",
        "contract_type": "sword",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Ingest the element",
        "description": "Embrace an element as 1/1 Armor that deals lethal damage in close contact. Suffer no damage from the element as it is, and half magical damage from it.",
        "seeming_benefits": {
            "elemental": "Extend damage from the appropriate element for your Wyrd in yards.",
            "ogre": "Suffer no damage from even magical forms of the element."
        },
        "book": "CTL 2e p.148"
    },
    "touch_of_wrath": {
        "name": "Touch of Wrath",
        "contract_type": "sword",
        "cost": "1 glamour",
        "dice_pool": "Intelligence + Crafts + Wyrd",
        "loopholes": "Leave a handprint",
        "description": "Cause Structure damage to an object with touch and threats.",
        "seeming_benefits": {
            "elemental": "Double damage against natural materials.",
            "wizened": "Harm the object with a gaze."
        },
        "book": "CTL 2e p.148"
    }
}

# Royal Contracts of the Sword
ROYAL_CONTRACTS_OF_THE_SWORD = {
    "elemental_fury": {
        "name": "Elemental Fury",
        "contract_type": "sword_royal",
        "cost": "1 glamour per tilt (1 glamour + 20 yards)",
        "dice_pool": "None",
        "loopholes": "Rage and rave",
        "description": "Conjure Environmental Tilts from the elements.",
        "seeming_benefits": {
            "elemental": "Inflict your Presence in bashing damage within the area.",
            "fairest": "The Tilts stay their hand against your allies."
        },
        "book": "CTL 2e p.149"
    },
    "oathbreakers_punishment": {
        "name": "Oathbreaker's Punishment",
        "contract_type": "sword_royal",
        "cost": "2 glamour",
        "dice_pool": "Wits + Empathy + Wyrd - Composure",
        "loopholes": "Promisesworn to you",
        "description": "Intuit the most serious promise a person has broken without making amends. You may harrow the person within the fortnight with a waking nightmare for each success.",
        "seeming_benefits": {
            "elemental": "Expose the subject's guilt, inflicting Notoriety.",
            "wizened": "Know the details of the breaking of the promise."
        },
        "book": "CTL 2e p.149"
    },
    "red_revenge": {
        "name": "Red Revenge",
        "contract_type": "sword_royal",
        "cost": "3 glamour",
        "dice_pool": "None",
        "loopholes": "Avenging a friend",
        "description": "Go Berserk. Take 3/3 Armor and +3 to Initiative, Intimidation, and Physical dice pools.",
        "seeming_benefits": {
            "elemental": "Close combat attacks gain a +1 weapon bonus.",
            "ogre": "Your strikes Knock Down."
        },
        "book": "CTL 2e p.149"
    },
    "relentless_pursuit": {
        "name": "Relentless Pursuit",
        "contract_type": "sword_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Old running shoes",
        "description": "Name your quarry to intuit their direction, distance, and dimension from you until next sunrise or sunset.",
        "seeming_benefits": {
            "beast": "Envision your quarry's current situation.",
            "elemental": "Add Glamour when the sun reaches the horizon to reset the Contract's duration and add a cumulative +1 to pursue."
        },
        "book": "CTL 2e p.150"
    },
    "thief_of_reason": {
        "name": "Thief of Reason",
        "contract_type": "sword_royal",
        "cost": "1 glamour, 1 willpower",
        "dice_pool": "Presence + Subterfuge + Wyrd - Resolve",
        "loopholes": "Victim expresses doubt in their sanity",
        "description": "Roll successes as a Clarity attack, or an attack to temporarily reduce another stability trait. The attack also saps Willpower. Suffer a breaking point at 4 dice.",
        "seeming_benefits": {
            "beast": "You may contest Presence + Intimidation + Wyrd vs Composure + Tolerance to provoke a Fugue in the victim.",
            "fairest": "Add Glamour to name a conditional trigger that hangs for a day."
        },
        "book": "CTL 2e p.150"
    }
}

# Contracts of Chalice
CONTRACTS_OF_CHALICE = {
    "filling_the_cup": {
        "name": "Filling the Cup",
        "contract_type": "chalice",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Speak current emotion for all to hear",
        "description": "Identify people feeling powerful emotions within (Wyrd x 40)m radius.",
        "seeming_benefits": {
            "beast": "Identify specific people by feeling alone if other contracts have already been applied.",
            "fairest": "Pick out anyone feeling strong emotions about the Fairest."
        },
        "book": "K&K p.34"
    },
    "frail_as_the_dying_word": {
        "name": "Frail as the Dying Word",
        "contract_type": "chalice",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Occult + Wyrd vs Composure + Tolerance",
        "loopholes": "Caster has experienced the frailty within the same scene",
        "description": "Inflict own minor frailty onto target, or major frailty if target already has it.",
        "seeming_benefits": {
            "fairest": "Inflict frailty from any fae present rather than own.",
            "darkling": "Pay additional Glamour to transfer frailty rather than sharing it."
        },
        "book": "K&K p.35"
    },
    "sleeps_sweet_embrace": {
        "name": "Sleep's Sweet Embrace",
        "contract_type": "chalice",
        "cost": "2 glamour, 1 willpower",
        "dice_pool": "Manipulation + Expression + Wyrd - Resolve",
        "loopholes": "Make a sleepy drink that target drinks within the scene.",
        "description": "With a touch, the target does not dream for nights/successes. Accelerated Lethal healing, but don't regain Willpower and immune to oneiromancy.",
        "seeming_benefits": {
            "beast": "Add two days to the duration.",
            "darkling": "Target appears dead while asleep, clash of wills to perceive they are alive."
        },
        "book": "K&K p.35"
    },
    "curses_cure": {
        "name": "Curse's Cure",
        "contract_type": "chalice",
        "cost": "1 glamour",
        "dice_pool": "Intelligence + Medicine + Wyrd",
        "loopholes": "Changeling tastes the toxin they intend to cure.",
        "description": "Drink potion to heal from poison more quickly or survive a deadly poison.",
        "seeming_benefits": {
            "beast": "Inflict the moderate Poisoned Tilt in a grapple move by biting the target.",
            "wizened": "Reduce severity of a disease or end the effects of a drug in the target's system."
        },
        "book": "K&K p.36"
    },
    "dreamers_phalanx": {
        "name": "Dreamer's Phalanx",
        "contract_type": "chalice",
        "cost": "1 glamour + 1 glamour per subject beyond 2nd",
        "dice_pool": "None",
        "loopholes": "All participants are part of the same sworn Oath.",
        "description": "Connect Bastions of all participating dreamers, creating shared Bastion with greater fortifications and 8-again on teamwork oneiromancy.",
        "seeming_benefits": {
            "beast": "Participants get +2 to actions contested by external intruders.",
            "wizened": "Teamwork actions are exceptional at 3 successes within shared or individual Bastions."
        },
        "book": "K&K p.36"
    }
}

# Royal Contracts of Chalice
ROYAL_CONTRACTS_OF_CHALICE = {
    "closing_deaths_door": {
        "name": "Closing Death's Door",
        "contract_type": "chalice_royal",
        "cost": "3 glamour, 1 willpower",
        "dice_pool": "Manipulation + Empathy + Wyrd",
        "loopholes": "The Changeling tries to revive a Touchstone, or someone they share an oath with.",
        "description": "Revive a corpse that has died within 1 chapter of the scene, gaining Goblin Debt/hours dead.",
        "seeming_benefits": {
            "darkling": "Gain a vision of their last moments before death.",
            "fairest": "Revived character gains the Swooned Condition."
        },
        "book": "K&K p.36"
    },
    "feast_of_plenty": {
        "name": "Feast of Plenty",
        "contract_type": "chalice_royal",
        "cost": "2 glamour",
        "dice_pool": "Presence + Socialize + Wyrd",
        "loopholes": "Greet everyone present by name and welcoming gesture.",
        "description": "Summon a feast that removes physical Conditions or Tilts and replenishes Willpower. Participants gain the Indebted Condition.",
        "seeming_benefits": {
            "elemental": "Anyone perceiving the feast rolls Composure + Wyrd to resist partaking.",
            "ogre": "Participants gain +1 Defense for the chapter."
        },
        "book": "K&K p.37"
    },
    "still_waters_run_deep": {
        "name": "Still Waters Run Deep",
        "contract_type": "chalice_royal",
        "cost": "2 glamour",
        "dice_pool": "Manipulation + Subterfuge + Wyrd - Resolve",
        "loopholes": "Changeling writes a paragraph about their emotions and seals it in a bottle.",
        "description": "Suppress a number of emotional Conditions equal to successes. Target cannot perform Hedgespinning, dreamweaving, incite Bedlam or harvest Glamour while under the effect.",
        "seeming_benefits": {
            "wizened": "Can suppress emotional or mental Conditions.",
            "ogre": "Can resolve one of the target's suppressed Conditions and gain the Beat instead."
        },
        "book": "K&K p.38"
    },
    "poison_the_well": {
        "name": "Poison the Well",
        "contract_type": "chalice_royal",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Expression + Wyrd - Resolve + Tolerance",
        "loopholes": "The Changeling personally influences or sabotages the target Merit.",
        "description": "Remove access to mundane Social Merits for the duration; merits turn against the target as if betrayed. If in the Hedge, can target some fae merits.",
        "seeming_benefits": {
            "fairest": "Gain access to the Merit targeted for the duration.",
            "elemental": "Merit returns at rate of one dot per scene rather than at once."
        },
        "book": "K&K p.38"
    },
    "shared_cup": {
        "name": "Shared Cup",
        "contract_type": "chalice_royal",
        "cost": "1 glamour + 1 glamour per subject beyond 2nd",
        "dice_pool": "Presence + Occult + Wyrd vs Composure + Tolerance",
        "loopholes": "Consume small part of body such as nail clipping from all participants.",
        "description": "Sharing a meal binds participants, lowering exceptional threshold for Hedgespinning and Bedlam, empathically linking them and sharing WP and Glamour refreshes.",
        "seeming_benefits": {
            "darkling": "Pay 1 Glamour to cut self off from the others and resist the effects.",
            "fairest": "All participants suffer the Swooned Condition."
        },
        "book": "K&K p.39"
    }
}

# Contracts of Coin
CONTRACTS_OF_COIN = {
    "book_of_black_and_red": {
        "name": "Book of Black and Red",
        "contract_type": "coin",
        "cost": "1 glamour",
        "dice_pool": "Wits + Academics + Wyrd vs Resolve + Tolerance",
        "loopholes": "The target lets the Changeling examine their records in the scene.",
        "description": "Learn 5 most significant debts and sworn obligations of a target, whether mundane or magical. Exploiting knowledge is at +2; target takes the Leveraged Condition.",
        "seeming_benefits": {
            "darkling": "Choose a non-magical debt and make the target owe the Changeling instead.",
            "wizened": "Only three successes needed to exploit knowledge to influence target's debts."
        },
        "book": "K&K p.39"
    },
    "give_and_take": {
        "name": "Give and Take",
        "contract_type": "coin",
        "cost": "1 glamour or 2 glamour",
        "dice_pool": "None",
        "loopholes": "Changeling and target exchange physical gifts they haven't given each other before.",
        "description": "Choose number of points up to half Wyrd from Glamour, Willpower or personal merits. Exchange these with the target.",
        "seeming_benefits": {
            "ogre": "Trade points of mild Clarity damage as well.",
            "wizened": "Exchange doesn't have to be equal, but target must still consent."
        },
        "book": "K&K p.40"
    },
    "beggar_knight": {
        "name": "Beggar Knight",
        "contract_type": "coin",
        "cost": "2 glamour",
        "dice_pool": "Manipulation + Academics + Wyrd - Composure",
        "loopholes": "The victim benefited from other people's hard work during the scene.",
        "description": "Curse a victim to lose equipment bonuses, resources or teamwork bonuses if these were not personally created by the target.",
        "seeming_benefits": {
            "elemental": "Mundane belongings the victim did not make also degrade.",
            "wizened": "Payments given to others also degrade, denying anyone else access to their Resource dots."
        },
        "book": "K&K p.40"
    },
    "coin_mark": {
        "name": "Coin Mark",
        "contract_type": "coin",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Permanently mark object with own name.",
        "description": "Enchant a small object to know its location respective to hers, sensing when it changes hands and learning the identity of the owner. Inflict Avarice by spending additional Glamour.",
        "seeming_benefits": {
            "beast": "Give Apprehensive Condition instead of Avarice.",
            "wizened": "Snap fingers and make the object return to their possession."
        },
        "book": "K&K p.41"
    },
    "grease_the_wheels": {
        "name": "Grease the Wheels",
        "contract_type": "coin",
        "cost": "1 glamour",
        "dice_pool": "Presence + Persuasion + Wyrd",
        "loopholes": "The target accepts a bribe or gift from the changeling.",
        "description": "Interact with member of organisation or bureaucracy to resolve issues with no difficulties and extremely fast, even if not physically possible.",
        "seeming_benefits": {
            "darkling": "Interactions are traceless unless convenient for the Darkling.",
            "fairest": "Gain the Connected Condition regarding the organisation."
        },
        "book": "K&K p.41"
    }
}

# Royal Contracts of Coin
ROYAL_CONTRACTS_OF_COIN = {
    "blood_debt": {
        "name": "Blood Debt",
        "contract_type": "coin_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "The changeling wears jewelry or other accessories that freshly pierce the skin.",
        "description": "Inflict variable points of lethal damage to someone who inflicts L/Agg/Clarity damage.",
        "seeming_benefits": {
            "elemental": "Baseline is two Lethal, rather than one.",
            "ogre": "Protection extended to all allies as long as Changeling is conscious."
        },
        "book": "K&K p.42"
    },
    "exchange_of_gilded_contracts": {
        "name": "Exchange of Gilded Contracts",
        "contract_type": "coin_royal",
        "cost": "3 glamour",
        "dice_pool": "None",
        "loopholes": "Wear reasonably convincing masks of each other.",
        "description": "Exchange a common Contract with a consenting target.",
        "seeming_benefits": {
            "darkling": "Exploit loophole on the traded Contract.",
            "ogre": "Changeling does not lose access to their borrowed Contract, being able to use both."
        },
        "book": "K&K p.42"
    },
    "golden_promise": {
        "name": "Golden Promise",
        "contract_type": "coin_royal",
        "cost": "2 glamour",
        "dice_pool": "Presence + Socialize + Wyrd - Availability",
        "loopholes": "Changeling arrives on the scene with a display of ostentatious wealth.",
        "description": "Reduce Availability of single service by number of successes rolled.",
        "seeming_benefits": {
            "fairest": "Split successes between multiple services.",
            "wizened": "Gain a +1 equipment bonus for acquired service."
        },
        "book": "K&K p.38"
    },
    "grand_revel_of_the_harvest": {
        "name": "Grand Revel of the Harvest",
        "contract_type": "coin_royal",
        "cost": "3 glamour, 1 willpower",
        "dice_pool": "None",
        "loopholes": "The Changeling supplies a banquet large enough for everyone and also partakes.",
        "description": "Enhance the senses; anyone engaging in celebration needs only 3 successes on Social rolls for exceptional success, as well as additional Willpower and Clarity gain.",
        "seeming_benefits": {
            "beast": "All partiers gain +2 bonus to Physical rolls to celebrate.",
            "fairest": "Social manouvering attitudes improve by two steps rather than one."
        },
        "book": "K&K p.43"
    },
    "thirty_pieces": {
        "name": "Thirty Pieces",
        "contract_type": "coin_royal",
        "cost": "3 glamour",
        "dice_pool": "Wits + Empathy + Wyrd vs Resolve + Tolerance",
        "loopholes": "Target accepted payment from the changeling to betray their fellows, even if they don't intend to follow through.",
        "description": "Name an action that the target will take that will betray the target's allies, friends or cause; the target will do it and gain the Guilty Condition after.",
        "seeming_benefits": {
            "darkling": "Target also gains the Notoriety Condition.",
            "elemental": "Safeguards or defenses that could have prevented the treachery will fail."
        },
        "book": "K&K p.44"
    }
}

# Contracts of Stars
CONTRACTS_OF_STARS = {
    "pole_star": {
        "name": "Pole Star",
        "contract_type": "stars",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Hold a piece of the target in their hand.",
        "description": "Name a person, place or item; the changeling's body acts like a compass and leads them to it. This only works in the mundane realm.",
        "seeming_benefits": {
            "beast": "The Changeling has +2 to Clash of Wills to uncover a hidden target.",
            "wizened": "Ask the Storyteller one question about an opponent or obstacle along the path."
        },
        "book": "K&K p.49"
    },
    "straight_on_til_morning": {
        "name": "Straight On 'Til Morning",
        "contract_type": "stars",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Promise to sleep when the task is done and have the statement sealed.",
        "description": "Tireless, suffering no Environmental Tilts, and take 8 again while navigating the Wishing Roads.",
        "seeming_benefits": {
            "fairest": "Affect number of travelers up to Wyrd.",
            "ogre": "Gain the Steadfast Condition."
        },
        "book": "K&K p.49"
    },
    "cynosure": {
        "name": "Cynosure",
        "contract_type": "stars",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Empathy + Wyrd vs Composure + Tolerance",
        "loopholes": "Let an opportunity to one of their own Aspirations slip by.",
        "description": "Discover one of the target's Aspirations; stars guide the changeling to find opportunities that would help the target achieve the Aspiration.",
        "seeming_benefits": {
            "darkling": "Gain the Condition Informed (Aspiration).",
            "ogre": "Add +2 to rolls to convince the target to be bold in seeking their fate."
        },
        "book": "K&K p.49"
    },
    "shooting_star": {
        "name": "Shooting Star",
        "contract_type": "stars",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Complete own creative work within the same scene.",
        "description": "Target someone who does creative work. They gain 1 Fame and provide more Glamour when used in harvesting.",
        "seeming_benefits": {
            "beast": "Athletes and others who perform physical excellence can be targeted.",
            "fairest": "Gain +2 to rolls to harvest Glamour."
        },
        "book": "K&K p.50"
    },
    "retrograde": {
        "name": "Retrograde",
        "contract_type": "stars",
        "cost": "1 glamour",
        "dice_pool": "Presence + Expression + Wyrd vs Resolve + Tolerance",
        "loopholes": "Changeling spins around widdershins while telling the story of misfortune.",
        "description": "Routine matters for the target go wrong in minor misfortunes.",
        "seeming_benefits": {
            "darkling": "Choose specific things that will go wrong, rather than anything.",
            "elemental": "Environmental or weather based Tilt affects the target also."
        },
        "book": "K&K p.50"
    }
}

# Royal Contracts of Stars
ROYAL_CONTRACTS_OF_STARS = {
    "frozen_star": {
        "name": "Frozen Star",
        "contract_type": "stars_royal",
        "cost": "2 glamour",
        "dice_pool": "Intelligence + (Empathy or Persuasion) + Wyrd vs Resolve + Tolerance",
        "loopholes": "Changeling is in physical contact with a piece of the target.",
        "description": "Choose a subject (cannot be the Changeling) and a target (can be the Changeling). For the duration of the Contract, the subject must travel to the target to make physical contact and suffers the Shaken Condition.",
        "seeming_benefits": {
            "darkling": "Inflict the Spooked Condition on the target.",
            "fairest": "If the Fairest is the target, they gain points of Goblin Debt from the subject while they are separated."
        },
        "book": "K&K p.51"
    },
    "star_light_star_bright": {
        "name": "Star Light, Star Bright",
        "contract_type": "stars_royal",
        "cost": "1 glamour or 2 glamour",
        "dice_pool": "None",
        "loopholes": "Coax the target into making a wish",
        "description": "Learn a wish the target has made in the last month; you must fulfill the wish (with some artistic license) or gain Oathbreaker Condition, but fulfilling the wish regains Willpower and a Beat, and you can teleport to the side of someone you have an Enchanted Bargain with (and can spend Glamour to take others along)",
        "seeming_benefits": {
            "ogre": "If the target is non-Fae, get +2 to harvest Glamour from them.",
            "wizened": "Learn the motivations and events driving the wish."
        },
        "book": "K&K p.51"
    },
    "light_of_ancient_stars": {
        "name": "Light of Ancient Stars",
        "contract_type": "stars_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Sing the names of stars in a constellation currently in the sky.",
        "description": "Ask questions about a past event the Changeling is personally connected to.",
        "seeming_benefits": {
            "darkling": "Gain Informed condition about the event",
            "wizened": "Gain a clear vision about a simple object present at the event, and gain a bonus to create a facsimile of it, including accurately reproducing any writing or diagrams."
        },
        "book": "K&K p.51"
    },
    "pinch_of_stardust": {
        "name": "Pinch of Stardust",
        "contract_type": "stars_royal",
        "cost": "3 glamour, 1 willpower",
        "dice_pool": "Intelligence + Crafts + Wyrd vs Resolve + Tolerance",
        "loopholes": "Add something of the Changeling to the creature's parts.",
        "description": "Create an entity from scraps and star stuff; it becomes a Touchstone for the target and inflicts the Delusional Condition, causing breaking points in caster and target.",
        "seeming_benefits": {
            "darkling": "The Darkling hears any secrets the target whispers to the creature.",
            "wizened": "The creation lasts until the end of the story, rather than chapter."
        },
        "book": "K&K p.52"
    }
}

# Goblin Contracts
GOBLIN_CONTRACTS = {
    "blessing_of_forgetfulness": {
        "name": "Blessing of Forgetfulness",
        "contract_type": "goblin",
        "cost": "2 glamour",
        "dice_pool": "Manipulation + Subterfuge + Wyrd vs Composure + Tolerance",
        "loopholes": "Painful events you helped weather",
        "description": "Overwrite the memory of one incident with an innocuous replacement.",
        "seeming_benefits": {},
        "book": "CTL 2e p.162"
    },
    "glib_tongue": {
        "name": "Glib Tongue",
        "contract_type": "goblin",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "A harmful lie",
        "description": "Tell a lie which mortals always believe. Add your Wyrd as a Subterfuge bonus against supernatural listeners.",
        "seeming_benefits": {},
        "book": "CTL 2e p.162"
    },
    "goblins_eye": {
        "name": "Goblin's Eye",
        "contract_type": "goblin",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Mark your eyelids with owl's feather ashes",
        "description": "You may Clash of Wills to pierce magical concealment by kenning, and ask questions about the nature of a kenned supernatural effect.",
        "seeming_benefits": {},
        "book": "CTL 2e p.163"
    },
    "goblins_luck": {
        "name": "Goblin's Luck",
        "contract_type": "goblin",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Rivals also benefit",
        "description": "Benefit from lucky circumstances.",
        "seeming_benefits": {},
        "book": "CTL 2e p.163"
    },
    "huntsmans_clarion": {
        "name": "Huntsman's Clarion",
        "contract_type": "goblin",
        "cost": "2 glamour",
        "dice_pool": "Wits + Empathy + Wyrd",
        "loopholes": "Blindfolded",
        "description": "Detect the presence, but not location, of Arcadian forces for a mile per Wyrd, starting in the Hedge.",
        "seeming_benefits": {},
        "book": "CTL 2e p.163"
    },
    "lost_visage": {
        "name": "Lost Visage",
        "contract_type": "goblin",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Leave behind a telltale possession",
        "description": "Erase yourself from memories of a scene. Supernatural memories force a Clash of Wills, and Gentry and Huntsmen are immune.",
        "seeming_benefits": {},
        "book": "CTL 2e p.163"
    },
    "mantle_mask": {
        "name": "Mantle Mask",
        "contract_type": "goblin",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Decorate the flesh appropriately",
        "description": "Appear to assume a different Court Mantle, or lack thereof.",
        "seeming_benefits": {},
        "book": "CTL 2e p.164"
    },
    "sight_of_truth_and_lies": {
        "name": "Sight of Truth and Lies",
        "contract_type": "goblin",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Business occasion",
        "description": "So long as you tell no lies, identify mundane lies and force a Clash of Wills against supernatural lies.",
        "seeming_benefits": {},
        "book": "CTL 2e p.164"
    },
    "uncanny": {
        "name": "Uncanny",
        "contract_type": "goblin",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Untrained",
        "description": "Take the rote quality on your next nonmagical, unresisted and uncontested rolled action.",
        "seeming_benefits": {},
        "book": "CTL 2e p.164"
    },
    "wayward_guide": {
        "name": "Wayward Guide",
        "contract_type": "goblin",
        "cost": "1 glamour per subject",
        "dice_pool": "None",
        "loopholes": "Lose your way too",
        "description": "Alter signs and markers to make mortals lose their way. You may target yourself to force a Clash of Wills against supernatural trackers.",
        "seeming_benefits": {},
        "book": "CTL 2e p.164"
    }
}

# ==================== SEASONAL CONTRACTS ====================

# Contracts of Spring
CONTRACTS_OF_SPRING = {
    "cupids_arrow": {
        "name": "Cupid's Arrow",
        "contract_type": "spring",
        "cost": "1 glamour",
        "dice_pool": "Wits + Empathy + Mantle vs Composure + Tolerance",
        "loopholes": "Ivy flower",
        "description": "Learn a subject's most ardent desire, and any associated Conditions or Tilts. You may refocus them around a new desire for a scene.",
        "seeming_benefits": {},
        "book": "CTL 2e p.151"
    },
    "dreams_of_the_earth": {
        "name": "Dreams of the Earth",
        "contract_type": "spring",
        "cost": "2 glamour",
        "dice_pool": "Presence + Expression + Mantle vs Composure + Tolerance",
        "loopholes": "Sand in their eyes",
        "description": "Lull a subject to sleep, which only lethal damage may interrupt for a minute per success.",
        "seeming_benefits": {},
        "book": "CTL 2e p.151"
    },
    "gift_of_warm_breath": {
        "name": "Gift of Warm Breath",
        "contract_type": "spring",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Feed them with your own cooking",
        "description": "Heal a subject of fatigue and bashing damage.",
        "seeming_benefits": {},
        "book": "CTL 2e p.151"
    },
    "springs_kiss": {
        "name": "Spring's Kiss",
        "contract_type": "spring",
        "cost": "1 glamour, optionally +1 glamour",
        "dice_pool": "None",
        "loopholes": "Yellow rain gear",
        "description": "Inflict Heavy Rain, and for extra Glamour, Flooded.",
        "seeming_benefits": {},
        "book": "CTL 2e p.151"
    },
    "wyrd_faced_stranger": {
        "name": "Wyrd-Faced Stranger",
        "contract_type": "spring",
        "cost": "*",
        "dice_pool": "Presence + Subterfuge + Mantle vs Composure + Tolerance",
        "loopholes": "A token of sentimental value",
        "description": "Appear as whom a subject most wants to see. Add your Mantle as bonus dice to stay in character.",
        "seeming_benefits": {},
        "book": "CTL 2e p.152"
    }
}

# Royal Contracts of Spring
ROYAL_CONTRACTS_OF_SPRING = {
    "blessing_of_spring": {
        "name": "Blessing of Spring",
        "contract_type": "spring_royal",
        "cost": "2 glamour, optionally +1 glamour",
        "dice_pool": "Intelligence + Medicine + Mantle vs Stamina + Tolerance",
        "loopholes": "Decorative ribbons and a dance",
        "description": "Brew a cordial of spring that causes plants to mature and fruit, heals animals and people of damage and transitory illness and poisons, and cures changelings of one Clarity Condition and point of Clarity damage. Everything returns after a scene.",
        "seeming_benefits": {},
        "book": "CTL 2e p.152"
    },
    "gift_of_warm_blood": {
        "name": "Gift of Warm Blood",
        "contract_type": "spring_royal",
        "cost": "1 glamour, 1 willpower",
        "dice_pool": "Wits + Medicine + Mantle",
        "loopholes": "Bleed for lethal damage",
        "description": "Downgrade a point of damage on the subject for each success.",
        "seeming_benefits": {},
        "book": "CTL 2e p.152"
    },
    "pandoras_gift": {
        "name": "Pandora's Gift",
        "contract_type": "spring_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Target just gave you a gift",
        "description": "Initiate a Build Equipment action at double the speed to mold a subject's desires into an object until next sunrise or sunset. Use as a bribe for a +3 Social bonus and a Glamour point.",
        "seeming_benefits": {},
        "book": "CTL 2e p.152"
    },
    "prince_of_ivy": {
        "name": "Prince of Ivy",
        "contract_type": "spring_royal",
        "cost": "2 glamour, 1 willpower",
        "dice_pool": "Presence + Expression + Mantle",
        "loopholes": "Bleed while barefoot in soil",
        "description": "Summon strangling vines. Each turn, you may sacrifice your movement, your action, and/or your Defense to establish a new grapple per. The vines roll successes as a dice pool at +3 and contest grapples reflexively.",
        "seeming_benefits": {},
        "book": "CTL 2e p.153"
    },
    "waking_the_inner_fae": {
        "name": "Waking the Inner Fae",
        "contract_type": "spring_royal",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Expression + Mantle vs Composure + Tolerance",
        "loopholes": "Tell them your secret desires",
        "description": "Inflict Wanton with a counterfeit gift wreath. Once a scene for the remaining story, recover Willpower by enticing your last victim into an action.",
        "seeming_benefits": {},
        "book": "CTL 2e p.153"
    }
}

# Contracts of Summer
CONTRACTS_OF_SUMMER = {
    "baleful_sense": {
        "name": "Baleful Sense",
        "contract_type": "summer",
        "cost": "1 glamour",
        "dice_pool": "Wits + Intimidation + Mantle vs Composure + Tolerance",
        "loopholes": "Goaded into screaming at you",
        "description": "Smell a subject's fiercest anger, and any associated Conditions or Tilts. You may refocus them around a new enmity for a scene.",
        "seeming_benefits": {},
        "book": "CTL 2e p.153"
    },
    "child_of_the_hearth": {
        "name": "Child of the Hearth",
        "contract_type": "summer",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Blow on an ember or spark",
        "description": "Inflict Extreme Heat or Extreme Cold, and shield yourself from either.",
        "seeming_benefits": {},
        "book": "CTL 2e p.154"
    },
    "helios_light": {
        "name": "Helios' Light",
        "contract_type": "summer",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Big summer hat",
        "description": "Project blinding sunlight, dealing half its damage as an occult bane.",
        "seeming_benefits": {},
        "book": "CTL 2e p.154"
    },
    "high_summers_zeal": {
        "name": "High Summer's Zeal",
        "contract_type": "summer",
        "cost": "2 glamour",
        "dice_pool": "Presence + Persuasion + Mantle vs Composure + Tolerance",
        "loopholes": "Foe drew first blood",
        "description": "Force a foe to spend Willpower or stand and fight, ignoring Beaten Down.",
        "seeming_benefits": {},
        "book": "CTL 2e p.155"
    },
    "vigilance_of_ares": {
        "name": "Vigilance of Ares",
        "contract_type": "summer",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Martial exercises",
        "description": "Predict ambushes and traps. Add Mantle to Initiative.",
        "seeming_benefits": {},
        "book": "CTL 2e p.155"
    }
}

# Royal Contracts of Summer
ROYAL_CONTRACTS_OF_SUMMER = {
    "fiery_tongue": {
        "name": "Fiery Tongue",
        "contract_type": "summer_royal",
        "cost": "1 glamour, 1 willpower",
        "dice_pool": "Presence + Intimidation + Mantle - Resolve",
        "loopholes": "Asserting dominance or superiority",
        "description": "Rebuke and insults open two Doors and deal bashing damage, or lethal against the fae.",
        "seeming_benefits": {},
        "book": "CTL 2e p.155"
    },
    "flames_of_summer": {
        "name": "Flames of Summer",
        "contract_type": "summer_royal",
        "cost": "2 glamour",
        "dice_pool": "Strength + Survival + Mantle",
        "loopholes": "Eat ice",
        "description": "Ignore wound penalties and unconsciousness from injury, and take +2 as a Physical bonus.",
        "seeming_benefits": {},
        "book": "CTL 2e p.155"
    },
    "helios_judgment": {
        "name": "Helios' Judgment",
        "contract_type": "summer_royal",
        "cost": "1 glamour, optionally 1 willpower",
        "dice_pool": "Dexterity + Athletics + Mantle",
        "loopholes": "Foe wears gold",
        "description": "Use a ray of sunlight as a returning thrown weapon with Mantle for a weapon rating, Range 10/30/50, and Initiative -2. With Willpower, it deals aggravated damage.",
        "seeming_benefits": {},
        "book": "CTL 2e p.155"
    },
    "solstice_revelation": {
        "name": "Solstice Revelation",
        "contract_type": "summer_royal",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Light a fired lantern",
        "description": "Illuminate an area to prevent hiding, forcing a Manipulation + Tolerance - Mantle roll to preserve mundane stealth, or a Clash of Wills against supernatural stealth.",
        "seeming_benefits": {},
        "book": "CTL 2e p.156"
    },
    "sunburnt_heart": {
        "name": "Sunburnt Heart",
        "contract_type": "summer_royal",
        "cost": "2 glamour",
        "dice_pool": "Manipulation + Persuasion + Mantle vs Composure + Tolerance",
        "loopholes": "Shine light into their eyes",
        "description": "Drive a subject Berserk, and add Mantle as a bonus to redirect their fury.",
        "seeming_benefits": {},
        "book": "CTL 2e p.156"
    }
}

# Contracts of Autumn
CONTRACTS_OF_AUTUMN = {
    "autumns_fury": {
        "name": "Autumn's Fury",
        "contract_type": "autumn",
        "cost": "2 glamour, optionally 1 additional glamour",
        "dice_pool": "None",
        "loopholes": "Level a metal rod at foes",
        "description": "Breathe out the Heavy Rain and Heavy Wind Tilts around you. For extra Glamour, each turn, the storm rolls successes as a +1L attack pool.",
        "seeming_benefits": {},
        "book": "CTL 2e p.156"
    },
    "last_harvest": {
        "name": "Last Harvest",
        "contract_type": "autumn",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Your Touchstone",
        "description": "Once per session, take 9-Again to harvest Glamour from a subject, or 8-Again to harvest the Glamour of Autumn.",
        "seeming_benefits": {},
        "book": "CTL 2e p.156"
    },
    "tale_of_the_baba_yaga": {
        "name": "Tale of the Baba Yaga",
        "contract_type": "autumn",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Subterfuge + Mantle vs Composure + Tolerance",
        "loopholes": "A familiar tale",
        "description": "Render the audience of a scary story Shaken.",
        "seeming_benefits": {},
        "book": "CTL 2e p.157"
    },
    "twilights_harbinger": {
        "name": "Twilight's Harbinger",
        "contract_type": "autumn",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Item of value to an involved subject",
        "description": "Know by omens when a given circumstance's end is about to come.",
        "seeming_benefits": {},
        "book": "CTL 2e p.157"
    },
    "witches_intuition": {
        "name": "Witches' Intuition",
        "contract_type": "autumn",
        "cost": "1 glamour",
        "dice_pool": "Wits + Subterfuge + Mantle vs Composure + Tolerance",
        "loopholes": "Eat part of your target",
        "description": "Taste a target's greatest fear, and any associated Conditions or Tilts. You may refocus them around a new fear for the scene.",
        "seeming_benefits": {},
        "book": "CTL 2e p.157"
    }
}

# Royal Contracts of Autumn
ROYAL_CONTRACTS_OF_AUTUMN = {
    "famines_bulwark": {
        "name": "Famine's Bulwark",
        "contract_type": "autumn_royal",
        "cost": "1 glamour",
        "dice_pool": "Wits + Occult + Mantle",
        "loopholes": "Eating recently handraised fruit",
        "description": "Read omens to ask the Storyteller a yes-or-no question per success. With multiple successes, one answer is false.",
        "seeming_benefits": {},
        "book": "CTL 2e p.157"
    },
    "mien_of_the_baba_yaga": {
        "name": "Mien of the Baba Yaga",
        "contract_type": "autumn_royal",
        "cost": "2 glamour",
        "dice_pool": "Presence + Intimidation + Mantle vs Composure + Tolerance",
        "loopholes": "Name their fear",
        "description": "Appear as a subject's greatest fear, driving them to flee and attacking their Clarity if applicable.",
        "seeming_benefits": {},
        "book": "CTL 2e p.158"
    },
    "riding_the_falling_leaves": {
        "name": "Riding the Falling Leaves",
        "contract_type": "autumn_royal",
        "cost": "2 glamour",
        "dice_pool": "Dexterity + Occult + Mantle",
        "loopholes": "Catch a falling leaf",
        "description": "Erupt into leaves flying on the wind. Once per turn, reflexively Dodge a non-saturation attack, and spend Glamour to inflict Spooked on success.",
        "seeming_benefits": {},
        "book": "CTL 2e p.158"
    },
    "sorcerers_rebuke": {
        "name": "Sorcerer's Rebuke",
        "contract_type": "autumn_royal",
        "cost": "2 glamour",
        "dice_pool": "Manipulation + Occult + Mantle",
        "loopholes": "Half a minute of grand warning",
        "description": "Touch a subject to strip them of Glamour or other supernatural energies.",
        "seeming_benefits": {},
        "book": "CTL 2e p.158"
    },
    "tasting_the_harvest": {
        "name": "Tasting the Harvest",
        "contract_type": "autumn_royal",
        "cost": "1 glamour per subject",
        "dice_pool": "Presence + Subterfuge + Mantle",
        "loopholes": "Jumpscare them",
        "description": "Eat subjects' fears, immunizing them from natural fear and adding your Mantle to contest supernatural fears. Grant +1 to rally against one such fear.",
        "seeming_benefits": {},
        "book": "CTL 2e p.158"
    }
}

# Contracts of Winter
CONTRACTS_OF_WINTER = {
    "the_dragon_knows": {
        "name": "The Dragon Knows",
        "contract_type": "winter",
        "cost": "1 glamour",
        "dice_pool": "Wits + Empathy + Mantle vs Composure + Tolerance",
        "loopholes": "Look into their eyes",
        "description": "Taste a subject's deepest regret, and any associated Conditions or Tilts. You may refocus them around a new sorrow for a scene.",
        "seeming_benefits": {},
        "book": "CTL 2e p.159"
    },
    "heart_of_ice": {
        "name": "Heart of Ice",
        "contract_type": "winter",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Barefoot in the cold",
        "description": "Freeze down to the heart, becoming immune to cold and emotional sway.",
        "seeming_benefits": {},
        "book": "CTL 2e p.159"
    },
    "ice_queens_call": {
        "name": "Ice Queen's Call",
        "contract_type": "winter",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Someone shivers",
        "description": "Gather the Blizzard Tilt, to which you are immune.",
        "seeming_benefits": {},
        "book": "CTL 2e p.159"
    },
    "slipknot_dreams": {
        "name": "Slipknot Dreams",
        "contract_type": "winter",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Empathy + Mantle vs Resolve + Tolerance",
        "loopholes": "Present them with a gift",
        "description": "Take the place of a subject's regretful yearning, rendering them Swooned.",
        "seeming_benefits": {},
        "book": "CTL 2e p.159"
    },
    "touch_of_winter": {
        "name": "Touch of Winter",
        "contract_type": "winter",
        "cost": "1 glamour",
        "dice_pool": "Intelligence + Science + Mantle",
        "loopholes": "Melts a handfull of ice into water",
        "description": "Flash-freeze a body of water by touch.",
        "seeming_benefits": {},
        "book": "CTL 2e p.160"
    }
}

# Royal Contracts of Winter
ROYAL_CONTRACTS_OF_WINTER = {
    "ermines_winter_coat": {
        "name": "Ermine's Winter Coat",
        "contract_type": "winter_royal",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Hidden in a burrow",
        "description": "Blend in, taking +3 to Stealth and penalizing attacks against you by -3. In mundane company, reduce the bonus for fae to pick you out as if at half Wyrd.",
        "seeming_benefits": {},
        "book": "CTL 2e p.160"
    },
    "fallow_fields": {
        "name": "Fallow Fields",
        "contract_type": "winter_royal",
        "cost": "2 glamour",
        "dice_pool": "Manipulation + Empathy + Mantle vs Resolve + Tolerance",
        "loopholes": "Write their Touchstone's name",
        "description": "Temporarily empty a subject's capacity for love, rendering them Broken and denying the use of their Anchors.",
        "seeming_benefits": {},
        "book": "CTL 2e p.161"
    },
    "field_of_regret": {
        "name": "Field of Regret",
        "contract_type": "winter_royal",
        "cost": "1 glamour per target, 1 willpower",
        "dice_pool": "Presence + Empathy + Mantle - Resolve",
        "loopholes": "Melancholy song",
        "description": "Harrow others with lonely hauntings, sapping Willpower and inflicting lethal damage.",
        "seeming_benefits": {},
        "book": "CTL 2e p.161"
    },
    "mantle_of_frost": {
        "name": "Mantle of Frost",
        "contract_type": "winter_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Dramatically drop your coat",
        "description": "Project an Extreme Cold strong enough to encase subjects in ice, to which you are immune.",
        "seeming_benefits": {},
        "book": "CTL 2e p.161"
    },
    "winters_curse": {
        "name": "Winter's Curse",
        "contract_type": "winter_royal",
        "cost": "2 glamour, 1 willpower",
        "dice_pool": "Presence + Survival + Mantle vs Resolve + Tolerance",
        "loopholes": "Swallow an ice cube",
        "description": "Freeze a subject's heart except concerning you, stripping the capacity for teamwork or Willpower and holding breaking points in abeyance.",
        "seeming_benefits": {},
        "book": "CTL 2e p.161"
    }
}

# ==================== INDEPENDENT CONTRACTS ====================

# Common Independent Contracts
COMMON_INDEPENDENT_CONTRACTS = {
    "coming_darkness": {
        "name": "Coming Darkness",
        "contract_type": "independent_common",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Extinguish a flame while invoking",
        "description": "Create area of darkness in (Wyrd x 5) meter radius, inflicts Blinded (both Eyes) tilt, may Stun. Invoker is unaffected, but their shadow might come loose.",
        "seeming_benefits": {
            "beast": "Can exempt others, up to half Wyrd",
            "darkling": "Darkness radius doubled"
        },
        "book": "K&K p.58"
    },
    "pomp_and_circumstance": {
        "name": "Pomp and Circumstance",
        "contract_type": "independent_common",
        "cost": "1 glamour or 1 glamour and 1 willpower",
        "dice_pool": "None",
        "loopholes": "Lay out a ring of poppies earlier in scene",
        "description": "Uninvited guests cannot enter a warded area unless invited in by someone inside, guests can't be tracked or spied by mundane means; with Willpower, no huntsmen or Gentry can even find the area, even magically.",
        "seeming_benefits": {
            "beast": "Can sense anyone coming near hidden area",
            "wizened": "Area gains the effect of their Safe Place or Hollow"
        },
        "book": "K&K p.59"
    },
    "shadow_puppet": {
        "name": "Shadow Puppet",
        "contract_type": "independent_common",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Perform a shadow puppet show for at least 3 people for at least 5 minutes before",
        "description": "Create a shadow Retainer with Merit dots up to half Wyrd which also has small amount of magic.",
        "seeming_benefits": {
            "beast": "Shadow puppet has expanded abilities",
            "darkling": "Shadow puppet can spend glamor to teleport from one shadow to another nearby"
        },
        "book": "K&K p.59"
    },
    "steal_influence": {
        "name": "Steal Influence",
        "contract_type": "independent_common",
        "cost": "1 glamour per Influence dot",
        "dice_pool": "Wits + Larceny + Wyrd vs Resolve + Wyrd",
        "loopholes": "Target has dealt lethal or agg damage to changeling in the scene",
        "description": "Steal dots of one Influence from a creature with that trait for Contract's duration, up to Glamour spent (only one Influence at a time).",
        "seeming_benefits": {
            "darkling": "Can steal multiple Influences, if applicable",
            "elemental": "Can change Influence to a different, related influence for duration"
        },
        "book": "K&K p.62"
    },
    "earths_gentle_movements": {
        "name": "Earth's Gentle Movements",
        "contract_type": "independent_common",
        "cost": "1 glamour",
        "dice_pool": "Strength + Crafts + Wyrd",
        "loopholes": "Place a pebble under tongue",
        "description": "Permanently reshape an area of earth for each success rolled, can Knock Down those in area.",
        "seeming_benefits": {
            "elemental": "Double area affected",
            "wizened": "Can shape stone with Wits + Craft + Wyrd instead"
        },
        "book": "K&K p.63"
    }
}

# Royal Independent Contracts
ROYAL_INDEPENDENT_CONTRACTS = {
    "dread_companion": {
        "name": "Dread Companion",
        "contract_type": "independent_royal",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Occult + Wyrd vs. Resistance + Wyrd",
        "loopholes": "Get ghost to affirm thread in same scene",
        "description": "Control a Hedge Ghost.",
        "seeming_benefits": {
            "darkling": "Gain access to Dematerialize Numen",
            "fairest": "Contract lasts until you leave The Hedge"
        },
        "book": "K&K p.60"
    },
    "cracked_mirror": {
        "name": "Cracked Mirror",
        "contract_type": "independent_royal",
        "cost": "1 glamour or 1 glamour and 1 willpower",
        "dice_pool": "Attribute + Ability + Wyrd vs Resistance + Tolerance unless Fetch is willing",
        "loopholes": "Put a significant crack in mirror used",
        "description": "Can use a mirror to spy on Fetch; for Willpower, can switch places with Fetch (Contract ends immediately after).",
        "seeming_benefits": {
            "darkling": "Can conceal spying from Fetch on Exceptional Success",
            "fairest": "If Fetch is willing, Fairest can switch without Willpower (but still requiring Glamour)"
        },
        "book": "K&K p.60"
    },
    "listen_with_winds_ears": {
        "name": "Listen With Wind's Ears",
        "contract_type": "independent_royal",
        "cost": "1 glamour or 2 glamour and 1 willpower",
        "dice_pool": "None",
        "loopholes": "Introduce self by real name in same scene to stranger",
        "description": "Can sense when name is spoken and eavesdrop on area; for Glamour and Willpower can teleport to that location.",
        "seeming_benefits": {
            "beast": "Double speed after teleporting",
            "fairest": "May drag whoever spoke their name to their location"
        },
        "book": "K&K p.61"
    },
    "momentary_respite": {
        "name": "Momentary Respite",
        "contract_type": "independent_royal",
        "cost": "1 glamour or 1 glamour + 1 willpower per scene extended",
        "dice_pool": "Stamina + Survival + Wyrd",
        "loopholes": "Hug an item representing rest or comfort",
        "description": "Each success grants a warding effect -- can ignore Tilts, poison, wound penalties, or even their last health box from Aggravated damage; Spend Willpower to extend duration.",
        "seeming_benefits": {
            "elemental": "Can ignore Environmental Tilts",
            "ogre": "Can ward another, paying all costs"
        },
        "book": "K&K p.61"
    },
    "earths_impenetrable_walls": {
        "name": "Earth's Impenetrable Walls",
        "contract_type": "independent_royal",
        "cost": "2 glamour",
        "dice_pool": "Strength + Crafts + Wyrd",
        "loopholes": "Successfully defended self or another from attack",
        "description": "Raises a Safe Place fortress from the earth, causing an earthquake, with additional benefits for each success.",
        "seeming_benefits": {
            "fairest": "Fortress also comes with hobgoblin Staff",
            "ogre": "Penalize others who attempt to Hedgespin in the fortress"
        },
        "book": "K&K p.64"
    }
}

# ==================== CONTRACTS OF THORN ====================

# Contracts of Thorn
CONTRACTS_OF_THORN = {
    "briars_herald": {
        "name": "Briar's Herald",
        "contract_type": "thorn",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Larceny + Wyrd vs Composure + Tolerance",
        "loopholes": "The Changeling causes a thorn, needle etc to prick the target and draw a drop of blood.",
        "description": "Whenever the target is in the Changeling's presence, they lose 10-again and all failures are dramatic; they know the changeling is at fault.",
        "seeming_benefits": {
            "darkling": "The Darkling can whisper messages whenever the target fails a roll.",
            "wizened": "Specify a clause that can end the Contract early."
        },
        "book": "K&K p.53"
    },
    "by_the_pricking_of_my_thumbs": {
        "name": "By the Pricking of My Thumbs",
        "contract_type": "thorn",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Brews a specific potion and look into it within the scene.",
        "description": "Extend senses into living plants.",
        "seeming_benefits": {
            "beast": "Use plants as natural melee weapons.",
            "darkling": "Occupy number of plants up to Resolve simultaneously."
        },
        "book": "K&K p.54"
    },
    "thistles_rebuke": {
        "name": "Thistle's Rebuke",
        "contract_type": "thorn",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Drink an entire glass of water.",
        "description": "Grow thorns and add 2/0 to armor rating. Anyone who touches the Changeling takes 1L; 2L under a grapple. Can fire thorns for 2L.",
        "seeming_benefits": {
            "elemental": "Touch for 2L, can reflexively retract and extend the thorns.",
            "fairest": "Effects can be invisible even under the Mask."
        },
        "book": "K&K p.54"
    },
    "the_gouging_curse": {
        "name": "The Gouging Curse",
        "contract_type": "thorn",
        "cost": "1 glamour",
        "dice_pool": "Manipulation + Occult + Wyrd vs Composure + Tolerance",
        "loopholes": "Let the victim choose an action the Changeling cannot take.",
        "description": "Issue a dire warning to forbid the target from taking an action, they are cursed if they do the action.",
        "seeming_benefits": {
            "fairest": "Also specify a task that can end the curse, inflicting Awestruck if the victim does so.",
            "ogre": "Extend duration to whole story if the action is harming the Ogre's allies."
        },
        "book": "K&K p.54"
    },
    "embrace_of_nettles": {
        "name": "Embrace of Nettles",
        "contract_type": "thorn",
        "cost": "1 glamour",
        "dice_pool": "None",
        "loopholes": "Leave behind a meaningful personal item the Hedge will consume.",
        "description": "Invoke reflexively when the Hedge shifts: deflect the target of Hedgespinning, defer the successes for later; double-down by adding to both the Hedge and the Changeling's own Hedgespinning rolls.",
        "seeming_benefits": {
            "darkling": "When deferring, negate successes up to either Manipulation or half Wyrd.",
            "fairest": "When doubling down, may apply successes to ally's roll rather than own."
        },
        "book": "K&K p.55"
    }
}

# Royal Contracts of Thorn
ROYAL_CONTRACTS_OF_THORN = {
    "acanthas_fury": {
        "name": "Acantha's Fury",
        "contract_type": "thorn_royal",
        "cost": "2 glamour, 1 willpower",
        "dice_pool": "Presence + Survival + Wyrd vs Stamina + Tolerance",
        "loopholes": "Hold fresh clipping of the kind of plant the transformation will use.",
        "description": "Point at target, who slowly transforms into a thorny plant over several minutes. Changeling must offer a task; target may agree to a binding promise to complete it to avoid transformation. Invoking this Contract is a breaking point of 4 dice.",
        "seeming_benefits": {
            "elemental": "Target number of characters up to Wyrd.",
            "wizened": "May seal the promise without paying Glamour."
        },
        "book": "K&K p.55"
    },
    "awaken_portal": {
        "name": "Awaken Portal",
        "contract_type": "thorn_royal",
        "cost": "2 glamour",
        "dice_pool": "None",
        "loopholes": "Take 15 minutes to clean or repair the entrance.",
        "description": "Portal to a Bastion, Hollow or the Hedge gains temporary sentience.",
        "seeming_benefits": {
            "beast": "Portal goblin has a bite attack of 2L.",
            "elemental": "Portal goblin has 2 dot Influence in chosen element."
        },
        "book": "K&K p.56"
    },
    "crown_of_thorns": {
        "name": "Crown of Thorns",
        "contract_type": "thorn_royal",
        "cost": "2 glamour",
        "dice_pool": "Presence + Occult + Wyrd vs Resolve + Tolerance",
        "loopholes": "Weave a crown of thorns and put it on the target's head.",
        "description": "Deliver message anonymously that forbids the target from performing a specific instant action. If they do so, they suffer the Comatose Condition and 1L.",
        "seeming_benefits": {
            "beast": "Comatose target loses 1WP per night and cannot regain it.",
            "darkling": "While disguised, Darkling gets exceptional successes on 3 to manipulate the target into taking the forbidden action."
        },
        "book": "K&K p.57"
    },
    "shrikes_larder": {
        "name": "Shrike's Larder",
        "contract_type": "thorn_royal",
        "cost": "1 to 3 glamour",
        "dice_pool": "None",
        "loopholes": "Impale an effigy representing the target on a thorn.",
        "description": "Create thorns and spines that slow victims and have various effects on Glamour, Initiative or Speed.",
        "seeming_benefits": {
            "beast": "Harvesting Glamour gives 2 rather than 1 Glamour per success.",
            "wizened": "Can target vehicles as well as individuals."
        },
        "book": "K&K p.57"
    },
    "witchs_brambles": {
        "name": "Witch's Brambles",
        "contract_type": "thorn_royal",
        "cost": "2 to 3 glamour + 1 willpower",
        "dice_pool": "Presence + Occult + Wyrd vs Resolve + Tolerance",
        "loopholes": "Pierce own flesh with pointy object.",
        "description": "Hedgespin in the mortal world.",
        "seeming_benefits": {
            "beast": "Invoke the Contract to make a bite attack do aggravated instead of Lethal",
            "darkling": "Have +1 success to subtle Hedgespinning but -1 for paradigm shifts"
        },
        "book": "K&K p.55"
    }
}

# ==================== CONSOLIDATED CONTRACT COLLECTIONS ====================

# Crown Contracts
ALL_CROWN_CONTRACTS = {
    **CONTRACTS_OF_THE_CROWN,
    **ROYAL_CONTRACTS_OF_THE_CROWN
}

# Jewel Contracts
ALL_JEWEL_CONTRACTS = {
    **CONTRACTS_OF_JEWELS,
    **ROYAL_CONTRACTS_OF_JEWELS
}

# Mirror Contracts
ALL_MIRROR_CONTRACTS = {
    **CONTRACTS_OF_THE_MIRROR,
    **ROYAL_CONTRACTS_OF_THE_MIRROR
}

# Shield Contracts
ALL_SHIELD_CONTRACTS = {
    **CONTRACTS_OF_THE_SHIELD,
    **ROYAL_CONTRACTS_OF_THE_SHIELD
}

# Steed Contracts
ALL_STEED_CONTRACTS = {
    **CONTRACTS_OF_THE_STEED,
    **ROYAL_CONTRACTS_OF_THE_STEED
}

# Sword Contracts
ALL_SWORD_CONTRACTS = {
    **CONTRACTS_OF_THE_SWORD,
    **ROYAL_CONTRACTS_OF_THE_SWORD
}

# Chalice Contracts
ALL_CHALICE_CONTRACTS = {
    **CONTRACTS_OF_CHALICE,
    **ROYAL_CONTRACTS_OF_CHALICE
}

# Coin Contracts
ALL_COIN_CONTRACTS = {
    **CONTRACTS_OF_COIN,
    **ROYAL_CONTRACTS_OF_COIN
}

# Stars Contracts
ALL_STARS_CONTRACTS = {
    **CONTRACTS_OF_STARS,
    **ROYAL_CONTRACTS_OF_STARS
}

# Spring Contracts
ALL_SPRING_CONTRACTS = {
    **CONTRACTS_OF_SPRING,
    **ROYAL_CONTRACTS_OF_SPRING
}

# Summer Contracts
ALL_SUMMER_CONTRACTS = {
    **CONTRACTS_OF_SUMMER,
    **ROYAL_CONTRACTS_OF_SUMMER
}

# Autumn Contracts
ALL_AUTUMN_CONTRACTS = {
    **CONTRACTS_OF_AUTUMN,
    **ROYAL_CONTRACTS_OF_AUTUMN
}

# Winter Contracts
ALL_WINTER_CONTRACTS = {
    **CONTRACTS_OF_WINTER,
    **ROYAL_CONTRACTS_OF_WINTER
}

# Independent Contracts
ALL_INDEPENDENT_CONTRACTS = {
    **COMMON_INDEPENDENT_CONTRACTS,
    **ROYAL_INDEPENDENT_CONTRACTS
}

# Thorn Contracts
ALL_THORN_CONTRACTS = {
    **CONTRACTS_OF_THORN,
    **ROYAL_CONTRACTS_OF_THORN
}

# All Changeling Contracts
ALL_CHANGELING_CONTRACTS = {
    **ALL_CROWN_CONTRACTS,
    **ALL_JEWEL_CONTRACTS,
    **ALL_MIRROR_CONTRACTS,
    **ALL_SHIELD_CONTRACTS,
    **ALL_STEED_CONTRACTS,
    **ALL_SWORD_CONTRACTS,
    **ALL_CHALICE_CONTRACTS,
    **ALL_COIN_CONTRACTS,
    **ALL_STARS_CONTRACTS,
    **ALL_SPRING_CONTRACTS,
    **ALL_SUMMER_CONTRACTS,
    **ALL_AUTUMN_CONTRACTS,
    **ALL_WINTER_CONTRACTS,
    **ALL_INDEPENDENT_CONTRACTS,
    **ALL_THORN_CONTRACTS,
    **GOBLIN_CONTRACTS
}

# ==================== HELPER FUNCTIONS ====================

def get_contract(contract_key):
    """Get a specific contract by key."""
    return ALL_CHANGELING_CONTRACTS.get(contract_key.lower().replace(" ", "_"))


def get_contracts_by_type(contract_type):
    """Get all contracts of a specific type."""
    contracts = {}
    for key, data in ALL_CHANGELING_CONTRACTS.items():
        if data.get('contract_type') == contract_type:
            contracts[key] = data
    return contracts


def get_contracts_by_category(category):
    """Get all contracts in a category (e.g., 'crown', 'jewel', 'goblin', 'spring', 'thorn', 'independent')."""
    category_map = {
        'crown': ALL_CROWN_CONTRACTS,
        'jewel': ALL_JEWEL_CONTRACTS,
        'mirror': ALL_MIRROR_CONTRACTS,
        'shield': ALL_SHIELD_CONTRACTS,
        'steed': ALL_STEED_CONTRACTS,
        'sword': ALL_SWORD_CONTRACTS,
        'chalice': ALL_CHALICE_CONTRACTS,
        'coin': ALL_COIN_CONTRACTS,
        'stars': ALL_STARS_CONTRACTS,
        'spring': ALL_SPRING_CONTRACTS,
        'summer': ALL_SUMMER_CONTRACTS,
        'autumn': ALL_AUTUMN_CONTRACTS,
        'winter': ALL_WINTER_CONTRACTS,
        'independent': ALL_INDEPENDENT_CONTRACTS,
        'thorn': ALL_THORN_CONTRACTS,
        'goblin': GOBLIN_CONTRACTS
    }
    return category_map.get(category.lower(), {})


def get_all_contracts():
    """Get all changeling contracts."""
    return ALL_CHANGELING_CONTRACTS


