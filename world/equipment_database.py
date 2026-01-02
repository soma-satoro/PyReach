"""
Equipment Database for Chronicles of Darkness
Based on Hurt Locker supplement

This module contains comprehensive weapon and armor data for the combat system.
"""

class WeaponData:
    """Data class for weapon statistics based on Chronicles of Darkness Hurt Locker"""
    
    def __init__(self, name, damage=0, initiative_mod=0, weapon_type="melee", 
                 size=1, strength_req=1, availability=1, tags="", capacity="single"):
        self.name = name
        self.damage = damage  # Damage modifier (added to successes)
        self.initiative_mod = initiative_mod  # Initiative modifier
        self.weapon_type = weapon_type  # "melee", "ranged", "thrown"
        self.size = size  # Weapon size
        self.strength_req = strength_req  # Minimum strength requirement
        self.availability = availability  # Availability rating
        self.tags = tags  # Special weapon tags
        self.capacity = capacity  # For ranged weapons
        
    def get_attack_dice_pool(self, character):
        """Calculate attack dice pool for this weapon based on CoD 2e rules"""
        attrs = character.db.stats.get("attributes", {})
        skills = character.db.stats.get("skills", {})
        
        # Determine correct attribute + skill combination
        if self.weapon_type == "ranged":
            # All ranged weapons use Dexterity + Firearms, including bows and crossbows
            attr_value = attrs.get("dexterity", 1)
            skill_value = skills.get("firearms", 0)
        elif self.weapon_type == "thrown":
            # All thrown weapons use Dexterity + Athletics, including big thrown weapons like spears
            attr_value = attrs.get("dexterity", 1)
            skill_value = skills.get("athletics", 0)
        elif self.is_brawl_weapon():
            # Fist weapons (brass knuckles, tiger claws) use Strength + Brawl
            attr_value = attrs.get("strength", 1)
            skill_value = skills.get("brawl", 0)
        elif self.uses_dexterity():
            # Whips and certain exotic weapons use Dexterity + Weaponry
            attr_value = attrs.get("dexterity", 1)
            skill_value = skills.get("weaponry", 0)
        else:
            # Most melee weapons except the above use Strength + Weaponry
            attr_value = attrs.get("strength", 1)
            skill_value = skills.get("weaponry", 0)
            
        return attr_value + skill_value
    
    def is_brawl_weapon(self):
        """Check if weapon uses Brawl skill instead of Weaponry"""
        return "brawl" in self.tags.lower()
    
    def uses_dexterity(self):
        """Check if weapon uses Dexterity instead of Strength for melee"""
        return "dexterity" in self.tags.lower() and self.weapon_type == "melee"
    
    def applies_defense(self):
        """Check if Defense applies against this weapon"""
        # Slow weapons allow full Defense even for ranged attacks
        if self.has_tag("slow"):
            return True
        # Defense applies to unarmed, melee weaponry, and thrown attacks
        # Defense does NOT apply to ranged (firearms) attacks
        return self.weapon_type in ["melee", "thrown"] or self.is_brawl_weapon()
        
    def get_damage_rating(self):
        """Get weapon damage rating"""
        return self.damage
        
    def is_ranged(self):
        """Check if weapon is ranged"""
        return self.weapon_type in ["ranged", "thrown"]
    
    def has_tag(self, tag_name):
        """Check if weapon has a specific tag"""
        return tag_name.lower() in self.tags.lower()
    
    def get_attack_modifier(self):
        """Get attack roll modifier from weapon tags"""
        modifier = 0
        if self.has_tag("accurate"):
            modifier += 1
        if self.has_tag("inaccurate"):
            modifier -= 1
        return modifier
    
    def get_defense_modifier(self):
        """Get Defense modifier when wielding this weapon"""
        modifier = 0
        if self.has_tag("guard"):
            modifier += 1
        if self.has_tag("reach"):
            modifier += 1  # Applied situationally vs smaller weapons
        return modifier
    
    def get_grapple_modifier(self):
        """Get grapple dice modifier from weapon tags"""
        modifier = 0
        if self.has_tag("grapple"):
            modifier += self.damage  # Add weapon's dice bonus to grapple
        if self.has_tag("reach"):
            modifier -= 1  # Reach weapons suffer -1 in grapples
        return modifier
    
    def get_armor_piercing(self):
        """Get armor piercing rating from tags"""
        # Look for piercing tags (piercing_1, piercing_2, etc.)
        for tag in self.tags.split(","):
            tag = tag.strip().lower()
            if tag.startswith("piercing_"):
                try:
                    return int(tag.split("_")[1])
                except (IndexError, ValueError):
                    pass
        return 0
    
    def get_roll_type_modifiers(self):
        """Get special dice roll types from weapon tags"""
        from world.utils.dice_utils import RollType
        roll_types = set()
        
        if self.has_tag("8-again"):
            roll_types.add(RollType.EIGHT_AGAIN)
        elif self.has_tag("9-again"):
            roll_types.add(RollType.NINE_AGAIN)
        else:
            roll_types.add(RollType.TEN_AGAIN)  # Default 10-again
            
        return roll_types
    
    def causes_tilt(self, tilt_name):
        """Check if weapon causes a specific tilt"""
        tilt_tags = {
            "bleeding": "bleed",
            "burning": "incendiary", 
            "knockdown": "knockdown",
            "stunned": "stun"
        }
        return self.has_tag(tilt_tags.get(tilt_name.lower(), ""))
    
    def get_tilt_modifier(self, tilt_name):
        """Get modifier for tilt application"""
        # Some tags double the weapon bonus for tilt purposes
        if tilt_name.lower() == "bleeding" and self.has_tag("bleed"):
            return self.damage * 2
        elif tilt_name.lower() == "knockdown" and self.has_tag("knockdown"):
            return self.damage * 2
        elif tilt_name.lower() == "stunned" and self.has_tag("stun"):
            return self.damage * 2
        return self.damage
    
    def is_concealed_when_not_attacking(self):
        """Check if weapon provides concealment when not used to attack"""
        return self.has_tag("concealed")
    
    def get_concealment_modifier(self):
        """Get concealment modifier from weapon size"""
        if self.is_concealed_when_not_attacking():
            return self.size
        return 0
    
    def is_fragile(self):
        """Check if weapon is fragile (reduced Durability)"""
        return self.has_tag("fragile")
    
    def is_two_handed(self):
        """Check if weapon requires two hands"""
        return self.has_tag("two-handed")
    
    def can_be_thrown(self):
        """Check if weapon can be thrown"""
        return self.has_tag("thrown") or self.weapon_type == "thrown"
    
    def is_aerodynamic(self):
        """Check if thrown weapon is aerodynamic (doubles range)"""
        return self.has_tag("thrown (a)") or self.has_tag("aerodynamic")
    
    def provides_skill_enhancement(self):
        """Check if weapon enhances specific skills"""
        enhance_tags = []
        for tag in self.tags.split(","):
            tag = tag.strip().lower()
            if tag.startswith("enhance"):
                enhance_tags.append(tag)
        return enhance_tags


