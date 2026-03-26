"""
Group-specific merits, numina, and other data for Chronicles of Darkness.

This module contains definitions for group-specific merits and abilities,
particularly for Packs (Werewolf), Krewes (Geist), Cults (Mummy),
Mystery Cults (Mortal/Mage), and Cells (Hunter).
"""

# Pack Merits (Werewolf: The Forsaken)
PACK_MERITS = {
    'Den': {
        'min': 1,
        'max': 5,
        'prerequisites': ['Pack'],
        'description': 'An enclosed physical location for Packs to relax and feel safe',
        'source': 'Pack 29'
    },
    'Directed Rage': {
        'min': 3,
        'max': 5,
        'prerequisites': ['Pack'],
        'description': 'Packs have found a way to direct their Rage-filled members anger at foes rather than friends',
        'effects': {
            3: 'Packmates suffering Wasu-Im act as if they were one step closer to harmony for control time',
            4: 'Characters in Basu-Im may roll Resolve + Composure to prioritize attacking non-pack members',
            5: "Characters won't target or pursue packmates so long as they aren't a threat and roll Resolve + Composure to ignore innocents"
        },
        'source': 'Pack 30'
    },
    'Magnanimous Totem': {
        'min': 2,
        'max': 4,
        'prerequisites': ['Pack'],
        'description': 'Allows non-Uratha to take Totem merit',
        'effects': {
            2: 'Wolf-Blooded may take up to 5 dots in the Totem merit',
            3: 'Humans may take 1 dot of Totem',
            4: 'Humans may take up to 5 dots of Totem'
        },
        'source': 'Pack 30'
    },
    'Moon\'s Grace': {
        'min': 3,
        'max': 5,
        'prerequisites': ['Pack', 'Wolf-Blooded and Humans only'],
        'description': 'Allows non-Uratha pack members to use werewolf abilities',
        'effects': {
            3: 'Pack may learn to use Pack Tactics as if they were Uratha',
            4: 'Any member of the Pack may learn and lead Wolf Rites as if they were a Werewolf',
            5: 'Pack members may gain Renown and receive Shadow and Wolf Gifts from spirits, spending Willpower instead of Essence'
        },
        'note': 'Cannot be taken if an Uratha is part of the Pack at 5 dots',
        'source': 'Pack 31'
    },
    'Territorial Advantage': {
        'min': 1,
        'max': 5,
        'prerequisites': ['Pack'],
        'description': 'Packs may leverage familiarity with their territory to inflict Conditions or Tilts on intruders',
        'mechanics': 'Roll Attribute + Skill + Merit Dots vs Attribute + the same Skill',
        'source': 'Pack 31'
    }
}

