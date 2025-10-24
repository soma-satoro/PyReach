"""
Area Manager

Manages game areas and their codes.
- Defining available area codes and names
- Auto-numbering rooms within areas
- ASCII map generation
- Area lookup and validation
"""

from evennia.scripts.scripts import DefaultScript


class AreaManager(DefaultScript):
    """
    A script that manages area definitions and room numbering.
    This is a persistent script that stores area configuration data.
    """
    
    def at_script_creation(self):
        """Initialize the area manager with default areas."""
        self.key = "area_manager"
        self.desc = "Manages game areas and room codes"
        self.interval = 0  # Don't repeat
        self.persistent = True
        self.start_delay = True
        
        # Initialize default areas if they don't exist
        self._init_default_areas()
    
    def _init_default_areas(self):
        """Initialize the default areas if they don't exist."""
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self.db.areas = {
                'HE': {
                    'name': 'The Hedge',
                    'description': 'The twisted realm between the mortal world and Arcadia',
                    'next_room': 1,
                    'rooms': {}  # Will store room_number: room_id mappings
                },
                'SH': {
                    'name': 'The Shadow',
                    'description': 'The spirit world',
                    'next_room': 1,
                    'rooms': {}
                },
                'WD': {
                    'name': 'The Wilderness',
                    'description': 'Wilderness beyond the city or noted locations',
                    'next_room': 1,
                    'rooms': {}
                },
                'CT': {
                    'name': 'Court Holdings',
                    'description': 'Areas controlled by specific courts',
                    'next_room': 1,
                    'rooms': {}
                }
            }
    
    def get_areas(self):
        """Return all defined areas."""
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
        return self.db.areas
    
    def get_area_codes(self):
        """Return list of all area codes."""
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
        return list(self.db.areas.keys())
    
    def get_area_info(self, area_code):
        """Get information about a specific area."""
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
        return self.db.areas.get(area_code.upper(), None)
    
    def add_area(self, area_code, name, description=""):
        """
        Add a new area to the system.
        
        Args:
            area_code (str): Two-letter area code
            name (str): Full name of the area
            description (str): Description of the area
        """
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
            
        area_code = area_code.upper()
        if len(area_code) != 2:
            return False, "Area code must be exactly 2 characters"
        
        if area_code in self.db.areas:
            return False, f"Area code {area_code} already exists"
        
        self.db.areas[area_code] = {
            'name': name,
            'description': description,
            'next_room': 1,
            'rooms': {}
        }
        return True, f"Area {area_code} ({name}) added successfully"
    
    def remove_area(self, area_code):
        """
        Remove an area from the system.
        
        Args:
            area_code (str): Two-letter area code
        """
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
            
        area_code = area_code.upper()
        if area_code not in self.db.areas:
            return False, f"Area code {area_code} not found"
        
        # Check if any rooms are using this area
        if self.db.areas[area_code]['rooms']:
            return False, f"Cannot remove area {area_code}: {len(self.db.areas[area_code]['rooms'])} rooms still use this area"
        
        del self.db.areas[area_code]
        return True, f"Area {area_code} removed successfully"
    
    def get_next_room_number(self, area_code):
        """
        Get the next available room number for an area.
        
        Args:
            area_code (str): Two-letter area code
            
        Returns:
            str: Full room code (e.g., "HE03")
        """
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
            
        area_code = area_code.upper()
        if area_code not in self.db.areas:
            return None
        
        next_num = self.db.areas[area_code]['next_room']
        room_code = f"{area_code}{next_num:02d}"
        
        # Increment for next time
        self.db.areas[area_code]['next_room'] = next_num + 1
        
        return room_code
    
    def register_room(self, area_code, room_number, room_id):
        """
        Register a room with the area manager.
        
        Args:
            area_code (str): Two-letter area code
            room_number (int): Room number within the area
            room_id (int): Database ID of the room object
        """
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
            
        area_code = area_code.upper()
        if area_code not in self.db.areas:
            return False
        
        self.db.areas[area_code]['rooms'][room_number] = room_id
        return True
    
    def unregister_room(self, area_code, room_number):
        """
        Unregister a room from the area manager.
        
        Args:
            area_code (str): Two-letter area code
            room_number (int): Room number within the area
        """
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
            
        area_code = area_code.upper()
        if area_code not in self.db.areas:
            return False
        
        if room_number in self.db.areas[area_code]['rooms']:
            del self.db.areas[area_code]['rooms'][room_number]
            return True
        return False
    
    def get_area_rooms(self, area_code):
        """
        Get all rooms in a specific area.
        
        Args:
            area_code (str): Two-letter area code
            
        Returns:
            dict: Dictionary of room_number: room_id mappings
        """
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
            
        area_code = area_code.upper()
        if area_code not in self.db.areas:
            return {}
        
        return self.db.areas[area_code]['rooms']
    
    def validate_area_code(self, area_code):
        """
        Check if an area code is valid.
        
        Args:
            area_code (str): Two-letter area code
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Ensure areas are initialized
        if not hasattr(self.db, 'areas') or self.db.areas is None:
            self._init_default_areas()
            
        return area_code.upper() in self.db.areas
    
    def get_room_coordinates(self, room_id):
        """
        Get coordinates for a room if they exist.
        This is used for map generation.
        
        Args:
            room_id (int): Database ID of the room
            
        Returns:
            tuple: (x, y) coordinates or None if not set
        """
        from evennia import search_object
        room = search_object(f"#{room_id}")
        if not room:
            return None
        
        room = room[0]
        if (hasattr(room.db, 'map_x') and hasattr(room.db, 'map_y') and 
            room.db.map_x is not None and room.db.map_y is not None):
            return (room.db.map_x, room.db.map_y)
        
        return None
    
    def set_room_coordinates(self, room_id, x, y):
        """
        Set coordinates for a room for map generation.
        
        Args:
            room_id (int): Database ID of the room
            x (int): X coordinate
            y (int): Y coordinate
        """
        from evennia import search_object
        room = search_object(f"#{room_id}")
        if not room:
            return False
        
        room = room[0]
        room.db.map_x = x
        room.db.map_y = y
        return True


def get_area_manager():
    """
    Get the global area manager instance.
    Creates it if it doesn't exist.
    """
    from evennia import search_script
    
    managers = search_script("area_manager")
    if managers:
        return managers[0]
    
    # Create the area manager if it doesn't exist
    from evennia import create_script
    manager = create_script(AreaManager, key="area_manager")
    return manager
