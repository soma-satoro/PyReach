from evennia.utils import logger
from evennia.commands.default.general import CmdLook
from evennia.utils.search import search_object
from utils.search_helpers import search_character
import evennia
from evennia.server.models import ServerConfig
from typeclasses.characters import Character
from evennia.commands.command import Command
from evennia.utils import search
from evennia.commands.default.muxcommand import MuxCommand
from evennia.locks import lockfuncs
from evennia.utils.utils import inherits_from
from datetime import datetime
from django.utils import timezone
from evennia import default_cmds
from evennia.utils.search import search_object
from evennia.utils import evtable
from evennia.utils.utils import crop
from evennia.objects.models import ObjectDB
from world.groups.utils import (
    auto_assign_character_groups, 
    get_character_groups, 
    remove_character_from_group
)

# Import roster models if they exist, otherwise skip roster functionality
try:
    from world.cofd.models import Roster, RosterMember
    ROSTER_AVAILABLE = True
except ImportError:
    ROSTER_AVAILABLE = False

class CmdApprove(MuxCommand):
    """
    Approve a player's character.

    Usage:
      approve <character_name>

    This command approves a player's character, removing the 'unapproved' tag
    and adding the 'approved' tag. This allows the player to start playing.
    The character will also be automatically added to the appropriate roster
    based on their sphere/type.
    """
    key = "approve"
    aliases = ["+approve"]
    locks = "cmd:perm(Admin)"
    help_category = "Admin Commands"

    def func(self):
        if not self.args:
            self.caller.msg("Usage: +approve <character>")
            return
            
        # Use our new search helper
        target = search_character(self.caller, self.args)
        if not target:
            return

        # Check both tag and attribute for approval status
        is_approved = target.tags.has("approved", category="approval") and target.db.approved
        if is_approved:
            self.caller.msg(f"{target.name} is already approved.")
            return

        # Set both the tag and the attribute
        target.db.approved = True
        target.tags.remove("unapproved", category="approval")
        target.tags.add("approved", category="approval")
        
        # Determine character's sphere based on their template
        sphere = 'Other'  # Default sphere with consistent capitalization
        if hasattr(target, 'db') and hasattr(target.db, 'stats'):
            stats = target.db.stats
            if stats and 'other' in stats:
                template = stats['other'].get('template', '')
                if template:
                    # Capitalize first letter for consistency
                    sphere = template.capitalize()

        # Try to find a roster matching the sphere (case-insensitive)
        # Note: This is for the optional Django model-based roster system
        if ROSTER_AVAILABLE:
            try:
                roster = Roster.objects.filter(sphere__iexact=sphere).first()
                if roster:
                    # Add character to roster
                    if not RosterMember.objects.filter(roster=roster, character=target).exists():
                        RosterMember.objects.create(
                            roster=roster,
                            character=target,
                            approved=True,
                            approved_by=self.caller.account,
                            approved_date=timezone.now()
                        )
                        self.caller.msg(f"Added {target.name} to the {roster.name} sphere roster.")
            except Exception as e:
                self.caller.msg(f"Error adding to sphere roster: {str(e)}")
        
        # Automatically assign character to appropriate groups
        try:
            assigned_groups = auto_assign_character_groups(target)
            if assigned_groups:
                self.caller.msg(f"Auto-assigned {target.name} to groups: {', '.join(assigned_groups)}")
                target.msg(f"You have been automatically assigned to the following groups: {', '.join(assigned_groups)}")
            else:
                self.caller.msg(f"No automatic group assignments made for {target.name}")
        except Exception as e:
            self.caller.msg(f"Error assigning groups: {str(e)}")
        
        logger.log_info(f"{target.name} has been approved by {self.caller.name}")

        self.caller.msg(f"You have approved {target.name}.")
        target.msg("Your character has been approved. You may now begin playing.")

