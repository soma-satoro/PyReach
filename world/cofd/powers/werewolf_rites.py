"""
Werewolf Rites for Chronicles of Darkness 2nd Edition.

Rites in Werewolf: The Forsaken 2e are organized by:
- Rite category (Wolf Rites, Pack Rites, Other Rites)
- Rank (1-5 dots)
- Prerequisites (tribe, lodge, merit requirements)
- Essence cost

Based on Werewolf: The Forsaken 2nd Edition and supplements.
"""

# ==================== WOLF RITES ====================
# Rites that individual werewolves perform

WOLF_RITES = {
    "chain_rage": {
        "name": "Chain Rage",
        "rite_type": "wolf",
        "rank": 1,
        "prerequisites": None,
        "cost": None,
        "description": "Participants carrying a ritual focus may exit Death Rage through extended concentration, for a month.",
        "book": "WTF 2e 139-140"
    },
    "messenger": {
        "name": "Messenger",
        "rite_type": "wolf",
        "rank": 1,
        "prerequisites": None,
        "cost": None,
        "description": "A lune conveys a message to a werewolf elsewhere in the world.",
        "book": "WTF 2e 140"
    },
    "bottle_spirit": {
        "name": "Bottle Spirit",
        "rite_type": "wolf",
        "rank": 2,
        "prerequisites": "Bone Shadow",
        "cost": None,
        "description": "Bind a spirit into a bottle for at least a day, where it does not bleed Essence.",
        "book": "WTF 2e 140"
    },
    "infest_locus": {
        "name": "Infest Locus",
        "rite_type": "wolf",
        "rank": 2,
        "prerequisites": "Fire-Touched",
        "cost": None,
        "description": "Infest a locus, making any who draw Essence from it gain the Sick Tilt.",
        "book": "NH-SM 20"
    },
    "rite_of_the_shroud": {
        "name": "Rite of the Shroud",
        "rite_type": "wolf",
        "rank": 2,
        "prerequisites": "Bale Hound",
        "cost": None,
        "description": "Obscure the tarnish on Auspice and Renown brands.",
        "book": "NH-SM 39"
    },
    "sacred_hunt": {
        "name": "Sacred Hunt",
        "rite_type": "wolf",
        "rank": 2,
        "prerequisites": None,
        "cost": None,
        "description": "Mark quarry for the Sacred Hunt. Spirit quarry may be consumed for Essence or obliged to inscribe a Gift. The ritualist's tribe confers additional benefits on the pack.",
        "tribe_benefits": {
            "blood_talons": "Perceive the Renown of Forsaken and Pure.",
            "bone_shadows": "Touch and strike ephemera bodily.",
            "hunters_in_darkness": "Sense the strength of the Gauntlet, alterations to it, and your quarry's passage between worlds.",
            "iron_masters": "Choose which Lunacy Condition manifests in humans.",
            "storm_lords": "Identify the Ridden, Urged, and Claimed.",
            "fire_touched": "Spirits following your direction or attacking your quarry take your spirit Rank as bonus dice.",
            "ivory_claws": "Intuit links to the quarry through blood or community, and penalize attempts by the quarry's relatives to hinder you by Primal Urge.",
            "predator_kings": "Acquire your spirit Rank in Influence (Nature), which rolls Strength + Primal Urge.",
            "hounds_of_consumption": "Double the Essence gain for consuming forbidden flesh.",
            "hounds_of_destruction": "Increase damage inflicted by half Primal Urge (rounded up).",
            "hounds_of_disharmony": "Identify the weakest link in a group, gaining an exceptional success on 3 successes instead of 5.",
            "hounds_of_exposure": "Use Uncontested Tracking to identify the prey's most devastating secret.",
            "hounds_of_invasion": "Add Primal Urge to Stealth pools, and inflict Stealth + Primal Urge as a penalty to being tracked or discovered.",
            "geryo": "Activate World Shaking and roll Perception to know the direction to the prey; Natural weapons count as the prey's Bane, even if they don't normally possess a Bane."
        },
        "book": "WTF 2e 140, 310; DEC 79; NH-SM 36-37, 155-156"
    },
    "carrion_feast": {
        "name": "Carrion Feast",
        "rite_type": "wolf",
        "rank": 3,
        "prerequisites": "Eater of the Dead",
        "cost": None,
        "description": "Consume carrion for Essence and to draw on animal carrion's symbolic strengths as a dice bonus, or to draw out Willpower from human carrion.",
        "book": "Pack 91"
    },
    "flay_auspice": {
        "name": "Flay Auspice",
        "rite_type": "wolf",
        "rank": 3,
        "prerequisites": "Pure",
        "cost": None,
        "description": "Permanently remove the Auspice of a willing werewolf, making them one of the Pure.",
        "book": "NH-SM 20"
    },
    "kindle_fury": {
        "name": "Kindle Fury",
        "rite_type": "wolf",
        "rank": 3,
        "prerequisites": "Blood Talon",
        "cost": None,
        "description": "Whip up the Destroyer within the Blood, acting as an extra Anchor for a month.",
        "book": "WTF 2e 140"
    },
    "rite_of_absolution": {
        "name": "Rite of Absolution",
        "rite_type": "wolf",
        "rank": 3,
        "prerequisites": "Bale Hound",
        "cost": None,
        "description": "Gain a dice pool that can be drawn upon for bonus dice in breaking point rolls when in service of the Maeljin.",
        "book": "NH-SM 39"
    },
    "shadowbind": {
        "name": "Shadowbind",
        "rite_type": "wolf",
        "rank": 3,
        "prerequisites": None,
        "cost": None,
        "description": "Bind a spirit within a ritual space, naming the conditions that will set it free.",
        "book": "WTF 2e 141"
    },
    "the_thorn_pursuit": {
        "name": "The Thorn Pursuit",
        "rite_type": "wolf",
        "rank": 3,
        "prerequisites": None,
        "cost": None,
        "description": "Opens a hedge portal their prey of a Sacred Hunt used within the last chapter.",
        "book": "Hedge 34"
    },
    "between_worlds": {
        "name": "Between Worlds",
        "rite_type": "wolf",
        "rank": 4,
        "prerequisites": None,
        "cost": None,
        "description": "Use a Locus to Reach into the Gauntlet rather than Flesh or Shadow, but permanently defile the Locus used, destroying its power forever.",
        "book": "NH-SM 151"
    },
    "fetish": {
        "name": "Fetish",
        "rite_type": "wolf",
        "rank": 4,
        "prerequisites": None,
        "cost": "● per dot",
        "description": "Create a fetish by binding a spirit within an item.",
        "book": "WTF 2e 141"
    },
    "shadow_bridge": {
        "name": "Shadow Bridge",
        "rite_type": "wolf",
        "rank": 4,
        "prerequisites": "Fire-Touched",
        "cost": None,
        "description": "Use a sacrifice to form a bridge between two loci, crossing between them instead of between Shadow and Flesh.",
        "book": "NH-SM 20"
    },
    "twilight_purge": {
        "name": "Twilight Purge",
        "rite_type": "wolf",
        "rank": 4,
        "prerequisites": None,
        "cost": "●●●",
        "description": "Hurl beings out of Twilight for at least an hour.",
        "book": "WTF 2e 141-142"
    },
    "devour": {
        "name": "Devour",
        "rite_type": "wolf",
        "rank": 5,
        "prerequisites": None,
        "cost": None,
        "description": "Consume the flesh of a werewolf, Becoming a Devourer. Future rituals provide an Enlightenment (NH-SM 56).",
        "book": "NH-SM 54"
    },
    "forge_alliance": {
        "name": "Forge Alliance",
        "rite_type": "wolf",
        "rank": 5,
        "prerequisites": None,
        "cost": "● per pack",
        "description": "Join packs together mystically for a month or until a shared quarry is brought low.",
        "book": "WTF 2e 142"
    },
    "urfarahs_bane": {
        "name": "Urfarah's Bane",
        "rite_type": "wolf",
        "rank": 5,
        "prerequisites": None,
        "cost": "●●●●●",
        "description": "One werewolf is singled out of the pack until sunrise. Her claws and teeth deal aggravated damage to Uratha.",
        "book": "WTF 2e 142"
    },
    "veil": {
        "name": "Veil",
        "rite_type": "wolf",
        "rank": 5,
        "prerequisites": "Iron Master",
        "cost": "●●●●●",
        "description": "Spirits destroy records of a recent supernatural event.",
        "book": "WTF 2e 142"
    }
}

