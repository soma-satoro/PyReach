"""
Chronicles of Darkness dice rolling system.
Implements the standard CoD dice pool mechanics with 10-sided dice.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.utils import inherits_from
from evennia.utils.evmenu import EvMenu
from world.conditions import STANDARD_CONDITIONS, Condition
from world.utils.dice_utils import roll_dice, interpret_roll_results, roll_to_job_display, roll_to_room_display, format_roll_display, RollType
from django.utils import timezone

class CmdRoll(MuxCommand):
    """
    Roll dice for Chronicles of Darkness system.
    
    Usage:
      +roll[/switches] <stat> + <skill> [+/- modifier]
                            [vs player:stat+skill or vs <value>]

    Switches (Multiple switches can be combined):
      /8 - 8-again, /9 - 9-again, /rote - Reroll all failed dice once
      /reflex and /damage - No wound penalties apply
      /job - Roll to a job (uses expansive format, adds to job comments)
      /secret - Hide skill/stat details from room observers
      /specialty - Use specialty bonus (+1 die if character has specialty)

    VS Rolls and /oppose rolls (Resisted/Contested):
      VS rolls subtract dice from your pool based on opponent's stats or a
      static value.
      Opposed rolls make both parties roll and compare successes.
      Both roller and target see full details.

    /extended switch:
      Extended actions require multiple rolls to accumulate successes toward a goal.
      Maximum rolls is automatically calculated as Attribute + Skill (+ 2 if Patient merit).
      Format: +roll/extended <stat> + <skill>=<target> [rolls:<max>]
      +roll/extended intelligence + academics=10 (auto-calculates max rolls)
      +roll/extended intelligence + academics=10 rolls:3 (only 3 rolls max)
      +roll/extended/9 wits + investigation=15 (9-again, auto-calculates max)
    """
    
    key = "+roll"
    aliases = ["roll"]
    help_category = "Skill and Condition Checks"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
        
        args = self.args.strip()
        self.dice_pool = 0
        self.modifier = 0
        self.roll_type = None  # 'stat_skill', 'direct', 'stat_skill_mod', 'job'
        self.roll_types = set()
        self.job_id = None
        self.is_job_roll = False
        self.is_opposed = False
        self.is_secret = False
        self.is_extended = False
        self.is_specialty = False
        self.stat_name = None
        self.skill_name = None
        self.vs_target = None
        self.vs_target_char = None
        self.vs_stats = []
        self.vs_modifier = 0
        self.vs_value = 0
        self.extended_target = 0  # Target successes for extended rolls
        self.extended_max_rolls = 0  # Max number of rolls for extended action
        
        # Parse switches
        if self.switches:
            for switch in self.switches:
                if switch == "8":
                    self.roll_types.add(RollType.EIGHT_AGAIN)
                elif switch == "9":
                    self.roll_types.add(RollType.NINE_AGAIN)
                elif switch == "10":
                    self.roll_types.add(RollType.TEN_AGAIN)
                elif switch == "rote":
                    self.roll_types.add(RollType.ROTE)
                elif switch == "reflex":
                    self.roll_types.add(RollType.REFLEXIVE)
                elif switch == "damage":
                    self.roll_types.add(RollType.DAMAGE)
                elif switch == "job":
                    self.is_job_roll = True
                elif switch == "opposed":
                    self.is_opposed = True
                elif switch == "secret":
                    self.is_secret = True
                elif switch == "extended":
                    self.is_extended = True
                elif switch == "specialty":
                    self.is_specialty = True
        
        # If no roll types specified, use normal (10-again)
        if not self.roll_types:
            self.roll_types = {RollType.NORMAL}
        
        # Check for extended roll syntax
        import re
        if self.is_extended:
            # Extended format: <stat> + <skill>=<target> [rolls:<max>]
            # Example: intelligence + academics=10 (auto-calculates max rolls)
            # Example: intelligence + academics=10 rolls:5 (specifies max 5 rolls)
            extended_match = re.search(r'rolls:(\d+)', args, re.IGNORECASE)
            if extended_match:
                self.extended_max_rolls = int(extended_match.group(1))
                # Remove the rolls:X part from args
                args = args[:extended_match.start()].strip()
            else:
                # Will auto-calculate based on attribute + skill (+ 2 if Patient)
                self.extended_max_rolls = 0
            
            # Now check for target successes (should be in format: stat+skill=target)
            if "=" not in args:
                self.caller.msg("Extended rolls require a target. Example: +roll/extended intelligence + academics=10")
                return
            
            dice_part, target_part = args.split("=", 1)
            try:
                self.extended_target = int(target_part.strip())
            except ValueError:
                self.caller.msg("Invalid target successes specified.")
                return
            
            if self.extended_target < 5:
                self.caller.msg("Extended actions should have a target of at least 5 successes.")
                return
            
            # Continue parsing the dice part
            args = dice_part.strip()
        
        # Check for VS syntax (case insensitive)
        vs_match = re.search(r'\s+vs\s+', args, re.IGNORECASE)
        
        if vs_match:
            # Split on the VS keyword
            dice_part = args[:vs_match.start()].strip()
            vs_part = args[vs_match.end():].strip()
            
            # Parse the VS part
            if not self._parse_vs_expression(vs_part):
                return
            
            # Handle job rolls with VS
            if self.is_job_roll and "=" in dice_part:
                job_dice, job_id = dice_part.split("=", 1)
                try:
                    self.job_id = int(job_id.strip())
                except ValueError:
                    self.caller.msg("Invalid job ID specified.")
                    return
                self._parse_dice_expression(job_dice.strip(), is_job=True)
            else:
                self._parse_dice_expression(dice_part, is_job=self.is_job_roll)
        else:
            # Handle job rolls specially
            if self.is_job_roll and "=" in args:
                dice_part, job_part = args.split("=", 1)
                dice_part = dice_part.strip()
                job_part = job_part.strip()
                
                try:
                    self.job_id = int(job_part)
                except ValueError:
                    self.caller.msg("Invalid job ID specified.")
                    return
                
                # Parse the dice part using the enhanced parsing
                self._parse_dice_expression(dice_part, is_job=True)
            else:
                # Regular roll parsing
                if self.is_job_roll:
                    self.caller.msg("Job rolls require a job ID. Use: +roll/job <dice>=<job_id>")
                    return
                    
                self._parse_dice_expression(args, is_job=False)
    
    def _parse_dice_expression(self, expression, is_job=False):
        """
        Enhanced parsing for dice expressions that handles various modifier formats.
        
        Supports formats like:
        - "5" (direct dice)
        - "strength + weaponry" (stat + skill)
        - "strength + weaponry + 3" (stat + skill + modifier)
        - "strength + weaponry - 2" (stat + skill - modifier)
        - "strength+weaponry-2" (compact format)
        """
        expression = expression.strip()
        
        # First, try to parse as a single number (direct dice)
        try:
            self.dice_pool = int(expression)
            self.roll_type = 'job_direct' if is_job else 'direct'
            return
        except ValueError:
            pass
        
        # Split on + to get main parts
        parts = [part.strip() for part in expression.split("+")]
        
        if len(parts) == 1:
            # Could be a stat name with attached modifier (e.g., "strength-2")
            part = parts[0]
            stat, modifier = self._extract_modifier_from_part(part)
            if modifier is not None:
                # Single stat with modifier - this is unusual but we'll handle it
                stat_value = self.get_stat_value(stat.lower())
                if stat_value is None:
                    self.caller.msg(f"You don't have the attribute '{stat}' set.")
                    return
                self.dice_pool = stat_value
                self.modifier = modifier
                self.stat_name = stat
                self.roll_type = 'job_stat_mod' if is_job else 'stat_mod'
            else:
                self.caller.msg("Invalid roll format. See help for usage.")
            return
            
        elif len(parts) == 2:
            # Could be "stat + skill" or "stat + skill-modifier"
            stat = parts[0].lower()
            skill_part = parts[1]
            
            # Check if the skill part has an attached modifier
            skill, modifier = self._extract_modifier_from_part(skill_part)
            
            # Get stat and skill values
            stat_value = self.get_stat_value(stat)
            skill_value = self.get_stat_value(skill.lower())
            
            if stat_value is None:
                self.caller.msg(f"You don't have the attribute '{stat}' set.")
                return
            if skill_value is None:
                self.caller.msg(f"You don't have the skill '{skill}' set.")
                return
                
            self.dice_pool = stat_value + skill_value
            self.modifier = modifier if modifier is not None else 0
            self.stat_name = stat
            self.skill_name = skill
            
            if modifier is not None:
                self.roll_type = 'job_stat_skill_mod' if is_job else 'stat_skill_mod'
            else:
                self.roll_type = 'job_stat_skill' if is_job else 'stat_skill'
            
        elif len(parts) == 3:
            # "stat + skill + modifier" format
            stat = parts[0].lower()
            skill = parts[1].lower()
            modifier_part = parts[2]
            
            try:
                modifier = int(modifier_part)
            except ValueError:
                self.caller.msg("Invalid modifier specified.")
                return
                
            # Get stat and skill values
            stat_value = self.get_stat_value(stat)
            skill_value = self.get_stat_value(skill)
            
            if stat_value is None:
                self.caller.msg(f"You don't have the attribute '{stat}' set.")
                return
            if skill_value is None:
                self.caller.msg(f"You don't have the skill '{skill}' set.")
                return
                
            self.dice_pool = stat_value + skill_value
            self.modifier = modifier
            self.stat_name = stat
            self.skill_name = skill
            self.roll_type = 'job_stat_skill_mod' if is_job else 'stat_skill_mod'
            
        else:
            self.caller.msg("Invalid roll format. See help for usage.")
            return
    
    def _extract_modifier_from_part(self, part):
        """
        Extract modifier from a part like 'empathy-5' or 'empathy - 5'.
        Returns (skill_name, modifier) or (skill_name, None) if no modifier.
        """
        part = part.strip()
        
        # Look for + or - in the part
        if '+' in part:
            # Handle positive modifier
            split_parts = part.split('+', 1)
            if len(split_parts) == 2:
                skill_name = split_parts[0].strip()
                try:
                    modifier = int(split_parts[1].strip())
                    return skill_name, modifier
                except ValueError:
                    pass
        elif '-' in part:
            # Handle negative modifier - but be careful of skill names with hyphens
            # We look for the last occurrence of - followed by digits
            import re
            match = re.match(r'^(.+?)\s*-\s*(\d+)$', part)
            if match:
                skill_name = match.group(1).strip()
                try:
                    modifier = -int(match.group(2))
                    return skill_name, modifier
                except ValueError:
                    pass
        
        # No modifier found
        return part, None

    def _parse_vs_expression(self, vs_expr):
        """
        Parse VS expression to determine what we're rolling against.
        
        Formats:
        - "soma:defense" - target's single stat
        - "soma:strength+weaponry" - target's multiple stats
        - "soma:defense-1" - target's stat with modifier
        - "5" - static value
        
        Returns:
            bool: True if parsing was successful, False otherwise
        """
        vs_expr = vs_expr.strip()
        
        # Check if it's a static value
        try:
            self.vs_value = int(vs_expr)
            self.vs_target = "static"
            return True
        except ValueError:
            pass
        
        # Must be character:stat format
        if ":" not in vs_expr:
            self.caller.msg("VS format must be '<target>:<stat>' or a number. Example: soma:defense or 5")
            return False
        
        target_name, stat_expr = vs_expr.split(":", 1)
        target_name = target_name.strip()
        stat_expr = stat_expr.strip()
        
        # Find the target character
        target_char = self.caller.search(target_name, global_search=True)
        if not target_char:
            return False
        
        # Check if target is a character with stats
        if not hasattr(target_char, 'db') or not target_char.db.stats:
            self.caller.msg(f"{target_char.get_display_name(self.caller)} doesn't have any stats.")
            return False
        
        self.vs_target_char = target_char
        self.vs_target = target_char.get_display_name(self.caller)
        
        # Parse the stat expression (can be "defense", "strength+weaponry", "defense-1", etc.)
        self.vs_value = self._calculate_vs_value(target_char, stat_expr)
        if self.vs_value is None:
            return False
        
        return True
    
    def _calculate_vs_value(self, target_char, stat_expr):
        """
        Calculate the VS value from a target character's stat expression.
        
        Supports:
        - "defense" - single stat
        - "strength+weaponry" - multiple stats
        - "defense-1" - stat with modifier
        - "strength+weaponry+2" - multiple stats with modifier
        
        Returns:
            int: The calculated value, or None if error
        """
        # First check if there's a modifier at the end
        import re
        
        # Try to extract a trailing modifier
        modifier_match = re.search(r'([+-])\s*(\d+)$', stat_expr)
        modifier = 0
        if modifier_match:
            sign = modifier_match.group(1)
            value = int(modifier_match.group(2))
            modifier = value if sign == '+' else -value
            stat_expr = stat_expr[:modifier_match.start()].strip()
            self.vs_modifier = modifier
        
        # Split on + to get individual stats
        stat_parts = [s.strip() for s in stat_expr.split('+')]
        
        total_value = 0
        self.vs_stats = []
        
        for stat_name in stat_parts:
            stat_name = stat_name.lower().strip()
            if not stat_name:
                continue
            
            stat_value = self.get_stat_value_from_char(target_char, stat_name)
            if stat_value is None:
                self.caller.msg(f"{self.vs_target} doesn't have '{stat_name}' set.")
                return None
            
            self.vs_stats.append((stat_name, stat_value))
            total_value += stat_value
        
        return total_value + modifier

    def get_stat_value(self, stat_name):
        """Get a stat value from the character's stats"""
        return self.get_stat_value_from_char(self.caller, stat_name)
    
    def get_stat_value_from_char(self, character, stat_name):
        """Get a stat value from a specific character's stats"""
        if not character.db.stats:
            return None
            
        # Check attributes
        attributes = character.db.stats.get("attributes", {})
        if stat_name in attributes:
            return attributes.get(stat_name)
        
        # Check skills
        skills = character.db.stats.get("skills", {})
        if stat_name in skills:
            return skills.get(stat_name)
        
        # Check advantages
        advantages = character.db.stats.get("advantages", {})
        if stat_name in advantages:
            return advantages.get(stat_name)
            
        return None
    
    def get_specialty_bonus(self):
        """
        Check if character has a specialty for the skill being rolled.
        Returns 1 if specialty exists, 0 otherwise, and the specialty name.
        """
        if not self.skill_name or not self.caller.db.stats:
            return 0, None
        
        # Check if there's a specialties dictionary in stats
        specialties = self.caller.db.stats.get("specialties", {})
        
        # Check if this skill has a specialty
        skill_specialty = specialties.get(self.skill_name.lower())
        
        if skill_specialty:
            return 1, skill_specialty
        
        return 0, None
    
    def has_patient_merit(self):
        """Check if character has the Patient merit."""
        if not self.caller.db.stats:
            return False
        
        merits = self.caller.db.stats.get("merits", {})
        return "patient" in [m.lower() for m in merits.keys()]

    def func(self):
        """Execute the roll command."""
        if not hasattr(self, 'dice_pool'):
            return
        
        # Handle extended rolls (multiple rolls to reach target)
        if self.is_extended:
            self.handle_extended_roll()
            return
        
        # Handle opposed rolls (both parties roll)
        if self.is_opposed:
            self.handle_opposed_roll()
            return
        
        # Apply specialty bonus if requested
        specialty_bonus = 0
        specialty_name = None
        if self.is_specialty:
            specialty_bonus, specialty_name = self.get_specialty_bonus()
            if specialty_bonus == 0:
                self.caller.msg(f"You don't have a specialty in {self.skill_name}.")
            return
            
        # Apply modifier and wound penalties
        wound_penalty = 0
        if (hasattr(self.caller, 'get_wound_penalty') and 
            RollType.REFLEXIVE not in self.roll_types and 
            RollType.DAMAGE not in self.roll_types):
            # Wound penalties don't apply to reflexive actions or damage rolls
            wound_penalty = self.caller.get_wound_penalty()
        elif not hasattr(self.caller, 'get_wound_penalty'):
            # Fallback: calculate wound penalty directly if method doesn't exist
            from world.utils.health_utils import calculate_wound_penalty
            if (RollType.REFLEXIVE not in self.roll_types and 
                RollType.DAMAGE not in self.roll_types):
                wound_penalty = calculate_wound_penalty(self.caller)
        
        # Apply VS penalty if present
        vs_penalty = 0
        if self.vs_target:
            vs_penalty = -self.vs_value
        
        final_pool = self.dice_pool + self.modifier + wound_penalty + vs_penalty + specialty_bonus
        
        # Roll the dice using the utility function
        rolls, successes, ones = roll_dice(final_pool, 8, self.roll_types)
        
        # Get stat and skill values for display
        stat_value = None
        skill_value = None
        
        if self.stat_name:
            stat_value = self.get_stat_value(self.stat_name.lower())
        if self.skill_name:
            skill_value = self.get_stat_value(self.skill_name.lower())
        
        # Get character name
        character_name = self.caller.get_display_name(self.caller)
        
        # Handle job rolls specially
        if self.is_job_roll:
            self.handle_job_roll(rolls, successes, ones, self.stat_name, self.skill_name, stat_value, skill_value, character_name, wound_penalty, vs_penalty)
        else:
            # Regular roll handling with VS display
            if self.vs_target:
                player_msg = self._format_vs_roll_display(
                    rolls, successes, ones, stat_value, skill_value, character_name, wound_penalty, vs_penalty
                )
            else:
                # Format the roll message for the player (with dice details)
                player_msg = roll_to_job_display(
                    successes=successes,
                    ones=ones,
                    rolls=rolls,
                    dice_pool=self.dice_pool,
                    roll_types=self.roll_types,
                    modifier=self.modifier,
                    stat_name=self.stat_name,
                    skill_name=self.skill_name,
                    stat_value=stat_value,
                    skill_value=skill_value,
                    character_name=character_name,
                    wound_penalty=wound_penalty
                )
            
            # Send to the player
            self.caller.msg(player_msg)
            
            # If this is a VS roll with a target character, send them the full display too
            if self.vs_target and self.vs_target_char and self.vs_target_char != self.caller:
                self.vs_target_char.msg(player_msg)
            
            # Format the roll message for room observers
            if self.vs_target:
                room_msg = self._format_vs_room_display(
                    successes, ones, character_name, wound_penalty, vs_penalty, specialty_name
                )
            else:
                if self.is_secret:
                    # Secret rolls show stat names and results but hide values
                    final_pool = self.dice_pool + self.modifier + wound_penalty
                    if successes == 0 and ones >= 1 and final_pool <= 0:
                        result = f"|r{successes} successes (Dramatic Failure)|n"
                    elif successes >= 5:
                        result = f"|g{successes} successes (Exceptional Success)|n"
                    elif successes > 0:
                        result = f"|g{successes} successes|n"
                    else:
                        result = f"|y{successes} successes|n"
                    
                    # Build roll description with stat names
                    if self.stat_name and self.skill_name:
                        roll_desc = f"{self.stat_name.title()} + {self.skill_name.title()}"
                        if self.is_specialty and specialty_name:
                            roll_desc += " with a specialty"
                    elif self.stat_name:
                        roll_desc = self.stat_name.title()
                    else:
                        roll_desc = "a dice roll"
                    
                    room_msg = f"|c{character_name}|n rolls {roll_desc}: {result}"
                else:
                    room_msg = roll_to_room_display(
                        successes=successes,
                        ones=ones,
                        dice_pool=self.dice_pool,
                        roll_types=self.roll_types,
                        modifier=self.modifier,
                        stat_name=self.stat_name,
                        skill_name=self.skill_name,
                        character_name=character_name,
                        wound_penalty=wound_penalty
                    )
            
            # Send to others in the room
            if self.caller.location:
                # Exclude both the caller and the target (if applicable)
                exclude_list = [self.caller]
                if self.vs_target_char and self.vs_target_char != self.caller:
                    exclude_list.append(self.vs_target_char)
                self.caller.location.msg_contents(room_msg, exclude=exclude_list)
            
            # Handle exceptional success
            if successes >= 5:
                self.caller.msg("|Y|[bExceptional Success achieved! You may add a condition.|n|Y]|n")
                self.caller.msg("|yUse: |w+condition/add <condition_name>|n")
                # Award beat for exceptional success
                self.award_beat("exceptional_success")
            
            # Handle dramatic failure
            if successes == 0 and ones >= 1 and final_pool <= 0:
                # Award beat for dramatic failure
                self.award_beat("dramatic_failure")

    def handle_extended_roll(self):
        """Handle extended actions (multiple rolls to reach target successes)."""
        # Validate that we have stat + skill for extended rolls
        if not self.stat_name or not self.skill_name:
            self.caller.msg("Extended actions require Attribute + Skill format.")
            return
        
        # Get stat and skill values
        stat_value = self.get_stat_value(self.stat_name.lower())
        skill_value = self.get_stat_value(self.skill_name.lower())
        
        if stat_value is None or skill_value is None:
            self.caller.msg("Invalid attribute or skill specified.")
            return
        
        # Calculate maximum rolls (Attribute + Skill + 2 if Patient)
        max_rolls = stat_value + skill_value
        has_patient = self.has_patient_merit()
        if has_patient:
            max_rolls += 2
        
        # Use specified max rolls if less than calculated max
        if self.extended_max_rolls > 0:
            if self.extended_max_rolls > max_rolls:
                self.caller.msg(f"You can only make up to {max_rolls} rolls (Attribute {stat_value} + Skill {skill_value}{' + 2 (Patient)' if has_patient else ''}).")
                return
            max_rolls = self.extended_max_rolls
        
        # Get specialty bonus if applicable
        specialty_bonus = 0
        specialty_name = None
        if self.is_specialty:
            specialty_bonus, specialty_name = self.get_specialty_bonus()
            if specialty_bonus == 0:
                self.caller.msg(f"You don't have a specialty in {self.skill_name}.")
                return
        
        # Get wound penalty
        wound_penalty = 0
        if (hasattr(self.caller, 'get_wound_penalty') and 
            RollType.REFLEXIVE not in self.roll_types and 
            RollType.DAMAGE not in self.roll_types):
            wound_penalty = self.caller.get_wound_penalty()
        elif not hasattr(self.caller, 'get_wound_penalty'):
            from world.utils.health_utils import calculate_wound_penalty
            if (RollType.REFLEXIVE not in self.roll_types and 
                RollType.DAMAGE not in self.roll_types):
                wound_penalty = calculate_wound_penalty(self.caller)
        
        character_name = self.caller.get_display_name(self.caller)
        
        # Store extended action state on character
        extended_state = {
            'dice_pool': self.dice_pool,
            'modifier': self.modifier,
            'wound_penalty': wound_penalty,
            'specialty_bonus': specialty_bonus,
            'specialty_name': specialty_name,
            'roll_types': self.roll_types,
            'stat_name': self.stat_name,
            'skill_name': self.skill_name,
            'stat_value': stat_value,
            'skill_value': skill_value,
            'target': self.extended_target,
            'max_rolls': max_rolls,
            'current_roll': 0,
            'total_successes': 0,
            'roll_results': [],
            'dramatic_failure_penalty': 0,
            'character_name': character_name,
            'is_secret': self.is_secret,
            'exceptional_bonuses': [],  # Track exceptional success bonuses chosen
            'target_reduction': 0  # Track reductions from exceptional successes
        }
        
        self.caller.ndb.extended_action = extended_state
        
        # Display extended action header
        self._display_extended_action_header(extended_state)
        
        # Start the first roll
        self._continue_extended_action()
    
    def _display_extended_action_header(self, state):
        """Display the header for an extended action."""
        msg = []
        msg.append("|w" + "=" * 70 + "|n")
        msg.append("|W|[bEXTENDED ACTION|n")
        msg.append("|w" + "-" * 70 + "|n")
        
        roll_desc = f"{state['stat_name'].title()} + {state['skill_name'].title()}"
        if state['specialty_name']:
            roll_desc += f" ({state['specialty_name']})"
        
        msg.append(f"|c{state['character_name']}|n attempts {roll_desc}")
        msg.append(f"  Target: |w{state['target']}|n successes")
        msg.append(f"  Maximum Rolls: |w{state['max_rolls']}|n")
        msg.append(f"  Base Pool: |w{state['stat_value']}|n ({state['stat_name'].title()}) + |w{state['skill_value']}|n ({state['skill_name'].title()})")
        if state['specialty_name']:
            msg.append(f"  Specialty Bonus: |w+1|n die ({state['specialty_name']})")
        
        msg.append("|w" + "-" * 70 + "|n")
        
        self.caller.msg("\n".join(msg))
        
        # Show to staff even if secret
        if state['is_secret'] and self.caller.location:
            for obj in self.caller.location.contents:
                if obj != self.caller and obj.check_permstring("Builder"):
                    msg_text = '\n'.join(msg)
                    obj.msg(f"|y[STAFF - Extended Action Started]|n\n{msg_text}")
    
    def _continue_extended_action(self):
        """Continue processing the extended action with one more roll."""
        state = self.caller.ndb.extended_action
        if not state:
            return
        
        # Check if we've reached max rolls or target
        adjusted_target = state['target'] - state['target_reduction']
        if state['current_roll'] >= state['max_rolls'] or state['total_successes'] >= adjusted_target:
            self._finish_extended_action()
            return
        
        # Increment roll number
        state['current_roll'] += 1
        
        # Calculate pool for this roll
        current_pool = (state['dice_pool'] + state['modifier'] + state['wound_penalty'] + 
                       state['specialty_bonus'] - state['dramatic_failure_penalty'])
        
        if current_pool < 0:
            current_pool = 0
        
        # Roll the dice
        rolls, successes, ones = roll_dice(current_pool, 8, state['roll_types'])
        
        # Determine result type
        result_type = "success"
        if successes == 0 and ones >= 1 and current_pool <= 0:
            result_type = "dramatic_failure"
            state['dramatic_failure_penalty'] = 2  # Next roll gets -2 penalty
            # Award beat for dramatic failure
            self.award_beat("dramatic_failure")
        elif successes == 0:
            result_type = "failure"
        elif successes >= 5:
            result_type = "exceptional_success"
            # Award beat for exceptional success
            self.award_beat("exceptional_success")
        
        # Add to total (only if not a failure)
        if result_type != "failure" and result_type != "dramatic_failure":
            state['total_successes'] += successes
        
        # Store roll result
        roll_result = {
            "roll_num": state['current_roll'],
            "pool": current_pool,
            "rolls": rolls,
            "successes": successes,
            "ones": ones,
            "result_type": result_type,
            "cumulative": state['total_successes']
        }
        state['roll_results'].append(roll_result)
        
        # Display this roll
        self._display_single_extended_roll(roll_result, state)
        
        # Check if target reached
        if state['total_successes'] >= adjusted_target:
            self._finish_extended_action()
            return
        
        # Handle exceptional success - prompt for bonus choice
        if result_type == "exceptional_success":
            EvMenu(self.caller, {
                "extended_exceptional_menu": extended_exceptional_menu,
                "_apply_exceptional_node": _apply_exceptional_node
            }, startnode="extended_exceptional_menu", persistent=False)
            return
        
        # Handle failure - prompt for condition or abandon
        if result_type == "failure":
            EvMenu(self.caller, {
                "extended_failure_menu": extended_failure_menu,
                "condition_selection_menu": condition_selection_menu,
                "_apply_condition_node": _apply_condition_node,
                "_abandon_node": _abandon_node
            }, startnode="extended_failure_menu", persistent=False)
            return
        
        # Continue to next roll
        self._continue_extended_action()
    
    def _display_single_extended_roll(self, roll_result, state):
        """Display a single roll in the extended action."""
        dice_str = ", ".join(str(d) for d in sorted(roll_result["rolls"], reverse=True)) if roll_result["rolls"] else "none"
        
        msg = []
        msg.append(f"\nRoll #{roll_result['roll_num']}:")
        msg.append(f"  Pool: |w{roll_result['pool']}|n dice")
        msg.append(f"  Dice: [{dice_str}]")
        msg.append(f"  Successes: |w{roll_result['successes']}|n")
        
        adjusted_target = state['target'] - state['target_reduction']
        
        if roll_result["result_type"] == "dramatic_failure":
            msg.append(f"  |r|[bDRAMATIC FAILURE!|n|r]|n - Next roll suffers -2 penalty")
            msg.append(f"  Cumulative: |r{roll_result['cumulative']}|n/{adjusted_target}")
        elif roll_result["result_type"] == "failure":
            msg.append(f"  |yFailure|n - Choose: Accept a Condition or abandon the action")
            msg.append(f"  Cumulative: |y{roll_result['cumulative']}|n/{adjusted_target}")
        elif roll_result["result_type"] == "exceptional_success":
            msg.append(f"  |g|[bEXCEPTIONAL SUCCESS!|n|g]|n")
            msg.append(f"  Choose: Reduce required successes by {state['skill_value']}, reduce time by 25%, or apply exceptional result")
            msg.append(f"  Cumulative: |g{roll_result['cumulative']}|n/{adjusted_target}")
        else:
            msg.append(f"  Cumulative: |g{roll_result['cumulative']}|n/{adjusted_target}")
        
        self.caller.msg("\n".join(msg))
        
        # Show to staff even if secret
        if state['is_secret'] and self.caller.location:
            for obj in self.caller.location.contents:
                if obj != self.caller and obj.check_permstring("Builder"):
                    msg_text = '\n'.join(msg)
                    obj.msg(f"|y[STAFF]|n {msg_text}")
    
    def _finish_extended_action(self):
        """Finish and display the extended action results."""
        state = self.caller.ndb.extended_action
        if not state:
            return
        
        # Format and send the extended roll display
        self._display_extended_roll(state)
        
        # Send room message
        if self.caller.location:
            roll_desc = f"{state['stat_name'].title()} + {state['skill_name'].title()}"
            if state['is_secret'] and state['specialty_name']:
                roll_desc += " with a specialty"
            
            adjusted_target = state['target'] - state['target_reduction']
            if state['total_successes'] >= adjusted_target:
                result_msg = f"|gSucceeded!|n ({state['total_successes']}/{adjusted_target} successes in {len(state['roll_results'])} roll{'s' if len(state['roll_results']) > 1 else ''})"
            else:
                result_msg = f"|yFailed.|n ({state['total_successes']}/{adjusted_target} successes after {len(state['roll_results'])} roll{'s' if len(state['roll_results']) > 1 else ''})"
            
            room_msg = f"|c{state['character_name']}|n performs an extended action using {roll_desc}: {result_msg}"
            
            # Send to room (staff will have already seen the details)
            self.caller.location.msg_contents(room_msg, exclude=[self.caller])
        
        # Clear state
        del self.caller.ndb.extended_action
    
    def _display_extended_roll(self, state):
        """Display the final summary of an extended action to the player."""
        roll_results = state['roll_results']
        total_successes = state['total_successes']
        target = state['target'] - state['target_reduction']
        
        msg = []
        msg.append("|w" + "-" * 70 + "|n")
        
        # Display exceptional bonuses if any
        if state['exceptional_bonuses']:
            msg.append(f"|gExceptional Bonuses Applied:|n {', '.join(state['exceptional_bonuses'])}")
            msg.append("")
        
        # Final result
        if total_successes >= target:
            msg.append(f"|W|[bSUCCESS!|n Achieved {total_successes}/{target} successes in {len(roll_results)} roll{'s' if len(roll_results) > 1 else ''}|n")
        else:
            msg.append(f"|W|[bINCOMPLETE|n Achieved {total_successes}/{target} successes after {len(roll_results)} roll{'s' if len(roll_results) > 1 else ''}|n")
        
        msg.append("|w" + "=" * 70 + "|n")
        
        self.caller.msg("\n".join(msg))
        
        # Show to staff even if secret
        if state['is_secret'] and self.caller.location:
            for obj in self.caller.location.contents:
                if obj != self.caller and obj.check_permstring("Builder"):
                    msg_text = '\n'.join(msg)
                    obj.msg(f"|y[STAFF - Extended Action Complete]|n\n{msg_text}")

    def handle_opposed_roll(self):
        """Handle opposed rolls where both parties roll and compare."""
        if not self.vs_target_char:
            self.caller.msg("Opposed rolls require a target character. Example: +roll/opposed strength+brawl vs soma:strength+brawl")
            return
        
        # Apply specialty bonus if requested
        specialty_bonus = 0
        specialty_name = None
        if self.is_specialty:
            specialty_bonus, specialty_name = self.get_specialty_bonus()
            if specialty_bonus == 0:
                self.caller.msg(f"You don't have a specialty in {self.skill_name}.")
                return
        
        # Get wound penalties for both characters
        attacker_wound_penalty = 0
        if (hasattr(self.caller, 'get_wound_penalty') and 
            RollType.REFLEXIVE not in self.roll_types and 
            RollType.DAMAGE not in self.roll_types):
            attacker_wound_penalty = self.caller.get_wound_penalty()
        elif not hasattr(self.caller, 'get_wound_penalty'):
            from world.utils.health_utils import calculate_wound_penalty
            if (RollType.REFLEXIVE not in self.roll_types and 
                RollType.DAMAGE not in self.roll_types):
                attacker_wound_penalty = calculate_wound_penalty(self.caller)
        
        defender_wound_penalty = 0
        if hasattr(self.vs_target_char, 'get_wound_penalty'):
            defender_wound_penalty = self.vs_target_char.get_wound_penalty()
        elif hasattr(self.vs_target_char, 'db'):
            from world.utils.health_utils import calculate_wound_penalty
            defender_wound_penalty = calculate_wound_penalty(self.vs_target_char)
        
        # Calculate final pools
        attacker_pool = self.dice_pool + self.modifier + attacker_wound_penalty + specialty_bonus
        defender_pool = self.vs_value + defender_wound_penalty
        
        # Roll for both parties
        attacker_rolls, attacker_successes, attacker_ones = roll_dice(attacker_pool, 8, self.roll_types)
        defender_rolls, defender_successes, defender_ones = roll_dice(defender_pool, 8, self.roll_types)
        
        # Get character names
        attacker_name = self.caller.get_display_name(self.caller)
        defender_name = self.vs_target_char.get_display_name(self.caller)
        
        # Determine winner
        if attacker_successes > defender_successes:
            result = f"|g{attacker_name} wins by {attacker_successes - defender_successes} success(es)!|n"
            winner = attacker_name
        elif defender_successes > attacker_successes:
            result = f"|r{defender_name} wins by {defender_successes - attacker_successes} success(es)!|n"
            winner = defender_name
        else:
            result = "|yIt's a tie!|n"
            winner = "Tie"
        
        # Format the opposed roll display
        msg = self._format_opposed_display(
            attacker_name, attacker_rolls, attacker_successes, attacker_pool, attacker_wound_penalty,
            defender_name, defender_rolls, defender_successes, defender_pool, defender_wound_penalty,
            result, winner
        )
        
        # Send to both parties
        self.caller.msg(msg)
        if self.vs_target_char != self.caller:
            self.vs_target_char.msg(msg)
        
        # Send to room
        if self.caller.location:
            if self.is_secret:
                # Secret rolls show stat names but hide values
                # Build roll description with stat names
                if self.stat_name and self.skill_name:
                    attacker_roll_desc = f"{self.stat_name.title()} + {self.skill_name.title()}"
                    if self.is_specialty and specialty_name:
                        attacker_roll_desc += " with a specialty"
                elif self.stat_name:
                    attacker_roll_desc = self.stat_name.title()
                else:
                    attacker_roll_desc = "dice"
                
                # Build defender's stat description
                if self.vs_stats:
                    defender_stat_names = " + ".join(s[0].title() for s in self.vs_stats)
                    defender_roll_desc = defender_stat_names
                else:
                    defender_roll_desc = "dice"
                
                room_msg = f"|c{attacker_name}|n rolls {attacker_roll_desc} vs |c{defender_name}|n's {defender_roll_desc}: {result}"
            else:
                room_msg = f"|c{attacker_name}|n rolls opposed against |c{defender_name}|n: {result}"
            self.caller.location.msg_contents(room_msg, exclude=[self.caller, self.vs_target_char])
        
        # Handle exceptional successes and dramatic failures for both parties
        # Attacker (caller)
        if attacker_successes >= 5:
            self.caller.msg("|Y|[bExceptional Success achieved! You may add a condition.|n|Y]|n")
            self.award_beat("exceptional_success")
        
        if attacker_successes == 0 and attacker_ones >= 1 and attacker_pool <= 0:
            self.award_beat("dramatic_failure")
        
        # Defender (target) - award beats if they're a player character
        if self.vs_target_char and self.vs_target_char != self.caller:
            if defender_successes >= 5:
                self.vs_target_char.msg("|Y|[bExceptional Success achieved! You may add a condition.|n|Y]|n")
                # Award beat to defender
                self._award_beat_to_character(self.vs_target_char, "exceptional_success")
            
            if defender_successes == 0 and defender_ones >= 1 and defender_pool <= 0:
                # Award beat to defender for dramatic failure
                self._award_beat_to_character(self.vs_target_char, "dramatic_failure")
    
    def _format_opposed_display(self, attacker_name, attacker_rolls, attacker_successes, attacker_pool, attacker_wound,
                                defender_name, defender_rolls, defender_successes, defender_pool, defender_wound, result, winner):
        """Format the display for an opposed roll."""
        
        msg = []
        msg.append("|w" + "=" * 70 + "|n")
        msg.append("|W|[bOPPOSED ROLL|n")
        msg.append("|w" + "-" * 70 + "|n")
        
        # Attacker's roll - show stat names and result only
        stat_display = ""
        if self.stat_name and self.skill_name:
            stat_display = f"{self.stat_name.title()} + {self.skill_name.title()}"
        elif self.stat_name:
            stat_display = self.stat_name.title()
        
        msg.append(f"|c{attacker_name}|n rolls {stat_display}")
        msg.append(f"  Result: |w{attacker_successes}|n success(es)")
        
        msg.append("|w" + "-" * 70 + "|n")
        
        # Defender's roll - show stat names and result only
        defender_stat_display = ""
        if self.vs_stats:
            defender_stat_display = " + ".join(s[0].title() for s in self.vs_stats)
        
        msg.append(f"|c{defender_name}|n rolls {defender_stat_display}")
        msg.append(f"  Result: |w{defender_successes}|n success(es)")
        
        msg.append("|w" + "-" * 70 + "|n")
        msg.append(f"|W|[bRESULT:|n {result}|n")
        msg.append("|w" + "=" * 70 + "|n")
        
        return "\n".join(msg)
    
    def _format_vs_roll_display(self, rolls, successes, ones, stat_value, skill_value, character_name, wound_penalty, vs_penalty):
        """Format display for VS (contested) rolls."""
        dice_str = ", ".join(str(d) for d in sorted(rolls, reverse=True))
        
        msg = []
        msg.append("|w" + "=" * 70 + "|n")
        msg.append("|W|[bCONTESTED ROLL|n")
        msg.append("|w" + "-" * 70 + "|n")
        
        # Roll description - show stat names without values
        if self.stat_name and self.skill_name:
            msg.append(f"|c{character_name}|n rolls {self.stat_name.title()} + {self.skill_name.title()}")
        else:
            msg.append(f"|c{character_name}|n rolls dice")
        
        # VS description - show opponent's stat names without values
        if self.vs_target == "static":
            vs_desc = f"vs {self.vs_value}"
        else:
            if self.vs_stats:
                vs_stat_names = " + ".join(s[0].title() for s in self.vs_stats)
                vs_desc = f"vs |c{self.vs_target}|n's {vs_stat_names}"
            else:
                vs_desc = f"vs |c{self.vs_target}|n"
        
        msg.append(f"  {vs_desc}")
        
        # Show final pool
        final_pool = self.dice_pool + self.modifier + wound_penalty + vs_penalty
        msg.append(f"  Final Pool: |w{final_pool}|n dice")
        
        msg.append("|w" + "-" * 70 + "|n")
        msg.append(f"  Dice: [{dice_str}]")
        msg.append(f"  Successes: |w{successes}|n")
        if ones > 0:
            msg.append(f"  Ones: |r{ones}|n")
        
        # Success interpretation
        if successes == 0 and ones >= 1 and final_pool <= 0:
            msg.append(f"  |r|[bDRAMATIC FAILURE!|n|r]|n")
        elif successes >= 5:
            msg.append(f"  |g|[bEXCEPTIONAL SUCCESS!|n|g]|n")
        elif successes > 0:
            msg.append(f"  |gSuccess|n")
        else:
            msg.append(f"  |yFailure|n")
        
        msg.append("|w" + "=" * 70 + "|n")
        
        return "\n".join(msg)
    
    def _format_vs_room_display(self, successes, ones, character_name, wound_penalty, vs_penalty, specialty_name=None):
        """Format room display for VS rolls (without dice details)."""
        
        # If secret, return message with stat names but hide values
        if self.is_secret:
            final_pool = self.dice_pool + self.modifier + wound_penalty + vs_penalty
            if successes == 0 and ones >= 1 and final_pool <= 0:
                result = f"|r{successes} successes (Dramatic Failure)|n"
            elif successes >= 5:
                result = f"|g{successes} successes (Exceptional Success)|n"
            elif successes > 0:
                result = f"|g{successes} successes|n"
            else:
                result = f"|y{successes} successes|n"
            
            # Build roll description with stat names
            if self.stat_name and self.skill_name:
                roll_desc = f"{self.stat_name.title()} + {self.skill_name.title()}"
                if self.is_specialty and specialty_name:
                    roll_desc += " with a specialty"
            elif self.stat_name:
                roll_desc = self.stat_name.title()
            else:
                roll_desc = "dice"
            
            # Build VS description with stat names
            if self.vs_target == "static":
                return f"|c{character_name}|n rolls {roll_desc} vs {self.vs_value}: {result}"
            else:
                if self.vs_stats:
                    vs_stat_names = " + ".join(s[0].title() for s in self.vs_stats)
                    vs_desc = f"|c{self.vs_target}|n's {vs_stat_names}"
                else:
                    vs_desc = f"|c{self.vs_target}|n"
                return f"|c{character_name}|n rolls {roll_desc} vs {vs_desc}: {result}"
        
        # Build roll description
        if self.stat_name and self.skill_name:
            roll_desc = f"{self.stat_name.title()} + {self.skill_name.title()}"
        else:
            roll_desc = f"{self.dice_pool} dice"
        
        # VS description
        if self.vs_target == "static":
            vs_desc = f"vs {self.vs_value}"
        else:
            if self.vs_stats:
                vs_stat_names = " + ".join(s[0].title() for s in self.vs_stats)
                vs_desc = f"vs {self.vs_target}'s {vs_stat_names}"
        
        final_pool = self.dice_pool + self.modifier + wound_penalty + vs_penalty
        
        # Result description
        if successes == 0 and ones >= 1 and final_pool <= 0:
            result = f"|r{successes} successes (Dramatic Failure)|n"
        elif successes >= 5:
            result = f"|g{successes} successes (Exceptional Success)|n"
        elif successes > 0:
            result = f"|g{successes} successes|n"
        else:
            result = f"|y{successes} successes|n"
        
        return f"|c{character_name}|n rolls {roll_desc} {vs_desc}: {result}"
    
    def handle_job_roll(self, rolls, successes, ones, stat_name, skill_name, stat_value, skill_value, character_name, wound_penalty=0, vs_penalty=0):
        """Handle rolls made to jobs."""
        from world.jobs.models import Job
        
        try:
            # Get the job
            job = Job.objects.get(id=self.job_id, archive_id__isnull=True)
            
            # Check if the player has permission to roll to this job
            if not (job.requester == self.caller.account or 
                    job.participants.filter(id=self.caller.account.id).exists() or 
                    job.assignee == self.caller.account or
                    self.caller.check_permstring("Admin")):
                self.caller.msg("You don't have permission to roll to this job.")
                return
                
            # Use VS display if applicable, otherwise use standard display
            if self.vs_target:
                job_roll_display = self._format_vs_roll_display(
                    rolls, successes, ones, stat_value, skill_value, character_name, wound_penalty, vs_penalty
                )
            else:
                # Use the original expansive box format for job rolls
                job_roll_display = format_roll_display(
                    successes=successes,
                    ones=ones,
                    rolls=rolls,
                    dice_pool=self.dice_pool,
                    roll_types=self.roll_types,
                    modifier=self.modifier,
                    stat_name=stat_name,
                    skill_name=skill_name,
                    stat_value=stat_value,
                    skill_value=skill_value,
                    wound_penalty=wound_penalty
                )
            
            # Send the expansive format to the roller
            self.caller.msg(job_roll_display)
            
            # Create a roll summary for the job comment
            if stat_name and skill_name:
                modifier_parts = []
                if self.modifier != 0:
                    modifier_parts.append(f"{self.modifier:+d}")
                if wound_penalty != 0:
                    modifier_parts.append(f"{wound_penalty:+d} (wound)")
                if vs_penalty != 0:
                    if self.vs_target == "static":
                        modifier_parts.append(f"{vs_penalty:+d} (vs {self.vs_value})")
                    else:
                        modifier_parts.append(f"{vs_penalty:+d} (vs {self.vs_target})")
                
                if modifier_parts:
                    modifier_str = " " + " ".join(modifier_parts)
                    roll_desc = f"{stat_name.title()} + {skill_name.title()}{modifier_str}"
                else:
                    roll_desc = f"{stat_name.title()} + {skill_name.title()}"
            else:
                final_pool = self.dice_pool + self.modifier + wound_penalty + vs_penalty
                roll_desc = f"{final_pool} dice"
                if wound_penalty != 0:
                    roll_desc += f" (includes {wound_penalty:+d} wound penalty)"
                if vs_penalty != 0:
                    roll_desc += f" (includes {vs_penalty:+d} vs penalty)"
            
            # Success interpretation for the comment
            final_pool_for_failure = self.dice_pool + self.modifier + wound_penalty + vs_penalty
            if successes == 0 and ones >= 1 and final_pool_for_failure <= 0:
                result = f"{successes} successes (Dramatic Failure)"
            elif successes >= 5:
                result = f"{successes} successes (Exceptional Success)"
            elif successes > 0:
                result = f"{successes} successes"
            else:
                result = f"{successes} successes"
            
            # Use the enhanced roll display format for the job comment
            enhanced_comment_text = job_roll_display
            
            # Add the roll as a comment to the job
            roll_comment = {
                "author": character_name,
                "text": enhanced_comment_text,
                "created_at": timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            if not job.comments:
                job.comments = []
            job.comments.append(roll_comment)
            job.save()
            
            # Notify job participants about the roll
            from commands.jobs.jobs_commands import CmdJobs
            cmd_jobs = CmdJobs()
            cmd_jobs.caller = self.caller
            
            # Create a simple format for notifications (since they're sent via mail)
            dice_str = ", ".join(str(roll) for roll in sorted(rolls, reverse=True))
            notification_message = f"{character_name} made a dice roll on Job #{self.job_id}: {roll_desc} -> {result} ({dice_str})"
            cmd_jobs.send_mail_to_all_participants(job, notification_message, exclude_account=self.caller.account)
            
            # Post to the jobs channel for staff notification
            cmd_jobs.post_to_jobs_channel(character_name, job.id, "made a dice roll on")
            
            self.caller.msg(f"|gRoll added to Job #{self.job_id} and participants notified.|n")
            
            # Handle exceptional success (message already included in format_roll_display)
            if successes >= 5:
                # Award beat for exceptional success
                self.award_beat("exceptional_success")
            
            # Handle dramatic failure for job rolls
            if successes == 0 and ones >= 1 and final_pool_for_failure <= 0:
                # Award beat for dramatic failure
                self.award_beat("dramatic_failure")
                
        except Job.DoesNotExist:
            self.caller.msg(f"Job #{self.job_id} not found or is archived.")
        except Exception as e:
            self.caller.msg(f"Error rolling to job: {str(e)}")
            from evennia.utils import logger
            logger.log_err(f"Error in handle_job_roll: {str(e)}", exc_info=True)
    
    def award_beat(self, source):
        """
        Award a beat to the character for exceptional success or dramatic failure.
        
        Args:
            source (str): The source of the beat ('exceptional_success' or 'dramatic_failure')
        """
        try:
            # Use the character's experience property to award the beat
            exp_handler = self.caller.experience
            exp_handler.add_beat()
            
            # Log the beat gain
            from world.xp_logger import get_xp_logger
            logger = get_xp_logger(self.caller)
            
            # Format the message based on the source
            if source == "exceptional_success":
                source_msg = "exceptional success"
                color = "|g"
                logger.log_beat(1, "Exceptional Success", details="Automatic from dice roll")
            elif source == "dramatic_failure":
                source_msg = "dramatic failure"
                color = "|r"
                logger.log_beat(1, "Dramatic Failure", details="Automatic from dice roll")
            else:
                source_msg = source.replace("_", " ")
                color = "|y"
            
            self.caller.msg(f"{color}You gained 1 beat from {source_msg}!|n")
            
            # Post to Dice channel
            self._post_to_dice_channel(source_msg)
            
        except Exception as e:
            # Don't let beat awarding errors break the roll command
            from evennia.utils import logger
            logger.log_err(f"Error awarding beat for {source}: {str(e)}")
            self.caller.msg(f"|rError awarding beat: {str(e)}|n")
    
    def _post_to_dice_channel(self, source_msg, character=None):
        """Post beat award notification to the Dice channel."""
        try:
            from evennia.comms.models import ChannelDB
            from evennia.utils import create
            
            # Use specified character or default to caller
            char = character or self.caller
            
            # Try to find the Dice channel
            channel = None
            found_channel = ChannelDB.objects.channel_search("Dice")
            if found_channel:
                channel = found_channel[0]
            
            if not channel:
                # Create the channel if it doesn't exist
                channel = create.create_channel(
                    "Dice",
                    desc="Notifications for exceptional successes and dramatic failures",
                    locks="control:perm(Admin);listen:all();send:all()"
                )
                if not channel:
                    # Failed to create channel
                    from evennia.utils import logger
                    logger.log_err("Failed to create Dice channel")
                    return
            
            # Get character name
            character_name = char.get_display_name(char)
            
            # Format the message based on source
            if source_msg == "exceptional success":
                icon = "|g[!]|n"
                message = f"{icon} |c{character_name}|n earned a beat from an |gexceptional success|n!"
            elif source_msg == "dramatic failure":
                icon = "|r[X]|n"
                message = f"{icon} |c{character_name}|n earned a beat from a |rdramatic failure|n!"
            else:
                icon = "|y[+]|n"
                message = f"{icon} |c{character_name}|n earned a beat from {source_msg}!"
            
            # Post to channel
            channel.msg(f"[DICE] {message}")
                
        except Exception as e:
            # Don't break the roll if channel posting fails
            from evennia.utils import logger
            logger.log_err(f"Error posting to Dice channel: {str(e)}")
    
    def _award_beat_to_character(self, character, source):
        """Award a beat to a specific character (used for opposed rolls)."""
        try:
            exp_handler = character.experience
            exp_handler.add_beat()
            
            from world.xp_logger import get_xp_logger
            logger = get_xp_logger(character)
            
            if source == "exceptional_success":
                source_msg = "exceptional success"
                color = "|g"
                logger.log_beat(1, "Exceptional Success", details="Automatic from opposed roll")
            elif source == "dramatic_failure":
                source_msg = "dramatic failure"
                color = "|r"
                logger.log_beat(1, "Dramatic Failure", details="Automatic from opposed roll")
            else:
                source_msg = source.replace("_", " ")
                color = "|y"
            
            character.msg(f"{color}You gained 1 beat from {source_msg}!|n")
            
            # Post to Dice channel
            self._post_to_dice_channel(source_msg, character)
            
        except Exception as e:
            from evennia.utils import logger
            logger.log_err(f"Error awarding beat to {character}: {str(e)}") 


# EvMenu functions for extended action handling

def extended_failure_menu(caller):
    """Menu node for handling extended action failures."""
    text = "|yYou rolled a failure on your extended action.|n\n\n"
    text += "Do you want to:\n"
    text += "  |w1|n - Accept a Condition and continue\n"
    text += "  |w2|n - Abandon the action\n"
    
    options = (
        {"key": "1", "desc": "Accept a Condition", "goto": "condition_selection_menu"},
        {"key": "2", "desc": "Abandon the action", "goto": "_abandon_node"},
        {"key": "_default", "goto": "extended_failure_menu"}
    )
    
    return text, options


def _abandon_node(caller, raw_string):
    """Node that abandons the extended action."""
    caller.msg("|yYou abandon the extended action.|n")
    
    # Finish the action
    from evennia.utils import delay
    def finish_action(c):
        cmd = CmdRoll()
        cmd.caller = c
        cmd._finish_extended_action()
    
    delay(0.1, finish_action, caller)
    
    return None, None


def condition_selection_menu(caller):
    """Menu node for selecting a condition to apply."""
    # Get list of all available conditions
    conditions = []
    for key, condition in STANDARD_CONDITIONS.items():
        conditions.append((key, condition.name))
    
    # Sort by name
    conditions.sort(key=lambda x: x[1])
    
    # Store conditions list in caller for access by callback
    caller.ndb._temp_conditions_list = conditions
    
    # Format text with 3-column display
    text = "|wSelect a condition to apply:|n\n\n"
    
    # Calculate columns
    num_conditions = len(conditions)
    rows = (num_conditions + 2) // 3  # Round up to get number of rows
    
    for row in range(rows):
        line_parts = []
        for col in range(3):
            idx = row + (col * rows)
            if idx < num_conditions:
                num = idx + 1
                name = conditions[idx][1]
                # Pad to 28 characters for alignment
                line_parts.append(f"{num:2d}: {name:<25}")
        text += " ".join(line_parts) + "\n"
    
    text += "\n"
    
    # Build options (EvMenu will still show them, but formatted differently)
    options = []
    for idx, (key, name) in enumerate(conditions, 1):
        options.append({
            "key": str(idx),
            "desc": name,
            "goto": "_apply_condition_node"
        })
    
    options.append({"key": "_default", "goto": "condition_selection_menu"})
    
    return text, options


def _apply_condition_node(caller, raw_string):
    """Node that applies a condition and closes the menu."""
    # Get the selected condition from the raw input
    try:
        selection = int(raw_string.strip())
        conditions_list = caller.ndb._temp_conditions_list
        if selection < 1 or selection > len(conditions_list):
            caller.msg("Invalid selection.")
            return "condition_selection_menu", None
        
        condition_key = conditions_list[selection - 1][0]
    except (ValueError, TypeError, AttributeError):
        caller.msg("Invalid selection.")
        return "condition_selection_menu", None
    
    # Get the condition
    condition = STANDARD_CONDITIONS.get(condition_key)
    if not condition:
        caller.msg("Invalid condition selected.")
        return None, None
    
    # Add to character using their condition handler
    if hasattr(caller, 'conditions'):
        caller.conditions.add(condition)
    else:
        caller.msg(f"|gYou accept the condition: |w{condition.name}|n")
    
    # Continue the extended action
    from evennia.utils import delay
    delay(0.1, _continue_after_menu, caller)
    
    # Return None to close menu
    return None, None


def extended_exceptional_menu(caller):
    """Menu node for handling extended action exceptional successes."""
    state = caller.ndb.extended_action
    if not state:
        return "Error: No extended action in progress.", None
    
    text = "|gYou rolled an Exceptional Success!|n\n\n"
    text += "Choose your bonus:\n"
    text += f"  |w1|n - Reduce required successes by {state['skill_value']}\n"
    text += "  |w2|n - Reduce time by 25%\n"
    text += "  |w3|n - Apply exceptional result\n"
    
    options = (
        {"key": "1", "desc": "Reduce successes", "goto": "_apply_exceptional_node"},
        {"key": "2", "desc": "Reduce time", "goto": "_apply_exceptional_node"},
        {"key": "3", "desc": "Exceptional result", "goto": "_apply_exceptional_node"},
        {"key": "_default", "goto": "extended_exceptional_menu"}
    )
    
    return text, options


def _apply_exceptional_node(caller, raw_string):
    """Node that applies an exceptional bonus and closes the menu."""
    state = caller.ndb.extended_action
    if not state:
        return None, None
    
    # Determine which option was selected
    try:
        selection = int(raw_string.strip())
    except (ValueError, TypeError):
        caller.msg("Invalid selection.")
        return "extended_exceptional_menu", None
    
    if selection == 1:
        state['target_reduction'] += state['skill_value']
        caller.msg(f"|gTarget successes reduced by {state['skill_value']}! New target: {state['target'] - state['target_reduction']}|n")
        state['exceptional_bonuses'].append(f"Reduced successes by {state['skill_value']}")
    elif selection == 2:
        caller.msg("|gTime required reduced by 25%!|n")
        state['exceptional_bonuses'].append("Time reduced by 25%")
    elif selection == 3:
        caller.msg("|gExceptional result will be applied when the action completes!|n")
        state['exceptional_bonuses'].append("Exceptional result applied")
    else:
        caller.msg("Invalid selection.")
        return "extended_exceptional_menu", None
    
    # Continue the extended action
    from evennia.utils import delay
    delay(0.1, _continue_after_menu, caller)
    
    # Return None to close menu
    return None, None


def _continue_after_menu(caller):
    """Helper to continue extended action after menu closes."""
    cmd = CmdRoll()
    cmd.caller = caller
    cmd._continue_extended_action()


def _abandon_node(caller, raw_string):
    """Node that abandons the extended action."""
    caller.msg("|yYou abandon the extended action.|n")
    
    # Finish the action
    from evennia.utils import delay
    def finish_action(c):
        cmd = CmdRoll()
        cmd.caller = c
        cmd._finish_extended_action()
    
    delay(0.1, finish_action, caller)
    
    return None, None 