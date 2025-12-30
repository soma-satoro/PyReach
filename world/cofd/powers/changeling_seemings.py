"""
Changeling: The Lost Seemings and Entitlements
Detailed seeming and entitlement information for Chronicles of Darkness 2nd Edition.
Based on Changeling: The Lost 2nd Edition core book and supplements.
"""

# ============================================================================
# SEEMINGS
# ============================================================================

ALL_SEEMINGS = {
    "beast": {
        "name": "Beast",
        "regalia": "Steed",
        "bonus_attribute": "Resistance",
        "blessing": "While unafraid, or for Glamour per three turns, deal lethal damage unarmed and take +3 to Initiative and Speed.",
        "curse": "Risk Clarity damage at half Wyrd when hasty or careless decisions harm others.",
        "description": "Grims and Savages who roamed Faerie under the heart and skin of an animal",
        "book": "CTL 2e 22"
    },
    "darkling": {
        "name": "Darkling",
        "regalia": "Mirror",
        "bonus_attribute": "Finesse",
        "blessing": "Spend Willpower, and with witnesses Glamour, to touch and become the insubstantial for three turns.",
        "curse": "Risk Clarity damage at half Wyrd when a secret you know turns out false.",
        "description": "Wisps and Mountebanks who knew safety in Faerie by disappearing into darkness",
        "book": "CTL 2e 24"
    },
    "elemental": {
        "name": "Elemental",
        "regalia": "Sword",
        "bonus_attribute": "Resistance",
        "blessing": "When surrounded by your element and either half-full of Willpower or for Glamour, act through it up to three yards away.",
        "curse": "Risk Clarity damage at half Wyrd when browbeat or coerced into a course of action.",
        "description": "Sprites and Torrents infused with and molded by the materials and environment of Faerie",
        "book": "CTL 2e 26"
    },
    "fairest": {
        "name": "Fairest",
        "regalia": "Crown",
        "bonus_attribute": "Power",
        "blessing": "While in harmony or for Glamour, you may spend Willpower on another character's behalf.",
        "curse": "Risk Clarity damage at half Wyrd when your actions are responsible for harming your allies.",
        "description": "Sovereigns and Muses touched by the heights of Faerie's glory, beauty, and cruelty",
        "book": "CTL 2e 28"
    },
    "ogre": {
        "name": "Ogre",
        "regalia": "Shield",
        "bonus_attribute": "Power",
        "blessing": "When you strike on someone else's behalf, or for Glamour, inflict Beaten Down for three turns.",
        "curse": "Risk Clarity damage at half Wyrd when those who aren't your enemies cower from you.",
        "description": "Bruisers and Gargoyles who endure the marks of blunt brutality",
        "book": "CTL 2e 30"
    },
    "wizened": {
        "name": "Wizened",
        "regalia": "Jewel",
        "bonus_attribute": "Finesse",
        "blessing": "With appropriate tools, or for Glamour, make Build Equipment rolls to work one material into another.",
        "curse": "Risk Clarity damage at half Wyrd when taken off-guard by unpleasant surprise.",
        "description": "Hatters and Domovye worn down by the crafts and labors of their Durance",
        "book": "CTL 2e 32"
    },
}

# ============================================================================
# ENTITLEMENTS
# ============================================================================

