from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.equipment_database import WEAPON_DATABASE, ARMOR_DATABASE, WeaponData, ArmorData
from world.equipment_purchasing import PURCHASE_CONFIG, get_available_equipment, can_purchase_equipment, purchase_equipment, EquipmentPurchasingConfig, add_resource_points
from world.utils.formatting import header, footer, section_header, divider, format_stat, format_stat_labeled, get_theme_colors
from world.utils.ansi_utils import wrap_ansi
from .base import DeveloperMixin, TargetResolutionMixin


def _find_equipment_key(equipment_dict, name):
    """Find equipment dict key by case-insensitive name match. Returns canonical key or None."""
    if not equipment_dict or not name:
        return None
    name_lower = name.strip().lower()
    for key in equipment_dict:
        if key.lower() == name_lower:
            return key
    return None


class CmdEquipment(MuxCommand):
    """
    Manage equipment, weapons, and armor.
    
    Usage:
        +equipment - List your equipment (default)
        +equipment/list - List your equipment
        +equipment/add <name> <type> [rating] - Add equipment
        +equipment/remove <name> - Remove equipment
        +equipment/view <name> - View equipment details
        +equipment/wield <weapon> - Wield a weapon
        +equipment/unwield - Stop wielding weapon
        +equipment/wear <armor> - Wear armor
        +equipment/unwear - Remove armor
        +equipment/weapons - List available weapons to add
        +equipment/armor - List available armor to add
        
    Types:
        weapon - Combat weapons with damage and availability
        armor - Protective gear with armor ratings
        equipment - General items with availability rating
        style - Fighting styles and specializations
    """
    key = "+equipment"
    aliases = ["+eq"]
    help_category = "Gear & Resources"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            self.list_equipment()
            return

        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_equipment()
        elif switch == "add":
            self.add_equipment()
        elif switch == "remove":
            self.remove_equipment()
        elif switch == "view":
            self.view_equipment()
        elif switch == "wield":
            self.wield_weapon()
        elif switch == "unwield":
            self.unwield_weapon()
        elif switch == "wear":
            self.wear_armor()
        elif switch == "unwear":
            self.unwear_armor()
        elif switch == "weapons":
            self.list_available_weapons()
        elif switch == "armor":
            self.list_available_armor()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def list_equipment(self):
        """List all equipment"""
        if not self.caller.db.equipment:
            self.caller.msg("You have no equipment.")
            return

        output = [header(f"Equipment: {self.caller.name}", width=78, char="=")]

        wielded_weapon = self.caller.db.wielded_weapon
        worn_armor = self.caller.db.worn_armor

        weapons = []
        armor = []
        equipment = []
        styles = []

        for name, item in self.caller.db.equipment.items():
            if item["type"] == "weapon":
                status = " (wielded)" if name == wielded_weapon else ""
                weapons.append(f"  |w{name}|n (Dmg: {item.get('damage', 0)}, Init: {item.get('initiative', 0):+d}){status}")
            elif item["type"] == "armor":
                status = " (worn)" if name == worn_armor else ""
                armor.append(f"  |w{name}|n (Armor: {item.get('general_armor', 0)}/{item.get('ballistic_armor', 0)}){status}")
            elif item["type"] == "equipment":
                avail = item.get("rating", item.get("availability", "-"))
                equipment.append(f"  |w{name}|n (Availability {avail})")
            elif item["type"] == "style":
                styles.append(f"  |w{name}|n ({item.get('rating', '-')} dots)")

        if weapons:
            output.append(section_header("Weapons", width=78))
            output.extend(sorted(weapons))

        if armor:
            output.append(section_header("Armor", width=78))
            output.extend(sorted(armor))

        if equipment:
            output.append(section_header("Equipment", width=78))
            output.extend(sorted(equipment))

        if styles:
            output.append(section_header("Fighting Styles", width=78))
            output.extend(sorted(styles))

        output.append(footer(width=78, char="="))
        self.caller.msg("\n".join(output))
    
    def add_equipment(self):
        """Add equipment, weapon, or armor"""
        args = self.args.split()
        if len(args) < 2:
            self.caller.msg("Usage: +equipment/add <name> <type> [rating]")
            self.caller.msg("Types: weapon, armor, equipment, style")
            return

        name = args[0]
        type_ = args[1].lower()
        rating = int(args[2]) if len(args) > 2 else None

        if type_ not in ["weapon", "armor", "equipment", "style"]:
            self.caller.msg("Invalid type. Use: weapon, armor, equipment, or style")
            return

        if not self.caller.db.equipment:
            self.caller.db.equipment = {}

        existing_key = _find_equipment_key(self.caller.db.equipment, name)
        if existing_key:
            self.caller.msg(f"You already have {existing_key}.")
            return
            
        # Handle different equipment types
        if type_ == "weapon":
            weapon_key = name.lower().replace(" ", "_")
            if weapon_key not in WEAPON_DATABASE:
                self.caller.msg(f"Unknown weapon: {name}")
                self.caller.msg("Use '+equipment/weapons' to see available weapons.")
                return
            weapon = WEAPON_DATABASE[weapon_key]
            self.caller.db.equipment[weapon.name] = {
                "type": "weapon",
                "damage": weapon.damage,
                "initiative": weapon.initiative_mod,
                "strength": weapon.strength_req,
                "size": weapon.size,
                "range": weapon.weapon_type,
                "availability": weapon.availability,
                "capacity": weapon.capacity,
                "tags": weapon.tags
            }
            
        elif type_ == "armor":
            armor_key = name.lower().replace(" ", "_")
            if armor_key not in ARMOR_DATABASE:
                self.caller.msg(f"Unknown armor: {name}")
                self.caller.msg("Use '+equipment/armor' to see available armor.")
                return
            armor = ARMOR_DATABASE[armor_key]
            self.caller.db.equipment[armor.name] = {
                "type": "armor",
                "general_armor": armor.general_armor,
                "ballistic_armor": armor.ballistic_armor,
                "strength": armor.strength_req,
                "defense": armor.defense_penalty,
                "speed": armor.speed_penalty,
                "availability": armor.availability,
                "coverage": armor.coverage,
                "notes": armor.notes
            }
            
        elif type_ == "equipment":
            if rating is None:
                self.caller.msg("Equipment requires availability rating (1-5)")
                return
            if not 1 <= rating <= 5:
                self.caller.msg("Equipment availability must be 1-5")
                return
            self.caller.db.equipment[name] = {
                "type": "equipment",
                "rating": rating
            }
            
        elif type_ == "style":
            if rating is None:
                self.caller.msg("Fighting style requires dot rating (1-5)")
                return
            if not 1 <= rating <= 5:
                self.caller.msg("Fighting style ratings must be 1-5")
                return
            self.caller.db.equipment[name] = {
                "type": "style",
                "rating": rating
            }
            
        self.caller.msg(f"Added {type_} {name}")
    
    def remove_equipment(self):
        """Remove equipment or merit"""
        name = self.args.strip()
        if not name:
            self.caller.msg("Usage: +equipment/remove <name>")
            return

        key = _find_equipment_key(self.caller.db.equipment or {}, name)
        if not key:
            self.caller.msg(f"You don't have '{name}'.")
            return

        if key == self.caller.db.wielded_weapon:
            self.caller.db.wielded_weapon = None
        if key == self.caller.db.worn_armor:
            self.caller.db.worn_armor = None

        del self.caller.db.equipment[key]
        self.caller.msg(f"Removed {key}.")
    
    def view_equipment(self):
        """View equipment details"""
        name = self.args.strip()
        if not name:
            self.caller.msg("Usage: +equipment/view <name>")
            return

        key = _find_equipment_key(self.caller.db.equipment or {}, name)
        if not key:
            self.caller.msg(f"You don't have '{name}'.")
            return

        item = self.caller.db.equipment[key]
        output = [header(f"Equipment: {key}", width=78, char="-")]
        output.append(format_stat_labeled("Type", item["type"].title(), width=78))

        if item["type"] == "weapon":
            output.append(format_stat_labeled("Damage", item.get("damage", 0), width=78))
            output.append(format_stat_labeled("Initiative", f"{item.get('initiative', 0):+d}", width=78))
            output.append(format_stat_labeled("Strength", item.get("strength", "-"), width=78))
            output.append(format_stat_labeled("Size", item.get("size", "-"), width=78))
            output.append(format_stat_labeled("Range", item.get("range", "-"), width=78))
            output.append(format_stat_labeled("Availability", item.get("availability", "-"), width=78))
            if item.get("capacity") and item.get("capacity") != "single":
                output.append(format_stat_labeled("Capacity", item["capacity"], width=78))
            if item.get("tags"):
                output.append(format_stat_labeled("Tags", item["tags"], width=78))

        elif item["type"] == "armor":
            output.append(format_stat_labeled("General Armor", item.get("general_armor", 0), width=78))
            output.append(format_stat_labeled("Ballistic Armor", item.get("ballistic_armor", 0), width=78))
            output.append(format_stat_labeled("Strength Req", item.get("strength", "-"), width=78))
            output.append(format_stat_labeled("Defense Penalty", f"{item.get('defense', 0):+d}", width=78))
            output.append(format_stat_labeled("Speed Penalty", f"{item.get('speed', 0):+d}", width=78))
            output.append(format_stat_labeled("Availability", item.get("availability", "-"), width=78))
            if item.get("coverage"):
                output.append(format_stat_labeled("Coverage", ", ".join(item["coverage"]), width=78))
            if item.get("notes"):
                output.append(format_stat_labeled("Notes", item["notes"], width=78))

        elif item["type"] == "equipment":
            avail = item.get("rating", item.get("availability", "-"))
            output.append(format_stat_labeled("Availability", avail, width=78))
            if item.get("category"):
                output.append(format_stat_labeled("Category", item["category"], width=78))
            if item.get("die_bonus") is not None:
                output.append(format_stat_labeled("Die Bonus", item["die_bonus"], width=78))
            if item.get("durability") is not None:
                output.append(format_stat_labeled("Durability", item["durability"], width=78))
            if item.get("size") is not None:
                output.append(format_stat_labeled("Size", item["size"], width=78))
            if item.get("structure") is not None:
                output.append(format_stat_labeled("Structure", item["structure"], width=78))
            if item.get("skill_bonuses"):
                bonuses = ", ".join(f"{k}:+{v}" for k, v in item["skill_bonuses"].items())
                output.append(format_stat_labeled("Skill Bonuses", bonuses, width=78))
            if item.get("special_properties"):
                prop_parts = []
                for k, v in item["special_properties"].items():
                    if v is True:
                        prop_parts.append(k)
                    else:
                        prop_parts.append(f"{k}:{v}")
                output.append(format_stat_labeled("Special Properties", ", ".join(prop_parts), width=78))
            if item.get("effect"):
                _, text_color, _ = get_theme_colors()
                output.append("")
                output.append(f"|{text_color}Effect|n")
                wrapped = wrap_ansi(item["effect"], width=74, left_padding=4)
                output.extend(wrapped.split("\n"))

        elif item["type"] == "style":
            output.append(format_stat_labeled("Dots", item.get("rating", "-"), width=78))
            output.append(format_stat_labeled("Description", "Fighting style technique", width=78))

        output.append(footer(width=78, char="-"))
        self.caller.msg("\n".join(output))
    
    def wield_weapon(self):
        """Wield a weapon"""
        weapon_name = self.args.strip()
        if not weapon_name:
            self.caller.msg("Usage: +equipment/wield <weapon>")
            return

        key = _find_equipment_key(self.caller.db.equipment or {}, weapon_name)
        if not key:
            self.caller.msg(f"You don't have '{weapon_name}'.")
            return

        item = self.caller.db.equipment[key]
        if item["type"] != "weapon":
            self.caller.msg(f"{key} is not a weapon.")
            return
            
        if self.caller.db.wielded_weapon:
            self.caller.msg(f"You stop wielding {self.caller.db.wielded_weapon}.")

        self.caller.db.wielded_weapon = key
        self.caller.msg(f"You wield {key}.")
        self.caller.location.msg_contents(
            f"{self.caller.name} wields {key}.",
            exclude=[self.caller]
        )
    
    def unwield_weapon(self):
        """Stop wielding current weapon"""
        if not self.caller.db.wielded_weapon:
            self.caller.msg("You are not wielding a weapon")
            return
            
        weapon_name = self.caller.db.wielded_weapon
        self.caller.db.wielded_weapon = None
        self.caller.msg(f"You stop wielding {weapon_name}")
        self.caller.location.msg_contents(
            f"{self.caller.name} stops wielding {weapon_name}.",
            exclude=[self.caller]
        )
    
    def wear_armor(self):
        """Wear armor"""
        armor_name = self.args.strip()
        if not armor_name:
            self.caller.msg("Usage: +equipment/wear <armor>")
            return

        key = _find_equipment_key(self.caller.db.equipment or {}, armor_name)
        if not key:
            self.caller.msg(f"You don't have '{armor_name}'.")
            return

        item = self.caller.db.equipment[key]
        if item["type"] != "armor":
            self.caller.msg(f"{key} is not armor.")
            return
            
        if self.caller.db.worn_armor:
            self.caller.msg(f"You remove {self.caller.db.worn_armor}.")

        self.caller.db.worn_armor = key
        self.caller.msg(f"You wear {key}.")
        self.caller.location.msg_contents(
            f"{self.caller.name} puts on {key}.",
            exclude=[self.caller]
        )
    
    def unwear_armor(self):
        """Remove current armor"""
        if not self.caller.db.worn_armor:
            self.caller.msg("You are not wearing armor")
            return
            
        armor_name = self.caller.db.worn_armor
        self.caller.db.worn_armor = None
        self.caller.msg(f"You remove {armor_name}")
        self.caller.location.msg_contents(
            f"{self.caller.name} removes {armor_name}.",
            exclude=[self.caller]
        )
    
    def list_available_weapons(self):
        """List all available weapons that can be added"""
        output = [header("Available Weapons", width=78, char="=")]
        output.append("|wSource:|n Chronicles of Darkness: Hurt Locker")
        output.append(divider(width=78))

        categories = {
            "Melee - Bladed": [],
            "Melee - Blunt": [],
            "Melee - Exotic": [],
            "Melee - Improvised": [],
            "Melee - Polearms": [],
            "Ranged - Archery": [],
            "Ranged - Thrown": [],
            "Ranged - Firearms": [],
            "Ranged - Nonlethal": [],
            "Explosives": [],
            "Heavy Weapons": []
        }
        
        for weapon_key, weapon in WEAPON_DATABASE.items():
            weapon_str = f"{weapon.name} - Dam:{weapon.damage} Init:{weapon.initiative_mod:+d} Str:{weapon.strength_req} Size:{weapon.size} Avail:{weapon.availability}"
            if weapon.tags:
                weapon_str += f" ({weapon.tags})"
            
            # Categorize weapons based on name patterns
            if any(blade in weapon_key for blade in ["axe", "sword", "knife", "machete", "rapier", "hatchet"]):
                categories["Melee - Bladed"].append(weapon_str)
            elif any(blunt in weapon_key for blunt in ["brass_knuckles", "club", "nightstick", "nunchaku", "sap", "sledgehammer"]):
                categories["Melee - Blunt"].append(weapon_str)
            elif any(exotic in weapon_key for exotic in ["chain", "whip", "tiger_claws", "shield", "stake", "stun_gun_melee", "kusari", "catchpole"]):
                categories["Melee - Exotic"].append(weapon_str)
            elif any(improv in weapon_key for improv in ["blowtorch", "board", "improvised", "nail_gun", "shovel", "tire_iron"]):
                categories["Melee - Improvised"].append(weapon_str)
            elif any(pole in weapon_key for pole in ["spear", "staff"]):
                categories["Melee - Polearms"].append(weapon_str)
            elif any(arch in weapon_key for arch in ["bow", "crossbow"]):
                categories["Ranged - Archery"].append(weapon_str)
            elif weapon.weapon_type == "thrown" or "throwing" in weapon_key or "molotov" in weapon_key:
                categories["Ranged - Thrown"].append(weapon_str)
            elif any(firearm in weapon_key for firearm in ["pistol", "revolver", "smg", "rifle", "shotgun"]):
                categories["Ranged - Firearms"].append(weapon_str)
            elif any(nonlethal in weapon_key for nonlethal in ["pepper_spray", "stun_gun_ranged"]):
                categories["Ranged - Nonlethal"].append(weapon_str)
            elif any(explosive in weapon_key for explosive in ["grenade", "bomb", "round", "launcher"]):
                categories["Explosives"].append(weapon_str)
            elif "flamethrower" in weapon_key:
                categories["Heavy Weapons"].append(weapon_str)
        
        for category, weapons in categories.items():
            if weapons:
                output.append(section_header(category, width=78))
                for weapon in sorted(weapons):
                    output.append(f"  {weapon}")

        output.append(divider(width=78))
        output.append("|wDamage types|n are determined automatically based on weapon category.")
        output.append("|wUsage:|n +equipment/add <weapon_name> weapon | +equipment/view <weapon_name>")
        output.append(footer(width=78, char="="))
        self.caller.msg("\n".join(output))
    
    def list_available_armor(self):
        """List all available armor that can be added"""
        output = [header("Available Armor", width=78, char="=")]
        output.append("|wSource:|n Chronicles of Darkness: Hurt Locker")
        output.append(divider(width=78))

        modern_armor = []
        archaic_armor = []

        for armor_key, armor in ARMOR_DATABASE.items():
            armor_str = f"  |w{armor.name}|n - Armor:{armor.general_armor}/{armor.ballistic_armor} Str:{armor.strength_req} Def:{armor.defense_penalty:+d} Spd:{armor.speed_penalty:+d} Avail:{armor.availability}"

            if any(modern in armor_key for modern in ["reinforced", "sports", "kevlar", "flak", "riot", "bomb", "helmet_modern"]):
                modern_armor.append(armor_str)
            else:
                archaic_armor.append(armor_str)

        if modern_armor:
            output.append(section_header("Modern Armor", width=78))
            output.extend(sorted(modern_armor))

        if archaic_armor:
            output.append(section_header("Archaic Armor", width=78))
            output.extend(sorted(archaic_armor))

        output.append(divider(width=78))
        output.append("|wFormat:|n General/Ballistic - General reduces damage, Ballistic downgrades firearm lethal to bashing.")
        output.append("|wUsage:|n +equipment/add <armor_name> armor | +equipment/view <armor_name>")
        output.append(footer(width=78, char="="))
        self.caller.msg("\n".join(output)) 


