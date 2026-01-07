"""
Room

Rooms are simple containers that has no location of their own.
Room typeclass with formatted displays for the game.

"""

from evennia.objects.objects import DefaultRoom
from evennia.utils import utils, evtable
from evennia.utils.ansi import ANSIString
from evennia.server.models import ServerConfig
import time

from .objects import ObjectParent


class Room(DefaultRoom):
    """
    Rooms with custom formatting.
    
    Features:
    - Formatted room headers with location hierarchy
    - Character display with idle times and shortdesc
    - Separated directions (cardinal) from other exits
    - Places system integration
    - IC Area mapping integration
    
    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Objects.
    """

    def at_object_creation(self):
        """
        Called once when the room is first created.
        Set up default attributes for the room display.
        """
        super().at_object_creation()
        
        # Default attributes for room display
        self.db.area_name = "Unknown Area"
        self.db.area_code = "XX00"
        self.db.location_hierarchy = ["Unknown", "Unknown"]
        self.db.places_active = True
        
    def return_appearance(self, looker, **kwargs):
        """
        This formats a description. It is the hook a 'look' command
        should call.
        
        Args:
            looker (Object): Object doing the looking.
            **kwargs: Arbitrary, optional arguments for users
                overriding the call (unused by default).
        """
        if not looker:
            return ""
            
        # Build the formatted room display
        appearance_parts = []
        
        # Header
        header = self.get_display_header(looker)
        if header:
            appearance_parts.append(header)
            
        # Description
        desc = self.get_display_desc(looker)
        if desc:
            appearance_parts.append(desc)
            
        # Places section
        places = self.get_display_places(looker)
        if places:
            appearance_parts.append(places)
            
        # Characters section
        characters = self.get_display_characters(looker)
        if characters:
            appearance_parts.append(characters)
            
        # Directions section
        directions = self.get_display_directions(looker)
        if directions:
            appearance_parts.append(directions)
            
        # Exits section
        exits = self.get_display_exits(looker)
        if exits:
            appearance_parts.append(exits)
            
        # Footer
        footer = self.get_display_footer(looker)
        if footer:
            appearance_parts.append(footer)
            
        return "\n".join(appearance_parts)

    def get_theme_colors(self):
        """Get theme colors from server config or defaults."""
        theme_colors = ServerConfig.objects.conf("ROOM_THEME_COLORS")
        if theme_colors:
            colors = theme_colors.split(",")
            if len(colors) >= 3:
                return colors[0], colors[1], colors[2]
        # Default colors (green)
        return 'g', 'g', 'g'
    
    def get_display_header(self, looker, **kwargs):
        """
        Get the formatted header for the room display.
        
        Format: ===> Room Name - Area1 - Area2 - Area3 <===
        """
        # Get theme colors
        header_color, text_color, divider_color = self.get_theme_colors()
        
        room_name = self.get_display_name(looker)
        hierarchy = self.db.location_hierarchy or ["Unknown", "Unknown"]
        
        # Convert _SaverList to regular list if needed
        if hasattr(hierarchy, '__iter__') and not isinstance(hierarchy, (str, bytes)):
            hierarchy = list(hierarchy)
        
        # Ensure we have exactly 2 hierarchy items
        if len(hierarchy) < 2:
            hierarchy = hierarchy + ["Unknown"] * (2 - len(hierarchy))
        elif len(hierarchy) > 2:
            hierarchy = hierarchy[:2]
        
        # Build the location string
        location_string = " - ".join([room_name] + hierarchy)
        
        # Create the header with proper centering and theme colors
        header_content = f" {location_string} "
        total_width = 80
        equals_per_side = (total_width - len(header_content) - 4) // 2  # -4 for the arrows
        
        header = f"|{header_color}" + "=" * equals_per_side + ">" + f"|{text_color}" + header_content + f"|{header_color}" + "<" + "=" * equals_per_side + "|n"
        
        return header

    def get_display_desc(self, looker, **kwargs):
        """
        Get the room description with proper formatting.
        Shows Shadow/Hisil description if looker is in Shadow or peeking.
        """
        # Check if we should show Shadow description
        try:
            from world.reality_systems import is_in_shadow, is_peeking_shadow
            
            if is_in_shadow(looker):
                # Show Hisil description if available
                hisil_desc = getattr(self.db, 'hisil_desc', None)
                if hisil_desc:
                    desc = hisil_desc
                else:
                    desc = "(The Shadow reflects the material world here, but no specific description has been set.)"
            elif is_peeking_shadow(looker):
                # Show Hisil description when peeking
                hisil_desc = getattr(self.db, 'hisil_desc', None)
                if hisil_desc:
                    desc = f"|c[Peering into the Shadow]|n\n{hisil_desc}"
                else:
                    desc = "|c[Peering into the Shadow]|n\n(No specific Shadow description has been set.)"
            else:
                # Show normal description
                desc = self.db.desc
        except ImportError:
            # Fallback if reality_systems not available
            desc = self.db.desc
            
        if not desc:
            return ""
            
        # Process special characters first
        try:
            from utils.text import process_special_characters
            desc = process_special_characters(desc)
        except ImportError:
            # Fallback: basic substitution if utils module not available
            desc = desc.replace('%r%r', '\n\n').replace('%r', '\n').replace('%t', '     ')
            
        # Format description with proper indentation and spacing
        formatted_desc = "\n\n"
        
        # Split into paragraphs and add proper spacing
        paragraphs = desc.split('\n\n')
        for i, paragraph in enumerate(paragraphs):
            # Clean up the paragraph and add tab indentation
            clean_paragraph = ' '.join(paragraph.split())
            formatted_desc += f"\t{clean_paragraph}\n"
            if i < len(paragraphs) - 1:  # Add spacing between paragraphs
                formatted_desc += "\n"
                
        return formatted_desc

    def get_display_places(self, looker, **kwargs):
        """
        Get the places section display.
        """
        if not self.db.places_active:
            return ""
            
        # Check if there are any places defined
        places = getattr(self.db, 'places', {})
        if not places:
            return ""
            
        places_text = "\n"
        places_text += " " * 12 + "Places are active here. Use plook and plook # to see descriptions." + " " * 12
        places_text += "\n"
        
        return places_text

    def get_display_characters(self, looker, **kwargs):
        """
        Get the characters section with idle times and shortdesc.
        Filters characters based on reality state (Shadow/Hisil).
        
        Format: Name                     IdleTime Description
        """
        # Get all characters in the room (including the looker)
        all_characters = [obj for obj in self.contents if obj.has_account]
        
        # Filter based on reality state
        try:
            from world.reality_systems import is_in_shadow, is_peeking_shadow
            
            looker_in_shadow = is_in_shadow(looker)
            looker_peeking = is_peeking_shadow(looker)
            
            characters = []
            for char in all_characters:
                char_in_shadow = is_in_shadow(char)
                
                # Show character if:
                # 1. Both are in same reality (both in Shadow or both in material)
                # 2. Looker is peeking and can see Shadow
                if looker_in_shadow == char_in_shadow:
                    characters.append(char)
                elif looker_peeking and char_in_shadow:
                    characters.append(char)
        except ImportError:
            # Fallback if reality_systems not available
            characters = all_characters
        
        if not characters:
            return ""
            
        # Get theme colors
        header_color, text_color, divider_color = self.get_theme_colors()
        
        char_lines = []
        char_lines.append(f"|{divider_color}----> Characters <" + "-" * 62 + "|n")
        
        # Display characters in two columns with dot leaders
        for i in range(0, len(characters), 2):
            left_char = characters[i]
            right_char = characters[i + 1] if i + 1 < len(characters) else None
            
            # Left column
            left_name = left_char.get_display_name(looker)
            left_idle = self.get_character_idle_time(left_char)
            # Create dot leader between name and idle time (total width 28 chars)
            left_dots = "." * (35 - len(left_name) - len(left_idle))
            left_text = f"{left_name}{left_dots}{left_idle}"
            
            # Right column (if exists)
            if right_char:
                right_name = right_char.get_display_name(looker)
                right_idle = self.get_character_idle_time(right_char)
                # Create dot leader between name and idle time (total width 28 chars)
                right_dots = "." * (35 - len(right_name) - len(right_idle))
                right_text = f"{right_name}{right_dots}{right_idle}"
            else:
                right_text = ""
            
            # Combine columns with proper spacing (left column is 39 chars total)
            line = f"{left_text:<39} {right_text}"
            char_lines.append(line.rstrip())
            
        return "\n" + "\n".join(char_lines)

    def get_character_idle_time(self, character):
        """
        Calculate and format the idle time for a character.
        
        Returns:
            str: Formatted idle time (e.g., "5m", "2h", "0s")
        """
        # Get the character's session
        sessions = character.sessions.all()
        if not sessions:
            return "?"
            
        # Get the most recent activity time
        last_activity = None
        for session in sessions:
            if hasattr(session, 'cmd_last') and session.cmd_last:
                if not last_activity or session.cmd_last > last_activity:
                    last_activity = session.cmd_last
                    
        if not last_activity:
            return "0s"
            
        # Calculate idle time
        idle_seconds = int(time.time() - last_activity)
        
        if idle_seconds < 60:
            return f"{idle_seconds}s"
        elif idle_seconds < 3600:
            return f"{idle_seconds // 60}m"
        else:
            return f"{idle_seconds // 3600}h"

    def get_display_directions(self, looker, **kwargs):
        """
        Get exits that are cardinal directions.
        
        Cardinal directions: north, south, east, west, northeast, northwest, southeast, southwest, up, down
        """
        cardinal_directions = {
            'north': 'N', 'south': 'S', 'east': 'E', 'west': 'W',
            'northeast': 'NE', 'northwest': 'NW', 'southeast': 'SE', 'southwest': 'SW',
            'up': 'U', 'down': 'D', 'n': 'N', 's': 'S', 'e': 'E', 'w': 'W',
            'ne': 'NE', 'nw': 'NW', 'se': 'SE', 'sw': 'SW', 'u': 'U', 'd': 'D'
        }
        
        directions = []
        
        # Get all exits and filter for cardinal directions
        for exit_obj in self.exits:
            exit_name = exit_obj.key.lower()
            exit_aliases = [alias.lower() for alias in exit_obj.aliases.all()]
            
            # Check if this exit is a cardinal direction
            # Priority: 1) Check aliases first, 2) Fall back to exact exit name match
            is_cardinal = False
            matched_abbrev = None
            
            # First check if any of the exit's aliases match a cardinal direction
            for alias in exit_aliases:
                if alias in cardinal_directions:
                    is_cardinal = True
                    matched_abbrev = cardinal_directions[alias]
                    break
            
            # If no alias matched, check if the exit name exactly matches a cardinal direction
            if not is_cardinal and exit_name in cardinal_directions:
                is_cardinal = True
                matched_abbrev = cardinal_directions[exit_name]
            
            if is_cardinal:
                # Get the destination name
                dest_name = "Unknown"
                if exit_obj.destination:
                    dest_name = exit_obj.destination.get_display_name(looker)
                
                directions.append(f"{dest_name} <{matched_abbrev}>")
                    
        if not directions:
            return ""
            
        # Get theme colors
        header_color, text_color, divider_color = self.get_theme_colors()
        
        # Format directions section
        dir_lines = []
        dir_lines.append(f"|{divider_color}----> Directions <" + "-" * 62 + "|n")
        
        # Display directions in groups of 2 per line with extra spacing
        for i in range(0, len(directions), 2):
            line_dirs = directions[i:i+2]
            formatted_dirs = []
            for direction in line_dirs:
                formatted_dirs.append(f"{direction:<40}")
            dir_lines.append("".join(formatted_dirs).rstrip())
            
        return "\n" + "\n".join(dir_lines)

    def get_display_exits(self, looker, **kwargs):
        """
        Get exits that are NOT cardinal directions.
        Filters Hedge Gates based on viewer's ability to see them.
        """
        cardinal_directions = {
            'north', 'south', 'east', 'west', 'northeast', 'northwest', 
            'southeast', 'southwest', 'up', 'down', 'n', 's', 'e', 'w',
            'ne', 'nw', 'se', 'sw', 'u', 'd'
        }
        
        other_exits = []
        
        # Get all exits and filter for non-cardinal directions
        for exit_obj in self.exits:
            # Check if viewer can see this exit (Hedge Gates)
            try:
                from world.reality_systems import can_see_hedge_gate
                if not can_see_hedge_gate(looker, exit_obj):
                    continue
            except ImportError:
                pass  # Show all exits if reality_systems not available
            
            exit_name = exit_obj.key.lower()
            exit_aliases = [alias.lower() for alias in exit_obj.aliases.all()]
            
            # Check if this exit is NOT a cardinal direction
            # Priority: 1) Check aliases first, 2) Fall back to exact exit name match
            is_cardinal = False
            
            # First check if any of the exit's aliases match a cardinal direction
            for alias in exit_aliases:
                if alias in cardinal_directions:
                    is_cardinal = True
                    break
            
            # If no alias matched, check if the exit name exactly matches a cardinal direction
            if not is_cardinal and exit_name in cardinal_directions:
                is_cardinal = True
                    
            if not is_cardinal:
                # Get the exit display (usually just the key, but could include aliases)
                exit_display = exit_obj.key
                
                # Check if it's a Hedge Gate and color it appropriately
                try:
                    from world.reality_systems import is_hedge_gate
                    if is_hedge_gate(exit_obj):
                        # Get theme colors for hedge gates
                        header_color, _, _ = self.get_theme_colors()
                        exit_display = f"|{header_color}{exit_display}|n"
                except ImportError:
                    pass
                
                if exit_obj.aliases.all():
                    # Show primary alias in brackets
                    exit_display += f" <{exit_obj.aliases.all()[0]}>"
                other_exits.append(exit_display)
                
        if not other_exits:
            return ""
            
        # Get theme colors
        header_color, text_color, divider_color = self.get_theme_colors()
        
        # Format exits section
        exit_lines = []
        exit_lines.append(f"|{divider_color}----> Exits <" + "-" * 67 + "|n")
        
        # Display exits in groups of 3 per line
        for i in range(0, len(other_exits), 3):
            line_exits = other_exits[i:i+3]
            formatted_exits = []
            for exit in line_exits:
                formatted_exits.append(f"{exit:<30}")
            exit_lines.append("".join(formatted_exits).rstrip())
            
        return "\n" + "\n".join(exit_lines)

    def get_display_footer(self, looker, **kwargs):
        """
        Get the footer with IC/OOC Area information.
        
        Format: ======> IC Area - AREACODE <====
                ======> OOC Area - AREACODE <=== (if room has 'ooc' tag)
        """
        # Get theme colors
        header_color, text_color, divider_color = self.get_theme_colors()
        
        area_name = self.db.area_name or "Unknown Area"
        area_code = self.db.area_code or "XX00"
        
        # Check if room has 'ooc' tag (check both Evennia tags and db.tags attribute)
        is_ooc = False
        
        # Check Evennia's tag system
        if self.tags.get("ooc", category=None):
            is_ooc = True
        
        # Also check db.tags attribute (for legacy/alternative tag storage)
        # db.tags can be a _SaverList (Evennia's list wrapper) or regular list/string
        if hasattr(self.db, 'tags') and self.db.tags:
            try:
                # Try to check if 'ooc' is in the tags (works for lists, _SaverList, etc.)
                if 'ooc' in self.db.tags:
                    is_ooc = True
            except TypeError:
                # If 'in' operator fails, check if it's a string
                if isinstance(self.db.tags, str) and self.db.tags == 'ooc':
                    is_ooc = True
        
        area_type = "OOC Area" if is_ooc else "IC Area"
        
        footer_content = f" {area_type} - {area_code} "
        total_width = 80
        equals_per_side = (total_width - len(footer_content) - 4) // 2  # -4 for the arrows
        
        footer = f"|{header_color}" + "=" * equals_per_side + ">" + f"|{text_color}" + footer_content + f"|{header_color}" + "<" + "=" * equals_per_side + "|n"
        
        return "\n" + footer

    def set_area_info(self, area_name, area_code, location_hierarchy=None):
        """
        Convenience method to set area information for the room.
        
        Args:
            area_name (str): The name of the IC area
            area_code (str): The area code (e.g., "HE03")
            location_hierarchy (list): List of location names for the header
        """
        self.db.area_name = area_name
        self.db.area_code = area_code
        if location_hierarchy:
            self.db.location_hierarchy = list(location_hierarchy)

    def set_places_active(self, active=True):
        """
        Enable or disable the places system display for this room.
        
        Args:
            active (bool): Whether places should be shown
        """
        self.db.places_active = active

    def add_place(self, place_name, place_desc, place_number=None):
        """
        Add a place to this room's places system.
        
        Args:
            place_name (str): Name of the place
            place_desc (str): Description of the place
            place_number (int): Optional specific number for the place
        """
        if not hasattr(self.db, 'places') or not self.db.places:
            self.db.places = {}
            
        if place_number is None:
            # Find the next available number
            existing_numbers = [int(k) for k in self.db.places.keys() if k.isdigit()]
            place_number = max(existing_numbers, default=0) + 1
        
        # Process special characters in the place description
        try:
            from utils.text import process_special_characters
            processed_desc = process_special_characters(place_desc)
        except ImportError:
            # Fallback: basic substitution if utils module not available
            processed_desc = place_desc.replace('%r%r', '\n\n').replace('%r', '\n').replace('%t', '     ')
            
        self.db.places[str(place_number)] = {
            'name': place_name,
            'desc': processed_desc
        }
        
        return place_number


