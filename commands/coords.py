"""
Coordinate Directory Command

Player-facing command for fast-travel coordination system.
Shows area codes and allows bookmarking favorite locations.
"""

import re
from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.evtable import EvTable
from evennia.utils.search import search_object
from world.area_manager import get_area_manager


class CmdCoords(MuxCommand):
    """
    View area codes for fast-travel and manage favorites.
    
    Usage:
        +coords                  - List all available area codes
        +coords <area_code>      - Show rooms in a specific area
        +coords/fav <code>       - Add a room to your favorites
        +coords/unfav <code>     - Remove a room from favorites
        +coords/favs             - List your favorite locations
        
    The coordinate system allows quick travel to any location using
    +go/coord <code>. Use this command to browse available destinations.
    
    Examples:
        +coords                  - View all areas
        +coords BV               - View all rooms in Bayview
        +coords/fav BV01         - Bookmark Park Boulevard & Bay Road
        +coords/favs             - View your bookmarked locations
        +coords/unfav BV01       - Remove bookmark
    """
    
    key = "+coords"
    aliases = ["+coord", "+coordinates"]
    locks = "cmd:all()"
    help_category = "OOC/IC Movement"
    
    def func(self):
        """Execute the command"""
        caller = self.caller
        
        # Handle switches
        if self.switches:
            switch = self.switches[0].lower()
            
            if switch == "fav":
                self.add_favorite()
            elif switch == "unfav":
                self.remove_favorite()
            elif switch == "favs":
                self.list_favorites()
            else:
                caller.msg(f"Invalid switch '{switch}'. Valid switches: /fav, /unfav, /favs")
            return
        
        # No switches - check if they specified an area code
        if self.args.strip():
            area_code = self.args.strip().upper()
            self.show_area_rooms(area_code)
        else:
            self.show_all_areas()
    
    def show_all_areas(self):
        """Show a directory of all available area codes"""
        caller = self.caller
        area_manager = get_area_manager()
        areas = area_manager.get_areas()
        
        if not areas:
            caller.msg("No areas have been defined yet.")
            return
        
        # Build styled output
        output = []
        output.append("|y" + "=" * 78 + "|n")
        title = "COORDINATE DIRECTORY"
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        output.append("Use |c+go/coord <code>|n to fast-travel to any location.")
        output.append("Use |c+coords <area>|n to see all rooms in that area.")
        output.append("")
        
        # Section header
        output.append(self._format_section_header("|wAVAILABLE AREAS|n"))
        output.append("")
        
        # Create table of areas
        for code, info in sorted(areas.items()):
            room_count = len(info['rooms'])
            if room_count > 0:
                room_text = f"{room_count} room{'s' if room_count != 1 else ''}"
                output.append(f"  |c{code}|n - |w{info['name']}|n ({room_text})")
        
        output.append("")
        
        # Footer with usage info
        output.append("|xTip: Use +coords/fav <code> to bookmark your favorite locations.|n")
        output.append("|y" + "=" * 78 + "|n")
        
        caller.msg("\n".join(output))
    
    def show_area_rooms(self, area_code):
        """Show all rooms in a specific area"""
        caller = self.caller
        area_manager = get_area_manager()
        
        # Validate area code
        info = area_manager.get_area_info(area_code)
        
        if not info:
            caller.msg(f"Area code '{area_code}' not found.")
            caller.msg("Use |c+coords|n to see all available areas.")
            return
        
        rooms = info['rooms']
        if not rooms:
            caller.msg(f"No rooms found in area {area_code} ({info['name']}).")
            return
        
        # Build styled output
        output = []
        output.append("|y" + "=" * 78 + "|n")
        title = f"AREA COORDINATES - {info['name']}"
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        output.append(f"|wArea Code:|n {area_code}")
        if info['description']:
            output.append(f"|wDescription:|n {info['description']}")
        output.append("")
        
        # Section header
        output.append(self._format_section_header("|wROOMS IN THIS AREA|n"))
        output.append("")
        
        # Get user's favorites for marking
        favorites = self._get_favorites()
        
        # List all rooms with their codes
        for room_num in sorted(rooms.keys()):
            room_id = rooms[room_num]
            room_obj = search_object(f"#{room_id}")
            
            room_code = f"{area_code}{room_num:02d}"
            
            if room_obj:
                room_name = room_obj[0].name
                # Mark favorites with a star
                fav_marker = "|y★|n " if room_code in favorites else "  "
                output.append(f"{fav_marker}|c{room_code}|n - {room_name}")
            else:
                output.append(f"  |c{room_code}|n - |rDeleted Room|n")
        
        output.append("")
        
        # Footer with usage info
        total_rooms = len(rooms)
        output.append(f"|gTotal: {total_rooms} room{'s' if total_rooms != 1 else ''}|n")
        output.append("|xUse +go/coord <code> to travel to any of these rooms.|n")
        output.append("|xUse +coords/fav <code> to bookmark a location.|n")
        output.append("|y" + "=" * 78 + "|n")
        
        caller.msg("\n".join(output))
    
    def add_favorite(self):
        """Add a room code to favorites"""
        caller = self.caller
        
        if not self.args.strip():
            caller.msg("Usage: +coords/fav <room code>")
            caller.msg("Example: +coords/fav BV01")
            return
        
        room_code = self.args.strip().upper()
        
        # Validate room code format (2 letters + 2 digits)
        if not re.match(r'^[A-Z]{2}\d{2}$', room_code):
            caller.msg("Invalid room code format. Use format like BV01, DT03, etc.")
            return
        
        # Verify the room exists
        from evennia.utils.search import search_object_attribute
        matching_rooms = search_object_attribute(
            key="area_code",
            value=room_code,
            category=None
        )
        
        if not matching_rooms:
            caller.msg(f"No room found with code '{room_code}'.")
            caller.msg("Use |c+coords <area>|n to see available room codes.")
            return
        
        # Initialize favorites if needed
        if not hasattr(caller.db, 'favorite_coords') or caller.db.favorite_coords is None:
            caller.db.favorite_coords = []
        
        # Check if already favorited
        if room_code in caller.db.favorite_coords:
            caller.msg(f"'{room_code}' is already in your favorites.")
            return
        
        # Add to favorites
        caller.db.favorite_coords.append(room_code)
        room_name = matching_rooms[0].name
        
        # Force synchronization to prevent deserialization issues
        caller.save()
        
        # Log the favorite addition
        import evennia
        evennia.logger.log_info(
            f"Favorite Added: {caller.name} (#{caller.id}) added {room_code} "
            f"({room_name}) to favorites"
        )
        
        caller.msg(f"|gAdded to favorites:|n {room_code} - {room_name}")
        caller.msg("Use |c+coords/favs|n to view all your favorites.")
    
    def remove_favorite(self):
        """Remove a room code from favorites"""
        caller = self.caller
        
        if not self.args.strip():
            caller.msg("Usage: +coords/unfav <room code>")
            caller.msg("Example: +coords/unfav BV01")
            return
        
        room_code = self.args.strip().upper()
        
        # Initialize favorites if needed
        if not hasattr(caller.db, 'favorite_coords') or caller.db.favorite_coords is None:
            caller.db.favorite_coords = []
        
        # Check if it's in favorites
        if room_code not in caller.db.favorite_coords:
            caller.msg(f"'{room_code}' is not in your favorites.")
            return
        
        # Remove from favorites
        caller.db.favorite_coords.remove(room_code)
        
        # Force synchronization to prevent deserialization issues
        caller.save()
        
        # Log the favorite removal
        import evennia
        evennia.logger.log_info(
            f"Favorite Removed: {caller.name} (#{caller.id}) removed {room_code} "
            f"from favorites"
        )
        
        caller.msg(f"|yRemoved from favorites:|n {room_code}")
        caller.msg("Use |c+coords/favs|n to view your remaining favorites.")
    
    def list_favorites(self):
        """List all favorited locations"""
        caller = self.caller
        
        # Initialize favorites if needed
        if not hasattr(caller.db, 'favorite_coords') or caller.db.favorite_coords is None:
            caller.db.favorite_coords = []
        
        favorites = caller.db.favorite_coords
        
        # Build styled output
        output = []
        output.append("|y" + "=" * 78 + "|n")
        title = "FAVORITE LOCATIONS"
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        if not favorites:
            output.append("|xYou have no favorite locations bookmarked.|n")
            output.append("")
            output.append("Use |c+coords/fav <code>|n to bookmark a location.")
            output.append("Example: |c+coords/fav BV01|n")
        else:
            output.append(self._format_section_header("|wYOUR FAVORITES|n"))
            output.append("")
            
            # Look up each favorite and display it
            from evennia.utils.search import search_object_attribute
            
            for room_code in sorted(favorites):
                # Try to find the room
                matching_rooms = search_object_attribute(
                    key="area_code",
                    value=room_code,
                    category=None
                )
                
                if matching_rooms:
                    room = matching_rooms[0]
                    area_name = room.db.area_name or "Unknown Area"
                    output.append(f"  |y★|n |c{room_code}|n - {room.name}")
                    output.append(f"      |x{area_name}|n")
                else:
                    output.append(f"  |y★|n |c{room_code}|n - |rRoom Not Found|n")
            
            output.append("")
            output.append(f"|gTotal: {len(favorites)} favorite{'s' if len(favorites) != 1 else ''}|n")
            output.append("|xUse +go/coord <code> to travel to any favorite.|n")
            output.append("|xUse +coords/unfav <code> to remove a favorite.|n")
        
        output.append("|y" + "=" * 78 + "|n")
        
        caller.msg("\n".join(output))
    
    def _get_favorites(self):
        """Get the caller's list of favorite room codes"""
        caller = self.caller
        if not hasattr(caller.db, 'favorite_coords') or caller.db.favorite_coords is None:
            return []
        return caller.db.favorite_coords
    
    def _format_section_header(self, section_name):
        """Format a section header matching +sheet style"""
        total_width = 78
        # Remove ANSI codes for length calculation
        clean_name = re.sub(r'\|[a-zA-Z]', '', section_name)
        name_length = len(clean_name)
        available_dash_space = total_width - name_length - 4
        left_dashes = available_dash_space // 2
        right_dashes = available_dash_space - left_dashes
        return f"|g<{'-' * left_dashes}|n {section_name} |g{'-' * right_dashes}>|n"
