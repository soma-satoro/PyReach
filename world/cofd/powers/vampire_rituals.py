"""
Vampire Ritual Magic Systems for Chronicles of Darkness 2nd Edition.

This module contains ritual magic systems (Scales of the Dragon, Theban Sorcery, and Cruac).
These are covenant-specific supernatural powers that work differently from Disciplines.

Ritual magic uses:
- Ranks (1-5 dots) instead of progressive discipline levels  
- Target numbers for dice pools
- Opposition mechanics for contested rolls
- Material components or sacraments
- Longer casting times than instant discipline powers
"""

# ==================== SCALES OF THE DRAGON ====================
# Ordo Dracul alchemical rituals organized by Mystery

SCALES_ASCENDANT = {
    "day_wake_conditioning": {
        "name": "Day-Wake Conditioning",
        "type": "scale",
        "mystery": "ascendant",
        "rank": 1,
        "description": "Use directed insomnia to invert a subject vampire's circadian rhythm.",
        "book": "VTR 2e p.156"
    },
    "flesh_graft_treatment": {
        "name": "Flesh Graft Treatment",
        "type": "scale",
        "mystery": "ascendant",
        "rank": 4,
        "description": "Soak skin grafts in human blood to enhance a subject's ability to heal through Vitae.",
        "book": "VTR 2e p.156"
    },
    "epidermal_shielding_bath": {
        "name": "Epidermal Shielding Bath",
        "type": "scale",
        "mystery": "ascendant",
        "rank": 5,
        "description": "Submerge a subject vampire in an alchemical bath of blood and reagents to shield them from sunlight as if they possessed higher Humanity.",
        "book": "VTR 2e p.156"
    }
}

SCALES_QUINTESSENCE = {
    "cold_of_the_grave": {
        "name": "Cold of the Grave",
        "type": "scale",
        "mystery": "quintessence",
        "rank": 3,
        "description": "Mix a tithe of local Kindred's Vitae with your own and a slurry of ground corpses to share Smother with resident Kindred.",
        "book": "Thousand Years p.82"
    },
    "codependency": {
        "name": "Codependency",
        "type": "scale",
        "mystery": "quintessence",
        "rank": 5,
        "description": "Bury ghouls alive across your domain, anointed with Vitae, to attune the domain to your Aspirations subconsciously and share Fingers on a Dead Pulse with resident Kindred.",
        "book": "Thousand Years p.82"
    }
}

SCALES_VOIVODE = {
    "blood_cleansing_ritual": {
        "name": "Blood Cleansing Ritual",
        "type": "scale",
        "mystery": "voivode",
        "rank": 1,
        "description": "Wash a subject of the blood bond with blood and viscera.",
        "book": "VTR 2e p.158"
    },
    "sanguinary_invigoration": {
        "name": "Sanguinary Invigoration",
        "type": "scale",
        "mystery": "voivode",
        "rank": 2,
        "description": "Inject a living vessel with an alchemical solution of your blood to permit vampires to feed from the vessel as if at lower Blood Potency.",
        "book": "VTR 2e p.159"
    },
    "fealtys_reward": {
        "name": "Fealty's Reward",
        "type": "scale",
        "mystery": "voivode",
        "rank": 3,
        "description": "Ritually drain and feed a thrall to transform them into a proprietary ghoul for a year.",
        "book": "VTR 2e p.159"
    },
    "mass_embrace": {
        "name": "Mass Embrace",
        "type": "scale",
        "mystery": "voivode",
        "rank": 5,
        "description": "Exsanguinate a roomful of people and mix their blood with your own to raise all of them as hungry vampires.",
        "book": "VTR 2e p.159"
    }
}

SCALES_WYRM = {
    "kindred_sense_endowment": {
        "name": "Kindred Sense Endowment",
        "type": "scale",
        "mystery": "wyrm",
        "rank": 2,
        "description": "Apply a compound of blood and bone to a mortal subject, imbuing them with temporary Kindred Senses.",
        "book": "VTR 2e p.157"
    },
    "augmented_vitae_draught": {
        "name": "Augmented Vitae Draught",
        "type": "scale",
        "mystery": "wyrm",
        "rank": 4,
        "description": "Draw your Vitae out into sterilized equipment to store Physical Intensity in it for mortal drinkers.",
        "book": "VTR 2e p.157"
    },
    "surgical_heart_removal": {
        "name": "Surgical Heart Removal",
        "type": "scale",
        "mystery": "wyrm",
        "rank": 5,
        "description": "Bypass a vampire subject's circulatory system. The heartless vampire cannot feed, but is immune to staking and may regenerate so long as their heart is intact.",
        "book": "VTR 2e p.158"
    }
}

SCALES_ZIRNITRA = {
    "psychic_lobotomy": {
        "name": "Psychic Lobotomy",
        "type": "scale",
        "mystery": "zirnitra",
        "rank": 1,
        "description": "Surgically damage a subject's brain. They lose any Supernatural Merits, but add your dots in the Coil of Zirnitra to resist mental probing or influence.",
        "book": "Secrets of the Covenants p.200"
    },
    "grafting_unholy_flesh": {
        "name": "Grafting Unholy Flesh",
        "type": "scale",
        "mystery": "zirnitra",
        "rank": 4,
        "description": "Graft a supernatural being's body part onto a vampire or ghoul subject to steal the use of one of the being's powers.",
        "book": "Secrets of the Covenants p.200"
    }
}

