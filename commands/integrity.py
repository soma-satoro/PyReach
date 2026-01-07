from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from evennia.utils.evmenu import EvMenu
from evennia.utils.evmore import EvMore
from world.experience import ExperienceHandler
from world.conditions import STANDARD_CONDITIONS
from world.utils.dice_utils import roll_dice, RollType
from utils.search_helpers import search_character
from world.reality_systems import get_template
from world.cofd.integrity_systems import BREAKING_POINTS_BY_TEMPLATE, get_breaking_points

class CmdIntegrity(MuxCommand):
    """
    Make breaking point rolls and manage integrity.
    
    Usage:
        +integrity - View your current integrity status
        +integrity/check - Make a breaking point/integrity check for yourself
        +integrity/check <character> - Staff: Make a check for another character
        +integrity/check +<value> - Make a check with a positive modifier
        +integrity/check -<value> - Make a check with a negative modifier
        +integrity/check +<stat> - Add a stat to the pool (e.g., +resolve, +composure)
        +integrity/break - View your template's breaking points list
        +integrity/heal <amount> [type] - Heal Clarity damage (Changelings only)
        +integrity/heal <character>=<amount> [type] - Heal another's Clarity (staff)
        
    Breaking point rolls use Resolve + Composure with an automatic modifier
    based on your current Integrity:
        
        Integrity 8-10: +2 dice
        Integrity 6-7:  +1 die
        Integrity 4-5:  No modifier
        Integrity 2-3:  -1 die
        Integrity 1:    -2 dice
        
    Results (Mortal/Hunter/Vampire):
        Dramatic Failure: Lose 1 Integrity, choose a severe Condition (Broken, 
                         Fugue, or Madness), gain a Beat
        Failure:         Lose 1 Integrity, choose a minor Condition (Guilty, 
                         Shaken, or Spooked)
        Success:         No Integrity loss, choose a minor Condition (Guilty, 
                         Shaken, or Spooked)
        Exceptional:     Gain a Beat and 1 temporary Willpower (up to max)
        
    Changeling Clarity Attacks:
        For Changelings, use severity (1-5 dice) instead of modifiers:
        +integrity/check 3  - 3-dice Clarity attack
        
        Results:
        Dramatic Failure: No damage, regain 1 Willpower
        Failure:         No damage
        Success:         Roll Wyrd for mild Clarity damage
        Exceptional:     Roll Wyrd for severe Clarity damage
        
    Examples:
        +integrity - View your current integrity status
        +integrity/check - Make a breaking point check
        +integrity/check +2 - Make a check with +2 modifier (protecting loved one)
        +integrity/check -3 - Make a check with -3 penalty (witnessed murder)
        +integrity/check +resolve - Add resolve as a bonus
        +integrity/check John - Staff: Force a check for John
        +integrity/break - View all breaking points for your template
        +integrity/heal 2 mild - Heal 2 mild Clarity damage (Changelings)
        +integrity/heal 1 severe - Heal 1 severe Clarity damage (Changelings)
        +integrity/heal John=2 mild - Staff: Heal John's Clarity
    """
    key = "+integrity"
    aliases = ["+int", "+breakingpoint", "+bp"]
    help_category = "Skill and Condition Checks"
    
    def func(self):
        """Execute the command"""
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        if is_legacy_mode():
            self.caller.msg("|rIntegrity system uses CoD 2e mechanics and is disabled in Legacy Mode.|n")
            return
        
        # Handle switches
        if self.switches:
            switch = self.switches[0].lower()
            
            if switch == "break":
                self.show_breaking_points()
                return
            elif switch == "heal":
                self.handle_clarity_heal()
                return
            elif switch == "check" or switch == "roll":  # Support both for backwards compatibility
                # Parse the arguments for check
                target = self.caller
                manual_modifier = 0
                stat_bonuses = []
                
                if self.args:
                    args = self.args.strip()
                    
                    # Check if it's a plain number first (for Changeling severity or general modifier)
                    try:
                        manual_modifier = int(args)
                    except ValueError:
                        # Not a plain number
                        # Check if it's a modifier with +/- prefix
                        if args.startswith('+') or args.startswith('-'):
                            # Try to parse as signed number
                            try:
                                manual_modifier = int(args)
                            except ValueError:
                                # Not a number, might be a stat name like "+resolve"
                                stat_name = args[1:].lower()
                                
                                # Try to get the stat value
                                try:
                                    attributes = self.caller.db.stats.get("attributes", {})
                                    skills = self.caller.db.stats.get("skills", {})
                                    
                                    if stat_name in attributes:
                                        stat_value = attributes[stat_name]
                                        stat_bonuses.append((stat_name, stat_value))
                                    elif stat_name in skills:
                                        stat_value = skills[stat_name]
                                        stat_bonuses.append((stat_name, stat_value))
                                    else:
                                        self.caller.msg(f"|rUnknown stat: {stat_name}|n")
                                        return
                                except (KeyError, TypeError):
                                    self.caller.msg(f"|rCould not find stat: {stat_name}|n")
                                    return
                        else:
                            # It's not a number or +/- prefix, must be a character name - staff only
                            if not self.caller.check_permstring("Admin"):
                                self.caller.msg("|rOnly staff can make breaking point checks for other characters.|n")
                                return
                            
                            target = search_character(self.caller, args)
                            if not target:
                                return
                
                # Perform the breaking point check
                self.perform_breaking_point_roll(target, manual_modifier, stat_bonuses)
                return
            else:
                self.caller.msg(f"|rInvalid switch: {switch}|n")
                self.caller.msg("Valid switches: /break, /check")
                return
        
        # No switches - show current integrity status
        self.show_integrity_status()
    
    def handle_clarity_heal(self):
        """Handle Clarity healing for Changelings."""
        # Check if caller is a Changeling
        template = get_template(self.caller).lower()
        
        # Parse target character for staff
        target = self.caller
        remaining_args = self.args
        is_staff = self.caller.check_permstring("Admin")
        
        if not self.args:
            self.caller.msg("Usage: +integrity/heal <amount> [type] or +integrity/heal <character>=<amount> [type]")
            self.caller.msg("Types: mild, severe (defaults to mild)")
            return
        
        # Check for staff targeting another character (format: <char>=<amount> [type])
        if "=" in self.args:
            if not is_staff:
                self.caller.msg("|rOnly staff can heal other characters' Clarity.|n")
                return
            
            parts = self.args.split("=", 1)
            target_name = parts[0].strip()
            remaining_args = parts[1].strip()
            
            target = search_character(self.caller, target_name)
            if not target:
                return
        else:
            remaining_args = self.args
        
        # Check if target is a Changeling
        target_template = get_template(target).lower()
        if target_template != "changeling":
            self.caller.msg(f"|r{target.name} is not a Changeling. Clarity healing only applies to Changelings.|n")
            return
        
        # Parse arguments: <amount> [type]
        args_list = remaining_args.split()
        try:
            amount = int(args_list[0])
        except (ValueError, IndexError):
            self.caller.msg("Amount must be a number.")
            return
        
        # Parse damage type (mild or severe)
        damage_type_str = args_list[1].lower() if len(args_list) > 1 else "mild"
        
        if damage_type_str in ["mild", "m"]:
            damage_type = "mild"
            heal_severe = False
        elif damage_type_str in ["severe", "s", "sev"]:
            damage_type = "severe"
            heal_severe = True
        else:
            self.caller.msg(f"|rInvalid damage type: {damage_type_str}. Use 'mild' or 'severe'.|n")
            return
        
        if amount < 1:
            self.caller.msg("Heal amount must be at least 1.")
            return
        
        # Heal Clarity damage
        from world.cofd.clarity_utils import heal_clarity_damage, get_clarity_display_with_info
        
        success, msg = heal_clarity_damage(target, amount, heal_severe)
        
        if target == self.caller:
            self.caller.msg(msg)
        else:
            if success:
                self.caller.msg(f"|gYou heal {amount} {damage_type} Clarity damage from {target.name}.|n")
                target.msg(msg)
            else:
                self.caller.msg(msg)
        
        # Show updated Clarity status
        if success:
            clarity_display = get_clarity_display_with_info(target)
            if target == self.caller:
                self.caller.msg(f"\n|wClarity Track:|n\n{clarity_display}")
            else:
                self.caller.msg(f"\n|w{target.name}'s Clarity Track:|n\n{clarity_display}")
    
    def show_integrity_status(self):
        """Display current integrity status and relevant breaking points."""
        template = get_template(self.caller).lower()
        bp_data = get_breaking_points(template)
        
        # Get current integrity level
        try:
            current_level = self.caller.db.stats['other'].get('integrity', 7)
        except (KeyError, TypeError, AttributeError):
            current_level = 7
        
        output = []
        output.append("|g<" + "=" * 78 + ">|n")
        
        if bp_data:
            integrity_name = bp_data["name"]
            title = f"YOUR {integrity_name.upper()} STATUS"
        else:
            integrity_name = "Integrity"
            title = "YOUR INTEGRITY STATUS"
        
        output.append("|g" + title.center(80) + "|n")
        output.append("|g<" + "=" * 78 + ">|n")
        output.append("")
        output.append(f"|wCurrent {integrity_name}:|n {current_level} / 10")
        output.append("")
        
        # Show template-specific information
        if template == "changeling":
            self._show_changeling_clarity_status(output, current_level)
        elif template == "vampire":
            self._show_vampire_humanity_status(output, current_level, bp_data)
        elif template == "werewolf":
            self._show_werewolf_harmony_status(output, current_level)
        elif template in ["mortal", "mortal+", "hunter"]:
            self._show_mortal_integrity_status(output, current_level)
        else:
            output.append("|yYour template does not have specific integrity mechanics defined.|n")
            output.append("|yIntegrity is managed by Storyteller discretion.|n")
        
        output.append("")
        output.append("|g<" + "=" * 78 + ">|n")
        output.append("")
        
        # Send with pagination
        text = "\n".join(output)
        EvMore(self.caller, text, always_page=False, session=self.session, justify_kwargs=False, exit_on_lastpage=True)
    
    def _show_changeling_clarity_status(self, output, current_level):
        """Show Changeling-specific Clarity status."""
        # Get Clarity damage track
        from world.cofd.clarity_utils import get_clarity_display_with_info
        
        # Get Wyrd
        try:
            wyrd = self.caller.db.stats['advantages'].get('wyrd', 1)
        except (KeyError, TypeError):
            wyrd = 1
        
        clarity_display = get_clarity_display_with_info(self.caller)
        output.append("|wClarity Track:|n")
        output.append(clarity_display)
        output.append("")
        output.append(f"|wYour Wyrd:|n {wyrd} (used for damage rolls)")
        output.append("")
        
        output.append("|wHow Clarity Attacks Work:|n")
        output.append("  1. Roll dice based on breaking point severity (1-5 dice)")
        output.append("  2. Add modifiers based on situation (+3 to -3)")
        output.append("  3. Roll results:")
        output.append(f"     • |gDramatic Failure:|n No damage, regain 1 Willpower!")
        output.append(f"     • |gFailure:|n No damage taken")
        output.append(f"     • |ySuccess:|n Roll Wyrd ({wyrd}) for mild damage (/)")
        output.append(f"     • |rExceptional:|n Roll Wyrd ({wyrd}) for severe damage (X)")
        output.append("  4. Damage in rightmost 3 boxes = gain Clarity Condition")
        output.append("")
        output.append("|wHealing Clarity:|n")
        output.append("  • Spend scene with Touchstone: heal all mild OR 1 severe")
        output.append("  • Resolve Clarity Condition: heal 1 damage")
        output.append("  • Resolve Persistent Condition: heal 2 damage")
        output.append("  • Command: +integrity/heal <amount> <type>")
        output.append("")
        output.append("|wPerception Modifiers:|n")
        if current_level >= 5:
            output.append(f"  • Undamaged Clarity 5+: |g+2 dice to perception rolls|n")
        elif current_level >= 3:
            output.append(f"  • Undamaged Clarity 3-4: |y-1 die to perception rolls|n")
        else:
            output.append(f"  • Undamaged Clarity 1-2: |r-2 dice to perception rolls|n")
            output.append(f"  • |rDramatic failures on perception = hallucinations|n")
    
    def _show_vampire_humanity_status(self, output, current_level, bp_data):
        """Show Vampire-specific Humanity status."""
        # Show Banes if any
        banes = getattr(self.caller.db, "banes", []) or []
        if banes:
            from world.cofd.integrity_systems import VAMPIRE_BANES
            output.append("|wYour Banes:|n")
            for i, bane_key in enumerate(banes, 1):
                bane_data = VAMPIRE_BANES.get(bane_key, {})
                bane_name = bane_data.get("name", bane_key.title())
                output.append(f"  {i}. |r{bane_name}|n")
            output.append(f"|xBane Penalty: -{len(banes)} dice to detachment rolls|n")
            output.append("")
        
        # Show Touchstones bonus
        bio_data = getattr(self.caller.db, "bio_data", {})
        if bio_data:
            touchstones = bio_data.get("touchstones", []) or []
            if touchstones:
                touchstone_bonus = min(len(touchstones), 2)
                output.append(f"|wTouchstones:|n {len(touchstones)} (+{touchstone_bonus} dice max)")
                output.append("")
        
        breaking_points = bp_data["data"]
        bp_info = breaking_points.get(current_level, {})
        
        if bp_info:
            dice = bp_info["dice"]
            breaks = bp_info["breaks"]
            
            output.append(f"|wBreaking Points at Humanity {current_level}:|n")
            output.append(f"|x(Base: {dice} {'die' if dice == 1 else 'dice'} to resist detachment)|n")
            output.append("")
            for bp in breaks:
                output.append(f"  • {bp}")
            output.append("")
        
        output.append("|wHow Detachment Works:|n")
        output.append("  • Facing a breaking point: Always gain 1 Beat")
        output.append("  • Roll base dice + Touchstones - Banes + modifiers")
        output.append("  • Dramatic Failure: Lose 1 Humanity, Jaded Condition")
        output.append("  • Failure: Lose 1 Humanity, Bestial/Competitive/Wanton")
        output.append("  • Success: No loss, Bestial/Competitive/Wanton")
        output.append("  • Exceptional: No loss, Inspired Condition")
        output.append("")
        output.append("|wBanes:|n")
        output.append("  • When losing Humanity, can take a Bane + Beat")
        output.append("  • Prevents future loss from that breaking point")
        output.append("  • Each Bane gives -1 to future rolls")
        output.append(f"  • Maximum 3 Banes (you have {len(banes)})")
    
    def _show_werewolf_harmony_status(self, output, current_level):
        """Show Werewolf-specific Harmony status."""
        output.append("|wHow Harmony Works:|n")
        output.append("  • Harmony measures balance between flesh and spirit")
        output.append("  • Breaking points directly modify Harmony (no roll)")
        output.append("  • Toward Flesh: Lowers Harmony")
        output.append("  • Toward Spirit: Raises Harmony")
        output.append("  • Penalties shown in breaking points list")
        output.append("")
        
        if current_level <= 3:
            output.append("|yYour Harmony is 3 or lower:|n")
            output.append("|yAdditional breaking points are active (see +integrity/break)|n")
        elif current_level >= 8:
            output.append("|cYour Harmony is 8 or higher:|n")
            output.append("|cAdditional breaking points are active (see +integrity/break)|n")
    
    def _show_mortal_integrity_status(self, output, current_level):
        """Show Mortal/Hunter-specific Integrity status."""
        # Try to get breaking points from bio
        bio_data = getattr(self.caller.db, "bio_data", {})
        if bio_data:
            breaking_points = bio_data.get("breaking_points", {})
            if breaking_points:
                output.append("|wYour Breaking Points (from +bio):|n")
                for i in range(1, 6):
                    bp = breaking_points.get(f"bp{i}", "")
                    if bp:
                        output.append(f"  {i}. {bp}")
                output.append("")
        
        output.append("|wHow Integrity Works:|n")
        output.append("  • Breaking points trigger when you violate your morals")
        output.append("  • Roll Resolve + Composure (+ Integrity modifiers)")
        output.append("  • Failure: Lose 1 Integrity, gain Condition")
        output.append("  • Dramatic Failure: Lose 1 Integrity, severe Condition, gain Beat")
        output.append("  • Success: No loss, gain minor Condition")
        output.append("  • Exceptional: Gain Beat and 1 Willpower")
        output.append("")
        output.append("|wIntegrity Modifiers:|n")
        if current_level >= 8:
            output.append("  • Integrity 8-10: |g+2 dice|n")
        elif current_level >= 6:
            output.append("  • Integrity 6-7: |g+1 die|n")
        elif current_level >= 4:
            output.append("  • Integrity 4-5: No modifier")
        elif current_level >= 2:
            output.append("  • Integrity 2-3: |y-1 die|n")
        else:
            output.append("  • Integrity 1: |r-2 dice|n")
    
    def show_breaking_points(self):
        """Display breaking points for the character's template."""
        # Get character template
        template = get_template(self.caller).lower()
        
        # Check if template has breaking points defined
        bp_data = get_breaking_points(template)
        if not bp_data:
            self.caller.msg(f"|yYour template ({template}) does not have specific breaking points defined.|n")
            self.caller.msg("|yBreaking points are determined by Storyteller discretion.|n")
            return
        
        integrity_name = bp_data["name"]
        breaking_points = bp_data["data"]
        
        # Get current integrity level
        try:
            current_level = self.caller.db.stats['other'].get('integrity', 7)
        except (KeyError, TypeError, AttributeError):
            current_level = 7
        
        # Build output
        output = []
        output.append("|g<" + "=" * 78 + ">|n")
        title = f"{integrity_name.upper()} BREAKING POINTS"
        output.append("|g" + title.center(80) + "|n")
        output.append("|g<" + "=" * 78 + ">|n")
        output.append("")
        output.append(f"|wCurrent {integrity_name}:|n {current_level}")
        output.append("")
        
        # Check the type of breaking points display
        bp_type = bp_data.get("type", "descending")
        
        if bp_type == "dual":
            # Display dual nature breaking points (Werewolf style)
            output.append("|yHarmony measures your balance between flesh and spirit.|n")
            output.append("|yBreaking points push you in one direction or the other.|n")
            output.append("")
            
            # Toward Flesh
            flesh_data = breaking_points.get("toward_flesh", {})
            output.append("|r<==================== TOWARD FLESH ====================>|n")
            output.append(f"|x{flesh_data.get('description', '')}|n")
            output.append("")
            for bp in flesh_data.get("breaks", []):
                penalty = bp.get("penalty", -1)
                action = bp.get("action", "")
                penalty_str = f" |r({penalty:+d} Harmony)|n" if penalty < 0 else ""
                output.append(f"  • {action}{penalty_str}")
            output.append("")
            
            # Low Harmony threshold
            low_data = breaking_points.get("low_harmony", {})
            if current_level <= low_data.get("threshold", 3):
                output.append("|y<============ HARMONY 3 OR LOWER (ACTIVE) ============>|n")
            else:
                output.append("|x<============ Harmony 3 or Lower (inactive) ==========>|n")
            output.append(f"|x{low_data.get('description', '')}|n")
            output.append("")
            for bp in low_data.get("breaks", []):
                penalty = bp.get("penalty", -1)
                action = bp.get("action", "")
                penalty_str = f" |r({penalty:+d} Harmony)|n" if penalty < 0 else ""
                output.append(f"  • {action}{penalty_str}")
            output.append("")
            
            # Toward Spirit
            spirit_data = breaking_points.get("toward_spirit", {})
            output.append("|c<==================== TOWARD SPIRIT ====================>|n")
            output.append(f"|x{spirit_data.get('description', '')}|n")
            output.append("")
            for bp in spirit_data.get("breaks", []):
                penalty = bp.get("penalty", -1)
                action = bp.get("action", "")
                penalty_str = f" |r({penalty:+d} Harmony)|n" if penalty < 0 else ""
                output.append(f"  • {action}{penalty_str}")
            output.append("")
            
            # High Harmony threshold
            high_data = breaking_points.get("high_harmony", {})
            if current_level >= high_data.get("threshold", 8):
                output.append("|y<============ HARMONY 8 OR MORE (ACTIVE) =============>|n")
            else:
                output.append("|x<=========== Harmony 8 or More (inactive) ===========>|n")
            output.append(f"|x{high_data.get('description', '')}|n")
            output.append("")
            for bp in high_data.get("breaks", []):
                penalty = bp.get("penalty", -1)
                action = bp.get("action", "")
                penalty_str = f" |r({penalty:+d} Harmony)|n" if penalty < 0 else ""
                output.append(f"  • {action}{penalty_str}")
            output.append("")
            
        elif bp_type == "descending":
            # Display breaking points from highest to lowest (Vampire style)
            for level in sorted(breaking_points.keys(), reverse=True):
                bp_info = breaking_points[level]
                dice = bp_info["dice"]
                breaks = bp_info["breaks"]
                
                # Highlight current level
                if level == current_level:
                    header = f"|c{integrity_name} {level} ({dice} {'Die' if dice == 1 else 'Dice'}) <<< YOUR CURRENT LEVEL|n"
                else:
                    header = f"|w{integrity_name} {level}|n ({dice} {'Die' if dice == 1 else 'Dice'})"
                
                output.append(header)
                
                # List breaking points with bullets
                for break_point in breaks:
                    output.append(f"  • {break_point}")
                
                output.append("")
        else:
            # Display by severity (Changeling style)
            output.append("|yBreaking points are organized by severity (dice pool).|n")
            output.append("|yMore dice = more severe breaking point.|n")
            output.append("")
            
            for severity in sorted(breaking_points.keys()):
                bp_info = breaking_points[severity]
                dice = bp_info["dice"]
                breaks = bp_info["breaks"]
                
                header = f"|w{dice} {'Die' if dice == 1 else 'Dice'}|n |x(Minor)|n" if dice == 1 else f"|w{dice} Dice|n |r(Severe)|n" if dice >= 4 else f"|w{dice} Dice|n"
                
                output.append(header)
                
                # List breaking points with bullets
                for break_point in breaks:
                    output.append(f"  • {break_point}")
                
                output.append("")
        
        output.append("|g<" + "=" * 78 + ">|n")
        output.append("")
        
        if bp_type == "dual":
            output.append("|yNote:|n When you commit a breaking point, you lose the indicated Harmony.")
            output.append("Breaking points toward Flesh lower Harmony. Breaking points toward Spirit raise it.")
            output.append("Threshold breaking points only apply when you're at that Harmony level.")
        elif bp_type == "descending":
            output.append("|yNote:|n Breaking points require a degeneration roll using the listed dice.")
            output.append("Roll results determine if you lose a point of " + integrity_name + " and gain Conditions.")
        else:
            output.append("|yNote:|n When you encounter a breaking point, roll the listed number of dice.")
            output.append("Your current " + integrity_name + " may modify the roll. Failure means losing " + integrity_name + ".")
        
        output.append("")
        
        # Send with pagination
        text = "\n".join(output)
        EvMore(self.caller, text, always_page=False, session=self.session, justify_kwargs=False, exit_on_lastpage=True)
    
    def perform_breaking_point_roll(self, target, manual_modifier=0, stat_bonuses=None):
        """Perform a breaking point roll for a character."""
        # Check template to determine which system to use
        template = get_template(target).lower()
        
        if template == "changeling":
            self.perform_clarity_attack(target, manual_modifier, stat_bonuses)
            return
        elif template == "vampire":
            self.perform_vampire_detachment(target, manual_modifier, stat_bonuses)
            return
        
        # Get character stats
        if not hasattr(target.db, 'stats'):
            self.caller.msg(f"{target.name} does not have stats set up.")
            return
        
        try:
            resolve = target.db.stats["attributes"]["resolve"]
            composure = target.db.stats["attributes"]["composure"]
        except (KeyError, TypeError):
            self.caller.msg(f"{target.name} does not have Resolve or Composure set.")
            return
        
        # Get current integrity (stored in stats['other']['integrity'])
        try:
            integrity = target.db.stats['other']['integrity']
        except (KeyError, TypeError):
            integrity = 7  # Default if not set
        
        # Calculate automatic modifier based on integrity
        if integrity >= 8:
            auto_modifier = 2
        elif integrity >= 6:
            auto_modifier = 1
        elif integrity >= 4:
            auto_modifier = 0
        elif integrity >= 2:
            auto_modifier = -1
        else:  # integrity == 1
            auto_modifier = -2
        
        # Add stat bonuses if provided
        stat_bonus_total = 0
        if stat_bonuses:
            for stat_name, stat_value in stat_bonuses:
                stat_bonus_total += stat_value
        
        # Calculate total dice pool
        dice_pool = resolve + composure + auto_modifier + manual_modifier + stat_bonus_total
        
        # Ensure minimum pool
        if dice_pool < 0:
            dice_pool = 0
        
        # Perform the roll
        rolls, successes, ones = roll_dice(dice_pool, 10, {RollType.NORMAL})
        
        # Determine result type (CoD 2e rules)
        result_type = "success"
        # Dramatic failure only on chance dice (pool = 0, roll 1 die, get a 1)
        if dice_pool == 0 and ones >= 1:
            result_type = "dramatic_failure"
        elif successes == 0:
            result_type = "failure"
        elif successes >= 5:
            result_type = "exceptional_success"
        
        # Format and display the roll result
        self._display_breaking_point_result(target, dice_pool, rolls, successes, ones, result_type, 
                                            integrity, resolve, composure, auto_modifier, manual_modifier, stat_bonuses)
        
        # Store the result for menu processing
        target.ndb.breaking_point_result = {
            'result_type': result_type,
            'successes': successes,
            'integrity': integrity,
            'caller': self.caller  # Store who initiated the roll (for staff rolls)
        }
        
        # Handle the result
        if result_type == "dramatic_failure":
            self._handle_dramatic_failure(target)
        elif result_type == "failure":
            self._handle_failure(target)
        elif result_type == "success":
            self._handle_success(target)
        elif result_type == "exceptional_success":
            self._handle_exceptional_success(target)
    
    def perform_clarity_attack(self, target, severity_modifier=0, stat_bonuses=None):
        """Perform a Clarity attack for a Changeling."""
        # Get Wyrd for damage calculation
        try:
            wyrd = target.db.stats['advantages'].get('wyrd', 1)
        except (KeyError, TypeError):
            wyrd = 1
        
        # Determine severity - if no modifier provided, ask or default to 1
        # For now, we'll use the manual_modifier as the base severity
        # In a full implementation, you'd prompt for severity
        base_severity = abs(severity_modifier) if severity_modifier != 0 else 1
        
        # Add stat bonuses to severity
        stat_bonus_total = 0
        if stat_bonuses:
            for stat_name, stat_value in stat_bonuses:
                stat_bonus_total += stat_value
        
        # Calculate total attack dice pool
        attack_pool = base_severity + stat_bonus_total
        
        # Ensure minimum pool
        if attack_pool < 0:
            attack_pool = 0
        
        # Perform the Clarity attack roll
        rolls, successes, ones = roll_dice(attack_pool, 10, {RollType.NORMAL})
        
        # Determine result type (CoD 2e rules)
        result_type = "success"
        # Dramatic failure only on chance dice (pool = 0, roll 1 die, get a 1)
        if attack_pool == 0 and ones >= 1:
            result_type = "dramatic_failure"
        elif successes == 0:
            result_type = "failure"
        elif successes >= 5:
            result_type = "exceptional_success"
        
        # Display the attack result
        self._display_clarity_attack_result(target, attack_pool, rolls, successes, ones, result_type,
                                           base_severity, stat_bonuses, wyrd)
        
        # Handle the result
        if result_type == "dramatic_failure":
            self._handle_clarity_dramatic_failure(target)
        elif result_type == "failure":
            self._handle_clarity_failure(target)
        elif result_type == "success":
            self._handle_clarity_success(target, wyrd, severe=False)
        elif result_type == "exceptional_success":
            self._handle_clarity_success(target, wyrd, severe=True)
    
    def _display_clarity_attack_result(self, target, attack_pool, rolls, successes, ones,
                                       result_type, base_severity, stat_bonuses, wyrd):
        """Display the formatted Clarity attack result."""
        # Build header
        output = []
        output.append("|y" + "=" * 78 + "|n")
        title = f"CLARITY ATTACK - {target.name}"
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        # Attack pool breakdown
        output.append("|wClarity Attack Dice Pool:|n")
        breakdown = []
        breakdown.append(f"  Base Severity: {base_severity}")
        if stat_bonuses:
            for stat_name, stat_value in stat_bonuses:
                breakdown.append(f"  {stat_name.title()}: +{stat_value}")
        breakdown.append(f"  |cTotal: {attack_pool} dice|n")
        output.extend(breakdown)
        output.append("")
        
        # Roll results
        output.append("|wAttack Roll Results:|n")
        
        # Format dice rolls with color coding
        formatted_rolls = []
        for die in rolls:
            if die == 10:
                formatted_rolls.append(f"|g{die}|n")
            elif die >= 8:
                formatted_rolls.append(f"|c{die}|n")
            elif die == 1:
                formatted_rolls.append(f"|r{die}|n")
            else:
                formatted_rolls.append(f"|x{die}|n")
        
        output.append(f"  Rolls: {' '.join(formatted_rolls)}")
        output.append(f"  |cSuccesses: {successes}|n")
        if ones > 0:
            output.append(f"  |rOnes: {ones}|n")
        output.append("")
        
        # Result type
        if result_type == "dramatic_failure":
            output.append("|g" + "DRAMATIC FAILURE - NO DAMAGE!".center(78) + "|n")
        elif result_type == "failure":
            output.append("|g" + "FAILURE - NO DAMAGE".center(78) + "|n")
        elif result_type == "success":
            output.append("|y" + f"SUCCESS - ROLL WYRD ({wyrd} DICE) FOR MILD DAMAGE".center(78) + "|n")
        elif result_type == "exceptional_success":
            output.append("|r" + f"EXCEPTIONAL - ROLL WYRD ({wyrd} DICE) FOR SEVERE DAMAGE!".center(78) + "|n")
        
        output.append("|y" + "=" * 78 + "|n")
        
        # Send to roller and target (if different)
        message = "\n".join(output)
        self.caller.msg(message)
        if target != self.caller:
            target.msg(message)
        
        # Send to room
        room_msg = []
        room_msg.append(f"|c{target.name}|n experiences a Clarity attack.")
        if result_type == "dramatic_failure":
            room_msg.append("|g[Dramatic Failure - No Damage]|n")
        elif result_type == "failure":
            room_msg.append("|g[Failure - No Damage]|n")
        elif result_type == "success":
            room_msg.append("|y[Success - Mild Damage]|n")
        elif result_type == "exceptional_success":
            room_msg.append("|r[Exceptional - Severe Damage!]|n")
        
        # Announce to room (exclude self and staff if different)
        if target.location:
            exclude = [target]
            if self.caller != target:
                exclude.append(self.caller)
            target.location.msg_contents("\n".join(room_msg), exclude=exclude)
    
    def _handle_clarity_dramatic_failure(self, target):
        """Handle Clarity attack dramatic failure - no damage, regain Willpower, gain Beat."""
        target.msg("|gYou shake off the attack on your perception of reality!|n")
        
        # Award beat for dramatic failure
        if not hasattr(target, 'experience'):
            target.experience = ExperienceHandler(target)
        target.experience.add_beat(1)
        
        # Log the beat gain
        from world.xp_logger import get_xp_logger
        logger = get_xp_logger(target)
        logger.log_beat(1, "Clarity Attack Dramatic Failure", details="Resisted attack completely")
        
        target.msg("|yYou gain a Beat for dramatic failure!|n")
        
        # Regain 1 Willpower
        try:
            max_willpower = target.db.stats['advantages']['willpower']
        except (KeyError, TypeError):
            max_willpower = 3
        
        # Initialize willpower_current if it doesn't exist or is None
        if not hasattr(target.db, 'willpower_current') or target.db.willpower_current is None:
            target.db.willpower_current = max_willpower
        
        current_willpower = target.db.willpower_current
        
        # Handle case where current_willpower might still be None
        if current_willpower is None:
            current_willpower = max_willpower
            target.db.willpower_current = max_willpower
        
        if current_willpower < max_willpower:
            target.db.willpower_current = current_willpower + 1
            target.msg(f"|cYou regain 1 Willpower! Current: {target.db.willpower_current}/{max_willpower}|n")
        else:
            target.msg(f"|cYour Willpower is already at maximum ({max_willpower}).|n")
    
    def _handle_clarity_failure(self, target):
        """Handle Clarity attack failure - no damage."""
        target.msg("|gYou manage to maintain your grip on reality.|n")
    
    def perform_vampire_detachment(self, target, manual_modifier=0, stat_bonuses=None):
        """Perform a Humanity detachment roll for a Vampire."""
        # Get current Humanity to determine dice pool
        try:
            humanity = target.db.stats['other']['integrity']
        except (KeyError, TypeError):
            humanity = 7
        
        # Get the dice pool from Humanity level
        bp_data = get_breaking_points("vampire")
        if bp_data and humanity in bp_data["data"]:
            base_dice = bp_data["data"][humanity]["dice"]
        else:
            base_dice = 4  # Default
        
        # Add Touchstone bonuses (up to +2 dice)
        touchstone_bonus = 0
        bio_data = getattr(target.db, "bio_data", {})
        if bio_data:
            touchstones = bio_data.get("touchstones", []) or []
            touchstone_bonus = min(len(touchstones), 2)  # Maximum +2 from Touchstones
        
        # Get Bane penalties
        bane_penalty = 0
        banes = getattr(target.db, "banes", []) or []
        bane_penalty = -len(banes)  # -1 per Bane
        
        # Add stat bonuses if provided
        stat_bonus_total = 0
        if stat_bonuses:
            for stat_name, stat_value in stat_bonuses:
                stat_bonus_total += stat_value
        
        # Calculate total dice pool (Willpower cannot be spent on this)
        dice_pool = base_dice + touchstone_bonus + bane_penalty + manual_modifier + stat_bonus_total
        
        # Ensure minimum pool
        if dice_pool < 0:
            dice_pool = 0
        
        # Award Beat for facing breaking point (always)
        if not hasattr(target, 'experience'):
            target.experience = ExperienceHandler(target)
        target.experience.add_beat(1)
        
        # Log the beat gain
        from world.xp_logger import get_xp_logger
        logger = get_xp_logger(target)
        logger.log_beat(1, "Vampire Breaking Point", details=f"Humanity {humanity}")
        
        # Perform the roll
        rolls, successes, ones = roll_dice(dice_pool, 10, {RollType.NORMAL})
        
        # Determine result type (CoD 2e rules)
        result_type = "success"
        if dice_pool == 0 and ones >= 1:
            result_type = "dramatic_failure"
        elif successes == 0:
            result_type = "failure"
        elif successes >= 5:
            result_type = "exceptional_success"
        
        # Display the result
        self._display_vampire_detachment_result(target, dice_pool, rolls, successes, ones, result_type,
                                               humanity, base_dice, touchstone_bonus, bane_penalty, 
                                               manual_modifier, stat_bonuses, len(banes))
        
        # Store result for menu processing
        target.ndb.vampire_detachment_result = {
            'result_type': result_type,
            'successes': successes,
            'humanity': humanity,
            'caller': self.caller,
            'banes': banes
        }
        
        # Handle the result
        if result_type == "dramatic_failure":
            self._handle_vampire_dramatic_failure(target)
        elif result_type == "failure":
            self._handle_vampire_failure(target)
        elif result_type == "success":
            self._handle_vampire_success(target)
        elif result_type == "exceptional_success":
            self._handle_vampire_exceptional_success(target)
    
    def _display_vampire_detachment_result(self, target, dice_pool, rolls, successes, ones,
                                           result_type, humanity, base_dice, touchstone_bonus,
                                           bane_penalty, manual_modifier, stat_bonuses, num_banes):
        """Display the formatted Vampire detachment result."""
        # Build header
        output = []
        output.append("|y" + "=" * 78 + "|n")
        title = f"HUMANITY DETACHMENT ROLL - {target.name}"
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        output.append("|rYou gain a Beat for facing a breaking point.|n")
        output.append("")
        
        # Dice pool breakdown
        output.append("|wDice Pool:|n")
        breakdown = []
        breakdown.append(f"  Base (Humanity {humanity}): {base_dice}")
        if touchstone_bonus > 0:
            breakdown.append(f"  Touchstones: +{touchstone_bonus}")
        if num_banes > 0:
            breakdown.append(f"  Banes ({num_banes}): {bane_penalty}")
        if stat_bonuses:
            for stat_name, stat_value in stat_bonuses:
                breakdown.append(f"  {stat_name.title()}: +{stat_value}")
        if manual_modifier != 0:
            mod_sign = "+" if manual_modifier > 0 else ""
            breakdown.append(f"  Situational Modifier: {mod_sign}{manual_modifier}")
        breakdown.append(f"  |cTotal: {dice_pool} dice|n")
        output.extend(breakdown)
        output.append("")
        
        # Roll results
        output.append("|wRoll Results:|n")
        
        # Format dice rolls with color coding
        formatted_rolls = []
        for die in rolls:
            if die == 10:
                formatted_rolls.append(f"|g{die}|n")
            elif die >= 8:
                formatted_rolls.append(f"|c{die}|n")
            elif die == 1:
                formatted_rolls.append(f"|r{die}|n")
            else:
                formatted_rolls.append(f"|x{die}|n")
        
        output.append(f"  Rolls: {' '.join(formatted_rolls)}")
        output.append(f"  |cSuccesses: {successes}|n")
        if ones > 0:
            output.append(f"  |rOnes: {ones}|n")
        output.append("")
        
        # Result type
        if result_type == "dramatic_failure":
            output.append("|r" + "DRAMATIC FAILURE".center(78) + "|n")
        elif result_type == "failure":
            output.append("|y" + "FAILURE".center(78) + "|n")
        elif result_type == "success":
            output.append("|g" + "SUCCESS".center(78) + "|n")
        elif result_type == "exceptional_success":
            output.append("|G" + "EXCEPTIONAL SUCCESS!".center(78) + "|n")
        
        output.append("|y" + "=" * 78 + "|n")
        
        # Send to roller and target (if different)
        message = "\n".join(output)
        self.caller.msg(message)
        if target != self.caller:
            target.msg(message)
        
        # Send to room
        room_msg = []
        room_msg.append(f"|c{target.name}|n faces a test of Humanity.")
        if result_type == "dramatic_failure":
            room_msg.append("|r[Dramatic Failure]|n")
        elif result_type == "failure":
            room_msg.append("|y[Failure]|n")
        elif result_type == "success":
            room_msg.append("|g[Success]|n")
        elif result_type == "exceptional_success":
            room_msg.append("|G[Exceptional Success!]|n")
        
        # Announce to room (exclude self and staff if different)
        if target.location:
            exclude = [target]
            if self.caller != target:
                exclude.append(self.caller)
            target.location.msg_contents("\n".join(room_msg), exclude=exclude)
    
    def _handle_vampire_dramatic_failure(self, target):
        """Handle Vampire dramatic failure - lose Humanity, gain Jaded, option for Bane."""
        # Lose 1 Humanity
        try:
            current_humanity = target.db.stats['other']['integrity']
        except (KeyError, TypeError):
            current_humanity = 7
        
        new_humanity = max(0, current_humanity - 1)
        
        # Ensure the 'other' dict exists
        if 'other' not in target.db.stats:
            target.db.stats['other'] = {}
        target.db.stats['other']['integrity'] = new_humanity
        
        target.msg(f"|rYou lose 1 Humanity! New Humanity: {new_humanity}|n")
        target.msg(f"|rYou gain the Jaded Condition.|n")
        
        # Show Bane option menu
        EvMenu(target, {
            "vampire_bane_option_menu": vampire_bane_option_menu,
            "vampire_bane_selection_menu": vampire_bane_selection_menu,
            "_apply_vampire_bane": _apply_vampire_bane,
            "_skip_bane": _skip_bane
        }, startnode="vampire_bane_option_menu", persistent=False)
    
    def _handle_vampire_failure(self, target):
        """Handle Vampire failure - lose Humanity, choice of Bestial/Competitive/Wanton, option for Bane."""
        # Lose 1 Humanity
        try:
            current_humanity = target.db.stats['other']['integrity']
        except (KeyError, TypeError):
            current_humanity = 7
        
        new_humanity = max(0, current_humanity - 1)
        
        # Ensure the 'other' dict exists
        if 'other' not in target.db.stats:
            target.db.stats['other'] = {}
        target.db.stats['other']['integrity'] = new_humanity
        
        target.msg(f"|rYou lose 1 Humanity! New Humanity: {new_humanity}|n")
        
        # Show condition menu
        EvMenu(target, {
            "vampire_failure_condition_menu": vampire_failure_condition_menu,
            "vampire_bane_option_menu": vampire_bane_option_menu,
            "vampire_bane_selection_menu": vampire_bane_selection_menu,
            "_apply_vampire_condition_then_bane": _apply_vampire_condition_then_bane,
            "_apply_vampire_bane": _apply_vampire_bane,
            "_skip_bane": _skip_bane
        }, startnode="vampire_failure_condition_menu", persistent=False)
    
    def _handle_vampire_success(self, target):
        """Handle Vampire success - no Humanity loss, choice of Bestial/Competitive/Wanton."""
        target.msg("|gYou hold onto your Humanity!|n")
        
        # Show condition menu (no Bane option on success)
        EvMenu(target, {
            "vampire_success_condition_menu": vampire_success_condition_menu,
            "_apply_vampire_condition_success": _apply_vampire_condition_success
        }, startnode="vampire_success_condition_menu", persistent=False)
    
    def _handle_vampire_exceptional_success(self, target):
        """Handle Vampire exceptional success - no loss, gain Inspired Condition."""
        target.msg("|GYou hold onto your Humanity with renewed vigor!|n")
        target.msg("|cYou gain the Inspired Condition.|n")
        
        # Apply Inspired condition if it exists in system
        condition = STANDARD_CONDITIONS.get("inspired")
        if condition and hasattr(target, 'conditions'):
            target.conditions.add(condition)
        
        # Clean up stored data
        if hasattr(target.ndb, 'vampire_detachment_result'):
            del target.ndb.vampire_detachment_result
    
    def _handle_clarity_success(self, target, wyrd, severe=False):
        """Handle Clarity attack success - roll Wyrd for damage."""
        from world.cofd.clarity_utils import add_clarity_damage
        
        # Roll Wyrd for damage
        damage_rolls, damage_successes, damage_ones = roll_dice(wyrd, 10, {RollType.NORMAL})
        
        # Format damage roll display
        formatted_rolls = []
        for die in damage_rolls:
            if die == 10:
                formatted_rolls.append(f"|g{die}|n")
            elif die >= 8:
                formatted_rolls.append(f"|c{die}|n")
            elif die == 1:
                formatted_rolls.append(f"|r{die}|n")
            else:
                formatted_rolls.append(f"|x{die}|n")
        
        damage_type = "severe" if severe else "mild"
        
        target.msg("")
        target.msg("|y" + "=" * 78 + "|n")
        target.msg(f"|wClarity Damage Roll (Wyrd {wyrd}):|n")
        target.msg(f"  Rolls: {' '.join(formatted_rolls)}")
        target.msg(f"  |cDamage: {damage_successes} points of {damage_type} damage|n")
        target.msg("|y" + "=" * 78 + "|n")
        target.msg("")
        
        # Award beat for exceptional success
        if severe:  # Exceptional success
            if not hasattr(target, 'experience'):
                target.experience = ExperienceHandler(target)
            target.experience.add_beat(1)
            
            # Log the beat gain
            from world.xp_logger import get_xp_logger
            logger = get_xp_logger(target)
            logger.log_beat(1, "Clarity Attack Exceptional Success", details=f"Severe damage: {damage_successes}")
            
            target.msg("|yYou gain a Beat for exceptional success!|n")
        
        # Apply damage
        if damage_successes > 0:
            success, msg, condition_triggered = add_clarity_damage(target, damage_type, damage_successes)
            target.msg(msg)
            
            # If condition triggered, show menu
            if condition_triggered:
                # Store data for menu
                target.ndb.clarity_condition_result = {
                    'damage_type': damage_type,
                    'caller': self.caller
                }
                
                # Show appropriate condition menu based on damage type
                if severe:
                    EvMenu(target, {
                        "clarity_persistent_condition_menu": clarity_persistent_condition_menu,
                        "_apply_clarity_condition": _apply_clarity_condition
                    }, startnode="clarity_persistent_condition_menu", persistent=False)
                else:
                    EvMenu(target, {
                        "clarity_regular_condition_menu": clarity_regular_condition_menu,
                        "_apply_clarity_condition": _apply_clarity_condition
                    }, startnode="clarity_regular_condition_menu", persistent=False)
        else:
            target.msg("|gNo damage taken|n")
    
    def _display_breaking_point_result(self, target, dice_pool, rolls, successes, ones, 
                                        result_type, integrity, resolve, composure, 
                                        auto_modifier, manual_modifier, stat_bonuses=None):
        """Display the formatted breaking point roll result."""
        # Build header
        output = []
        output.append("|y" + "=" * 78 + "|n")
        title = f"BREAKING POINT ROLL - {target.name}"
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        # Pool breakdown
        output.append("|wDice Pool:|n")
        breakdown = []
        breakdown.append(f"  Resolve: {resolve}")
        breakdown.append(f"  Composure: {composure}")
        if auto_modifier != 0:
            mod_sign = "+" if auto_modifier > 0 else ""
            breakdown.append(f"  Integrity Modifier ({integrity}): {mod_sign}{auto_modifier}")
        if stat_bonuses:
            for stat_name, stat_value in stat_bonuses:
                breakdown.append(f"  {stat_name.title()}: +{stat_value}")
        if manual_modifier != 0:
            mod_sign = "+" if manual_modifier > 0 else ""
            breakdown.append(f"  Situational Modifier: {mod_sign}{manual_modifier}")
        breakdown.append(f"  |cTotal: {dice_pool} dice|n")
        output.extend(breakdown)
        output.append("")
        
        # Roll results
        output.append("|wRoll Results:|n")
        
        # Format dice rolls with color coding
        formatted_rolls = []
        for die in rolls:
            if die == 10:
                formatted_rolls.append(f"|g{die}|n")
            elif die >= 8:
                formatted_rolls.append(f"|c{die}|n")
            elif die == 1:
                formatted_rolls.append(f"|r{die}|n")
            else:
                formatted_rolls.append(f"|x{die}|n")
        
        output.append(f"  Rolls: {' '.join(formatted_rolls)}")
        output.append(f"  |cSuccesses: {successes}|n")
        if ones > 0:
            output.append(f"  |rOnes: {ones}|n")
        output.append("")
        
        # Result type
        if result_type == "dramatic_failure":
            output.append("|r" + "DRAMATIC FAILURE".center(78) + "|n")
        elif result_type == "failure":
            output.append("|y" + "FAILURE".center(78) + "|n")
        elif result_type == "success":
            output.append("|g" + "SUCCESS".center(78) + "|n")
        elif result_type == "exceptional_success":
            output.append("|G" + "EXCEPTIONAL SUCCESS!".center(78) + "|n")
        
        output.append("|y" + "=" * 78 + "|n")
        
        # Send to roller and target (if different)
        message = "\n".join(output)
        self.caller.msg(message)
        if target != self.caller:
            target.msg(message)
        
        # Send to room
        room_msg = []
        room_msg.append(f"|c{target.name}|n makes a breaking point roll.")
        if result_type == "dramatic_failure":
            room_msg.append("|r[Dramatic Failure]|n")
        elif result_type == "failure":
            room_msg.append("|y[Failure]|n")
        elif result_type == "success":
            room_msg.append("|g[Success]|n")
        elif result_type == "exceptional_success":
            room_msg.append("|G[Exceptional Success!]|n")
        
        # Announce to room (exclude self and staff if different)
        if target.location:
            exclude = [target]
            if self.caller != target:
                exclude.append(self.caller)
            target.location.msg_contents("\n".join(room_msg), exclude=exclude)
    
    def _handle_dramatic_failure(self, target):
        """Handle dramatic failure result - lose integrity, severe condition, gain beat."""
        # Lose 1 integrity
        try:
            current_integrity = target.db.stats['other']['integrity']
        except (KeyError, TypeError):
            current_integrity = 7
        
        new_integrity = max(0, current_integrity - 1)
        
        # Ensure the 'other' dict exists
        if 'other' not in target.db.stats:
            target.db.stats['other'] = {}
        target.db.stats['other']['integrity'] = new_integrity
        
        msg = f"|rYou lose 1 Integrity! New Integrity: {new_integrity}|n\n"
        msg += "|yYou gain a Beat for suffering a dramatic failure.|n"
        target.msg(msg)
        
        # Award beat
        if not hasattr(target, 'experience'):
            target.experience = ExperienceHandler(target)
        target.experience.add_beat(1)
        
        # Log the beat gain
        from world.xp_logger import get_xp_logger
        logger = get_xp_logger(target)
        logger.log_beat(1, "Breaking Point Dramatic Failure", details=f"Integrity: {new_integrity}")
        
        # Show condition menu for severe conditions
        EvMenu(target, {
            "breaking_point_dramatic_menu": breaking_point_dramatic_menu,
            "_apply_breaking_point_condition": _apply_breaking_point_condition
        }, startnode="breaking_point_dramatic_menu", persistent=False)
    
    def _handle_failure(self, target):
        """Handle failure result - lose integrity, minor condition."""
        # Lose 1 integrity
        try:
            current_integrity = target.db.stats['other']['integrity']
        except (KeyError, TypeError):
            current_integrity = 7
        
        new_integrity = max(0, current_integrity - 1)
        
        # Ensure the 'other' dict exists
        if 'other' not in target.db.stats:
            target.db.stats['other'] = {}
        target.db.stats['other']['integrity'] = new_integrity
        
        target.msg(f"|rYou lose 1 Integrity! New Integrity: {new_integrity}|n")
        
        # Show condition menu for minor conditions
        EvMenu(target, {
            "breaking_point_failure_menu": breaking_point_failure_menu,
            "_apply_breaking_point_condition": _apply_breaking_point_condition
        }, startnode="breaking_point_failure_menu", persistent=False)
    
    def _handle_success(self, target):
        """Handle success result - no integrity loss, minor condition."""
        target.msg("|gYou manage to hold yourself together.|n")
        
        # Show condition menu for minor conditions
        EvMenu(target, {
            "breaking_point_success_menu": breaking_point_success_menu,
            "_apply_breaking_point_condition": _apply_breaking_point_condition
        }, startnode="breaking_point_success_menu", persistent=False)
    
    def _handle_exceptional_success(self, target):
        """Handle exceptional success - gain beat and temporary willpower."""
        target.msg("|GYou not only survive the breaking point but find meaning in it!|n")
        
        # Award beat
        if not hasattr(target, 'experience'):
            target.experience = ExperienceHandler(target)
        target.experience.add_beat(1)
        
        # Log the beat gain
        from world.xp_logger import get_xp_logger
        logger = get_xp_logger(target)
        logger.log_beat(1, "Breaking Point Exceptional Success", details="Found meaning")
        
        target.msg("|yYou gain a Beat!|n")
        
        # Gain 1 temporary willpower
        try:
            max_willpower = target.db.stats['advantages']['willpower']
        except (KeyError, TypeError):
            max_willpower = 3
        
        if not hasattr(target.db, 'willpower_current'):
            target.db.willpower_current = max_willpower
        
        current_willpower = target.db.willpower_current
        
        if current_willpower < max_willpower:
            target.db.willpower_current = current_willpower + 1
            target.msg(f"|cYou regain 1 Willpower! Current: {target.db.willpower_current}/{max_willpower}|n")
        else:
            target.msg(f"|cYour Willpower is already at maximum ({max_willpower}).|n")


