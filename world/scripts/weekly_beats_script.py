"""
Weekly Beats Distribution Script

This script runs periodically to check if weekly beats should be distributed
and handles the automated distribution.
"""

from evennia.scripts.scripts import DefaultScript
from world.weekly_beats import WeeklyBeatsHandler
from evennia.utils import logger


class WeeklyBeatsScript(DefaultScript):
    """
    Script that handles weekly beat distribution.
    
    This script runs every hour to check if it's time to distribute weekly beats.
    It will only distribute if the weekly beats system is enabled and it's the
    correct time/day for distribution.
    """
    
    def at_script_creation(self):
        """Called when the script is first created."""
        self.key = "weekly_beats_distribution"
        self.desc = "Handles automated weekly beat distribution"
        self.interval = 3600  # Run every hour (3600 seconds)
        self.persistent = True
        self.start_delay = True
        
    def at_repeat(self):
        """Called every interval (every hour)."""
        try:
            # Check if we should distribute beats
            should_distribute, next_date = WeeklyBeatsHandler.should_distribute_beats()
            
            if should_distribute:
                logger.log_info("WeeklyBeatsScript: Starting weekly beat distribution...")
                
                success, message, count = WeeklyBeatsHandler.distribute_weekly_beats()
                
                if success:
                    logger.log_info(f"WeeklyBeatsScript: {message}")
                    # Optionally notify staff
                    self._notify_staff(f"Weekly beat distribution completed: {message}")
                else:
                    logger.log_err(f"WeeklyBeatsScript: Distribution failed - {message}")
            
        except Exception as e:
            logger.log_err(f"WeeklyBeatsScript: Error during distribution check - {e}")
    
    def _notify_staff(self, message):
        """Notify online staff about the distribution."""
        from evennia import search_object
        
        # Find online staff members
        staff_online = []
        for session in self.obj.sessions.all():
            if session.puppet and session.puppet.check_permstring("Builder"):
                staff_online.append(session.puppet)
        
        # Send notification to online staff
        for staff in staff_online:
            staff.msg(f"|yWeekly Beats System:|n {message}")
    
    def at_start(self):
        """Called when the script starts."""
        logger.log_info("WeeklyBeatsScript: Weekly beats distribution script started.")
        
    def at_stop(self):
        """Called when the script stops."""
        logger.log_info("WeeklyBeatsScript: Weekly beats distribution script stopped.")


def start_weekly_beats_script():
    """
    Start the weekly beats distribution script.
    
    Returns:
        WeeklyBeatsScript: The created script object
    """
    from evennia import search_script, create_script
    
    # Check if script already exists
    existing_scripts = search_script("weekly_beats_distribution")
    if existing_scripts:
        return existing_scripts[0]
    
    # Create new script
    script = create_script(WeeklyBeatsScript, key="weekly_beats_distribution")
    return script


def stop_weekly_beats_script():
    """
    Stop the weekly beats distribution script.
    
    Returns:
        bool: True if script was found and stopped
    """
    from evennia import search_script
    
    scripts = search_script("weekly_beats_distribution")
    if scripts:
        for script in scripts:
            script.stop()
        return True
    return False