class EquipmentData:
    """Data class for general equipment (non-weapons/armor)"""
    
    def __init__(self, name, category, die_bonus=0, durability=1, size=1, structure=1,
                 availability=1, effect="", skill_bonuses=None, special_properties=None):
        self.name = name
        self.category = category  # Equipment category (firearm_accessories, surveillance, etc.)
        self.die_bonus = die_bonus  # Bonus dice to relevant rolls
        self.durability = durability  # How resistant to damage
        self.size = size  # Physical size
        self.structure = structure  # Structural integrity
        self.availability = availability  # Availability rating
        self.effect = effect  # Description of what it does
        self.skill_bonuses = skill_bonuses or {}  # Dict of skill bonuses {"crafts": 2, "survival": 1}
        self.special_properties = special_properties or {}  # Dict of special effects
    
    def get_bonus_for_skill(self, skill_name):
        """Get the bonus this equipment provides for a specific skill"""
        return self.skill_bonuses.get(skill_name.lower(), 0)
    
    def has_property(self, property_name):
        """Check if equipment has a specific property"""
        return property_name.lower() in [k.lower() for k in self.special_properties.keys()]
    
    def get_property_value(self, property_name):
        """Get the value of a specific property"""
        for key, value in self.special_properties.items():
            if key.lower() == property_name.lower():
                return value
        return None


class ArmorData:
    """Data class for armor statistics"""
    
    def __init__(self, name, general_armor=0, ballistic_armor=0, strength_req=1, 
                 defense_penalty=0, speed_penalty=0, availability=1, coverage=None, notes=""):
        self.name = name
        self.general_armor = general_armor  # Reduces total damage
        self.ballistic_armor = ballistic_armor  # Downgrades firearm lethal to bashing
        self.strength_req = strength_req  # Minimum strength requirement
        self.defense_penalty = defense_penalty  # Defense penalty while wearing
        self.speed_penalty = speed_penalty  # Speed penalty while wearing
        self.availability = availability  # Availability rating
        self.coverage = coverage or []  # Body areas protected
        self.notes = notes  # Special notes
    
    def get_total_armor_vs_attack(self, attack_type="general", armor_piercing=0):
        """Calculate effective armor rating against an attack"""
        if attack_type == "ballistic":
            # Apply ballistic armor first, then general armor
            effective_ballistic = max(0, self.ballistic_armor - armor_piercing)
            remaining_piercing = max(0, armor_piercing - self.ballistic_armor)
            effective_general = max(0, self.general_armor - remaining_piercing)
            return effective_ballistic, effective_general
        else:
            # General attacks only face general armor
            effective_general = max(0, self.general_armor - armor_piercing)
            return 0, effective_general
    
    def applies_strength_penalty(self, character_strength):
        """Check if character suffers strength penalty for wearing armor"""
        return character_strength < self.strength_req
    
    def covers_location(self, location):
        """Check if armor covers a specific body location"""
        return location.lower() in [area.lower() for area in self.coverage]


