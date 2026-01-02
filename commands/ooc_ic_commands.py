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
    Move between In-Character and Out-of-Character areas, or fast-travel by coordinate.
    
    Usage:
        +go/ic          - Return to in-character areas
        +go/ooc         - Move to the out-of-character area
        +go/coord <code> - Fast-travel to a room by its area code
        
    Aliases:
        +ic, +ooc (for backward compatibility)
    
    The /ic switch will return you to where you were before using /ooc,
    or send you to the staff-designated IC starting room if no previous
    location is stored.
    
    The /ooc switch will teleport you to the staff-designated OOC room
    and store your current location for later return with /ic.
    
    The /coord switch allows fast-travel to any room by its area_code.
    For example, +go/coord BV01 will teleport you to the room with
    area_code "BV01".
    
    Examples:
        +go/ic
        +go/ooc
        +go/coord BV01
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
                caller.msg("Usage: +go/ic, +go/ooc, or +go/coord <area code>")
                caller.msg("Use +go/ic to return to in-character areas.")
                caller.msg("Use +go/ooc to move to the out-of-character area.")
                caller.msg("Use +go/coord <code> to fast-travel to a room by area code.")
            return
        
        switch = self.switches[0].lower()
        
        if switch == "ic":
            self.go_ic()
        elif switch == "ooc":
            self.go_ooc()
        elif switch == "coord":
            self.go_coord()
        else:
            caller.msg(f"Invalid switch '{switch}'. Use +go/ic, +go/ooc, or +go/coord")
    
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
    
    def go_coord(self):
        """Handle the /coord switch - fast-travel to a room by area code"""
        caller = self.caller
        
        # Check if an area code was provided
        if not self.args.strip():
            caller.msg("Usage: +go/coord <area code>")
            caller.msg("Example: +go/coord BV01")
            return
        
        area_code = self.args.strip().upper()
        
        # Search for rooms with matching area_code attribute
        from evennia.utils.search import search_object_attribute
        
        matching_rooms = search_object_attribute(
            key="area_code",
            value=area_code,
            category=None
        )
        
        if not matching_rooms:
            caller.msg(f"No room found with area code '{area_code}'.")
            caller.msg("Make sure you're using the correct area code format (e.g., BV01, DT03).")
            return
        
        # If multiple rooms found (shouldn't happen but handle it), take the first
        if len(matching_rooms) > 1:
            caller.msg(f"Warning: Multiple rooms found with area code '{area_code}'. Using the first one.")
            evennia.logger.log_warn(f"Multiple rooms with area_code '{area_code}': {[r.name for r in matching_rooms]}")
        
        destination = matching_rooms[0]
        
        # Verify the destination is accessible
        if not destination.access(caller, 'view'):
            caller.msg(f"You don't have permission to travel to that location.")
            return
        
        # Log the movement on the server
        current_location = caller.location
        if current_location and hasattr(current_location, "id"):
            evennia.logger.log_info(
                f"Coord Travel: {caller.name} (#{caller.id}) traveled from "
                f"{current_location.name} (#{current_location.id}) to "
                f"{destination.name} (#{destination.id}) [area_code: {area_code}]"
            )
        
        # Force synchronization before moving
        caller.save()
        
        # Move to destination
        if caller.move_to(
            destination,
            quiet=False,
            emit_to_obj=caller,
            move_type="teleport"
        ):
            # Get area name if available
            area_name = destination.db.area_name or "Unknown Area"
            
            caller.msg(f"You fast-travel to: {destination.name}")
            caller.msg(f"Area: {area_name} [{area_code}]")
            
            # Force another save after the move to ensure location is synchronized
            caller.save()
        else:
            caller.msg(f"Failed to travel to {destination.name}. Please contact staff.")


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


