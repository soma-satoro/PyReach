"""
OOC/IC Movement Commands

Commands for moving between in-character and out-of-character areas,
with proper location tracking and synchronization to prevent the
location desynchronization bugs experienced on Dies Irae.
"""

from evennia import default_cmds
from evennia.commands.default.muxcommand import MuxCommand
from world.utils.permission_utils import check_staff_permission, format_permission_error
from utils.search_helpers import search_character
import evennia
from evennia.server.models import ServerConfig


class CmdGo(MuxCommand):
    """
    Move between In-Character and Out-of-Character areas.
    
    Usage:
        +go/ic  - Return to in-character areas
        +go/ooc - Move to the out-of-character area
        
    Aliases:
        +ic, +ooc (for backward compatibility)
    
    The /ic switch will return you to where you were before using /ooc,
    or send you to the staff-designated IC starting room if no previous
    location is stored.
    
    The /ooc switch will teleport you to the staff-designated OOC room
    and store your current location for later return with /ic.
    
    Examples:
        +go/ic
        +go/ooc
        +ic
        +ooc
    """
    
    key = "+go"
    aliases = ["+ic", "+ooc", "ic"]
    locks = "cmd:all()"
    help_category = "OOC/IC Movement"
    
    def func(self):
        """Execute the command"""
        caller = self.caller
        
        # Check if caller is a character
        if not caller.has_account:
            caller.msg("Only characters can use this command.")
            return
        
        # Determine which switch to use based on the command or switches
        if not self.switches:
            # If no switch, check if they used an alias
            if self.cmdstring in ["+ic", "ic"]:
                self.go_ic()
            elif self.cmdstring == "+ooc":
                self.go_ooc()
            else:
                # No switch and main command - show help
                caller.msg("Usage: +go/ic or +go/ooc")
                caller.msg("Use +go/ic to return to in-character areas.")
                caller.msg("Use +go/ooc to move to the out-of-character area.")
            return
        
        switch = self.switches[0].lower()
        
        if switch == "ic":
            self.go_ic()
        elif switch == "ooc":
            self.go_ooc()
        else:
            caller.msg(f"Invalid switch '{switch}'. Use +go/ic or +go/ooc")
    
    def go_ooc(self):
        """Handle the /ooc switch - move to OOC area"""
        caller = self.caller
        
        # Get the designated OOC room from server configuration
        ooc_room_dbref = ServerConfig.objects.conf("OOC_ROOM_DBREF")
        if not ooc_room_dbref:
            caller.msg("No OOC room has been designated by staff. Use '+config/ooc <room>' to set one.")
            return
        
        # Search for the OOC room
        ooc_room = evennia.search_object(f"#{ooc_room_dbref}")
        if not ooc_room:
            caller.msg(f"OOC room #{ooc_room_dbref} not found. Please contact staff.")
            return
        
        ooc_room = ooc_room[0]  # search_object returns a list
        
        # Store current location for +go/ic command
        current_location = caller.location
        if current_location and hasattr(current_location, "id"):
            # Store the location directly as an object reference
            # This avoids serialization issues with dict attributes
            caller.db.pre_ooc_location = current_location
            
            # Log the movement on the server
            evennia.logger.log_info(f"OOC Movement: {caller.name} (#{caller.id}) moved from {current_location.name} (#{current_location.id}) to OOC room")
        else:
            caller.msg("Warning: Could not store your current location for return.")
        
        # Force synchronization before moving to prevent desync
        caller.save()
        
        # Move to OOC room
        if caller.move_to(
            ooc_room,
            quiet=False,
            emit_to_obj=caller,
            move_type="teleport"
        ):
            caller.msg(f"You have moved to the OOC area: {ooc_room.name}")
            caller.msg("Use +go/ic (or +ic) to return to your previous location or the IC starting area.")
            
            # Force another save after the move to ensure location is synchronized
            caller.save()
        else:
            caller.msg("Failed to move to the OOC room. Please contact staff.")
    
    def go_ic(self):
        """Handle the /ic switch - return to IC area"""
        caller = self.caller
        
        destination = None
        location_type = "starting"
        
        # First, try to get their stored pre-OOC location
        if hasattr(caller.db, 'pre_ooc_location') and caller.db.pre_ooc_location:
            stored_location = caller.db.pre_ooc_location
            
            # Verify the stored location still exists and is valid
            if (hasattr(stored_location, 'id') and 
                hasattr(stored_location, 'name') and
                stored_location.access(caller, 'view')):
                destination = stored_location
                location_type = "previous"
        
        # If no valid stored location, use the IC starting room
        if not destination:
            ic_room_dbref = ServerConfig.objects.conf("IC_STARTING_ROOM_DBREF")
            if not ic_room_dbref:
                caller.msg("No IC starting room has been designated by staff. Use '+config/ic <room>' to set one.")
                return
            
            # Search for the IC starting room
            ic_room = evennia.search_object(f"#{ic_room_dbref}")
            if not ic_room:
                caller.msg(f"IC starting room #{ic_room_dbref} not found. Please contact staff.")
                return
            
            destination = ic_room[0]  # search_object returns a list
        
        # Log the movement on the server
        current_location = caller.location
        if current_location and hasattr(current_location, "id"):
            evennia.logger.log_info(f"IC Movement: {caller.name} (#{caller.id}) moved from {current_location.name} (#{current_location.id}) to {destination.name} (#{destination.id}) [{location_type}]")
        
        # Force synchronization before moving
        caller.save()
        
        # Move to destination
        if caller.move_to(
            destination,
            quiet=False,
            emit_to_obj=caller,
            move_type="teleport"
        ):
            if location_type == "previous":
                caller.msg(f"You have returned to your previous location: {destination.name}")
                # Clear the stored location since we've used it
                caller.attributes.remove("pre_ooc_location")
            else:
                caller.msg(f"You have moved to the IC starting area: {destination.name}")
            
            # Force another save after the move to ensure location is synchronized
            caller.save()
        else:
            caller.msg("Failed to move to the IC area. Please contact staff.")