SCALES_ZIVA = {
    "bleed_the_sin": {
        "name": "Bleed the Sin",
        "type": "scale",
        "mystery": "ziva",
        "rank": 2,
        "description": "Maintain a subject drained of blood to offer them a discount on a dot of an Integrity trait.",
        "book": "Secrets of the Covenants p.201"
    },
    "siphon_the_soul": {
        "name": "Siphon the Soul",
        "type": "scale",
        "mystery": "ziva",
        "rank": 3,
        "description": "Nearly diablerize a vampire subject to consume a dot of the subject's Humanity.",
        "book": "Secrets of the Covenants p.202"
    }
}

SCALES_OTHER = {
    "spirit_tether": {
        "name": "Spirit Tether",
        "type": "scale",
        "mystery": "other",
        "rank": "Any coil:2",
        "prerequisites": "Resolve:4",
        "description": "Ingest or inject yourself with a mix of Vitae and hallucinogens, then repeatedly lull yourself into a near-torpor state. Gain the ability to astral project (as Auspex) and the ability to use specific other scales built on this one.",
        "book": "Night Horrors: Shunned by the Moon p.101"
    },
    "psychic_leech": {
        "name": "Psychic Leech",
        "type": "scale",
        "mystery": "other",
        "rank": "See Description",
        "prerequisites": "Spirit Tether, Empathy:3",
        "description": "Attune yourself to the Vitae of others by anointing several locations or individuals, then visit every anointed location or individual while under Spirit Tether. Can spend Willpower to drain Vitae from others while under Spirit Tether.",
        "book": "Night Horrors: Shunned by the Moon p.101"
    },
    "beseech_the_sleeping": {
        "name": "Beseech The Sleeping",
        "type": "scale",
        "mystery": "other",
        "rank": "See Description",
        "prerequisites": "Spirit Tether, Expression:2",
        "description": "Sleep through an entire night, then spend the entire day under the Blush of Life. The next time you use Spirit Tether, you can learn the recent memories of sleeping mortals.",
        "book": "Night Horrors: Shunned by the Moon p.101"
    },
    "command_the_mind": {
        "name": "Command The Mind",
        "type": "scale",
        "mystery": "other",
        "rank": "See Description",
        "prerequisites": "Psychic Leech, Manipulation:3, Dominate:1",
        "description": "While under Spirit Tether, use Psychic Leech to 'Embrace' your own body, spending a permanent Willpower dot. Gain the ability to spend Vitae to drain Willpower while not under Spirit Tether.",
        "book": "Night Horrors: Shunned by the Moon p.101"
    }
}

ALL_SCALES = {
    **SCALES_ASCENDANT,
    **SCALES_QUINTESSENCE,
    **SCALES_VOIVODE,
    **SCALES_WYRM,
    **SCALES_ZIRNITRA,
    **SCALES_ZIVA,
    **SCALES_OTHER
}

SCALES_BY_MYSTERY = {
    "ascendant": SCALES_ASCENDANT,
    "quintessence": SCALES_QUINTESSENCE,
    "voivode": SCALES_VOIVODE,
    "wyrm": SCALES_WYRM,
    "zirnitra": SCALES_ZIRNITRA,
    "ziva": SCALES_ZIVA,
    "other": SCALES_OTHER
}

# ==================== THEBAN SORCERY ====================
# Lancea et Sanctum miracles organized by rank

THEBAN_RANK_1 = {
    "apple_of_eden": {
        "name": "Apple of Eden",
        "type": "theban",
        "rank": 1,
        "target_number": 5,
        "opposition": "-",
        "sacrament": "●, apple",
        "description": "Infuse a fruit with Vitae. A human who eats the fruit suffers a breaking point, but distributes bonus dots between Intelligence and Wits and can safely perceive supernatural beings on sight for a matter of days.",
        "book": "Secrets of the Covenants p.194"
    },
    "blandishment_of_sin": {
        "name": "Blandishment of Sin",
        "type": "theban",
        "rank": 1,
        "target_number": 5,
        "opposition": "vs. Resolve + Tolerance",
        "sacrament": "Victim's written name",
        "description": "Upgrades the next strike of bashing damage against the victim before sunrise to lethal.",
        "book": "VTR 2e p.153"
    },
    "blood_scourge": {
        "name": "Blood Scourge",
        "type": "theban",
        "rank": 1,
        "target_number": 6,
        "opposition": "-",
        "sacrament": "*",
        "description": "Before sunrise, conjure a 2L whip of Vitae for a scene.",
        "book": "VTR 2e p.153"
    },
    "marian_apparition": {
        "name": "Marian Apparition",
        "type": "theban",
        "rank": 1,
        "target_number": 5,
        "opposition": "vs. Humanity",
        "sacrament": "Cloth stained by menstrual blood",
        "description": "Bless the cloth. When torn, the cloth induces shame through a sacred vision, causing Kindred to risk detachment more easily for a scene.",
        "book": "Secrets of the Covenants p.194"
    },
    "revelatory_shroud": {
        "name": "Revelatory Shroud",
        "type": "theban",
        "rank": 1,
        "target_number": 5,
        "opposition": "-",
        "sacrament": "Shroud",
        "description": "Display the face of the last person to touch an object or area.",
        "book": "Secrets of the Covenants p.194"
    },
    "vitae_reliquary": {
        "name": "Vitae Reliquary",
        "type": "theban",
        "rank": 1,
        "target_number": 5,
        "opposition": "-",
        "sacrament": "Small object",
        "description": "Infuse an object with Vitae for a month, which can be extracted as if feeding.",
        "book": "VTR 2e p.153"
    }
}

