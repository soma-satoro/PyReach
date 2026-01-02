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

# ========================================
# GENERAL EQUIPMENT DATABASE
# ========================================

GENERAL_EQUIPMENT_DATABASE = {
    # ========================================
    # FIREARM ACCESSORIES
    # ========================================
    "bipod": EquipmentData(
        name="Bipod",
        category="firearm_accessories",
        die_bonus=1,
        durability=2,
        size=2,
        structure=4,
        availability=1,
        effect="Helps stabilize a weapon when shooting at long range. Reduces penalty for firing at medium or long range by one. Reduces penalties for burst firing at multiple targets by one.",
        special_properties={"range_penalty_reduction": 1, "burst_penalty_reduction": 1}
    ),
    
    "ear_protection": EquipmentData(
        name="Ear Protection",
        category="firearm_accessories",
        die_bonus=-3,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Protects from being deafened by firearms discharge. Imposes -3 penalty to all sound-related Perception rolls.",
        skill_bonuses={"perception": -3},
        special_properties={"perception_type": "sound", "deafening_protection": True}
    ),
    
    "gunsmithing_kit": EquipmentData(
        name="Gunsmithing Kit",
        category="firearm_accessories",
        die_bonus=2,
        durability=2,
        size=2,
        structure=4,
        availability=2,
        effect="Provides tools needed to properly maintain, repair, or modify firearms. Requires extended Dexterity + Crafts roll (each roll = 15 minutes). Cleaning/simple repairs need 5 successes, complex repairs need 15 successes.",
        skill_bonuses={"crafts": 2},
        special_properties={"firearms_maintenance": True}
    ),
    
    "light_mount": EquipmentData(
        name="Light Mount",
        category="firearm_accessories",
        die_bonus=1,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Flashlight mounted on gun barrel. Subtracts die bonus from darkness penalties or adds to search rolls. Can blind targets but reveals shooter's position.",
        special_properties={"darkness_reduction": 1, "reveals_position": True}
    ),
    
    "light_mount_advanced": EquipmentData(
        name="Light Mount (Advanced)",
        category="firearm_accessories",
        die_bonus=2,
        durability=1,
        size=1,
        structure=2,
        availability=2,
        effect="High-intensity halogen or LED light mount. Subtracts die bonus from darkness penalties or adds to search rolls.",
        special_properties={"darkness_reduction": 2, "reveals_position": True}
    ),
    
    "reloading_bench": EquipmentData(
        name="Reloading Bench",
        category="firearm_accessories",
        die_bonus=2,
        durability=2,
        size=5,
        structure=6,
        availability=2,
        effect="Provides space and supplies to load custom bullets at home: gunpowder, shell casings, bullet press, polisher, etc. Allows secretive ammunition crafting or special bullet types.",
        skill_bonuses={"crafts": 2},
        special_properties={"ammunition_crafting": True}
    ),
    
    "sighting_tools": EquipmentData(
        name="Sighting Tools",
        category="firearm_accessories",
        die_bonus=2,
        durability=1,
        size=2,
        structure=3,
        availability=2,
        effect="Tools to maintain and realign gun sights. Extended Wits + Firearms action needing 10 successes. Successfully sighting in provides +1 to medium and long-range attacks for uses equal to 2x weapon Damage rating.",
        skill_bonuses={"firearms": 2},
        special_properties={"sight_alignment": True, "accuracy_bonus": 1}
    ),
    
    "speedloader": EquipmentData(
        name="Speedloader",
        category="firearm_accessories",
        die_bonus=0,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Allows quick reloading of revolvers and action-fed weapons without sacrificing Defense. Loads ammunition in small carousels or loads proper shotguns/rifles four rounds at a time.",
        special_properties={"quick_reload": True, "defense_maintained": True}
    ),
    
    "collapsible_stock": EquipmentData(
        name="Collapsible Stock",
        category="firearm_accessories",
        die_bonus=0,
        durability=2,
        size=0,
        structure=3,
        availability=2,
        effect="Folding or telescoping stock reduces weapon Size by 1 (minimum 2). Installation requires Dexterity + Crafts roll, 15 minutes per roll, 5 successes needed.",
        special_properties={"size_reduction": 1, "requires_installation": True}
    ),
    
    "suppressor": EquipmentData(
        name="Suppressor",
        category="firearm_accessories",
        die_bonus=0,
        durability=3,
        size=1,
        structure=4,
        availability=3,
        effect="Dampens noise and flash of firing gun. Bystanders within 50m suffer -4 to hearing-based Perception (subsonic ammo) or -2 within 100m (supersonic). Flash suppression inflicts -3 to pinpoint shooter location. Revolvers only get -2 penalty.",
        special_properties={"sound_dampening": 4, "flash_suppression": 3, "revolver_penalty": 2}
    ),
    
    # ========================================
    # SIGHTS
    # ========================================
    "fiber_optic_sight": EquipmentData(
        name="Fiber Optic Sight",
        category="sights",
        die_bonus=1,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Uses colored lights for precise shots. Gain additional +1 bonus when aiming. Works in any light conditions (red in daytime, green/yellow at night). Applies to firearms and bows.",
        special_properties={"aiming_bonus": 1, "all_weather": True}
    ),
    
    "laser_sight": EquipmentData(
        name="Laser Sight",
        category="sights",
        die_bonus=1,
        durability=1,
        size=1,
        structure=2,
        availability=2,
        effect="Greatly improves accuracy at short and medium ranges (no effect on long range). Visible red dot gives target die bonus to avoid surprise. In fog/dust, entire beam visible granting +1 to avoid surprise.",
        special_properties={"range_limit": "medium", "surprise_penalty": True}
    ),
    
    "laser_sight_infrared": EquipmentData(
        name="Laser Sight (Infrared)",
        category="sights",
        die_bonus=1,
        durability=1,
        size=1,
        structure=2,
        availability=3,
        effect="Infrared beam only visible with night vision. Can benefit from both infrared laser and night vision scope.",
        special_properties={"infrared": True, "requires_night_vision": True}
    ),
    
    "telescopic_scope": EquipmentData(
        name="Telescopic Scope",
        category="sights",
        die_bonus=0,
        durability=1,
        size=2,
        structure=3,
        availability=1,
        effect="Provides magnification over long distances. Ignore penalties for medium range, halve long range penalties.",
        special_properties={"medium_range_ignore": True, "long_range_halve": True}
    ),
    
    "night_vision_scope": EquipmentData(
        name="Night Vision Telescopic Sight",
        category="sights",
        die_bonus=0,
        durability=1,
        size=2,
        structure=3,
        availability=3,
        effect="Uses infrared lenses. Ignore darkness penalties at short and medium range, reduce long range penalty by one (to -3). Auto-shuts down in harsh light, returns 1 turn after exposure ends.",
        special_properties={"night_vision": True, "light_sensitive": True, "darkness_ignore_short_medium": True}
    ),
    
    "night_vision_scope_advanced": EquipmentData(
        name="Day/Night Telescopic Sight",
        category="sights",
        die_bonus=0,
        durability=1,
        size=2,
        structure=3,
        availability=4,
        effect="Advanced scope works normally in both light and darkness. Ignore darkness penalties at short and medium range, reduce long range penalty by one.",
        special_properties={"day_night": True, "darkness_ignore_short_medium": True}
    ),
    
    "thermal_scope": EquipmentData(
        name="Thermal Telescopic Sight",
        category="sights",
        die_bonus=0,
        durability=2,
        size=2,
        structure=4,
        availability=5,
        effect="Shows warm targets in white against cool blue background. Works day and night (some ambient light required). No short/medium range penalties, long range penalty reduced to -1. Doesn't help against undead or entities as warm as environment. At night: negates medium range penalties, halves long range.",
        special_properties={"thermal": True, "undead_ineffective": True, "day_night": True}
    ),
    
    # ========================================
    # SURVEILLANCE GEAR
    # ========================================
    "binoculars": EquipmentData(
        name="Binoculars",
        category="surveillance",
        die_bonus=0,
        durability=2,
        size=1,
        structure=3,
        availability=1,
        effect="Provides magnification over great distances. See clearly up to extreme range. At long range: -1 to sight Perception. At extreme range: -3 to sight Perception.",
        special_properties={"range_extension": "extreme", "long_range_penalty": -1, "extreme_range_penalty": -3}
    ),
    
    "binoculars_night_vision": EquipmentData(
        name="Night Vision Binoculars",
        category="surveillance",
        die_bonus=0,
        durability=2,
        size=1,
        structure=3,
        availability=3,
        effect="Binoculars with night vision. Similar penalties as regular binoculars but negates darkness penalties.",
        special_properties={"night_vision": True, "range_extension": "extreme"}
    ),
    
    "listening_device": EquipmentData(
        name="Listening Device (Bug)",
        category="surveillance",
        die_bonus=0,
        durability=1,
        size=1,
        structure=2,
        availability=2,
        effect="Small audio device (1-2 inches) transmits sounds to listeners/recorders. Planting requires Wits + Larceny. Finding: contested Wits + Investigation vs planter's Wits + Larceny. Range: quarter-mile via radio frequency.",
        special_properties={"audio_transmission": True, "range_meters": 402, "concealable": True}
    ),
    
    "listening_device_small": EquipmentData(
        name="Listening Device (Miniature)",
        category="surveillance",
        die_bonus=-1,
        durability=1,
        size=1,
        structure=2,
        availability=3,
        effect="Smaller bug that's harder to find. -1 penalty to Perception rolls to find it.",
        special_properties={"audio_transmission": True, "range_meters": 402, "harder_to_find": True}
    ),
    
    "bug_sweeper": EquipmentData(
        name="Bug Sweeper",
        category="surveillance",
        die_bonus=2,
        durability=1,
        size=1,
        structure=2,
        availability=3,
        effect="Scans for audio and video recording devices. Looks like small walkie-talkie. Scans radio frequencies and electromagnetic radiation. Adds die bonus to Wits + Investigation to find bugs.",
        skill_bonuses={"investigation": 2},
        special_properties={"bug_detection": True}
    ),
    
    "disguised_camera": EquipmentData(
        name="Disguised Camera",
        category="surveillance",
        die_bonus=0,
        durability=1,
        size=2,
        structure=3,
        availability=2,
        effect="Hidden cameras in clock radios, stuffed animals, smoke detectors, etc. Records video to internal storage (not transmission). ~2 hours recording time. Finding requires Wits + Investigation with penalty equal to Availability cost.",
        special_properties={"video_recording": True, "recording_hours": 2, "disguised": True}
    ),
    
    "disguised_camera_small": EquipmentData(
        name="Disguised Camera (Miniature)",
        category="surveillance",
        die_bonus=0,
        durability=1,
        size=1,
        structure=2,
        availability=3,
        effect="Smaller hidden camera, harder to find. More expensive models can record longer, higher resolution, or transmit wirelessly.",
        special_properties={"video_recording": True, "disguised": True, "miniature": True}
    ),
    
    "tracking_device": EquipmentData(
        name="Tracking Device",
        category="surveillance",
        die_bonus=2,
        durability=1,
        size=1,
        structure=2,
        availability=3,
        effect="Tiny microchip for tracking via GPS. Can be surgically implanted or installed in devices. Hiding: Wits + Larceny +2. Finding: Wits + Investigation vs concealment roll.",
        special_properties={"gps_tracking": True, "implantable": True}
    ),
    
    "keystroke_logger": EquipmentData(
        name="Keystroke Logger",
        category="surveillance",
        die_bonus=0,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Flash drive-like device captures keyboard inputs. Plugs between computer and keyboard. Logs passwords, emails, account numbers, everything typed. Installing surreptitiously: Wits + Computer.",
        skill_bonuses={"computer": 0},
        special_properties={"keylogging": True, "password_capture": True}
    ),
    
    "reverse_peephole": EquipmentData(
        name="Reverse Peephole",
        category="surveillance",
        die_bonus=0,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Looks like jeweler's loupe, allows looking IN through a peephole. Looking for something specific: Wits + Investigation at -4.",
        special_properties={"peephole_reversal": True}
    ),
    
    "spyware": EquipmentData(
        name="Spyware",
        category="surveillance",
        die_bonus=2,
        durability=0,
        size=0,
        structure=0,
        availability=2,
        effect="Software that tracks/monitors computer usage. Records keystrokes, web history, documents, chat logs. Remote installation requires hacking attempt.",
        skill_bonuses={"computer": 2},
        special_properties={"digital": True, "remote_installable": True}
    ),
    
    "wifi_sniffer": EquipmentData(
        name="Wi-Fi Sniffer",
        category="surveillance",
        die_bonus=0,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Small device scans for wireless networks within medium range. Shows signal strength. More discrete than laptops/phones. Doesn't allow network access itself.",
        special_properties={"network_scanning": True, "range": "medium"}
    ),
    
    "wiretap": EquipmentData(
        name="Wiretap",
        category="surveillance",
        die_bonus=0,
        durability=1,
        size=1,
        structure=2,
        availability=2,
        effect="Installed in phone or on phone line. Transmits conversations to third parties. Placing: Intelligence + Larceny, contested by Wits + Investigation if suspected.",
        special_properties={"phone_monitoring": True}
    ),
    
    # ========================================
    # SURVIVAL GEAR
    # ========================================
    "nbc_suit": EquipmentData(
        name="NBC Suit",
        category="survival",
        die_bonus=5,
        durability=1,
        size=5,
        structure=6,
        availability=2,
        effect="Nuclear, Biological, Chemical protection suit. Bulky plastic bodysuit with gas mask and air filtration. +5 to resist NBC agents including radiation. Single point of damage negates protection. After 5 days, bonus diminishes by 1 per day.",
        special_properties={"nbc_protection": 5, "fragile": True, "degrading": True}
    ),
    
    "potassium_iodide": EquipmentData(
        name="Bottle of Potassium Iodide",
        category="survival",
        die_bonus=1,
        durability=1,
        size=1,
        structure=2,
        availability=2,
        effect="Protects against radiation sickness. Two pills a day confer +1 to withstand up to level 3 radiation. Must be taken 4+ hours before exposure.",
        special_properties={"radiation_protection": 1, "dosage_required": True}
    ),
    
    "survival_kit_basic": EquipmentData(
        name="Basic Survival Kit",
        category="survival",
        die_bonus=1,
        durability=1,
        size=2,
        structure=3,
        availability=1,
        effect="Sleeping bag, canteen, flashlight, glowstick, food/water for 1 day. +1 to Survival rolls and Stamina + Resolve vs exposure.",
        skill_bonuses={"survival": 1},
        special_properties={"supplies_days": 1}
    ),
    
    "survival_kit_advanced": EquipmentData(
        name="Advanced Survival Kit",
        category="survival",
        die_bonus=2,
        durability=2,
        size=2,
        structure=4,
        availability=2,
        effect="Includes basic kit plus compass, tent, solar blanket, heating pads, multi-tool, rope, guide. Food/water for 2 days. +2 to Survival and Stamina + Resolve vs exposure. Negates level 2 environment effects (except radiation).",
        skill_bonuses={"survival": 2},
        special_properties={"supplies_days": 2, "environment_negation": 2}
    ),
    
    "survival_kit_superior": EquipmentData(
        name="Superior Survival Kit",
        category="survival",
        die_bonus=3,
        durability=2,
        size=3,
        structure=5,
        availability=3,
        effect="Everything from lesser kits plus GPS, water filtration, fishing rod, machete, cables, ponchos, 4-person tent. Food/water for 1 week. +3 to Survival and Stamina + Resolve. Negates level 3 environment (except radiation).",
        skill_bonuses={"survival": 3},
        special_properties={"supplies_days": 7, "environment_negation": 3}
    ),
    
    "survival_kit_urban": EquipmentData(
        name="Urban Survival Kit (Bug-Out Bag)",
        category="survival",
        die_bonus=3,
        durability=2,
        size=2,
        structure=4,
        availability=2,
        effect="Made for urban emergencies: blackouts, chemical attacks, disasters. Radio, maps, waterproof matches, antibiotics, flashlights, blankets, masks, food/water for 3 days. +3 to Survival/Stamina + Resolve. In wilderness: only +1 bonus.",
        skill_bonuses={"survival": 3},
        special_properties={"supplies_days": 3, "urban_specialized": True, "wilderness_penalty": True}
    ),
    
    # ========================================
    # MENTAL EQUIPMENT (Tools for Mental Skills)
    # ========================================
    "automotive_kit": EquipmentData(
        name="Automotive Kit",
        category="mental_equipment",
        die_bonus=1,
        durability=2,
        size=2,
        structure=3,
        availability=1,
        effect="Basic automotive tools for simple repairs. Trained characters can repair mundane issues without rolls if time isn't a factor.",
        skill_bonuses={"crafts": 1},
        special_properties={"automotive": True}
    ),
    
    "automotive_garage": EquipmentData(
        name="Automotive Garage",
        category="mental_equipment",
        die_bonus=2,
        durability=0,
        size=0,
        structure=0,
        availability=1,
        effect="Fully-stocked garage with heavy equipment. Required for complex tasks like engine/transmission replacement. Extended Intelligence + Crafts for major work.",
        skill_bonuses={"crafts": 2},
        special_properties={"automotive": True, "heavy_work": True, "location_based": True}
    ),
    
    "cache": EquipmentData(
        name="Cache",
        category="mental_equipment",
        die_bonus=1,
        durability=2,
        size=1,
        structure=5,
        availability=1,
        effect="Hidden, defensible place for items (usually weapons). Can never be more than half Size of parent object. Holds two items of its Size and any number of smaller items. Die bonus adds to concealment, subtracts from finding.",
        special_properties={"concealment": True, "capacity": 2}
    ),
    
    "cache_medium": EquipmentData(
        name="Cache (Medium)",
        category="mental_equipment",
        die_bonus=2,
        durability=2,
        size=3,
        structure=5,
        availability=2,
        effect="Larger hidden cache with better concealment. +2 to concealment/-2 to finding.",
        special_properties={"concealment": True, "capacity": 6}
    ),
    
    "cache_large": EquipmentData(
        name="Cache (Large)",
        category="mental_equipment",
        die_bonus=3,
        durability=2,
        size=5,
        structure=5,
        availability=3,
        effect="Large hidden cache with excellent concealment. +3 to concealment/-3 to finding.",
        special_properties={"concealment": True, "capacity": 10}
    ),
    
    "communications_headset": EquipmentData(
        name="Communications Headset",
        category="mental_equipment",
        die_bonus=2,
        durability=0,
        size=1,
        structure=1,
        availability=2,
        effect="Keeps characters in constant contact (~200 feet range). If practiced together: +2 to coordinated efforts (applies only to final roll in teamwork). Unpracticed: +1 and Wits + Composure to participate. Heavy objects (Durability 4+) require Wits + Composure to understand messages (-1 per Durability over 4).",
        special_properties={"communication": True, "range_feet": 200, "teamwork_bonus": 2}
    ),
    
    "crime_scene_kit": EquipmentData(
        name="Crime Scene Kit (CSI Kit)",
        category="mental_equipment",
        die_bonus=2,
        durability=2,
        size=3,
        structure=2,
        availability=2,
        effect="Toolbox with investigative aids: magnifiers, fingerprint dust, cameras, tape, chemicals, sample bags. +2 to Investigation. Allows evidence to be moved and analyzed offsite at leisure.",
        skill_bonuses={"investigation": 2},
        special_properties={"forensics": True, "evidence_collection": True}
    ),
    
    "code_kit": EquipmentData(
        name="Code Kit",
        category="mental_equipment",
        die_bonus=5,
        durability=1,
        size=2,
        structure=1,
        availability=1,
        effect="Tools for creating and interpreting codes (e.g., book codes). Successfully-designed cipher is difficult to break. Die bonus acts as penalty to crack the code without reference key.",
        special_properties={"encryption": True, "crack_penalty": 5}
    ),
    
    "cracking_software": EquipmentData(
        name="Cracking Software",
        category="mental_equipment",
        die_bonus=2,
        durability=0,
        size=0,
        structure=0,
        availability=3,
        effect="Quality software for forcing passwords, breaching firewalls. Acts as buffer between hacker and security - tracking requires two steps (identify software, then trace source). Security must roll twice, giving hacker chance to withdraw.",
        skill_bonuses={"computer": 2},
        special_properties={"hacking": True, "double_trace_required": True}
    ),
    
    "digital_recorder": EquipmentData(
        name="Digital Recorder",
        category="mental_equipment",
        die_bonus=1,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Coin-sized audio recorder. +1 to catch words/sounds and to concealment rolls. Can contest rolls to obscure discussion with Intelligence + Computer.",
        special_properties={"audio_recording": True, "concealable": True}
    ),
    
    "digital_recorder_advanced": EquipmentData(
        name="Digital Recorder (Advanced)",
        category="mental_equipment",
        die_bonus=2,
        durability=1,
        size=1,
        structure=2,
        availability=2,
        effect="Higher-quality recorder with better audio capture. +2 to catch words/sounds and concealment.",
        special_properties={"audio_recording": True, "concealable": True, "high_quality": True}
    ),
    
    "duct_tape": EquipmentData(
        name="Duct Tape",
        category="mental_equipment",
        die_bonus=1,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Versatile tool for reinforcing, stabilizing, binding, repairing. +1 to Crafts rolls OR adds 1 Durability to almost anything OR as restraint (-3 to break free, must overcome Structure).",
        skill_bonuses={"crafts": 1},
        special_properties={"versatile": True, "restraint": True, "durability_bonus": 1}
    ),
    
    "first_aid_kit_basic": EquipmentData(
        name="First-Aid Kit (Basic)",
        category="mental_equipment",
        die_bonus=0,
        durability=1,
        size=2,
        structure=3,
        availability=1,
        effect="Necessary supplies to stabilize injuries and stop wounds from worsening. Allows treatment rolls but provides no die bonus.",
        skill_bonuses={"medicine": 0},
        special_properties={"medical": True}
    ),
    
    "first_aid_kit_advanced": EquipmentData(
        name="First-Aid Kit (Advanced)",
        category="mental_equipment",
        die_bonus=1,
        durability=1,
        size=2,
        structure=3,
        availability=2,
        effect="Superior medical supplies. +1 to treatment rolls.",
        skill_bonuses={"medicine": 1},
        special_properties={"medical": True, "superior": True}
    ),
    
    "flashlight": EquipmentData(
        name="Flashlight",
        category="mental_equipment",
        die_bonus=1,
        durability=2,
        size=1,
        structure=3,
        availability=1,
        effect="Cuts through darkness. Die bonus subtracts from darkness penalties and adds to search rolls. Can be used as club or to blind targets (Dexterity + Athletics - Defense; contested Stamina, success = 1 turn blind, 2 turns if acute senses).",
        special_properties={"darkness_reduction": 1, "weapon_improvised": True, "blinding": True}
    ),
    
    "glowstick": EquipmentData(
        name="Glowstick",
        category="mental_equipment",
        die_bonus=2,
        durability=1,
        size=1,
        structure=1,
        availability=1,
        effect="Chemical light source (2-12 hours depending on type). Works underwater and in rain. Functions like flashlight but can't blind targets. Can be worn to prevent group members from going missing.",
        special_properties={"chemical_light": True, "waterproof": True, "wearable": True}
    ),
    
    "gps_tracker": EquipmentData(
        name="GPS Tracker",
        category="mental_equipment",
        die_bonus=3,
        durability=2,
        size=2,
        structure=2,
        availability=2,
        effect="GPS-enabled tracking device. Can track movements unless in caves, tunnels, or sewers. Characters can share GPS data or plant on unwitting subjects.",
        special_properties={"gps_tracking": True, "surface_only": True}
    ),
    
    "keylogging_software": EquipmentData(
        name="Keylogging Software",
        category="mental_equipment",
        die_bonus=2,
        durability=0,
        size=0,
        structure=0,
        availability=2,
        effect="Logs keystrokes on a computer to record data or passwords. Usually coupled with transmission software. Challenge is installing it (email scams or thumb drive with physical access). +2 to breach network or find important data.",
        skill_bonuses={"computer": 2},
        special_properties={"keylogging": True, "requires_installation": True}
    ),
    
    "luminol": EquipmentData(
        name="Luminol",
        category="mental_equipment",
        die_bonus=2,
        durability=0,
        size=1,
        structure=1,
        availability=1,
        effect="Chemical that reacts to metals in blood/bodily fluids causing faint glow (~30 seconds in dark). Aerosol can finds traces even after thorough cleaning. +2 to track by fluid traces or piece together crime scenes.",
        skill_bonuses={"investigation": 2},
        special_properties={"forensic": True, "blood_detection": True}
    ),
    
    "multi_tool": EquipmentData(
        name="Multi-Tool",
        category="mental_equipment",
        die_bonus=1,
        durability=3,
        size=1,
        structure=4,
        availability=1,
        effect="Portable tool for various tasks: sawing, wire stripping, bottle opening, filing. +1 to numerous Crafts tasks. Allows rolls when proper equipment unavailable. Can be weapon (0 lethal, -1 penalty).",
        skill_bonuses={"crafts": 1},
        special_properties={"versatile": True, "improvised_weapon": True}
    ),
    
    "personal_computer_basic": EquipmentData(
        name="Personal Computer (Basic)",
        category="mental_equipment",
        die_bonus=1,
        durability=2,
        size=3,
        structure=2,
        availability=1,
        effect="Basic computer for web surfing and simple tasks. +1 to Computer rolls.",
        skill_bonuses={"computer": 1},
        special_properties={"computing": True}
    ),
    
    "personal_computer_standard": EquipmentData(
        name="Personal Computer (Standard)",
        category="mental_equipment",
        die_bonus=2,
        durability=2,
        size=3,
        structure=2,
        availability=2,
        effect="Standard computer with decent processing power. +2 to Computer rolls.",
        skill_bonuses={"computer": 2},
        special_properties={"computing": True}
    ),
    
    "personal_computer_high_end": EquipmentData(
        name="Personal Computer (High-End)",
        category="mental_equipment",
        die_bonus=3,
        durability=2,
        size=3,
        structure=2,
        availability=3,
        effect="High-end computer with excellent processing. +3 to Computer rolls.",
        skill_bonuses={"computer": 3},
        special_properties={"computing": True, "high_performance": True}
    ),
    
    "personal_computer_professional": EquipmentData(
        name="Personal Computer (Professional)",
        category="mental_equipment",
        die_bonus=4,
        durability=2,
        size=3,
        structure=2,
        availability=4,
        effect="Professional-grade workstation. +4 to Computer rolls.",
        skill_bonuses={"computer": 4},
        special_properties={"computing": True, "professional": True}
    ),
    
    "smartphone_basic": EquipmentData(
        name="Smartphone (Basic)",
        category="mental_equipment",
        die_bonus=1,
        durability=2,
        size=1,
        structure=1,
        availability=1,
        effect="Basic smartphone with calls, texts, emails, photos, agenda, web. With apps becomes multi-tool of electronic age. Can handle GPS, facial recognition, text transcription/translation, directions, etc.",
        skill_bonuses={"computer": 1},
        special_properties={"portable_computing": True, "gps_capable": True, "camera": True}
    ),
    
    "smartphone_advanced": EquipmentData(
        name="Smartphone (Advanced)",
        category="mental_equipment",
        die_bonus=2,
        durability=2,
        size=1,
        structure=1,
        availability=2,
        effect="High-end smartphone with better processing and features. +2 to relevant Computer rolls.",
        skill_bonuses={"computer": 2},
        special_properties={"portable_computing": True, "gps_capable": True, "camera": True, "high_end": True}
    ),
    
    "smartphone_cutting_edge": EquipmentData(
        name="Smartphone (Cutting Edge)",
        category="mental_equipment",
        die_bonus=2,
        durability=2,
        size=1,
        structure=1,
        availability=3,
        effect="Latest flagship smartphone with top-tier capabilities. +2 to relevant Computer rolls.",
        skill_bonuses={"computer": 2},
        special_properties={"portable_computing": True, "gps_capable": True, "camera": True, "cutting_edge": True}
    ),
    
    "special_effects": EquipmentData(
        name="Special Effects Equipment",
        category="mental_equipment",
        die_bonus=2,
        durability=2,
        size=5,
        structure=3,
        availability=3,
        effect="Tricks used by amusement parks and magicians to fool witnesses (e.g., Pepper's Ghost illusion with mirrors/glass). +2 to deception. Witnesses fall for tricks unless suspicious. Can waste time or lead into traps.",
        skill_bonuses={"subterfuge": 2},
        special_properties={"illusion": True, "distraction": True}
    ),
    
    "surveillance_equipment": EquipmentData(
        name="Surveillance Equipment",
        category="mental_equipment",
        die_bonus=2,
        durability=2,
        size=2,
        structure=2,
        availability=3,
        effect="Motion detectors, cameras, monitors. High-end: infrared, heat sensors, barometric scanners. Detects and tracks who enters/leaves location. Unless actively avoided, presence is noticed and recorded. Avoiding: Dexterity + Stealth vs Intelligence + Computer/Crafts + equipment bonus.",
        skill_bonuses={"computer": 2},
        special_properties={"surveillance": True, "motion_detection": True}
    ),
    
    "talcum_powder": EquipmentData(
        name="Talcum Powder",
        category="mental_equipment",
        die_bonus=2,
        durability=0,
        size=1,
        structure=0,
        availability=1,
        effect="Shows presence of unseen things and evidence of intrusion. If area dusted: 5 successes on Dexterity + Stealth to enter without trace. Fewer successes obscure details. Can let ghosts/invisible entities communicate.",
        skill_bonuses={"investigation": 2},
        special_properties={"invisible_detection": True, "intrusion_detection": True}
    ),
    
    "ultraviolet_ink": EquipmentData(
        name="Ultraviolet Ink",
        category="mental_equipment",
        die_bonus=2,
        durability=1,
        size=1,
        structure=2,
        availability=1,
        effect="Invisible ink only visible under UV light. Excellent for relaying secret messages in plain sight or passing information through mundane channels under surveillance.",
        special_properties={"invisible_writing": True, "uv_required": True}
    ),
    
    # ========================================
    # PHYSICAL EQUIPMENT
    # ========================================
    "battering_ram": EquipmentData(
        name="Battering Ram",
        category="physical_equipment",
        die_bonus=4,
        durability=3,
        size=4,
        structure=8,
        availability=2,
        effect="Brings down doors and barricades with focused force. Uses Teamwork action (up to 4 participants). Primary actor adds +4. Ram ignores 2 points of Durability.",
        special_properties={"teamwork": True, "ignore_durability": 2, "max_participants": 4}
    ),
    
    "bear_trap": EquipmentData(
        name="Bear Trap",
        category="physical_equipment",
        die_bonus=2,
        durability=3,
        size=2,
        structure=5,
        availability=2,
        effect="Large metal jaw trap. Causes 3 lethal damage, ignores 2 armor/Durability. Escape: Strength + Stamina at -2 penalty (failure = 1 more lethal). Non-opposable thumbs must rip free. Hiding suffers -2 due to awkward shape/weight.",
        special_properties={"damage": 3, "armor_piercing": 2, "escape_difficulty": 2}
    ),
    
    "caltrops": EquipmentData(
        name="Caltrops",
        category="physical_equipment",
        die_bonus=2,
        durability=2,
        size=2,
        structure=3,
        availability=2,
        effect="Pointed metal pieces (one point always up). Moving through causes 1 lethal, ignores 1 armor/Durability. Safe movement: Dexterity + Athletics at -2, half Speed. Hiding: Wits + Larceny -3.",
        special_properties={"damage": 1, "armor_piercing": 1, "speed_reduction": 0.5}
    ),
    
    "camouflage_clothing": EquipmentData(
        name="Camouflage Clothing",
        category="physical_equipment",
        die_bonus=2,
        durability=1,
        size=2,
        structure=3,
        availability=2,
        effect="Allows wearer to blend with surroundings. Must be catered to environment (woodlands, urban, etc.). +2 to remain unnoticed.",
        skill_bonuses={"stealth": 2},
        special_properties={"environment_specific": True}
    ),
    
    "climbing_gear": EquipmentData(
        name="Climbing Gear",
        category="physical_equipment",
        die_bonus=2,
        durability=3,
        size=2,
        structure=2,
        availability=2,
        effect="Ropes, pulleys, handles, carabiners, hooks for scaling. +2 to Strength + Athletics for climbing. If properly applied (Wits + Athletics): prevents falling more than 10 feet at a time.",
        skill_bonuses={"athletics": 2},
        special_properties={"fall_prevention": True, "max_fall_feet": 10}
    ),
    
    "crowbar": EquipmentData(
        name="Crowbar",
        category="physical_equipment",
        die_bonus=2,
        durability=3,
        size=2,
        structure=4,
        availability=1,
        effect="Curved steel for prying. Adds to leverage rolls. When prying open: ignore 2 Durability on locks/barricades. Can be used as weapon.",
        skill_bonuses={"athletics": 2},
        special_properties={"leverage": True, "ignore_durability": 2, "improvised_weapon": True}
    ),
    
    "gas_mask": EquipmentData(
        name="Gas Mask",
        category="physical_equipment",
        die_bonus=5,
        durability=1,
        size=2,
        structure=3,
        availability=2,
        effect="Filtration device against noxious chemicals. Stand minor toxins indefinitely. Powerful toxins may still require rolls. +5 to resist toxins.",
        special_properties={"toxin_protection": 5}
    ),
    
    "handcuffs": EquipmentData(
        name="Handcuffs",
        category="physical_equipment",
        die_bonus=2,
        durability=4,
        size=1,
        structure=4,
        availability=1,
        effect="Steel restraints. Applying in grapple: Strength + Brawl - opponent's Strength. Breaking: Strength + Stamina -4 (reduces Structure by 1 per success, 1 bashing per attempt). Escaping by dexterity: Dexterity + Athletics -4 (1 bashing on success, 1 lethal on failure). Manual dexterity: -4 penalty from behind, -2 from front. Social: -3 with strangers.",
        special_properties={"restraint": True, "escape_difficulty": 4}
    ),
    
    "zip_ties": EquipmentData(
        name="Zip Ties (Heavy-Duty)",
        category="physical_equipment",
        die_bonus=0,
        durability=3,
        size=1,
        structure=3,
        availability=1,
        effect="Heavy plastic restraints. Slightly less durable than handcuffs but can be much tighter. -5 penalty from behind, -3 from front. Can be cut free.",
        special_properties={"restraint": True, "escape_difficulty": 5, "cuttable": True}
    ),
    
    "lockpicking_kit": EquipmentData(
        name="Lockpicking Kit",
        category="physical_equipment",
        die_bonus=2,
        durability=2,
        size=2,
        structure=2,
        availability=2,
        effect="Picks, tools, rods for manipulating locks. With 1+ Larceny: pick any mechanical lock without roll if time not an issue. If time matters: +2 to Dexterity + Larceny. Only works on mechanical locks.",
        skill_bonuses={"larceny": 2},
        special_properties={"lockpicking": True, "mechanical_only": True}
    ),
    
    "lockpicking_kit_portable": EquipmentData(
        name="Lockpicking Kit (Portable)",
        category="physical_equipment",
        die_bonus=1,
        durability=2,
        size=1,
        structure=1,
        availability=1,
        effect="Smaller, more concealable lockpick set. +1 bonus. Doesn't allow auto-success (may not have right tools).",
        skill_bonuses={"larceny": 1},
        special_properties={"lockpicking": True, "mechanical_only": True, "portable": True}
    ),
    
    "digital_lockpick": EquipmentData(
        name="Digital Lockpick",
        category="physical_equipment",
        die_bonus=2,
        durability=2,
        size=2,
        structure=2,
        availability=3,
        effect="For digital locks (typically one type like hotel keycards). Can be Size 1 if crafted as laptop/smartphone extension.",
        skill_bonuses={"larceny": 2},
        special_properties={"lockpicking": True, "digital_only": True, "specific_lock_type": True}
    ),
    
    "night_vision_goggles": EquipmentData(
        name="Night Vision Goggles",
        category="physical_equipment",
        die_bonus=2,
        durability=1,
        size=2,
        structure=1,
        availability=2,
        effect="Amplifies low-light conditions. No penalties for acting blind. Bright lights temporarily blind wearer.",
        special_properties={"night_vision": True, "light_sensitive": True}
    ),
    
    "rope": EquipmentData(
        name="Rope",
        category="physical_equipment",
        die_bonus=1,
        durability=2,
        size=3,
        structure=2,
        availability=1,
        effect="Simple, efficient utility tool. +1 to relevant Crafts rolls. As binding: Durability (or effective Strength) = user's Crafts score (+ Specialty if applicable). Solid knots can render subjects completely immobile.",
        skill_bonuses={"crafts": 1},
        special_properties={"binding": True, "versatile": True}
    ),
    
    "stun_gun_handheld": EquipmentData(
        name="Stun Gun (Handheld)",
        category="physical_equipment",
        die_bonus=0,
        durability=2,
        size=1,
        structure=2,
        availability=1,
        effect="Delivers overwhelming electricity. Live leads on handle. ~50 uses per charge. Attack: Dexterity + Weaponry - Defense. Hit: 1 lethal, successes subtract from victim's next pool. Maintain shock: Strength + Weaponry - target's Strength/Defense. Accumulated successes > victim's Size = collapse (neuromuscular incapacitation for 10 - Stamina turns).",
        special_properties={"nonlethal_option": True, "damage": 1, "incapacitation": True}
    ),
    
    "stun_gun_ranged": EquipmentData(
        name="Stun Gun (Ranged)",
        category="physical_equipment",
        die_bonus=0,
        durability=2,
        size=1,
        structure=2,
        availability=2,
        effect="Fires wired darts up to 15 feet. Similar battery life but compressed air cartridge replaced after each shot. Attack: Dexterity + Firearms - Defense. Darts remain in body adding +3 successes per turn automatically. Remove: Strength + Stamina (initial successes as penalty).",
        special_properties={"nonlethal_option": True, "damage": 1, "incapacitation": True, "range_feet": 15}
    ),
    
    "stun_gun_ranged_high_power": EquipmentData(
        name="Stun Gun (Ranged, High-Power)",
        category="physical_equipment",
        die_bonus=0,
        durability=2,
        size=1,
        structure=2,
        availability=3,
        effect="More powerful ranged stun gun with extended range (25 feet) and stronger charge.",
        special_properties={"nonlethal_option": True, "damage": 1, "incapacitation": True, "range_feet": 25, "enhanced": True}
    ),
    
    # ========================================
    # SOCIAL EQUIPMENT
    # ========================================
    "cash_small": EquipmentData(
        name="Cash (Small Amount)",
        category="social_equipment",
        die_bonus=1,
        durability=1,
        size=2,
        structure=1,
        availability=1,
        effect="Wad of cash/briefcase/bank account number. Not reflected in Resources Merit (not regular income). Can be expended for: +1 to social rolls where bribes help, purchase 1 item of equal Availability, or 1 month's income of equivalent Resources rating.",
        skill_bonuses={"persuasion": 1, "intimidation": 1, "streetwise": 1},
        special_properties={"bribe": True, "consumable": True}
    ),
    
    "cash_medium": EquipmentData(
        name="Cash (Medium Amount)",
        category="social_equipment",
        die_bonus=2,
        durability=1,
        size=2,
        structure=1,
        availability=2,
        effect="Substantial amount of cash for larger bribes and purchases. +2 to social rolls where money helps.",
        skill_bonuses={"persuasion": 2, "intimidation": 2, "streetwise": 2},
        special_properties={"bribe": True, "consumable": True}
    ),
    
    "cash_large": EquipmentData(
        name="Cash (Large Amount)",
        category="social_equipment",
        die_bonus=3,
        durability=1,
        size=2,
        structure=1,
        availability=3,
        effect="Large sum for significant transactions and influence. +3 to social rolls where money helps.",
        skill_bonuses={"persuasion": 3, "intimidation": 3, "streetwise": 3},
        special_properties={"bribe": True, "consumable": True}
    ),
    
    "cash_huge": EquipmentData(
        name="Cash (Huge Amount)",
        category="social_equipment",
        die_bonus=4,
        durability=1,
        size=2,
        structure=1,
        availability=4,
        effect="Massive amount of liquid assets. +4 to social rolls where money helps.",
        skill_bonuses={"persuasion": 4, "intimidation": 4, "streetwise": 4},
        special_properties={"bribe": True, "consumable": True}
    ),
    
    "cash_fortune": EquipmentData(
        name="Cash (Fortune)",
        category="social_equipment",
        die_bonus=5,
        durability=1,
        size=2,
        structure=1,
        availability=5,
        effect="A fortune in liquid assets. +5 to social rolls where money helps.",
        skill_bonuses={"persuasion": 5, "intimidation": 5, "streetwise": 5},
        special_properties={"bribe": True, "consumable": True}
    ),
    
    "disguise_basic": EquipmentData(
        name="Disguise (Basic)",
        category="social_equipment",
        die_bonus=1,
        durability=1,
        size=3,
        structure=2,
        availability=1,
        effect="Basic disguise to fit in or blend into crowd. Properly costumed: no rolls to blend in. Detect disguise: -1 penalty. +1 to remain hidden. Can emulate first dot of appropriate Social Merit for scene (requires Composure + Subterfuge, contested by Wits + Subterfuge).",
        skill_bonuses={"subterfuge": 1},
        special_properties={"disguise": True, "social_merit_emulation": 1}
    ),
    
    "disguise_quality": EquipmentData(
        name="Disguise (Quality)",
        category="social_equipment",
        die_bonus=2,
        durability=1,
        size=3,
        structure=2,
        availability=2,
        effect="High-quality disguise with better materials and detail. -2 to detect, +2 to hide.",
        skill_bonuses={"subterfuge": 2},
        special_properties={"disguise": True, "social_merit_emulation": 1}
    ),
    
    "disguise_professional": EquipmentData(
        name="Disguise (Professional)",
        category="social_equipment",
        die_bonus=3,
        durability=1,
        size=3,
        structure=2,
        availability=3,
        effect="Professional-grade disguise with prosthetics and makeup. -3 to detect, +3 to hide.",
        skill_bonuses={"subterfuge": 3},
        special_properties={"disguise": True, "social_merit_emulation": 1, "professional": True}
    ),
    
    "fashion_casual": EquipmentData(
        name="Fashion (Casual)",
        category="social_equipment",
        die_bonus=1,
        durability=1,
        size=2,
        structure=1,
        availability=1,
        effect="Fashionable clothing to draw positive attention and fit in. Must be appropriate to setting. If improperly dressed: -1 to all Social rolls. When proper: +1 to Social rolls.",
        skill_bonuses={"socialize": 1, "persuasion": 1},
        special_properties={"fashion": True, "context_dependent": True}
    ),
    
    "fashion_designer": EquipmentData(
        name="Fashion (Designer)",
        category="social_equipment",
        die_bonus=2,
        durability=1,
        size=2,
        structure=1,
        availability=3,
        effect="Designer clothing that makes strong impression. If proper context: +2 to Social rolls. If improper: -2.",
        skill_bonuses={"socialize": 2, "persuasion": 2},
        special_properties={"fashion": True, "context_dependent": True, "designer": True}
    ),
    
    "fashion_haute_couture": EquipmentData(
        name="Fashion (Haute Couture)",
        category="social_equipment",
        die_bonus=3,
        durability=1,
        size=2,
        structure=1,
        availability=5,
        effect="Exclusive haute couture commanding attention and respect. If proper context: +3 to Social rolls. If improper: -3.",
        skill_bonuses={"socialize": 3, "persuasion": 3},
        special_properties={"fashion": True, "context_dependent": True, "haute_couture": True}
    ),
}

# Equipment categories for reference
EQUIPMENT_CATEGORIES = {
    "firearm_accessories": "Equipment that enhances firearm functionality",
    "sights": "Optical and targeting equipment for firearms",
    "surveillance": "Equipment for monitoring, tracking, and observation",
    "survival": "Gear for surviving hostile environments",
    "mental_equipment": "Tools that enhance Mental skills (Intelligence, Wits, Resolve)",
    "physical_equipment": "Tools that enhance Physical skills (Strength, Dexterity, Stamina)",
    "social_equipment": "Items that enhance Social skills (Presence, Manipulation, Composure)"
}
