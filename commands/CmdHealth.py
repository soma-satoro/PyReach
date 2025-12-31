from evennia.commands.default.muxcommand import MuxCommand
from world.utils.health_utils import (
    get_health_track, compact_track, set_health_track, 
    get_health_display, get_health_display_with_penalty, parse_damage_type, damage_severity
)
from world.utils.permission_utils import check_builder_permission
from utils.search_helpers import search_character

class CmdHealth(MuxCommand):
    """
    Manage health and damage.
    
    Usage:
        +health - Show current health status
        +health <character> - View another character's health (staff only)
        +health/hurt <amount> [type] - Take damage (bashing/lethal/aggravated)
        +health/hurt <character>=<amount> [type] - Apply damage to character (staff only)
        +health/heal <amount> [type] - Heal damage 
        +health/heal <character>=<amount> [type] - Heal character's damage (staff only)
        +health/set <health_level> <type> - Set specific health box (staff only)
        +health/clear - Clear all damage 
        +health/clear <character> - Clear character's damage (staff only)
        +health/max <amount> - Set maximum health (staff only)
        +health/max <character>=<amount> - Set character's max health (staff only)
        
    Damage Types:
        bashing (b) - Represented by / (cyan)
        lethal (l) - Represented by X (red) 
        aggravated (a) - Represented by * (bright red)
        
    Examples:
        +health/hurt 2 lethal - Take 2 lethal damage
        +health/hurt John=3 bashing - Staff: Apply 3 bashing to John
        +health/heal 1 bashing - Heal 1 bashing damage
        +health/heal Jane=2 lethal - Staff: Heal 2 lethal from Jane
        +health/clear - Clear all damage
        +health/clear John - Staff: Clear John's damage
        +health John - Staff: View John's health
        
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
        
        # Parse target character for staff
        target = self.caller
        remaining_args = self.args
        is_staff = self.caller.check_permstring("Admin")
        
        # No switches - display health (check if args might be a character name)
        if not self.switches:
            if self.args:
                # Staff can view other characters
                if not is_staff:
                    self.caller.msg("|rYou can only view your own health. Staff can view others' health.|n")
                    return
                
                target = search_character(self.caller, self.args)
                if not target:
                    return
            
            # Get health stats for target
            advantages = target.db.stats.get("advantages", {})
            health_max = advantages.get("health", 7)
            
            # Initialize health damage dict if needed
            if not hasattr(target.db, 'health_damage') or target.db.health_damage is None:
                target.db.health_damage = {}
            
            display = self._get_health_display(target)
            if target == self.caller:
                self.caller.msg(f"Health: {display}")
            else:
                self.caller.msg(f"{target.name}'s Health: {display}")
            
            # Show damage summary
            track = self._get_health_track(target)
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
        if "hurt" in self.switches:
            if not self.args:
                self.caller.msg("Usage: +health/hurt <amount> [type] or +health/hurt <character>=<amount> [type]")
                return
            
            # Check for staff targeting another character (format: <char>=<amount> [type])
            if "=" in self.args:
                if not is_staff:
                    self.caller.msg("|rOnly staff can apply damage to other characters.|n")
                    return
                
                parts = self.args.split("=", 1)
                target_name = parts[0].strip()
                remaining_args = parts[1].strip()
                
                target = search_character(self.caller, target_name)
                if not target:
                    return
            else:
                remaining_args = self.args
            
            # Initialize target's health damage if needed
            if not hasattr(target.db, 'health_damage') or target.db.health_damage is None:
                target.db.health_damage = {}
            
            args_list = remaining_args.split()
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
            applied = self._apply_damage(target, amount, damage_type)
            
            if target == self.caller:
                if applied < amount:
                    self.caller.msg(f"Applied {applied} {damage_type} damage (health track full).")
                else:
                    self.caller.msg(f"You take {applied} {damage_type} damage.")
            else:
                if applied < amount:
                    self.caller.msg(f"Applied {applied} {damage_type} damage to {target.name} (health track full).")
                else:
                    self.caller.msg(f"You apply {applied} {damage_type} damage to {target.name}.")
                target.msg(f"You take {applied} {damage_type} damage.")
            
            # Show new health status
            display = self._get_health_display(target)
            if target == self.caller:
                self.caller.msg(f"Health: {display}")
            else:
                self.caller.msg(f"{target.name}'s Health: {display}")
            
            # Check for incapacitation
            track = self._get_health_track(target)
            if all(box is not None for box in track):
                if target == self.caller:
                    self.caller.msg("|rYou are incapacitated!|n")
                else:
                    self.caller.msg(f"|r{target.name} is incapacitated!|n")
                    target.msg("|rYou are incapacitated!|n")
        
        elif "heal" in self.switches:
            if not self.args:
                self.caller.msg("Usage: +health/heal <amount> [type] or +health/heal <character>=<amount> [type]")
                return
            
            # Check for staff targeting another character (format: <char>=<amount> [type])
            if "=" in self.args:
                if not is_staff:
                    self.caller.msg("|rOnly staff can heal other characters.|n")
                    return
                
                parts = self.args.split("=", 1)
                target_name = parts[0].strip()
                remaining_args = parts[1].strip()
                
                target = search_character(self.caller, target_name)
                if not target:
                    return
            else:
                remaining_args = self.args
            
            # Initialize target's health damage if needed
            if not hasattr(target.db, 'health_damage') or target.db.health_damage is None:
                target.db.health_damage = {}
            
            args_list = remaining_args.split()
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
            healed = self._heal_damage(target, amount, damage_type)
            
            if target == self.caller:
                if healed == 0:
                    self.caller.msg(f"No {damage_type} damage to heal.")
                else:
                    self.caller.msg(f"You heal {healed} {damage_type} damage.")
            else:
                if healed == 0:
                    self.caller.msg(f"{target.name} has no {damage_type} damage to heal.")
                else:
                    self.caller.msg(f"You heal {healed} {damage_type} damage from {target.name}.")
                    target.msg(f"You heal {healed} {damage_type} damage.")
            
            # Show new health status
            display = self._get_health_display(target)
            if target == self.caller:
                self.caller.msg(f"Health: {display}")
            else:
                self.caller.msg(f"{target.name}'s Health: {display}")
        
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
            # Check for staff targeting another character
            if self.args:
                if not is_staff:
                    self.caller.msg("|rOnly staff can clear other characters' damage.|n")
                    return
                
                target = search_character(self.caller, self.args)
                if not target:
                    return
            
            # Initialize target's health damage if needed
            if not hasattr(target.db, 'health_damage') or target.db.health_damage is None:
                target.db.health_damage = {}
            
            target.db.health_damage = {}
            
            if target == self.caller:
                self.caller.msg("All damage cleared.")
            else:
                self.caller.msg(f"All damage cleared from {target.name}.")
                target.msg("All damage cleared.")
            
            # Show new health status
            display = self._get_health_display(target)
            if target == self.caller:
                self.caller.msg(f"Health: {display}")
            else:
                self.caller.msg(f"{target.name}'s Health: {display}")
        
        elif "max" in self.switches:
            # Staff only
            if not is_staff:
                self.caller.msg("You don't have permission to set maximum health.")
                return
            
            if not self.args:
                self.caller.msg("Usage: +health/max <amount> or +health/max <character>=<amount>")
                return
            
            # Check for targeting another character (format: <char>=<amount>)
            if "=" in self.args:
                parts = self.args.split("=", 1)
                target_name = parts[0].strip()
                amount_str = parts[1].strip()
                
                target = search_character(self.caller, target_name)
                if not target:
                    return
            else:
                amount_str = self.args
            
            if not amount_str.isdigit():
                self.caller.msg("Amount must be a number.")
                return
            
            new_max = int(amount_str)
            if new_max < 1:
                self.caller.msg("Maximum health must be at least 1.")
                return
            
            # Update stats
            if not target.db.stats:
                target.db.stats = {}
            if "advantages" not in target.db.stats:
                target.db.stats["advantages"] = {}
            
            target.db.stats["advantages"]["health"] = new_max
            
            # Clear any damage beyond new maximum
            health_damage = target.db.health_damage or {}
            for level in list(health_damage.keys()):
                if level > new_max:
                    del health_damage[level]
            target.db.health_damage = health_damage
            
            if target == self.caller:
                self.caller.msg(f"Maximum health set to {new_max}.")
            else:
                self.caller.msg(f"{target.name}'s maximum health set to {new_max}.")
                target.msg(f"Your maximum health has been set to {new_max}.")
            
            # Show new health status
            display = self._get_health_display(target)
            if target == self.caller:
                self.caller.msg(f"Health: {display}")
            else:
                self.caller.msg(f"{target.name}'s Health: {display}")
        
        else:
            self.caller.msg("Valid switches: /hurt, /heal, /set, /clear, /max") 