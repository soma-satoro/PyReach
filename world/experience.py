from evennia.utils.utils import lazy_property
from evennia.typeclasses.attributes import AttributeProperty
from evennia.utils import logger

class ExperienceHandler:
    """
    A handler for managing experience points and beats for characters.
    For Mages, also manages Arcane Beats and Arcane Experience.
    For Prometheans, manages Vitriol Beats and Vitriol Experience.
    For Mummies, manages Reminisce Beats and Reminisce Experience.
    """
    def __init__(self, obj):
        self.obj = obj
        self._beats = 0
        self._experience = 0
        self._arcane_beats = 0
        self._arcane_experience = 0
        self._vitriol_beats = 0
        self._vitriol_experience = 0
        self._reminisce_beats = 0
        self._reminisce_experience = 0
        self._load_experience()
    
    def _load_experience(self):
        """Load experience data from the object's attributes"""
        # Check for legacy data in db.stats first
        legacy_beats = 0
        legacy_experience = 0
        
        if hasattr(self.obj, 'db') and self.obj.db.stats:
            other_stats = self.obj.db.stats.get('other', {})
            if 'beats' in other_stats or 'experience' in other_stats:
                legacy_beats = other_stats.get('beats', 0)
                legacy_experience = other_stats.get('experience', 0)
                
                # Migrate legacy data to attributes
                if legacy_beats > 0 or legacy_experience > 0:
                    self.obj.attributes.add('beats', legacy_beats)
                    self.obj.attributes.add('experience', legacy_experience)
                    
                    # Clear legacy data
                    other_stats.pop('beats', None)
                    other_stats.pop('experience', None)
        
        # Load from attributes (including migrated data)
        self._beats = self.obj.attributes.get('beats', default=legacy_beats)
        self._experience = self.obj.attributes.get('experience', default=legacy_experience)
        
        # Load arcane experience (Mage-specific)
        self._arcane_beats = self.obj.attributes.get('arcane_beats', default=0)
        self._arcane_experience = self.obj.attributes.get('arcane_experience', default=0)
        
        # Load vitriol experience (Promethean-specific)
        self._vitriol_beats = self.obj.attributes.get('vitriol_beats', default=0)
        self._vitriol_experience = self.obj.attributes.get('vitriol_experience', default=0)
        
        # Load reminisce experience (Mummy-specific)
        self._reminisce_beats = self.obj.attributes.get('reminisce_beats', default=0)
        self._reminisce_experience = self.obj.attributes.get('reminisce_experience', default=0)
    
    def _save_experience(self):
        """Save experience data to the object's attributes"""
        self.obj.attributes.add('beats', self._beats)
        self.obj.attributes.add('experience', self._experience)
        self.obj.attributes.add('arcane_beats', self._arcane_beats)
        self.obj.attributes.add('arcane_experience', self._arcane_experience)
        self.obj.attributes.add('vitriol_beats', self._vitriol_beats)
        self.obj.attributes.add('vitriol_experience', self._vitriol_experience)
        self.obj.attributes.add('reminisce_beats', self._reminisce_beats)
        self.obj.attributes.add('reminisce_experience', self._reminisce_experience)
    
    def add_beat(self, amount=1):
        """Add beats to the character"""
        self._beats += amount
        # Check if we can convert beats to experience
        while self._beats >= 5:
            self._beats -= 5
            self._experience += 1
        self._save_experience()
        self.obj.msg(f"You gained {amount} beat(s). You now have {self._beats} beats and {self._experience} experience.")
    
    def add_experience(self, amount):
        """Add experience directly to the character"""
        self._experience += amount
        self._save_experience()
        self.obj.msg(f"You gained {amount} experience. You now have {self._experience} experience.")
    
    def spend_experience(self, amount):
        """Spend experience points"""
        if self._experience >= amount:
            self._experience -= amount
            self._save_experience()
            self.obj.msg(f"You spent {amount} experience. You now have {self._experience} experience remaining.")
            return True
        else:
            self.obj.msg(f"You don't have enough experience. You need {amount} but only have {self._experience}.")
            return False
    
    @property
    def beats(self):
        """Get current beats"""
        return self._beats
    
    @property
    def experience(self):
        """Get current experience"""
        return self._experience
    
    @property
    def total_beats(self):
        """Get total beats including fractional beats"""
        fractional_beats = self.obj.attributes.get('fractional_beats', default=0.0)
        return self._beats + fractional_beats
    
    def add_fractional_beat(self, amount):
        """Add fractional beats to the character"""
        fractional_beats = self.obj.attributes.get('fractional_beats', default=0.0)
        fractional_beats += amount
        
        # Convert to whole beats when >= 1.0
        whole_beats = int(fractional_beats)
        fractional_beats = fractional_beats - whole_beats
        
        # Save fractional beats
        self.obj.attributes.add('fractional_beats', fractional_beats)
        
        # Add whole beats if any
        if whole_beats > 0:
            self.add_beat(whole_beats)
        
        return whole_beats, fractional_beats
    
    # Arcane Experience methods (Mage-specific)
    
    def add_arcane_beat(self, amount=1):
        """Add arcane beats to the character (Mage-specific)"""
        self._arcane_beats += amount
        # Check if we can convert arcane beats to arcane experience
        while self._arcane_beats >= 5:
            self._arcane_beats -= 5
            self._arcane_experience += 1
        self._save_experience()
        self.obj.msg(f"You gained {amount} arcane beat(s). You now have {self._arcane_beats} arcane beats and {self._arcane_experience} arcane experience.")
    
    def add_arcane_experience(self, amount):
        """Add arcane experience directly to the character (Mage-specific)"""
        self._arcane_experience += amount
        self._save_experience()
        self.obj.msg(f"You gained {amount} arcane experience. You now have {self._arcane_experience} arcane experience.")
    
    def spend_arcane_experience(self, amount):
        """Spend arcane experience points (Mage-specific)"""
        if self._arcane_experience >= amount:
            self._arcane_experience -= amount
            self._save_experience()
            self.obj.msg(f"You spent {amount} arcane experience. You now have {self._arcane_experience} arcane experience remaining.")
            return True
        else:
            self.obj.msg(f"You don't have enough arcane experience. You need {amount} but only have {self._arcane_experience}.")
            return False
    
    @property
    def arcane_beats(self):
        """Get current arcane beats"""
        return self._arcane_beats
    
    @property
    def arcane_experience(self):
        """Get current arcane experience"""
        return self._arcane_experience
    
    @property
    def total_arcane_beats(self):
        """Get total arcane beats including fractional arcane beats"""
        fractional_arcane_beats = self.obj.attributes.get('fractional_arcane_beats', default=0.0)
        return self._arcane_beats + fractional_arcane_beats
    
    def add_fractional_arcane_beat(self, amount):
        """Add fractional arcane beats to the character (Mage-specific)"""
        fractional_arcane_beats = self.obj.attributes.get('fractional_arcane_beats', default=0.0)
        fractional_arcane_beats += amount
        
        # Convert to whole beats when >= 1.0
        whole_beats = int(fractional_arcane_beats)
        fractional_arcane_beats = fractional_arcane_beats - whole_beats
        
        # Save fractional arcane beats
        self.obj.attributes.add('fractional_arcane_beats', fractional_arcane_beats)
        
        # Add whole beats if any
        if whole_beats > 0:
            self.add_arcane_beat(whole_beats)
        
        return whole_beats, fractional_arcane_beats
    
    # Vitriol Experience methods (Promethean-specific)
    
    def add_vitriol_beat(self, amount=1):
        """Add vitriol beats to the character (Promethean-specific)"""
        self._vitriol_beats += amount
        # Check if we can convert vitriol beats to vitriol experience
        while self._vitriol_beats >= 5:
            self._vitriol_beats -= 5
            self._vitriol_experience += 1
        self._save_experience()
        self.obj.msg(f"You gained {amount} vitriol beat(s). You now have {self._vitriol_beats} vitriol beats and {self._vitriol_experience} vitriol experience.")
    
    def add_vitriol_experience(self, amount):
        """Add vitriol experience directly to the character (Promethean-specific)"""
        self._vitriol_experience += amount
        self._save_experience()
        self.obj.msg(f"You gained {amount} vitriol experience. You now have {self._vitriol_experience} vitriol experience.")
    
    def spend_vitriol_experience(self, amount):
        """Spend vitriol experience points (Promethean-specific)"""
        if self._vitriol_experience >= amount:
            self._vitriol_experience -= amount
            self._save_experience()
            self.obj.msg(f"You spent {amount} vitriol experience. You now have {self._vitriol_experience} vitriol experience remaining.")
            return True
        else:
            self.obj.msg(f"You don't have enough vitriol experience. You need {amount} but only have {self._vitriol_experience}.")
            return False
    
    @property
    def vitriol_beats(self):
        """Get current vitriol beats"""
        return self._vitriol_beats
    
    @property
    def vitriol_experience(self):
        """Get current vitriol experience"""
        return self._vitriol_experience
    
    @property
    def total_vitriol_beats(self):
        """Get total vitriol beats including fractional vitriol beats"""
        fractional_vitriol_beats = self.obj.attributes.get('fractional_vitriol_beats', default=0.0)
        return self._vitriol_beats + fractional_vitriol_beats
    
    def add_fractional_vitriol_beat(self, amount):
        """Add fractional vitriol beats to the character (Promethean-specific)"""
        fractional_vitriol_beats = self.obj.attributes.get('fractional_vitriol_beats', default=0.0)
        fractional_vitriol_beats += amount
        
        # Convert to whole beats when >= 1.0
        whole_beats = int(fractional_vitriol_beats)
        fractional_vitriol_beats = fractional_vitriol_beats - whole_beats
        
        # Save fractional vitriol beats
        self.obj.attributes.add('fractional_vitriol_beats', fractional_vitriol_beats)
        
        # Add whole beats if any
        if whole_beats > 0:
            self.add_vitriol_beat(whole_beats)
        
        return whole_beats, fractional_vitriol_beats
    
    # Reminisce Experience methods (Mummy-specific)
    
    def add_reminisce_beat(self, amount=1):
        """Add reminisce beats to the character (Mummy-specific)"""
        self._reminisce_beats += amount
        # Check if we can convert reminisce beats to reminisce experience
        while self._reminisce_beats >= 5:
            self._reminisce_beats -= 5
            self._reminisce_experience += 1
        self._save_experience()
        self.obj.msg(f"You gained {amount} reminisce beat(s). You now have {self._reminisce_beats} reminisce beats and {self._reminisce_experience} reminisce experience.")
    
    def add_reminisce_experience(self, amount):
        """Add reminisce experience directly to the character (Mummy-specific)"""
        self._reminisce_experience += amount
        self._save_experience()
        self.obj.msg(f"You gained {amount} reminisce experience. You now have {self._reminisce_experience} reminisce experience.")
    
    def spend_reminisce_experience(self, amount):
        """Spend reminisce experience points (Mummy-specific)"""
        if self._reminisce_experience >= amount:
            self._reminisce_experience -= amount
            self._save_experience()
            self.obj.msg(f"You spent {amount} reminisce experience. You now have {self._reminisce_experience} reminisce experience remaining.")
            return True
        else:
            self.obj.msg(f"You don't have enough reminisce experience. You need {amount} but only have {self._reminisce_experience}.")
            return False
    
    @property
    def reminisce_beats(self):
        """Get current reminisce beats"""
        return self._reminisce_beats
    
    @property
    def reminisce_experience(self):
        """Get current reminisce experience"""
        return self._reminisce_experience
    
    @property
    def total_reminisce_beats(self):
        """Get total reminisce beats including fractional reminisce beats"""
        fractional_reminisce_beats = self.obj.attributes.get('fractional_reminisce_beats', default=0.0)
        return self._reminisce_beats + fractional_reminisce_beats
    
    def add_fractional_reminisce_beat(self, amount):
        """Add fractional reminisce beats to the character (Mummy-specific)"""
        fractional_reminisce_beats = self.obj.attributes.get('fractional_reminisce_beats', default=0.0)
        fractional_reminisce_beats += amount
        
        # Convert to whole beats when >= 1.0
        whole_beats = int(fractional_reminisce_beats)
        fractional_reminisce_beats = fractional_reminisce_beats - whole_beats
        
        # Save fractional reminisce beats
        self.obj.attributes.add('fractional_reminisce_beats', fractional_reminisce_beats)
        
        # Add whole beats if any
        if whole_beats > 0:
            self.add_reminisce_beat(whole_beats)
        
        return whole_beats, fractional_reminisce_beats

