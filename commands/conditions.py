from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.conditions import Condition, STANDARD_CONDITIONS
from utils.search_helpers import search_character

class CmdCondition(MuxCommand):
    """
    Manage conditions on characters.
    
    Usage:
        +condition - Show your current conditions
        +condition <character> - View another character's conditions (staff only)
        +condition/add <condition_name> - Add condition to yourself
        +condition/add <character> = <condition_name> - Add condition to character (staff only)
        +condition/remove <condition_name> - Remove condition from yourself
        +condition/remove <character> = <condition_name> - Remove condition from character (staff only)
        +condition/list - Show all available conditions in the system
        +condition/help <condition_name> - Show detailed information about a condition
        
    Examples:
        +condition - View your conditions
        +condition John - Staff: view John's conditions
        +condition/add blind - Add blind condition to yourself
        +condition/remove frightened - Remove frightened from yourself
        +condition/add John = blind - Staff: add blind to John
        +condition/list - See all conditions available
        +condition/help blind - See details about the blind condition
    """
    key = "+condition"
    aliases = ["+cond", "+conditions"]
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
        
        # No switches - show current conditions
        if not self.switches:
            self.cond_show()
            return
            
        # Get the switch and call the appropriate method
        switch = self.switches[0].lower()
        if switch == "add":
            self.cond_add()
        elif switch == "remove":
            self.cond_remove()
        elif switch == "list":
            self.cond_list_all()
        elif switch == "help":
            self.cond_help()
        else:
            self.caller.msg("Invalid switch. Use: add, remove, list, or help")
    
    def _format_section_header(self, section_name):
        """
        Create an arrow-style section header that spans 78 characters.
        Format: <----------------- SECTION NAME ----------------->
        """
        total_width = 78
        # Strip color codes for length calculation
        import re
        clean_name = re.sub(r'\|[a-z]', '', section_name)
        name_length = len(clean_name)
        # Account for < and > characters (2 total) and spaces around name (2 total)
        available_dash_space = total_width - name_length - 4
        
        # Split dashes evenly, with extra dash on the right if odd number
        left_dashes = available_dash_space // 2
        right_dashes = available_dash_space - left_dashes
        
        return f"|g<{'-' * left_dashes}|n {section_name} |g{'-' * right_dashes}>|n"
    
    def _check_permission(self, target):
        """Check if caller has permission to modify target's conditions"""
        if target == self.caller:
            return True
        return self.caller.check_permstring("Admin")
    
    def cond_add(self):
        """Add a condition to a character"""
        if not self.args:
            self.caller.msg("Usage: +condition/add <condition_name> or +condition/add <character> = <condition_name>")
            return
        
        # Check if there's an equals sign (targeting another character)
        if "=" in self.args:
            parts = self.args.split("=", 1)
            target_name = parts[0].strip()
            condition_name = parts[1].strip()
            
            # Find the target
            target = search_character(self.caller, target_name)
            if not target:
                return
                
            # Check permissions - only staff can target others
            if not self._check_permission(target):
                self.caller.msg("|rYou can only add conditions to yourself. Staff can add conditions to others.|n")
                return
        else:
            # No equals sign - default to self
            target = self.caller
            condition_name = self.args.strip()
            
        # Check if condition exists
        condition_name = condition_name.lower()
        if condition_name not in STANDARD_CONDITIONS:
            self.caller.msg(f"|rUnknown condition: |w{condition_name}|n")
            self.caller.msg("Use |w+condition/list|n to see all available conditions.")
            return
            
        # Add the condition
        condition = STANDARD_CONDITIONS[condition_name]
        target.conditions.add(condition)
        
        if target == self.caller:
            self.caller.msg(f"|gAdded condition |w{condition.name}|g to yourself.|n")
        else:
            self.caller.msg(f"|gAdded condition |w{condition.name}|g to |w{target.name}|g.|n")

    def cond_remove(self):
        """Remove a condition from a character"""
        if not self.args:
            self.caller.msg("Usage: +condition/remove <condition_name> or +condition/remove <character> = <condition_name>")
            return
        
        # Check if there's an equals sign (targeting another character)
        if "=" in self.args:
            parts = self.args.split("=", 1)
            target_name = parts[0].strip()
            condition_name = parts[1].strip()
            
            # Find the target
            target = search_character(self.caller, target_name)
            if not target:
                return
                
            # Check permissions - only staff can target others
            if not self._check_permission(target):
                self.caller.msg("|rYou can only remove conditions from yourself. Staff can remove conditions from others.|n")
                return
        else:
            # No equals sign - default to self
            target = self.caller
            condition_name = self.args.strip()
            
        # Remove the condition
        condition_name = condition_name.lower()
        if target.conditions.remove(condition_name):
            if target == self.caller:
                self.caller.msg(f"|gRemoved condition |w{condition_name}|g from yourself.|n")
            else:
                self.caller.msg(f"|gRemoved condition |w{condition_name}|g from |w{target.name}|g.|n")
        else:
            if target == self.caller:
                self.caller.msg(f"|rYou do not have the condition |w{condition_name}|r.|n")
            else:
                self.caller.msg(f"|r{target.name} does not have the condition |w{condition_name}|r.|n")

    def cond_show(self):
        """Show current conditions on a character"""
        if not self.args:
            target = self.caller
        else:
            # Check permission if viewing someone else
            if not self.caller.check_permstring("Admin"):
                self.caller.msg("|rYou can only view your own conditions. Staff can view others' conditions.|n")
                return
            
            target = search_character(self.caller, self.args)
            if not target:
                return
                
        conditions = target.conditions.all()
        
        # Build formatted output
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{f'Conditions - {target.name}'.center(78)}|n")
        output.append(f"|y{'='*78}|n")
        
        if not conditions:
            output.append("")
            if target == self.caller:
                output.append("|cYou have no active conditions.|n".center(78))
            else:
                output.append(f"|c{target.name} has no active conditions.|n".center(78))
            output.append("")
        else:
            output.append("")
            for condition in conditions:
                # Condition name in white
                output.append(f"|w{condition.name.upper()}|n")
                # Description
                output.append(f"  {condition.description}")
                
                # Additional details
                details = []
                if condition.duration:
                    details.append(f"|cDuration:|n {condition.duration}")
                if condition.resolution_method:
                    details.append(f"|cResolution:|n {condition.resolution_method}")
                
                if details:
                    for detail in details:
                        output.append(f"  {detail}")
                output.append("")
                
        output.append(f"|y{'='*78}|n")
        self.caller.msg("\n".join(output))
    
    def cond_list_all(self):
        """List all available conditions in the system in 3 columns"""
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{'Available Conditions'.center(78)}|n")
        output.append(f"|y{'='*78}|n")
        output.append("")
        output.append("|cUse |w+condition/help <name>|c to see details about a specific condition.|n")
        output.append("")
        
        # Get all condition names and sort them
        condition_names = sorted(STANDARD_CONDITIONS.keys())
        
        # Format in 3 columns
        col_width = 24
        num_cols = 3
        
        # Split into rows
        rows = []
        for i in range(0, len(condition_names), num_cols):
            row = condition_names[i:i+num_cols]
            rows.append(row)
        
        # Format each row
        for row in rows:
            formatted_row = ""
            for i, name in enumerate(row):
                # Title case the name for display
                display_name = name.replace("_", " ").title()
                if i < len(row) - 1:
                    formatted_row += f"|w{display_name:<{col_width}}|n"
                else:
                    formatted_row += f"|w{display_name}|n"
            output.append(formatted_row)
        
        output.append("")
        output.append(f"|y{'='*78}|n")
        self.caller.msg("\n".join(output))

    def cond_help(self):
        """Get information about a specific condition"""
        if not self.args:
            self.caller.msg("Usage: +condition/help <condition_name>")
            return
            
        condition_name = self.args.strip().lower()
        if condition_name not in STANDARD_CONDITIONS:
            self.caller.msg(f"|rUnknown condition: |w{condition_name}|n")
            self.caller.msg("Use |w+condition/list|n to see all available conditions.")
            return
            
        condition = STANDARD_CONDITIONS[condition_name]
        
        # Build formatted output
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{condition.name.center(78)}|n")
        output.append(f"|y{'='*78}|n")
        
        # Type
        output.append(self._format_section_header("|wTYPE|n"))
        condition_type = "|gPersistent|n" if condition.is_persistent else "|cTemporary|n"
        output.append(f"{condition_type}")
        output.append("")
        
        # Description
        output.append(self._format_section_header("|wDESCRIPTION|n"))
        output.append(f"{condition.description}")
        output.append("")
        
        # Possible Sources
        if condition.possible_sources:
            output.append(self._format_section_header("|wPOSSIBLE SOURCES|n"))
            output.append(f"{condition.possible_sources}")
            output.append("")
        
        # Beat
        if condition.beat:
            output.append(self._format_section_header("|wBEAT|n"))
            output.append(f"{condition.beat}")
            output.append("")
        
        # Resolution
        if condition.resolution_method:
            output.append(self._format_section_header("|wRESOLUTION|n"))
            output.append(f"{condition.resolution_method}")
            output.append("")
        
        # Duration
        if condition.duration:
            output.append(self._format_section_header("|wDURATION|n"))
            output.append(f"{condition.duration}")
            output.append("")
        
        # Effects
        if condition.effects:
            output.append(self._format_section_header("|wEFFECTS|n"))
            for effect, value in condition.effects.items():
                output.append(f"|c{effect}:|n {value}")
            output.append("")
                
        output.append(f"|y{'='*78}|n")
        self.caller.msg("\n".join(output)) 