# Krewe Merits (Geist: The Sin-Eaters)
# Krewes have both living and ghostly celebrants
KREWE_MERITS = {
    'Krewe Allies': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'You have influence and goodwill with a chosen group proportional to your dots in this Merit. Each session, you can call on your Allies for favors of a value rated 1 to 5 by the Storyteller, up to your rating in the Merit',
        'source': 'GTS 2e 85'
    },
    'Cenote': {
        'min': 1,
        'max': 5,
        'prerequisites': ['Safe Place'],
        'description': 'You tend a ghostly place where Plasm accumulates, at your Merit rating in points per chapter',
        'source': 'GTS 2e 85'
    },
    'Krewe Contacts': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'Choose a group or field for each dot of Contacts. You can roll Manipulation + (relevant Social Skill) to gather information or dirt from acquaintances in any of these groups or fields',
        'source': 'GTS 2e 86'
    },
    'Good Time Management': {
        'min': 1,
        'max': 1,
        'prerequisites': ['Academics 2 or Science 2'],
        'description': 'Make extended action rolls in half the necessary time. Krewe actions cost one less Effort, to a minimum of one Effort',
        'source': 'GTS 2e 86'
    },
    'Holy Acquaintances': {
        'min': 1,
        'max': 4,
        'prerequisites': [],
        'description': 'You have friends in the Church. Use requires a successful Presence + Social roll. Every dot gives an additional +2 to influencing people',
        'source': 'DE2 274'
    },
    'Immediate Disappearance': {
        'min': 1,
        'max': 3,
        'prerequisites': [],
        'description': 'Allow your krewe to disappear to the Underworld from one place. All people they\'ve met within the last three days forget them and pursuers stop looking for them temporarily. Requires a successful Dexterity + Stealth roll. Every additional dot increases the time pursuers stop looking for the krewe',
        'source': 'DE2 275'
    },
    'Krewe Library': {
        'min': 1,
        'max': 3,
        'prerequisites': [],
        'description': 'You have a cache of information relating to a particular Skill. Add your dots in Library to relevant extended rolls',
        'source': 'GTS 2e 86'
    },
    'Krewe Resources': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'You have disposable income proportional to your dots in this Merit. Once per session, you can securely procure an item or service with an Availability that doesn\'t exceed your Resources rating',
        'source': 'GTS 2e 88'
    },
    'Krewe Safe Place': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'You\'ve secured a place from intrusion. Apply your Safe Place rating as an Initiative bonus while there, and a penalty to break in. With Crafts you can install traps, forcing intruders to roll Dexterity + Larceny - Safe Place to avoid up to your Safe Place in lethal damage',
        'source': 'GTS 2e 88'
    },
    'Krewe Status': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'You have influence with a chosen group. You can draw on their facilities and resources, block the use of a relevant Social Merit lower than your Status rating once per session, and apply Status as a die bonus to Social rolls drawing on your influence',
        'source': 'GTS 2e 89'
    },
    'Supernatural Membership': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'Distribute twice your dots in this Merit as Supernatural Merit dots among your krewe\'s living celebrants',
        'source': 'GTS 2e 89'
    }
}

# Krewe Celebrant Information
# Krewes consist of both living and ghostly members
KREWE_CELEBRANT_INFO = {
    'ghostly_celebrants': {
        'description': 'Dead members who didn\'t get a second chance at life',
        'rank': 2,
        'attributes': 9,  # 9 dots to distribute between Power, Finesse, Resistance
        'manifestations': 1,  # Plus Twilight Form for free
        'influences': 2,  # 2 dots of Influences over their Anchors
        'numina': 3,  # 3 Numina
        'aspirations': 2,
        'anchors': 2,  # One is always their remains, one can be person/place/thing
        'virtue_vice': True
    },
    'living_celebrants': {
        'description': 'Living members of the krewe',
        'dice_pools': 3,  # Three actions with ratings of 5, 4, and 3 dice
        'base_pool': 2,  # Other actions use 2 dice
        'aspiration': 1,
        'concept': True,
        'supernatural_merits': 'Via Supernatural Membership Merit only'
    }
}

