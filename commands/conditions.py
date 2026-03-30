from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.conditions import Condition, STANDARD_CONDITIONS
from world.utils.formatting import footer, get_theme_colors, sheet_section_header
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
        +condition/clear <character> - Clear all conditions from a character (staff only)
        +condition/list - Show all conditions with name, summary, and resolution
        +condition/view <condition_name> - View full details of a condition
        
    Examples:
        +condition - View your conditions
        +condition John - Staff: view John's conditions
        +condition/add blind - Add blind condition to yourself
        +condition/remove frightened - Remove frightened from yourself
        +condition/add John = blind - Staff: add blind to John
        +condition/clear John - Staff: clear all conditions from John
        +condition/list - See all conditions with summaries
        +condition/view blind - See full details about the blind condition
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
        elif switch in ("view", "help"):
            self.cond_view()
        elif switch == "clear":
            self.cond_clear()
        else:
            self.caller.msg("Invalid switch. Use: add, remove, clear, list, or view")
    
    def _format_section_header(self, section_name):
        """Format a section header using theme colors."""
        return sheet_section_header(section_name)
    
    def _short_description(self, description, max_len=70):
        """Get a short summary of a description - first sentence or truncated."""
        if not description or not description.strip():
            return ""
        # Take first paragraph, then first sentence
        first_para = description.split("\n\n")[0].strip()
        if "." in first_para:
            first_sentence = first_para.split(".")[0] + "."
        else:
            first_sentence = first_para
        if len(first_sentence) > max_len:
            return first_sentence[: max_len - 3].rstrip() + "..."
        return first_sentence
    
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

    def cond_clear(self):
        """Clear all conditions from a character (staff only)"""
        if not self.caller.check_permstring("Admin"):
            self.caller.msg("|rOnly staff can clear all conditions.|n")
            return

        if not self.args:
            self.caller.msg("Usage: +condition/clear <character>")
            return

        target = search_character(self.caller, self.args)
        if not target:
            return

        count = target.conditions.clear()
        if target != self.caller:
            target.msg(f"|cA staff member has cleared all your conditions.|n")
        self.caller.msg(f"|gCleared {count} condition(s) from |w{target.name}|g.|n")

    def cond_show(self):
        """Show current conditions on a character"""
        if not self.args:
            target = self.caller
        else:
            # If the argument matches a condition name, show condition details.
            # This allows `+condition <condition_name>` to behave like view/help.
            if self._find_condition_key(self.args.strip()) is not None:
                self.cond_view()
                return

            # Check permission if viewing someone else
            if not self.caller.check_permstring("Admin"):
                self.caller.msg("|rInvalid syntax.|n")
                self.caller.msg("Use |w+condition|n to view your active conditions.")
                self.caller.msg("Use |w+condition/view <condition_name>|n (or |w+condition <condition_name>|n) for condition details.")
                self.caller.msg("See |whelp +condition|n for full usage.")
                return
            
            target = search_character(self.caller, self.args)
            if not target:
                self.caller.msg("Use |w+condition/view <condition_name>|n to view condition details.")
                return
                
        conditions = target.conditions.all()
        
        # Build formatted output
        output = []
        output.append(footer(78, char="="))
        _, text_color, _ = get_theme_colors()
        output.append(f"|{text_color}{f'Conditions - {target.name}'.center(78)}|n")
        output.append(footer(78, char="="))
        
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
                # Short summary instead of full description
                short_desc = self._short_description(condition.description)
                if short_desc:
                    output.append(f"  |x{short_desc}|n")
                if condition.duration:
                    output.append(f"  |cDuration:|n {condition.duration}")
                if condition.resolution_method:
                    output.append(f"  |cResolution:|n {condition.resolution_method}")
                output.append("")
            output.append("|cUse |w+condition/view <name>|c for full description of any condition.|n")
            output.append("")
                
        output.append(footer(78, char="="))
        self.caller.msg("\n".join(output))
    
    def cond_list_all(self):
        """List all available conditions with name, short summary, and resolution."""
        output = []
        output.append(footer(78, char="="))
        _, text_color, _ = get_theme_colors()
        output.append(f"|{text_color}{'Available Conditions'.center(78)}|n")
        output.append(footer(78, char="="))
        output.append("")
        output.append("|cUse |w+condition/view <name>|c for full description.|n")
        output.append("")
        
        # Get all conditions sorted by name
        condition_keys = sorted(STANDARD_CONDITIONS.keys())
        
        for key in condition_keys:
            condition = STANDARD_CONDITIONS[key]
            # Condition name
            output.append(f"|w{condition.name}|n")
            # Short explanation
            short_desc = self._short_description(condition.description)
            if short_desc:
                output.append(f"  |x{short_desc}|n")
            # Resolution statement
            if condition.resolution_method:
                output.append(f"  |cResolution:|n {condition.resolution_method}")
            output.append("")
        
        output.append(footer(78, char="="))
        self.caller.msg("\n".join(output))

    def _find_condition_key(self, name):
        """Find condition key by case-insensitive match (supports key or display name)."""
        name_clean = name.strip().lower()
        name_with_underscores = name_clean.replace(" ", "_")
        for key in STANDARD_CONDITIONS:
            if key.lower() == name_clean or key.lower() == name_with_underscores:
                return key
            if STANDARD_CONDITIONS[key].name.lower() == name_clean:
                return key
        return None

    def cond_view(self):
        """View full details of a specific condition."""
        if not self.args:
            self.caller.msg("Usage: +condition/view <condition_name>")
            return

        condition_key = self._find_condition_key(self.args.strip())
        if condition_key is None:
            self.caller.msg(f"|rUnknown condition: |w{self.args.strip()}|n")
            self.caller.msg("Use |w+condition/list|n to see all available conditions.")
            return

        condition = STANDARD_CONDITIONS[condition_key]

        # Build formatted output
        output = []
        output.append(footer(78, char="="))
        _, text_color, _ = get_theme_colors()
        output.append(f"|{text_color}{condition.name.center(78)}|n")
        output.append(footer(78, char="="))
        
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
                
        output.append(footer(78, char="="))
        self.caller.msg("\n".join(output)) 