class CmdUnapprove(MuxCommand):
    """
    Set a character's status to unapproved.

    Usage:
      unapprove <character_name>

    This command removes the 'approved' tag from a character and adds the 'unapproved' tag.
    This effectively reverts the character to an unapproved state, allowing them to use
    chargen commands again. The character will also be removed from any rosters they belong to.
    """
    key = "unapprove"
    aliases = ["+unapprove"]
    locks = "cmd:perm(Admin)"
    help_category = "Admin Commands"

    def func(self):
        if not self.args:
            self.caller.msg("Usage: unapprove <character_name>")
            return

        # Use our new search helper
        target = search_character(self.caller, self.args)
        if not target:
            return

        # Check both tag and attribute for approval status
        is_approved = target.tags.has("approved", category="approval") or target.db.approved
        if not is_approved:
            self.caller.msg(f"{target.name} is already unapproved.")
            return

        # Remove approved status and add unapproved tag
        target.db.approved = False
        target.tags.remove("approved", category="approval")
        target.tags.add("unapproved", category="approval")
        
        # Remove from any rosters
        if ROSTER_AVAILABLE:
            try:
                memberships = RosterMember.objects.filter(character=target)
                if memberships.exists():
                    roster_names = [m.roster.name for m in memberships]
                    memberships.delete()
                    self.caller.msg(f"Removed {target.name} from the following rosters: {', '.join(roster_names)}")
            except Exception as e:
                self.caller.msg(f"Error removing from rosters: {str(e)}")
        
        # Remove from all groups
        try:
            character_groups = get_character_groups(target)
            removed_groups = []
            
            for group in character_groups:
                if remove_character_from_group(target, group):
                    removed_groups.append(group.name)
            
            if removed_groups:
                self.caller.msg(f"Removed {target.name} from the following groups: {', '.join(removed_groups)}")
                target.msg(f"You have been removed from the following groups: {', '.join(removed_groups)}")
            else:
                self.caller.msg(f"{target.name} was not a member of any groups.")
                
        except Exception as e:
            self.caller.msg(f"Error removing from groups: {str(e)}")
        
        logger.log_info(f"{target.name} has been unapproved by {self.caller.name}")

        self.caller.msg(f"You have unapproved {target.name}.")
        target.msg("Your character has been unapproved. You may now use chargen commands again.")

class CmdMassUnapprove(MuxCommand):
    """
    Set all characters (both online and offline) to unapproved status.

    Usage:
      +massunapprove
      +massunapprove/confirm

    This command will list all characters that will be affected when run
    without the /confirm switch. Use /confirm to actually make the changes.
    This command affects ALL characters in the game, both online and offline.
    """

    key = "+massunapprove"
    locks = "cmd:perm(Admin)"
    help_category = "Admin Commands"

    def func(self):
        """Execute command."""
        caller = self.caller
        confirm = "confirm" in self.switches

        # Get all characters using Character typeclass
        all_chars = search_object("", typeclass=Character)
        
        # Filter to only get approved characters
        approved_chars = [char for char in all_chars 
                        if char.db.approved or char.tags.has("approved", category="approval")]
        
        if not approved_chars:
            caller.msg("No approved characters found.")
            return

        if not confirm:
            # Just show what would be affected
            msg = "The following characters would be set to unapproved:\n"
            for char in approved_chars:
                online_status = "online" if char.has_account else "offline"
                msg += f"- {char.name} ({online_status})\n"
            msg += f"\nTotal characters to be affected: {len(approved_chars)}"
            msg += "\nUse +massunapprove/confirm to execute the changes."
            caller.msg(msg)
            return

        # Actually make the changes
        count = 0
        total_groups_removed = 0
        
        for char in approved_chars:
            char.db.approved = False
            char.tags.add("unapproved", category="approval")
            if char.tags.has("approved", category="approval"):
                char.tags.remove("approved", category="approval")
            
            # Remove from groups
            try:
                character_groups = get_character_groups(char)
                for group in character_groups:
                    if remove_character_from_group(char, group):
                        total_groups_removed += 1
                
                if character_groups and char.has_account:  # Only message online characters
                    group_names = [g.name for g in character_groups]
                    char.msg(f"You have been removed from the following groups: {', '.join(group_names)}")
            except Exception as e:
                self.caller.msg(f"Error removing {char.name} from groups: {str(e)}")
            
            if char.has_account:  # Only message online characters
                char.msg("Your character has been set to unapproved status.")
            count += 1
            logger.log_info(f"{char.name} has been mass-unapproved by {caller.name}")

        caller.msg(f"Successfully set {count} character(s) to unapproved status.")
        if total_groups_removed > 0:
            caller.msg(f"Removed characters from a total of {total_groups_removed} group memberships.")