# Cult Merits (Mummy: The Curse)
# These are cult-specific merits (prefix with "Cult" to differentiate from individual merits)
CULT_MERITS = {
    'Cult Allies': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 108'
    },
    'Cult Contacts': {
        'min': 1,
        'max': 1,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 109'
    },
    'Devotees': {
        'min': 3,
        'max': 3,
        'prerequisites': [],
        'description': 'The cult has a bonus dot of Fidelity',
        'source': 'MTC 2e 110'
    },
    'Fanatical': {
        'min': 2,
        'max': 2,
        'prerequisites': [],
        'description': 'When you take more cult actions than your Dominance permits, overextended actions apply a +2 bonus to Reach and Grasp, but inflict additional Fidelity damage',
        'source': 'MTC 2e 111'
    },
    'Forbidden Rites': {
        'min': 1,
        'max': 5,
        'prerequisites': ['Ritual Sorcerer', 'Library (Occult) 2', 'Sorcerous Knowledge'],
        'description': 'As the supernatural Merit. Cultists led by a sorcerer may perform the rites as cult actions',
        'source': 'MTC 2e 117'
    },
    'Cult Library': {
        'min': 1,
        'max': 3,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 112'
    },
    'Observance': {
        'min': 2,
        'max': 2,
        'prerequisites': [],
        'description': 'Monthly tomb rites inspire cultists and cult actions. Participating mummies recover Willpower',
        'source': 'MTC 2e 112'
    },
    'Cult Resources': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 113'
    },
    'Cult Retainer': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 113'
    },
    'Ritualistic Cult': {
        'min': 1,
        'max': 1,
        'prerequisites': [],
        'description': 'The cult maintains a schedule of tomb rituals. Add Dominance as a bonus to restore Pillars through the tomb\'s Lifeweb',
        'source': 'MTC 2e 114'
    },
    'Cult Safe Place': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the location Merit, but for the cult',
        'source': 'MTC 2e 114'
    },
    'Scapegoats': {
        'min': 1,
        'max': 1,
        'prerequisites': [],
        'description': 'Once per story, the cult may resolve a mutiny by refocusing to a new cult action, healing two Fidelity wounds without sacrificing Reach or Grasp',
        'source': 'MTC 2e 114'
    },
    'Scorpion Cult Initiation': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the style Merit',
        'source': 'MTC 2e 114'
    },
    'Secretive': {
        'min': 3,
        'max': 3,
        'prerequisites': [],
        'description': 'Cultists hide their identities from the less initiated. Investigating a cultist\'s ties requires additional clues equal to their Scorpion Cult Initiation',
        'source': 'MTC 2e 115'
    },
    'Specialized Cultists': {
        'min': 1,
        'max': 1,
        'prerequisites': [],
        'description': 'Cult assistance provides 9-Again to a given Skill',
        'source': 'MTC 2e 115'
    },
    'Storied': {
        'min': 1,
        'max': 1,
        'prerequisites': [],
        'description': 'The cult is deniable or implausible, providing a +1 bonus to discredit enemies',
        'source': 'MTC 2e 115'
    },
    'Cult Staff': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 115'
    },
    'Cult Status': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 116'
    },
    'Syncretic': {
        'min': 1,
        'max': 1,
        'prerequisites': [],
        'description': 'The cult incorporates local beliefs, providing a +2 cult action bonus to work alongside believers',
        'source': 'MTC 2e 116'
    },
    'Vice-Ridden': {
        'min': 2,
        'max': 2,
        'prerequisites': ['Vice'],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 116'
    },
    'Virtuous': {
        'min': 2,
        'max': 2,
        'prerequisites': ['Virtue'],
        'description': 'As the universal Merit, but for the cult',
        'source': 'MTC 2e 116'
    },
    'Wayward Cult': {
        'min': 3,
        'max': 3,
        'prerequisites': [],
        'description': 'The cult maintains no Iremite faith or loyalty and is deceived as to the nature of their Arisen master. It has no Judge\'s Doctrine, though it can sacrifice Dominance to develop a third Doctrine of its own. Its Reach and Grasp gain a +2 bonus to block other cults, but the first attack by a rival cult under a mummy\'s leadership inflicts aggravated Fidelity damage',
        'source': 'MTC 2e 116'
    }
}

# Mystery Cult Merits (Mortal/Mage)
# Mystery Cults provide benefits at each level of initiation
MYSTERY_CULT_MERITS = {
    'Mystery Cult Initiation': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'Membership and rank within a Mystery Cult',
        'effects': {
            1: 'A Skill Specialty or one-dot Merit, pertaining to the lessons taught to initiates',
            2: 'A one-dot Merit',
            3: 'A Skill dot, or a two-dot Merit (often a supernatural Merit)',
            4: 'A three-dot Merit, often supernatural in origin',
            5: 'A three-dot Merit, or a major advantage not reflected in game traits'
        },
        'source': 'CofD'
    }
}

# Example Mystery Cults for reference
EXAMPLE_MYSTERY_CULTS = {
    'Chosen of Mammon': {
        'description': 'Followers of Mammon obtain material wealth and power at any cost',
        'benefits': {
            1: 'Politics Specialty in Bureaucracy',
            2: 'Language Merit (Aramaic)',
            3: 'Two dots between Contacts, Allies, Resources, or Retainers',
            4: 'Thief of Fate (4) Merit',
            5: 'Three dots of Resources plus one Resources 5 purchase per month from cult coffers'
        }
    },
    'Sisters of the Machine Gun, Brothers of the Bomb': {
        'description': 'Fight against the God-Machine with repurposed artifacts and technology',
        'benefits': {
            1: 'Occult Specialty in The God-Machine',
            2: 'Contacts - (Brothers and Sisters)',
            3: 'Can repurpose holy artifacts into weapons that hurt spirits and ghosts',
            4: 'Three dots in Retainers (wards and students)',
            5: 'Modified Encyclopedic Knowledge Merit relating to the God-Machine'
        }
    }
}

