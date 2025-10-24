"""
Hangout Commands

Commands for finding and traveling to designated hangout/roleplay locations.
Hangouts can be public social spaces (bars, cafes, parks, etc.) or 
group-specific locations accessible to group members.
"""

from evennia import default_cmds
from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.evtable import EvTable
import evennia
from typeclasses.groups import Group
from utils.search_helpers import search_character


class CmdHangouts(MuxCommand):
    """
    List available hangout locations for roleplay.
    
    Usage:
        +hangouts              - List all available hangout locations
        +hangouts/public       - List only public hangout locations
        +hangouts/groups       - List only group hangout locations
        +hangouts <name>       - Move to a specific hangout location
        +hangouts/return       - Return to your previous location
    
    Hangout locations include:
    - Public social spaces (bars, restaurants, cafes, parks, etc.)
    - Group-specific locations for groups you belong to
    
    Public hangout rooms are those tagged with social/gathering tags:
    bar, nightclub, restaurant, cafe, theater, church, gathering_hall,
    marketplace, park, etc.
    
    Group hangout locations are set by staff/group leaders using:
    +hangout/set <group>=<room>
    """
    
    key = "+hangouts"
    aliases = ["hangout", "hangouts"]
    locks = "cmd:all()"
    help_category = "OOC/IC Movement"
    
    # Tags that designate a room as a public hangout location
    HANGOUT_TAGS = [
        'bar', 'nightclub', 'restaurant', 'cafe', 'theater', 
        'church', 'synagogue', 'mosque', 'temple',
        'gathering_hall', 'marketplace', 'park', 'plaza',
        'court', 'throne_room', 'forum', 'agora',
        'ballroom', 'parlor', 'gentlemens_club', 'ladies_parlor',
        'coffee_shop', 'gym', 'stadium', 'playground',
    ]
    
    def func(self):
        """Execute the command"""
        caller = self.caller
        args = self.args.strip()
        
        # Check if caller is a character
        if not caller.has_account:
            caller.msg("Only characters can use this command.")
            return
        
        # Handle /return switch
        if "return" in self.switches:
            self.return_from_hangout()
            return
        
        # If they provided a hangout name, try to move there
        if args:
            self.move_to_hangout(args)
            return
        
        # Otherwise, list hangouts
        show_public = "public" in self.switches or not self.switches
        show_groups = "groups" in self.switches or not self.switches
        
        self.list_hangouts(show_public, show_groups)
    
    def list_hangouts(self, show_public=True, show_groups=True):
        """List available hangout locations."""
        caller = self.caller
        output = []
        
        output.append("|w" + "=" * 78 + "|n")
        output.append("|wAvailable Hangout Locations|n".center(78))
        output.append("|w" + "=" * 78 + "|n")
        
        # Public hangouts
        if show_public:
            public_hangouts = self.get_public_hangouts()
            if public_hangouts:
                output.append("\n|cPublic Hangout Locations:|n")
                output.append("|w" + "-" * 78 + "|n")
                
                table = EvTable(
                    "|wName|n",
                    "|wType|n",
                    "|wLocation|n",
                    border="cells",
                    width=78
                )
                
                for room in public_hangouts:
                    # Get room type from tags
                    room_type = self.get_room_type(room)
                    # Get location hierarchy for context
                    hierarchy = room.db.location_hierarchy or ["Unknown"]
                    location = hierarchy[0] if hierarchy else "Unknown"
                    
                    table.add_row(
                        room.name,
                        room_type.title(),
                        location
                    )
                
                output.append(str(table))
            else:
                output.append("\n|xNo public hangout locations available.|n")
        
        # Group hangouts
        if show_groups:
            group_hangouts = self.get_group_hangouts()
            if group_hangouts:
                output.append("\n|cGroup Hangout Locations:|n")
                output.append("|w" + "-" * 78 + "|n")
                
                table = EvTable(
                    "|wGroup|n",
                    "|wLocation|n",
                    "|wArea|n",
                    border="cells",
                    width=78
                )
                
                for group, room in group_hangouts:
                    # Get location hierarchy for context
                    hierarchy = room.db.location_hierarchy or ["Unknown"]
                    area = hierarchy[0] if hierarchy else "Unknown"
                    
                    table.add_row(
                        group.name,
                        room.name,
                        area
                    )
                
                output.append(str(table))
            else:
                output.append("\n|xNo group hangout locations available for your groups.|n")
        
        output.append("\n|wUsage:|n +hangouts <name> to travel to a location")
        output.append("       +hangouts/return to return to your previous location")
        output.append("|w" + "=" * 78 + "|n")
        
        caller.msg("\n".join(output))
    
    def get_public_hangouts(self):
        """Get all rooms tagged as public hangouts."""
        hangouts = []
        
        # Search for rooms with hangout tags
        all_rooms = evennia.search_tag(category="room_tag")
        
        # Also search rooms without category specification
        for tag in self.HANGOUT_TAGS:
            tagged_rooms = evennia.search_tag(tag)
            if tagged_rooms:
                for room in tagged_rooms:
                    # Make sure it's actually a room
                    if hasattr(room, 'return_appearance') and room not in hangouts:
                        # Check if it has any of our hangout tags
                        room_tags = room.tags.all()
                        if any(t in self.HANGOUT_TAGS for t in room_tags):
                            hangouts.append(room)
        
        # Sort by name
        hangouts.sort(key=lambda x: x.name)
        return hangouts
    
    def get_group_hangouts(self):
        """Get hangout locations for groups the caller belongs to."""
        caller = self.caller
        group_hangouts = []
        
        # Get all groups
        all_groups = Group.objects.all()
        
        for group in all_groups:
            # Check if caller is a member
            if group.is_member(caller):
                # Check if group has a hangout location set
                if hasattr(group.db, 'hangout_location') and group.db.hangout_location:
                    hangout_room = group.db.hangout_location
                    # Verify the room still exists
                    if hasattr(hangout_room, 'name'):
                        group_hangouts.append((group, hangout_room))
        
        # Sort by group name
        group_hangouts.sort(key=lambda x: x[0].name)
        return group_hangouts
    
    def get_room_type(self, room):
        """Get the primary type of a hangout room from its tags."""
        room_tags = room.tags.all()
        
        # Check tags in priority order
        priority_tags = [
            'bar', 'nightclub', 'restaurant', 'cafe', 'park',
            'theater', 'church', 'gathering_hall', 'marketplace'
        ]
        
        for tag in priority_tags:
            if tag in room_tags:
                return tag
        
        # Check any other hangout tag
        for tag in room_tags:
            if tag in self.HANGOUT_TAGS:
                return tag
        
        return "hangout"
    
    def move_to_hangout(self, hangout_name):
        """Move the caller to a specified hangout location."""
        caller = self.caller
        
        # Search both public and group hangouts
        public_hangouts = self.get_public_hangouts()
        group_hangouts = self.get_group_hangouts()
        
        # Combine all available hangouts
        all_hangouts = {room.name.lower(): room for room in public_hangouts}
        for group, room in group_hangouts:
            # Allow matching by room name or group name
            all_hangouts[room.name.lower()] = room
            all_hangouts[group.name.lower()] = room
        
        # Try to find a match
        hangout_lower = hangout_name.lower()
        destination = None
        
        # Exact match
        if hangout_lower in all_hangouts:
            destination = all_hangouts[hangout_lower]
        else:
            # Partial match
            matches = [name for name in all_hangouts.keys() if hangout_lower in name]
            if len(matches) == 1:
                destination = all_hangouts[matches[0]]
            elif len(matches) > 1:
                caller.msg(f"Multiple hangouts match '{hangout_name}':")
                for match in matches:
                    caller.msg(f"  - {all_hangouts[match].name}")
                caller.msg("Please be more specific.")
                return
            else:
                caller.msg(f"No hangout location found matching '{hangout_name}'.")
                caller.msg("Use '+hangouts' to see available locations.")
                return
        
        # Store current location for return
        current_location = caller.location
        if current_location and hasattr(current_location, "id"):
            caller.db.pre_hangout_location = current_location
            
            # Log the movement
            evennia.logger.log_info(
                f"Hangout Movement: {caller.name} (#{caller.id}) moved from "
                f"{current_location.name} (#{current_location.id}) to "
                f"{destination.name} (#{destination.id})"
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
            caller.msg(f"You travel to {destination.name}.")
            caller.msg("Use +hangouts/return to return to your previous location.")
            
            # Force another save after the move
            caller.save()
        else:
            caller.msg(f"Failed to travel to {destination.name}. Please contact staff.")
    
    def return_from_hangout(self):
        """Return the caller to their previous location."""
        caller = self.caller
        
        # Try to get their stored pre-hangout location
        if not hasattr(caller.db, 'pre_hangout_location') or not caller.db.pre_hangout_location:
            caller.msg("You don't have a previous location to return to.")
            caller.msg("You must have used +hangouts to travel somewhere first.")
            return
        
        stored_location = caller.db.pre_hangout_location
        
        # Verify the stored location still exists and is valid
        if not (hasattr(stored_location, 'id') and 
                hasattr(stored_location, 'name') and
                stored_location.access(caller, 'view')):
            caller.msg("Your previous location is no longer accessible.")
            caller.attributes.remove("pre_hangout_location")
            return
        
        # Log the movement
        current_location = caller.location
        if current_location and hasattr(current_location, "id"):
            evennia.logger.log_info(
                f"Hangout Return: {caller.name} (#{caller.id}) returned from "
                f"{current_location.name} (#{current_location.id}) to "
                f"{stored_location.name} (#{stored_location.id})"
            )
        
        # Force synchronization before moving
        caller.save()
        
        # Move to stored location
        if caller.move_to(
            stored_location,
            quiet=False,
            emit_to_obj=caller,
            move_type="teleport"
        ):
            caller.msg(f"You have returned to your previous location: {stored_location.name}")
            # Clear the stored location
            caller.attributes.remove("pre_hangout_location")
            
            # Force another save after the move
            caller.save()
        else:
            caller.msg("Failed to return to your previous location. Please contact staff.")


class CmdHangoutAdmin(MuxCommand):
    """
    Set or remove group hangout locations (Staff/Group Leader).
    
    Usage:
        +hangout/set <group>=<room>     - Set a group's hangout location
        +hangout/remove <group>         - Remove a group's hangout location
        +hangout/view <group>           - View a group's hangout location
    
    Examples:
        +hangout/set Ordo Dracul=The Dragon's Lair
        +hangout/set 1=#123
        +hangout/remove Ordo Dracul
        +hangout/view 1
    
    Only staff members and group leaders can set hangout locations for groups.
    """
    
    key = "+hangout"
    locks = "cmd:all()"
    help_category = "Group Management"
    
    def func(self):
        """Execute the command"""
        caller = self.caller
        
        # Only allow /set, /remove, or /view switches
        if not any(switch in ["set", "remove", "view"] for switch in self.switches):
            return  # Let the other command handle it
        
        # Check if caller is a character
        if not caller.has_account:
            caller.msg("Only characters can use this command.")
            return
        
        if "set" in self.switches:
            self.set_hangout()
        elif "remove" in self.switches:
            self.remove_hangout()
        elif "view" in self.switches:
            self.view_hangout()
    
    def set_hangout(self):
        """Set a group's hangout location."""
        caller = self.caller
        
        if not self.args or "=" not in self.args:
            caller.msg("Usage: +hangout/set <group>=<room>")
            return
        
        group_id, room_name = [part.strip() for part in self.args.split("=", 1)]
        
        # Find the group
        group = self.find_group(group_id)
        if not group:
            return
        
        # Check permissions
        if not self.can_manage_group(group):
            caller.msg(f"You don't have permission to manage {group.name}.")
            caller.msg("Only staff members and group leaders can set hangout locations.")
            return
        
        # Find the room
        room = self.find_room(room_name)
        if not room:
            return
        
        # Set the hangout location
        group.db.hangout_location = room
        
        caller.msg(f"Set {group.name}'s hangout location to: {room.name} (#{room.id})")
        evennia.logger.log_info(
            f"{caller.name} set group {group.name} (#{group.db.group_id}) "
            f"hangout to {room.name} (#{room.id})"
        )
    
    def remove_hangout(self):
        """Remove a group's hangout location."""
        caller = self.caller
        
        if not self.args:
            caller.msg("Usage: +hangout/remove <group>")
            return
        
        # Find the group
        group = self.find_group(self.args.strip())
        if not group:
            return
        
        # Check permissions
        if not self.can_manage_group(group):
            caller.msg(f"You don't have permission to manage {group.name}.")
            caller.msg("Only staff members and group leaders can remove hangout locations.")
            return
        
        # Remove the hangout location
        if hasattr(group.db, 'hangout_location'):
            old_location = group.db.hangout_location
            group.attributes.remove('hangout_location')
            caller.msg(f"Removed {group.name}'s hangout location.")
            if old_location:
                evennia.logger.log_info(
                    f"{caller.name} removed group {group.name} (#{group.db.group_id}) "
                    f"hangout (was: {old_location.name} #{old_location.id})"
                )
        else:
            caller.msg(f"{group.name} doesn't have a hangout location set.")
    
    def view_hangout(self):
        """View a group's hangout location."""
        caller = self.caller
        
        if not self.args:
            caller.msg("Usage: +hangout/view <group>")
            return
        
        # Find the group
        group = self.find_group(self.args.strip())
        if not group:
            return
        
        # Check if caller has access to view this group
        if not group.is_public and not group.is_member(caller) and not caller.check_permstring("builder"):
            caller.msg(f"You don't have access to view information about {group.name}.")
            return
        
        # Show hangout location
        if hasattr(group.db, 'hangout_location') and group.db.hangout_location:
            location = group.db.hangout_location
            caller.msg(f"|wGroup:|n {group.name}")
            caller.msg(f"|wHangout Location:|n {location.name} (#{location.id})")
            if hasattr(location.db, 'location_hierarchy') and location.db.location_hierarchy:
                hierarchy = location.db.location_hierarchy
                caller.msg(f"|wArea:|n {' - '.join(hierarchy)}")
        else:
            caller.msg(f"{group.name} doesn't have a hangout location set.")
    
    def find_group(self, identifier):
        """Find a group by ID or name."""
        caller = self.caller
        
        # Try to find by numeric ID
        if identifier.isdigit():
            from typeclasses.groups import get_group_by_id
            group = get_group_by_id(int(identifier))
            if group:
                return group
            caller.msg(f"No group found with ID {identifier}.")
            return None
        
        # Try to find by name
        from typeclasses.groups import get_group_by_name
        group = get_group_by_name(identifier)
        if group:
            return group
        
        caller.msg(f"No group found matching '{identifier}'.")
        caller.msg("Use '+groups' to see available groups.")
        return None
    
    def find_room(self, identifier):
        """Find a room by name or dbref."""
        caller = self.caller
        
        # Try dbref first
        if identifier.startswith("#"):
            room = evennia.search_object(identifier)
            if room:
                room = room[0]
                if hasattr(room, 'return_appearance'):
                    return room
                caller.msg(f"{identifier} is not a room.")
                return None
            caller.msg(f"No object found with dbref {identifier}.")
            return None
        
        # Search by name (prefer rooms in caller's current location or nearby)
        results = evennia.search_object(identifier, typeclass="typeclasses.rooms.Room")
        
        if not results:
            caller.msg(f"No room found matching '{identifier}'.")
            return None
        
        if len(results) > 1:
            caller.msg(f"Multiple rooms found matching '{identifier}':")
            for room in results[:10]:  # Limit to 10 results
                caller.msg(f"  {room.name} (#{room.id})")
            caller.msg("Please use a dbref (#123) to specify the exact room.")
            return None
        
        return results[0]
    
    def can_manage_group(self, group):
        """Check if caller can manage this group."""
        caller = self.caller
        
        # Staff can always manage
        if caller.check_permstring("builder"):
            return True
        
        # Group leader can manage
        if group.leader == caller:
            return True
        
        return False