THEBAN_RANK_2 = {
    "apparition_of_the_host": {
        "name": "Apparition of the Host",
        "type": "theban",
        "rank": 2,
        "target_number": 6,
        "opposition": "vs. Resolve + Tolerance",
        "sacrament": "Holly switch",
        "description": "Bless the switch for a month. When snapped, the switch terrorizes a victim with angelic phantasms, which can be displayed or hidden from other witnesses.",
        "book": "Secrets of the Covenants p.194"
    },
    "bloody_icon": {
        "name": "Bloody Icon",
        "type": "theban",
        "rank": 2,
        "target_number": 6,
        "opposition": "-",
        "sacrament": "Statue of a saint",
        "description": "Detach from Humanity in a religious reverie wherein the statue weeps Vitae, then crumbles.",
        "book": "Secrets of the Covenants p.195"
    },
    "curse_of_babel": {
        "name": "Curse of Babel",
        "type": "theban",
        "rank": 2,
        "target_number": 6,
        "opposition": "- Resolve",
        "sacrament": "Tongue",
        "description": "Prevent a victim from communicating until sunrise.",
        "book": "VTR 2e p.153"
    },
    "liars_plague": {
        "name": "Liar's Plague",
        "type": "theban",
        "rank": 2,
        "target_number": 5,
        "opposition": "vs. Resolve + Tolerance",
        "sacrament": "Carapace",
        "description": "Subject a victim for one scene to a curse of beetles if they lie.",
        "book": "VTR 2e p.153"
    },
    "the_walls_of_jericho": {
        "name": "The Walls of Jericho",
        "type": "theban",
        "rank": 2,
        "target_number": 6,
        "opposition": "-",
        "sacrament": "Horn",
        "description": "Mark a horn with the name of a Kindred subject. For a week, blow the horn and roll Presence + Academics + Theban Sorcery to damage inanimate surfaces between you and the subject.",
        "book": "Secrets of the Covenants p.195"
    }
}

THEBAN_RANK_3 = {
    "aarons_rod": {
        "name": "Aaron's Rod",
        "type": "theban",
        "rank": 3,
        "target_number": 8,
        "opposition": "-",
        "sacrament": "Rod",
        "description": "Bless the rod. When cast, it becomes a serpent which either obeys its wielder or instructions you gave during the blessing.",
        "book": "Secrets of the Covenants p.195"
    },
    "baptism_of_damnation": {
        "name": "Baptism of Damnation",
        "type": "theban",
        "rank": 3,
        "target_number": 6,
        "opposition": "vs Resolve + Tolerance",
        "sacrament": "Silver baptismal font",
        "description": "Conceives a healthy dhampir child to a participating vampire and mortal.",
        "book": "Half-Damned p.14"
    },
    "blessing_the_legion": {
        "name": "Blessing the Legion",
        "type": "theban",
        "rank": 3,
        "target_number": "6+",
        "opposition": "-",
        "sacrament": "Armor",
        "description": "Bless the armor with either your Vitae or the subject's. The subject wearing the armor may heal with its Vitae without counting towards per-turn maximums.",
        "book": "Secrets of the Covenants p.195"
    },
    "the_guiding_star": {
        "name": "The Guiding Star",
        "type": "theban",
        "rank": 3,
        "target_number": 8,
        "opposition": "-",
        "sacrament": "Star chart, gold coins",
        "description": "Bless the coins. A person carrying a coin may navigate by the stars to an exclusive place of refuge and blood bounty for a matter of nights.",
        "book": "Secrets of the Covenants p.196"
    },
    "malediction_of_despair": {
        "name": "Malediction of Despair",
        "type": "theban",
        "rank": 3,
        "target_number": 13,
        "opposition": "vs. Resolve + Tolerance",
        "sacrament": "Lock of victim's hair",
        "description": "Name an action to curse. The victim's next attempt within the month takes a -5 penalty.",
        "book": "VTR 2e p.154"
    },
    "miracle_of_the_dead_sun": {
        "name": "Miracle of the Dead Sun",
        "type": "theban",
        "rank": 3,
        "target_number": 6,
        "opposition": "-",
        "sacrament": "Silver jewelry",
        "description": "Bless the jewelry. When destroyed at the cost of a user's Humanity, the domain is shrouded in rainy night for ten minutes per remaining Humanity dot.",
        "book": "Secrets of the Covenants p.196"
    },
    "pledge_to_the_worthless_one": {
        "name": "Pledge to the Worthless One",
        "type": "theban",
        "rank": 3,
        "target_number": 8,
        "opposition": "-",
        "sacrament": "A contented mortal",
        "description": "Swear your soul to Belial for eternity. Choose a deadly sin. Active sinners nourish for twice the Vitae, but those innocent of the sin nourish for half. Always take bonuses as if mid-frenzy. Acquire a familiar, manifest the devil's mark, and lose the benefits of Touchstones.",
        "book": "Secrets of the Covenants p.196"
    },
    "the_rite_of_ascending_blood": {
        "name": "The Rite of Ascending Blood",
        "type": "theban",
        "rank": 3,
        "target_number": 7,
        "opposition": "-",
        "sacrament": "Baptismal font filled with Vitae",
        "description": "Harrowing mortification rebirths a revenant as the Kindred childe of a participating sire. Her Humanity returns to 7, her Disciplines are refunded, and she may instantly spend the experiences on appropriate purchases, including clan Disciplines and Blood Potency.",
        "book": "Half-Damned p.78"
    }
}

