"""
Hunter: The Vigil - Endowments System
Complete listing of all endowment powers from Hunter the Vigil
including descriptions, costs, dice pools, and book references.
"""

# ============================================================================
# ADVANCED ARMORY (Task Force: VALKYRIE)
# ============================================================================

ADVANCED_ARMORY = {
    "the bleeder": {
        "name": "The Bleeder",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "+3 ranged weapon induces the hemorrhage of supernaturally charged blood instead of damage, or with modifications, other forms of supernatural energies.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 152",
        "tags": ["weapon", "ranged", "blood"]
    },
    "compound rounds": {
        "name": "Compound Rounds",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Renewable. Shots take 9-Again and inflict lethal damage against monsters who normally resist firearms.",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 56",
        "tags": ["weapon", "ammunition", "renewable"]
    },
    "equalizer grenade": {
        "name": "Equalizer Grenade",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Flashing grenades that provoke a Clash of Wills against an affected monster's attempt to shapechange, rolling highest Resistance Attribute + Advanced Armory.",
        "cost": None,
        "dice_pool": "Highest Resistance Attribute + Advanced Armory",
        "loadout": "2 Sessions",
        "book": "HTV 2e 104",
        "tags": ["grenade", "shapeshifter", "renewable"]
    },
    "etheric goggles": {
        "name": "Etheric Goggles",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Night-vision goggles that can reveal entities in Twilight, granting a +3 bonus to investigating their Anchors.",
        "cost": None,
        "dice_pool": None,
        "loadout": "3 Sessions",
        "book": "HTV 2e 105",
        "tags": ["perception", "twilight", "spirits"]
    },
    "etheric rounds": {
        "name": "Etheric Rounds",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Soft bullets that deal Lethal damage to Manifest ephemeral entities, but Bashing damage to everything else, including un-Manifest entities in Twilight.",
        "cost": None,
        "dice_pool": None,
        "loadout": "1 Session",
        "book": "HTV 2e 105",
        "tags": ["weapon", "ammunition", "ephemeral", "renewable"]
    },
    "etheric tracker": {
        "name": "Etheric Tracker",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Fires a semitangible tracking pellet which embeds in a corporeal or noncorporeal target. Tracks pellets within half a mile for up to 24 hours.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 155",
        "tags": ["tracking", "utility"]
    },
    "frequency pulse emitter": {
        "name": "Frequency Pulse Emitter",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Renewable. High-frequency sonic grenade provokes a Stamina + Composure -3 roll for beings with heightened animal senses, or -5 for beings in full animal form, to resist being stunned.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 145",
        "tags": ["grenade", "sonic", "werewolf", "renewable"]
    },
    "gatekeeper device": {
        "name": "Gatekeeper Device",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Full bodysuit can be activated with Willpower to transition between the material realm and the Shadow or Underworld, with a twelve-hour cooldown.",
        "cost": "Willpower",
        "dice_pool": None,
        "book": "C&C 82",
        "tags": ["utility", "travel", "shadow", "underworld"]
    },
    "gleipnir restraints": {
        "name": "Gleipnir Restraints",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "A strip of kinetic-feedback plastic which may be used to Restrain in a grapple. A captive must contest Strength + Athletics against twice their own Strength in successes to break free.",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 32",
        "tags": ["restraint", "utility"]
    },
    "gungnir system": {
        "name": "Gungnir System",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "The Gungnir Multi-Function Targeting System, integrated into a submachine gun or assault rifle, provides thermal and night vision, mitigates range penalties, and highlights extranormal entities (which for an extra dot includes Twilight beings).",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 154",
        "tags": ["weapon", "perception", "targeting"]
    },
    "hod rounds": {
        "name": "Hod Rounds",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Renewable. Splintering mistletoe bullets impose a -2 penalty to fire, but deal half their damage to vampires as lethal and suffer no additional penalty to aim a staking shot.",
        "cost": None,
        "dice_pool": None,
        "book": "NS 135",
        "tags": ["weapon", "ammunition", "vampire", "renewable"]
    },
    "huginn visor": {
        "name": "Huginn Visor",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Sunglasses that inflict -3 to a monster's mind-altering powers.",
        "cost": None,
        "dice_pool": None,
        "loadout": "1 Session",
        "book": "HTV 2e 105",
        "tags": ["perception", "mental defense"]
    },
    "ice": {
        "name": "ICE",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "The Interstices Calculation Expedient detects traces of dimensional interstices open in the last 24 hours, for half a mile.",
        "cost": None,
        "dice_pool": None,
        "book": "C&C 82",
        "tags": ["detection", "utility"]
    },
    "logehamarr personal flamethrower": {
        "name": "Logehamarr Personal Flamethrower",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "A ranged heavy weapon anti-personnel flamethrower, resolved as a +0L long burst which inflicts a 4L gasoline burn on organic material. The Logehamarr's green flame immediately provokes vampires to flee.",
        "cost": None,
        "dice_pool": None,
        "book": "NS 136",
        "tags": ["weapon", "fire", "vampire"]
    },
    "mjolnir cannon": {
        "name": "Mjolnir Cannon",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Battery-powered lightning gun, with two settings for different levels of damage.",
        "cost": None,
        "dice_pool": None,
        "loadout": "1 Session",
        "book": "HTV 2e 105",
        "tags": ["weapon", "electricity"]
    },
    "munin serum": {
        "name": "Munin Serum",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "A syringe filled with a memory-altering substance, wiping a drugged person's memories of certain events.",
        "cost": None,
        "dice_pool": None,
        "loadout": "1 Session",
        "book": "HTV 2e 106",
        "tags": ["utility", "memory", "renewable"]
    },
    "odin reticle": {
        "name": "Odin Reticle",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Small display attached to other goggles or visors that provokes a Clash of Wills against supernaturally hidden creatures, rolling highest Resistance Attribute + Advanced Armory.",
        "cost": None,
        "dice_pool": "Highest Resistance Attribute + Advanced Armory",
        "loadout": "3 Sessions",
        "book": "HTV 2e 106",
        "tags": ["perception", "detection"]
    },
    "screamer pistol": {
        "name": "Screamer Pistol",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Low-frequency +3 sonic pistol disorients instead of dealing damage, preventing the target from focusing supernatural power for (target's Composure - successes + 1) turns.",
        "cost": None,
        "dice_pool": None,
        "book": "WF 125",
        "tags": ["weapon", "sonic", "disruption"]
    },
    "tranq rounds": {
        "name": "Tranq Rounds",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Renewable. Shots deal one point of lethal damage and a stacking -1 penalty. A target at a high penalty must spend Willpower to remain conscious.",
        "cost": None,
        "dice_pool": None,
        "book": "Slash 160",
        "tags": ["weapon", "ammunition", "incapacitation", "renewable"]
    },
    "urban response vehicle": {
        "name": "Urban Response Vehicle",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Armored vehicle disguised as a van, armed with a mounted +5L heavy machinegun, and powered by an electric generator. Cell members may pool Merit dots for the URV and enhance it by purchasing integrated Etheric Rounds, Etheric Goggle windows, a mounted Bleeder, an Equalizer Grenade Launcher, the Gungnir System, or a mounted Mjolnir Cannon.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 145",
        "tags": ["vehicle", "utility"]
    },
    "vdsb": {
        "name": "V.D.S.B.",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Phosphorescent flash bomb that stuns surprised targets and blinds all unprotected targets.",
        "cost": None,
        "dice_pool": None,
        "loadout": "1 Session",
        "book": "HTV 2e 106",
        "tags": ["trap", "light", "stun"]
    },
    "witch buster": {
        "name": "Witch Buster",
        "endowment_type": "advanced_armory",
        "conspiracy": "Task Force: VALKYRIE",
        "description": "Device uses a lithium battery to radiate energies that register to paranormal senses.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 151",
        "tags": ["detection", "mage"]
    },
}

# ============================================================================
# ANIMAL CONTROL KIT
# ============================================================================

ANIMAL_CONTROL_KIT = {
    "basic field kit": {
        "name": "Basic Field Kit",
        "endowment_type": "animal_control_kit",
        "conspiracy": "Various",
        "description": "Kit containing a signal jammer, a stun gun, and military-grade Kevlar armor.",
        "cost": None,
        "dice_pool": None,
        "loadout": "1 Session",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 44",
        "tags": ["utility", "armor", "equipment"]
    },
    "mobile transport unit": {
        "name": "Mobile Transport Unit",
        "endowment_type": "animal_control_kit",
        "conspiracy": "Various",
        "description": "Van with reinforced cages/chassis, anesthetic gas vents, and a soundproof barrier between the back and driver's seat.",
        "cost": None,
        "dice_pool": "Dexterity + Drive or Intelligence + Science",
        "loadout": "1 Session",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 44",
        "tags": ["vehicle", "utility", "capture"]
    },
    "pheromone blocker emitter": {
        "name": "Pheromone Blocker/Emitter",
        "endowment_type": "animal_control_kit",
        "conspiracy": "Various",
        "description": "Emits pheromones/inhibitors; provokes Clash of Wills against emotion powers or grants a +3 bonus to Social actions.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "loadout": "3 Sessions",
        "action": "Instant, Contested",
        "duration": "1 Scene",
        "book": "TF 44",
        "tags": ["social", "defense", "enhancement"]
    },
    "envenomed weapons": {
        "name": "Envenomed Weapons",
        "endowment_type": "animal_control_kit",
        "conspiracy": "Various",
        "description": "Weapons coated with venom that inflict the Drugged and Poisoned Tilts on a successful attack.",
        "cost": None,
        "dice_pool": "Dexterity + Firearms or Weaponry",
        "loadout": "3 Sessions",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 44",
        "tags": ["weapon", "poison"]
    },
    "temporary symbiont": {
        "name": "Temporary Symbiont",
        "endowment_type": "animal_control_kit",
        "conspiracy": "Various",
        "description": "Grants +2 to an Attribute and a Dread Power. Causes the Shaken/Spooked Conditions and a breaking point roll when detached.",
        "cost": "2 Lethal, 1 Willpower",
        "dice_pool": "Varies",
        "loadout": "1 Chapter",
        "action": "Instant",
        "duration": "1 Chapter",
        "book": "TF 45",
        "tags": ["enhancement", "dread power", "symbiont"]
    },
}

# ============================================================================
# BENEDICTION (Malleus Maleficarum)
# ============================================================================

BENEDICTION = {
    "the apostles teachings": {
        "name": "The Apostles' Teachings",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Instead of recovering Willpower from your Virtue, distribute your Resolve + Composure in Willpower among mortal allies.",
        "cost": None,
        "dice_pool": "Composure + Benediction",
        "book": "HTV 157",
        "tags": ["support", "willpower"]
    },
    "armor of st martin": {
        "name": "Armor of St. Martin",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "The ritualist gains (Benediction/Benediction) Armor.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Benediction",
        "target_successes": 7,
        "book": "HTV 2e 107",
        "tags": ["defense", "armor"]
    },
    "the binding of st amabilis": {
        "name": "The Binding of St. Amabilis",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "While you sing praises, werewolves who listen cannot benefit from supernatural healing.",
        "cost": "1 Willpower",
        "dice_pool": "Presence + Benediction",
        "book": "SpSl 147",
        "tags": ["werewolf", "suppression"]
    },
    "blessed protection of st agrippina": {
        "name": "Blessed Protection of St. Agrippina",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Bless a physically demarcated area as an extended action to ward against supernatural beings. Such beings within the area subtract your Benediction from their effective Power Attributes, and without Presence cannot enter.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Benediction",
        "book": "HTV 159",
        "tags": ["warding", "area effect"]
    },
    "the boon of lazarus": {
        "name": "The Boon of Lazarus",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "For one Willpower dot, return a corpse to life with full health and no Willpower. Revived characters are Soulless if the ritual began more than 5 minutes after death.",
        "cost": "1 Willpower dot",
        "dice_pool": None,
        "target_successes": 8,
        "book": "HTV 2e 107",
        "tags": ["resurrection", "healing"]
    },
    "the casting out of witches": {
        "name": "The Casting Out of Witches",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Pray as an extended action to compel monsters to suffer mounting penalties or flee the vicinity for an hour.",
        "cost": "1 Willpower",
        "dice_pool": "Presence + Benediction",
        "book": "C&C 76",
        "tags": ["mage", "expulsion"]
    },
    "epipodian safeguard": {
        "name": "Epipodian Safeguard",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Gain Benediction as a bonus against mental domination and similar powers.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "target_successes": 7,
        "book": "HTV 2e 107",
        "tags": ["mental defense"]
    },
    "fiacres staff": {
        "name": "Fiacre's Staff",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Bless an improvised weapon as a vampiric stake, removing its penalty and applying successes as a weapon bonus against the undead. Women perform a variant rite called the Benediction of the Rose.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Benediction",
        "book": "NS 138",
        "tags": ["vampire", "weapon", "blessing"]
    },
    "fortitude of st george": {
        "name": "Fortitude of St. George",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "The Hunter gains an extra dot of Stamina, and may roll Stamina + Benediction to resist Conditions or Tilts from deprivation and exertion.",
        "cost": None,
        "dice_pool": "Composure + Benediction",
        "target_successes": 6,
        "book": "HTV 2e 108",
        "tags": ["enhancement", "stamina"]
    },
    "the hands of st luke": {
        "name": "The Hands of St. Luke",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Restore up to Benediction in Lethal or Bashing damage on a target, or reduce Aggravated damage to Lethal by the same amount. Also resolve the target's Crippled Condition.",
        "cost": "1 Willpower",
        "dice_pool": "Intelligence + Benediction",
        "target_successes": 8,
        "book": "HTV 2e 108",
        "tags": ["healing"]
    },
    "la langue des saints": {
        "name": "La Langue des Saints",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Force a monster to honestly answer one question per threshold success.",
        "cost": "1 Willpower",
        "dice_pool": "Composure + Benediction vs Resolve + Subterfuge",
        "book": "NS 138",
        "tags": ["information", "interrogation"]
    },
    "loyolas fire": {
        "name": "Loyola's Fire",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Cast a holy light which compels the undead to panic and flee, losing Willpower while illuminated.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Benediction",
        "book": "NS 140",
        "tags": ["vampire", "light", "fear"]
    },
    "mantle of orleans": {
        "name": "Mantle of Orleans",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "While you continue to pray this scene, cellmates gain a +1 bonus to combat rolls and Defense, and a +3 bonus to Initiative and Speed.",
        "cost": "2 Willpower",
        "dice_pool": "Manipulation + Benediction",
        "book": "NS 141",
        "tags": ["support", "combat", "enhancement"]
    },
    "the miracle of gadarene": {
        "name": "The Miracle of Gadarene",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Cast an exorcised spirit into an animal as a symbolic rebuke, bound helpless while the animal lives.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 147",
        "tags": ["spirit", "binding"]
    },
    "peace of st joseph": {
        "name": "Peace of St. Joseph",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Apply Benediction as a penalty to an undead being's Initiative, Speed, and Physical actions for a scene.",
        "cost": None,
        "dice_pool": "Presence + Benediction vs Stamina + Potency",
        "book": "HMR 31",
        "tags": ["vampire", "debuff"]
    },
    "the preservation of the chastity of st agnes of rome": {
        "name": "The Preservation of the Chastity of St. Agnes of Rome",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "While you possess only one undamaged Health point, manifest Benediction as Armor for the scene. Suffer aggravated damage to expel the armor, dealing it as aggravated damage all around you.",
        "cost": "1 Willpower (2 Agg to expel)",
        "dice_pool": "Resolve + Benediction",
        "book": "C&C 75",
        "tags": ["armor", "desperate", "area attack"]
    },
    "revelationes coelestes": {
        "name": "Revelationes Coelestes",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Witches spontaneously bleed, suffering a -2 penalty for the scene.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Benediction",
        "book": "WF 125",
        "tags": ["mage", "debuff"]
    },
    "sanctification of the blessed virgin": {
        "name": "Sanctification of the Blessed Virgin",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Pray as an extended action to render something a blessed item for a scene, or lose a Willpower dot to bless it permanently.",
        "cost": "1 Willpower (or 1 Willpower dot)",
        "dice_pool": "Morality + Benediction",
        "book": "HTV 161",
        "tags": ["blessing", "utility"]
    },
    "scutum sancte trinitatis": {
        "name": "Scutum Sancte Trinitatis",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Take no non-aggravated damage for a turn per success, except from fire, disease, drugs, or poison.",
        "cost": "3 Willpower",
        "dice_pool": "Resolve + Benediction",
        "book": "BD 7",
        "tags": ["defense", "protection"]
    },
    "the shepherds blessing": {
        "name": "The Shepherd's Blessing",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "For one scene, become completely overlooked, gaining Benediction to Clash of Wills against supernatural powers.",
        "cost": "1 Willpower",
        "dice_pool": "Wits + Benediction",
        "target_successes": 6,
        "book": "HTV 2e 108",
        "tags": ["stealth", "concealment"]
    },
    "song of daniel": {
        "name": "Song of Daniel",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Calm wildlife, or for two Willpower other creatures, with a hymn, adding successes as a Social bonus and suppressing supernatural frenzies.",
        "cost": "1 Willpower (or 2 Willpower)",
        "dice_pool": "Charisma + Benediction - Resolve",
        "book": "NS 139",
        "tags": ["calming", "social"]
    },
    "st agathius call": {
        "name": "St. Agathius' Call",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Assailants with Morality <=6 must spend Willpower to strike anyone but you for the scene.",
        "cost": "1 Willpower",
        "dice_pool": "Presence + Benediction",
        "book": "Slash 161",
        "tags": ["protection", "redirect"]
    },
    "st collens clarity": {
        "name": "St. Collen's Clarity",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "See through illusions and other powers over your senses for a scene.",
        "cost": None,
        "dice_pool": "Wits + Benediction",
        "book": "HMR 56",
        "tags": ["perception", "anti-illusion"]
    },
    "true sight of st abel": {
        "name": "True Sight of St. Abel",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Recipients of this blessing may roll Resolve with an allocated bonus to perceive Twilight and to see monsters for what they are without Lunacy or Disbelief for a scene.",
        "cost": "1 Willpower",
        "dice_pool": "Intelligence + Benediction",
        "book": "HTV 162",
        "tags": ["perception", "true sight"]
    },
    "vade retro satana": {
        "name": "Vade Retro Satana",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Acting as either a Warding, Binding, Abjuring or Exorcism, additionally inflict Benediction in Lethal damage to an affected ephemeral entity.",
        "cost": None,
        "dice_pool": "Resolve + Composure + Benediction",
        "target_successes": 7,
        "book": "HTV 2e 108",
        "tags": ["exorcism", "demon", "spirit"]
    },
    "wrathful sword of st michael the archangel": {
        "name": "Wrathful Sword of St. Michael the Archangel",
        "endowment_type": "benediction",
        "conspiracy": "Malleus Maleficarum",
        "description": "Imbue a melee weapon with Benediction as damage rating against monsters.",
        "cost": "2 Willpower",
        "dice_pool": "Strength + Benediction",
        "target_successes": 7,
        "book": "HTV 2e 108",
        "tags": ["weapon", "blessing", "aggravated"]
    },
}

# Due to file length, I'll continue in the next part...
# ============================================================================
# CASTIGATION (Lucifuge)
# ============================================================================

CASTIGATION = {
    "abaddons call": {
        "name": "Abaddon's Call",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Raise a corpse as an undead servant for (Castigation) hours. Spend a Willpower dot to raise indefinitely.",
        "cost": "1 Willpower, 2 Bashing per roll",
        "dice_pool": "Resolve + Medicine",
        "book": "NS 142",
        "tags": ["necromancy", "minion"]
    },
    "abyssal bondage": {
        "name": "Abyssal Bondage",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Mark a witch with blood from a vein to redirect their next spell, or from an artery to send it completely out of control.",
        "cost": "1 Willpower, 1 Lethal or 1 Aggravated",
        "dice_pool": "Stamina + Resolve",
        "book": "WF 126",
        "tags": ["mage", "curse", "disruption"]
    },
    "calling forth the pit": {
        "name": "Calling Forth the Pit",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Banish a demon, or summon an unbound demon to your location.",
        "cost": "1 Lethal",
        "dice_pool": "Manipulation + Occult - Resistance",
        "action": "Extended (10, 30 minutes per roll)",
        "book": "HTV 2e 110",
        "tags": ["demon", "summoning"]
    },
    "coils of iniquity": {
        "name": "Coils of Iniquity",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Anoint yourself with sinner's blood. Apply successes as a Social bonus with those sharing the sinner's Vice for a day.",
        "cost": "1 Willpower dot",
        "dice_pool": "(10 - Morality) + Empathy",
        "book": "C&C 69",
        "tags": ["social", "enhancement"]
    },
    "familiar": {
        "name": "Familiar",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "A demonic servant in animal or Twilight form.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 165",
        "tags": ["minion", "demon"]
    },
    "familiar betrayal": {
        "name": "Familiar Betrayal",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Summon a werewolf's spirit familiar by name and bind its service for six days.",
        "cost": "2 Lethal, 1 Willpower per day",
        "dice_pool": "Presence + Resolve vs Resistance",
        "book": "SpSl 148",
        "tags": ["werewolf", "spirit", "binding"]
    },
    "family vestment": {
        "name": "Family Vestment",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Physically manifest a chosen demonic trait, such as wings or claws, for a scene or longer. Suffer derangement for a day thereafter.",
        "cost": "1 Willpower (1 Lethal+)",
        "dice_pool": "Strength + Stamina",
        "book": "C&C 69",
        "tags": ["transformation", "enhancement"]
    },
    "gaze of the penitent": {
        "name": "Gaze of the Penitent",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Inflict Guilty, and gain +2 on Social rolls against the target.",
        "cost": "1 Willpower",
        "dice_pool": "Wits + Empathy vs Resolve",
        "action": "Instant",
        "book": "HTV 2e 110",
        "tags": ["debuff", "gaze", "social"]
    },
    "guilts bloody trail": {
        "name": "Guilt's Bloody Trail",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Track a corpse's murderer by occult stigmata for a scene.",
        "cost": "1 Willpower",
        "dice_pool": "Intelligence + Investigation vs Wits + Subterfuge",
        "book": "Slash 161",
        "tags": ["tracking", "investigation"]
    },
    "gulf of hades": {
        "name": "Gulf of Hades",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Call up outer darkness to strip heat and energy. Electricity is rendered inert, the living suffer freezing lethal damage, and the reanimated lose Willpower.",
        "cost": None,
        "dice_pool": "Presence + Occult",
        "book": "HMR 30",
        "tags": ["area effect", "cold", "undead"]
    },
    "hellfire": {
        "name": "Hellfire",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Wield summoned fire as a +2L thrown weapon. The following turn, the surrounding area gains the Inferno Tilt.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "action": "Instant",
        "book": "HTV 2e 111",
        "tags": ["attack", "fire"]
    },
    "infernal visions": {
        "name": "Infernal Visions",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Gain harrowing insight into a topic once per session.",
        "cost": None,
        "dice_pool": "Wits + Composure",
        "book": "HTV 168",
        "tags": ["information", "vision"]
    },
    "mandate of hell": {
        "name": "Mandate of Hell",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Issue a command of only a few words, or a complex command of up to 2 steps with Willpower. Gain +2 to this Rite's pool if you know the demon's name.",
        "cost": "1 Willpower (optional)",
        "dice_pool": "Presence + Intimidation vs Resistance",
        "action": "Instant",
        "prerequisite": "Calling Forth the Pit",
        "book": "HTV 2e 111",
        "tags": ["demon", "command"]
    },
    "mark of lucifuge": {
        "name": "Mark of Lucifuge",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Transfer a permanent brand onto a vampire or other monster. Lucifuge, Malleus, Cainites, and the inhuman recognize the monster's nature by the brand.",
        "cost": "1-2 Willpower, 1 Lethal",
        "dice_pool": None,
        "book": "NS 143",
        "tags": ["marking", "vampire"]
    },
    "mark of the beast": {
        "name": "Mark of the Beast",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Take the shape of a demon temporarily, gaining +1 Size, +2 Armor, and (Castigation) bonus Physical Attribute dots. While in demon form, you may heal by spending Willpower and incapacitate mortals in terror.",
        "cost": "2 Willpower, 1 Lethal",
        "dice_pool": "Resolve + Intimidation",
        "book": "SpSl 148",
        "tags": ["transformation", "enhancement", "fear"]
    },
    "prima dictum": {
        "name": "Prima Dictum",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Mark a vampire (or learn variants for other monsters) with your blood and curse its Physical actions by your successes for a scene.",
        "cost": "2 Willpower, 2 Lethal",
        "dice_pool": "Resolve + Occult + Castigation vs Resolve + Potency",
        "book": "NS 142",
        "tags": ["vampire", "curse", "debuff"]
    },
    "rebuke lies": {
        "name": "Rebuke Lies",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "See through the falsehoods and trappings of a demon's Cover, or strip them away for a scene.",
        "cost": "1 Willpower (optional)",
        "dice_pool": "Wits + Investigation vs Presence + Composure or vs Resistance",
        "book": "HMR 133",
        "tags": ["demon", "detection", "dispel"]
    },
    "sense of the unrighteous": {
        "name": "Sense of the Unrighteous",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Detect sins hanging on people and places, as well as monsters without Morality.",
        "cost": None,
        "dice_pool": "10 - Morality",
        "book": "HTV 170",
        "tags": ["detection", "morality"]
    },
    "shackles of pandemonium": {
        "name": "Shackles of Pandemonium",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Anoint a ritual circle to bind a demon, naming a means by which it may escape.",
        "cost": "1 Lethal",
        "dice_pool": "Presence + Intimidation vs Resistance",
        "book": "HTV 170",
        "tags": ["demon", "binding", "ritual"]
    },
    "tongue of babel": {
        "name": "Tongue of Babel",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Understand all spoken human languages, and be understood by anyone when speaking. Move up one impression level in Social Maneuvering.",
        "cost": None,
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 111",
        "tags": ["communication", "utility", "social"]
    },
    "unholy aura": {
        "name": "Unholy Aura",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Intimidating aura grants Social rolls for the scene a +3 bonus (doubled against the fae) and 9-Again.",
        "cost": None,
        "dice_pool": "Presence + Intimidation vs Composure",
        "book": "HMR 55",
        "tags": ["social", "intimidation", "changeling"]
    },
    "unholy escapologist": {
        "name": "Unholy Escapologist",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Be released from any physical bonds.",
        "cost": "1 Willpower",
        "dice_pool": "Dexterity + Composure",
        "book": "CoH16 5",
        "tags": ["escape", "utility"]
    },
    "forged in fire": {
        "name": "Forged in Fire",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Become immune to fire, though not its other effects like smoke. After being exposed to fire or extreme heat, take -2 to most Social pools.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "duration": "1 Scene",
        "book": "HTV 2e 110",
        "tags": ["fire", "immunity", "defense"]
    },
    "sense weakness": {
        "name": "Sense Weakness",
        "endowment_type": "castigation",
        "conspiracy": "Lucifuge",
        "description": "Learn a Bane, the name of a demon, or another weakness of a target.",
        "cost": "1 Willpower",
        "dice_pool": "Wits + Empathy vs Finesse",
        "action": "Instant",
        "book": "HTV 2e 111",
        "tags": ["information", "weakness"]
    },
}

# ============================================================================
# DREAMSCAPE (The Merrick Institute)
# ============================================================================

DREAMSCAPE = {
    "dream shaping": {
        "name": "Dream Shaping",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "The character can Enhance, Deaden, Reshape, Create or Destroy matter in the dream world according to the dots she has in this Endowment.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "T&N 20",
        "tags": ["dreams", "manipulation"]
    },
    "dream shield": {
        "name": "Dream Shield",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "Each dot adds 1/1 armor in the dreamscape. Anytime she spends Willpower to add -2 to a resistance or +3 to a contested dice pool against Dread Powers.",
        "cost": "None (1 Willpower optional)",
        "dice_pool": None,
        "book": "T&N 20",
        "tags": ["dreams", "defense"]
    },
    "dream sword": {
        "name": "Dream Sword",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "The character can create a Size 1-3 physical weapon or can project an attack at anything within eyeshot with a Finesse + Power roll.",
        "cost": "1 Willpower",
        "dice_pool": "Finesse + Power",
        "book": "T&N 20",
        "tags": ["dreams", "weapon"]
    },
    "absorb and fortify": {
        "name": "Absorb and Fortify",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "When using Dream Shaping to remove Durability or Structure from an object, add her successes as temporary Health boxes. At three dots, you may also use Absorb and Fortify when using a Dream Sword attack.",
        "cost": None,
        "dice_pool": None,
        "prerequisite": "Dream Shaping 3, Dream Shield 1, Dream Sword 1 (for 3-dot version)",
        "book": "T&N 21",
        "tags": ["dreams", "healing"]
    },
    "colossus": {
        "name": "Colossus",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "The character can create massive structures in seconds.",
        "cost": None,
        "dice_pool": None,
        "prerequisite": "Dream Shaping 3",
        "book": "T&N 21",
        "tags": ["dreams", "construction"]
    },
    "dreampushing": {
        "name": "Dreampushing",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "Your character can create an \"invincible hand\" and enact minor influence on the dream world.",
        "cost": None,
        "dice_pool": None,
        "prerequisite": "Dream Shaping 1",
        "book": "T&N 21",
        "tags": ["dreams", "telekinesis"]
    },
    "regenerative mind": {
        "name": "Regenerative Mind",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "The character regains one WP every ten minutes or by taking 1B damage reflexively, she can immediately replenish one WP.",
        "cost": None,
        "dice_pool": None,
        "prerequisite": "Any Dreamscape Merit at 1",
        "book": "T&N 21",
        "tags": ["dreams", "willpower"]
    },
    "shielding mind": {
        "name": "Shielding Mind",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "The character can use Dream Shield on another person.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "prerequisite": "Dream Shield 2",
        "book": "T&N 21",
        "tags": ["dreams", "defense", "support"]
    },
    "warp": {
        "name": "Warp",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "Dream Shaping effects occur instantly, and may be used reflexively when used against inanimate objects.",
        "cost": None,
        "dice_pool": None,
        "prerequisite": "Dream Shaping 3",
        "book": "T&N 21",
        "tags": ["dreams", "speed"]
    },
    "wrack": {
        "name": "Wrack",
        "endowment_type": "dreamscape",
        "conspiracy": "The Merrick Institute",
        "description": "By choosing to remove damage from the weapon of the Dream Sword, could drain an Attribute from the victim a scene.",
        "cost": None,
        "dice_pool": None,
        "prerequisite": "Dream Sword 3",
        "book": "T&N 21",
        "tags": ["dreams", "debuff"]
    },
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_all_endowments():
    """Get all endowment powers."""
    return {
        **ADVANCED_ARMORY,
        **ANIMAL_CONTROL_KIT,
        **BENEDICTION,
        **CASTIGATION,
        **DREAMSCAPE,
        **ELIXIR,
        **ENKOIMESIS,
        **GOETIC_GOSPEL,
        **HORROR_WITHIN,
        **INFUSION,
        **INK,
        **INSPIRATION,
        **LIVES_REMEMBERED,
        **PERISPIRITISM,
        **RELIC,
        **RITES_DU_CHEVAL,
        **RITES_OF_DENIAL,
        **SEITOKUTEN,
        **TELEINFORMATICS,
        **THAUMATECHNOLOGY,
        **XENOTECHNOLOGY,
    }

def get_endowment(power_name):
    """
    Look up an endowment power by name (case-insensitive).
    Returns the power data or None if not found.
    """
    power_key = power_name.lower().strip()
    all_endowments = get_all_endowments()
    return all_endowments.get(power_key)

def get_endowments_by_type(endowment_type):
    """
    Get all powers of a specific endowment type.
    Valid types: 'advanced_armory', 'animal_control_kit', 'benediction', 'castigation', 
    'dreamscape', 'elixir', 'enkoimesis', 'goetic_gospel', 'horror_within', 'infusion', 
    'ink', 'inspiration', 'lives_remembered', 'perispiritism', 'relic', 'rites_du_cheval', 
    'rites_of_denial', 'seitokuten', 'teleinformatics', 'thaumatechnology', 'xenotechnology'
    """
    type_map = {
        "advanced_armory": ADVANCED_ARMORY,
        "animal_control_kit": ANIMAL_CONTROL_KIT,
        "benediction": BENEDICTION,
        "castigation": CASTIGATION,
        "dreamscape": DREAMSCAPE,
        "elixir": ELIXIR,
        "enkoimesis": ENKOIMESIS,
        "goetic_gospel": GOETIC_GOSPEL,
        "horror_within": HORROR_WITHIN,
        "infusion": INFUSION,
        "ink": INK,
        "inspiration": INSPIRATION,
        "lives_remembered": LIVES_REMEMBERED,
        "perispiritism": PERISPIRITISM,
        "relic": RELIC,
        "rites_du_cheval": RITES_DU_CHEVAL,
        "rites_of_denial": RITES_OF_DENIAL,
        "seitokuten": SEITOKUTEN,
        "teleinformatics": TELEINFORMATICS,
        "thaumatechnology": THAUMATECHNOLOGY,
        "xenotechnology": XENOTECHNOLOGY,
    }
    return type_map.get(endowment_type.lower(), {})

def get_endowments_by_conspiracy(conspiracy_name):
    """
    Get all powers for a specific conspiracy.
    """
    all_endowments = get_all_endowments()
    matching_powers = {}
    
    for key, power_data in all_endowments.items():
        if conspiracy_name.lower() in power_data.get("conspiracy", "").lower():
            matching_powers[key] = power_data
    
    return matching_powers

def get_endowments_by_tag(tag):
    """
    Get all powers with a specific tag.
    """
    all_endowments = get_all_endowments()
    matching_powers = {}
    
    for key, power_data in all_endowments.items():
        if tag.lower() in [t.lower() for t in power_data.get("tags", [])]:
            matching_powers[key] = power_data
    
    return matching_powers

def get_endowment_summary(power_name):
    """
    Get a formatted summary of an endowment power.
    """
    power_data = get_endowment(power_name)
    if not power_data:
        return f"Endowment power '{power_name}' not found."
    
    summary = []
    summary.append(f"=== {power_data['name']} ===")
    summary.append(f"Type: {power_data['endowment_type'].replace('_', ' ').title()}")
    summary.append(f"Conspiracy: {power_data['conspiracy']}")
    
    summary.append(f"\nDescription: {power_data['description']}")
    
    if power_data.get('cost'):
        summary.append(f"\nCost: {power_data['cost']}")
    
    if power_data.get('dice_pool'):
        summary.append(f"Dice Pool: {power_data['dice_pool']}")
    
    if power_data.get('prerequisite'):
        summary.append(f"Prerequisite: {power_data['prerequisite']}")
    
    summary.append(f"\nSource: {power_data['book']}")
    
    if power_data.get('tags'):
        summary.append(f"Tags: {', '.join(power_data['tags'])}")
    
    return "\n".join(summary)

# Book abbreviations (defined early for reference)
BOOK_ABBREVIATIONS = {
    "HTV": "Hunter: The Vigil",
    "HTV 2e": "Hunter: The Vigil 2nd Edition",
    "HMR": "Mortal Remains",
    "NS": "Night Stalkers",
    "SpSl": "Spirit Slayers",
    "WF": "Witch Finders",
    "C&C": "Compacts and Conspiracies",
    "Slash": "Slasher",
    "T&N": "Tooth and Nail",
    "BD": "Block by Bloody Dusk",
    "CoH15": "Chronicles of Horror 2015",
    "CoH16": "Chronicles of Horror 2016",
    "DE": "Dark Eras",
}

# ============================================================================
# ELIXIR (Ascending Ones)
# ============================================================================

ELIXIR = {
    "a glimpse of after": {
        "name": "A Glimpse of After",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Ignores wound penalties and only needs to roll for consciousness when rightmost Health is Lethal.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "HTV 174",
        "tags": ["resilience", "health"]
    },
    "agora salve": {
        "name": "Agora Salve",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Add Elixir to Social rolls.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "C&C 55",
        "tags": ["social", "enhancement"]
    },
    "amuns water": {
        "name": "Amun's Water",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Suffer -2 to all actions for the duration, but become invisible until you take a hostile action. Provokes a Clash of Wills against powers that can view the invisible.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Elixir",
        "duration": "1 Scene",
        "book": "HTV 2e 113",
        "tags": ["stealth", "invisibility"]
    },
    "balm of chronos": {
        "name": "Balm of Chronos",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Doubles Initiative modifier and Defense score. If used in a non-combat situation, gains a +3 to extended rolls.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "SpSl 149",
        "tags": ["speed", "enhancement"]
    },
    "bennu-bird feather": {
        "name": "Bennu-Bird Feather",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Heal 2B or 1L for each activation success, starting with the rightmost damage.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Elixir",
        "book": "HTV 2e 114",
        "tags": ["healing"]
    },
    "blood of the cobra": {
        "name": "Blood of the Cobra",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "+1 Strength and Dexterity per success rolled and blood becomes poisonous.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "HTV 178",
        "tags": ["enhancement", "poison"]
    },
    "breath of the dragon": {
        "name": "Breath of the Dragon",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Roll Stamina + Medicine vs. Stamina to inflict the Sick Tilt, and gain +2B on the next attack against the target.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Medicine vs Stamina",
        "book": "HTV 2e 113",
        "tags": ["attack", "poison"]
    },
    "breath of maat": {
        "name": "Breath of Ma'at",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Ignore all breaking point rolls, only rolling for a single breaking point at the end of the scene. If breaking the Code, gain Demoralized even when succeeding this roll.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "duration": "1 Scene",
        "book": "HTV 2e 113",
        "tags": ["morality", "protection"]
    },
    "crocodile tears": {
        "name": "Crocodile Tears",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Appear nearly dead.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "HTV 172",
        "tags": ["deception"]
    },
    "drop of dreams": {
        "name": "Drop of Dreams",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Falls unconscious and enter in the primordial dream for one hour.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "T&N 21",
        "tags": ["dreams", "travel"]
    },
    "elixir of the fiery heart": {
        "name": "Elixir of the Fiery Heart",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Resist fear effects equal to Elixir.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "HTV 174",
        "tags": ["fear resistance"]
    },
    "eye of ra": {
        "name": "Eye of Ra",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "When rolling to investigate or notice details, exceptionally succeed on 3 successes.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Elixir",
        "duration": "1 Scene",
        "book": "HTV 2e 114",
        "tags": ["perception", "investigation"]
    },
    "gentle mind": {
        "name": "Gentle Mind",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Do not increase Disquiet from Prometheans on ties, and can spend Willpower to reduce Stage 4 to Stage 3 in others.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "HMR 29",
        "tags": ["promethean", "resistance"]
    },
    "hound mark": {
        "name": "Hound Mark",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Perceive monsters within 5' (fae only with 1 dot, all monsters with 3 dots).",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "HMR 53",
        "tags": ["detection", "changeling"]
    },
    "hunting sight of the asp": {
        "name": "Hunting Sight of the Asp",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "See things in the thermal spectrum.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "NS 144",
        "tags": ["perception", "thermal"]
    },
    "incense of the next world": {
        "name": "Incense of the Next World",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Become invisible and ephemeral, able to see ghosts and spirits and using Willpower as Corpus. Upon death, return to your body with the Soulless Condition.",
        "cost": "2 Willpower",
        "dice_pool": "Stamina + Elixir",
        "duration": "1 Scene",
        "book": "HTV 2e 114",
        "tags": ["astral", "twilight", "spirit"]
    },
    "justice of maat": {
        "name": "Justice of Ma'at",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Bonus to Investigation equal to Elixir and +1 to Degeneration rolls.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "Slash 163",
        "tags": ["investigation", "morality"]
    },
    "liar pills": {
        "name": "Liar Pills",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Betray no emotion (and lie convincingly) for a scene.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "HMR 130",
        "tags": ["deception", "social"]
    },
    "mesmeric vapors": {
        "name": "Mesmeric Vapors",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Roll Stamina + Presence vs. Resolve as an extended action to make a target answer any questions, and gain 8-again to command them.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Presence vs Resolve",
        "duration": "1 Scene",
        "book": "HTV 2e 114",
        "tags": ["mind control", "interrogation"]
    },
    "mind-talking drug": {
        "name": "Mind-Talking Drug",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Mentally converse or scan the surface thoughts of another.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "HTV 175",
        "tags": ["telepathy", "information"]
    },
    "nehebkau tears": {
        "name": "Nehebkau Tears",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Temporarily become a Vampire.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "NS 145",
        "tags": ["transformation", "vampire"]
    },
    "red resin": {
        "name": "Red Resin",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "See monsters with morality 7 or lower.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "C&C 55",
        "tags": ["detection", "morality"]
    },
    "the tallymans eyes": {
        "name": "The Tallyman's Eyes",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Identify any magic user in sight.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "WF 127",
        "tags": ["detection", "mage"]
    },
    "thoths whisper": {
        "name": "Thoth's Whisper",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "Inhale a ghost for a variety of bonuses, including entering the Underworld.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "C&C 55",
        "tags": ["ghost", "underworld"]
    },
    "vapors of mercury": {
        "name": "Vapors of Mercury",
        "endowment_type": "elixir",
        "conspiracy": "Ascending Ones",
        "description": "The blood of the hunter transmutes into a silver substance that burns like acid if touched by a werewolf.",
        "cost": None,
        "dice_pool": "Stamina + Elixir",
        "book": "SpSl 149",
        "tags": ["werewolf", "defense"]
    },
}

# ============================================================================
# INK (Knights of Saint Adrian)
# ============================================================================

INK = {
    "bear mace": {
        "name": "Bear Mace",
        "endowment_type": "ink",
        "conspiracy": "Knights of Saint Adrian",
        "description": "Unarmed damage, plus inflicts Stunned Tilt on supernatural creatures. Can only be used (Ink) times per scene.",
        "cost": None,
        "dice_pool": "Part of Brawl attack",
        "book": "HMR 139",
        "tags": ["combat", "stun"]
    },
    "brother road": {
        "name": "Brother Road",
        "endowment_type": "ink",
        "conspiracy": "Knights of Saint Adrian",
        "description": "Ask specific questions about recent history in the area. Can only be used (Ink) times per scene.",
        "cost": None,
        "dice_pool": "Wits + Investigation",
        "book": "HMR 140",
        "tags": ["information", "history"]
    },
    "fist of revelation": {
        "name": "Fist of Revelation",
        "endowment_type": "ink",
        "conspiracy": "Knights of Saint Adrian",
        "description": "Unarmed damage, plus inflicts Knocked Down Tilt on demons, removes their Cover for a scene and reveals their Apocalyptic Form. Once per Demon per Scene, can't be used at same time as Bear Mace.",
        "cost": None,
        "dice_pool": "Part of Brawl attack",
        "book": "HMR 140",
        "tags": ["combat", "demon", "reveal"]
    },
    "king of the road": {
        "name": "King of the Road",
        "endowment_type": "ink",
        "conspiracy": "Knights of Saint Adrian",
        "description": "Bond a particular motor vehicle so that it will always reappear within a day if destroyed or lost.",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 140",
        "tags": ["utility", "vehicle"]
    },
    "the lord provides": {
        "name": "The Lord Provides",
        "endowment_type": "ink",
        "conspiracy": "Knights of Saint Adrian",
        "description": "When using a firearm of a particular bonded model, have infinite ammunition.",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 140",
        "tags": ["utility", "ammunition"]
    },
    "love hate": {
        "name": "LOVE/HATE",
        "endowment_type": "ink",
        "conspiracy": "Knights of Saint Adrian",
        "description": "Right (LOVE): Gain Informed Condition regarding a person while shaking their hand and general feeling if they are trustworthy. Left (HATE): Brawl attacks are Lethal rather than Bashing.",
        "cost": None,
        "dice_pool": "Wits + Composure (LOVE)",
        "book": "HMR 140",
        "tags": ["information", "combat"]
    },
    "pain magnet": {
        "name": "Pain Magnet",
        "endowment_type": "ink",
        "conspiracy": "Knights of Saint Adrian",
        "description": "Suffer damage for others nearby (but not if your last health box is filled).",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 141",
        "tags": ["protection", "sacrifice"]
    },
    "tough as the last guy": {
        "name": "Tough as the Last Guy",
        "endowment_type": "ink",
        "conspiracy": "Knights of Saint Adrian",
        "description": "Store a supernatural opponent's rating in Strength, Dexterity, Brawl, Firearms or Weaponry to use in a future scene.",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 141",
        "tags": ["enhancement", "adaptation"]
    },
}

# ============================================================================
# RITES DU CHEVAL (Les Mystères)
# ============================================================================

RITES_DU_CHEVAL = {
    "clinging leech": {
        "name": "Clinging Leech",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Sap health from a target for oneself. Grapple and Wits + Larceny Vs Resolve + Stamina, 1(L) for every success.",
        "cost": "1 Willpower",
        "dice_pool": "Wits + Larceny vs Resolve + Stamina",
        "book": "SpSl 157",
        "tags": ["attack", "drain", "grapple"]
    },
    "deny the moon": {
        "name": "Deny the Moon",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Negate the use of Dominions by werewolves.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 159",
        "tags": ["werewolf", "suppression"]
    },
    "elemental rebuke": {
        "name": "Elemental Rebuke",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Attack target with an elemental (fire, water, etc) effect. 1L for every success.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Occult + Les Mystères Status vs Resolve + Stamina",
        "book": "SpSl 155",
        "tags": ["attack", "elemental"]
    },
    "ephemeral disguise": {
        "name": "Ephemeral Disguise",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Spirit hides the caster with an unremarkable visage. (Mod. to Stealth rolls) Dramatic Failure: Glow in red -5, Success: +3, Exceptional Success: +3 no evidence in security systems or video.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 155",
        "tags": ["stealth", "disguise"]
    },
    "the hands of raphael": {
        "name": "The Hands of Raphael",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Heal sickness, and mend wounds in others.",
        "cost": "1 Willpower + Damage",
        "dice_pool": None,
        "book": "SpSl 156",
        "tags": ["healing"]
    },
    "light as a feather": {
        "name": "Light as a Feather",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Increase jumping ability, and protection from falling damage. +5 for Jumping rolls, Only 1(B) for falling.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 156",
        "tags": ["mobility", "protection"]
    },
    "skin of the loa": {
        "name": "Skin of the Loa",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Spirit grants temporary Armor. Dramatic Failure: Def. -2, Success: Melee armor +2, Exceptional Success: Armor +2.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 155",
        "tags": ["armor", "defense"]
    },
    "spiritual guidance": {
        "name": "Spiritual Guidance",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Gain expertise in a field and Rote Action.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "SpSl 157",
        "tags": ["enhancement", "skill"]
    },
    "voodo doll": {
        "name": "Voodo Doll",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Use a small doll to affect a target in positive or negative ways.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "SpSl 158",
        "tags": ["curse", "blessing", "sympathetic"]
    },
    "wearing the barons hat": {
        "name": "Wearing the Baron's Hat",
        "endowment_type": "rites_du_cheval",
        "conspiracy": "Les Mysteres",
        "description": "Gain amazing combat abilities and temporary health. +3 to Defense, +5 To Initiative and +5 health.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "SpSl 160",
        "tags": ["enhancement", "combat"]
    },
}

# ============================================================================
# SEITOKUTEN (Otodo)
# ============================================================================

SEITOKUTEN = {
    "hannya": {
        "name": "Hannya",
        "endowment_type": "seitokuten",
        "conspiracy": "Otodo",
        "description": "The hunter can intuits immaterial spirits and demons as if they were materialized. Whenever a character she can perceive suffers a breaking point she sees a flash across his aura.",
        "cost": None,
        "dice_pool": None,
        "book": "DE 319",
        "tags": ["perception", "spirit", "demon"]
    },
    "jabaku": {
        "name": "Jabaku",
        "endowment_type": "seitokuten",
        "conspiracy": "Otodo",
        "description": "Control demons or spirits the hunter can see or knows by name, it also works on human characters suffering the Thrall Condition.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Composure",
        "book": "DE 319",
        "tags": ["control", "spirit", "demon"]
    },
    "kaibutsu": {
        "name": "Kaibutsu",
        "endowment_type": "seitokuten",
        "conspiracy": "Otodo",
        "description": "The hunter grows into a monstrosity with 2/1 armor, +2 Size and you may spend Willpower to heal 1L or 2B of damage, also cause fear in humans.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "DE 319",
        "tags": ["transformation", "enhancement", "fear"]
    },
    "kenshi": {
        "name": "Kenshi",
        "endowment_type": "seitokuten",
        "conspiracy": "Otodo",
        "description": "This gift allows the hunter to craft a ban for a demon, spirit or human characters with the Soulless or Thrall Conditions.",
        "cost": None,
        "dice_pool": "Resolve + Composure",
        "book": "DE 320",
        "tags": ["ban", "spirit", "demon"]
    },
    "kigo": {
        "name": "Kigo",
        "endowment_type": "seitokuten",
        "conspiracy": "Otodo",
        "description": "The hunter marks a victim with a burning emblem. Even once the damage is healed, any Otodo or character able to see auras will see the mark.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Composure",
        "book": "DE 321",
        "tags": ["marking", "tracking"]
    },
    "shinigami buki": {
        "name": "Shinigami Buki",
        "endowment_type": "seitokuten",
        "conspiracy": "Otodo",
        "description": "The hunter can devour souls, to exorcise possessing spirits, or to destroy demons. It can be used against humans causing the Soulless or the Thrall Conditions.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "DE 321",
        "tags": ["exorcism", "spirit", "demon"]
    },
    "shonetsu jigoku": {
        "name": "Shonetsu Jigoku",
        "endowment_type": "seitokuten",
        "conspiracy": "Otodo",
        "description": "This gift allows the hunter to safely let her body burn with flames, coat a weapon with her fiery blood, or splash the flames across her enemies.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Composure",
        "book": "DE 321",
        "tags": ["fire", "attack", "enhancement"]
    },
}

# ============================================================================
# ENKOIMESIS
# ============================================================================

ENKOIMESIS = {
    "allergy diagnosis": {
        "name": "Allergy Diagnosis",
        "endowment_type": "enkoimesis",
        "conspiracy": "Various",
        "description": "Identifies allergies in subjects, including the monsters' banes.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "book": "TF 45",
        "tags": ["information", "banes"]
    },
    "calming touch": {
        "name": "Calming Touch",
        "endowment_type": "enkoimesis",
        "conspiracy": "Various",
        "description": "Eases fear and rage, grants 8-again quality on Animal Ken/Empathy rolls to calm targets, may end monster fury with Clash of Wills.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 45",
        "tags": ["calming", "support"]
    },
    "healing hands": {
        "name": "Healing Hands",
        "endowment_type": "enkoimesis",
        "conspiracy": "Various",
        "description": "Heals Enkoimesis dots in bashing/lethal damage to the living or inflicts aggravated damage on undead. Affected once per scene.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Medicine",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 46",
        "tags": ["healing", "vampire"]
    },
    "plague doctor": {
        "name": "Plague Doctor",
        "endowment_type": "enkoimesis",
        "conspiracy": "Various",
        "description": "Imposes/moderates Poisoned or Sick Tilts, with graver effects on exceptional success.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Medicine vs Stamina",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 46",
        "tags": ["poison", "disease", "debuff"]
    },
    "shared life": {
        "name": "Shared Life",
        "endowment_type": "enkoimesis",
        "conspiracy": "Various",
        "description": "Transfers damage to heal others or resurrect the recently dead, with additional risks.",
        "cost": "1 Willpower, 1 Willpower dot",
        "dice_pool": None,
        "action": "Instant",
        "book": "TF 46",
        "tags": ["healing", "resurrection", "sacrifice"]
    },
}

# ============================================================================
# HORROR WITHIN
# ============================================================================

HORROR_WITHIN = {
    "slashers shadow": {
        "name": "Slasher's Shadow",
        "endowment_type": "horror_within",
        "conspiracy": "Various",
        "description": "Choose an Attribute fitting a slasher's themes when gaining this Endowment. Increase that Attribute by two dots for the scene.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 46",
        "tags": ["enhancement", "slasher"]
    },
    "inexorable": {
        "name": "Inexorable",
        "endowment_type": "horror_within",
        "conspiracy": "Various",
        "description": "Delay marking damage from a single source for three turns, ignoring wound penalties. Lethal damage will not roll over into aggravated afterwards.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Reflexive",
        "duration": "3 Turns",
        "book": "TF 47",
        "tags": ["resilience", "defense"]
    },
    "ground-eating stride": {
        "name": "Ground-Eating Stride",
        "endowment_type": "horror_within",
        "conspiracy": "Various",
        "description": "Double Speed, always have Edge in chases, and ignore Speed penalties from Environmental Tilts.",
        "cost": "1 Willpower, 1 Lethal",
        "dice_pool": None,
        "action": "Reflexive",
        "duration": "1 Scene",
        "book": "TF 47",
        "tags": ["speed", "chase"]
    },
    "harry": {
        "name": "Harry",
        "endowment_type": "horror_within",
        "conspiracy": "Various",
        "description": "Chase a target, imposing a -2 penalty to their Wits rolls; declare a pre-set trap at chase start.",
        "cost": "1 Willpower",
        "dice_pool": "Manipulation + Intimidation + Size",
        "action": "Instant, Resisted",
        "duration": "1 Scene",
        "book": "TF 47",
        "tags": ["chase", "intimidation"]
    },
    "the fiend unleashed": {
        "name": "The Fiend Unleashed",
        "endowment_type": "horror_within",
        "conspiracy": "Various",
        "description": "Choose an Undertaking when gaining this endowment. Gain access to the Talent of a chosen Undertaking and suffer its Frailties. Gain Guilty, Shaken, or Spooked Condition afterward.",
        "cost": "2 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 47",
        "tags": ["slasher", "transformation"]
    },
}

# ============================================================================
# INFUSION
# ============================================================================

INFUSION = {
    "inferno flask": {
        "name": "Inferno Flask",
        "endowment_type": "infusion",
        "conspiracy": "Various",
        "description": "Become the center of an Inferno Tilt and gain immunity to the extremes of heat and cold.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "duration": "1 Scene",
        "book": "TF 48",
        "tags": ["fire", "immunity"]
    },
    "lesser infusion": {
        "name": "Lesser Infusion",
        "endowment_type": "infusion",
        "conspiracy": "Various",
        "description": "Adapt body to otherworld conditions, gaining 8-again on Survival rolls. White Hare Society members enjoy an extended duration and don't take damage.",
        "cost": "1 Lethal (optional)",
        "dice_pool": None,
        "duration": "1 Week",
        "book": "TF 48",
        "tags": ["adaptation", "survival"]
    },
    "liquid courage": {
        "name": "Liquid Courage",
        "endowment_type": "infusion",
        "conspiracy": "Various",
        "description": "Regain a point of Willpower, receive the Steadfast Condition, become immune to fear, and Stun monsters in response to Dread Powers.",
        "cost": None,
        "dice_pool": None,
        "duration": "1 Scene",
        "book": "TF 48",
        "tags": ["willpower", "fear resistance"]
    },
    "primal heart elixir": {
        "name": "Primal Heart Elixir",
        "endowment_type": "infusion",
        "conspiracy": "Various",
        "description": "Warp the body, gain natural weaponry, and become immune to Environmental Tilts; 8-again on Social rolls with otherworld denizens.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "duration": "1 Day",
        "book": "TF 48",
        "tags": ["transformation", "weapon", "social"]
    },
    "wandering scarecrow": {
        "name": "Wandering Scarecrow",
        "endowment_type": "infusion",
        "conspiracy": "Various",
        "description": "Animate a doll to serve as a 3-dot Retainer with one Dread Power, use Eye Spy to see through its eyes.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "duration": "1 Week",
        "book": "TF 48",
        "tags": ["minion", "scrying"]
    },
}

# ============================================================================
# INSPIRATION
# ============================================================================

INSPIRATION = {
    "depths of depravity": {
        "name": "Depths of Depravity",
        "endowment_type": "inspiration",
        "conspiracy": "Various",
        "description": "Disturb minds with intrusive thoughts from viewing the painting, granting Willpower but inflicting the Addicted Condition. Monsters suffer the Obsessive condition instead. Spend willpower to cause the Insensate Tilt to viewers, which turns into the Traumatized Tilt after resolving.",
        "cost": "1 Willpower (optional)",
        "dice_pool": None,
        "target_successes": 8,
        "duration": "1 Week",
        "book": "TF 49",
        "tags": ["mental attack", "condition"]
    },
    "hunger of the wolf": {
        "name": "Hunger of the Wolf",
        "endowment_type": "inspiration",
        "conspiracy": "Various",
        "description": "Make monsters' Dread Powers more taxing and incite humans to crave flesh, letting them regain willpower by doing so.",
        "cost": "1 Willpower",
        "dice_pool": "Contested",
        "target_successes": 8,
        "duration": "1 Scene",
        "book": "TF 49",
        "tags": ["debuff", "cannibalism"]
    },
    "the lonely ones": {
        "name": "The Lonely Ones",
        "endowment_type": "inspiration",
        "conspiracy": "Various",
        "description": "Become so uninteresting as to be effectively invisible, attracting attention only from observers the Masterwork finds attractive. Both they and the wearer gain the Swooned Condition for one another.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "target_successes": 7,
        "action": "Instant",
        "duration": "1 Day",
        "book": "TF 50",
        "tags": ["stealth", "social"]
    },
    "pallid bust of pallas": {
        "name": "Pallid Bust of Pallas",
        "endowment_type": "inspiration",
        "conspiracy": "Various",
        "description": "Grant the Informed Condition with a subject of your choice, but lose memories based on roll result, gaining the Amnesia condition.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "target_successes": 8,
        "action": "Instant",
        "duration": "1 Week",
        "book": "TF 50",
        "tags": ["information", "memory"]
    },
    "the red wax mask": {
        "name": "The Red Wax Mask",
        "endowment_type": "inspiration",
        "conspiracy": "Various",
        "description": "Animate nearby statues as 3-dot Retainers specialized in physical actions. However, they seek blood sacrifices in the last hour before dawn.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "target_successes": 12,
        "action": "Instant",
        "duration": "1 Night",
        "book": "TF 50",
        "tags": ["minion", "animation"]
    },
}

# ============================================================================
# LIVES REMEMBERED
# ============================================================================

LIVES_REMEMBERED = {
    "old enemies": {
        "name": "Old Enemies",
        "endowment_type": "lives_remembered",
        "conspiracy": "Various",
        "description": "Ask up to three questions about a target monster, gain a +2 bonus on Intelligence + Occult rolls for similar monsters.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 51",
        "tags": ["information", "knowledge"]
    },
    "remembered skill": {
        "name": "Remembered Skill",
        "endowment_type": "lives_remembered",
        "conspiracy": "Various",
        "description": "Treat yourself as having three dots in a chosen Skill for a single Specialty.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 51",
        "tags": ["skill enhancement", "temporary"]
    },
    "time capsule": {
        "name": "Time Capsule",
        "endowment_type": "lives_remembered",
        "conspiracy": "Various",
        "description": "Receive needed equipment with Availability up to the hunter's Lives Remembered dots.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "book": "TF 51",
        "tags": ["equipment", "utility"]
    },
    "visions out of time": {
        "name": "Visions Out of Time",
        "endowment_type": "lives_remembered",
        "conspiracy": "Various",
        "description": "See past/future moments like the Psychometry Merit, but imposing no additional Condition. However, these events must come from before or after the hunter's lifetime.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "book": "TF 51",
        "tags": ["vision", "psychometry"]
    },
    "whispers from babel": {
        "name": "Whispers from Babel",
        "endowment_type": "lives_remembered",
        "conspiracy": "Various",
        "description": "Choose a Mental Merit up to Lives Remembered dots to gain its benefits for the scene.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 51",
        "tags": ["merit", "temporary", "mental"]
    },
}

# ============================================================================
# PERISPIRITISM
# ============================================================================

PERISPIRITISM = {
    "auric shield": {
        "name": "Auric Shield",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "Provides 2 Armor against Manifest ghosts' attacks and provokes a Clash of Wills against numina and dread powers, but take a two-die penalty to all actions in the next scene.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 115",
        "tags": ["ghost", "armor", "defense"]
    },
    "borrowed power": {
        "name": "Borrowed Power",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "Draw power from a nearby ghost to gain access to a numen.",
        "cost": "2 Willpower",
        "dice_pool": "Stamina + Occult",
        "action": "Instant",
        "book": "HTV 2e 116",
        "tags": ["ghost", "numen", "power theft"]
    },
    "command ghost": {
        "name": "Command Ghost",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "Must have Ghost Speech. Give a ghost a simple command that it will follow as best it can.",
        "cost": "1 Willpower",
        "dice_pool": "Presence + Intimidation vs Resistance",
        "action": "Instant",
        "prerequisite": "Ghost Speech",
        "book": "HTV 2e 117",
        "tags": ["ghost", "command"]
    },
    "dark reflection": {
        "name": "Dark Reflection",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "Use a reflective surface to project your visions for others to see and interpret.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 117",
        "tags": ["scrying", "communication"]
    },
    "ephemeral weapon": {
        "name": "Ephemeral Weapon",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "Roll Resolve + Occult to resist Shaken, and create a 1L weapon, or 3L against ephemeral entities.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Occult",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 117",
        "tags": ["weapon", "ghost"]
    },
    "expulsion": {
        "name": "Expulsion",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "Reduce the Open Condition to Anchor, and mark an area as a Bane for all ghosts.",
        "cost": "1 Willpower",
        "dice_pool": "Presence + Occult",
        "action": "Instant",
        "duration": "1 day",
        "book": "HTV 2e 117",
        "tags": ["ghost", "warding"]
    },
    "ghost speech": {
        "name": "Ghost Speech",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "See into ghostly Twilight and focus on a ghost to communicate with it.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 118",
        "tags": ["ghost", "communication", "twilight"]
    },
    "know death": {
        "name": "Know Death",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "Provoke a Clash of Wills to reveal a dead creature or ghost's true form.",
        "cost": "1 Willpower",
        "dice_pool": "Wits + Investigation vs Composure",
        "action": "Instant",
        "book": "HTV 2e 118",
        "tags": ["ghost", "detection"]
    },
    "third eye": {
        "name": "Third Eye",
        "endowment_type": "perispiritism",
        "conspiracy": "Various",
        "description": "Gain additional Clue Elements when Investigating, and avoid Incomplete Clues. Roll Composure + Occult afterwards to avoid Shaken.",
        "cost": "1 Willpower",
        "dice_pool": "Composure + Occult",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 119",
        "tags": ["investigation", "clues"]
    },
}

# ============================================================================
# XENOTECHNOLOGY (Gizmo)
# ============================================================================

XENOTECHNOLOGY = {
    "cloaking device": {
        "name": "Cloaking Device",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Switch between Stealth and Infiltration modes, granting invisibility or 8-again on disguises.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 8,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 53",
        "tags": ["stealth", "invisibility", "disguise"]
    },
    "cyberglass": {
        "name": "Cyberglass",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Perceive the reality frequency of alien facilities or their servants.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 5,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 53",
        "tags": ["perception", "alien"]
    },
    "psi-crown": {
        "name": "Psi-Crown",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Tinfoil hat circlet of unearthly materials which protects against mind probes/control, provoking a Clash of Wills with 8-again on the roll.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 6,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 54",
        "tags": ["mental defense", "telepathy"]
    },
    "ray gun": {
        "name": "Ray Gun",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Range 30/60/120, Clip 3, Initiative -3 ranged weapon with damage equal to Xenotechnology rating that ignores material armor.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 10,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 54",
        "tags": ["weapon", "energy"]
    },
    "scramblers": {
        "name": "Scramblers",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Long-ranged communications equipment which can also disrupt communications and surveillance within one mile, affecting supernatural equipment with a Clash of Wills.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 5,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 54",
        "tags": ["communication", "disruption"]
    },
}

# ============================================================================
# RELIC (Aegis Kai Doru)
# ============================================================================

RELIC = {
    "aegis talisman": {
        "name": "Aegis Talisman",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Provide 3/3 armor and bonuses to contend or resist supernatural effects. Spend additional willpower to paralyze a target.",
        "cost": "1 Willpower (2 Willpower optional)",
        "dice_pool": "Presence + Occult vs Resolve",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HtV 2e 276",
        "tags": ["armor", "fear", "paralysis"]
    },
    "barnabas-in-amber": {
        "name": "Barnabas-in-Amber",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "A severed head relic that detects other Relics.",
        "cost": None,
        "dice_pool": None,
        "book": "C&C 50",
        "tags": ["detection", "relic"]
    },
    "the beauty jar": {
        "name": "The Beauty Jar",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "The hunter gains the following benefits: Fame Merit at three dots, Striking Looks Merit at four dots and removal of the Unskilled penalty when it comes to Social rolls. The hunter can end the benefits by kissing someone.",
        "cost": "2 Willpower",
        "dice_pool": None,
        "book": "C&C 50",
        "tags": ["social", "enhancement"]
    },
    "blood of pope joan": {
        "name": "Blood of Pope Joan",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Level 1 Blessed item and gives Werewolves -2 against anyone carrying the Relic.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 180",
        "tags": ["werewolf", "blessed"]
    },
    "box of the treaty elm": {
        "name": "Box of the Treaty Elm",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Any oath spoken over the box is completely binding, if a group betrays the oath everyone immediately lose all Willpower and suffer a -2 penalty to all dice rolls against the opposing group.",
        "cost": "2 Willpower, 1 Willpower dot",
        "dice_pool": "Resolve + Empathy",
        "book": "SpSl 210",
        "tags": ["oath", "binding"]
    },
    "centurions gladdius": {
        "name": "Centurion's Gladdius",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Normally a 1B melee weapon. If Willpower is spent, the weapon removes any magical properties of a struck object. Alternatively, if 1L is spent, the weapon becomes a 2L weapon.",
        "cost": "1 Willpower or 1 Lethal",
        "dice_pool": None,
        "book": "WF 127",
        "tags": ["weapon", "dispel"]
    },
    "dead mans face": {
        "name": "Dead Man's Face",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Reanimate the head of a dead person.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "HTV 184",
        "tags": ["necromancy", "information"]
    },
    "doru talisman": {
        "name": "Doru Talisman",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Launch a 3A ranged attack with a range of 10/20/40 yards/meters.",
        "cost": "2 Willpower",
        "dice_pool": "Dexterity + Weaponry - Defense",
        "action": "Instant, Resisted",
        "duration": "1 Scene",
        "book": "TF 52",
        "tags": ["weapon", "area attack", "aggravated"]
    },
    "dream relic": {
        "name": "Dream Relic",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Modification to an existing Relic that now it only exists within the scope of dreams.",
        "cost": "1 Willpower or 1 Lethal",
        "dice_pool": None,
        "book": "T&N 21",
        "tags": ["dreams", "modification"]
    },
    "eye of hubris": {
        "name": "Eye of Hubris",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Cause Dread Power failures to become dramatic failures, or impose Tilts on targets using dread powers that don't require rolls.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 52",
        "tags": ["mage", "suppression", "dread power"]
    },
    "heart of stone": {
        "name": "Heart of Stone",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "When hooked up to an electrical charge, it becomes an object of obsession.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 181",
        "tags": ["obsession", "control"]
    },
    "heart of the succubus": {
        "name": "Heart of the Succubus",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Determine the direction of the nearest Demon.",
        "cost": None,
        "dice_pool": "Wits + Academics",
        "book": "HMR 129",
        "tags": ["demon", "detection"]
    },
    "hex sign": {
        "name": "Hex Sign",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Affix symbols to a location that provide a variety of effects.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Occult",
        "book": "WF 191",
        "tags": ["warding", "protection"]
    },
    "icarine servitor": {
        "name": "Icarine Servitor",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Living wax servant.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 180",
        "tags": ["minion", "servant"]
    },
    "idol of gevandan": {
        "name": "Idol of Gevandan",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "When active, it makes all werewolves be determined to take possession of the idol, even from each other.",
        "cost": "1 Willpower dot",
        "dice_pool": None,
        "book": "SpSl 150",
        "tags": ["werewolf", "compulsion"]
    },
    "kirkestedes lenses": {
        "name": "Kirkestede's Lenses",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Gain bonuses to research.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 307",
        "tags": ["research", "information"]
    },
    "the oath stone": {
        "name": "The Oath Stone",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Swear upon the stone in order to gain benefits to hunting Relics and combatting both werewolves and mages.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "book": "C&C 51",
        "tags": ["oath", "enhancement"]
    },
    "ohtas": {
        "name": "Ohtas",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Any Vigil related action is at +1 If benefiting Lenape tribe, then add additional +2.",
        "cost": "1 Willpower",
        "dice_pool": "Resolve + Occult",
        "book": "WF 187",
        "tags": ["enhancement", "vigil"]
    },
    "one-eyed kings": {
        "name": "One-Eyed Kings",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Spy through one coin with the other's eye, provoking a Clash of Wills in warded locations.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 53",
        "tags": ["scrying", "perception"]
    },
    "orpheus eye": {
        "name": "Orpheus' Eye",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "User can see into Twilight.",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 28",
        "tags": ["twilight", "perception"]
    },
    "phylactery of commius": {
        "name": "Phylactery of Commius",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Bind a spirit to the Phylactery in order to gain a number of benefits.",
        "cost": "1 Willpower dot",
        "dice_pool": None,
        "book": "SpSl 150",
        "tags": ["spirit", "binding"]
    },
    "prometheus blood": {
        "name": "Prometheus' Blood",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "When placed in the abdomen of a living person making the person it's placed inside immune to disease, poison, and infection. Once per turn, user can spend 1 Willpower to downgrade all lethal damage to bashing damage.",
        "cost": "1 Willpower (optional)",
        "dice_pool": None,
        "book": "CoH15 1",
        "tags": ["healing", "protection"]
    },
    "ringsel": {
        "name": "Ringsel",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Heal at a rate of 1 Willpower for 1 Bashing and 2 Willpower for 1 Lethal or negate a degeneration for 1 Willpower instead.",
        "cost": "1-2 Willpower",
        "dice_pool": None,
        "book": "HTV 181",
        "tags": ["healing", "morality"]
    },
    "saint georges sword": {
        "name": "Saint George's Sword",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "A 1L sword. When a target is struck with it, he bleeds and causes 1L per turn. This bleeding can only be stopped by killing the sword user.",
        "cost": None,
        "dice_pool": "Resolve + Composure",
        "book": "T&N 22",
        "tags": ["weapon", "bleeding"]
    },
    "scale of scylla": {
        "name": "Scale of Scylla",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Become invisible to Vampires.",
        "cost": "1 Willpower, 1 Lethal",
        "dice_pool": None,
        "book": "NS 146",
        "tags": ["vampire", "invisibility"]
    },
    "the silver key": {
        "name": "The Silver Key",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Open a gate into the Hedge, but only once per location.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "HMR 52",
        "tags": ["changeling", "travel"]
    },
    "skeleton key": {
        "name": "Skeleton Key",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Unlock any door and prompt a Clash of Wills with 8-again against monster-sealed doors.",
        "cost": None,
        "dice_pool": None,
        "action": "Instant",
        "book": "HtV 2e 276",
        "tags": ["utility", "locks"]
    },
    "stone mans staff": {
        "name": "Stone Man's Staff",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "+2 bonus to attack. Travel to any visible point.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "Spearfinger 7",
        "tags": ["weapon", "teleportation"]
    },
    "mask of terror": {
        "name": "Mask of Terror",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Inspire supernatural fear in one person.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "book": "Slash 163",
        "tags": ["fear", "social"]
    },
    "perseus mirrored shield": {
        "name": "Perseus' Mirrored Shield",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "The hunter becomes immune to Dread Powers that use a Resisted or Contested roll against her but all relevant actions suffer a -2 penalty.",
        "cost": "1 Willpower",
        "dice_pool": "Wits + Composure",
        "book": "T&N 22",
        "tags": ["defense", "reflection"]
    },
    "ulunsuti the blazing diamond": {
        "name": "Ulun'suti the Blazing Diamond",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Once per story, reroll one task. Three times per story, add +1 to any task. Conjure flame.",
        "cost": "1 Willpower",
        "dice_pool": "Dexterity + Occult",
        "book": "Spearfinger 7",
        "tags": ["reroll", "fire", "enhancement"]
    },
    "watchful keris": {
        "name": "Watchful Keris",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "2L knife with +1 Initiative and can make a reflexive roll to avoid being surprised in combat.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 181",
        "tags": ["weapon", "initiative"]
    },
    "witch-candle": {
        "name": "Witch-Candle",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Summon gargoyles.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "book": "HTV 183",
        "tags": ["summoning", "minion"]
    },
    "worm pipe": {
        "name": "Worm Pipe",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Resurrect a corpse.",
        "cost": "1 Lethal, 1 Willpower dot",
        "dice_pool": None,
        "book": "NS 146",
        "tags": ["resurrection", "necromancy"]
    },
    "zenobias golden chain": {
        "name": "Zenobia's Golden Chain",
        "endowment_type": "relic",
        "conspiracy": "Aegis Kai Doru",
        "description": "Interrogate monsters, revealing their most guarded secret and inflicting the Leveraged condition if they do not answer three questions honestly.",
        "cost": "1 Willpower",
        "dice_pool": "Presence + Intimidation vs Composure + Subterfuge",
        "action": "Instant, Contested",
        "duration": "1 Scene",
        "book": "TF 53",
        "tags": ["interrogation", "information", "social"]
    },
}

# ============================================================================
# THAUMATECHNOLOGY (Cheiron Group)
# ============================================================================

THAUMATECHNOLOGY = {
    "agonizer": {
        "name": "Agonizer",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Parasitic bug that feeds off of magic.",
        "cost": None,
        "dice_pool": None,
        "book": "WF 128",
        "tags": ["mage", "parasite"]
    },
    "anger patch": {
        "name": "Anger Patch",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Detect vampires at a cost of -1 to Social rolls against them.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 185",
        "tags": ["vampire", "detection"]
    },
    "banality worm": {
        "name": "Banality Worm",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Add Resolve to resist supernatural effects. -1 on Degeneration rolls.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 189",
        "tags": ["resistance", "morality"]
    },
    "berserker splice": {
        "name": "Berserker Splice",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Under stress, gain 2 points to Strength, plus 1 point per every point of Lethal damage taken, and gains Iron Stamina temporarily.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 152",
        "tags": ["enhancement", "berserker"]
    },
    "biliary tree of the cynocephali": {
        "name": "Biliary Tree of the Cynocephali",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Any Toxin entering body starts out at -5 Toxicity. +2 to Resist Disease.",
        "cost": None,
        "dice_pool": None,
        "book": "BbBB 25",
        "tags": ["poison resistance", "disease resistance"]
    },
    "cortical adaptation": {
        "name": "Cortical Adaptation",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "After spending a point of Willpower, the Hunter gets +3 to Investigation and Empathy in regards to Slasher murders and purchase Slasher merits.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "book": "Slash 164",
        "tags": ["investigation", "slasher"]
    },
    "cranial cortex augmentation": {
        "name": "Cranial Cortex Augmentation",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Gain Dream Powers: Dream Seeing (3), Dream Shaping (3) and Dream Walking (3) for 8-Stamina weeks; each re-application of this power has 10% greater chance of failing.",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 54",
        "tags": ["dreams", "augmentation"]
    },
    "devils eye": {
        "name": "Devil's Eye",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "See into Twilight, and Clash of Wills against any invisible characters.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 122",
        "tags": ["perception", "twilight", "invisibility"]
    },
    "ectocrine gland": {
        "name": "Ectocrine Gland",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "See and communicate with non-manifested Twilight entities (ghosts and spirits). While active, -2 to 'real-world' Perception tests, and hunter is easier to possess by entities.",
        "cost": None,
        "dice_pool": None,
        "book": "SpSl 151",
        "tags": ["twilight", "spirit", "ghost"]
    },
    "evil eye": {
        "name": "Evil Eye",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Replace an eye and suffer the One Eye flaw. Additionally receive -2 to all Social rolls when the eye is exposed. Gain any one of these Dread Powers: Confuse, Fury, Sleep, Hypnotize or Terrify.",
        "cost": None,
        "dice_pool": None,
        "book": "NS 148",
        "tags": ["dread power", "eye"]
    },
    "hand of glory": {
        "name": "Hand of Glory",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Suffer -2 to manual dexterity and inflict Immobilized, and prevent a target from remembering while under the effects.",
        "cost": "1 Willpower",
        "dice_pool": "Presence + Occult vs Resolve + Tolerance",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 123",
        "tags": ["mesmerize", "immobilize"]
    },
    "lovers lips": {
        "name": "Lover's Lips",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Receive 9-Again on Social rolls against characters who ingest the liquid from the implant.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 187",
        "tags": ["social", "enhancement"]
    },
    "optic thorn": {
        "name": "Optic Thorn",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Allows user to see 'supernaturally augmented' hunters.",
        "cost": None,
        "dice_pool": None,
        "book": "C&C 62",
        "tags": ["perception", "hunter detection"]
    },
    "personal defense swarm": {
        "name": "Personal Defense Swarm",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Summon a swarm around you that attacks with +1L, but suffer 1L whenever using or recalling the swarm.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 123",
        "tags": ["defense", "swarm"]
    },
    "plasmic caul": {
        "name": "Plasmic Caul",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "See ghosts in Twilight, gain +1 to any roll involved with them, and spend one Willpower for a 'secondary' effect.",
        "cost": "1 Willpower (optional)",
        "dice_pool": None,
        "book": "C&C 64",
        "tags": ["ghost", "twilight"]
    },
    "quick-step": {
        "name": "Quick-Step",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "+3 Speed, 9-Again on Athletic checks involving running or moving quickly, and retains Defense against Firearms while running.",
        "cost": None,
        "dice_pool": None,
        "book": "HTV 188",
        "tags": ["speed", "movement"]
    },
    "twitcher": {
        "name": "Twitcher",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Gain +3 to Initiative, and spend Willpower to use the higher of Dexterity or Wits for Defense, including during surprise.",
        "cost": "1 Willpower (optional)",
        "dice_pool": None,
        "action": "Reflexive",
        "duration": "Indefinite",
        "book": "HTV 2e 125",
        "tags": ["defense", "initiative"]
    },
    "regenerative nodule": {
        "name": "Regenerative Nodule",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Once per story, increase healing rate dramatically and ignore wound penalties, but increase food needs.",
        "cost": None,
        "dice_pool": None,
        "action": "Instant",
        "book": "HTV 2e 123",
        "tags": ["healing", "regeneration"]
    },
    "vitriol pump": {
        "name": "Vitriol Pump",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Add three successes to a roll, up to three times before requiring a week's recharge.",
        "cost": None,
        "dice_pool": None,
        "book": "HMR 29",
        "tags": ["enhancement", "bonus"]
    },
    "voice of the banshee": {
        "name": "Voice of the Banshee",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "At the cost of 1WP, make a bashing attack with Stamina+Expression against all creatures with enhanced hearing that also disrupts their concentration. The upgraded version also afflicts those affected with the Depression or Melancholia derangement.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Expression",
        "book": "NS 148",
        "tags": ["attack", "sonic", "derangement"]
    },
    "weapon of last resort": {
        "name": "Weapon of Last Resort",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Wield unarmed attacks as +1L weapons, and spend Willpower to inflict the Immobilized Tilt when biting.",
        "cost": "1 Willpower (optional)",
        "dice_pool": None,
        "duration": "Permanent",
        "book": "HTV 2e 125",
        "tags": ["weapon", "brawl"]
    },
    "sonic resonance attenuator": {
        "name": "Sonic Resonance Attenuator",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Suffer a two-die penalty to notice your immediate vicinity, but reveal a nearby auditory phenomenon in full clarity.",
        "cost": "1 Willpower",
        "dice_pool": "Wits + Empathy",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 124",
        "tags": ["perception", "sonic"]
    },
    "time attenuator": {
        "name": "Time Attenuator",
        "endowment_type": "thaumatechnology",
        "conspiracy": "Cheiron Group",
        "description": "Halt anything that would affect your body over time, including diseases, new Conditions, and healing from any source.",
        "cost": "1 Willpower",
        "dice_pool": "Intelligence + Medicine",
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 125",
        "tags": ["temporal", "stasis"]
    },
}

XENOTECHNOLOGY = {
    "cloaking device": {
        "name": "Cloaking Device",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Switch between Stealth and Infiltration modes, granting invisibility or 8-again on disguises.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 8,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 53",
        "tags": ["stealth", "invisibility", "disguise"]
    },
    "cyberglass": {
        "name": "Cyberglass",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Perceive the reality frequency of alien facilities or their servants.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 5,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 53",
        "tags": ["perception", "alien"]
    },
    "psi-crown": {
        "name": "Psi-Crown",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Tinfoil hat circlet of unearthly materials which protects against mind probes/control, provoking a Clash of Wills with 8-again on the roll.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 6,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 54",
        "tags": ["mental defense", "telepathy"]
    },
    "ray gun": {
        "name": "Ray Gun",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Range 30/60/120, Clip 3, Initiative -3 ranged weapon with damage equal to Xenotechnology rating that ignores material armor.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 10,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 54",
        "tags": ["weapon", "energy"]
    },
    "scramblers": {
        "name": "Scramblers",
        "endowment_type": "xenotechnology",
        "conspiracy": "Various",
        "description": "Long-ranged communications equipment which can also disrupt communications and surveillance within one mile, affecting supernatural equipment with a Clash of Wills.",
        "cost": None,
        "dice_pool": None,
        "target_successes": 5,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "TF 54",
        "tags": ["communication", "disruption"]
    }
}
# ============================================================================
# TELEINFORMATICS (Vanguard Serial Crimes Unit)
# ============================================================================

TELEINFORMATICS = {
    # Interview Category
    "just one more thing": {
        "name": "Just One More Thing",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "interview",
        "description": "Discover just the right question to ask the suspect.",
        "cost": "1 Bashing",
        "dice_pool": "Teleinformatics + Subterfuge",
        "book": "Slash 166",
        "tags": ["interrogation", "information"]
    },
    "polygraph": {
        "name": "Polygraph",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "interview",
        "description": "Exceptionally succeed on 3 successes against a target.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 120",
        "tags": ["interrogation", "lie detection"]
    },
    "synchronization": {
        "name": "Synchronization",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "interview",
        "description": "Copy the subject's mind.",
        "cost": "1 Willpower, 1 Lethal",
        "dice_pool": "Teleinformatics + Empathy - subject's Resolve",
        "book": "Slash 167",
        "tags": ["telepathy", "mind reading"]
    },
    "the talon": {
        "name": "The Talon",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "interview",
        "description": "Attack as a +2B mental weapon and inflict Traumatized.",
        "cost": "1 Bashing",
        "dice_pool": "Resolve + Intimidation vs Composure",
        "action": "Instant",
        "book": "HTV 2e 121",
        "tags": ["debuff", "mental attack"]
    },
    "tactical co-ordination": {
        "name": "Tactical Co-Ordination",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "interview",
        "description": "Link minds with others and all members get bonuses on Skills for each member with a higher rating.",
        "cost": "1 Willpower, 1 Lethal",
        "dice_pool": "Teleinformatics + Brawl - # of other agents",
        "book": "Slash 168",
        "tags": ["teamwork", "telepathy"]
    },
    # Investigation Category
    "psychometry": {
        "name": "Psychometry",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "investigation",
        "description": "Understand an object.",
        "cost": "1 Bashing",
        "dice_pool": "Teleinformatics + Crafts",
        "book": "Slash 169",
        "tags": ["information", "psychometry"]
    },
    "scene read": {
        "name": "Scene Read",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "investigation",
        "description": "Normal investigation of a scene at instant speed.",
        "cost": "1 Bashing",
        "dice_pool": "Teleinformatics + Investigation",
        "book": "Slash 169",
        "tags": ["investigation", "speed"]
    },
    "speed of thought": {
        "name": "Speed Of Thought",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "investigation",
        "description": "Use the greater of Wits or Dexterity for Defense, and move to the top of Initiative.",
        "cost": "1 Lethal",
        "dice_pool": None,
        "action": "Reflexive",
        "duration": "1 Scene",
        "book": "HTV 2e 121",
        "tags": ["speed", "defense"]
    },
    "postcognition": {
        "name": "Postcognition",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "investigation",
        "description": "Gain Clues about a crime, and become Informed with Willpower spent.",
        "cost": "1 Lethal (1 Willpower optional)",
        "dice_pool": "Wits + Investigation - Time modifier",
        "action": "Instant",
        "book": "HTV 2e 120",
        "tags": ["information", "vision"]
    },
    "hall of mirrors": {
        "name": "Hall Of Mirrors",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "investigation",
        "description": "Ask a question of a subject's future, becoming Informed.",
        "cost": "1 Lethal",
        "dice_pool": "Wits + Occult",
        "action": "Extended (5, 5 minutes per roll)",
        "book": "HTV 2e 120",
        "tags": ["precognition", "information"]
    },
    # Research Category
    "network": {
        "name": "Network",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "research",
        "description": "Know the right place to look.",
        "cost": "1 Bashing",
        "dice_pool": "Teleinformatics + Academics",
        "book": "Slash 173",
        "tags": ["research", "information"]
    },
    "deep background": {
        "name": "Deep Background",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "research",
        "description": "Find documents relating to a suspect at 3 successes per document.",
        "cost": "1 Bashing per roll",
        "dice_pool": "Teleinformatics + Computer",
        "book": "Slash 173",
        "tags": ["research", "information"]
    },
    "bookworm": {
        "name": "Bookworm",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "research",
        "description": "Automatically succeed at any Academics or Occult based research action.",
        "cost": "1 Willpower, 1 Lethal",
        "dice_pool": None,
        "book": "Slash 174",
        "tags": ["research", "automatic success"]
    },
    "tag": {
        "name": "Tag",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "research",
        "description": "Spy on a target through cameras and small animals, gaining +2 to track the target and becoming Informed.",
        "cost": "1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "duration": "1 Scene",
        "book": "HTV 2e 121",
        "tags": ["tracking", "surveillance"]
    },
    "omnicompetence": {
        "name": "Omnicompetence",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "category": "research",
        "description": "Temporarily increase one skill to 5 dots or all skills in a category to 3 dots.",
        "cost": "1 Lethal or 1 Aggravated",
        "dice_pool": "Teleinformatics + Larceny",
        "book": "Slash 175",
        "tags": ["skill enhancement", "temporary"]
    },
    "codex": {
        "name": "Codex",
        "endowment_type": "teleinformatics",
        "conspiracy": "Vanguard Serial Crimes Unit",
        "description": "For one investigation or research, halve the time and exceptionally succeed on 3 successes.",
        "cost": "1 Lethal, 1 Willpower",
        "dice_pool": None,
        "action": "Instant",
        "book": "HTV 2e 119",
        "tags": ["research", "investigation"]
    },
}

# ============================================================================
# GOETIC GOSPEL (Knights of Saint George)
# ============================================================================

GOETIC_GOSPEL = {
    # Gospel of Agares
    "lie of the heart": {
        "name": "Lie of the Heart",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "agares",
        "description": "Ignore spells that affect anyone in a given area.",
        "cost": "1 Willpower",
        "dice_pool": "Wits + Goetic Gospels",
        "book": "WF 130",
        "tags": ["mage", "protection"]
    },
    "crocodile armor": {
        "name": "Crocodile Armor",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "agares",
        "description": "Gain armor against spells or enchanted weapons equal to Goetic Gospels rating.",
        "cost": "1 Willpower",
        "dice_pool": "Stamina + Goetic Gospels",
        "book": "WF 130",
        "tags": ["mage", "armor"]
    },
    "agares goshawk": {
        "name": "Agares' Goshawk",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "agares",
        "description": "Dispell a spell.",
        "cost": "1 Willpower",
        "dice_pool": "Manipulation + Goetic Gospels vs spell die pool",
        "book": "WF 130",
        "tags": ["mage", "dispel"]
    },
    "envys barb": {
        "name": "Envy's Barb",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "agares",
        "description": "Counter a spell. The Hunter can take any amount of Bashing to receive +2 on the roll for each point of Bashing spent. Optionally, the Hunter can spend a Lethal damage and deal Lethal damage to the spell caster equal to additional successes made on the Goetic Gospel roll.",
        "cost": "1 Willpower (1 Lethal optional)",
        "dice_pool": "Presence + Goetic Gospels",
        "book": "WF 131",
        "tags": ["mage", "counter", "reflect"]
    },
    "flagellants denial": {
        "name": "Flagellant's Denial",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "agares",
        "description": "Negate all spells in a 5 yard radius of the Hunter at a level equal to or lower than the amount of Lethal damage taken.",
        "cost": "1 Willpower (spent per activation), 1-5 Lethal (spent once for a scene)",
        "dice_pool": "Resolve + Goetic Gospels",
        "book": "WF 131",
        "tags": ["mage", "suppression", "area effect"]
    },
    # Gospel of Amon
    "stolen vice": {
        "name": "Stolen Vice",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "amon",
        "description": "Whenever the target would indulge his or her vice, she receives no Willpower. If 2B is spent, the Hunter receives it instead.",
        "cost": "1 Willpower (2 Bashing optional)",
        "dice_pool": "Manipulation + Goetic Gospels vs Resolve + Gnosis",
        "book": "WF 132",
        "tags": ["mage", "curse", "willpower"]
    },
    "maddening whispers": {
        "name": "Maddening Whispers",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "amon",
        "description": "Inflict a mild derangement on a target. If 1L is spent, inflict a severe derangement instead.",
        "cost": "1 Willpower (1 Lethal optional)",
        "dice_pool": "Composure + Goetic Gospels",
        "book": "WF 133",
        "tags": ["mage", "derangement", "mental attack"]
    },
    "magpie mysteries": {
        "name": "Magpie Mysteries",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "amon",
        "description": "Steal the ability to use spells from a given Mystery from the target and deny the target use. If 1L is spent, the target is denied use of two Mysteries.",
        "cost": "1 Willpower (1 Lethal optional)",
        "dice_pool": "Dexterity + Goetic Gospels vs Composure + Gnosis",
        "book": "WF 133",
        "tags": ["mage", "theft", "suppression"]
    },
    "viscous cycle": {
        "name": "Viscous Cycle",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "amon",
        "description": "Make the target make a degeneration roll equal to the most severe sin they have committed. If they fail, they receive -3 on all rolls and cannot regain WP from their Virtue for the rest of the scene. If 1L is spent, the degeneration roll is made as though it were one level worse.",
        "cost": "1 Willpower (1 Lethal optional)",
        "dice_pool": "Presence + Goetic Gospels",
        "book": "WF 133",
        "tags": ["mage", "curse", "morality"]
    },
    "demon king of nothing": {
        "name": "Demon King of Nothing",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "amon",
        "description": "All spells the target rolls are Vulgar. If an additional 1L is spent, all spells also receive a -1 Vulgarity modifier.",
        "cost": "1 Willpower, 1 Lethal (1 Lethal optional)",
        "dice_pool": "Stamina + Goetic Gospels vs Resolve + Gnosis",
        "book": "WF 134",
        "tags": ["mage", "curse", "paradox"]
    },
    # Gospel of Beleth
    "glutenous devourer": {
        "name": "Glutenous Devourer",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "beleth",
        "description": "Prevent the target from generating or receiving Source. The target also loses Source equal to successes rolled. If 1L is spent, the target loses 1 Willpower each time they try to generate Source.",
        "cost": "1 Willpower (1 Lethal optional)",
        "dice_pool": "Wits + Goetic Gospels - Subject's Resolve",
        "book": "WF 134",
        "tags": ["mage", "source", "drain"]
    },
    "servitor of sloth": {
        "name": "Servitor of Sloth",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "beleth",
        "description": "Whenever the target would use a point of Source, they must also spend a point of Willpower. If 1L was spent, the target must also succeed on a Resolve+Composure roll to spend Source.",
        "cost": "1 Willpower (1 Lethal optional)",
        "dice_pool": "Intelligence + Goetic Gospels vs Resolve + Gnosis",
        "book": "WF 134",
        "tags": ["mage", "source", "restriction"]
    },
    "poison baubles": {
        "name": "Poison Baubles",
        "endowment_type": "goetic_gospel",
        "conspiracy": "Knights of Saint George",
        "gospel": "beleth",
        "description": "The target receives Lethal damage equal to the amount of Source the target is storing up to the Hunter's Goetic Gospels rating.",
        "cost": "1 Willpower, 1 Lethal",
        "dice_pool": "Presence + Goetic Gospels vs Stamina + Gnosis",
        "book": "WF 135",
        "tags": ["mage", "attack", "source"]
    },
}

# ============================================================================
# RITES OF DENIAL (Cainite Heresy)
# ============================================================================

RITES_OF_DENIAL = {
    "aggravate": {
        "name": "Aggravate",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Weapon now deals Lethal damage and gains a bonus equal to dots in Rites of Denial. The bonus only applies to Vampires, minions of Vampires and unliving creatures.",
        "cost": "1 Willpower, 2 thimbles of blood",
        "dice_pool": None,
        "book": "NS 151",
        "tags": ["vampire", "weapon", "enhancement"]
    },
    "befoul": {
        "name": "Befoul",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "If a Vampire sleeps in the targeted location, they receive 1L per hour slept there and cannot spend Blood for any purpose.",
        "cost": "1 Willpower, 4 thimbles of blood",
        "dice_pool": None,
        "book": "NS 151",
        "tags": ["vampire", "curse", "location"]
    },
    "behold": {
        "name": "Behold",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "All non-hidden Vampires within sight are revealed for what they are.",
        "cost": "1 Willpower, 1 thimble of blood",
        "dice_pool": None,
        "book": "NS 152",
        "tags": ["vampire", "detection"]
    },
    "deny": {
        "name": "Deny",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Create a barrier that blocks the access of Vampires.",
        "cost": "1 Willpower, 2 thimbles of blood",
        "dice_pool": None,
        "book": "NS 152",
        "tags": ["vampire", "barrier"]
    },
    "evade": {
        "name": "Evade",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Gain Speed bonus equal to Endowment dots.",
        "cost": "1 Willpower, 1 thimble of blood",
        "dice_pool": None,
        "book": "NS 153",
        "tags": ["speed", "escape"]
    },
    "invoke": {
        "name": "Invoke",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Create an apotrope that repels Vampires and deals 1 Aggravated damage if it touches them.",
        "cost": "1 Willpower, 3 thimbles of blood",
        "dice_pool": None,
        "book": "NS 153",
        "tags": ["vampire", "ward", "aggravated"]
    },
    "mark": {
        "name": "Mark",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Gain bonus die equal to endowment to stake or decapitate a Vampire.",
        "cost": "1 Willpower, 2 thimbles of blood",
        "dice_pool": None,
        "book": "NS 153",
        "tags": ["vampire", "enhancement", "staking"]
    },
    "obligate": {
        "name": "Obligate",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Fix a Vampire to the ground.",
        "cost": "1 Willpower, 2 thimbles of blood",
        "dice_pool": None,
        "book": "NS 154",
        "tags": ["vampire", "immobilize"]
    },
    "pilfer": {
        "name": "Pilfer",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Know a secret a Vampire doesn't want known.",
        "cost": "1 Willpower, 3 thimbles of blood",
        "dice_pool": None,
        "book": "NS 154",
        "tags": ["vampire", "information"]
    },
    "prohibit": {
        "name": "Prohibit",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Another person's blood offer no nourishment to Vampires and when drunk, deals damage to the Vampire equal to the caster's Endowment dots.",
        "cost": "1 Willpower, 2 thimbles of blood",
        "dice_pool": None,
        "book": "NS 154",
        "tags": ["vampire", "curse", "blood"]
    },
    "question": {
        "name": "Question",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Give a Vampire a Severe Derangement.",
        "cost": "1 Willpower, 5 thimbles of blood",
        "dice_pool": None,
        "book": "NS 155",
        "tags": ["vampire", "derangement"]
    },
    "reflect": {
        "name": "Reflect",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Powers against the Hunter that would require eye contact get a penalty equal to the Hunter's Endowment dots.",
        "cost": "1 Willpower, 1 thimble of blood",
        "dice_pool": None,
        "book": "NS 156",
        "tags": ["vampire", "defense", "mental"]
    },
    "unmask": {
        "name": "Unmask",
        "endowment_type": "rites_of_denial",
        "conspiracy": "Cainite Heresy",
        "description": "Make a Vampire illuminate brightly and appear in all media and mirrors.",
        "cost": "1 Willpower, 1 thimble of blood",
        "dice_pool": None,
        "book": "NS 156",
        "tags": ["vampire", "reveal", "exposure"]
    },
}

# Endowments by type
ADVANCED_ARMORY_POWERS = list(ADVANCED_ARMORY.keys())
ANIMAL_CONTROL_KIT_POWERS = list(ANIMAL_CONTROL_KIT.keys())
BENEDICTION_POWERS = list(BENEDICTION.keys())
CASTIGATION_POWERS = list(CASTIGATION.keys())
DREAMSCAPE_POWERS = list(DREAMSCAPE.keys())
ELIXIR_POWERS = list(ELIXIR.keys())
ENKOIMESIS_POWERS = list(ENKOIMESIS.keys())
GOETIC_GOSPEL_POWERS = list(GOETIC_GOSPEL.keys())
HORROR_WITHIN_POWERS = list(HORROR_WITHIN.keys())
INFUSION_POWERS = list(INFUSION.keys())
INK_POWERS = list(INK.keys())
INSPIRATION_POWERS = list(INSPIRATION.keys())
LIVES_REMEMBERED_POWERS = list(LIVES_REMEMBERED.keys())
PERISPIRITISM_POWERS = list(PERISPIRITISM.keys())
RELIC_POWERS = list(RELIC.keys())
RITES_DU_CHEVAL_POWERS = list(RITES_DU_CHEVAL.keys())
RITES_OF_DENIAL_POWERS = list(RITES_OF_DENIAL.keys())
SEITOKUTEN_POWERS = list(SEITOKUTEN.keys())
TELEINFORMATICS_POWERS = list(TELEINFORMATICS.keys())
THAUMATECHNOLOGY_POWERS = list(THAUMATECHNOLOGY.keys())
XENOTECHNOLOGY_POWERS = list(XENOTECHNOLOGY.keys())

# All valid endowment power names for validation
ALL_ENDOWMENT_POWERS = list(get_all_endowments().keys())