# Weapon definitions from Chronicles of Darkness: Hurt Locker
WEAPON_DATABASE = {
    # UNARMED
    "unarmed": WeaponData("Unarmed", damage=0, initiative_mod=0, weapon_type="melee", 
                         size=1, strength_req=1, availability=0, tags="brawl"),
    
    # MELEE WEAPONS - BLADED
    "battle_axe": WeaponData("Battle Axe", damage=3, initiative_mod=-4, weapon_type="melee",
                            size=3, strength_req=3, availability=3, tags="9-again, two-handed"),
    "fire_axe": WeaponData("Fire Axe", damage=2, initiative_mod=-4, weapon_type="melee",
                          size=3, strength_req=3, availability=2, tags="9-again, two-handed"),
    "great_sword": WeaponData("Great Sword", damage=4, initiative_mod=-5, weapon_type="melee",
                             size=3, strength_req=4, availability=4, tags="9-again, two-handed"),
    "hatchet": WeaponData("Hatchet", damage=1, initiative_mod=-2, weapon_type="melee",
                         size=1, strength_req=1, availability=2),
    "knife_small": WeaponData("Small Knife", damage=0, initiative_mod=0, weapon_type="melee",
                             size=1, strength_req=1, availability=1, tags="thrown"),
    "knife_hunting": WeaponData("Hunting Knife", damage=1, initiative_mod=-1, weapon_type="melee",
                               size=2, strength_req=1, availability=2, tags="enhance_crafts_survival"),
    "machete": WeaponData("Machete", damage=2, initiative_mod=-2, weapon_type="melee",
                         size=2, strength_req=2, availability=2),
    "rapier": WeaponData("Rapier", damage=1, initiative_mod=-2, weapon_type="melee",
                        size=2, strength_req=1, availability=2, tags="piercing_1"),
    "sword": WeaponData("Sword", damage=3, initiative_mod=-3, weapon_type="melee",
                       size=3, strength_req=2, availability=3),
    
    # MELEE WEAPONS - BLUNT
    "brass_knuckles": WeaponData("Brass Knuckles", damage=0, initiative_mod=0, weapon_type="melee",
                                size=1, strength_req=1, availability=1, tags="brawl"),
    "metal_club": WeaponData("Metal Club", damage=2, initiative_mod=-2, weapon_type="melee",
                            size=2, strength_req=2, availability=1, tags="stun"),
    "nightstick": WeaponData("Nightstick", damage=1, initiative_mod=-1, weapon_type="melee",
                            size=2, strength_req=2, availability=2, tags="stun"),
    "nunchaku": WeaponData("Nunchaku", damage=1, initiative_mod=1, weapon_type="melee",
                          size=2, strength_req=2, availability=2, tags="stun, dexterity_requirement"),
    "sap": WeaponData("Sap", damage=0, initiative_mod=-1, weapon_type="melee",
                     size=2, strength_req=2, availability=1, tags="stun"),
    "sledgehammer": WeaponData("Sledgehammer", damage=3, initiative_mod=-4, weapon_type="melee",
                              size=3, strength_req=3, availability=1, tags="knockdown, stun"),
    
    # MELEE WEAPONS - EXOTIC
    "catchpole": WeaponData("Catchpole", damage=0, initiative_mod=-3, weapon_type="melee",
                           size=2, strength_req=2, availability=1, tags="grapple, reach"),
    "chain": WeaponData("Chain", damage=1, initiative_mod=-3, weapon_type="melee",
                       size=2, strength_req=2, availability=1, tags="grapple, inaccurate, reach"),
    "chainsaw": WeaponData("Chainsaw", damage=3, initiative_mod=-6, weapon_type="melee",
                          size=3, strength_req=4, availability=3, tags="bleed, inaccurate, two-handed"),
    "whip": WeaponData("Whip", damage=0, initiative_mod=-2, weapon_type="melee",
                      size=2, strength_req=1, availability=1, tags="grapple, stun, dexterity_weaponry"),
    "tiger_claws": WeaponData("Tiger Claws", damage=1, initiative_mod=-1, weapon_type="melee",
                             size=2, strength_req=2, availability=2, tags="brawl"),
    "shield_small": WeaponData("Small Shield", damage=0, initiative_mod=-2, weapon_type="melee",
                              size=2, strength_req=2, availability=2, tags="concealed"),
    "shield_large": WeaponData("Large Shield", damage=2, initiative_mod=-4, weapon_type="melee",
                              size=3, strength_req=3, availability=2, tags="concealed"),
    
    # MELEE WEAPONS - IMPROVISED
    "blowtorch": WeaponData("Blowtorch", damage=0, initiative_mod=-2, weapon_type="melee",
                           size=2, strength_req=2, availability=2, tags="incendiary, piercing_2"),
    "board_with_nail": WeaponData("Board with Nail", damage=1, initiative_mod=-3, weapon_type="melee",
                                 size=2, strength_req=2, availability=0, tags="fragile, stun"),
    "improvised_shield": WeaponData("Improvised Shield", damage=0, initiative_mod=-4, weapon_type="melee",
                                   size=2, strength_req=2, availability=1, tags="concealed"),
    "shovel": WeaponData("Shovel", damage=1, initiative_mod=-3, weapon_type="melee",
                        size=2, strength_req=2, availability=1, tags="knockdown"),
    "tire_iron": WeaponData("Tire Iron", damage=1, initiative_mod=-3, weapon_type="melee",
                           size=2, strength_req=2, availability=2, tags="guard, inaccurate"),
    
    # MELEE WEAPONS - POLEARMS
    "spear": WeaponData("Spear", damage=2, initiative_mod=-2, weapon_type="melee",
                       size=4, strength_req=2, availability=1, tags="reach, two-handed"),
    "staff": WeaponData("Staff", damage=1, initiative_mod=-1, weapon_type="melee",
                       size=4, strength_req=2, availability=1, tags="knockdown, reach, two-handed"),
    
    # RANGED WEAPONS - ARCHERY
    "short_bow": WeaponData("Short Bow", damage=2, initiative_mod=-3, weapon_type="ranged",
                           size=3, strength_req=2, availability=2, capacity="low"),
    "long_bow": WeaponData("Long Bow", damage=3, initiative_mod=-4, weapon_type="ranged",
                          size=4, strength_req=3, availability=2, capacity="low"),
    "crossbow": WeaponData("Crossbow", damage=2, initiative_mod=-5, weapon_type="ranged",
                          size=3, strength_req=3, availability=3, capacity="low"),
    
    # RANGED WEAPONS - FIREARMS
    "light_pistol": WeaponData("Light Pistol", damage=1, initiative_mod=0, weapon_type="ranged",
                              size=1, strength_req=2, availability=2, capacity="medium"),
    "heavy_pistol": WeaponData("Heavy Pistol", damage=2, initiative_mod=-2, weapon_type="ranged",
                              size=1, strength_req=3, availability=3, capacity="medium"),
    "light_revolver": WeaponData("Light Revolver", damage=1, initiative_mod=0, weapon_type="ranged",
                                size=2, strength_req=2, availability=2, capacity="low"),
    "heavy_revolver": WeaponData("Heavy Revolver", damage=2, initiative_mod=-2, weapon_type="ranged",
                                size=3, strength_req=3, availability=2, capacity="low"),
    "smg_small": WeaponData("Small SMG", damage=1, initiative_mod=-2, weapon_type="ranged",
                           size=1, strength_req=2, availability=3, capacity="high"),
    "smg_heavy": WeaponData("Heavy SMG", damage=2, initiative_mod=-3, weapon_type="ranged",
                           size=2, strength_req=3, availability=3, capacity="high"),
    "rifle": WeaponData("Rifle", damage=4, initiative_mod=-5, weapon_type="ranged",
                       size=3, strength_req=2, availability=2, capacity="low"),
    "big_game_rifle": WeaponData("Big Game Rifle", damage=5, initiative_mod=-5, weapon_type="ranged",
                                size=4, strength_req=3, availability=5, capacity="low", tags="stun"),
    "assault_rifle": WeaponData("Assault Rifle", damage=3, initiative_mod=-3, weapon_type="ranged",
                               size=3, strength_req=3, availability=3, capacity="high", tags="9-again"),
    "shotgun": WeaponData("Shotgun", damage=3, initiative_mod=-4, weapon_type="ranged",
                         size=2, strength_req=3, availability=2, capacity="low", tags="9-again"),
    
    # RANGED WEAPONS - NONLETHAL
    "pepper_spray": WeaponData("Pepper Spray", damage=0, initiative_mod=0, weapon_type="ranged",
                              size=1, strength_req=1, availability=1, capacity="low", tags="slow"),
    "stun_gun_ranged": WeaponData("Stun Gun (Ranged)", damage=0, initiative_mod=-1, weapon_type="ranged",
                                 size=1, strength_req=1, availability=1, capacity="medium", tags="slow, stun"),
    
    # THROWN WEAPONS
    "throwing_knife": WeaponData("Throwing Knife", damage=0, initiative_mod=0, weapon_type="thrown",
                                size=1, strength_req=1, availability=1, tags="thrown"),
    "molotov_cocktail": WeaponData("Molotov Cocktail", damage=1, initiative_mod=-2, weapon_type="thrown",
                                  size=2, strength_req=2, availability=1, tags="incendiary"),
    
    # ADDITIONAL EXOTIC WEAPONS
    "kusari_gama_chain": WeaponData("Kusari Gama (Chain)", damage=1, initiative_mod=-3, weapon_type="melee",
                                   size=2, strength_req=2, availability=1, tags="grapple, inaccurate, reach"),
    "kusari_gama_sickle": WeaponData("Kusari Gama (Sickle)", damage=1, initiative_mod=-1, weapon_type="melee",
                                    size=2, strength_req=1, availability=2),
    "stake": WeaponData("Stake", damage=0, initiative_mod=-4, weapon_type="melee",
                       size=1, strength_req=1, availability=0),
    "stun_gun_melee": WeaponData("Stun Gun (Melee)", damage=0, initiative_mod=-1, weapon_type="melee",
                                size=1, strength_req=1, availability=1, tags="stun, no_bonus_damage"),
    
    # EXPLOSIVES - GRENADES
    "frag_grenade_standard": WeaponData("Frag Grenade (Standard)", damage=2, initiative_mod=0, weapon_type="thrown",
                                       size=1, strength_req=2, availability=4, tags="knockdown, stun, blast_10, force_3"),
    "frag_grenade_heavy": WeaponData("Frag Grenade (Heavy)", damage=3, initiative_mod=-1, weapon_type="thrown",
                                    size=1, strength_req=2, availability=4, tags="knockdown, stun, blast_5, force_4"),
    "pipe_bomb": WeaponData("Pipe Bomb", damage=1, initiative_mod=-1, weapon_type="thrown",
                           size=1, strength_req=2, availability=1, tags="inaccurate, stun, blast_5, force_2"),
    "smoke_grenade": WeaponData("Smoke Grenade", damage=0, initiative_mod=0, weapon_type="thrown",
                               size=1, strength_req=2, availability=2, tags="concealment, blast_10"),
    "stun_grenade": WeaponData("Stun Grenade", damage=0, initiative_mod=0, weapon_type="thrown",
                              size=1, strength_req=2, availability=2, tags="knockdown, stun, blast_5, force_2"),
    "thermite_grenade": WeaponData("Thermite Grenade", damage=3, initiative_mod=0, weapon_type="thrown",
                                  size=1, strength_req=2, availability=4, tags="ap_8, incendiary, blast_5, force_4"),
    "white_phosphorous": WeaponData("White Phosphorous", damage=3, initiative_mod=0, weapon_type="thrown",
                                   size=1, strength_req=2, availability=4, tags="ap_3, incendiary, concealment, blast_5, force_4"),
    
    # EXPLOSIVES - LAUNCHERS
    "grenade_launcher_standalone": WeaponData("Grenade Launcher (Standalone)", damage=0, initiative_mod=-5, weapon_type="ranged",
                                             size=3, strength_req=3, availability=4, capacity="low", tags="heavy_recoil"),
    "grenade_launcher_underbarrel": WeaponData("Grenade Launcher (Underbarrel)", damage=0, initiative_mod=-3, weapon_type="ranged",
                                              size=2, strength_req=2, availability=4, capacity="low", tags="attachment"),
    "automatic_grenade_launcher": WeaponData("Automatic Grenade Launcher", damage=0, initiative_mod=-6, weapon_type="ranged",
                                            size=4, strength_req=0, availability=5, capacity="high", tags="vehicle_mounted"),
    
    # GRENADE AMMUNITION
    "baton_round": WeaponData("Baton Round", damage=1, initiative_mod=0, weapon_type="ranged",
                             size=1, strength_req=0, availability=2, capacity="single", tags="knockdown, stun, force_5"),
    "buckshot_round": WeaponData("Buckshot Round", damage=1, initiative_mod=0, weapon_type="ranged",
                                size=1, strength_req=0, availability=4, capacity="single", tags="knockdown, blast_10, force_4"),
    "he_round": WeaponData("HE Round", damage=3, initiative_mod=0, weapon_type="ranged",
                          size=1, strength_req=0, availability=4, capacity="single", tags="knockdown, blast_10, force_4"),
    "hedp_round": WeaponData("HEDP Round", damage=2, initiative_mod=0, weapon_type="ranged",
                            size=1, strength_req=0, availability=4, capacity="single", tags="knockdown, ap_4, blast_10, force_3"),
    
    # HEAVY WEAPONS - FLAMETHROWERS
    "flamethrower_civilian": WeaponData("Flamethrower (Civilian)", damage=0, initiative_mod=-4, weapon_type="ranged",
                                       size=4, strength_req=3, availability=3, capacity="high", tags="incendiary"),
    "flamethrower_military": WeaponData("Flamethrower (Military)", damage=0, initiative_mod=-5, weapon_type="ranged",
                                       size=4, strength_req=3, availability=5, capacity="high", tags="incendiary"),
}