THEBAN_RANK_4 = {
    "blandishment_of_sin_advanced": {
        "name": "Blandishment of Sin (Advanced)",
        "type": "theban",
        "rank": 4,
        "target_number": 8,
        "opposition": "vs. Resolve + Tolerance",
        "sacrament": "Victim's written name",
        "description": "Upgrades the next strike of lethal damage against the victim before sunrise to aggravated.",
        "book": "VTR 2e p.153"
    },
    "curse_of_isolation": {
        "name": "Curse of Isolation",
        "type": "theban",
        "rank": 4,
        "target_number": 15,
        "opposition": "vs Resolve + Tolerance",
        "sacrament": "Edged weapon",
        "description": "Elder miracle. Strip a vampire of their bond to a present Touchstone, stealing the Touchstone for your own use.",
        "book": "Thousand Years p.79"
    },
    "gift_of_lazarus": {
        "name": "Gift of Lazarus",
        "type": "theban",
        "rank": 4,
        "target_number": 8,
        "opposition": "-",
        "sacrament": "Communion wafer",
        "description": "Raise a fresh corpse as a dead servant for a month.",
        "book": "VTR 2e p.154"
    },
    "great_prophecy": {
        "name": "Great Prophecy",
        "type": "theban",
        "rank": 4,
        "target_number": 8,
        "opposition": "-",
        "sacrament": "Saint's body part",
        "description": "Issue a prophecy to a group of people, foretelling the thrust of their fate within the month, and how it can be averted.",
        "book": "Secrets of the Covenants p.196"
    },
    "stigmata": {
        "name": "Stigmata",
        "type": "theban",
        "rank": 4,
        "target_number": 5,
        "opposition": "- Stamina",
        "sacrament": "Crucifix",
        "description": "Curse a victim to temporarily bleed from stigmatic wounds, causing lethal damage or sapping Vitae.",
        "book": "VTR 2e p.154"
    },
    "trials_of_job": {
        "name": "Trials of Job",
        "type": "theban",
        "rank": 4,
        "target_number": 10,
        "opposition": "- Resolve",
        "sacrament": "Ox or ram horn",
        "description": "Curse a victim to suffering, failure, abandonment, and sickness for a night per Potency.",
        "book": "Dark Eras 2 p.339"
    }
}

THEBAN_RANK_5 = {
    "apocalypse": {
        "name": "Apocalypse",
        "type": "theban",
        "rank": 5,
        "target_number": "10+",
        "opposition": "-",
        "sacrament": "Ancient text",
        "description": "Exposes signs of supernatural beings' true nature for a week, disrupting obfuscatory and illusory powers.",
        "book": "Secrets of the Covenants p.197"
    },
    "the_judgment_fast": {
        "name": "The Judgment Fast",
        "type": "theban",
        "rank": 5,
        "target_number": 15,
        "opposition": "-",
        "sacrament": "Rotten feast",
        "description": "Curse the domain for a month. Vampires there only sustain up to their Humanity in Vitae.",
        "book": "Secrets of the Covenants p.197"
    },
    "orison_of_voices": {
        "name": "Orison of Voices",
        "type": "theban",
        "rank": 5,
        "target_number": 8,
        "opposition": "-",
        "sacrament": "Rosary",
        "description": "Elder miracle. For three nights, hear speech that invokes your name.",
        "book": "Thousand Years p.79"
    },
    "sins_of_the_ancestors": {
        "name": "Sins of the Ancestors",
        "type": "theban",
        "rank": 5,
        "target_number": 6,
        "opposition": "-",
        "sacrament": "Quantity of victim's blood",
        "description": "Elder miracle. For each Potency, ask the Storyteller a simple question about a member of the victim's blood lineage.",
        "book": "Thousand Years p.79"
    },
    "transubstantiation": {
        "name": "Transubstantiation",
        "type": "theban",
        "rank": 5,
        "target_number": 8,
        "opposition": "vs. Stamina + Tolerance",
        "sacrament": "Drop of gold",
        "description": "Transmute one substance or being into another until sunrise.",
        "book": "VTR 2e p.154"
    }
}

ALL_THEBAN = {
    **THEBAN_RANK_1,
    **THEBAN_RANK_2,
    **THEBAN_RANK_3,
    **THEBAN_RANK_4,
    **THEBAN_RANK_5
}

THEBAN_BY_RANK = {
    1: THEBAN_RANK_1,
    2: THEBAN_RANK_2,
    3: THEBAN_RANK_3,
    4: THEBAN_RANK_4,
    5: THEBAN_RANK_5
}

# ==================== CRUAC ====================
# Circle of the Crone blood sorcery organized by rank

CRUAC_RANK_1 = {
    "ban_of_the_spiteful_bastard": {
        "name": "Ban of the Spiteful Bastard",
        "type": "cruac",
        "rank": 1,
        "target_number": 6,
        "opposition": "- Composure",
        "description": "Revenants only. Curse your sire to rise without Vitae for your Potency in nights.",
        "book": "Half-Damned p.78"
    },
    "mantle_of_amorous_fire": {
        "name": "Mantle of Amorous Fire",
        "type": "cruac",
        "rank": 1,
        "target_number": 5,
        "opposition": "-",
        "description": "Dance to exhaustion. Add Cruac as a Presence bonus for the night.",
        "book": "Secrets of the Covenants p.184"
    },
    "pangs_of_proserpina": {
        "name": "Pangs of Proserpina",
        "type": "cruac",
        "rank": 1,
        "target_number": 6,
        "opposition": "vs Composure + Tolerance",
        "description": "A victim up to a mile away suffers feelings of intense hunger, provoking frenzy in Kindred.",
        "book": "VTR 2e p.152"
    },
    "pool_of_forbidden_truths": {
        "name": "Pool of Forbidden Truths",
        "type": "cruac",
        "rank": 1,
        "target_number": 5,
        "opposition": "-",
        "description": "The caster gains the Primeval Truths Condition and experiences a vision. Roll Wits + Investigation + Cruac to interpret.",
        "book": "Secrets of the Covenants p.184"
    },
    "rigor_mortis": {
        "name": "Rigor Mortis",
        "type": "cruac",
        "rank": 1,
        "target_number": 5,
        "opposition": "- Composure",
        "description": "A vampiric victim within a mile stiffens and suffers a -3 Physical penalty.",
        "book": "VTR 2e p.152"
    }
}

