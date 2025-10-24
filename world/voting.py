"""
Voting and Recommendation System

This module handles the voting and recommendation system for awarding experience points.
Players can vote for each other and write recommendations, with time limits and configurable rewards.
"""

from datetime import datetime, timedelta
from evennia.objects.objects import DefaultObject
from evennia.server.models import ServerConfig
from evennia.utils import logger
from evennia.utils.utils import make_iter


class VotingHandler:
    """
    Handler for managing votes and recommendations for characters.
    """
    
    def __init__(self, obj):
        self.obj = obj
        self._load_votes()
        
    def _load_votes(self):
        """Load voting data from the object's attributes"""
        # Load votes given by this character
        self.votes_given = self.obj.attributes.get('votes_given', default={})
        # Load votes received by this character  
        self.votes_received = self.obj.attributes.get('votes_received', default=[])
        # Load recommendations received
        self.recommendations_received = self.obj.attributes.get('recommendations_received', default=[])
        
    def _save_votes(self):
        """Save voting data to the object's attributes"""
        self.obj.attributes.add('votes_given', self.votes_given)
        self.obj.attributes.add('votes_received', self.votes_received)
        self.obj.attributes.add('recommendations_received', self.recommendations_received)
        
    def can_vote_for(self, target_name):
        """
        Check if this character can vote for the target character.
        
        Args:
            target_name (str): Name of the target character
            
        Returns:
            tuple: (can_vote, reason) - bool and string explanation
        """
        # Get vote cooldown from settings (default 1 week)
        vote_cooldown_hours = self.get_setting('vote_cooldown_hours', 168)  # 168 hours = 1 week
        
        # Check if already voted for this character recently
        if target_name in self.votes_given:
            last_vote_time = datetime.fromisoformat(self.votes_given[target_name])
            time_since_vote = datetime.now() - last_vote_time
            cooldown_time = timedelta(hours=vote_cooldown_hours)
            
            if time_since_vote < cooldown_time:
                remaining_time = cooldown_time - time_since_vote
                days = remaining_time.days
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                
                time_str = []
                if days:
                    time_str.append(f"{days} day{'s' if days != 1 else ''}")
                if hours:
                    time_str.append(f"{hours} hour{'s' if hours != 1 else ''}")
                if minutes and not days:  # Only show minutes if less than a day
                    time_str.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
                    
                return False, f"You must wait {', '.join(time_str)} before voting for {target_name} again."
                
        return True, ""
        
    def can_recommend_for(self, target_name):
        """
        Check if this character can write a recommendation for the target character.
        
        Args:
            target_name (str): Name of the target character
            
        Returns:
            tuple: (can_recommend, reason) - bool and string explanation
        """
        # Get recommendation cooldown from settings (default 1 week)
        recc_cooldown_hours = self.get_setting('recc_cooldown_hours', 168)  # 168 hours = 1 week
        
        # Check recent recommendations
        recent_reccs = [r for r in self.recommendations_received 
                       if r.get('from_character') == self.obj.name]
        
        if recent_reccs:
            last_recc = max(recent_reccs, key=lambda x: datetime.fromisoformat(x['timestamp']))
            last_recc_time = datetime.fromisoformat(last_recc['timestamp'])
            time_since_recc = datetime.now() - last_recc_time
            cooldown_time = timedelta(hours=recc_cooldown_hours)
            
            if time_since_recc < cooldown_time:
                remaining_time = cooldown_time - time_since_recc
                days = remaining_time.days
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                
                time_str = []
                if days:
                    time_str.append(f"{days} day{'s' if days != 1 else ''}")
                if hours:
                    time_str.append(f"{hours} hour{'s' if hours != 1 else ''}")
                if minutes and not days:
                    time_str.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
                    
                return False, f"You must wait {', '.join(time_str)} before writing another recommendation for {target_name}."
                
        return True, ""
        
    def vote_for(self, target_character):
        """
        Cast a vote for the target character, awarding XP.
        
        Args:
            target_character: The character object to vote for
            
        Returns:
            bool: True if vote was successful
        """
        target_name = target_character.name
        
        # Check if voting system is enabled
        if not self.is_voting_system_enabled():
            return False, "The voting system is currently disabled. Weekly automated beats are active instead."
        
        # Check if can vote
        can_vote, reason = self.can_vote_for(target_name)
        if not can_vote:
            return False, reason
            
        # Record the vote
        self.votes_given[target_name] = datetime.now().isoformat()
        self._save_votes()
        
        # Award XP to target
        vote_beats = self.get_setting('vote_beats', 0.5)  # Default half a beat
            
        # Add fractional beats using the character's experience property
        target_exp_handler = target_character.experience
        whole_beats, remaining_fractional = target_exp_handler.add_fractional_beat(vote_beats)
                
        # Record vote received
        target_voting_handler = VotingHandler(target_character)
        target_voting_handler.votes_received.append({
            'from_character': self.obj.name,
            'timestamp': datetime.now().isoformat(),
            'beats_awarded': vote_beats
        })
        target_voting_handler._save_votes()
        
        return True, f"Vote cast successfully! {target_name} received {vote_beats} beats."
        
    def recommend_for(self, target_character, recommendation_text):
        """
        Write a recommendation for the target character, awarding additional XP.
        
        Args:
            target_character: The character object to recommend
            recommendation_text (str): The recommendation text
            
        Returns:
            tuple: (success, message)
        """
        target_name = target_character.name
        
        # Check if voting system is enabled
        if not self.is_voting_system_enabled():
            return False, "The recommendation system is currently disabled. Weekly automated beats are active instead."
        
        # Check if can recommend
        can_recommend, reason = self.can_recommend_for(target_name)
        if not can_recommend:
            return False, reason
            
        # Award XP to target
        recc_beats = self.get_setting('recc_beats', 1.0)  # Default 1 beat
            
        # Add fractional beats using the character's experience property
        target_exp_handler = target_character.experience
        whole_beats, remaining_fractional = target_exp_handler.add_fractional_beat(recc_beats)
                
        # Record recommendation
        target_voting_handler = VotingHandler(target_character)
        target_voting_handler.recommendations_received.append({
            'from_character': self.obj.name,
            'timestamp': datetime.now().isoformat(),
            'text': recommendation_text,
            'beats_awarded': recc_beats
        })
        target_voting_handler._save_votes()
        
        return True, f"Recommendation submitted! {target_name} received {recc_beats} beats."
        
    def get_recent_votes(self, days=30):
        """Get votes received in the last N days"""
        cutoff_date = datetime.now() - timedelta(days=days)
        return [vote for vote in self.votes_received 
                if datetime.fromisoformat(vote['timestamp']) > cutoff_date]
                
    def get_recent_recommendations(self, days=30):
        """Get recommendations received in the last N days"""
        cutoff_date = datetime.now() - timedelta(days=days)
        return [recc for recc in self.recommendations_received 
                if datetime.fromisoformat(recc['timestamp']) > cutoff_date]
                
    @staticmethod
    def get_setting(key, default):
        """Get a voting system setting from ServerConfig"""
        return ServerConfig.objects.conf(f'voting_{key}', default=default)
        
    @staticmethod
    def set_setting(key, value):
        """Set a voting system setting in ServerConfig"""
        ServerConfig.objects.conf(f'voting_{key}', value=value)
        
    @staticmethod
    def get_all_settings():
        """Get all voting system settings"""
        settings = {}
        all_configs = ServerConfig.objects.all()
        for config in all_configs:
            if config.key.startswith('voting_') or config.key.startswith('weekly_beats_'):
                key = config.key[7:] if config.key.startswith('voting_') else config.key
                settings[key] = config.value
        return settings
    
    @staticmethod
    def is_voting_system_enabled():
        """Check if the voting system is enabled (mutually exclusive with weekly beats)"""
        return ServerConfig.objects.conf('xp_system_mode', default='voting') == 'voting'
    
    @staticmethod
    def is_weekly_beats_enabled():
        """Check if the weekly beats system is enabled"""
        return ServerConfig.objects.conf('xp_system_mode', default='voting') == 'weekly'
    
    @staticmethod
    def set_xp_system_mode(mode):
        """Set the XP system mode (voting or weekly)"""
        if mode not in ['voting', 'weekly']:
            return False, f"Invalid mode '{mode}'. Must be 'voting' or 'weekly'."
        
        ServerConfig.objects.conf('xp_system_mode', value=mode)
        return True, f"XP system mode set to '{mode}'."
    
    @staticmethod
    def get_weekly_beats_settings():
        """Get weekly beats system settings"""
        return {
            'weekly_beats_amount': ServerConfig.objects.conf('weekly_beats_amount', default=5),
            'weekly_beats_day': ServerConfig.objects.conf('weekly_beats_day', default='sunday'),
            'weekly_beats_time': ServerConfig.objects.conf('weekly_beats_time', default='00:00'),
            'last_weekly_distribution': ServerConfig.objects.conf('last_weekly_distribution', default=None)
        }


def get_character_by_name(name):
    """
    Helper function to get a character by name.
    
    Args:
        name (str): Character name to search for
        
    Returns:
        Character or None: Found character object or None
    """
    from evennia import search_object
    
    # Search for character
    matches = search_object(name, typeclass="typeclasses.characters.Character")
    
    if not matches:
        return None
    elif len(matches) > 1:
        # Multiple matches, try exact match first
        exact_matches = [obj for obj in matches if obj.name.lower() == name.lower()]
        if len(exact_matches) == 1:
            return exact_matches[0]
        return None  # Ambiguous
    else:
        return matches[0]