class CmdBuy(MuxCommand):
    """
    Purchase equipment using Resources merit.
    
    Usage:
        +buy/list [category] - List available equipment
        +buy/info <item> - Get detailed item information
        +buy <item> - Purchase an item
        +buy/status - Check your resource status
        +buy/help - Show purchasing help
        
    Categories: weapons, armor, all
    
    Examples:
        +buy/list weapons - Show available weapons
        +buy/info sword - Get sword details
        +buy sword - Purchase a sword
        +buy/status - Check resource points/limits
    """
    
    key = "+buy"
    aliases = ["+purchase", "+shop"]
    help_category = "Gear & Resources"
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            if not self.args:
                self.caller.msg("Usage: +buy <item>, +buy/list, +buy/status, or +buy/help")
                return
            else:
                # Direct purchase
                self.purchase_item()
                return
                
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_equipment()
        elif switch == "info":
            self.item_info()
        elif switch == "status":
            self.resource_status()
        elif switch == "help":
            self.show_help()
        else:
            self.caller.msg("Invalid switch. Use: list, info, status, or help")
    
    def purchase_item(self):
        """Purchase an item"""
        item_name = self.args.strip().lower().replace(" ", "_")
        
        if not item_name:
            self.caller.msg("Usage: +buy <item>")
            return
            
        # Check if character has Resources merit
        merits = self.caller.db.stats.get("merits", {})
        if "resources" not in merits or merits["resources"].get("dots", 0) == 0:
            self.caller.msg("You need the Resources merit to purchase equipment.")
            return
            
        # Attempt purchase
        success, message = purchase_equipment(self.caller, item_name)
        
        if success:
            self.caller.msg(f"|gSUCCESS:|n {message}")
            # Announce to location
            available_equipment = get_available_equipment()
            if item_name in available_equipment:
                item_display_name = available_equipment[item_name]['name']
                self.caller.location.msg_contents(
                    f"{self.caller.name} acquires {item_display_name}.",
                    exclude=[self.caller]
                )
        else:
            self.caller.msg(f"|rFAILED:|n {message}")
    
    def list_equipment(self):
        """List available equipment for purchase"""
        category = self.args.strip().lower() if self.args else "all"
        
        available_equipment = get_available_equipment()
        
        # Filter by category
        if category == "weapons":
            items = {k: v for k, v in available_equipment.items() if v['type'] == 'weapon'}
            title = "Available Weapons for Purchase"
        elif category == "armor":
            items = {k: v for k, v in available_equipment.items() if v['type'] == 'armor'}
            title = "Available Armor for Purchase"
        else:
            items = available_equipment
            title = "Available Equipment for Purchase"
            
        if not items:
            self.caller.msg(f"No {category} available for purchase.")
            return

        output = [header(title, width=78, char="=")]
        output.append(format_stat("Resource Mode", PURCHASE_CONFIG.resource_mode.title(), width=78))
        output.append(divider(width=78))

        # Group by availability
        by_availability = {}
        for key, item in items.items():
            avail = item['availability']
            if avail not in by_availability:
                by_availability[avail] = []
            by_availability[avail].append((key, item))
        
        for availability in sorted(by_availability.keys()):
            output.append(section_header(f"Availability {availability}", width=78))

            for key, item in sorted(by_availability[availability], key=lambda x: x[1]['name']):
                # Check if character can afford
                can_afford, _ = can_purchase_equipment(self.caller, key)
                afford_indicator = "|g✓|n" if can_afford else "|r✗|n"
                
                # Add item details
                if item['type'] == 'weapon':
                    weapon = item['data']
                    details = f"Dmg:{weapon.damage} Init:{weapon.initiative_mod:+d} Str:{weapon.strength_req}"
                    if weapon.tags:
                        details += f" ({weapon.tags})"
                elif item['type'] == 'armor':
                    armor = item['data']
                    details = f"Armor:{armor.general_armor}/{armor.ballistic_armor} Str:{armor.strength_req} Def:{armor.defense_penalty:+d}"
                else:
                    details = ""
                    
                output.append(f"  {afford_indicator} |w{item['name']}|n - {details}")

        output.append(divider(width=78))
        output.append("|wUsage:|n +buy <item> | +buy/info <item> | +buy/status")
        output.append(footer(width=78, char="="))
        self.caller.msg("\n".join(output))
    
    def item_info(self):
        """Get detailed information about an item"""
        if not self.args:
            self.caller.msg("Usage: +buy/info <item>")
            return
            
        item_name = self.args.strip().lower().replace(" ", "_")
        available_equipment = get_available_equipment()
        
        if item_name not in available_equipment:
            self.caller.msg(f"Unknown item: '{self.args.strip()}'.")
            return

        item = available_equipment[item_name]
        can_afford, afford_message = can_purchase_equipment(self.caller, item_name)
        afford_status = "|gAffordable|n" if can_afford else f"|rNot Affordable|n ({afford_message})"

        output = [header(f"Equipment: {item['name']}", width=78, char="-")]
        output.append(format_stat("Type", item["type"].title(), width=78))
        output.append(format_stat("Availability", item["availability"], width=78))
        output.append(format_stat("Status", afford_status, width=78))
        output.append(divider(width=78))
        
        if item["type"] == "weapon":
            weapon = item["data"]
            output.append(format_stat("Damage", f"+{weapon.damage}", width=78))
            output.append(format_stat("Initiative Mod", f"{weapon.initiative_mod:+d}", width=78))
            output.append(format_stat("Strength Req", weapon.strength_req, width=78))
            output.append(format_stat("Size", weapon.size, width=78))
            output.append(format_stat("Weapon Type", weapon.weapon_type.title(), width=78))
            if weapon.capacity != "single":
                output.append(format_stat("Capacity", weapon.capacity.title(), width=78))
            if weapon.tags:
                output.append(format_stat("Special Tags", weapon.tags, width=78))

        elif item["type"] == "armor":
            armor = item["data"]
            output.append(format_stat("General Armor", armor.general_armor, width=78))
            output.append(format_stat("Ballistic Armor", armor.ballistic_armor, width=78))
            output.append(format_stat("Strength Req", armor.strength_req, width=78))
            output.append(format_stat("Defense Penalty", f"{armor.defense_penalty:+d}", width=78))
            output.append(format_stat("Speed Penalty", f"{armor.speed_penalty:+d}", width=78))
            output.append(format_stat("Coverage", ", ".join(armor.coverage), width=78))
            if armor.notes:
                output.append(format_stat("Notes", armor.notes, width=78))

        output.append(footer(width=78, char="-"))
        self.caller.msg("\n".join(output))
    
    def resource_status(self):
        """Show character's resource status"""
        status_info = PURCHASE_CONFIG.get_status_info(self.caller)

        output = [header(f"Resource Status: {self.caller.name}", width=78, char="=")]
        output.append(format_stat("Mode", status_info["mode"], width=78))
        output.append(format_stat("Resources Merit", status_info["resource_rating"], width=78))

        if status_info["mode"] == "Absolute Value":
            output.append(format_stat("Max Availability", status_info["max_availability"], width=78))
            output.append(format_stat("Purchases This Period", f"{status_info['purchases_this_period']}/{status_info['max_purchases']}", width=78))
        else:
            output.append(format_stat("Current Pool", status_info["current_pool"], width=78))
            output.append(format_stat("Maximum Pool", status_info["max_pool"], width=78))
            output.append(format_stat("Next Refresh", status_info["next_refresh"].strftime("%Y-%m-%d"), width=78))

        merits = self.caller.db.stats.get("merits", {})
        bonus_sources = []
        for merit_name, bonus_per_dot in PURCHASE_CONFIG.bonus_merits.items():
            merit_dots = merits.get(merit_name, {}).get("dots", 0)
            if merit_dots > 0:
                bonus = int(merit_dots * bonus_per_dot)
                if bonus > 0:
                    bonus_sources.append(f"{merit_name.title()} {merit_dots} (+{bonus})")

        if bonus_sources:
            output.append(format_stat("Resource Bonuses", ", ".join(bonus_sources), width=78))

        output.append(footer(width=78, char="="))
        self.caller.msg("\n".join(output))
    
    def show_help(self):
        """Show purchasing help"""
        output = [header("Equipment Purchasing System", width=78, char="=")]
        output.append(format_stat("Resource Mode", PURCHASE_CONFIG.resource_mode.title(), width=78))
        output.append(format_stat("Refresh Period", f"{PURCHASE_CONFIG.refresh_period_days} days", width=78))
        output.append(divider(width=78))

        if PURCHASE_CONFIG.resource_mode == "absolute":
            output.append(section_header("Absolute Mode", width=78))
            output.append("  Resources merit rating determines max item availability.")
            output.append("  Resources 3 can buy any Availability 3 or lower item.")
            output.append("  Purchase limits may apply per period.")
        else:
            output.append(section_header("Pool Mode", width=78))
            output.append("  Gain resource points equal to Resources merit each period.")
            output.append("  Spend points to purchase items (Availability = cost).")
            output.append("  Can save up for expensive items." if PURCHASE_CONFIG.allow_saving else "  Cannot save points between periods.")

        output.append(divider(width=78))
        output.append(section_header("Commands", width=78))
        output.append("  +buy/list [category] - List equipment  +buy/info <item> - Item details")
        output.append("  +buy <item> - Purchase  +buy/status - Resource status")
        output.append(section_header("Merit Bonuses", width=78))
        for merit_name, bonus_per_dot in PURCHASE_CONFIG.bonus_merits.items():
            output.append(format_stat(merit_name.title(), f"+{bonus_per_dot} per dot", width=78))

        output.append(footer(width=78, char="="))
        self.caller.msg("\n".join(output))

