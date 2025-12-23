from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.equipment_database import WEAPON_DATABASE, ARMOR_DATABASE, WeaponData, ArmorData
from world.equipment_purchasing import PURCHASE_CONFIG, get_available_equipment, can_purchase_equipment, purchase_equipment, EquipmentPurchasingConfig
from .base import BuilderMixin


class CmdEquipment(MuxCommand):
    """
    Manage equipment, weapons, and armor.
    
    Usage:
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
            self.caller.msg("Usage: +equipment/list, +equipment/add, +equipment/remove, +equipment/view, +equipment/wield, +equipment/wear, +equipment/weapons, or +equipment/armor")
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
            self.caller.msg("You have no equipment")
            return
            
        output = ["Your Equipment:"]
        
        # Check what's currently equipped
        wielded_weapon = self.caller.db.wielded_weapon
        worn_armor = self.caller.db.worn_armor
        
        # Group by type
        weapons = []
        armor = []
        equipment = []
        styles = []
        
        for name, item in self.caller.db.equipment.items():
            if item["type"] == "weapon":
                status = " (wielded)" if name == wielded_weapon else ""
                weapons.append(f"{name} (Dmg: {item.get('damage', 0)}, Initiative: {item.get('initiative', 0):+d}){status}")
            elif item["type"] == "armor":
                status = " (worn)" if name == worn_armor else ""
                armor.append(f"{name} (Armor: {item.get('general_armor', 0)}/{item.get('ballistic_armor', 0)}){status}")
            elif item["type"] == "equipment":
                equipment.append(f"{name} (Availability {item['rating']})")
            elif item["type"] == "style":
                styles.append(f"{name} ({item['rating']} dots)")
                
        if weapons:
            output.append("\nWeapons:")
            output.extend(f"  {item}" for item in sorted(weapons))
            
        if armor:
            output.append("\nArmor:")
            output.extend(f"  {item}" for item in sorted(armor))
            
        if equipment:
            output.append("\nEquipment:")
            output.extend(f"  {item}" for item in sorted(equipment))
            
        if styles:
            output.append("\nFighting Styles:")
            output.extend(f"  {item}" for item in sorted(styles))
            
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
            
        # Initialize equipment if not exists
        if not self.caller.db.equipment:
            self.caller.db.equipment = {}
            
        if name in self.caller.db.equipment:
            self.caller.msg(f"You already have {name}")
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
        
        if not self.caller.db.equipment or name not in self.caller.db.equipment:
            self.caller.msg(f"You don't have {name}")
            return
            
        # Check if item is currently equipped
        if name == self.caller.db.wielded_weapon:
            self.caller.db.wielded_weapon = None
            self.caller.msg(f"You stop wielding {name}")
        if name == self.caller.db.worn_armor:
            self.caller.db.worn_armor = None
            self.caller.msg(f"You remove {name}")
            
        del self.caller.db.equipment[name]
        self.caller.msg(f"Removed {name}")
    
    def view_equipment(self):
        """View equipment details"""
        name = self.args.strip()
        
        if not self.caller.db.equipment or name not in self.caller.db.equipment:
            self.caller.msg(f"You don't have {name}")
            return
            
        item = self.caller.db.equipment[name]
        
        output = [
            f"Name: {name}",
            f"Type: {item['type'].title()}"
        ]
        
        # Add type-specific information
        if item["type"] == "weapon":
            output.extend([
                f"Damage: {item['damage']}",
                f"Initiative: {item['initiative']:+d}",
                f"Strength: {item['strength']}",
                f"Size: {item['size']}",
                f"Range: {item['range']}",
                f"Availability: {item['availability']}"
            ])
            if item.get("capacity"):
                output.append(f"Capacity: {item['capacity']}")
            if item.get("tags"):
                output.append(f"Tags: {item['tags']}")
                
        elif item["type"] == "armor":
            output.extend([
                f"General Armor: {item['general_armor']}",
                f"Ballistic Armor: {item['ballistic_armor']}",
                f"Strength Requirement: {item['strength']}",
                f"Defense Penalty: {item['defense']:+d}",
                f"Speed Penalty: {item['speed']:+d}",
                f"Availability: {item['availability']}"
            ])
            if item.get("coverage"):
                output.append(f"Coverage: {', '.join(item['coverage'])}")
            if item.get("notes"):
                output.append(f"Notes: {item['notes']}")
                
        elif item["type"] == "equipment":
            output.append(f"Availability: {item['rating']}")
            
        elif item["type"] == "style":
            output.extend([
                f"Dots: {item['rating']}",
                f"Description: Fighting style technique"
            ])
            
        self.caller.msg("\n".join(output))
    
    def wield_weapon(self):
        """Wield a weapon"""
        weapon_name = self.args.strip()
        
        if not weapon_name:
            self.caller.msg("Usage: +equipment/wield <weapon>")
            return
            
        if not self.caller.db.equipment or weapon_name not in self.caller.db.equipment:
            self.caller.msg(f"You don't have {weapon_name}")
            return
            
        item = self.caller.db.equipment[weapon_name]
        if item["type"] != "weapon":
            self.caller.msg(f"{weapon_name} is not a weapon")
            return
            
        # Unwield current weapon if any
        if self.caller.db.wielded_weapon:
            self.caller.msg(f"You stop wielding {self.caller.db.wielded_weapon}")
            
        self.caller.db.wielded_weapon = weapon_name
        self.caller.msg(f"You wield {weapon_name}")
        self.caller.location.msg_contents(
            f"{self.caller.name} wields {weapon_name}.",
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
            
        if not self.caller.db.equipment or armor_name not in self.caller.db.equipment:
            self.caller.msg(f"You don't have {armor_name}")
            return
            
        item = self.caller.db.equipment[armor_name]
        if item["type"] != "armor":
            self.caller.msg(f"{armor_name} is not armor")
            return
            
        # Remove current armor if any
        if self.caller.db.worn_armor:
            self.caller.msg(f"You remove {self.caller.db.worn_armor}")
            
        self.caller.db.worn_armor = armor_name
        self.caller.msg(f"You wear {armor_name}")
        self.caller.location.msg_contents(
            f"{self.caller.name} puts on {armor_name}.",
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
        output = ["Available Weapons (from Chronicles of Darkness: Hurt Locker):"]
        
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
                output.append(f"\n|c{category}:|n")
                for weapon in sorted(weapons):
                    output.append(f"  {weapon}")
        
        output.append("\nDamage types are determined automatically based on weapon category.")
        output.append("Use '+equipment/add <weapon_name> weapon' to add a weapon.")
        output.append("Use '+equipment/view <weapon_name>' for detailed information.")
        self.caller.msg("\n".join(output))
    
    def list_available_armor(self):
        """List all available armor that can be added"""
        output = ["Available Armor (from Chronicles of Darkness: Hurt Locker):"]
        
        # Separate modern and archaic armor
        modern_armor = []
        archaic_armor = []
        
        for armor_key, armor in ARMOR_DATABASE.items():
            armor_str = f"{armor.name} - Armor:{armor.general_armor}/{armor.ballistic_armor} Str:{armor.strength_req} Def:{armor.defense_penalty:+d} Spd:{armor.speed_penalty:+d} Avail:{armor.availability}"
            
            if any(modern in armor_key for modern in ["reinforced", "sports", "kevlar", "flak", "riot", "bomb", "helmet_modern"]):
                modern_armor.append(armor_str)
            else:
                archaic_armor.append(armor_str)
        
        if modern_armor:
            output.append(f"\n|cModern Armor:|n")
            for armor in sorted(modern_armor):
                output.append(f"  {armor}")
                
        if archaic_armor:
            output.append(f"\n|cArchaic Armor:|n")
            for armor in sorted(archaic_armor):
                output.append(f"  {armor}")
        
        output.append("\nArmor format: General/Ballistic armor ratings")
        output.append("General armor reduces total damage, Ballistic downgrades firearm lethal to bashing")
        output.append("Use '+equipment/add <armor_name> armor' to add armor.")
        output.append("Use '+equipment/view <armor_name>' for detailed information.")
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
            
        output = [f"|c{title}|n"]
        output.append(f"Resource Mode: |y{PURCHASE_CONFIG.resource_mode.title()}|n")
        output.append("")
        
        # Group by availability
        by_availability = {}
        for key, item in items.items():
            avail = item['availability']
            if avail not in by_availability:
                by_availability[avail] = []
            by_availability[avail].append((key, item))
        
        # Display by availability level
        for availability in sorted(by_availability.keys()):
            output.append(f"|yAvailability {availability}:|n")
            
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
                    
                output.append(f"  {afford_indicator} |y{item['name']}|n - {details}")
        
        output.append("")
        output.append("|yUsage:|n")
        output.append("  +buy <item> - Purchase item")
        output.append("  +buy/info <item> - Get detailed information")
        output.append("  +buy/status - Check your resource status")
        
        self.caller.msg("\n".join(output))
    
    def item_info(self):
        """Get detailed information about an item"""
        if not self.args:
            self.caller.msg("Usage: +buy/info <item>")
            return
            
        item_name = self.args.strip().lower().replace(" ", "_")
        available_equipment = get_available_equipment()
        
        if item_name not in available_equipment:
            self.caller.msg(f"Unknown item: {item_name}")
            return
            
        item = available_equipment[item_name]
        
        output = [f"|cEquipment Information: {item['name']}|n"]
        output.append(f"Type: {item['type'].title()}")
        output.append(f"Availability: {item['availability']}")
        
        # Check affordability
        can_afford, afford_message = can_purchase_equipment(self.caller, item_name)
        afford_status = "|gAffordable|n" if can_afford else f"|rNot Affordable|n ({afford_message})"
        output.append(f"Status: {afford_status}")
        output.append("")
        
        # Add type-specific details
        if item['type'] == 'weapon':
            weapon = item['data']
            output.extend([
                f"Damage: +{weapon.damage}",
                f"Initiative Modifier: {weapon.initiative_mod:+d}",
                f"Strength Requirement: {weapon.strength_req}",
                f"Size: {weapon.size}",
                f"Weapon Type: {weapon.weapon_type.title()}"
            ])
            
            if weapon.capacity != "single":
                output.append(f"Capacity: {weapon.capacity.title()}")
                
            if weapon.tags:
                output.append(f"Special Tags: {weapon.tags}")
                
        elif item['type'] == 'armor':
            armor = item['data']
            output.extend([
                f"General Armor: {armor.general_armor}",
                f"Ballistic Armor: {armor.ballistic_armor}",
                f"Strength Requirement: {armor.strength_req}",
                f"Defense Penalty: {armor.defense_penalty:+d}",
                f"Speed Penalty: {armor.speed_penalty:+d}",
                f"Coverage: {', '.join(armor.coverage)}"
            ])
            
            if armor.notes:
                output.append(f"Notes: {armor.notes}")
        
        self.caller.msg("\n".join(output))
    
    def resource_status(self):
        """Show character's resource status"""
        status_info = PURCHASE_CONFIG.get_status_info(self.caller)
        
        output = [f"|cResource Status for {self.caller.name}|n"]
        output.append(f"Mode: {status_info['mode']}")
        output.append(f"Resources Merit Rating: {status_info['resource_rating']}")
        
        if status_info['mode'] == 'Absolute Value':
            output.append(f"Maximum Item Availability: {status_info['max_availability']}")
            output.append(f"Purchases This Period: {status_info['purchases_this_period']}/{status_info['max_purchases']}")
        else:
            output.append(f"Current Resource Pool: {status_info['current_pool']}")
            output.append(f"Maximum Pool: {status_info['max_pool']}")
            output.append(f"Next Refresh: {status_info['next_refresh'].strftime('%Y-%m-%d')}")
            
        # Show bonus merits
        merits = self.caller.db.stats.get("merits", {})
        bonus_sources = []
        for merit_name, bonus_per_dot in PURCHASE_CONFIG.bonus_merits.items():
            merit_dots = merits.get(merit_name, {}).get("dots", 0)
            if merit_dots > 0:
                bonus = int(merit_dots * bonus_per_dot)
                if bonus > 0:
                    bonus_sources.append(f"{merit_name.title()} {merit_dots} (+{bonus})")
                    
        if bonus_sources:
            output.append(f"Resource Bonuses: {', '.join(bonus_sources)}")
            
        self.caller.msg("\n".join(output))
    
    def show_help(self):
        """Show purchasing help"""
        output = [
            "|cEquipment Purchasing System|n",
            "",
            f"|yResource Mode:|n {PURCHASE_CONFIG.resource_mode.title()}",
            f"|yRefresh Period:|n {PURCHASE_CONFIG.refresh_period_days} days",
        ]
        
        if PURCHASE_CONFIG.resource_mode == "absolute":
            output.extend([
                "",
                "|yAbsolute Mode:|n",
                "- Your Resources merit rating determines maximum item availability",
                "- Resources 3 can buy any Availability 3 or lower item",
                "- Purchase limits may apply per period"
            ])
        else:
            output.extend([
                "",
                "|yPool Mode:|n", 
                "- Gain resource points equal to Resources merit each period",
                "- Spend points to purchase items (Availability = cost)",
                "- Can save up points for expensive items" if PURCHASE_CONFIG.allow_saving else "- Cannot save points between periods"
            ])
            
        output.extend([
            "",
            "|yCommands:|n",
            "+buy/list [category] - List available equipment",
            "+buy/info <item> - Get item details",
            "+buy <item> - Purchase item",
            "+buy/status - Check resource status",
            "",
            "|yMerit Bonuses:|n"
        ])
        
        for merit_name, bonus_per_dot in PURCHASE_CONFIG.bonus_merits.items():
            output.append(f"  {merit_name.title()}: +{bonus_per_dot} per dot")
            
        self.caller.msg("\n".join(output))