class CmdSummon(MuxCommand):
    """
    Summon a player or object to your location.

    Usage:
      +summon <character>
      +summon/quiet <character>
      +summon/debug <character> - Show additional diagnostic information

    Switches:
      quiet - Don't announce the summoning to the character
      debug - Display debug information about location storage
    """

    key = "+summon"
    locks = "cmd:perm(storyteller)"
    help_category = "Player Storyteller"
    switch_options = ("quiet", "debug")

    def func(self):
        """Implement the command"""
        caller = self.caller
        args = self.args.strip()
        debug_mode = "debug" in self.switches

        if not args:
            caller.msg("Usage: +summon <character>")
            return

        # Use our new search helper
        target = search_character(caller, args)
        if not target:
            return

        # Store their current location for +return
        if inherits_from(target, "evennia.objects.objects.DefaultCharacter"):
            original_location = target.location
            
            # Make sure the location is valid
            if original_location and hasattr(original_location, "id"):
                # Store location directly as object reference to avoid serialization issues
                target.db.pre_summon_location = original_location
                
                # Log the movement on the server
                evennia.logger.log_info(f"Staff Summon: {caller.name} (#{caller.id}) summoned {target.name} (#{target.id}) from {original_location.name} (#{original_location.id}) to {caller.location.name} (#{caller.location.id})")
                
                if debug_mode:
                    caller.msg(f"DEBUG: Stored {original_location.name} (#{original_location.id}) as pre_summon_location for {target.name}")
            else:
                caller.msg(f"Warning: Could not store a valid original location for {target.name}")
                if debug_mode:
                    caller.msg(f"DEBUG: Current location is {original_location}")
            
        # Force synchronization before moving to prevent desync
        target.save()
        
        # Do the teleport
        if target.move_to(
            caller.location,
            quiet="quiet" in self.switches,
            emit_to_obj=caller,
            move_type="teleport",
        ):
            caller.msg(f"You have summoned {target.name} to your location.")
            if "quiet" not in self.switches:
                target.msg(f"{caller.name} has summoned you.")
            
            # Force another save after the move to ensure location is synchronized
            target.save()
            
            # Double-check storage worked
            if debug_mode and hasattr(target, "db"):
                if target.db.pre_summon_location:
                    stored_loc = target.db.pre_summon_location
                    caller.msg(f"DEBUG: Confirmed {target.name} has pre_summon_location: {stored_loc.name} (#{stored_loc.id})")
                else:
                    caller.msg(f"DEBUG: Failed to store pre_summon_location for {target.name}")
        else:
            caller.msg(f"Failed to summon {target.name}.")