CRUAC_RANK_2 = {
    "cheval": {
        "name": "Cheval",
        "type": "cruac",
        "rank": 2,
        "target_number": 5,
        "opposition": "- Composure",
        "description": "Borrow a touched subject's sight and hearing for the rest of the night.",
        "book": "VTR 2e p.152"
    },
    "mantle_of_the_beasts_breath": {
        "name": "Mantle of the Beast's Breath",
        "type": "cruac",
        "rank": 2,
        "target_number": 5,
        "opposition": "-",
        "description": "Dance to exhaustion. Gain the Raptured Condition and add Cruac as a bonus to ride the wave for the night.",
        "book": "Secrets of the Covenants p.184"
    },
    "hydras_vitae": {
        "name": "Hydra's Vitae",
        "type": "cruac",
        "rank": 2,
        "target_number": 5,
        "opposition": "-",
        "description": "Transform blood in your system into a poison causing lethal damage, yielding no Vitae when drank.",
        "book": "VTR 2e p.152"
    },
    "shed_the_virulent_bowels": {
        "name": "Shed the Virulent Bowels",
        "type": "cruac",
        "rank": 2,
        "target_number": 6,
        "opposition": "vs Stamina + Tolerance",
        "description": "Use a lock of hair or sympathetic link to hang a curse over a living victim for a month. Trigger the curse to cause enough lethal damage to fill the victim's Health.",
        "book": "Secrets of the Covenants p.185"
    }
}

CRUAC_RANK_3 = {
    "curse_of_aphrodites_favor": {
        "name": "Curse of Aphrodite's Favor",
        "type": "cruac",
        "rank": 3,
        "target_number": 6,
        "opposition": "vs Composure + Tolerance",
        "description": "Concoct enough potion for three drops to feed a victim over three nights, inflicting a Vinculum to another chosen subject.",
        "book": "Secrets of the Covenants p.185"
    },
    "curse_of_the_beloved_toy": {
        "name": "Curse of the Beloved Toy",
        "type": "cruac",
        "rank": 3,
        "target_number": 6,
        "opposition": "-",
        "description": "Slay a victim and trap their soul in a keepsake of theirs, rendering it a cursed item which expends the sorcerous Vitae to plague owners with dramatic failures.",
        "book": "Secrets of the Covenants p.185"
    },
    "deflection_of_wooden_doom": {
        "name": "Deflection of Wooden Doom",
        "type": "cruac",
        "rank": 3,
        "target_number": 6,
        "opposition": "-",
        "description": "Caster becomes immune to staking for one night.",
        "book": "VTR 2e p.153"
    },
    "donning_the_beasts_flesh": {
        "name": "Donning the Beast's Flesh",
        "type": "cruac",
        "rank": 3,
        "target_number": 7,
        "opposition": "-",
        "description": "Flay a beast and craft its skin into a garment. Spend Vitae while wearing the skin to approximate the beast's form.",
        "book": "Secrets of the Covenants p.184"
    },
    "mantle_of_the_glorious_dervish": {
        "name": "Mantle of the Glorious Dervish",
        "type": "cruac",
        "rank": 3,
        "target_number": 5,
        "opposition": "-",
        "description": "Dance to exhaustion. Until sunrise, the caster gains a point of armor against all attacks, cannot be ambushed or surprised, and deals an extra point of damage when striking.",
        "book": "Secrets of the Covenants p.185"
    },
    "touch_of_the_morrigan": {
        "name": "Touch of the Morrigan",
        "type": "cruac",
        "rank": 3,
        "target_number": 6,
        "opposition": "-",
        "description": "Prepare a deadly touch to inflict Potency in lethal damage within the night.",
        "book": "VTR 2e p.153"
    }
}