class ChargenRoom(Room):
    """
    Special room typeclass for character generation.
    
    This room displays character creation progress for all characters present,
    showing how many points they've spent vs. how many they have available
    based on their template (starting with mortal base).
    
    Features:
    - Tracks mortal base points (Attributes, Skills, Specialties, Merits)
    - Displays points spent vs. available for each character
    - Template-aware (future expansion for supernatural templates)
    """
    
    def at_object_creation(self):
        """Called when the chargen room is first created."""
        super().at_object_creation()
        
        # Tag this room as chargen by default
        if not hasattr(self.db, 'tags') or not self.db.tags:
            self.db.tags = []
        if 'chargen' not in self.db.tags:
            self.db.tags.append('chargen')
        if 'ooc' not in self.db.tags:
            self.db.tags.append('ooc')
    
    def calculate_chargen_points(self, character):
        """
        Calculate character generation points for a character.
        
        Returns a dictionary with:
        - attributes_spent, attributes_available
        - skills_spent, skills_available  
        - specialties_spent, specialties_available
        - merits_spent, merits_available
        - attribute categories (mental, physical, social) with points and priority
        - skill categories (mental, physical, social) with points and priority
        
        Args:
            character: The character object to calculate points for
            
        Returns:
            dict: Point allocation information
        """
        stats = getattr(character.db, 'stats', {})
        if not stats:
            return None
            
        # Mortal base starting points
        # Attributes: 5/4/3 dots to ADD to starting values (all attrs start at 1)
        # Skills: 11/7/4 dots to distribute among categories (all skills start at 0)
        MORTAL_ATTR_POINTS = 12  # 5 + 4 + 3 = 12 total dots to add
        MORTAL_SKILL_POINTS = 22  # 11 + 7 + 4 = 22 total dots to distribute
        MORTAL_SPECIALTY_POINTS = 3
        MORTAL_MERIT_POINTS = 7
        
        # Define attribute categories
        MENTAL_ATTRIBUTES = ['intelligence', 'wits', 'resolve']
        PHYSICAL_ATTRIBUTES = ['strength', 'dexterity', 'stamina']
        SOCIAL_ATTRIBUTES = ['presence', 'manipulation', 'composure']
        
        # Define skill categories
        MENTAL_SKILLS = ['academics', 'computer', 'crafts', 'investigation', 'medicine', 'occult', 'politics', 'science']
        PHYSICAL_SKILLS = ['athletics', 'brawl', 'drive', 'firearms', 'larceny', 'stealth', 'survival', 'weaponry']
        SOCIAL_SKILLS = ['animal_ken', 'empathy', 'expression', 'intimidation', 'persuasion', 'socialize', 'streetwise', 'subterfuge']
        
        attributes = stats.get('attributes', {})
        skills = stats.get('skills', {})
        
        # Calculate attribute points by category (above starting 1)
        attr_mental = sum(max(0, attributes.get(attr, 1) - 1) for attr in MENTAL_ATTRIBUTES)
        attr_physical = sum(max(0, attributes.get(attr, 1) - 1) for attr in PHYSICAL_ATTRIBUTES)
        attr_social = sum(max(0, attributes.get(attr, 1) - 1) for attr in SOCIAL_ATTRIBUTES)
        
        # Calculate skill points by category
        skill_mental = sum(skills.get(skill, 0) for skill in MENTAL_SKILLS)
        skill_physical = sum(skills.get(skill, 0) for skill in PHYSICAL_SKILLS)
        skill_social = sum(skills.get(skill, 0) for skill in SOCIAL_SKILLS)
        
        # Determine attribute priorities (5/4/3)
        # These are dots to ADD to the starting values (not total dots)
        attr_categories = [
            ('Mental', attr_mental),
            ('Physical', attr_physical),
            ('Social', attr_social)
        ]
        attr_categories_sorted = sorted(attr_categories, key=lambda x: x[1], reverse=True)
        attr_priorities = {}
        for i, (cat_name, points) in enumerate(attr_categories_sorted):
            if i == 0:
                priority = 'Primary (5)'
                expected = 5  # 5 dots to add to starting values
            elif i == 1:
                priority = 'Secondary (4)'
                expected = 4  # 4 dots to add to starting values
            else:
                priority = 'Tertiary (3)'
                expected = 3  # 3 dots to add to starting values
            attr_priorities[cat_name] = {'points': points, 'priority': priority, 'expected': expected}
        
        # Determine skill priorities (11/7/4)
        skill_categories = [
            ('Mental', skill_mental),
            ('Physical', skill_physical),
            ('Social', skill_social)
        ]
        skill_categories_sorted = sorted(skill_categories, key=lambda x: x[1], reverse=True)
        skill_priorities = {}
        for i, (cat_name, points) in enumerate(skill_categories_sorted):
            if i == 0:
                priority = 'Primary (11)'
                expected = 11
            elif i == 1:
                priority = 'Secondary (7)'
                expected = 7
            else:
                priority = 'Tertiary (4)'
                expected = 4
            skill_priorities[cat_name] = {'points': points, 'priority': priority, 'expected': expected}
        
        # Calculate total points
        attr_spent = attr_mental + attr_physical + attr_social
        skill_spent = skill_mental + skill_physical + skill_social
        
        # Calculate specialties
        specialties = stats.get('specialties', {})
        specialty_count = 0
        for skill, specs in specialties.items():
            if isinstance(specs, list):
                specialty_count += len(specs)
            elif isinstance(specs, int):
                specialty_count += specs
                
        # Calculate merits
        merits = stats.get('merits', {})
        merit_spent = 0
        for merit_name, merit_data in merits.items():
            if isinstance(merit_data, dict):
                merit_spent += merit_data.get('dots', 0)
            elif isinstance(merit_data, int):
                merit_spent += merit_data
        
        return {
            'attributes_spent': attr_spent,
            'attributes_available': MORTAL_ATTR_POINTS,
            'attribute_categories': attr_priorities,
            'skills_spent': skill_spent,
            'skills_available': MORTAL_SKILL_POINTS,
            'skill_categories': skill_priorities,
            'specialties_spent': specialty_count,
            'specialties_available': MORTAL_SPECIALTY_POINTS,
            'merits_spent': merit_spent,
            'merits_available': MORTAL_MERIT_POINTS,
            'template': stats.get('other', {}).get('template', 'Mortal')
        }
    
    def get_chargen_display(self, looker):
        """
        Generate a display of character generation progress for all characters in the room.
        
        Args:
            looker: The character viewing the room
            
        Returns:
            str: Formatted chargen progress display
        """
        # Get all characters in the room (including the looker)
        characters = [obj for obj in self.contents if obj.has_account]
        
        if not characters:
            return ""
        
        # Get theme colors
        header_color, text_color, divider_color = self.get_theme_colors()
        
        lines = []
        lines.append(f"\n|{divider_color}{'=' * 78}|n")
        lines.append(f"|{header_color}CHARACTER GENERATION PROGRESS|n".center(78))
        lines.append(f"|{divider_color}{'=' * 78}|n")
        
        for char in characters:
            points = self.calculate_chargen_points(char)
            
            if not points:
                continue
                
            char_name = char.get_display_name(looker)
            template = points.get('template', 'Mortal')
            
            # Character header
            lines.append(f"\n|y{char_name}|n ({template})")
            lines.append(f"|{divider_color}{'-' * 78}|n")
            
            # Attributes with category breakdown
            attr_spent = points['attributes_spent']
            attr_avail = points['attributes_available']
            attr_remaining = attr_avail - attr_spent
            attr_color = '|g' if attr_remaining >= 0 else '|r'
            lines.append(f"  |wAttributes:|n   {attr_color}{attr_spent}/{attr_avail}|n  (Remaining: {attr_color}{attr_remaining}|n)")
            
            # Show attribute categories
            attr_cats = points.get('attribute_categories', {})
            for cat_name in ['Mental', 'Physical', 'Social']:
                if cat_name in attr_cats:
                    cat_data = attr_cats[cat_name]
                    cat_points = cat_data['points']
                    cat_priority = cat_data['priority']
                    cat_expected = cat_data['expected']
                    cat_color = '|g' if cat_points == cat_expected else ('|y' if abs(cat_points - cat_expected) <= 1 else '|r')
                    lines.append(f"    {cat_name:10s} {cat_color}{cat_points:2d}/{cat_expected:2d}|n  {cat_priority}")
            
            # Skills with category breakdown
            skill_spent = points['skills_spent']
            skill_avail = points['skills_available']
            skill_remaining = skill_avail - skill_spent
            skill_color = '|g' if skill_remaining >= 0 else '|r'
            lines.append(f"  |wSkills:|n       {skill_color}{skill_spent}/{skill_avail}|n  (Remaining: {skill_color}{skill_remaining}|n)")
            
            # Show skill categories
            skill_cats = points.get('skill_categories', {})
            for cat_name in ['Mental', 'Physical', 'Social']:
                if cat_name in skill_cats:
                    cat_data = skill_cats[cat_name]
                    cat_points = cat_data['points']
                    cat_priority = cat_data['priority']
                    cat_expected = cat_data['expected']
                    cat_color = '|g' if cat_points == cat_expected else ('|y' if abs(cat_points - cat_expected) <= 1 else '|r')
                    lines.append(f"    {cat_name:10s} {cat_color}{cat_points:2d}/{cat_expected:2d}|n  {cat_priority}")
            
            # Specialties
            spec_spent = points['specialties_spent']
            spec_avail = points['specialties_available']
            spec_remaining = spec_avail - spec_spent
            spec_color = '|g' if spec_remaining >= 0 else '|r'
            lines.append(f"  |wSpecialties:|n  {spec_color}{spec_spent}/{spec_avail}|n  (Remaining: {spec_color}{spec_remaining}|n)")
            
            # Merits
            merit_spent = points['merits_spent']
            merit_avail = points['merits_available']
            merit_remaining = merit_avail - merit_spent
            merit_color = '|g' if merit_remaining >= 0 else '|r'
            lines.append(f"  |wMerits:|n       {merit_color}{merit_spent}/{merit_avail}|n  (Remaining: {merit_color}{merit_remaining}|n)")
            
        lines.append(f"|{divider_color}{'=' * 78}|n\n")
        
        return "\n".join(lines)
    
    def return_appearance(self, looker, **kwargs):
        """
        Override the appearance to include chargen progress.
        
        Args:
            looker: The character viewing the room
            **kwargs: Additional arguments
            
        Returns:
            str: Full room appearance with chargen progress
        """
        # Get the standard room appearance
        standard_appearance = super().return_appearance(looker, **kwargs)
        
        # Add chargen progress display
        chargen_display = self.get_chargen_display(looker)
        
        if chargen_display:
            return standard_appearance + chargen_display
        else:
            return standard_appearance