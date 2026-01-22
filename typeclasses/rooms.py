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
from world.cofd.chargen_tracker import (
    calculate_chargen_points,
    calculate_vampire_chargen,
    calculate_werewolf_chargen,
    calculate_changeling_chargen,
    calculate_mage_chargen,
    calculate_deviant_chargen,
    calculate_geist_chargen,
    calculate_hunter_chargen,
    calculate_mummy_chargen,
    calculate_promethean_chargen,
    calculate_mortalplus_chargen,
    format_covenant_name,
    format_tribe_name
)


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
        # Calculate equals needed: total_width - len(content) - 2 (for > and <)
        total_equals = total_width - len(header_content) - 2
        equals_per_side = total_equals // 2
        # Add extra equals to right side if total is odd
        equals_right = equals_per_side + (total_equals % 2)
        
        header = f"|{header_color}" + "=" * equals_per_side + ">" + f"|{text_color}" + header_content + f"|{header_color}" + "<" + "=" * equals_right + "|n"
        
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
        # Calculate equals needed: total_width - len(content) - 2 (for > and <)
        total_equals = total_width - len(footer_content) - 2
        equals_per_side = total_equals // 2
        # Add extra equals to right side if total is odd
        equals_right = equals_per_side + (total_equals % 2)
        
        footer = f"|{header_color}" + "=" * equals_per_side + ">" + f"|{text_color}" + footer_content + f"|{header_color}" + "<" + "=" * equals_right + "|n"
        
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
        Delegates to chargen_tracker utility module.
        
        Args:
            character: The character object to calculate points for
            
        Returns:
            dict: Point allocation information
        """
        return calculate_chargen_points(character)
    
    def _format_covenant_name(self, covenant):
        """Delegate to chargen_tracker utility module."""
        return format_covenant_name(covenant)
    
    def _format_tribe_name(self, tribe):
        """Delegate to chargen_tracker utility module."""
        return format_tribe_name(tribe)
    
    def _calculate_vampire_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_vampire_chargen(character, stats, merits)
    
    def _calculate_werewolf_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_werewolf_chargen(character, stats, merits)
    
    def _calculate_changeling_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_changeling_chargen(character, stats, merits)
    
    def _calculate_mage_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_mage_chargen(character, stats, merits)
    
    def _calculate_deviant_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_deviant_chargen(character, stats, merits)
    
    def _calculate_geist_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_geist_chargen(character, stats, merits)
    
    def _calculate_hunter_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_hunter_chargen(character, stats, merits)
    
    def _calculate_mummy_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_mummy_chargen(character, stats, merits)
    
    def _calculate_promethean_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_promethean_chargen(character, stats, merits)
    
    def _calculate_mortalplus_chargen(self, character, stats, merits):
        """Delegate to chargen_tracker utility module."""
        return calculate_mortalplus_chargen(character, stats, merits)
    
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
        lines.append("")  # Empty line for spacing (matching base room desc format)
        lines.append(f"|{divider_color}{'=' * 80}|n")
        
        # Properly center the header text (visible length only, not counting color codes)
        header_text = "CHARACTER GENERATION PROGRESS"
        padding = (80 - len(header_text)) // 2
        centered_header = " " * padding + f"|{header_color}{header_text}|n" + " " * padding
        # Adjust for odd lengths
        if len(header_text) % 2 == 1:
            centered_header += " "
        lines.append(centered_header)
        
        lines.append(f"|{divider_color}{'=' * 80}|n")
        
        for char in characters:
            points = self.calculate_chargen_points(char)
            
            if not points:
                continue
                
            char_name = char.get_display_name(looker)
            template = points.get('template', 'Mortal')
            
            # Character header
            lines.append(f"\n|y{char_name}|n ({template})")
            lines.append(f"|{divider_color}{'-' * 80}|n")
            
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
            
            # Show favored stat if set
            favored_stat = points.get('favored_stat', None)
            if favored_stat:
                lines.append(f"  |cFavored Stat:|n {favored_stat.replace('_', ' ').title()} |g(free dot)|n")
            
            # Template-specific sections
            if 'vampire' in points:
                lines.append("")  # Empty line for spacing
                self._add_vampire_display(lines, points['vampire'], divider_color)
            elif 'werewolf' in points:
                lines.append("")  # Empty line for spacing
                self._add_werewolf_display(lines, points['werewolf'], divider_color)
            elif 'changeling' in points:
                lines.append("")  # Empty line for spacing
                self._add_changeling_display(lines, points['changeling'], divider_color)
            elif 'mage' in points:
                lines.append("")  # Empty line for spacing
                self._add_mage_display(lines, points['mage'], divider_color)
            elif 'deviant' in points:
                lines.append("")  # Empty line for spacing
                self._add_deviant_display(lines, points['deviant'], divider_color)
            elif 'geist' in points:
                lines.append("")  # Empty line for spacing
                self._add_geist_display(lines, points['geist'], divider_color)
            elif 'hunter' in points:
                lines.append("")  # Empty line for spacing
                self._add_hunter_display(lines, points['hunter'], divider_color)
            elif 'mummy' in points:
                lines.append("")  # Empty line for spacing
                self._add_mummy_display(lines, points['mummy'], divider_color)
            elif 'promethean' in points:
                lines.append("")  # Empty line for spacing
                self._add_promethean_display(lines, points['promethean'], divider_color)
            elif 'mortalplus' in points:
                lines.append("")  # Empty line for spacing
                self._add_mortalplus_display(lines, points['mortalplus'], divider_color)
            
        lines.append(f"|{divider_color}{'=' * 80}|n")
        lines.append("")  # Empty line for spacing after the display
        
        return "\n".join(lines)
    
    def _add_vampire_display(self, lines, vamp_data, divider_color):
        """Add vampire-specific chargen information to the display."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |cVAMPIRE TEMPLATE|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Clan and favored attributes
        clan = vamp_data['clan'].title() if vamp_data['clan'] else '|rNot Set|n'
        lines.append(f"  |wClan:|n         {clan}")
        
        if vamp_data['favored_attributes']:
            favored_options = vamp_data['favored_attributes']
            selected = vamp_data.get('favored_attr_used', None)
            
            if selected and selected in favored_options:
                # Show selected attribute in green, others dimmed
                favored_display = []
                for attr in favored_options:
                    if attr == selected:
                        favored_display.append(f"|g{attr.title()}|n |g[SELECTED]|n")
                    else:
                        favored_display.append(f"|x{attr.title()}|n")
                lines.append(f"  |wClan Bonus:|n   {' or '.join(favored_display)}")
            else:
                # Show both options, none selected
                favored_str = ' or '.join([a.title() for a in favored_options])
                lines.append(f"  |wClan Bonus:|n   {favored_str} |rx|n")
                lines.append(f"    |y(Use +stat/favored <attribute> to select free dot)|n")
        
        # Mask and Dirge
        mask_status = '|gok!|n' if vamp_data['has_mask'] else '|rx|n'
        dirge_status = '|gok!|n' if vamp_data['has_dirge'] else '|rx|n'
        lines.append(f"  |wMask:|n         {mask_status}    |wDirge:|n {dirge_status}")
        
        # Disciplines
        disc_spent = vamp_data['discipline_dots_total']
        disc_avail = vamp_data['discipline_dots_available']
        disc_remaining = disc_avail - disc_spent
        disc_color = '|g' if disc_remaining >= 0 else '|r'
        
        lines.append(f"  |wDisciplines:|n  {disc_color}{disc_spent}/{disc_avail}|n  (Remaining: {disc_color}{disc_remaining}|n)")
        
        # Show discipline breakdown
        in_clan = vamp_data['in_clan_dots']
        out_of_clan = vamp_data['out_of_clan_dots']
        covenant = vamp_data['covenant_power_dots']
        
        # Validation: at least 2 must be in-clan
        in_clan_status = '|g' if in_clan >= 2 else '|r'
        lines.append(f"    In-Clan:    {in_clan_status}{in_clan}|n (need at least 2)")
        if out_of_clan > 0:
            lines.append(f"    Out-of-Clan: {out_of_clan}")
        if covenant > 0:
            lines.append(f"    Covenant:    {covenant} (requires Covenant Status)")
        
        # List actual disciplines taken
        if vamp_data['disciplines']:
            disc_list = []
            for disc_name, dots in vamp_data['disciplines'].items():
                disc_lower = disc_name.lower().replace(' ', '_')
                # Mark if in-clan
                if disc_lower in vamp_data['in_clan_disciplines']:
                    disc_list.append(f"{disc_name} {dots} |g(in-clan)|n")
                else:
                    disc_list.append(f"{disc_name} {dots}")
            lines.append(f"    Taken: {', '.join(disc_list)}")
        
        # Blood Potency
        bp = vamp_data['blood_potency']
        bp_cost = vamp_data['bp_merit_cost']
        if bp_cost > 0:
            lines.append(f"  |wBlood Potency:|n {bp} (1 free + {bp - 1} from merits = {bp_cost} merit dots)")
        else:
            lines.append(f"  |wBlood Potency:|n {bp} (free dot)")
        
        # Covenant
        covenant_display = None
        if vamp_data['covenant']:
            # Format covenant name with proper full name
            covenant_display = self._format_covenant_name(vamp_data['covenant'])
        
        if covenant_display:
            lines.append(f"  |wCovenant:|n     {covenant_display}")
            # Check if they have Covenant Status merit
            covenant_status = vamp_data.get('covenant_status', None)
            covenant_status_dots = vamp_data.get('covenant_status_dots', 0)
            
            if covenant_status and isinstance(covenant_status_dots, int) and covenant_status_dots > 0:
                lines.append(f"    Status: {covenant_status_dots} dot{'s' if covenant_status_dots != 1 else ''} |g(enables benefits)|n")
            elif covenant_status:
                lines.append(f"    |yStatus: Present but no dots set (use +stat)|n")
            else:
                lines.append(f"    |yStatus: None (get Status merit for benefits)|n")
        else:
            lines.append(f"  |wCovenant:|n     |yNone (optional)|n")
        
        # Touchstone reminder
        touchstone_status = '|g(Merit taken)|n' if vamp_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
    
    def _add_werewolf_display(self, lines, wolf_data, divider_color):
        """Add werewolf-specific chargen information to the display."""
        lines.append(f"  |c{'~' * 76}|n")
        lines.append(f"  |cWEREWOLF TEMPLATE|n")
        lines.append(f"  |c{'~' * 76}|n")
        
        # Auspice and Tribe
        auspice = wolf_data['auspice'].replace('_', ' ').title() if wolf_data['auspice'] else '|rNot Set|n'
        tribe = self._format_tribe_name(wolf_data['tribe']) if wolf_data['tribe'] else '|rNot Set|n'
        lines.append(f"  |wAuspice:|n      {auspice}")
        lines.append(f"  |wTribe:|n        {tribe}")
        
        # Auspice skill bonus
        if wolf_data['auspice_skills']:
            skill_options = wolf_data['auspice_skills']
            selected = wolf_data.get('auspice_skill_used', None)
            
            if selected and selected in skill_options:
                # Show selected skill in green, others dimmed
                skill_display = []
                for skill in skill_options:
                    if skill == selected:
                        skill_display.append(f"|g{skill.replace('_', ' ').title()}|n |g[SELECTED]|n")
                    else:
                        skill_display.append(f"|x{skill.replace('_', ' ').title()}|n")
                lines.append(f"  |wAuspice Bonus:|n {', '.join(skill_display)}")
            else:
                # Show all options, none selected
                skills_str = ', '.join([s.replace('_', ' ').title() for s in skill_options])
                lines.append(f"  |wAuspice Bonus:|n {skills_str} |rx|n")
                lines.append(f"    |y(Use +stat/favored <skill> to select free dot)|n")
        
        # Bone and Blood
        bone_status = '|gok!|n' if wolf_data['has_bone'] else '|rx|n'
        blood_status = '|gok!|n' if wolf_data['has_blood'] else '|rx|n'
        lines.append(f"  |wBone:|n         {bone_status}    |wBlood:|n {blood_status}")
        
        # Renown
        renown_total = wolf_data['total_renown']
        renown_expected = wolf_data['expected_renown']
        renown_remaining = renown_expected - renown_total
        renown_color = '|g' if renown_remaining >= 0 and not wolf_data['has_excessive_renown'] else '|r'
        
        lines.append(f"  |wRenown:|n       {renown_color}{renown_total}/{renown_expected}|n  (Remaining: {renown_color}{renown_remaining}|n)")
        
        # Show renown breakdown
        renown = wolf_data['renown']
        renown_parts = []
        for r_name, r_dots in renown.items():
            if r_dots > 0:
                # Mark auspice and tribe renown
                markers = []
                if r_name == wolf_data['auspice_renown']:
                    markers.append('auspice')
                if r_name == wolf_data['tribe_renown']:
                    markers.append('tribe')
                
                marker_str = f" |c({', '.join(markers)})|n" if markers else ""
                renown_parts.append(f"{r_name.title()} {r_dots}{marker_str}")
        
        if renown_parts:
            lines.append(f"    {', '.join(renown_parts)}")
        
        # Validation warnings
        if not wolf_data['has_auspice_renown'] and wolf_data['auspice_renown']:
            lines.append(f"    |rWarning: Need 1+ {wolf_data['auspice_renown'].title()} (auspice)|n")
        if not wolf_data['has_tribe_renown'] and wolf_data['tribe_renown']:
            lines.append(f"    |rWarning: Need 1+ {wolf_data['tribe_renown'].title()} (tribe)|n")
        if wolf_data['has_excessive_renown']:
            lines.append(f"    |rWarning: Cannot have 3+ in any Renown at chargen|n")
        
        # Gifts
        lines.append(f"  |wGifts:|n")
        
        # Moon Gift
        moon_gift_status = '|gok!|n' if wolf_data['has_moon_gift'] else '|rx|n'
        lines.append(f"    Moon Gift ({wolf_data['moon_gift_name']}): {moon_gift_status}")
        
        # Shadow/Wolf Gifts (should have 2+ facets)
        expected_facets = 2  # Minimum expected at chargen
        facet_color = '|g' if wolf_data['gift_facets'] >= expected_facets else '|y'
        lines.append(f"    Shadow/Wolf Gift Facets: {facet_color}{wolf_data['gift_facets']}|n (need at least 2)")
        
        # List gifts taken
        if wolf_data['gifts']:
            gift_list = []
            for gift_name, gift_value in wolf_data['gifts'].items():
                dots = gift_value if isinstance(gift_value, int) else 1
                gift_list.append(f"{gift_name} {dots}")
            lines.append(f"    Taken: {', '.join(gift_list)}")
        
        # Show tribe gifts available
        if wolf_data['tribe_gifts']:
            tribe_gifts_str = ', '.join([g.title() for g in wolf_data['tribe_gifts']])
            lines.append(f"    Tribe Gifts: {tribe_gifts_str}")
        
        # Rites
        rite_dots = wolf_data['rite_dots']
        rites_from_merits = wolf_data['rites_from_merits']
        
        if rites_from_merits > 0:
            lines.append(f"  |wRites:|n        {rite_dots} dots (2 base + {rites_from_merits} from merits)")
        else:
            rite_color = '|g' if rite_dots >= 2 else '|y'
            lines.append(f"  |wRites:|n        {rite_color}{rite_dots}|n dots (need 2 base)")
        
        if wolf_data['rites']:
            rite_list = [f"{r}" for r in wolf_data['rites'].keys()]
            lines.append(f"    Taken: {', '.join(rite_list)}")
        
        # Primal Urge
        pu = wolf_data['primal_urge']
        pu_cost = wolf_data['pu_merit_cost']
        if pu_cost > 0:
            lines.append(f"  |wPrimal Urge:|n  {pu} (1 free + {pu - 1} from merits = {pu_cost} merit dots)")
        else:
            lines.append(f"  |wPrimal Urge:|n  {pu} (free dot)")
        
        # Required Merits
        totem_status = '|gok!|n' if wolf_data['has_totem'] else '|rx|n'
        first_tongue_status = '|gok!|n' if wolf_data['has_first_tongue'] else '|rx|n'
        lines.append(f"  |wTotem:|n        {totem_status}  (1 dot, free)")
        lines.append(f"  |wFirst Tongue:|n {first_tongue_status}  (Language Merit, free)")
        
        # Touchstone reminder
        lines.append(f"  |wTouchstones:|n  |y(Use +touchstone for Physical & Spiritual)|n")
    
    def _add_changeling_display(self, lines, changeling_data, divider_color):
        """Add changeling-specific chargen information to the display."""
        lines.append(f"  |m{'=' * 80}|n")
        lines.append(f"  |mCHANGELING TEMPLATE|n")
        lines.append(f"  |m{'=' * 80}|n")
        
        # Seeming and Kith
        seeming = changeling_data['seeming'].title() if changeling_data['seeming'] else '|rNot Set|n'
        kith = changeling_data['kith'].replace('_', ' ').title() if changeling_data['kith'] else '|yNone|n'
        lines.append(f"  |wSeeming:|n      {seeming}")
        lines.append(f"  |wKith:|n         {kith}")
        
        # Court
        court = changeling_data['court'].replace('_', ' ').title() if changeling_data['court'] else '|yNone (optional)|n'
        lines.append(f"  |wCourt:|n        {court}")
        
        # Favored Attribute (from seeming)
        if changeling_data['favored_attributes']:
            category = changeling_data['attribute_category']
            favored_options = changeling_data['favored_attributes']
            selected = changeling_data.get('favored_attr_used', None)
            
            if selected and selected in favored_options:
                favored_display = []
                for attr in favored_options:
                    if attr == selected:
                        favored_display.append(f"|g{attr.title()}|n |g[SELECTED]|n")
                    else:
                        favored_display.append(f"|x{attr.title()}|n")
                lines.append(f"  |wSeeming Bonus:|n {' or '.join(favored_display)} |c({category.title()})|n")
            else:
                favored_str = ' or '.join([a.title() for a in favored_options])
                lines.append(f"  |wSeeming Bonus:|n {favored_str} |rx|n |c({category.title()})|n")
                lines.append(f"    |y(Use +stat/favored <attribute> to select free dot)|n")
        
        # Needle and Thread
        needle_status = '|gok!|n' if changeling_data['has_needle'] else '|rx|n'
        thread_status = '|gok!|n' if changeling_data['has_thread'] else '|rx|n'
        lines.append(f"  |wNeedle:|n       {needle_status}    |wThread:|n {thread_status}")
        
        # Contracts
        common_taken = changeling_data['common_contracts']
        common_avail = changeling_data['contracts_available']
        royal_taken = changeling_data['royal_contracts']
        royal_avail = changeling_data['royal_available']
        
        contracts_color = '|g' if common_taken <= common_avail else '|r'
        royal_color = '|g' if royal_taken <= royal_avail else '|r'
        
        lines.append(f"  |wContracts:|n")
        lines.append(f"    Common:  {contracts_color}{common_taken}/{common_avail}|n (need 2 from favored)")
        lines.append(f"    Royal:   {royal_color}{royal_taken}/{royal_avail}|n")
        
        # Favored Regalia
        seeming_regalia = changeling_data.get('seeming_regalia', None)
        chosen_regalia = changeling_data.get('favored_regalia', None)
        
        regalia_parts = []
        if seeming_regalia:
            regalia_parts.append(f"|g{seeming_regalia.title()}|n (seeming)")
        
        if chosen_regalia:
            regalia_parts.append(f"|g{chosen_regalia.title()}|n (chosen)")
        else:
            regalia_parts.append('|yNone|n (chosen)')
        
        if regalia_parts:
            lines.append(f"    Favored Regalia: {', '.join(regalia_parts)}")
            if not chosen_regalia:
                lines.append(f"    |y(Use +stat favored regalia=<name> to choose 2nd)|n")
        
        # List contracts taken
        if changeling_data['contracts']:
            contract_list = []
            for contract_name in changeling_data['contracts'].keys():
                display_name = contract_name.replace('contract:', '').replace('_', ' ').title()
                contract_list.append(display_name)
            if contract_list:
                lines.append(f"    Taken: {', '.join(contract_list[:6])}")
                if len(contract_list) > 6:
                    lines.append(f"           {', '.join(contract_list[6:])}")
        
        # Wyrd
        wyrd = changeling_data['wyrd']
        wyrd_cost = changeling_data['wyrd_merit_cost']
        if wyrd_cost > 0:
            lines.append(f"  |wWyrd:|n         {wyrd} (1 free + {wyrd - 1} from merits = {wyrd_cost} merit dots)")
        else:
            lines.append(f"  |wWyrd:|n         {wyrd} (free dot)")
        
        # Mantle (free from court)
        if changeling_data['court']:
            if changeling_data['has_mantle']:
                mantle_dots = changeling_data['mantle_dots']
                if mantle_dots >= 1:
                    lines.append(f"  |wMantle:|n       {mantle_dots} dot{'s' if mantle_dots > 1 else ''} |g(1 free from court)|n")
                else:
                    lines.append(f"  |wMantle:|n       |yPresent but no dots set|n")
            else:
                lines.append(f"  |wMantle:|n       |rx|n |y(Get Mantle merit for court benefits)|n")
        
        # Touchstone reminder
        touchstone_status = '|g(Merit taken)|n' if changeling_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
        lines.append(f"    |c(Composure + 1 Clarity boxes)|n")
    
    def _add_mage_display(self, lines, mage_data, divider_color):
        """Add mage-specific chargen information to the display."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |bMAGE TEMPLATE|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Path and Order
        path = mage_data['path'].title() if mage_data['path'] else '|rNot Set|n'
        order = mage_data['order'].replace('_', ' ').title() if mage_data['order'] else '|yNone|n'
        lines.append(f"  |wPath:|n         {path}")
        lines.append(f"  |wOrder:|n        {order}")
        
        # Ruling and Inferior Arcana
        if mage_data['ruling_arcana']:
            ruling_str = ', '.join([a.title() for a in mage_data['ruling_arcana']])
            lines.append(f"  |wRuling Arcana:|n {ruling_str}")
        
        if mage_data['inferior_arcanum']:
            lines.append(f"  |wInferior:|n     {mage_data['inferior_arcanum'].title()}")
        
        # Rote Skills
        if mage_data['rote_skills']:
            rote_str = ', '.join([s.replace('_', ' ').title() for s in mage_data['rote_skills']])
            lines.append(f"  |wRote Skills:|n  {rote_str}")
        
        # Favored Attribute (Resistance: Composure, Resolve, Stamina)
        favored_options = ['Composure', 'Resolve', 'Stamina']
        selected = mage_data.get('favored_attr_used', None)
        
        if selected:
            favored_display = []
            for attr in favored_options:
                if attr.lower() == selected:
                    favored_display.append(f"|g{attr}|n |g[SELECTED]|n")
                else:
                    favored_display.append(f"|x{attr}|n")
            lines.append(f"  |wResistance Bonus:|n {' or '.join(favored_display)}")
        else:
            lines.append(f"  |wResistance Bonus:|n {' or '.join(favored_options)} |rx|n")
            lines.append(f"    |y(Use +stat/favored <attribute> to select free dot)|n")
        
        # Arcana
        arcana_dots = mage_data['arcana_dots']
        arcana_avail = mage_data['arcana_available']
        arcana_remaining = arcana_avail - arcana_dots
        arcana_color = '|g' if arcana_remaining >= 0 else '|r'
        
        lines.append(f"  |wArcana:|n       {arcana_color}{arcana_dots}/{arcana_avail}|n  (Remaining: {arcana_color}{arcana_remaining}|n)")
        
        # Arcana validations
        ruling_dots = mage_data['ruling_dots']
        ruling_color = '|g' if 3 <= ruling_dots <= 5 else '|r'
        lines.append(f"    Ruling:  {ruling_color}{ruling_dots}|n (need 3-5 dots in Ruling Arcana)")
        
        both_ruling_status = '|gok!|n' if mage_data['has_both_ruling'] else '|rx|n'
        lines.append(f"    Both Ruling have 1+: {both_ruling_status}")
        
        max_dots = mage_data['max_arcanum_dots']
        max_color = '|g' if max_dots <= 3 else '|r'
        lines.append(f"    Max in one: {max_color}{max_dots}|n (limit 3 dots)")
        
        if mage_data['has_inferior']:
            lines.append(f"    |rWarning: Cannot have dots in Inferior Arcanum ({mage_data['inferior_arcanum'].title()})|n")
        
        # List arcana taken
        if mage_data['arcana']:
            arcana_list = []
            for arcanum_name, dots in mage_data['arcana'].items():
                arcanum_lower = arcanum_name.lower().replace(' ', '_')
                # Mark ruling/inferior
                if arcanum_lower in mage_data['ruling_arcana']:
                    arcana_list.append(f"{arcanum_name.title()} {dots} |c(ruling)|n")
                elif arcanum_lower == mage_data['inferior_arcanum']:
                    arcana_list.append(f"{arcanum_name.title()} {dots} |r(inferior!)|n")
                else:
                    arcana_list.append(f"{arcanum_name.title()} {dots}")
            lines.append(f"    Taken: {', '.join(arcana_list)}")
        
        # Rotes
        rotes = mage_data['rotes_count']
        rotes_avail = mage_data['rotes_available']
        rotes_color = '|g' if rotes >= rotes_avail else '|y'
        lines.append(f"  |wRotes:|n        {rotes_color}{rotes}/{rotes_avail}|n")
        
        # Gnosis
        gnosis = mage_data['gnosis']
        gnosis_cost = mage_data['gnosis_merit_cost']
        if gnosis_cost > 0:
            lines.append(f"  |wGnosis:|n       {gnosis} (1 free + {gnosis - 1} from merits = {gnosis_cost} merit dots)")
        else:
            lines.append(f"  |wGnosis:|n       {gnosis} (free dot)")
        
        # Obsessions
        obs_count = mage_data['obsessions_count']
        obs_expected = mage_data['expected_obsessions']
        obs_color = '|g' if obs_count >= obs_expected else '|y'
        lines.append(f"  |wObsessions:|n   {obs_color}{obs_count}/{obs_expected}|n")
        if mage_data['obsessions']:
            for obs in mage_data['obsessions']:
                lines.append(f"    - {obs}")
        
        # Praxes
        prax_count = mage_data['praxes_count']
        prax_expected = mage_data['expected_praxes']
        prax_color = '|g' if prax_count >= prax_expected else '|y'
        lines.append(f"  |wPraxes:|n       {prax_color}{prax_count}/{prax_expected}|n  (1 per Gnosis)")
        if mage_data['praxes']:
            for prax in mage_data['praxes']:
                lines.append(f"    - {prax.replace('_', ' ').title()}")
        
        # Nimbus
        nimbus_status = '|gok!|n' if mage_data['has_immediate_nimbus'] else '|rx|n'
        lines.append(f"  |wNimbus:|n       {nimbus_status}  |y(Use +stat/mage nimbus to set)|n")
        
        # Dedicated Tool
        tool_status = '|gok!|n' if mage_data['has_dedicated_tool'] else '|rx|n'
        if mage_data['dedicated_tool']:
            lines.append(f"  |wDedicated Tool:|n {tool_status}  ({mage_data['dedicated_tool']})")
        else:
            lines.append(f"  |wDedicated Tool:|n {tool_status}  |y(Use +stat/mage dedicated_tool=<name>)|n")
        
        # Order Benefits
        if mage_data['order']:
            lines.append(f"  |wOrder Benefits:|n")
            
            # Occult skill
            occult_dots = mage_data['occult_dots']
            occult_status = '|gok!|n' if occult_dots >= 1 else '|rx|n'
            lines.append(f"    Occult:      {occult_status}  ({occult_dots} dot{'s' if occult_dots > 1 else ''}, need 1+)")
            
            # Order Status
            if mage_data['has_order_status']:
                status_dots = mage_data['order_status_dots']
                if status_dots >= 1:
                    lines.append(f"    Order Status: |gok!|n  ({status_dots} dot{'s' if status_dots > 1 else ''}, 1 free)")
                else:
                    lines.append(f"    Order Status: |yPresent but no dots set|n")
            else:
                lines.append(f"    Order Status: |rx|n  |y(Get Order Status merit)|n")
            
            # High Speech
            speech_status = '|gok!|n' if mage_data['has_high_speech'] else '|rx|n'
            lines.append(f"    High Speech:  {speech_status}  (Language Merit, free)")
    
    def _add_deviant_display(self, lines, deviant_data, divider_color):
        """Add deviant-specific chargen information to the display."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rDEVIANT TEMPLATE|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Origin and Clade
        origin_name = deviant_data.get('origin_name', 'Unknown')
        clade_display = deviant_data['clade_display'] if deviant_data['clade_display'] else '|rNot Set|n'
        lines.append(f"  |wOrigin:|n       {origin_name}")
        lines.append(f"  |wClade:|n        {clade_display}")
        
        # Forms (optional)
        if deviant_data['form']:
            forms_str = ', '.join([f.replace('_', ' ').title() for f in deviant_data['form']])
            lines.append(f"  |wForm:|n         {forms_str}")
        
        # Origin bonus
        bonus_type = deviant_data.get('origin_bonus_type', None)
        bonus_stat = deviant_data.get('origin_bonus_stat', None)
        if bonus_type and bonus_stat:
            if bonus_type == 'any':
                lines.append(f"  |wOrigin Bonus:|n  1 Scar-free Magnitude (any Variation)")
            else:
                lines.append(f"  |wOrigin Bonus:|n  1 Scar-free Magnitude ({bonus_type.title()} Variation)")
            
            if bonus_stat == 'choice':
                lines.append(f"                 +1 Loyalty or Conviction (your choice)")
            else:
                lines.append(f"                 +1 {bonus_stat.title()}")
        
        # Variations
        var_mag = deviant_data['variation_magnitude']
        lines.append(f"  |wVariations:|n   {var_mag} Magnitude total")
        
        if deviant_data['variations']:
            var_list = []
            for var_name, magnitude in deviant_data['variations'].items():
                # Remove prefix for display
                display_name = var_name.replace('variation:', '').replace('_', ' ').title()
                var_list.append(f"{display_name} {magnitude}")
            
            # Display variations
            lines.append(f"    |c(At least half from Clade or Universal)|n")
            for var in var_list:
                lines.append(f"    - {var}")
        else:
            lines.append(f"    |yNo variations set yet|n")
        
        # Scars
        scar_mag = deviant_data['scar_magnitude']
        lines.append(f"  |wScars:|n        {scar_mag} Magnitude total")
        lines.append(f"    |c(Each Variation needs matching Scar)|n")
        
        if deviant_data['scars']:
            scar_list = []
            for scar_name, magnitude in deviant_data['scars'].items():
                # Remove prefix for display
                display_name = scar_name.replace('scar:', '').replace('_', ' ').title()
                scar_list.append(f"{display_name} {magnitude}")
            
            for scar in scar_list:
                lines.append(f"    - {scar}")
        else:
            lines.append(f"    |yNo scars set yet|n")
        
        # Loyalty and Conviction
        loyalty = deviant_data['loyalty']
        conviction = deviant_data['conviction']
        
        # Loyalty Touchstones
        loyalty_ts = deviant_data['loyalty_touchstones']
        loyalty_needed = deviant_data['loyalty_touchstones_needed']
        loyalty_count = len(loyalty_ts)
        loyalty_color = '|g' if loyalty_count >= loyalty_needed else '|r'
        
        lines.append(f"  |wLoyalty:|n      {loyalty} ({loyalty_color}{loyalty_count}/{loyalty_needed}|n Touchstones)")
        if loyalty_ts:
            for ts in loyalty_ts:
                lines.append(f"    - {ts}")
        elif loyalty_needed > 0:
            lines.append(f"    |y(Use +touchstone to add)|n")
        
        # Conviction Touchstones
        conviction_ts = deviant_data['conviction_touchstones']
        conviction_needed = deviant_data['conviction_touchstones_needed']
        conviction_count = len(conviction_ts)
        conviction_color = '|g' if conviction_count >= conviction_needed else '|r'
        
        lines.append(f"  |wConviction:|n   {conviction} ({conviction_color}{conviction_count}/{conviction_needed}|n Touchstones)")
        if conviction_ts:
            for ts in conviction_ts:
                lines.append(f"    - {ts}")
        elif conviction_needed > 0:
            lines.append(f"    |y(Use +touchstone to add)|n")
        
        # Acclimation
        acclimation = deviant_data['acclimation']
        acclimation_cost = deviant_data['acclimation_merit_cost']
        if acclimation_cost > 0:
            lines.append(f"  |wAcclimation:|n  {acclimation} ({acclimation_cost} merit dots)")
        else:
            lines.append(f"  |wAcclimation:|n  {acclimation} (starts at 0)")
    
    def _add_geist_display(self, lines, geist_data, divider_color):
        """Add Sin-Eater/Geist-specific chargen information to the display."""
        lines.append(f"  |g{'=' * 80}|n")
        lines.append(f"  |gSIN-EATER TEMPLATE|n")
        lines.append(f"  |g{'=' * 80}|n")
        
        # Burden
        burden = geist_data['burden'].title() if geist_data['burden'] else '|rNot Set|n'
        lines.append(f"  |wBurden:|n       {burden}")
        
        # Haunt Affinities
        if geist_data['haunt_affinities']:
            affinity_str = ', '.join([h.title() for h in geist_data['haunt_affinities']])
            lines.append(f"  |wHaunt Affinity:|n {affinity_str}")
        
        # Root and Bloom
        root_status = '|gok!|n' if geist_data['has_root'] else '|rx|n'
        bloom_status = '|gok!|n' if geist_data['has_bloom'] else '|rx|n'
        lines.append(f"  |wRoot:|n         {root_status}    |wBloom:|n {bloom_status}")
        
        # Haunts
        haunt_dots = geist_data['haunt_dots']
        haunt_avail = geist_data['haunt_available']
        haunt_remaining = haunt_avail - haunt_dots
        haunt_color = '|g' if haunt_remaining >= 0 else '|r'
        
        lines.append(f"  |wHaunts:|n       {haunt_color}{haunt_dots}/{haunt_avail}|n  (Remaining: {haunt_color}{haunt_remaining}|n)")
        
        # Affinity check
        affinity_dots = geist_data['affinity_dots']
        affinity_status = '|g' if affinity_dots >= 2 else '|r'
        lines.append(f"    Affinity:  {affinity_status}{affinity_dots}|n (need at least 2 in affinity Haunts)")
        
        # List haunts taken
        if geist_data['haunts']:
            haunt_list = []
            for haunt_name, dots in geist_data['haunts'].items():
                haunt_lower = haunt_name.lower().replace(' ', '_')
                # Mark if affinity
                if haunt_lower in geist_data['haunt_affinities']:
                    haunt_list.append(f"{haunt_name.title()} {dots} |c(affinity)|n")
                else:
                    haunt_list.append(f"{haunt_name.title()} {dots}")
            lines.append(f"    Taken: {', '.join(haunt_list)}")
        
        # Key
        key_status = '|gok!|n' if geist_data['has_key'] else '|rx|n'
        if geist_data['keys']:
            key_names = ', '.join([k.replace('key:', '').replace('_', ' ').title() for k in geist_data['keys']])
            lines.append(f"  |wKey:|n          {key_status}  ({key_names})")
        else:
            lines.append(f"  |wKey:|n          {key_status}  |y(Reflects death circumstances)|n")
        
        # Ceremonies
        ceremony_count = geist_data['ceremonies_count']
        if ceremony_count > 0:
            lines.append(f"  |wCeremonies:|n   {ceremony_count}")
            for ceremony in geist_data['ceremonies']:
                ceremony_name = ceremony.replace('ceremony:', '').replace('_', ' ').title()
                lines.append(f"    - {ceremony_name}")
        
        # Synergy
        synergy = geist_data['synergy']
        synergy_cost = geist_data['synergy_merit_cost']
        if synergy_cost > 0:
            lines.append(f"  |wSynergy:|n      {synergy} (1 free + {synergy - 1} from merits = {synergy_cost} merit dots)")
        else:
            lines.append(f"  |wSynergy:|n      {synergy} (free dot)")
        
        # Free Merit
        tolerance_status = '|gok!|n' if geist_data['has_tolerance_biology'] else '|rx|n'
        lines.append(f"  |wTolerance for Biology:|n {tolerance_status}  (free merit)")
        
        # Touchstone
        touchstone_status = '|g(Merit taken)|n' if geist_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
        
        # Geist companion section
        lines.append(f"\n  |y{'~' * 80}|n")
        lines.append(f"  |yGEIST COMPANION|n")
        lines.append(f"  |y{'~' * 80}|n")
        
        # Geist Name
        name_status = '|gok!|n' if geist_data['has_geist_name'] else '|rx|n'
        if geist_data['geist_name']:
            lines.append(f"  |wName/Title:|n   {name_status}  {geist_data['geist_name']}")
        else:
            lines.append(f"  |wName/Title:|n   {name_status}  |y(Use +stat/geist geist_name=<title>)|n")
        
        # Geist Attributes
        geist_spent = geist_data['geist_attr_spent']
        geist_avail = geist_data['geist_attr_available']
        geist_remaining = geist_avail - geist_spent
        geist_color = '|g' if geist_remaining >= 0 else '|r'
        
        lines.append(f"  |wAttributes:|n   {geist_color}{geist_spent}/{geist_avail}|n  (Power/Finesse/Resistance)")
        
        power = geist_data['geist_power']
        finesse = geist_data['geist_finesse']
        resistance = geist_data['geist_resistance']
        lines.append(f"    Power: {power}, Finesse: {finesse}, Resistance: {resistance} (max 9 each)")
        
        # Geist Virtue and Vice
        virtue_status = '|gok!|n' if geist_data['has_geist_virtue'] else '|rx|n'
        vice_status = '|gok!|n' if geist_data['has_geist_vice'] else '|rx|n'
        
        if geist_data['geist_virtue']:
            lines.append(f"  |wVirtue:|n       {virtue_status}  {geist_data['geist_virtue']}")
        else:
            lines.append(f"  |wVirtue:|n       {virtue_status}  |y(Use +stat/geist virtue=<name>)|n")
        
        if geist_data['geist_vice']:
            lines.append(f"  |wVice:|n         {vice_status}  {geist_data['geist_vice']}")
        else:
            lines.append(f"  |wVice:|n         {vice_status}  |y(Use +stat/geist vice=<name>)|n")
        
        # Remembrance
        remembrance_status = '|gok!|n' if geist_data['has_remembrance'] else '|rx|n'
        lines.append(f"  |wRemembrance:|n  {remembrance_status}  |y(Memory image, use +stat/geist)|n")
        
        # Remembrance Trait
        trait_status = '|gok!|n' if geist_data['has_remembrance_trait'] else '|rx|n'
        if geist_data['remembrance_trait']:
            lines.append(f"  |wRemembrance Trait:|n {trait_status}  {geist_data['remembrance_trait']}")
        else:
            lines.append(f"  |wRemembrance Trait:|n {trait_status}  |y(Skill or Merit ≤3)|n")
        
        # Crisis Point
        crisis_status = '|gok!|n' if geist_data['has_crisis_point'] else '|rx|n'
        if geist_data['crisis_point']:
            lines.append(f"  |wCrisis Point:|n {crisis_status}  {geist_data['crisis_point']}")
        else:
            lines.append(f"  |wCrisis Point:|n {crisis_status}  |y(Use +stat/geist crisis_point=<trigger>)|n")
        
        # Geist Rank
        rank = geist_data['geist_rank']
        lines.append(f"  |wRank:|n         {rank} (3 default, higher with Dread Geist merit)")
        
        # Ban and Bane
        ban_status = '|gok!|n' if geist_data['has_ban'] else '|rx|n'
        bane_status = '|gok!|n' if geist_data['has_bane'] else '|rx|n'
        
        if geist_data['geist_ban']:
            lines.append(f"  |wBan:|n          {ban_status}  {geist_data['geist_ban']}")
        else:
            lines.append(f"  |wBan:|n          {ban_status}  |y(Use +stat/geist ban=<restriction>)|n")
        
        if geist_data['geist_bane']:
            lines.append(f"  |wBane:|n         {bane_status}  {geist_data['geist_bane']}")
        else:
            lines.append(f"  |wBane:|n         {bane_status}  |y(Use +stat/geist bane=<weakness>)|n")
        
        # Innate Key
        key_status = '|gok!|n' if geist_data['has_innate_key'] else '|rx|n'
        if geist_data['innate_key']:
            lines.append(f"  |wInnate Key:|n   {key_status}  {geist_data['innate_key']}")
        else:
            lines.append(f"  |wInnate Key:|n   {key_status}  |y(Use +stat/geist innate_key=<key>)|n")
    
    def _add_hunter_display(self, lines, hunter_data, divider_color):
        """Add Hunter-specific chargen information to the display."""
        lines.append(f"  |y{'=' * 80}|n")
        lines.append(f"  |yHUNTER TEMPLATE|n")
        lines.append(f"  |y{'=' * 80}|n")
        
        # Tier and Organization
        tier = hunter_data['tier']
        org_type = hunter_data['org_type'] if hunter_data['org_type'] else 'Unknown'
        lines.append(f"  |wTier:|n         {tier} ({org_type})")
        
        if tier == 1:
            # Tier 1: Individual cell
            profession = hunter_data.get('profession', '')
            if profession:
                lines.append(f"  |wProfession:|n   {profession.replace('_', ' ').title()}")
            lines.append(f"  |wCell:|n         Independent (no formal organization)")
        else:
            # Tier 2+: Compact or Conspiracy
            organization = hunter_data['organization']
            if organization:
                lines.append(f"  |w{org_type}:|n      {organization.replace('_', ' ').title()}")
            else:
                lines.append(f"  |w{org_type}:|n      |rNot Set|n")
        
        # Tactics (all tiers get 3)
        tactics = hunter_data['tactics']
        tactics_count = hunter_data['tactics_count']
        expected_tactics = hunter_data['expected_tactics']
        tactics_color = '|g' if tactics_count >= expected_tactics else '|r'
        
        lines.append(f"  |wTactics:|n      {tactics_color}{tactics_count}/{expected_tactics}|n  (cell favored tactics)")
        if tactics:
            for tactic in tactics:
                lines.append(f"    - {tactic.replace('_', ' ').title()}")
        else:
            lines.append(f"    |y(Use +stat tactics=<tactic1,tactic2,tactic3>)|n")
        
        lines.append(f"    |c(Gain 8-again when performing these tactics)|n")
        
        # Status (Tier 2+ only)
        if tier >= 2:
            if hunter_data['has_status']:
                status_dots = hunter_data['status_dots']
                if status_dots >= 1:
                    lines.append(f"  |w{org_type} Status:|n |gok!|n  ({status_dots} dot{'s' if status_dots > 1 else ''}, 1 free)")
                else:
                    lines.append(f"  |w{org_type} Status:|n |yPresent but no dots set|n")
            else:
                lines.append(f"  |w{org_type} Status:|n |rx|n  |y(Get Status merit, 1 free)|n")
        
        # Endowments (Tier 3 only)
        if tier == 3:
            endowments = hunter_data['endowments']
            endowments_count = hunter_data['endowments_count']
            expected_endowments = hunter_data['expected_endowments']
            endowments_color = '|g' if endowments_count >= expected_endowments else '|r'
            
            lines.append(f"  |wEndowments:|n   {endowments_color}{endowments_count}/{expected_endowments}|n  (conspiracy powers)")
            if endowments:
                for endowment in endowments:
                    endowment_name = endowment.replace('endowment:', '').replace('_', ' ').title()
                    lines.append(f"    - {endowment_name}")
            else:
                lines.append(f"    |y(Use +stat endowment:<name>=known)|n")
    
    def _add_mummy_display(self, lines, mummy_data, divider_color):
        """Add Mummy/Arisen-specific chargen information to the display."""
        lines.append(f"  |y{'=' * 80}|n")
        lines.append(f"  |yMUMMY (ARISEN) TEMPLATE|n")
        lines.append(f"  |y{'=' * 80}|n")
        
        # Decree, Guild, Judge
        decree_name = mummy_data.get('decree_name', 'Unknown')
        guild = mummy_data['guild'].replace('_', ' ').title() if mummy_data['guild'] else '|rNot Set|n'
        judge = mummy_data['judge'].replace('_', ' ').title() if mummy_data['judge'] else '|yNone|n'
        
        lines.append(f"  |wDecree:|n       {decree_name}")
        lines.append(f"  |wGuild:|n        {guild}")
        if mummy_data['guild_vessel']:
            lines.append(f"    Vessel: {mummy_data['guild_vessel']}")
        lines.append(f"  |wJudge:|n        {judge}")
        
        # Balance and Burden (Mummy's anchors)
        balance_status = '|gok!|n' if mummy_data['has_balance'] else '|rx|n'
        burden_status = '|gok!|n' if mummy_data['has_burden'] else '|rx|n'
        lines.append(f"  |wBalance:|n      {balance_status}    |wBurden:|n {burden_status}")
        lines.append(f"    |c(Mummy's Virtue/Vice equivalents)|n")
        
        # Pillars
        pillar_total = mummy_data['pillar_total']
        pillar_avail = mummy_data['pillar_available']
        pillar_remaining = pillar_avail - pillar_total
        pillar_color = '|g' if pillar_remaining >= 0 else '|r'
        
        lines.append(f"  |wPillars:|n      {pillar_color}{pillar_total}/{pillar_avail}|n  (5 aspects of soul)")
        
        # Show pillar breakdown
        pillars = mummy_data['pillars']
        defining_pillar = mummy_data['defining_pillar']
        pillar_parts = []
        
        for pillar_name in ['ab', 'ba', 'ka', 'ren', 'sheut']:
            dots = pillars.get(pillar_name, 0)
            if dots > 0:
                # Mark defining pillar
                if pillar_name == defining_pillar:
                    pillar_parts.append(f"{pillar_name.title()} {dots} |c(defining)|n")
                else:
                    pillar_parts.append(f"{pillar_name.title()} {dots}")
        
        if pillar_parts:
            lines.append(f"    {', '.join(pillar_parts)}")
        
        # Validation: defining pillar must be highest
        if not mummy_data['defining_pillar_is_highest'] and defining_pillar:
            lines.append(f"    |rWarning: {defining_pillar.title()} (defining) must be highest|n")
        
        # Affinities
        affinities_count = mummy_data['affinities_count']
        expected_affinities = mummy_data['expected_affinities']
        affinity_color = '|g' if affinities_count >= expected_affinities else '|r'
        
        lines.append(f"  |wAffinities:|n   {affinity_color}{affinities_count}/{expected_affinities}|n")
        lines.append(f"    |c(1 decree + 1 guild + 2 soul)|n")
        
        if mummy_data['decree_affinity']:
            affinity_display = mummy_data['decree_affinity'].replace('_', ' ').title()
            lines.append(f"    Decree: {affinity_display} (automatic)")
        
        if mummy_data['affinities']:
            for affinity in mummy_data['affinities']:
                affinity_name = affinity.replace('affinity:', '').replace('_', ' ').title()
                lines.append(f"    - {affinity_name}")
        
        # Utterances
        utterances_count = mummy_data['utterances_count']
        expected_utterances = mummy_data['expected_utterances']
        utterance_color = '|g' if utterances_count >= expected_utterances else '|r'
        
        lines.append(f"  |wUtterances:|n   {utterance_color}{utterances_count}/{expected_utterances}|n")
        
        dreams_status = '|gok!|n' if mummy_data['has_dreams_of_dead_gods'] else '|rx|n'
        lines.append(f"    Dreams of Dead Gods: {dreams_status} (automatic)")
        
        if mummy_data['utterances']:
            for utterance in mummy_data['utterances']:
                if 'dreams' not in utterance.lower():
                    utterance_name = utterance.replace('utterance:', '').replace('_', ' ').title()
                    lines.append(f"    - {utterance_name}")
        
        # Memory and Sekhem
        memory = mummy_data['memory']
        sekhem = mummy_data['sekhem']
        lines.append(f"  |wMemory:|n       {memory} (starts at 3)")
        lines.append(f"  |wSekhem:|n       {sekhem} (starts at 8-10 based on awakening)")
        
        # Free Merits
        cult_status = '|gok!|n' if mummy_data['has_cult'] else '|rx|n'
        tomb_status = '|gok!|n' if mummy_data['has_tomb'] else '|rx|n'
        
        cult_dots = mummy_data['cult_dots']
        tomb_dots = mummy_data['tomb_dots']
        
        if cult_dots >= 1:
            lines.append(f"  |wCult:|n         {cult_status}  ({cult_dots} dot{'s' if cult_dots > 1 else ''}, 1 free)")
        else:
            lines.append(f"  |wCult:|n         {cult_status}  |y(Get Cult merit, 1 free)|n")
        
        if tomb_dots >= 1:
            lines.append(f"  |wTomb:|n         {tomb_status}  ({tomb_dots} dot{'s' if tomb_dots > 1 else ''}, 1 free)")
        else:
            lines.append(f"  |wTomb:|n         {tomb_status}  |y(Get Tomb merit, 1 free)|n")
        
        # Touchstone
        lines.append(f"  |wTouchstone:|n   |y(Use +touchstone, need 1)|n")
    
    def _add_promethean_display(self, lines, promethean_data, divider_color):
        """Add Promethean-specific chargen information to the display."""
        lines.append(f"  |c{'=' * 80}|n")
        lines.append(f"  |cPROMETHEAN TEMPLATE|n")
        lines.append(f"  |c{'=' * 80}|n")
        
        # Lineage and Refinement
        lineage = promethean_data['lineage'].title() if promethean_data['lineage'] else '|rNot Set|n'
        refinement = promethean_data['refinement'].title() if promethean_data['refinement'] else '|rNot Set|n'
        role = promethean_data['role'].replace('_', ' ').title() if promethean_data['role'] else '|yNone|n'
        
        lines.append(f"  |wLineage:|n      {lineage}")
        lines.append(f"  |wRefinement:|n   {refinement}")
        if promethean_data['role']:
            lines.append(f"  |wRole:|n         {role}")
        
        # Elpis and Torment
        elpis_status = '|gok!|n' if promethean_data['has_elpis'] else '|rx|n'
        torment_status = '|gok!|n' if promethean_data['has_torment'] else '|rx|n'
        lines.append(f"  |wElpis:|n        {elpis_status}    |wTorment:|n {torment_status}")
        
        # Bestowment
        bestowment_status = '|gok!|n' if promethean_data['has_bestowment'] else '|rx|n'
        
        if promethean_data['bestowments']:
            bestowment_names = ', '.join([b.replace('bestowment:', '').replace('_', ' ').title() for b in promethean_data['bestowments']])
            lines.append(f"  |wBestowment:|n   {bestowment_status}  {bestowment_names}")
        else:
            lines.append(f"  |wBestowment:|n   {bestowment_status}")
            if promethean_data['bestowment_options']:
                options_str = ' or '.join(promethean_data['bestowment_options'])
                lines.append(f"    Options: {options_str}")
        
        # Transmutations/Alembics
        alembics_count = promethean_data['alembics_count']
        expected_alembics = promethean_data['expected_alembics']
        alembic_color = '|g' if alembics_count >= expected_alembics else '|r'
        
        lines.append(f"  |wAlembics:|n     {alembic_color}{alembics_count}/{expected_alembics}|n  (manifestations of transmutations)")
        
        # Show refinement transmutations
        if promethean_data['refinement_transmutations']:
            trans_str = ', '.join([t.title() for t in promethean_data['refinement_transmutations']])
            lines.append(f"    Refinement grants: {trans_str}")
        
        # List alembics taken
        if promethean_data['alembics']:
            alembic_list = []
            for alembic in promethean_data['alembics']:
                alembic_name = alembic.replace('alembic:', '').replace('_', ' ').title()
                alembic_list.append(alembic_name)
            lines.append(f"    Taken: {', '.join(alembic_list)}")
        
        # List transmutations (if any are set as powers)
        if promethean_data['transmutations']:
            trans_list = []
            for trans_name, dots in promethean_data['transmutations'].items():
                trans_list.append(f"{trans_name.title()} {dots}")
            if trans_list:
                lines.append(f"    Transmutations: {', '.join(trans_list)}")
        
        # Azoth and Pyros
        azoth = promethean_data['azoth']
        pyros = promethean_data['pyros']
        max_pyros = promethean_data['max_pyros']
        
        lines.append(f"  |wAzoth:|n        {azoth} (starts at 1, Divine Fire strength)")
        lines.append(f"  |wPyros:|n        {pyros}/{max_pyros} (fuel, starts at half max)")
        
        # Pilgrimage
        pilgrimage = promethean_data['pilgrimage']
        lines.append(f"  |wPilgrimage:|n   {pilgrimage} (progress toward humanity, starts at 1)")
        
        # Touchstone
        touchstone_status = '|g(Merit taken)|n' if promethean_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
        lines.append(f"    |c(1 associated with Role/Pilgrimage)|n")
        
        # Pilgrimage Questions reminder
        lines.append(f"\n  |cPilgrimage Questions:|n |y(Use +bio to answer)|n")
        lines.append(f"    - What sort of human do you want to be?")
        lines.append(f"    - How have humans taught you to fear and hate?")
        lines.append(f"    - How did you split with your creator?")
        lines.append(f"    - What keeps you on the Pilgrimage?")
        lines.append(f"    - What would you give up to become human?")
    
    def _add_mortalplus_display(self, lines, mortalplus_data, divider_color):
        """Add Mortal+ template-specific chargen information to the display."""
        template_type = mortalplus_data.get('template_type', '').lower()
        
        if template_type == 'ghoul':
            self._add_ghoul_display(lines, mortalplus_data, divider_color)
        elif template_type == 'revenant':
            self._add_revenant_display(lines, mortalplus_data, divider_color)
        elif template_type == 'dhampir':
            self._add_dhampir_display(lines, mortalplus_data, divider_color)
        elif template_type in ['wolf-blooded', 'wolf_blooded', 'wolfblooded']:
            self._add_wolfblooded_display(lines, mortalplus_data, divider_color)
        elif template_type == 'psychic':
            self._add_psychic_display(lines, mortalplus_data, divider_color)
        elif template_type == 'atariya':
            self._add_atariya_display(lines, mortalplus_data, divider_color)
        elif template_type == 'infected':
            self._add_infected_display(lines, mortalplus_data, divider_color)
        elif template_type == 'plain':
            self._add_plain_display(lines, mortalplus_data, divider_color)
        elif template_type in ['lost_boy', 'lost boy']:
            self._add_lostboy_display(lines, mortalplus_data, divider_color)
        elif template_type in ['psychic_vampire', 'psychic vampire']:
            self._add_psychicvampire_display(lines, mortalplus_data, divider_color)
        elif template_type in ['immortal', 'endless']:
            self._add_immortal_display(lines, mortalplus_data, divider_color)
        elif template_type == 'proximus':
            self._add_proximus_display(lines, mortalplus_data, divider_color)
        elif template_type == 'sleepwalker':
            self._add_sleepwalker_display(lines, mortalplus_data, divider_color)
        elif template_type in ['fae-touched', 'fae_touched', 'faetouched']:
            self._add_faetouched_display(lines, mortalplus_data, divider_color)
        else:
            # Generic Mortal+ display
            lines.append(f"  |w{'=' * 80}|n")
            lines.append(f"  |wMORTAL+ TEMPLATE|n")
            lines.append(f"  |w{'=' * 80}|n")
            if template_type:
                lines.append(f"  |wType:|n         {template_type.replace('_', ' ').title()}")
            else:
                lines.append(f"  |wType:|n         |rNot Set|n")
                lines.append(f"    |y(Use +stat template_type=<type>)|n")
    
    def _add_ghoul_display(self, lines, ghoul_data, divider_color):
        """Add Ghoul-specific chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rGHOUL (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Regnant's Clan
        clan = ghoul_data['clan'].title() if ghoul_data['clan'] else '|rNot Set|n'
        lines.append(f"  |wRegnant Clan:|n {clan}")
        
        # Blood Potency
        bp = ghoul_data['blood_potency']
        lines.append(f"  |wBlood Potency:|n {bp} (always 0, cannot increase)")
        
        # Disciplines
        disc_dots = ghoul_data['discipline_dots']
        disc_avail = ghoul_data['discipline_available']
        disc_remaining = disc_avail - disc_dots
        disc_color = '|g' if disc_remaining >= 0 else '|r'
        
        lines.append(f"  |wDisciplines:|n  {disc_color}{disc_dots}/{disc_avail}|n (from regnant's in-clan)")
        
        if ghoul_data['disciplines']:
            disc_list = []
            for disc_name, dots in ghoul_data['disciplines'].items():
                disc_lower = disc_name.lower().replace(' ', '_')
                if disc_lower in ghoul_data['in_clan_disciplines']:
                    disc_list.append(f"{disc_name.title()} {dots} |c(in-clan)|n")
                else:
                    disc_list.append(f"{disc_name.title()} {dots}")
            lines.append(f"    Taken: {', '.join(disc_list)}")
    
    def _add_revenant_display(self, lines, revenant_data, divider_color):
        """Add Revenant-specific chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rREVENANT (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Family Clan
        clan = revenant_data['clan'].title() if revenant_data['clan'] else '|yNone|n'
        lines.append(f"  |wFamily Clan:|n  {clan}")
        
        # Blood Potency
        bp = revenant_data['blood_potency']
        lines.append(f"  |wBlood Potency:|n {bp} (1 for revenants, cannot increase)")
        
        # Mask, Dirge, Touchstone
        mask_status = '|gok!|n' if revenant_data['has_mask'] else '|rx|n'
        dirge_status = '|gok!|n' if revenant_data['has_dirge'] else '|rx|n'
        lines.append(f"  |wMask:|n         {mask_status}    |wDirge:|n {dirge_status}")
        
        touchstone_status = '|g(Merit taken)|n' if revenant_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
        
        # Disciplines
        disc_dots = revenant_data['discipline_dots']
        disc_avail = revenant_data['discipline_available']
        disc_remaining = disc_avail - disc_dots
        disc_color = '|g' if disc_remaining >= 0 else '|r'
        
        phys_dots = revenant_data['physical_discipline_dots']
        phys_status = '|g' if phys_dots >= 1 else '|r'
        
        lines.append(f"  |wDisciplines:|n  {disc_color}{disc_dots}/{disc_avail}|n")
        lines.append(f"    Physical: {phys_status}{phys_dots}|n (need at least 1)")
        lines.append(f"    |c(No unique clan disciplines)|n")
        
        if revenant_data['disciplines']:
            disc_list = []
            for disc_name, dots in revenant_data['disciplines'].items():
                disc_list.append(f"{disc_name.title()} {dots}")
            lines.append(f"    Taken: {', '.join(disc_list)}")
    
    def _add_dhampir_display(self, lines, dhampir_data, divider_color):
        """Add Dhampir-specific chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rDHAMPIR (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Parent Clan
        parent_clan = dhampir_data['parent_clan'].title() if dhampir_data['parent_clan'] else '|rNot Set|n'
        lines.append(f"  |wParent Clan:|n  {parent_clan}")
        
        # Destiny, Doom, Affliction
        destiny = dhampir_data['destiny'] if dhampir_data['destiny'] else '|yNone|n'
        doom = dhampir_data['doom'] if dhampir_data['doom'] else '|yNone|n'
        affliction = dhampir_data['affliction'] if dhampir_data['affliction'] else '|yNone|n'
        
        lines.append(f"  |wDestiny:|n      {destiny}")
        lines.append(f"  |wDoom:|n         {doom}")
        lines.append(f"  |wAffliction:|n   {affliction}")
        
        # Required Merits
        blood_sense_status = '|gok!|n' if dhampir_data['has_blood_sense'] else '|rx|n'
        omen_status = '|gok!|n' if dhampir_data['has_omen_sensitivity'] else '|rx|n'
        fate_status = '|gok!|n' if dhampir_data['has_thief_of_fate'] else '|rx|n'
        
        lines.append(f"  |wBlood Sense:|n  {blood_sense_status}  (free merit)")
        lines.append(f"  |wOmen Sensitivity:|n {omen_status}  (free merit)")
        lines.append(f"  |wThief of Fate:|n {fate_status}  (free merit)")
        
        # Themes
        if dhampir_data['parent_themes']:
            themes_str = ', '.join([t.title() for t in dhampir_data['parent_themes']])
            themes_status = '|gok!|n' if dhampir_data['parent_themes_set'] else '|rx|n'
            lines.append(f"  |wClan Themes:|n  {themes_status}  ({themes_str})")
            lines.append(f"    |c(1 dot each in parent clan themes)|n")
        
        # Twists
        twist_dots = dhampir_data['twist_dots']
        twist_avail = dhampir_data['twist_available']
        twist_remaining = twist_avail - twist_dots
        twist_color = '|g' if twist_remaining >= 0 else '|r'
        
        lines.append(f"  |wTwists:|n       {twist_color}{twist_dots}/{twist_avail}|n (free dots + clan unique)")
        
        if dhampir_data['twists']:
            twist_list = []
            for twist_name, dots in dhampir_data['twists'].items():
                display_name = twist_name.replace('twist:', '').replace('_', ' ').title()
                twist_list.append(f"{display_name} {dots}")
            lines.append(f"    Taken: {', '.join(twist_list)}")
        
        # Malisons (optional)
        if dhampir_data['malisons']:
            malison_list = [m.replace('malison:', '').replace('_', ' ').title() for m in dhampir_data['malisons']]
            lines.append(f"  |wMalisons:|n     {len(malison_list)} (3 merit dots each)")
            for malison in malison_list:
                lines.append(f"    - {malison}")
    
    def _add_wolfblooded_display(self, lines, wolfblooded_data, divider_color):
        """Add Wolf-Blooded-specific chargen information."""
        lines.append(f"  |c{'=' * 80}|n")
        lines.append(f"  |cWOLF-BLOODED (MORTAL+)|n")
        lines.append(f"  |c{'=' * 80}|n")
        
        # Tell
        tell = wolfblooded_data['tell'].replace('_', ' ').title() if wolfblooded_data['tell'] else '|rNot Set|n'
        tell_status = '|gok!|n' if wolfblooded_data['has_tell'] else '|rx|n'
        
        lines.append(f"  |wTell:|n         {tell_status}  {tell}")
        lines.append(f"    |c(Inherited trait from werewolf ancestry)|n")
    
    def _add_psychic_display(self, lines, psychic_data, divider_color):
        """Add Psychic-specific chargen information."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |bPSYCHIC (MORTAL+)|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Psychic Merits
        merit_count = len(psychic_data['psychic_merits'])
        merit_dots = psychic_data['psychic_merit_dots']
        
        if merit_count > 0:
            lines.append(f"  |wPsychic Merits:|n {merit_count} merits ({merit_dots} dots total)")
            for merit in psychic_data['psychic_merits']:
                lines.append(f"    - {merit}")
        else:
            lines.append(f"  |wPsychic Merits:|n |yNone purchased yet|n")
            lines.append(f"    |c(Purchase psychic merits like Telepathy, Telekinesis, etc.)|n")
    
    def _add_atariya_display(self, lines, atariya_data, divider_color):
        """Add Atariya-specific chargen information."""
        lines.append(f"  |y{'=' * 80}|n")
        lines.append(f"  |yATARIYA (MORTAL+)|n")
        lines.append(f"  |y{'=' * 80}|n")
        
        # Damn Lucky Merit
        damn_lucky_status = '|gok!|n' if atariya_data['has_damn_lucky'] else '|rx|n'
        lines.append(f"  |wDamn Lucky:|n   {damn_lucky_status}  (required merit)")
        lines.append(f"    |c(Caught attention of luck itself)|n")
    
    def _add_infected_display(self, lines, infected_data, divider_color):
        """Add Infected-specific chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rINFECTED (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Carrier Merit
        carrier_status = '|gok!|n' if infected_data['has_carrier'] else '|rx|n'
        lines.append(f"  |wCarrier:|n      {carrier_status}  (1 dot, free)")
        lines.append(f"  |wCondition:|n    Latent Symptoms (starts with this)")
        lines.append(f"    |c(Disease that doesn't behave normally)|n")
    
    def _add_plain_display(self, lines, plain_data, divider_color):
        """Add Plain-specific chargen information."""
        lines.append(f"  |w{'=' * 80}|n")
        lines.append(f"  |wPLAIN (MORTAL+)|n")
        lines.append(f"  |w{'=' * 80}|n")
        
        # Plain Reader Merit
        reader_status = '|gok!|n' if plain_data['has_plain_reader'] else '|rx|n'
        lines.append(f"  |wPlain Reader:|n {reader_status}  (free merit)")
        lines.append(f"    |c(Devoted to radical nonviolence)|n")
        
        # Other Plain Merits
        if plain_data['plain_merits']:
            lines.append(f"  |wPlain Merits:|n  {len(plain_data['plain_merits'])}")
            for merit in plain_data['plain_merits']:
                lines.append(f"    - {merit}")
    
    def _add_lostboy_display(self, lines, lostboy_data, divider_color):
        """Add Lost Boy (Delta Protocol) chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rLOST BOY / DELTA PROTOCOL (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Protocol Merit
        protocol_status = '|gok!|n' if lostboy_data['has_protocol'] else '|rx|n'
        protocol_dots = lostboy_data['protocol_dots']
        
        if protocol_dots > 0:
            lines.append(f"  |wProtocol:|n     {protocol_status}  Mk {protocol_dots} (1 free)")
        else:
            lines.append(f"  |wProtocol:|n     {protocol_status}  |y(Get Protocol merit, 1 free)|n")
        
        lines.append(f"    |c(Augmentation level, determines withdrawal rate)|n")
        
        # Protocol Augmentation Merits
        if lostboy_data['protocol_merits']:
            lines.append(f"  |wAugmentations:|n {len(lostboy_data['protocol_merits'])}")
            for merit in lostboy_data['protocol_merits']:
                lines.append(f"    - {merit}")
        
        lines.append(f"\n    |rWarning: Requires Serum or suffers withdrawal|n")
    
    def _add_psychicvampire_display(self, lines, psychicvamp_data, divider_color):
        """Add Psychic Vampire chargen information."""
        lines.append(f"  |m{'=' * 80}|n")
        lines.append(f"  |mPSYCHIC VAMPIRE (MORTAL+)|n")
        lines.append(f"  |m{'=' * 80}|n")
        
        # Psychic Vampirism Merit
        vampirism_status = '|gok!|n' if psychicvamp_data['has_psychic_vampirism'] else '|rx|n'
        vampirism_dots = psychicvamp_data['vampirism_dots']
        
        if vampirism_dots > 0:
            lines.append(f"  |wPsychic Vampirism:|n {vampirism_status}  {vampirism_dots} dot{'s' if vampirism_dots > 1 else ''} (1 free)")
        else:
            lines.append(f"  |wPsychic Vampirism:|n {vampirism_status}  |y(Get merit, 1 free)|n")
        
        # Ephemera
        ephemera = psychicvamp_data['ephemera']
        max_ephemera = psychicvamp_data['max_ephemera']
        lines.append(f"  |wEphemera:|n     {ephemera}/{max_ephemera} (psychic fuel, max = Resolve)")
        lines.append(f"    |c(Steals life energy, loses 1/day)|n")
        
        # Ephemeral Battery
        if psychicvamp_data['has_ephemeral_battery']:
            lines.append(f"  |wEphemeral Battery:|n |gok!|n (increases storage)")
        
        # Relic option
        if psychicvamp_data['has_relic']:
            lines.append(f"  |wRelic-Bound:|n  |gok!|n (bonus merit dot)")
    
    def _add_immortal_display(self, lines, immortal_data, divider_color):
        """Add Immortal (Endless) chargen information."""
        lines.append(f"  |y{'=' * 80}|n")
        lines.append(f"  |yIMMORTAL / ENDLESS (MORTAL+)|n")
        lines.append(f"  |y{'=' * 80}|n")
        
        # Immortality Type
        immortal_name = immortal_data['immortal_name']
        subtype = immortal_data['subtype']
        
        if subtype:
            lines.append(f"  |wType:|n         {immortal_name}")
        else:
            lines.append(f"  |wType:|n         |rNot Set|n")
            lines.append(f"    |y(Use +stat subtype=<type>)|n")
            lines.append(f"    Options: blood_bather, body_thief, mystical_thief,")
            lines.append(f"             psychic_thief, eternal, reborn")
        
        # Favored Attribute
        favored_attr = immortal_data['favored_attribute']
        if favored_attr:
            attr_display = favored_attr.title()
            if immortal_data['has_favored_attr']:
                lines.append(f"  |wFavored Attr:|n  |gok!|n  {attr_display} |c(free dot)|n")
            else:
                lines.append(f"  |wFavored Attr:|n  |rx|n  {attr_display} |y(use +stat/favored)|n")
        
        # Endless Potency
        if immortal_data['has_endless_potency']:
            potency_dots = immortal_data['potency_dots']
            lines.append(f"  |wEndless Potency:|n |gok!|n  {potency_dots} dot{'s' if potency_dots > 1 else ''} (1 free in {favored_attr.title()})")
        elif favored_attr:
            lines.append(f"  |wEndless Potency:|n |rx|n  |y(Get Endless Potency: {favored_attr.title()} merit, 1 free)|n")
        
        # Virtue and Vice
        virtue_status = '|gok!|n' if immortal_data['has_virtue'] else '|rx|n'
        vice_status = '|gok!|n' if immortal_data['has_vice'] else '|rx|n'
        lines.append(f"  |wVirtue:|n       {virtue_status}    |wVice:|n {vice_status}")
        
        # Curse/Method
        if immortal_data['has_curse_method']:
            lines.append(f"  |wMethod/Curse:|n {immortal_data['curse_method']}")
        else:
            lines.append(f"  |wMethod/Curse:|n |y(Describe immortality process)|n")
        
        # Sekhem
        sekhem = immortal_data['sekhem']
        lines.append(f"  |wSekhem:|n       {sekhem} (starts at 1, max 5)")
        
        # Type-specific features
        if subtype == 'blood_bather':
            lines.append(f"\n  |cBlood Bather Aspects:|n")
            lines.append(f"    - Bathed in Life (ritual heals damage, maintains youth)")
            lines.append(f"    - Sacrificial Secrets (+6 starting XP)")
            lines.append(f"    - Strong Immune System (immune to natural disease)")
            lines.append(f"    |rIntegrity starts at 5 (not 7)|n")
        
        elif subtype in ['body_thief', 'mystical_thief', 'psychic_thief']:
            lines.append(f"\n  |cBody Thief Aspects:|n")
            lines.append(f"    - Borrowed Prowess (keeps Mental/Social, takes Physical)")
            lines.append(f"    - Steal Sense (borrow victim's sense for +2 bonus)")
            lines.append(f"    - Unobtrusive (fade into crowds, +Sekhem to blend)")
        
        elif subtype == 'eternal':
            # Relic
            if immortal_data['has_relic']:
                relic_dots = immortal_data['relic_dots']
                lines.append(f"  |wRelic:|n        |gok!|n  {relic_dots} dot{'s' if relic_dots > 1 else ''} (1 free, anchor)")
            else:
                lines.append(f"  |wRelic:|n        |rx|n  |y(Get Relic merit, 1 free)|n")
            
            lines.append(f"\n  |cEternal Aspects:|n")
            lines.append(f"    - Appraisal (detect powers/curses in objects)")
            lines.append(f"    - Consequence Free (shunt Conditions to anchor)")
            lines.append(f"    - Vital Shell (cannot die while anchor exists)")
        
        elif subtype == 'reborn':
            lines.append(f"\n  |cReborn Aspects:|n")
            lines.append(f"    - Dreams of Lives Unlived (fated visions)")
            lines.append(f"    - Solid Integrity (+2 to breaking points)")
            lines.append(f"    - Untrained Ease (no unskilled penalties)")
        
        # Investment (Mummy Cult)
        if immortal_data['has_investment']:
            lines.append(f"\n  |wMummy Investment:|n {immortal_data['investment']}")
            if immortal_data['invested_pillars']:
                lines.append(f"    |c(Can use master's Tier 1 Utterances)|n")
        else:
            lines.append(f"\n  |wMummy Investment:|n |yNone (optional)|n")
    
    def _add_proximus_display(self, lines, proximus_data, divider_color):
        """Add Proximus-specific chargen information."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |bPROXIMUS (MORTAL+)|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Dynasty
        dynasty = proximus_data['dynasty'].replace('_', ' ').title() if proximus_data['dynasty'] else '|yNone|n'
        lines.append(f"  |wDynasty:|n      {dynasty}")
        
        # Parent Path
        parent_path = proximus_data['parent_path'].title() if proximus_data['parent_path'] else '|rNot Set|n'
        lines.append(f"  |wParent Path:|n  {parent_path}")
        
        # Blessing Arcana
        if proximus_data['ruling_arcana']:
            ruling_str = ', '.join([a.title() for a in proximus_data['ruling_arcana']])
            lines.append(f"    Ruling: {ruling_str}")
        
        chosen = proximus_data['chosen_arcanum']
        if chosen:
            lines.append(f"    Chosen: {chosen.title()}")
        else:
            lines.append(f"    Chosen: |yNone|n |y(Use +stat blessing_arcanum=<name>)|n")
        
        # Blessings (as merits, max 30 dots)
        blessing_dots = proximus_data['blessing_dots']
        max_blessings = proximus_data['max_blessings']
        blessing_remaining = max_blessings - blessing_dots
        blessing_color = '|g' if blessing_remaining >= 0 else '|r'
        
        lines.append(f"  |wBlessings:|n    {blessing_color}{blessing_dots}/{max_blessings}|n dots (purchased as merits)")
        
        if proximus_data['blessings']:
            for blessing in proximus_data['blessings'][:5]:  # Show first 5
                blessing_name = blessing.replace('blessing:', '').replace('_', ' ').title()
                lines.append(f"    - {blessing_name}")
            if len(proximus_data['blessings']) > 5:
                lines.append(f"    ... and {len(proximus_data['blessings']) - 5} more")
        
        # Mana
        mana = proximus_data['mana']
        max_mana = proximus_data['max_mana']
        lines.append(f"  |wMana:|n         {mana}/{max_mana} (always max 5 for Proximi)")
        
        # Familial Curse
        curse_status = '|gok!|n' if proximus_data['has_curse'] else '|rx|n'
        if proximus_data['curse']:
            lines.append(f"  |wFamilial Curse:|n {curse_status}")
            lines.append(f"    {proximus_data['curse']}")
        else:
            lines.append(f"  |wFamilial Curse:|n {curse_status}  |y(Set curse description)|n")
        
        lines.append(f"\n    |c(Persistent Condition from bloodline)|n")
    
    def _add_sleepwalker_display(self, lines, sleepwalker_data, divider_color):
        """Add Sleepwalker-specific chargen information."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |bSLEEPWALKER (MORTAL+)|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Sleepwalker Merit
        sleepwalker_status = '|gok!|n' if sleepwalker_data['has_sleepwalker'] else '|rx|n'
        lines.append(f"  |wSleepwalker:|n  {sleepwalker_status}  (1 dot, free)")
        lines.append(f"    |c(Immune to Curse, cause no Dissonance)|n")
        
        # Sleepwalker Merits
        if sleepwalker_data['sleepwalker_merits']:
            lines.append(f"  |wSleepwalker Merits:|n {len(sleepwalker_data['sleepwalker_merits'])}")
            for merit in sleepwalker_data['sleepwalker_merits']:
                lines.append(f"    - {merit}")
        else:
            lines.append(f"  |wSleepwalker Merits:|n |yNone purchased yet|n")
            lines.append(f"    |c(Can assist mages with rituals)|n")
    
    def _add_faetouched_display(self, lines, faetouched_data, divider_color):
        """Add Fae-Touched-specific chargen information."""
        lines.append(f"  |m{'=' * 80}|n")
        lines.append(f"  |mFAE-TOUCHED (MORTAL+)|n")
        lines.append(f"  |m{'=' * 80}|n")
        
        # Promise
        promise_status = '|gok!|n' if faetouched_data['has_promise'] else '|rx|n'
        if faetouched_data['promise']:
            lines.append(f"  |wPromise:|n      {promise_status}")
            lines.append(f"    {faetouched_data['promise']}")
            if faetouched_data['promise_type']:
                lines.append(f"    Type: {faetouched_data['promise_type'].title()}")
        else:
            lines.append(f"  |wPromise:|n      {promise_status}  |y(Set promise description)|n")
        
        lines.append(f"    |c(Grants +1 die to actions that fortify promise)|n")
        
        # Wyrd (always 0)
        wyrd = faetouched_data['wyrd']
        if wyrd == 0:
            lines.append(f"  |wWyrd:|n         {wyrd} |g(correct, always 0)|n")
        else:
            lines.append(f"  |wWyrd:|n         {wyrd} |r(should be 0!)|n")
        
        # Glamour
        glamour = faetouched_data['glamour']
        max_glamour = faetouched_data['max_glamour']
        lines.append(f"  |wGlamour:|n      {glamour}/{max_glamour} (can bank up to 10)")
        lines.append(f"    |c(Harvest from emotions or Hedge bounty)|n")
        
        # Favored Regalia
        favored_regalia = faetouched_data.get('favored_regalia', None)
        if favored_regalia:
            lines.append(f"  |wFavored Regalia:|n {favored_regalia.title()} |gok!|n")
        else:
            lines.append(f"  |wFavored Regalia:|n |rx|n |y(Use +stat favored regalia=<name>)|n")
        
        # Contracts
        contract_count = faetouched_data['contract_count']
        expected_contracts = faetouched_data['expected_contracts']
        contract_color = '|g' if contract_count >= expected_contracts else '|r'
        
        lines.append(f"  |wContracts:|n    {contract_color}{contract_count}/{expected_contracts}|n (Common from favored Regalia)")
        
        if faetouched_data['contracts']:
            for contract in faetouched_data['contracts']:
                contract_name = contract.replace('contract:', '').replace('_', ' ').title()
                lines.append(f"    - {contract_name}")
        
        # Court Goodwill (for Court Contracts)
        if faetouched_data['court_goodwill']:
            lines.append(f"  |wCourt Goodwill:|n")
            for court, dots in faetouched_data['court_goodwill'].items():
                court_name = court.replace('goodwill:', '').replace('_', ' ').title()
                lines.append(f"    {court_name}: {dots}")
        
        # Fae-Touched Merits
        if faetouched_data['faetouched_merits']:
            lines.append(f"  |wFae-Touched Merits:|n {len(faetouched_data['faetouched_merits'])}")
            for merit in faetouched_data['faetouched_merits']:
                lines.append(f"    - {merit}")
        
        # Starting Conditions (warnings)
        lines.append(f"\n  |rStarting Conditions:|n")
        lines.append(f"    - Madness (Hedge exposure)")
        lines.append(f"    - Arcadian Dreams")
        lines.append(f"    - Hedge Addiction")
        
        # Limitations
        lines.append(f"\n  |cLimitations:|n")
        lines.append(f"    - Cannot use Loopholes in Contracts")
        lines.append(f"    - Must be taught Contracts (cannot learn alone)")
        lines.append(f"    - Cannot auto-gain seeming benefits")
        lines.append(f"    - Cannot enter own dreams naturally")
    
    def get_display_desc(self, looker, **kwargs):
        """
        Override the room description to show chargen progress instead.
        
        Args:
            looker: The character viewing the room
            **kwargs: Additional arguments
            
        Returns:
            str: Chargen progress display instead of room description
        """
        # Return chargen display as the room description
        chargen_display = self.get_chargen_display(looker)
        
        if chargen_display:
            return chargen_display
        else:
            # Fallback to regular description if no chargen data
            return super().get_display_desc(looker, **kwargs)
        auspice_skill_used = other.get('favored_stat', None)
        
        # Check if favored stat is set and is one of the valid auspice skills
        has_auspice_skill_bonus = (auspice_skill_used is not None and 
                                   auspice_skill_used in auspice_skills)
        
        # Calculate Renown
        renown = stats.get('renown', {
            'glory': 0,
            'honor': 0,
            'cunning': 0,
            'purity': 0,
            'wisdom': 0
        })
        
        total_renown = sum(renown.values())
        expected_renown = 3 if tribe != 'ghost_wolf' else 2
        
        # Check for proper renown distribution
        auspice_renown = auspice_info.get('renown')
        tribe_renown = tribe_info.get('renown')
        
        has_auspice_renown = renown.get(auspice_renown, 0) >= 1 if auspice_renown else False
        has_tribe_renown = renown.get(tribe_renown, 0) >= 1 if tribe_renown else True  # Ghost wolves don't need tribe renown
        
        # Check if any renown is at 3+ (shouldn't be at chargen)
        has_excessive_renown = any(r >= 3 for r in renown.values())
        
        # Get Gifts
        powers = stats.get('powers', {})
        gifts = {}
        gift_facets = 0
        has_moon_gift = False
        
        for power_name, power_value in powers.items():
            power_lower = power_name.lower().replace(' ', '_')
            if 'gift' in power_lower or power_lower in ['inspiration', 'rage', 'strength', 'death', 
                                                         'elemental', 'insight', 'nature', 'stealth',
                                                         'warding', 'knowledge', 'shaping', 'technology',
                                                         'evasion', 'dominance', 'weather']:
                gifts[power_name] = power_value
                if isinstance(power_value, int):
                    gift_facets += power_value
                else:
                    gift_facets += 1
                
                # Check for moon gift
                if auspice_info.get('moon_gift', '').lower() in power_name.lower():
                    has_moon_gift = True
        
        # Get Rites
        rites = {}
        rite_dots = 0
        for power_name, power_value in powers.items():
            power_lower = power_name.lower()
            if 'rite' in power_lower and 'rite_' in power_lower:
                rites[power_name] = power_value
                if isinstance(power_value, int):
                    rite_dots += power_value
                else:
                    rite_dots += 1
        
        # Calculate rites from merits (merit dots traded for rites)
        # Base is 2 dots, anything above that came from merits
        rites_from_merits = max(0, rite_dots - 2)
        
        # Primal Urge tracking
        other = stats.get('other', {})
        primal_urge = other.get('primal_urge', 1)
        pu_from_merits = max(0, primal_urge - 1)
        pu_merit_cost = pu_from_merits * 5
        
        # Check for Bone and Blood (stored in bio, not anchors)
        # Get bio (might already be retrieved earlier in the function)
        bio = stats.get('bio', {})
        anchors = stats.get('anchors', {})
        
        # Check bio first (modern storage), then anchors (legacy storage)
        has_bone = (('bone' in bio and bio['bone'] and bio['bone'] != '<not set>') or 
                    ('bone' in anchors and anchors['bone'] and anchors['bone'] != '<not set>'))
        has_blood = (('blood' in bio and bio['blood'] and bio['blood'] != '<not set>') or 
                     ('blood' in anchors and anchors['blood'] and anchors['blood'] != '<not set>'))
        
        # Check for required merits
        has_totem = any('totem' in m.lower() for m in merits.keys())
        has_first_tongue = any('first tongue' in m.lower() or 'language' in m.lower() for m in merits.keys())
        
        # Touchstone check (need to check via command, not stored in stats typically)
        # We'll just note that they need to use +touchstone command
        
        return {
            'auspice': auspice,
            'tribe': tribe,
            'auspice_skills': auspice_skills,
            'has_auspice_skill_bonus': has_auspice_skill_bonus,
            'auspice_skill_used': auspice_skill_used,
            'tribe_gifts': tribe_info.get('gifts', []),
            'renown': renown,
            'total_renown': total_renown,
            'expected_renown': expected_renown,
            'auspice_renown': auspice_renown,
            'tribe_renown': tribe_renown,
            'has_auspice_renown': has_auspice_renown,
            'has_tribe_renown': has_tribe_renown,
            'has_excessive_renown': has_excessive_renown,
            'gifts': gifts,
            'gift_facets': gift_facets,
            'has_moon_gift': has_moon_gift,
            'moon_gift_name': auspice_info.get('moon_gift', 'Unknown'),
            'rites': rites,
            'rite_dots': rite_dots,
            'rites_from_merits': rites_from_merits,
            'primal_urge': primal_urge,
            'pu_merit_cost': pu_merit_cost,
            'has_bone': has_bone,
            'has_blood': has_blood,
            'has_totem': has_totem,
            'has_first_tongue': has_first_tongue
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
        lines.append("")  # Empty line for spacing (matching base room desc format)
        lines.append(f"|{divider_color}{'=' * 80}|n")
        
        # Properly center the header text (visible length only, not counting color codes)
        header_text = "CHARACTER GENERATION PROGRESS"
        padding = (80 - len(header_text)) // 2
        centered_header = " " * padding + f"|{header_color}{header_text}|n" + " " * padding
        # Adjust for odd lengths
        if len(header_text) % 2 == 1:
            centered_header += " "
        lines.append(centered_header)
        
        lines.append(f"|{divider_color}{'=' * 80}|n")
        
        for char in characters:
            points = self.calculate_chargen_points(char)
            
            if not points:
                continue
                
            char_name = char.get_display_name(looker)
            template = points.get('template', 'Mortal')
            
            # Character header
            lines.append(f"\n|y{char_name}|n ({template})")
            lines.append(f"|{divider_color}{'-' * 80}|n")
            
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
            
            # Show favored stat if set
            favored_stat = points.get('favored_stat', None)
            if favored_stat:
                lines.append(f"  |cFavored Stat:|n {favored_stat.replace('_', ' ').title()} |g(free dot)|n")
            
            # Template-specific sections
            if 'vampire' in points:
                lines.append("")  # Empty line for spacing
                self._add_vampire_display(lines, points['vampire'], divider_color)
            elif 'werewolf' in points:
                lines.append("")  # Empty line for spacing
                self._add_werewolf_display(lines, points['werewolf'], divider_color)
            elif 'changeling' in points:
                lines.append("")  # Empty line for spacing
                self._add_changeling_display(lines, points['changeling'], divider_color)
            elif 'mage' in points:
                lines.append("")  # Empty line for spacing
                self._add_mage_display(lines, points['mage'], divider_color)
            elif 'deviant' in points:
                lines.append("")  # Empty line for spacing
                self._add_deviant_display(lines, points['deviant'], divider_color)
            elif 'geist' in points:
                lines.append("")  # Empty line for spacing
                self._add_geist_display(lines, points['geist'], divider_color)
            elif 'hunter' in points:
                lines.append("")  # Empty line for spacing
                self._add_hunter_display(lines, points['hunter'], divider_color)
            elif 'mummy' in points:
                lines.append("")  # Empty line for spacing
                self._add_mummy_display(lines, points['mummy'], divider_color)
            elif 'promethean' in points:
                lines.append("")  # Empty line for spacing
                self._add_promethean_display(lines, points['promethean'], divider_color)
            elif 'mortalplus' in points:
                lines.append("")  # Empty line for spacing
                self._add_mortalplus_display(lines, points['mortalplus'], divider_color)
            
        lines.append(f"|{divider_color}{'=' * 80}|n")
        lines.append("")  # Empty line for spacing after the display
        
        return "\n".join(lines)
    
    def _add_vampire_display(self, lines, vamp_data, divider_color):
        """
        Add vampire-specific chargen information to the display.
        
        Args:
            lines: List of strings to append display lines to
            vamp_data: Dictionary of vampire chargen data
            divider_color: Color code for dividers
        """
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |cVAMPIRE TEMPLATE|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Clan and favored attributes
        clan = vamp_data['clan'].title() if vamp_data['clan'] else '|rNot Set|n'
        lines.append(f"  |wClan:|n         {clan}")
        
        if vamp_data['favored_attributes']:
            favored_options = vamp_data['favored_attributes']
            selected = vamp_data.get('favored_attr_used', None)
            
            if selected and selected in favored_options:
                # Show selected attribute in green, others dimmed
                favored_display = []
                for attr in favored_options:
                    if attr == selected:
                        favored_display.append(f"|g{attr.title()}|n |g[SELECTED]|n")
                    else:
                        favored_display.append(f"|x{attr.title()}|n")
                lines.append(f"  |wClan Bonus:|n   {' or '.join(favored_display)}")
            else:
                # Show both options, none selected
                favored_str = ' or '.join([a.title() for a in favored_options])
                lines.append(f"  |wClan Bonus:|n   {favored_str} |rx|n")
                lines.append(f"    |y(Use +stat/favored <attribute> to select free dot)|n")
        
        # Mask and Dirge
        mask_status = '|gok!|n' if vamp_data['has_mask'] else '|rx|n'
        dirge_status = '|gok!|n' if vamp_data['has_dirge'] else '|rx|n'
        lines.append(f"  |wMask:|n         {mask_status}    |wDirge:|n {dirge_status}")
        
        # Disciplines
        disc_spent = vamp_data['discipline_dots_total']
        disc_avail = vamp_data['discipline_dots_available']
        disc_remaining = disc_avail - disc_spent
        disc_color = '|g' if disc_remaining >= 0 else '|r'
        
        lines.append(f"  |wDisciplines:|n  {disc_color}{disc_spent}/{disc_avail}|n  (Remaining: {disc_color}{disc_remaining}|n)")
        
        # Show discipline breakdown
        in_clan = vamp_data['in_clan_dots']
        out_of_clan = vamp_data['out_of_clan_dots']
        covenant = vamp_data['covenant_power_dots']
        
        # Validation: at least 2 must be in-clan
        in_clan_status = '|g' if in_clan >= 2 else '|r'
        lines.append(f"    In-Clan:    {in_clan_status}{in_clan}|n (need at least 2)")
        if out_of_clan > 0:
            lines.append(f"    Out-of-Clan: {out_of_clan}")
        if covenant > 0:
            lines.append(f"    Covenant:    {covenant} (requires Covenant Status)")
        
        # List actual disciplines taken
        if vamp_data['disciplines']:
            disc_list = []
            for disc_name, dots in vamp_data['disciplines'].items():
                disc_lower = disc_name.lower().replace(' ', '_')
                # Mark if in-clan
                if disc_lower in vamp_data['in_clan_disciplines']:
                    disc_list.append(f"{disc_name} {dots} |g(in-clan)|n")
                else:
                    disc_list.append(f"{disc_name} {dots}")
            lines.append(f"    Taken: {', '.join(disc_list)}")
        
        # Blood Potency
        bp = vamp_data['blood_potency']
        bp_cost = vamp_data['bp_merit_cost']
        if bp_cost > 0:
            lines.append(f"  |wBlood Potency:|n {bp} (1 free + {bp - 1} from merits = {bp_cost} merit dots)")
        else:
            lines.append(f"  |wBlood Potency:|n {bp} (free dot)")
        
        # Covenant
        covenant_display = None
        if vamp_data['covenant']:
            # Format covenant name with proper full name
            covenant_display = self._format_covenant_name(vamp_data['covenant'])
        
        if covenant_display:
            lines.append(f"  |wCovenant:|n     {covenant_display}")
            # Check if they have Covenant Status merit
            covenant_status = vamp_data.get('covenant_status', None)
            covenant_status_dots = vamp_data.get('covenant_status_dots', 0)
            
            if covenant_status and isinstance(covenant_status_dots, int) and covenant_status_dots > 0:
                lines.append(f"    Status: {covenant_status_dots} dot{'s' if covenant_status_dots != 1 else ''} |g(enables benefits)|n")
            elif covenant_status:
                lines.append(f"    |yStatus: Present but no dots set (use +stat)|n")
            else:
                lines.append(f"    |yStatus: None (get Status merit for benefits)|n")
        else:
            lines.append(f"  |wCovenant:|n     |yNone (optional)|n")
        
        # Touchstone reminder
        touchstone_status = '|g(Merit taken)|n' if vamp_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
    
    def _add_werewolf_display(self, lines, wolf_data, divider_color):
        """
        Add werewolf-specific chargen information to the display.
        
        Args:
            lines: List of strings to append display lines to
            wolf_data: Dictionary of werewolf chargen data
            divider_color: Color code for dividers
        """
        lines.append(f"  |c{'~' * 76}|n")
        lines.append(f"  |cWEREWOLF TEMPLATE|n")
        lines.append(f"  |c{'~' * 76}|n")
        
        # Auspice and Tribe
        auspice = wolf_data['auspice'].replace('_', ' ').title() if wolf_data['auspice'] else '|rNot Set|n'
        tribe = self._format_tribe_name(wolf_data['tribe']) if wolf_data['tribe'] else '|rNot Set|n'
        lines.append(f"  |wAuspice:|n      {auspice}")
        lines.append(f"  |wTribe:|n        {tribe}")
        
        # Auspice skill bonus
        if wolf_data['auspice_skills']:
            skill_options = wolf_data['auspice_skills']
            selected = wolf_data.get('auspice_skill_used', None)
            
            if selected and selected in skill_options:
                # Show selected skill in green, others dimmed
                skill_display = []
                for skill in skill_options:
                    if skill == selected:
                        skill_display.append(f"|g{skill.replace('_', ' ').title()}|n |g[SELECTED]|n")
                    else:
                        skill_display.append(f"|x{skill.replace('_', ' ').title()}|n")
                lines.append(f"  |wAuspice Bonus:|n {', '.join(skill_display)}")
            else:
                # Show all options, none selected
                skills_str = ', '.join([s.replace('_', ' ').title() for s in skill_options])
                lines.append(f"  |wAuspice Bonus:|n {skills_str} |rx|n")
                lines.append(f"    |y(Use +stat/favored <skill> to select free dot)|n")
        
        # Bone and Blood
        bone_status = '|gok!|n' if wolf_data['has_bone'] else '|rx|n'
        blood_status = '|gok!|n' if wolf_data['has_blood'] else '|rx|n'
        lines.append(f"  |wBone:|n         {bone_status}    |wBlood:|n {blood_status}")
        
        # Renown
        renown_total = wolf_data['total_renown']
        renown_expected = wolf_data['expected_renown']
        renown_remaining = renown_expected - renown_total
        renown_color = '|g' if renown_remaining >= 0 and not wolf_data['has_excessive_renown'] else '|r'
        
        lines.append(f"  |wRenown:|n       {renown_color}{renown_total}/{renown_expected}|n  (Remaining: {renown_color}{renown_remaining}|n)")
        
        # Show renown breakdown
        renown = wolf_data['renown']
        renown_parts = []
        for r_name, r_dots in renown.items():
            if r_dots > 0:
                # Mark auspice and tribe renown
                markers = []
                if r_name == wolf_data['auspice_renown']:
                    markers.append('auspice')
                if r_name == wolf_data['tribe_renown']:
                    markers.append('tribe')
                
                marker_str = f" |c({', '.join(markers)})|n" if markers else ""
                renown_parts.append(f"{r_name.title()} {r_dots}{marker_str}")
        
        if renown_parts:
            lines.append(f"    {', '.join(renown_parts)}")
        
        # Validation warnings
        if not wolf_data['has_auspice_renown'] and wolf_data['auspice_renown']:
            lines.append(f"    |rWarning: Need 1+ {wolf_data['auspice_renown'].title()} (auspice)|n")
        if not wolf_data['has_tribe_renown'] and wolf_data['tribe_renown']:
            lines.append(f"    |rWarning: Need 1+ {wolf_data['tribe_renown'].title()} (tribe)|n")
        if wolf_data['has_excessive_renown']:
            lines.append(f"    |rWarning: Cannot have 3+ in any Renown at chargen|n")
        
        # Gifts
        lines.append(f"  |wGifts:|n")
        
        # Moon Gift
        moon_gift_status = '|gok!|n' if wolf_data['has_moon_gift'] else '|rx|n'
        lines.append(f"    Moon Gift ({wolf_data['moon_gift_name']}): {moon_gift_status}")
        
        # Shadow/Wolf Gifts (should have 2+ facets)
        expected_facets = 2  # Minimum expected at chargen
        facet_color = '|g' if wolf_data['gift_facets'] >= expected_facets else '|y'
        lines.append(f"    Shadow/Wolf Gift Facets: {facet_color}{wolf_data['gift_facets']}|n (need at least 2)")
        
        # List gifts taken
        if wolf_data['gifts']:
            gift_list = []
            for gift_name, gift_value in wolf_data['gifts'].items():
                dots = gift_value if isinstance(gift_value, int) else 1
                gift_list.append(f"{gift_name} {dots}")
            lines.append(f"    Taken: {', '.join(gift_list)}")
        
        # Show tribe gifts available
        if wolf_data['tribe_gifts']:
            tribe_gifts_str = ', '.join([g.title() for g in wolf_data['tribe_gifts']])
            lines.append(f"    Tribe Gifts: {tribe_gifts_str}")
        
        # Rites
        rite_dots = wolf_data['rite_dots']
        rites_from_merits = wolf_data['rites_from_merits']
        
        if rites_from_merits > 0:
            lines.append(f"  |wRites:|n        {rite_dots} dots (2 base + {rites_from_merits} from merits)")
        else:
            rite_color = '|g' if rite_dots >= 2 else '|y'
            lines.append(f"  |wRites:|n        {rite_color}{rite_dots}|n dots (need 2 base)")
        
        if wolf_data['rites']:
            rite_list = [f"{r}" for r in wolf_data['rites'].keys()]
            lines.append(f"    Taken: {', '.join(rite_list)}")
        
        # Primal Urge
        pu = wolf_data['primal_urge']
        pu_cost = wolf_data['pu_merit_cost']
        if pu_cost > 0:
            lines.append(f"  |wPrimal Urge:|n  {pu} (1 free + {pu - 1} from merits = {pu_cost} merit dots)")
        else:
            lines.append(f"  |wPrimal Urge:|n  {pu} (free dot)")
        
        # Required Merits
        totem_status = '|gok!|n' if wolf_data['has_totem'] else '|rx|n'
        first_tongue_status = '|gok!|n' if wolf_data['has_first_tongue'] else '|rx|n'
        lines.append(f"  |wTotem:|n        {totem_status}  (1 dot, free)")
        lines.append(f"  |wFirst Tongue:|n {first_tongue_status}  (Language Merit, free)")
        
        # Touchstone reminder
        lines.append(f"  |wTouchstones:|n  |y(Use +touchstone for Physical & Spiritual)|n")
    
    def _add_changeling_display(self, lines, changeling_data, divider_color):
        """Add changeling-specific chargen information to the display."""
        lines.append(f"  |m{'=' * 80}|n")
        lines.append(f"  |mCHANGELING TEMPLATE|n")
        lines.append(f"  |m{'=' * 80}|n")
        
        # Seeming and Kith
        seeming = changeling_data['seeming'].title() if changeling_data['seeming'] else '|rNot Set|n'
        kith = changeling_data['kith'].replace('_', ' ').title() if changeling_data['kith'] else '|yNone|n'
        lines.append(f"  |wSeeming:|n      {seeming}")
        lines.append(f"  |wKith:|n         {kith}")
        
        # Court
        court = changeling_data['court'].replace('_', ' ').title() if changeling_data['court'] else '|yNone (optional)|n'
        lines.append(f"  |wCourt:|n        {court}")
        
        # Favored Attribute (from seeming)
        if changeling_data['favored_attributes']:
            category = changeling_data['attribute_category']
            favored_options = changeling_data['favored_attributes']
            selected = changeling_data.get('favored_attr_used', None)
            
            if selected and selected in favored_options:
                favored_display = []
                for attr in favored_options:
                    if attr == selected:
                        favored_display.append(f"|g{attr.title()}|n |g[SELECTED]|n")
                    else:
                        favored_display.append(f"|x{attr.title()}|n")
                lines.append(f"  |wSeeming Bonus:|n {' or '.join(favored_display)} |c({category.title()})|n")
            else:
                favored_str = ' or '.join([a.title() for a in favored_options])
                lines.append(f"  |wSeeming Bonus:|n {favored_str} |rx|n |c({category.title()})|n")
                lines.append(f"    |y(Use +stat/favored <attribute> to select free dot)|n")
        
        # Needle and Thread
        needle_status = '|gok!|n' if changeling_data['has_needle'] else '|rx|n'
        thread_status = '|gok!|n' if changeling_data['has_thread'] else '|rx|n'
        lines.append(f"  |wNeedle:|n       {needle_status}    |wThread:|n {thread_status}")
        
        # Contracts
        common_taken = changeling_data['common_contracts']
        common_avail = changeling_data['contracts_available']
        royal_taken = changeling_data['royal_contracts']
        royal_avail = changeling_data['royal_available']
        
        contracts_color = '|g' if common_taken <= common_avail else '|r'
        royal_color = '|g' if royal_taken <= royal_avail else '|r'
        
        lines.append(f"  |wContracts:|n")
        lines.append(f"    Common:  {contracts_color}{common_taken}/{common_avail}|n (need 2 from favored)")
        lines.append(f"    Royal:   {royal_color}{royal_taken}/{royal_avail}|n")
        
        # Favored Regalia
        seeming_regalia = changeling_data.get('seeming_regalia', None)
        chosen_regalia = changeling_data.get('favored_regalia', None)
        
        regalia_parts = []
        if seeming_regalia:
            regalia_parts.append(f"|g{seeming_regalia.title()}|n (seeming)")
        
        if chosen_regalia:
            regalia_parts.append(f"|g{chosen_regalia.title()}|n (chosen)")
        else:
            regalia_parts.append('|yNone|n (chosen)')
        
        if regalia_parts:
            lines.append(f"    Favored Regalia: {', '.join(regalia_parts)}")
            if not chosen_regalia:
                lines.append(f"    |y(Use +stat favored regalia=<name> to choose 2nd)|n")
        
        # List contracts taken
        if changeling_data['contracts']:
            contract_list = []
            for contract_name in changeling_data['contracts'].keys():
                display_name = contract_name.replace('contract:', '').replace('_', ' ').title()
                contract_list.append(display_name)
            if contract_list:
                lines.append(f"    Taken: {', '.join(contract_list[:6])}")
                if len(contract_list) > 6:
                    lines.append(f"           {', '.join(contract_list[6:])}")
        
        # Wyrd
        wyrd = changeling_data['wyrd']
        wyrd_cost = changeling_data['wyrd_merit_cost']
        if wyrd_cost > 0:
            lines.append(f"  |wWyrd:|n         {wyrd} (1 free + {wyrd - 1} from merits = {wyrd_cost} merit dots)")
        else:
            lines.append(f"  |wWyrd:|n         {wyrd} (free dot)")
        
        # Mantle (free from court)
        if changeling_data['court']:
            if changeling_data['has_mantle']:
                mantle_dots = changeling_data['mantle_dots']
                if mantle_dots >= 1:
                    lines.append(f"  |wMantle:|n       {mantle_dots} dot{'s' if mantle_dots > 1 else ''} |g(1 free from court)|n")
                else:
                    lines.append(f"  |wMantle:|n       |yPresent but no dots set|n")
            else:
                lines.append(f"  |wMantle:|n       |rx|n |y(Get Mantle merit for court benefits)|n")
        
        # Touchstone reminder
        touchstone_status = '|g(Merit taken)|n' if changeling_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
        lines.append(f"    |c(Composure + 1 Clarity boxes)|n")
    
    def _add_mage_display(self, lines, mage_data, divider_color):
        """Add mage-specific chargen information to the display."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |bMAGE TEMPLATE|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Path and Order
        path = mage_data['path'].title() if mage_data['path'] else '|rNot Set|n'
        order = mage_data['order'].replace('_', ' ').title() if mage_data['order'] else '|yNone|n'
        lines.append(f"  |wPath:|n         {path}")
        lines.append(f"  |wOrder:|n        {order}")
        
        # Ruling and Inferior Arcana
        if mage_data['ruling_arcana']:
            ruling_str = ', '.join([a.title() for a in mage_data['ruling_arcana']])
            lines.append(f"  |wRuling Arcana:|n {ruling_str}")
        
        if mage_data['inferior_arcanum']:
            lines.append(f"  |wInferior:|n     {mage_data['inferior_arcanum'].title()}")
        
        # Rote Skills
        if mage_data['rote_skills']:
            rote_str = ', '.join([s.replace('_', ' ').title() for s in mage_data['rote_skills']])
            lines.append(f"  |wRote Skills:|n  {rote_str}")
        
        # Favored Attribute (Resistance: Composure, Resolve, Stamina)
        favored_options = ['Composure', 'Resolve', 'Stamina']
        selected = mage_data.get('favored_attr_used', None)
        
        if selected:
            favored_display = []
            for attr in favored_options:
                if attr.lower() == selected:
                    favored_display.append(f"|g{attr}|n |g[SELECTED]|n")
                else:
                    favored_display.append(f"|x{attr}|n")
            lines.append(f"  |wResistance Bonus:|n {' or '.join(favored_display)}")
        else:
            lines.append(f"  |wResistance Bonus:|n {' or '.join(favored_options)} |rx|n")
            lines.append(f"    |y(Use +stat/favored <attribute> to select free dot)|n")
        
        # Arcana
        arcana_dots = mage_data['arcana_dots']
        arcana_avail = mage_data['arcana_available']
        arcana_remaining = arcana_avail - arcana_dots
        arcana_color = '|g' if arcana_remaining >= 0 else '|r'
        
        lines.append(f"  |wArcana:|n       {arcana_color}{arcana_dots}/{arcana_avail}|n  (Remaining: {arcana_color}{arcana_remaining}|n)")
        
        # Arcana validations
        ruling_dots = mage_data['ruling_dots']
        ruling_color = '|g' if 3 <= ruling_dots <= 5 else '|r'
        lines.append(f"    Ruling:  {ruling_color}{ruling_dots}|n (need 3-5 dots in Ruling Arcana)")
        
        both_ruling_status = '|gok!|n' if mage_data['has_both_ruling'] else '|rx|n'
        lines.append(f"    Both Ruling have 1+: {both_ruling_status}")
        
        max_dots = mage_data['max_arcanum_dots']
        max_color = '|g' if max_dots <= 3 else '|r'
        lines.append(f"    Max in one: {max_color}{max_dots}|n (limit 3 dots)")
        
        if mage_data['has_inferior']:
            lines.append(f"    |rWarning: Cannot have dots in Inferior Arcanum ({mage_data['inferior_arcanum'].title()})|n")
        
        # List arcana taken
        if mage_data['arcana']:
            arcana_list = []
            for arcanum_name, dots in mage_data['arcana'].items():
                arcanum_lower = arcanum_name.lower().replace(' ', '_')
                # Mark ruling/inferior
                if arcanum_lower in mage_data['ruling_arcana']:
                    arcana_list.append(f"{arcanum_name.title()} {dots} |c(ruling)|n")
                elif arcanum_lower == mage_data['inferior_arcanum']:
                    arcana_list.append(f"{arcanum_name.title()} {dots} |r(inferior!)|n")
                else:
                    arcana_list.append(f"{arcanum_name.title()} {dots}")
            lines.append(f"    Taken: {', '.join(arcana_list)}")
        
        # Rotes
        rotes = mage_data['rotes_count']
        rotes_avail = mage_data['rotes_available']
        rotes_color = '|g' if rotes >= rotes_avail else '|y'
        lines.append(f"  |wRotes:|n        {rotes_color}{rotes}/{rotes_avail}|n")
        
        # Gnosis
        gnosis = mage_data['gnosis']
        gnosis_cost = mage_data['gnosis_merit_cost']
        if gnosis_cost > 0:
            lines.append(f"  |wGnosis:|n       {gnosis} (1 free + {gnosis - 1} from merits = {gnosis_cost} merit dots)")
        else:
            lines.append(f"  |wGnosis:|n       {gnosis} (free dot)")
        
        # Obsessions
        obs_count = mage_data['obsessions_count']
        obs_expected = mage_data['expected_obsessions']
        obs_color = '|g' if obs_count >= obs_expected else '|y'
        lines.append(f"  |wObsessions:|n   {obs_color}{obs_count}/{obs_expected}|n")
        if mage_data['obsessions']:
            for obs in mage_data['obsessions']:
                lines.append(f"    - {obs}")
        
        # Praxes
        prax_count = mage_data['praxes_count']
        prax_expected = mage_data['expected_praxes']
        prax_color = '|g' if prax_count >= prax_expected else '|y'
        lines.append(f"  |wPraxes:|n       {prax_color}{prax_count}/{prax_expected}|n  (1 per Gnosis)")
        if mage_data['praxes']:
            for prax in mage_data['praxes']:
                lines.append(f"    - {prax.replace('_', ' ').title()}")
        
        # Nimbus
        nimbus_status = '|gok!|n' if mage_data['has_immediate_nimbus'] else '|rx|n'
        lines.append(f"  |wNimbus:|n       {nimbus_status}  |y(Use +stat/mage nimbus to set)|n")
        
        # Dedicated Tool
        tool_status = '|gok!|n' if mage_data['has_dedicated_tool'] else '|rx|n'
        if mage_data['dedicated_tool']:
            lines.append(f"  |wDedicated Tool:|n {tool_status}  ({mage_data['dedicated_tool']})")
        else:
            lines.append(f"  |wDedicated Tool:|n {tool_status}  |y(Use +stat/mage dedicated_tool=<name>)|n")
        
        # Order Benefits
        if mage_data['order']:
            lines.append(f"  |wOrder Benefits:|n")
            
            # Occult skill
            occult_dots = mage_data['occult_dots']
            occult_status = '|gok!|n' if occult_dots >= 1 else '|rx|n'
            lines.append(f"    Occult:      {occult_status}  ({occult_dots} dot{'s' if occult_dots > 1 else ''}, need 1+)")
            
            # Order Status
            if mage_data['has_order_status']:
                status_dots = mage_data['order_status_dots']
                if status_dots >= 1:
                    lines.append(f"    Order Status: |gok!|n  ({status_dots} dot{'s' if status_dots > 1 else ''}, 1 free)")
                else:
                    lines.append(f"    Order Status: |yPresent but no dots set|n")
            else:
                lines.append(f"    Order Status: |rx|n  |y(Get Order Status merit)|n")
            
            # High Speech
            speech_status = '|gok!|n' if mage_data['has_high_speech'] else '|rx|n'
            lines.append(f"    High Speech:  {speech_status}  (Language Merit, free)")
    
    def _add_deviant_display(self, lines, deviant_data, divider_color):
        """Add deviant-specific chargen information to the display."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rDEVIANT TEMPLATE|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Origin and Clade
        origin_name = deviant_data.get('origin_name', 'Unknown')
        clade_display = deviant_data['clade_display'] if deviant_data['clade_display'] else '|rNot Set|n'
        lines.append(f"  |wOrigin:|n       {origin_name}")
        lines.append(f"  |wClade:|n        {clade_display}")
        
        # Forms (optional)
        if deviant_data['form']:
            forms_str = ', '.join([f.replace('_', ' ').title() for f in deviant_data['form']])
            lines.append(f"  |wForm:|n         {forms_str}")
        
        # Origin bonus
        bonus_type = deviant_data.get('origin_bonus_type', None)
        bonus_stat = deviant_data.get('origin_bonus_stat', None)
        if bonus_type and bonus_stat:
            if bonus_type == 'any':
                lines.append(f"  |wOrigin Bonus:|n  1 Scar-free Magnitude (any Variation)")
            else:
                lines.append(f"  |wOrigin Bonus:|n  1 Scar-free Magnitude ({bonus_type.title()} Variation)")
            
            if bonus_stat == 'choice':
                lines.append(f"                 +1 Loyalty or Conviction (your choice)")
            else:
                lines.append(f"                 +1 {bonus_stat.title()}")
        
        # Variations
        var_mag = deviant_data['variation_magnitude']
        lines.append(f"  |wVariations:|n   {var_mag} Magnitude total")
        
        if deviant_data['variations']:
            var_list = []
            for var_name, magnitude in deviant_data['variations'].items():
                # Remove prefix for display
                display_name = var_name.replace('variation:', '').replace('_', ' ').title()
                var_list.append(f"{display_name} {magnitude}")
            
            # Display variations
            lines.append(f"    |c(At least half from Clade or Universal)|n")
            for var in var_list:
                lines.append(f"    - {var}")
        else:
            lines.append(f"    |yNo variations set yet|n")
        
        # Scars
        scar_mag = deviant_data['scar_magnitude']
        lines.append(f"  |wScars:|n        {scar_mag} Magnitude total")
        lines.append(f"    |c(Each Variation needs matching Scar)|n")
        
        if deviant_data['scars']:
            scar_list = []
            for scar_name, magnitude in deviant_data['scars'].items():
                # Remove prefix for display
                display_name = scar_name.replace('scar:', '').replace('_', ' ').title()
                scar_list.append(f"{display_name} {magnitude}")
            
            for scar in scar_list:
                lines.append(f"    - {scar}")
        else:
            lines.append(f"    |yNo scars set yet|n")
        
        # Loyalty and Conviction
        loyalty = deviant_data['loyalty']
        conviction = deviant_data['conviction']
        
        # Loyalty Touchstones
        loyalty_ts = deviant_data['loyalty_touchstones']
        loyalty_needed = deviant_data['loyalty_touchstones_needed']
        loyalty_count = len(loyalty_ts)
        loyalty_color = '|g' if loyalty_count >= loyalty_needed else '|r'
        
        lines.append(f"  |wLoyalty:|n      {loyalty} ({loyalty_color}{loyalty_count}/{loyalty_needed}|n Touchstones)")
        if loyalty_ts:
            for ts in loyalty_ts:
                lines.append(f"    - {ts}")
        elif loyalty_needed > 0:
            lines.append(f"    |y(Use +touchstone to add)|n")
        
        # Conviction Touchstones
        conviction_ts = deviant_data['conviction_touchstones']
        conviction_needed = deviant_data['conviction_touchstones_needed']
        conviction_count = len(conviction_ts)
        conviction_color = '|g' if conviction_count >= conviction_needed else '|r'
        
        lines.append(f"  |wConviction:|n   {conviction} ({conviction_color}{conviction_count}/{conviction_needed}|n Touchstones)")
        if conviction_ts:
            for ts in conviction_ts:
                lines.append(f"    - {ts}")
        elif conviction_needed > 0:
            lines.append(f"    |y(Use +touchstone to add)|n")
        
        # Acclimation
        acclimation = deviant_data['acclimation']
        acclimation_cost = deviant_data['acclimation_merit_cost']
        if acclimation_cost > 0:
            lines.append(f"  |wAcclimation:|n  {acclimation} ({acclimation_cost} merit dots)")
        else:
            lines.append(f"  |wAcclimation:|n  {acclimation} (starts at 0)")
    
    def _add_geist_display(self, lines, geist_data, divider_color):
        """Add Sin-Eater/Geist-specific chargen information to the display."""
        lines.append(f"  |g{'=' * 80}|n")
        lines.append(f"  |gSIN-EATER TEMPLATE|n")
        lines.append(f"  |g{'=' * 80}|n")
        
        # Burden
        burden = geist_data['burden'].title() if geist_data['burden'] else '|rNot Set|n'
        lines.append(f"  |wBurden:|n       {burden}")
        
        # Haunt Affinities
        if geist_data['haunt_affinities']:
            affinity_str = ', '.join([h.title() for h in geist_data['haunt_affinities']])
            lines.append(f"  |wHaunt Affinity:|n {affinity_str}")
        
        # Root and Bloom
        root_status = '|gok!|n' if geist_data['has_root'] else '|rx|n'
        bloom_status = '|gok!|n' if geist_data['has_bloom'] else '|rx|n'
        lines.append(f"  |wRoot:|n         {root_status}    |wBloom:|n {bloom_status}")
        
        # Haunts
        haunt_dots = geist_data['haunt_dots']
        haunt_avail = geist_data['haunt_available']
        haunt_remaining = haunt_avail - haunt_dots
        haunt_color = '|g' if haunt_remaining >= 0 else '|r'
        
        lines.append(f"  |wHaunts:|n       {haunt_color}{haunt_dots}/{haunt_avail}|n  (Remaining: {haunt_color}{haunt_remaining}|n)")
        
        # Affinity check
        affinity_dots = geist_data['affinity_dots']
        affinity_status = '|g' if affinity_dots >= 2 else '|r'
        lines.append(f"    Affinity:  {affinity_status}{affinity_dots}|n (need at least 2 in affinity Haunts)")
        
        # List haunts taken
        if geist_data['haunts']:
            haunt_list = []
            for haunt_name, dots in geist_data['haunts'].items():
                haunt_lower = haunt_name.lower().replace(' ', '_')
                # Mark if affinity
                if haunt_lower in geist_data['haunt_affinities']:
                    haunt_list.append(f"{haunt_name.title()} {dots} |c(affinity)|n")
                else:
                    haunt_list.append(f"{haunt_name.title()} {dots}")
            lines.append(f"    Taken: {', '.join(haunt_list)}")
        
        # Key
        key_status = '|gok!|n' if geist_data['has_key'] else '|rx|n'
        if geist_data['keys']:
            key_names = ', '.join([k.replace('key:', '').replace('_', ' ').title() for k in geist_data['keys']])
            lines.append(f"  |wKey:|n          {key_status}  ({key_names})")
        else:
            lines.append(f"  |wKey:|n          {key_status}  |y(Reflects death circumstances)|n")
        
        # Ceremonies
        ceremony_count = geist_data['ceremonies_count']
        if ceremony_count > 0:
            lines.append(f"  |wCeremonies:|n   {ceremony_count}")
            for ceremony in geist_data['ceremonies']:
                ceremony_name = ceremony.replace('ceremony:', '').replace('_', ' ').title()
                lines.append(f"    - {ceremony_name}")
        
        # Synergy
        synergy = geist_data['synergy']
        synergy_cost = geist_data['synergy_merit_cost']
        if synergy_cost > 0:
            lines.append(f"  |wSynergy:|n      {synergy} (1 free + {synergy - 1} from merits = {synergy_cost} merit dots)")
        else:
            lines.append(f"  |wSynergy:|n      {synergy} (free dot)")
        
        # Free Merit
        tolerance_status = '|gok!|n' if geist_data['has_tolerance_biology'] else '|rx|n'
        lines.append(f"  |wTolerance for Biology:|n {tolerance_status}  (free merit)")
        
        # Touchstone
        touchstone_status = '|g(Merit taken)|n' if geist_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
        
        # Geist companion section
        lines.append(f"\n  |y{'~' * 80}|n")
        lines.append(f"  |yGEIST COMPANION|n")
        lines.append(f"  |y{'~' * 80}|n")
        
        # Geist Name
        name_status = '|gok!|n' if geist_data['has_geist_name'] else '|rx|n'
        if geist_data['geist_name']:
            lines.append(f"  |wName/Title:|n   {name_status}  {geist_data['geist_name']}")
        else:
            lines.append(f"  |wName/Title:|n   {name_status}  |y(Use +stat/geist geist_name=<title>)|n")
        
        # Geist Attributes
        geist_spent = geist_data['geist_attr_spent']
        geist_avail = geist_data['geist_attr_available']
        geist_remaining = geist_avail - geist_spent
        geist_color = '|g' if geist_remaining >= 0 else '|r'
        
        lines.append(f"  |wAttributes:|n   {geist_color}{geist_spent}/{geist_avail}|n  (Power/Finesse/Resistance)")
        
        power = geist_data['geist_power']
        finesse = geist_data['geist_finesse']
        resistance = geist_data['geist_resistance']
        lines.append(f"    Power: {power}, Finesse: {finesse}, Resistance: {resistance} (max 9 each)")
        
        # Geist Virtue and Vice
        virtue_status = '|gok!|n' if geist_data['has_geist_virtue'] else '|rx|n'
        vice_status = '|gok!|n' if geist_data['has_geist_vice'] else '|rx|n'
        
        if geist_data['geist_virtue']:
            lines.append(f"  |wVirtue:|n       {virtue_status}  {geist_data['geist_virtue']}")
        else:
            lines.append(f"  |wVirtue:|n       {virtue_status}  |y(Use +stat/geist virtue=<name>)|n")
        
        if geist_data['geist_vice']:
            lines.append(f"  |wVice:|n         {vice_status}  {geist_data['geist_vice']}")
        else:
            lines.append(f"  |wVice:|n         {vice_status}  |y(Use +stat/geist vice=<name>)|n")
        
        # Remembrance
        remembrance_status = '|gok!|n' if geist_data['has_remembrance'] else '|rx|n'
        lines.append(f"  |wRemembrance:|n  {remembrance_status}  |y(Memory image, use +stat/geist)|n")
        
        # Remembrance Trait
        trait_status = '|gok!|n' if geist_data['has_remembrance_trait'] else '|rx|n'
        if geist_data['remembrance_trait']:
            lines.append(f"  |wRemembrance Trait:|n {trait_status}  {geist_data['remembrance_trait']}")
        else:
            lines.append(f"  |wRemembrance Trait:|n {trait_status}  |y(Skill or Merit ≤3)|n")
        
        # Crisis Point
        crisis_status = '|gok!|n' if geist_data['has_crisis_point'] else '|rx|n'
        if geist_data['crisis_point']:
            lines.append(f"  |wCrisis Point:|n {crisis_status}  {geist_data['crisis_point']}")
        else:
            lines.append(f"  |wCrisis Point:|n {crisis_status}  |y(Use +stat/geist crisis_point=<trigger>)|n")
        
        # Geist Rank
        rank = geist_data['geist_rank']
        lines.append(f"  |wRank:|n         {rank} (3 default, higher with Dread Geist merit)")
        
        # Ban and Bane
        ban_status = '|gok!|n' if geist_data['has_ban'] else '|rx|n'
        bane_status = '|gok!|n' if geist_data['has_bane'] else '|rx|n'
        
        if geist_data['geist_ban']:
            lines.append(f"  |wBan:|n          {ban_status}  {geist_data['geist_ban']}")
        else:
            lines.append(f"  |wBan:|n          {ban_status}  |y(Use +stat/geist ban=<restriction>)|n")
        
        if geist_data['geist_bane']:
            lines.append(f"  |wBane:|n         {bane_status}  {geist_data['geist_bane']}")
        else:
            lines.append(f"  |wBane:|n         {bane_status}  |y(Use +stat/geist bane=<weakness>)|n")
        
        # Innate Key
        key_status = '|gok!|n' if geist_data['has_innate_key'] else '|rx|n'
        if geist_data['innate_key']:
            lines.append(f"  |wInnate Key:|n   {key_status}  {geist_data['innate_key']}")
        else:
            lines.append(f"  |wInnate Key:|n   {key_status}  |y(Use +stat/geist innate_key=<key>)|n")
    
    def _add_hunter_display(self, lines, hunter_data, divider_color):
        """Add Hunter-specific chargen information to the display."""
        lines.append(f"  |y{'=' * 80}|n")
        lines.append(f"  |yHUNTER TEMPLATE|n")
        lines.append(f"  |y{'=' * 80}|n")
        
        # Tier and Organization
        tier = hunter_data['tier']
        org_type = hunter_data['org_type'] if hunter_data['org_type'] else 'Unknown'
        lines.append(f"  |wTier:|n         {tier} ({org_type})")
        
        if tier == 1:
            # Tier 1: Individual cell
            profession = hunter_data.get('profession', '')
            if profession:
                lines.append(f"  |wProfession:|n   {profession.replace('_', ' ').title()}")
            lines.append(f"  |wCell:|n         Independent (no formal organization)")
        else:
            # Tier 2+: Compact or Conspiracy
            organization = hunter_data['organization']
            if organization:
                lines.append(f"  |w{org_type}:|n      {organization.replace('_', ' ').title()}")
            else:
                lines.append(f"  |w{org_type}:|n      |rNot Set|n")
        
        # Tactics (all tiers get 3)
        tactics = hunter_data['tactics']
        tactics_count = hunter_data['tactics_count']
        expected_tactics = hunter_data['expected_tactics']
        tactics_color = '|g' if tactics_count >= expected_tactics else '|r'
        
        lines.append(f"  |wTactics:|n      {tactics_color}{tactics_count}/{expected_tactics}|n  (cell favored tactics)")
        if tactics:
            for tactic in tactics:
                lines.append(f"    - {tactic.replace('_', ' ').title()}")
        else:
            lines.append(f"    |y(Use +stat tactics=<tactic1,tactic2,tactic3>)|n")
        
        lines.append(f"    |c(Gain 8-again when performing these tactics)|n")
        
        # Status (Tier 2+ only)
        if tier >= 2:
            if hunter_data['has_status']:
                status_dots = hunter_data['status_dots']
                if status_dots >= 1:
                    lines.append(f"  |w{org_type} Status:|n |gok!|n  ({status_dots} dot{'s' if status_dots > 1 else ''}, 1 free)")
                else:
                    lines.append(f"  |w{org_type} Status:|n |yPresent but no dots set|n")
            else:
                lines.append(f"  |w{org_type} Status:|n |rx|n  |y(Get Status merit, 1 free)|n")
        
        # Endowments (Tier 3 only)
        if tier == 3:
            endowments = hunter_data['endowments']
            endowments_count = hunter_data['endowments_count']
            expected_endowments = hunter_data['expected_endowments']
            endowments_color = '|g' if endowments_count >= expected_endowments else '|r'
            
            lines.append(f"  |wEndowments:|n   {endowments_color}{endowments_count}/{expected_endowments}|n  (conspiracy powers)")
            if endowments:
                for endowment in endowments:
                    endowment_name = endowment.replace('endowment:', '').replace('_', ' ').title()
                    lines.append(f"    - {endowment_name}")
            else:
                lines.append(f"    |y(Use +stat endowment:<name>=known)|n")
    
    def _add_mummy_display(self, lines, mummy_data, divider_color):
        """Add Mummy/Arisen-specific chargen information to the display."""
        lines.append(f"  |y{'=' * 80}|n")
        lines.append(f"  |yMUMMY (ARISEN) TEMPLATE|n")
        lines.append(f"  |y{'=' * 80}|n")
        
        # Decree, Guild, Judge
        decree_name = mummy_data.get('decree_name', 'Unknown')
        guild = mummy_data['guild'].replace('_', ' ').title() if mummy_data['guild'] else '|rNot Set|n'
        judge = mummy_data['judge'].replace('_', ' ').title() if mummy_data['judge'] else '|yNone|n'
        
        lines.append(f"  |wDecree:|n       {decree_name}")
        lines.append(f"  |wGuild:|n        {guild}")
        if mummy_data['guild_vessel']:
            lines.append(f"    Vessel: {mummy_data['guild_vessel']}")
        lines.append(f"  |wJudge:|n        {judge}")
        
        # Balance and Burden (Mummy's anchors)
        balance_status = '|gok!|n' if mummy_data['has_balance'] else '|rx|n'
        burden_status = '|gok!|n' if mummy_data['has_burden'] else '|rx|n'
        lines.append(f"  |wBalance:|n      {balance_status}    |wBurden:|n {burden_status}")
        lines.append(f"    |c(Mummy's Virtue/Vice equivalents)|n")
        
        # Pillars
        pillar_total = mummy_data['pillar_total']
        pillar_avail = mummy_data['pillar_available']
        pillar_remaining = pillar_avail - pillar_total
        pillar_color = '|g' if pillar_remaining >= 0 else '|r'
        
        lines.append(f"  |wPillars:|n      {pillar_color}{pillar_total}/{pillar_avail}|n  (5 aspects of soul)")
        
        # Show pillar breakdown
        pillars = mummy_data['pillars']
        defining_pillar = mummy_data['defining_pillar']
        pillar_parts = []
        
        for pillar_name in ['ab', 'ba', 'ka', 'ren', 'sheut']:
            dots = pillars.get(pillar_name, 0)
            if dots > 0:
                # Mark defining pillar
                if pillar_name == defining_pillar:
                    pillar_parts.append(f"{pillar_name.title()} {dots} |c(defining)|n")
                else:
                    pillar_parts.append(f"{pillar_name.title()} {dots}")
        
        if pillar_parts:
            lines.append(f"    {', '.join(pillar_parts)}")
        
        # Validation: defining pillar must be highest
        if not mummy_data['defining_pillar_is_highest'] and defining_pillar:
            lines.append(f"    |rWarning: {defining_pillar.title()} (defining) must be highest|n")
        
        # Affinities
        affinities_count = mummy_data['affinities_count']
        expected_affinities = mummy_data['expected_affinities']
        affinity_color = '|g' if affinities_count >= expected_affinities else '|r'
        
        lines.append(f"  |wAffinities:|n   {affinity_color}{affinities_count}/{expected_affinities}|n")
        lines.append(f"    |c(1 decree + 1 guild + 2 soul)|n")
        
        if mummy_data['decree_affinity']:
            affinity_display = mummy_data['decree_affinity'].replace('_', ' ').title()
            lines.append(f"    Decree: {affinity_display} (automatic)")
        
        if mummy_data['affinities']:
            for affinity in mummy_data['affinities']:
                affinity_name = affinity.replace('affinity:', '').replace('_', ' ').title()
                lines.append(f"    - {affinity_name}")
        
        # Utterances
        utterances_count = mummy_data['utterances_count']
        expected_utterances = mummy_data['expected_utterances']
        utterance_color = '|g' if utterances_count >= expected_utterances else '|r'
        
        lines.append(f"  |wUtterances:|n   {utterance_color}{utterances_count}/{expected_utterances}|n")
        
        dreams_status = '|gok!|n' if mummy_data['has_dreams_of_dead_gods'] else '|rx|n'
        lines.append(f"    Dreams of Dead Gods: {dreams_status} (automatic)")
        
        if mummy_data['utterances']:
            for utterance in mummy_data['utterances']:
                if 'dreams' not in utterance.lower():
                    utterance_name = utterance.replace('utterance:', '').replace('_', ' ').title()
                    lines.append(f"    - {utterance_name}")
        
        # Memory and Sekhem
        memory = mummy_data['memory']
        sekhem = mummy_data['sekhem']
        lines.append(f"  |wMemory:|n       {memory} (starts at 3)")
        lines.append(f"  |wSekhem:|n       {sekhem} (starts at 8-10 based on awakening)")
        
        # Free Merits
        cult_status = '|gok!|n' if mummy_data['has_cult'] else '|rx|n'
        tomb_status = '|gok!|n' if mummy_data['has_tomb'] else '|rx|n'
        
        cult_dots = mummy_data['cult_dots']
        tomb_dots = mummy_data['tomb_dots']
        
        if cult_dots >= 1:
            lines.append(f"  |wCult:|n         {cult_status}  ({cult_dots} dot{'s' if cult_dots > 1 else ''}, 1 free)")
        else:
            lines.append(f"  |wCult:|n         {cult_status}  |y(Get Cult merit, 1 free)|n")
        
        if tomb_dots >= 1:
            lines.append(f"  |wTomb:|n         {tomb_status}  ({tomb_dots} dot{'s' if tomb_dots > 1 else ''}, 1 free)")
        else:
            lines.append(f"  |wTomb:|n         {tomb_status}  |y(Get Tomb merit, 1 free)|n")
        
        # Touchstone
        lines.append(f"  |wTouchstone:|n   |y(Use +touchstone, need 1)|n")
    
    def _add_promethean_display(self, lines, promethean_data, divider_color):
        """Add Promethean-specific chargen information to the display."""
        lines.append(f"  |c{'=' * 80}|n")
        lines.append(f"  |cPROMETHEAN TEMPLATE|n")
        lines.append(f"  |c{'=' * 80}|n")
        
        # Lineage and Refinement
        lineage = promethean_data['lineage'].title() if promethean_data['lineage'] else '|rNot Set|n'
        refinement = promethean_data['refinement'].title() if promethean_data['refinement'] else '|rNot Set|n'
        role = promethean_data['role'].replace('_', ' ').title() if promethean_data['role'] else '|yNone|n'
        
        lines.append(f"  |wLineage:|n      {lineage}")
        lines.append(f"  |wRefinement:|n   {refinement}")
        if promethean_data['role']:
            lines.append(f"  |wRole:|n         {role}")
        
        # Elpis and Torment
        elpis_status = '|gok!|n' if promethean_data['has_elpis'] else '|rx|n'
        torment_status = '|gok!|n' if promethean_data['has_torment'] else '|rx|n'
        lines.append(f"  |wElpis:|n        {elpis_status}    |wTorment:|n {torment_status}")
        
        # Bestowment
        bestowment_status = '|gok!|n' if promethean_data['has_bestowment'] else '|rx|n'
        
        if promethean_data['bestowments']:
            bestowment_names = ', '.join([b.replace('bestowment:', '').replace('_', ' ').title() for b in promethean_data['bestowments']])
            lines.append(f"  |wBestowment:|n   {bestowment_status}  {bestowment_names}")
        else:
            lines.append(f"  |wBestowment:|n   {bestowment_status}")
            if promethean_data['bestowment_options']:
                options_str = ' or '.join(promethean_data['bestowment_options'])
                lines.append(f"    Options: {options_str}")
        
        # Transmutations/Alembics
        alembics_count = promethean_data['alembics_count']
        expected_alembics = promethean_data['expected_alembics']
        alembic_color = '|g' if alembics_count >= expected_alembics else '|r'
        
        lines.append(f"  |wAlembics:|n     {alembic_color}{alembics_count}/{expected_alembics}|n  (manifestations of transmutations)")
        
        # Show refinement transmutations
        if promethean_data['refinement_transmutations']:
            trans_str = ', '.join([t.title() for t in promethean_data['refinement_transmutations']])
            lines.append(f"    Refinement grants: {trans_str}")
        
        # List alembics taken
        if promethean_data['alembics']:
            alembic_list = []
            for alembic in promethean_data['alembics']:
                alembic_name = alembic.replace('alembic:', '').replace('_', ' ').title()
                alembic_list.append(alembic_name)
            lines.append(f"    Taken: {', '.join(alembic_list)}")
        
        # List transmutations (if any are set as powers)
        if promethean_data['transmutations']:
            trans_list = []
            for trans_name, dots in promethean_data['transmutations'].items():
                trans_list.append(f"{trans_name.title()} {dots}")
            if trans_list:
                lines.append(f"    Transmutations: {', '.join(trans_list)}")
        
        # Azoth and Pyros
        azoth = promethean_data['azoth']
        pyros = promethean_data['pyros']
        max_pyros = promethean_data['max_pyros']
        
        lines.append(f"  |wAzoth:|n        {azoth} (starts at 1, Divine Fire strength)")
        lines.append(f"  |wPyros:|n        {pyros}/{max_pyros} (fuel, starts at half max)")
        
        # Pilgrimage
        pilgrimage = promethean_data['pilgrimage']
        lines.append(f"  |wPilgrimage:|n   {pilgrimage} (progress toward humanity, starts at 1)")
        
        # Touchstone
        touchstone_status = '|g(Merit taken)|n' if promethean_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
        lines.append(f"    |c(1 associated with Role/Pilgrimage)|n")
        
        # Pilgrimage Questions reminder
        lines.append(f"\n  |cPilgrimage Questions:|n |y(Use +bio to answer)|n")
        lines.append(f"    - What sort of human do you want to be?")
        lines.append(f"    - How have humans taught you to fear and hate?")
        lines.append(f"    - How did you split with your creator?")
        lines.append(f"    - What keeps you on the Pilgrimage?")
        lines.append(f"    - What would you give up to become human?")
    
    def _add_mortalplus_display(self, lines, mortalplus_data, divider_color):
        """Add Mortal+ template-specific chargen information to the display."""
        template_type = mortalplus_data.get('template_type', '').lower()
        
        if template_type == 'ghoul':
            self._add_ghoul_display(lines, mortalplus_data, divider_color)
        elif template_type == 'revenant':
            self._add_revenant_display(lines, mortalplus_data, divider_color)
        elif template_type == 'dhampir':
            self._add_dhampir_display(lines, mortalplus_data, divider_color)
        elif template_type in ['wolf-blooded', 'wolf_blooded', 'wolfblooded']:
            self._add_wolfblooded_display(lines, mortalplus_data, divider_color)
        elif template_type == 'psychic':
            self._add_psychic_display(lines, mortalplus_data, divider_color)
        elif template_type == 'atariya':
            self._add_atariya_display(lines, mortalplus_data, divider_color)
        elif template_type == 'infected':
            self._add_infected_display(lines, mortalplus_data, divider_color)
        elif template_type == 'plain':
            self._add_plain_display(lines, mortalplus_data, divider_color)
        elif template_type in ['lost_boy', 'lost boy']:
            self._add_lostboy_display(lines, mortalplus_data, divider_color)
        elif template_type in ['psychic_vampire', 'psychic vampire']:
            self._add_psychicvampire_display(lines, mortalplus_data, divider_color)
        elif template_type in ['immortal', 'endless']:
            self._add_immortal_display(lines, mortalplus_data, divider_color)
        elif template_type == 'proximus':
            self._add_proximus_display(lines, mortalplus_data, divider_color)
        elif template_type == 'sleepwalker':
            self._add_sleepwalker_display(lines, mortalplus_data, divider_color)
        elif template_type in ['fae-touched', 'fae_touched', 'faetouched']:
            self._add_faetouched_display(lines, mortalplus_data, divider_color)
        else:
            # Generic Mortal+ display
            lines.append(f"  |w{'=' * 80}|n")
            lines.append(f"  |wMORTAL+ TEMPLATE|n")
            lines.append(f"  |w{'=' * 80}|n")
            if template_type:
                lines.append(f"  |wType:|n         {template_type.replace('_', ' ').title()}")
            else:
                lines.append(f"  |wType:|n         |rNot Set|n")
                lines.append(f"    |y(Use +stat template_type=<type>)|n")
    
    def _add_ghoul_display(self, lines, ghoul_data, divider_color):
        """Add Ghoul-specific chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rGHOUL (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Regnant's Clan
        clan = ghoul_data['clan'].title() if ghoul_data['clan'] else '|rNot Set|n'
        lines.append(f"  |wRegnant Clan:|n {clan}")
        
        # Blood Potency
        bp = ghoul_data['blood_potency']
        lines.append(f"  |wBlood Potency:|n {bp} (always 0, cannot increase)")
        
        # Disciplines
        disc_dots = ghoul_data['discipline_dots']
        disc_avail = ghoul_data['discipline_available']
        disc_remaining = disc_avail - disc_dots
        disc_color = '|g' if disc_remaining >= 0 else '|r'
        
        lines.append(f"  |wDisciplines:|n  {disc_color}{disc_dots}/{disc_avail}|n (from regnant's in-clan)")
        
        if ghoul_data['disciplines']:
            disc_list = []
            for disc_name, dots in ghoul_data['disciplines'].items():
                disc_lower = disc_name.lower().replace(' ', '_')
                if disc_lower in ghoul_data['in_clan_disciplines']:
                    disc_list.append(f"{disc_name.title()} {dots} |c(in-clan)|n")
                else:
                    disc_list.append(f"{disc_name.title()} {dots}")
            lines.append(f"    Taken: {', '.join(disc_list)}")
    
    def _add_revenant_display(self, lines, revenant_data, divider_color):
        """Add Revenant-specific chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rREVENANT (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Family Clan
        clan = revenant_data['clan'].title() if revenant_data['clan'] else '|yNone|n'
        lines.append(f"  |wFamily Clan:|n  {clan}")
        
        # Blood Potency
        bp = revenant_data['blood_potency']
        lines.append(f"  |wBlood Potency:|n {bp} (1 for revenants, cannot increase)")
        
        # Mask, Dirge, Touchstone
        mask_status = '|gok!|n' if revenant_data['has_mask'] else '|rx|n'
        dirge_status = '|gok!|n' if revenant_data['has_dirge'] else '|rx|n'
        lines.append(f"  |wMask:|n         {mask_status}    |wDirge:|n {dirge_status}")
        
        touchstone_status = '|g(Merit taken)|n' if revenant_data['has_touchstone_merit'] else '|y(Use +touchstone)|n'
        lines.append(f"  |wTouchstone:|n   {touchstone_status}")
        
        # Disciplines
        disc_dots = revenant_data['discipline_dots']
        disc_avail = revenant_data['discipline_available']
        disc_remaining = disc_avail - disc_dots
        disc_color = '|g' if disc_remaining >= 0 else '|r'
        
        phys_dots = revenant_data['physical_discipline_dots']
        phys_status = '|g' if phys_dots >= 1 else '|r'
        
        lines.append(f"  |wDisciplines:|n  {disc_color}{disc_dots}/{disc_avail}|n")
        lines.append(f"    Physical: {phys_status}{phys_dots}|n (need at least 1)")
        lines.append(f"    |c(No unique clan disciplines)|n")
        
        if revenant_data['disciplines']:
            disc_list = []
            for disc_name, dots in revenant_data['disciplines'].items():
                disc_list.append(f"{disc_name.title()} {dots}")
            lines.append(f"    Taken: {', '.join(disc_list)}")
    
    def _add_dhampir_display(self, lines, dhampir_data, divider_color):
        """Add Dhampir-specific chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rDHAMPIR (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Parent Clan
        parent_clan = dhampir_data['parent_clan'].title() if dhampir_data['parent_clan'] else '|rNot Set|n'
        lines.append(f"  |wParent Clan:|n  {parent_clan}")
        
        # Destiny, Doom, Affliction
        destiny = dhampir_data['destiny'] if dhampir_data['destiny'] else '|yNone|n'
        doom = dhampir_data['doom'] if dhampir_data['doom'] else '|yNone|n'
        affliction = dhampir_data['affliction'] if dhampir_data['affliction'] else '|yNone|n'
        
        lines.append(f"  |wDestiny:|n      {destiny}")
        lines.append(f"  |wDoom:|n         {doom}")
        lines.append(f"  |wAffliction:|n   {affliction}")
        
        # Required Merits
        blood_sense_status = '|gok!|n' if dhampir_data['has_blood_sense'] else '|rx|n'
        omen_status = '|gok!|n' if dhampir_data['has_omen_sensitivity'] else '|rx|n'
        fate_status = '|gok!|n' if dhampir_data['has_thief_of_fate'] else '|rx|n'
        
        lines.append(f"  |wBlood Sense:|n  {blood_sense_status}  (free merit)")
        lines.append(f"  |wOmen Sensitivity:|n {omen_status}  (free merit)")
        lines.append(f"  |wThief of Fate:|n {fate_status}  (free merit)")
        
        # Themes
        if dhampir_data['parent_themes']:
            themes_str = ', '.join([t.title() for t in dhampir_data['parent_themes']])
            themes_status = '|gok!|n' if dhampir_data['parent_themes_set'] else '|rx|n'
            lines.append(f"  |wClan Themes:|n  {themes_status}  ({themes_str})")
            lines.append(f"    |c(1 dot each in parent clan themes)|n")
        
        # Twists
        twist_dots = dhampir_data['twist_dots']
        twist_avail = dhampir_data['twist_available']
        twist_remaining = twist_avail - twist_dots
        twist_color = '|g' if twist_remaining >= 0 else '|r'
        
        lines.append(f"  |wTwists:|n       {twist_color}{twist_dots}/{twist_avail}|n (free dots + clan unique)")
        
        if dhampir_data['twists']:
            twist_list = []
            for twist_name, dots in dhampir_data['twists'].items():
                display_name = twist_name.replace('twist:', '').replace('_', ' ').title()
                twist_list.append(f"{display_name} {dots}")
            lines.append(f"    Taken: {', '.join(twist_list)}")
        
        # Malisons (optional)
        if dhampir_data['malisons']:
            malison_list = [m.replace('malison:', '').replace('_', ' ').title() for m in dhampir_data['malisons']]
            lines.append(f"  |wMalisons:|n     {len(malison_list)} (3 merit dots each)")
            for malison in malison_list:
                lines.append(f"    - {malison}")
    
    def _add_wolfblooded_display(self, lines, wolfblooded_data, divider_color):
        """Add Wolf-Blooded-specific chargen information."""
        lines.append(f"  |c{'=' * 80}|n")
        lines.append(f"  |cWOLF-BLOODED (MORTAL+)|n")
        lines.append(f"  |c{'=' * 80}|n")
        
        # Tell
        tell = wolfblooded_data['tell'].replace('_', ' ').title() if wolfblooded_data['tell'] else '|rNot Set|n'
        tell_status = '|gok!|n' if wolfblooded_data['has_tell'] else '|rx|n'
        
        lines.append(f"  |wTell:|n         {tell_status}  {tell}")
        lines.append(f"    |c(Inherited trait from werewolf ancestry)|n")
    
    def _add_psychic_display(self, lines, psychic_data, divider_color):
        """Add Psychic-specific chargen information."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |bPSYCHIC (MORTAL+)|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Psychic Merits
        merit_count = len(psychic_data['psychic_merits'])
        merit_dots = psychic_data['psychic_merit_dots']
        
        if merit_count > 0:
            lines.append(f"  |wPsychic Merits:|n {merit_count} merits ({merit_dots} dots total)")
            for merit in psychic_data['psychic_merits']:
                lines.append(f"    - {merit}")
        else:
            lines.append(f"  |wPsychic Merits:|n |yNone purchased yet|n")
            lines.append(f"    |c(Purchase psychic merits like Telepathy, Telekinesis, etc.)|n")
    
    def _add_atariya_display(self, lines, atariya_data, divider_color):
        """Add Atariya-specific chargen information."""
        lines.append(f"  |y{'=' * 80}|n")
        lines.append(f"  |yATARIYA (MORTAL+)|n")
        lines.append(f"  |y{'=' * 80}|n")
        
        # Damn Lucky Merit
        damn_lucky_status = '|gok!|n' if atariya_data['has_damn_lucky'] else '|rx|n'
        lines.append(f"  |wDamn Lucky:|n   {damn_lucky_status}  (required merit)")
        lines.append(f"    |c(Caught attention of luck itself)|n")
    
    def _add_infected_display(self, lines, infected_data, divider_color):
        """Add Infected-specific chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rINFECTED (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Carrier Merit
        carrier_status = '|gok!|n' if infected_data['has_carrier'] else '|rx|n'
        lines.append(f"  |wCarrier:|n      {carrier_status}  (1 dot, free)")
        lines.append(f"  |wCondition:|n    Latent Symptoms (starts with this)")
        lines.append(f"    |c(Disease that doesn't behave normally)|n")
    
    def _add_plain_display(self, lines, plain_data, divider_color):
        """Add Plain-specific chargen information."""
        lines.append(f"  |w{'=' * 80}|n")
        lines.append(f"  |wPLAIN (MORTAL+)|n")
        lines.append(f"  |w{'=' * 80}|n")
        
        # Plain Reader Merit
        reader_status = '|gok!|n' if plain_data['has_plain_reader'] else '|rx|n'
        lines.append(f"  |wPlain Reader:|n {reader_status}  (free merit)")
        lines.append(f"    |c(Devoted to radical nonviolence)|n")
        
        # Other Plain Merits
        if plain_data['plain_merits']:
            lines.append(f"  |wPlain Merits:|n  {len(plain_data['plain_merits'])}")
            for merit in plain_data['plain_merits']:
                lines.append(f"    - {merit}")
    
    def _add_lostboy_display(self, lines, lostboy_data, divider_color):
        """Add Lost Boy (Delta Protocol) chargen information."""
        lines.append(f"  |r{'=' * 80}|n")
        lines.append(f"  |rLOST BOY / DELTA PROTOCOL (MORTAL+)|n")
        lines.append(f"  |r{'=' * 80}|n")
        
        # Protocol Merit
        protocol_status = '|gok!|n' if lostboy_data['has_protocol'] else '|rx|n'
        protocol_dots = lostboy_data['protocol_dots']
        
        if protocol_dots > 0:
            lines.append(f"  |wProtocol:|n     {protocol_status}  Mk {protocol_dots} (1 free)")
        else:
            lines.append(f"  |wProtocol:|n     {protocol_status}  |y(Get Protocol merit, 1 free)|n")
        
        lines.append(f"    |c(Augmentation level, determines withdrawal rate)|n")
        
        # Protocol Augmentation Merits
        if lostboy_data['protocol_merits']:
            lines.append(f"  |wAugmentations:|n {len(lostboy_data['protocol_merits'])}")
            for merit in lostboy_data['protocol_merits']:
                lines.append(f"    - {merit}")
        
        lines.append(f"\n    |rWarning: Requires Serum or suffers withdrawal|n")
    
    def _add_psychicvampire_display(self, lines, psychicvamp_data, divider_color):
        """Add Psychic Vampire chargen information."""
        lines.append(f"  |m{'=' * 80}|n")
        lines.append(f"  |mPSYCHIC VAMPIRE (MORTAL+)|n")
        lines.append(f"  |m{'=' * 80}|n")
        
        # Psychic Vampirism Merit
        vampirism_status = '|gok!|n' if psychicvamp_data['has_psychic_vampirism'] else '|rx|n'
        vampirism_dots = psychicvamp_data['vampirism_dots']
        
        if vampirism_dots > 0:
            lines.append(f"  |wPsychic Vampirism:|n {vampirism_status}  {vampirism_dots} dot{'s' if vampirism_dots > 1 else ''} (1 free)")
        else:
            lines.append(f"  |wPsychic Vampirism:|n {vampirism_status}  |y(Get merit, 1 free)|n")
        
        # Ephemera
        ephemera = psychicvamp_data['ephemera']
        max_ephemera = psychicvamp_data['max_ephemera']
        lines.append(f"  |wEphemera:|n     {ephemera}/{max_ephemera} (psychic fuel, max = Resolve)")
        lines.append(f"    |c(Steals life energy, loses 1/day)|n")
        
        # Ephemeral Battery
        if psychicvamp_data['has_ephemeral_battery']:
            lines.append(f"  |wEphemeral Battery:|n |gok!|n (increases storage)")
        
        # Relic option
        if psychicvamp_data['has_relic']:
            lines.append(f"  |wRelic-Bound:|n  |gok!|n (bonus merit dot)")
    
    def _add_immortal_display(self, lines, immortal_data, divider_color):
        """Add Immortal (Endless) chargen information."""
        lines.append(f"  |y{'=' * 80}|n")
        lines.append(f"  |yIMMORTAL / ENDLESS (MORTAL+)|n")
        lines.append(f"  |y{'=' * 80}|n")
        
        # Immortality Type
        immortal_name = immortal_data['immortal_name']
        subtype = immortal_data['subtype']
        
        if subtype:
            lines.append(f"  |wType:|n         {immortal_name}")
        else:
            lines.append(f"  |wType:|n         |rNot Set|n")
            lines.append(f"    |y(Use +stat subtype=<type>)|n")
            lines.append(f"    Options: blood_bather, body_thief, mystical_thief,")
            lines.append(f"             psychic_thief, eternal, reborn")
        
        # Favored Attribute
        favored_attr = immortal_data['favored_attribute']
        if favored_attr:
            attr_display = favored_attr.title()
            if immortal_data['has_favored_attr']:
                lines.append(f"  |wFavored Attr:|n  |gok!|n  {attr_display} |c(free dot)|n")
            else:
                lines.append(f"  |wFavored Attr:|n  |rx|n  {attr_display} |y(use +stat/favored)|n")
        
        # Endless Potency
        if immortal_data['has_endless_potency']:
            potency_dots = immortal_data['potency_dots']
            lines.append(f"  |wEndless Potency:|n |gok!|n  {potency_dots} dot{'s' if potency_dots > 1 else ''} (1 free in {favored_attr.title()})")
        elif favored_attr:
            lines.append(f"  |wEndless Potency:|n |rx|n  |y(Get Endless Potency: {favored_attr.title()} merit, 1 free)|n")
        
        # Virtue and Vice
        virtue_status = '|gok!|n' if immortal_data['has_virtue'] else '|rx|n'
        vice_status = '|gok!|n' if immortal_data['has_vice'] else '|rx|n'
        lines.append(f"  |wVirtue:|n       {virtue_status}    |wVice:|n {vice_status}")
        
        # Curse/Method
        if immortal_data['has_curse_method']:
            lines.append(f"  |wMethod/Curse:|n {immortal_data['curse_method']}")
        else:
            lines.append(f"  |wMethod/Curse:|n |y(Describe immortality process)|n")
        
        # Sekhem
        sekhem = immortal_data['sekhem']
        lines.append(f"  |wSekhem:|n       {sekhem} (starts at 1, max 5)")
        
        # Type-specific features
        if subtype == 'blood_bather':
            lines.append(f"\n  |cBlood Bather Aspects:|n")
            lines.append(f"    - Bathed in Life (ritual heals damage, maintains youth)")
            lines.append(f"    - Sacrificial Secrets (+6 starting XP)")
            lines.append(f"    - Strong Immune System (immune to natural disease)")
            lines.append(f"    |rIntegrity starts at 5 (not 7)|n")
        
        elif subtype in ['body_thief', 'mystical_thief', 'psychic_thief']:
            lines.append(f"\n  |cBody Thief Aspects:|n")
            lines.append(f"    - Borrowed Prowess (keeps Mental/Social, takes Physical)")
            lines.append(f"    - Steal Sense (borrow victim's sense for +2 bonus)")
            lines.append(f"    - Unobtrusive (fade into crowds, +Sekhem to blend)")
        
        elif subtype == 'eternal':
            # Relic
            if immortal_data['has_relic']:
                relic_dots = immortal_data['relic_dots']
                lines.append(f"  |wRelic:|n        |gok!|n  {relic_dots} dot{'s' if relic_dots > 1 else ''} (1 free, anchor)")
            else:
                lines.append(f"  |wRelic:|n        |rx|n  |y(Get Relic merit, 1 free)|n")
            
            lines.append(f"\n  |cEternal Aspects:|n")
            lines.append(f"    - Appraisal (detect powers/curses in objects)")
            lines.append(f"    - Consequence Free (shunt Conditions to anchor)")
            lines.append(f"    - Vital Shell (cannot die while anchor exists)")
        
        elif subtype == 'reborn':
            lines.append(f"\n  |cReborn Aspects:|n")
            lines.append(f"    - Dreams of Lives Unlived (fated visions)")
            lines.append(f"    - Solid Integrity (+2 to breaking points)")
            lines.append(f"    - Untrained Ease (no unskilled penalties)")
        
        # Investment (Mummy Cult)
        if immortal_data['has_investment']:
            lines.append(f"\n  |wMummy Investment:|n {immortal_data['investment']}")
            if immortal_data['invested_pillars']:
                lines.append(f"    |c(Can use master's Tier 1 Utterances)|n")
        else:
            lines.append(f"\n  |wMummy Investment:|n |yNone (optional)|n")
    
    def _add_proximus_display(self, lines, proximus_data, divider_color):
        """Add Proximus-specific chargen information."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |bPROXIMUS (MORTAL+)|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Dynasty
        dynasty = proximus_data['dynasty'].replace('_', ' ').title() if proximus_data['dynasty'] else '|yNone|n'
        lines.append(f"  |wDynasty:|n      {dynasty}")
        
        # Parent Path
        parent_path = proximus_data['parent_path'].title() if proximus_data['parent_path'] else '|rNot Set|n'
        lines.append(f"  |wParent Path:|n  {parent_path}")
        
        # Blessing Arcana
        if proximus_data['ruling_arcana']:
            ruling_str = ', '.join([a.title() for a in proximus_data['ruling_arcana']])
            lines.append(f"    Ruling: {ruling_str}")
        
        chosen = proximus_data['chosen_arcanum']
        if chosen:
            lines.append(f"    Chosen: {chosen.title()}")
        else:
            lines.append(f"    Chosen: |yNone|n |y(Use +stat blessing_arcanum=<name>)|n")
        
        # Blessings (as merits, max 30 dots)
        blessing_dots = proximus_data['blessing_dots']
        max_blessings = proximus_data['max_blessings']
        blessing_remaining = max_blessings - blessing_dots
        blessing_color = '|g' if blessing_remaining >= 0 else '|r'
        
        lines.append(f"  |wBlessings:|n    {blessing_color}{blessing_dots}/{max_blessings}|n dots (purchased as merits)")
        
        if proximus_data['blessings']:
            for blessing in proximus_data['blessings'][:5]:  # Show first 5
                blessing_name = blessing.replace('blessing:', '').replace('_', ' ').title()
                lines.append(f"    - {blessing_name}")
            if len(proximus_data['blessings']) > 5:
                lines.append(f"    ... and {len(proximus_data['blessings']) - 5} more")
        
        # Mana
        mana = proximus_data['mana']
        max_mana = proximus_data['max_mana']
        lines.append(f"  |wMana:|n         {mana}/{max_mana} (always max 5 for Proximi)")
        
        # Familial Curse
        curse_status = '|gok!|n' if proximus_data['has_curse'] else '|rx|n'
        if proximus_data['curse']:
            lines.append(f"  |wFamilial Curse:|n {curse_status}")
            lines.append(f"    {proximus_data['curse']}")
        else:
            lines.append(f"  |wFamilial Curse:|n {curse_status}  |y(Set curse description)|n")
        
        lines.append(f"\n    |c(Persistent Condition from bloodline)|n")
    
    def _add_sleepwalker_display(self, lines, sleepwalker_data, divider_color):
        """Add Sleepwalker-specific chargen information."""
        lines.append(f"  |b{'=' * 80}|n")
        lines.append(f"  |bSLEEPWALKER (MORTAL+)|n")
        lines.append(f"  |b{'=' * 80}|n")
        
        # Sleepwalker Merit
        sleepwalker_status = '|gok!|n' if sleepwalker_data['has_sleepwalker'] else '|rx|n'
        lines.append(f"  |wSleepwalker:|n  {sleepwalker_status}  (1 dot, free)")
        lines.append(f"    |c(Immune to Curse, cause no Dissonance)|n")
        
        # Sleepwalker Merits
        if sleepwalker_data['sleepwalker_merits']:
            lines.append(f"  |wSleepwalker Merits:|n {len(sleepwalker_data['sleepwalker_merits'])}")
            for merit in sleepwalker_data['sleepwalker_merits']:
                lines.append(f"    - {merit}")
        else:
            lines.append(f"  |wSleepwalker Merits:|n |yNone purchased yet|n")
            lines.append(f"    |c(Can assist mages with rituals)|n")
    
    def _add_faetouched_display(self, lines, faetouched_data, divider_color):
        """Add Fae-Touched-specific chargen information."""
        lines.append(f"  |m{'=' * 80}|n")
        lines.append(f"  |mFAE-TOUCHED (MORTAL+)|n")
        lines.append(f"  |m{'=' * 80}|n")
        
        # Promise
        promise_status = '|gok!|n' if faetouched_data['has_promise'] else '|rx|n'
        if faetouched_data['promise']:
            lines.append(f"  |wPromise:|n      {promise_status}")
            lines.append(f"    {faetouched_data['promise']}")
            if faetouched_data['promise_type']:
                lines.append(f"    Type: {faetouched_data['promise_type'].title()}")
        else:
            lines.append(f"  |wPromise:|n      {promise_status}  |y(Set promise description)|n")
        
        lines.append(f"    |c(Grants +1 die to actions that fortify promise)|n")
        
        # Wyrd (always 0)
        wyrd = faetouched_data['wyrd']
        if wyrd == 0:
            lines.append(f"  |wWyrd:|n         {wyrd} |g(correct, always 0)|n")
        else:
            lines.append(f"  |wWyrd:|n         {wyrd} |r(should be 0!)|n")
        
        # Glamour
        glamour = faetouched_data['glamour']
        max_glamour = faetouched_data['max_glamour']
        lines.append(f"  |wGlamour:|n      {glamour}/{max_glamour} (can bank up to 10)")
        lines.append(f"    |c(Harvest from emotions or Hedge bounty)|n")
        
        # Favored Regalia
        favored_regalia = faetouched_data.get('favored_regalia', None)
        if favored_regalia:
            lines.append(f"  |wFavored Regalia:|n {favored_regalia.title()} |gok!|n")
        else:
            lines.append(f"  |wFavored Regalia:|n |rx|n |y(Use +stat favored regalia=<name>)|n")
        
        # Contracts
        contract_count = faetouched_data['contract_count']
        expected_contracts = faetouched_data['expected_contracts']
        contract_color = '|g' if contract_count >= expected_contracts else '|r'
        
        lines.append(f"  |wContracts:|n    {contract_color}{contract_count}/{expected_contracts}|n (Common from favored Regalia)")
        
        if faetouched_data['contracts']:
            for contract in faetouched_data['contracts']:
                contract_name = contract.replace('contract:', '').replace('_', ' ').title()
                lines.append(f"    - {contract_name}")
        
        # Court Goodwill (for Court Contracts)
        if faetouched_data['court_goodwill']:
            lines.append(f"  |wCourt Goodwill:|n")
            for court, dots in faetouched_data['court_goodwill'].items():
                court_name = court.replace('goodwill:', '').replace('_', ' ').title()
                lines.append(f"    {court_name}: {dots}")
        
        # Fae-Touched Merits
        if faetouched_data['faetouched_merits']:
            lines.append(f"  |wFae-Touched Merits:|n {len(faetouched_data['faetouched_merits'])}")
            for merit in faetouched_data['faetouched_merits']:
                lines.append(f"    - {merit}")
        
        # Starting Conditions (warnings)
        lines.append(f"\n  |rStarting Conditions:|n")
        lines.append(f"    - Madness (Hedge exposure)")
        lines.append(f"    - Arcadian Dreams")
        lines.append(f"    - Hedge Addiction")
        
        # Limitations
        lines.append(f"\n  |cLimitations:|n")
        lines.append(f"    - Cannot use Loopholes in Contracts")
        lines.append(f"    - Must be taught Contracts (cannot learn alone)")
        lines.append(f"    - Cannot auto-gain seeming benefits")
        lines.append(f"    - Cannot enter own dreams naturally")
    
    def get_display_desc(self, looker, **kwargs):
        """
        Override the room description to show chargen progress instead.
        
        Args:
            looker: The character viewing the room
            **kwargs: Additional arguments
            
        Returns:
            str: Chargen progress display instead of room description
        """
        # Return chargen display as the room description
        chargen_display = self.get_chargen_display(looker)
        
        if chargen_display:
            return chargen_display
        else:
            # Fallback to regular description if no chargen data
            return super().get_display_desc(looker, **kwargs)