# EvMenu functions for Vampire detachment

def vampire_failure_condition_menu(caller):
    """Menu for Vampire failure - Bestial/Competitive/Wanton."""
    text = "|y=== HUMANITY LOSS - CONDITION ===|n\n\n"
    text += "You let go of your mortal attachments and move toward monstrosity.\n"
    text += "Choose a Condition:\n\n"
    text += "  |w1|n - |rBestial|n - Your Beast nature emerges\n"
    text += "  |w2|n - |rCompetitive|n - You must dominate others\n"
    text += "  |w3|n - |rWanton|n - You revel in selfish desires\n"
    text += "\nType the number of your choice:\n"
    
    options = (
        {"key": "1", "desc": "Bestial", "goto": "_apply_vampire_condition_then_bane"},
        {"key": "2", "desc": "Competitive", "goto": "_apply_vampire_condition_then_bane"},
        {"key": "3", "desc": "Wanton", "goto": "_apply_vampire_condition_then_bane"},
        {"key": "_default", "goto": "vampire_failure_condition_menu"}
    )
    
    return text, options


def vampire_success_condition_menu(caller):
    """Menu for Vampire success - Bestial/Competitive/Wanton."""
    text = "|g=== HUMANITY MAINTAINED - CONDITION ===|n\n\n"
    text += "You hold onto your Humanity, but your nature pushes you to withdraw.\n"
    text += "Choose a Condition:\n\n"
    text += "  |w1|n - |yBestial|n - Your Beast nature emerges\n"
    text += "  |w2|n - |yCompetitive|n - You must dominate others\n"
    text += "  |w3|n - |yWanton|n - You revel in selfish desires\n"
    text += "\nType the number of your choice:\n"
    
    options = (
        {"key": "1", "desc": "Bestial", "goto": "_apply_vampire_condition_success"},
        {"key": "2", "desc": "Competitive", "goto": "_apply_vampire_condition_success"},
        {"key": "3", "desc": "Wanton", "goto": "_apply_vampire_condition_success"},
        {"key": "_default", "goto": "vampire_success_condition_menu"}
    )
    
    return text, options


