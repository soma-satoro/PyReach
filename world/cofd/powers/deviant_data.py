"""
Deviant: The Renegades - Variations, Scars, and Forms Data
This module contains all the detailed information about Deviant powers.
"""

# ==================== ORIGINS ====================

DEVIANT_ORIGINS_DETAILED = {
    "autourgic": {
        "formal_name": "Autourgics",
        "informal_name": "Elect",
        "anchor": "Loyalty",
        "variation_type": "Overt",
        "description": "Those who sought the power of the Divergence, to serve a cause or just for its own sake.",
        "book": "DTR 24"
    },
    "epimorph": {
        "formal_name": "Epimorphs",
        "informal_name": "Volunteers",
        "anchor": "Loyalty",
        "variation_type": "Subtle",
        "description": "Those led to the procedure that would break them by promises or lies.",
        "book": "DTR 26"
    },
    "exomorph": {
        "formal_name": "Exomorphs",
        "informal_name": "Unwilling",
        "anchor": "Conviction",
        "variation_type": "Overt",
        "description": "Those whom others have subjected to the Divergence by force.",
        "book": "DTR 28"
    },
    "genotypal": {
        "formal_name": "Genotypals",
        "informal_name": "Born",
        "anchor": "Conviction",
        "variation_type": "Subtle",
        "description": "Those whose transformation was fated from birth, by heritage, prophecy, or prenatal treatment.",
        "book": "DTR 30"
    },
    "pathological": {
        "formal_name": "Pathologicals",
        "informal_name": "Accidents",
        "anchor": "Any",
        "variation_type": "Any",
        "description": "Those transformed by sheer freak circumstance.",
        "book": "DTR 32"
    }
}

# ==================== CLADES ====================

DEVIANT_CLADES_DETAILED = {
    "cephalist": {
        "formal_name": "Cephalists",
        "informal_name": "Psychics",
        "description": "Those transformed by the cracking open of the mind to influence deeper reality.",
        "book": "DTR 34"
    },
    "chimeric": {
        "formal_name": "Chimerics",
        "informal_name": "Hybrids",
        "description": "Those transformed by fusion with other sorts of life, whether engineered, transplanted, or infected.",
        "book": "DTR 36"
    },
    "coactive": {
        "formal_name": "Coactives",
        "informal_name": "Infused",
        "description": "Those transformed by being charged with and absorbing potent energies.",
        "book": "DTR 38"
    },
    "invasive": {
        "formal_name": "Invasives",
        "informal_name": "Cyborgs",
        "description": "Those transformed by the merging of their body with occult artifacts or mechanical devices.",
        "book": "DTR 40"
    },
    "mutant": {
        "formal_name": "Mutants",
        "informal_name": "Grotesques",
        "description": "Those transformed by the rebellion of their body into bizarre shapes and natures.",
        "book": "DTR 42"
    }
}

# ==================== ADAPTATIONS ====================

DEVIANT_ADAPTATIONS = {
    # Universal Adaptations
    "stubborn_resolve": {
        "name": "Stubborn Resolve",
        "category": "Universal",
        "description": "Once per chapter, use your Loyalty or Conviction as a bonus to resist being swayed.",
        "frequency": "Once per chapter",
        "cost": None,
        "book": "DTR 112"
    },
    
    # Cephalist Adaptations
    "focus": {
        "name": "Focus",
        "category": "Cephalist",
        "description": "Once per chapter, push a Variation beyond its Magnitude for the scene, at a potential cost of Willpower.",
        "frequency": "Once per chapter",
        "cost": "Willpower (potential)",
        "book": "DTR 112"
    },
    "iron_will": {
        "name": "Iron Will",
        "category": "Cephalist",
        "description": "Spend Willpower to refresh a per-scene or per-chapter Variation or Adaptation.",
        "frequency": "Variable",
        "cost": "Willpower",
        "book": "DTR 112"
    },
    
    # Chimeric Adaptations
    "untamed": {
        "name": "Untamed",
        "category": "Chimeric",
        "description": "Once per chapter, suppress the Magnitude of Scars, at a potential cost of Willpower.",
        "frequency": "Once per chapter",
        "cost": "Willpower (potential)",
        "book": "DTR 112"
    },
    "adrenaline_surge": {
        "name": "Adrenaline Surge",
        "category": "Chimeric",
        "description": "Take resistant damage to refresh a per-scene or per-chapter Variation or Adaptation.",
        "frequency": "Variable",
        "cost": "Resistant damage",
        "book": "DTR 112"
    },
    
    # Coactive Adaptations
    "consume": {
        "name": "Consume",
        "category": "Coactive",
        "description": "Once per chapter, push a Variation beyond its Magnitude for the scene, at a potential cost of resistant damage.",
        "frequency": "Once per chapter",
        "cost": "Resistant damage (potential)",
        "book": "DTR 112"
    },
    "living_conduit": {
        "name": "Living Conduit",
        "category": "Coactive",
        "description": "Spend Willpower to refresh a per-scene or per-chapter Variation or Adaptation.",
        "frequency": "Variable",
        "cost": "Willpower",
        "book": "DTR 112"
    },
    
    # Invasive Adaptations
    "redundancy": {
        "name": "Redundancy",
        "category": "Invasive",
        "description": "Once per chapter, heal damage and Tilts taken from a scene.",
        "frequency": "Once per chapter",
        "cost": None,
        "book": "DTR 112"
    },
    "overclock": {
        "name": "Overclock",
        "category": "Invasive",
        "description": "Take resistant damage to refresh a per-scene or per-chapter Variation or Adaptation.",
        "frequency": "Variable",
        "cost": "Resistant damage",
        "book": "DTR 113"
    },
    
    # Mutant Adaptations
    "unpredictable": {
        "name": "Unpredictable",
        "category": "Mutant",
        "description": "Once per chapter, temporarily exchange a Variation for a Universal Variation up to half its Magnitude for the scene.",
        "frequency": "Once per chapter",
        "cost": None,
        "book": "DTR 113"
    },
    "forced_growth": {
        "name": "Forced Growth",
        "category": "Mutant",
        "description": "Take minor instability to refresh a per-scene or per-chapter Variation or Adaptation.",
        "frequency": "Variable",
        "cost": "Minor instability",
        "book": "DTR 113"
    }
}

# Adaptation Categories for easy lookup
ADAPTATION_CATEGORIES = {
    "universal": ["stubborn_resolve"],
    "cephalist": ["focus", "iron_will"],
    "chimeric": ["untamed", "adrenaline_surge"],
    "coactive": ["consume", "living_conduit"],
    "invasive": ["redundancy", "overclock"],
    "mutant": ["unpredictable", "forced_growth"]
}

# ==================== VARIATIONS ====================

# Universal Variations
VARIATION_ABSORB_INSTABILITY = {
    "name": "Absorb Instability",
    "keywords": ["Direct", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Sense a target's Instability and apply half Scar Power to reduce Scar Resistance penalties from Instability.",
        2: "Transfer Instability from the target to yourself.",
        3: "Choose one: Resilient (reduce level of Instability taken), Soothing (allow target to ignore Scar Power medium Instabilities or one Major), or Stabilizing (reduce target's Scar and Variation Magnitudes by Scar Power)",
        4: "Receive two Magnitude 3 benefits.",
        5: "Receive all Magnitude 3 benefits."
    },
    "book": "DevC 15"
}

VARIATION_AQUATIC = {
    "name": "Aquatic",
    "keywords": ["Subtle", "Perpetual", "Tiered"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Breathe underwater and ignore swimming penalties.",
        2: "Choose Habitat (marine life cooperative, unimpeded by pressure) or Speed (swimming speed becomes Scar Power x 20)",
        3: "Receive both Magnitude 2 benefits."
    },
    "book": "DTR 113"
}

VARIATION_BIOLUMINESCENCE = {
    "name": "Bioluminescence",
    "keywords": ["Overt", "Directed", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Project colors and patterns of light.",
        2: "Direct intense light to blind others.",
        3: "Light acquires supernatural qualities of sunlight.",
        4: "Direct concentrated waves of hazardous radiation."
    },
    "deviations": {
        "Aura": {"cost": 1, "effect": "Your entire body projects light. With higher Magnitude, produce Blazing Light Tilt."}
    },
    "book": "DTR 113"
}

VARIATION_BONELESS = {
    "name": "Boneless",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Freely contort and dislocate joints, unimpeded by mundane bondage, add Scar Power as grappling bonus.",
        2: "Body can fold like an octopus. Scar Power penalizes grappling opponents.",
        3: "Body can dissolve into mobile sludge.",
        4: "Body can sublime into low-hanging vapor."
    },
    "deviations": {
        "Defensive": {"cost": 1, "effect": "Collapse reflexively."}
    },
    "book": "DTR 114"
}

VARIATION_BRACHIATION = {
    "name": "Brachiation",
    "keywords": ["Overt", "Reflexive", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Choose Bounding (leap up to 2x Scar Power in meters, bonus to resist fall damage) or Wall Crawling (scale sheer vertical surfaces)",
        2: "Choose Generalist (receive both Magnitude 1 benefits), Leaper (ignore fall damage, leap up to Scar Power x 5 meters, requires Bounding), or Spider (scale inverted surfaces and ceilings, requires Wall Crawling)",
        3: "Receive all Magnitude 2 benefits."
    },
    "book": "DTR 114"
}

VARIATION_CAMOUFLAGE = {
    "name": "Camouflage",
    "keywords": ["Subtle", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Fade from notice, add Scar Power as Stealth bonus while not moving or drawing attention.",
        2: "Choose Mobile (moving retains camouflage) or Invisible (disappear from sight, bystanders roll chance die to notice)",
        3: "Receive both Magnitude 2 benefits.",
        4: "Choose Multi-Sensory (camouflage erases scent, sound, echolocation) or Wavelengths (erases infrared/ultraviolet traces)",
        5: "Receive both Magnitude 4 benefits."
    },
    "book": "DTR 115"
}

VARIATION_CARAPACE = {
    "name": "Carapace",
    "keywords": ["Subtle", "Discrete", "Perpetual"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Choose either 1/3 or 2/0 Armor.",
        2: "Choose either 2/4 or 3/0 Armor.",
        3: "Choose 2/4 or 3/0 Armor, plus one: Bulletproof (+2 ballistic, immune to non-AP firearms) or Dense (+1 general, ignore minimum bashing)",
        4: "Choose 2/4 or 3/0 Armor, receive both Magnitude 3 benefits.",
        5: "Choose 2/4 or 3/0 Armor, receive both Magnitude 3 benefits, and whenever Armor applies it reduces damage to one point."
    },
    "book": "DTR 115"
}

VARIATION_ELECTROKINESIS = {
    "name": "Electrokinesis",
    "keywords": ["Overt", "Directed", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Choose one per Magnitude dot: Conductivity (electrocute with available charges up to 2x Scar Power damage), Input (interface with smart devices), Output (control device functions), Power (power device on/off), or Research (scan stored data quickly)",
        2: "Choose two total effects.",
        3: "Choose three total effects.",
        4: "Choose four total effects.",
        5: "Choose five total effects."
    },
    "book": "DTR 116"
}

VARIATION_ENHANCED_SPEED = {
    "name": "Enhanced Speed",
    "keywords": ["Overt", "Reflexive", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Add Scar Power to Initiative. Double Speed.",
        2: "Add half Scar Power to Defense. Ignore Defense penalties from consecutive attacks.",
        3: "Choose Alacrity (act at any Initiative), Fleetness (multiply Speed by Scar Power x Magnitude), or Guerilla (apply Defense vs firearms, keep half Defense during charges/all-out attacks)",
        4: "Choose a second Magnitude 3 benefit.",
        5: "Receive all Magnitude 3 benefits."
    },
    "book": "DTR 117"
}