ALL_ENTITLEMENTS = {
    "baron_of_the_lesser_ones": {
        "name": "Baron of the Lesser Ones",
        "description": "Diplomat and mediator accepted among hobgoblins.",
        "prerequisites": "Empathy:2, Intimidation or Persuasion:2, any of Gentrified Bearing, Hob Kin, or Interdisciplinary Specialty (Goblins)",
        "curse": "Bonus damage dice to breaking points favoring hobgoblins.",
        "token": "A signet ring which helps to navigate and make deliveries into and through the Hedge.",
        "blessings": [
            "Gain half Wyrd as Allies among a subset of hobgoblins.",
            "Swear a hostile oath against a changeling from a predecessor's work. Recover all Willpower by fulfilling the oath."
        ],
        "book": "OAT 37"
    },
    "dauphines_of_wayward_children": {
        "name": "Dauphines of Wayward Children",
        "description": "Three cooperative caretakers for youth without homes.",
        "prerequisites": {
            "Sophomore": "Presence:2, Persuasion:2, Wyrd:3",
            "Chaperone": "Manipulation:2, Empathy:2, Wyrd:3",
            "Dowager": "Composure:2, Intimidation:2, Wyrd:3"
        },
        "curse": "Bonus damage dice to breaking points from losing a ward.",
        "token": "A lily brooch with which to locate wards and children in need. It provides bonuses to the caretaker's role among the three and can allow wards to pierce the Mask.",
        "blessings": [
            "Inherit a gift from a past ward which becomes a Token rated at half Wyrd.",
            "Non-changeling wards gain the Lucid Dreamer Merit. Treat their Bastion Fortification as 1, and dreamweave there with an extra phantom success."
        ],
        "book": "OAT 40"
    },
    "master_of_keys": {
        "name": "Master of Keys",
        "description": "Inquisitive seeker charged with unlocking the discovery of secrets and revelations.",
        "prerequisites": "Investigation:2, Empathy:2, any Merit used to uncover secrets",
        "curse": "Bonus damage dice to breaking points from holding back a secret.",
        "token": "The key to unlock your final doom still in wait. It tarnishes for a night when exposed to those who would end you, and grants the rote quality to rolls to access things locked away.",
        "blessings": [
            "Portal from any door to a free Safe Place with a two-dot Library.",
            "Spend Glamour when portaling through a Hedgeway to change its Key."
        ],
        "book": "OAT 44"
    },
    "modiste_of_elfhame": {
        "name": "Modiste of Elfhame",
        "description": "Luxurious tailor and witch that infuses their creations with the magic of the Hedge.",
        "prerequisites": "Crafts:2, Expression:2, Hollow:1+, Hedge Sorcerer",
        "curse": "Bonus damage dice to breaking points while pursuing materials for garments.",
        "token": "Bone sewing needle that grows in size and can be used as a substitute for hecatombs during Hedge Sorcery.",
        "blessings": [
            "Gain half Wyrd as Workshop (specialties based on garment crafting) which is always stocked with mundane supplies for crafting clothing.",
            "Garments crafted by the Modiste give wearers the effect of Striking Looks:1 while worn."
        ],
        "book": "Hedge 72"
    },
    "thorn_dancer": {
        "name": "Thorn Dancer",
        "description": "Graceful dancer that glides through the Thorns, exploring for their own amusement or leading others.",
        "prerequisites": "Socialize:2, Athletics:3, Expression:2, any movement based skill specialty",
        "curse": "Bonus damage dice to breaking points while not in the Hedge.",
        "token": "Gladiatorial boots/sandals that protect the wearer from extreme environments, falls, and Conditions from the Thorns. Can spend Willpower to extend to others.",
        "blessings": [
            "Gain Arcadian Metabolism and Hob Kin Merits.",
            "Reduce Clarity damage by an additional die while in the Hedge."
        ],
        "book": "Hedge 148"
    },
    "sibylline_fishers": {
        "name": "Sibylline Fishers",
        "description": "Digital oracles that trawl the BriarNet and beyond for secrets given by the Hedge.",
        "prerequisites": "Computers:3, Investigation:2, Wyrd:3",
        "curse": "Prompts a Clarity attack when their own secrets are revealed, even voluntarily.",
        "token": "A Token computer program that can operate on any internet-capable device that generates prophesies of the past, present, and future.",
        "blessings": [
            "8-again to Investigation rolls to find secrets.",
            "Can speak with the authority of an oracle to try to gain the Connected condition with a group of listeners."
        ],
        "book": "Hedge 151"
    },
    "spiderborn_riders": {
        "name": "Spiderborn Riders",
        "description": "Nomadic free spirits that reject all authority, roaming the Hedge freeing others from chains.",
        "prerequisites": "Resolve:3",
        "curse": "Bonus damage dice to breaking points when refusing to help other people in the Hedge.",
        "token": "Cut-off biker vests with individualized patches, always featuring a spiderweb and lightning bolt. Allows the wearer to know the pledges of another and helps intimidate the servants of the Fae.",
        "blessings": [
            "Gain Indomitable Merit, if already possessed, gain additional bonus dice against mental influence.",
            "Spend Glamour while navigating the Hedge to be lead to where they are needed most."
        ],
        "book": "Hedge 154"
    },
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_seeming(seeming_name):
    """Get a specific seeming by name."""
    seeming_key = seeming_name.lower().replace(" ", "_")
    return ALL_SEEMINGS.get(seeming_key)

def get_all_seemings():
    """Get all seeming data."""
    return ALL_SEEMINGS.copy()

def get_entitlement(entitlement_name):
    """Get a specific entitlement by name."""
    entitlement_key = entitlement_name.lower().replace(" ", "_")
    return ALL_ENTITLEMENTS.get(entitlement_key)

def get_all_entitlements():
    """Get all entitlement data."""
    return ALL_ENTITLEMENTS.copy()