def vampire_bane_option_menu(caller):
    """Menu to choose whether to take a Bane."""
    result_data = caller.ndb.vampire_detachment_result
    if not result_data:
        return "Error: No detachment data found.", None
    
    banes = result_data.get('banes', [])
    num_banes = len(banes)
    
    if num_banes >= 3:
        caller.msg("|rYou already have 3 Banes (maximum). Cannot take another.|n")
        # Clean up and close
        del caller.ndb.vampire_detachment_result
        return None, None
    
    text = "|y=== OPTIONAL: TAKE A BANE ===|n\n\n"
    text += "You may take a Bane to prevent future Humanity loss from this breaking point.\n\n"
    text += "|wBenefits:|n\n"
    text += "  • Gain 1 additional Beat\n"
    text += "  • Cannot lose Humanity from this breaking point again\n\n"
    text += "|rDrawbacks:|n\n"
    text += f"  • -1 die penalty to all future detachment rolls (currently {num_banes}, would be {num_banes + 1})\n"
    text += f"  • Maximum 3 Banes allowed\n\n"
    text += "Do you want to take a Bane?\n\n"
    text += "  |w1|n - Yes, take a Bane (+1 Beat, -1 future detachment)\n"
    text += "  |w2|n - No, continue without a Bane\n"
    
    options = (
        {"key": "1", "desc": "Take a Bane", "goto": "vampire_bane_selection_menu"},
        {"key": "2", "desc": "Skip Bane", "goto": "_skip_bane"},
        {"key": "_default", "goto": "vampire_bane_option_menu"}
    )
    
    return text, options