# Experience costs for different improvements
EXPERIENCE_COSTS = {
    'attribute': 4,  # per dot
    'merit': 1,      # per dot
    'skill_specialty': 1,
    'skill': 2,      # per dot
    'integrity': 2   # per dot
}

# Ways to earn beats
BEAT_SOURCES = {
    'dramatic_failure': 1,      # When a dramatic failure occurs
    'exceptional_success': 1,   # When an exceptional success occurs
    'conditions': 1,            # When resolving a condition
    'aspirations': 1,           # When fulfilling an aspiration
    'story': 1,                 # At the end of a story
    'scene': 1,                 # At the end of a scene
    'session': 1,               # At the end of a session
    'roleplay': 1,              # For good roleplay
    'challenge': 1,             # For overcoming a significant challenge
    'sacrifice': 1,             # For making a meaningful sacrifice
    'discovery': 1,             # For making an important discovery
    'relationship': 1,          # For developing relationships
    'consequence': 1,           # For accepting consequences
    'learning': 1,              # For learning from mistakes
    'growth': 1                 # For character growth
}

# Mage-specific: Arcane Experience costs
# Some can be bought with EITHER normal XP or Arcane XP (marked 'either')
# Some MUST be bought with Arcane XP only (marked 'arcane_only')
ARCANE_EXPERIENCE_COSTS = {
    'arcanum_to_limit': {
        'cost': 4,              # per dot
        'currency': 'either'    # Can use normal XP or Arcane XP
    },
    'arcanum_above_limit': {
        'cost': 5,              # per dot
        'currency': 'either'    # Can use normal XP or Arcane XP
    },
    'gnosis': {
        'cost': 5,              # per dot
        'currency': 'either'    # Can use normal XP or Arcane XP
    },
    'rote': {
        'cost': 1,
        'currency': 'either'    # Can use normal XP or Arcane XP
    },
    'praxis': {
        'cost': 1,
        'currency': 'arcane_only'  # MUST use Arcane XP
    },
    'wisdom': {
        'cost': 2,              # per dot
        'currency': 'arcane_only'  # MUST use Arcane XP
    },
    'legacy_attainment_tutored': {
        'cost': 1,
        'currency': 'either'    # Can use normal XP or Arcane XP
    },
    'legacy_attainment_untutored': {
        'cost': 1,
        'currency': 'arcane_only'  # MUST use Arcane XP
    }
}

# Ways to earn Arcane Beats (Mage-specific)
ARCANE_BEAT_SOURCES = {
    'obsession': 1,                  # Fulfill or make major headway into an Obsession
    'magical_condition': 1,          # Resolve a Condition from spellcasting, Paradox, or magical effect
    'spell_dramatic_failure': 1,     # Voluntarily make a spellcasting roll a dramatic failure
    'act_of_hubris': 1,             # Risk an Act of Hubris against Wisdom
    'legacy_tutoring': 1,            # Spend a scene tutoring/being tutored in a Legacy
    'supernatural_encounter': 1      # Meaningful new supernatural encounter (ST discretion)
} 