CRUAC_RANK_4 = {
    "blood_blight": {
        "name": "Blood Blight",
        "type": "cruac",
        "rank": 4,
        "target_number": 8,
        "opposition": "vs Stamina + Tolerance",
        "description": "Inflict Potency in lethal damage or Vitae loss by scouring blood, often provoking frenzy.",
        "book": "VTR 2e p.153"
    },
    "blood_price": {
        "name": "Blood Price",
        "type": "cruac",
        "rank": 4,
        "target_number": 8,
        "opposition": "vs Composure + Tolerance",
        "description": "Steal up to Potency in ingested Vitae from a present vampire or ghoul victim for the night.",
        "book": "VTR 2e p.153"
    },
    "bounty_of_the_storm": {
        "name": "Bounty of the Storm",
        "type": "cruac",
        "rank": 4,
        "target_number": 10,
        "opposition": "-",
        "description": "Consume a precious item to prepare a storm that awaits a crowd to strike, dealing your Cruac in bashing damage to the victim and slaying a third of the rest, leaving behind massive wealth. Risk detachment at Humanity 2.",
        "book": "Secrets of the Covenants p.185"
    },
    "feeding_the_crone": {
        "name": "Feeding the Crone",
        "type": "cruac",
        "rank": 4,
        "target_number": 10,
        "opposition": "-",
        "description": "Deal aggravated damage with your bite, but ingest no Vitae, until sunrise. End early by spending Vitae.",
        "book": "VTR 2e p.153"
    },
    "gorgons_gaze": {
        "name": "Gorgon's Gaze",
        "type": "cruac",
        "rank": 4,
        "target_number": 7,
        "opposition": "-",
        "description": "Roll Presence + Occult + Cruac - Stamina against the first person to see your eyes, petrifying a fifth of their body per success. Petrified Kindred may heal petrifications as severe damage.",
        "book": "Secrets of the Covenants p.185"
    },
    "manananggals_working": {
        "name": "Manananggal's Working",
        "type": "cruac",
        "rank": 4,
        "target_number": 8,
        "opposition": "-",
        "description": "Elder rite. Dismember yourself, willfully animating the severed body parts independently for the night.",
        "book": "Thousand Years p.78"
    },
    "mantle_of_the_predator_goddess": {
        "name": "Mantle of the Predator Goddess",
        "type": "cruac",
        "rank": 4,
        "target_number": 8,
        "opposition": "-",
        "description": "Dance to exhaustion. Add Cruac as a feeding bonus and as bonus Herd dots. Any character fed from gains the Raptured Condition.",
        "book": "Secrets of the Covenants p.186"
    },
    "quicken_the_withered_womb": {
        "name": "Quicken the Withered Womb",
        "type": "cruac",
        "rank": 4,
        "target_number": 8,
        "opposition": "-",
        "description": "Guarantee fertile conception when coupling for the night.",
        "book": "Half-Damned p.14"
    },
    "the_red_blossoms": {
        "name": "The Red Blossoms",
        "type": "cruac",
        "rank": 4,
        "target_number": 6,
        "opposition": "-",
        "description": "Causes plants to grow into an archway to enter the Hedge.",
        "book": "Hedge p.34"
    },
    "willful_vitae": {
        "name": "Willful Vitae",
        "type": "cruac",
        "rank": 4,
        "target_number": 7,
        "opposition": "-",
        "description": "Prevent the onset of blood addiction or the Vinculum for the night.",
        "book": "VTR 2e p.153"
    }
}

CRUAC_RANK_5 = {
    "birthing_the_god": {
        "name": "Birthing the God",
        "type": "cruac",
        "rank": 5,
        "target_number": 15,
        "opposition": "-",
        "description": "Gather body parts to violently birth an undead flesh-eating god with Size a fifth of the Vitae used, Blood Potency a third of the Vitae, and one Skill rating inherited from each celebrant. Spend used Vitae to assign the god dots of Attributes and Disciplines.",
        "book": "Secrets of the Covenants p.186"
    },
    "denying_hades": {
        "name": "Denying Hades",
        "type": "cruac",
        "rank": 5,
        "target_number": 8,
        "opposition": "-",
        "description": "Disgorge Vitae and suffer a point of aggravated damage to trap a deceased spirit in its days-old body, hung between life and death.",
        "book": "Secrets of the Covenants p.186"
    },
    "gwydions_curse": {
        "name": "Gwydion's Curse",
        "type": "cruac",
        "rank": 5,
        "target_number": 10,
        "opposition": "-",
        "description": "Elder rite. Animate plants and trees for a yard per Potency for the night, which roll your Blood Potency to attack and can spend the rite's Vitae to heal themselves.",
        "book": "Thousand Years p.78"
    },
    "mantle_of_the_crone": {
        "name": "Mantle of the Crone",
        "type": "cruac",
        "rank": 5,
        "target_number": 10,
        "opposition": "-",
        "description": "Dance to exhaustion. For the night, inflict Primeval Truths with your visage, and aggravated damage with your touch. Spend Willpower to transmute objects into animals temporarily.",
        "book": "Secrets of the Covenants p.186"
    },
    "scapegoat": {
        "name": "Scapegoat",
        "type": "cruac",
        "rank": 5,
        "target_number": 12,
        "opposition": "- Resolve",
        "description": "Elder rite. Feed the ritual Vitae to a mortal vessel. For one night, the mortal suffers any breaking points or inured banes, not you.",
        "book": "Thousand Years p.78"
    }
}

ALL_CRUAC = {
    **CRUAC_RANK_1,
    **CRUAC_RANK_2,
    **CRUAC_RANK_3,
    **CRUAC_RANK_4,
    **CRUAC_RANK_5
}

CRUAC_BY_RANK = {
    1: CRUAC_RANK_1,
    2: CRUAC_RANK_2,
    3: CRUAC_RANK_3,
    4: CRUAC_RANK_4,
    5: CRUAC_RANK_5
}