def vampire_bane_selection_menu(caller):
    """Menu to select which Bane to take."""
    from world.cofd.integrity_systems import VAMPIRE_BANES
    
    text = "|r=== SELECT YOUR BANE ===|n\n\n"
    text += "Choose a Bane that represents your vampire's spiritual scars:\n\n"
    
    banes_list = list(VAMPIRE_BANES.items())
    for i, (key, bane_data) in enumerate(banes_list, 1):
        text += f"  |w{i:2d}|n - |c{bane_data['name']}|n\n"
        text += f"       |x{bane_data['description'][:70]}...|n\n"
    
    text += "\nType the number of your choice:\n"
    
    # Build options dynamically
    options = []
    for i in range(1, len(banes_list) + 1):
        options.append({
            "key": str(i),
            "desc": banes_list[i-1][1]['name'],
            "goto": "_apply_vampire_bane"
        })
    
    options.append({"key": "_default", "goto": "vampire_bane_selection_menu"})
    
    return text, tuple(options)


def _apply_vampire_condition_then_bane(caller, raw_string):
    """Apply chosen condition (failure case) then show Bane option."""
    result_data = caller.ndb.vampire_detachment_result
    if not result_data:
        caller.msg("Error: No detachment data found.")
        return None, None
    
    # Map selection to condition
    condition_map = {
        '1': 'bestial',
        '2': 'competitive',
        '3': 'wanton'
    }
    
    selection = raw_string.strip()
    condition_key = condition_map.get(selection)
    
    if not condition_key:
        caller.msg("Invalid selection. Please choose 1, 2, or 3.")
        return "vampire_failure_condition_menu", None
    
    # Apply the condition
    condition = STANDARD_CONDITIONS.get(condition_key)
    if condition and hasattr(caller, 'conditions'):
        caller.conditions.add(condition)
        caller.msg(f"\n|gYou have gained the Condition: |w{condition.name}|n")
    else:
        caller.msg(f"\n|gYou accept the Condition: {condition_key.title()}|n")
    
    # Continue to Bane option
    return "vampire_bane_option_menu", None


