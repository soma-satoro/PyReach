"""
Voting and Recommendation Commands

Commands for the voting and recommendation system that awards experience points.
"""

from evennia.commands.command import Command
from world.voting import VotingHandler, get_character_by_name
from datetime import datetime, timedelta


class CmdVote(Command):
    """
    Vote for another player to award them experience.
    
    Usage:
        +vote <character>
        
    This command allows you to vote for another player, awarding them experience
    points in the form of beats. You can only vote for each player once per week
    (or whatever time limit staff has set).
    
    Each vote awards half a beat by default. Players need 5 beats to gain 1 XP.
    
    Examples:
        +vote Alice
        +vote Bob
    """
    
    key = "+vote"
    help_category = "Roleplaying Tools"
    locks = "cmd:all()"
    
    def func(self):
        """Execute the vote command."""
        if not self.args:
            self.caller.msg("Usage: +vote <character>")
            return
            
        target_name = self.args.strip()
        
        # Validate input length and sanitize
        if len(target_name) > 50:
            self.caller.msg("|rCharacter name is too long.|n")
            return
            
        # Basic sanitization - allow only alphanumeric, spaces, and common punctuation
        import re
        if not re.match(r'^[a-zA-Z0-9\s\-_\'\.]+$', target_name):
            self.caller.msg("|rInvalid character name format.|n")
            return
        
        # Check if trying to vote for self
        if target_name.lower() == self.caller.name.lower():
            self.caller.msg("You cannot vote for yourself!")
            return
            
        # Find target character
        target_character = get_character_by_name(target_name)
        if not target_character:
            self.caller.msg(f"Character '{target_name}' not found.")
            return
            
        # Initialize voting handler
        voting_handler = VotingHandler(self.caller)
        
        # Attempt to vote
        success, message = voting_handler.vote_for(target_character)
        
        if success:
            # Notify both players
            self.caller.msg(f"|gYou voted for {target_character.name}!|n {message}")
            target_character.msg(f"|g{self.caller.name} voted for you!|n")
        else:
            self.caller.msg(f"|rVote failed:|n {message}")