# Cell Merits (Hunter: The Vigil)
CELL_MERITS = {
    'Safe Place': {
        'min': 1,
        'max': 5,
        'prerequisites': ['Cell'],
        'description': 'A secure location for the cell to operate from',
        'source': 'HTV'
    }
}

# Cell Tactics (Hunter: The Vigil 2e)
# Cells are focused around tactical coordination
CELL_TACTICS = {
    # Investigation Tactics
    'Field Medicine': {
        'requirements': 'Primary actor: Medicine 2. Target\'s rightmost Health box must be filled with lethal damage',
        'primary_pool': 'Dexterity + Medicine',
        'secondary_pools': [
            'Dexterity + Medicine (0/2)',
            'Strength + Brawl or Weaponry, or Dexterity + Firearms (1/2)',
            'Dexterity + Stealth (0/2)'
        ],
        'description': 'Patch up an ally so they don\'t die right away',
        'source': 'TTF 8',
        'type': 'investigation'
    },
    'Identification': {
        'requirements': 'Occult 2 (Primary)',
        'primary_pool': 'Intelligence + Occult vs. Manipulation + Subterfuge + Potency',
        'secondary_pools': [
            'Wits + Investigation (0/3)',
            'Wits + Stealth (0/1)',
            'Wits + Occult (0/3)'
        ],
        'description': 'Identify if a target is supernatural, becoming Informed. At least one secondary actor must roll Investigation or Stealth',
        'source': 'HTV 2e 155',
        'type': 'investigation'
    },
    'Monster Lore': {
        'requirements': 'A specific type of monster, Relevant Social Merit 2 (Secondary)',
        'primary_pool': 'Intelligence + Occult',
        'secondary_pools': [
            'Presence or Manipulation + Socialize (0/3)',
            'Resolve + Academics or Investigation or Computer (1/3)',
            'Strength or Presence + Intimidation or Streetwise (0/2)'
        ],
        'description': 'Learn a single weakness, common power, and piece of information on the origin of a monster type. Primary actor becomes Informed',
        'source': 'HTV 2e 156',
        'type': 'investigation'
    },
    'Profiling': {
        'requirements': 'Investigation 2, Empathy 2 (Primary), Skill rolled 2 (Secondary)',
        'primary_pool': 'Intelligence + Investigation vs. Wits + Subterfuge or Investigation + Potency',
        'secondary_pools': [
            'Presence or Manipulation + Persuasion (0/2)',
            'Intelligence + Computer (0/2)',
            'Wits + Stealth or Expression (0/1)',
            'Intelligence + Academics or Occult (1/3)'
        ],
        'description': 'Learn a monster\'s Potency, one mental or social trait rating, human guise and any Anchors and Aspirations',
        'source': 'HTV 2e 156',
        'type': 'investigation'
    },
    'Sweep': {
        'requirements': '',
        'primary_pool': 'Wits + Composure vs. Wits + Stealth + Potency',
        'secondary_pools': [
            'Strength + Athletics or Dexterity + Larceny (1/5)',
            'Wits + Investigation or Survival (0/5)'
        ],
        'description': 'Search a location, finding any traps or ambushers, gaining a bonus to investigating the area if there are none',
        'source': 'HTV 2e 157',
        'type': 'investigation'
    },
    
    # Physical Tactics
    'Called Shot': {
        'requirements': '',
        'primary_pool': 'Strength + Weaponry or Dexterity + Firearms - target\'s Defense',
        'secondary_pools': [
            'Manipulation + Persuasion or Subterfuge (1/2)',
            'Strength + Brawl (1/2)'
        ],
        'description': 'While taking a called shot penalty, the primary actor attacks with +1 weapon modifier and inflicts a tilt and initiative penalty',
        'source': 'HTV 2e 157',
        'type': 'physical'
    },
    'Capture': {
        'requirements': '',
        'primary_pool': 'Dexterity + Survival or Crafts vs. Dexterity or Strength + Athletics or Brawl + Potency',
        'secondary_pools': [
            'Wits + Athletics (1/3)',
            'Strength + Brawl (1/3)'
        ],
        'description': 'Immobilize a target, penalizing any attempts to break free',
        'source': 'HTV 2e 157',
        'type': 'physical'
    },
    'Controlled Immolation': {
        'requirements': '',
        'primary_pool': 'Stamina + Athletics or Firearms vs. Stamina + Athletics + Potency',
        'secondary_pools': [
            'Wits + Brawl or Weaponry (1/4)',
            'Wits + Survival or Science (1/5)'
        ],
        'description': 'For every turn the Cell continues to roll and succeed, the target is burning and Blinded, and the fire does not spread elsewhere',
        'source': 'HTV 2e 158',
        'type': 'physical'
    },
    'Corral': {
        'requirements': '',
        'primary_pool': 'Strength or Manipulation + Intimidation vs. Composure + Empathy + Potency',
        'secondary_pools': [
            'Wits + Composure (1/5)',
            'Manipulation + Subterfuge or Survival (1/3)'
        ],
        'description': 'Herd a target to a specific location',
        'source': 'HTV 2e 158',
        'type': 'physical'
    },
    'Harvest': {
        'requirements': 'Occult 2 (Any), Specialty related to the target\'s type (Any)',
        'primary_pool': 'Dexterity + Medicine vs. Strength + Athletics or Brawl + Potency',
        'secondary_pools': [
            'Strength + Brawl (1/3)',
            'Intelligence + Occult (1/2)'
        ],
        'description': 'Extract a sample from the target for every turn of success. If the target\'s type has been studied before, the Occult roll is not necessary',
        'source': 'HTV 2e 159',
        'type': 'physical'
    },
    'Infiltration': {
        'requirements': 'Primary actor: Stealth 3+. Secondary actors: 2+ in Skills used for this Tactic',
        'primary_pool': 'Wits + Composure vs. Wits + Composure + Potency',
        'secondary_pools': [
            'Dexterity + Stealth (1/5)',
            'Presence + Expression or Intimidation (1)'
        ],
        'description': 'The primary actor enters the monster\'s inner sanctum. She may make up to 3 Investigation, Larceny, or Occult rolls before needing to exit',
        'source': 'TTF 8',
        'type': 'physical'
    },
    'Lure': {
        'requirements': 'Occult 2 (Any), Enticing agent',
        'primary_pool': 'Wits + Composure vs. Wits + Composure + Potency',
        'secondary_pools': [
            'Presence + Persuasion or Subterfuge (1)',
            'Manipulation + Occult or Streetwise (1/2)',
            'Dexterity + Larceny (0/2)'
        ],
        'description': 'Lure a target in, Surprising it',
        'source': 'HTV 2e 159',
        'type': 'physical'
    },
    'Scatter': {
        'requirements': '',
        'primary_pool': 'Wits + Composure vs. Wits + Composure + Potency',
        'secondary_pools': [
            'Dexterity + Stealth (1/5)',
            'Presence + Expression or Intimidation (1)'
        ],
        'description': 'While someone distracts the target, all others escape the scene and the Primary actor becomes Informed on the target',
        'source': 'HTV 2e 159',
        'type': 'physical'
    },
    
    # Social Tactics
    'Adrenaline Rush': {
        'requirements': '',
        'primary_pool': 'Presence + Expression',
        'secondary_pools': [
            'Resolve + Occult (0/6)',
            'Resolve + Empathy (0/6)'
        ],
        'description': 'A Cell becomes immune to losing consciousness from Bashing damage, do not suffer wound penalties, and gain a bonus to resisting fear. At least one secondary action must be taken',
        'source': 'HTV 2e 160',
        'type': 'social'
    },
    'Bluff': {
        'requirements': 'Primary actor: Intimidation, Persuasion, or Socialize 3+',
        'primary_pool': 'Presence + Intimidation, Persuasion, or Socialize vs. Composure + Empathy + Potency of lead gatekeeper',
        'secondary_pools': [
            'Intelligence + Computer (0/1)',
            'Manipulation + Subterfuge vs. Composure + Empathy (1/5)',
            'Composure + Intimidation (1/3)'
        ],
        'description': 'The primary actor bluffs her way past any gatekeepers, convincing them that the target is expecting her, or that she\'s someone they\'d get in trouble for turning away',
        'source': 'TTF 9',
        'type': 'social'
    },
    'Expose': {
        'requirements': 'Knowledge of the target\'s identity',
        'primary_pool': 'Wits + Presence or Manipulation vs. Manipulation + Subterfuge + Potency',
        'secondary_pools': [
            'Wits + Investigation or Stealth (1/4)',
            'Wits + Socialize (1/3)'
        ],
        'description': 'The target is inflicted with the Leveraged or Notoriety Condition as they are blackmailed or publicly exposed',
        'source': 'HTV 2e 160',
        'type': 'social'
    },
    'Freeing Mind': {
        'requirements': 'Target must be supernaturally affected',
        'primary_pool': 'Manipulation + Intimidation or Subterfuge vs. subject\'s Composure + Resolve + monster\'s Potency',
        'secondary_pools': [
            'Presence + Persuasion or Empathy (1/2)',
            'Wits + Brawl or Weaponry or Intimidation (0/3, ND)'
        ],
        'description': 'Break or suppress a monster\'s power on the target, helping the subject permanently end any suppressed effect. Secondary actors using the Wits based pool prevent any interruptions or complications instead of adding dice to the primary actor\'s pool',
        'source': 'HTV 2e 160',
        'type': 'social'
    }
}