# Armor definitions from Chronicles of Darkness: Hurt Locker
ARMOR_DATABASE = {
    # MODERN ARMOR
    "reinforced_clothing": ArmorData("Reinforced Clothing", general_armor=1, ballistic_armor=0,
                                    strength_req=1, defense_penalty=0, speed_penalty=0, availability=1,
                                    coverage=["torso", "arms", "legs"]),
    "sports_gear": ArmorData("Sports Gear", general_armor=2, ballistic_armor=0,
                            strength_req=2, defense_penalty=-1, speed_penalty=-1, availability=1,
                            coverage=["torso", "arms", "legs"]),
    "kevlar_vest": ArmorData("Kevlar Vest", general_armor=1, ballistic_armor=3,
                            strength_req=1, defense_penalty=0, speed_penalty=0, availability=1,
                            coverage=["torso"]),
    "flak_jacket": ArmorData("Flak Jacket", general_armor=2, ballistic_armor=4,
                            strength_req=1, defense_penalty=-1, speed_penalty=0, availability=2,
                            coverage=["torso", "arms"]),
    "full_riot_gear": ArmorData("Full Riot Gear", general_armor=3, ballistic_armor=5,
                               strength_req=2, defense_penalty=-2, speed_penalty=-1, availability=3,
                               coverage=["torso", "arms", "legs"]),
    "bomb_suit": ArmorData("Bomb Suit", general_armor=4, ballistic_armor=6,
                          strength_req=3, defense_penalty=-5, speed_penalty=-4, availability=5,
                          coverage=["torso", "arms", "head"]),
    "helmet_modern": ArmorData("Modern Helmet", general_armor=0, ballistic_armor=0,
                              strength_req=2, defense_penalty=-1, speed_penalty=0, availability=3,
                              coverage=["head"],
                              notes="Extends armor protection to head. Half of worn armor's normal ratings (rounded up). -1 to sight/hearing Perception rolls"),   
    # ARCHAIC ARMOR
    "leather_hard": ArmorData("Hard Leather", general_armor=2, ballistic_armor=0,
                             strength_req=2, defense_penalty=-1, speed_penalty=0, availability=1,
                             coverage=["torso", "arms"]),
    "chainmail": ArmorData("Chainmail", general_armor=3, ballistic_armor=1,
                          strength_req=3, defense_penalty=-2, speed_penalty=-2, availability=2,
                          coverage=["torso", "arms"],
                          notes="Full suit can protect entire body at additional cost"),
    "plate_mail": ArmorData("Plate Mail", general_armor=4, ballistic_armor=2,
                           strength_req=3, defense_penalty=-2, speed_penalty=-3, availability=4,
                           coverage=["torso", "arms", "legs"]),
    "helmet_archaic": ArmorData("Archaic Helmet", general_armor=0, ballistic_armor=0,
                               strength_req=2, defense_penalty=-1, speed_penalty=0, availability=3,
                               coverage=["head"],
                               notes="Extends armor protection to head. Half of worn armor's normal ratings (rounded up). -1 to sight/hearing Perception rolls"),
    "lorica_segmentata": ArmorData("Lorica Segmentata", general_armor=2, ballistic_armor=2,
                                  strength_req=3, defense_penalty=-2, speed_penalty=-3, availability=4,
                                  coverage=["torso"]),
}