class CmdRecommend(Command):
    """
    Write a recommendation for another player to award them extra experience.
    
    Usage:
        +recc <character>=<recommendation text>
        +recc/list [character]
        
    This command allows you to write a detailed recommendation for another player,
    awarding them additional experience points. Recommendations provide more XP
    than simple votes and include text explaining why the player deserves recognition.
    
    You can only write one recommendation per week (or whatever time limit staff has set).
    Each recommendation awards 1 beat by default.
    
    Examples:
        +recc Alice=Great roleplay during the investigation scene!
        +recc Bob=Excellent leadership during the combat encounter.
        +recc/list         - List your recent recommendations
        +recc/list Alice   - List recommendations for Alice
    """
    
    key = "+recc"
    aliases = ["+recommend"]
    help_category = "Roleplaying Tools"
    locks = "cmd:all()"
    
    def parse(self):
        """Parse the command arguments."""
        self.switch = ""
        self.target_name = ""
        self.recommendation_text = ""
        
        if "/" in self.args:
            if self.args.startswith("/"):
                parts = self.args[1:].split(" ", 1)
                self.switch = parts[0]
                self.remaining_args = parts[1] if len(parts) > 1 else ""
            else:
                switch_part, remaining = self.args.split("/", 1)
                parts = remaining.split(" ", 1)
                self.switch = parts[0]
                self.remaining_args = parts[1] if len(parts) > 1 else ""
        else:
            self.remaining_args = self.args.strip()
            
        if not self.switch and "=" in self.remaining_args:
            parts = self.remaining_args.split("=", 1)
            self.target_name = parts[0].strip()
            self.recommendation_text = parts[1].strip()
        elif self.switch == "list":
            self.target_name = self.remaining_args.strip()
    
    def func(self):
        """Execute the recommendation command."""
        if self.switch == "list":
            self.list_recommendations()
        elif self.target_name and self.recommendation_text:
            self.write_recommendation()
        else:
            self.caller.msg("Usage: +recc <character>=<recommendation text> or +recc/list [character]")
            
    def write_recommendation(self):
        """Write a recommendation for a character."""
        # Check if trying to recommend self
        if self.target_name.lower() == self.caller.name.lower():
            self.caller.msg("You cannot write a recommendation for yourself!")
            return
            
        # Find target character
        target_character = get_character_by_name(self.target_name)
        if not target_character:
            self.caller.msg(f"Character '{self.target_name}' not found.")
            return
            
        # Validate recommendation text
        if len(self.recommendation_text) < 10:
            self.caller.msg("Recommendation text must be at least 10 characters long.")
            return
            
        if len(self.recommendation_text) > 500:
            self.caller.msg("Recommendation text cannot exceed 500 characters.")
            return
            
        # Initialize voting handler
        voting_handler = VotingHandler(self.caller)
        
        # Attempt to recommend
        success, message = voting_handler.recommend_for(target_character, self.recommendation_text)
        
        if success:
            # Notify both players
            self.caller.msg(f"|gYou wrote a recommendation for {target_character.name}!|n {message}")
            target_character.msg(f"|g{self.caller.name} wrote a recommendation for you!|n You received experience.")
        else:
            self.caller.msg(f"|rRecommendation failed:|n {message}")
            
    def list_recommendations(self):
        """List recommendations."""
        if self.target_name:
            # List recommendations for a specific character
            target_character = get_character_by_name(self.target_name)
            if not target_character:
                self.caller.msg(f"Character '{self.target_name}' not found.")
                return
                
            voting_handler = VotingHandler(target_character)
            recommendations = voting_handler.get_recent_recommendations(30)
            
            if not recommendations:
                self.caller.msg(f"{target_character.name} has no recent recommendations.")
                return
                
            output = [f"|wRecommendations for {target_character.name}|n"]
            output.append("=" * 50)
            
            for i, recc in enumerate(sorted(recommendations, key=lambda x: x['timestamp'], reverse=True), 1):
                timestamp = datetime.fromisoformat(recc['timestamp'])
                formatted_time = timestamp.strftime("%Y-%m-%d %H:%M")
                output.append(f"\n|c{i}. From {recc['from_character']} ({formatted_time})|n")
                output.append(f"   Beats: {recc['beats_awarded']}")
                output.append(f"   Text: {recc['text']}")
                
        else:
            # List caller's recent recommendations
            voting_handler = VotingHandler(self.caller)
            recommendations = voting_handler.get_recent_recommendations(30)
            
            if not recommendations:
                self.caller.msg("You have no recent recommendations.")
                return
                
            output = [f"|wYour Recent Recommendations|n"]
            output.append("=" * 40)
            
            for i, recc in enumerate(sorted(recommendations, key=lambda x: x['timestamp'], reverse=True), 1):
                timestamp = datetime.fromisoformat(recc['timestamp'])
                formatted_time = timestamp.strftime("%Y-%m-%d %H:%M")
                output.append(f"\n|c{i}. From {recc['from_character']} ({formatted_time})|n")
                output.append(f"   Beats: {recc['beats_awarded']}")
                output.append(f"   Text: {recc['text']}")
                
        self.caller.msg("\n".join(output))


