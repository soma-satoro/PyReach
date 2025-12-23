from evennia.commands.default.muxcommand import MuxCommand
from world.experience import ExperienceHandler

class CmdAspiration(MuxCommand):
    """
    Manage your character's aspirations.
    
    Usage:
        +aspiration/list - List your current aspirations
        +aspiration/add <number> <description> - Add or update an aspiration
        +aspiration/remove <number> - Remove an aspiration
        +aspiration/fulfill <number> - Mark an aspiration as fulfilled and gain a beat
        
    Aspirations are character goals that drive story and generate beats when fulfilled.
    You can have up to 3 aspirations at a time.
    """
    key = "+aspiration"
    aliases = ["+asp"]
    help_category = "Chargen & Character Info"
    
    def func(self):
        """Execute the command"""
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        if is_legacy_mode():
            self.caller.msg("|rAspiration system is disabled in Legacy Mode.|n")
            self.caller.msg("Legacy Mode uses only Virtue and Vice for character motivation.")
            return
        
        if not self.switches:
            self.caller.msg("Usage: +aspiration/list, +aspiration/add, +aspiration/remove, or +aspiration/fulfill")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_aspirations()
        elif switch == "add":
            self.add_aspiration()
        elif switch == "remove":
            self.remove_aspiration()
        elif switch == "fulfill":
            self.fulfill_aspiration()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def list_aspirations(self):
        """List current aspirations"""
        aspirations = self.caller.db.aspirations or [None, None, None]
        
        if all(asp is None for asp in aspirations):
            self.caller.msg("You have no aspirations set.")
            return
            
        output = ["Your aspirations:"]
        for i, asp in enumerate(aspirations, 1):
            if asp:
                output.append(f"{i}. {asp}")
            else:
                output.append(f"{i}. (empty)")
                
        self.caller.msg("\n".join(output))
    
    def add_aspiration(self):
        """Add or update an aspiration"""
        try:
            number, description = self.args.split(" ", 1)
            number = int(number)
        except ValueError:
            self.caller.msg("Usage: +aspiration/add <number> <description>")
            return
            
        if not 1 <= number <= 3:
            self.caller.msg("Aspiration number must be 1, 2, or 3")
            return
            
        # Initialize aspirations if not exists
        if not self.caller.db.aspirations:
            self.caller.db.aspirations = [None, None, None]
            
        self.caller.db.aspirations[number-1] = description
        self.caller.msg(f"Set aspiration {number} to: {description}")
    
    def remove_aspiration(self):
        """Remove an aspiration"""
        try:
            number = int(self.args)
        except ValueError:
            self.caller.msg("Usage: +aspiration/remove <number>")
            return
            
        if not 1 <= number <= 3:
            self.caller.msg("Aspiration number must be 1, 2, or 3")
            return
            
        if not self.caller.db.aspirations or self.caller.db.aspirations[number-1] is None:
            self.caller.msg(f"You don't have an aspiration set for slot {number}")
            return
            
        self.caller.db.aspirations[number-1] = None
        self.caller.msg(f"Removed aspiration {number}")
    
    def fulfill_aspiration(self):
        """Mark an aspiration as fulfilled and gain a beat"""
        try:
            number = int(self.args)
        except ValueError:
            self.caller.msg("Usage: +aspiration/fulfill <number>")
            return
            
        if not 1 <= number <= 3:
            self.caller.msg("Aspiration number must be 1, 2, or 3")
            return
            
        if not self.caller.db.aspirations or self.caller.db.aspirations[number-1] is None:
            self.caller.msg(f"You don't have an aspiration set for slot {number}")
            return
            
        # Get the aspiration description before removing it
        description = self.caller.db.aspirations[number-1]
        
        # Remove the fulfilled aspiration
        self.caller.db.aspirations[number-1] = None
        
        # Add a beat
        if not hasattr(self.caller, 'experience'):
            self.caller.experience = ExperienceHandler(self.caller)
        self.caller.experience.add_beat(1)
        
        self.caller.msg(f"You have fulfilled your aspiration: {description}")
        self.caller.msg("You gain 1 beat for fulfilling an aspiration.") 