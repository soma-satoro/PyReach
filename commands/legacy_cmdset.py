"""
Command set for Legacy Mode commands.

This module contains all the commands that are specific to Legacy Mode operation.
"""

from evennia.commands.cmdset import CmdSet
from commands.CmdLegacy import CmdLegacy

class LegacyCmdSet(CmdSet):
    """
    Command set containing all Legacy Mode specific commands.
    
    This should be added to the default character command set to make
    the legacy commands available to all characters.
    """
    
    key = "Legacy Commands"
    
    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        # Legacy mode management (admin only)
        self.add(CmdLegacy())
        
        # Note: Virtue and Vice are now handled by the +stat system
        # when legacy mode is active