class CmdSummon(MuxCommand):
    """
    Summon a player to your location (Staff only).
    
    Usage:
        +summon <player name>
        +summon/quiet <player name>
    
    Switches:
        quiet - Don't announce to the player or the room
    
    This command allows staff to bring a player to their current location
    for direct communication, adjudicating rolls, disputes, etc. The player's
    previous location is stored so they can be returned later with +return.
    """
    
    key = "+summon"
    aliases = ["summon"]
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
            caller.msg("Usage: +summon <player name>")
            return
        
        # Verify caller has a valid location
        if not caller.location:
            caller.msg("You don't appear to be anywhere.")
            return
        
        # Search for the target player
        target = search_character(caller, args)
        if not target:
            return
        
        # Don't summon yourself
        if target == caller:
            caller.msg("You cannot summon yourself.")
            return
        
        # Store target's current location for +return command
        target_location = target.location
        if target_location and hasattr(target_location, "id"):
            # Store the location directly as an object reference
            # This avoids serialization issues with dict attributes
            target.db.pre_summon_location = target_location
            
            # Log the movement on the server
            evennia.logger.log_info(f"Staff Summon: {caller.name} (#{caller.id}) summoned {target.name} (#{target.id}) from {target_location.name} (#{target_location.id}) to {caller.location.name} (#{caller.location.id})")
        else:
            caller.msg(f"Warning: Could not store {target.name}'s current location for return.")
        
        # Force synchronization before moving to prevent desync
        target.save()
        
        # Move target to caller's location
        if target.move_to(
            caller.location,
            quiet="quiet" in self.switches,
            emit_to_obj=target,
            move_type="teleport"
        ):
            caller.msg(f"You have summoned {target.name} to your location.")
            if "quiet" not in self.switches:
                target.msg(f"You have been summoned by {caller.name}.")
            else:
                # Even in quiet mode, notify the player they were summoned
                target.msg(f"You have been summoned by staff.")
            
            # Force another save after the move to ensure location is synchronized
            target.save()
        else:
            caller.msg(f"Failed to summon {target.name}.")


class CmdReturn(MuxCommand):
    """
    Return a player to their previous location (Staff only).
    
    Usage:
        +return <player name>
        +return/quiet <player name>
    
    Switches:
        quiet - Don't announce to the player or the room
    
    This command returns a player to the location they were in before
    being summoned with +summon. If no stored location exists, the
    command will fail.
    """
    
    key = "+return"
    aliases = ["return"]
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
            caller.msg("Usage: +return <player name>")
            return
        
        # Search for the target player
        target = search_character(caller, args)
        if not target:
            return
        
        # Get the stored pre-summon location
        destination = None
        if hasattr(target.db, 'pre_summon_location') and target.db.pre_summon_location:
            stored_location = target.db.pre_summon_location
            
            # Verify the stored location still exists and is valid
            if (hasattr(stored_location, 'id') and 
                hasattr(stored_location, 'name') and
                stored_location.access(target, 'view')):
                destination = stored_location
        
        if not destination:
            caller.msg(f"{target.name} has no stored location to return to. They may not have been summoned.")
            return
        
        # Log the movement on the server
        current_location = target.location
        if current_location and hasattr(current_location, "id"):
            evennia.logger.log_info(f"Staff Return: {caller.name} (#{caller.id}) returned {target.name} (#{target.id}) from {current_location.name} (#{current_location.id}) to {destination.name} (#{destination.id})")
        
        # Force synchronization before moving
        target.save()
        
        # Move target back to their previous location
        if target.move_to(
            destination,
            quiet="quiet" in self.switches,
            emit_to_obj=target,
            move_type="teleport"
        ):
            caller.msg(f"You have returned {target.name} to {destination.name}.")
            if "quiet" not in self.switches:
                target.msg(f"You have been returned to your previous location by {caller.name}.")
            else:
                target.msg(f"You have been returned to your previous location by staff.")
            
            # Clear the stored location since we've used it
            target.attributes.remove("pre_summon_location")
            
            # Force another save after the move to ensure location is synchronized
            target.save()
        else:
            caller.msg(f"Failed to return {target.name}.")