# Tag descriptions for reference
WEAPON_TAG_DESCRIPTIONS = {
    "8-again": "Re-roll 8s, 9s, and 10s on attack rolls",
    "9-again": "Re-roll 9s and 10s on attack rolls", 
    "accurate": "+1 to attack rolls",
    "bleed": "Doubles weapon bonus for Bleeding Tilt",
    "brawl": "Uses Brawl skill, enhanced by unarmed bonuses",
    "concealed": "Adds Size to Defense when used defensively",
    "enhance_crafts_survival": "Provides bonus to Crafts or Survival rolls",
    "fragile": "-1 to weapon's Durability",
    "grapple": "Adds weapon dice to grapple rolls",
    "guard": "+1 Defense when wielding",
    "inaccurate": "-1 penalty to attack rolls",
    "incendiary": "Causes Burning Tilt",
    "knockdown": "Doubles weapon bonus for Knockdown Tilt",
    "piercing_1": "Armor Piercing 1 - reduces armor by 1",
    "piercing_2": "Armor Piercing 2 - reduces armor by 2", 
    "reach": "+1 Defense vs smaller weapons, -1 penalty in grapples",
    "slow": "Target gains full Defense against attack",
    "stun": "Doubles weapon bonus for Stun Tilt", 
    "thrown": "Can be thrown as ranged attack",
    "two-handed": "Requires two hands, can use one-handed at +1 Strength requirement"
}