# Motley Merits (Changeling: The Lost)
# Note: Motleys are often linked to specific oaths (system not yet implemented)
MOTLEY_MERITS = {
    'Motley Hollow': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'A shared dwelling in the Hedge accessible to motley members',
        'source': 'CTL 2e'
    },
    'Motley Workshop': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'A shared workspace for crafting and repairs',
        'source': 'CTL 2e'
    },
    'Motley Token': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'A shared Token accessible to motley members',
        'source': 'CTL 2e'
    },
    'Stable Trod': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'A stable path through the Hedge known to the motley',
        'source': 'CTL 2e'
    },
    'Motley Allies': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the motley',
        'source': 'CTL 2e'
    },
    'Motley Contacts': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the motley',
        'source': 'CTL 2e'
    },
    'Motley Library': {
        'min': 1,
        'max': 3,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the motley',
        'source': 'CTL 2e'
    },
    'Motley Resources': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the motley',
        'source': 'CTL 2e'
    },
    'Motley Retainer': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the motley',
        'source': 'CTL 2e'
    },
    'Motley Safe Place': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the motley',
        'source': 'CTL 2e'
    },
    'Motley Staff': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the motley',
        'source': 'CTL 2e'
    },
    'Motley Status': {
        'min': 1,
        'max': 5,
        'prerequisites': [],
        'description': 'As the universal Merit, but for the motley',
        'source': 'CTL 2e'
    }
}

