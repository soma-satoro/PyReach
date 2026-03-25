from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.experience import ExperienceHandler
from world.utils.permission_utils import require_approved_character
from utils.search_helpers import search_character

class CmdSocial(MuxCommand):
    """
    Manage social interactions and maneuvering.
    
    Usage:
        +social/impression <target> <level> - Set impression level with target
        +social/doors <target> - Check doors with target
        +social/leverage <target> <type> <description> - Use leverage
        +social/roll <target> <goal> - Make a social roll
        
    Impression Levels:
        perfect - Target is completely receptive
        excellent - Target is very receptive
        good - Target is somewhat receptive
        average - Target is neutral
        hostile - Target is resistant
        
    Leverage Types:
        soft - Bribes, favors, promises
        hard - Threats, blackmail, coercion
    """
    key = "+social"
    aliases = ["+soc"]
    help_category = "Roleplaying Tools"
    
    def func(self):
        """Execute the command"""
        if not require_approved_character(self.caller, "+social"):
            return

        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        if is_legacy_mode():
            self.caller.msg("|rSocial combat system is disabled in Legacy Mode.|n")
            self.caller.msg("Legacy Mode uses traditional social interaction without doors mechanics.")
            return
        
        if not self.switches:
            self.caller.msg("Usage: +social/impression, +social/doors, +social/leverage, or +social/roll")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "impression":
            self.set_impression()
        elif switch == "doors":
            self.check_doors()
        elif switch == "leverage":
            self.use_leverage()
        elif switch == "roll":
            self.social_roll()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def set_impression(self):
        """Set impression level with a target"""
        try:
            target_name, level = self.args.split(" ", 1)
        except ValueError:
            self.caller.msg("Usage: +social/impression <target> <level>")
            return
            
        target = search_character(self.caller, target_name)
        if not target:
            return
            
        level = level.lower()
        if level not in ["perfect", "excellent", "good", "average", "hostile"]:
            self.caller.msg("Invalid impression level. Use: perfect, excellent, good, average, hostile")
            return
            
        # Store impression in target's attributes
        if not target.db.impressions:
            target.db.impressions = {}
        target.db.impressions[self.caller.id] = level
        
        self.caller.msg(f"Set impression level with {target.name} to {level}")
    
    def check_doors(self):
        """Check doors with a target"""
        target = search_character(self.caller, self.args)
        if not target:
            return
            
        # Get target's resolve and composure
        resolve = target.db.attributes["mental"]["resolve"]
        composure = target.db.attributes["social"]["composure"]
        
        # Doors is the lower of resolve and composure
        doors = min(resolve, composure)
        
        # Get current impression level
        impression = target.db.impressions.get(self.caller.id, "average")
        
        # Calculate time between rolls based on impression
        time_intervals = {
            "perfect": "1 minute",
            "excellent": "5 minutes",
            "good": "15 minutes",
            "average": "30 minutes",
            "hostile": "1 hour"
        }
        
        self.caller.msg(f"Current impression with {target.name}: {impression}")
        self.caller.msg(f"Doors: {doors}")
        self.caller.msg(f"Time between rolls: {time_intervals[impression]}")
    
    def use_leverage(self):
        """Use leverage on a target"""
        try:
            target_name, leverage_type, description = self.args.split(" ", 2)
        except ValueError:
            self.caller.msg("Usage: +social/leverage <target> <type> <description>")
            return
            
        target = search_character(self.caller, target_name)
        if not target:
            return
            
        leverage_type = leverage_type.lower()
        if leverage_type not in ["soft", "hard"]:
            self.caller.msg("Invalid leverage type. Use: soft or hard")
            return
            
        # Store leverage in target's attributes
        if not target.db.leverage:
            target.db.leverage = {}
        if self.caller.id not in target.db.leverage:
            target.db.leverage[self.caller.id] = []
            
        target.db.leverage[self.caller.id].append({
            "type": leverage_type,
            "description": description
        })
        
        self.caller.msg(f"Added {leverage_type} leverage with {target.name}: {description}")
    
    def social_roll(self):
        """Make a social roll"""
        try:
            target_name, goal = self.args.split(" ", 1)
        except ValueError:
            self.caller.msg("Usage: +social/roll <target> <goal>")
            return
            
        target = search_character(self.caller, target_name)
        if not target:
            return
            
        # Get current impression level
        impression = target.db.impressions.get(self.caller.id, "average")
        
        # Get target's doors
        resolve = target.db.attributes["mental"]["resolve"]
        composure = target.db.attributes["social"]["composure"]
        doors = min(resolve, composure)
        
        # Calculate dice pool based on impression
        impression_modifiers = {
            "perfect": 3,
            "excellent": 2,
            "good": 1,
            "average": 0,
            "hostile": -1
        }
        
        # Base pool is manipulation + persuasion
        manipulation = self.caller.db.attributes["social"]["manipulation"]
        persuasion = self.caller.db.skills["social"].get("persuasion", 0)
        
        # Add impression modifier
        dice_pool = manipulation + persuasion + impression_modifiers[impression]
        
        # Add any applicable leverage
        if target.db.leverage and self.caller.id in target.db.leverage:
            leverage = target.db.leverage[self.caller.id]
            if any(l["type"] == "soft" for l in leverage):
                dice_pool += 1
            if any(l["type"] == "hard" for l in leverage):
                dice_pool += 2
        
        # Make the roll
        self.caller.msg(f"Making social roll against {target.name} for: {goal}")
        self.caller.msg(f"Dice pool: {dice_pool}")
        self.caller.msg(f"Target doors: {doors}")
        
        # Use the existing roll command
        self.caller.execute_cmd(f"+roll {dice_pool}") 