class CmdVoteAdmin(Command):
    """
    Administrative commands for managing the XP systems (voting and weekly beats).
    
    Usage:
        +voteadmin/settings                    - Show current settings
        +voteadmin/set <setting>=<value>       - Set a system setting
        +voteadmin/reset <character>           - Reset vote cooldowns for character
        +voteadmin/stats [character]           - Show voting statistics
        +voteadmin/mode <voting|weekly>        - Switch between voting and weekly beats systems
        +voteadmin/weekly                      - Show weekly beats system info
        +voteadmin/distribute                  - Force weekly beat distribution (weekly mode only)
        +voteadmin/script <start|stop>         - Start/stop weekly beats automation script
        
    Available Settings:
        Voting System:
            vote_cooldown_hours    - Hours between votes (default: 168 = 1 week)
            recc_cooldown_hours    - Hours between recommendations (default: 168 = 1 week)  
            vote_beats             - Beats awarded per vote (default: 0.5)
            recc_beats             - Beats awarded per recommendation (default: 1.0)
        
        Weekly Beats System:
            weekly_beats_amount    - Beats distributed weekly (default: 5)
            weekly_beats_day       - Day of week for distribution (default: sunday)
            weekly_beats_time      - Time of day for distribution (default: 00:00)
        
    Examples:
        +voteadmin/mode weekly
        +voteadmin/set weekly_beats_amount=6
        +voteadmin/set weekly_beats_day=monday
        +voteadmin/weekly
        +voteadmin/distribute
    """
    
    key = "+voteadmin"
    help_category = "Admin Commands"
    locks = "cmd:perm(Builder)"
    
    def parse(self):
        """Parse command arguments."""
        self.switch = ""
        self.remaining_args = ""
        
        if "/" in self.args:
            if self.args.startswith("/"):
                parts = self.args[1:].split(" ", 1)
                self.switch = parts[0]
                self.remaining_args = parts[1] if len(parts) > 1 else ""
            else:
                parts = self.args.split("/", 1)
                if len(parts) > 1:
                    switch_args = parts[1].split(" ", 1)
                    self.switch = switch_args[0]
                    self.remaining_args = switch_args[1] if len(switch_args) > 1 else ""
        else:
            self.remaining_args = self.args.strip()
    
    def func(self):
        """Execute the admin command."""
        if self.switch == "settings":
            self.show_settings()
        elif self.switch == "set":
            self.set_setting()
        elif self.switch == "reset":
            self.reset_cooldowns()
        elif self.switch == "stats":
            self.show_stats()
        elif self.switch == "mode":
            self.set_mode()
        elif self.switch == "weekly":
            self.show_weekly_info()
        elif self.switch == "distribute":
            self.force_distribution()
        elif self.switch == "script":
            self.manage_script()
        else:
            self.caller.msg("Usage: +voteadmin/settings, +voteadmin/set <setting>=<value>, "
                          "+voteadmin/reset <character>, +voteadmin/stats [character], "
                          "+voteadmin/mode <voting|weekly>, +voteadmin/weekly, "
                          "+voteadmin/distribute, or +voteadmin/script <start|stop>")
            
    def show_settings(self):
        """Show current system settings."""
        from evennia.server.models import ServerConfig
        
        current_mode = ServerConfig.objects.conf('xp_system_mode', default='voting')
        
        output = ["|wExperience Point System Settings|n"]
        output.append("=" * 40)
        output.append(f"Current Mode: |y{current_mode.title()}|n")
        output.append("")
        
        if current_mode == 'voting':
            output.append("|cVoting System Settings:|n")
            output.append(f"  Vote Cooldown: |c{VotingHandler.get_setting('vote_cooldown_hours', 168)}|n hours")
            output.append(f"  Recommendation Cooldown: |c{VotingHandler.get_setting('recc_cooldown_hours', 168)}|n hours")
            output.append(f"  Vote Beats Award: |y{VotingHandler.get_setting('vote_beats', 0.5)}|n beats")
            output.append(f"  Recommendation Beats Award: |y{VotingHandler.get_setting('recc_beats', 1.0)}|n beats")
        else:
            weekly_settings = VotingHandler.get_weekly_beats_settings()
            output.append("|cWeekly Beats System Settings:|n")
            output.append(f"  Weekly Beats Amount: |y{weekly_settings['weekly_beats_amount']}|n beats")
            output.append(f"  Distribution Day: |c{weekly_settings['weekly_beats_day'].title()}|n")
            output.append(f"  Distribution Time: |c{weekly_settings['weekly_beats_time']}|n")
            
            if weekly_settings['last_weekly_distribution']:
                last_dist = datetime.fromisoformat(weekly_settings['last_weekly_distribution'])
                output.append(f"  Last Distribution: |g{last_dist.strftime('%Y-%m-%d %H:%M')}|n")
            else:
                output.append("  Last Distribution: |rNever|n")
                
        self.caller.msg("\n".join(output))
        
    def set_setting(self):
        """Set a voting system setting."""
        if "=" not in self.remaining_args:
            self.caller.msg("Usage: +voteadmin/set <setting>=<value>")
            return
            
        setting, value_str = self.remaining_args.split("=", 1)
        setting = setting.strip()
        value_str = value_str.strip()
        
        # Validate setting name
        voting_settings = ['vote_cooldown_hours', 'recc_cooldown_hours', 'vote_beats', 'recc_beats']
        weekly_settings = ['weekly_beats_amount', 'weekly_beats_day', 'weekly_beats_time']
        valid_settings = voting_settings + weekly_settings
        
        if setting not in valid_settings:
            self.caller.msg(f"Invalid setting. Valid settings: {', '.join(valid_settings)}")
            return
            
        # Convert value
        try:
            if setting.endswith('_hours') or setting == 'weekly_beats_amount':
                value = int(value_str) if setting.endswith('_hours') else float(value_str)
                if value < 1 if setting.endswith('_hours') else value < 0:
                    self.caller.msg("Hours must be at least 1." if setting.endswith('_hours') else "Beat values cannot be negative.")
                    return
            elif setting.endswith('_beats'):
                value = float(value_str)
                if value < 0:
                    self.caller.msg("Beat values cannot be negative.")
                    return
            elif setting == 'weekly_beats_day':
                valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                if value_str.lower() not in valid_days:
                    self.caller.msg(f"Invalid day. Valid days: {', '.join(valid_days)}")
                    return
                value = value_str.lower()
            elif setting == 'weekly_beats_time':
                # Validate time format HH:MM
                import re
                if not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', value_str):
                    self.caller.msg("Invalid time format. Use HH:MM (24-hour format).")
                    return
                value = value_str
            else:
                value = value_str
        except ValueError:
            self.caller.msg(f"Invalid value '{value_str}' for setting '{setting}'.")
            return
            
        # Set the setting
        from evennia.server.models import ServerConfig
        if setting in ['weekly_beats_amount', 'weekly_beats_day', 'weekly_beats_time']:
            ServerConfig.objects.conf(setting, value=value)
        else:
            VotingHandler.set_setting(setting, value)
        self.caller.msg(f"|gSetting '{setting}' set to '{value}'.|n")
        
    def reset_cooldowns(self):
        """Reset vote cooldowns for a character."""
        if not self.remaining_args:
            self.caller.msg("Usage: +voteadmin/reset <character>")
            return
            
        character_name = self.remaining_args.strip()
        target_character = get_character_by_name(character_name)
        
        if not target_character:
            self.caller.msg(f"Character '{character_name}' not found.")
            return
            
        # Reset voting data
        target_character.attributes.add('votes_given', {})
        target_character.attributes.add('votes_received', [])
        target_character.attributes.add('recommendations_received', [])
        
        self.caller.msg(f"|gReset all vote cooldowns and history for {target_character.name}.|n")
        
    def show_stats(self):
        """Show voting statistics."""
        if self.remaining_args:
            # Stats for specific character
            character_name = self.remaining_args.strip()
            target_character = get_character_by_name(character_name)
            
            if not target_character:
                self.caller.msg(f"Character '{character_name}' not found.")
                return
                
            voting_handler = VotingHandler(target_character)
            votes = voting_handler.get_recent_votes(30)
            recommendations = voting_handler.get_recent_recommendations(30)
            
            output = [f"|wVoting Statistics for {target_character.name}|n"]
            output.append("=" * 50)
            output.append(f"Recent Votes (30 days): |c{len(votes)}|n")
            output.append(f"Recent Recommendations (30 days): |c{len(recommendations)}|n")
            
            total_vote_beats = sum(vote.get('beats_awarded', 0.5) for vote in votes)
            total_recc_beats = sum(recc.get('beats_awarded', 1.0) for recc in recommendations)
            
            output.append(f"Beats from Votes: |y{total_vote_beats}|n")
            output.append(f"Beats from Recommendations: |y{total_recc_beats}|n")
            output.append(f"Total Beats from Voting: |y{total_vote_beats + total_recc_beats}|n")
            
        else:
            # General stats (would need to iterate through all characters - simplified for now)
            output = ["|wVoting System Statistics|n"]
            output.append("=" * 30)
            output.append("Use +voteadmin/stats <character> for character-specific stats.")
            
        self.caller.msg("\n".join(output))
        
    def set_mode(self):
        """Set the XP system mode."""
        if not self.remaining_args:
            self.caller.msg("Usage: +voteadmin/mode <voting|weekly>")
            return
            
        mode = self.remaining_args.strip().lower()
        success, message = VotingHandler.set_xp_system_mode(mode)
        
        if success:
            self.caller.msg(f"|g{message}|n")
            if mode == 'weekly':
                self.caller.msg("Remember to start the weekly beats script with +voteadmin/script start")
        else:
            self.caller.msg(f"|r{message}|n")
            
    def show_weekly_info(self):
        """Show weekly beats system information."""
        from world.weekly_beats import WeeklyBeatsHandler
        
        info = WeeklyBeatsHandler.get_next_distribution_info()
        
        output = ["|wWeekly Beats System Information|n"]
        output.append("=" * 40)
        output.append(f"System Enabled: |{'g' if info['enabled'] else 'r'}{info['enabled']}|n")
        output.append(f"Beats per Week: |y{info['beats_amount']}|n")
        output.append(f"Distribution Day: |c{info['distribution_day'].title()}|n")
        output.append(f"Distribution Time: |c{info['distribution_time']}|n")
        
        if info['last_distribution']:
            last_dist = datetime.fromisoformat(info['last_distribution'])
            output.append(f"Last Distribution: |g{last_dist.strftime('%Y-%m-%d %H:%M')}|n")
        else:
            output.append("Last Distribution: |rNever|n")
            
        if info['next_distribution']:
            next_dist = datetime.fromisoformat(info['next_distribution'])
            output.append(f"Next Distribution: |y{next_dist.strftime('%Y-%m-%d %H:%M')}|n")
            
        if info['should_distribute_now']:
            output.append("|rReady for distribution now!|n")
            
        # Check script status
        from evennia import search_script
        scripts = search_script("weekly_beats_distribution")
        if scripts:
            output.append("Automation Script: |gRunning|n")
        else:
            output.append("Automation Script: |rStopped|n")
            
        self.caller.msg("\n".join(output))
        
    def force_distribution(self):
        """Force immediate weekly beat distribution."""
        if not VotingHandler.is_weekly_beats_enabled():
            self.caller.msg("Weekly beats system is not enabled. Use +voteadmin/mode weekly first.")
            return
            
        from world.weekly_beats import WeeklyBeatsHandler
        
        self.caller.msg("Forcing weekly beat distribution...")
        success, message, count = WeeklyBeatsHandler.force_distribution()
        
        if success:
            self.caller.msg(f"|g{message}|n")
        else:
            self.caller.msg(f"|r{message}|n")
            
    def manage_script(self):
        """Start or stop the weekly beats automation script."""
        if not self.remaining_args:
            self.caller.msg("Usage: +voteadmin/script <start|stop>")
            return
            
        action = self.remaining_args.strip().lower()
        
        if action == "start":
            from world.scripts.weekly_beats_script import start_weekly_beats_script
            script = start_weekly_beats_script()
            if script:
                self.caller.msg("|gWeekly beats automation script started.|n")
            else:
                self.caller.msg("|rFailed to start weekly beats script.|n")
        elif action == "stop":
            from world.scripts.weekly_beats_script import stop_weekly_beats_script
            if stop_weekly_beats_script():
                self.caller.msg("|gWeekly beats automation script stopped.|n")
            else:
                self.caller.msg("|yNo weekly beats script was running.|n")
        else:
            self.caller.msg("Usage: +voteadmin/script <start|stop>")
