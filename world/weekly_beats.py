"""
Weekly Beats Distribution System

This module handles the automated weekly distribution of beats to all active players.
It's mutually exclusive with the voting system.
"""

from datetime import datetime, timedelta
from evennia import search_object
from evennia.server.models import ServerConfig
from evennia.utils import logger
from world.voting import VotingHandler


class WeeklyBeatsHandler:
    """
    Handler for managing weekly beat distribution.
    """
    
    @staticmethod
    def should_distribute_beats():
        """
        Check if beats should be distributed this week.
        
        Returns:
            tuple: (should_distribute, next_distribution_date)
        """
        if not VotingHandler.is_weekly_beats_enabled():
            return False, None
            
        settings = VotingHandler.get_weekly_beats_settings()
        last_distribution = settings['last_weekly_distribution']
        target_day = settings['weekly_beats_day'].lower()
        target_time = settings['weekly_beats_time']
        
        # Parse target time
        try:
            hour, minute = map(int, target_time.split(':'))
        except (ValueError, AttributeError):
            hour, minute = 0, 0
            
        # Get current time
        now = datetime.now()
        
        # Calculate next distribution date
        days_ahead = {
            'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
            'friday': 4, 'saturday': 5, 'sunday': 6
        }.get(target_day, 6)  # Default to Sunday
        
        # Find next occurrence of target day
        days_until_target = (days_ahead - now.weekday()) % 7
        if days_until_target == 0:  # Today is target day
            target_time_today = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if now >= target_time_today:
                # Already past time today, schedule for next week
                days_until_target = 7
                
        next_distribution = now + timedelta(days=days_until_target)
        next_distribution = next_distribution.replace(hour=hour, minute=minute, second=0, microsecond=0)
        
        # Check if we should distribute now
        if last_distribution:
            last_dist_date = datetime.fromisoformat(last_distribution)
            # Don't distribute if we already distributed this week
            if (now - last_dist_date).days < 7:
                return False, next_distribution
                
        # Check if it's time to distribute
        if days_until_target == 0:
            target_time_today = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if now >= target_time_today:
                return True, next_distribution
                
        return False, next_distribution
    
    @staticmethod
    def distribute_weekly_beats():
        """
        Distribute weekly beats to all active characters.
        
        Returns:
            tuple: (success, message, characters_affected)
        """
        if not VotingHandler.is_weekly_beats_enabled():
            return False, "Weekly beats system is not enabled.", 0
            
        settings = VotingHandler.get_weekly_beats_settings()
        beats_amount = settings['weekly_beats_amount']
        
        # Get all character objects
        characters = search_object(typeclass="typeclasses.characters.Character")
        
        if not characters:
            return False, "No characters found.", 0
            
        characters_affected = 0
        distribution_log = []
        
        for character in characters:
            try:
                # Skip characters that haven't been active recently (optional filter)
                if WeeklyBeatsHandler._is_character_eligible(character):                    
                    # Add beats using the character's experience property
                    exp_handler = character.experience
                    whole_beats, remaining_fractional = exp_handler.add_fractional_beat(beats_amount)
                    
                    # Log to XP logger
                    from world.xp_logger import get_xp_logger
                    xp_logger = get_xp_logger(character)
                    xp_logger.log_beat(beats_amount, "Weekly Distribution", details="Automatic weekly beat award")
                    
                    # Notify character
                    character.msg(f"|gWeekly Beat Distribution!|n You received {beats_amount} beats from the weekly distribution.")
                    
                    # Log the distribution
                    distribution_log.append({
                        'character': character.name,
                        'beats_awarded': beats_amount,
                        'timestamp': datetime.now().isoformat()
                    })
                    
                    characters_affected += 1
                    
            except Exception as e:
                logger.log_err(f"Error distributing beats to {character.name}: {e}")
                continue
        
        # Record the distribution
        ServerConfig.objects.conf('last_weekly_distribution', value=datetime.now().isoformat())
        ServerConfig.objects.conf('last_distribution_log', value=distribution_log)
        
        return True, f"Distributed {beats_amount} beats to {characters_affected} characters.", characters_affected
    
    @staticmethod
    def _is_character_eligible(character):
        """
        Check if a character is eligible for weekly beats.
        
        Args:
            character: Character object to check
            
        Returns:
            bool: True if eligible
        """
        # Check if character has been active in the last month
        # This is a basic implementation - you can customize eligibility criteria
        
        # Always eligible for now - you can add activity checks here
        # For example:
        # last_login = character.db.last_login
        # if last_login:
        #     days_since_login = (datetime.now() - last_login).days
        #     return days_since_login <= 30  # Active within last 30 days
        
        return True
    
    @staticmethod
    def get_next_distribution_info():
        """
        Get information about the next weekly distribution.
        
        Returns:
            dict: Information about next distribution
        """
        should_distribute, next_date = WeeklyBeatsHandler.should_distribute_beats()
        settings = VotingHandler.get_weekly_beats_settings()
        
        return {
            'enabled': VotingHandler.is_weekly_beats_enabled(),
            'should_distribute_now': should_distribute,
            'next_distribution': next_date.isoformat() if next_date else None,
            'beats_amount': settings['weekly_beats_amount'],
            'distribution_day': settings['weekly_beats_day'],
            'distribution_time': settings['weekly_beats_time'],
            'last_distribution': settings['last_weekly_distribution']
        }
    
    @staticmethod
    def force_distribution():
        """
        Force an immediate distribution of weekly beats (admin only).
        
        Returns:
            tuple: (success, message, characters_affected)
        """
        return WeeklyBeatsHandler.distribute_weekly_beats()
    
    @staticmethod
    def get_distribution_history():
        """
        Get the history of recent distributions.
        
        Returns:
            list: List of recent distributions
        """
        last_log = ServerConfig.objects.conf('last_distribution_log', default=[])
        return last_log if isinstance(last_log, list) else []