WEAPON_DATA = {
    # MELEE WEAPONS - BLADED
    "battle_axe": {"damage": 3, "initiative": -4, "strength": 3, "size": 3, "tags": "9-again, two-handed", "range": "melee", "availability": 3},
    "fire_axe": {"damage": 2, "initiative": -4, "strength": 3, "size": 3, "tags": "9-again, two-handed", "range": "melee", "availability": 2},
    "great_sword": {"damage": 4, "initiative": -5, "strength": 4, "size": 3, "tags": "9-again, two-handed", "range": "melee", "availability": 4},
    "hatchet": {"damage": 1, "initiative": -2, "strength": 1, "size": 1, "tags": "", "range": "melee", "availability": 2},
    "knife_small": {"damage": 0, "initiative": 0, "strength": 1, "size": 1, "tags": "thrown", "range": "melee", "availability": 1},
    "knife_hunting": {"damage": 1, "initiative": -1, "strength": 1, "size": 2, "tags": "enhance_crafts_survival", "range": "melee", "availability": 2},
    "machete": {"damage": 2, "initiative": -2, "strength": 2, "size": 2, "tags": "", "range": "melee", "availability": 2},
    "rapier": {"damage": 1, "initiative": -2, "strength": 1, "size": 2, "tags": "piercing_1", "range": "melee", "availability": 2},
    "sword": {"damage": 3, "initiative": -3, "strength": 2, "size": 3, "tags": "initiative_bonus_1", "range": "melee", "availability": 3},

    # MELEE WEAPONS - BLUNT
    "brass_knuckles": {"damage": 0, "initiative": 0, "strength": 1, "size": 1, "tags": "brawl", "range": "melee", "availability": 1},
    "metal_club": {"damage": 2, "initiative": -2, "strength": 2, "size": 2, "tags": "stun", "range": "melee", "availability": 1},
    "nightstick": {"damage": 1, "initiative": -1, "strength": 2, "size": 2, "tags": "stun", "range": "melee", "availability": 2},
    "nunchaku": {"damage": 1, "initiative": 1, "strength": 2, "size": 2, "tags": "stun, dexterity_requirement", "range": "melee", "availability": 2},
    "sap": {"damage": 0, "initiative": -1, "strength": 2, "size": 2, "tags": "stun", "range": "melee", "availability": 1},
    "sledgehammer": {"damage": 3, "initiative": -4, "strength": 3, "size": 3, "tags": "knockdown, stun", "range": "melee", "availability": 1},

    # MELEE WEAPONS - EXOTIC
    "catchpole": {"damage": 0, "initiative": -3, "strength": 2, "size": 2, "tags": "grapple, reach", "range": "melee", "availability": 1},
    "chain": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "grapple, inaccurate, reach", "range": "melee", "availability": 1},
    "chainsaw": {"damage": 3, "initiative": -6, "strength": 4, "size": 3, "tags": "bleed, inaccurate, two-handed", "range": "melee", "availability": 3},
    "kusari_gama_chain": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "grapple, inaccurate, reach", "range": "melee", "availability": 1},
    "kusari_gama_sickle": {"damage": 1, "initiative": -1, "strength": 1, "size": 2, "tags": "", "range": "melee", "availability": 2},
    "shield_small": {"damage": 0, "initiative": -2, "strength": 2, "size": 2, "tags": "concealed", "range": "melee", "availability": 2},
    "shield_large": {"damage": 2, "initiative": -4, "strength": 3, "size": 3, "tags": "concealed", "range": "melee", "availability": 2},
    "stake": {"damage": 0, "initiative": -4, "strength": 1, "size": 1, "tags": "", "range": "melee", "availability": 0},
    "stun_gun_melee": {"damage": 0, "initiative": -1, "strength": 1, "size": 1, "tags": "stun, no_bonus_damage", "range": "melee", "availability": 1},
    "tiger_claws": {"damage": 1, "initiative": -1, "strength": 2, "size": 2, "tags": "brawl", "range": "melee", "availability": 2},
    "whip": {"damage": 0, "initiative": -2, "strength": 1, "size": 2, "tags": "grapple, stun, dexterity_weaponry", "range": "melee", "availability": 1},

    # MELEE WEAPONS - IMPROVISED
    "blowtorch": {"damage": 0, "initiative": -2, "strength": 2, "size": 2, "tags": "incendiary, piercing_2, blinded_tilt", "range": "melee", "availability": 2},
    "board_with_nail": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "fragile, stun", "range": "melee", "availability": 0},
    "improvised_shield": {"damage": 0, "initiative": -4, "strength": 2, "size": 2, "tags": "concealed", "range": "melee", "availability": 1},
    "nail_gun": {"damage": 0, "initiative": -2, "strength": 2, "size": 2, "tags": "inaccurate, piercing_1, strength_firearms", "range": "melee", "availability": 1},
    "shovel": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "knockdown", "range": "melee", "availability": 1},
    "tire_iron": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "guard, inaccurate", "range": "melee", "availability": 2},

    # MELEE WEAPONS - POLEARMS
    "spear": {"damage": 2, "initiative": -2, "strength": 2, "size": 4, "tags": "reach, two-handed", "range": "melee", "availability": 1},
    "staff": {"damage": 1, "initiative": -1, "strength": 2, "size": 4, "tags": "knockdown, reach, two-handed", "range": "melee", "availability": 1},

    # RANGED WEAPONS - ARCHERY
    "short_bow": {"damage": 2, "range": "medium", "capacity": "low", "initiative": -3, "strength": 2, "size": 3, "availability": 2, "tags": ""},
    "long_bow": {"damage": 3, "range": "medium", "capacity": "low", "initiative": -4, "strength": 3, "size": 4, "availability": 2, "tags": ""},
    "crossbow": {"damage": 2, "range": "long", "capacity": "low", "initiative": -5, "strength": 3, "size": 3, "availability": 3, "tags": ""},

    # RANGED WEAPONS - THROWN
    "throwing_knife": {"damage": 0, "range": "close", "capacity": "single", "initiative": 0, "strength": 1, "size": 1, "availability": 1, "tags": "thrown"},

    # RANGED WEAPONS - FIREARMS
    "light_pistol": {"damage": 1, "range": "long", "capacity": "medium", "initiative": 0, "strength": 2, "size": 1, "availability": 2, "tags": ""},
    "heavy_pistol": {"damage": 2, "range": "long", "capacity": "medium", "initiative": -2, "strength": 3, "size": 1, "availability": 3, "tags": ""},
    "light_revolver": {"damage": 1, "range": "long", "capacity": "low", "initiative": 0, "strength": 2, "size": 2, "availability": 2, "tags": ""},
    "heavy_revolver": {"damage": 2, "range": "long", "capacity": "low", "initiative": -2, "strength": 3, "size": 3, "availability": 2, "tags": ""},
    "smg_small": {"damage": 1, "range": "medium", "capacity": "high", "initiative": -2, "strength": 2, "size": 1, "availability": 3, "tags": ""},
    "smg_heavy": {"damage": 2, "range": "medium", "capacity": "high", "initiative": -3, "strength": 3, "size": 2, "availability": 3, "tags": ""},
    "rifle": {"damage": 4, "range": "extreme", "capacity": "low", "initiative": -5, "strength": 2, "size": 3, "availability": 2, "tags": ""},
    "big_game_rifle": {"damage": 5, "range": "extreme", "capacity": "low", "initiative": -5, "strength": 3, "size": 4, "availability": 5, "tags": "stun"},
    "assault_rifle": {"damage": 3, "range": "long", "capacity": "high", "initiative": -3, "strength": 3, "size": 3, "availability": 3, "tags": "9-again"},
    "shotgun": {"damage": 3, "range": "medium", "capacity": "low", "initiative": -4, "strength": 3, "size": 2, "availability": 2, "tags": "9-again"},

    # RANGED WEAPONS - NONLETHAL
    "pepper_spray": {"damage": 0, "range": "close", "capacity": "low", "initiative": 0, "strength": 1, "size": 1, "availability": 1, "tags": "slow"},
    "stun_gun_ranged": {"damage": 0, "range": "close", "capacity": "medium", "initiative": -1, "strength": 1, "size": 1, "availability": 1, "tags": "slow, stun, no_bonus_damage"},

    # EXPLOSIVES - GRENADES
    "frag_grenade_standard": {"damage": 2, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 4, "tags": "knockdown, stun, blast_10, force_3"},
    "frag_grenade_heavy": {"damage": 3, "range": "thrown", "capacity": "single", "initiative": -1, "strength": 2, "size": 1, "availability": 4, "tags": "knockdown, stun, blast_5, force_4"},
    "molotov_cocktail": {"damage": 1, "range": "thrown", "capacity": "single", "initiative": -2, "strength": 2, "size": 2, "availability": 1, "tags": "incendiary, blast_3, force_2"},
    "pipe_bomb": {"damage": 1, "range": "thrown", "capacity": "single", "initiative": -1, "strength": 2, "size": 1, "availability": 1, "tags": "inaccurate, stun, blast_5, force_2"},
    "smoke_grenade": {"damage": 0, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 2, "tags": "concealment, blast_10"},
    "stun_grenade": {"damage": 0, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 2, "tags": "knockdown, stun, blast_5, force_2"},
    "thermite_grenade": {"damage": 3, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 4, "tags": "ap_8, incendiary, blast_5, force_4"},
    "white_phosphorous": {"damage": 3, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 4, "tags": "ap_3, incendiary, concealment, blast_5, force_4"},

    # EXPLOSIVES - GRENADE LAUNCHERS
    "grenade_launcher_standalone": {"damage": "varies", "range": "long", "capacity": "low", "initiative": -5, "strength": 3, "size": 3, "availability": 4, "tags": "heavy_recoil"},
    "grenade_launcher_underbarrel": {"damage": "varies", "range": "long", "capacity": "low", "initiative": -3, "strength": 2, "size": 2, "availability": 4, "tags": "attachment"},
    "automatic_grenade_launcher": {"damage": "varies", "range": "extreme", "capacity": "high", "initiative": -6, "strength": 0, "size": 4, "availability": 5, "tags": "vehicle_mounted"},

    # EXPLOSIVES - GRENADE AMMUNITION
    "baton_round": {"damage": 1, "range": "long", "capacity": "single", "initiative": 0, "strength": 0, "size": 1, "availability": 2, "tags": "knockdown, stun, force_5"},
    "buckshot_round": {"damage": 1, "range": "long", "capacity": "single", "initiative": 0, "strength": 0, "size": 1, "availability": 4, "tags": "knockdown, blast_10, force_4"},
    "he_round": {"damage": 3, "range": "long", "capacity": "single", "initiative": 0, "strength": 0, "size": 1, "availability": 4, "tags": "knockdown, blast_10, force_4"},
    "hedp_round": {"damage": 2, "range": "long", "capacity": "single", "initiative": 0, "strength": 0, "size": 1, "availability": 4, "tags": "knockdown, ap_4, blast_10, force_3"},

    # HEAVY WEAPONS - FLAMETHROWERS
    "flamethrower_civilian": {"damage": "special", "range": "short", "capacity": "high", "initiative": -4, "strength": 3, "size": 4, "availability": 3, "tags": "incendiary"},
    "flamethrower_military": {"damage": "special", "range": "medium", "capacity": "high", "initiative": -5, "strength": 3, "size": 4, "availability": 5, "tags": "incendiary"},
}

