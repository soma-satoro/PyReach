from evennia.commands.default.muxcommand import MuxCommand
from world.experience import ExperienceHandler

class CmdAspiration(MuxCommand):
    """
    Manage your character's aspirations.
    
    Usage:
        +aspiration/list - List your current aspirations
        +aspiration/add <short|long> <description> - Add an aspiration
        +aspiration/change <number> <new description> - Change an existing aspiration
        +aspiration/remove <number> - Remove an aspiration
        +aspiration/fulfill <number> - Mark an aspiration as fulfilled and gain a beat
        
    Aspirations are character goals that drive story and generate beats when fulfilled.
    You can have up to 6 aspirations at a time (any combination of short-term and long-term).
    
    Short-term aspirations are immediate goals that can be fulfilled in 1-3 scenes.
    Long-term aspirations are major goals that take multiple sessions to achieve.
    Both provide the same number of beats when fulfilled (1 beat).
    
    Examples:
        +aspiration/add short Learn about the vampire who sired my friend
        +aspiration/add long Become the primogen of my clan
        +aspiration/change 2 Destroy the vampire who sired my friend
        +aspiration/fulfill 1
        +aspiration/remove 3
    """
    key = "+aspiration"
    aliases = ["+asp"]
    help_category = "Chargen & Character Info"
    
    def func(self):
        """Execute the command"""
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        if is_legacy_mode():
            self.caller.msg("|rAspiration system is disabled in Legacy Mode.|n")
            self.caller.msg("Legacy Mode uses only Virtue and Vice for character motivation.")
            return
        
        if not self.switches:
            self.caller.msg("Usage: +aspiration/list, +aspiration/add, +aspiration/change, +aspiration/remove, or +aspiration/fulfill")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_aspirations()
        elif switch == "add":
            self.add_aspiration()
        elif switch == "change":
            self.change_aspiration()
        elif switch == "remove":
            self.remove_aspiration()
        elif switch == "fulfill":
            self.fulfill_aspiration()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def list_aspirations(self):
        """List current aspirations with styled output"""
        # Initialize aspirations if not exists
        if not hasattr(self.caller.db, 'aspirations') or self.caller.db.aspirations is None:
            self.caller.db.aspirations = []
        
        # Clean up and validate aspirations (only reassign if we actually filtered something)
        if self.caller.db.aspirations:
            original_count = len(self.caller.db.aspirations)
            valid_aspirations = []
            for asp in self.caller.db.aspirations:
                # Use duck typing instead of isinstance - Evennia uses _SaverDict which isn't a regular dict
                # Check if it's dict-like by trying to access keys
                try:
                    if "type" in asp and "description" in asp:
                        # Valid new format (works for both dict and _SaverDict)
                        valid_aspirations.append(asp)
                    elif isinstance(asp, str) and asp:
                        # Old format string - convert to new format
                        valid_aspirations.append({
                            "type": "short-term",
                            "description": asp
                        })
                except (TypeError, AttributeError):
                    # Not dict-like, skip it
                    pass
            
            # Only reassign if we actually changed something (to avoid unnecessary writes)
            if len(valid_aspirations) != original_count:
                self.caller.attributes.add("aspirations", valid_aspirations)
        
        aspirations = self.caller.db.aspirations
        
        if not aspirations or len(aspirations) == 0:
            self.caller.msg("You have no aspirations set.")
            return
        
        # Build styled output matching +sheet format
        output = []
        output.append("|y" + "=" * 78 + "|n")
        output.append("|y" + "ASPIRATIONS".center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        # Separate short-term and long-term (works with both dict and _SaverDict)
        short_term = []
        long_term = []
        for asp in aspirations:
            if asp:
                try:
                    if asp.get("type") == "short-term":
                        short_term.append(asp)
                    elif asp.get("type") == "long-term":
                        long_term.append(asp)
                except (AttributeError, TypeError):
                    # Not dict-like, skip
                    pass
        
        # Short-term aspirations section
        output.append(self._format_section_header("|wSHORT-TERM ASPIRATIONS|n"))
        if short_term:
            for i, asp in enumerate(short_term, 1):
                # Find the actual index in the full list
                actual_index = aspirations.index(asp) + 1
                output.append(f"|c{actual_index}.|n {asp['description']}")
        else:
            output.append("|x(none)|n")
        output.append("")
        
        # Long-term aspirations section
        output.append(self._format_section_header("|wLONG-TERM ASPIRATIONS|n"))
        if long_term:
            for i, asp in enumerate(long_term, 1):
                # Find the actual index in the full list
                actual_index = aspirations.index(asp) + 1
                output.append(f"|c{actual_index}.|n {asp['description']}")
        else:
            output.append("|x(none)|n")
        output.append("")
        
        # Footer with count
        total_count = len(aspirations)
        output.append(f"|gTotal: {total_count}/6 aspirations|n")
        output.append("|y" + "=" * 78 + "|n")
        
        self.caller.msg("\n".join(output))
    
    def _format_section_header(self, section_name):
        """Format a section header matching +sheet style"""
        total_width = 78
        # Remove ANSI codes for length calculation
        import re
        clean_name = re.sub(r'\|[a-zA-Z]', '', section_name)
        name_length = len(clean_name)
        available_dash_space = total_width - name_length - 4
        left_dashes = available_dash_space // 2
        right_dashes = available_dash_space - left_dashes
        return f"|g<{'-' * left_dashes}|n {section_name} |g{'-' * right_dashes}>|n"
    
    def add_aspiration(self):
        """Add a new aspiration"""
        try:
            asp_type, description = self.args.split(" ", 1)
            asp_type = asp_type.lower()
        except ValueError:
            self.caller.msg("Usage: +aspiration/add <short|long> <description>")
            self.caller.msg("Example: +aspiration/add short Find the missing artifact")
            return
        
        # Validate type
        if asp_type not in ["short", "long", "short-term", "long-term"]:
            self.caller.msg("Aspiration type must be 'short' or 'long'")
            self.caller.msg("Example: +aspiration/add short Find the missing artifact")
            return
        
        # Normalize type
        if asp_type == "short":
            asp_type = "short-term"
        elif asp_type == "long":
            asp_type = "long-term"
        
        # Initialize aspirations if not exists
        if not hasattr(self.caller.db, 'aspirations') or self.caller.db.aspirations is None:
            self.caller.db.aspirations = []
        
        # Count only valid aspirations (works with both dict and _SaverDict)
        valid_count = 0
        for asp in self.caller.db.aspirations:
            try:
                if "type" in asp:
                    valid_count += 1
            except (TypeError, AttributeError):
                pass
        
        # Check if at max (6 aspirations)
        if valid_count >= 6:
            self.caller.msg("|rYou already have 6 aspirations (the maximum).|n")
            self.caller.msg("Remove or fulfill an aspiration before adding a new one.")
            return
        
        # Add the new aspiration
        new_aspiration = {
            "type": asp_type,
            "description": description
        }
        
        # Important: Create a new list to trigger Evennia's persistence
        # Modifying a list in place doesn't always save properly
        aspirations_list = list(self.caller.db.aspirations)
        aspirations_list.append(new_aspiration)
        
        # Use attributes.add() to ensure it saves properly
        self.caller.attributes.add("aspirations", aspirations_list)
        
        # Count from the list we just created (not from db which might not be updated yet)
        number = len(aspirations_list)
        type_display = "Short-term" if asp_type == "short-term" else "Long-term"
        self.caller.msg(f"|gAdded {type_display} aspiration #{number}:|n {description}")
    
    def change_aspiration(self):
        """Change an existing aspiration's description"""
        try:
            number, new_description = self.args.split(" ", 1)
            number = int(number)
        except ValueError:
            self.caller.msg("Usage: +aspiration/change <number> <new description>")
            self.caller.msg("Example: +aspiration/change 2 Destroy the vampire nest")
            return
        
        # Initialize aspirations if not exists
        if not hasattr(self.caller.db, 'aspirations') or not self.caller.db.aspirations:
            self.caller.msg("You don't have any aspirations set yet.")
            return
        
        if not 1 <= number <= len(self.caller.db.aspirations):
            self.caller.msg(f"Invalid aspiration number. You have {len(self.caller.db.aspirations)} aspirations.")
            return
        
        # Update the description (create new list to trigger Evennia persistence)
        aspirations_list = list(self.caller.db.aspirations)
        old_description = aspirations_list[number-1]["description"]
        aspirations_list[number-1]["description"] = new_description
        self.caller.attributes.add("aspirations", aspirations_list)
        
        asp_type = self.caller.db.aspirations[number-1]["type"]
        type_display = "Short-term" if asp_type == "short-term" else "Long-term"
        
        self.caller.msg(f"|gChanged {type_display} aspiration #{number}:|n")
        self.caller.msg(f"|xOld:|n {old_description}")
        self.caller.msg(f"|cNew:|n {new_description}")
    
    def remove_aspiration(self):
        """Remove an aspiration"""
        try:
            number = int(self.args)
        except ValueError:
            self.caller.msg("Usage: +aspiration/remove <number>")
            return
        
        # Initialize aspirations if not exists
        if not hasattr(self.caller.db, 'aspirations') or not self.caller.db.aspirations:
            self.caller.msg("You don't have any aspirations set yet.")
            return
        
        if not 1 <= number <= len(self.caller.db.aspirations):
            self.caller.msg(f"Invalid aspiration number. You have {len(self.caller.db.aspirations)} aspirations.")
            return
        
        # Remove the aspiration (create new list to trigger Evennia persistence)
        aspirations_list = list(self.caller.db.aspirations)
        removed_asp = aspirations_list.pop(number-1)
        self.caller.attributes.add("aspirations", aspirations_list)
        
        type_display = "Short-term" if removed_asp["type"] == "short-term" else "Long-term"
        self.caller.msg(f"|gRemoved {type_display} aspiration:|n {removed_asp['description']}")
    
    def fulfill_aspiration(self):
        """Mark an aspiration as fulfilled and gain a beat"""
        try:
            number = int(self.args)
        except ValueError:
            self.caller.msg("Usage: +aspiration/fulfill <number>")
            return
        
        # Initialize aspirations if not exists
        if not hasattr(self.caller.db, 'aspirations') or not self.caller.db.aspirations:
            self.caller.msg("You don't have any aspirations set yet.")
            return
        
        if not 1 <= number <= len(self.caller.db.aspirations):
            self.caller.msg(f"Invalid aspiration number. You have {len(self.caller.db.aspirations)} aspirations.")
            return
        
        # Get the aspiration before removing it (create new list to trigger Evennia persistence)
        aspirations_list = list(self.caller.db.aspirations)
        fulfilled_asp = aspirations_list.pop(number-1)
        self.caller.attributes.add("aspirations", aspirations_list)
        
        type_display = "Short-term" if fulfilled_asp["type"] == "short-term" else "Long-term"
        description = fulfilled_asp["description"]
        
        # Add a beat
        if not hasattr(self.caller, 'experience'):
            self.caller.experience = ExperienceHandler(self.caller)
        self.caller.experience.add_beat(1)
        
        self.caller.msg("|y" + "=" * 78 + "|n")
        self.caller.msg("|yASPIRATION FULFILLED!|n".center(78))
        self.caller.msg("|y" + "=" * 78 + "|n")
        self.caller.msg(f"|g{type_display} aspiration:|n {description}")
        self.caller.msg("")
        self.caller.msg("|c+1 Beat|n for fulfilling an aspiration!")
        self.caller.msg("|y" + "=" * 78 + "|n") 