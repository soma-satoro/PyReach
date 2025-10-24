"""
NPC (Non-Player Character) typeclass for Chronicles of Darkness.

NPCs are characters controlled by the game or staff, not players.
They can use the same stat system as player characters and be puppeted.
"""

from evennia.objects.objects import DefaultCharacter
from evennia.utils import lazy_property
from world.cofd.stat_dictionary import attribute_dictionary, skill_dictionary
from .characters import Character

class NPC(Character):
    """
    Base NPC typeclass for Chronicles of Darkness.
    
    NPCs use the same stat system as player characters and can be controlled by staff
    or their creator. They can participate in scenes, combat, and social interactions.
    """
    
    def at_object_creation(self):
        """Called when NPC is first created."""
        super().at_object_creation()
        
        # Set NPC flag
        self.db.is_npc = True
        
        # NPC-specific attributes
        self.db.npc_type = "standard"  # standard, minor, major, boss
        self.db.threat_level = 1  # 1-5 scale
        self.db.creator = None  # Who created this NPC
        self.db.controllers = []  # List of characters who can control this NPC
        
        # Puppeting support
        self.db.puppetable = True
        
        # Auto-approve NPCs so they can be modified
        self.db.approved = False
        
        # Set default mortal template
        if "other" not in self.db.stats:
            self.db.stats["other"] = {}
        self.db.stats["other"]["template"] = "Mortal"
    
    def get_display_name(self, looker=None, **kwargs):
        """Return the display name with NPC indicator."""
        name = super().get_display_name(looker, **kwargs)
        if looker and (looker.check_permstring("Builder") or looker in self.db.controllers):
            return f"{name} |y(NPC)|n"
        return name
    
    def at_say(self, message, msg_self=None, msg_location=None, receivers=None, msg_receivers=None, **kwargs):
        """NPCs speak with a different color when not puppeted."""
        # Only color differently if not being puppeted
        if not self.account:
            message = f"|c{message}|n"
        super().at_say(message, msg_self, msg_location, receivers, msg_receivers, **kwargs)
    
    def can_puppet(self, account):
        """Check if an account can puppet this NPC."""
        if not account or not account.character:
            return False
            
        character = account.character
        
        # Staff can always puppet
        if character.check_permstring("Builder"):
            return True
            
        # Creator can puppet
        if self.db.creator and self.db.creator == character:
            return True
            
        # Authorized controllers can puppet
        if character in self.db.controllers:
            return True
            
        return False
    
    def can_control(self, character):
        """Check if a character can control this NPC (legacy method)."""
        if character.check_permstring("Builder"):
            return True
        if self.db.creator and self.db.creator == character:
            return True
        if character in self.db.controllers:
            return True
        return False
    
    def set_creator(self, character):
        """Set who created this NPC."""
        self.db.creator = character
        if character:
            character.msg(f"You are now the creator of {self.name}.")
    
    def add_controller(self, character):
        """Add a character who can control this NPC."""
        if character not in self.db.controllers:
            self.db.controllers.append(character)
            character.msg(f"You now have control permissions for {self.name}.")
            return True
        return False
    
    def remove_controller(self, character):
        """Remove a character's control permissions."""
        if character in self.db.controllers:
            self.db.controllers.remove(character)
            character.msg(f"You no longer have control permissions for {self.name}.")
            return True
        return False
    
    def start_puppeting(self, account):
        """Handle when an account starts puppeting this NPC."""
        if not self.can_puppet(account):
            account.msg("You don't have permission to puppet that NPC.")
            return False
            
        # Store the account's original character
        if account.character and account.character != self:
            self.db.original_character = account.character
            
        # Set up puppeting
        account.puppet_object(None)  # Unpuppet current
        account.puppet_object(self)  # Puppet the NPC
        
        self.msg("You are now puppeting this NPC. Use 'unpuppet' to return to your character.")
        return True
    
    def stop_puppeting(self, account):
        """Handle when an account stops puppeting this NPC."""
        original_char = self.db.original_character
        
        # Unpuppet the NPC
        account.puppet_object(None)
        
        # Return to original character if it exists
        if original_char:
            account.puppet_object(original_char)
            self.db.original_character = None
            account.msg(f"You are no longer puppeting {self.name}.")
            return True
        else:
            account.msg(f"You are no longer puppeting {self.name}. You have no active character.")
            return False
    
    def generate_random_stats(self, archetype="standard", template="Mortal"):
        """Generate random stats based on archetype and template."""
        from world.cofd.npc_archetypes import get_archetype
        
        # Get the archetype configuration
        archetype_config = get_archetype(archetype, template)
        if not archetype_config:
            return False
            
        # Set template first
        success, message = self.set_template(template, reset_stats=True)
        if not success:
            return False
            
        # Apply archetype-based stat generation
        archetype_config.apply_to_npc(self)
        
        # Calculate derived stats
        self.calculate_derived_stats()
        
        return True
    
    def quick_stats(self, stat_type, stat_name):
        """Quick stat lookup for NPCs using the character stat system."""
        if not self.db.stats:
            return 0
            
        if stat_type == "attribute":
            return self.db.stats.get("attributes", {}).get(stat_name, 0)
        elif stat_type == "skill":
            return self.db.stats.get("skills", {}).get(stat_name, 0)
        elif stat_type == "merit":
            merit_data = self.db.stats.get("merits", {}).get(stat_name, {})
            return merit_data.get("dots", 0) if isinstance(merit_data, dict) else 0
        elif stat_type == "advantage":
            return self.db.stats.get("advantages", {}).get(stat_name, 0)
        elif stat_type == "other":
            return self.db.stats.get("other", {}).get(stat_name, 0)
        
        return 0
    
    def take_damage(self, amount, damage_type="bashing"):
        """Damage tracking for NPCs using the character system."""
        if not hasattr(self.db, 'health_damage'):
            self.db.health_damage = {}
            
        # Add damage to tracking
        if damage_type not in self.db.health_damage:
            self.db.health_damage[damage_type] = 0
        self.db.health_damage[damage_type] += amount
        
        # Check total damage
        total_damage = sum(self.db.health_damage.values())
        health = self.db.stats.get("advantages", {}).get("health", 7)
        
        if total_damage >= health:
            self.location.msg_contents(f"{self.name} is incapacitated!")
            self.db.incapacitated = True
    
    def heal_damage(self, amount, damage_type=None):
        """Heal damage from the NPC."""
        if not hasattr(self.db, 'health_damage'):
            self.db.health_damage = {}
            return
            
        if damage_type:
            # Heal specific damage type
            if damage_type in self.db.health_damage:
                self.db.health_damage[damage_type] = max(0, self.db.health_damage[damage_type] - amount)
        else:
            # Heal any damage (prioritize bashing first)
            remaining = amount
            for dtype in ["bashing", "lethal", "aggravated"]:
                if dtype in self.db.health_damage and remaining > 0:
                    healed = min(remaining, self.db.health_damage[dtype])
                    self.db.health_damage[dtype] -= healed
                    remaining -= healed
        
        # Check if no longer incapacitated
        total_damage = sum(self.db.health_damage.values())
        health = self.db.stats.get("advantages", {}).get("health", 7)
        
        if total_damage < health:
            self.db.incapacitated = False


class MinorNPC(NPC):
    """
    Minor NPCs with reduced stats.
    Used for crowds, basic antagonists, etc.
    """
    
    def at_object_creation(self):
        """Set up minor NPC."""
        super().at_object_creation()
        self.db.npc_type = "minor"
        self.db.threat_level = 1


class MajorNPC(NPC):
    """
    Major NPCs with enhanced stats.
    Important story characters, recurring antagonists, etc.
    """
    
    def at_object_creation(self):
        """Set up major NPC."""
        super().at_object_creation()
        self.db.npc_type = "major"
        self.db.threat_level = 3


class BossNPC(NPC):
    """
    Boss NPCs with exceptional capabilities.
    Major antagonists, powerful entities, etc.
    """
    
    def at_object_creation(self):
        """Set up boss NPC."""
        super().at_object_creation()
        self.db.npc_type = "boss"
        self.db.threat_level = 5
        
        # Boss-specific abilities
        self.db.boss_actions = 2  # Extra actions per turn
        self.db.damage_resistance = {"bashing": 1, "lethal": 0, "aggravated": 0} 