VARIATION_ENVIRONMENTAL_ADAPTATION = {
    "name": "Environmental Adaptation",
    "keywords": ["Subtle", "Discrete", "Perpetual", "Reflexive"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Choose environment type. Apply Magnitude as Survival bonus, ignore level 1 extreme environments and one moderate Environmental Tilt per scene.",
        2: "Ignore level 2 extreme environments and two moderate Tilts per scene.",
        3: "Ignore level 3 extreme environments, one severe and two moderate Tilts per scene.",
        4: "Ignore level 4 extreme environments and all Environmental Tilts."
    },
    "deviations": {
        "General": {"cost": 1, "effect": "Becomes Toggled instead of Perpetual, activates once per chapter, applies to all environments except wholly unnatural."}
    },
    "book": "DTR 118"
}

VARIATION_FACE_THIEF = {
    "name": "Face Thief",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Disguise part of body as subject's for scene or chapter (with Willpower).",
        2: "Disguise entire body including voice but not Size. Subterfuge rolls gain rote quality.",
        3: "Replicate all bodily features and apparel, including up to 2 Size difference.",
        4: "Replicate language, instinctive greetings, and up to Scar Power in subject's Social Merits."
    },
    "deviations": {
        "Recollection": {"cost": 1, "effect": "Create generic disguises, recreate previous disguises, assume disguises from recorded images at -4 penalty."}
    },
    "book": "DTR 118"
}

VARIATION_FLIGHT = {
    "name": "Flight",
    "keywords": ["Overt", "Reflexive", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Control falls and take no falling damage.",
        2: "Glide at lateral Speed of (Scar Power + 10), descend 3-30m per turn.",
        3: "Ascend Scar Power in meters as instant action.",
        4: "Choose Grace (hover without descending, ascend reflexively) or Velocity (lateral Speed increases to Scar Power^2 x 20)",
        5: "Receive both Magnitude 4 benefits."
    },
    "book": "DTR 119"
}

VARIATION_GIGANTIC = {
    "name": "Gigantic",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Increase Size by +1. Apply 8-Again to Strength and Stamina feats. Add Size difference to derived traits. Lift objects up to Size. Once per chapter when deactivating, heal Size difference in damage.",
        2: "Increase Size by +3. Other benefits as Magnitude 1.",
        3: "Increase Size by +6. Other benefits as Magnitude 1.",
        4: "Increase Size by +10. Other benefits as Magnitude 1.",
        5: "Increase Size by +15. Other benefits as Magnitude 1."
    },
    "book": "DTR 119"
}

VARIATION_HEALER = {
    "name": "Healer",
    "keywords": ["Overt", "Directed", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Heal a given subject once per chapter to cure minor ailments and remove half your Scar Power in wound penalties for the scene.",
        2: "Heal all bashing damage or remove up to your Scar Power in symptomatic Tilts.",
        3: "Heal your Scar Power in lethal damage or remove one Condition ailment.",
        4: "Once per chapter, heal half your Scar Power in aggravated damage, remove a Persistent Condition, or restore a destroyed body part.",
        5: "You can resurrect the dead, though decomposition can make this traumatic, and repeated use courts instability."
    },
    "deviations": {
        "Aura": {"cost": 1, "effect": "The Variation heals everyone in short range, but not yourself."}
    },
    "book": "DTR 121"
}

VARIATION_HOLOGRAPHIC_PROJECTION = {
    "name": "Holographic Projection",
    "keywords": ["Overt", "Directed", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Conjure uncanny illusions up to Size 5.",
        2: "Conjure realistic illusions.",
        3: "Conjure tangible illusions."
    },
    "deviations": {
        "Aura": {"cost": 1, "effect": "Conjure multiple illusions out to short range."},
        "Control": {"cost": 1, "effect": "Direct multiple illusions reflexively, which persist when you leave their range."}
    },
    "book": "DTR 121"
}

VARIATION_HYPER_COMPETENCE = {
    "name": "Hyper-Competence",
    "keywords": ["Subtle", "Perpetual", "Reflexive", "Tiered"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Choose an associated Skill. The Skill imposes no unskilled penalty, always applies a specialty bonus, and achieves exceptional success on a threshold of three instead of five.",
        2: "Add half Scar Power as bonus dice to the chosen Skill.",
        3: "Apply the rote quality to rolls of the chosen Skill."
    },
    "deviations": {
        "Multicompetence": {"cost": 1, "effect": "Add your Scar Power in associated Skills."},
        "Natural Talent": {"cost": 2, "effect": "Incompatible with Multicompetence. Instead of one Skill, choose all Mental, all Physical, or all Social Skills."}
    },
    "book": "DTR 122"
}

VARIATION_IMMUNITY = {
    "name": "Immunity",
    "keywords": ["Subtle", "Discrete", "Perpetual", "Reflexive"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Immunity to your Scar Power in Personal Tilts and associated Conditions.",
        2: "Immunity to your Scar Power in types of hazard (fire, electricity, poison, radiation, etc).",
        3: "Force a Clash of Wills to negate all supernatural powers directed at you by a particular type of supernatural being."
    },
    "deviations": {
        "Area": {"cost": 1, "effect": "The Variation becomes Toggled instead of Perpetual and bestows immunity over a ten meter radius."}
    },
    "book": "DTR 122"
}

VARIATION_LASH = {
    "name": "Lash",
    "keywords": ["Overt", "Discrete", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Make a unique attack, which rolls Attribute + Skill - Defense. Choose whether the attack is close (Strength) or ranged (Dexterity), which combat Skill it employs, and what type of damage it does (bashing, lethal, or none). Choose one benefit, plus two for each dot of base Magnitude after the first.",
        2: "As Magnitude 1, choose three total benefits.",
        3: "As Magnitude 1, choose five total benefits.",
        4: "As Magnitude 1, choose seven total benefits.",
        5: "As Magnitude 1, choose nine total benefits."
    },
    "book": "DTR 122",
    "note": "Benefits include: Blasting, Caustic, Channel, Conjured, Deadly, Deafening, Disabling, Envenomed, Forceful, Grappling, Immolating, Insidious, Obscuring, Piercing, Quick, Reach, Sickening, Soporific, Touch, Versatile. Deviations add more benefits with costs."
}

VARIATION_MINIATURIZATION = {
    "name": "Miniaturization",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Shrink by -1 Size, gaining a +2 bonus to avoid notice or circumnavigate. Calculate Health with an effective Size no less than Scar Power.",
        2: "Shrink down to Size 1, adjusting the dice bonus to (6 - Size). Add half that value to Defense. Shrunken Size limits your Speed and carrying capacity.",
        3: "Shrink down to Size 0 to reduce rolls to notice you to a chance die, and penalize deliberate searches for you by -5.",
        4: "Shrink down to microscopic level."
    },
    "deviations": {
        "Defensive": {"cost": 1, "effect": "Once per turn, you may shrink reflexively, which can reduce an attack's successes by Scar Power."}
    },
    "book": "DTR 126"
}

VARIATION_OUT_OF_PHASE = {
    "name": "Out of Phase",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Render part of a limb insubstantial to materials up to Durability 1.",
        2: "Choose Stone (pass through Durability 2 materials) or Torso (render up to half the body insubstantial, which can apply as partial cover)",
        3: "Choose Balance (receive both Magnitude 2 benefits), Steel (requires Stone, pass through Durability 3 materials), or Body (requires Torso, render the entire body insubstantial)",
        4: "Receive all Magnitude 3 benefits."
    },
    "deviations": {
        "Defensive": {"cost": 1, "effect": "Reflexively toggle insubstantiality once per turn."}
    },
    "book": "DTR 126"
}

VARIATION_PYROKINESIS = {
    "name": "Pyrokinesis",
    "keywords": ["Overt", "Directed", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Influence torchfires below Scar Power 3, bonfires below Scar Power 5, and infernos at Scar Power 5. Choose Influence (direct the path and movement of a fire, aiming with Scar Finesse) or Pyrotechnics (alter the shape and billowing of a fire to create displays and control visibility)",
        2: "Receive both Magnitude 1 benefits. Combust sparks.",
        3: "Choose Ignite (ignite spontaneous fires) or Extinguish (extinguish fires and suppress combustion)",
        4: "Receive both Magnitude 3 benefits."
    },
    "deviations": {
        "Aura": {"cost": 1, "effect": "Exert equal pyrokinetic influence over short range. Immune to fires with heat damage up to half your Scar Power."}
    },
    "book": "DTR 127"
}

VARIATION_SHADOW_SELVES = {
    "name": "Shadow Selves",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Manifest up to (Scar Power) copies of yourself, which dissipate when damaged and can only perform basic actions.",
        2: "You may 'ride' a copy as an instant action, directing its body instead of your own.",
        3: "Your copies can act under their own direction."
    },
    "deviations": {
        "Prism": {"cost": 1, "effect": "You can generate copy selves with distinct appearances and body types."},
        "Superposition": {"cost": 1, "effect": "You can redefine which body is real and not a copy as an instant action."}
    },
    "book": "DTR 128"
}

VARIATION_SHADOWS_OF_THE_PAST = {
    "name": "Shadows of the Past",
    "keywords": ["Subtle", "Directed", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Enter a trance to glimpse fragments of a person or location's past, relevant enough to your endeavors to offer half your Scar Power as a circumstantial bonus.",
        2: "Narrow visions of import down to a 24-hour radius around a given past time or event.",
        3: "Invite others to share your visions. Choose Living History (once per chapter, project yourself into a hypothetical role to interact with the vision) or Precision (narrow visions down to an hour radius)",
        4: "Receive both Magnitude 3 benefits.",
        5: "Once per story or by risking instability, carry something up to twice Scar Power in Size back with you from the shadow of the past."
    },
    "book": "DTR 129"
}

VARIATION_SPECIALIZED_SENSE = {
    "name": "Specialized Sense",
    "keywords": ["Subtle", "Discrete", "Perpetual", "Reflexive"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Choose Animal (gain up to your Scar Power in +2 enhanced senses), Technology (duplicate a chosen mechanical sensor or imaging tool, +3 bonus to appropriate analysis), or Sixth Sense (sense the presence of a chosen type of supernatural being within 10 meters)",
        2: "As Sixth Sense, and you can perceive one type of manifestation or energy which is normally invisible. +2 Occult bonus to assess.",
        3: "As Magnitude 2, and once per chapter, you can declare the discovery of a detail related to that manifestation or energy. +3 Occult bonus."
    },
    "book": "DTR 129"
}

VARIATION_STORM_CALLER = {
    "name": "Storm-Caller",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Choose an environmental hazard. Control the hazard by manifesting or removing a level one extreme environment or a moderate Environmental Tilt. Take an instant action to replace the Tilt with a new Tilt.",
        2: "Control extreme environments of level up to half Scar Power. Take an instant action to control another Tilt, or 'stack' a Tilt upon itself to make it severe, up to Scar Power in simultaneous Tilts.",
        3: "Control any number of Tilts up to your maximum when first activating the Variation.",
        4: "Once per story or by risking instability, control a level four extreme environment."
    },
    "deviations": {
        "Universal": {"cost": 1, "effect": "The Variation may be activated once per chapter, but can control a different environmental hazard for each activation."}
    },
    "book": "DTR 130"
}

