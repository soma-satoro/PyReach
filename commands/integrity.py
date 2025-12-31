from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from evennia.utils.evmenu import EvMenu
from world.experience import ExperienceHandler
from world.conditions import STANDARD_CONDITIONS
from world.utils.dice_utils import roll_dice, RollType
from utils.search_helpers import search_character

class CmdIntegrity(MuxCommand):
    """
    Make breaking point rolls and manage integrity.
    
    Usage:
        +integrity - Make a breaking point roll for yourself
        +integrity <character> - Staff: Make a breaking point roll for another character
        +integrity +<value> - Make a breaking point roll with a positive modifier
        +integrity -<value> - Make a breaking point roll with a negative modifier
        
    Breaking point rolls use Resolve + Composure with an automatic modifier
    based on your current Integrity:
        
        Integrity 8-10: +2 dice
        Integrity 6-7:  +1 die
        Integrity 4-5:  No modifier
        Integrity 2-3:  -1 die
        Integrity 1:    -2 dice
        
    Results:
        Dramatic Failure: Lose 1 Integrity, choose a severe Condition (Broken, 
                         Fugue, or Madness), gain a Beat
        Failure:         Lose 1 Integrity, choose a minor Condition (Guilty, 
                         Shaken, or Spooked)
        Success:         No Integrity loss, choose a minor Condition (Guilty, 
                         Shaken, or Spooked)
        Exceptional:     Gain a Beat and 1 temporary Willpower (up to max)
        
    Examples:
        +integrity - Make a breaking point roll
        +integrity +2 - Make a breaking point roll with +2 modifier
        +integrity -1 - Make a breaking point roll with -1 penalty
        +integrity John - Staff: Force a breaking point roll for John
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
        
        # Parse the arguments
        target = self.caller
        manual_modifier = 0
        
        if self.args:
            args = self.args.strip()
            
            # Check if it's a modifier (+/-value)
            if args.startswith('+') or args.startswith('-'):
                try:
                    manual_modifier = int(args)
                except ValueError:
                    self.caller.msg("Invalid modifier. Use +integrity +<value> or +integrity -<value>")
                    return
            else:
                # It's a character name - staff only
                if not self.caller.check_permstring("Admin"):
                    self.caller.msg("|rOnly staff can make breaking point rolls for other characters.|n")
                    return
                
                target = search_character(self.caller, args)
                if not target:
                    return
        
        # Perform the breaking point roll
        self.perform_breaking_point_roll(target, manual_modifier)
    
    def perform_breaking_point_roll(self, target, manual_modifier=0):
        """Perform a breaking point roll for a character."""
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
        
        # Calculate total dice pool
        dice_pool = resolve + composure + auto_modifier + manual_modifier
        
        # Ensure minimum pool
        if dice_pool < 0:
            dice_pool = 0
        
        # Perform the roll
        rolls, successes, ones = roll_dice(dice_pool, 10, {RollType.NORMAL})
        
        # Determine result type
        result_type = "success"
        if successes == 0 and ones >= 1 and dice_pool == 0:
            result_type = "dramatic_failure"
        elif successes == 0:
            result_type = "failure"
        elif successes >= 5:
            result_type = "exceptional_success"
        
        # Format and display the roll result
        self._display_breaking_point_result(target, dice_pool, rolls, successes, ones, result_type, 
                                            integrity, resolve, composure, auto_modifier, manual_modifier)
        
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
    
    def _display_breaking_point_result(self, target, dice_pool, rolls, successes, ones, 
                                        result_type, integrity, resolve, composure, 
                                        auto_modifier, manual_modifier):
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