# ==================== PACK RITES ====================
# Rites that benefit the entire pack

PACK_RITES = {
    "banish": {
        "name": "Banish",
        "rite_type": "pack",
        "rank": 1,
        "prerequisites": None,
        "cost": None,
        "description": "Banish a creature of flesh from the Spirit Realm, or vice-versa.",
        "book": "WTF 2e 142-143"
    },
    "harness_the_cycle": {
        "name": "Harness the Cycle",
        "rite_type": "pack",
        "rank": 1,
        "prerequisites": None,
        "cost": None,
        "description": "Draw Essence (for werewolves) and Willpower (for humans) from the turning of the seasons.",
        "book": "WTF 2e 143"
    },
    "totemic_empowerment": {
        "name": "Totemic Empowerment",
        "rite_type": "pack",
        "rank": 1,
        "prerequisites": None,
        "cost": None,
        "description": "Unite a pack member with the power of your totem until sunrise.",
        "book": "WTF 2e 143"
    },
    "hunting_ground": {
        "name": "Hunting Ground",
        "rite_type": "pack",
        "rank": 2,
        "prerequisites": None,
        "cost": None,
        "description": "Claim territory for a season, granting bonuses to hunt there and interact with residents.",
        "book": "WTF 2e 143-144"
    },
    "moons_mad_love": {
        "name": "Moon's Mad Love",
        "rite_type": "pack",
        "rank": 2,
        "prerequisites": None,
        "cost": None,
        "description": "Wards packmates from the effects of Lunacy for a month.",
        "book": "WTF 2e 144"
    },
    "shackled_lightning": {
        "name": "Shackled Lightning",
        "rite_type": "pack",
        "rank": 2,
        "prerequisites": None,
        "cost": "● per 10 subjects",
        "description": "Contain a spirit of lightning to render your legion Indomitable so long as they remain silent and you spend no Essence, after which you release a berserker rage.",
        "book": "DEC 80"
    },
    "sigrblot": {
        "name": "Sigrblot",
        "rite_type": "pack",
        "rank": 2,
        "prerequisites": None,
        "cost": "●+ per court",
        "description": "Feed participating spirit courts with Essence, after which they suffer -5 to Reach for up to a season.",
        "book": "DE 165"
    },
    "wellspring": {
        "name": "Wellspring",
        "rite_type": "pack",
        "rank": 2,
        "prerequisites": None,
        "cost": None,
        "description": "Charges the Resonance of a locus for a month, spreading the power of its Influence. The pack must honor a ban for the locus.",
        "book": "WTF 2e 144-145"
    },
    "banshee_howl": {
        "name": "Banshee Howl",
        "rite_type": "pack",
        "rank": 3,
        "prerequisites": "Lodge of the Screaming Moon",
        "cost": None,
        "description": "Lays claim over deaths within the territory, denying supernatural beings outside the pack of any benefits from a kill.",
        "book": "Pack 87"
    },
    "raiment_of_the_storm": {
        "name": "Raiment of the Storm",
        "rite_type": "pack",
        "rank": 3,
        "prerequisites": "Storm Lord",
        "cost": None,
        "description": "Draw power from a storm in the form of Armor, supernatural protection, and safety from electrocution, at the cost of a ban to remain active during the storm.",
        "book": "WTF 2e 145"
    },
    "shadowcall": {
        "name": "Shadowcall",
        "rite_type": "pack",
        "rank": 3,
        "prerequisites": None,
        "cost": None,
        "description": "Offer gathra to summon a particular spirit.",
        "book": "WTF 2e 145"
    },
    "supplication": {
        "name": "Supplication",
        "rite_type": "pack",
        "rank": 3,
        "prerequisites": None,
        "cost": None,
        "description": "Spread gathra around your territory and honor a spirit choir's ban to ease relations with them for a season.",
        "book": "WTF 2e 145"
    },
    "hidden_path": {
        "name": "Hidden Path",
        "rite_type": "pack",
        "rank": 4,
        "prerequisites": "Hunter in Darkness",
        "cost": None,
        "description": "Find a secret land route across flesh and spirit to a destination, ten times as quick and without interception.",
        "book": "WTF 2e 145-146"
    },
    "expel": {
        "name": "Expel",
        "rite_type": "pack",
        "rank": 4,
        "prerequisites": None,
        "cost": None,
        "description": "Cast a spirit out of a host person or object.",
        "book": "WTF 2e 146"
    },
    "heal_old_wounds": {
        "name": "Heal Old Wounds",
        "rite_type": "pack",
        "rank": 4,
        "prerequisites": None,
        "cost": None,
        "description": "Attempt to seal a Wound within territory claimed by the Hunting Ground rite.",
        "book": "NH-SM 84"
    },
    "great_hunt": {
        "name": "Great Hunt",
        "rite_type": "pack",
        "rank": 5,
        "prerequisites": None,
        "cost": None,
        "description": "Until the sun rises, non-werewolf packmates assume Urhan form and gain a werewolf's senses and regeneration, under a ban to hunt a named quarry.",
        "book": "WTF 2e 146"
    },
    "shadow_distortion": {
        "name": "Shadow Distortion",
        "rite_type": "pack",
        "rank": 5,
        "prerequisites": "Fire-Touched",
        "cost": "● x 10",
        "description": "Inflict a penalty to non-packmates in the Shadow, and attacks and abilities used against packmates are also penalised.",
        "book": "NH-SM 20"
    },
    "unleash_shadow": {
        "name": "Unleash Shadow",
        "rite_type": "pack",
        "rank": 5,
        "prerequisites": "Fire-Touched",
        "cost": None,
        "description": "Any Manifestation cost is reduced to 1 Essence in the pack's territory, and the power of spirits is enhanced in the territory.",
        "book": "NH-SM 20"
    }
}