VARIATION_SUPERHUMAN_ATTRIBUTE = {
    "name": "Superhuman Attribute",
    "keywords": ["Subtle", "Discrete", "Perpetual", "Reflexive"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Choose an Attribute. Its rating increases to the higher of (Attribute + Magnitude) or (Magnitude + 3), to a maximum of 10, for all purposes except calculating supernatural derived traits or effects.",
        2: "As Magnitude 1.",
        3: "As Magnitude 1, and receive the corresponding benefit: Intelligence (once per chapter, declare an unanticipated fact), Wits (once per scene, declare notice of a detail), Resolve (resist supernatural mental influence with Clash of Wills), Strength (lift objects up to Scar Power x 5 in Size, pierce half Scar Power in Armor), Dexterity (calculate Defense with higher of Wits/Dexterity, never fall from balance loss), Stamina (resist supernatural transformation with Clash of Wills), Presence (once per chapter, declare presence of a person who might appear), Manipulation (once per chapter, claim non-hostile civilians as temporary Allies/Contacts/Resources/Retainer up to half Scar Power), Composure (when you spend Willpower to enhance a roll and fail, recover the spent Willpower)",
        4: "As Magnitude 3.",
        5: "As Magnitude 3."
    },
    "book": "DTR 131"
}

VARIATION_TELEKINESIS = {
    "name": "Telekinesis",
    "keywords": ["Overt", "Directed", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Hold an object up to your (Magnitude x Scar Power) in Size in place. Against living targets, direct Scar Finesse - Defense as a grappling roll, capable of the Hold, Restrain, and Drop Prone maneuvers.",
        2: "Move a held object at a Speed up to your (Magnitude x Scar Power), or operate it 'manually' at a distance. Telekinetic grapple maneuvers add Control Weapon, Damage, and Disarm.",
        3: "Choose Throw (hurl an object or target to deal half Size in lethal damage) or Deflect (roll Scar Finesse to subtract successes from physical attacks)",
        4: "Choose Versatility (receive both Magnitude 3 benefits), Crush/Dismember (requires Throw, inflict Scar Power + Acclimation - Durability damage to held objects), or Force Field (requires Deflect, conjure telekinetic barrier with half Scar Power in Durability)",
        5: "Receive all Magnitude 4 benefits."
    },
    "book": "DTR 132"
}

VARIATION_TRANSLOCATION = {
    "name": "Translocation",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Universal",
    "magnitude_effects": {
        1: "Once per turn, reflexively roll Scar Finesse to teleport within a 10/20/40 meter range to an exposed destination.",
        2: "Choose Blind (translocate to an unexposed destination at a -4 penalty) or Far-Reaching (increase range to 30/60/120 meters)",
        3: "Receive both Magnitude 2 benefits."
    },
    "deviations": {
        "Conjuration": {"cost": 1, "effect": "Direct the Variation to translocate an object of Size up to (Magnitude + Scar Power) from one point within range to another."},
        "Defensive": {"cost": 1, "effect": "You may reflexively translocate yourself when it is not your turn, accumulating penalties for repeated translocations."}
    },
    "book": "DTR 134"
}

# Cephalist Variations
VARIATION_ASTRAL_TRAVEL = {
    "name": "Astral Travel",
    "keywords": ["Subtle", "Tiered", "Toggled"],
    "category": "Cephalist",
    "magnitude_effects": {
        1: "Once per chapter, roll Scar Finesse in a dream state to uncover a clue.",
        2: "Leave your body behind to project as an insubstantial astral entity for up to a scene.",
        3: "While astrally projecting, you may explore the dreams of a visited sleeper, becoming Informed.",
        4: "Choose Dream Walker (transform your body into astral ephemera rather than leaving it behind) or Dream Gates (travel from one sleeper's dreams to those of a strongly associated sleeper)",
        5: "Receive both Magnitude 4 benefits."
    },
    "book": "DTR 134"
}

VARIATION_BODY_SNATCHER = {
    "name": "Body Snatcher",
    "keywords": ["Subtle", "Directed", "Tiered", "Toggled"],
    "category": "Cephalist",
    "magnitude_effects": {
        1: "Ride a subject's senses for up to a scene, leaving your body behind for the duration.",
        2: "Read a vessel's surface thoughts. You may transfer from one vessel to another. Spend Willpower to ride a vessel for another chapter.",
        3: "You may control the vessel's actions for a turn. If your action inflicts lethal damage or a breaking point, the vessel resists further control.",
        4: "Choose Body Swap (swap bodies with a ridden vessel) or Puppet Possession (suppress the vessel's consciousness, preventing resistance)",
        5: "Receive both Magnitude 4 benefits."
    },
    "book": "DTR 135"
}

VARIATION_CREEPING_DREAD = {
    "name": "Creeping Dread",
    "keywords": ["Subtle", "Directed", "Tiered", "Toggled"],
    "category": "Cephalist",
    "magnitude_effects": {
        1: "Inflict an Integrity breaking point or the Shaken Condition. Apply half Scar Power as a scenelong bonus to frighten victims.",
        2: "Inflict for a scene the fear of a present chosen focus. The victim must roll Resolve + Composure to approach the focus of their fear, and suffer a -2 penalty on confronting actions.",
        3: "The subject becomes Frightened of the chosen focus, and Insensate when unable to flee.",
        4: "The threat of the chosen focus inflicts Beaten Down."
    },
    "deviations": {
        "Aura": {"cost": 1, "effect": "The Variation targets everyone within short range."}
    },
    "book": "DTR 135"
}

VARIATION_MEMORY_THIEF = {
    "name": "Memory Thief",
    "keywords": ["Subtle", "Directed", "Tiered", "Toggled"],
    "category": "Cephalist",
    "magnitude_effects": {
        1: "Steal the memory of a routine situation from a subject. The subject may regenerate the lost memory if prompted with evidence or retelling.",
        2: "Steal a recent memory of your choice, up to a scene in length.",
        3: "Choose Forgotten Goal (steal a short-term Aspiration) or Forgotten Milestone (steal memories of emotional weight or strenuous investment)",
        4: "Choose Fickle Memory (receive both Magnitude 3 benefits), Stolen Triumph (requires Forgotten Goal, steal a long-term Aspiration), or Formative Memory (requires Forgotten Milestone, steal a fundamental, identity-shaping memory)",
        5: "Receive all Magnitude 4 benefits."
    },
    "book": "DTR 136"
}

VARIATION_TELEPATHY = {
    "name": "Telepathy",
    "keywords": ["Subtle", "Directed", "Tiered", "Toggled"],
    "category": "Cephalist",
    "magnitude_effects": {
        1: "Choose Attune (once per chapter, read a subject's surface thoughts and ask up to your Scar Power in relevant questions) or Project (broadcast thoughts to a subject)",
        2: "Receive both Magnitude 1 benefits. When Projecting you can open yourself to return broadcasts, which you can relay between multiple subjects.",
        3: "Choose Network (simultaneously connect to up to your Scar Power in subjects as a single action) or Recontact (Project to anyone you have telepathically connected with before, at a -4 penalty for unwilling targets beyond long range)",
        4: "Choose Balance (receive both Magnitude 3 benefits), Hivemind (requires Network, subjects can choose to share Skill ratings), or Forceful (requires Recontact, project experienced memories to a subject)",
        5: "Receive all Magnitude 4 benefits."
    },
    "book": "DTR 137"
}

# Chimeric Variations
VARIATION_ANIMAL_TRANSFORMATION = {
    "name": "Animal Transformation",
    "keywords": ["Overt", "Discrete", "Toggled"],
    "category": "Chimeric",
    "magnitude_effects": {
        2: "Transform into a particular animal up to Size 2.",
        3: "Choose Medium (transform into a particular animal up to Size 5) or Swarm (transform into a swarm of small animals up to (Magnitude + Scar Power) meters across)",
        4: "Choose Large (transform into a particular animal up to Size 9) or Biting Swarm (transform into a swarm which inflicts half your Scar Power in bashing damage each turn)",
        5: "Choose Huge (transform into a particular animal up to Size 15) or Lethal Swarm (transform into a swarm which inflicts lethal damage)"
    },
    "deviations": {
        "Shapeshifter": {"cost": 1, "effect": "Animal Transformation becomes Tiered instead of Discrete and can be activated once per chapter, but yields any shape whose required Magnitude is met."}
    },
    "book": "DTR 138"
}

VARIATION_MIMICRY = {
    "name": "Mimicry",
    "keywords": ["Subtle", "Tiered", "Toggled"],
    "category": "Chimeric",
    "magnitude_effects": {
        1: "You may suppress any Scars that do not exceed Mimicry in Magnitude. Entangled Variations are also suppressed.",
        2: "As Magnitude 1.",
        3: "As Magnitude 1.",
        4: "As Magnitude 1.",
        5: "As Magnitude 1."
    },
    "book": "DTR 139"
}

VARIATION_MONSTROUS_TRANSFORMATION = {
    "name": "Monstrous Transformation",
    "keywords": ["Overt", "Discrete", "Toggled"],
    "category": "Chimeric",
    "magnitude_effects": {
        2: "Choose secondary Variations which could be collectively entangled with a Scar of equal Magnitude to Monstrous Transformation. Activating Monstrous Transformation activates these secondary Variations.",
        3: "As Magnitude 2.",
        4: "As Magnitude 2.",
        5: "As Magnitude 2."
    },
    "book": "DTR 139"
}

VARIATION_PHEROMONES = {
    "name": "Pheromones",
    "keywords": ["Subtle", "Directed", "Perpetual", "Tiered"],
    "category": "Chimeric",
    "magnitude_effects": {
        1: "Improve your impression level upon a living subject, and reduce your exceptional success threshold for Social actions against them to three instead of five.",
        2: "Choose Communication (you and the subject can communicate fluently) or Status (the subject defers as if you possessed half Scar Power in Status in an admired group)",
        3: "Receive both Magnitude 2 benefits.",
        4: "Compel the subject with simple commands. Intelligent subjects resist suicidal commands."
    },
    "deviations": {
        "Aura": {"cost": 1, "effect": "The Variation targets all members of a species in short range."}
    },
    "book": "DTR 140"
}

VARIATION_PREDATORS_CUNNING = {
    "name": "Predator's Cunning",
    "keywords": ["Subtle", "Perpetual", "Reflexive", "Tiered"],
    "category": "Chimeric",
    "magnitude_effects": {
        1: "Choose Elusive (guards and pursuers suffer a -2 penalty to find or tail you, apply half Scar Power as a bonus to maneuver around traps) or Vigilant (when not ambushed, reflexively draw a weapon or activate Lash, and reflexively procure concealment up to half your Scar Power)",
        2: "Receive both Magnitude 1 benefits.",
        3: "Choose Alert (retain Defense and Vigilant benefits when ambushed, make reflexive Stealth roll against unnoticed surveillance) or Uncanny (retain Defense against firearms, ignore Defense penalties from multiple attackers)",
        4: "Receive both Magnitude 3 benefits.",
        5: "When not ambushed, you alone act for a full turn at the beginning of combat. Opponents must roll Wits + Composure - your Scar Power to retain their Defense."
    },
    "book": "DTR 141"
}

# Coactive Variations
VARIATION_BLESSING = {
    "name": "Blessing",
    "keywords": ["Subtle", "Directed", "Perpetual", "Reflexive", "Tiered"],
    "category": "Coactive",
    "magnitude_effects": {
        1: "Choose Lucky (once per chapter, conjure a moderate stroke of fortune, which can apply half Scar Power as a circumstantial bonus) or Unlucky (once per chapter, inflict a moderate stroke of misfortune, which can apply half Scar Power as a penalty)",
        2: "Choose Balanced (receive both Magnitude 1 benefits), Charmed (requires Lucky, once per scene, introduce a favorable turn of events), or Albatross (requires Unlucky, once per scene, inflict a misfortunate plot twist)",
        3: "Choose Destiny's Chosen (receive all Magnitude 2 benefits), Near Miss (requires Lucky, once per chapter, slip away from a scene retroactively), or Supernatural Aid (requires Unlucky, once per chapter, attract the arrival of a known character)",
        4: "Receive all Magnitude 3 benefits."
    },
    "deviations": {
        "Aura": {"cost": 1, "effect": "The Variation can simultaneously target multiple characters in short range, including yourself."}
    },
    "book": "DTR 141"
}