class CmdReturn(MuxCommand):
    """
    Return a previously summoned character back to their original location.

    Usage:
      +return <character>
      +return/quiet <character>
      +return/all - Return all summoned characters in current location
      +return/force <character> - Use alternative location attributes if available
      +return/set <character> = <location> - Manually set return location

    Switches:
      quiet - Don't announce the return to the character
      all - Return all summoned characters in current location
      force - Try alternative location attributes (prelogout_location) if available
      set - Manually set a return location for a character
    """

    key = "+return"
    locks = "cmd:perm(storyteller)"
    help_category = "Player Storyteller"
    switch_options = ("quiet", "all", "force", "set")
    rhs_split = ("=",)

    def return_character(self, character, quiet=False, force=False):
        """Return a character to their pre-summon location"""
        # First try the primary location attribute
        if hasattr(character, "db") and character.db.pre_summon_location:
            prev_location = character.db.pre_summon_location
            location_type = "pre-summon"
        # If force is True, try alternative location attributes
        elif force and hasattr(character, "db"):
            # Try prelogout_location as fallback
            if character.db.prelogout_location:
                prev_location = character.db.prelogout_location
                location_type = "prelogout"
            else:
                self.caller.msg(f"{character.name} has no stored locations to return to.")
                return False
        else:
            self.caller.msg(f"{character.name} has no stored previous location to return to.")
            self.caller.msg("Use +return/force to try alternative location attributes, or +return/set to set one manually.")
            return False

        # Verify the location still exists and is valid
        if not (prev_location and hasattr(prev_location, 'id') and 
                hasattr(prev_location, 'name') and
                prev_location.access(character, 'view')):
            self.caller.msg(f"The previous {location_type} location for {character.name} is no longer valid.")
            if location_type == "pre-summon":
                character.attributes.remove("pre_summon_location")
            return False
        
        # Log the movement on the server
        current_location = character.location
        if current_location and hasattr(current_location, "id"):
            evennia.logger.log_info(f"Staff Return: {self.caller.name} (#{self.caller.id}) returned {character.name} (#{character.id}) from {current_location.name} (#{current_location.id}) to {prev_location.name} (#{prev_location.id})")
        
        # Force synchronization before moving to prevent desync
        character.save()
            
        # Move the character back
        if character.move_to(
            prev_location,
            quiet=quiet,
            emit_to_obj=self.caller,
            move_type="teleport",
        ):
            self.caller.msg(f"Returned {character.name} to their {location_type} location: {prev_location.name}.")
            if not quiet:
                character.msg(f"{self.caller.name} has returned you to your previous location.")
                
            # Clear the stored location if it was pre_summon_location
            if location_type == "pre-summon":
                character.attributes.remove("pre_summon_location")
            
            # Force another save after the move to ensure location is synchronized
            character.save()
            return True
        else:
            self.caller.msg(f"Failed to return {character.name}.")
            return False

    def func(self):
        """Implement the command"""
        caller = self.caller
        args = self.args.strip()
        quiet = "quiet" in self.switches
        force = "force" in self.switches

        # Handle setting a return location manually
        if "set" in self.switches:
            if not self.rhs:
                caller.msg("Usage: +return/set <character> = <location>")
                return
                
            # Use our new search helper
            target = search_character(caller, self.lhs)
            if not target:
                return
                
            destination = caller.search(self.rhs, global_search=True)
            if not destination:
                return
                
            # Set the pre_summon_location attribute
            target.db.pre_summon_location = destination
            caller.msg(f"Set return location for {target.name} to {destination.name}.")
            return

        if "all" in self.switches:
            # Return all summoned characters in the current location
            returned_count = 0
            for character in caller.location.contents:
                if inherits_from(character, "evennia.objects.objects.DefaultCharacter"):
                    if self.return_character(character, quiet, force):
                        returned_count += 1
                        
            if returned_count:
                caller.msg(f"Returned {returned_count} character(s) to their previous locations.")
            else:
                caller.msg("No characters with stored previous locations found here.")
            return

        if not args:
            caller.msg("Usage: +return <character>")
            return

        # Use our new search helper
        target = search_character(caller, args)
        if not target:
            return
            
        # Return the character
        self.return_character(target, quiet, force)


