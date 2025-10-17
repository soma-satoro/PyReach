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
        +sheet/ascii [character] - Force ASCII display (no Unicode dots)
        +sheet/geist [character] - Display geist character sheet (Sin-Eater only)
        +sheet/geist/ascii [character] - Display geist sheet in ASCII mode
        +sheet/mage [character] - Display mage-specific sheet (Mage only)
        +sheet/mage/ascii [character] - Display mage sheet in ASCII mode
        +sheet/demon [character] - Display demonic form sheet (Demon only)
        +sheet/demon/ascii [character] - Display demon form sheet in ASCII mode
        +sheet/deviant [character] - Display deviant powers sheet (Deviant only)
        +sheet/deviant/ascii [character] - Display deviant sheet in ASCII mode
        +sheet/show - Show your sheet to everyone in the room
        +sheet/show [player] - Show your sheet to a specific player
        +sheet/show/geist [player] - Show your geist sheet to the room or a player
        +sheet/show/mage [player] - Show your mage sheet to the room or a player
        +sheet/show/demon [player] - Show your demon form sheet to the room or a player
        +sheet/show/deviant [player] - Show your deviant sheet to the room or a player
        +sheet/show/ascii [player] - Show your sheet in ASCII mode
        
    Shows all character statistics in an organized format.
    The /geist switch displays the secondary character sheet for a Sin-Eater's bound geist.
    The /mage switch displays mage-specific details like Nimbus, Obsessions, Praxes, and Dedicated Tool.
    The /demon switch displays the demonic form sheet showing Modifications, Technologies, Propulsion, and Process.
    The /deviant switch displays the Deviant powers sheet showing Variations and Scars with their entanglements.
    The /show switch allows you to share your character sheet with others in the room or privately.
    """
    
    key = "+sheet"
    aliases = ["sheet"]
    help_category = "Character Sheets and Development"
    
    def _get_dots_style(self, force_ascii=False):
        """
        Determine whether to use Unicode or ASCII dots based on client support.
        
        Args:
            force_ascii (bool): Force ASCII display regardless of client support
            
        Returns:
            tuple: (filled_char, empty_char, supports_utf8)
        """
        # Check if user explicitly wants ASCII
        if force_ascii or "ascii" in self.switches:
            return ("*", "-", False)
        
        # Check session UTF-8 support
        if self.session:
            # Check if the client explicitly supports UTF-8:
            utf8_support = self.session.protocol_flags.get("UTF-8", None)
            encoding = self.session.protocol_flags.get("ENCODING", "utf-8").lower()
            
            # If the client explicitly doesn't support UTF-8 or uses non-UTF-8 encoding:
            if utf8_support is False or encoding not in ["utf-8", "utf8"]:
                return ("*", "-", False)
        
        # Unicode is default if there's not a specific error, the client is unknown, or the player doesn't specify ascii
        return ("●", "○", True)
    
    def _format_dots(self, value, max_value=5, force_ascii=False):
        """
        Format a stat value as dots (Unicode or ASCII).
        
        Args:
            value (int): Current stat value
            max_value (int): Maximum possible value
            force_ascii (bool): Force ASCII display
            
        Returns:
            str: Formatted dot display
        """
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        
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
    
    def _show_encoding_warning(self, supports_utf8):
        """
        Show encoding warning if not using UTF-8.
        
        Args:
            supports_utf8 (bool): Whether UTF-8 is supported
        """
        if not supports_utf8:
            warning = [
                "",
                "|y" + "="*78 + "|n",
                "|rNOTE: Your client doesn't support UTF-8 encoding.|n",
                "|w- Set your MUD client to use UTF-8 encoding|n",
                "|w- Or use: option encoding=utf-8  (if you're not logged in)|n",
                "|w- Or use: +sheet/ascii for ASCII display|n",
                "|y" + "="*78 + "|n",
                ""
            ]
            self.caller.msg("\n".join(warning))

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
    
    def _format_powers_display(self, powers, template_powers, force_ascii):
        """Format the powers section for display."""
        if not template_powers:
            return ["No powers available for this template."]
        
        power_lines = []
        
        # Group powers by category if applicable
        displayed_powers = []
        for power_name in template_powers:
            power_value = powers.get(power_name, 0)
            # Handle both numeric (1-5) and semantic ("known") power values
            if power_value == "known" or (isinstance(power_value, int) and power_value > 0):
                # For semantic powers (embeds, exploits, etc.), just show the name
                if power_value == "known":
                    dots = ""  # No dots for known/unknown powers
                else:
                    dots = self._format_dots(power_value, 5, force_ascii)
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
                elif power_name.startswith('rite_'):
                    display_name = power_name[5:]   # Remove 'rite_'
                elif power_name.startswith('embed:'):
                    display_name = power_name[6:]   # Remove 'embed:'
                elif power_name.startswith('exploit:'):
                    display_name = power_name[8:]   # Remove 'exploit:'
                
                # Format display with or without dots
                if dots:
                    power_display = f"{display_name.replace('_', ' ').title():<20} {dots}"
                else:
                    power_display = f"{display_name.replace('_', ' ').title()}"
                displayed_powers.append(power_display)
        
        if not displayed_powers:
            return ["No powers learned yet."]
        
        # Display powers in 2 columns like merits
        for i in range(0, len(displayed_powers), 2):
            left_power = displayed_powers[i] if i < len(displayed_powers) else ""
            right_power = displayed_powers[i + 1] if i + 1 < len(displayed_powers) else ""
            
            # Format with proper spacing (39 chars for left column)
            left_formatted = left_power.ljust(39)
            power_lines.append(f"{left_formatted} {right_power}")
        
        return power_lines
    
    def _format_secondary_powers_display(self, powers, template_secondary_powers, force_ascii):
        """Format the secondary powers (rituals/rites) section for display."""
        if not template_secondary_powers:
            return ["No secondary powers available for this template."]
        
        power_lines = []
        
        # Group secondary powers by category if applicable
        displayed_powers = []
        for power_name in template_secondary_powers:
            power_value = powers.get(power_name, 0)
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
                elif power_name.startswith('rite_'):
                    display_name = power_name[5:]   # Remove 'rite_'
                elif power_name.startswith('embed:'):
                    display_name = power_name[6:]   # Remove 'embed:'
                elif power_name.startswith('exploit:'):
                    display_name = power_name[8:]   # Remove 'exploit:'
                
                # Format display with or without dots
                if display_marker:
                    power_display = f"{display_name.replace('_', ' ').title():<20} {display_marker}"
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
            left_formatted = left_power.ljust(39)
            power_lines.append(f"{left_formatted} {right_power}")
        
        return power_lines

    def func(self):
        """Display the character sheet"""
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
        
        # Auto-migrate legacy stats if any exist (silent)
        # Note: Migration functionality has been moved to admin commands
        # self._migrate_legacy_stats(target)
        
        if not target.db.stats:
            self.caller.msg(f"{target.name} has no character sheet set up yet.")
            self.caller.msg("Use +stat <stat>=<value> to set your stats.")
            return
        
        # Get dot style and check UTF-8 support
        force_ascii = "ascii" in self.switches
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        
        # Show encoding warning if needed (only for self, not when viewing others)
        if target == self.caller and not supports_utf8 and "ascii" not in self.switches:
            self._show_encoding_warning(supports_utf8)
        
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
        
        # Add template-specific bio fields
        for field in template_fields:
            if field not in ["virtue", "vice"]:  # virtue/vice already added above if valid
                field_value = bio.get(field, "<not set>")
                # Special case for cover_identity to display as "Cover ID"
                if field == "cover_identity":
                    field_label = "Cover ID"
                else:
                    field_label = field.replace("_", " ").title()
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
                mental.append(f"{attr.title():<15} {dots}")
            
            # Physical
            physical = []
            for attr in ["strength", "dexterity", "stamina"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                physical.append(f"{attr.title():<15} {dots}")
            
            # Social
            social = []
            for attr in ["presence", "manipulation", "composure"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
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
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
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
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
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
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
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
                
                merit_display = f"{display_name:<25} {dots}"
                merit_list.append(merit_display)
        
        # Create advantages list (including integrity)
        advantage_list = [
            f"{'Defense':<15} : {advantages.get('defense', 0)}",
            f"{'Speed':<15} : {advantages.get('speed', 0)}",
            f"{'Initiative':<15} : {advantages.get('initiative', 0)}",
            f"{'Size':<15} : {other.get('size', 5)}"
        ]
        
        # Add integrity to advantages (except for Geist characters who don't use integrity)
        if template != "geist":
            integrity_name = target.get_integrity_name(template)
            advantage_list.append(f"{integrity_name:<15} : {other.get('integrity', 7)}")
        
        # Add template-specific advantages
        if template == "changeling":
            wyrd = advantages.get("wyrd", 0)
            if wyrd > 0:
                advantage_list.append(f"{'Wyrd':<15} : {wyrd}")
        elif template == "werewolf":
            primal_urge = advantages.get("primal_urge", 0)
            if primal_urge > 0:
                advantage_list.append(f"{'Primal Urge':<15} : {primal_urge}")
        elif template == "vampire":
            blood_potency = advantages.get("blood_potency", 0)
            if blood_potency > 0:
                advantage_list.append(f"{'Blood Potency':<15} : {blood_potency}")
        elif template == "mage":
            gnosis = advantages.get("gnosis", 0)
            if gnosis > 0:
                advantage_list.append(f"{'Gnosis':<15} : {gnosis}")
        #elif template == "beast":
        #    satiety = advantages.get("satiety", 0)
        #    if satiety > 0:
        #        advantage_list.append(f"{'Satiety':<15} : {satiety}")
        elif template == "deviant":
            deviation = advantages.get("deviation", 0)
            if deviation > 0:
                advantage_list.append(f"{'Deviation':<15} : {deviation}")
        elif template == "demon":
            primum = advantages.get("primum", 0)
            if primum > 0:
                advantage_list.append(f"{'Primum':<15} : {primum}")
        elif template == "promethean":
            azoth = advantages.get("azoth", 0)
            if azoth > 0:
                advantage_list.append(f"{'Azoth':<15} : {azoth}")
        elif template == "geist":
            # Geist characters use Synergy instead of integrity
            synergy = advantages.get("synergy", 1)
            advantage_list.append(f"{'Synergy':<15} : {synergy}")
        elif template == "legacy_changingbreeds":
            feral_heart = advantages.get("feral_heart", 1)
            if feral_heart > 0:
                advantage_list.append(f"{'Feral Heart':<15} : {feral_heart}")
        
        # Create section headers using the same format as other sections
        merits_header = f"|g<{'-' * 12} MERITS {'-' * 13}>|n"
        advantages_header = f"|g<{'-' * 12} ADVANTAGES {'-' * 13}>|n"
        output.append(f"{merits_header.ljust(36)} {advantages_header}")
        
        # Display merits and advantages side by side
        max_rows = max(len(merit_list) if merit_list else 1, len(advantage_list))
        for i in range(max_rows):
            left_item = merit_list[i] if i < len(merit_list) else ""
            right_item = advantage_list[i] if i < len(advantage_list) else ""
            
            # Handle empty merits case
            if not merit_list and i == 0:
                left_item = "No merits yet."
            
            left_formatted = left_item.ljust(48)
            output.append(f"{left_formatted} {right_item}")
        
        # Add note if werewolf is shifted
        if template.lower() == "werewolf":
            current_form = getattr(target.db, 'current_form', 'hishu')
            if current_form != 'hishu':
                output.append(" " * 48 + " |y▸ Modified by form|n")
        
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
                            favor_display = f"{favor_name.replace('_', ' ').title():<25} {dots_display}"
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
                            aspect_display = f"{aspect_name.replace('_', ' ').title():<25} {dots_display}"
                        else:
                            aspect_display = f"{aspect_name.replace('_', ' ').title()}"
                    else:
                        aspect_display = f"{aspect_name.replace('_', ' ').title()}"
                    aspect_list.append(aspect_display)
            
            # Create section headers
            favors_header = f"|g<{'-' * 12} FAVORS {'-' * 13}>|n"
            aspects_header = f"|g<{'-' * 12} ASPECTS {'-' * 13}>|n"
            output.append(f"{favors_header.ljust(36)} {aspects_header}")
            
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
                
                left_formatted = left_item.ljust(48)
                output.append(f"{left_formatted} {right_item}")
        
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
            'beast': 'NIGHTMARES',
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
            'beast': 'RITUALS',
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
                        
                        left_formatted = left_key.ljust(39)
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
                    haunt_display = f"{haunt_name.replace('_', ' ').title():<15} {dots}"
                    haunt_list.append(haunt_display)
                
                # Display haunts in 2 columns like merits
                for i in range(0, len(haunt_list), 2):
                    left_haunt = haunt_list[i] if i < len(haunt_list) else ""
                    right_haunt = haunt_list[i + 1] if i + 1 < len(haunt_list) else ""
                    
                    # Format with proper spacing (39 chars for left column)
                    left_formatted = left_haunt.ljust(39)
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
                    
                    left_formatted = left_ceremony.ljust(39)
                    output.append(f"{left_formatted} {right_ceremony}")
            else:
                output.append("No ceremonies learned yet.")
        
        else:
            # Regular template power display (skip for hunter since endowments are handled separately)
            if template.lower() != "hunter":
                if powers or template_powers:
                    output.append(self._format_section_header(f"|w{primary_section}|n"))
                    
                    if template_powers:
                        power_display = self._format_powers_display(powers, template_powers, force_ascii)
                        output.extend(power_display)
                    else:
                        output.append("No primary powers available for this template.")
        
        # Secondary Powers (rituals, rites, blood sorcery) - skip for Geist and Hunter since handled separately
        if template.lower() not in ["geist", "hunter"] and (powers or template_secondary_powers):
            if template_secondary_powers:  # Only show section if template has secondary powers
                output.append(self._format_section_header(f"|w{secondary_section}|n"))
                
                secondary_power_display = self._format_secondary_powers_display(powers, template_secondary_powers, force_ascii)
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
                    
                    left_formatted = left_endowment.ljust(39)
                    output.append(f"  {left_formatted} {right_endowment}")
            else:
                output.append("No endowment powers learned yet.")
            
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
            
            # Display each category that has powers
            for category in ["Discipline Powers", "Devotions", "Coils of the Dragon", 
                           "Scales of the Dragon", "Theban Sorcery", "Cruac"]:
                if category in vamp_powers and vamp_powers[category]:
                    output.append(self._format_section_header(f"|w{category.upper()}|n"))
                    for power in sorted(vamp_powers[category]):
                        output.append(f"  {power}")
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
                        
                        left_formatted = left_tell.ljust(39)
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
                        
                        left_formatted = left_power.ljust(39)
                        output.append(f"{left_formatted} {right_power}")
        
        # Pools section (horizontal layout)
        output.append(self._format_section_header("|wPOOLS|n"))
        
        # Get pools data
        health_max = advantages.get("health", 7)
        health_track = self._get_health_track(target)
        
        # Save the compacted track back to ensure consistency
        self._set_health_track(target, health_track)
        
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
        
        willpower_dots = self._format_dots(willpower_current, willpower_max, force_ascii)
        
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
            
            pool_dots = self._format_dots(pool_current, pool_max, force_ascii)
            pool_display = f"{pool_name} ({pool_current}/{pool_max})"
        
        # Create horizontal pools layout
        health_label = "Health"
        willpower_label = f"Willpower ({willpower_current}/{willpower_max})"
        
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
                    output.append(f"{i}. {asp}")
        
        # Legacy Experience (only show in legacy mode)
        if legacy_mode:
            output.append(self._format_section_header("|wEXPERIENCE|n"))
            legacy_xp = target.attributes.get('legacy_experience', default=0)
            output.append(f"Experience Points: |y{legacy_xp}|n")
        
        output.append(f"|y{'='*78}|n")
        
        # Add encoding info to bottom if ASCII mode is being used
        if not supports_utf8 or force_ascii:
            if force_ascii:
                output.append("|g(ASCII mode active - use +sheet without /ascii for Unicode)|n")
            else:
                output.append("|y(ASCII mode due to encoding - see note above for UTF-8)|n")
        
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
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        
        # Show encoding warning if needed (only for self, not when viewing others)
        if target == self.caller and not supports_utf8 and "ascii" not in self.switches:
            self._show_encoding_warning(supports_utf8)
        
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
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        
        # Show encoding warning if needed
        if target == self.caller and not supports_utf8 and "ascii" not in self.switches:
            self._show_encoding_warning(supports_utf8)
        
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
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        
        # Show encoding warning if needed (only for self, not when viewing others)
        if target == self.caller and not supports_utf8 and "ascii" not in self.switches:
            self._show_encoding_warning(supports_utf8)
        
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
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        
        # Show encoding warning if needed (only for self, not when viewing others)
        if target == self.caller and not supports_utf8 and "ascii" not in self.switches:
            self._show_encoding_warning(supports_utf8)
        
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
                filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
                
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
        
        # Add template-specific bio fields
        for field in template_fields:
            if field not in ["virtue", "vice"]:  # virtue/vice already added above if valid
                field_value = bio.get(field, "<not set>")
                # Special case for cover_identity to display as "Cover ID"
                if field == "cover_identity":
                    field_label = "Cover ID"
                else:
                    field_label = field.replace("_", " ").title()
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
                mental.append(f"{attr.title():<15} {dots}")
            
            # Physical
            physical = []
            for attr in ["strength", "dexterity", "stamina"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                physical.append(f"{attr.title():<15} {dots}")
            
            # Social
            social = []
            for attr in ["presence", "manipulation", "composure"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
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
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
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
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
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
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
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
                
                merit_display = f"{display_name:<25} {dots}"
                merit_list.append(merit_display)
        
        # Create advantages list (including integrity)
        advantage_list = [
            f"{'Defense':<15} : {advantages.get('defense', 0)}",
            f"{'Speed':<15} : {advantages.get('speed', 0)}",
            f"{'Initiative':<15} : {advantages.get('initiative', 0)}",
            f"{'Size':<15} : {other.get('size', 5)}"
        ]
        
        # Add integrity to advantages (except for Geist characters who don't use integrity)
        if template != "geist":
            integrity_name = target.get_integrity_name(template)
            advantage_list.append(f"{integrity_name:<15} : {other.get('integrity', 7)}")
        
        # Add template-specific advantages
        if template == "changeling":
            wyrd = advantages.get("wyrd", 0)
            if wyrd > 0:
                advantage_list.append(f"{'Wyrd':<15} : {wyrd}")
        elif template == "werewolf":
            primal_urge = advantages.get("primal_urge", 0)
            if primal_urge > 0:
                advantage_list.append(f"{'Primal Urge':<15} : {primal_urge}")
        elif template == "vampire":
            blood_potency = advantages.get("blood_potency", 0)
            if blood_potency > 0:
                advantage_list.append(f"{'Blood Potency':<15} : {blood_potency}")
        elif template == "mage":
            gnosis = advantages.get("gnosis", 0)
            if gnosis > 0:
                advantage_list.append(f"{'Gnosis':<15} : {gnosis}")
        elif template == "deviant":
            deviation = advantages.get("deviation", 0)
            if deviation > 0:
                advantage_list.append(f"{'Deviation':<15} : {deviation}")
        elif template == "demon":
            primum = advantages.get("primum", 0)
            if primum > 0:
                advantage_list.append(f"{'Primum':<15} : {primum}")
        elif template == "promethean":
            azoth = advantages.get("azoth", 0)
            if azoth > 0:
                advantage_list.append(f"{'Azoth':<15} : {azoth}")
        elif template == "geist":
            # Geist characters use Synergy instead of integrity
            synergy = advantages.get("synergy", 1)
            advantage_list.append(f"{'Synergy':<15} : {synergy}")
        elif template == "legacy_changingbreeds":
            feral_heart = advantages.get("feral_heart", 1)
            if feral_heart > 0:
                advantage_list.append(f"{'Feral Heart':<15} : {feral_heart}")
        
        # Create section headers using the same format as other sections
        merits_header = f"|g<{'-' * 12} MERITS {'-' * 13}>|n"
        advantages_header = f"|g<{'-' * 12} ADVANTAGES {'-' * 13}>|n"
        output.append(f"{merits_header.ljust(36)} {advantages_header}")
        
        # Display merits and advantages side by side
        max_rows = max(len(merit_list) if merit_list else 1, len(advantage_list))
        for i in range(max_rows):
            left_item = merit_list[i] if i < len(merit_list) else ""
            right_item = advantage_list[i] if i < len(advantage_list) else ""
            
            # Handle empty merits case
            if not merit_list and i == 0:
                left_item = "No merits yet."
            
            left_formatted = left_item.ljust(48)
            output.append(f"{left_formatted} {right_item}")
        
        # Add note if werewolf is shifted
        if template.lower() == "werewolf":
            current_form = getattr(target.db, 'current_form', 'hishu')
            if current_form != 'hishu':
                output.append(" " * 48 + " |y▸ Modified by form|n")
        
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
                            favor_display = f"{favor_name.replace('_', ' ').title():<25} {dots_display}"
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
                            aspect_display = f"{aspect_name.replace('_', ' ').title():<25} {dots_display}"
                        else:
                            aspect_display = f"{aspect_name.replace('_', ' ').title()}"
                    else:
                        aspect_display = f"{aspect_name.replace('_', ' ').title()}"
                    aspect_list.append(aspect_display)
            
            # Create section headers
            favors_header = f"|g<{'-' * 12} FAVORS {'-' * 13}>|n"
            aspects_header = f"|g<{'-' * 12} ASPECTS {'-' * 13}>|n"
            output.append(f"{favors_header.ljust(36)} {aspects_header}")
            
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
                
                left_formatted = left_item.ljust(48)
                output.append(f"{left_formatted} {right_item}")
        
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
            'beast': 'NIGHTMARES',
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
            'beast': 'RITUALS',
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
                        
                        left_formatted = left_key.ljust(39)
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
                    haunt_display = f"{haunt_name.replace('_', ' ').title():<15} {dots}"
                    haunt_list.append(haunt_display)
                
                # Display haunts in 2 columns like merits
                for i in range(0, len(haunt_list), 2):
                    left_haunt = haunt_list[i] if i < len(haunt_list) else ""
                    right_haunt = haunt_list[i + 1] if i + 1 < len(haunt_list) else ""
                    
                    # Format with proper spacing (39 chars for left column)
                    left_formatted = left_haunt.ljust(39)
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
                    
                    left_formatted = left_ceremony.ljust(39)
                    output.append(f"{left_formatted} {right_ceremony}")
            else:
                output.append("No ceremonies learned yet.")
        
        else:
            # Regular template power display (skip for hunter since endowments are handled separately)
            if template.lower() != "hunter":
                if powers or template_powers:
                    output.append(self._format_section_header(f"|w{primary_section}|n"))
                    
                    if template_powers:
                        power_display = self._format_powers_display(powers, template_powers, force_ascii)
                        output.extend(power_display)
                    else:
                        output.append("No primary powers available for this template.")
        
        # Secondary Powers (rituals, rites, blood sorcery) - skip for Geist and Hunter since handled separately
        if template.lower() not in ["geist", "hunter"] and (powers or template_secondary_powers):
            if template_secondary_powers:  # Only show section if template has secondary powers
                output.append(self._format_section_header(f"|w{secondary_section}|n"))
                
                secondary_power_display = self._format_secondary_powers_display(powers, template_secondary_powers, force_ascii)
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
                    
                    left_formatted = left_endowment.ljust(39)
                    output.append(f"  {left_formatted} {right_endowment}")
            else:
                output.append("No endowment powers learned yet.")
            
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
            
            # Display each category that has powers
            for category in ["Discipline Powers", "Devotions", "Coils of the Dragon", 
                           "Scales of the Dragon", "Theban Sorcery", "Cruac"]:
                if category in vamp_powers and vamp_powers[category]:
                    output.append(self._format_section_header(f"|w{category.upper()}|n"))
                    for power in sorted(vamp_powers[category]):
                        output.append(f"  {power}")
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
                        
                        left_formatted = left_tell.ljust(39)
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
                        
                        left_formatted = left_power.ljust(39)
                        output.append(f"{left_formatted} {right_power}")
        
        # Pools section (horizontal layout)
        output.append(self._format_section_header("|wPOOLS|n"))
        
        # Get pools data
        health_max = advantages.get("health", 7)
        health_track = self._get_health_track(target)
        
        # Save the compacted track back to ensure consistency
        self._set_health_track(target, health_track)
        
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
        
        willpower_dots = self._format_dots(willpower_current, willpower_max, force_ascii)
        
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
            
            pool_dots = self._format_dots(pool_current, pool_max, force_ascii)
            pool_display = f"{pool_name} ({pool_current}/{pool_max})"
        
        # Create horizontal pools layout
        health_label = "Health"
        willpower_label = f"Willpower ({willpower_current}/{willpower_max})"
        
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
                    output.append(f"{i}. {asp}")
        
        # Legacy Experience (only show in legacy mode)
        if legacy_mode:
            output.append(self._format_section_header("|wEXPERIENCE|n"))
            legacy_xp = target.attributes.get('legacy_experience', default=0)
            output.append(f"Experience Points: |y{legacy_xp}|n")
        
        output.append(f"|y{'='*78}|n")
        
        # Add encoding info to bottom if ASCII mode is being used
        if not supports_utf8 or force_ascii:
            if force_ascii:
                output.append("|g(ASCII mode active - use +sheet without /ascii for Unicode)|n")
            else:
                output.append("|y(ASCII mode due to encoding - see note above for UTF-8)|n")
        
        return output 