# ==================== OTHER RITES ====================
# Special rites from other sources

OTHER_RITES = {
    "lupus_venandi": {
        "name": "Lupus Venandi",
        "rite_type": "other",
        "rank": 4,
        "prerequisites": "Apocalypsis Fidei Merit",
        "cost": None,
        "description": "Impose the Siskur-Dah Condition on a werewolf against the chosen prey, compelling the werewolf to complete their hunt.",
        "book": "NH-SM 134-135"
    }
}

# ==================== CONSOLIDATED RITES ====================

ALL_WEREWOLF_RITES = {
    **WOLF_RITES,
    **PACK_RITES,
    **OTHER_RITES
}

# Rites organized by category
RITES_BY_CATEGORY = {
    "wolf": WOLF_RITES,
    "pack": PACK_RITES,
    "other": OTHER_RITES
}

# Rites organized by rank
RITES_BY_RANK = {
    1: {},
    2: {},
    3: {},
    4: {},
    5: {}
}

# Populate rank dictionary
for rite_key, rite_data in ALL_WEREWOLF_RITES.items():
    rank = rite_data.get('rank')
    if rank:
        RITES_BY_RANK[rank][rite_key] = rite_data

# Helper functions
def get_rite(rite_key):
    """Get a specific rite by key."""
    return ALL_WEREWOLF_RITES.get(rite_key.lower().replace(" ", "_").replace("'", ""))


