import re
from evennia.commands.default.muxcommand import MuxCommand
from world.cofd.merits.general_merits import merits_dict, all_merits


class CmdExperience(MuxCommand):
    """
    Manage your character's experience points and beats.

    Usage:
        +xp                              - Show your current experience and beats
        +xp/log                          - Show complete XP history with all gains/losses
        +xp/beat <source>               - Add a beat from a valid source
        +xp/arcane <source>             - Add an arcane beat (Mages only)
        +xp/vitriol <source>            - Add a vitriol beat (Prometheans only)
        +xp/reminisce <source>          - Add a reminisce beat (Mummies only)
        +xp/award <character>=<beats>   - Award beats to a character (staff only)
        +xp/spend <stat>=<dots>         - Spend experience on any stat
        +xp/spend <stat:instance>=<dots> - Spend experience on instanced merit
        +xp/costs                       - Show experience point costs for your template

    Valid beat sources:
        dramatic_failure, exceptional_success, conditions, aspirations,
        story, scene, session, roleplay, challenge, sacrifice,
        discovery, relationship, consequence, learning, growth
    
    Valid arcane beat sources (Mages only):
        obsession, magical_condition, spell_dramatic_failure, 
        act_of_hubris, legacy_tutoring, supernatural_encounter
        
    Note: Exceptional successes and dramatic failures from dice rolls 
    automatically award beats - no need to manually request them.

    General XP Costs (All Templates):
        Attributes: 4 XP per dot
        Skills: 2 XP per dot  
        Merits: 1 XP per dot (supports instances)
        Skill Specialty: 1 XP each
        Integrity: 2 XP per dot
        Lost Willpower: 1 XP per dot
    
    Template-Specific Costs:
        Use +xp/costs to see costs for your specific template, including
        affinity calculations and special XP types.

    Examples:
        +xp/spend strength=4                    - Raise Strength to 4 dots
        +xp/spend unseen_sense:ghosts=2         - Buy Unseen Sense (Ghosts) merit
        +xp/spend athletics_specialty=running   - Add Running specialty to Athletics
        +xp/spend willpower=7                   - Restore lost Willpower
        +xp/spend animalism=3                   - Raise Animalism (Vampire)
        +xp/spend forces=2                      - Raise Forces (Mage)
        +xp/spend primal_urge=2                 - Raise Primal Urge (Werewolf)
        +xp/award nicole=15                     - Award 15 beats to Nicole (staff only)
    """
    key = "+xp"
    aliases = ["+experience", "+beat"]
    help_category = "Chargen & Character Info"

    def func(self):
        """Execute the command."""
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        legacy_mode = is_legacy_mode()
        
        # Get the appropriate experience handler
        if legacy_mode:
            from world.legacy_experience import LegacyExperienceHandler
            exp_handler = LegacyExperienceHandler(self.caller)
        else:
            # Use the character's experience property which uses lazy loading
            exp_handler = self.caller.experience

        # MuxCommand uses self.switches (a list) - check if empty or get first switch
        if not self.switches:
            self.show_experience(exp_handler)
        elif self.switches[0] == "beat":
            if legacy_mode:
                self.caller.msg("|rBeats system is disabled in Legacy Mode.|n")
                self.caller.msg("Experience is awarded directly. Use +xp/award for staff awards.")
            else:
                self.add_beat(exp_handler)
        elif self.switches[0] == "arcane":
            if legacy_mode:
                self.caller.msg("|rArcane beats are not available in Legacy Mode.|n")
            else:
                self.add_arcane_beat(exp_handler)
        elif self.switches[0] == "vitriol":
            if legacy_mode:
                self.caller.msg("|rVitriol beats are not available in Legacy Mode.|n")
            else:
                self.add_vitriol_beat(exp_handler)
        elif self.switches[0] == "reminisce":
            if legacy_mode:
                self.caller.msg("|rReminisce beats are not available in Legacy Mode.|n")
            else:
                self.add_reminisce_beat(exp_handler)
        elif self.switches[0] == "spend":
            # Check for secondary switch (arcane)
            if len(self.switches) > 1 and self.switches[1] == "arcane":
                self.spend_arcane_experience(exp_handler)
            else:
                self.spend_experience(exp_handler)
        elif self.switches[0] == "buy":
            self.buy_merit(exp_handler)
        elif self.switches[0] == "refund":
            self.refund_merit(exp_handler)
        elif self.switches[0] == "list":
            self.list_merits()
        elif self.switches[0] == "info":
            self.merit_info()
        elif self.switches[0] == "costs":
            # Check for secondary switch (arcane)
            if len(self.switches) > 1 and self.switches[1] == "arcane":
                self.show_arcane_costs()
            else:
                self.show_costs()
        elif self.switches[0] == "log":
            self.show_xp_log(exp_handler)
        elif self.switches[0] == "award":
            self.award_beats(exp_handler)
        else:
            self.caller.msg("Unknown switch. See 'help +xp' for usage.")

    def show_experience(self, exp_handler):
        """Show current experience with styled output and recent history."""
        from commands.CmdLegacy import is_legacy_mode
        from world.xp_logger import get_xp_logger
        
        legacy_mode = is_legacy_mode()
        
        # Check character template for special XP types
        character_template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
        is_mage = character_template.lower() in ["mage", "legacy_mage"]
        is_promethean = character_template.lower() == "promethean"
        is_mummy = character_template.lower() == "mummy"
        
        # Build styled output matching aspirations format
        output = []
        output.append("|y" + "=" * 78 + "|n")
        output.append("|y" + "EXPERIENCE & BEATS".center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        if legacy_mode:
            # Legacy mode - show only experience points
            output.append(self._format_section_header("|wCURRENT TOTALS|n"))
            output.append(f"Experience Points: |y{exp_handler.experience}|n")
            output.append("")
            output.append("|cLegacy Mode:|n Experience awarded directly, no beats system")
        else:
            # Modern mode - show beats and experience
            output.append(self._format_section_header("|wCURRENT TOTALS|n"))
            
            fractional_beats = self.caller.attributes.get('fractional_beats', default=0.0)
            if fractional_beats > 0:
                output.append(f"Beats: |c{exp_handler.beats}|n + |c{fractional_beats:.1f}|n fractional = |c{exp_handler.total_beats:.1f}|n total")
            else:
                output.append(f"Beats: |c{exp_handler.beats}|n")
                
            output.append(f"Experience Points: |y{exp_handler.experience}|n")
            output.append(f"|x(5 beats = 1 experience point)|n")
            
            # Show arcane experience for Mages
            if is_mage:
                output.append("")
                fractional_arcane_beats = self.caller.attributes.get('fractional_arcane_beats', default=0.0)
                if fractional_arcane_beats > 0:
                    output.append(f"Arcane Beats: |m{exp_handler.arcane_beats}|n + |m{fractional_arcane_beats:.1f}|n fractional = |m{exp_handler.total_arcane_beats:.1f}|n total")
                else:
                    output.append(f"Arcane Beats: |m{exp_handler.arcane_beats}|n")
                
                output.append(f"Arcane Experience: |M{exp_handler.arcane_experience}|n")
                output.append(f"|x(5 arcane beats = 1 arcane experience)|n")
            
            # Show vitriol experience for Prometheans
            if is_promethean:
                output.append("")
                fractional_vitriol_beats = self.caller.attributes.get('fractional_vitriol_beats', default=0.0)
                if fractional_vitriol_beats > 0:
                    output.append(f"Vitriol Beats: |g{exp_handler.vitriol_beats}|n + |g{fractional_vitriol_beats:.1f}|n fractional = |g{exp_handler.total_vitriol_beats:.1f}|n total")
                else:
                    output.append(f"Vitriol Beats: |g{exp_handler.vitriol_beats}|n")
                
                output.append(f"Vitriol Experience: |G{exp_handler.vitriol_experience}|n")
                output.append(f"|x(5 vitriol beats = 1 vitriol experience)|n")
            
            # Show reminisce experience for Mummies
            if is_mummy:
                output.append("")
                fractional_reminisce_beats = self.caller.attributes.get('fractional_reminisce_beats', default=0.0)
                if fractional_reminisce_beats > 0:
                    output.append(f"Reminisce Beats: |y{exp_handler.reminisce_beats}|n + |y{fractional_reminisce_beats:.1f}|n fractional = |y{exp_handler.total_reminisce_beats:.1f}|n total")
                else:
                    output.append(f"Reminisce Beats: |y{exp_handler.reminisce_beats}|n")
                
                output.append(f"Reminisce Experience: |Y{exp_handler.reminisce_experience}|n")
                output.append(f"|x(5 reminisce beats = 1 reminisce experience)|n")
            
            output.append("")
            
            # Recent changes section
            output.append(self._format_section_header("|wRECENT CHANGES (Last 5)|n"))
            logger = get_xp_logger(self.caller)
            recent = logger.get_recent_changes(5)
            
            if recent:
                for entry in recent:
                    output.append(logger.format_log_entry(entry, show_date=True))
            else:
                output.append("|x(no recent changes)|n")
            
            output.append("")
            output.append("|gUse |n+xp/log|g to see full XP history|n")
        
        output.append("|y" + "=" * 78 + "|n")
        self.caller.msg("\n".join(output))
    
    def _format_section_header(self, section_name):
        """Format section header matching aspiration style."""
        import re
        total_width = 78
        # Remove ANSI codes for length calculation
        clean_name = re.sub(r'\|[a-zA-Z]', '', section_name)
        name_length = len(clean_name)
        available_dash_space = total_width - name_length - 4
        left_dashes = available_dash_space // 2
        right_dashes = available_dash_space - left_dashes
        return f"|g<{'-' * left_dashes}|n {section_name} |g{'-' * right_dashes}>|n"
    
    def show_xp_log(self, exp_handler):
        """Show full XP history."""
        from world.xp_logger import get_xp_logger
        
        logger = get_xp_logger(self.caller)
        all_changes = logger.get_all_changes()
        
        if not all_changes:
            self.caller.msg("No XP history recorded yet.")
            return
        
        output = []
        output.append("|y" + "=" * 78 + "|n")
        output.append("|y" + "COMPLETE XP HISTORY".center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        for entry in all_changes:
            output.append(logger.format_log_entry(entry, show_date=True))
        
        output.append("")
        output.append(f"|gTotal entries: {len(all_changes)}|n")
        output.append("|y" + "=" * 78 + "|n")
        
        self.caller.msg("\n".join(output))
    
    def award_beats(self, exp_handler):
        """Award beats to a character (staff only)."""
        from world.xp_logger import get_xp_logger
        
        # Check staff permissions
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("|rYou must be staff to award beats to other characters.|n")
            return
        
        # Parse character=beats
        if "=" not in self.args:
            self.caller.msg("Usage: +xp/award <character>=<beats>")
            self.caller.msg("Example: +xp/award Nicole=15")
            return
        
        try:
            character_name, beats_str = self.args.split("=", 1)
            character_name = character_name.strip()
            beats_amount = float(beats_str.strip())
        except ValueError:
            self.caller.msg("Usage: +xp/award <character>=<beats>")
            self.caller.msg("Beats must be a number (can include decimals like 0.5)")
            return
        
        # Validate beats amount
        if beats_amount <= 0:
            self.caller.msg("Beats amount must be positive.")
            return
        
        if beats_amount > 100:
            self.caller.msg("Cannot award more than 100 beats at once. Award multiple times if needed.")
            return
        
        # Find target character
        from world.voting import get_character_by_name
        target_character = get_character_by_name(character_name)
        
        if not target_character:
            self.caller.msg(f"Character '{character_name}' not found.")
            return
        
        # Award the beats
        target_exp_handler = target_character.experience
        whole_beats, remaining_fractional = target_exp_handler.add_fractional_beat(beats_amount)
        
        # Calculate XP equivalent
        xp_equivalent = int(beats_amount / 5)
        
        # Log the award
        logger = get_xp_logger(target_character)
        logger.log_beat(beats_amount, "Staff Award", details=f"Awarded by {self.caller.name}")
        
        # Notify staff
        if xp_equivalent > 0:
            self.caller.msg(f"|gAwarded {beats_amount} beats ({xp_equivalent} XP) to {target_character.name}.|n")
        else:
            self.caller.msg(f"|gAwarded {beats_amount} beats to {target_character.name}.|n")
        
        self.caller.msg(f"{target_character.name}'s new totals: {target_exp_handler.beats} beats, {target_exp_handler.experience} XP")
        
        # Notify target player
        if xp_equivalent > 0:
            target_character.msg(f"|gStaff Award!|n {self.caller.name} awarded you {beats_amount} beats ({xp_equivalent} XP)!")
        else:
            target_character.msg(f"|gStaff Award!|n {self.caller.name} awarded you {beats_amount} beats!")
        
        target_character.msg(f"Your new totals: {target_exp_handler.beats} beats, {target_exp_handler.experience} XP")

    def add_beat(self, exp_handler):
        """Add a beat from a valid source."""
        from world.xp_logger import get_xp_logger
        
        valid_sources = [
            "dramatic_failure", "exceptional_success", "conditions", "aspirations",
            "story", "scene", "session", "roleplay", "challenge", "sacrifice",
            "discovery", "relationship", "consequence", "learning", "growth"
        ]
        
        source = self.args.strip().lower().replace(" ", "_")
        if not source:
            self.caller.msg("You must specify a beat source. Valid sources: " + ", ".join(valid_sources))
            return
            
        if source not in valid_sources:
            self.caller.msg(f"Invalid beat source '{source}'. Valid sources: " + ", ".join(valid_sources))
            return
            
        exp_handler.add_beat()
        
        # Log the beat gain
        logger = get_xp_logger(self.caller)
        logger.log_beat(1, source.replace('_', ' ').title(), details="Added via +xp/beat command")
        
        self.caller.msg(f"|gAdded 1 beat from '{source.replace('_', ' ')}'.|n")
        self.caller.msg(f"Current beats: {exp_handler.beats}, Experience: {exp_handler.experience}")
    
    def add_arcane_beat(self, exp_handler):
        """Add an arcane beat from a valid source (Mages only)."""
        from world.xp_logger import get_xp_logger
        
        # Check if character is a Mage
        character_template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() not in ["mage", "legacy_mage"]:
            self.caller.msg("|rOnly Mages can earn Arcane Beats.|n")
            self.caller.msg(f"Your template is: {character_template}")
            return
        
        valid_sources = [
            "obsession", "magical_condition", "spell_dramatic_failure",
            "act_of_hubris", "legacy_tutoring", "supernatural_encounter"
        ]
        
        source = self.args.strip().lower().replace(" ", "_")
        if not source:
            self.caller.msg("You must specify an arcane beat source. Valid sources: " + ", ".join(valid_sources))
            return
            
        if source not in valid_sources:
            self.caller.msg(f"Invalid arcane beat source '{source}'. Valid sources: " + ", ".join(valid_sources))
            return
        
        # Add descriptions for each source
        source_descriptions = {
            "obsession": "fulfilling or making major headway into an Obsession",
            "magical_condition": "resolving a Condition from spellcasting, Paradox, or magical effect",
            "spell_dramatic_failure": "voluntarily making a spellcasting roll a dramatic failure",
            "act_of_hubris": "risking an Act of Hubris against Wisdom",
            "legacy_tutoring": "spending a scene tutoring/being tutored in a Legacy",
            "supernatural_encounter": "having a meaningful new supernatural encounter"
        }
        
        exp_handler.add_arcane_beat()
        
        # Log the arcane beat gain
        logger = get_xp_logger(self.caller)
        logger.log_change('arcane_beat', 1, source.replace('_', ' ').title(), details="Added via +xp/arcane command")
        
        self.caller.msg(f"|mAdded 1 arcane beat from {source_descriptions[source]}.|n")
        self.caller.msg(f"Current arcane beats: {exp_handler.arcane_beats}, Arcane experience: {exp_handler.arcane_experience}")

    def add_vitriol_beat(self, exp_handler):
        """Add a vitriol beat from a valid source (Prometheans only)."""
        from world.xp_logger import get_xp_logger
        
        # Check if character is a Promethean
        character_template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() != "promethean":
            self.caller.msg("|rOnly Prometheans can earn Vitriol Beats.|n")
            self.caller.msg(f"Your template is: {character_template}")
            return
        
        valid_sources = [
            "milestone", "azothic_radiance", "transmutation", "lineage_discovery",
            "roleplay", "sacrifice", "pilgrimage_progress"
        ]
        
        source = self.args.strip().lower().replace(" ", "_")
        if not source:
            self.caller.msg("You must specify a vitriol beat source. Valid sources: " + ", ".join(valid_sources))
            return
            
        if source not in valid_sources:
            self.caller.msg(f"Invalid vitriol beat source '{source}'. Valid sources: " + ", ".join(valid_sources))
            return
        
        exp_handler.add_vitriol_beat()
        
        # Log the vitriol beat gain
        logger = get_xp_logger(self.caller)
        logger.log_change('vitriol_beat', 1, source.replace('_', ' ').title(), details="Added via +xp/vitriol command")
        
        self.caller.msg(f"|gAdded 1 vitriol beat from '{source.replace('_', ' ')}'.|n")
        self.caller.msg(f"Current vitriol beats: {exp_handler.vitriol_beats}, Vitriol experience: {exp_handler.vitriol_experience}")

    def add_reminisce_beat(self, exp_handler):
        """Add a reminisce beat from a valid source (Mummies only)."""
        from world.xp_logger import get_xp_logger
        
        # Check if character is a Mummy
        character_template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() != "mummy":
            self.caller.msg("|rOnly Mummies can earn Reminisce Beats.|n")
            self.caller.msg(f"Your template is: {character_template}")
            return
        
        valid_sources = [
            "memory_regained", "cult_advancement", "pillar_fulfilled",
            "decree_completed", "roleplay", "sacrifice", "ancient_discovery"
        ]
        
        source = self.args.strip().lower().replace(" ", "_")
        if not source:
            self.caller.msg("You must specify a reminisce beat source. Valid sources: " + ", ".join(valid_sources))
            return
            
        if source not in valid_sources:
            self.caller.msg(f"Invalid reminisce beat source '{source}'. Valid sources: " + ", ".join(valid_sources))
            return
        
        exp_handler.add_reminisce_beat()
        
        # Log the reminisce beat gain
        logger = get_xp_logger(self.caller)
        logger.log_change('reminisce_beat', 1, source.replace('_', ' ').title(), details="Added via +xp/reminisce command")
        
        self.caller.msg(f"|yAdded 1 reminisce beat from '{source.replace('_', ' ')}'.|n")
        self.caller.msg(f"Current reminisce beats: {exp_handler.reminisce_beats}, Reminisce experience: {exp_handler.reminisce_experience}")

    def spend_experience(self, exp_handler):
        """Spend experience on any stat type."""
        if "=" not in self.args:
            self.caller.msg("Usage: +xp/spend <stat>=<value>")
            self.caller.msg("Examples:")
            self.caller.msg("  +xp/spend strength=4")
            self.caller.msg("  +xp/spend unseen_sense:ghosts=2")
            self.caller.msg("  +xp/spend athletics_specialty=running")
            return
        
        # Check if werewolf character is in a form that allows stat modification
        from commands.shapeshifting import can_modify_stats_while_shifted
        can_modify, reason = can_modify_stats_while_shifted(self.caller)
        if not can_modify:
            self.caller.msg(f"|r{reason}|n")
            return
            
        stat_input, value_str = self.args.split("=", 1)
        stat_input = stat_input.strip().lower()
        value_str = value_str.strip()
            
        # Initialize stats if needed
        if not self.caller.db.stats:
            self.caller.db.stats = {
                "attributes": {},
                "skills": {},
                "advantages": {},
                "anchors": {},
                "bio": {},
                "merits": {},
                "specialties": {},
                "powers": {},
                "other": {}
            }
            
        stats = self.caller.db.stats
        template = stats.get("other", {}).get("template", "Mortal").lower()
        
        # Parse stat input for instances (merit:instance or skill_specialty)
        instance = None
        if ":" in stat_input:
            # Instanced merit or similar
            stat_name, instance = stat_input.split(":", 1)
            stat_name = stat_name.strip().lower().replace(" ", "_")
            instance = instance.strip()
        elif "_specialty" in stat_input:
            # Skill specialty
            skill_name = stat_input.replace("_specialty", "").strip().lower()
            return self._spend_on_specialty(exp_handler, skill_name, value_str)
        else:
            stat_name = stat_input.replace(" ", "_")
        
        # Try to parse as number (for dot-rated stats)
        try:
            target_dots = int(value_str)
            is_dot_rated = True
        except ValueError:
            # Not a number - could be a specialty name or semantic stat
            is_dot_rated = False
            target_dots = None
        
        # Import necessary modules
        from world.cofd.stat_dictionary import attribute_dictionary, skill_dictionary
        from world.xp_costs import calculate_xp_cost
        
        # Determine stat type and current value
        stat_type = None
        current_dots = 0
        max_dots = 5
        stat_category = None
        
        # Check for attributes
        if stat_name in attribute_dictionary:
            stat_type = 'attribute'
            stat_category = 'attributes'
            current_dots = stats.get("attributes", {}).get(stat_name, 1)
            max_dots = 5
        # Check for skills
        elif stat_name in skill_dictionary:
            stat_type = 'skill'
            stat_category = 'skills'
            current_dots = stats.get("skills", {}).get(stat_name, 0)
            max_dots = 5
        # Check for integrity/morality stats
        elif stat_name in ['integrity', 'humanity', 'wisdom', 'harmony', 'clarity', 'cover', 'synergy', 'pilgrimage', 'satiety', 'memory']:
            stat_type = 'integrity'
            stat_category = 'other'
            current_dots = stats["other"].get("integrity", 7)
            max_dots = 10
        # Check for willpower restoration
        elif stat_name == 'willpower':
            return self._spend_on_willpower(exp_handler, target_dots)
        # Check for merits
        elif instance or self._is_merit(stat_name):
            stat_type = 'merit'
            stat_category = 'merits'
            merit_key = f"{stat_name}:{instance}" if instance else stat_name
            current_dots = stats.get("merits", {}).get(merit_key, {}).get("dots", 0) if isinstance(stats.get("merits", {}).get(merit_key), dict) else 0
            max_dots = 5  # Will be validated against merit definition
        # Template-specific stats
        else:
            # Delegate to template-specific handler
            return self._spend_on_template_stat(exp_handler, stat_name, target_dots, instance)
        
        # Validate dot-rated purchase
        if not is_dot_rated:
            self.caller.msg(f"{stat_name.title()} requires a numeric dot rating.")
            return
            
        if target_dots <= current_dots:
            self.caller.msg(f"You already have {stat_name.title()} at {current_dots} dots or higher.")
            return
            
        if target_dots > max_dots:
            self.caller.msg(f"{stat_name.title()} cannot exceed {max_dots} dots.")
            return
            
        # Calculate cost using xp_costs module
        cost, xp_type = calculate_xp_cost(
            self.caller, stat_type, stat_name, current_dots, target_dots,
            instance=instance
        )
        
        if cost == 0:
            self.caller.msg(f"Unable to calculate cost for {stat_name}.")
            return
            
        # Check if we have enough XP
        if exp_handler.experience < cost:
            self.caller.msg(f"Insufficient experience. Need {cost} XP, have {exp_handler.experience} XP.")
            return
        
        # Spend the XP
        exp_handler.spend_experience(cost)
        
        # Update the stat
        if instance:
            merit_key = f"{stat_name}:{instance}"
            if merit_key not in stats[stat_category]:
                stats[stat_category][merit_key] = {}
            stats[stat_category][merit_key]["dots"] = target_dots
        else:
            stats[stat_category][stat_name] = target_dots
        
        # Log the expenditure
        from world.xp_logger import get_xp_logger
        logger = get_xp_logger(self.caller)
        display_name = f"{stat_name.title()} ({instance})" if instance else stat_name.title()
        logger.log_experience(-cost, f"{display_name}: {current_dots} > {target_dots}")
        
        self.caller.msg(f"|gSpent {cost} XP to raise {display_name} to {target_dots} dots.|n")
        self.caller.msg(f"Remaining experience: {exp_handler.experience}")
    
    def _is_merit(self, stat_name):
        """Check if a stat name is a valid merit."""
        from world.cofd.merits.general_merits import merits_dict
        return stat_name in merits_dict
    
    def _spend_on_specialty(self, exp_handler, skill_name, specialty_name):
        """Handle spending XP on a skill specialty."""
        from world.cofd.stat_dictionary import skill_dictionary
        from world.xp_logger import get_xp_logger
        
        # Validate skill exists
        if skill_name not in skill_dictionary:
            self.caller.msg(f"Unknown skill '{skill_name}'.")
            return
        
        # Check if character has dots in the skill
        skill_dots = self.caller.db.stats.get("skills", {}).get(skill_name, 0)
        if skill_dots == 0:
            self.caller.msg(f"You must have at least 1 dot in {skill_name.title()} to buy a specialty.")
            return
        
        # Check if specialty already exists
        specialties = self.caller.db.stats.get("specialties", {})
        skill_specialties = specialties.get(skill_name, [])
        if specialty_name.lower() in [s.lower() for s in skill_specialties]:
            self.caller.msg(f"You already have the '{specialty_name}' specialty for {skill_name.title()}.")
            return
        
        # Cost is 1 XP
        cost = 1
        
        if exp_handler.experience < cost:
            self.caller.msg(f"Insufficient experience. Need {cost} XP, have {exp_handler.experience} XP.")
            return
        
        # Spend the XP
        exp_handler.spend_experience(cost)
        
        # Add the specialty
        if skill_name not in specialties:
            specialties[skill_name] = []
        specialties[skill_name].append(specialty_name)
        self.caller.db.stats["specialties"] = specialties
        
        # Log the expenditure
        logger = get_xp_logger(self.caller)
        logger.log_experience(-cost, f"Specialty: {skill_name.title()} ({specialty_name})")
        
        self.caller.msg(f"|gSpent {cost} XP to add '{specialty_name}' specialty to {skill_name.title()}.|n")
        self.caller.msg(f"Remaining experience: {exp_handler.experience}")
    
    def _spend_on_willpower(self, exp_handler, target_dots):
        """Handle restoring lost willpower dots."""
        from world.xp_logger import get_xp_logger
        
        # Get current willpower and maximum
        composure = self.caller.db.stats.get("attributes", {}).get("composure", 1)
        resolve = self.caller.db.stats.get("attributes", {}).get("resolve", 1)
        max_willpower = composure + resolve
        current_willpower = self.caller.db.stats.get("advantages", {}).get("willpower", max_willpower)
        
        if current_willpower >= max_willpower:
            self.caller.msg(f"Your Willpower is already at maximum ({max_willpower}).")
            return
        
        if target_dots > max_willpower:
            self.caller.msg(f"Your maximum Willpower is {max_willpower} (Composure + Resolve).")
            return
        
        if target_dots <= current_willpower:
            self.caller.msg(f"Your Willpower is already {current_willpower} or higher.")
            return
        
        # Calculate cost
        dots_to_restore = target_dots - current_willpower
        cost = dots_to_restore * 1  # 1 XP per dot
        
        if exp_handler.experience < cost:
            self.caller.msg(f"Insufficient experience. Need {cost} XP, have {exp_handler.experience} XP.")
            return
        
        # Spend the XP
        exp_handler.spend_experience(cost)
        
        # Restore willpower
        if "advantages" not in self.caller.db.stats:
            self.caller.db.stats["advantages"] = {}
        self.caller.db.stats["advantages"]["willpower"] = target_dots
        
        # Log the expenditure
        logger = get_xp_logger(self.caller)
        logger.log_experience(-cost, f"Willpower Restored: {current_willpower} > {target_dots}")
        
        self.caller.msg(f"|gSpent {cost} XP to restore Willpower to {target_dots} dots.|n")
        self.caller.msg(f"Remaining experience: {exp_handler.experience}")
    
    def _spend_on_template_stat(self, exp_handler, stat_name, target_dots, instance=None):
        """Handle spending XP on template-specific stats."""
        template = self.caller.db.stats.get("other", {}).get("template", "Mortal").lower()
        
        # Route to appropriate template handler
        if template == 'werewolf':
            return self._spend_werewolf(exp_handler, stat_name, target_dots)
        elif template == 'vampire':
            return self._spend_vampire(exp_handler, stat_name, target_dots)
        elif template == 'mage':
            return self._spend_mage(exp_handler, stat_name, target_dots)
        elif template == 'changeling':
            return self._spend_changeling(exp_handler, stat_name, target_dots)
        elif template == 'geist':
            return self._spend_geist(exp_handler, stat_name, target_dots)
        elif template == 'demon':
            return self._spend_demon(exp_handler, stat_name, target_dots)
        elif template == 'hunter':
            return self._spend_hunter(exp_handler, stat_name, target_dots)
        elif template == 'deviant':
            return self._spend_deviant(exp_handler, stat_name, target_dots)
        elif template == 'promethean':
            return self._spend_promethean(exp_handler, stat_name, target_dots)
        elif template == 'mummy':
            return self._spend_mummy(exp_handler, stat_name, target_dots)
        elif template == 'mortal+':
            return self._spend_mortal_plus(exp_handler, stat_name, target_dots)
        else:
            self.caller.msg(f"Unknown stat '{stat_name}' for template {template}.")
            return
    
    def _spend_werewolf(self, exp_handler, stat_name, target_dots):
        """Handle Werewolf template XP spending."""
        from world.xp_costs import calculate_xp_cost, WEREWOLF_COSTS
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        powers = stats.get("powers", {})
        
        # Check for renown
        if stat_name in ['cunning', 'glory', 'honor', 'purity', 'wisdom']:
            current_dots = powers.get(stat_name, 0)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have {stat_name.title()} at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'renown', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            powers[stat_name] = target_dots
            stats["powers"] = powers
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"{stat_name.title()} (Renown): {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise {stat_name.title()} to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Check for primal urge
        if stat_name == 'primal_urge':
            current_dots = stats.get("advantages", {}).get("primal_urge", 1)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Primal Urge at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'primal_urge', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            if "advantages" not in stats:
                stats["advantages"] = {}
            stats["advantages"]["primal_urge"] = target_dots
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Primal Urge: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise Primal Urge to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Check for gifts (category-rated 1-5)
        gift_categories = ['full_moon', 'gibbous_moon', 'half_moon', 'crescent_moon', 'new_moon',
                          'dominance', 'strength', 'inspiration', 'knowledge', 'insight', 'warding',
                          'evasion', 'stealth', 'elemental', 'shaping', 'death', 'nature', 'rage',
                          'technology', 'weather']
        if stat_name in gift_categories:
            current_dots = powers.get(stat_name, 0)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have {stat_name.title()} gifts at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'gift', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            powers[stat_name] = target_dots
            stats["powers"] = powers
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"{stat_name.replace('_', ' ').title()} (Gift): {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise {stat_name.replace('_', ' ').title()} to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Check for rites (semantic, not dot-rated)
        if not target_dots:
            # Might be a rite
            cost = WEREWOLF_COSTS['rite']
            if exp_handler.experience < cost:
                self.caller.msg(f"Insufficient experience. Need {cost} XP, have {exp_handler.experience} XP.")
                return
            exp_handler.spend_experience(cost)
            # Add rite to powers
            if stat_name not in powers:
                powers[stat_name] = "known"
            stats["powers"] = powers
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Rite: {stat_name.replace('_', ' ').title()}")
            self.caller.msg(f"|gSpent {cost} XP to learn the {stat_name.replace('_', ' ').title()} rite.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        self.caller.msg(f"Unknown Werewolf stat '{stat_name}'.")
    
    def _spend_vampire(self, exp_handler, stat_name, target_dots):
        """Handle Vampire template XP spending."""
        from world.xp_costs import calculate_xp_cost
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        powers = stats.get("powers", {})
        
        # Check for disciplines
        disciplines = ['animalism', 'auspex', 'celerity', 'dominate', 'majesty', 'nightmare',
                      'obfuscate', 'protean', 'resilience', 'vigor', 'cachexy', 'crochan',
                      'dead_signal']
        if stat_name in disciplines:
            current_dots = powers.get(stat_name, 0)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have {stat_name.title()} at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'discipline', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            powers[stat_name] = target_dots
            stats["powers"] = powers
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"{stat_name.title()} (Discipline): {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise {stat_name.title()} to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Check for blood potency
        if stat_name == 'blood_potency':
            current_dots = stats.get("advantages", {}).get("blood_potency", 1)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Blood Potency at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'blood_potency', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            if "advantages" not in stats:
                stats["advantages"] = {}
            stats["advantages"]["blood_potency"] = target_dots
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Blood Potency: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise Blood Potency to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Check for Cruac/Theban Sorcery (dot-rated)
        if stat_name in ['cruac', 'theban_sorcery']:
            current_dots = powers.get(stat_name, 0)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have {stat_name.replace('_', ' ').title()} at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, stat_name, stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            powers[stat_name] = target_dots
            stats["powers"] = powers
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"{stat_name.replace('_', ' ').title()}: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise {stat_name.replace('_', ' ').title()} to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        self.caller.msg(f"Unknown Vampire stat '{stat_name}'.")
        self.caller.msg("Use +xp/costs to see available stats for your template.")
    
    def _spend_mage(self, exp_handler, stat_name, target_dots):
        """Handle Mage template XP spending."""
        self.caller.msg("Mage abilities use the arcane XP system.")
        self.caller.msg("Use: +xp/spend/arcane <stat>=<dots>")
        self.caller.msg("Or use normal XP with: +xp/spend <stat>=<dots>")
        return
    
    def _spend_changeling(self, exp_handler, stat_name, target_dots):
        """Handle Changeling template XP spending."""
        from world.xp_costs import calculate_xp_cost, is_changeling_contract_favored
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        powers = stats.get("powers", {})
        
        # Check for Wyrd
        if stat_name == 'wyrd':
            current_dots = stats.get("advantages", {}).get("wyrd", 1)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Wyrd at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'wyrd', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            if "advantages" not in stats:
                stats["advantages"] = {}
            stats["advantages"]["wyrd"] = target_dots
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Wyrd: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise Wyrd to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Check for contracts (dot-rated)
        # Contracts might be specified individually
        if target_dots and target_dots > 0:
            current_dots = powers.get(stat_name, 0)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have {stat_name.replace('_', ' ').title()} at {current_dots} dots.")
                return
            
            # Calculate cost (checks if favored)
            cost, xp_type = calculate_xp_cost(self.caller, 'contract', stat_name, current_dots, target_dots)
            
            if exp_handler.experience < cost:
                self.caller.msg(f"Insufficient experience. Need {cost} XP, have {exp_handler.experience} XP.")
                return
            
            exp_handler.spend_experience(cost)
            powers[stat_name] = target_dots
            stats["powers"] = powers
            
            # Indicate if favored
            is_favored = is_changeling_contract_favored(self.caller, stat_name)
            favored_text = " (Favored)" if is_favored else ""
            
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"{stat_name.replace('_', ' ').title()} (Contract){favored_text}: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise {stat_name.replace('_', ' ').title()}{favored_text} to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Unknown stat
        self.caller.msg(f"Unknown Changeling stat '{stat_name}'.")
        self.caller.msg("Use +xp/costs to see available stats for your template.")
    
    def _spend_geist(self, exp_handler, stat_name, target_dots):
        """Handle Geist (Sin-Eater) template XP spending."""
        from world.xp_costs import calculate_xp_cost
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        powers = stats.get("powers", {})
        
        # Check for Synergy
        if stat_name == 'synergy':
            current_dots = stats.get("advantages", {}).get("synergy", 1)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Synergy at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'synergy', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            if "advantages" not in stats:
                stats["advantages"] = {}
            stats["advantages"]["synergy"] = target_dots
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Synergy: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise Synergy to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Check for Haunts
        haunts = ['the_boneyard', 'the_caul', 'the_curse', 'the_dirge', 
                 'the_marionette', 'the_memoria', 'the_oracle', 'the_shroud', 'the_tomb']
        if stat_name in haunts:
            current_dots = powers.get(stat_name, 0)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have {stat_name.replace('_', ' ').title()} at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'haunt', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            powers[stat_name] = target_dots
            stats["powers"] = powers
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"{stat_name.replace('_', ' ').title()} (Haunt): {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise {stat_name.replace('_', ' ').title()} to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        self.caller.msg(f"Unknown Geist stat '{stat_name}'.")
    
    def _spend_demon(self, exp_handler, stat_name, target_dots):
        """Handle Demon template XP spending."""
        from world.xp_costs import calculate_xp_cost, DEMON_COSTS
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        powers = stats.get("powers", {})
        
        # Check for Primum
        if stat_name == 'primum':
            current_dots = stats.get("advantages", {}).get("primum", 1)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Primum at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'primum', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            if "advantages" not in stats:
                stats["advantages"] = {}
            stats["advantages"]["primum"] = target_dots
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Primum: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise Primum to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Check for Cover
        if stat_name == 'cover':
            current_dots = stats.get("advantages", {}).get("cover", 7)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Cover at {current_dots} dots.")
                return
            cost, xp_type = calculate_xp_cost(self.caller, 'cover', stat_name, current_dots, target_dots)
            exp_handler.spend_experience(cost)
            if "advantages" not in stats:
                stats["advantages"] = {}
            stats["advantages"]["cover"] = target_dots
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Cover: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {cost} XP to raise Cover to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        # Embeds and Exploits are semantic
        if not target_dots:
            # Try as embed or exploit
            cost = DEMON_COSTS['embed']  # Same cost for both
            if exp_handler.experience < cost:
                self.caller.msg(f"Insufficient experience. Need {cost} XP, have {exp_handler.experience} XP.")
                return
            exp_handler.spend_experience(cost)
            powers[stat_name] = "known"
            stats["powers"] = powers
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Embed/Exploit: {stat_name.replace('_', ' ').title()}")
            self.caller.msg(f"|gSpent {cost} XP to learn {stat_name.replace('_', ' ').title()}.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        self.caller.msg(f"Unknown Demon stat '{stat_name}'.")
    
    def _spend_hunter(self, exp_handler, stat_name, target_dots):
        """Handle Hunter template XP spending."""
        from world.xp_costs import HUNTER_COSTS
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        powers = stats.get("powers", {})
        
        # Endowments are typically semantic
        if not target_dots:
            cost = HUNTER_COSTS['endowment']
            if exp_handler.experience < cost:
                self.caller.msg(f"Insufficient experience. Need {cost} XP, have {exp_handler.experience} XP.")
                return
            exp_handler.spend_experience(cost)
            powers[stat_name] = "known"
            stats["powers"] = powers
            logger = get_xp_logger(self.caller)
            logger.log_experience(-cost, f"Endowment: {stat_name.replace('_', ' ').title()}")
            self.caller.msg(f"|gSpent {cost} XP to learn the {stat_name.replace('_', ' ').title()} endowment.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        self.caller.msg(f"Unknown Hunter stat '{stat_name}'.")
    
    def _spend_deviant(self, exp_handler, stat_name, target_dots):
        """Handle Deviant template XP spending."""
        from world.xp_costs import calculate_xp_cost
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        
        # Check for Variation (magnitude-rated)
        if stat_name == 'variation' or 'variation' in stat_name:
            self.caller.msg("Variations must be purchased through storyteller approval.")
            self.caller.msg("Cost: 4 XP per dot of Magnitude.")
            return
        
        # Check for Acclimation
        if stat_name == 'acclimation':
            self.caller.msg("Acclimation must be purchased through storyteller approval.")
            self.caller.msg("Cost: 5 XP. Requires meeting core book criteria.")
            return
        
        self.caller.msg(f"Unknown Deviant stat '{stat_name}'.")
    
    def _spend_promethean(self, exp_handler, stat_name, target_dots):
        """Handle Promethean template XP spending."""
        from world.xp_costs import calculate_xp_cost, PROMETHEAN_COSTS
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        
        # Check for Azoth (can use either normal or vitriol XP)
        if stat_name == 'azoth':
            current_dots = stats.get("advantages", {}).get("azoth", 1)
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Azoth at {current_dots} dots.")
                return
            
            dots_to_buy = target_dots - current_dots
            normal_cost = dots_to_buy * PROMETHEAN_COSTS['azoth_normal']
            vitriol_cost = dots_to_buy * PROMETHEAN_COSTS['azoth_vitriol']
            
            self.caller.msg(f"Azoth can be raised with either:")
            self.caller.msg(f"  {normal_cost} Normal XP")
            self.caller.msg(f"  {vitriol_cost} Vitriol XP")
            self.caller.msg("Please specify: +xp/spend azoth=<dots> (normal) or use vitriol via staff.")
            
            if exp_handler.experience < normal_cost:
                self.caller.msg(f"Insufficient normal experience. Need {normal_cost} XP, have {exp_handler.experience} XP.")
                return
            
            exp_handler.spend_experience(normal_cost)
            if "advantages" not in stats:
                stats["advantages"] = {}
            stats["advantages"]["azoth"] = target_dots
            logger = get_xp_logger(self.caller)
            logger.log_experience(-normal_cost, f"Azoth: {current_dots} > {target_dots}")
            self.caller.msg(f"|gSpent {normal_cost} XP to raise Azoth to {target_dots} dots.|n")
            self.caller.msg(f"Remaining experience: {exp_handler.experience}")
            return
        
        self.caller.msg(f"Promethean stats like Pilgrimage, Alembics, and Athanors require Vitriol XP.")
        self.caller.msg("Please coordinate with staff for vitriol-based purchases.")
    
    def _spend_mummy(self, exp_handler, stat_name, target_dots):
        """Handle Mummy template XP spending."""
        from world.xp_costs import calculate_xp_cost
        from world.xp_logger import get_xp_logger
        
        stats = self.caller.db.stats
        
        # Memory uses Reminisce XP only
        if stat_name == 'memory':
            self.caller.msg("Memory can only be raised with Reminisce XP.")
            self.caller.msg("Cost: 3 Reminisce XP per dot.")
            return
        
        # Cult attributes
        if stat_name in ['reach', 'grasp']:
            self.caller.msg("Cult attributes (Reach/Grasp) are purchased separately.")
            self.caller.msg("Cost: 6 XP per dot.")
            return
        
        # Dominance
        if stat_name == 'dominance':
            self.caller.msg("Dominance is purchased separately.")
            self.caller.msg("Cost: 5 XP per dot.")
            return
        
        self.caller.msg(f"Unknown Mummy stat '{stat_name}'.")
        self.caller.msg("Affinities, Utterances, and Pillars are purchased through +stat.")
    
    def _spend_mortal_plus(self, exp_handler, stat_name, target_dots):
        """Handle Mortal+ template XP spending."""
        stats = self.caller.db.stats
        template_type = stats.get("bio", {}).get("template_type", "").lower()
        
        self.caller.msg(f"Mortal+ ({template_type}) template stat purchases vary by type.")
        self.caller.msg("Please coordinate with staff or use +xp/costs for details.")

    def buy_merit(self, exp_handler):
        """Purchase a merit with experience."""
        if not self.args:
            self.caller.msg("Usage: +xp/buy <merit>=[dots]")
            return
        
        # Check if werewolf character is in a form that allows stat modification
        from commands.shapeshifting import can_modify_stats_while_shifted
        can_modify, reason = can_modify_stats_while_shifted(self.caller)
        if not can_modify:
            self.caller.msg(f"|r{reason}|n")
            return
            
        parts = self.args.split("=", 1)
        merit_name = parts[0].lower().replace(" ", "_")
        dots = 1
        
        if len(parts) > 1:
            try:
                dots = int(parts[1])
            except ValueError:
                self.caller.msg("Dots must be a number.")
                return
                
        # Find merit
        if merit_name not in merits_dict:
            self.caller.msg(f"Merit '{merit_name}' not found. Use +xp/list merits to see available merits.")
            return
            
        merit = merits_dict[merit_name]
        
        # Validate dots
        if dots < merit.min_value or dots > merit.max_value:
            self.caller.msg(f"{merit.name} must be between {merit.min_value} and {merit.max_value} dots.")
            return
            
        # Check if already have merit
        if not self.caller.db.stats:
            self.caller.db.stats = {
                "attributes": {},
                "skills": {},
                "advantages": {},
                "anchors": {},
                "bio": {},
                "merits": {},
                "other": {}
            }
            
        current_merits = self.caller.db.stats.get("merits", {})
        if merit_name in current_merits:
            self.caller.msg(f"You already have {merit.name}. Use +xp/spend to increase it.")
            return
            
        # Check prerequisites
        if merit.prerequisite and not self._check_prerequisites(merit.prerequisite):
            self.caller.msg(f"You don't meet the prerequisites for {merit.name}: {merit.prerequisite}")
            return
            
        # Calculate cost
        total_cost = dots  # 1 XP per dot for merits
        
        if exp_handler.experience < total_cost:
            self.caller.msg(f"Insufficient experience. Need {total_cost} XP, have {exp_handler.experience} XP.")
            return
            
        # Purchase merit
        exp_handler.spend_experience(total_cost)
        
        # Log the XP expenditure
        from world.xp_logger import get_xp_logger
        logger = get_xp_logger(self.caller)
        logger.log_experience(-total_cost, f"Merit: {merit.name} ({dots} dots)")
        
        current_merits[merit_name] = {
            "dots": dots,
            "max_dots": merit.max_value,
            "merit_type": merit.merit_type,
            "description": merit.description
        }
        self.caller.db.stats["merits"] = current_merits
        
        self.caller.msg(f"|gPurchased {merit.name} at {dots} dots for {total_cost} XP.|n")
        self.caller.msg(f"Remaining experience: {exp_handler.experience}")

    def _check_prerequisites(self, prerequisite_string):
        """Check if character meets prerequisites."""
        if not prerequisite_string:
            return True
            
        # Parse prerequisite string
        # Format: "attribute:value", "skill:value", "[option1,option2]", "[req1 and req2]"
        prereqs = prerequisite_string.split(",")
        
        for prereq in prereqs:
            prereq = prereq.strip()
            
            # Handle OR requirements [option1,option2]
            if prereq.startswith("[") and prereq.endswith("]"):
                or_options = prereq[1:-1].split(",")
                or_met = False
                for option in or_options:
                    if self._check_single_prerequisite(option.strip()):
                        or_met = True
                        break
                if not or_met:
                    return False
            else:
                if not self._check_single_prerequisite(prereq):
                    return False
                    
        return True
        
    def _check_single_prerequisite(self, prereq):
        """Check a single prerequisite requirement."""
        prereq = prereq.strip()
        stats = self.caller.db.stats or {}
        
        # Handle template-based prerequisites (no colon)
        if ":" not in prereq:
            current_template = stats.get("other", {}).get("template", "Mortal").lower()
            
            # Handle negative prerequisites (non_template)
            if prereq.startswith("non_"):
                required_template = prereq[4:]  # Remove "non_" prefix
                return current_template != required_template
            
            # Handle template checks
            if prereq in ["mummy", "vampire", "mage", "werewolf", "changeling", "hunter", 
                         "beast", "demon", "deviant", "geist", "promethean", "mortal", "mortal+"]:
                return current_template == prereq
                
            # If not a known template prerequisite, return False
            return False
            
        # Handle stat:value prerequisites
        stat_name, required_value = prereq.split(":", 1)
        stat_name = stat_name.strip().lower()
        
        try:
            required_value = int(required_value.strip())
        except ValueError:
            return False
        
        # Handle generic "skill" prerequisite - check for ANY skill at required level
        if stat_name == "skill":
            skills = stats.get("skills", {})
            for skill_value in skills.values():
                if skill_value >= required_value:
                    return True
            return False
        
        # Handle generic "specialty" prerequisite - check for ANY specialty
        if stat_name == "specialty":
            specialties = stats.get("specialties", {})
            total_specialties = sum(len(spec_list) for spec_list in specialties.values())
            return total_specialties >= required_value
            
        # Check attributes
        current_value = stats.get("attributes", {}).get(stat_name, 1)
        if current_value >= required_value:
            return True
            
        # Check skills
        current_value = stats.get("skills", {}).get(stat_name, 0)
        if current_value >= required_value:
            return True
            
        # Check merits
        current_value = stats.get("merits", {}).get(stat_name, {}).get("dots", 0)
        if current_value >= required_value:
            return True
            
        return False

    def refund_merit(self, exp_handler):
        """Refund a merit for experience (staff only)."""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can refund merits.")
            return
            
        merit_name = self.args.strip().lower().replace(" ", "_")
        if not merit_name:
            self.caller.msg("Usage: +xp/refund <merit>")
            return
            
        current_merits = self.caller.db.stats.get("merits", {})
        if merit_name not in current_merits:
            self.caller.msg(f"You don't have the merit '{merit_name}'.")
            return
            
        merit_data = current_merits[merit_name]
        refund_amount = merit_data["dots"]
        
        # Remove merit and refund experience
        del current_merits[merit_name]
        exp_handler.add_experience(refund_amount)
        
        # Log the XP refund
        from world.xp_logger import get_xp_logger
        logger = get_xp_logger(self.caller)
        logger.log_experience(refund_amount, f"Merit Refund: {merit_name.replace('_', ' ').title()} ({refund_amount} dots)")
        
        self.caller.msg(f"|gRefunded {merit_name.replace('_', ' ').title()} for {refund_amount} XP.|n")
        self.caller.msg(f"Current experience: {exp_handler.experience}")

    def list_merits(self):
        """List available merits by category."""
        category = self.args.strip().lower()
        
        if category and category not in ["mental", "physical", "social", "fighting", "style", "supernatural"]:
            self.caller.msg("Valid categories: mental, physical, social, fighting, style, supernatural")
            return
            
        output = []
        output.append("|wAvailable Merits|n")
        output.append("=" * 50)
        
        # Group merits by category
        merit_categories = {}
        for merit in all_merits:
            if not category or merit.merit_type == category:
                if merit.merit_type not in merit_categories:
                    merit_categories[merit.merit_type] = []
                merit_categories[merit.merit_type].append(merit)
                
        # Display merits
        for cat_name in ["mental", "physical", "social", "fighting", "style", "supernatural"]:
            if cat_name in merit_categories:
                output.append(f"\n|c{cat_name.title()} Merits:|n")
                for merit in sorted(merit_categories[cat_name], key=lambda x: x.name):
                    dots_str = f"{merit.min_value}" if merit.min_value == merit.max_value else f"{merit.min_value}-{merit.max_value}"
                    prereq_str = f" (Prereq: {merit.prerequisite})" if merit.prerequisite else ""
                    output.append(f"  {merit.name} ({dots_str} dots){prereq_str}")
                    output.append(f"    {merit.description}")
                    
        if not merit_categories:
            output.append("No merits found for the specified category.")
            
        self.caller.msg("\n".join(output))

    def merit_info(self):
        """Show detailed information about a specific merit."""
        merit_name = self.args.strip().lower().replace(" ", "_")
        if not merit_name:
            self.caller.msg("Usage: +xp/info <merit>")
            return
            
        if merit_name not in merits_dict:
            self.caller.msg(f"Merit '{merit_name}' not found. Use +xp/list merits to see available merits.")
            return
            
        merit = merits_dict[merit_name]
        
        output = []
        output.append(f"|w{merit.name}|n")
        output.append("-" * len(merit.name))
        output.append(f"Type: |c{merit.merit_type.title()}|n")
        
        if merit.min_value == merit.max_value:
            output.append(f"Dots: |y{merit.min_value}|n")
        else:
            output.append(f"Dots: |y{merit.min_value}-{merit.max_value}|n")
            
        output.append(f"Cost: |y{merit.min_value if merit.min_value == merit.max_value else f'{merit.min_value}-{merit.max_value}'} XP|n")
        
        if merit.prerequisite:
            output.append(f"Prerequisites: |r{merit.prerequisite}|n")
            
        output.append(f"\nDescription:")
        output.append(merit.description)
        
        self.caller.msg("\n".join(output))

    def spend_arcane_experience(self, exp_handler):
        """Spend arcane experience on mage-specific abilities."""
        # Check if character is a Mage
        character_template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() not in ["mage", "legacy_mage"]:
            self.caller.msg("|rOnly Mages can spend Arcane Experience.|n")
            self.caller.msg(f"Your template is: {character_template}")
            return
        
        if "=" not in self.args:
            self.caller.msg("Usage: +xp/spend/arcane <stat>=<dots>")
            return
            
        stat_name, target_dots_str = self.args.split("=", 1)
        stat_name = stat_name.strip().lower()
        
        # Handle different arcane expenditures
        if stat_name == "praxis":
            # Praxis requires a spell name, not dots
            self.caller.msg("To buy a praxis, use: +stat/mage praxis=<spell_name>")
            self.caller.msg("Praxis cost: 1 Arcane XP (must use Arcane XP)")
            return
        elif stat_name in ["wisdom", "integrity"]:
            # Wisdom costs arcane XP
            try:
                target_dots = int(target_dots_str.strip())
            except ValueError:
                self.caller.msg("Target dots must be a number.")
                return
            
            current_dots = self.caller.db.stats.get("other", {}).get("integrity", 7)
            
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Wisdom at {current_dots} dots or higher.")
                return
            
            if target_dots > 10:
                self.caller.msg("Wisdom cannot exceed 10 dots.")
                return
            
            # Calculate cost (2 Arcane XP per dot)
            dots_to_buy = target_dots - current_dots
            total_cost = dots_to_buy * 2
            
            if exp_handler.arcane_experience < total_cost:
                self.caller.msg(f"Insufficient arcane experience. Need {total_cost} Arcane XP, have {exp_handler.arcane_experience} Arcane XP.")
                return
            
            # Spend arcane experience and update stat
            exp_handler.spend_arcane_experience(total_cost)
            self.caller.db.stats["other"]["integrity"] = target_dots
            
            # Log the arcane XP expenditure
            from world.xp_logger import get_xp_logger
            logger = get_xp_logger(self.caller)
            logger.log_change('arcane_experience', -total_cost, f"Wisdom: {current_dots} > {target_dots}")
            
            self.caller.msg(f"|gSpent {total_cost} Arcane XP to raise Wisdom to {target_dots} dots.|n")
            self.caller.msg(f"Remaining arcane experience: {exp_handler.arcane_experience}")
            
        elif stat_name == "gnosis":
            # Gnosis can use either regular XP or Arcane XP (5 per dot)
            try:
                target_dots = int(target_dots_str.strip())
            except ValueError:
                self.caller.msg("Target dots must be a number.")
                return
            
            current_dots = self.caller.db.stats.get("advantages", {}).get("gnosis", 1)
            
            if target_dots <= current_dots:
                self.caller.msg(f"You already have Gnosis at {current_dots} dots or higher.")
                return
            
            if target_dots > 10:
                self.caller.msg("Gnosis cannot exceed 10 dots.")
                return
            
            # Calculate cost (5 Arcane XP per dot)
            dots_to_buy = target_dots - current_dots
            total_cost = dots_to_buy * 5
            
            if exp_handler.arcane_experience < total_cost:
                self.caller.msg(f"Insufficient arcane experience. Need {total_cost} Arcane XP, have {exp_handler.arcane_experience} Arcane XP.")
                return
            
            # Spend arcane experience and update stat
            exp_handler.spend_arcane_experience(total_cost)
            self.caller.db.stats["advantages"]["gnosis"] = target_dots
            
            # Log the arcane XP expenditure
            from world.xp_logger import get_xp_logger
            logger = get_xp_logger(self.caller)
            logger.log_change('arcane_experience', -total_cost, f"Gnosis: {current_dots} > {target_dots}")
            
            self.caller.msg(f"|gSpent {total_cost} Arcane XP to raise Gnosis to {target_dots} dots.|n")
            self.caller.msg(f"Remaining arcane experience: {exp_handler.arcane_experience}")
            self.caller.msg(f"|mNote:|n You gained 1 free praxis with this Gnosis increase!")
            
        else:
            # Check if it's an arcana
            from world.cofd.templates.mage import MAGE_ARCANA
            
            # Map common names to proper arcana names
            arcana_mapping = {
                "death": "arcanum_death",
                "fate": "fate",
                "forces": "forces",
                "life": "life",
                "matter": "matter",
                "mind": "mind",
                "prime": "prime",
                "space": "space",
                "spirit": "spirit",
                "time": "time"
            }
            
            if stat_name in arcana_mapping:
                arcana_name = arcana_mapping[stat_name]
            elif stat_name in MAGE_ARCANA:
                arcana_name = stat_name
            else:
                self.caller.msg(f"'{stat_name}' is not a valid mage ability that can be purchased with Arcane XP.")
                self.caller.msg("Valid options: arcana (death, fate, forces, life, matter, mind, prime, space, spirit, time), gnosis, wisdom")
                return
            
            try:
                target_dots = int(target_dots_str.strip())
            except ValueError:
                self.caller.msg("Target dots must be a number.")
                return
            
            current_dots = self.caller.db.stats.get("powers", {}).get(arcana_name, 0)
            
            if target_dots <= current_dots:
                self.caller.msg(f"You already have {arcana_name.replace('arcanum_', '').title()} at {current_dots} dots or higher.")
                return
            
            if target_dots > 5:
                self.caller.msg("Arcana cannot exceed 5 dots.")
                return
            
            # Determine gnosis limit for arcana
            gnosis = self.caller.db.stats.get("advantages", {}).get("gnosis", 1)
            arcana_limit = gnosis + 5  # Ruling arcana can go to Gnosis + 5
            
            # Calculate cost (4 Arcane XP per dot to limit, 5 per dot above limit)
            dots_to_buy = target_dots - current_dots
            total_cost = 0
            
            for dot in range(current_dots + 1, target_dots + 1):
                if dot <= arcana_limit:
                    total_cost += 4
                else:
                    total_cost += 5
            
            if exp_handler.arcane_experience < total_cost:
                self.caller.msg(f"Insufficient arcane experience. Need {total_cost} Arcane XP, have {exp_handler.arcane_experience} Arcane XP.")
                return
            
            # Spend arcane experience and update stat
            exp_handler.spend_arcane_experience(total_cost)
            
            if "powers" not in self.caller.db.stats:
                self.caller.db.stats["powers"] = {}
            
            self.caller.db.stats["powers"][arcana_name] = target_dots
            
            # Log the arcane XP expenditure
            from world.xp_logger import get_xp_logger
            logger = get_xp_logger(self.caller)
            display_name = arcana_name.replace("arcanum_", "").replace("_", " ").title()
            logger.log_change('arcane_experience', -total_cost, f"{display_name}: {current_dots} > {target_dots}")
            
            self.caller.msg(f"|gSpent {total_cost} Arcane XP to raise {display_name} to {target_dots} dots.|n")
            self.caller.msg(f"Remaining arcane experience: {exp_handler.arcane_experience}")
    
    def show_costs(self):
        """Show experience point costs for character's template."""
        from world.xp_costs import (
            GENERAL_COSTS, WEREWOLF_COSTS, VAMPIRE_COSTS, MAGE_COSTS,
            CHANGELING_COSTS, DEMON_COSTS, GEIST_COSTS, HUNTER_COSTS,
            DEVIANT_COSTS, PROMETHEAN_COSTS, MUMMY_COSTS,
            get_werewolf_affinity_gifts, get_vampire_clan_disciplines,
            get_geist_affinity_haunts, get_mage_arcanum_type
        )
        
        stats = self.caller.db.stats
        template = stats.get("other", {}).get("template", "Mortal").lower()
        
        output = []
        output.append("|y" + "=" * 78 + "|n")
        output.append("|y" + "EXPERIENCE POINT COSTS".center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        # General costs (all templates)
        output.append("|wGENERAL COSTS (All Templates)|n")
        output.append("-" * 78)
        output.append(f"Attributes:        |y{GENERAL_COSTS['attribute']} XP|n per dot")
        output.append(f"Skills:            |y{GENERAL_COSTS['skill']} XP|n per dot")
        output.append(f"Merits:            |y{GENERAL_COSTS['merit']} XP|n per dot")
        output.append(f"Skill Specialty:   |y{GENERAL_COSTS['skill_specialty']} XP|n each")
        output.append(f"Integrity:         |y{GENERAL_COSTS['integrity']} XP|n per dot")
        output.append(f"Lost Willpower:    |y{GENERAL_COSTS['lost_willpower']} XP|n per dot restored")
        output.append("")
        
        # Template-specific costs
        if template == 'werewolf':
            output.append("|wWEREWOLF COSTS|n")
            output.append("-" * 78)
            output.append(f"Affinity Gift:     |y{WEREWOLF_COSTS['affinity_gift']} XP|n")
            output.append(f"Non-Affinity Gift: |y{WEREWOLF_COSTS['non_affinity_gift']} XP|n")
            output.append(f"Renown:            |y{WEREWOLF_COSTS['renown']} XP|n per dot")
            output.append(f"Rite:              |y{WEREWOLF_COSTS['rite']} XP|n")
            output.append(f"Primal Urge:       |y{WEREWOLF_COSTS['primal_urge']} XP|n per dot")
            output.append("")
            # Show affinity gifts
            affinity_gifts = get_werewolf_affinity_gifts(self.caller)
            if affinity_gifts:
                output.append("|cYour Affinity Gifts:|n")
                output.append(", ".join([g.replace('_', ' ').title() for g in affinity_gifts]))
                output.append("")
        
        elif template == 'vampire':
            output.append("|wVAMPIRE COSTS|n")
            output.append("-" * 78)
            output.append(f"Clan Discipline:   |y{VAMPIRE_COSTS['clan_discipline']} XP|n per dot")
            output.append(f"Out-of-Clan Disc.: |y{VAMPIRE_COSTS['out_of_clan_discipline']} XP|n per dot")
            output.append(f"Cruac:             |y{VAMPIRE_COSTS['cruac']} XP|n per dot")
            output.append(f"Theban Sorcery:    |y{VAMPIRE_COSTS['theban_sorcery']} XP|n per dot")
            output.append(f"Blood Ritual:      |y{VAMPIRE_COSTS['blood_ritual']} XP|n")
            output.append(f"Humanity:          |y{VAMPIRE_COSTS['humanity']} XP|n per dot")
            output.append(f"Blood Potency:     |y{VAMPIRE_COSTS['blood_potency']} XP|n per dot")
            output.append("")
            # Show clan disciplines
            clan_disciplines = get_vampire_clan_disciplines(self.caller)
            if clan_disciplines:
                output.append("|cYour In-Clan Disciplines:|n")
                output.append(", ".join([d.replace('_', ' ').title() for d in clan_disciplines]))
                output.append("")
        
        elif template == 'mage':
            output.append("|wMAGE COSTS|n")
            output.append("-" * 78)
            output.append(f"Arcanum (to limit):  |m{MAGE_COSTS['arcanum_to_limit']} XP|n per dot (normal or arcane)")
            output.append(f"Arcanum (above):     |m{MAGE_COSTS['arcanum_above_limit']} XP|n per dot (normal only)")
            output.append(f"Gnosis:              |m{MAGE_COSTS['gnosis']} XP|n per dot (normal or arcane)")
            output.append(f"Rote:                |m{MAGE_COSTS['rote']} XP|n (normal or arcane)")
            output.append(f"Praxis:              |M{MAGE_COSTS['praxis']} Arcane XP|n (arcane only)")
            output.append(f"Wisdom:              |M{MAGE_COSTS['wisdom']} Arcane XP|n per dot (arcane only)")
            output.append("")
            output.append("|cArcanum Limits:|n")
            output.append("Ruling: 5 dots, Common: 4 dots, Inferior: 2 dots")
            output.append("Use +xp/costs/arcane for more details")
            output.append("")
        
        elif template == 'changeling':
            output.append("|wCHANGELING COSTS|n")
            output.append("-" * 78)
            output.append(f"Common Contract:        |y{CHANGELING_COSTS['common_contract']} XP|n")
            output.append(f"Royal Contract:         |y{CHANGELING_COSTS['royal_contract']} XP|n")
            output.append(f"Favored Common:         |y{CHANGELING_COSTS['favored_common_contract']} XP|n")
            output.append(f"Favored Royal:          |y{CHANGELING_COSTS['favored_royal_contract']} XP|n")
            output.append(f"Goblin Contract:        |y{CHANGELING_COSTS['goblin_contract']} XP|n")
            output.append(f"Out-of-Seeming Benefit: |y{CHANGELING_COSTS['out_of_seeming_benefit']} XP|n")
            output.append(f"Wyrd:                   |y{CHANGELING_COSTS['wyrd']} XP|n per dot")
            output.append("")
            # Show favored regalia
            from world.xp_costs import get_changeling_favored_regalia
            favored_regalia = get_changeling_favored_regalia(self.caller)
            if favored_regalia:
                output.append("|cYour Favored Regalia:|n")
                output.append(", ".join([r.title() for r in favored_regalia]))
                output.append("")
            else:
                output.append("|rNo favored regalia set.|n Use +stat to set kith and favored_regalia.")
                output.append("")
        
        elif template == 'geist':
            output.append("|wGEIST (SIN-EATER) COSTS|n")
            output.append("-" * 78)
            output.append(f"Affinity Haunt:     |y{GEIST_COSTS['affinity_haunt']} XP|n per dot")
            output.append(f"Non-Affinity Haunt: |y{GEIST_COSTS['non_affinity_haunt']} XP|n per dot")
            output.append(f"Ceremony:           |y{GEIST_COSTS['ceremony']} XP|n")
            output.append(f"Synergy:            |y{GEIST_COSTS['synergy']} XP|n per dot")
            output.append("")
            # Show affinity haunts
            affinity_haunts = get_geist_affinity_haunts(self.caller)
            if affinity_haunts:
                output.append("|cYour Affinity Haunts:|n")
                output.append(", ".join([h.replace('_', ' ').title() for h in affinity_haunts]))
                output.append("")
        
        elif template == 'demon':
            output.append("|wDEMON COSTS|n")
            output.append("-" * 78)
            output.append(f"Embed:   |y{DEMON_COSTS['embed']} XP|n")
            output.append(f"Exploit: |y{DEMON_COSTS['exploit']} XP|n")
            output.append(f"Primum:  |y{DEMON_COSTS['primum']} XP|n per dot")
            output.append(f"Cover:   |y{DEMON_COSTS['cover']} XP|n per dot")
            output.append("")
        
        elif template == 'hunter':
            output.append("|wHUNTER COSTS|n")
            output.append("-" * 78)
            output.append(f"Endowment: |y{HUNTER_COSTS['endowment']} XP|n")
            output.append("")
        
        elif template == 'deviant':
            output.append("|wDEVIANT COSTS|n")
            output.append("-" * 78)
            output.append(f"Variation:   |y{DEVIANT_COSTS['variation']} XP|n per dot")
            output.append(f"Acclimation: |y{DEVIANT_COSTS['acclimation']} XP|n")
            output.append("|xNote: New Variations must have an entangled Scar|n")
            output.append("")
        
        elif template == 'promethean':
            output.append("|wPROMETHEAN COSTS|n")
            output.append("-" * 78)
            output.append(f"Azoth (normal):     |y{PROMETHEAN_COSTS['azoth_normal']} XP|n per dot")
            output.append(f"Azoth (vitriol):    |g{PROMETHEAN_COSTS['azoth_vitriol']} Vitriol XP|n per dot")
            output.append(f"Pilgrimage:         |g{PROMETHEAN_COSTS['pilgrimage']} Vitriol XP|n (vitriol only)")
            output.append(f"Calcify Alembic:    |g{PROMETHEAN_COSTS['calcify_alembic']} Vitriol XP|n (vitriol only)")
            output.append(f"Create Athanor:     |g{PROMETHEAN_COSTS['create_athanor']} Vitriol XP|n (vitriol only)")
            output.append("")
        
        elif template == 'mummy':
            output.append("|wMUMMY COSTS|n")
            output.append("-" * 78)
            output.append(f"Affinity:          |y{MUMMY_COSTS['affinity']} XP|n")
            output.append(f"Utterance:         |y{MUMMY_COSTS['utterance']} XP|n")
            output.append(f"Defining Pillar:   |y{MUMMY_COSTS['defining_pillar']} XP|n per dot")
            output.append(f"Other Pillar:      |y{MUMMY_COSTS['other_pillar']} XP|n per dot")
            output.append(f"Memory:            |y{MUMMY_COSTS['memory']} Reminisce XP|n per dot (reminisce only)")
            output.append(f"Cult Attribute:    |y{MUMMY_COSTS['cult_attribute']} XP|n per dot")
            output.append(f"Cult Merit:        |y{MUMMY_COSTS['cult_merit']} XP|n per dot")
            output.append(f"Dominance:         |y{MUMMY_COSTS['dominance']} XP|n per dot")
            output.append("")
        
        elif template == 'mortal+':
            template_type = stats.get("bio", {}).get("template_type", "").lower()
            output.append(f"|wMORTAL+ COSTS ({template_type.upper()})|n")
            output.append("-" * 78)
            if template_type == 'dhampir':
                from world.xp_costs import DHAMPIR_COSTS
                output.append(f"Twist:             |y{DHAMPIR_COSTS['twist']} XP|n per dot")
                output.append(f"In-Clan Theme:     |y{DHAMPIR_COSTS['in_clan_theme']} XP|n per dot")
                output.append(f"Out-of-Clan Theme: |y{DHAMPIR_COSTS['out_of_clan_theme']} XP|n per dot")
                output.append(f"Malison:           |y{DHAMPIR_COSTS['malison']} XP|n")
            elif template_type in ['ghoul', 'revenant']:
                from world.xp_costs import GHOUL_COSTS
                output.append(f"Clan Discipline:   |y{GHOUL_COSTS['clan_discipline']} XP|n per dot")
                output.append(f"Out-of-Clan Disc.: |y{GHOUL_COSTS['out_of_clan_discipline']} XP|n per dot")
                output.append(f"Cruac:             |y{GHOUL_COSTS['cruac']} XP|n per dot")
                output.append(f"Theban Sorcery:    |y{GHOUL_COSTS['theban_sorcery']} XP|n per dot")
                output.append(f"Blood Ritual:      |y{GHOUL_COSTS['blood_ritual']} XP|n")
            elif template_type == 'proximi':
                from world.xp_costs import PROXIMI_COSTS
                output.append(f"Blessing:          |y{PROXIMI_COSTS['blessing']} XP|n per dot")
                output.append("|x(Max 30 total dots across all blessings)|n")
            elif template_type == 'fae_touched':
                from world.xp_costs import FAE_TOUCHED_COSTS, get_changeling_favored_regalia
                output.append(f"Common Contract:   |y{FAE_TOUCHED_COSTS['common_contract']} XP|n")
                output.append(f"Royal Contract:    |y{FAE_TOUCHED_COSTS['royal_contract']} XP|n")
                output.append(f"Favored Common:    |y{FAE_TOUCHED_COSTS['favored_common_contract']} XP|n")
                output.append(f"Favored Royal:     |y{FAE_TOUCHED_COSTS['favored_royal_contract']} XP|n")
                output.append(f"Goblin Contract:   |y{FAE_TOUCHED_COSTS['goblin_contract']} XP|n")
                output.append("")
                # Show favored regalia (uses same system as Changelings)
                favored_regalia = get_changeling_favored_regalia(self.caller)
                if favored_regalia:
                    output.append("|cYour Favored Regalia:|n")
                    output.append(", ".join([r.title() for r in favored_regalia]))
                else:
                    output.append("|rNo favored regalia set.|n Use +stat favored_regalia=<regalia>")
            else:
                output.append("See staff for template-specific costs.")
            output.append("")
        
        output.append("|gExamples:|n")
        output.append("  +xp/spend strength=4                  - Raise Strength")
        output.append("  +xp/spend unseen_sense:ghosts=2       - Buy instanced merit")
        output.append("  +xp/spend athletics_specialty=running - Add specialty")
        output.append("")
        output.append("|y" + "=" * 78 + "|n")
        
        self.caller.msg("\n".join(output))
    
    def show_arcane_costs(self):
        """Show arcane experience point costs (Mage-specific)."""
        # Check if character is a Mage
        character_template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() not in ["mage", "legacy_mage"]:
            self.caller.msg("|rOnly Mages have Arcane Experience costs.|n")
            self.caller.msg(f"Your template is: {character_template}")
            return
        
        output = []
        output.append("|mArcane Experience Costs (Mages Only)|n")
        output.append("=" * 50)
        output.append("")
        output.append("|wCan use EITHER Regular XP or Arcane XP:|n")
        output.append("  Arcanum (to limit):       |m4 XP|n per dot")
        output.append("  Arcanum (above limit):    |m5 XP|n per dot")
        output.append("  Gnosis:                   |m5 XP|n per dot")
        output.append("  Rote:                     |m1 XP|n")
        output.append("  Legacy Attainment (tutor):|m1 XP|n")
        output.append("")
        output.append("|wMUST use Arcane XP ONLY:|n")
        output.append("  Praxis:                   |M1 Arcane XP|n")
        output.append("  Wisdom:                   |M2 Arcane XP|n per dot")
        output.append("  Legacy Attainment (solo): |M1 Arcane XP|n")
        output.append("")
        output.append("|gNote:|n Increasing Gnosis grants 1 free Praxis")
        output.append("|gNote:|n Arcanum limit = Gnosis + 5 for ruling arcana")
        output.append("")
        output.append("Usage:")
        output.append("  |w+xp/spend/arcane <arcanum>=<dots>|n  - Raise an arcanum")
        output.append("  |w+xp/spend/arcane gnosis=<dots>|n     - Raise Gnosis")
        output.append("  |w+xp/spend/arcane wisdom=<dots>|n     - Raise Wisdom")
        output.append("  |w+stat/mage praxis=<spell_name>|n     - Learn a praxis (1 Arcane XP)")
        
        self.caller.msg("\n".join(output)) 