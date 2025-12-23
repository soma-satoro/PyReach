from evennia.commands.default.muxcommand import MuxCommand
from world.utils.health_utils import (
    get_health_track, compact_track, set_health_track, 
    get_health_display, get_health_display_with_penalty, parse_damage_type, damage_severity
)
from world.utils.permission_utils import check_builder_permission

class CmdHealth(MuxCommand):
    """
    Manage health and damage.
    
    Usage:
        +health - Show current health status
        +health/damage <amount> [type] - Take damage (bashing/lethal/aggravated)
        +health/heal <amount> [type] - Heal damage 
        +health/set <health_level> <type> - Set specific health box
        +health/clear - Clear all damage 
        +health/max <amount> - Set maximum health (staff only)
        
    Damage Types:
        bashing (b) - Represented by / (cyan)
        lethal (l) - Represented by X (red) 
        aggravated (a) - Represented by * (bright red)
        
    Examples:
        +health/damage 2 lethal - Take 2 lethal damage
        +health/damage 1 - Take 1 bashing damage (default)
        +health/heal 1 bashing - Heal 1 bashing damage
        +health/set 3 aggravated - Set health level 3 to aggravated
        +health/clear - Clear all damage
        
    Note: More severe damage pushes less severe damage to the right.
    Aggravated > Lethal > Bashing. Healing happens from right to left.
    """
    
    key = "+health"
    aliases = ["health", "damage"]
    help_category = "Chargen & Character Info"
    
    def _get_health_display(self, caller, force_ascii=False):
        """Get a visual representation of current health with wound penalty"""
        return get_health_display_with_penalty(caller, force_ascii)
    
    def _get_health_track(self, caller):
        """Get health track as an array where index 0 is leftmost (most severe)."""
        return get_health_track(caller)
    
    def _set_health_track(self, caller, track):
        """Set health track from array format back to dictionary format."""
        set_health_track(caller, track)
    
    def _damage_severity(self, damage_type):
        """Return numeric severity for damage comparison"""
        return damage_severity(damage_type)
    
    def _parse_damage_type(self, type_str):
        """Parse damage type from string"""
        return parse_damage_type(type_str)
    
    def _apply_damage(self, caller, amount, damage_type):
        """
        Apply damage using World of Darkness rules:
        - Bashing: goes in leftmost empty spot
        - Lethal: goes in leftmost non-lethal/aggravated spot, pushes bashing right
        - Aggravated: goes in leftmost non-aggravated spot, pushes everything right
        """
        track = self._get_health_track(caller)
        health_max = len(track)
        applied = 0
        
        for _ in range(amount):
            if applied >= amount:
                break
                
            # Find insertion point based on damage type
            insert_pos = None
            
            if damage_type == "bashing":
                # Bashing goes in leftmost empty spot
                for i in range(health_max):
                    if track[i] is None:
                        insert_pos = i
                        break
            elif damage_type == "lethal":
                # Lethal goes in leftmost spot that's not lethal or aggravated
                for i in range(health_max):
                    if track[i] is None or track[i] == "bashing":
                        insert_pos = i
                        break
            elif damage_type == "aggravated":
                # Aggravated goes in leftmost spot that's not aggravated
                for i in range(health_max):
                    if track[i] != "aggravated":
                        insert_pos = i
                        break
            
            # If no valid position found, health track is full
            if insert_pos is None:
                break
            
            # Apply the damage with proper pushing
            if not self._insert_damage_with_push(track, insert_pos, damage_type, health_max):
                break  # Couldn't apply damage, track full
            
            applied += 1
        
        self._set_health_track(caller, track)
        return applied
    
    def _insert_damage_with_push(self, track, insert_pos, damage_type, health_max):
        """
        Insert damage at position and push less severe damage to the right.
        Returns True if successful, False if track is full.
        """
        # Collect all damage from insert_pos to end that needs to be pushed
        damage_to_push = []
        for i in range(insert_pos, health_max):
            if track[i] is not None:
                damage_to_push.append(track[i])
            track[i] = None
        
        # Place the new damage
        track[insert_pos] = damage_type
        
        # Now place the pushed damage back, maintaining severity order
        current_pos = insert_pos + 1
        for old_damage in damage_to_push:
            # Find the correct position for this damage
            placed = False
            for pos in range(current_pos, health_max):
                if track[pos] is None:
                    track[pos] = old_damage
                    placed = True
                    break
            
            if not placed:
                # Track is full, damage is lost
                return len([d for d in damage_to_push if d == old_damage]) == 1
        
        return True
    
    def _heal_damage(self, caller, amount, damage_type):
        """
        Heal damage from right to left (most recent first), then compact the track.
        """
        track = self._get_health_track(caller)
        health_max = len(track)
        healed = 0
        
        # Heal from right to left
        for i in range(health_max - 1, -1, -1):
            if healed >= amount:
                break
                
            if track[i] == damage_type:
                track[i] = None
                healed += 1
        
        # Compact the track - move all damage left to eliminate gaps
        compact_track(track)
        
        self._set_health_track(caller, track)
        return healed
    


    def func(self):
        """Manage health and damage"""
        
        # Get current health stats
        advantages = self.caller.db.stats.get("advantages", {})
        health_max = advantages.get("health", 7)
        
        # Initialize health damage dict if needed
        if not hasattr(self.caller.db, 'health_damage') or self.caller.db.health_damage is None:
            self.caller.db.health_damage = {}
        
        # No switches - just display current health
        if not self.switches:
            display = self._get_health_display(self.caller)
            self.caller.msg(f"Health: {display}")
            
            # Show damage summary
            track = self._get_health_track(self.caller)
            damage_counts = {"bashing": 0, "lethal": 0, "aggravated": 0}
            for damage_type in track:
                if damage_type:
                    damage_counts[damage_type] += 1
            
            summary = []
            for dtype, count in damage_counts.items():
                if count > 0:
                    summary.append(f"{count} {dtype}")
            
            if summary:
                self.caller.msg(f"Damage: {', '.join(summary)}")
            else:
                self.caller.msg("No damage taken.")
            return
        
        # Handle switches
        if "damage" in self.switches:
            if not self.args:
                self.caller.msg("Usage: +health/damage <amount> [type]")
                return
            
            args_list = self.args.split()
            try:
                amount = int(args_list[0])
            except (ValueError, IndexError):
                self.caller.msg("Amount must be a number.")
                return
            
            damage_type = self._parse_damage_type(args_list[1] if len(args_list) > 1 else "bashing")
            
            if amount < 1:
                self.caller.msg("Damage amount must be at least 1.")
                return
            
            # Apply damage using WoD rules
            applied = self._apply_damage(self.caller, amount, damage_type)
            
            if applied < amount:
                self.caller.msg(f"Applied {applied} {damage_type} damage (health track full).")
            else:
                self.caller.msg(f"You take {applied} {damage_type} damage.")
            
            # Show new health status
            display = self._get_health_display(self.caller)
            self.caller.msg(f"Health: {display}")
            
            # Check for incapacitation
            track = self._get_health_track(self.caller)
            if all(box is not None for box in track):
                self.caller.msg("|rYou are incapacitated!|n")
        
        elif "heal" in self.switches:
            if not self.args:
                self.caller.msg("Usage: +health/heal <amount> [type]")
                return
            
            args_list = self.args.split()
            try:
                amount = int(args_list[0])
            except (ValueError, IndexError):
                self.caller.msg("Amount must be a number.")
                return
            
            damage_type = self._parse_damage_type(args_list[1] if len(args_list) > 1 else "bashing")
            
            if amount < 1:
                self.caller.msg("Heal amount must be at least 1.")
                return
            
            # Heal damage from right to left
            healed = self._heal_damage(self.caller, amount, damage_type)
            
            if healed == 0:
                self.caller.msg(f"No {damage_type} damage to heal.")
            else:
                self.caller.msg(f"You heal {healed} {damage_type} damage.")
            
            # Show new health status
            display = self._get_health_display(self.caller)
            self.caller.msg(f"Health: {display}")
        
        elif "set" in self.switches:
            # Staff only
            if not check_builder_permission(self.caller):
                self.caller.msg("You don't have permission to set health.")
                return
            
            if not self.args:
                self.caller.msg("Usage: +health/set <health_level> <type>")
                return
            
            args_list = self.args.split()
            try:
                health_level = int(args_list[0])
                damage_type = self._parse_damage_type(args_list[1] if len(args_list) > 1 else "clear")
            except (ValueError, IndexError):
                self.caller.msg("Usage: +health/set <health_level> <type>")
                return
            
            if health_level < 1 or health_level > health_max:
                self.caller.msg(f"Health level must be between 1 and {health_max}.")
                return
            
            health_damage = self.caller.db.health_damage
            
            if damage_type == "clear":
                if health_level in health_damage:
                    del health_damage[health_level]
                    self.caller.msg(f"Cleared damage from health level {health_level}.")
                else:
                    self.caller.msg(f"Health level {health_level} has no damage.")
            else:
                health_damage[health_level] = damage_type
                self.caller.msg(f"Set health level {health_level} to {damage_type} damage.")
            
            self.caller.db.health_damage = health_damage
            
            # Show new health status
            display = self._get_health_display(self.caller)
            self.caller.msg(f"Health: {display}")
        
        elif "clear" in self.switches:
           
            self.caller.db.health_damage = {}
            self.caller.msg("All damage cleared.")
            
            # Show new health status
            display = self._get_health_display(self.caller)
            self.caller.msg(f"Health: {display}")
        
        elif "max" in self.switches:
            # Staff only
            if not check_builder_permission(self.caller):
                self.caller.msg("You don't have permission to set maximum health.")
                return
            
            if not self.args or not self.args.isdigit():
                self.caller.msg("Usage: +health/max <amount>")
                return
            
            new_max = int(self.args)
            if new_max < 1:
                self.caller.msg("Maximum health must be at least 1.")
                return
            
            # Update stats
            if not self.caller.db.stats:
                self.caller.db.stats = {}
            if "advantages" not in self.caller.db.stats:
                self.caller.db.stats["advantages"] = {}
            
            self.caller.db.stats["advantages"]["health"] = new_max
            
            # Clear any damage beyond new maximum
            health_damage = self.caller.db.health_damage or {}
            for level in list(health_damage.keys()):
                if level > new_max:
                    del health_damage[level]
            self.caller.db.health_damage = health_damage
            
            self.caller.msg(f"Maximum health set to {new_max}.")
            
            # Show new health status
            display = self._get_health_display(self.caller)
            self.caller.msg(f"Health: {display}")
        
        else:
            self.caller.msg("Valid switches: /damage, /heal, /set, /clear, /max") 