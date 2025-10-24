"""
Resource Refresh Script for Equipment Purchasing System

This script runs periodically to refresh resource pools for all characters
based on their configured refresh periods.
"""

from evennia.scripts.scripts import DefaultScript
from evennia import search_object
from world.equipment_purchasing import PURCHASE_CONFIG
from datetime import datetime, timedelta
import time

class ResourceRefreshScript(DefaultScript):
    """
    Script that periodically refreshes resource pools for all characters.
    
    This script runs every hour and checks if any characters need their
    resource pools refreshed based on their individual refresh periods.
    """
    
    def at_script_creation(self):
        """Called when the script is first created"""
        self.key = "resource_refresh_script"
        self.desc = "Refreshes character resource pools for equipment purchasing"
        self.interval = 3600  # Run every hour (3600 seconds)
        self.persistent = True  # Survive server restarts
        self.start_delay = True  # Don't run immediately on creation
        
    def at_repeat(self):
        """Called every interval (hourly)"""
        self.refresh_all_character_resources()
        
    def refresh_all_character_resources(self):
        """Refresh resource pools for all characters that need it"""
        # Find all character objects
        characters = search_object(typeclass="typeclasses.characters.Character")
        
        refreshed_count = 0
        error_count = 0
        
        for character in characters:
            try:
                if self.refresh_character_resources(character):
                    refreshed_count += 1
            except Exception as e:
                error_count += 1
                # Log the error but don't stop processing other characters
                character.msg(f"Error refreshing your resource pool: {e}")
                
        # Log results (only if there were refreshes or errors)
        if refreshed_count > 0 or error_count > 0:
            print(f"Resource Refresh: {refreshed_count} characters refreshed, {error_count} errors")
    
    def refresh_character_resources(self, character):
        """Refresh resources for a single character if needed"""
        # Skip characters without stats or Resources merit
        if not hasattr(character.db, 'stats') or not character.db.stats:
            return False
            
        merits = character.db.stats.get("merits", {})
        if "resources" not in merits or merits["resources"].get("dots", 0) == 0:
            return False  # No Resources merit, skip
            
        # Check if character needs refresh
        if not hasattr(character.db, 'resource_pool') or character.db.resource_pool is None:
            # First time setup - initialize with full points
            resource_limit = PURCHASE_CONFIG.get_resource_limit(character)
            character.db.resource_pool = {
                'points': resource_limit,
                'last_refresh': time.time(),
                'purchases_this_period': 0
            }
            character.msg(f"Your resource pool has been initialized with {resource_limit} points.")
            return True
            
        pool_data = character.db.resource_pool
        
        # Ensure valid timestamp
        if 'last_refresh' not in pool_data or pool_data['last_refresh'] is None:
            pool_data['last_refresh'] = time.time()
            return False
            
        # Check if refresh is needed
        last_refresh = datetime.fromtimestamp(pool_data['last_refresh'])
        now = datetime.now()
        days_since_refresh = (now - last_refresh).days
        
        if days_since_refresh >= PURCHASE_CONFIG.refresh_period_days:
            # Time to refresh!
            resource_limit = PURCHASE_CONFIG.get_resource_limit(character)
            old_points = pool_data.get('points', 0)
            
            if PURCHASE_CONFIG.allow_saving:
                # Add new points to existing (up to double limit)
                new_points = min(old_points + resource_limit, resource_limit * 2)
            else:
                # Reset to full
                new_points = resource_limit
                
            pool_data['points'] = new_points
            pool_data['last_refresh'] = time.time()
            pool_data['purchases_this_period'] = 0
            
            # Notify character if they're online
            if character.sessions.all():
                points_gained = new_points - old_points
                if points_gained > 0:
                    character.msg(f"Your resource pool has been refreshed! Gained {points_gained} points (now {new_points}).")
                else:
                    character.msg(f"Your resource pool has been refreshed! You have {new_points} points.")
                    
            return True
            
        return False  # No refresh needed


def create_resource_refresh_script():
    """Create or restart the resource refresh script"""
    # Check if script already exists
    existing_scripts = search_object("resource_refresh_script", typeclass="world.scripts.resource_refresh_script.ResourceRefreshScript")
    
    if existing_scripts:
        # Stop existing script
        for script in existing_scripts:
            script.stop()
            script.delete()
    
    # Create new script
    script = ResourceRefreshScript.create("resource_refresh_script")
    return script


def stop_resource_refresh_script():
    """Stop the resource refresh script"""
    scripts = search_object("resource_refresh_script", typeclass="world.scripts.resource_refresh_script.ResourceRefreshScript")
    
    for script in scripts:
        script.stop()
        script.delete()
        
    return len(scripts)