VARIATION_FATES_AGENT = {
    "name": "Fate's Agent",
    "keywords": ["Subtle", "Perpetual", "Reflexive", "Tiered"],
    "category": "Coactive",
    "magnitude_effects": {
        1: "Choose a type of supernatural being. Intuit the use of power by such forces on you or your location, and its source. Attempts to gather information about you by these forces provoke a Clash of Wills.",
        2: "Choose Counter (spend your action in a turn to neutralize such supernatural powers with a Clash of Wills) or Dispel (direct against an appropriate temporary magical effect to end it, or a long-term magical effect to suppress it for a scene)",
        3: "Receive both Magnitude 2 benefits.",
        4: "You may turn Countered personal effects against you back on their source."
    },
    "deviations": {
        "Universal": {"cost": 1, "effect": "The Variation may be activated once per chapter, but works against all supernatural powers, regardless of origin."}
    },
    "book": "DTR 142"
}

VARIATION_OTHERWORLDLY_CONNECTION = {
    "name": "Otherworldly Connection",
    "keywords": ["Subtle", "Perpetual", "Tiered"],
    "category": "Coactive",
    "magnitude_effects": {
        1: "Choose a supernatural nature or origin. Perceive entities and forces that proceed from that nature.",
        2: "Communicate with associated beings, with whom you benefit from half Scar Power in Status.",
        3: "You can physically interact with associated insubstantial beings, and vice-versa.",
        4: "Direct an exorcism or banishment against an associated being. Intelligent beings force a Clash of Wills over the loss of Willpower, and are exorcised for a story when they run out.",
        5: "Direct at an associated being or phenomenon to bring it into the material realm, forcing a Clash of Wills if the being is intelligent. Each summoning after the first in a story inflicts instability."
    },
    "book": "DTR 143"
}

VARIATION_PRECOGNITION = {
    "name": "Precognition",
    "keywords": ["Subtle", "Reflexive", "Tiered", "Toggled"],
    "category": "Coactive",
    "magnitude_effects": {
        1: "Roll chance dice as normal dice. You may spend Willpower to add dice to a pool after rolling.",
        2: "Direct at a subject to glimpse their future, asking up to your Scar Power in questions about their likely future each chapter.",
        3: "Once per chapter, you may avert the results of a failed action by instead performing a different action.",
        4: "Choose Bifurcation (once per chapter, reflexively direct against a subject to force them to perform a different action) or Prophecy (glimpse a scene from later in the story and 'rewind' to do it over)",
        5: "Receive both Magnitude 4 benefits."
    },
    "book": "DTR 144"
}

VARIATION_PSYCHO_ONOMASTICS = {
    "name": "Psycho-Onomastics",
    "keywords": ["Subtle", "Reflexive", "Tiered", "Toggled"],
    "category": "Coactive",
    "magnitude_effects": {
        1: "When someone is introduced by name, you may discern whether it is their true name. If it is, intuit your Scar Power in details about who they are.",
        2: "You can recognize anyone introduced by name no matter their guise or transformation.",
        3: "Choose Invoke Name (hear conversations when your true name is invoked) or True Name (when someone is introduced, intuit their true name and address them across any distance)",
        4: "Receive both Magnitude 3 benefits.",
        5: "Direct against a target you know by true name to temporarily erase their name, preventing magic which uses that name and disrupting identification and records. Spend Willpower to maintain the erasure for a chapter."
    },
    "book": "DTR 145"
}

# Invasive Variations
VARIATION_COMPUTER_AIDED_PROCESSING = {
    "name": "Computer-Aided Processing",
    "keywords": ["Subtle", "Reflexive", "Tiered", "Toggled"],
    "category": "Invasive",
    "magnitude_effects": {
        1: "Choose one benefit (each usable once per chapter): Biokinesis (gain Scar Power + 1 dots of temporary Physical Merits), Combat Programming (gain Scar Power + 1 dots of temporary Fighting Merits), Data Warehouse (gain Scar Power + 1 dots of temporary Mental Merits), Human Clay (reassign up to Scar Power / 2 + 1 dots between two Physical Attributes), or Mind Hack (reassign up to Scar Power / 2 + 1 dots between two Mental Attributes)",
        2: "Choose two total benefits.",
        3: "Choose three total benefits.",
        4: "Choose four total benefits.",
        5: "Choose five total benefits."
    },
    "book": "DTR 145"
}

VARIATION_HIDDEN_COMPARTMENTS = {
    "name": "Hidden Compartments",
    "keywords": ["Subtle", "Tiered", "Toggled"],
    "category": "Invasive",
    "magnitude_effects": {
        1: "Once per scene, withdraw a Size 1 item from your body worth up to half Scar Power in Availability.",
        2: "Once per chapter, draw a Size 1 item worth up to Scar Power in Availability.",
        3: "Once per story or at the cost of instability, draw a Size 1 item up to Availability 5, which may have supernatural properties."
    },
    "deviations": {
        "Extra Capacity": {"cost": 1, "effect": "You may draw items of Size up to (Scar Power / 2 + 1)."},
        "Varied Inventory": {"cost": 1, "effect": "Draw items more frequently: per chapter instead of per story, per scene instead of per chapter, and per turn instead of per scene."}
    },
    "book": "DTR 146"
}

VARIATION_INTEGRATE_TECHNOLOGY = {
    "name": "Integrate Technology",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Invasive",
    "magnitude_effects": {
        1: "Interface with handled tools to apply 8-Again to them.",
        2: "Absorb tools up to half your Scar Power in Size to replicate their function bodily. The total Size of all absorbed tools cannot exceed (Scar Power x Magnitude).",
        3: "Absorbed tools suffer no depletion of power, ammunition, or other materials.",
        4: "You may merge into machine your Size or larger, up to Size 30, taking any actions the machine can. Your Health suffers any Structure damage taken."
    },
    "deviations": {
        "Battery": {"cost": 1, "effect": "Your body can produce an electric charge, which can power devices or issue twice your Scar Power in bashing damage."}
    },
    "book": "DTR 146"
}

VARIATION_OMNICOMPETENCE = {
    "name": "Omnicompetence",
    "keywords": ["Subtle", "Discrete", "Perpetual", "Reflexive"],
    "category": "Invasive",
    "magnitude_effects": {
        1: "Ignore untrained Skill penalties.",
        2: "Ignore untrained Skill penalties, and choose Jack of All (once per chapter, treat all Skills as having a minimum of one dot) or Journeyman (once per chapter, treat any one Skill as having three dots)",
        3: "Ignore untrained Skill penalties, and choose Balanced (receive both Magnitude 2 benefits), Polymath (once per chapter, treat all Skills as having a minimum of three dots), or Mastery (once per chapter, treat any one Skill as having five dots)",
        4: "Ignore untrained Skill penalties, and receive both Polymath and Mastery.",
        5: "Treat all Skills as having a minimum of one dot, receive Journeyman as a once per scene ability, and receive both Polymath and Mastery."
    },
    "book": "DTR 147"
}

VARIATION_SENSOR_ARRAY = {
    "name": "Sensor Array",
    "keywords": ["Subtle", "Perpetual", "Tiered"],
    "category": "Invasive",
    "magnitude_effects": {
        1: "Once per scene, recalibrate your senses to suppress overwhelming extremes, such as blinding light. Prevent associated Personal Tilts and ignore up to -3 in associated penalties.",
        2: "Calibrate fine senses, such as telescopic sight or low light vision, applying a +2 equipment bonus.",
        3: "Calibrate to sense input undetectable to humans, such as supersonic frequencies or radio waves, applying a +3 equipment bonus.",
        4: "Calibrate occult senses, such as ghostly ephemera or astral projections, applying a +2 Occult bonus."
    },
    "deviations": {
        "Rapid": {"cost": 1, "effect": "Calibrate senses reflexively."},
        "Versatile": {"cost": 1, "effect": "Calibrate up to your Scar Power in senses at once, and recalibrate a number of times per scene equal to Scar Power."}
    },
    "book": "DTR 148"
}

# Mutant Variations
VARIATION_ANOMALOUS_BIOLOGY = {
    "name": "Anomalous Biology",
    "keywords": ["Subtle", "Perpetual", "Tiered"],
    "category": "Mutant",
    "magnitude_effects": {
        1: "Add Magnitude as a bonus to play dead, and choose one benefit: Ageless (never age), Bloodless (never bleed, don't bleed out from lethal damage, suffer only bashing from weapons), Breathless (never suffocate, add Scar Power as Stealth bonus), Heartless (no heartbeat, ignore poison and disease), Hungerless (never starve or suffer dehydration), Lifeless (no body warmth, baffle sensors, treat extreme heat/cold as one level lower), Mindless (ignore mundane attempts to assess/influence your mind, resist supernatural with Clash of Wills), Painless (half wound penalties, remain conscious when Health is filled with damage), or Tireless (never require rest)",
        2: "Choose two total benefits.",
        3: "Choose four total benefits.",
        4: "Choose six total benefits.",
        5: "Choose all nine benefits."
    },
    "book": "DTR 148"
}

VARIATION_DEADLY_ICHOR = {
    "name": "Deadly Ichor",
    "keywords": ["Overt", "Discrete", "Reflexive", "Toggled"],
    "category": "Mutant",
    "magnitude_effects": {
        1: "When you suffer lethal damage in close combat, you may reflexively retaliate. Build the attack like a close Lash, which adds Contact to its available choices.",
        2: "As Magnitude 1.",
        3: "As Magnitude 1.",
        4: "As Magnitude 1.",
        5: "As Magnitude 1."
    },
    "deviations": {
        "Proximal": {"cost": 1, "effect": "Retaliate against even unsuccessful close attacks."},
        "Pressurized": {"cost": 1, "effect": "Build like a ranged Lash, and retaliate against ranged attacks."},
        "Retaliatory": {"cost": 2, "effect": "Build like a ranged Lash, and retaliate against even unsuccessful ranged attacks."}
    },
    "book": "DTR 149"
}

VARIATION_INHUMAN_DIGESTION = {
    "name": "Inhuman Digestion",
    "keywords": ["Overt", "Tiered", "Toggled"],
    "category": "Mutant",
    "magnitude_effects": {
        1: "Safely consume and digest any material up to Durability 1. Bites deal lethal damage with 1 armor-piercing.",
        2: "You may copy a Variation and entangled Scar from a bitten Deviant for a scene.",
        3: "Once per chapter, you may steal a Variation and entangled Scar from a bitten Deviant for a chapter. You may spend experiences to render the theft permanent."
    },
    "deviations": {
        "Adamant Jaws": {"cost": 1, "effect": "Consume materials of any Durability. Add half Scar Power to armor-piercing."},
        "Cannibalize": {"cost": 1, "effect": "Bites deal aggravated damage. Each wound bitten from a humanoid heals a non-aggravated wound."}
    },
    "book": "DTR 149"
}

VARIATION_RAPID_HEALING = {
    "name": "Rapid Healing",
    "keywords": ["Subtle", "Discrete", "Perpetual", "Persistent only"],
    "category": "Mutant",
    "magnitude_effects": {
        1: "Heal twice as fast.",
        2: "Heal one bashing wound each turn, and all bashing damage and minor ailments at the end of a scene.",
        3: "As Magnitude 2, and heal all lethal damage and common diseases and poisons at the end of a chapter.",
        4: "Heal one non-aggravated wound each turn, all non-aggravated damage and ailments at the end of a scene, and all aggravated damage and bodily impairments at the end of a chapter.",
        5: "As Magnitude 4, and recover from any death except the End Stage."
    },
    "book": "DTR 151"
}

