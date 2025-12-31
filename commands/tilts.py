from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.tilts import Tilt, STANDARD_TILTS
from utils.search_helpers import search_character

class CmdTilt(MuxCommand):
    """
    Manage tilts on characters and environments during combat.
    
    Usage:
        +tilt - Show your current tilts
        +tilt <character> - View another character's tilts (staff only)
        +tilt/add <tilt_name> - Add tilt to yourself
        +tilt/add <character> = <tilt_name> - Add tilt to character (staff only)
        +tilt/remove <tilt_name> - Remove tilt from yourself
        +tilt/remove <character> = <tilt_name> - Remove tilt from character (staff only)
        +tilt/list - Show all available tilts in the system
        +tilt/help <tilt_name> - Show detailed information about a tilt
        +tilt/env/add <tilt_name> - Add environmental tilt (staff only)
        +tilt/env/remove <tilt_name> - Remove environmental tilt (staff only)
        +tilt/env/list - List environmental tilts
        +tilt/advance - Advance all tilts by one turn (staff/combat)
        +tilt/clear <character> - Clear all tilts (staff only)
        +tilt/env/clear - Clear all environmental tilts (staff only)
        
    Examples:
        +tilt - View your tilts
        +tilt John - Staff: view John's tilts
        +tilt/add blinded - Add blinded tilt to yourself
        +tilt/remove knocked_down - Remove knocked down from yourself
        +tilt/add John = stunned - Staff: add stunned to John
        +tilt/list - See all tilts available
        +tilt/help blinded - See details about the blinded tilt
        +tilt/env/add darkness - Staff: add darkness to location
        +tilt/advance - Advance tilts by one turn
    """
    key = "+tilt"
    aliases = ["+tilts"]
    locks = "cmd:all()"
    help_category = "Automated Combat System"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()
    
    def _normalize_tilt_name(self, name):
        """Normalize a tilt name by replacing spaces with underscores and lowercasing"""
        return name.strip().lower().replace(" ", "_")
    
    def func(self):
        """
        This is the main command function that handles the switches.
        """
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        if is_legacy_mode():
            self.caller.msg("|rTilts system is disabled in Legacy Mode.|n")
            self.caller.msg("Legacy Mode uses traditional World of Darkness mechanics without tilts.")
            return
        
        # No switches - show current tilts
        if not self.switches:
            self.tilt_show()
            return
            
        # Handle environmental tilts
        if "env" in self.switches:
            self.handle_environmental()
            return
            
        # Handle other switches
        switch = self.switches[0].lower()
        if switch == "add":
            self.tilt_add()
        elif switch == "remove":
            self.tilt_remove()
        elif switch == "list":
            self.tilt_list_all()
        elif switch == "help":
            self.tilt_help()
        elif switch == "advance":
            self.tilt_advance()
        elif switch == "clear":
            self.tilt_clear()
        else:
            self.caller.msg("Invalid switch. Use: add, remove, list, help, env, advance, or clear")
    
    def handle_environmental(self):
        """Handle environmental tilt commands"""
        if len(self.switches) < 2:
            self.caller.msg("Usage: +tilt/env/add, +tilt/env/remove, +tilt/env/list, or +tilt/env/clear")
            return
            
        env_switch = self.switches[1].lower()
        if env_switch == "add":
            self.env_add()
        elif env_switch == "remove":
            self.env_remove()
        elif env_switch == "list":
            self.env_list()
        elif env_switch == "clear":
            self.env_clear()
        else:
            self.caller.msg("Invalid environmental switch. Use: add, remove, list, or clear")
    
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
        """Check if caller has permission to modify target's tilts"""
        if target == self.caller:
            return True
        return self.caller.check_permstring("Admin")
    
    def _check_combat_permission(self):
        """Check if caller can advance tilts (in combat or staff)"""
        if self.caller.check_permstring("Admin"):
            return True
        # Check if caller is in combat
        if hasattr(self.caller.location, 'combat_tracker'):
            return self.caller in self.caller.location.combat_tracker.participants
        return False
    
    def tilt_add(self):
        """Add a tilt to a character"""
        if not self.args:
            self.caller.msg("Usage: +tilt/add <tilt_name> or +tilt/add <character> = <tilt_name>")
            return
        
        # Check if there's an equals sign (targeting another character)
        if "=" in self.args:
            parts = self.args.split("=", 1)
            target_name = parts[0].strip()
            tilt_name = parts[1].strip()
            
            # Find the target
            target = search_character(self.caller, target_name)
            if not target:
                return
                
            # Check permissions - only staff can target others
            if not self._check_permission(target):
                self.caller.msg("|rYou can only add tilts to yourself. Staff can add tilts to others.|n")
                return
        else:
            # No equals sign - default to self
            target = self.caller
            tilt_name = self.args.strip()
            
        # Check if tilt exists
        tilt_name = self._normalize_tilt_name(tilt_name)
        if tilt_name not in STANDARD_TILTS:
            self.caller.msg(f"|rUnknown tilt: |w{tilt_name}|n")
            self.caller.msg("Use |w+tilt/list|n to see all available tilts.")
            return
            
        # Check if it's a personal tilt
        tilt_template = STANDARD_TILTS[tilt_name]
        if tilt_template.tilt_type != "personal":
            self.caller.msg(f"|r'{tilt_name}' is an environmental tilt. Use |w+tilt/env/add {tilt_name}|r instead.|n")
            return
            
        # Create a new instance of the tilt
        tilt = Tilt(
            name=tilt_template.name,
            description=tilt_template.description,
            tilt_type=tilt_template.tilt_type,
            duration=tilt_template.duration,
            effects=tilt_template.effects,
            resolution_method=tilt_template.resolution_method,
            condition_equivalent=tilt_template.condition_equivalent
        )
        
        # Add the tilt
        target.tilts.add(tilt)
        
        if target == self.caller:
            self.caller.msg(f"|gAdded tilt |w{tilt.name}|g to yourself.|n")
        else:
            self.caller.msg(f"|gAdded tilt |w{tilt.name}|g to |w{target.name}|g.|n")

    def tilt_remove(self):
        """Remove a tilt from a character"""
        if not self.args:
            self.caller.msg("Usage: +tilt/remove <tilt_name> or +tilt/remove <character> = <tilt_name>")
            return
        
        # Check if there's an equals sign (targeting another character)
        if "=" in self.args:
            parts = self.args.split("=", 1)
            target_name = parts[0].strip()
            tilt_name = parts[1].strip()
            
            # Find the target
            target = search_character(self.caller, target_name)
            if not target:
                return
                
            # Check permissions - only staff can target others
            if not self._check_permission(target):
                self.caller.msg("|rYou can only remove tilts from yourself. Staff can remove tilts from others.|n")
                return
        else:
            # No equals sign - default to self
            target = self.caller
            tilt_name = self.args.strip()
            
        # Remove the tilt
        tilt_name = self._normalize_tilt_name(tilt_name)
        if target.tilts.remove(tilt_name):
            if target == self.caller:
                self.caller.msg(f"|gRemoved tilt |w{tilt_name}|g from yourself.|n")
            else:
                self.caller.msg(f"|gRemoved tilt |w{tilt_name}|g from |w{target.name}|g.|n")
        else:
            if target == self.caller:
                self.caller.msg(f"|rYou do not have the tilt |w{tilt_name}|r.|n")
            else:
                self.caller.msg(f"|r{target.name} does not have the tilt |w{tilt_name}|r.|n")

    def tilt_show(self):
        """Show current tilts on a character"""
        if not self.args:
            target = self.caller
        else:
            # Check permission if viewing someone else
            if not self.caller.check_permstring("Admin"):
                self.caller.msg("|rYou can only view your own tilts. Staff can view others' tilts.|n")
                return
            
            target = search_character(self.caller, self.args)
            if not target:
                return
                
        tilts = target.tilts.all()
        
        # Build formatted output
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{f'Tilts - {target.name}'.center(78)}|n")
        output.append(f"|y{'='*78}|n")
        
        if not tilts:
            output.append("")
            if target == self.caller:
                output.append("|cYou have no active tilts.|n".center(78))
            else:
                output.append(f"|c{target.name} has no active tilts.|n".center(78))
            output.append("")
        else:
            output.append("")
            for tilt in tilts:
                # Tilt name in white
                output.append(f"|w{tilt.name.upper()}|n")
                # Description
                output.append(f"  {tilt.description}")
                
                # Additional details
                details = []
                if tilt.turns_remaining is not None:
                    details.append(f"|cTurns Remaining:|n {tilt.turns_remaining}")
                elif tilt.duration:
                    details.append(f"|cDuration:|n {tilt.duration} turns")
                if tilt.resolution_method:
                    details.append(f"|cResolution:|n {tilt.resolution_method}")
                
                if details:
                    for detail in details:
                        output.append(f"  {detail}")
                output.append("")
                
        output.append(f"|y{'='*78}|n")
        self.caller.msg("\n".join(output))

    def tilt_list_all(self):
        """List all available tilts in the system in 3 columns"""
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{'Available Tilts'.center(78)}|n")
        output.append(f"|y{'='*78}|n")
        output.append("")
        output.append("|cUse |w+tilt/help <name>|c to see details about a specific tilt.|n")
        output.append("")
        
        # Personal Tilts section
        output.append(self._format_section_header("|wPERSONAL TILTS|n"))
        personal_tilts = sorted([name for name, tilt in STANDARD_TILTS.items() if tilt.tilt_type == "personal"])
        
        # Format in 3 columns
        col_width = 24
        num_cols = 3
        
        if personal_tilts:
            # Split into rows
            rows = []
            for i in range(0, len(personal_tilts), num_cols):
                row = personal_tilts[i:i+num_cols]
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
        else:
            output.append("|x(none)|n")
        
        output.append("")
        
        # Environmental Tilts section
        output.append(self._format_section_header("|wENVIRONMENTAL TILTS|n"))
        environmental_tilts = sorted([name for name, tilt in STANDARD_TILTS.items() if tilt.tilt_type == "environmental"])
        
        if environmental_tilts:
            # Split into rows
            rows = []
            for i in range(0, len(environmental_tilts), num_cols):
                row = environmental_tilts[i:i+num_cols]
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
        else:
            output.append("|x(none)|n")
        
        output.append("")
        output.append(f"|y{'='*78}|n")
        self.caller.msg("\n".join(output))
        
    def tilt_help(self):
        """Get information about a specific tilt"""
        if not self.args:
            self.caller.msg("Usage: +tilt/help <tilt_name>")
            return
            
        tilt_name = self._normalize_tilt_name(self.args)
        if tilt_name not in STANDARD_TILTS:
            self.caller.msg(f"|rUnknown tilt: |w{tilt_name}|n")
            self.caller.msg("Use |w+tilt/list|n to see all available tilts.")
            return
            
        tilt = STANDARD_TILTS[tilt_name]
        
        # Build formatted output
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{tilt.name.center(78)}|n")
        output.append(f"|y{'='*78}|n")
        
        # Type
        output.append(self._format_section_header("|wTYPE|n"))
        tilt_type_display = "|cPersonal|n" if tilt.tilt_type == "personal" else "|yEnvironmental|n"
        output.append(f"{tilt_type_display}")
        output.append("")
        
        # Description
        output.append(self._format_section_header("|wDESCRIPTION|n"))
        output.append(f"{tilt.description}")
        output.append("")
        
        # Duration
        output.append(self._format_section_header("|wDURATION|n"))
        if tilt.duration:
            output.append(f"{tilt.duration} turns")
        else:
            output.append("Until resolved")
        output.append("")
        
        # Resolution
        if tilt.resolution_method:
            output.append(self._format_section_header("|wRESOLUTION|n"))
            output.append(f"{tilt.resolution_method}")
            output.append("")
        
        # Effects
        if tilt.effects:
            output.append(self._format_section_header("|wEFFECTS|n"))
            output.append(f"{tilt.effects}")
            output.append("")
        
        # Condition Equivalent
        if tilt.condition_equivalent:
            output.append(self._format_section_header("|wCONDITION EQUIVALENT|n"))
            output.append(f"Becomes |w{tilt.condition_equivalent}|n condition when out of combat")
            output.append("")
                
        output.append(f"|y{'='*78}|n")
        self.caller.msg("\n".join(output))
    
    def tilt_advance(self):
        """Advance all tilts by one turn"""
        if not self._check_combat_permission():
            self.caller.msg("Only staff or combat participants can advance tilts.")
            return
            
        # Advance personal tilts for all characters in location
        expired_personal = []
        for obj in self.caller.location.contents:
            if hasattr(obj, 'tilts'):
                expired = obj.tilts.advance_turn()
                if expired:
                    expired_personal.extend([(obj, tilt) for tilt in expired])
        
        # Advance environmental tilts
        expired_environmental = []
        if hasattr(self.caller.location, 'environmental_tilts'):
            expired_environmental = self.caller.location.environmental_tilts.advance_turn()
        
        # Report results
        output = ["Advanced all tilts by one turn."]
        
        if expired_personal:
            output.append("\nExpired personal tilts:")
            for obj, tilt_name in expired_personal:
                output.append(f"  {obj.name}: {tilt_name}")
                
        if expired_environmental:
            output.append("\nExpired environmental tilts:")
            for tilt_name in expired_environmental:
                output.append(f"  {tilt_name}")
                
        if not expired_personal and not expired_environmental:
            output.append("No tilts expired this turn.")
            
        self.caller.msg("\n".join(output))
    
    def tilt_clear(self):
        """Clear all tilts from a character (staff only)"""
        if not self.caller.check_permstring("Admin"):
            self.caller.msg("|rOnly staff can clear all tilts.|n")
            return
            
        if not self.args:
            self.caller.msg("Usage: +tilt/clear <character>")
            return
        
        target = search_character(self.caller, self.args)
        if not target:
            return
                
        target.tilts.clear_all()
        self.caller.msg(f"|gCleared all tilts from {target.name}.|n")
    
    def env_add(self):
        """Add an environmental tilt"""
        if not self.caller.check_permstring("Admin"):
            self.caller.msg("|rOnly staff can add environmental tilts.|n")
            return
            
        if not self.args:
            self.caller.msg("Usage: +tilt/env/add <tilt_name>")
            return
            
        tilt_name = self._normalize_tilt_name(self.args)
        if tilt_name not in STANDARD_TILTS:
            self.caller.msg(f"|rUnknown tilt: |w{tilt_name}|n")
            self.caller.msg("Use |w+tilt/list|n to see all available tilts.")
            return
            
        # Check if it's an environmental tilt
        tilt_template = STANDARD_TILTS[tilt_name]
        if tilt_template.tilt_type != "environmental":
            self.caller.msg(f"|r'{tilt_name}' is a personal tilt. Use |w+tilt/add {tilt_name}|r instead.|n")
            return
            
        # Create environmental tilt handler if needed
        if not hasattr(self.caller.location, 'environmental_tilts'):
            from world.tilts import EnvironmentalTiltHandler
            self.caller.location.environmental_tilts = EnvironmentalTiltHandler(self.caller.location)
        
        # Create a new instance of the tilt
        tilt = Tilt(
            name=tilt_template.name,
            description=tilt_template.description,
            tilt_type=tilt_template.tilt_type,
            duration=tilt_template.duration,
            effects=tilt_template.effects,
            resolution_method=tilt_template.resolution_method,
            condition_equivalent=tilt_template.condition_equivalent
        )
        
        # Add the environmental tilt
        self.caller.location.environmental_tilts.add(tilt)
        self.caller.msg(f"|gAdded environmental tilt |w{tilt.name}|g to this location.|n")
    
    def env_remove(self):
        """Remove an environmental tilt"""
        if not self.caller.check_permstring("Admin"):
            self.caller.msg("|rOnly staff can remove environmental tilts.|n")
            return
            
        if not self.args:
            self.caller.msg("Usage: +tilt/env/remove <tilt_name>")
            return
            
        if not hasattr(self.caller.location, 'environmental_tilts'):
            self.caller.msg("|cNo environmental tilts in this location.|n")
            return
            
        tilt_name = self._normalize_tilt_name(self.args)
        if self.caller.location.environmental_tilts.remove(tilt_name):
            self.caller.msg(f"|gRemoved environmental tilt |w{tilt_name}|g from this location.|n")
        else:
            self.caller.msg(f"|rThis location does not have the environmental tilt |w{tilt_name}|r.|n")
    
    def env_list(self):
        """List all environmental tilts in the current location"""
        if not hasattr(self.caller.location, 'environmental_tilts'):
            self.caller.msg("|cNo environmental tilts in this location.|n")
            return
            
        tilts = self.caller.location.environmental_tilts.all()
        if not tilts:
            self.caller.msg("|cNo environmental tilts in this location.|n")
            return
            
        # Format the output
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{'Environmental Tilts'.center(78)}|n")
        output.append(f"|y{'='*78}|n")
        output.append("")
        
        for tilt in tilts:
            # Tilt name in white
            output.append(f"|w{tilt.name.upper()}|n")
            # Description
            output.append(f"  {tilt.description}")
            
            # Additional details
            details = []
            if tilt.turns_remaining is not None:
                details.append(f"|cTurns Remaining:|n {tilt.turns_remaining}")
            elif tilt.duration:
                details.append(f"|cDuration:|n {tilt.duration} turns")
            if tilt.resolution_method:
                details.append(f"|cResolution:|n {tilt.resolution_method}")
            
            if details:
                for detail in details:
                    output.append(f"  {detail}")
            output.append("")
        
        output.append(f"|y{'='*78}|n")
        self.caller.msg("\n".join(output))
    
    def env_clear(self):
        """Clear all environmental tilts (staff only)"""
        if not self.caller.check_permstring("Admin"):
            self.caller.msg("|rOnly staff can clear all environmental tilts.|n")
            return
            
        if not hasattr(self.caller.location, 'environmental_tilts'):
            self.caller.msg("|cNo environmental tilts in this location.|n")
            return
            
        self.caller.location.environmental_tilts.clear_all()
        self.caller.msg("|gCleared all environmental tilts from this location.|n") 