def _apply_vampire_condition_success(caller, raw_string):
    """Apply chosen condition (success case) and close."""
    result_data = caller.ndb.vampire_detachment_result
    if not result_data:
        caller.msg("Error: No detachment data found.")
        return None, None
    
    # Map selection to condition
    condition_map = {
        '1': 'bestial',
        '2': 'competitive',
        '3': 'wanton'
    }
    
    selection = raw_string.strip()
    condition_key = condition_map.get(selection)
    
    if not condition_key:
        caller.msg("Invalid selection. Please choose 1, 2, or 3.")
        return "vampire_success_condition_menu", None
    
    # Apply the condition
    condition = STANDARD_CONDITIONS.get(condition_key)
    if condition and hasattr(caller, 'conditions'):
        caller.conditions.add(condition)
        caller.msg(f"\n|gYou have gained the Condition: |w{condition.name}|n")
    else:
        caller.msg(f"\n|gYou accept the Condition: {condition_key.title()}|n")
    
    # Clean up and close
    del caller.ndb.vampire_detachment_result
    return None, None


def _apply_vampire_bane(caller, raw_string):
    """Apply selected Bane to the vampire."""
    from world.cofd.integrity_systems import VAMPIRE_BANES
    
    result_data = caller.ndb.vampire_detachment_result
    if not result_data:
        caller.msg("Error: No detachment data found.")
        return None, None
    
    banes_list = list(VAMPIRE_BANES.items())
    
    try:
        selection = int(raw_string.strip())
        if selection < 1 or selection > len(banes_list):
            caller.msg("Invalid selection.")
            return "vampire_bane_selection_menu", None
        
        bane_key = banes_list[selection - 1][0]
        bane_data = banes_list[selection - 1][1]
    except (ValueError, TypeError):
        caller.msg("Invalid selection.")
        return "vampire_bane_selection_menu", None
    
    # Initialize banes list if needed
    if not hasattr(caller.db, 'banes') or caller.db.banes is None:
        caller.db.banes = []
    
    # Add the Bane
    caller.db.banes.append(bane_key)
    
    caller.msg(f"\n|rYou have gained the Bane: |w{bane_data['name']}|n")
    caller.msg(f"|x{bane_data['description']}|n")
    caller.msg(f"\n|yYou gain an additional Beat for taking this Bane!|n")
    
    # Award the Bane beat
    if not hasattr(caller, 'experience'):
        caller.experience = ExperienceHandler(caller)
    caller.experience.add_beat(1)
    
    # Log the beat gain
    from world.xp_logger import get_xp_logger
    logger = get_xp_logger(caller)
    logger.log_beat(1, "Vampire Bane Taken", details=f"Bane: {bane_data['name']}")
    
    # Clean up and close
    del caller.ndb.vampire_detachment_result
    return None, None


