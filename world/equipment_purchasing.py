"""
Equipment Purchasing System for Chronicles of Darkness
Flexible system that allows staff to configure purchasing rules per game
"""

import time
from datetime import datetime, timedelta
from world.equipment_database import WEAPON_DATABASE, ARMOR_DATABASE, GENERAL_EQUIPMENT_DATABASE

class EquipmentPurchasingConfig:
    """Configuration class for equipment purchasing rules"""
    
    def __init__(self):
        # Default configuration - can be overridden by staff
        self.resource_mode = "pool"  # "pool" or "absolute"
        self.refresh_period_days = 30  # How often resources refresh
        self.max_purchases_per_period = None  # None = unlimited, int = max purchases
        self.allow_saving = True  # Can players save up resource points?
        self.bonus_merits = {  # Merits that provide bonus resources
            "contacts": 1,  # +1 resource per dot
            "allies": 1,    # +1 resource per dot
            "status": 0.5   # +0.5 resource per dot (rounded down)
        }
        
    def get_resource_limit(self, character):
        """Get character's resource limit based on merit and bonuses"""
        merits = character.db.stats.get("merits", {})
        base_resources = merits.get("resources", {}).get("dots", 0)
        
        # Add bonus from other merits
        bonus = 0
        for merit_name, bonus_per_dot in self.bonus_merits.items():
            merit_dots = merits.get(merit_name, {}).get("dots", 0)
            bonus += int(merit_dots * bonus_per_dot)
            
        return base_resources + bonus
    
    def can_afford(self, character, availability_cost):
        """Check if character can afford an item"""
        if self.resource_mode == "absolute":
            # In absolute mode, Resources rating must be >= item availability
            return self.get_resource_limit(character) >= availability_cost
        else:  # pool mode
            current_pool = self.get_current_resource_pool(character)
            return current_pool >= availability_cost
    
    def get_current_resource_pool(self, character):
        """Get character's current resource pool points"""
        resource_limit = self.get_resource_limit(character)
        
        if not hasattr(character.db, 'resource_pool') or character.db.resource_pool is None:
            # First time initialization - give them their starting points
            character.db.resource_pool = {
                'points': resource_limit,  # Start with full resource points
                'last_refresh': time.time(),
                'purchases_this_period': 0
            }
            
        pool_data = character.db.resource_pool
        
        # Ensure all required fields exist and are valid
        if 'last_refresh' not in pool_data or pool_data['last_refresh'] is None:
            pool_data['last_refresh'] = time.time()
        if 'points' not in pool_data:
            pool_data['points'] = resource_limit  # Give them starting points
        if 'purchases_this_period' not in pool_data:
            pool_data['purchases_this_period'] = 0
        
        # Check if it's time to refresh
        last_refresh = datetime.fromtimestamp(pool_data['last_refresh'])
        now = datetime.now()
        days_since_refresh = (now - last_refresh).days
        
        if days_since_refresh >= self.refresh_period_days:
            # Refresh the pool
            resource_limit = self.get_resource_limit(character)
            if self.allow_saving:
                # Add new points to existing (up to double limit)
                pool_data['points'] = min(pool_data['points'] + resource_limit, resource_limit * 2)
            else:
                # Reset to full
                pool_data['points'] = resource_limit
                
            pool_data['last_refresh'] = time.time()
            pool_data['purchases_this_period'] = 0
            
        return pool_data['points']
    
    def spend_resources(self, character, cost):
        """Spend resource points"""
        if self.resource_mode == "absolute":
            # Absolute mode doesn't spend points, just tracks purchases
            if not hasattr(character.db, 'resource_pool') or character.db.resource_pool is None:
                character.db.resource_pool = {
                    'points': 0,
                    'last_refresh': time.time(),
                    'purchases_this_period': 0
                }
            
            pool_data = character.db.resource_pool
            
            # Ensure all required fields exist
            if 'last_refresh' not in pool_data or pool_data['last_refresh'] is None:
                pool_data['last_refresh'] = time.time()
            if 'purchases_this_period' not in pool_data:
                pool_data['purchases_this_period'] = 0
            
            # Check purchase limit
            if (self.max_purchases_per_period and 
                pool_data['purchases_this_period'] >= self.max_purchases_per_period):
                return False, "You have reached your purchase limit for this period."
                
            pool_data['purchases_this_period'] += 1
            return True, f"Purchase successful. {pool_data['purchases_this_period']}/{self.max_purchases_per_period or 'unlimited'} purchases this period."
            
        else:  # pool mode
            current_pool = self.get_current_resource_pool(character)
            if current_pool < cost:
                return False, f"Insufficient resources. You have {current_pool}, need {cost}."
                
            character.db.resource_pool['points'] -= cost
            character.db.resource_pool['purchases_this_period'] += 1
            
            remaining = character.db.resource_pool['points']
            return True, f"Purchase successful. {remaining} resource points remaining."
    
    def get_next_refresh_date(self, character):
        """Get when character's resources will next refresh"""
        if not hasattr(character.db, 'resource_pool') or character.db.resource_pool is None:
            return datetime.now()
            
        pool_data = character.db.resource_pool
        if 'last_refresh' not in pool_data or pool_data['last_refresh'] is None:
            return datetime.now()
            
        last_refresh = datetime.fromtimestamp(pool_data['last_refresh'])
        return last_refresh + timedelta(days=self.refresh_period_days)
    
    def get_status_info(self, character):
        """Get character's resource status information"""
        resource_limit = self.get_resource_limit(character)
        
        if self.resource_mode == "absolute":
            purchases_this_period = 0
            if hasattr(character.db, 'resource_pool') and character.db.resource_pool is not None:
                purchases_this_period = character.db.resource_pool.get('purchases_this_period', 0)
                
            info = {
                'mode': 'Absolute Value',
                'resource_rating': resource_limit,
                'max_availability': resource_limit,
                'current_pool': 'N/A',
                'purchases_this_period': purchases_this_period,
                'max_purchases': self.max_purchases_per_period or 'Unlimited'
            }
        else:  # pool mode
            current_pool = self.get_current_resource_pool(character)
            
            purchases_this_period = 0
            if hasattr(character.db, 'resource_pool') and character.db.resource_pool is not None:
                purchases_this_period = character.db.resource_pool.get('purchases_this_period', 0)
                
            info = {
                'mode': 'Resource Pool',
                'resource_rating': resource_limit,
                'current_pool': current_pool,
                'max_pool': resource_limit * 2 if self.allow_saving else resource_limit,
                'purchases_this_period': purchases_this_period,
                'next_refresh': self.get_next_refresh_date(character)
            }
            
        return info

