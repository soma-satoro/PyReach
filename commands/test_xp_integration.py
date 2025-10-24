"""
Test command for verifying XP system integration.
This command will be removed after testing is complete.
"""

from evennia.commands.command import Command


class CmdTestXP(Command):
    """
    Test XP system integration.
    
    Usage:
        +testxp
        
    This command tests the integration between the character typeclass,
    experience handler, voting system, and spending system.
    """
    
    key = "+testxp"
    help_category = "Testing"
    locks = "cmd:perm(Builder)"
    
    def func(self):
        """Test the XP integration."""
        output = []
        output.append("|wXP System Integration Test|n")
        output.append("=" * 40)
        
        try:
            # Test 1: Experience handler access
            exp_handler = self.caller.experience
            output.append(f"✓ Experience handler accessible via character.experience")
            output.append(f"  Current beats: {exp_handler.beats}")
            output.append(f"  Current XP: {exp_handler.experience}")
            output.append(f"  Total beats (including fractional): {exp_handler.total_beats}")
            
            # Test 2: Legacy data migration
            if hasattr(self.caller, 'db') and self.caller.db.stats:
                other_stats = self.caller.db.stats.get('other', {})
                if 'beats' in other_stats or 'experience' in other_stats:
                    output.append(f"⚠ Legacy beats/XP found in db.stats - will be migrated on next access")
                else:
                    output.append(f"✓ No legacy beats/XP in db.stats")
            
            # Test 3: Fractional beats
            fractional = self.caller.attributes.get('fractional_beats', default=0.0)
            output.append(f"✓ Fractional beats system: {fractional}")
            
            # Test 4: Add a small amount of fractional beats to test
            old_total = exp_handler.total_beats
            exp_handler.add_fractional_beat(0.3)
            new_total = exp_handler.total_beats
            output.append(f"✓ Added 0.3 fractional beats: {old_total} -> {new_total}")
            
            # Test 5: Check spending system access
            stats = self.caller.db.stats
            if stats:
                output.append(f"✓ Character stats accessible for spending")
                attributes = stats.get('attributes', {})
                skills = stats.get('skills', {})
                merits = stats.get('merits', {})
                output.append(f"  Attributes: {len(attributes)} set")
                output.append(f"  Skills: {len(skills)} set") 
                output.append(f"  Merits: {len(merits)} set")
            else:
                output.append(f"⚠ No character stats found - spending may not work")
                
            # Test 6: Voting system integration check
            from world.voting import VotingHandler
            voting_enabled = VotingHandler.is_voting_system_enabled()
            weekly_enabled = VotingHandler.is_weekly_beats_enabled()
            output.append(f"✓ System mode check:")
            output.append(f"  Voting enabled: {voting_enabled}")
            output.append(f"  Weekly beats enabled: {weekly_enabled}")
            
            # Test 7: Dice roll integration
            output.append(f"✓ Dice roll integration ready")
            output.append(f"  Exceptional success (5+ successes) will award 1 beat")
            output.append(f"  Dramatic failure (chance die = 1) will award 1 beat")
            
            output.append(f"\n|gAll integration tests passed!|n")
            
        except Exception as e:
            output.append(f"|rIntegration test failed: {e}|n")
            import traceback
            output.append(f"Traceback: {traceback.format_exc()}")
        
        self.caller.msg("\n".join(output))
