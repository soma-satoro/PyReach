from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.conditions import Condition, STANDARD_CONDITIONS
from utils.search_helpers import search_character

class CmdCondition(MuxCommand):
    """
    Manage conditions on characters.
    
    Usage:
        +condition/add [character] = <condition_name>
        +condition/remove [character] = <condition_name>
        +condition/list [character]
        +condition/help <condition_name>
        
    Examples:
        +condition/add = blind
        +condition/add self = blind
        +condition/remove = frightened
        +condition/remove John = frightened (admin only)
        +condition/list
        +condition/help blind
    """
    key = "+condition"
    aliases = ["+cond"]
    locks = "cmd:all()"
    help_category = "Skill and Condition Checks"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
    
    def func(self):
        """
        This is the main command function that handles the switches.
        """
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        if is_legacy_mode():
            self.caller.msg("|rConditions system is disabled in Legacy Mode.|n")
            self.caller.msg("Legacy Mode uses traditional World of Darkness mechanics without conditions.")
            return
        
        if not self.switches:
            self.caller.msg("Usage: +condition/add, +condition/remove, +condition/list, or +condition/help")
            return
            
        # Get the switch and call the appropriate method
        switch = self.switches[0].lower()
        if switch == "add":
            self.cond_add()
        elif switch == "remove":
            self.cond_remove()
        elif switch == "list":
            self.cond_list()
        elif switch == "help":
            self.cond_help()
        else:
            self.caller.msg("Invalid switch. Use: add, remove, list, or help")
    
    def _check_permission(self, target):
        """Check if caller has permission to modify target's conditions"""
        if target == self.caller:
            return True
        return self.caller.check_permstring("Admin")
    
    def cond_add(self):
        """Add a condition to a character"""
        if not self.args or "=" not in self.args:
            self.caller.msg("Usage: +condition/add [character] = <condition_name>")
            return
            
        parts = self.args.split("=", 1)
        if len(parts) == 2:
            target_name, condition_name = [part.strip() for part in parts]
        else:
            # If no target specified, default to caller
            target_name = "self"
            condition_name = parts[0].strip()
        
        # Find the target
        target = search_character(self.caller, target_name)
        if not target:
            return
            
        # Check permissions
        if not self._check_permission(target):
            self.caller.msg("You can only add conditions to yourself. Admins can add conditions to others.")
            return
            
        # Check if condition exists
        condition_name = condition_name.lower()
        if condition_name not in STANDARD_CONDITIONS:
            self.caller.msg(f"Unknown condition: {condition_name}")
            return
            
        # Add the condition
        condition = STANDARD_CONDITIONS[condition_name]
        target.conditions.add(condition)
        self.caller.msg(f"Added condition {condition.name} to {target.name}")

    def cond_remove(self):
        """Remove a condition from a character"""
        if not self.args or "=" not in self.args:
            self.caller.msg("Usage: +condition/remove [character] = <condition_name>")
            return
            
        parts = self.args.split("=", 1)
        if len(parts) == 2:
            target_name, condition_name = [part.strip() for part in parts]
        else:
            # If no target specified, default to caller
            target_name = "self"
            condition_name = parts[0].strip()
        
        # Find the target
        target = search_character(self.caller, target_name)
        if not target:
            return
            
        # Check permissions
        if not self._check_permission(target):
            self.caller.msg("You can only remove conditions from yourself. Admins can remove conditions from others.")
            return
            
        # Remove the condition
        if target.conditions.remove(condition_name):
            self.caller.msg(f"Removed condition {condition_name} from {target.name}")
        else:
            self.caller.msg(f"{target.name} does not have the condition {condition_name}")

    def cond_list(self):
        """List all conditions on a character"""
        if not self.args:
            target = self.caller
        else:
            target = search_character(self.caller, self.args)
            if not target:
                return
                
        conditions = target.conditions.all()
        if not conditions:
            self.caller.msg(f"{target.name} has no conditions.")
            return
            
        # Format the output
        output = [f"Conditions on {target.name}:"]
        for condition in conditions:
            output.append(f"  {condition.name}: {condition.description}")
            if condition.duration:
                output.append(f"    Duration: {condition.duration}")
            if condition.resolution_method:
                output.append(f"    Resolution: {condition.resolution_method}")
                
        self.caller.msg("\n".join(output))

    def cond_help(self):
        """Get information about a specific condition"""
        if not self.args:
            self.caller.msg("Usage: +condition/help <condition_name>")
            return
            
        condition_name = self.args.strip().lower()
        if condition_name not in STANDARD_CONDITIONS:
            self.caller.msg(f"Unknown condition: {condition_name}")
            return
            
        condition = STANDARD_CONDITIONS[condition_name]
        output = [
            f"Condition: {condition.name}",
            f"Type: {'Persistent' if condition.is_persistent else 'Temporary'}",
            "",
            f"Description: {condition.description}"
        ]
        
        if condition.possible_sources:
            output.append("")
            output.append(f"Possible Sources: {condition.possible_sources}")
        
        if condition.beat:
            output.append("")
            output.append(f"Beat: {condition.beat}")
        
        if condition.resolution_method:
            output.append("")
            output.append(f"Resolution: {condition.resolution_method}")
        
        if condition.duration:
            output.append("")
            output.append(f"Duration: {condition.duration}")
        
        if condition.effects:
            output.append("")
            output.append("Effects:")
            for effect, value in condition.effects.items():
                output.append(f"  {effect}: {value}")
                
        self.caller.msg("\n".join(output)) 