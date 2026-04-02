"""
Building Commands

Commands for world building including areas, rooms, and mapping.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.evtable import EvTable
from evennia.utils import create, utils
from evennia.utils.search import search_object
from evennia.server.models import ServerConfig
from utils.text import process_special_characters
from world.area_manager import get_area_manager
from world.utils.permission_utils import check_staff_permission
from world.utils import ansi_subs  # noqa: F401
from world.utils.formatting import get_theme_colors
import re
import time


class CmdAreaManage(MuxCommand):
    """
    Manage game areas and their codes.
    
    Usage:
      +area/list - List all defined areas
      +area/add <code>=<name>/<description> - Add a new area
      +area/remove <code> - Remove an area (if no rooms use it)
      +area/info <code> - Show detailed info about an area
      +area/rooms <code> - List all rooms in an area
      +area/init - Initialize/reset area manager (admin only)
      
    Examples:
      +area/list
      +area/add TW=The Thorns/Twisted pathways of the deep Hedge
      +area/info HE
      +area/rooms HE
      +area/remove TW
      +area/init
    """
    
    key = "+area"
    locks = "cmd:perm(builders)"
    help_category = "Building Commands"
    
    def func(self):
        caller = self.caller
        area_manager = get_area_manager()
        
        if not self.switches:
            caller.msg("Usage: +area/list, +area/add, +area/remove, +area/info, +area/rooms, +area/init")
            return
        
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_areas(area_manager)
        elif switch == "add":
            self.add_area(area_manager)
        elif switch == "remove":
            self.remove_area(area_manager)
        elif switch == "info":
            self.area_info(area_manager)
        elif switch == "rooms":
            self.list_area_rooms(area_manager)
        elif switch == "init":
            self.init_area_manager(area_manager)
        else:
            caller.msg("Valid switches: /list, /add, /remove, /info, /rooms, /init")
    
    def list_areas(self, area_manager):
        """List all defined areas."""
        areas = area_manager.get_areas()
        width = 78
        header_color, text_color, _ = get_theme_colors()

        def centered_dash_line(text):
            label = f" {text} "
            if len(label) >= width:
                return f"|{text_color}{label}|n"
            left = (width - len(label)) // 2
            right = width - len(label) - left
            return (
                f"|{header_color}{'-' * left}|n"
                f"|{text_color}{label}|n"
                f"|{header_color}{'-' * right}|n"
            )

        lines = [
            centered_dash_line("Area Directory"),
            "",
            f"|{text_color}Use +area/info <code> for details and +area/rooms <code> to list room mappings.|n",
            centered_dash_line("Defined Areas"),
        ]

        for code, info in sorted(areas.items()):
            room_count = len(info['rooms'])
            next_num = info['next_room']
            room_label = "room" if room_count == 1 else "rooms"
            lines.append(
                f"|{text_color}{code}|n {info['name']} - {room_count} {room_label} - "
                f"next: |{text_color}{code}{next_num:02d}|n"
            )

        lines.append(f"|{header_color}{'-' * width}|n")
        self.caller.msg("\n".join(lines))
    
    def add_area(self, area_manager):
        """Add a new area."""
        if not self.args or "=" not in self.args:
            self.caller.msg("Usage: +area/add <code>=<name>/<description>")
            return
        
        code, rest = self.args.split("=", 1)
        code = code.strip().upper()
        
        if "/" in rest:
            name, description = rest.split("/", 1)
            name = name.strip()
            description = description.strip()
        else:
            name = rest.strip()
            description = ""
        
        if len(code) != 2:
            self.caller.msg("Area code must be exactly 2 characters.")
            return
        
        success, message = area_manager.add_area(code, name, description)
        self.caller.msg(message)
    
    def remove_area(self, area_manager):
        """Remove an area."""
        if not self.args:
            self.caller.msg("Usage: +area/remove <code>")
            return
        
        code = self.args.strip().upper()
        success, message = area_manager.remove_area(code)
        self.caller.msg(message)
    
    def area_info(self, area_manager):
        """Show detailed information about an area."""
        if not self.args:
            self.caller.msg("Usage: +area/info <code>")
            return
        
        code = self.args.strip().upper()
        info = area_manager.get_area_info(code)
        
        if not info:
            self.caller.msg(f"Area code {code} not found.")
            return
        
        self.caller.msg(f"|wArea Information: {code}|n")
        self.caller.msg(f"Name: {info['name']}")
        self.caller.msg(f"Description: {info['description'] or 'No description set'}")
        self.caller.msg(f"Next Room Number: {code}{info['next_room']:02d}")
        self.caller.msg(f"Total Rooms: {len(info['rooms'])}")
        
        if info['rooms']:
            self.caller.msg(f"\nRoom Numbers: {', '.join([f'{code}{num:02d}' for num in sorted(info['rooms'].keys())])}")
    
    def list_area_rooms(self, area_manager):
        """List all rooms in an area."""
        if not self.args:
            self.caller.msg("Usage: +area/rooms <code>")
            return
        
        code = self.args.strip().upper()
        info = area_manager.get_area_info(code)
        
        if not info:
            self.caller.msg(f"Area code {code} not found.")
            return
        
        rooms = info['rooms']
        if not rooms:
            self.caller.msg(f"No rooms found in area {code}.")
            return
        
        table = EvTable("Room Code", "Room Name", "DB#", border="cells")
        
        for room_num in sorted(rooms.keys()):
            room_id = rooms[room_num]
            room_obj = search_object(f"#{room_id}")
            
            room_code = f"{code}{room_num:02d}"
            
            if room_obj:
                room_name = room_obj[0].name
                table.add_row(room_code, room_name, f"#{room_id}")
            else:
                table.add_row(room_code, "|rDeleted Room|n", f"#{room_id}")
        
        self.caller.msg(f"Rooms in Area {code} ({info['name']}):\n{table}")
    
    def init_area_manager(self, area_manager):
        """Initialize/reset the area manager (admin only)."""
        if not self.caller.check_permstring("admin"):
            self.caller.msg("Only administrators can initialize the area manager.")
            return
        
        # Force re-initialization
        area_manager._init_default_areas()
        self.caller.msg("Area manager initialized with default areas.")
        
        # Show the areas
        areas = area_manager.get_areas()
        self.caller.msg(f"Initialized {len(areas)} default areas: {', '.join(areas.keys())}")


class CmdRoomSetup(MuxCommand):
    """
    Set up room area information and display properties.
    
    Usage:
      +room/area here=<area_code>           - Set area and auto-assign room code
      +room/area <target>=<area_code>
      +room/code here=<specific_code>       - Manual override of room code (advanced)
      +room/code <target>=<specific_code>
      +room/coords here=<x>,<y>             - Set room coordinates for mapping
      +room/coords <target>=<x>,<y>
      +room/hierarchy here=<location1>,<location2>
      +room/hierarchy <target>=<location1>,<location2>
      +room/places here=on/off
      +room/places <target>=on/off
      +room/tag <target>=<tag1>,<tag2>,...  - Set room tags (comma-separated)
      +room/tags <target>                   - View room tags
      +room/hisil <target>=<description>    - Set Shadow/Hisil description
      +room/gauntlet <target>=<0-5>         - Set Gauntlet strength rating
      +room/chargen <target>=on/off         - Convert room to/from ChargenRoom typeclass
      +room/lock <exit>=<rules>             - Lock an exit in your current room
      +room/unlock <exit>                   - Remove lock from an exit in your current room
      +room/hide <exit>=<rules>             - Hide an exit with template/type/stat/merit visibility rules
      +room/unhide <exit>                   - Make a hidden exit visible to all again
      
    Target must be specified:
      - 'here' for current room
      - Room name (e.g., "The Square")
      - Database reference (e.g., "#123")
      
    How it works:
      - Use /area with a 2-letter area code (HE, SH, WD, CT)
      - This automatically sets the area name and assigns the next room code
      - Use /code only for manual overrides of specific room codes
      - Use /coords to set room position for ASCII maps
      
    Examples:
      +room/area here=HE               - Set current room to Hedge area
      +room/area #123=SH               - Set room #123 to Shadow area
      +room/code here=HE05             - Manual override to set current room to HE05
      +room/coords here=10,5           - Set current room coordinates for mapping
      +room/hierarchy here=The Square,New Redoubt
      +room/places here=on
      +room/tag here=library,research          - Tag room for investigation purposes
      +room/tags here                          - View current room tags
      +room/hisil here=A twisted reflection...  - Set Shadow description
      +room/gauntlet here=3                     - Set Gauntlet strength
      +room/chargen here=on                     - Convert room to ChargenRoom (shows point tracking)
      +room/lock Main Door=templates:changeling,mage;streetwise:3
      +room/unlock Main Door
      +room/hide Hedge Gate=changeling
      +room/hide Avernian Gate=geist
      +room/hide Tomb Gate=mummy
      +room/hide Secret Door=changeling;mortalplus:fae_touched;streetwise:3;merit:status=2
    
    Common Room Tags:
      Research & Knowledge:
        library, occult_library, archive, computer, research, scriptorium,
        museum, university, laboratory, observatory, clinic, morgue
      
      Social & Gathering:
        bar, nightclub, restaurant, cafe, theater, church, synagogue, mosque,
        gathering_hall, marketplace, stadium, playground, park
      
      Supernatural:
        locus, consecrated, desecrated, hollow, verge, nexus, ley_line,
        haunted, possessed, tainted, blessed, cursed, warded, elysium,
        shadow, underworld, arcadia, hedge, supernal, freehold, consilium,
        sanctum, avernian_gate, dead_road, goblin_market, 
      
      Investigation:
        crime_scene, evidence_room, interrogation, surveillance, safe_house,
        black_market, underground, hidden, secret, restricted
      
      Functional:
        workshop, forge, armory, vault, treasury, stable, garage, warehouse,
        storage, kitchen, infirmary, training_ground, ritual_chamber
      
      Time Period Specific:
        ancient (ruins, catacombs, temple, amphitheater, stadium, bathhouse, forum, agora)
        medieval (castle, monastery, scriptorium, dungeon, keep, bailey)
        victorian (parlor, ballroom, gentlemens_club, opium_den, factory)
        modern (office, apartment, penthouse, parking_garage, server_room)
    """
    
    key = "+room"
    locks = "cmd:perm(builders)"
    help_category = "Building Commands"
    
    def parse(self):
        """
        Custom parsing to handle switch=value and target=value syntax.
        """
        super().parse()
        
        # Parse the arguments to handle both formats:
        # +room/switch=value (no target, use current room)
        # +room/switch target=value (specific target)
        
        self.target_room = None
        self.switch_value = None
        
        if self.switches and self.args:
            args = self.args.strip()
            
            # Check if there's a target specified (format: target=value)
            if '=' in args:
                target_part, value_part = args.split('=', 1)
                target_part = target_part.strip()
                value_part = value_part.strip()
                
                # Target is now required - no empty target allowed
                if not target_part:
                    self.target_room = None  # Will cause error in func()
                    self.switch_value = None
                else:
                    # Format was /switch target=value
                    self.target_room = target_part
                    self.switch_value = value_part
            else:
                # No = found, invalid syntax
                self.target_room = None
                self.switch_value = None
        elif self.switches:
            # Switch but no args - will show usage error
            self.target_room = "here"
            self.switch_value = None
        else:
            # No switches, handle old syntax in func()
            self.target_room = None
            self.switch_value = None
    
    def get_target_room(self, target_str):
        """
        Resolve a target string to a room object.
        
        Args:
            target_str (str): Target specification ('here', room name, or #dbref)
            
        Returns:
            Room object or None if not found
        """
        if not target_str or target_str.lower() == "here":
            return self.caller.location
        
        # Handle database reference (#123)
        if target_str.startswith('#'):
            try:
                dbref = int(target_str[1:])
                rooms = search_object(f"#{dbref}")
                if rooms and hasattr(rooms[0], 'location') and rooms[0].location is None:
                    # Verify it's actually a room (rooms have location=None)
                    return rooms[0]
            except ValueError:
                pass
        
        # Handle room name search
        rooms = search_object(target_str, typeclass='typeclasses.rooms.Room')
        if rooms:
            return rooms[0]
        
        # Fallback: try general search and filter for rooms
        objects = search_object(target_str)
        for obj in objects:
            if hasattr(obj, 'location') and obj.location is None:
                # This is likely a room
                return obj
        
        return None

    def _normalize_lock_id(self, value):
        return str(value or "").strip().lower().replace("-", "_").replace(" ", "_")

    def _parse_visibility_groups(self, raw_groups):
        """
        Parse visibility groups for hidden exits.
        """
        alias_map = {
            "sin_eater": "geist",
            "sin_eaters": "geist",
            "sineater": "geist",
            "sineaters": "geist",
            "hunters": "hunter",
            "mummies": "mummy",
        }
        allowed = {
            "changeling", "geist", "werewolf", "vampire",
            "mage", "promethean", "deviant", "demon", "hunter", "mummy",
        }
        parsed = []
        for group in raw_groups.split(","):
            normalized = self._normalize_lock_id(group)
            if not normalized:
                continue
            normalized = alias_map.get(normalized, normalized)
            if normalized not in allowed:
                raise ValueError(
                    f"Unknown group '{group.strip()}'. "
                    f"Allowed: {', '.join(sorted(allowed))}"
                )
            parsed.append(normalized)
        parsed = sorted(set(parsed))
        if not parsed:
            raise ValueError("You must specify at least one group.")
        return parsed

    def _parse_hide_rules(self, raw_rules):
        """
        Parse hidden-exit visibility requirements.

        Supported examples:
          changeling
          changeling,mummy
          changeling;streetwise:3;merit:status=2
          templates:changeling,mage;mortalplus:fae_touched
        """
        raw_rules = (raw_rules or "").strip()
        if not raw_rules:
            raise ValueError("No hide rules supplied.")

        # Simple form: "<group1>,<group2>"
        if ";" not in raw_rules and ":" not in raw_rules:
            return {
                "templates": self._parse_visibility_groups(raw_rules),
                "mortalplus": [],
                "stats": [],
                "merits": [],
            }

        attribute_fields = {
            "strength", "dexterity", "stamina", "presence", "manipulation",
            "composure", "intelligence", "wits", "resolve",
        }
        skill_fields = {
            "academics", "computer", "crafts", "investigation", "medicine",
            "occult", "politics", "science", "athletics", "brawl", "drive",
            "firearms", "larceny", "stealth", "survival", "weaponry",
            "animal_ken", "empathy", "expression", "intimidation",
            "persuasion", "socialize", "streetwise", "subterfuge",
        }

        parsed = {
            "templates": [],
            "mortalplus": [],
            "stats": [],
            "merits": [],
        }

        tokenized = [token.strip() for token in raw_rules.split(";") if token.strip()]
        for token in tokenized:
            if ":" not in token:
                parsed["templates"].extend(self._parse_visibility_groups(token))
                continue

            key, value = token.split(":", 1)
            key = self._normalize_lock_id(key)
            value = value.strip()

            if key in {"template", "templates", "group", "groups"}:
                parsed["templates"].extend(self._parse_visibility_groups(value))
                continue

            if key in {"mortalplus", "mortal_plus", "type", "template_type"}:
                values = [self._normalize_lock_id(v) for v in value.split(",") if v.strip()]
                parsed["mortalplus"].extend(values)
                continue

            if key == "skill":
                # Legacy support: skill:streetwise=3
                match = re.match(r"^\s*([a-zA-Z_][a-zA-Z0-9_ ]*)\s*(>=|<=|==|=|>|<)?\s*(\d+)\s*$", value)
                if not match:
                    raise ValueError(f"Invalid skill rule '{token}'.")
                stat_name, operator, amount = match.groups()
                normalized_op = ">="
                if operator in {"<=", "<"}:
                    normalized_op = operator
                parsed["stats"].append(
                    {
                        "name": self._normalize_lock_id(stat_name),
                        "op": normalized_op,
                        "value": int(amount),
                    }
                )
                continue

            if key in attribute_fields or key in skill_fields:
                match = re.match(r"^\s*(>=|<=|==|=|>|<)?\s*(\d+)\s*$", value)
                if not match:
                    raise ValueError(f"Invalid stat requirement '{token}'. Use {key}:3.")
                operator, amount = match.groups()
                normalized_op = ">="
                if operator in {"<=", "<"}:
                    normalized_op = operator
                parsed["stats"].append(
                    {
                        "name": key,
                        "op": normalized_op,
                        "value": int(amount),
                    }
                )
                continue

            if key in {"merit", "merits"}:
                # merit:status=2,resources=3 OR merit:status (defaults to 1+)
                merit_parts = [part.strip() for part in value.split(",") if part.strip()]
                if not merit_parts:
                    raise ValueError("Merit rules must include at least one merit.")
                for merit_part in merit_parts:
                    merit_match = re.match(
                        r"^\s*([a-zA-Z0-9_ \-]+)\s*(>=|<=|==|=|>|<)?\s*(\d+)?\s*$",
                        merit_part,
                    )
                    if not merit_match:
                        raise ValueError(f"Invalid merit requirement '{merit_part}'.")
                    merit_name, operator, amount = merit_match.groups()
                    normalized_op = ">="
                    if operator in {"<=", "<"}:
                        normalized_op = operator
                    parsed["merits"].append(
                        {
                            "name": self._normalize_lock_id(merit_name),
                            "op": normalized_op,
                            "value": int(amount) if amount else 1,
                        }
                    )
                continue

            # Allow a comma-list of template groups inside any unknown key only if value is empty.
            raise ValueError(
                f"Unknown hide rule key '{key}'. "
                "Use templates:, mortalplus:, <stat>:<value>, or merit:."
            )

        parsed["templates"] = sorted(set(parsed["templates"]))
        parsed["mortalplus"] = sorted(set(parsed["mortalplus"]))

        unique_stats = {}
        for req in parsed["stats"]:
            unique_stats[(req["name"], req["op"], req["value"])] = req
        parsed["stats"] = list(unique_stats.values())

        unique_merits = {}
        for req in parsed["merits"]:
            unique_merits[(req["name"], req["op"], req["value"])] = req
        parsed["merits"] = list(unique_merits.values())

        if not (parsed["templates"] or parsed["mortalplus"] or parsed["stats"] or parsed["merits"]):
            raise ValueError("No valid hide rules were supplied.")
        return parsed

    def _parse_lock_rules(self, raw_rules):
        """
        Parse room-entry rules from a semicolon-separated string.

        Supported tokens:
          staff (preferred), players / staffonly (legacy)
          template:<a,b,c>
          templates:<a,b,c>
          mortalplus:<a,b,c>
          skill:<name><op><value>   (legacy/optional)
          <stat_name>:<value>       (preferred, minimum-threshold)
          bio:<field>=<a,b,c>
          court:<a,b> / seeming:<a,b> / kith:<a,b> / tribe:<a,b> ...
        """
        tokenized = [token.strip() for token in raw_rules.split(";") if token.strip()]
        if not tokenized:
            raise ValueError("No lock rules supplied.")

        rules = {
            "staff_only": False,
            "templates": [],
            "mortalplus": [],
            "skills": [],
            "stats": [],
            "bio": {},
        }

        direct_bio_fields = {
            "court", "seeming", "kith", "tribe", "auspice",
            "clan", "order", "path", "guild", "decree",
            "judge", "cult", "tomb", "needle", "thread",
            "subtype", "profession", "organization", "creed",
        }
        attribute_fields = {
            "strength", "dexterity", "stamina", "presence", "manipulation",
            "composure", "intelligence", "wits", "resolve",
        }
        skill_fields = {
            "academics", "computer", "crafts", "investigation", "medicine",
            "occult", "politics", "science", "athletics", "brawl", "drive",
            "firearms", "larceny", "stealth", "survival", "weaponry",
            "animal_ken", "empathy", "expression", "intimidation",
            "persuasion", "socialize", "streetwise", "subterfuge",
        }

        for token in tokenized:
            lower = token.lower()

            if lower in {"staff", "players", "staffonly", "staff_only"}:
                rules["staff_only"] = True
                continue

            if ":" not in token:
                raise ValueError(f"Invalid lock token '{token}'. Use key:value format.")

            key, value = token.split(":", 1)
            key = self._normalize_lock_id(key)
            value = value.strip()

            if key in {"template", "templates"}:
                values = [self._normalize_lock_id(v) for v in value.split(",") if v.strip()]
                rules["templates"].extend(values)
                continue

            if key in {"mortalplus", "mortal_plus", "type", "template_type"}:
                values = [self._normalize_lock_id(v) for v in value.split(",") if v.strip()]
                rules["mortalplus"].extend(values)
                continue

            if key == "skill":
                # Minimum requirement syntax (merit-prereq style):
                #   skill:streetwise=3   -> Streetwise 3+
                # Backward compatible with older operator forms.
                match = re.match(r"^\s*([a-zA-Z_][a-zA-Z0-9_ ]*)\s*(>=|<=|==|=|>|<)?\s*(\d+)\s*$", value)
                if not match:
                    raise ValueError(f"Invalid skill rule '{token}'.")
                skill_name, operator, amount = match.groups()
                # Use minimum requirement semantics by default.
                normalized_op = ">="
                if operator in {"<=", "<"}:
                    normalized_op = operator
                rules["skills"].append(
                    {
                        "name": self._normalize_lock_id(skill_name),
                        "op": normalized_op,
                        "value": int(amount),
                    }
                )
                continue

            # Preferred shorthand: streetwise:3, occult:2, presence:4, etc.
            if key in attribute_fields or key in skill_fields:
                match = re.match(r"^\s*(>=|<=|==|=|>|<)?\s*(\d+)\s*$", value)
                if not match:
                    raise ValueError(
                        f"Invalid stat requirement '{token}'. Use {key}:3 or {key}>=3."
                    )
                operator, amount = match.groups()
                normalized_op = ">="
                if operator in {"<=", "<"}:
                    normalized_op = operator
                rules["stats"].append(
                    {
                        "name": key,
                        "op": normalized_op,
                        "value": int(amount),
                    }
                )
                continue

            if key == "bio":
                if "=" not in value:
                    raise ValueError(f"Invalid bio rule '{token}'. Use bio:<field>=<value1,value2>.")
                field, values = value.split("=", 1)
                field = self._normalize_lock_id(field)
                parsed_values = [self._normalize_lock_id(v) for v in values.split(",") if v.strip()]
                if not parsed_values:
                    raise ValueError(f"Bio rule '{token}' has no values.")
                rules["bio"][field] = parsed_values
                continue

            if key in direct_bio_fields:
                parsed_values = [self._normalize_lock_id(v) for v in value.split(",") if v.strip()]
                if not parsed_values:
                    raise ValueError(f"Bio field rule '{token}' has no values.")
                rules["bio"][key] = parsed_values
                continue

            raise ValueError(f"Unknown lock rule key '{key}'.")

        # De-duplicate lists for cleaner storage.
        rules["templates"] = sorted(set(rules["templates"]))
        rules["mortalplus"] = sorted(set(rules["mortalplus"]))
        unique_stats = {}
        for req in rules["stats"]:
            unique_stats[(req["name"], req["op"], req["value"])] = req
        rules["stats"] = list(unique_stats.values())
        return rules

    def _get_room_exits(self, room):
        """
        Return exits that exist in the target room.
        """
        return list(room.exits)

    def _match_room_exits(self, room, exit_name):
        """
        Match current-room exits by key or alias.
        """
        target = self._normalize_lock_id(exit_name)
        room_exits = self._get_room_exits(room)
        matches = []
        for ex in room_exits:
            key_match = self._normalize_lock_id(ex.key) == target
            alias_match = any(self._normalize_lock_id(alias) == target for alias in ex.aliases.all())
            if key_match or alias_match:
                matches.append(ex)
        return matches
    
    def func(self):
        caller = self.caller
        switch = self.switches[0].lower() if self.switches else None
        
        # Determine target room
        if self.switches:
            # /lock, /unlock, /hide, /unhide operate on current room exits.
            if switch in ["lock", "unlock", "hide", "unhide"]:
                location = caller.location
                if not location:
                    caller.msg("You must be in a room to use this command.")
                    return
            else:
                # Using switch syntax, get target room
                target_room = self.get_target_room(self.target_room)
                if not target_room:
                    if self.target_room and self.target_room.lower() != "here":
                        caller.msg(f"Room '{self.target_room}' not found.")
                    else:
                        caller.msg("You must be in a room to use this command.")
                    return
                location = target_room
        else:
            # Using old syntax, use current location
            location = caller.location
            if not location:
                caller.msg("You must be in a room to use this command.")
                return
            
        # If no switches and no args, display current settings
        if not self.switches and not self.args:
            self.display_current_settings(location)
            return
            
        # Handle switch-based syntax
        if self.switches:
            # Check if target and value are properly specified.
            # /tags does not use "=", and /lock,/unlock,/hide,/unhide default to current room.
            if switch not in ["tags", "lock", "unlock", "hide", "unhide"] and (not self.target_room or not self.switch_value):
                caller.msg(f"Usage: +room/{switch} <target>=<value>")
                caller.msg("Target must be 'here', a room name, or #dbref")
                caller.msg(f"Example: +room/{switch} here=<value>")
                return
            
            # Handle /tags separately since it doesn't use = syntax
            if switch == "tags":
                if not self.target_room and self.args:
                    # Format: +room/tags here (no = sign)
                    self.target_room = self.args.strip()
                elif not self.target_room:
                    self.target_room = "here"
                
                # Get the target room
                target_room = self.get_target_room(self.target_room)
                if not target_room:
                    caller.msg(f"Room '{self.target_room}' not found.")
                    return
                
                room_info = f"#{target_room.id}" if target_room != caller.location else "here"
                tags = getattr(target_room.db, 'tags', []) or []
                if tags:
                    caller.msg(f"Room tags for {target_room.name} ({room_info}): {', '.join(tags)}")
                else:
                    caller.msg(f"No tags set for room {target_room.name} ({room_info})")
                return
            
            value = self.switch_value
                
            if switch == "area":
                # Area switch now expects a 2-letter area code and auto-assigns room code
                area_manager = get_area_manager()
                
                if len(value) != 2:
                    caller.msg("Area code must be exactly 2 letters (e.g., HE, SH, WD, CT). Use '+area/list' to see available areas.")
                    return
                
                area_code = value.upper()
                if not area_manager.validate_area_code(area_code):
                    caller.msg(f"Area code {area_code} is not defined. Use '+area/list' to see available areas.")
                    return
                
                # Get area info and auto-assign room code
                area_info = area_manager.get_area_info(area_code)
                full_code = area_manager.get_next_room_number(area_code)
                
                # Set both area name and room code
                location.db.area_name = area_info['name']
                location.db.area_code = full_code
                
                # Register with area manager
                room_number = int(full_code[2:])
                area_manager.register_room(area_code, room_number, location.id)
                
                room_info = f"#{location.id}" if location != caller.location else "here"
                caller.msg(f"Room assigned to area '{area_info['name']}' with code {full_code} for room {location.name} ({room_info})")
                
            elif switch == "code":
                # Code switch is for manual override of specific room codes only
                area_manager = get_area_manager()
                
                if len(value) != 4:
                    caller.msg("Room code must be exactly 4 characters (e.g., HE03). Use '+room/area=HE' for auto-assignment.")
                    return
                
                area_code = value[:2].upper()
                try:
                    room_number = int(value[2:])
                    full_code = f"{area_code}{room_number:02d}"
                except ValueError:
                    caller.msg("Invalid room code format. Must be like HE03.")
                    return
                
                if not area_manager.validate_area_code(area_code):
                    caller.msg(f"Area code {area_code} is not defined. Use '+area/list' to see available areas.")
                    return
                
                # Check if room number is already taken
                area_rooms = area_manager.get_area_rooms(area_code)
                if room_number in area_rooms and area_rooms[room_number] != location.id:
                    existing_room = search_object(f"#{area_rooms[room_number]}")
                    if existing_room:
                        caller.msg(f"Room code {full_code} is already assigned to: {existing_room[0].name}")
                        return
                
                # Set the room code and area name
                location.db.area_code = full_code
                area_info = area_manager.get_area_info(area_code)
                if area_info:
                    location.db.area_name = area_info['name']
                
                # Register with area manager
                area_manager.register_room(area_code, room_number, location.id)
                
                # Update next room number if this is higher
                if room_number >= area_info['next_room']:
                    area_manager.db.areas[area_code]['next_room'] = room_number + 1
                
                room_info = f"#{location.id}" if location != caller.location else "here"
                caller.msg(f"Room code manually set to {full_code} for room {location.name} ({room_info})")
                
            elif switch == "coords":
                # Set room coordinates for mapping
                area_manager = get_area_manager()
                
                if "," not in value:
                    caller.msg("Usage: +room/coords <target>=<x>,<y>")
                    return
                
                try:
                    x_str, y_str = value.split(",", 1)
                    x = int(x_str.strip())
                    y = int(y_str.strip())
                except ValueError:
                    caller.msg("Coordinates must be integers. Usage: +room/coords <target>=<x>,<y>")
                    return
                
                success = area_manager.set_room_coordinates(location.id, x, y)
                if success:
                    room_info = f"#{location.id}" if location != caller.location else "here"
                    caller.msg(f"Room coordinates set to ({x}, {y}) for room {location.name} ({room_info})")
                else:
                    caller.msg("Error setting room coordinates.")
                
            elif switch == "hierarchy":
                hierarchy = [item.strip() for item in value.split(",")]
                if len(hierarchy) != 2:
                    caller.msg("Hierarchy must have exactly 2 location names separated by commas.")
                    return
                location.db.location_hierarchy = hierarchy
                room_info = f"#{location.id}" if location != caller.location else "here"
                caller.msg(f"Location hierarchy set to '{' - '.join(hierarchy)}' for room {location.name} ({room_info})")
                
            elif switch == "places":
                room_info = f"#{location.id}" if location != caller.location else "here"
                if value.lower() in ["on", "true", "yes", "1"]:
                    location.db.places_active = True
                    caller.msg(f"Places system enabled for room {location.name} ({room_info})")
                elif value.lower() in ["off", "false", "no", "0"]:
                    location.db.places_active = False
                    caller.msg(f"Places system disabled for room {location.name} ({room_info})")
                else:
                    caller.msg("Places setting must be 'on' or 'off'.")
            
            elif switch == "tag":
                # Set room tags
                tags = [tag.strip() for tag in value.split(",") if tag.strip()]
                if not hasattr(location.db, 'tags') or location.db.tags is None:
                    location.db.tags = []
                location.db.tags = tags
                room_info = f"#{location.id}" if location != caller.location else "here"
                if tags:
                    caller.msg(f"Room tags set to: {', '.join(tags)} for room {location.name} ({room_info})")
                else:
                    caller.msg(f"Room tags cleared for room {location.name} ({room_info})")
            
            elif switch == "hisil":
                # Set Hisil/Shadow description
                hisil_desc = process_special_characters(value)
                location.db.hisil_desc = hisil_desc
                room_info = f"#{location.id}" if location != caller.location else "here"
                caller.msg(f"Hisil description set for room {location.name} ({room_info})")
                caller.msg(f"Preview:\n{hisil_desc}")
            
            elif switch == "gauntlet":
                # Set Gauntlet rating
                try:
                    gauntlet_strength = int(value)
                except ValueError:
                    caller.msg("Gauntlet strength must be a number between 0 and 5.")
                    return
                
                if gauntlet_strength < 0 or gauntlet_strength > 5:
                    caller.msg("Gauntlet strength must be between 0 and 5.")
                    return
                
                location.db.gauntlet_strength = gauntlet_strength
                
                # Show the rating with description
                strength_desc = {
                    0: "Verge (no Gauntlet)",
                    1: "Locus (+2 dice)",
                    2: "Wilderness (0 modifier)",
                    3: "Small town (-1 dice)",
                    4: "City suburbs (-2 dice)",
                    5: "Dense urban (-3 dice)"
                }
                
                room_info = f"#{location.id}" if location != caller.location else "here"
                caller.msg(f"Gauntlet strength set to {gauntlet_strength} for room {location.name} ({room_info})")
                caller.msg(f"Description: {strength_desc.get(gauntlet_strength, 'Unknown')}")
            
            elif switch == "chargen":
                # Convert room to/from ChargenRoom typeclass
                from evennia import create_object
                
                room_info = f"#{location.id}" if location != caller.location else "here"
                value_lower = value.lower()
                
                if value_lower in ["on", "true", "yes", "1"]:
                    # Convert to ChargenRoom
                    if location.typename == "ChargenRoom":
                        caller.msg(f"Room {location.name} ({room_info}) is already a ChargenRoom.")
                        return
                    
                    # Swap typeclass to ChargenRoom
                    from typeclasses.rooms import ChargenRoom
                    old_typeclass = location.typename
                    location.swap_typeclass("typeclasses.rooms.ChargenRoom", clean_attributes=False)
                    
                    # Ensure chargen and ooc tags are set
                    if not hasattr(location.db, 'tags') or not location.db.tags:
                        location.db.tags = []
                    if 'chargen' not in location.db.tags:
                        location.db.tags.append('chargen')
                    if 'ooc' not in location.db.tags:
                        location.db.tags.append('ooc')
                    
                    caller.msg(f"Room {location.name} ({room_info}) converted to ChargenRoom.")
                    caller.msg("This room will now display character generation progress for all characters present.")
                    caller.msg("Tags 'chargen' and 'ooc' have been automatically applied.")
                    
                elif value_lower in ["off", "false", "no", "0"]:
                    # Convert back to normal Room
                    if location.typename != "ChargenRoom":
                        caller.msg(f"Room {location.name} ({room_info}) is not a ChargenRoom.")
                        return
                    
                    # Swap typeclass back to normal Room
                    from typeclasses.rooms import Room
                    location.swap_typeclass("typeclasses.rooms.Room", clean_attributes=False)
                    
                    caller.msg(f"Room {location.name} ({room_info}) converted back to normal Room.")
                    caller.msg("Character generation progress display has been disabled.")
                else:
                    caller.msg("Chargen setting must be 'on' or 'off'.")

            elif switch == "lock":
                # Lock exits in this room with dynamic entry checks.
                lock_args = self.args.strip()
                if "=" not in lock_args:
                    caller.msg("Usage: +room/lock <exit>=<rules>")
                    caller.msg("Example: +room/lock Main Door=templates:changeling,mage;streetwise:3")
                    return

                exit_part, rule_part = lock_args.split("=", 1)
                exit_name = exit_part.strip()
                if not exit_name:
                    caller.msg("You must specify which inbound exit to lock.")
                    return

                try:
                    parsed_rules = self._parse_lock_rules(rule_part.strip())
                except ValueError as err:
                    caller.msg(f"Lock parse error: {err}")
                    return

                matches = self._match_room_exits(location, exit_name)
                if not matches:
                    caller.msg(f"No exits named '{exit_name}' were found in room {location.name}.")
                    return

                for ex in matches:
                    if ex.db.room_entry_prev_traverse is None:
                        ex.db.room_entry_prev_traverse = ex.locks.get("traverse")
                    ex.db.room_entry_requirements = parsed_rules
                    ex.db.room_entry_locked_by = caller
                    ex.locks.add("traverse:entrycheck()")

                room_info = f"#{location.id}" if location != caller.location else "here"
                caller.msg(
                    f"Applied room-entry lock to {len(matches)} exit(s) in "
                    f"{location.name} ({room_info})."
                )

            elif switch == "unlock":
                # Remove entry locks from exits in this room.
                unlock_args = self.args.strip()
                if "=" in unlock_args:
                    # Backward compatibility: +room/unlock <target>=<exit>
                    _, unlock_args = unlock_args.split("=", 1)

                exit_name = unlock_args.strip()
                if not exit_name:
                    caller.msg("Usage: +room/unlock <exit>")
                    return

                matches = self._match_room_exits(location, exit_name)
                if not matches:
                    caller.msg(f"No exits named '{exit_name}' were found in room {location.name}.")
                    return

                for ex in matches:
                    prev = ex.db.room_entry_prev_traverse
                    if prev:
                        ex.locks.add(f"traverse:{prev}")
                    else:
                        ex.locks.add("traverse:all()")
                    ex.attributes.remove("room_entry_requirements")
                    ex.attributes.remove("room_entry_locked_by")
                    ex.attributes.remove("room_entry_prev_traverse")

                room_info = f"#{location.id}" if location != caller.location else "here"
                caller.msg(
                    f"Removed room-entry lock from {len(matches)} exit(s) in "
                    f"{location.name} ({room_info})."
                )

            elif switch == "hide":
                hide_args = self.args.strip()
                if "=" not in hide_args:
                    caller.msg("Usage: +room/hide <exit>=<rules>")
                    caller.msg("Example: +room/hide Hedge Gate=changeling;streetwise:3;merit:status=2")
                    return
                exit_name, groups_text = hide_args.split("=", 1)
                exit_name = exit_name.strip()
                if not exit_name:
                    caller.msg("You must specify an exit name or alias to hide.")
                    return
                try:
                    visibility_rules = self._parse_hide_rules(groups_text)
                except ValueError as err:
                    caller.msg(str(err))
                    return

                matches = self._match_room_exits(location, exit_name)
                if not matches:
                    caller.msg(f"No exits named '{exit_name}' were found in room {location.name}.")
                    return

                for ex in matches:
                    if ex.db.exit_prev_view_lock is None:
                        ex.db.exit_prev_view_lock = ex.locks.get("view")
                    ex.db.exit_hidden = True
                    ex.db.exit_view_templates = visibility_rules.get("templates", [])
                    ex.db.exit_view_requirements = visibility_rules
                    ex.locks.add("view:exitviewcheck()")

                summary_bits = []
                if visibility_rules.get("templates"):
                    summary_bits.append(f"templates={','.join(visibility_rules['templates'])}")
                if visibility_rules.get("mortalplus"):
                    summary_bits.append(f"mortalplus={','.join(visibility_rules['mortalplus'])}")
                if visibility_rules.get("stats"):
                    summary_bits.append(f"stats={len(visibility_rules['stats'])}")
                if visibility_rules.get("merits"):
                    summary_bits.append(f"merits={len(visibility_rules['merits'])}")
                summary = "; ".join(summary_bits) if summary_bits else "rules applied"
                caller.msg(
                    f"Hidden {len(matches)} exit(s). {summary}."
                )

            elif switch == "unhide":
                exit_name = self.args.strip()
                if "=" in exit_name:
                    _, exit_name = exit_name.split("=", 1)
                exit_name = exit_name.strip()
                if not exit_name:
                    caller.msg("Usage: +room/unhide <exit>")
                    return

                matches = self._match_room_exits(location, exit_name)
                if not matches:
                    caller.msg(f"No exits named '{exit_name}' were found in room {location.name}.")
                    return

                for ex in matches:
                    prev_view = ex.db.exit_prev_view_lock
                    if prev_view:
                        ex.locks.add(f"view:{prev_view}")
                    else:
                        ex.locks.add("view:all()")
                    ex.attributes.remove("exit_hidden")
                    ex.attributes.remove("exit_view_templates")
                    ex.attributes.remove("exit_view_requirements")
                    ex.attributes.remove("exit_prev_view_lock")

                caller.msg(f"Unhid {len(matches)} exit(s) in {location.name}.")
                    
            else:
                caller.msg(
                    "Valid switches: /area, /code, /coords, /hierarchy, /places, /tag, "
                    "/tags, /hisil, /gauntlet, /chargen, /lock, /unlock, /hide, /unhide"
                )
        else:
            # Old syntax fallback for backwards compatibility
            if "=" not in self.args:
                caller.msg("Usage: +room/<switch> <target>=<value>")
                caller.msg("Target must be 'here', a room name, or #dbref")
                caller.msg("Example: +room/area here=HE")
                return
                
            setting, value = self.args.split("=", 1)
            setting = setting.strip().lower()
            value = value.strip()
            
            # For old syntax, assume 'here' as target
            caller.msg("Note: Old syntax detected. Please use: +room/<switch> here=<value>")
            caller.msg("Proceeding with current room as target...")
            
            if setting == "area":
                # Legacy syntax: treat as area code assignment
                area_manager = get_area_manager()
                
                if len(value) != 2:
                    caller.msg("Area code must be exactly 2 letters (e.g., HE, SH, WD, CT). Use '+area/list' to see available areas.")
                    return
                
                area_code = value.upper()
                if not area_manager.validate_area_code(area_code):
                    caller.msg(f"Area code {area_code} is not defined. Use '+area/list' to see available areas.")
                    return
                
                # Get area info and auto-assign room code
                area_info = area_manager.get_area_info(area_code)
                full_code = area_manager.get_next_room_number(area_code)
                
                # Set both area name and room code
                location.db.area_name = area_info['name']
                location.db.area_code = full_code
                
                # Register with area manager
                room_number = int(full_code[2:])
                area_manager.register_room(area_code, room_number, location.id)
                
                caller.msg(f"Room assigned to area '{area_info['name']}' with code {full_code}")
                
            elif setting == "code":
                # Legacy syntax: manual room code override
                area_manager = get_area_manager()
                
                if len(value) != 4:
                    caller.msg("Room code must be exactly 4 characters (e.g., HE03). Use 'area=HE' for auto-assignment.")
                    return
                
                area_code = value[:2].upper()
                try:
                    room_number = int(value[2:])
                    full_code = f"{area_code}{room_number:02d}"
                except ValueError:
                    caller.msg("Invalid room code format. Must be like HE03.")
                    return
                
                if not area_manager.validate_area_code(area_code):
                    caller.msg(f"Area code {area_code} is not defined. Use '+area/list' to see available areas.")
                    return
                
                # Set the room code and area name
                location.db.area_code = full_code
                area_info = area_manager.get_area_info(area_code)
                if area_info:
                    location.db.area_name = area_info['name']
                
                # Register with area manager
                area_manager.register_room(area_code, room_number, location.id)
                
                caller.msg(f"Room code manually set to {full_code}")
                
            elif setting == "hierarchy":
                hierarchy = [item.strip() for item in value.split(",")]
                if len(hierarchy) != 2:
                    caller.msg("Hierarchy must have exactly 2 location names separated by commas.")
                    return
                location.db.location_hierarchy = hierarchy
                caller.msg(f"Location hierarchy set to: {' - '.join(hierarchy)}")
                
            elif setting == "places":
                if value.lower() in ["on", "true", "yes", "1"]:
                    location.db.places_active = True
                    caller.msg("Places system enabled for this room.")
                elif value.lower() in ["off", "false", "no", "0"]:
                    location.db.places_active = False
                    caller.msg("Places system disabled for this room.")
                else:
                    caller.msg("Places setting must be 'on' or 'off'.")
                    
            else:
                caller.msg("Valid settings: area, code, hierarchy, places")
            
    def display_current_settings(self, location):
        """Display the current room settings."""
        table = EvTable("Setting", "Value", border="cells")
        
        table.add_row("Area Name", location.db.area_name or "Not set")
        table.add_row("Area Code", location.db.area_code or "Not set")
        
        hierarchy = location.db.location_hierarchy
        if hierarchy:
            # Convert _SaverList to regular list if needed
            if hasattr(hierarchy, '__iter__') and not isinstance(hierarchy, (str, bytes)):
                hierarchy = list(hierarchy)
            table.add_row("Hierarchy", " - ".join(hierarchy))
        else:
            table.add_row("Hierarchy", "Not set")
            
        table.add_row("Places Active", "Yes" if location.db.places_active else "No")
        
        # Show coordinates if set
        if hasattr(location.db, 'map_x') and hasattr(location.db, 'map_y'):
            table.add_row("Map Coordinates", f"({location.db.map_x}, {location.db.map_y})")
        else:
            table.add_row("Map Coordinates", "Not set")
        
        self.caller.msg(f"Room Settings for {location.name}:\n{table}")


class CmdPlaces(MuxCommand):
    """
    Add a place to the current room.
    
    Usage:
      places/add <name>=<description>
      places/remove <number>
      places/list or places
      places/info <number>
      
    Examples:
      places/add The Stone Pool=A shallow pool in the center of the square
      places/remove 5
      places/list
      places/info 5
    """
    
    key = "places"
    locks = "cmd:perm(builders)"
    help_category = "Building Commands"

    def func(self):
        caller = self.caller
        location = caller.location
        
        if not location:
            caller.msg("You must be in a room to use this command.")
            return
            
        places = getattr(location.db, 'places', {})
        if not places:
            caller.msg("No places defined in this room.")
            return
            
        table = EvTable("#", "Name", "Description", border="cells")
        
        for place_num in sorted(places.keys(), key=lambda x: int(x) if x.isdigit() else 0):
            place = places[place_num]
            table.add_row(place_num, place['name'], place['desc'][:50] + "..." if len(place['desc']) > 50 else place['desc'])
            
        caller.msg(f"Places in {location.name}:\n{table}")

    def func_add(self):
        caller = self.caller
        location = caller.location
        
        if not location:
            caller.msg("You must be in a room to use this command.")
            return
            
        if not self.args or "=" not in self.args:
            caller.msg("Usage: places/add <name>=<description> or places/add <number>:<name>=<description>")
            return
            
        # Check if we have a custom number
        place_number = None
        if ":" in self.args and self.args.split(":")[0].isdigit():
            number_part, rest = self.args.split(":", 1)
            place_number = int(number_part)
            name, desc = rest.split("=", 1)
        else:
            name, desc = self.args.split("=", 1)
            
        name = name.strip()
        desc = desc.strip()
        
        if not name or not desc:
            caller.msg("Both name and description are required.")
            return
        
        # Process special characters in the description
        desc = process_special_characters(desc)
            
        # Add the place using the room's method
        if hasattr(location, 'add_place'):
            place_num = location.add_place(name, desc, place_number)
            caller.msg(f"Place #{place_num} '{name}' added to {location.name}.")
        else:
            caller.msg("This room doesn't support the places system.")

    def func_remove(self):
        caller = self.caller
        location = caller.location
        
        if not location:
            caller.msg("You must be in a room to use this command.")
            return
            
        if not self.args or not self.args.isdigit():
            caller.msg("Usage: places/remove <number>")
            return
            
        place_num = self.args.strip()
        places = getattr(location.db, 'places', {})
        
        if place_num not in places:
            caller.msg(f"No place #{place_num} found in this room.")
            return
            
        place_name = places[place_num]['name']
        del places[place_num]
        location.db.places = places
        
        caller.msg(f"Place #{place_num} '{place_name}' removed from {location.name}.")
  
    def func_info(self):
        caller = self.caller
        location = caller.location
        
        if not location:
            caller.msg("You must be in a room to use this command.")
            return
            
        places = getattr(location.db, 'places', {})
        if not places:
            caller.msg("There are no special places to look at here.")
            return
            
        # If no argument, list all places
        if not self.args:
            table = EvTable("#", "Place", border="cells", width=60)
            for place_num in sorted(places.keys(), key=lambda x: int(x) if x.isdigit() else 0):
                place = places[place_num]
                table.add_row(place_num, place['name'])
            caller.msg(f"Places you can look at here:\n{table}")
            caller.msg("Use 'places/info <number>' or 'places/info <name>' to look at a specific place.")
            return
            
        search_term = self.args.strip().lower()
        
        # First try to find by number
        if search_term in places:
            place = places[search_term]
            caller.msg(f"|w{place['name']}|n\n{place['desc']}")
            return
            
        # Then try to find by name
        for place_num, place in places.items():
            if search_term in place['name'].lower():
                caller.msg(f"|w{place['name']}|n\n{place['desc']}")
                return
                
        caller.msg(f"No place matching '{self.args}' found here.")


class CmdRoomInfo(MuxCommand):
    """
    Display detailed information about the current room's settings.
    
    Usage:
      roominfo
    """
    
    key = "roominfo"
    locks = "cmd:perm(builders)"
    help_category = "Building Commands"
    
    def func(self):
        caller = self.caller
        location = caller.location
        
        if not location:
            caller.msg("You must be in a room to use this command.")
            return
            
        # Basic room info
        caller.msg(f"|wRoom Information for: {location.name}|n")
        caller.msg(f"Dbref: #{location.id}")
        caller.msg(f"Typeclass: {location.typename}")
        
        # Area info
        caller.msg(f"\n|cArea Information:|n")
        caller.msg(f"Area Name: {location.db.area_name or 'Not set'}")
        caller.msg(f"Area Code: {location.db.area_code or 'Not set'}")
        
        hierarchy = location.db.location_hierarchy
        if hierarchy:
            # Convert _SaverList to regular list if needed
            if hasattr(hierarchy, '__iter__') and not isinstance(hierarchy, (str, bytes)):
                hierarchy = list(hierarchy)
            caller.msg(f"Location Hierarchy: {' - '.join(hierarchy)}")
        else:
            caller.msg("Location Hierarchy: Not set")
            
        # Coordinates info
        if hasattr(location.db, 'map_x') and hasattr(location.db, 'map_y'):
            caller.msg(f"Map Coordinates: ({location.db.map_x}, {location.db.map_y})")
        else:
            caller.msg("Map Coordinates: Not set")
            
        # Places info
        caller.msg(f"\n|cPlaces System:|n")
        caller.msg(f"Places Active: {'Yes' if location.db.places_active else 'No'}")
        
        places = getattr(location.db, 'places', {})
        if places is None:
            places = {}
        caller.msg(f"Places Defined: {len(places)}")
        
        # Tags info
        caller.msg(f"\n|cRoom Tags:|n")
        tags = getattr(location.db, 'tags', []) or []
        if tags:
            caller.msg(f"Tags: {', '.join(tags)}")
        else:
            caller.msg("Tags: None")
        
        # Exits info
        caller.msg(f"\n|cExits:|n")
        if location.exits:
            for exit_obj in location.exits:
                dest_name = exit_obj.destination.name if exit_obj.destination else "None"
                caller.msg(f"  {exit_obj.name} -> {dest_name}")
        else:
            caller.msg("  No exits")
            
        # Contents info (characters only)
        characters = [obj for obj in location.contents if obj.has_account]
        caller.msg(f"\n|cCharacters Present:|n")
        caller.msg(f"Count: {len(characters)}")
        for char in characters:
            shortdesc = char.db.shortdesc or "No short description"
            caller.msg(f"  {char.name}: {shortdesc}")


class CmdTempRoom(MuxCommand):
    """
    Create and manage temporary RP rooms.

    Usage:
      temproom <room name>
      temproom/desc <description>
      temproom/hierarch <location1>,<location2>
      temproom/priv
      temproom/pub
      temproom/perm
      temproom/!perm
      temproom/destroy
      temproom/undo
    """

    key = "temproom"
    locks = "cmd:all()"
    help_category = "Roleplaying Tools"

    def _normalized(self, value):
        return str(value).strip().lower()

    def _room_tags(self, room):
        tags = set()
        if hasattr(room, "tags"):
            for tag in room.tags.all(return_key_and_category=False):
                tags.add(self._normalized(tag))
        raw_tags = getattr(room.db, "tags", None) or []
        if isinstance(raw_tags, str):
            raw_tags = [raw_tags]
        try:
            for tag in raw_tags:
                tags.add(self._normalized(tag))
        except TypeError:
            tags.add(self._normalized(raw_tags))
        return tags

    def _is_ooc_room(self, room):
        if not room:
            return False

        ooc_markers = {"ooc", "ooc area"}
        room_tags = self._room_tags(room)
        if room_tags & ooc_markers:
            return True

        hierarchy = room.db.location_hierarchy or []
        if isinstance(hierarchy, str):
            hierarchy = [hierarchy]
        for location_name in hierarchy:
            if self._normalized(location_name) == "ooc area":
                return True
        return False

    def _is_exception_source(self, room):
        if not room:
            return False

        if bool(getattr(room.db, "temproom_allow_source", False)):
            return True

        room_tags = self._room_tags(room)
        tag_markers = {"rp nexus", "rp_nexus", "temproom_exception", "temproom_ok"}
        if room_tags & tag_markers:
            return True

        configured_dbrefs = ServerConfig.objects.conf("TEMPROOM_SOURCE_EXCEPTIONS", default=[])
        if isinstance(configured_dbrefs, str):
            configured_dbrefs = [entry.strip() for entry in configured_dbrefs.split(",") if entry.strip()]
        normalized = set()
        for entry in configured_dbrefs or []:
            normalized.add(str(entry).strip().lstrip("#"))
        return str(room.id) in normalized

    def _can_build_from(self, source_room):
        if not source_room:
            return False
        if self._is_exception_source(source_room):
            return True
        return not self._is_ooc_room(source_room)

    def _is_temproom(self, room):
        return bool(room and room.is_typeclass("typeclasses.rooms.TempRoom", exact=False))

    def _is_owner_or_staff(self, caller, room):
        if check_staff_permission(caller):
            return True
        owner = getattr(room.db, "temproom_owner", None)
        return owner == caller

    def _normalize_hierarchy(self, hierarchy_value):
        """
        Normalize hierarchy input into exactly two location strings.
        """
        if isinstance(hierarchy_value, str):
            if "," in hierarchy_value:
                parts = [part.strip() for part in hierarchy_value.split(",", 1)]
            else:
                parts = [hierarchy_value.strip()]
        elif hierarchy_value:
            parts = [str(part).strip() for part in list(hierarchy_value)]
        else:
            parts = []

        parts = [part for part in parts if part]

        if not parts:
            return ["Unknown", "Unknown"]
        if len(parts) == 1:
            return [parts[0], "Unknown"]
        return [parts[0], parts[1]]

    def _build_alias(self, room_name, location):
        words = re.findall(r"[A-Za-z0-9]+", room_name)
        if words:
            base = "".join(word[0].lower() for word in words)
        else:
            compact = "".join(ch for ch in room_name.lower() if ch.isalnum())
            base = compact[:2] if compact else "tr"

        used = set()
        for exit_obj in location.exits:
            used.add(self._normalized(exit_obj.key))
            for alias in exit_obj.aliases.all():
                used.add(self._normalized(alias))

        if base not in used:
            return base

        idx = 1
        while f"{base}{idx}" in used:
            idx += 1
        return f"{base}{idx}"

    def _set_entrance_private(self, room, is_private):
        entrance = getattr(room.db, "temproom_entrance_exit", None)
        if not entrance:
            return False
        if is_private:
            entrance.locks.add("view:false();traverse:false()")
        else:
            entrance.locks.add("view:all();traverse:all()")
        room.db.temproom_private = bool(is_private)
        return True

    def _destroy_temproom(self, room, caller=None, reason="expired"):
        source_room = getattr(room.db, "temproom_source_room", None)
        entrance = getattr(room.db, "temproom_entrance_exit", None)
        return_exit = getattr(room.db, "temproom_return_exit", None)

        if caller and caller.location == room:
            destination = source_room if source_room else caller.home
            if destination:
                caller.move_to(destination, quiet=True, move_type="teleport")

        if entrance:
            entrance.delete()
        if return_exit:
            return_exit.delete()

        owner = getattr(room.db, "temproom_owner", None)
        room_name = room.name
        room.delete()

        if owner and owner.sessions.all():
            owner.msg(f"|yYour temporary room '{room_name}' was destroyed ({reason}).|n")
        return True

    def _is_empty_for_destroy(self, room, caller):
        for obj in room.contents:
            if obj == caller:
                continue
            if obj.destination:  # exits inside the room
                continue
            return False
        return True

    def _ensure_cleanup_script(self):
        from world.scripts.temproom_cleanup_script import start_temproom_cleanup_script

        start_temproom_cleanup_script()

    def _create_temproom(self):
        caller = self.caller
        source_room = caller.location
        room_name = self.args.strip()

        if not source_room:
            caller.msg("You must be in a room to create a temproom.")
            return
        if not room_name:
            caller.msg("Usage: temproom <room name>")
            return
        if not self._can_build_from(source_room):
            caller.msg(
                "You can only create temprooms from IC locations "
                "(or approved exception rooms)."
            )
            return
        if self._is_temproom(source_room):
            caller.msg("You cannot create a temproom from inside another temproom.")
            return

        alias = self._build_alias(room_name, source_room)
        source_hierarchy = self._normalize_hierarchy(
            getattr(source_room.db, "location_hierarchy", None)
        )

        new_room = create.create_object(
            typeclass="typeclasses.rooms.TempRoom",
            key=room_name,
            location=None,
        )
        new_room.db.desc = "A temporary scene space."
        new_room.db.temproom_owner = caller
        new_room.db.temproom_source_room = source_room
        new_room.db.temproom_created_at = time.time()
        new_room.db.temproom_last_activity = time.time()
        new_room.db.temproom_private = False
        new_room.db.temproom_permanent = False
        new_room.db.area_name = source_room.db.area_name or "Unknown Area"
        new_room.db.area_code = source_room.db.area_code or "XX00"
        new_room.db.location_hierarchy = source_hierarchy

        entrance_exit = create.create_object(
            typeclass="typeclasses.exits.Exit",
            key=room_name,
            location=source_room,
            destination=new_room,
            aliases=[alias],
        )
        entrance_exit.locks.add("view:all();traverse:all()")
        entrance_exit.db.temproom_exit = True
        entrance_exit.db.temproom_owner = caller
        entrance_exit.db.temproom_room = new_room

        return_exit = create.create_object(
            typeclass="typeclasses.exits.Exit",
            key="Out",
            location=new_room,
            destination=source_room,
            aliases=["o", "out"],
        )
        return_exit.locks.add("view:all();traverse:all()")
        return_exit.db.temproom_exit = True
        return_exit.db.temproom_room = new_room

        new_room.db.temproom_entrance_exit = entrance_exit
        new_room.db.temproom_return_exit = return_exit

        self._ensure_cleanup_script()

        caller.msg(
            f"|gTemporary room created:|n {new_room.name}. "
            f"Entrance exit here: {entrance_exit.key} <{alias}>"
        )
        source_room.msg_contents(
            f"A temporary entrance to {new_room.name} appears.",
            exclude=[caller],
        )

    def _set_desc(self):
        caller = self.caller
        room = caller.location
        if not self._is_temproom(room):
            caller.msg("You must be inside a temproom to use /desc.")
            return
        if not self._is_owner_or_staff(caller, room):
            caller.msg("Only the owner or staff can change this room's description.")
            return
        if not self.args.strip():
            caller.msg("Usage: temproom/desc <description>")
            return
        room.db.desc = process_special_characters(self.args.strip())
        room.db.temproom_last_activity = time.time()
        caller.msg("Temproom description updated.")

    def _set_hierarchy(self):
        caller = self.caller
        room = caller.location
        if not self._is_temproom(room):
            caller.msg("You must be inside a temproom to use /hierarch.")
            return
        if not self._is_owner_or_staff(caller, room):
            caller.msg("Only the owner or staff can change hierarchy.")
            return
        if "," not in self.args:
            caller.msg("Usage: temproom/hierarch <location1>,<location2>")
            return

        hierarchy = self._normalize_hierarchy(self.args.strip())
        room.db.location_hierarchy = hierarchy
        room.db.temproom_last_activity = time.time()
        caller.msg(f"Temproom hierarchy set to: {hierarchy[0]} - {hierarchy[1]}")

    def _set_private(self, value):
        caller = self.caller
        room = caller.location
        if not self._is_temproom(room):
            caller.msg("You must be inside a temproom to use this switch.")
            return
        if not self._is_owner_or_staff(caller, room):
            caller.msg("Only the owner or staff can change privacy.")
            return
        if not self._set_entrance_private(room, value):
            caller.msg("This temproom has no valid entrance exit to update.")
            return
        room.db.temproom_last_activity = time.time()
        if value:
            caller.msg("Temproom is now private. Entrance is hidden and locked.")
        else:
            caller.msg("Temproom is now public. Entrance is visible and unlocked.")

    def _set_perm(self, value):
        caller = self.caller
        room = caller.location
        if not self._is_temproom(room):
            caller.msg("You must be inside a temproom to use this switch.")
            return
        if not check_staff_permission(caller):
            caller.msg("Only staff can set or unset permanent temprooms.")
            return
        room.db.temproom_permanent = bool(value)
        if value:
            caller.msg("Temproom is now permanent-temporary (will not auto-expire).")
        else:
            caller.msg("Temproom auto-expiration restored.")

    def _destroy_here(self):
        caller = self.caller
        room = caller.location
        if not self._is_temproom(room):
            caller.msg("You must be inside a temproom to destroy it.")
            return
        if not self._is_owner_or_staff(caller, room):
            caller.msg("Only the owner or staff can destroy this temproom.")
            return
        if not self._is_empty_for_destroy(room, caller):
            caller.msg("This temproom is not empty. Clear it before destroying.")
            return
        self._destroy_temproom(room, caller=caller, reason="manual destroy")
        caller.msg("Temproom destroyed.")

    def func(self):
        if not self.switches:
            self._create_temproom()
            return

        switch = self.switches[0].lower()
        if switch == "desc":
            self._set_desc()
        elif switch in ("hierarch", "hierarchy"):
            self._set_hierarchy()
        elif switch == "priv":
            self._set_private(True)
        elif switch == "pub":
            self._set_private(False)
        elif switch == "perm":
            self._set_perm(True)
        elif switch in ("!perm", "unperm"):
            self._set_perm(False)
        elif switch in ("destroy", "undo"):
            self._destroy_here()
        else:
            self.caller.msg(
                "Valid switches: /desc, /hierarch, /priv, /pub, /perm, /!perm, /destroy, /undo"
            )


class CmdMap(MuxCommand):
    """
    Display an ASCII map of rooms in an area.
    
    Usage:
      +map - Show map of current area
      +map <area_code> - Show map of specific area
      +map/legend - Show map legend and symbols
      
    Examples:
      +map - Show map of current room's area
      +map HE - Show map of Hedge area
      +map/legend - Show what symbols mean
    """
    
    key = "+map"
    locks = "cmd:all()"
    help_category = "Roleplaying Tools"
    
    def func(self):
        caller = self.caller
        area_manager = get_area_manager()
        
        # Handle legend switch
        if self.switches and self.switches[0].lower() == "legend":
            self.show_legend()
            return
        
        # Determine area code
        area_code = None
        if self.args:
            area_code = self.args.strip().upper()
            if not area_manager.validate_area_code(area_code):
                caller.msg(f"Area code {area_code} not found. Use '+area/list' to see available areas.")
                return
        else:
            # Use current room's area
            location = caller.location
            if not location or not location.db.area_code:
                caller.msg("You must specify an area code or be in a room with an area code set.")
                caller.msg("Usage: +map <area_code>")
                return
            area_code = location.db.area_code[:2]  # First 2 characters
        
        # Generate and display the map
        self.generate_map(area_manager, area_code)
    
    def show_legend(self):
        """Show the map legend."""
        legend = """
|wMap Legend:|n

|c@|n - Your current location
|w#|n - Room with coordinates set
|r?|n - Room without coordinates
|g+|n - Connection between rooms
|y||n - Vertical connection
|y-|n - Horizontal connection

|wNotes:|n
- Only rooms with coordinates set using '+room/coords' will show precise positions
- Rooms without coordinates will be listed separately
- Use '+room/coords here=<x>,<y>' to set room positions for better maps
"""
        self.caller.msg(legend)
    
    def generate_map(self, area_manager, area_code):
        """Generate ASCII map for an area."""
        area_info = area_manager.get_area_info(area_code)
        if not area_info:
            self.caller.msg(f"Area {area_code} not found.")
            return
        
        rooms = area_info['rooms']
        if not rooms:
            self.caller.msg(f"No rooms found in area {area_code}.")
            return
        
        # Get room objects and coordinates
        room_coords = {}
        rooms_without_coords = []
        current_room_coords = None
        
        for room_num, room_id in rooms.items():
            room_obj = search_object(f"#{room_id}")
            if not room_obj:
                continue
            
            room_obj = room_obj[0]
            coords = area_manager.get_room_coordinates(room_id)
            
            if coords:
                room_coords[coords] = {
                    'room': room_obj,
                    'code': f"{area_code}{room_num:02d}",
                    'id': room_id
                }
                
                # Check if this is the caller's current room
                if self.caller.location and self.caller.location.id == room_id:
                    current_room_coords = coords
            else:
                rooms_without_coords.append({
                    'room': room_obj,
                    'code': f"{area_code}{room_num:02d}",
                    'id': room_id
                })
        
        if not room_coords:
            self.caller.msg(f"No rooms in area {area_code} have coordinates set.")
            self.caller.msg("Use '+room/coords here=<x>,<y>' to set room positions.")
            self.caller.msg("Example: +room/coords here=0,0")
            if rooms_without_coords:
                self.caller.msg(f"\nRooms without coordinates:")
                for room_info in rooms_without_coords:
                    self.caller.msg(f"  {room_info['code']}: {room_info['room'].name}")
            return
        
        # Calculate map bounds - ensure we have valid coordinates
        coords_list = list(room_coords.keys())
        if not coords_list:
            self.caller.msg(f"No valid coordinates found for area {area_code}.")
            return
            
        min_x = min(coord[0] for coord in coords_list)
        max_x = max(coord[0] for coord in coords_list)
        min_y = min(coord[1] for coord in coords_list)
        max_y = max(coord[1] for coord in coords_list)
        
        # Create the map grid
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        
        # Limit map size for display
        if width > 50 or height > 30:
            self.caller.msg("Map too large to display (max 50x30). Consider adjusting room coordinates.")
            return
        
        # Initialize map with spaces
        map_grid = []
        for y in range(height):
            map_grid.append([' '] * width)
        
        # Place rooms on the map
        for (x, y), room_info in room_coords.items():
            grid_x = x - min_x
            grid_y = max_y - y  # Flip Y axis for display (top = higher Y)
            
            if (x, y) == current_room_coords:
                map_grid[grid_y][grid_x] = '|c@|n'  # Current location
            else:
                map_grid[grid_y][grid_x] = '|w#|n'  # Regular room
        
        # Add connections (basic implementation)
        self.add_connections_to_map(map_grid, room_coords, min_x, max_y)
        
        # Display the map
        self.caller.msg(f"|wMap of {area_info['name']} ({area_code}):|n\n")
        
        for row in map_grid:
            self.caller.msg(''.join(row))
        
        # Show room list
        self.caller.msg(f"\n|wRooms in {area_code}:|n")
        for (x, y), room_info in sorted(room_coords.items()):
            symbol = '@' if (x, y) == current_room_coords else '#'
            self.caller.msg(f"  {symbol} ({x:2},{y:2}) {room_info['code']}: {room_info['room'].name}")
        
        if rooms_without_coords:
            self.caller.msg(f"\n|yRooms without coordinates:|n")
            for room_info in rooms_without_coords:
                self.caller.msg(f"  ? {room_info['code']}: {room_info['room'].name}")
    
    def add_connections_to_map(self, map_grid, room_coords, min_x, max_y):
        """Add basic connections between adjacent rooms."""
        height = len(map_grid)
        width = len(map_grid[0]) if map_grid else 0
        
        # This is a simple implementation that shows connections between 
        # horizontally and vertically adjacent rooms
        for (x, y), room_info in room_coords.items():
            room_obj = room_info['room']
            grid_x = x - min_x
            grid_y = max_y - y
            
            # Check exits and see if they connect to adjacent coordinates
            for exit_obj in room_obj.exits:
                if not exit_obj.destination:
                    continue
                
                dest_coords = None
                for (dx, dy), dest_info in room_coords.items():
                    if dest_info['id'] == exit_obj.destination.id:
                        dest_coords = (dx, dy)
                        break
                
                if dest_coords:
                    dest_x, dest_y = dest_coords
                    dest_grid_x = dest_x - min_x
                    dest_grid_y = max_y - dest_y
                    
                    # Add connection lines for adjacent rooms
                    if abs(dest_grid_x - grid_x) == 1 and dest_grid_y == grid_y:
                        # Horizontal connection
                        conn_x = min(grid_x, dest_grid_x) + 1
                        if 0 <= conn_x < width and 0 <= grid_y < height:
                            if map_grid[grid_y][conn_x] == ' ':
                                map_grid[grid_y][conn_x] = '|y-|n'
                    elif abs(dest_grid_y - grid_y) == 1 and dest_grid_x == grid_x:
                        # Vertical connection
                        conn_y = min(grid_y, dest_grid_y) + 1
                        if 0 <= grid_x < width and 0 <= conn_y < height:
                            if map_grid[conn_y][grid_x] == ' ':
                                map_grid[conn_y][grid_x] = '|y||n'