# Cabal Merits (Mage groups)
# Placeholder for future Mage-specific cabal merits
CABAL_MERITS = {
    # Add Mage cabal-specific merits here
}

# Map group types to their specific merits
GROUP_TYPE_MERITS = {
    'pack': PACK_MERITS,
    'krewe': KREWE_MERITS,
    'cult': CULT_MERITS,
    'mysterycult': MYSTERY_CULT_MERITS,
    'cabal': CABAL_MERITS,
    'cell': CELL_MERITS,
    'motley': MOTLEY_MERITS,
}

# Spirit Numina
SPIRIT_NUMINA = {
    # Standard Numina
    'Aggressive Meme': {
        'cost': '7 Essence',
        'action': 'Contested',
        'roll': 'vs Resolve + Composure + Tolerance',
        'description': 'Implant a contagious idea',
        'source': 'CofD 136'
    },
    'Awe': {
        'cost': '3 Essence',
        'action': 'Contested',
        'roll': 'vs Presence + Composure + Tolerance',
        'description': 'Momentarily incapacitate through dread',
        'source': 'CofD 136'
    },
    'Beast Eyes': {
        'cost': '1 Essence',
        'action': 'Instant',
        'description': 'Use the senses of an animal',
        'source': 'DtD 223'
    },
    'Blast': {
        'cost': '2 Essence per rating',
        'action': 'Instant',
        'description': 'Ranged weapon attack. The weapon rating can be raised up to the ephemera\'s Rank',
        'source': 'CofD 136'
    },
    'Dement': {
        'cost': '1 Essence',
        'action': 'Contested',
        'roll': 'vs Intelligence + Tolerance',
        'reaching': True,
        'description': 'Harrow a subject with the Insane Tilt',
        'source': 'CofD 136'
    },
    'Drain': {
        'cost': 'None',
        'action': 'Contested',
        'roll': 'vs Stamina + Resolve + Tolerance',
        'description': 'Steal Essence or Willpower',
        'source': 'CofD 137'
    },
    'Emotional Aura': {
        'cost': '1 Essence',
        'action': 'Instant',
        'reaching': True,
        'description': 'Overwhelm those in your presence with a chosen feeling for a scene, inflicting a -2 action penalty',
        'source': 'CofD 137'
    },
    'Entrap': {
        'cost': '2+ Essence',
        'action': 'Contested',
        'roll': 'vs Dexterity + Tolerance',
        'description': 'Fully restrain a target with a restraint Durability of Rank, boosted by extra Essence spent',
        'source': 'NH-CH 82'
    },
    'Entropic Decay': {
        'cost': '3 Essence',
        'action': 'Instant',
        'reaching': True,
        'description': 'Directly inflict lethal damage through unnatural decay',
        'source': 'WTF 2e 192'
    },
    'Essence Thief': {
        'cost': '1 Essence',
        'action': 'Instant',
        'description': 'Interact with and consume ephemeral entities of a dissimilar type',
        'source': 'CofD 137'
    },
    'Fate Sense': {
        'cost': '1 Essence',
        'action': 'Contested',
        'roll': 'vs Resolve + Tolerance',
        'description': 'Read a character\'s destiny',
        'source': 'CofD 137'
    },
    'Firestarter': {
        'cost': '1 Essence',
        'action': 'Instant',
        'reaching': True,
        'description': 'Ignite combustibles',
        'source': 'CofD 137'
    },
    'Hallucination': {
        'cost': '1 Essence',
        'action': 'Contested',
        'roll': 'vs Wits + Composure + Tolerance',
        'description': 'Inflict false sensory information',
        'source': 'CofD 137'
    },
    'Host Jump': {
        'cost': '3 Essence',
        'action': 'Instant',
        'prerequisites': ['Possess or Claim'],
        'description': 'Pass from host to valid host by touch',
        'source': 'CofD 137'
    },
    'Implant Mission': {
        'cost': '2 Essence',
        'action': 'Instant',
        'reaching': True,
        'description': 'Obsess an ordinary human with a given task',
        'source': 'CofD 137'
    },
    'Innocuous': {
        'cost': 'None',
        'action': 'Passive',
        'description': 'Penalize rolls to notice you by -2',
        'source': 'CofD 137'
    },
    'Left-Handed Spanner': {
        'cost': '1 Essence',
        'action': 'Instant',
        'description': 'Disable a device by touch',
        'source': 'CofD 137'
    },
    'Mortal Mask': {
        'cost': '1 Essence',
        'action': 'Instant',
        'prerequisites': ['Materialize'],
        'description': 'Adopt a human seeming while material',
        'source': 'CofD 137'
    },
    'Omen Trance': {
        'cost': '1 or 3 Essence',
        'action': 'Instant',
        'description': 'Channel a vision of the future to forestall danger',
        'source': 'CofD 138'
    },
    'Pathfinder': {
        'cost': '1 Essence',
        'action': 'Instant',
        'reaching': True,
        'description': 'Know the quickest path to a given destination',
        'source': 'CofD 138'
    },
    'Rapture': {
        'cost': '2 Essence',
        'action': 'Contested',
        'roll': 'vs Resolve + Tolerance',
        'reaching': True,
        'description': 'Briefly incapacitate a victim with pleasure',
        'source': 'CofD 138'
    },
    'Regenerate': {
        'cost': '1 Essence',
        'action': 'Instant',
        'description': 'Heal a point of non-aggravated damage',
        'source': 'CofD 138'
    },
    'Resurrection': {
        'cost': '10 Essence',
        'action': 'Extended',
        'prerequisites': ['Rank 4'],
        'description': 'Resurrect a once-living being from an untimely death',
        'source': 'CofD 138'
    },
    'Seek': {
        'cost': '0-1 Essence',
        'action': 'Instant',
        'reaching': True,
        'description': 'Sense the proximity of Anchor, Resonant, or Infrastructure Conditions',
        'source': 'CofD 138'
    },
    'Speed': {
        'cost': '2 or 4 Essence',
        'action': 'Instant',
        'description': 'Double or triple Speed',
        'source': 'CofD 138'
    },
    'Sign': {
        'cost': '1 Essence',
        'action': 'Instant',
        'description': 'Write a message into the Material Realm',
        'source': 'CofD 138'
    },
    'Stalwart': {
        'cost': 'None',
        'action': 'Passive',
        'description': 'Calculate base Defense as equal to Resistance',
        'source': 'CofD 138'
    },
    'Strike Blind': {
        'cost': '1 Essence',
        'action': 'Instant',
        'description': 'Blind people in an area, causing the Blinding Tilt',
        'source': 'DtD 223'
    },
    'Telekinesis': {
        'cost': '1 Essence',
        'action': 'Instant',
        'reaching': True,
        'description': 'Exert gross manipulation of things in the Material Realm',
        'source': 'CofD 138'
    },
    'Transmute': {
        'cost': '1/3/5 Essence',
        'action': 'Extended',
        'description': 'Change one substance into another with greater penalty based on how common the result would be',
        'source': 'DtD 223'
    },
    # Spiritual Numina
    'Domination': {
        'cost': '2 Essence',
        'action': 'Contested',
        'roll': 'vs Resolve + Presence',
        'description': 'Intimidate a character, inflicting Cowed',
        'source': 'NH-SM 77',
        'type': 'spiritual'
    },
    'Living Barren': {
        'cost': 'None',
        'action': 'Passive',
        'description': 'Your presence dims and deadens the Shadow, creating temporary barrens and shoals',
        'source': 'NH-SM 80',
        'type': 'spiritual'
    },
    'Usurp': {
        'cost': '2 Essence',
        'action': 'Contested',
        'roll': 'vs Resolve + Composure + Primal Urge or Finesse + Resistance',
        'description': 'Impose yourself as totem over a werewolf, or steal an entire pack from a totem',
        'source': 'NH-SM 77',
        'type': 'spiritual'
    },
}