def _skip_bane(caller, raw_string):
    """Skip taking a Bane and close the menu."""
    caller.msg("|yYou choose not to take a Bane at this time.|n")
    
    # Clean up and close
    if hasattr(caller.ndb, 'vampire_detachment_result'):
        del caller.ndb.vampire_detachment_result
    
    return None, None


# EvMenu functions for breaking point condition selection

def breaking_point_dramatic_menu(caller):
    """Menu for dramatic failure - severe conditions."""
    text = "|r=== DRAMATIC FAILURE - SEVERE CONDITION ===|n\n\n"
    text += "Your worldview has been damaged, perhaps beyond repair.\n"
    text += "Choose a severe Condition:\n\n"
    text += "  |w1|n - |rBroken|n - You feel utterly defeated and hopeless\n"
    text += "  |w2|n - |rFugue|n - You lose time and memory, dissociating from reality\n"
    text += "  |w3|n - |rMadness|n - Your grip on sanity has been compromised\n"
    text += "\nType the number of your choice:\n"
    
    options = (
        {"key": "1", "desc": "Broken", "goto": "_apply_breaking_point_condition"},
        {"key": "2", "desc": "Fugue", "goto": "_apply_breaking_point_condition"},
        {"key": "3", "desc": "Madness", "goto": "_apply_breaking_point_condition"},
        {"key": "_default", "goto": "breaking_point_dramatic_menu"}
    )
    
    return text, options