VARIATION_SACRED_FLESH = {
    "name": "Sacred Flesh",
    "keywords": ["Subtle", "Discrete", "Toggled"],
    "category": "Mutant",
    "magnitude_effects": {
        1: "Choose a secondary Variation of equal Magnitude. You can bestow use of the Variation to others for a scene by one chosen method: Boon (direct Sacred Flesh to bestow on a target), Secretion (once per chapter, produce your Scar Power in doses of a medium), Token (as Secretion, but producing the medium inflicts minor instability, and doses do not expire), or Fragment (as Secretion, but you produce one reusable medium that does not expire, once per story or by risking instability)",
        2: "As Magnitude 1.",
        3: "As Magnitude 1.",
        4: "As Magnitude 1.",
        5: "As Magnitude 1."
    },
    "deviations": {
        "Flexibility": {"cost": 1, "effect": "Choose half Scar Power in extra methods."},
        "Self-Cannibalism": {"cost": 1, "effect": "You can bestow the Variation to yourself."}
    },
    "book": "DTR 151"
}


# Controlled Scars
SCAR_CONCENTRATION = {
    "name": "Concentration",
    "keywords": ["Subtle", "Mental", "Repeatable"],
    "activation": "Controlled",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat when distraction causes Variation to shut down or misfire.",
        2: "Lethal damage, Faltering, Stunned or Distracted provoke Scar Resistance. On failure, Variation deactivates.",
        3: "As Magnitude 2, and choose Tenuous (attacks/hostile powers provoke) or Unfocused (distracting Tilts require Scar Resistance)",
        4: "As Magnitude 3, but suffer both complications."
    },
    "deviations": {
        "After-Effect": {"cost": 1, "effect": "Directed-Only. Directing for more consecutive turns than Scar Resistance inflicts chosen negative Condition."},
        "Self-Doubt": {"cost": 1, "effect": "Effect shuts down Variations for full scene."},
        "Single-Minded": {"cost": 1, "effect": "Directed-Only. Failing to direct active Variation for a turn provokes Scar Resistance."}
    },
    "book": "DTR 152"
}

SCAR_COOLDOWN = {
    "name": "Cooldown",
    "keywords": ["Subtle", "Any", "Directed-Only", "Repeatable"],
    "activation": "Controlled",
    "category": "Any",
    "magnitude_effects": {
        1: "Take a beat when repeated use causes Variation to fail or malfunction.",
        2: "Directing on consecutive turns inflicts cumulative -1 Scar Finesse penalty. Dissipates when not directing for a turn.",
        3: "As Magnitude 2, but penalty starts at (6 - Scar Resistance), and dissipates by 1 per turn without directing.",
        4: "As Magnitude 3, and choose Blackout (dramatic failure shuts down for scene) or Ponderous (reducing penalty takes 2 turns)",
        5: "As Magnitude 4, but suffer both complications."
    },
    "book": "DTR 153"
}

SCAR_DEPLETION = {
    "name": "Depletion",
    "keywords": ["Subtle", "Any", "Repeatable"],
    "activation": "Controlled",
    "category": "Any",
    "magnitude_effects": {
        1: "Take a beat to briefly exhaust use of Variation.",
        2: "Variations function up to Scar Resistance consecutive turns before needing instant action to replenish.",
        3: "As Magnitude 2, but recharging forfeits Defense, and each successive recharge takes another consecutive action.",
        4: "As Magnitude 3, and choose Brief (single turn depletes) or Slow-Charging (recharging takes (6 - Scar Resistance) hours)",
        5: "As Magnitude 4, but suffer both complications."
    },
    "deviations": {
        "Hazardous Recharge": {"cost": 1, "effect": "Recharging inflicts lethal damage."}
    },
    "book": "DTR 153"
}

SCAR_ADDICTIVE_VARIATION = {
    "name": "Addictive Variation",
    "keywords": ["Subtle", "Mental or Physical", "Toggled-Only"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to suffer from withdrawal or wield power just to stave it off.",
        2: "Suffer Addicted (Persistent), becoming Deprived when you go for a chapter without activating an entangled Variation.",
        3: "As Magnitude 2, and choose Disorienting (while entangled Variations are active, suffer Intoxicated or Drugged) or Lingering (Deprived becomes Persistent, resolving by recovering medium instability or spending a story without activating any entangled Variations)",
        4: "As Magnitude 3, and choose Compounded (suffer both Magnitude 3 complications) or Severe (increase the Deprived penalty to -2, and apply it to derived traits)",
        5: "As Magnitude 4, but suffer both complications."
    },
    "book": "DTR 158"
}

# Additional Controlled Scars
SCAR_DETERIORATION = {
    "name": "Deterioration",
    "keywords": ["Overt", "Physical", "Repeatable"],
    "activation": "Controlled",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when using an entangled Variation to suffer temporary debility.",
        2: "Activating an entangled Variation provokes Scar Resistance. On failure, suffer your choice of Arm Wrack, Blinded, Deafened, or Leg Wrack for the scene.",
        3: "As Magnitude 2, and choose Lingering (debility lasts for a chapter, becoming a corresponding Persistent Condition) or Painful (activating also inflicts bashing damage) or Severe (suffer a severe version of the debility)",
        4: "As Magnitude 3, but choose two complications.",
        5: "As Magnitude 3, but suffer all three complications."
    },
    "book": "DTR 153"
}

SCAR_FLUCTUATING_VARIATION = {
    "name": "Fluctuating Variation",
    "keywords": ["Subtle", "Any", "Repeatable", "Tiered-Only"],
    "activation": "Controlled",
    "category": "Any",
    "magnitude_effects": {
        3: "Choose how each entangled Variation behaves at each possible Magnitude. Entangled Variations activate at a Magnitude equal to your activation successes. For each turn an entangled Variation remains active, it shifts one dot of Magnitude; roll Scar Resistance to control which direction it shifts."
    },
    "book": "DTR 154"
}

SCAR_PERILOUS_VARIATION = {
    "name": "Perilous Variation",
    "keywords": ["Overt", "Physical", "Repeatable"],
    "activation": "Controlled",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when the pain of activating an entangled Variation hinders you.",
        2: "Activating an entangled Variation inflicts bashing damage.",
        3: "Activating an entangled Variation inflicts lethal damage.",
        4: "Activating an entangled Variation inflicts aggravated damage."
    },
    "deviations": {
        "Ongoing": {"cost": 2, "effect": "Directed only. Directing an entangled Variation also inflicts damage."}
    },
    "book": "DTR 154"
}

SCAR_PERSISTENT_DRAWBACK = {
    "name": "Persistent Drawback",
    "keywords": ["Subtle", "Secondary", "Repeatable"],
    "activation": "Controlled",
    "category": "Any",
    "magnitude_effects": {
        1: "Choose a Persistent Scar of equal Magnitude. While any entangled Variations are active, suffer the effects of that Scar.",
        2: "As Magnitude 1.",
        3: "As Magnitude 1.",
        4: "As Magnitude 1.",
        5: "As Magnitude 1."
    },
    "deviations": {
        "Continual": {"cost": 1, "effect": "Always suffer the secondary Scar's effects."}
    },
    "book": "DTR 154"
}

SCAR_POWER_FAILURE = {
    "name": "Power Failure",
    "keywords": ["Subtle", "Any", "Repeatable"],
    "activation": "Controlled",
    "category": "Any",
    "magnitude_effects": {
        1: "Take a beat when your entangled Variations weaken or fail because of a chosen circumstance, such as 'on holy ground' or 'suffering lethal damage'.",
        2: "The chosen circumstance provokes a Scar Resistance roll each turn to prevent Magnitude loss, and penalizes Scar Finesse to activate them by (6 - Scar Resistance).",
        3: "As Magnitude 2, but failing Scar Resistance instead deactivates that Variation for as long as the circumstance persists.",
        4: "As Magnitude 3, but the Variation remains deactivated for a scene minimum.",
        5: "As Magnitude 3, but the Variation remains deactivated for a chapter minimum."
    },
    "deviations": {
        "Rare": {"cost": -1, "effect": "The circumstance is very specific or narrow."},
        "Common": {"cost": 1, "effect": "The circumstance is common or easy to encounter."}
    },
    "book": "DTR 155"
}

SCAR_PREPARATION = {
    "name": "Preparation",
    "keywords": ["Subtle", "Any", "Repeatable"],
    "activation": "Controlled",
    "category": "Any",
    "magnitude_effects": {
        1: "Take a beat when your entangled Variations take too long to activate.",
        2: "Activating an entangled Variation first requires a ritual, input sequence, or other instant action.",
        3: "As Magnitude 2, and choose Elaborate (priming an entangled Variation sacrifices Defense and takes up to three actions or one hour with low Scar Resistance) or Staged (the activating Scar Finesse roll becomes an extended action with a target of twice Magnitude)",
        4: "As Magnitude 2, and choose Grueling (as Staged, but each interval sacrifices Defense and takes extra time as per Elaborate priming) or Lengthy (as Elaborate, but entangled Variations cannot be primed during action scenes)",
        5: "As Magnitude 4, but suffer both complications."
    },
    "deviations": {
        "Recharge": {"cost": 1, "effect": "Directed-Only. After directing an entangled Variation, you must wait (4 - Scar Resistance ÷ 2) turns to direct again."}
    },
    "book": "DTR 155"
}

SCAR_TABULA_RASA = {
    "name": "Tabula Rasa",
    "keywords": ["Subtle", "Mental"],
    "activation": "Controlled",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to forget something important from the stress of using entangled Variations.",
        2: "Remembering what occurred while using entangled Variations provokes Scar Resistance, or penalizes other rolls involving relevant details by -2.",
        3: "Lose all memory of scenes wherein you activated entangled Variations. Given a strong reminder, you may spend Willpower to recover the memory for a scene, and doing so (6 - Scar Resistance) times recovers it permanently.",
        4: "As Magnitude 3, and choose Permanence (you may not spend Willpower to recover memories) or Rapid (memory loss sets in immediately after a turn of Variation use)",
        5: "As Magnitude 4, but suffer both complications."
    },
    "book": "DTR 155"
}

SCAR_TRIBULATION = {
    "name": "Tribulation",
    "keywords": ["Subtle", "Mental", "Repeatable"],
    "activation": "Controlled",
    "category": "Mental",
    "magnitude_effects": {
        3: "You must spend Willpower to activate entangled Variations.",
        4: "As Magnitude 3, and paying the activation cost takes an instant action."
    },
    "deviations": {
        "Draining": {"cost": 2, "effect": "Directed-Only. You must also spend Willpower to direct the Variation for a turn."}
    },
    "book": "DTR 156"
}

SCAR_UNSTABLE_VARIATION = {
    "name": "Unstable Variation",
    "keywords": ["Subtle", "Any", "Repeatable"],
    "activation": "Controlled",
    "category": "Any",
    "magnitude_effects": {
        1: "Take a beat to temporarily suffer more from Scars due to using entangled Variations.",
        2: "Activating an entangled Variation worsens a Scar by a dot of Magnitude and inflicts a -2 Scar Resistance penalty for the rest of the scene.",
        3: "As Magnitude 2, and activating entangled Variations inflicts minor instability.",
        4: "As Magnitude 3, but the instability is medium.",
        5: "As Magnitude 3, but the instability is major."
    },
    "book": "DTR 156"
}

