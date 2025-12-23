"""
Administrative command for initializing the area manager system.
This is a one-time setup command for administrators.
"""

from evennia.commands.default.muxcommand import MuxCommand
from world.area_manager import get_area_manager


class CmdInitAreaManager(MuxCommand):
    """
    Initialize the area manager system.
    
    Usage:
      @init_area_manager
      
    This command creates and initializes the area manager script
    with default areas. It should only be run once when setting
    up the game for the first time.
    """
    
    key = "@init_area_manager"
    locks = "cmd:perm(admin)"
    help_category = "Admin Commands"
    
    def func(self):
        caller = self.caller
        
        try:
            # Get or create the area manager
            area_manager = get_area_manager()
            
            # Force initialization of default areas
            area_manager._init_default_areas()
            
            # Show success message
            areas = area_manager.get_areas()
            caller.msg(f"|gArea manager successfully initialized!|n")
            caller.msg(f"Created {len(areas)} default areas:")
            
            for code, info in areas.items():
                caller.msg(f"  {code}: {info['name']}")
            
            caller.msg(f"\nArea manager script ID: #{area_manager.id}")
            caller.msg("Use '+area/list' to see area details.")
            
        except Exception as e:
            caller.msg(f"|rError initializing area manager: {e}|n")
            caller.msg("Please contact a developer.")