class CmdBuyConfig(MuxCommand, DeveloperMixin):
    """
    Configure equipment purchasing system (Developer+ only).
    
    Usage:
        +buyconfig/mode <pool|absolute> - Set resource mode
        +buyconfig/period <days> - Set refresh period
        +buyconfig/maxpurchases <number> - Set max purchases per period
        +buyconfig/saving <on|off> - Allow saving resource points
        +buyconfig/bonus <merit> <bonus_per_dot> - Set merit bonus
        +buyconfig/remove <merit> - Remove merit bonus
        +buyconfig/script <start|stop|restart|status> - Manage refresh script
        +buyconfig/status - Show current configuration
        +buyconfig/reset - Reset to defaults
        
    Examples:
        +buyconfig/mode pool - Use resource pool system
        +buyconfig/period 14 - Refresh every 2 weeks
        +buyconfig/maxpurchases 5 - Max 5 purchases per period
        +buyconfig/bonus contacts 1 - Contacts merit gives +1 per dot
        +buyconfig/remove fame - Remove fame merit bonus
        +buyconfig/script start - Start automatic refresh script
    """
    
    key = "+buyconfig"
    aliases = ["+purchaseconfig"]
    help_category = "Gear & Resources"
    
    def func(self):
        """Execute the command"""
        if not self.check_developer_access():
            return

        if not self.switches:
            self.caller.msg("Usage: +buyconfig/mode, +buyconfig/period, +buyconfig/status, etc. Use +buyconfig/help for full list.")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "mode":
            self.set_mode()
        elif switch == "period":
            self.set_period()
        elif switch == "maxpurchases":
            self.set_max_purchases()
        elif switch == "saving":
            self.set_saving()
        elif switch == "bonus":
            self.set_bonus()
        elif switch == "remove":
            self.remove_bonus()
        elif switch == "status":
            self.show_config()
        elif switch == "reset":
            self.reset_config()
        elif switch == "help":
            self.show_config_help()
        elif switch == "script":
            self.manage_refresh_script()
        else:
            self.caller.msg("Invalid switch. Use +buyconfig/help for available options.")
    
    def set_mode(self):
        """Set resource mode"""
        if not self.args:
            self.caller.msg("Usage: +buyconfig/mode <pool|absolute>")
            return
            
        mode = self.args.strip().lower()
        if mode not in ["pool", "absolute"]:
            self.caller.msg("Mode must be 'pool' or 'absolute'")
            return
            
        PURCHASE_CONFIG.resource_mode = mode
        self.caller.msg(f"Set resource mode to: {mode}")
    
    def set_period(self):
        """Set refresh period"""
        if not self.args:
            self.caller.msg("Usage: +buyconfig/period <days>")
            return
            
        try:
            days = int(self.args.strip())
            if days < 1:
                self.caller.msg("Period must be at least 1 day")
                return
        except ValueError:
            self.caller.msg("Period must be a number of days")
            return
            
        PURCHASE_CONFIG.refresh_period_days = days
        self.caller.msg(f"Set refresh period to: {days} days")
    
    def set_max_purchases(self):
        """Set maximum purchases per period"""
        if not self.args:
            self.caller.msg("Usage: +buyconfig/maxpurchases <number|unlimited>")
            return
            
        arg = self.args.strip().lower()
        if arg in ["unlimited", "none", "0"]:
            PURCHASE_CONFIG.max_purchases_per_period = None
            self.caller.msg("Set maximum purchases to: unlimited")
        else:
            try:
                max_purchases = int(arg)
                if max_purchases < 1:
                    self.caller.msg("Maximum purchases must be at least 1")
                    return
                PURCHASE_CONFIG.max_purchases_per_period = max_purchases
                self.caller.msg(f"Set maximum purchases per period to: {max_purchases}")
            except ValueError:
                self.caller.msg("Maximum purchases must be a number or 'unlimited'")
    
    def set_saving(self):
        """Set whether players can save resource points"""
        if not self.args:
            self.caller.msg("Usage: +buyconfig/saving <on|off>")
            return
            
        setting = self.args.strip().lower()
        if setting in ["on", "true", "yes", "1"]:
            PURCHASE_CONFIG.allow_saving = True
            self.caller.msg("Resource point saving: ENABLED")
        elif setting in ["off", "false", "no", "0"]:
            PURCHASE_CONFIG.allow_saving = False
            self.caller.msg("Resource point saving: DISABLED")
        else:
            self.caller.msg("Setting must be 'on' or 'off'")
    
    def set_bonus(self):
        """Set merit bonus for resources"""
        args = self.args.split()
        if len(args) != 2:
            self.caller.msg("Usage: +buyconfig/bonus <merit_name> <bonus_per_dot>")
            return
            
        merit_name = args[0].lower()
        try:
            bonus_per_dot = float(args[1])
        except ValueError:
            self.caller.msg("Bonus per dot must be a number")
            return
            
        PURCHASE_CONFIG.bonus_merits[merit_name] = bonus_per_dot
        self.caller.msg(f"Set {merit_name} bonus to: {bonus_per_dot} per dot")
    
    def remove_bonus(self):
        """Remove a merit bonus"""
        if not self.args:
            self.caller.msg("Usage: +buyconfig/remove <merit_name>")
            return
            
        merit_name = self.args.strip().lower()
        
        if merit_name not in PURCHASE_CONFIG.bonus_merits:
            self.caller.msg(f"Merit '{merit_name}' does not have a resource bonus.")
            available_merits = ", ".join(PURCHASE_CONFIG.bonus_merits.keys())
            self.caller.msg(f"Available merit bonuses: {available_merits}")
            return
            
        # Remove the merit bonus
        del PURCHASE_CONFIG.bonus_merits[merit_name]
        self.caller.msg(f"Removed resource bonus for {merit_name} merit.")
    
    def show_config(self):
        """Show current configuration"""
        output = [header("Equipment Purchase Configuration", width=78, char="=")]
        output.append(format_stat("Resource Mode", PURCHASE_CONFIG.resource_mode.title(), width=78))
        output.append(format_stat("Refresh Period", f"{PURCHASE_CONFIG.refresh_period_days} days", width=78))
        output.append(format_stat("Max Purchases", PURCHASE_CONFIG.max_purchases_per_period or "Unlimited", width=78))
        output.append(format_stat("Allow Saving", "Yes" if PURCHASE_CONFIG.allow_saving else "No", width=78))
        output.append(section_header("Merit Bonuses", width=78))
        for merit_name, bonus in PURCHASE_CONFIG.bonus_merits.items():
            output.append(format_stat(merit_name.title(), f"+{bonus} per dot", width=78))
        output.append(footer(width=78, char="="))
        self.caller.msg("\n".join(output))
    
    def reset_config(self):
        """Reset configuration to defaults"""
        global PURCHASE_CONFIG
        PURCHASE_CONFIG = EquipmentPurchasingConfig()
        self.caller.msg("Reset equipment purchase configuration to defaults.")
    
    def manage_refresh_script(self):
        """Manage the resource refresh script"""
        if not self.args:
            self.caller.msg("Usage: +buyconfig/script <start|stop|restart|status>")
            return
            
        action = self.args.strip().lower()
        
        if action == "start":
            try:
                from world.scripts.resource_refresh_script import create_resource_refresh_script
                script = create_resource_refresh_script()
                self.caller.msg("Resource refresh script started successfully.")
                self.caller.msg(f"Script will run every hour to check for resource refreshes.")
            except Exception as e:
                self.caller.msg(f"Error starting script: {e}")
                
        elif action == "stop":
            try:
                from world.scripts.resource_refresh_script import stop_resource_refresh_script
                count = stop_resource_refresh_script()
                if count > 0:
                    self.caller.msg(f"Stopped {count} resource refresh script(s).")
                else:
                    self.caller.msg("No resource refresh scripts were running.")
            except Exception as e:
                self.caller.msg(f"Error stopping script: {e}")
                
        elif action == "restart":
            try:
                from world.scripts.resource_refresh_script import create_resource_refresh_script
                script = create_resource_refresh_script()
                self.caller.msg("Resource refresh script restarted successfully.")
            except Exception as e:
                self.caller.msg(f"Error restarting script: {e}")
                
        elif action == "status":
            try:
                from evennia import search_object
                scripts = search_object("resource_refresh_script", 
                                       typeclass="world.scripts.resource_refresh_script.ResourceRefreshScript")
                if scripts:
                    script = scripts[0]
                    self.caller.msg(f"Resource refresh script is RUNNING.")
                    self.caller.msg(f"Interval: {script.interval} seconds (every hour)")
                    self.caller.msg(f"Next run: {script.time_until_next_repeat()} seconds")
                else:
                    self.caller.msg("Resource refresh script is NOT RUNNING.")
                    self.caller.msg("Use '+buyconfig/script start' to start it.")
            except Exception as e:
                self.caller.msg(f"Error checking script status: {e}")
                
        else:
            self.caller.msg("Invalid action. Use: start, stop, restart, or status")
    
    def show_config_help(self):
        """Show configuration help"""
        output = [header("Equipment Purchase Configuration Help", width=78, char="=")]
        output.append(section_header("Available Commands", width=78))
        output.append("  +buyconfig/mode <pool|absolute>     - Set resource spending mode")
        output.append("  +buyconfig/period <days>            - Set refresh frequency")
        output.append("  +buyconfig/maxpurchases <number>     - Limit purchases per period")
        output.append("  +buyconfig/saving <on|off>           - Allow saving resource points")
        output.append("  +buyconfig/bonus <merit> <bonus>    - Set merit resource bonus")
        output.append("  +buyconfig/remove <merit>            - Remove merit resource bonus")
        output.append("  +buyconfig/script <start|stop|status> - Manage refresh script")
        output.append("  +buyconfig/status                   - Show current settings")
        output.append("  +buyconfig/reset                    - Reset to defaults")
        output.append(section_header("Resource Modes", width=78))
        output.append("  |wPool:|n Gain points each period; spend on items; can save up.")
        output.append("  |wAbsolute:|n Buy any item Availability ≤ Resources merit; purchase limits apply.")
        output.append(section_header("Examples", width=78))
        output.append("  +buyconfig/mode pool  +buyconfig/period 30  +buyconfig/bonus contacts 1")
        output.append(footer(width=78, char="="))
        self.caller.msg("\n".join(output))


