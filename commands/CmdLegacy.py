from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import logger

class CmdLegacy(MuxCommand):
    """
    Toggle legacy mode for Chronicles/World of Darkness 1st Edition framework.
    
    Usage:
        +legacy on|off - Toggle legacy mode on or off
        +legacy - Show current legacy mode status
        
    Legacy Mode Changes:
        - Removes aspirations and related commands
        - Replaces beats with legacy experience point system
        - Disables conditions and tilts systems
        - Disables social combat with doors
        - Uses only Virtue/Vice as anchors (removes other anchor types)
        - Updates character sheet display to legacy format
        
    This is a global setting that affects all characters and systems.
    Only administrators can change this setting.
    """
    
    key = "+legacy"
    aliases = ["legacy"]
    help_category = "Admin Commands"
    locks = "cmd:perm(Admin)"  # Only admins can use this command
    
    def func(self):
        """Execute the legacy mode command"""
        if not self.args:
            # Show current status
            self.show_legacy_status()
            return
            
        arg = self.args.strip().lower()
        
        if arg in ["on", "1", "true", "yes"]:
            self.set_legacy_mode(True)
        elif arg in ["off", "0", "false", "no"]:
            self.set_legacy_mode(False)
        else:
            self.caller.msg("Usage: +legacy on|off")
            return
    
    def show_legacy_status(self):
        """Show the current legacy mode status"""
        # Check if legacy mode is enabled globally
        legacy_mode = self.caller.db.legacy_mode if hasattr(self.caller.db, 'legacy_mode') else False
        
        # Check global setting on the server
        from evennia import settings
        global_legacy = getattr(settings, 'LEGACY_MODE', False)
        
        # Use server setting if available, otherwise character setting
        current_mode = global_legacy or legacy_mode
        
        output = []
        output.append("|y" + "="*60 + "|n")
        output.append("|wLEGACY MODE STATUS|n".center(60))
        output.append("|y" + "="*60 + "|n")
        
        if current_mode:
            output.append("|gLegacy Mode: |GENABLED|n")
            output.append("")
            output.append("|wActive Legacy Features:|n")
            output.append("- Chronicles/World of Darkness 1st Edition framework")
            output.append("- Virtue/Vice only anchors (no aspirations)")
            output.append("- Legacy experience point system (no beats)")
            output.append("- Conditions and tilts disabled")
            output.append("- Social combat with doors disabled")
            output.append("- Legacy character sheet format")
        else:
            output.append("|rLegacy Mode: |RDISABLED|n")
            output.append("")
            output.append("|wStandard Chronicles of Darkness 2nd Edition active|n")
        
        output.append("|y" + "="*60 + "|n")
        self.caller.msg("\n".join(output))
    
    def set_legacy_mode(self, enable):
        """Set legacy mode on or off"""
        # Set global legacy mode flag
        from evennia import settings
        
        # Store in server attributes for persistence
        from evennia.server.models import ServerConfig
        
        try:
            if enable:
                ServerConfig.objects.conf('legacy_mode', True)
                self.caller.msg("|gLegacy mode has been |GENABLED|g.|n")
                self.caller.msg("|yAll systems will now operate in Chronicles/World of Darkness 1st Edition mode.|n")
                
                # Log the change
                logger.log_info(f"Legacy mode enabled by {self.caller.name}")
                
                # Announce to all connected players
                from evennia.server.sessionhandler import SESSIONS
                announcement = "|ySystem Announcement:|n Legacy mode has been enabled. The game is now operating in Chronicles/World of Darkness 1st Edition framework."
                for session in SESSIONS.get_sessions():
                    if session.puppet:
                        session.puppet.msg(announcement)
            else:
                ServerConfig.objects.conf('legacy_mode', False)
                self.caller.msg("|rLegacy mode has been |RDISABLED|r.|n")
                self.caller.msg("|yAll systems will now operate in standard Chronicles of Darkness 2nd Edition mode.|n")
                
                # Log the change
                logger.log_info(f"Legacy mode disabled by {self.caller.name}")
                
                # Announce to all connected players
                from evennia.server.sessionhandler import SESSIONS
                announcement = "|ySystem Announcement:|n Legacy mode has been disabled. The game is now operating in standard Chronicles of Darkness 2nd Edition framework."
                for session in SESSIONS.get_sessions():
                    if session.puppet:
                        session.puppet.msg(announcement)
                        
        except Exception as e:
            self.caller.msg(f"|rError setting legacy mode: {e}|n")
            logger.log_err(f"Error setting legacy mode: {e}")


def is_legacy_mode():
    """
    Utility function to check if legacy mode is currently active.
    Can be imported and used by other modules.
    
    Returns:
        bool: True if legacy mode is active, False otherwise
    """
    from evennia.server.models import ServerConfig
    try:
        return ServerConfig.objects.conf('legacy_mode', default=False)
    except:
        return False