# ARMOR DATABASE
# Rating: First number is general armor (reduces total damage), second is ballistic armor (downgrades lethal to bashing)
# Strength: Minimum Strength requirement. Lower Strength causes -1 to Brawl and Weaponry rolls
# Defense: Defense penalty while wearing armor
# Speed: Speed penalty while wearing armor  
# Availability: Cost in Resources dots or appropriate Social Merit level
# Coverage: Body areas protected by the armor

ARMOR_DATA = {
    # MODERN ARMOR
    "reinforced_clothing": {
        "general_armor": 1, 
        "ballistic_armor": 0, 
        "strength": 1, 
        "defense": 0, 
        "speed": 0, 
        "availability": 1, 
        "coverage": ["torso", "arms", "legs"]
    },
    "sports_gear": {
        "general_armor": 2, 
        "ballistic_armor": 0, 
        "strength": 2, 
        "defense": -1, 
        "speed": -1, 
        "availability": 1, 
        "coverage": ["torso", "arms", "legs"]
    },
    "kevlar_vest": {
        "general_armor": 1, 
        "ballistic_armor": 3, 
        "strength": 1, 
        "defense": 0, 
        "speed": 0, 
        "availability": 1, 
        "coverage": ["torso"]
    },
    "flak_jacket": {
        "general_armor": 2, 
        "ballistic_armor": 4, 
        "strength": 1, 
        "defense": -1, 
        "speed": 0, 
        "availability": 2, 
        "coverage": ["torso", "arms"]
    },
    "full_riot_gear": {
        "general_armor": 3, 
        "ballistic_armor": 5, 
        "strength": 2, 
        "defense": -2, 
        "speed": -1, 
        "availability": 3, 
        "coverage": ["torso", "arms", "legs"]
    },
    "bomb_suit": {
        "general_armor": 4, 
        "ballistic_armor": 6, 
        "strength": 3, 
        "defense": -5, 
        "speed": -4, 
        "availability": 5, 
        "coverage": ["torso", "arms", "head"]
    },
    "helmet_modern": {
        "general_armor": "special", 
        "ballistic_armor": "special", 
        "strength": 2, 
        "defense": -1, 
        "speed": 0, 
        "availability": 3, 
        "coverage": ["head"],
        "notes": "Extends armor protection to head. Half of worn armor's normal ratings (rounded up). -1 to sight/hearing Perception rolls"
    },

    # ARCHAIC ARMOR
    "leather_hard": {
        "general_armor": 2, 
        "ballistic_armor": 0, 
        "strength": 2, 
        "defense": -1, 
        "speed": 0, 
        "availability": 1, 
        "coverage": ["torso", "arms"]
    },
    "lorica_segmentata": {
        "general_armor": 2, 
        "ballistic_armor": 2, 
        "strength": 3, 
        "defense": -2, 
        "speed": -3, 
        "availability": 4, 
        "coverage": ["torso"]
    },
    "chainmail": {
        "general_armor": 3, 
        "ballistic_armor": 1, 
        "strength": 3, 
        "defense": -2, 
        "speed": -2, 
        "availability": 2, 
        "coverage": ["torso", "arms"],
        "notes": "Full suit can protect entire body at additional cost of one dot"
    },
    "plate_mail": {
        "general_armor": 4, 
        "ballistic_armor": 2, 
        "strength": 3, 
        "defense": -2, 
        "speed": -3, 
        "availability": 4, 
        "coverage": ["torso", "arms", "legs"]
    },
    "helmet_archaic": {
        "general_armor": "special", 
        "ballistic_armor": "special", 
        "strength": 2, 
        "defense": -1, 
        "speed": 0, 
        "availability": 3, 
        "coverage": ["head"],
        "notes": "Extends armor protection to head. Half of worn armor's normal ratings (rounded up). -1 to sight/hearing Perception rolls"
    }
}