def get_rites_by_type(rite_type):
    """Get all rites of a specific type (wolf, pack, other)."""
    rite_type = rite_type.lower().replace(" ", "_")
    return RITES_BY_CATEGORY.get(rite_type, {})


def get_rites_by_rank(rank):
    """Get all rites at a specific rank."""
    return RITES_BY_RANK.get(rank, {})


def get_all_rites():
    """Get all werewolf rites."""
    return ALL_WEREWOLF_RITES


def get_wolf_rites():
    """Get all wolf rites (individual rites)."""
    return WOLF_RITES


def get_pack_rites():
    """Get all pack rites."""
    return PACK_RITES


def get_other_rites():
    """Get all other rites."""
    return OTHER_RITES


def check_rite_prerequisites(character, rite_data):
    """
    Check if a character meets the prerequisites for a rite.
    
    Args:
        character: The character object
        rite_data: The rite data dictionary
        
    Returns:
        tuple: (meets_prereqs, error_message)
    """
    prerequisites = rite_data.get("prerequisites")
    
    # No prerequisites means anyone can learn it
    if not prerequisites:
        return True, None
    
    # Get character's tribe
    tribe = character.db.stats.get("bio", {}).get("tribe", "").lower().replace(" ", "_")
    
    # Check tribe prerequisites
    tribe_prereqs = {
        "blood talon": "blood_talons",
        "blood talons": "blood_talons",
        "bone shadow": "bone_shadows",
        "bone shadows": "bone_shadows",
        "hunter in darkness": "hunters_in_darkness",
        "hunters in darkness": "hunters_in_darkness",
        "iron master": "iron_masters",
        "iron masters": "iron_masters",
        "storm lord": "storm_lords",
        "storm lords": "storm_lords",
        "fire-touched": "fire_touched",
        "fire touched": "fire_touched"
    }
    
    prereq_lower = prerequisites.lower()
    
    # Check if prerequisite is a tribe
    for tribe_name, tribe_key in tribe_prereqs.items():
        if tribe_name in prereq_lower:
            if tribe != tribe_key:
                return False, f"Requires tribe: {prerequisites}"
            return True, None
    
    # Check for lodge prerequisites
    if "lodge" in prereq_lower:
        lodge = character.db.stats.get("bio", {}).get("lodge", "").lower()
        if prereq_lower not in lodge:
            return False, f"Requires: {prerequisites}"
        return True, None
    
    # Check for merit prerequisites
    if "merit" in prereq_lower:
        # Would need to check character's merits
        # For now, just warn about the requirement
        return True, f"Note: Requires {prerequisites}"
    
    # Check for Pure/Bale Hound prerequisites
    if "pure" in prereq_lower or "bale hound" in prereq_lower:
        # Would need to check if character is Pure
        return True, f"Note: Requires {prerequisites}"
    
    # Unknown prerequisite type - allow but warn
    return True, f"Note: Requires {prerequisites}"


def get_rites_for_tribe(tribe):
    """
    Get all rites available to a specific tribe.
    
    Args:
        tribe: The tribe name
        
    Returns:
        dict: Dictionary of available rites
    """
    tribe_lower = tribe.lower().replace(" ", "_")
    available_rites = {}
    
    for rite_key, rite_data in ALL_WEREWOLF_RITES.items():
        prereqs = rite_data.get("prerequisites")
        
        # Include rites with no prerequisites
        if not prereqs:
            available_rites[rite_key] = rite_data
        else:
            # Check if this rite's prerequisite matches the tribe
            prereq_lower = prereqs.lower().replace(" ", "_").replace("-", "_")
            if tribe_lower in prereq_lower:
                available_rites[rite_key] = rite_data
    
    return available_rites