# Bloodline-Specific Cruac (Penumbrae)
PENUMBRAE_CRUAC = {
    "sanguine_augur": {
        "name": "Sanguine Augur",
        "type": "cruac",
        "bloodline": "penumbrae",
        "rank": 1,
        "target_number": 6,
        "opposition": "-",
        "description": "Dream cryptic revelations about the last vessel you fed from. Spend Vitae to broaden or clarify the vision.",
        "book": "Night Horrors: Shunned by the Moon p.40"
    },
    "wisdom_of_the_blood": {
        "name": "Wisdom of the Blood",
        "type": "cruac",
        "bloodline": "penumbrae",
        "rank": 3,
        "target_number": 6,
        "opposition": "-",
        "description": "Read prophecies about a subject in the dreams of a torpid vampire.",
        "book": "Night Horrors: Shunned by the Moon p.40"
    },
    "clothos_skein": {
        "name": "Clotho's Skein",
        "type": "cruac",
        "bloodline": "penumbrae",
        "rank": 5,
        "target_number": 9,
        "opposition": "vs Resolve + Tolerance",
        "description": "Dreamwalk the threads connecting Kindred through the daysleep to implant a suggestion in a vampire's sleep.",
        "book": "Night Horrors: Shunned by the Moon p.40"
    }
}

# ==================== BLOODLINE-SPECIFIC DEVOTIONS ====================

# Khaibit Bloodline Devotions (Obtenebration)
KHAIBIT_DEVOTIONS = {
    "udjat": {
        "name": "Udjat",
        "type": "devotion",
        "bloodline": "khaibit",
        "prerequisites": "-",
        "xp_cost": "-",
        "cost": "(●)",
        "description": "You can see in total darkness and can't be blinded by injury or supernatural imposition. Spend Vitae to perceive beings in Twilight for one scene, during which you can't be possessed by strix.",
        "book": "Onyx Path blog"
    },
    "ba": {
        "name": "Ba",
        "type": "devotion",
        "bloodline": "khaibit",
        "prerequisites": "Obfuscate:2",
        "xp_cost": 2,
        "cost": "●●●",
        "description": "Grasp a shadow large enough to contain you and don it, becoming darkness yourself. You're treated as a being in Twilight, able to touch (and be touched by) anything else in Twilight. Half your Speed and, whenever you're hurt, take an extra two lethal damage in this state. The Ba offers no protection against fire or sunlight.",
        "book": "Onyx Path blog"
    },
    "iteru": {
        "name": "Iteru",
        "type": "devotion",
        "bloodline": "khaibit",
        "prerequisites": "Celerity ••",
        "xp_cost": 2,
        "cost": "●",
        "description": "Slip reflexively into a shadow and back out of any contiguous shadow. Once per scene, using the Iteru can grant the rote quality to a Dodge.",
        "book": "Onyx Path blog"
    },
    "pseshkf": {
        "name": "Pseshkf",
        "type": "devotion",
        "bloodline": "khaibit",
        "prerequisites": "Vigor:2",
        "xp_cost": 2,
        "cost": "●+",
        "description": "Coat an object in frozen darkness. Add Blood Potency to its Durability and Vitae spent to its Structure. Coated weapons add one to their weapon rating against physical targets, and apply a weapon rating equal to your Blood Potency to the noncorporeal. You can wield a coated object at a distance through the Tyet, even while immaterial through the Ba.",
        "book": "Onyx Path blog"
    },
    "tyet": {
        "name": "Tyet",
        "type": "devotion",
        "bloodline": "khaibit",
        "prerequisites": "Vigor:2",
        "xp_cost": 2,
        "cost": "●+",
        "description": "Expel darkness out for your Blood Potency times Vitae spent, in yards. You can shape the cloud of shadow, including preexisting shadows within the space of the cloud.",
        "book": "Onyx Path blog"
    }
}

# Nosoi Bloodline Devotions
NOSOI_DEVOTIONS = {
    "infectious_bite": {
        "name": "Infectious Bite",
        "type": "devotion",
        "bloodline": "nosoi",
        "prerequisites": "-",
        "xp_cost": "-",
        "cost": "●",
        "description": "Contest Manipulation + Medicine + Protean vs Stamina + Supernatural Tolerance to infect a mortal with your blood sickness.",
        "book": "Night Horrors: Shunned by the Moon p.32"
    },
    "plague_doctors_mask": {
        "name": "Plague Doctor's Mask",
        "type": "devotion",
        "bloodline": "nosoi",
        "prerequisites": "Obfuscate:2",
        "xp_cost": 1,
        "cost": "●",
        "description": "Use Touch of Shadow to mask the symptoms of a blood sickness.",
        "book": "Night Horrors: Shunned by the Moon p.32"
    },
    "tiny_guardian": {
        "name": "Tiny Guardian",
        "type": "devotion",
        "bloodline": "nosoi",
        "prerequisites": "Protean:3",
        "xp_cost": 1,
        "cost": "●/bug",
        "description": "Requires Swarm Form. Bud off intelligent, loyal insect servants.",
        "book": "Night Horrors: Shunned by the Moon p.32"
    }
}

# Scions of the First City Devotions
SCIONS_DEVOTIONS = {
    "city_attunement": {
        "name": "City Attunement",
        "type": "devotion",
        "bloodline": "scions",
        "prerequisites": "-",
        "xp_cost": "-",
        "cost": "●",
        "description": "Touch hands with the surface of your city to see through its eyes. This is required to use other Scion Devotions in a particular city.",
        "book": "Night Horrors: Shunned by the Moon p.44"
    },
    "incriminating_evidence": {
        "name": "Incriminating Evidence",
        "type": "devotion",
        "bloodline": "scions",
        "prerequisites": "Auspex:3",
        "xp_cost": 1,
        "cost": "(●)",
        "description": "Roll Wits + Empathy + Auspex to search your city for clues of wrongdoing by a touched subject. Use for free once each scene.",
        "book": "Night Horrors: Shunned by the Moon p.44"
    },
    "our_mothers_mind": {
        "name": "Our Mother's Mind",
        "type": "devotion",
        "bloodline": "scions",
        "prerequisites": "Auspex:5",
        "xp_cost": 3,
        "cost": "●●",
        "description": "Walk barefoot through your city and contest Intelligence + Occult + Auspex vs Resolve + Tolerance to seek and impede quarry.",
        "book": "Night Horrors: Shunned by the Moon p.44"
    }
}

