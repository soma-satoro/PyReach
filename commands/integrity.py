from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.experience import ExperienceHandler
from world.conditions import STANDARD_CONDITIONS

class CmdIntegrity(MuxCommand):
    """
    Manage breaking points and integrity.
    
    Usage:
        +integrity/check - Check your current integrity
        +integrity/roll <modifier> - Make a breaking point roll
        +integrity/lose <amount> - Lose integrity points
        +integrity/gain <amount> - Gain integrity points
        +integrity/condition <condition> - Add a condition from breaking point
        
    Breaking point rolls are made with Resolve + Composure + modifiers.
    The difficulty is based on your current integrity level.
    """
    key = "+integrity"
    aliases = ["+int"]
    help_category = "Skill and Condition Checks"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
        
        args = self.args.strip()
        self.switches = []
    def func(self):
        """Execute the command"""
        if not self.switches:
            self.caller.msg("Usage: +integrity/check, +integrity/roll, +integrity/lose, +integrity/gain, or +integrity/condition")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "check":
            self.check_integrity()
        elif switch == "roll":
            self.breaking_point_roll()
        elif switch == "lose":
            self.lose_integrity()
        elif switch == "gain":
            self.gain_integrity()
        elif switch == "condition":
            self.add_condition()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def check_integrity(self):
        """Check current integrity"""
        integrity = self.caller.db.integrity or 7  # Default for mortals
        
        # Get integrity level description
        if integrity >= 8:
            level = "High"
        elif integrity >= 6:
            level = "Good"
        elif integrity >= 4:
            level = "Average"
        elif integrity >= 2:
            level = "Low"
        else:
            level = "Critical"
            
        self.caller.msg(f"Current Integrity: {integrity} ({level})")
    
    def breaking_point_roll(self):
        """Make a breaking point roll"""
        try:
            modifier = int(self.args)
        except ValueError:
            self.caller.msg("Usage: +integrity/roll <modifier>")
            return
            
        # Get current integrity
        integrity = self.caller.db.integrity or 7
        
        # Calculate difficulty based on integrity
        if integrity >= 8:
            difficulty = 3
        elif integrity >= 6:
            difficulty = 4
        elif integrity >= 4:
            difficulty = 5
        elif integrity >= 2:
            difficulty = 6
        else:
            difficulty = 7
            
        # Calculate dice pool
        resolve = self.caller.db.attributes["mental"]["resolve"]
        composure = self.caller.db.attributes["social"]["composure"]
        dice_pool = resolve + composure + modifier
        
        self.caller.msg(f"Making breaking point roll")
        self.caller.msg(f"Current integrity: {integrity}")
        self.caller.msg(f"Difficulty: {difficulty}")
        self.caller.msg(f"Dice pool: {dice_pool}")
        
        # Use the existing roll command
        self.caller.execute_cmd(f"+roll {dice_pool}")
        
        # Store the difficulty for condition application
        self.caller.db.last_breaking_point = {
            "difficulty": difficulty,
            "successes": 0  # Will be updated by roll command
        }
    
    def lose_integrity(self):
        """Lose integrity points"""
        try:
            amount = int(self.args)
        except ValueError:
            self.caller.msg("Usage: +integrity/lose <amount>")
            return
            
        current = self.caller.db.integrity or 7
        new = max(0, current - amount)
        
        self.caller.db.integrity = new
        self.caller.msg(f"Lost {amount} integrity. New total: {new}")
        
        # Check for beat generation
        if amount > 0:
            if not hasattr(self.caller, 'experience'):
                self.caller.experience = ExperienceHandler(self.caller)
            self.caller.experience.add_beat(1)
            
            # Log the beat gain
            from world.xp_logger import get_xp_logger
            logger = get_xp_logger(self.caller)
            logger.log_beat(1, "Breaking Point", details=f"Risked breaking point, lost {amount} integrity")
            
            self.caller.msg("|yBeat gained for risking breaking point!|n")
    
    def gain_integrity(self):
        """Gain integrity points"""
        try:
            amount = int(self.args)
        except ValueError:
            self.caller.msg("Usage: +integrity/gain <amount>")
            return
            
        current = self.caller.db.integrity or 7
        new = min(10, current + amount)
        
        self.caller.db.integrity = new
        self.caller.msg(f"Gained {amount} integrity. New total: {new}")
    
    def add_condition(self):
        """Add a condition from breaking point"""
        condition_name = self.args.strip().lower()
        
        if condition_name not in STANDARD_CONDITIONS:
            self.caller.msg(f"Unknown condition: {condition_name}")
            return
            
        # Get last breaking point roll
        last_roll = self.caller.db.last_breaking_point
        if not last_roll:
            self.caller.msg("No breaking point roll has been made")
            return
            
        # Add the condition
        condition = STANDARD_CONDITIONS[condition_name]
        self.caller.conditions.add(condition)
        
        self.caller.msg(f"Added condition: {condition.name}")
        self.caller.msg(f"Description: {condition.description}")
        
        # Clear the last roll
        del self.caller.db.last_breaking_point 