class CmdConfigOOCIC(MuxCommand):
    """
    Configure OOC/IC room settings from in-game.
    
    Usage:
        +config/ooc
        +config/ooc <room dbref or name>
        +config/ic
        +config/ic <room dbref or name>
        +config/ooc/clear
        +config/ic/clear
        +config/list
        +config/theme <color1>,<color2>,<color3>  - Set theme colors (header, text, dividers)
        +config/theme/clear                       - Clear theme colors (use defaults)
    
    Switches:
        ooc - Set or view the OOC room setting
        ic - Set or view the IC starting room setting
        clear - Clear the specified setting
        list - List all OOC/IC configuration settings
    
    This command allows developer-level staff to configure the OOC_ROOM_DBREF
    and IC_STARTING_ROOM_DBREF settings without editing the configuration file.
    
    Examples:
        +config/list                    # Show current settings
        +config/ooc #123               # Set OOC room to dbref #123
        +config/ooc OOC Lounge         # Set OOC room by name
        +config/ic #1                  # Set IC starting room to dbref #1
        +config/ooc/clear              # Clear OOC room setting
    """
    
    key = "+config"
    aliases = ["config"]
    locks = "cmd:perm(developer)"
    help_category = "Admin Commands"
    switch_options = ("ooc", "ic", "clear", "list", "theme")
    
    def func(self):
        """Execute the command"""
        caller = self.caller
        args = self.args.strip()
        
        # Check developer permissions
        if not caller.check_permstring("developer"):
            caller.msg("You need developer permissions to use this command.")
            return
        
        # Handle list switch - show current settings
        if "list" in self.switches or not self.switches:
            self.show_current_settings()
            return
        
        # Handle clear switches
        if "clear" in self.switches:
            if "ooc" in self.switches:
                self.clear_setting("OOC_ROOM_DBREF", "OOC room")
            elif "ic" in self.switches:
                self.clear_setting("IC_STARTING_ROOM_DBREF", "IC starting room")
            elif "theme" in self.switches:
                self.clear_setting("ROOM_THEME_COLORS", "theme colors")
            else:
                caller.msg("Usage: +config/ooc/clear, +config/ic/clear, or +config/theme/clear")
            return
        
        # Handle setting configuration
        if "ooc" in self.switches:
            if not args:
                self.show_setting("OOC_ROOM_DBREF", "OOC room")
            else:
                self.set_room_setting("OOC_ROOM_DBREF", "OOC room", args)
        elif "ic" in self.switches:
            if not args:
                self.show_setting("IC_STARTING_ROOM_DBREF", "IC starting room")
            else:
                self.set_room_setting("IC_STARTING_ROOM_DBREF", "IC starting room", args)
        elif "theme" in self.switches:
            if not args:
                self.show_theme_colors()
            else:
                self.set_theme_colors(args)
        else:
            caller.msg("Usage: +config/ooc <room>, +config/ic <room>, or +config/theme <colors>")
    
    def show_current_settings(self):
        """Show all current OOC/IC configuration settings"""
        caller = self.caller
        
        caller.msg("=== OOC/IC Configuration Settings ===")
        
        # Get OOC room setting
        ooc_dbref = ServerConfig.objects.conf("OOC_ROOM_DBREF")
        if ooc_dbref:
            ooc_room = evennia.search_object(f"#{ooc_dbref}")
            if ooc_room:
                caller.msg(f"OOC Room: #{ooc_dbref} ({ooc_room[0].name})")
            else:
                caller.msg(f"OOC Room: #{ooc_dbref} (ROOM NOT FOUND)")
        else:
            caller.msg("OOC Room: Not set")
        
        # Get IC starting room setting
        ic_dbref = ServerConfig.objects.conf("IC_STARTING_ROOM_DBREF")
        if ic_dbref:
            ic_room = evennia.search_object(f"#{ic_dbref}")
            if ic_room:
                caller.msg(f"IC Starting Room: #{ic_dbref} ({ic_room[0].name})")
            else:
                caller.msg(f"IC Starting Room: #{ic_dbref} (ROOM NOT FOUND)")
        else:
            caller.msg("IC Starting Room: Not set")
        
        # Get theme colors setting
        theme_colors = ServerConfig.objects.conf("ROOM_THEME_COLORS")
        if theme_colors:
            caller.msg(f"Theme Colors: {theme_colors}")
            caller.msg("(Affects rooms, +roster, who, +census, +lookup, and other formatted displays)")
        else:
            caller.msg("Theme Colors: Not set (using defaults: green)")
        
        caller.msg("\nUse '+config/ooc <room>' or '+config/ic <room>' to set these values.")
        caller.msg("Use '+config/theme <color1>,<color2>,<color3>' to set theme colors.")
        caller.msg("Use '+config/ooc/clear', '+config/ic/clear', or '+config/theme/clear' to clear them.")
    
    def show_setting(self, setting_key, setting_name):
        """Show a specific setting"""
        caller = self.caller
        
        dbref = ServerConfig.objects.conf(setting_key)
        if dbref:
            room = evennia.search_object(f"#{dbref}")
            if room:
                caller.msg(f"{setting_name}: #{dbref} ({room[0].name})")
            else:
                caller.msg(f"{setting_name}: #{dbref} (ROOM NOT FOUND)")
        else:
            caller.msg(f"{setting_name}: Not set")
    
    def set_room_setting(self, setting_key, setting_name, room_input):
        """Set a room setting by dbref or name"""
        caller = self.caller
        
        # Try to find the room
        room = None
        
        # First try as a dbref
        if room_input.startswith('#'):
            try:
                dbref = int(room_input[1:])
                room = evennia.search_object(f"#{dbref}")
                if room:
                    room = room[0]
            except ValueError:
                pass
        
        # If not found as dbref, try by name
        if not room:
            room_matches = caller.search(room_input, global_search=True)
            if room_matches:
                room = room_matches
        
        if not room:
            caller.msg(f"Could not find room '{room_input}'.")
            return
        
        # Verify it's actually a room
        if not hasattr(room, 'location') or room.location is not None:
            caller.msg(f"'{room.name}' doesn't appear to be a room.")
            return
        
        # Set the configuration
        ServerConfig.objects.conf(setting_key, room.id)
        
        # Log the change
        evennia.logger.log_info(f"Config Change: {caller.name} (#{caller.id}) set {setting_key} to {room.name} (#{room.id})")
        
        caller.msg(f"Set {setting_name} to: {room.name} (#{room.id})")
        caller.msg(f"The {setting_name.lower()} commands will now use this room.")
    
    def clear_setting(self, setting_key, setting_name):
        """Clear a configuration setting"""
        caller = self.caller
        
        # Get current value for logging
        current_value = ServerConfig.objects.conf(setting_key)
        
        # Clear the setting
        ServerConfig.objects.conf(setting_key, delete=True)
        
        # Log the change
        evennia.logger.log_info(f"Config Change: {caller.name} (#{caller.id}) cleared {setting_key} (was: {current_value})")
        
        caller.msg(f"Cleared {setting_name} setting.")
        if "ROOM" not in setting_key:
            caller.msg(f"The {setting_name.lower()} commands will no longer work until this is set again.")
    
    def set_theme_colors(self, colors_input):
        """Set theme colors for room display."""
        caller = self.caller
        
        # Parse colors
        colors = [c.strip().lower() for c in colors_input.split(",")]
        
        if len(colors) != 3:
            caller.msg("Usage: +config/theme <color1>,<color2>,<color3>")
            caller.msg("Colors: header, header_text, dividers")
            caller.msg("Example: +config/theme red,yellow,blue")
            caller.msg("Valid colors: r, g, b, m, c, y, w, x (or full names like red, green, etc.)")
            return
        
        # Validate colors
        valid_colors = {
            'r': 'red', 'red': 'red',
            'g': 'green', 'green': 'green', 
            'b': 'blue', 'blue': 'blue',
            'm': 'magenta', 'magenta': 'magenta',
            'c': 'cyan', 'cyan': 'cyan',
            'y': 'yellow', 'yellow': 'yellow',
            'w': 'white', 'white': 'white',
            'x': 'black', 'black': 'black'
        }
        
        normalized_colors = []
        for color in colors:
            if color not in valid_colors:
                caller.msg(f"Invalid color: {color}")
                caller.msg("Valid colors: r, g, b, m, c, y, w, x (or red, green, blue, magenta, cyan, yellow, white, black)")
                return
            # Store the single-letter code for consistency
            normalized_colors.append(color if len(color) == 1 else color[0])
        
        # Store as comma-separated string
        theme_string = ",".join(normalized_colors)
        ServerConfig.objects.conf("ROOM_THEME_COLORS", theme_string)
        
        # Log the change
        evennia.logger.log_info(f"Config Change: {caller.name} (#{caller.id}) set ROOM_THEME_COLORS to {theme_string}")
        
        color_names = [valid_colors[c] for c in normalized_colors]
        caller.msg(f"Set theme colors to: {', '.join(color_names)}")
        caller.msg(f"  Header/Footer: |{normalized_colors[0]}████|n {color_names[0]}")
        caller.msg(f"  Header Text: |{normalized_colors[1]}████|n {color_names[1]}")
        caller.msg(f"  Dividers: |{normalized_colors[2]}████|n {color_names[2]}")
        caller.msg("\nTheme affects: rooms, +roster, who, +census, +lookup, and other formatted displays.")
    
    def show_theme_colors(self):
        """Show current theme colors."""
        caller = self.caller
        
        theme_colors = ServerConfig.objects.conf("ROOM_THEME_COLORS")
        if theme_colors:
            colors = theme_colors.split(",")
            color_map = {'r': 'red', 'g': 'green', 'b': 'blue', 'm': 'magenta', 
                        'c': 'cyan', 'y': 'yellow', 'w': 'white', 'x': 'black'}
            
            caller.msg("Current theme colors:")
            if len(colors) >= 3:
                caller.msg(f"  Header/Footer: |{colors[0]}████|n {color_map.get(colors[0], colors[0])}")
                caller.msg(f"  Header Text: |{colors[1]}████|n {color_map.get(colors[1], colors[1])}")
                caller.msg(f"  Dividers: |{colors[2]}████|n {color_map.get(colors[2], colors[2])}")
            else:
                caller.msg(f"  {theme_colors} (invalid format)")
        else:
            caller.msg("Theme colors not set (using defaults: green for all)")
            caller.msg("Affects: rooms, +roster, who, +census, +lookup")


