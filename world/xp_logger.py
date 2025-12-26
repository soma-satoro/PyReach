"""
XP Logger System for Chronicles of Darkness

Tracks all experience and beat gains/losses with detailed logging.
"""

from datetime import datetime, timezone


class XPLogger:
    """
    Handles logging of all XP and beat changes for a character.
    
    Log entries are stored as a list of dictionaries with:
    - timestamp: datetime when the change occurred
    - type: 'beat' or 'experience'
    - amount: numeric change (positive for gains, negative for losses)
    - source: string describing the source/reason
    - details: optional additional information
    """
    
    def __init__(self, character):
        """
        Initialize the XP logger for a character.
        
        Args:
            character: The character object
        """
        self.character = character
        
        # Initialize log if it doesn't exist
        if not hasattr(self.character.db, 'xp_log') or self.character.db.xp_log is None:
            self.character.attributes.add("xp_log", [])
    
    def log_change(self, change_type, amount, source, details=None):
        """
        Log an XP or beat change.
        
        Args:
            change_type (str): 'beat' or 'experience'
            amount (float): Amount changed (positive for gains, negative for losses)
            source (str): Source of the change
            details (str, optional): Additional details
        """
        # Get current log
        xp_log = list(self.character.db.xp_log) if self.character.db.xp_log else []
        
        # Create log entry
        entry = {
            'timestamp': datetime.now(timezone.utc),
            'type': change_type,
            'amount': amount,
            'source': source,
            'details': details
        }
        
        # Add to log
        xp_log.append(entry)
        
        # Save using attributes.add for proper persistence
        self.character.attributes.add("xp_log", xp_log)
    
    def log_beat(self, amount, source, details=None):
        """
        Log a beat change.
        
        Args:
            amount (float): Amount of beats (positive for gains, negative for losses)
            source (str): Source of the beats
            details (str, optional): Additional details
        """
        self.log_change('beat', amount, source, details)
    
    def log_experience(self, amount, source, details=None):
        """
        Log an experience change.
        
        Args:
            amount (int): Amount of XP (positive for gains, negative for losses)
            source (str): Source of the XP
            details (str, optional): Additional details
        """
        self.log_change('experience', amount, source, details)
    
    def get_recent_changes(self, count=5):
        """
        Get the most recent XP/beat changes.
        
        Args:
            count (int): Number of recent changes to retrieve
            
        Returns:
            list: List of log entries (most recent first)
        """
        xp_log = self.character.db.xp_log if self.character.db.xp_log else []
        
        # Return most recent entries
        return list(reversed(xp_log[-count:]))
    
    def get_all_changes(self):
        """
        Get all XP/beat changes.
        
        Returns:
            list: List of all log entries (most recent first)
        """
        xp_log = self.character.db.xp_log if self.character.db.xp_log else []
        return list(reversed(xp_log))
    
    def get_changes_by_type(self, change_type):
        """
        Get all changes of a specific type.
        
        Args:
            change_type (str): 'beat' or 'experience'
            
        Returns:
            list: List of log entries of that type (most recent first)
        """
        xp_log = self.character.db.xp_log if self.character.db.xp_log else []
        filtered = [entry for entry in xp_log if entry.get('type') == change_type]
        return list(reversed(filtered))
    
    def get_changes_by_source(self, source):
        """
        Get all changes from a specific source.
        
        Args:
            source (str): Source to filter by
            
        Returns:
            list: List of log entries from that source (most recent first)
        """
        xp_log = self.character.db.xp_log if self.character.db.xp_log else []
        filtered = [entry for entry in xp_log if entry.get('source') == source]
        return list(reversed(filtered))
    
    def format_log_entry(self, entry, show_date=True):
        """
        Format a log entry for display with text wrapping at 80 characters.
        
        Args:
            entry (dict): Log entry to format
            show_date (bool): Whether to show full date or just time
            
        Returns:
            str: Formatted log entry (may contain newlines for wrapping)
        """
        import re
        import textwrap
        
        timestamp = entry.get('timestamp')
        change_type = entry.get('type', 'unknown')
        amount = entry.get('amount', 0)
        source = entry.get('source', 'Unknown')
        details = entry.get('details')
        
        # Format timestamp
        if timestamp:
            if show_date:
                time_str = timestamp.strftime('%Y-%m-%d %H:%M')
            else:
                time_str = timestamp.strftime('%H:%M')
        else:
            time_str = 'Unknown time'
        
        # Format amount with color
        if amount > 0:
            amount_str = f"|g+{amount}|n"
        elif amount < 0:
            amount_str = f"|r{amount}|n"
        else:
            amount_str = f"{amount}"
        
        # Format type
        if change_type == 'beat':
            type_str = f"{amount_str} |cbeat{'s' if abs(amount) != 1 else ''}|n"
        elif change_type == 'arcane_beat':
            type_str = f"{amount_str} |marcane beat{'s' if abs(amount) != 1 else ''}|n"
        elif change_type == 'arcane_experience':
            type_str = f"{amount_str} |marcane XP|n"
        else:
            type_str = f"{amount_str} |yXP|n"
        
        # Build base line
        base_line = f"|x{time_str}|n {type_str} from |w{source}|n"
        
        if details:
            full_line = f"{base_line} - {details}"
            
            # Calculate display length (removing ANSI codes)
            clean_line = re.sub(r'\|[a-zA-Z]', '', full_line)
            
            # If line is too long, wrap the details
            if len(clean_line) > 80:
                # Return base line + wrapped details on next line
                detail_indent = "  "
                wrapped_details = textwrap.fill(details, width=78, 
                                               initial_indent=detail_indent,
                                               subsequent_indent=detail_indent)
                return f"{base_line}\n{wrapped_details}"
            else:
                return full_line
        else:
            return base_line
    
    def clear_log(self):
        """Clear all log entries (admin only)."""
        self.character.attributes.add("xp_log", [])


def get_xp_logger(character):
    """
    Get an XP logger instance for a character.
    
    Args:
        character: The character object
        
    Returns:
        XPLogger: Logger instance
    """
    return XPLogger(character)

