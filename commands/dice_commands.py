"""
Chronicles of Darkness dice rolling system.
Implements the standard CoD dice pool mechanics with 10-sided dice.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.utils import inherits_from
from world.conditions import STANDARD_CONDITIONS
from world.utils.dice_utils import roll_dice, interpret_roll_results, roll_to_job_display, roll_to_room_display, format_roll_display, RollType
from django.utils import timezone

class CmdRoll(MuxCommand):
    """
    Roll dice for Chronicles of Darkness system.
    
    Usage:
        +roll[/8|9|10|rote|reflex|damage|job] <stat> + <skill> [+/- modifier]
        +roll[/8|9|10|rote|reflex|damage|job] <number of dice>
        +roll[/8|9|10|rote|reflex|damage|job] <stat> + <skill> + <modifier>
        +roll/job <dice pool>=<job id>
        +roll/job <stat> + <skill>=<job id>
    
    Switches:
        /8 - 8-again (roll again on 8 or higher)
        /9 - 9-again (roll again on 9 or higher)
        /10 - 10-again (roll again on 10)
        /rote - Reroll all failed dice once
        /reflex - Reflexive action (no action cost)
        /damage - Damage roll (no wound penalties apply)
        /job - Roll to a job (uses expansive format, adds to job comments)
        
    Multiple switches can be combined, e.g.:
        +roll/8/rote Strength + Weaponry
    
    Examples:
        +roll/8 Strength + Weaponry
        +roll/9/rote 4
        +roll/reflex Strength + Weaponry + 3
        +roll/damage Strength + 2
        +roll/job Wits + Investigation=123
        +roll/job/8 5=456
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
        self.stat_name = None
        self.skill_name = None
        
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
        
        # If no roll types specified, use normal (10-again)
        if not self.roll_types:
            self.roll_types = {RollType.NORMAL}
        
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

    def get_stat_value(self, stat_name):
        """Get a stat value from the character's stats"""
        if not self.caller.db.stats:
            return None
            
        # Check attributes
        attributes = self.caller.db.stats.get("attributes", {})
        if stat_name in attributes:
            return attributes.get(stat_name)
        
        # Check skills
        skills = self.caller.db.stats.get("skills", {})
        if stat_name in skills:
            return skills.get(stat_name)
        
        # Check advantages
        advantages = self.caller.db.stats.get("advantages", {})
        if stat_name in advantages:
            return advantages.get(stat_name)
            
        return None

    def func(self):
        """Execute the roll command."""
        if not hasattr(self, 'dice_pool'):
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
        
        final_pool = self.dice_pool + self.modifier + wound_penalty
        
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
            self.handle_job_roll(rolls, successes, ones, self.stat_name, self.skill_name, stat_value, skill_value, character_name, wound_penalty)
        else:
            # Regular roll handling
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
            
            # Format the roll message for room observers (without dice details)
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
                self.caller.location.msg_contents(room_msg, exclude=[self.caller])
            
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

    def handle_job_roll(self, rolls, successes, ones, stat_name, skill_name, stat_value, skill_value, character_name, wound_penalty=0):
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
                
                if modifier_parts:
                    modifier_str = " " + " ".join(modifier_parts)
                    roll_desc = f"{stat_name.title()} + {skill_name.title()}{modifier_str}"
                else:
                    roll_desc = f"{stat_name.title()} + {skill_name.title()}"
            else:
                final_pool = self.dice_pool + self.modifier + wound_penalty
                roll_desc = f"{final_pool} dice"
                if wound_penalty != 0:
                    roll_desc += f" (includes {wound_penalty:+d} wound penalty)"
            
            # Success interpretation for the comment
            final_pool_for_failure = self.dice_pool + self.modifier + wound_penalty
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
            
        except Exception as e:
            # Don't let beat awarding errors break the roll command
            from evennia.utils import logger
            logger.log_err(f"Error awarding beat for {source}: {str(e)}")
            self.caller.msg(f"|rError awarding beat: {str(e)}|n") 