from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from evennia import search_object
from world.utils.health_utils import get_health_track, set_health_track, compact_track
from world.cofd.templates import get_template_definition
from world.legacy_virtues_vices import LEGACY_VIRTUES, LEGACY_VICES, get_virtue_info, get_vice_info
from utils.search_helpers import search_character

class CmdSheet(MuxCommand):
    """
    Display your character sheet.
    
    Usage:
        +sheet [character] - Display character sheet
        +sheet/ascii [character] - Display with numeric format this time
        +sheet/unicode [character] - Display with Unicode dots (●●●○○) this time
        +sheet/ascii default - Set numeric display as your permanent default
        +sheet/unicode default - Set Unicode dots as your permanent default
        +sheet/[template] [character] - Display template secondary sheet
            - Mage: Nimbus, Obsessions, Praxes, and Dedicated Tool
            - Demon: Modifications, Technologies, Propulsion, and Process
            - Deviant: Variations and Scars
            - Geist: Bound Geist
        +sheet/show - Show your sheet to everyone in the room
        +sheet/show [player] - Show your sheet to a specific player
        +sheet/show/[template] [player] - Show your template secondary sheet to a player
        
    Shows all character statistics in an organized format.
    
    Display Modes:
    - Numeric (Default): Stats shown as numbers (Strength.......3, Health 5/7)
    - Unicode (Opt-in): Stats shown as dots (●●●○○)
    
    To set your permanent preference:
      +sheet/unicode default  - Always use Unicode dots
      +sheet/ascii default    - Always use numeric (resets to default)
    
    Your preference persists across logins.
    """
    
    key = "+sheet"
    aliases = ["sheet"]
    help_category = "Chargen & Character Info"
    
    def _get_dots_style(self, force_ascii=False, force_unicode=False):
        """
        Determine whether to use Unicode dots or numeric display.
        
        Args:
            force_ascii (bool): Force numeric display regardless of user preference
            force_unicode (bool): Force Unicode display regardless of user preference
            
        Returns:
            tuple: (filled_char, empty_char, supports_utf8, use_numeric)
        """
        # Check if user explicitly wants numeric display via switch
        if force_ascii or "ascii" in self.switches:
            return ("*", "-", False, True)  # use_numeric=True
        
        # Check if user explicitly wants Unicode display via switch
        if force_unicode or "unicode" in self.switches:
            return ("●", "○", True, False)  # use_numeric=False
        
        # Check user's saved preference (from +sheet/unicode default or +sheet/ascii default)
        if hasattr(self.caller, 'db') and hasattr(self.caller.db, 'use_unicode_dots'):
            if self.caller.db.use_unicode_dots:
                return ("●", "○", True, False)  # User saved Unicode preference
        
        # Fallback: Check if set via @option (for backward compatibility)
        if hasattr(self.caller, 'account') and self.caller.account:
            try:
                unicode_option = self.caller.account.options.get("UNICODE_DOTS")
                if unicode_option is True:  # Explicitly check for True (boolean)
                    return ("●", "○", True, False)  # User explicitly enabled Unicode
            except Exception:
                pass  # Option not available, continue to default
        
        # Default to numeric display for all users
        return ("*", "-", False, True)  # use_numeric=True as default
    
    def _format_dots(self, value, max_value=5, force_ascii=False, show_max=False):
        """
        Format a stat value as dots (Unicode), numbers (non-UTF8), or ASCII.
        
        Args:
            value (int): Current stat value
            max_value (int): Maximum possible value
            force_ascii (bool): Force numeric display
            show_max (bool): For numeric mode, show max value (e.g., pools vs stats)
            
        Returns:
            str: Formatted dot display or numeric display
        """
        filled_char, empty_char, supports_utf8, use_numeric = self._get_dots_style(force_ascii)
        
        # If numeric display is requested (non-UTF8 clients or /ascii switch)
        if use_numeric:
            # Handle values exceeding maximum (e.g., shapeshifted werewolves)
            if value > max_value:
                if show_max:
                    return f"{value}/{max_value} |y(+{value - max_value})|n"
                else:
                    return f"{value} |y(+{value - max_value})|n"
            else:
                # For pools, show current/max; for stats, show just the value
                if show_max:
                    return f"{value}/{max_value}"
                else:
                    return str(value)
        
        # Unicode/ASCII dots display
        # Handle values exceeding maximum (e.g., shapeshifted werewolves)
        if value > max_value:
            # Show all filled dots with a special indicator
            filled = filled_char * value
            return f"{filled} |y(+{value - max_value})|n"
        else:
            # Normal display with filled and empty dots
            filled = filled_char * value
            empty = empty_char * (max_value - value)
            return filled + empty
    

    def _get_template_bio_fields(self, template):
        """Get valid bio fields for a specific template from the template registry"""
        if not template:
            return ["virtue", "vice"]  # Default fallback for empty/None template
            
        template = template.lower().replace(" ", "_")
        
        # Handle alternate naming
        if template == "mortal plus":
            template = "mortal_plus"
        elif template == "legacy_vampire":
            template = "legacy_vampire"
        elif template == "legacy_werewolf":
            template = "legacy_werewolf" 
        elif template == "legacy_mage":
            template = "legacy_mage"
        elif template == "legacy_changeling":
            template = "legacy_changeling"
        elif template == "legacy_geist":
            template = "legacy_geist"
        elif template == "legacy_promethean":
            template = "legacy_promethean"
        elif template == "legacy_hunter":
            template = "legacy_hunter"
        elif template == "legacy_changingbreeds" or template == "legacy_changing_breeds":
            template = "legacy_changingbreeds"
        
        # Try to get template definition from registry
        template_def = get_template_definition(template)
        if template_def and "bio_fields" in template_def:
            return template_def["bio_fields"]
        
        # Fallback for legacy templates if registry lookup fails
        legacy_bio_fields = {
            "legacy_vampire": ["clan", "covenant", "sire", "embrace_date", "virtue", "vice"],
            "legacy_werewolf": ["auspice", "tribe", "pack", "virtue", "vice"],
            "legacy_mage": ["path", "order", "cabal", "shadow_name", "virtue", "vice"],
            "legacy_changeling": ["seeming", "kith", "court", "motley", "keeper", "virtue", "vice"],
            "legacy_geist": ["archetype", "threshold", "krewe", "geist_name", "virtue", "vice"],
            "legacy_promethean": ["lineage", "refinement", "creator", "role", "virtue", "vice"],
            "legacy_hunter": ["profession", "organization", "creed", "cell", "virtue", "vice"],
            "legacy_changingbreeds": ["accord", "breed", "nahual", "virtue", "vice", "pack"]
        }
        
        if template in legacy_bio_fields:
            return legacy_bio_fields[template]
        
        # Fallback to default mortal fields if template not found
        return ["virtue", "vice"]

    def _format_section_header(self, section_name):
        """
        Create an arrow-style section header that spans 78 characters.
        Format: <----------------- SECTION NAME ----------------->
        """
        total_width = 78
        name_length = len(section_name)
        # Account for < and > characters (2 total) and spaces around name (2 total)
        available_dash_space = total_width - name_length - 4
        
        # Split dashes evenly, with extra dash on the right if odd number
        left_dashes = available_dash_space // 2
        right_dashes = available_dash_space - left_dashes
        
        return f"|g<{'-' * left_dashes}|n {section_name} |g{'-' * right_dashes}>|n"

    def _get_health_track(self, character):
        """Get health track as an array where index 0 is leftmost (most severe)."""
        return get_health_track(character)
    
    def _set_health_track(self, character, track):
        """Set health track from array format back to dictionary format."""
        set_health_track(character, track)
    
    def _calculate_health_stats(self, health_track, health_max):
        """
        Calculate health statistics from health track.
        
        Args:
            health_track (list): Health track array with damage types
            health_max (int): Maximum health
            
        Returns:
            tuple: (current_health, bashing_count, lethal_count, aggravated_count)
        """
        bashing_count = 0
        lethal_count = 0
        aggravated_count = 0
        
        for damage_type in health_track:
            if damage_type == "bashing":
                bashing_count += 1
            elif damage_type == "lethal":
                lethal_count += 1
            elif damage_type == "aggravated":
                aggravated_count += 1
        
        total_damage = bashing_count + lethal_count + aggravated_count
        current_health = health_max - total_damage
        
        return (current_health, bashing_count, lethal_count, aggravated_count)
    
    def _get_template_powers(self, template):
        """Get the list of available primary powers for a specific template."""
        if not template:
            return []
        
        # Import template power utilities
        from world.cofd.templates import get_template_primary_powers
        
        # Get primary powers from template definition
        return get_template_primary_powers(template)
    
    def _get_template_secondary_powers(self, template):
        """Get the list of available secondary powers (rituals, rites) for a specific template."""
        if not template:
            return []
        
        # Import template power utilities
        from world.cofd.templates import get_template_secondary_powers
        
        # Get secondary powers from template definition
        return get_template_secondary_powers(template)
    
    def _get_sleepwalker_spells(self):
        """Get the list of spells available to Sleepwalkers and Proximus.
        
        Sleepwalkers typically have access to 1-2 dot spells.
        Proximus have access to 1-3 dot spells from their bloodline arcana.
        """
        try:
            from world.cofd.powers.mage_spells import SLEEPWALKER_SPELLS, PROXIMUS_SPELLS, ALL_MAGE_SPELLS
            # Return all spell keys for checking
            return list(ALL_MAGE_SPELLS.keys())
        except ImportError:
            # If mage_spells not found, return empty list
            return []
    
    def _format_powers_display(self, powers, template_powers, force_ascii, use_numeric=False, template=None):
        """Format the powers section for display."""
        if not template_powers:
            return ["No powers available for this template."]
        
        power_lines = []
        
        # Import contract lookup for Changeling
        contract_data = None
        if template and (template.lower() == "changeling" or template.lower() == "legacy_changeling"):
            try:
                from world.cofd.powers.changeling_contracts import get_contract
                contract_data = get_contract
            except ImportError:
                contract_data = None
        
        # Group powers by category if applicable
        displayed_powers = []
        for power_name in template_powers:
            # Check for power with and without prefix (e.g., "spinning_wheel" and "contract:spinning_wheel")
            power_value = powers.get(power_name, 0)
            if power_value == 0:
                # Try with contract: prefix for Changeling contracts (stored as "contract:spinning_wheel")
                prefixed_name = f"contract:{power_name}"
                power_value = powers.get(prefixed_name, 0)
            # Handle both numeric (1-5) and semantic ("known") power values
            if power_value == "known" or (isinstance(power_value, int) and power_value > 0):
                # For semantic powers (embeds, exploits, etc.), just show the name
                if power_value == "known":
                    dots = ""  # No dots for known/unknown powers
                else:
                    dots = self._format_dots(power_value, 5, force_ascii)
                # Clean up display name - remove prefixes and format properly
                display_name = power_name
                contract_key = power_name  # Store original key for contract lookup
                if power_name.startswith('discipline_'):
                    display_name = power_name[11:]  # Remove 'discipline_'
                elif power_name.startswith('arcanum_'):
                    display_name = power_name[8:]   # Remove 'arcanum_'
                elif power_name.startswith('gift_'):
                    display_name = power_name[5:]   # Remove 'gift_'
                elif power_name.startswith('contract_'):
                    display_name = power_name[9:]   # Remove 'contract_'
                    contract_key = display_name
                elif power_name.startswith('contract:'):
                    display_name = power_name[9:]   # Remove 'contract:' (for stored format)
                    contract_key = display_name
                elif power_name.startswith('rite_'):
                    display_name = power_name[5:]   # Remove 'rite_'
                elif power_name.startswith('embed:'):
                    display_name = power_name[6:]   # Remove 'embed:'
                elif power_name.startswith('exploit:'):
                    display_name = power_name[8:]   # Remove 'exploit:'
                elif power_name.startswith('bestowment:'):
                    display_name = power_name[11:]  # Remove 'bestowment:'
                elif power_name.startswith('alembic:'):
                    display_name = power_name[8:]   # Remove 'alembic:'
                
                # For Changeling contracts, add category and type information
                contract_info = ""
                if contract_data and contract_key:
                    contract = contract_data(contract_key)
                    if contract:
                        contract_type = contract.get('contract_type', '')
                        # Parse contract_type to extract category and royal/common
                        if contract_type:
                            # Handle independent contracts first
                            if contract_type == 'independent_common':
                                category = 'independent'
                                is_royal = False
                            elif contract_type == 'independent_royal':
                                category = 'independent'
                                is_royal = True
                            # Check if it's royal (contains _royal)
                            elif '_royal' in contract_type:
                                is_royal = True
                                category = contract_type.replace('_royal', '')
                            else:
                                # All other contracts without _royal are Common
                                is_royal = False
                                category = contract_type
                            
                            # Format category name (capitalize first letter)
                            category_display = category.capitalize()
                            
                            # Determine type (Royal or Common)
                            type_display = "Royal" if is_royal else "Common"
                            
                            contract_info = f" ({category_display}, {type_display})"
                
                # Format display with or without dots
                if dots:
                    power_name_display = display_name.replace('_', ' ').title()
                    # Use dot padding in numeric mode for better readability
                    if use_numeric:
                        padding = '.' * (37 - len(power_name_display))
                        power_display = f"{power_name_display}{padding}{dots}"
                    else:
                        power_display = f"{power_name_display:<37} {dots}"
                else:
                    power_name_display = display_name.replace('_', ' ').title()
                    power_display = f"{power_name_display}{contract_info}"
                displayed_powers.append(power_display)
        
        if not displayed_powers:
            return ["No powers learned yet."]
        
        # Display powers in 2 columns like merits
        for i in range(0, len(displayed_powers), 2):
            left_power = displayed_powers[i] if i < len(displayed_powers) else ""
            right_power = displayed_powers[i + 1] if i + 1 < len(displayed_powers) else ""
            
            # Format with proper spacing (39 chars for left column)
            left_formatted = left_power.ljust(42)
            power_lines.append(f"{left_formatted}{right_power}")
        
        return power_lines
    
    def _format_secondary_powers_display(self, powers, template_secondary_powers, force_ascii, use_numeric=False):
        """Format the secondary powers (rituals/rites) section for display."""
        if not template_secondary_powers:
            return ["No secondary powers available for this template."]
        
        power_lines = []
        
        # Group secondary powers by category if applicable
        displayed_powers = []
        for power_name in template_secondary_powers:
            # Check for power with and without prefix (e.g., "spinning_wheel" and "contract:spinning_wheel")
            power_value = powers.get(power_name, 0)
            if power_value == 0:
                # Try with contract: prefix for Changeling contracts (stored as "contract:spinning_wheel")
                prefixed_name = f"contract:{power_name}"
                power_value = powers.get(prefixed_name, 0)
            # Handle both numeric (1-5) and semantic ("known") power values
            if power_value == "known" or (isinstance(power_value, int) and power_value > 0):
                # For secondary powers, show dots if numeric, nothing if "known"
                if power_value == "known":
                    display_marker = ""  # No dots for known/unknown powers
                else:
                    display_marker = self._format_dots(power_value, 5, force_ascii)
                
                # Clean up display name - remove prefixes and format properly
                display_name = power_name
                if power_name.startswith('discipline_'):
                    display_name = power_name[11:]  # Remove 'discipline_'
                elif power_name.startswith('arcanum_'):
                    display_name = power_name[8:]   # Remove 'arcanum_'
                elif power_name.startswith('gift_'):
                    display_name = power_name[5:]   # Remove 'gift_'
                elif power_name.startswith('contract_'):
                    display_name = power_name[9:]   # Remove 'contract_'
                elif power_name.startswith('contract:'):
                    display_name = power_name[9:]   # Remove 'contract:' (for stored format)
                elif power_name.startswith('rite_'):
                    display_name = power_name[5:]   # Remove 'rite_'
                elif power_name.startswith('embed:'):
                    display_name = power_name[6:]   # Remove 'embed:'
                elif power_name.startswith('exploit:'):
                    display_name = power_name[8:]   # Remove 'exploit:'
                elif power_name.startswith('bestowment:'):
                    display_name = power_name[11:]  # Remove 'bestowment:'
                elif power_name.startswith('alembic:'):
                    display_name = power_name[8:]   # Remove 'alembic:'
                
                # Format display with or without dots
                if display_marker:
                    power_name_display = display_name.replace('_', ' ').title()
                    # Use dot padding in numeric mode for better readability
                    if use_numeric:
                        padding = '.' * (37 - len(power_name_display))
                        power_display = f"{power_name_display}{padding}{display_marker}"
                    else:
                        power_display = f"{power_name_display:<37} {display_marker}"
                else:
                    power_display = f"{display_name.replace('_', ' ').title()}"
                displayed_powers.append(power_display)
        
        if not displayed_powers:
            return ["No secondary powers learned yet."]
        
        # Display powers in 2 columns like merits
        for i in range(0, len(displayed_powers), 2):
            left_power = displayed_powers[i] if i < len(displayed_powers) else ""
            right_power = displayed_powers[i + 1] if i + 1 < len(displayed_powers) else ""
            
            # Format with proper spacing (39 chars for left column)
            left_formatted = left_power.ljust(42)
            power_lines.append(f"{left_formatted}{right_power}")
        
        return power_lines

    def func(self):
        """Display the character sheet"""
        # Check if this is a request to set default display mode
        if self.args and self.args.strip().lower() == "default":
            if "unicode" in self.switches:
                self.caller.db.use_unicode_dots = True
                self.caller.msg("|gUnicode dots display (●●●○○) set as your permanent default.|n")
                self.caller.msg("Use |w+sheet/ascii default|n to switch back to numeric display.")
                return
            elif "ascii" in self.switches:
                self.caller.db.use_unicode_dots = False
                self.caller.msg("|gNumeric display set as your permanent default.|n")
                self.caller.msg("Use |w+sheet/unicode default|n to switch to Unicode dots.")
                return
            else:
                self.caller.msg("|rYou must use either |w+sheet/unicode default|r or |w+sheet/ascii default|r.|n")
                return
        
        # Check if this is a show request
        if "show" in self.switches:
            self.show_sheet_to_others()
            return
        
        # Check if this is a geist sheet request
        if "geist" in self.switches:
            self.show_geist_sheet()
            return
        
        # Check if this is a mage sheet request
        if "mage" in self.switches:
            self.show_mage_sheet()
            return
        
        # Check if this is a demon form sheet request
        if "demon" in self.switches:
            self.show_demon_form_sheet()
            return
        
        # Check if this is a deviant powers sheet request
        if "deviant" in self.switches:
            self.show_deviant_sheet()
            return
            
        # Determine target
        if self.args:
            target = search_character(self.caller, self.args.strip())
            if not target:
                return
        else:
            target = self.caller
            
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        legacy_mode = is_legacy_mode()
        

        if not target.db.stats:
            self.caller.msg(f"{target.name} has no character sheet set up yet.")
            self.caller.msg("Use +stat <stat>=<value> to set your stats.")
            return
        
        # Get dot style and check UTF-8 support
        force_ascii = "ascii" in self.switches
        filled_char, empty_char, supports_utf8, use_numeric = self._get_dots_style(force_ascii)
        
        # Build the sheet display
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{target.name.center(78)}|n")
        if target.db.approved:
            output.append(f"|g{'APPROVED'.center(78)}|n")
        else:
            output.append(f"|r{'NOT APPROVED'.center(78)}|n")
        
        # Show legacy mode status
        if legacy_mode:
            output.append(f"|m{'nWoD 1st Edition'.center(78)}|n")
        
        output.append(f"|y{'='*78}|n")
        
        # Bio Section
        output.append(self._format_section_header("|wBIO|n"))
        
        # Get bio information from stats
        bio = target.db.stats.get("bio", {})
        other = target.db.stats.get("other", {})
        
        # Bio data with defaults
        full_name = bio.get("full_name", bio.get("fullname", "<not set>"))
        birthdate = bio.get("birthdate", "<not set>")
        concept = bio.get("concept", "<not set>")
        template = other.get("template", "Mortal")
        
        # Get template-specific fields to determine what to show
        template_fields = self._get_template_bio_fields(template)
        
        # Only get virtue/vice if they're valid for this template
        virtue = bio.get("virtue", "<not set>") if "virtue" in template_fields else None
        vice = bio.get("vice", "<not set>") if "vice" in template_fields else None
        
        bio_items = [
            ("Full Name", full_name),
            ("Template", template),
            ("Birthdate", birthdate),
            ("Concept", concept)
        ]
        
        # Add virtue/vice if they're valid for this template
        if virtue is not None:
            bio_items.append(("Virtue", virtue))
        if vice is not None:
            bio_items.append(("Vice", vice))
        
            # Add template-specific bio fields
        for field in template_fields:
            if field not in ["virtue", "vice", "game_line"]:  # virtue/vice already added, game_line is internal only
                # Skip abilities field for Mortal+ (those are merits)
                if field == "abilities":
                    continue
                
                # Skip regnant for non-Ghouls
                if field == "regnant":
                    mortal_plus_type = bio.get("template_type", "").lower()
                    if mortal_plus_type != "ghoul":
                        continue
                
                # Skip promise for non-Fae-Touched
                if field == "promise":
                    mortal_plus_type = bio.get("template_type", "").lower()
                    if mortal_plus_type not in ["fae-touched", "fae_touched"]:
                        continue
                
                # Check bio first, then other as fallback (for existing characters that may have these in other)
                field_value = bio.get(field, other.get(field, "<not set>"))
                
                # Special display labels for certain fields
                if field == "cover_identity":
                    field_label = "Cover ID"
                elif field == "template_type":
                    field_label = "Type"
                    # Format template_type: replace underscores/hyphens with spaces and title case
                    if field_value != "<not set>":
                        field_value = field_value.replace("_", " ").replace("-", " ").title()
                elif field == "subtype":
                    # Check Mortal+ type to determine label
                    mortal_plus_type = bio.get("template_type", "").lower()
                    
                    # Wolf-Blooded: show as "Tell"
                    if "wolf" in mortal_plus_type:
                        field_label = "Tell"
                        # Format Tell name: replace underscores with spaces and title case
                        if field_value != "<not set>":
                            field_value = field_value.replace("_", " ").title()
                    # Ghoul: show as "Clan"
                    elif mortal_plus_type == "ghoul":
                        field_label = "Clan"
                        # Format clan name: replace underscores with spaces and title case
                        if field_value != "<not set>":
                            field_value = field_value.replace("_", " ").title()
                    # Fae-Touched and certain other types: skip subtype entirely
                    elif mortal_plus_type in ["fae-touched", "fae_touched", "psychic", "lost boy", "dreamer", "atariya", "infected", "psychic vampire"]:
                        continue  
                    else:
                        field_label = "Subtype"
                        # Format subtype: replace underscores with spaces and title case
                        if field_value != "<not set>":
                            field_value = field_value.replace("_", " ").title()
                else:
                    field_label = field.replace("_", " ").title()
                    
                    capitalization_fixes = {
                        "burden": True,  # Geist
                        "seeming": True, "kith": True, "court": True,  # Changeling
                        "guild": True, "judge": True, "decree": True,  # Mummy
                        "incarnation": True, "agenda": True, "catalyst": True,  # Demon
                        "origin": True, "clade": True, "conspiracy": True,  # Deviant
                        "auspice": True,  # Werewolf
                        "clan": True, "bloodline": True,  # Vampire
                        "lineage": True, "refinement": True  # Promethean
                    }
                    # Special handling for keeper and entitlement - use title case (all words capitalized)
                    if field in ["keeper", "entitlement"] and field_value != "<not set>":
                        field_value = field_value.replace("_", " ").replace("-", " ").title()
                    elif field in capitalization_fixes and field_value != "<not set>":
                        # Convert to sentence case (first letter uppercase, rest lowercase)
                        field_value = field_value.capitalize()
                
                bio_items.append((field_label, field_value))
        
        # Add current form for Werewolves
        if template.lower() == "werewolf":
            from commands.shapeshifting import WEREWOLF_FORMS
            current_form = getattr(target.db, 'current_form', 'hishu')
            if current_form not in WEREWOLF_FORMS:
                current_form = 'hishu'
            form_display = WEREWOLF_FORMS[current_form]['display_name']
            # Add visual indicator if not in base form
            if current_form != 'hishu':
                form_display = f"|y{form_display} (SHIFTED)|n"
            bio_items.append(("Current Form", form_display))
        
        # Display bio items in two-column format
        for i in range(0, len(bio_items), 2):
            left_label, left_value = bio_items[i]
            left_text = f"{left_label:<12}: {left_value}"
            
            if i + 1 < len(bio_items):
                right_label, right_value = bio_items[i + 1]
                right_text = f"{right_label:<12}: {right_value}"
            else:
                right_text = ""
            
            left_formatted = left_text.ljust(39)
            output.append(f"{left_formatted} {right_text}")
        
        # In legacy mode, add detailed virtue/vice information
        if legacy_mode and virtue is not None and vice is not None:
            output.append("")  # Add spacing
            legacy_virtue_vice = self._format_legacy_virtue_vice(virtue, vice)
            output.extend(legacy_virtue_vice)
        
        # Attributes
        attrs = target.db.stats.get("attributes", {})
        if attrs:
            output.append(self._format_section_header("|wATTRIBUTES|n"))
            
            # Mental
            mental = []
            for attr in ["intelligence", "wits", "resolve"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                if use_numeric:
                    attr_name = attr.title()
                    padding = '.' * (20 - len(attr_name))
                    mental.append(f"{attr_name}{padding}{dots}")
                else:
                    mental.append(f"{attr.title():<15} {dots}")
            
            # Physical
            physical = []
            for attr in ["strength", "dexterity", "stamina"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                if use_numeric:
                    attr_name = attr.title()
                    padding = '.' * (20 - len(attr_name))
                    physical.append(f"{attr_name}{padding}{dots}")
                else:
                    physical.append(f"{attr.title():<15} {dots}")
            
            # Social
            social = []
            for attr in ["presence", "manipulation", "composure"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                if use_numeric:
                    attr_name = attr.title()
                    padding = '.' * (20 - len(attr_name))
                    social.append(f"{attr_name}{padding}{dots}")
                else:
                    social.append(f"{attr.title():<15} {dots}")
            
            # Display in columns (aligned with skills)
            for i in range(3):
                row = mental[i].ljust(26) + physical[i].ljust(26) + social[i]
                output.append(row)
            
            # Add note if werewolf is shifted
            if template.lower() == "werewolf":
                current_form = getattr(target.db, 'current_form', 'hishu')
                if current_form != 'hishu':
                    output.append("|y  ▸ Attributes modified by current form (temporary bonuses)|n")
        
        # Skills
        skills = target.db.stats.get("skills", {})
        specialties = target.db.stats.get("specialties", {})
        if skills:
            output.append(self._format_section_header("|wSKILLS|n"))
            
            # Mental Skills
            mental_skills = ["academics", "computer", "crafts", "investigation", "medicine", "occult", "politics", "science"]
            mental_display = []
            mental_specialties = []
            for skill in mental_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_name = skill.replace('_', ' ').title()
                if use_numeric:
                    padding = '.' * (20 - len(skill_name))
                    skill_text = f"{skill_name}{padding}{dots}"
                else:
                    skill_text = f"{skill_name:<15} {dots}"
                mental_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    mental_specialties.append(f"  ({specialty_list})")
                else:
                    mental_specialties.append("")
            
            # Physical Skills
            physical_skills = ["athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry"]
            physical_display = []
            physical_specialties = []
            for skill in physical_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_name = skill.replace('_', ' ').title()
                if use_numeric:
                    padding = '.' * (20 - len(skill_name))
                    skill_text = f"{skill_name}{padding}{dots}"
                else:
                    skill_text = f"{skill_name:<15} {dots}"
                physical_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    physical_specialties.append(f"  ({specialty_list})")
                else:
                    physical_specialties.append("")
            
            # Social Skills
            social_skills = ["animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]
            social_display = []
            social_specialties = []
            for skill in social_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_name = skill.replace('_', ' ').title()
                if use_numeric:
                    padding = '.' * (20 - len(skill_name))
                    skill_text = f"{skill_name}{padding}{dots}"
                else:
                    skill_text = f"{skill_name:<15} {dots}"
                social_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    social_specialties.append(f"  ({specialty_list})")
                else:
                    social_specialties.append("")
            
            max_rows = max(len(mental_display), len(physical_display), len(social_display))
            for i in range(max_rows):
                row = ""
                if i < len(mental_display):
                    row += mental_display[i].ljust(26)
                else:
                    row += " " * 26
                if i < len(physical_display):
                    row += physical_display[i].ljust(26)
                else:
                    row += " " * 26
                if i < len(social_display):
                    row += social_display[i]
                output.append(row)
            
            # Display all specialties at the bottom of the skills section
            specialty_groups = []
            for skill_name, specialty_list in specialties.items():
                if specialty_list:
                    skill_display = skill_name.replace('_', ' ').title()
                    specialty_text = ", ".join(specialty_list)
                    specialty_groups.append(f"{skill_display} ({specialty_text})")
            
            if specialty_groups:
                output.append("")  # Empty line before specialties
                # Join all specialty groups with commas and wrap to fit line length
                specialties_text = ", ".join(specialty_groups)
                output.append(f"|cSpecialties:|n")
                output.append(f"  {specialties_text}")
        
        # Merits and Advantages sections side by side
        merits = target.db.stats.get("merits", {})
        advantages = target.db.stats.get("advantages", {})
        other = target.db.stats.get("other", {})
        template = other.get("template", "Mortal").lower().replace(" ", "_")
        
        merit_list = []
        if merits:
            for merit_name, merit_data in sorted(merits.items()):
                dots = self._format_dots(merit_data.get("dots", 1), merit_data.get("max_dots", 5), force_ascii)
                
                # Format merit display with instance if present
                display_name = merit_name
                if ":" in merit_name:
                    base_name, instance = merit_name.split(":", 1)
                    display_name = f"{base_name.replace('_', ' ').title()} ({instance.replace('_', ' ').title()})"
                else:
                    display_name = merit_name.replace('_', ' ').title()
                
                if use_numeric:
                    padding = '.' * (30 - len(display_name))
                    merit_display = f"{display_name}{padding}{dots}"
                else:
                    merit_display = f"{display_name:<30} {dots}"
                merit_list.append(merit_display)
        
        if use_numeric:
            advantage_list = [
                f"  Defense................... {advantages.get('defense', 0)}",
                f"  Speed..................... {advantages.get('speed', 0)}",
                f"  Initiative................ {advantages.get('initiative', 0)}",
                f"  Size...................... {other.get('size', 5)}"
            ]
        else:
            advantage_list = [
                f"{'Defense':<15} : {advantages.get('defense', 0)}",
                f"{'Speed':<15} : {advantages.get('speed', 0)}",
                f"{'Initiative':<15} : {advantages.get('initiative', 0)}",
                f"{'Size':<15} : {other.get('size', 5)}"
            ]
        
        # Add integrity to advantages (except for Geist characters who don't use integrity)
        if template != "geist":
            integrity_name = target.get_integrity_name(template)
            if use_numeric:
                padding = '.' * (26 - len(integrity_name))
                advantage_list.append(f"  {integrity_name}{padding} {other.get('integrity', 7)}")
            else:
                advantage_list.append(f"  {integrity_name:<21} : {other.get('integrity', 7)}")
        
        # Add template-specific advantages
        if template == "changeling":
            wyrd = advantages.get("wyrd", 0)
            if wyrd > 0:
                if use_numeric:
                    advantage_list.append(f"  Wyrd...................... {wyrd}")
                else:
                    advantage_list.append(f"{'Wyrd':<15} : {wyrd}")
        elif template == "werewolf":
            primal_urge = advantages.get("primal_urge", 0)
            if primal_urge > 0:
                if use_numeric:
                    advantage_list.append(f"  Primal Urge............... {primal_urge}")
                else:
                    advantage_list.append(f"{'Primal Urge':<15} : {primal_urge}")
        elif template == "vampire":
            blood_potency = advantages.get("blood_potency", 0)
            if blood_potency > 0:
                if use_numeric:
                    advantage_list.append(f"  Blood Potency............. {blood_potency}")
                else:
                    advantage_list.append(f"{'Blood Potency':<15} : {blood_potency}")
        elif template == "mage":
            gnosis = advantages.get("gnosis", 0)
            if gnosis > 0:
                if use_numeric:
                    advantage_list.append(f"  Gnosis.................... {gnosis}")
                else:
                    advantage_list.append(f"{'Gnosis':<15} : {gnosis}")
        elif template == "deviant":
            deviation = advantages.get("deviation", 0)
            if deviation > 0:
                if use_numeric:
                    advantage_list.append(f"  Deviation................. {deviation}")
                else:
                    advantage_list.append(f"{'Deviation':<15} : {deviation}")
        elif template == "demon":
            primum = advantages.get("primum", 0)
            if primum > 0:
                if use_numeric:
                    advantage_list.append(f"  Primum.................... {primum}")
                else:
                    advantage_list.append(f"{'Primum':<15} : {primum}")
        elif template == "promethean":
            azoth = advantages.get("azoth", 0)
            if azoth > 0:
                if use_numeric:
                    advantage_list.append(f"  Azoth..................... {azoth}")
                else:
                    advantage_list.append(f"{'Azoth':<15} : {azoth}")
        elif template == "geist":
            # Geist characters use Synergy instead of integrity
            synergy = advantages.get("synergy", 1)
            if use_numeric:
                advantage_list.append(f"  Synergy................... {synergy}")
            else:
                advantage_list.append(f"{'Synergy':<15} : {synergy}")
        elif template == "legacy_changingbreeds":
            feral_heart = advantages.get("feral_heart", 1)
            if feral_heart > 0:
                if use_numeric:
                    advantage_list.append(f"  Feral Heart............... {feral_heart}")
                else:
                    advantage_list.append(f"{'Feral Heart':<15} : {feral_heart}")
        
        merits_header = f"|g<{'-' * 12} MERITS {'-' * 13}>|n"
        advantages_header = f"|g<{'-' * 10} ADVANTAGES {'-' * 11}>|n"
        output.append(f"{merits_header.ljust(42)} {advantages_header}")
        
        max_rows = max(len(merit_list) if merit_list else 1, len(advantage_list))
        for i in range(max_rows):
            left_item = merit_list[i] if i < len(merit_list) else ""
            right_item = advantage_list[i] if i < len(advantage_list) else ""
            
            if not merit_list and i == 0:
                left_item = "No merits yet."
            
            left_formatted = left_item.ljust(38)
            output.append(f"{left_formatted}{right_item}")
        
        # Add note if werewolf is shifted
        if template.lower() == "werewolf":
            current_form = getattr(target.db, 'current_form', 'hishu')
            if current_form != 'hishu':
                output.append(" " * 42 + " |y▸ Modified by form|n")
        
        if template == "legacy_changingbreeds":
            favors = target.db.stats.get("favors", {})
            aspects = target.db.stats.get("aspects", {})
            
            favor_list = []
            if favors:
                for favor_name, favor_data in sorted(favors.items()):
                    if isinstance(favor_data, dict):
                        dots = favor_data.get("dots", 0)
                        if dots > 0:
                            dots_display = self._format_dots(dots, favor_data.get("max_dots", 5), force_ascii)
                            favor_name_display = favor_name.replace('_', ' ').title()
                            # Use dot padding in numeric mode for better readability
                            if use_numeric:
                                padding = '.' * (37 - len(favor_name_display))
                                favor_display = f"{favor_name_display}{padding}{dots_display}"
                            else:
                                favor_display = f"{favor_name_display:<37} {dots_display}"
                        else:
                            favor_display = f"{favor_name.replace('_', ' ').title()}"
                    else:
                        favor_display = f"{favor_name.replace('_', ' ').title()}"
                    favor_list.append(favor_display)
            
            aspect_list = []
            if aspects:
                for aspect_name, aspect_data in sorted(aspects.items()):
                    if isinstance(aspect_data, dict):
                        dots = aspect_data.get("dots", 0)
                        if dots > 0:
                            dots_display = self._format_dots(dots, aspect_data.get("max_dots", 5), force_ascii)
                            aspect_name_display = aspect_name.replace('_', ' ').title()
                            # Use dot padding in numeric mode for better readability
                            if use_numeric:
                                padding = '.' * (37 - len(aspect_name_display))
                                aspect_display = f"{aspect_name_display}{padding}{dots_display}"
                            else:
                                aspect_display = f"{aspect_name_display:<37} {dots_display}"
                        else:
                            aspect_display = f"{aspect_name.replace('_', ' ').title()}"
                    else:
                        aspect_display = f"{aspect_name.replace('_', ' ').title()}"
                    aspect_list.append(aspect_display)
            
            favors_header = f"|g<{'-' * 12} FAVORS {'-' * 13}>|n"
            aspects_header = f"|g<{'-' * 10} ASPECTS {'-' * 11}>|n"
            output.append(f"{favors_header.ljust(42)} {aspects_header}")
            
            max_rows = max(len(favor_list) if favor_list else 1, len(aspect_list) if aspect_list else 1)
            for i in range(max_rows):
                left_item = favor_list[i] if i < len(favor_list) else ""
                right_item = aspect_list[i] if i < len(aspect_list) else ""
                
                if not favor_list and i == 0:
                    left_item = "No favors yet."
                if not aspect_list and i == 0:
                    right_item = "No aspects yet."
                
                left_formatted = left_item.ljust(38)
                output.append(f"{left_formatted}{right_item}")
        
        # Primary Powers (disciplines, arcana, gifts)
        powers = target.db.stats.get("powers", {})
        template_powers = self._get_template_powers(template)
        template_secondary_powers = self._get_template_secondary_powers(template)
        
        # Determine section names based on template
        primary_section_names = {
            'vampire': 'DISCIPLINES',
            'legacy_vampire': 'DISCIPLINES',
            'mage': 'ARCANA',
            'legacy_mage': 'ARCANA',
            'werewolf': 'GIFTS',
            'legacy_werewolf': 'GIFTS',
            'changeling': 'CONTRACTS',
            'legacy_changeling': 'CONTRACTS',
            'geist': 'KEYS',
            'legacy_geist': 'KEYS',
            'promethean': 'TRANSMUTATIONS',
            'legacy_promethean': 'TRANSMUTATIONS',
            'demon': 'EMBEDS',
            'hunter': 'ENDOWMENTS',
            'legacy_hunter': 'TACTICS',
            'deviant': 'VARIATIONS'
        }
        secondary_section_names = {
            'vampire': 'BLOOD SORCERY & COILS',
            'werewolf': 'RITES',
            'geist': 'CEREMONIES',
            'promethean': 'BESTOWMENTS',
            'demon': 'EXPLOITS',
            'hunter': 'TACTICS',
            'deviant': 'RITUALS'
        }
        
        primary_section = primary_section_names.get(template.lower(), 'POWERS')
        secondary_section = secondary_section_names.get(template.lower(), 'RITUALS')
        
        # Special handling for Geist characters (Keys, Haunts, Ceremonies)
        if template.lower() == "geist":
            # Keys section (from geist_stats)
            output.append(self._format_section_header("|wKEYS|n"))
            
            if hasattr(target.db, 'geist_stats') and target.db.geist_stats:
                geist_keys = target.db.geist_stats.get("keys", {})
                key_list = []
                for key_name, has_key in geist_keys.items():
                    if has_key:
                        key_list.append(key_name.replace("_", " ").title())
                
                if key_list:
                    # Display keys in 2 columns
                    for i in range(0, len(key_list), 2):
                        left_key = key_list[i] if i < len(key_list) else ""
                        right_key = key_list[i + 1] if i + 1 < len(key_list) else ""
                        
                        left_formatted = left_key.ljust(42)
                        output.append(f"{left_formatted} {right_key}")
                else:
                    output.append("No keys unlocked yet.")
            else:
                output.append("No keys unlocked yet.")
            
            output.append("")
            output.append("|gSee +sheet/geist for detailed key information and geist character sheet.|n")
            
            # Haunts section (category powers stored in regular powers)
            output.append(self._format_section_header("|wHAUNTS|n"))
            
            # Get haunts from regular powers or geist_stats
            haunts_from_powers = {}
            haunts_from_geist = {}
            
            # Check regular powers for haunts
            haunt_names = ["boneyard", "caul", "curse", "dirge", "marionette", "memoria", "oracle", "rage", "shroud", "tomb"]
            for haunt_name in haunt_names:
                if haunt_name in powers and powers[haunt_name] > 0:
                    haunts_from_powers[haunt_name] = powers[haunt_name]
            
            # Check geist_stats for haunts  
            if hasattr(target.db, 'geist_stats') and target.db.geist_stats:
                geist_haunts = target.db.geist_stats.get("haunts", {})
                for haunt_name, rating in geist_haunts.items():
                    if rating > 0:
                        haunts_from_geist[haunt_name] = rating
            
            # Combine and display haunts
            all_haunts = {**haunts_from_powers, **haunts_from_geist}
            if all_haunts:
                haunt_list = []
                for haunt_name, haunt_rating in all_haunts.items():
                    dots = self._format_dots(haunt_rating, 5, force_ascii)
                    haunt_name_display = haunt_name.replace('_', ' ').title()
                    # Use dot padding in numeric mode for better readability
                    if use_numeric:
                        padding = '.' * (37 - len(haunt_name_display))
                        haunt_display = f"{haunt_name_display}{padding}{dots}"
                    else:
                        haunt_display = f"{haunt_name_display:<37} {dots}"
                    haunt_list.append(haunt_display)
                
                # Display haunts in 2 columns like merits
                for i in range(0, len(haunt_list), 2):
                    left_haunt = haunt_list[i] if i < len(haunt_list) else ""
                    right_haunt = haunt_list[i + 1] if i + 1 < len(haunt_list) else ""
                    
                    # Format with proper spacing (39 chars for left column)
                    left_formatted = left_haunt.ljust(42)
                    output.append(f"{left_formatted} {right_haunt}")
            else:
                output.append("No haunts learned yet.")
            
            # Ceremonies section (individual abilities stored in regular powers)
            output.append(self._format_section_header("|wCEREMONIES|n"))
            
            ceremony_names = [
                "dead_mans_camera", "death_watch", "diviners_jawbone", "lovers_telephone", "ishtars_perfume",
                "crow_girl_kiss", "gifts_of_persephone", "ghost_trap", "skeleton_key", "bestow_regalia", 
                "krewe_binding", "speaker_for_the_dead", "black_cats_crossing", "bloody_codex", "dumb_supper",
                "forge_anchor", "maggot_homonculus", "pass_on", "ghost_binding", "persephones_return"
            ]
            
            ceremony_list = []
            for ceremony_name in ceremony_names:
                if ceremony_name in powers and powers[ceremony_name] > 0:
                    ceremony_display = ceremony_name.replace('_', ' ').title()
                    ceremony_list.append(ceremony_display)
            
            if ceremony_list:
                # Display ceremonies in 2 columns
                for i in range(0, len(ceremony_list), 2):
                    left_ceremony = ceremony_list[i] if i < len(ceremony_list) else ""
                    right_ceremony = ceremony_list[i + 1] if i + 1 < len(ceremony_list) else ""
                    
                    left_formatted = left_ceremony.ljust(42)
                    output.append(f"{left_formatted} {right_ceremony}")
            else:
                output.append("No ceremonies learned yet.")
        
        else:
            # Regular template power display (skip for hunter since endowments are handled separately)
            # Also skip powers section for certain Mortal+ types that use merits instead
            # Skip Werewolf primary powers (GIFTS) since they only have individual facets, not rated gifts
            skip_powers = False
            if template.lower() == "mortal_plus" or template.lower() == "mortal plus":
                template_type = bio.get("template_type", "").lower()
                no_power_types = ["psychic", "lost boy", "dreamer", "atariya", "infected", "psychic vampire"]
                if template_type in no_power_types:
                    skip_powers = True
            elif template.lower() == "werewolf":
                skip_powers = True  # Werewolves don't have rated gifts, only individual facets
            
            if template.lower() != "hunter" and not skip_powers:
                if powers or template_powers:
                    output.append(self._format_section_header(f"|w{primary_section}|n"))
                    
                    if template_powers:
                        power_display = self._format_powers_display(powers, template_powers, force_ascii, use_numeric, template)
                        output.extend(power_display)
                    else:
                        output.append("No primary powers available for this template.")
        
        # Secondary Powers (rituals, rites, blood sorcery) - skip for Geist, Hunter, Werewolf, and Vampire since handled separately
        # Also check if section would be empty before displaying
        if template.lower() not in ["geist", "hunter", "werewolf", "vampire"] and (powers or template_secondary_powers):
            if template_secondary_powers:  # Only show section if template has secondary powers
                # Check if there are any secondary powers actually learned
                has_secondary_powers = False
                for power_name in template_secondary_powers:
                    power_value = powers.get(power_name, 0)
                    if power_value == "known" or (isinstance(power_value, int) and power_value > 0):
                        has_secondary_powers = True
                        break
                
                if has_secondary_powers:
                    output.append(self._format_section_header(f"|w{secondary_section}|n"))
                    secondary_power_display = self._format_secondary_powers_display(powers, template_secondary_powers, force_ascii, use_numeric)
                    output.extend(secondary_power_display)
                
                # Add hint for demon characters
                if template.lower() == "demon":
                    output.append("")
                    output.append("|gSee +sheet/demon for detailed demonic form traits (Modifications, Technologies, Propulsion, Process).|n")
        
        # Mage Spells section (individual spells without ratings)
        if template.lower() in ["mage", "legacy_mage"]:
            output.append(self._format_section_header("|wSPELLS|n"))
            
            # Get all spell powers
            from world.cofd.powers.mage_spells import ALL_MAGE_SPELLS, get_spell
            
            spell_list = []
            for power_name, value in powers.items():
                if power_name.startswith("spell:") and value == "known":
                    # Extract spell key from "spell:spell_name"
                    spell_key = power_name[6:]  # Remove "spell:" prefix
                    
                    # Look up spell data
                    spell_data = get_spell(spell_key)
                    if spell_data:
                        # Format arcana dots (e.g., "●●●●●" for level 5)
                        spell_level = spell_data['level']
                        arcana_dots = self._format_dots(spell_level, 5, force_ascii)
                        arcana_name = spell_data['arcana'].title()
                        
                        spell_display = f"{spell_data['name']} ({arcana_name} {arcana_dots})"
                        spell_list.append(spell_display)
                    else:
                        # Spell not found in database, show as unknown
                        spell_display = f"{spell_key.replace('_', ' ').title()} (Unknown Spell)"
                        spell_list.append(spell_display)
            
            if spell_list:
                # Display spells in single column for readability
                for spell in sorted(spell_list):
                    output.append(f"  {spell}")
            else:
                output.append("No spells learned yet.")
            
            output.append("")
            output.append("|gSee +sheet/mage for Nimbus, Obsessions, Praxes, and Dedicated Tool.|n")
        
        # Hunter Endowments section (individual powers without ratings)
        if template.lower() == "hunter":
            output.append(self._format_section_header("|wENDOWMENTS|n"))
            
            # Get all endowment powers
            from world.cofd.powers.hunter_endowments import get_endowment
            
            endowment_list = []
            for power_name, value in powers.items():
                if power_name.startswith("endowment:") and value == "known":
                    # Extract endowment key from "endowment:endowment_name"
                    endowment_key = power_name[10:]  # Remove "endowment:" prefix
                    
                    # Look up endowment data
                    power_data = get_endowment(endowment_key)
                    if power_data:
                        endowment_type = power_data['endowment_type'].replace('_', ' ').title()
                        # Truncate name if too long for 2-column display (max 35 chars with type info)
                        endowment_name = power_data['name']
                        endowment_display = f"{endowment_name} ({endowment_type})"
                        endowment_list.append(endowment_display)
                    else:
                        # Endowment not found in database, show as unknown
                        endowment_display = f"{endowment_key.title()} (Unknown Endowment)"
                        endowment_list.append(endowment_display)
            
            if endowment_list:
                # Display endowments in 2 columns for space efficiency
                sorted_endowments = sorted(endowment_list)
                for i in range(0, len(sorted_endowments), 2):
                    left_endowment = sorted_endowments[i] if i < len(sorted_endowments) else ""
                    right_endowment = sorted_endowments[i + 1] if i + 1 < len(sorted_endowments) else ""
                    
                    # Truncate if needed (39 chars for left column)
                    if len(left_endowment) > 37:
                        left_endowment = left_endowment[:34] + "..."
                    if len(right_endowment) > 37:
                        right_endowment = right_endowment[:34] + "..."
                    
                    left_formatted = left_endowment.ljust(42)
                    output.append(f"  {left_formatted} {right_endowment}")
            else:
                output.append("No endowment powers learned yet.")
            
            output.append("")
            
            # Tactics section
            output.append(self._format_section_header("|wTACTICS|n"))
            
            from world.cofd.powers.hunter_tactics import get_all_tactics
            
            all_tactics = get_all_tactics()
            tactic_list = []
            
            # Check for tactics stored directly (without prefix) or with "tactic:" prefix
            for power_name, value in powers.items():
                tactic_key = None
                if power_name.startswith("tactic:"):
                    tactic_key = power_name[7:]  # Remove "tactic:" prefix
                elif power_name in all_tactics:
                    tactic_key = power_name
                
                if tactic_key and (value == "known" or (isinstance(value, int) and value > 0)):
                    tactic_data = all_tactics.get(tactic_key)
                    if tactic_data:
                        tactic_type = tactic_data.get('category', 'Unknown').replace('_', ' ').title()
                        tactic_name = tactic_data.get('name', tactic_key.replace('_', ' ').title())
                        tactic_display = f"{tactic_name} ({tactic_type})"
                        tactic_list.append(tactic_display)
                    else:
                        tactic_display = f"{tactic_key.replace('_', ' ').title()} (Unknown Tactic)"
                        tactic_list.append(tactic_display)
            
            if tactic_list:
                # Display tactics in 2 columns
                sorted_tactics = sorted(tactic_list)
                for i in range(0, len(sorted_tactics), 2):
                    left_tactic = sorted_tactics[i] if i < len(sorted_tactics) else ""
                    right_tactic = sorted_tactics[i + 1] if i + 1 < len(sorted_tactics) else ""
                    
                    left_formatted = left_tactic.ljust(42)
                    output.append(f"  {left_formatted} {right_tactic}")
            else:
                output.append("No tactics learned yet.")
            
            output.append("")
        
        # Werewolf Gifts section (individual gifts without ratings)
        if template.lower() == "werewolf":
            output.append(self._format_section_header("|wGIFTS (FACETS)|n"))
            
            from world.cofd.powers.werewolf_gifts import get_gift
            
            gift_list = []
            for power_name, value in powers.items():
                if power_name.startswith("gift:") and value == "known":
                    # Extract gift key from "gift:gift_name"
                    gift_key = power_name[5:]  # Remove "gift:" prefix
                    
                    # Look up gift data
                    gift_data = get_gift(gift_key)
                    if gift_data:
                        renown = gift_data['renown'].title()
                        rank_dots = self._format_dots(gift_data['rank'], 5, force_ascii)
                        
                        gift_display = f"{gift_data['name']} ({renown} {rank_dots})"
                        gift_list.append(gift_display)
                    else:
                        # Gift not found, show as unknown
                        gift_display = f"{gift_key.replace('_', ' ').title()} (Unknown Gift)"
                        gift_list.append(gift_display)
            
            if gift_list:
                # Display gifts in single column for readability
                for gift in sorted(gift_list):
                    output.append(f"  {gift}")
            else:
                output.append("No gifts learned yet.")
            
            output.append("")
        
        # Vampire Discipline Powers/Devotions/Ritual sections
        if template.lower() == "vampire":
            from world.cofd.powers.vampire_disciplines import get_discipline_power, ALL_DEVOTIONS
            from world.cofd.powers.vampire_rituals import get_ritual_power
            
            # Collect all vampire semantic powers by category
            vamp_powers = {}
            
            for power_name, value in powers.items():
                if value == "known":
                    if power_name.startswith("discipline_power:"):
                        key = power_name[17:]
                        data = get_discipline_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Discipline Powers" not in vamp_powers:
                            vamp_powers["Discipline Powers"] = []
                        vamp_powers["Discipline Powers"].append(name)
                    elif power_name.startswith("devotion:"):
                        key = power_name[9:]
                        data = ALL_DEVOTIONS.get(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Devotions" not in vamp_powers:
                            vamp_powers["Devotions"] = []
                        vamp_powers["Devotions"].append(name)
                    elif power_name.startswith("coil:"):
                        key = power_name[5:]
                        data = get_discipline_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Coils of the Dragon" not in vamp_powers:
                            vamp_powers["Coils of the Dragon"] = []
                        vamp_powers["Coils of the Dragon"].append(name)
                    elif power_name.startswith("scale:"):
                        key = power_name[6:]
                        data = get_ritual_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Scales of the Dragon" not in vamp_powers:
                            vamp_powers["Scales of the Dragon"] = []
                        vamp_powers["Scales of the Dragon"].append(name)
                    elif power_name.startswith("theban:"):
                        key = power_name[7:]
                        data = get_ritual_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Theban Sorcery" not in vamp_powers:
                            vamp_powers["Theban Sorcery"] = []
                        vamp_powers["Theban Sorcery"].append(name)
                    elif power_name.startswith("cruac:"):
                        key = power_name[6:]
                        data = get_ritual_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Cruac" not in vamp_powers:
                            vamp_powers["Cruac"] = []
                        vamp_powers["Cruac"].append(name)
            
            # Display each category that has powers in multicolumn format (3 columns, 80 chars)
            for category in ["Discipline Powers", "Devotions", "Coils of the Dragon", 
                           "Scales of the Dragon", "Theban Sorcery", "Cruac"]:
                if category in vamp_powers and vamp_powers[category]:
                    output.append(self._format_section_header(f"|w{category.upper()}|n"))
                    sorted_powers = sorted(vamp_powers[category])
                    # Display in 3 columns (max 26 chars per column to fit in 80 chars)
                    for i in range(0, len(sorted_powers), 3):
                        col1 = sorted_powers[i] if i < len(sorted_powers) else ""
                        col2 = sorted_powers[i + 1] if i + 1 < len(sorted_powers) else ""
                        col3 = sorted_powers[i + 2] if i + 2 < len(sorted_powers) else ""
                        
                        # Format each column (26 chars max, truncate if needed)
                        col1_formatted = col1[:26].ljust(26) if col1 else ""
                        col2_formatted = col2[:26].ljust(26) if col2 else ""
                        col3_formatted = col3[:26] if col3 else ""
                        
                        output.append(f"  {col1_formatted} {col2_formatted} {col3_formatted}")
                    output.append("")
        
        # Mummy Affinity and Utterance sections
        if template.lower() == "mummy":
            from world.cofd.powers.mummy_powers import MUMMY_AFFINITIES, MUMMY_UTTERANCES
            
            # Collect all mummy powers by category
            mummy_powers = {
                "Affinities": [],
                "Utterances": []
            }
            
            for power_name, value in powers.items():
                if value == "known" or (isinstance(value, int) and value > 0):
                    # Check for affinities
                    affinity_data = MUMMY_AFFINITIES.get(power_name)
                    if affinity_data:
                        name = affinity_data['name']
                        pillar = affinity_data.get('pillar', '')
                        if pillar:
                            mummy_powers["Affinities"].append(f"{name} ({pillar})")
                        else:
                            mummy_powers["Affinities"].append(name)
                    
                    # Check for utterances
                    utterance_data = MUMMY_UTTERANCES.get(power_name)
                    if utterance_data:
                        name = utterance_data['name']
                        tier = utterance_data.get('tier', '')
                        if tier:
                            mummy_powers["Utterances"].append(f"{name} [{tier}]")
                        else:
                            mummy_powers["Utterances"].append(name)
            
            # Display Affinities
            if mummy_powers["Affinities"]:
                output.append(self._format_section_header("|wAFFINITIES|n"))
                for power in sorted(mummy_powers["Affinities"]):
                    output.append(f"  {power}")
                output.append("")
            
            # Display Utterances
            if mummy_powers["Utterances"]:
                output.append(self._format_section_header("|wUTTERANCES|n"))
                # Group utterances by base name (remove tier info for sorting)
                utterance_dict = {}
                for power in mummy_powers["Utterances"]:
                    base_name = power.split('[')[0].strip()
                    if base_name not in utterance_dict:
                        utterance_dict[base_name] = []
                    utterance_dict[base_name].append(power)
                
                for base_name in sorted(utterance_dict.keys()):
                    for power in utterance_dict[base_name]:
                        output.append(f"  {power}")
                output.append("")
        
        # Mortal+ specific sections (Demon-Blooded, Wolf-Blooded, Sleepwalkers/Proximus)
        if template.lower() in ["mortal_plus", "mortal plus"]:
            template_type = bio.get("template_type", "").lower()
            
            # Demon-Blooded Level
            if "demon" in template_type or template_type == "demon-blooded":
                demon_level = bio.get("demon_blooded_level", bio.get("subtype", "<not set>"))
                if demon_level and demon_level != "<not set>":
                    output.append(self._format_section_header("|wDEMON-BLOODED|n"))
                    output.append(f"  Level: {demon_level.replace('_', ' ').title()}")
                    
                    # Display any embed powers they have
                    embed_list = []
                    for power_name, rating in powers.items():
                        if rating > 0 and "_embed" in power_name:
                            embed_display = power_name.replace("_embed", "").replace("_", " ").title()
                            embed_list.append(embed_display)
                    
                    if embed_list:
                        output.append(f"  Embeds: {', '.join(sorted(embed_list))}")
            
            # Wolf-Blooded Tells
            elif "wolf" in template_type or template_type == "wolf-blooded":
                tells = bio.get("wolf_blooded_tells", [])
                if not tells:
                    # Check if stored as single tell in subtype
                    subtype = bio.get("subtype", "")
                    if subtype and subtype != "<not set>":
                        tells = [subtype]
                
                output.append(self._format_section_header("|wWOLF-BLOODED TELLS|n"))
                
                if tells:
                    tell_list = []
                    if isinstance(tells, str):
                        tells = [tells]
                    for tell in tells:
                        tell_display = tell.replace("_", " ").title()
                        tell_list.append(tell_display)
                    
                    # Display tells in 2 columns
                    for i in range(0, len(tell_list), 2):
                        left_tell = tell_list[i] if i < len(tell_list) else ""
                        right_tell = tell_list[i + 1] if i + 1 < len(tell_list) else ""
                        
                        left_formatted = left_tell.ljust(42)
                        output.append(f"  {left_formatted} {right_tell}")
                else:
                    output.append("  No tells manifested yet.")
            
            # Sleepwalker/Proximus Spells
            elif template_type in ["sleepwalker", "proximus"]:
                output.append(self._format_section_header("|wSPELLS|n"))
                
                # Import spell data
                from world.cofd.powers.mage_spells import ALL_MAGE_SPELLS, get_spell
                
                # Get spell powers
                spell_list = []
                for power_name, value in powers.items():
                    # Check if it's a spell: notation power
                    if power_name.startswith("spell:") and value == "known":
                        # Extract spell key from "spell:spell_name"
                        spell_key = power_name[6:]  # Remove "spell:" prefix
                        
                        # Look up spell data
                        spell_data = get_spell(spell_key)
                        if spell_data:
                            # Format arcana dots (e.g., "●●●●●" for level 5)
                            spell_level = spell_data['level']
                            arcana_dots = self._format_dots(spell_level, 5, force_ascii)
                            arcana_name = spell_data['arcana'].title()
                            
                            spell_display = f"{spell_data['name']} ({arcana_name} {arcana_dots})"
                            spell_list.append(spell_display)
                        else:
                            # Spell not found in database, show as unknown
                            spell_display = f"{spell_key.replace('_', ' ').title()} (Unknown Spell)"
                            spell_list.append(spell_display)
                
                if spell_list:
                    # Display spells in single column for readability
                    for spell in sorted(spell_list):
                        output.append(f"  {spell}")
                else:
                    output.append("No spells learned yet.")
                    if template_type == "proximus":
                        output.append("|g(Proximus have access to limited mage spells)|n")
                    else:
                        output.append("|g(Sleepwalkers can learn spells from mages)|n")
            
            # Psychic Powers
            elif template_type == "psychic":
                psychic_powers = []
                from world.cofd.templates.mortal_plus import PSYCHIC_POWERS
                
                for power_name in PSYCHIC_POWERS:
                    power_key = power_name.replace(" ", "_").lower()
                    if power_key in powers and powers[power_key] > 0:
                        dots = self._format_dots(powers[power_key], 5, force_ascii)
                        power_display = f"{power_name.replace('_', ' ').title():<20} {dots}"
                        psychic_powers.append(power_display)
                
                if psychic_powers:
                    output.append(self._format_section_header("|wPSYCHIC POWERS|n"))
                    
                    # Display psychic powers in 2 columns
                    for i in range(0, len(psychic_powers), 2):
                        left_power = psychic_powers[i] if i < len(psychic_powers) else ""
                        right_power = psychic_powers[i + 1] if i + 1 < len(psychic_powers) else ""
                        
                        left_formatted = left_power.ljust(42)
                        output.append(f"{left_formatted} {right_power}")
        
        # Pools section (horizontal layout)
        output.append(self._format_section_header("|wPOOLS|n"))
        
        # Get pools data
        health_max = advantages.get("health", 7)
        health_track = self._get_health_track(target)
        
        # Save the compacted track back to ensure consistency
        self._set_health_track(target, health_track)
        
        # Calculate health statistics
        current_health, bashing_count, lethal_count, aggravated_count = self._calculate_health_stats(health_track, health_max)
        
        # Create health boxes
        health_boxes = []
        for i in range(health_max):
            damage_type = health_track[i]
            if damage_type == "bashing":
                health_boxes.append("[|c/|n]")  # Cyan for bashing
            elif damage_type == "lethal":
                health_boxes.append("[|rX|n]")  # Red for lethal
            elif damage_type == "aggravated":
                health_boxes.append("[|R*|n]")  # Bright red for aggravated
            else:
                health_boxes.append("[ ]")
        
        # Willpower - calculate dynamically if not in advantages
        willpower_max = advantages.get("willpower")
        if willpower_max is None:
            # Calculate from resolve + composure
            attrs = target.db.stats.get("attributes", {})
            resolve = attrs.get("resolve", 1)
            composure = attrs.get("composure", 1)
            willpower_max = resolve + composure
        willpower_current = target.db.willpower_current
        if willpower_current is None:
            willpower_current = willpower_max  # Default to full
        
        willpower_dots = self._format_dots(willpower_current, willpower_max, force_ascii, show_max=True)
        
        # Template-specific resource pools
        resource_pools = {
            "geist": ("Plasm", "plasm"),
            "changeling": ("Glamour", "glamour"), 
            "vampire": ("Vitae", "vitae"),
            "werewolf": ("Essence", "essence"),
            "mage": ("Mana", "mana"),
            "demon": ("Aether", "aether"),
            "promethean": ("Pyros", "pyros")
        }
        
        pool_display = ""
        if template in resource_pools:
            pool_name, pool_key = resource_pools[template]
            pool_current = getattr(target.db, f"{pool_key}_current", None)
            pool_max = advantages.get(pool_key, 10)  # Default max of 10 for most pools
            
            if pool_current is None:
                pool_current = pool_max  # Default to full
            
            pool_dots = self._format_dots(pool_current, pool_max, force_ascii, show_max=True)
            # In numeric mode, don't duplicate the max in label (it's shown below)
            if use_numeric:
                pool_display = pool_name
            else:
                pool_display = f"{pool_name} ({pool_current}/{pool_max})"
        
        # Create horizontal pools layout with health numeric display
        # Build health label with current/max and damage breakdown (always shown for health)
        health_label = f"Health ({current_health}/{health_max}"
        if bashing_count > 0 or lethal_count > 0 or aggravated_count > 0:
            damage_parts = []
            if bashing_count > 0:
                damage_parts.append(f"{bashing_count}B")
            if lethal_count > 0:
                damage_parts.append(f"{lethal_count}L")
            if aggravated_count > 0:
                damage_parts.append(f"{aggravated_count}A")
            health_label += f" - {' '.join(damage_parts)}"
        health_label += ")"
        
        # In numeric mode, don't duplicate the max in label (it's shown below)
        if use_numeric:
            willpower_label = "Willpower"
        else:
            willpower_label = f"Willpower ({willpower_current}/{willpower_max})"
        
        if use_numeric:
            # Numeric mode: Horizontal layout with numeric values
            # Health on left with boxes, pools on right
            if pool_display:
                # Three items: Health, Resource Pool, Willpower on same line
                pool_text = f"{pool_name}: {pool_current}/{pool_max}"
                output.append(f"{health_label:<28}{pool_text:<28}Willpower: {willpower_current}/{willpower_max}")
                output.append(f"{''.join(health_boxes)}")
            else:
                # Two items: Health, Willpower
                output.append(f"{health_label:<40}Willpower: {willpower_current}/{willpower_max}")
                output.append(f"{''.join(health_boxes):<40}")
        else:
            # Unicode mode: Side-by-side layout
            if pool_display:
                # Three pools: Health, Resource Pool, Willpower
                output.append(f"{health_label:^26}{pool_display:^26}{willpower_label:^26}")
                health_section = f"{''.join(health_boxes):^26}"
                pool_section = f"{pool_dots if 'pool_dots' in locals() else '':^26}"
                willpower_section = f"{willpower_dots:^26}"
                output.append(f"{health_section}{pool_section}{willpower_section}")
            else:
                # Two pools: Health, Willpower
                output.append(f"{health_label:^39}{willpower_label:^39}")
                health_section = f"{''.join(health_boxes):^39}"
                willpower_section = f"{willpower_dots:^39}"
                output.append(f"{health_section}{willpower_section}")

        # Aspirations (only show if there are any and not in legacy mode)
        if not legacy_mode:
            aspirations_list = [asp for asp in target.db.aspirations if asp] if target.db.aspirations else []
            if aspirations_list:
                output.append(self._format_section_header("|wASPIRATIONS|n"))
                for i, asp in enumerate(aspirations_list, 1):
                    # Handle both old format (strings) and new format (dicts)
                    try:
                        if "type" in asp and "description" in asp:
                            # New format dict (works with _SaverDict too)
                            asp_type = asp.get('type', 'short-term')
                            description = asp.get('description', str(asp))
                            type_label = "|c[ST]|n" if asp_type == 'short-term' else "|y[LT]|n"
                            output.append(f"{i}. {type_label} {description}")
                        else:
                            # Old format or string
                            output.append(f"{i}. {asp}")
                    except (TypeError, AttributeError):
                        # Fallback for any unexpected format
                        output.append(f"{i}. {asp}")
        
        # Legacy Experience (only show in legacy mode)
        if legacy_mode:
            output.append(self._format_section_header("|wEXPERIENCE|n"))
            legacy_xp = target.attributes.get('legacy_experience', default=0)
            output.append(f"Experience Points: |y{legacy_xp}|n")
        
        output.append(f"|y{'='*78}|n")
        
        self.caller.msg("\n".join(output))
    
    def show_geist_sheet(self):
        """Display the geist character sheet for Sin-Eaters"""
        # Determine target
        if self.args:
            target = search_character(self.caller, self.args.strip())
            if not target:
                return
        else:
            target = self.caller
        
        # Check if character is a Sin-Eater
        character_template = target.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() != "geist":
            self.caller.msg(f"{target.name} is not a Sin-Eater. Current template: {character_template}")
            self.caller.msg("Only Sin-Eater characters have a geist to display.")
            return
        
        # Check if geist stats exist
        if not hasattr(target.db, 'geist_stats') or not target.db.geist_stats:
            self.caller.msg(f"{target.name} has no geist character sheet set up yet.")
            self.caller.msg("Use +stat/geist <stat>=<value> to set geist stats.")
            return
        
        # Get dot style and check UTF-8 support
        force_ascii = "ascii" in self.switches
        filled_char, empty_char, supports_utf8, use_numeric = self._get_dots_style(force_ascii)
        
        # Import the template-specific render function
        from world.cofd.templates.geist import render_geist_sheet
        
        # Render the geist sheet
        output = render_geist_sheet(target, self.caller, force_ascii)
        
        if output is None:
            self.caller.msg(f"{target.name} has no geist character sheet set up yet.")
            self.caller.msg("Use +stat/geist <stat>=<value> to set geist stats.")
            return
        
        # Add encoding warning if needed
        if not supports_utf8 and not force_ascii:
            output.append("|y(ASCII mode due to encoding - see note above for UTF-8)|n")
        
        self.caller.msg("\n".join(output))
    
    def show_mage_sheet(self):
        """Display the mage-specific character sheet"""
        # Determine target
        if self.args:
            target = search_character(self.caller, self.args.strip())
            if not target:
                return
        else:
            target = self.caller
        
        # Check if character is a Mage
        character_template = target.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() not in ["mage", "legacy_mage"]:
            self.caller.msg(f"{target.name} is not a Mage. Current template: {character_template}")
            self.caller.msg("Only Mage characters have mage-specific details to display.")
            return
        
        # Get dot style and check UTF-8 support
        force_ascii = "ascii" in self.switches
        filled_char, empty_char, supports_utf8, use_numeric = self._get_dots_style(force_ascii)
        
        # Import the template-specific render function
        from world.cofd.templates.mage import render_mage_sheet
        
        # Render the mage sheet
        output = render_mage_sheet(target, self.caller, force_ascii)
        
        if output is None:
            self.caller.msg(f"{target.name} has no mage stats set up yet.")
            self.caller.msg("Use +stat/mage <stat>=<value> to set mage stats.")
            return
        
        # Add encoding warning if needed
        if not supports_utf8 and not force_ascii:
            output.append("|y(ASCII mode due to encoding - see note above for UTF-8)|n")
        
        self.caller.msg("\n".join(output))
    
    def show_demon_form_sheet(self):
        """Display the demonic form character sheet for Demons"""
        # Determine target
        if self.args:
            target = search_character(self.caller, self.args.strip())
            if not target:
                return
        else:
            target = self.caller
        
        # Check if character is a Demon
        character_template = target.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() != "demon":
            self.caller.msg(f"{target.name} is not a Demon. Current template: {character_template}")
            self.caller.msg("Only Demon characters have a demonic form to display.")
            return
        
        # Check if demon form stats exist
        if not hasattr(target.db, 'demon_form_stats') or not target.db.demon_form_stats:
            self.caller.msg(f"{target.name} has no demonic form character sheet set up yet.")
            self.caller.msg("Use +stat/demon <stat>=<value> to set demonic form traits.")
            return
        
        # Get dot style and check UTF-8 support
        force_ascii = "ascii" in self.switches
        filled_char, empty_char, supports_utf8, use_numeric = self._get_dots_style(force_ascii)
        
        # Import the template-specific render function
        from world.cofd.templates.demon import render_demon_form_sheet
        
        # Render the demon form sheet
        output = render_demon_form_sheet(target, self.caller, force_ascii)
        
        if output is None:
            self.caller.msg(f"{target.name} has no demonic form character sheet set up yet.")
            self.caller.msg("Use +stat/demon <stat>=<value> to set demonic form traits.")
            return
        
        # Add encoding warning if needed
        if not supports_utf8 and not force_ascii:
            output.append("|y(ASCII mode due to encoding - see note above for UTF-8)|n")
        
        self.caller.msg("\n".join(output))
    
    def show_deviant_sheet(self):
        """Display the Deviant-specific character sheet showing Variations and Scars"""
        # Determine target
        if self.args:
            target = search_character(self.caller, self.args.strip())
            if not target:
                return
        else:
            target = self.caller
        
        # Check if character is a Deviant
        character_template = target.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() != "deviant":
            self.caller.msg(f"{target.name} is not a Deviant. Current template: {character_template}")
            self.caller.msg("Only Deviant characters have Variations and Scars to display.")
            return
        
        # Get dot style and check UTF-8 support
        force_ascii = "ascii" in self.switches
        filled_char, empty_char, supports_utf8, use_numeric = self._get_dots_style(force_ascii)
        
        # Import the template-specific render function
        from world.cofd.templates.deviant import render_deviant_sheet
        
        # Render the deviant sheet
        output = render_deviant_sheet(target, self.caller, force_ascii)
        
        if output is None:
            self.caller.msg(f"{target.name} has no Deviant powers set up yet.")
            self.caller.msg("Use +stat to set variations and scars.")
            return
        
        # Add encoding warning if needed
        if not supports_utf8 and not force_ascii:
            output.append("|y(ASCII mode due to encoding - see note above for UTF-8)|n")
        
        self.caller.msg("\n".join(output))
    
    def _format_legacy_virtue_vice(self, virtue_name, vice_name):
        """Format legacy virtue and vice with detailed descriptions"""
        output = []
        
        # Virtue information
        if virtue_name and virtue_name != "<not set>":
            virtue_info = get_virtue_info(virtue_name)
            if virtue_info:
                output.append(f"|gVirtue: {virtue_info['name']}|n")
                output.append(f"  {virtue_info['description']}")
                output.append(f"  |cWillpower Regained:|n {virtue_info['willpower_condition']}")
                output.append("")
        
        # Vice information  
        if vice_name and vice_name != "<not set>":
            vice_info = get_vice_info(vice_name)
            if vice_info:
                output.append(f"|rVice: {vice_info['name']}|n")
                output.append(f"  {vice_info['description']}")
                output.append(f"  |cWillpower Regained:|n {vice_info['willpower_condition']}")
                output.append("")
        
        return output
    
    def show_sheet_to_others(self):
        """Show character sheet to room or specific player"""
        # Determine if showing to room or specific player
        if self.args:
            target_name = self.args.strip()
            show_to_room = False
        else:
            target_name = None
            show_to_room = True
        
        # The sheet always shows the caller's sheet
        character = self.caller
        
        # Check if character has stats
        if not character.db.stats:
            self.caller.msg("You don't have a character sheet set up yet.")
            self.caller.msg("Use +stat <stat>=<value> to set your stats.")
            return
        
        # Build the sheet output by temporarily redirecting messages
        # We'll capture the output by storing the original switches
        original_switches = self.switches[:]
        original_args = self.args
        
        # Remove 'show' from switches so we can call the normal display method
        display_switches = [s for s in self.switches if s != 'show']
        self.switches = display_switches
        self.args = ""  # Always show caller's sheet
        
        # Build sheet output
        sheet_output = []
        
        # Temporarily capture the output by overriding msg
        original_msg = self.caller.msg
        
        def capture_msg(text, **kwargs):
            sheet_output.append(text)
        
        self.caller.msg = capture_msg
        
        try:
            # Determine which sheet type to show
            if "geist" in display_switches:
                self.show_geist_sheet()
            elif "mage" in display_switches:
                self.show_mage_sheet()
            elif "demon" in display_switches:
                self.show_demon_form_sheet()
            elif "deviant" in display_switches:
                self.show_deviant_sheet()
            else:
                # Call the main sheet display logic
                # We need to manually call the sheet building code
                # since func() has early returns for switches
                if not character.db.stats:
                    self.caller.msg(f"{character.name} has no character sheet set up yet.")
                    return
                
                # Get dot style and check UTF-8 support
                force_ascii = "ascii" in display_switches
                filled_char, empty_char, supports_utf8, use_numeric = self._get_dots_style(force_ascii)
                
                # Build the sheet display (copying the main logic from func())
                output = self._build_main_sheet(character, force_ascii, supports_utf8)
                self.caller.msg("\n".join(output))
        finally:
            # Restore original msg function
            self.caller.msg = original_msg
            self.switches = original_switches
            self.args = original_args
        
        # Get the captured sheet output
        if not sheet_output:
            self.caller.msg("Failed to generate sheet output.")
            return
        
        sheet_display = "\n".join(sheet_output) if isinstance(sheet_output[0], str) else sheet_output[0]
        
        # Add header to indicate who is sharing
        share_header = f"|y{self.caller.name} shares their character sheet:|n\n"
        full_display = share_header + sheet_display
        
        if show_to_room:
            # Show to everyone in the room
            location = self.caller.location
            if not location:
                self.caller.msg("You are not in a room.")
                return
            
            # Send to everyone in the room except the caller
            location.msg_contents(full_display, exclude=[self.caller])
            self.caller.msg(f"You show your character sheet to the room.")
        else:
            # Show to a specific player
            target = search_object(target_name)
            
            if not target:
                self.caller.msg(f"Could not find player '{target_name}'.")
                return
            
            if len(target) > 1:
                self.caller.msg(f"Multiple matches found for '{target_name}'. Please be more specific.")
                return
            
            target = target[0]
            
            # Check if target is online
            if not target.sessions.all():
                self.caller.msg(f"{target.name} is not currently online.")
                return
            
            # Send to target
            target.msg(full_display)
            self.caller.msg(f"You show your character sheet to {target.name}.")
    
    def _build_main_sheet(self, target, force_ascii, supports_utf8):
        """Build the main character sheet output (extracted from func for reuse)"""
        # This is the main sheet building logic from func()
        
        # Get use_numeric flag for formatting
        _, _, _, use_numeric = self._get_dots_style(force_ascii)
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        legacy_mode = is_legacy_mode()
        
        # Build the sheet display
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{target.name.center(78)}|n")
        if target.db.approved:
            output.append(f"|g{'APPROVED'.center(78)}|n")
        else:
            output.append(f"|r{'NOT APPROVED'.center(78)}|n")
        
        # Show legacy mode status
        if legacy_mode:
            output.append(f"|m{'nWoD 1st Edition'.center(78)}|n")
        
        output.append(f"|y{'='*78}|n")
        
        # Bio Section
        output.append(self._format_section_header("|wBIO|n"))
        
        # Get bio information from stats
        bio = target.db.stats.get("bio", {})
        other = target.db.stats.get("other", {})
        
        # Bio data with defaults
        full_name = bio.get("full_name", bio.get("fullname", "<not set>"))
        birthdate = bio.get("birthdate", "<not set>")
        concept = bio.get("concept", "<not set>")
        template = other.get("template", "Mortal")
        
        # Get template-specific fields to determine what to show
        template_fields = self._get_template_bio_fields(template)
        
        # Only get virtue/vice if they're valid for this template
        virtue = bio.get("virtue", "<not set>") if "virtue" in template_fields else None
        vice = bio.get("vice", "<not set>") if "vice" in template_fields else None
        
        # Get elpis/torment for Prometheans
        elpis = bio.get("elpis", "<not set>") if "elpis" in template_fields else None
        torment = bio.get("torment", "<not set>") if "torment" in template_fields else None
        
        # Create a list of all bio items to display
        bio_items = [
            ("Full Name", full_name),
            ("Template", template),
            ("Birthdate", birthdate),
            ("Concept", concept)
        ]
        
        # Add virtue/vice if they're valid for this template
        if virtue is not None:
            bio_items.append(("Virtue", virtue))
        if vice is not None:
            bio_items.append(("Vice", vice))
        
        # Add elpis/torment if they're valid for this template (Prometheans)
        if elpis is not None:
            bio_items.append(("Elpis", elpis))
        if torment is not None:
            bio_items.append(("Torment", torment))
        
        # Add template-specific bio fields
        for field in template_fields:
            if field not in ["virtue", "vice", "elpis", "torment", "game_line"]:  # anchors already added, game_line is internal only
                # Skip abilities field for Mortal+ (those are merits)
                if field == "abilities":
                    continue
                
                # Skip regnant for non-Ghouls
                if field == "regnant":
                    mortal_plus_type = bio.get("template_type", "").lower()
                    if mortal_plus_type != "ghoul":
                        continue
                
                # Skip promise for non-Fae-Touched
                if field == "promise":
                    mortal_plus_type = bio.get("template_type", "").lower()
                    if mortal_plus_type not in ["fae-touched", "fae_touched"]:
                        continue
                
                # Check bio first, then other as fallback (for existing characters that may have these in other)
                field_value = bio.get(field, other.get(field, "<not set>"))
                
                # Special display labels for certain fields
                if field == "cover_identity":
                    field_label = "Cover ID"
                elif field == "template_type":
                    field_label = "Type"
                    # Format template_type: replace underscores/hyphens with spaces and title case
                    if field_value != "<not set>":
                        field_value = field_value.replace("_", " ").replace("-", " ").title()
                elif field == "subtype":
                    # Check Mortal+ type to determine label
                    mortal_plus_type = bio.get("template_type", "").lower()
                    
                    # Wolf-Blooded: show as "Tell"
                    if "wolf" in mortal_plus_type:
                        field_label = "Tell"
                        # Format Tell name: replace underscores with spaces and title case
                        if field_value != "<not set>":
                            field_value = field_value.replace("_", " ").title()
                    # Ghoul: show as "Clan"
                    elif mortal_plus_type == "ghoul":
                        field_label = "Clan"
                        # Format clan name: replace underscores with spaces and title case
                        if field_value != "<not set>":
                            field_value = field_value.replace("_", " ").title()
                    # Fae-Touched and certain other types: skip subtype entirely
                    elif mortal_plus_type in ["fae-touched", "fae_touched", "psychic", "lost boy", "dreamer", "atariya", "infected", "psychic vampire"]:
                        continue  # Skip this field
                    else:
                        field_label = "Subtype"
                        # Format subtype: replace underscores with spaces and title case
                        if field_value != "<not set>":
                            field_value = field_value.replace("_", " ").title()
                else:
                    field_label = field.replace("_", " ").title()
                    
                    # Fix capitalization for specific bio fields - use sentence case instead of title case
                    capitalization_fixes = {
                        "burden": True,  # Geist
                        "seeming": True, "kith": True, "court": True,  # Changeling
                        "guild": True, "judge": True, "decree": True,  # Mummy
                        "incarnation": True, "agenda": True, "catalyst": True,  # Demon
                        "origin": True, "clade": True, "conspiracy": True,  # Deviant
                        "auspice": True,  # Werewolf
                        "clan": True, "bloodline": True,  # Vampire
                        "lineage": True, "refinement": True  # Promethean
                    }
                    # Special handling for keeper and entitlement - use title case (all words capitalized)
                    if field in ["keeper", "entitlement"] and field_value != "<not set>":
                        field_value = field_value.replace("_", " ").replace("-", " ").title()
                    elif field in capitalization_fixes and field_value != "<not set>":
                        # Convert to sentence case (first letter uppercase, rest lowercase)
                        field_value = field_value.capitalize()
                
                bio_items.append((field_label, field_value))
        
        # Add current form for Werewolves
        if template.lower() == "werewolf":
            from commands.shapeshifting import WEREWOLF_FORMS
            current_form = getattr(target.db, 'current_form', 'hishu')
            if current_form not in WEREWOLF_FORMS:
                current_form = 'hishu'
            form_display = WEREWOLF_FORMS[current_form]['display_name']
            # Add visual indicator if not in base form
            if current_form != 'hishu':
                form_display = f"|y{form_display} (SHIFTED)|n"
            bio_items.append(("Current Form", form_display))
        
        # Display bio items in two-column format
        for i in range(0, len(bio_items), 2):
            left_label, left_value = bio_items[i]
            left_text = f"{left_label:<12}: {left_value}"
            
            if i + 1 < len(bio_items):
                right_label, right_value = bio_items[i + 1]
                right_text = f"{right_label:<12}: {right_value}"
            else:
                right_text = ""
            
            left_formatted = left_text.ljust(39)
            output.append(f"{left_formatted} {right_text}")
        
        # In legacy mode, add detailed virtue/vice information
        if legacy_mode and virtue is not None and vice is not None:
            output.append("")  # Add spacing
            legacy_virtue_vice = self._format_legacy_virtue_vice(virtue, vice)
            output.extend(legacy_virtue_vice)
        
        # Attributes
        attrs = target.db.stats.get("attributes", {})
        if attrs:
            output.append(self._format_section_header("|wATTRIBUTES|n"))
            
            # Mental
            mental = []
            for attr in ["intelligence", "wits", "resolve"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                # Use dot padding in numeric mode for better readability
                if use_numeric:
                    attr_name = attr.title()
                    padding = '.' * (15 - len(attr_name))
                    mental.append(f"{attr_name}{padding}{dots}")
                else:
                    mental.append(f"{attr.title():<15} {dots}")
            
            # Physical
            physical = []
            for attr in ["strength", "dexterity", "stamina"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                # Use dot padding in numeric mode for better readability
                if use_numeric:
                    attr_name = attr.title()
                    padding = '.' * (15 - len(attr_name))
                    physical.append(f"{attr_name}{padding}{dots}")
                else:
                    physical.append(f"{attr.title():<15} {dots}")
            
            # Social
            social = []
            for attr in ["presence", "manipulation", "composure"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                # Use dot padding in numeric mode for better readability
                if use_numeric:
                    attr_name = attr.title()
                    padding = '.' * (15 - len(attr_name))
                    social.append(f"{attr_name}{padding}{dots}")
                else:
                    social.append(f"{attr.title():<15} {dots}")
            
            # Display in columns (aligned with skills)
            for i in range(3):
                row = mental[i].ljust(26) + physical[i].ljust(26) + social[i]
                output.append(row)
            
            # Add note if werewolf is shifted
            if template.lower() == "werewolf":
                current_form = getattr(target.db, 'current_form', 'hishu')
                if current_form != 'hishu':
                    output.append("|y  ▸ Attributes modified by current form (temporary bonuses)|n")
        
        # Skills
        skills = target.db.stats.get("skills", {})
        specialties = target.db.stats.get("specialties", {})
        if skills:
            output.append(self._format_section_header("|wSKILLS|n"))
            
            # Mental Skills
            mental_skills = ["academics", "computer", "crafts", "investigation", "medicine", "occult", "politics", "science"]
            mental_display = []
            mental_specialties = []
            for skill in mental_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_name = skill.replace('_', ' ').title()
                # Use dot padding in numeric mode for better readability
                if use_numeric:
                    padding = '.' * (15 - len(skill_name))
                    skill_text = f"{skill_name}{padding}{dots}"
                else:
                    skill_text = f"{skill_name:<15} {dots}"
                mental_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    mental_specialties.append(f"  ({specialty_list})")
                else:
                    mental_specialties.append("")
            
            # Physical Skills
            physical_skills = ["athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry"]
            physical_display = []
            physical_specialties = []
            for skill in physical_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_name = skill.replace('_', ' ').title()
                # Use dot padding in numeric mode for better readability
                if use_numeric:
                    padding = '.' * (15 - len(skill_name))
                    skill_text = f"{skill_name}{padding}{dots}"
                else:
                    skill_text = f"{skill_name:<15} {dots}"
                physical_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    physical_specialties.append(f"  ({specialty_list})")
                else:
                    physical_specialties.append("")
            
            # Social Skills
            social_skills = ["animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]
            social_display = []
            social_specialties = []
            for skill in social_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_name = skill.replace('_', ' ').title()
                # Use dot padding in numeric mode for better readability
                if use_numeric:
                    padding = '.' * (15 - len(skill_name))
                    skill_text = f"{skill_name}{padding}{dots}"
                else:
                    skill_text = f"{skill_name:<15} {dots}"
                social_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    social_specialties.append(f"  ({specialty_list})")
                else:
                    social_specialties.append("")
            
            # Display skills in clean columns (no specialties inline)
            max_rows = max(len(mental_display), len(physical_display), len(social_display))
            for i in range(max_rows):
                row = ""
                if i < len(mental_display):
                    row += mental_display[i].ljust(26)
                else:
                    row += " " * 26
                if i < len(physical_display):
                    row += physical_display[i].ljust(26)
                else:
                    row += " " * 26
                if i < len(social_display):
                    row += social_display[i]
                output.append(row)
            
            # Display all specialties at the bottom of the skills section
            specialty_groups = []
            for skill_name, specialty_list in specialties.items():
                if specialty_list:
                    skill_display = skill_name.replace('_', ' ').title()
                    specialty_text = ", ".join(specialty_list)
                    specialty_groups.append(f"{skill_display} ({specialty_text})")
            
            if specialty_groups:
                output.append("")  # Empty line before specialties
                # Join all specialty groups with commas and wrap to fit line length
                specialties_text = ", ".join(specialty_groups)
                output.append(f"|cSpecialties:|n")
                output.append(f"  {specialties_text}")
        
        # Merits and Advantages sections side by side
        merits = target.db.stats.get("merits", {})
        advantages = target.db.stats.get("advantages", {})
        other = target.db.stats.get("other", {})
        template = other.get("template", "Mortal").lower().replace(" ", "_")
        
        # Create merits list
        merit_list = []
        if merits:
            for merit_name, merit_data in sorted(merits.items()):
                dots = self._format_dots(merit_data.get("dots", 1), merit_data.get("max_dots", 5), force_ascii)
                
                # Format merit display with instance if present
                display_name = merit_name
                if ":" in merit_name:
                    base_name, instance = merit_name.split(":", 1)
                    display_name = f"{base_name.replace('_', ' ').title()} ({instance.replace('_', ' ').title()})"
                else:
                    display_name = merit_name.replace('_', ' ').title()
                
                # Use dot padding in numeric mode for better readability
                if use_numeric:
                    padding = '.' * (28 - len(display_name))
                    merit_display = f"{display_name}{padding}{dots}"
                else:
                    merit_display = f"{display_name:<28} {dots}"
                merit_list.append(merit_display)
        
        # Create advantages list (including integrity)
        # Use dot padding in numeric mode for consistency
        if use_numeric:
            advantage_list = [
                f"Defense................... {advantages.get('defense', 0)}",
                f"Speed..................... {advantages.get('speed', 0)}",
                f"Initiative................ {advantages.get('initiative', 0)}",
                f"Size...................... {other.get('size', 5)}"
            ]
        else:
            advantage_list = [
                f"{'Defense':<15} : {advantages.get('defense', 0)}",
                f"{'Speed':<15} : {advantages.get('speed', 0)}",
                f"{'Initiative':<15} : {advantages.get('initiative', 0)}",
                f"{'Size':<15} : {other.get('size', 5)}"
            ]
        
        # Add integrity to advantages (except for Geist characters who don't use integrity)
        if template != "geist":
            integrity_name = target.get_integrity_name(template)
            if use_numeric:
                padding = '.' * (21 - len(integrity_name))
                advantage_list.append(f"{integrity_name}{padding} {other.get('integrity', 7)}")
            else:
                advantage_list.append(f"{integrity_name:<15} : {other.get('integrity', 7)}")
        
        # Add template-specific advantages
        if template == "changeling":
            wyrd = advantages.get("wyrd", 0)
            if wyrd > 0:
                if use_numeric:
                    advantage_list.append(f"Wyrd...................... {wyrd}")
                else:
                    advantage_list.append(f"{'Wyrd':<15} : {wyrd}")
        elif template == "werewolf":
            primal_urge = advantages.get("primal_urge", 0)
            if primal_urge > 0:
                if use_numeric:
                    advantage_list.append(f"Primal Urge............... {primal_urge}")
                else:
                    advantage_list.append(f"{'Primal Urge':<15} : {primal_urge}")
        elif template == "vampire":
            blood_potency = advantages.get("blood_potency", 0)
            if blood_potency > 0:
                if use_numeric:
                    advantage_list.append(f"Blood Potency............. {blood_potency}")
                else:
                    advantage_list.append(f"{'Blood Potency':<15} : {blood_potency}")
        elif template == "mage":
            gnosis = advantages.get("gnosis", 0)
            if gnosis > 0:
                if use_numeric:
                    advantage_list.append(f"Gnosis.................... {gnosis}")
                else:
                    advantage_list.append(f"{'Gnosis':<15} : {gnosis}")
        elif template == "deviant":
            deviation = advantages.get("deviation", 0)
            if deviation > 0:
                if use_numeric:
                    advantage_list.append(f"Deviation................. {deviation}")
                else:
                    advantage_list.append(f"{'Deviation':<15} : {deviation}")
        elif template == "demon":
            primum = advantages.get("primum", 0)
            if primum > 0:
                if use_numeric:
                    advantage_list.append(f"Primum.................... {primum}")
                else:
                    advantage_list.append(f"{'Primum':<15} : {primum}")
        elif template == "promethean":
            azoth = advantages.get("azoth", 0)
            if azoth > 0:
                if use_numeric:
                    advantage_list.append(f"Azoth..................... {azoth}")
                else:
                    advantage_list.append(f"{'Azoth':<15} : {azoth}")
        elif template == "geist":
            # Geist characters use Synergy instead of integrity
            synergy = advantages.get("synergy", 1)
            if use_numeric:
                advantage_list.append(f"Synergy................... {synergy}")
            else:
                advantage_list.append(f"{'Synergy':<15} : {synergy}")
        elif template == "legacy_changingbreeds":
            feral_heart = advantages.get("feral_heart", 1)
            if feral_heart > 0:
                if use_numeric:
                    advantage_list.append(f"Feral Heart............... {feral_heart}")
                else:
                    advantage_list.append(f"{'Feral Heart':<15} : {feral_heart}")
        
        # Create section headers using the same format as other sections
        merits_header = f"|g<{'-' * 12} MERITS {'-' * 13}>|n"
        advantages_header = f"|g<{'-' * 10} ADVANTAGES {'-' * 11}>|n"
        output.append(f"{merits_header.ljust(42)} {advantages_header}")
        
        # Display merits and advantages side by side
        max_rows = max(len(merit_list) if merit_list else 1, len(advantage_list))
        for i in range(max_rows):
            left_item = merit_list[i] if i < len(merit_list) else ""
            right_item = advantage_list[i] if i < len(advantage_list) else ""
            
            # Handle empty merits case
            if not merit_list and i == 0:
                left_item = "No merits yet."
            
            left_formatted = left_item.ljust(38)
            output.append(f"{left_formatted}{right_item}")
        
        # Add note if werewolf is shifted
        if template.lower() == "werewolf":
            current_form = getattr(target.db, 'current_form', 'hishu')
            if current_form != 'hishu':
                output.append(" " * 42 + " |y▸ Modified by form|n")
        
        # Changing Breeds: Favors and Aspects sections side by side
        if template == "legacy_changingbreeds":
            favors = target.db.stats.get("favors", {})
            aspects = target.db.stats.get("aspects", {})
            
            # Create favors list
            favor_list = []
            if favors:
                for favor_name, favor_data in sorted(favors.items()):
                    if isinstance(favor_data, dict):
                        dots = favor_data.get("dots", 0)
                        if dots > 0:
                            dots_display = self._format_dots(dots, favor_data.get("max_dots", 5), force_ascii)
                            favor_name_display = favor_name.replace('_', ' ').title()
                            # Use dot padding in numeric mode for better readability
                            if use_numeric:
                                padding = '.' * (37 - len(favor_name_display))
                                favor_display = f"{favor_name_display}{padding}{dots_display}"
                            else:
                                favor_display = f"{favor_name_display:<37} {dots_display}"
                        else:
                            favor_display = f"{favor_name.replace('_', ' ').title()}"
                    else:
                        favor_display = f"{favor_name.replace('_', ' ').title()}"
                    favor_list.append(favor_display)
            
            # Create aspects list
            aspect_list = []
            if aspects:
                for aspect_name, aspect_data in sorted(aspects.items()):
                    if isinstance(aspect_data, dict):
                        dots = aspect_data.get("dots", 0)
                        if dots > 0:
                            dots_display = self._format_dots(dots, aspect_data.get("max_dots", 5), force_ascii)
                            aspect_name_display = aspect_name.replace('_', ' ').title()
                            # Use dot padding in numeric mode for better readability
                            if use_numeric:
                                padding = '.' * (37 - len(aspect_name_display))
                                aspect_display = f"{aspect_name_display}{padding}{dots_display}"
                            else:
                                aspect_display = f"{aspect_name_display:<37} {dots_display}"
                        else:
                            aspect_display = f"{aspect_name.replace('_', ' ').title()}"
                    else:
                        aspect_display = f"{aspect_name.replace('_', ' ').title()}"
                    aspect_list.append(aspect_display)
            
            # Create section headers
            favors_header = f"|g<{'-' * 12} FAVORS {'-' * 13}>|n"
            aspects_header = f"|g<{'-' * 10} ASPECTS {'-' * 11}>|n"
            output.append(f"{favors_header.ljust(42)} {aspects_header}")
            
            # Display favors and aspects side by side
            max_rows = max(len(favor_list) if favor_list else 1, len(aspect_list) if aspect_list else 1)
            for i in range(max_rows):
                left_item = favor_list[i] if i < len(favor_list) else ""
                right_item = aspect_list[i] if i < len(aspect_list) else ""
                
                # Handle empty lists
                if not favor_list and i == 0:
                    left_item = "No favors yet."
                if not aspect_list and i == 0:
                    right_item = "No aspects yet."
                
                left_formatted = left_item.ljust(38)
                output.append(f"{left_formatted}{right_item}")
        
        # Primary Powers (disciplines, arcana, gifts)
        powers = target.db.stats.get("powers", {})
        template_powers = self._get_template_powers(template)
        template_secondary_powers = self._get_template_secondary_powers(template)
        
        # Determine section names based on template
        primary_section_names = {
            'vampire': 'DISCIPLINES',
            'legacy_vampire': 'DISCIPLINES',
            'mage': 'ARCANA',
            'legacy_mage': 'ARCANA',
            'werewolf': 'GIFTS',
            'legacy_werewolf': 'GIFTS',
            'changeling': 'CONTRACTS',
            'legacy_changeling': 'CONTRACTS',
            'geist': 'KEYS',
            'legacy_geist': 'KEYS',
            'promethean': 'TRANSMUTATIONS',
            'legacy_promethean': 'TRANSMUTATIONS',
            'demon': 'EMBEDS',
            'hunter': 'ENDOWMENTS',
            'legacy_hunter': 'TACTICS',
            'deviant': 'VARIATIONS'
        }
        secondary_section_names = {
            'vampire': 'BLOOD SORCERY & COILS',
            'werewolf': 'RITES',
            'geist': 'CEREMONIES',
            'promethean': 'BESTOWMENTS',
            'demon': 'EXPLOITS',
            'hunter': 'TACTICS',
            'deviant': 'RITUALS'
        }
        
        primary_section = primary_section_names.get(template.lower(), 'POWERS')
        secondary_section = secondary_section_names.get(template.lower(), 'RITUALS')
        
        # Special handling for Geist characters (Keys, Haunts, Ceremonies)
        if template.lower() == "geist":
            # Keys section (from geist_stats)
            output.append(self._format_section_header("|wKEYS|n"))
            
            if hasattr(target.db, 'geist_stats') and target.db.geist_stats:
                geist_keys = target.db.geist_stats.get("keys", {})
                key_list = []
                for key_name, has_key in geist_keys.items():
                    if has_key:
                        key_list.append(key_name.replace("_", " ").title())
                
                if key_list:
                    # Display keys in 2 columns
                    for i in range(0, len(key_list), 2):
                        left_key = key_list[i] if i < len(key_list) else ""
                        right_key = key_list[i + 1] if i + 1 < len(key_list) else ""
                        
                        left_formatted = left_key.ljust(42)
                        output.append(f"{left_formatted} {right_key}")
                else:
                    output.append("No keys unlocked yet.")
            else:
                output.append("No keys unlocked yet.")
            
            output.append("")
            output.append("|gSee +sheet/geist for detailed key information and geist character sheet.|n")
            
            # Haunts section (category powers stored in regular powers)
            output.append(self._format_section_header("|wHAUNTS|n"))
            
            # Get haunts from regular powers or geist_stats
            haunts_from_powers = {}
            haunts_from_geist = {}
            
            # Check regular powers for haunts
            haunt_names = ["boneyard", "caul", "curse", "dirge", "marionette", "memoria", "oracle", "rage", "shroud", "tomb"]
            for haunt_name in haunt_names:
                if haunt_name in powers and powers[haunt_name] > 0:
                    haunts_from_powers[haunt_name] = powers[haunt_name]
            
            # Check geist_stats for haunts  
            if hasattr(target.db, 'geist_stats') and target.db.geist_stats:
                geist_haunts = target.db.geist_stats.get("haunts", {})
                for haunt_name, rating in geist_haunts.items():
                    if rating > 0:
                        haunts_from_geist[haunt_name] = rating
            
            # Combine and display haunts
            all_haunts = {**haunts_from_powers, **haunts_from_geist}
            if all_haunts:
                haunt_list = []
                for haunt_name, haunt_rating in all_haunts.items():
                    dots = self._format_dots(haunt_rating, 5, force_ascii)
                    haunt_name_display = haunt_name.replace('_', ' ').title()
                    # Use dot padding in numeric mode for better readability
                    if use_numeric:
                        padding = '.' * (37 - len(haunt_name_display))
                        haunt_display = f"{haunt_name_display}{padding}{dots}"
                    else:
                        haunt_display = f"{haunt_name_display:<37} {dots}"
                    haunt_list.append(haunt_display)
                
                # Display haunts in 2 columns like merits
                for i in range(0, len(haunt_list), 2):
                    left_haunt = haunt_list[i] if i < len(haunt_list) else ""
                    right_haunt = haunt_list[i + 1] if i + 1 < len(haunt_list) else ""
                    
                    # Format with proper spacing (39 chars for left column)
                    left_formatted = left_haunt.ljust(42)
                    output.append(f"{left_formatted} {right_haunt}")
            else:
                output.append("No haunts learned yet.")
            
            # Ceremonies section (individual abilities stored in regular powers)
            output.append(self._format_section_header("|wCEREMONIES|n"))
            
            ceremony_names = [
                "dead_mans_camera", "death_watch", "diviners_jawbone", "lovers_telephone", "ishtars_perfume",
                "crow_girl_kiss", "gifts_of_persephone", "ghost_trap", "skeleton_key", "bestow_regalia", 
                "krewe_binding", "speaker_for_the_dead", "black_cats_crossing", "bloody_codex", "dumb_supper",
                "forge_anchor", "maggot_homonculus", "pass_on", "ghost_binding", "persephones_return"
            ]
            
            ceremony_list = []
            for ceremony_name in ceremony_names:
                if ceremony_name in powers and powers[ceremony_name] > 0:
                    ceremony_display = ceremony_name.replace('_', ' ').title()
                    ceremony_list.append(ceremony_display)
            
            if ceremony_list:
                # Display ceremonies in 2 columns
                for i in range(0, len(ceremony_list), 2):
                    left_ceremony = ceremony_list[i] if i < len(ceremony_list) else ""
                    right_ceremony = ceremony_list[i + 1] if i + 1 < len(ceremony_list) else ""
                    
                    left_formatted = left_ceremony.ljust(42)
                    output.append(f"{left_formatted} {right_ceremony}")
            else:
                output.append("No ceremonies learned yet.")
        
        else:
            # Regular template power display (skip for hunter since endowments are handled separately)
            # Also skip powers section for certain Mortal+ types that use merits instead
            # Skip Werewolf primary powers (GIFTS) since they only have individual facets, not rated gifts
            skip_powers = False
            if template.lower() == "mortal_plus" or template.lower() == "mortal plus":
                template_type = bio.get("template_type", "").lower()
                no_power_types = ["psychic", "lost boy", "dreamer", "atariya", "infected", "psychic vampire"]
                if template_type in no_power_types:
                    skip_powers = True
            elif template.lower() == "werewolf":
                skip_powers = True  # Werewolves don't have rated gifts, only individual facets
            
            if template.lower() != "hunter" and not skip_powers:
                if powers or template_powers:
                    output.append(self._format_section_header(f"|w{primary_section}|n"))
                    
                    if template_powers:
                        power_display = self._format_powers_display(powers, template_powers, force_ascii, use_numeric, template)
                        output.extend(power_display)
                    else:
                        output.append("No primary powers available for this template.")
        
        # Secondary Powers (rituals, rites, blood sorcery) - skip for Geist, Hunter, Werewolf, and Vampire since handled separately
        # Also check if section would be empty before displaying
        if template.lower() not in ["geist", "hunter", "werewolf", "vampire"] and (powers or template_secondary_powers):
            if template_secondary_powers:  # Only show section if template has secondary powers
                # Check if there are any secondary powers actually learned
                has_secondary_powers = False
                for power_name in template_secondary_powers:
                    power_value = powers.get(power_name, 0)
                    if power_value == "known" or (isinstance(power_value, int) and power_value > 0):
                        has_secondary_powers = True
                        break
                
                if has_secondary_powers:
                    output.append(self._format_section_header(f"|w{secondary_section}|n"))
                    secondary_power_display = self._format_secondary_powers_display(powers, template_secondary_powers, force_ascii, use_numeric)
                    output.extend(secondary_power_display)
                
                # Add hint for demon characters
                if template.lower() == "demon":
                    output.append("")
                    output.append("|gSee +sheet/demon for detailed demonic form traits (Modifications, Technologies, Propulsion, Process).|n")
        
        # Mage Spells section (individual spells without ratings)
        if template.lower() in ["mage", "legacy_mage"]:
            output.append(self._format_section_header("|wSPELLS|n"))
            
            # Get all spell powers
            from world.cofd.powers.mage_spells import ALL_MAGE_SPELLS, get_spell
            
            spell_list = []
            for power_name, value in powers.items():
                if power_name.startswith("spell:") and value == "known":
                    # Extract spell key from "spell:spell_name"
                    spell_key = power_name[6:]  # Remove "spell:" prefix
                    
                    # Look up spell data
                    spell_data = get_spell(spell_key)
                    if spell_data:
                        # Format arcana dots (e.g., "●●●●●" for level 5)
                        spell_level = spell_data['level']
                        arcana_dots = self._format_dots(spell_level, 5, force_ascii)
                        arcana_name = spell_data['arcana'].title()
                        
                        spell_display = f"{spell_data['name']} ({arcana_name} {arcana_dots})"
                        spell_list.append(spell_display)
                    else:
                        # Spell not found in database, show as unknown
                        spell_display = f"{spell_key.replace('_', ' ').title()} (Unknown Spell)"
                        spell_list.append(spell_display)
            
            if spell_list:
                # Display spells in single column for readability
                for spell in sorted(spell_list):
                    output.append(f"  {spell}")
            else:
                output.append("No spells learned yet.")
            
            output.append("")
            output.append("|gSee +sheet/mage for Nimbus, Obsessions, Praxes, and Dedicated Tool.|n")
        
        # Hunter Endowments section (individual powers without ratings)
        if template.lower() == "hunter":
            output.append(self._format_section_header("|wENDOWMENTS|n"))
            
            # Get all endowment powers
            from world.cofd.powers.hunter_endowments import get_endowment
            
            endowment_list = []
            for power_name, value in powers.items():
                if power_name.startswith("endowment:") and value == "known":
                    # Extract endowment key from "endowment:endowment_name"
                    endowment_key = power_name[10:]  # Remove "endowment:" prefix
                    
                    # Look up endowment data
                    power_data = get_endowment(endowment_key)
                    if power_data:
                        endowment_type = power_data['endowment_type'].replace('_', ' ').title()
                        # Truncate name if too long for 2-column display (max 35 chars with type info)
                        endowment_name = power_data['name']
                        endowment_display = f"{endowment_name} ({endowment_type})"
                        endowment_list.append(endowment_display)
                    else:
                        # Endowment not found in database, show as unknown
                        endowment_display = f"{endowment_key.title()} (Unknown Endowment)"
                        endowment_list.append(endowment_display)
            
            if endowment_list:
                # Display endowments in 2 columns for space efficiency
                sorted_endowments = sorted(endowment_list)
                for i in range(0, len(sorted_endowments), 2):
                    left_endowment = sorted_endowments[i] if i < len(sorted_endowments) else ""
                    right_endowment = sorted_endowments[i + 1] if i + 1 < len(sorted_endowments) else ""
                    
                    # Truncate if needed (39 chars for left column)
                    if len(left_endowment) > 37:
                        left_endowment = left_endowment[:34] + "..."
                    if len(right_endowment) > 37:
                        right_endowment = right_endowment[:34] + "..."
                    
                    left_formatted = left_endowment.ljust(42)
                    output.append(f"  {left_formatted} {right_endowment}")
            else:
                output.append("No endowment powers learned yet.")
            
            output.append("")
            
            # Tactics section
            output.append(self._format_section_header("|wTACTICS|n"))
            
            from world.cofd.powers.hunter_tactics import get_all_tactics
            
            all_tactics = get_all_tactics()
            tactic_list = []
            
            # Check for tactics stored directly (without prefix) or with "tactic:" prefix
            for power_name, value in powers.items():
                tactic_key = None
                if power_name.startswith("tactic:"):
                    tactic_key = power_name[7:]  # Remove "tactic:" prefix
                elif power_name in all_tactics:
                    tactic_key = power_name
                
                if tactic_key and (value == "known" or (isinstance(value, int) and value > 0)):
                    tactic_data = all_tactics.get(tactic_key)
                    if tactic_data:
                        tactic_type = tactic_data.get('category', 'Unknown').replace('_', ' ').title()
                        tactic_name = tactic_data.get('name', tactic_key.replace('_', ' ').title())
                        tactic_display = f"{tactic_name} ({tactic_type})"
                        tactic_list.append(tactic_display)
                    else:
                        tactic_display = f"{tactic_key.replace('_', ' ').title()} (Unknown Tactic)"
                        tactic_list.append(tactic_display)
            
            if tactic_list:
                # Display tactics in 2 columns
                sorted_tactics = sorted(tactic_list)
                for i in range(0, len(sorted_tactics), 2):
                    left_tactic = sorted_tactics[i] if i < len(sorted_tactics) else ""
                    right_tactic = sorted_tactics[i + 1] if i + 1 < len(sorted_tactics) else ""
                    
                    left_formatted = left_tactic.ljust(42)
                    output.append(f"  {left_formatted} {right_tactic}")
            else:
                output.append("No tactics learned yet.")
            
            output.append("")
        
        # Werewolf Gifts section (individual gifts without ratings)
        if template.lower() == "werewolf":
            output.append(self._format_section_header("|wGIFTS (FACETS)|n"))
            
            from world.cofd.powers.werewolf_gifts import get_gift
            
            gift_list = []
            for power_name, value in powers.items():
                if power_name.startswith("gift:") and value == "known":
                    # Extract gift key from "gift:gift_name"
                    gift_key = power_name[5:]  # Remove "gift:" prefix
                    
                    # Look up gift data
                    gift_data = get_gift(gift_key)
                    if gift_data:
                        renown = gift_data['renown'].title()
                        rank_dots = self._format_dots(gift_data['rank'], 5, force_ascii)
                        
                        gift_display = f"{gift_data['name']} ({renown} {rank_dots})"
                        gift_list.append(gift_display)
                    else:
                        # Gift not found, show as unknown
                        gift_display = f"{gift_key.replace('_', ' ').title()} (Unknown Gift)"
                        gift_list.append(gift_display)
            
            if gift_list:
                # Display gifts in single column for readability
                for gift in sorted(gift_list):
                    output.append(f"  {gift}")
            else:
                output.append("No gifts learned yet.")
            
            output.append("")
        
        # Vampire Discipline Powers/Devotions/Ritual sections
        if template.lower() == "vampire":
            from world.cofd.powers.vampire_disciplines import get_discipline_power, ALL_DEVOTIONS
            from world.cofd.powers.vampire_rituals import get_ritual_power
            
            # Collect all vampire semantic powers by category
            vamp_powers = {}
            
            for power_name, value in powers.items():
                if value == "known":
                    if power_name.startswith("discipline_power:"):
                        key = power_name[17:]
                        data = get_discipline_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Discipline Powers" not in vamp_powers:
                            vamp_powers["Discipline Powers"] = []
                        vamp_powers["Discipline Powers"].append(name)
                    elif power_name.startswith("devotion:"):
                        key = power_name[9:]
                        data = ALL_DEVOTIONS.get(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Devotions" not in vamp_powers:
                            vamp_powers["Devotions"] = []
                        vamp_powers["Devotions"].append(name)
                    elif power_name.startswith("coil:"):
                        key = power_name[5:]
                        data = get_discipline_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Coils of the Dragon" not in vamp_powers:
                            vamp_powers["Coils of the Dragon"] = []
                        vamp_powers["Coils of the Dragon"].append(name)
                    elif power_name.startswith("scale:"):
                        key = power_name[6:]
                        data = get_ritual_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Scales of the Dragon" not in vamp_powers:
                            vamp_powers["Scales of the Dragon"] = []
                        vamp_powers["Scales of the Dragon"].append(name)
                    elif power_name.startswith("theban:"):
                        key = power_name[7:]
                        data = get_ritual_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Theban Sorcery" not in vamp_powers:
                            vamp_powers["Theban Sorcery"] = []
                        vamp_powers["Theban Sorcery"].append(name)
                    elif power_name.startswith("cruac:"):
                        key = power_name[6:]
                        data = get_ritual_power(key)
                        name = data['name'] if data else key.replace('_', ' ').title()
                        if "Cruac" not in vamp_powers:
                            vamp_powers["Cruac"] = []
                        vamp_powers["Cruac"].append(name)
            
            # Display each category that has powers in multicolumn format (3 columns, 80 chars)
            for category in ["Discipline Powers", "Devotions", "Coils of the Dragon", 
                           "Scales of the Dragon", "Theban Sorcery", "Cruac"]:
                if category in vamp_powers and vamp_powers[category]:
                    output.append(self._format_section_header(f"|w{category.upper()}|n"))
                    sorted_powers = sorted(vamp_powers[category])
                    # Display in 3 columns (max 26 chars per column to fit in 80 chars)
                    for i in range(0, len(sorted_powers), 3):
                        col1 = sorted_powers[i] if i < len(sorted_powers) else ""
                        col2 = sorted_powers[i + 1] if i + 1 < len(sorted_powers) else ""
                        col3 = sorted_powers[i + 2] if i + 2 < len(sorted_powers) else ""
                        
                        # Format each column (26 chars max, truncate if needed)
                        col1_formatted = col1[:26].ljust(26) if col1 else ""
                        col2_formatted = col2[:26].ljust(26) if col2 else ""
                        col3_formatted = col3[:26] if col3 else ""
                        
                        output.append(f"  {col1_formatted} {col2_formatted} {col3_formatted}")
                    output.append("")
        
        # Mummy Affinity and Utterance sections
        if template.lower() == "mummy":
            from world.cofd.powers.mummy_powers import MUMMY_AFFINITIES, MUMMY_UTTERANCES
            
            # Collect all mummy powers by category
            mummy_powers = {
                "Affinities": [],
                "Utterances": []
            }
            
            for power_name, value in powers.items():
                if value == "known" or (isinstance(value, int) and value > 0):
                    # Check for affinities
                    affinity_data = MUMMY_AFFINITIES.get(power_name)
                    if affinity_data:
                        name = affinity_data['name']
                        pillar = affinity_data.get('pillar', '')
                        if pillar:
                            mummy_powers["Affinities"].append(f"{name} ({pillar})")
                        else:
                            mummy_powers["Affinities"].append(name)
                    
                    # Check for utterances
                    utterance_data = MUMMY_UTTERANCES.get(power_name)
                    if utterance_data:
                        name = utterance_data['name']
                        tier = utterance_data.get('tier', '')
                        if tier:
                            mummy_powers["Utterances"].append(f"{name} [{tier}]")
                        else:
                            mummy_powers["Utterances"].append(name)
            
            # Display Affinities
            if mummy_powers["Affinities"]:
                output.append(self._format_section_header("|wAFFINITIES|n"))
                for power in sorted(mummy_powers["Affinities"]):
                    output.append(f"  {power}")
                output.append("")
            
            # Display Utterances
            if mummy_powers["Utterances"]:
                output.append(self._format_section_header("|wUTTERANCES|n"))
                # Group utterances by base name (remove tier info for sorting)
                utterance_dict = {}
                for power in mummy_powers["Utterances"]:
                    base_name = power.split('[')[0].strip()
                    if base_name not in utterance_dict:
                        utterance_dict[base_name] = []
                    utterance_dict[base_name].append(power)
                
                for base_name in sorted(utterance_dict.keys()):
                    for power in utterance_dict[base_name]:
                        output.append(f"  {power}")
                output.append("")
        
        # Mortal+ specific sections (Demon-Blooded, Wolf-Blooded, Sleepwalkers/Proximus)
        if template.lower() in ["mortal_plus", "mortal plus"]:
            template_type = bio.get("template_type", "").lower()
            
            # Demon-Blooded Level
            if "demon" in template_type or template_type == "demon-blooded":
                demon_level = bio.get("demon_blooded_level", bio.get("subtype", "<not set>"))
                if demon_level and demon_level != "<not set>":
                    output.append(self._format_section_header("|wDEMON-BLOODED|n"))
                    output.append(f"  Level: {demon_level.replace('_', ' ').title()}")
                    
                    # Display any embed powers they have
                    embed_list = []
                    for power_name, rating in powers.items():
                        if rating > 0 and "_embed" in power_name:
                            embed_display = power_name.replace("_embed", "").replace("_", " ").title()
                            embed_list.append(embed_display)
                    
                    if embed_list:
                        output.append(f"  Embeds: {', '.join(sorted(embed_list))}")
            
            # Wolf-Blooded Tells
            elif "wolf" in template_type or template_type == "wolf-blooded":
                tells = bio.get("wolf_blooded_tells", [])
                if not tells:
                    # Check if stored as single tell in subtype
                    subtype = bio.get("subtype", "")
                    if subtype and subtype != "<not set>":
                        tells = [subtype]
                
                output.append(self._format_section_header("|wWOLF-BLOODED TELLS|n"))
                
                if tells:
                    tell_list = []
                    if isinstance(tells, str):
                        tells = [tells]
                    for tell in tells:
                        tell_display = tell.replace("_", " ").title()
                        tell_list.append(tell_display)
                    
                    # Display tells in 2 columns
                    for i in range(0, len(tell_list), 2):
                        left_tell = tell_list[i] if i < len(tell_list) else ""
                        right_tell = tell_list[i + 1] if i + 1 < len(tell_list) else ""
                        
                        left_formatted = left_tell.ljust(42)
                        output.append(f"  {left_formatted} {right_tell}")
                else:
                    output.append("  No tells manifested yet.")
            
            # Sleepwalker/Proximus Spells
            elif template_type in ["sleepwalker", "proximus"]:
                output.append(self._format_section_header("|wSPELLS|n"))
                
                # Import spell data
                from world.cofd.powers.mage_spells import ALL_MAGE_SPELLS, get_spell
                
                # Get spell powers
                spell_list = []
                for power_name, value in powers.items():
                    # Check if it's a spell: notation power
                    if power_name.startswith("spell:") and value == "known":
                        # Extract spell key from "spell:spell_name"
                        spell_key = power_name[6:]  # Remove "spell:" prefix
                        
                        # Look up spell data
                        spell_data = get_spell(spell_key)
                        if spell_data:
                            # Format arcana dots (e.g., "●●●●●" for level 5)
                            spell_level = spell_data['level']
                            arcana_dots = self._format_dots(spell_level, 5, force_ascii)
                            arcana_name = spell_data['arcana'].title()
                            
                            spell_display = f"{spell_data['name']} ({arcana_name} {arcana_dots})"
                            spell_list.append(spell_display)
                        else:
                            # Spell not found in database, show as unknown
                            spell_display = f"{spell_key.replace('_', ' ').title()} (Unknown Spell)"
                            spell_list.append(spell_display)
                
                if spell_list:
                    # Display spells in single column for readability
                    for spell in sorted(spell_list):
                        output.append(f"  {spell}")
                else:
                    output.append("No spells learned yet.")
                    if template_type == "proximus":
                        output.append("|g(Proximus have access to limited mage spells)|n")
                    else:
                        output.append("|g(Sleepwalkers can learn spells from mages)|n")
            
            # Psychic Powers
            elif template_type == "psychic":
                psychic_powers = []
                from world.cofd.templates.mortal_plus import PSYCHIC_POWERS
                
                for power_name in PSYCHIC_POWERS:
                    power_key = power_name.replace(" ", "_").lower()
                    if power_key in powers and powers[power_key] > 0:
                        dots = self._format_dots(powers[power_key], 5, force_ascii)
                        power_display = f"{power_name.replace('_', ' ').title():<20} {dots}"
                        psychic_powers.append(power_display)
                
                if psychic_powers:
                    output.append(self._format_section_header("|wPSYCHIC POWERS|n"))
                    
                    # Display psychic powers in 2 columns
                    for i in range(0, len(psychic_powers), 2):
                        left_power = psychic_powers[i] if i < len(psychic_powers) else ""
                        right_power = psychic_powers[i + 1] if i + 1 < len(psychic_powers) else ""
                        
                        left_formatted = left_power.ljust(42)
                        output.append(f"{left_formatted} {right_power}")
        
        # Pools section (horizontal layout)
        output.append(self._format_section_header("|wPOOLS|n"))
        
        # Get pools data
        health_max = advantages.get("health", 7)
        health_track = self._get_health_track(target)
        
        # Save the compacted track back to ensure consistency
        self._set_health_track(target, health_track)
        
        # Calculate health statistics
        current_health, bashing_count, lethal_count, aggravated_count = self._calculate_health_stats(health_track, health_max)
        
        # Create health boxes
        health_boxes = []
        for i in range(health_max):
            damage_type = health_track[i]
            if damage_type == "bashing":
                health_boxes.append("[|c/|n]")  # Cyan for bashing
            elif damage_type == "lethal":
                health_boxes.append("[|rX|n]")  # Red for lethal
            elif damage_type == "aggravated":
                health_boxes.append("[|R*|n]")  # Bright red for aggravated
            else:
                health_boxes.append("[ ]")
        
        # Willpower - calculate dynamically if not in advantages
        willpower_max = advantages.get("willpower")
        if willpower_max is None:
            # Calculate from resolve + composure
            attrs = target.db.stats.get("attributes", {})
            resolve = attrs.get("resolve", 1)
            composure = attrs.get("composure", 1)
            willpower_max = resolve + composure
        willpower_current = target.db.willpower_current
        if willpower_current is None:
            willpower_current = willpower_max  # Default to full
        
        willpower_dots = self._format_dots(willpower_current, willpower_max, force_ascii, show_max=True)
        
        # Template-specific resource pools
        resource_pools = {
            "geist": ("Plasm", "plasm"),
            "changeling": ("Glamour", "glamour"), 
            "vampire": ("Vitae", "vitae"),
            "werewolf": ("Essence", "essence"),
            "mage": ("Mana", "mana"),
            "demon": ("Aether", "aether"),
            "promethean": ("Pyros", "pyros")
        }
        
        pool_display = ""
        if template in resource_pools:
            pool_name, pool_key = resource_pools[template]
            pool_current = getattr(target.db, f"{pool_key}_current", None)
            pool_max = advantages.get(pool_key, 10)  # Default max of 10 for most pools
            
            if pool_current is None:
                pool_current = pool_max  # Default to full
            
            pool_dots = self._format_dots(pool_current, pool_max, force_ascii, show_max=True)
            # In numeric mode, don't duplicate the max in label (it's shown below)
            if use_numeric:
                pool_display = pool_name
            else:
                pool_display = f"{pool_name} ({pool_current}/{pool_max})"
        
        # Create horizontal pools layout with health numeric display
        # Build health label with current/max and damage breakdown (always shown for health)
        health_label = f"Health ({current_health}/{health_max}"
        if bashing_count > 0 or lethal_count > 0 or aggravated_count > 0:
            damage_parts = []
            if bashing_count > 0:
                damage_parts.append(f"{bashing_count}B")
            if lethal_count > 0:
                damage_parts.append(f"{lethal_count}L")
            if aggravated_count > 0:
                damage_parts.append(f"{aggravated_count}A")
            health_label += f" - {' '.join(damage_parts)}"
        health_label += ")"
        
        # In numeric mode, don't duplicate the max in label (it's shown below)
        if use_numeric:
            willpower_label = "Willpower"
        else:
            willpower_label = f"Willpower ({willpower_current}/{willpower_max})"
        
        if use_numeric:
            # Numeric mode: Horizontal layout with numeric values
            # Health on left with boxes, pools on right
            if pool_display:
                # Three items: Health, Resource Pool, Willpower on same line
                pool_text = f"{pool_name}: {pool_current}/{pool_max}"
                output.append(f"{health_label:<28}{pool_text:<32}Willpower: {willpower_current}/{willpower_max}")
                output.append(f"{''.join(health_boxes)}")
            else:
                # Two items: Health, Willpower
                output.append(f"{health_label:<40}Willpower: {willpower_current}/{willpower_max}")
                output.append(f"{''.join(health_boxes):<40}")
        else:
            # Unicode mode: Side-by-side layout
            if pool_display:
                # Three pools: Health, Resource Pool, Willpower
                output.append(f"{health_label:^26}{pool_display:^26}{willpower_label:^26}")
                health_section = f"{''.join(health_boxes):^26}"
                pool_section = f"{pool_dots if 'pool_dots' in locals() else '':^26}"
                willpower_section = f"{willpower_dots:^26}"
                output.append(f"{health_section}{pool_section}{willpower_section}")
            else:
                # Two pools: Health, Willpower
                output.append(f"{health_label:^39}{willpower_label:^39}")
                health_section = f"{''.join(health_boxes):^39}"
                willpower_section = f"{willpower_dots:^39}"
                output.append(f"{health_section}{willpower_section}")

        # Aspirations (only show if there are any and not in legacy mode)
        if not legacy_mode:
            aspirations_list = [asp for asp in target.db.aspirations if asp] if target.db.aspirations else []
            if aspirations_list:
                output.append(self._format_section_header("|wASPIRATIONS|n"))
                for i, asp in enumerate(aspirations_list, 1):
                    # Handle both old format (strings) and new format (dicts)
                    try:
                        if "type" in asp and "description" in asp:
                            # New format dict (works with _SaverDict too)
                            asp_type = asp.get('type', 'short-term')
                            description = asp.get('description', str(asp))
                            type_label = "|c[ST]|n" if asp_type == 'short-term' else "|y[LT]|n"
                            output.append(f"{i}. {type_label} {description}")
                        else:
                            # Old format or string
                            output.append(f"{i}. {asp}")
                    except (TypeError, AttributeError):
                        # Fallback for any unexpected format
                        output.append(f"{i}. {asp}")
        
        # Legacy Experience (only show in legacy mode)
        if legacy_mode:
            output.append(self._format_section_header("|wEXPERIENCE|n"))
            legacy_xp = target.attributes.get('legacy_experience', default=0)
            output.append(f"Experience Points: |y{legacy_xp}|n")
        
        output.append(f"|y{'='*78}|n")
        
        return output 