# Totem Advantage Experience Costs
TOTEM_ADVANTAGE_COSTS = {
    'attribute': 5,
    'skill': 3,
    'specialty': 1,
    'merit': 2  # per dot
}

# Totem Points to Advantage Experience
TOTEM_POINTS_TO_EXPERIENCE = [
    (1, 8, 1),    # 1-8 points = 1 experience
    (9, 14, 3),   # 9-14 points = 3 experiences
    (15, 20, 5),  # 15-20 points = 5 experiences
    (21, 999, 10) # 20+ points = 10 experiences
]

def get_advantage_experience(totem_points):
    """Calculate how many experiences are available based on totem points."""
    for min_points, max_points, experiences in TOTEM_POINTS_TO_EXPERIENCE:
        if min_points <= totem_points <= max_points:
            return experiences
    return 0

# Rank requirements (based on total attributes)
RANK_BY_ATTRIBUTES = [
    (1, 5, 1),
    (6, 10, 2),
    (11, 15, 3),
    (16, 20, 4),
    (21, 999, 5)
]

def get_rank_from_attributes(total_attributes):
    """Determine spirit rank from total attribute dots."""
    for min_attr, max_attr, rank in RANK_BY_ATTRIBUTES:
        if min_attr <= total_attributes <= max_attr:
            return rank
    return 1

# Maximum Essence by Rank
MAX_ESSENCE_BY_RANK = {
    1: 10,
    2: 15,
    3: 20,
    4: 25,
    5: 50
}

# Number of Numina by Totem Points
def get_numina_count(totem_points):
    """Calculate how many numina a totem can have."""
    # Starts with 1, gets +1 per 4 totem points
    return 1 + (totem_points // 4)