# Global configuration instance - can be modified by staff
PURCHASE_CONFIG = EquipmentPurchasingConfig()

def get_available_equipment():
    """Get all available equipment for purchase"""
    equipment = {}
    
    # Add weapons
    for key, weapon in WEAPON_DATABASE.items():
        equipment[key] = {
            'name': weapon.name,
            'type': 'weapon',
            'availability': weapon.availability,
            'data': weapon
        }
    
    # Add armor
    for key, armor in ARMOR_DATABASE.items():
        equipment[key] = {
            'name': armor.name,
            'type': 'armor', 
            'availability': armor.availability,
            'data': armor
        }
    
    # Add general equipment
    for key, item in GENERAL_EQUIPMENT_DATABASE.items():
        equipment[key] = {
            'name': item.name,
            'type': 'equipment',
            'category': item.category,
            'availability': item.availability,
            'data': item
        }
        
    return equipment

def can_purchase_equipment(character, equipment_key):
    """Check if character can purchase specific equipment"""
    available_equipment = get_available_equipment()
    
    if equipment_key not in available_equipment:
        return False, "Equipment not found."
        
    item = available_equipment[equipment_key]
    availability = item['availability']
    
    # Check if character can afford it
    if not PURCHASE_CONFIG.can_afford(character, availability):
        if PURCHASE_CONFIG.resource_mode == "absolute":
            resource_limit = PURCHASE_CONFIG.get_resource_limit(character)
            return False, f"You need Resources {availability} to purchase this item. You have Resources {resource_limit}."
        else:
            current_pool = PURCHASE_CONFIG.get_current_resource_pool(character)
            return False, f"You need {availability} resource points. You have {current_pool}."
    
    # Check if character already has this equipment
    if hasattr(character.db, 'equipment') and character.db.equipment:
        if equipment_key in character.db.equipment or item['name'] in character.db.equipment:
            return False, "You already have this equipment."
    
    return True, "Purchase available."

def purchase_equipment(character, equipment_key):
    """Purchase equipment for character"""
    # Check if purchase is allowed
    can_purchase, message = can_purchase_equipment(character, equipment_key)
    if not can_purchase:
        return False, message
        
    available_equipment = get_available_equipment()
    item = available_equipment[equipment_key]
    availability = item['availability']
    
    # Spend resources
    success, spend_message = PURCHASE_CONFIG.spend_resources(character, availability)
    if not success:
        return False, spend_message
        
    # Initialize equipment if needed
    if not hasattr(character.db, 'equipment') or not character.db.equipment:
        character.db.equipment = {}
    
    # Add equipment to character
    if item['type'] == 'weapon':
        weapon = item['data']
        character.db.equipment[item['name']] = {
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
    elif item['type'] == 'armor':
        armor = item['data']
        character.db.equipment[item['name']] = {
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
    elif item['type'] == 'equipment':
        equip = item['data']
        character.db.equipment[item['name']] = {
            "type": "equipment",
            "category": equip.category,
            "die_bonus": equip.die_bonus,
            "durability": equip.durability,
            "size": equip.size,
            "structure": equip.structure,
            "availability": equip.availability,
            "effect": equip.effect,
            "skill_bonuses": equip.skill_bonuses,
            "special_properties": equip.special_properties
        }
    
    return True, f"Purchased {item['name']}! {spend_message}"
