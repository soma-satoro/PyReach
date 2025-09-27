import re
from evennia import Command
from world.cofd.merits.general_merits import merits_dict, all_merits


class CmdExperience(Command):
    """
    Manage your character's experience points and beats.

    Usage:
        +xp                              - Show your current experience and beats
        +xp/beat <source>               - Add a beat from a valid source
        +xp/spend <stat>=<dots>         - Spend experience on attributes/skills
        +xp/buy <merit>=[dots]          - Purchase a merit with experience
        +xp/refund <merit>              - Refund a merit for experience (staff only)
        +xp/list merits [category]      - List available merits by category
        +xp/info <merit>                - Show detailed merit information
        +xp/costs                       - Show experience point costs

    Merit Categories:
        mental, physical, social, fighting, style, supernatural

    Valid beat sources:
        dramatic_failure, exceptional_success, conditions, aspirations,
        story, scene, session, roleplay, challenge, sacrifice,
        discovery, relationship, consequence, learning, growth
        
    Note: Exceptional successes and dramatic failures from dice rolls 
    automatically award beats - no need to manually request them.

    Experience Costs:
        Attributes: 4 XP per dot
        Skills: 2 XP per dot  
        Merits: 1 XP per dot
        Integrity: 2 XP per dot
        Specialties: 1 XP each

    Examples:
        +xp/buy contacts=3              - Buy Contacts merit at 3 dots
        +xp/spend strength=4            - Raise Strength to 4 dots
        +xp/list merits mental          - List mental merits
        +xp/info fast_reflexes          - Show Fast Reflexes merit details
    """
    key = "+xp"
    aliases = ["+experience", "+beat"]
    help_category = "Character Sheets and Development"

    def parse(self):
        """Parse the command line."""
        # Handle switches
        if "/" in self.args:
            if self.args.startswith("/"):
                self.switch = self.args[1:].split(" ")[0]
                self.remaining_args = " ".join(self.args.split(" ")[1:])
            else:
                parts = self.args.split("/", 1)
                self.switch = parts[1].split(" ")[0] if len(parts) > 1 else ""
                self.remaining_args = " ".join(parts[1].split(" ")[1:]) if len(parts) > 1 else ""
        else:
            self.switch = ""
            self.remaining_args = self.args.strip()

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

        if not self.switch:
            self.show_experience(exp_handler)
        elif self.switch == "beat":
            if legacy_mode:
                self.caller.msg("|rBeats system is disabled in Legacy Mode.|n")
                self.caller.msg("Experience is awarded directly. Use +xp/award for staff awards.")
            else:
                self.add_beat(exp_handler)
        elif self.switch == "spend":
            self.spend_experience(exp_handler)
        elif self.switch == "buy":
            self.buy_merit(exp_handler)
        elif self.switch == "refund":
            self.refund_merit(exp_handler)
        elif self.switch == "list":
            self.list_merits()
        elif self.switch == "info":
            self.merit_info()
        elif self.switch == "costs":
            self.show_costs()
        else:
            self.caller.msg("Unknown switch. See 'help +xp' for usage.")

    def show_experience(self, exp_handler):
        """Show current experience and beats."""
        from commands.CmdLegacy import is_legacy_mode
        legacy_mode = is_legacy_mode()
        
        output = []
        output.append("|wExperience Summary|n")
        output.append("-" * 40)
        
        if legacy_mode:
            # Legacy mode - show only experience points
            output.append(f"Experience Points: |y{exp_handler.experience}|n")
            output.append("|cLegacy Mode:|n Experience awarded directly, no beats system")
        else:
            # Modern mode - show beats and experience
            fractional_beats = self.caller.attributes.get('fractional_beats', default=0.0)
            if fractional_beats > 0:
                output.append(f"Beats: |c{exp_handler.beats}|n + |c{fractional_beats:.1f}|n fractional = |c{exp_handler.total_beats:.1f}|n total")
            else:
                output.append(f"Beats: |c{exp_handler.beats}|n")
                
            output.append(f"Experience Points: |y{exp_handler.experience}|n")
            output.append(f"(5 beats = 1 experience point)")
        
        self.caller.msg("\n".join(output))

    def add_beat(self, exp_handler):
        """Add a beat from a valid source."""
        valid_sources = [
            "dramatic_failure", "exceptional_success", "conditions", "aspirations",
            "story", "scene", "session", "roleplay", "challenge", "sacrifice",
            "discovery", "relationship", "consequence", "learning", "growth"
        ]
        
        source = self.remaining_args.strip().lower().replace(" ", "_")
        if not source:
            self.caller.msg("You must specify a beat source. Valid sources: " + ", ".join(valid_sources))
            return
            
        if source not in valid_sources:
            self.caller.msg(f"Invalid beat source '{source}'. Valid sources: " + ", ".join(valid_sources))
            return
            
        exp_handler.add_beat()
        self.caller.msg(f"|gAdded 1 beat from '{source.replace('_', ' ')}'.|n")
        self.caller.msg(f"Current beats: {exp_handler.beats}, Experience: {exp_handler.experience}")

    def spend_experience(self, exp_handler):
        """Spend experience on attributes, skills, etc."""
        if "=" not in self.remaining_args:
            self.caller.msg("Usage: +xp/spend <stat>=<dots>")
            return
            
        stat_name, target_dots_str = self.remaining_args.split("=", 1)
        stat_name = stat_name.strip().lower()
        
        try:
            target_dots = int(target_dots_str.strip())
        except ValueError:
            self.caller.msg("Target dots must be a number.")
            return
            
        # Initialize stats if needed
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
            
        stats = self.caller.db.stats
        
        # Determine stat category and get current value
        current_dots = 0
        stat_category = None
        cost_per_dot = 0
        max_dots = 5
        
        # Check attributes
        from world.cofd.models import ATTRIBUTES
        for category, attr_list in ATTRIBUTES.items():
            attr_names = [attr.name.lower() for attr in attr_list]
            if stat_name in attr_names:
                stat_category = "attributes"
                current_dots = stats["attributes"].get(stat_name, 1)
                cost_per_dot = 4
                break
                
        # Check skills
        if not stat_category:
            from world.cofd.models import SKILLS
            for category, skill_list in SKILLS.items():
                skill_names = [skill.name.lower() for skill in skill_list]
                if stat_name in skill_names:
                    stat_category = "skills"
                    current_dots = stats["skills"].get(stat_name, 0)
                    cost_per_dot = 2
                    break
                    
        # Check integrity
        if not stat_category and stat_name == "integrity":
            stat_category = "other"
            current_dots = stats["other"].get("integrity", 7)
            cost_per_dot = 2
            max_dots = 10
            
        if not stat_category:
            self.caller.msg(f"Unknown stat '{stat_name}'. Use attributes, skills, or integrity.")
            return
            
        if target_dots <= current_dots:
            self.caller.msg(f"You already have {stat_name} at {current_dots} dots or higher.")
            return
            
        if target_dots > max_dots:
            self.caller.msg(f"{stat_name.title()} cannot exceed {max_dots} dots.")
            return
            
        # Calculate cost
        dots_to_buy = target_dots - current_dots
        total_cost = dots_to_buy * cost_per_dot
        
        if exp_handler.experience < total_cost:
            self.caller.msg(f"Insufficient experience. Need {total_cost} XP, have {exp_handler.experience} XP.")
            return
            
        # Spend experience and update stat
        exp_handler.spend_experience(total_cost)
        stats[stat_category][stat_name] = target_dots
        
        self.caller.msg(f"|gSpent {total_cost} XP to raise {stat_name.title()} to {target_dots} dots.|n")
        self.caller.msg(f"Remaining experience: {exp_handler.experience}")

    def buy_merit(self, exp_handler):
        """Purchase a merit with experience."""
        if not self.remaining_args:
            self.caller.msg("Usage: +xp/buy <merit>=[dots]")
            return
            
        parts = self.remaining_args.split("=", 1)
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
            
        merit_name = self.remaining_args.strip().lower().replace(" ", "_")
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
        
        self.caller.msg(f"|gRefunded {merit_name.replace('_', ' ').title()} for {refund_amount} XP.|n")
        self.caller.msg(f"Current experience: {exp_handler.experience}")

    def list_merits(self):
        """List available merits by category."""
        category = self.remaining_args.strip().lower()
        
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
        merit_name = self.remaining_args.strip().lower().replace(" ", "_")
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

    def show_costs(self):
        """Show experience point costs."""
        output = []
        output.append("|wExperience Point Costs|n")
        output.append("=" * 30)
        output.append("Attributes: |y4 XP|n per dot")
        output.append("Skills: |y2 XP|n per dot")
        output.append("Merits: |y1 XP|n per dot")
        output.append("Integrity: |y2 XP|n per dot")
        output.append("Specialties: |y1 XP|n each")
        output.append("\nUse |w+xp/list merits|n to see available merits")
        output.append("Use |w+xp/info <merit>|n for merit details")
        
        self.caller.msg("\n".join(output)) 