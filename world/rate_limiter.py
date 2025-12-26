"""
Rate Limiting System for Chronicles of Darkness

Tracks and enforces rate limits on various actions.
"""

from datetime import datetime, timedelta, timezone


def check_rate_limit(character, action_type, max_count, period_days):
    """
    Check if an action is within rate limits.
    
    Args:
        character: The character object
        action_type (str): Type of action (e.g., 'aspiration_fulfill', 'aspiration_change')
        max_count (int): Maximum number of times allowed in period
        period_days (int): Number of days in the period
        
    Returns:
        tuple: (can_perform, message)
            can_perform (bool): Whether the action is allowed
            message (str): Details about limit status or time remaining
    """
    # Initialize rate_limits if not exists
    if not hasattr(character.db, 'rate_limits') or character.db.rate_limits is None:
        character.attributes.add("rate_limits", {})
    
    rate_limits = character.db.rate_limits
    
    # Get actions of this type
    if action_type not in rate_limits:
        return True, f"{max_count} {action_type.replace('_', ' ')} actions available this period."
    
    actions = rate_limits.get(action_type, [])
    
    # Filter to actions within the period
    cutoff_time = datetime.now(timezone.utc) - timedelta(days=period_days)
    recent_actions = []
    for action in actions:
        try:
            if action.get('timestamp') and action['timestamp'] > cutoff_time:
                recent_actions.append(action)
        except (TypeError, AttributeError):
            # Skip invalid entries
            pass
    
    # Check if at limit
    if len(recent_actions) >= max_count:
        # Find oldest action that will expire
        oldest = min(recent_actions, key=lambda x: x['timestamp'])
        available_at = oldest['timestamp'] + timedelta(days=period_days)
        time_remaining = available_at - datetime.now(timezone.utc)
        
        # Format time remaining
        if time_remaining.days > 0:
            time_str = f"{time_remaining.days} day{'s' if time_remaining.days != 1 else ''}"
        else:
            hours = int(time_remaining.seconds / 3600)
            if hours > 0:
                time_str = f"{hours} hour{'s' if hours != 1 else ''}"
            else:
                minutes = int(time_remaining.seconds / 60)
                time_str = f"{minutes} minute{'s' if minutes != 1 else ''}"
        
        available_str = available_at.strftime('%Y-%m-%d %H:%M UTC')
        action_name = action_type.replace('_', ' ')
        
        return False, f"You've used all {max_count} {action_name} actions this {'week' if period_days == 7 else 'period'}. Next available in {time_str} (at {available_str})."
    
    remaining = max_count - len(recent_actions)
    action_name = action_type.replace('_', ' ')
    return True, f"{remaining} {action_name} action{'s' if remaining != 1 else ''} remaining this {'week' if period_days == 7 else 'period'}."


def check_per_target_rate_limit(character, action_type, target_name, period_days):
    """
    Check if an action targeting a specific character is within rate limits.
    
    Args:
        character: The character performing the action
        action_type (str): Type of action (e.g., 'vote', 'recommend')
        target_name (str): Name of the target character
        period_days (int): Number of days in the period (7 for week, 30 for month)
        
    Returns:
        tuple: (can_perform, message)
    """
    # Initialize rate_limits if not exists
    if not hasattr(character.db, 'rate_limits') or character.db.rate_limits is None:
        character.attributes.add("rate_limits", {})
    
    rate_limits = character.db.rate_limits
    
    # Get actions of this type
    if action_type not in rate_limits:
        return True, f"You can {action_type} {target_name}."
    
    actions = rate_limits.get(action_type, [])
    
    # Filter to actions targeting this character within the period
    cutoff_time = datetime.now(timezone.utc) - timedelta(days=period_days)
    recent_for_target = []
    for action in actions:
        try:
            if (action.get('target') == target_name and 
                action.get('timestamp') and 
                action['timestamp'] > cutoff_time):
                recent_for_target.append(action)
        except (TypeError, AttributeError):
            # Skip invalid entries
            pass
    
    if len(recent_for_target) > 0:
        last_action = recent_for_target[0]
        available_at = last_action['timestamp'] + timedelta(days=period_days)
        time_remaining = available_at - datetime.now(timezone.utc)
        
        # Format time remaining
        if time_remaining.days > 0:
            time_str = f"{time_remaining.days} day{'s' if time_remaining.days != 1 else ''}"
        else:
            hours = int(time_remaining.seconds / 3600)
            if hours > 0:
                time_str = f"{hours} hour{'s' if hours != 1 else ''}"
            else:
                minutes = int(time_remaining.seconds / 60)
                time_str = f"{minutes} minute{'s' if minutes != 1 else ''}"
        
        available_str = available_at.strftime('%Y-%m-%d %H:%M UTC')
        period_str = "week" if period_days == 7 else "month"
        
        return False, f"You already {action_type}d {target_name} this {period_str}. Next available in {time_str} (at {available_str})."
    
    return True, f"You can {action_type} {target_name}."