class CmdFixGroupTypes(MuxCommand):
    """
    Fix group types for sphere-level groups.
    
    Usage:
        +fixgrouptypes
        +fixgrouptypes/confirm
    
    This command scans all groups and updates any sphere-level groups
    (Vampire, Mage, Changeling, etc.) to have the 'Sphere' type instead of
    their current type (Coterie, Cabal, Motley, etc.).
    
    Without /confirm, it will show what would be changed.
    With /confirm, it will actually make the changes.
    """
    
    key = "+fixgrouptypes"
    locks = "cmd:perm(Admin)"
    help_category = "Admin Commands"
    switch_options = ("confirm",)
    
    def func(self):
        """Execute the command"""
        from world.groups.utils import get_all_groups, determine_group_type
        
        caller = self.caller
        confirm = "confirm" in self.switches
        
        # Define sphere names
        sphere_names = ['vampire', 'werewolf', 'mage', 'changeling', 'hunter', 'geist', 
                       'mummy', 'demon', 'deviant', 'promethean', 'mortal+', 'mortal']
        
        # Get all groups
        all_groups = get_all_groups()
        
        # Find groups that need fixing
        groups_to_fix = []
        for group in all_groups:
            if group.name.lower() in sphere_names and group.group_type != 'sphere':
                groups_to_fix.append(group)
        
        if not groups_to_fix:
            caller.msg("No groups need fixing. All sphere-level groups already have the correct type.")
            return
        
        # Show what would be changed
        caller.msg("|wGroups that need fixing:|n")
        caller.msg("")
        
        for group in groups_to_fix:
            caller.msg(f"  #{group.group_id} |c{group.name}|n")
            caller.msg(f"    Current type: |r{group.get_group_type_display()}|n")
            caller.msg(f"    New type: |gSphere|n")
            caller.msg("")
        
        caller.msg(f"|wTotal groups to fix: {len(groups_to_fix)}|n")
        
        if not confirm:
            caller.msg("")
            caller.msg("Use |y+fixgrouptypes/confirm|n to apply these changes.")
            return
        
        # Apply the changes
        fixed_count = 0
        for group in groups_to_fix:
            old_type = group.get_group_type_display()
            group.group_type = 'sphere'
            group.save()
            fixed_count += 1
            
            # Log the change
            logger.log_info(f"Group Type Fix: {caller.name} changed {group.name} (#{group.group_id}) from {old_type} to Sphere")
        
        caller.msg("")
        caller.msg(f"|gSuccessfully fixed {fixed_count} group(s)!|n")
        caller.msg("All sphere-level groups now have the 'Sphere' type.")