# Lidérc (Siphon) Bloodline Devotions
LIDERC_DEVOTIONS = {
    "the_give_and_take": {
        "name": "The Give-and-Take",
        "type": "devotion",
        "bloodline": "liderc",
        "prerequisites": "Celerity or Vigor:3",
        "xp_cost": 1,
        "cost": "●●",
        "description": "Gift a feeding vessel with two dots of your Physical Disciplines for a night, but steal any Willpower they recover from Vice.",
        "book": "Night Horrors: Shunned by the Moon p.27"
    },
    "the_look": {
        "name": "The Look",
        "type": "devotion",
        "bloodline": "liderc",
        "prerequisites": "Majesty:2",
        "xp_cost": 1,
        "cost": "○",
        "description": "Use exceptional success to provoke emotion to psychically drain Vitae from a victim's will.",
        "book": "Night Horrors: Shunned by the Moon p.27"
    },
    "the_one_that_got_away": {
        "name": "The One That Got Away",
        "type": "devotion",
        "bloodline": "liderc",
        "prerequisites": "Obfuscate:4",
        "xp_cost": 2,
        "cost": "●",
        "description": "By feeding on a sleeping victim, conflate yourself with their ideal, inflicting yourself as a temporary Vice.",
        "book": "Night Horrors: Shunned by the Moon p.27"
    },
    "the_pledge": {
        "name": "The Pledge",
        "type": "devotion",
        "bloodline": "liderc",
        "prerequisites": "Majesty:2",
        "xp_cost": 1,
        "cost": "○",
        "description": "Pledge yourself to a consenting vessel. They gain your Majesty in fawning Social Merits, and you recover Willpower from rousing their passion, but cannot target anyone else with Siphon.",
        "book": "Night Horrors: Shunned by the Moon p.27"
    }
}

# Vardyvle Bloodline Devotions
VARDYVLE_DEVOTIONS = {
    "shapeshifting": {
        "name": "Shapeshifting",
        "type": "devotion",
        "bloodline": "vardyvle",
        "prerequisites": "Protean:2, Obfuscate:1",
        "xp_cost": 1,
        "cost": "●/feature",
        "description": "Copy features from the appearance of a vessel for a night.",
        "book": "Night Horrors: Shunned by the Moon p.49"
    }
}

# All bloodline-specific devotions
ALL_BLOODLINE_DEVOTIONS_EXTENDED = {
    **KHAIBIT_DEVOTIONS,
    **NOSOI_DEVOTIONS,
    **SCIONS_DEVOTIONS,
    **LIDERC_DEVOTIONS,
    **VARDYVLE_DEVOTIONS
}

# Helper functions
def get_scales_by_mystery(mystery_name=None):
    """Get Scales of the Dragon by mystery."""
    if mystery_name:
        mystery_name = mystery_name.lower().replace(" ", "_")
        return SCALES_BY_MYSTERY.get(mystery_name, {})
    return ALL_SCALES


def get_all_scales():
    """Get all Scales of the Dragon."""
    return ALL_SCALES


def get_theban_by_rank(rank=None):
    """Get Theban Sorcery miracles by rank."""
    if rank:
        return THEBAN_BY_RANK.get(rank, {})
    return ALL_THEBAN


def get_all_theban():
    """Get all Theban Sorcery miracles."""
    return ALL_THEBAN


def get_cruac_by_rank(rank=None):
    """Get Cruac rites by rank."""
    if rank:
        return CRUAC_BY_RANK.get(rank, {})
    return ALL_CRUAC


def get_all_cruac():
    """Get all Cruac rites."""
    return ALL_CRUAC


def get_ritual_power(power_key):
    """Get any ritual power (Scale, Theban, or Cruac) by key."""
    power_key = power_key.lower().replace(" ", "_")
    # Check Scales
    if power_key in ALL_SCALES:
        return ALL_SCALES[power_key]
    # Check Theban
    if power_key in ALL_THEBAN:
        return ALL_THEBAN[power_key]
    # Check Cruac
    if power_key in ALL_CRUAC:
        return ALL_CRUAC[power_key]
    # Check Penumbrae
    if power_key in PENUMBRAE_CRUAC:
        return PENUMBRAE_CRUAC[power_key]
    # Check bloodline devotions
    if power_key in ALL_BLOODLINE_DEVOTIONS_EXTENDED:
        return ALL_BLOODLINE_DEVOTIONS_EXTENDED[power_key]
    return None


def get_bloodline_devotion(bloodline_name):
    """Get devotions for a specific bloodline."""
    bloodline_map = {
        "khaibit": KHAIBIT_DEVOTIONS,
        "nosoi": NOSOI_DEVOTIONS,
        "scions": SCIONS_DEVOTIONS,
        "liderc": LIDERC_DEVOTIONS,
        "vardyvle": VARDYVLE_DEVOTIONS
    }
    return bloodline_map.get(bloodline_name.lower().replace(" ", "_"), {})


def get_all_bloodline_devotions():
    """Get all bloodline-specific devotions."""
    return ALL_BLOODLINE_DEVOTIONS_EXTENDED