# Armor mechanics notes
armor_rules = {
    "general_armor": "Reduces total damage taken by one point per level, starting with most severe damage type",
    "ballistic_armor": "Each point downgrades one point of lethal damage from firearms to bashing damage",
    "application_order": "Apply ballistic armor first, then general armor",
    "minimum_damage": "Successful attack always inflicts at least one bashing damage to armored mortal target",
    "supernatural_exception": "Vampires, spell-protected mages, and werewolves with thick hides are not subject to minimum damage rule",
    "called_shots": "If attacker targets unarmored location, armor protection doesn't apply",
    "riot_shields": "Sometimes come with large bulletproof shields (ballistic armor 2, stacks with armor ratings)"
}

# Coverage area definitions
coverage_areas = {
    "head": "Head and face protection",
    "torso": "Chest, back, and vital organs", 
    "arms": "Arms and shoulders",
    "legs": "Legs and lower body"
}

# Capacity definitions
capacity_types = {
    "single": "Single use per scene",
    "low": "Empties on short burst or failure",
    "medium": "Empties on medium burst, two short bursts, or dramatic failure", 
    "high": "Empties on long burst, two medium bursts, or three short bursts"
}

# Range definitions
range_types = {
    "melee": "Personal space (0-2 meters)",
    "close": "0-5 meters", 
    "short": "5-30 meters",
    "medium": "30-100 meters", 
    "long": "100-300 meters",
    "extreme": "300+ meters",
    "thrown": "Varies by Strength and weapon type"
}

# Availability definitions
availability_costs = {
    0: "Free/No cost",
    1: "• (1 Resources dot or appropriate Social Merit)",
    2: "•• (2 Resources dots or appropriate Social Merit)", 
    3: "••• (3 Resources dots or appropriate Social Merit)",
    4: "•••• (4 Resources dots or appropriate Social Merit)",
    5: "••••• (5 Resources dots or appropriate Social Merit)"
}

# Tag definitions
tag_descriptions = {
    "9-again": "Re-roll 9s and 10s on attack rolls",
    "8-again": "Re-roll 8s, 9s, and 10s on attack rolls", 
    "accurate": "+1 to attack rolls",
    "ap_3": "Armor Piercing 3 - reduces armor by 3",
    "ap_4": "Armor Piercing 4 - reduces armor by 4", 
    "ap_8": "Armor Piercing 8 - reduces armor by 8",
    "bleed": "Doubles weapon bonus for Bleeding Tilt",
    "blast_3": "3 meter blast radius",
    "blast_5": "5 meter blast radius", 
    "blast_10": "10 meter blast radius",
    "brawl": "Uses Brawl skill, enhanced by unarmed bonuses",
    "concealed": "Adds Size to Defense when used defensively",
    "concealment": "Provides concealment modifier",
    "dexterity_requirement": "-1 Damage and Initiative without Dexterity 3+",
    "dexterity_weaponry": "Uses Dexterity + Weaponry to attack",
    "enhance_crafts_survival": "Provides bonus to Crafts or Survival rolls",
    "force_2": "Force rating 2 for explosive knockback",
    "force_3": "Force rating 3 for explosive knockback",
    "force_4": "Force rating 4 for explosive knockback", 
    "force_5": "Force rating 5 for explosive knockback",
    "fragile": "-1 to weapon's Durability",
    "grapple": "Adds weapon dice to grapple rolls",
    "guard": "+1 Defense when wielding",
    "heavy_recoil": "Causes Knocked Down Tilt if not properly braced",
    "inaccurate": "-1 penalty to attack rolls",
    "incendiary": "Causes Burning Tilt",
    "initiative_bonus_1": "+1 Initiative when wielding",
    "knockdown": "Doubles weapon bonus for Knockdown Tilt",
    "no_bonus_damage": "Bonus successes don't add to damage",
    "piercing_1": "Armor Piercing 1 - reduces armor by 1",
    "piercing_2": "Armor Piercing 2 - reduces armor by 2", 
    "reach": "+1 Defense vs smaller weapons, -1 penalty in grapples",
    "slow": "Target gains full Defense against attack",
    "strength_firearms": "Uses Strength + Firearms to attack",
    "stun": "Doubles weapon bonus for Stun Tilt", 
    "thrown": "Can be thrown as ranged attack",
    "two-handed": "Requires two hands, can use one-handed at +1 Strength requirement"
}
