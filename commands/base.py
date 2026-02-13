"""
Base command classes and mixins for shared functionality.
"""

import re
from evennia.commands.default.muxcommand import MuxCommand
from world.utils.permission_utils import (
    check_staff_permission, check_admin_permission, check_builder_permission,
    can_modify_character_stats, format_permission_error
)

class StaffOnlyMixin:
    """Mixin for commands that require staff permissions."""
    
    def check_staff_access(self):
        """Check if caller has staff access, return error message if not."""
        if not check_staff_permission(self.caller):
            self.caller.msg(format_permission_error("Staff"))
            return False
        return True

class AdminOnlyMixin:
    """Mixin for commands that require admin permissions."""
    
    def check_admin_access(self):
        """Check if caller has admin access, return error message if not."""
        if not check_admin_permission(self.caller):
            self.caller.msg(format_permission_error("Admin"))
            return False
        return True

class BuilderMixin:
    """Mixin for commands that require builder permissions."""
    
    def check_builder_access(self):
        """Check if caller has builder access, return error message if not."""
        if not check_builder_permission(self.caller):
            self.caller.msg(format_permission_error("Builder"))
            return False
        return True

class CharacterStatsMixin:
    """Mixin for commands that modify character stats."""
    
    def can_modify_stats(self, target):
        """
        Check if caller can modify target's stats.
        
        Args:
            target: The character whose stats would be modified
            
        Returns:
            bool: True if modification is allowed
        """
        can_modify, reason = can_modify_character_stats(self.caller, target)
        if not can_modify:
            self.caller.msg(reason)
        return can_modify

class HealthMixin:
    """Mixin for commands that work with health systems."""
    
    def get_health_summary(self, character):
        """
        Get a summary of character's current health status.
        
        Args:
            character: The character to check
            
        Returns:
            dict: Health summary with current/max and damage counts
        """
        from world.utils.health_utils import get_health_track
        
        advantages = character.db.stats.get("advantages", {})
        health_max = advantages.get("health", 7)
        track = get_health_track(character)
        
        damage_counts = {"bashing": 0, "lethal": 0, "aggravated": 0}
        for damage_type in track:
            if damage_type:
                damage_counts[damage_type] += 1
        
        total_damage = sum(damage_counts.values())
        
        return {
            "current": health_max - total_damage,
            "maximum": health_max,
            "damage_counts": damage_counts,
            "total_damage": total_damage
        }

class TargetResolutionMixin:
    """Mixin for commands that need to resolve character targets."""
    
    def find_target(self, target_name, global_search=True):
        """
        Find a target character with standardized error handling.
        
        Supports both character names and aliases.
        
        Args:
            target_name: Name or alias to search for
            global_search: Whether to search globally (default: True)
            
        Returns:
            Character object or None if not found
        """
        if not target_name:
            return self.caller
        
        from utils.search_helpers import search_character
        target = search_character(self.caller, target_name, global_search=global_search)
        
        return target