def record_action(character, action_type, target_name=None, details=None):
    """
    Record an action for rate limiting.
    
    Args:
        character: The character performing the action
        action_type (str): Type of action
        target_name (str, optional): Target character name if applicable
        details (str, optional): Additional details
    """
    # Initialize rate_limits if not exists
    if not hasattr(character.db, 'rate_limits') or character.db.rate_limits is None:
        character.attributes.add("rate_limits", {})
    
    # Get current rate limits (create new dict to trigger persistence)
    rate_limits = dict(character.db.rate_limits) if character.db.rate_limits else {}
    
    if action_type not in rate_limits:
        rate_limits[action_type] = []
    
    # Create action record
    action = {
        'timestamp': datetime.now(timezone.utc),
        'target': target_name,
        'details': details
    }
    
    # Add to list (create new list to trigger persistence)
    actions = list(rate_limits.get(action_type, []))
    actions.append(action)
    rate_limits[action_type] = actions
    
    # Save using attributes.add for proper Evennia persistence
    character.attributes.add("rate_limits", rate_limits)


def get_action_count(character, action_type, period_days):
    """
    Get the count of actions performed in the period.
    
    Args:
        character: The character object
        action_type (str): Type of action
        period_days (int): Number of days to look back
        
    Returns:
        int: Number of actions in the period
    """
    if not hasattr(character.db, 'rate_limits') or character.db.rate_limits is None:
        return 0
    
    rate_limits = character.db.rate_limits
    
    if action_type not in rate_limits:
        return 0
    
    actions = rate_limits.get(action_type, [])
    cutoff_time = datetime.now(timezone.utc) - timedelta(days=period_days)
    
    count = 0
    for action in actions:
        try:
            if action.get('timestamp') and action['timestamp'] > cutoff_time:
                count += 1
        except (TypeError, AttributeError):
            pass
    
    return count


def clear_old_actions(character, days_to_keep=90):
    """
    Clean up old action records to prevent database bloat.
    
    Args:
        character: The character object
        days_to_keep (int): Number of days of history to keep
    """
    if not hasattr(character.db, 'rate_limits') or character.db.rate_limits is None:
        return
    
    rate_limits = dict(character.db.rate_limits)
    cutoff_time = datetime.now(timezone.utc) - timedelta(days=days_to_keep)
    
    cleaned = False
    for action_type in rate_limits:
        actions = rate_limits[action_type]
        new_actions = []
        
        for action in actions:
            try:
                if action.get('timestamp') and action['timestamp'] > cutoff_time:
                    new_actions.append(action)
                else:
                    cleaned = True
            except (TypeError, AttributeError):
                # Remove invalid entries
                cleaned = True
        
        rate_limits[action_type] = new_actions
    
    if cleaned:
        character.attributes.add("rate_limits", rate_limits)