class CmdBuyConfig(MuxCommand, BuilderMixin):
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
        if not self.check_builder_access():
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
        output = [
            "|cEquipment Purchase Configuration|n",
            f"Resource Mode: {PURCHASE_CONFIG.resource_mode.title()}",
            f"Refresh Period: {PURCHASE_CONFIG.refresh_period_days} days",
            f"Max Purchases: {PURCHASE_CONFIG.max_purchases_per_period or 'Unlimited'}",
            f"Allow Saving: {'Yes' if PURCHASE_CONFIG.allow_saving else 'No'}",
            "",
            "|yMerit Bonuses:|n"
        ]
        
        for merit_name, bonus in PURCHASE_CONFIG.bonus_merits.items():
            output.append(f"  {merit_name.title()}: +{bonus} per dot")
            
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
        output = [
            "|cEquipment Purchase Configuration Help|n",
            "",
            "|yAvailable Commands:|n",
            "+buyconfig/mode <pool|absolute> - Set resource spending mode",
            "+buyconfig/period <days> - Set how often resources refresh",
            "+buyconfig/maxpurchases <number> - Limit purchases per period",
            "+buyconfig/saving <on|off> - Allow saving resource points",
            "+buyconfig/bonus <merit> <bonus> - Set merit resource bonus",
            "+buyconfig/remove <merit> - Remove merit resource bonus",
            "+buyconfig/script <start|stop|status> - Manage automatic refresh script",
            "+buyconfig/status - Show current settings",
            "+buyconfig/reset - Reset to defaults",
            "",
            "|yResource Modes:|n",
            "|yPool Mode:|n Characters gain resource points each period equal to their Resources merit.",
            "They spend these points to buy items. Can save up for expensive items.",
            "",
            "|yAbsolute Mode:|n Characters can buy any item with Availability ≤ their Resources merit.",
            "Purchase frequency is limited by max purchases per period setting.",
            "",
            "|yExamples:|n",
            "+buyconfig/mode pool - Use resource pool system",
            "+buyconfig/period 30 - Monthly refresh (default)",
            "+buyconfig/bonus contacts 1 - Contacts merit adds +1 resource per dot"
        ]
        
        self.caller.msg("\n".join(output))