def breaking_point_failure_menu(caller):
    """Menu for failure - minor conditions."""
    text = "|y=== FAILURE - MINOR CONDITION ===|n\n\n"
    text += "Your worldview has been shaken. Choose a Condition:\n\n"
    text += "  |w1|n - |yGuilty|n - You feel responsible and ashamed\n"
    text += "  |w2|n - |yShaken|n - You are rattled and off-balance\n"
    text += "  |w3|n - |ySpooked|n - You are frightened and anxious\n"
    text += "\nType the number of your choice:\n"
    
    options = (
        {"key": "1", "desc": "Guilty", "goto": "_apply_breaking_point_condition"},
        {"key": "2", "desc": "Shaken", "goto": "_apply_breaking_point_condition"},
        {"key": "3", "desc": "Spooked", "goto": "_apply_breaking_point_condition"},
        {"key": "_default", "goto": "breaking_point_failure_menu"}
    )
    
    return text, options


def breaking_point_success_menu(caller):
    """Menu for success - minor conditions."""
    text = "|g=== SUCCESS - MINOR CONDITION ===|n\n\n"
    text += "You've come through intact, but the experience still affects you.\n"
    text += "Choose a Condition:\n\n"
    text += "  |w1|n - |yGuilty|n - You feel responsible and ashamed\n"
    text += "  |w2|n - |yShaken|n - You are rattled and off-balance\n"
    text += "  |w3|n - |ySpooked|n - You are frightened and anxious\n"
    text += "\nType the number of your choice:\n"
    
    options = (
        {"key": "1", "desc": "Guilty", "goto": "_apply_breaking_point_condition"},
        {"key": "2", "desc": "Shaken", "goto": "_apply_breaking_point_condition"},
        {"key": "3", "desc": "Spooked", "goto": "_apply_breaking_point_condition"},
        {"key": "_default", "goto": "breaking_point_success_menu"}
    )
    
    return text, options