# Involuntary Scars
SCAR_INVOLUNTARY_STIMULUS = {
    "name": "Involuntary Stimulus",
    "keywords": ["Subtle", "Any", "Repeatable"],
    "activation": "Involuntary",
    "category": "Any",
    "magnitude_effects": {
        1: "Take a beat when your entangled Variations act up in a chosen circumstance, such as 'under a full moon' or 'when enraged'.",
        2: "Self-activated Variations become Overt, and choose Insistent (the stimulus provokes Scar Resistance, and activates entangled Variations on failure) or Reactive (the stimulus prevents deactivating the Variation until you take an appropriate rolled action to insulate yourself)",
        3: "As Magnitude 2, but suffer both complications."
    },
    "deviations": {
        "Rare": {"cost": -1, "effect": "The circumstance is very specific or narrow."},
        "Common": {"cost": 1, "effect": "The circumstance is common or easy to encounter."},
        "Uncontrollable": {"cost": 1, "effect": "You cannot voluntarily activate the entangled Variations."},
        "Unpredictable": {"cost": 1, "effect": "Once per scene, the Storyteller may provoke Scar Resistance. On failure, entangled Variations activate themselves."}
    },
    "book": "DTR 156"
}

SCAR_POWER_BUILD_UP = {
    "name": "Power Build-Up",
    "keywords": ["Subtle", "Any", "Repeatable"],
    "activation": "Involuntary",
    "category": "Any",
    "magnitude_effects": {
        1: "Take a beat when entangled Variations erupt and lash out.",
        2: "Entangled Variations become Overt, and choose Insistent (once per scene, the Storyteller may provoke Scar Resistance. On failure, the Variation activates itself) or Volcanic (you must roll Scar Resistance to deactivate an entangled Variation before the end of the scene)",
        3: "As Magnitude 2, and choose Compounded (suffer both Magnitude 2 complications) or Uncontrollable (requires Insistent. You can only activate an entangled Variation once per chapter) or Destructive (requires Volcanic. Directed only. The Storyteller may direct an activated entangled Variation you are not currently directing)",
        4: "Directed only. As Magnitude 3, but suffer all three complications."
    },
    "book": "DTR 157"
}

# Additional Persistent Scars
SCAR_ALTERNATE_PERSONA = {
    "name": "Alternate Persona",
    "keywords": ["Subtle", "Mental or Social", "Repeatable"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to switch personalities.",
        2: "Once per scene, the Storyteller may provoke Scar Resistance. On failure, your other personality surfaces for (6 - Scar Resistance) turns.",
        3: "As Magnitude 2, but you also shift personalities at regular intervals. You may roll Scar Resistance to surface the other personality for (Scar Resistance) turns."
    },
    "deviations": {
        "Forgetful Persona": {"cost": -1, "effect": "The alternate persona lacks the primary persona's memories."},
        "Inferior Persona": {"cost": -1, "effect": "The alternate persona cannot activate Variations not entangled with this Scar."},
        "Invoked": {"cost": -1, "effect": "You may choose to shift personalities as an instant action."},
        "Partner": {"cost": -1, "effect": "The personas share general goals, and do not differ in Aspiration."},
        "Perfect Recall": {"cost": -1, "effect": "The primary persona retains full memory of the alternate persona's actions."},
        "Aware Persona": {"cost": 1, "effect": "The alternate persona retains full memory of the primary persona's actions."},
        "Bestial": {"cost": 1, "effect": "The alternate persona lacks higher thought and suffers the Bestial Condition."},
        "Blackouts": {"cost": 1, "effect": "The primary persona lacks the alternate persona's memories."},
        "Cross-Purposes": {"cost": 1, "effect": "The personas have conflicting goals, and the alternate Persona has its own distinct Touchstones."},
        "Superior Persona": {"cost": 1, "effect": "Only the alternate persona can activate Variations entangled with this Scar."}
    },
    "book": "DTR 158"
}

SCAR_AMNESIA = {
    "name": "Amnesia",
    "keywords": ["Subtle", "Mental"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Suffer Amnesia (Persistent).",
        2: "As Magnitude 1. Also penalize rolls to remember facts from before your Divergence by -2, and lose one key memory from that time altogether.",
        3: "As Magnitude 2, but increase the penalty to -4, and lose multiple key memories.",
        4: "As Magnitude 3, but completely lose your memory of several years. You may be Shaken by revelations of the past.",
        5: "As Magnitude 4, but lose all memories prior to Divergence. You may Falter from revelations of the past."
    },
    "book": "DTR 159"
}

SCAR_BANE = {
    "name": "Bane",
    "keywords": ["Subtle", "Physical", "Repeatable"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when you suffer pain from exposure to a certain material or stimulus, like silver or bright light.",
        2: "Direct exposure to your bane inflicts a bashing wound each turn, or upgrades damage type if already harmful, and prevents healing.",
        3: "As Magnitude 2, but the bane inflicts lethal wounds, or upgrades damage and adds an additional wound.",
        4: "As Magnitude 3, but the bane inflicts aggravated wounds, or upgrades and doubles damage."
    },
    "deviations": {
        "Rare": {"cost": -1, "effect": "The bane is very specific or rare."},
        "Common": {"cost": 1, "effect": "The bane is common or easy to encounter."},
        "Draining": {"cost": 1, "effect": "Toggled-Only. Each turn of direct exposure reduces the Magnitude of entangled Variations for the scene."},
        "Paralyzing": {"cost": 1, "effect": "Direct exposure inflicts Stunned or Insensate."}
    },
    "book": "DTR 160"
}

SCAR_BESTIAL_MIND = {
    "name": "Bestial Mind",
    "keywords": ["Subtle", "Mental"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat when animal instincts inspire ill-advised behavior.",
        2: "Suffer Bestial (Persistent).",
        3: "As Magnitude 2, and during combat, roll Scar Resistance to resist your choice of Beaten Down, Insane, Insensate, or Stunned.",
        4: "As Magnitude 3, and you cannot Build Equipment. Suffer a (6 - Scar Resistance) penalty to Mental Skills.",
        5: "As Magnitude 4, and you can only use the simplest of tools."
    },
    "book": "DTR 161"
}

SCAR_CONSPICUOUS_APPEARANCE = {
    "name": "Conspicuous Appearance",
    "keywords": ["Overt", "Physical or Social"],
    "activation": "Persistent",
    "category": "Social",
    "magnitude_effects": {
        1: "Take a beat to draw unwelcome attention from particular unnatural features. Conspiracies gain half Magnitude as a surveillance bonus.",
        2: "You must contest Wits + Subterfuge vs Wits + Composure to hide your unnatural features. Baseline humans who notice worsen impression and strip 10-Again from Social rolls.",
        3: "As Magnitude 2, but take a -3 penalty to conceal your appearance. Suffer Notoriety (Persistent).",
        4: "As Magnitude 3, but you cannot hide your unnatural appearance at all. Choose Terrible (all Social rolls against Baselines reduced to chance die, except Intimidation which gains +2 bonus) or Monstrous (suffer Hunted (Persistent). Monster hunters pursue you)",
        5: "As Magnitude 4, but suffer both complications."
    },
    "book": "DTR 161"
}

SCAR_DEPENDENCY = {
    "name": "Dependency",
    "keywords": ["Subtle", "Physical", "Repeatable"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Suffer one withdrawal symptom, staved off for two chapters by a given material treatment or intake. Gathering supply takes effort and a roll at a penalty of (6 - Scar Resistance).",
        2: "Suffer two withdrawal symptoms.",
        3: "Suffer three withdrawal symptoms.",
        4: "Suffer four withdrawal symptoms.",
        5: "Suffer five withdrawal symptoms: Fatigued, Ill (cannot heal, suffer daily bashing wound), Sluggish (penalize Initiative and Speed by -3 and Physical actions by -2), Submissive (suffer Broken, or during action scenes, Beaten Down)."
    },
    "deviations": {
        "Common": {"cost": -1, "effect": "Supply is easily acquired, imposing no penalty."},
        "Rare": {"cost": 1, "effect": "Supply is rare and precious, and acquisition is always contested."}
    },
    "book": "DTR 162"
}

SCAR_FRAGILITY = {
    "name": "Fragility",
    "keywords": ["Subtle", "Physical"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when you are hindered by the pain of your condition.",
        2: "Suffer Stunned for a turn the first time in a scene your wound penalty escalates.",
        3: "Suffer Stunned for a turn whenever your wound penalty escalates.",
        4: "Suffer Immobilized for (6 - Scar Resistance) turns whenever your wound penalty escalates.",
        5: "As Magnitude 4, and when a scene begins while you suffer damage, suffer Disabled until you fully recover."
    },
    "book": "DTR 163"
}

SCAR_FROZEN_HEART = {
    "name": "Frozen Heart",
    "keywords": ["Subtle", "Social"],
    "activation": "Persistent",
    "category": "Social",
    "magnitude_effects": {
        1: "Take a beat to turn away help and close yourself off.",
        2: "Raise the unskilled Social penalty to -3, and reduce your maximum rating in Empathy, Expression, and Persuasion by half Magnitude.",
        3: "As Magnitude 2, and begin every chapter Stoic.",
        4: "As Magnitude 3, but you may not voluntarily fail a roll to resolve Stoic. Choose either Loyalty or Conviction. Whenever you uphold that Anchor's Touchstones, you may recover Willpower or heal instability, not both.",
        5: "As Magnitude 4, but the complication applies to both Anchors."
    },
    "book": "DTR 163"
}

SCAR_GENETIC_DISORDER = {
    "name": "Genetic Disorder",
    "keywords": ["Subtle", "Physical"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat to suffer a spell of weakness.",
        2: "Suffer the moderate Sick Tilt, or outside action scenes, penalize strenuous physical actions by half Magnitude.",
        3: "As Magnitude 2, and fatigue sets in after six sleepless hours.",
        4: "As Magnitude 3, but suffer the severe Sick Tilt.",
        5: "As Magnitude 4, and you must roll Scar Resistance daily, with any appropriate equipment bonuses to resist your condition. On failure, suffer a lethal wound or minor instability."
    },
    "book": "DTR 163"
}

SCAR_GLITCH = {
    "name": "Glitch",
    "keywords": ["Subtle", "Mental"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to fail an action due to momentary confusion.",
        2: "After spending Willpower on a roll bonus, you cannot do so again that scene without first suffering a voluntary failure.",
        3: "As Magnitude 2, and spending Willpower on a roll bonus inflicts Distracted, resolved by voluntary failure or healing instability.",
        4: "As Magnitude 3, but the same complications apply to spending Willpower costs for Variations, Scars, or Adaptations.",
        5: "As Magnitude 4, but these complications apply to all Willpower expenditures, and you must recover all Willpower to resolve Distracted."
    },
    "book": "DTR 163"
}

SCAR_HALLUCINATIONS = {
    "name": "Hallucinations",
    "keywords": ["Subtle", "Mental or Social"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to disrupt a scene by interacting with delusions.",
        2: "Once per scene, the Storyteller may provoke Scar Resistance. On failure, you suffer Distracted.",
        3: "As Magnitude 2, and once per chapter, the Storyteller may introduce a hallucinated entity to the scene. Interventions from others may allow a Scar Resistance roll to dispel the hallucination.",
        4: "As Magnitude 3, and choose Phantasmagoria (hallucinations can turn perceived scenes intense and complicated) or Stubborn (only the intervention of Loyalty Touchstones can help dispel hallucinations)",
        5: "As Magnitude 4, but suffer both complications."
    },
    "book": "DTR 164"
}

SCAR_HEMOPHILIA = {
    "name": "Hemophilia",
    "keywords": ["Subtle", "Physical"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when you suffer from an otherwise light injury.",
        2: "When bashing damage escalates your wound penalty, upgrade a bashing wound to lethal.",
        3: "As Magnitude 2, and when non-bashing damage escalates your wound penalty, suffer a lethal wound every minute until you receive medical attention.",
        4: "As Magnitude 3, and after a scene in which you suffer damage, suffer Disabled.",
        5: "As Magnitude 4, but all damage provokes the Scar, not just when it escalates wound penalties."
    },
    "book": "DTR 164"
}