class InputValidationMixin:
    """Mixin for secure input validation and sanitization."""
    
    # Maximum lengths for different input types
    MAX_NAME_LENGTH = 50
    MAX_DESCRIPTION_LENGTH = 4000
    MAX_TITLE_LENGTH = 200
    MAX_MESSAGE_LENGTH = 8000
    
    # Allowed attribute names for dynamic access (whitelist approach)
    SAFE_DB_ATTRIBUTES = {
        'stats', 'approved', 'conditions', 'tilts', 'health', 'willpower',
        'beats', 'experience', 'clues', 'notes', 'leverage', 'anchors',
        'mystery_clues', 'npc_clues', 'places', 'pre_summon_location',
        'prelogout_location', 'public_alts', 'private_alts', 'alt_blocks',
        'pending_alt_requests', 'fractional_beats', 'idle_message',
        # Pool current values
        'willpower_current', 'glamour_current', 'essence_current', 'blood_current',
        'mana_current', 'plasm_current', 'satiety_current', 'instability_current',
        'aether_current', 'pyros_current',
        # Legacy attributes that may need migration
        'strength', 'dexterity', 'stamina', 'presence', 'manipulation', 
        'composure', 'intelligence', 'wits', 'resolve', 'integrity', 'size',
        'template', 'fullname', 'birthdate', 'concept', 'virtue', 'vice'
    }
    
    def validate_input_length(self, input_text, max_length, field_name="Input"):
        """
        Validate input length and provide user-friendly error messages.
        
        Args:
            input_text (str): The input to validate
            max_length (int): Maximum allowed length
            field_name (str): Name of the field for error messages
            
        Returns:
            bool: True if valid, False if too long
        """
        if not input_text:
            return True
            
        if len(input_text) > max_length:
            self.caller.msg(f"|r{field_name} is too long. Maximum {max_length} characters, you provided {len(input_text)}.|n")
            return False
        return True
    
    def sanitize_input(self, input_text, allow_newlines=True):
        """
        Sanitize user input to prevent injection attacks.
        
        Args:
            input_text (str): Input to sanitize
            allow_newlines (bool): Whether to allow newline characters
            
        Returns:
            str: Sanitized input
        """
        if not input_text:
            return ""
            
        # Remove null bytes and control characters except newlines/tabs
        if allow_newlines:
            sanitized = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', input_text)
        else:
            sanitized = re.sub(r'[\x00-\x1F\x7F]', '', input_text)
            
        # Trim excessive whitespace
        sanitized = re.sub(r'\s+', ' ', sanitized).strip()
        
        return sanitized
    
    def safe_getattr(self, obj, attr_name, default=None):
        """
        Safely get attribute from object with whitelist validation.
        
        Args:
            obj: Object to get attribute from
            attr_name (str): Name of attribute
            default: Default value if attribute doesn't exist
            
        Returns:
            Attribute value or default
        """
        # Validate attribute name against whitelist
        if hasattr(obj, 'db') and attr_name not in self.SAFE_DB_ATTRIBUTES:
            self.caller.msg(f"|rAccess to attribute '{attr_name}' is not allowed.|n")
            return default
            
        try:
            return getattr(obj.db if hasattr(obj, 'db') else obj, attr_name, default)
        except (AttributeError, TypeError):
            return default
    
    def safe_setattr(self, obj, attr_name, value):
        """
        Safely set attribute on object with whitelist validation.
        
        Args:
            obj: Object to set attribute on
            attr_name (str): Name of attribute
            value: Value to set
            
        Returns:
            bool: True if successful, False if blocked
        """
        # Validate attribute name against whitelist
        if hasattr(obj, 'db') and attr_name not in self.SAFE_DB_ATTRIBUTES:
            self.caller.msg(f"|rModification of attribute '{attr_name}' is not allowed.|n")
            return False
            
        try:
            setattr(obj.db if hasattr(obj, 'db') else obj, attr_name, value)
            return True
        except (AttributeError, TypeError) as e:
            self.caller.msg(f"|rFailed to set attribute: {e}|n")
            return False
    
    def parse_equals_syntax(self, args, required_parts=2):
        """
        Safely parse command arguments with equals syntax.
        
        Args:
            args (str): Raw arguments
            required_parts (int): Number of parts required after split
            
        Returns:
            list or None: Split parts if valid, None if invalid
        """
        if not args or "=" not in args:
            return None
            
        parts = [part.strip() for part in args.split("=", required_parts - 1)]
        
        if len(parts) != required_parts:
            return None
            
        # Validate each part is not empty
        for i, part in enumerate(parts):
            if not part:
                return None
                
        return parts

class BasePyReachCommand(MuxCommand, InputValidationMixin):
    """
    Base command class for game commands with common functionality and security.
    """
    
    def at_pre_cmd(self):
        """Called before command execution."""
        # Add any global pre-command logic here
        return super().at_pre_cmd()
    
    def at_post_cmd(self):
        """Called after command execution."""
        # Add any global post-command logic here
        return super().at_post_cmd()
    
    def format_error(self, message):
        """Format error messages consistently."""
        return f"|r{message}|n"
    
    def format_success(self, message):
        """Format success messages consistently."""
        return f"|g{message}|n"
    
    def format_info(self, message):
        """Format info messages consistently."""
        return f"|c{message}|n"