def _apply_breaking_point_condition(caller, raw_string):
    """Apply the chosen condition and close the menu."""
    # Get the stored result data
    result_data = caller.ndb.breaking_point_result
    if not result_data:
        caller.msg("Error: No breaking point data found.")
        return None, None
    
    result_type = result_data['result_type']
    
    # Map selection to condition
    condition_map = {
        'dramatic_failure': {
            '1': 'broken',
            '2': 'fugue',
            '3': 'madness'
        },
        'failure': {
            '1': 'guilty',
            '2': 'shaken',
            '3': 'spooked'
        },
        'success': {
            '1': 'guilty',
            '2': 'shaken',
            '3': 'spooked'
        }
    }
    
    # Get the selected condition
    try:
        selection = raw_string.strip()
        condition_key = condition_map[result_type].get(selection)
        
        if not condition_key:
            caller.msg("Invalid selection. Please choose 1, 2, or 3.")
            # Return to the appropriate menu
            if result_type == 'dramatic_failure':
                return "breaking_point_dramatic_menu", None
            elif result_type == 'failure':
                return "breaking_point_failure_menu", None
            else:
                return "breaking_point_success_menu", None
        
    except (ValueError, TypeError, KeyError):
        caller.msg("Invalid selection.")
        return None, None
    
    # Get the condition from STANDARD_CONDITIONS
    condition = STANDARD_CONDITIONS.get(condition_key)
    if not condition:
        caller.msg(f"Error: Condition '{condition_key}' not found in system.")
        return None, None
    
    # Add the condition to the character
    if hasattr(caller, 'conditions'):
        caller.conditions.add(condition)
        caller.msg(f"\n|gYou have gained the Condition: |w{condition.name}|n")
        caller.msg(f"|x{condition.description}|n")
    else:
        caller.msg(f"\n|gYou accept the Condition: |w{condition.name}|n")
        caller.msg(f"|x{condition.description}|n")
    
    # Clean up the stored data
    del caller.ndb.breaking_point_result
    
    # Close the menu
    return None, None


# EvMenu functions for Clarity condition selection

def clarity_regular_condition_menu(caller):
    """Menu for Clarity damage - regular Clarity Conditions."""
    text = "|y=== CLARITY DAMAGE - REGULAR CONDITION ===|n\n\n"
    text += "Your grip on reality has been shaken.\n"
    text += "Choose a Clarity Condition:\n\n"
    text += "  |w1|n - |cComatose|n - Lost in your own dreams\n"
    text += "  |w2|n - |cConfused|n - Reality is uncertain\n"
    text += "  |w3|n - |cDissociation|n - Disconnected from yourself\n"
    text += "  |w4|n - |cDistracted|n - Unable to focus properly\n"
    text += "  |w5|n - |cShaken|n - Rattled and off-balance\n"
    text += "  |w6|n - |cSpooked|n - Frightened and anxious\n"
    text += "\nType the number of your choice:\n"
    
    options = (
        {"key": "1", "desc": "Comatose", "goto": "_apply_clarity_condition"},
        {"key": "2", "desc": "Confused", "goto": "_apply_clarity_condition"},
        {"key": "3", "desc": "Dissociation", "goto": "_apply_clarity_condition"},
        {"key": "4", "desc": "Distracted", "goto": "_apply_clarity_condition"},
        {"key": "5", "desc": "Shaken", "goto": "_apply_clarity_condition"},
        {"key": "6", "desc": "Spooked", "goto": "_apply_clarity_condition"},
        {"key": "_default", "goto": "clarity_regular_condition_menu"}
    )
    
    return text, options


def clarity_persistent_condition_menu(caller):
    """Menu for severe Clarity damage - Persistent Clarity Conditions."""
    text = "|r=== SEVERE CLARITY DAMAGE - PERSISTENT CONDITION ===|n\n\n"
    text += "Your perception of reality has been fundamentally damaged.\n"
    text += "Choose a Persistent Clarity Condition:\n\n"
    text += "  |w1|n - |rBroken|n (Persistent) - Utterly defeated and hopeless\n"
    text += "  |w2|n - |rDelusional|n (Persistent) - False beliefs and perceptions\n"
    text += "  |w3|n - |rFugue|n (Persistent) - Lost time and dissociation\n"
    text += "  |w4|n - |rNumb|n (Persistent) - Emotionally disconnected\n"
    text += "  |w5|n - |rSleepwalking|n (Persistent) - Acting without awareness\n"
    text += "\nType the number of your choice:\n"
    
    options = (
        {"key": "1", "desc": "Broken", "goto": "_apply_clarity_condition"},
        {"key": "2", "desc": "Delusional", "goto": "_apply_clarity_condition"},
        {"key": "3", "desc": "Fugue", "goto": "_apply_clarity_condition"},
        {"key": "4", "desc": "Numb", "goto": "_apply_clarity_condition"},
        {"key": "5", "desc": "Sleepwalking", "goto": "_apply_clarity_condition"},
        {"key": "_default", "goto": "clarity_persistent_condition_menu"}
    )
    
    return text, options


def _apply_clarity_condition(caller, raw_string):
    """Apply the chosen Clarity condition and close the menu."""
    # Get the stored result data
    result_data = caller.ndb.clarity_condition_result
    if not result_data:
        caller.msg("Error: No Clarity condition data found.")
        return None, None
    
    damage_type = result_data['damage_type']
    
    # Map selection to condition based on damage type
    from world.cofd.clarity_utils import CLARITY_CONDITIONS_REGULAR, CLARITY_CONDITIONS_PERSISTENT
    
    if damage_type == "severe":
        condition_list = CLARITY_CONDITIONS_PERSISTENT
        condition_map = {
            '1': 'broken',
            '2': 'delusional',
            '3': 'fugue',
            '4': 'numb',
            '5': 'sleepwalking'
        }
        menu_node = "clarity_persistent_condition_menu"
    else:
        condition_list = CLARITY_CONDITIONS_REGULAR
        condition_map = {
            '1': 'comatose',
            '2': 'confused',
            '3': 'dissociation',
            '4': 'distracted',
            '5': 'shaken',
            '6': 'spooked'
        }
        menu_node = "clarity_regular_condition_menu"
    
    # Get the selected condition
    try:
        selection = raw_string.strip()
        condition_key = condition_map.get(selection)
        
        if not condition_key:
            caller.msg("Invalid selection. Please choose a valid number.")
            return menu_node, None
        
    except (ValueError, TypeError, KeyError):
        caller.msg("Invalid selection.")
        return None, None
    
    # Get the condition from STANDARD_CONDITIONS
    condition = STANDARD_CONDITIONS.get(condition_key)
    if not condition:
        caller.msg(f"|yCondition '{condition_key}' not found in system. Manually add with +condition/add {condition_key}|n")
        # Clean up and close
        del caller.ndb.clarity_condition_result
        return None, None
    
    # Add the condition to the character
    if hasattr(caller, 'conditions'):
        caller.conditions.add(condition)
        caller.msg(f"\n|gYou have gained the Clarity Condition: |w{condition.name}|n")
        caller.msg(f"|x{condition.description}|n")
    else:
        caller.msg(f"\n|gYou accept the Clarity Condition: |w{condition.name}|n")
        caller.msg(f"|x{condition.description}|n")
    
    # Clean up the stored data
    del caller.ndb.clarity_condition_result
    
    # Close the menu
    return None, None