SCAR_LYING_EYES = {
    "name": "Lying Eyes",
    "keywords": ["Subtle", "Social"],
    "activation": "Persistent",
    "category": "Social",
    "magnitude_effects": {
        1: "Take a beat to dramatically fail a Social action, seeming untrustworthy or dangerous.",
        2: "Suffer Notoriety with strangers and new acquaintances.",
        3: "As Magnitude 2, and worsen impressions from strangers. All Social failures on new meetings are dramatic failures.",
        4: "As Magnitude 3, but treat everyone except close friends and proven allies as strangers.",
        5: "As Magnitude 4, and strangers' impressions remain hostile except under leverage."
    },
    "book": "DTR 164"
}

SCAR_MAINTENANCE = {
    "name": "Maintenance",
    "keywords": ["Subtle", "Mental or Physical", "Repeatable", "Toggled-Only"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when an entangled Variation misfires and needs brief maintenance.",
        2: "Entangled Variations function for a scene before requiring some form of repair or treatment, with each maintenance roll taking (12 - Scar Resistance) minutes. You must roll Scar Resistance to activate a Variation still in need of maintenance, and cannot reattempt this roll after failing.",
        3: "As Magnitude 2, and choose Dependent (someone else must perform maintenance, though you may assist through teamwork) or Time-Consuming (maintenance takes hours instead of minutes) or Volatile (choose an added cost to the Scar Resistance roll above: Willpower, minor instability, or a lethal wound)",
        4: "As Magnitude 3, but choose two complications.",
        5: "As Magnitude 3, but suffer all three complications."
    },
    "book": "DTR 165"
}

SCAR_MISFORTUNE = {
    "name": "Misfortune",
    "keywords": ["Subtle", "Any"],
    "activation": "Persistent",
    "category": "Any",
    "magnitude_effects": {
        1: "Take a beat to suffer a voluntary failure from a turn of bad luck or circumstance.",
        2: "Once per chapter, the Storyteller may introduce an inconvenient misfortune. The misfortune may impose (6 - Scar Resistance) as a dice penalty, or as a bonus to an opposing action.",
        3: "As Magnitude 2, and choose Cursed (once per chapter, the Storyteller may introduce a severe misfortune or great coincidence) or Frequent (inconvenient misfortune strikes once per scene)",
        4: "As Magnitude 3, but suffer both complications."
    },
    "deviations": {
        "Association": {"cost": 1, "effect": "The Storyteller may target cohorts or Loyalty Touchstones with your misfortune."}
    },
    "book": "DTR 165"
}

SCAR_MISSING_LIMB = {
    "name": "Missing Limb",
    "keywords": ["Overt", "Physical"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when deterred by limited use of your limb.",
        2: "One of your appendages is damaged or malformed. Choose Hands (take a -2 penalty to manual dexterity) or Feet (half Speed. -1 to Defense and to Physical locomotion)",
        3: "You entirely lack one limb or its use. Permanently suffer either moderate Arm or Leg Wrack.",
        4: "You lack two limbs or their use. Permanently suffer either severe Arm Wrack, severe Leg Wrack, or both moderate Arm and Leg Wrack.",
        5: "You've lost all four limbs. Permanently suffer both severe Arm and Leg Wrack, as well as Disabled (Persistent)."
    },
    "book": "DTR 165"
}

SCAR_MURDEROUS_URGE = {
    "name": "Murderous Urge",
    "keywords": ["Subtle", "Mental"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to inappropriately escalate a confrontation.",
        2: "Confrontations outside of cohorts and Loyalty Touchstones provoke Scar Resistance. On failure, escalate hostility to threats, threats to violence, and violence to deadly force for the scene. You may then roll Scar Resistance to deescalate.",
        3: "As Magnitude 2, but you may not deescalate. You must either take a life or be restrained for (6 - Scar Resistance) turns.",
        4: "As Magnitude 3, but taking a life still requires a Scar Resistance roll to deescalate. On failure, seek another victim.",
        5: "As Magnitude 4, but cohorts and Loyalty Touchstones are not excluded. Dramatic failure on Scar Resistance prevents murder from ending the rampage."
    },
    "book": "DTR 166"
}

SCAR_NATIVE_ENVIRONMENT = {
    "name": "Native Environment",
    "keywords": ["Subtle", "Physical"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Choose a particular type of environment, such as forests or underwater. Take a beat to suffer hardships outside your native environment. Above Magnitude 1, treat other environments as extreme environments of a level equal to (Magnitude - 1), which may impose appropriate Environmental Tilts.",
        2: "As Magnitude 1.",
        3: "As Magnitude 1.",
        4: "As Magnitude 1.",
        5: "As Magnitude 1."
    },
    "deviations": {
        "Acclimated": {"cost": -1, "effect": "Within your native environment, ignore native Environmental Tilts and extreme environments up to the level you suffer from foreign environments."}
    },
    "book": "DTR 166"
}

SCAR_PARANOIA = {
    "name": "Paranoia",
    "keywords": ["Subtle", "Mental or Social"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to undermine yourself with mistrust.",
        2: "Disruptions to your routine or expectations of a person's behavior provoke Scar Resistance. On failure, suffer a -2 penalty to perception, Social actions, and using Social Merits.",
        3: "As Magnitude 2, but suffer Spooked on failure, and until the end of the scene, Social and perception rolls secretly contest against false conclusions.",
        4: "As Magnitude 3, and while Spooked, you cannot create Loyalty Touchstones or restore them from Wavering. Once per scene, the Storyteller may reduce a secret contest to a chance die.",
        5: "As Magnitude 4, and you may not convert a Conviction Touchstone into a Loyalty Touchstone without Wavering."
    },
    "book": "DTR 167"
}

SCAR_PHILIA = {
    "name": "Philia",
    "keywords": ["Subtle", "Mental", "Repeatable"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to indulge in your philia in a way that causes complications.",
        2: "Whenever you have a chance to indulge, suffer (6 - Scar Resistance) to actions that don't enable you to do so. When indulging, your attention is held by it for (6 - Scar Resistance) minutes.",
        3: "Choose Consuming (roll Scar Resistance to turn away from indulging yourself, each turn in action scenes) or Destructive (take 1L when indulging) or Routine (suffer a minor Instability each chapter you don't indulge)",
        4: "Choose two Magnitude 3 complications.",
        5: "Suffer all Magnitude 3 complications."
    },
    "deviations": {
        "Rare": {"cost": -1, "effect": "The philia is very specific or uncommon."},
        "Common": {"cost": 1, "effect": "The philia is prolific or easy to encounter."}
    },
    "book": "DevC 16"
}

SCAR_PHOBIA = {
    "name": "Phobia",
    "keywords": ["Subtle", "Mental", "Repeatable"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat when your particular phobia emerges at an inopportune time.",
        2: "You must roll Scar Resistance to voluntarily confront your phobia. While you face your phobia, penalize all actions by (6 - Scar Resistance). Spend Willpower to suppress your fear for a scene.",
        3: "As Magnitude 2, but you may not suppress your fear with Willpower, and Scar Resistance rolls only let you confront your phobia for (Scar Resistance) turns before you must roll again.",
        4: "Your phobia inflicts Frightened, or when escape is impossible, Insensate. Even when your phobia is a direct threat, you must spend Willpower to resist, and suffer a (6 - Scar Resistance) penalty to do so."
    },
    "deviations": {
        "Rare": {"cost": -1, "effect": "The phobia is very specific or uncommon."},
        "Common": {"cost": 1, "effect": "The phobia is prolific or easy to encounter."}
    },
    "book": "DTR 167"
}

SCAR_SENSORY_DEPRIVATION = {
    "name": "Sensory Deprivation",
    "keywords": ["Subtle", "Physical"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when dulled or impaired sense.",
        2: "Choose one, suffering a -3 penalty on actions that rely on that sense: Ageusia (no sense of taste), Anosmia (no sense of smell), or Hearing (suffer partial deafness, applying the moderate Deafened Tilt)",
        3: "Choose Combined (suffer both Ageusia and Anosmia) or Deaf (total deafness, applying Deaf (Persistent) and the severe Deafened Tilt) or Eyesight (partial blindness, applying the moderate Blinded Tilt)",
        4: "Choose either two Magnitude 3 complications, or Blind (total blindness, applying Blind (Persistent) and the severe Blinded Tilt)",
        5: "Choose either all three Magnitude 3 complications, or one Magnitude 3 complication and Blind."
    },
    "book": "DTR 168"
}

SCAR_SILENCE = {
    "name": "Silence",
    "keywords": ["Subtle", "Social"],
    "activation": "Persistent",
    "category": "Social",
    "magnitude_effects": {
        1: "Take a beat when you are unable to express yourself clearly.",
        2: "Your power of speech is limited. Reduce your maximum rating in Persuasion, Socialize, and Subterfuge by Magnitude, and suffer a -2 Social penalty when nonverbal cues are unavailable.",
        3: "As Magnitude 2, and you cannot speak verbally.",
        4: "As Magnitude 3, and you cannot communicate in formally structured language, verbal or otherwise. Communication through body language requires an Expression roll at a -4 penalty."
    },
    "book": "DTR 168"
}

SCAR_SLUGGISH_METABOLISM = {
    "name": "Sluggish Metabolism",
    "keywords": ["Subtle", "Physical"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat to suffer from poor constitution and slow recovery.",
        2: "Heal half as quickly. Suffer a (6 - Scar Resistance) Stamina penalty to resist toxins.",
        3: "As Magnitude 2, and choose Glacial (instead heal bashing wounds in two days, lethal wounds weekly, and aggravated wounds monthly) or Incurable (resist supernatural healing) or Invalid (you require long-term infrastructural treatment or repairs to heal non-bashing damage)",
        4: "As Magnitude 3, but choose two complications.",
        5: "As Magnitude 3, but suffer all three complications."
    },
    "book": "DTR 168"
}

SCAR_SUBLIMINAL_CONDITIONING = {
    "name": "Subliminal Conditioning",
    "keywords": ["Subtle", "Mental or Social"],
    "activation": "Persistent",
    "category": "Mental",
    "magnitude_effects": {
        1: "Take a beat to respond to a certain trigger stimulus with a compulsive response.",
        2: "Your compulsion holds sway for (6 - Scar Resistance) turns of defined command or forbiddance. You may stop yourself with a Scar Resistance roll if the compulsion would make you falter.",
        3: "As Magnitude 2, and while under compulsion, you must obey orders issued by the source of the stimulus. Scar Resistance only lasts for a turn before it must be rerolled.",
        4: "As Magnitude 3, but the compulsion holds sway for a full scene. Every (6 - Scar Resistance) turns, you may roll Scar Resistance to suppress compulsion for your Scar Resistance in turns."
    },
    "deviations": {
        "Rare": {"cost": -1, "effect": "The trigger is very detailed or requires specific equipment."},
        "Common": {"cost": 1, "effect": "The trigger is common or easy to encounter."},
        "Complex": {"cost": 1, "effect": "Once per chapter, the Storyteller may cause compulsion through unknown or unexpected trigger."}
    },
    "book": "DTR 169"
}

SCAR_SUPPRESSION = {
    "name": "Suppression",
    "keywords": ["Subtle", "Any", "Repeatable"],
    "activation": "Persistent",
    "category": "Any",
    "magnitude_effects": {
        1: "Specify an Attribute. Take a beat to suffer voluntary failure when exercising the Attribute. Above Magnitude 1, that Attribute's actions lose 10-Again, and you may not spend Willpower to boost them. For each Magnitude dot above 2, treat the Attribute as one dot lower for all purposes except Scar Finesse, Scar Power, and Scar Resistance.",
        2: "As Magnitude 1.",
        3: "As Magnitude 1.",
        4: "As Magnitude 1.",
        5: "As Magnitude 1."
    },
    "book": "DTR 170"
}

