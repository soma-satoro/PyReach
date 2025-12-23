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
        # Initialize aspirations if not exists (migrate from old format)
        if not hasattr(self.caller.db, 'aspirations') or self.caller.db.aspirations is None:
            self.caller.db.aspirations = []
        
        # Migrate old format (list of strings/None) to new format (list of dicts)
        if self.caller.db.aspirations and len(self.caller.db.aspirations) > 0:
            # Check if migration is needed (contains non-dict items)
            needs_migration = any(item is not None and not isinstance(item, dict) for item in self.caller.db.aspirations)
            
            if needs_migration:
                old_aspirations = self.caller.db.aspirations
                self.caller.db.aspirations = []
                for asp in old_aspirations:
                    if isinstance(asp, dict):
                        # Already in new format, keep it
                        self.caller.db.aspirations.append(asp)
                    elif asp and isinstance(asp, str):
                        # Old format string, migrate to new format
                        self.caller.db.aspirations.append({
                            "type": "short-term",
                            "description": asp
                        })
                    # Skip None values from old format
        
        # Filter out any remaining None values that might have snuck in
        if self.caller.db.aspirations:
            self.caller.db.aspirations = [asp for asp in self.caller.db.aspirations if asp is not None]
        
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
        
        # Separate short-term and long-term (filter out any None values as safety check)
        short_term = [asp for asp in aspirations if asp and asp.get("type") == "short-term"]
        long_term = [asp for asp in aspirations if asp and asp.get("type") == "long-term"]
        
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
        
        # Initialize aspirations if not exists or is empty/contains only None
        if not hasattr(self.caller.db, 'aspirations') or self.caller.db.aspirations is None:
            self.caller.db.aspirations = []
        
        # Clean out any None values from old format
        if self.caller.db.aspirations:
            self.caller.db.aspirations = [asp for asp in self.caller.db.aspirations if asp is not None and (isinstance(asp, dict) or isinstance(asp, str))]
        
        # Check if at max (6 aspirations)
        if len(self.caller.db.aspirations) >= 6:
            self.caller.msg("|rYou already have 6 aspirations (the maximum).|n")
            self.caller.msg("Remove or fulfill an aspiration before adding a new one.")
            return
        
        # Add the new aspiration
        new_aspiration = {
            "type": asp_type,
            "description": description
        }
        self.caller.db.aspirations.append(new_aspiration)
        
        number = len(self.caller.db.aspirations)
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
        
        # Update the description
        old_description = self.caller.db.aspirations[number-1]["description"]
        self.caller.db.aspirations[number-1]["description"] = new_description
        
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
        
        # Remove the aspiration
        removed_asp = self.caller.db.aspirations.pop(number-1)
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
        
        # Get the aspiration before removing it
        fulfilled_asp = self.caller.db.aspirations.pop(number-1)
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