class CmdJoin(MuxCommand):
    """
    Teleport to a player's location (Staff only).
    
    Usage:
        +join <player name>
        +join/quiet <player name>
    
    Switches:
        quiet - Don't announce your arrival to the player
    
    This command allows staff to teleport to a player for direct
    communication, adjudicating rolls, disputes, etc.
    """
    
    key = "+join"
    aliases = ["join"]
    locks = "cmd:perm(staff)"
    help_category = "Roleplaying Tools"
    
    def func(self):
        """Execute the command"""
        caller = self.caller
        args = self.args.strip()
        
        # Check staff permissions
        if not check_staff_permission(caller):
            caller.msg(format_permission_error("Staff"))
            return
        
        if not args:
            caller.msg("Usage: +join <player name>")
            return
        
        # Search for the target player
        target = search_character(caller, args)
        if not target:
            return
        
        # Verify target has a valid location
        if not target.location:
            caller.msg(f"{target.name} doesn't appear to be anywhere.")
            return
        
        # Store caller's current location for potential return
        current_location = caller.location
        if current_location and hasattr(current_location, "id"):
            caller.db.pre_join_location = current_location
            
            # Log the movement on the server
            evennia.logger.log_info(f"Staff Join: {caller.name} (#{caller.id}) joined {target.name} (#{target.id}) at {target.location.name} (#{target.location.id}) from {current_location.name} (#{current_location.id})")
        
        # Force synchronization before moving
        caller.save()
        
        # Move to target's location
        if caller.move_to(
            target.location,
            quiet="quiet" in self.switches,
            emit_to_obj=caller,
            move_type="teleport"
        ):
            caller.msg(f"You have joined {target.name} at {target.location.name}.")
            if "quiet" not in self.switches:
                target.msg(f"{caller.name} has joined you.")
            
            # Force another save after the move
            caller.save()
        else:
            caller.msg(f"Failed to join {target.name}.")