SCAR_THIN_SKIN = {
    "name": "Thin Skin",
    "keywords": ["Subtle", "Physical"],
    "activation": "Persistent",
    "category": "Physical",
    "magnitude_effects": {
        1: "Take a beat when you cave or buckle under heightened pain. Above Magnitude 1, reduce your health by one, two, four, or eight points, according to Magnitude.",
        2: "As Magnitude 1.",
        3: "As Magnitude 1.",
        4: "As Magnitude 1.",
        5: "As Magnitude 1."
    },
    "deviations": {
        "Painful": {"cost": 1, "effect": "Wound penalties set in one wound sooner, escalating to a maximum -4."},
        "Agonizing": {"cost": 2, "effect": "Wound penalties set in two wounds sooner, escalating to a maximum -5."}
    },
    "book": "DTR 170"
}

SCAR_TRUSTING = {
    "name": "Trusting",
    "keywords": ["Subtle", "Social"],
    "activation": "Persistent",
    "category": "Social",
    "magnitude_effects": {
        1: "Take a beat when your trusting nature causes a complication.",
        2: "Choose Credulous (suffer a (6 - Scar Resistance) penalty on Empathy rolls to detect deception) or Transparent (suffer a (6 - Scar Resistance) penalty on Subterfuge rolls to lie to another)",
        3: "Suffer both Magnitude 2 complications.",
        4: "Once per chapter, when a Loyalty Touchstone makes a request, suffer a (6 - Scar Resistance) penalty to act in any way that doesn't further it in that scene.",
        5: "As above, but the request replaces an Aspiration and the penalty lasts until it's fulfilled or the end of the story, whichever comes first. Additionally, to switch a Loyalty Touchstone to Conviction requires Wavering first."
    },
    "book": "DevC 16"
}

DEVIANT_FORMS = {
    "amalgam": {
        "name": "Amalgam",
        "description": "Combination of two or more distinct, sapient beings, whether multiple humans fused together or direct combinations with supernatural entities.",
        "mechanics": "Can gain access to communal talents of the gestalt, sacrificing initial Skill dots to gain flexible pool of temporary dots.",
        "book": "DTR 89"
    },
    "self_made": {
        "name": "Self-Made",
        "description": "Unlike most Deviants, the Self-Made are their own Progenitors.",
        "mechanics": "Lacking an external bond to blame as cause of Divergence, the Self-Made possess more agency in establishing Touchstones.",
        "book": "DTR 89"
    },
    "symbiote": {
        "name": "Symbiote",
        "description": "Possess Variations with a mind of their own, drawing power from sources with a distinct and separate mind or agenda.",
        "mechanics": "If the Deviant is not acting in accordance with the symbiotic entity's traits, they may find their Variations are no longer obedient.",
        "book": "DTR 89"
    },
    "transmissible": {
        "name": "Transmissible",
        "description": "Spread their Divergence like a contagion.",
        "mechanics": "Can infect other human beings during play like a disease, with choices for transmittable vectors, virulence, and means to resist.",
        "book": "DTR 89"
    },
    "devoted": {
        "name": "Devoted",
        "description": "A fifth Form detailed separately.",
        "mechanics": "Special Form with unique mechanics.",
        "book": "DTR 238"
    }
}

# Scar Attribute Associations
SCAR_ATTRIBUTES = {
    "mental": {
        "power": "Intelligence",
        "finesse": "Wits",
        "resistance": "Resolve"
    },
    "physical": {
        "power": "Strength",
        "finesse": "Dexterity",
        "resistance": "Stamina"
    },
    "social": {
        "power": "Presence",
        "finesse": "Manipulation",
        "resistance": "Composure"
    }
}

# Export all data
ALL_VARIATIONS = {
    # Universal Variations
    "absorb_instability": VARIATION_ABSORB_INSTABILITY,
    "aquatic": VARIATION_AQUATIC,
    "bioluminescence": VARIATION_BIOLUMINESCENCE,
    "boneless": VARIATION_BONELESS,
    "brachiation": VARIATION_BRACHIATION,
    "camouflage": VARIATION_CAMOUFLAGE,
    "carapace": VARIATION_CARAPACE,
    "electrokinesis": VARIATION_ELECTROKINESIS,
    "enhanced_speed": VARIATION_ENHANCED_SPEED,
    "environmental_adaptation": VARIATION_ENVIRONMENTAL_ADAPTATION,
    "face_thief": VARIATION_FACE_THIEF,
    "flight": VARIATION_FLIGHT,
    "gigantic": VARIATION_GIGANTIC,
    "healer": VARIATION_HEALER,
    "holographic_projection": VARIATION_HOLOGRAPHIC_PROJECTION,
    "hyper_competence": VARIATION_HYPER_COMPETENCE,
    "immunity": VARIATION_IMMUNITY,
    "lash": VARIATION_LASH,
    "miniaturization": VARIATION_MINIATURIZATION,
    "out_of_phase": VARIATION_OUT_OF_PHASE,
    "pyrokinesis": VARIATION_PYROKINESIS,
    "shadow_selves": VARIATION_SHADOW_SELVES,
    "shadows_of_the_past": VARIATION_SHADOWS_OF_THE_PAST,
    "specialized_sense": VARIATION_SPECIALIZED_SENSE,
    "storm_caller": VARIATION_STORM_CALLER,
    "superhuman_attribute": VARIATION_SUPERHUMAN_ATTRIBUTE,
    "telekinesis": VARIATION_TELEKINESIS,
    "translocation": VARIATION_TRANSLOCATION,
    
    # Cephalist Variations
    "astral_travel": VARIATION_ASTRAL_TRAVEL,
    "body_snatcher": VARIATION_BODY_SNATCHER,
    "creeping_dread": VARIATION_CREEPING_DREAD,
    "memory_thief": VARIATION_MEMORY_THIEF,
    "telepathy": VARIATION_TELEPATHY,
    
    # Chimeric Variations
    "animal_transformation": VARIATION_ANIMAL_TRANSFORMATION,
    "mimicry": VARIATION_MIMICRY,
    "monstrous_transformation": VARIATION_MONSTROUS_TRANSFORMATION,
    "pheromones": VARIATION_PHEROMONES,
    "predators_cunning": VARIATION_PREDATORS_CUNNING,
    
    # Coactive Variations
    "blessing": VARIATION_BLESSING,
    "fates_agent": VARIATION_FATES_AGENT,
    "otherworldly_connection": VARIATION_OTHERWORLDLY_CONNECTION,
    "precognition": VARIATION_PRECOGNITION,
    "psycho_onomastics": VARIATION_PSYCHO_ONOMASTICS,
    
    # Invasive Variations
    "computer_aided_processing": VARIATION_COMPUTER_AIDED_PROCESSING,
    "hidden_compartments": VARIATION_HIDDEN_COMPARTMENTS,
    "integrate_technology": VARIATION_INTEGRATE_TECHNOLOGY,
    "omnicompetence": VARIATION_OMNICOMPETENCE,
    "sensor_array": VARIATION_SENSOR_ARRAY,
    
    # Mutant Variations
    "anomalous_biology": VARIATION_ANOMALOUS_BIOLOGY,
    "deadly_ichor": VARIATION_DEADLY_ICHOR,
    "inhuman_digestion": VARIATION_INHUMAN_DIGESTION,
    "rapid_healing": VARIATION_RAPID_HEALING,
    "sacred_flesh": VARIATION_SACRED_FLESH
}

ALL_SCARS = {
    # Controlled Scars
    "concentration": SCAR_CONCENTRATION,
    "cooldown": SCAR_COOLDOWN,
    "depletion": SCAR_DEPLETION,
    "deterioration": SCAR_DETERIORATION,
    "fluctuating_variation": SCAR_FLUCTUATING_VARIATION,
    "perilous_variation": SCAR_PERILOUS_VARIATION,
    "persistent_drawback": SCAR_PERSISTENT_DRAWBACK,
    "power_failure": SCAR_POWER_FAILURE,
    "preparation": SCAR_PREPARATION,
    "tabula_rasa": SCAR_TABULA_RASA,
    "tribulation": SCAR_TRIBULATION,
    "unstable_variation": SCAR_UNSTABLE_VARIATION,
    
    # Involuntary Scars
    "involuntary_stimulus": SCAR_INVOLUNTARY_STIMULUS,
    "power_build_up": SCAR_POWER_BUILD_UP,
    
    # Persistent Scars
    "addictive_variation": SCAR_ADDICTIVE_VARIATION,
    "alternate_persona": SCAR_ALTERNATE_PERSONA,
    "amnesia": SCAR_AMNESIA,
    "bane": SCAR_BANE,
    "bestial_mind": SCAR_BESTIAL_MIND,
    "conspicuous_appearance": SCAR_CONSPICUOUS_APPEARANCE,
    "dependency": SCAR_DEPENDENCY,
    "fragility": SCAR_FRAGILITY,
    "frozen_heart": SCAR_FROZEN_HEART,
    "genetic_disorder": SCAR_GENETIC_DISORDER,
    "glitch": SCAR_GLITCH,
    "hallucinations": SCAR_HALLUCINATIONS,
    "hemophilia": SCAR_HEMOPHILIA,
    "lying_eyes": SCAR_LYING_EYES,
    "maintenance": SCAR_MAINTENANCE,
    "misfortune": SCAR_MISFORTUNE,
    "missing_limb": SCAR_MISSING_LIMB,
    "murderous_urge": SCAR_MURDEROUS_URGE,
    "native_environment": SCAR_NATIVE_ENVIRONMENT,
    "paranoia": SCAR_PARANOIA,
    "philia": SCAR_PHILIA,
    "phobia": SCAR_PHOBIA,
    "sensory_deprivation": SCAR_SENSORY_DEPRIVATION,
    "silence": SCAR_SILENCE,
    "sluggish_metabolism": SCAR_SLUGGISH_METABOLISM,
    "subliminal_conditioning": SCAR_SUBLIMINAL_CONDITIONING,
    "suppression": SCAR_SUPPRESSION,
    "thin_skin": SCAR_THIN_SKIN,
    "trusting": SCAR_TRUSTING
}

# Variation Categories
VARIATION_CATEGORIES = {
    "universal": ["absorb_instability", "aquatic", "bioluminescence", "boneless", "brachiation", 
                  "camouflage", "carapace", "electrokinesis", "enhanced_speed", "environmental_adaptation",
                  "face_thief", "flight", "gigantic", "healer", "holographic_projection", "hyper_competence",
                  "immunity", "lash", "miniaturization", "out_of_phase", "pyrokinesis", "shadow_selves",
                  "shadows_of_the_past", "specialized_sense", "storm_caller", "superhuman_attribute", 
                  "telekinesis", "translocation"],
    "cephalist": ["astral_travel", "body_snatcher", "creeping_dread", "memory_thief", "telepathy"],
    "chimeric": ["animal_transformation", "mimicry", "monstrous_transformation", "pheromones", "predators_cunning"],
    "coactive": ["blessing", "fates_agent", "otherworldly_connection", "precognition", "psycho_onomastics"],
    "invasive": ["computer_aided_processing", "hidden_compartments", "integrate_technology", "omnicompetence", "sensor_array"],
    "mutant": ["anomalous_biology", "deadly_ichor", "inhuman_digestion", "rapid_healing", "sacred_flesh"]
}

# Scar Activation Types
SCAR_ACTIVATION_TYPES = ["Controlled", "Involuntary", "Persistent"]

# Export origin and clade names
DEVIANT_ORIGIN_NAMES = list(DEVIANT_ORIGINS_DETAILED.keys())
DEVIANT_CLADE_NAMES = list(DEVIANT_CLADES_DETAILED.keys())
DEVIANT_ADAPTATION_NAMES = list(DEVIANT_ADAPTATIONS.keys())