class CmdAddResources(MuxCommand, DeveloperMixin, TargetResolutionMixin):
    """
    Grant resource points to a character for purchasing equipment (Builder+ only).
    
    Usage:
        +addresources <character> <amount>
        
    In pool mode, adds points to the target's resource pool. Negative amounts
    reduce the pool (to a minimum of 0). Only works when resource mode is "pool".
    
    Examples:
        +addresources Alice 5 - Grant Alice 5 resource points
        +addresources Bob -2 - Remove 2 resource points from Bob
    """
    
    key = "+addresources"
    aliases = ["+grantresources", "+resourcegrant"]
    help_category = "Gear & Resources"
    
    def func(self):
        """Execute the command"""
        if not self.check_developer_access():
            return

        args = self.args.split()
        if len(args) < 2:
            self.caller.msg("Usage: +addresources <character> <amount>")
            self.caller.msg("Example: +addresources Alice 5")
            return
            
        target_name = args[0]
        try:
            amount = int(args[1])
        except ValueError:
            self.caller.msg("Amount must be a number.")
            return
            
        target = self.find_target(target_name)
        if not target:
            return
            
        success, message = add_resource_points(target, amount)
        
        if success:
            self.caller.msg(f"|g{message}|n")
            if amount > 0:
                target.msg(f"Staff has granted you {amount} resource points for equipment purchases.")
            elif amount < 0:
                target.msg(f"Staff has adjusted your resource points by {amount}.")
        else:
            self.caller.msg(f"|r{message}|n")
