"""
Group TypeClasses for Evennia.

This module contains the TypeClass definitions for groups, replacing the Django model approach
with proper Evennia TypeClasses for better integration and functionality.
"""

from evennia.objects.objects import DefaultObject
from evennia import create_object, logger
from evennia.comms.models import ChannelDB
from evennia.utils import create as utils_create
from django.conf import settings


class Group(DefaultObject):
    """
    A TypeClass for groups that can contain characters as members.
    
    This replaces the Django model approach with a proper Evennia TypeClass,
    providing better integration with the Evennia architecture.
    """
    
    # Group types as choices
    GROUP_TYPES = [
        ('coterie', 'Coterie'),      # Vampire groups
        ('pack', 'Pack'),            # Werewolf groups  
        ('cabal', 'Cabal'),          # Mage groups
        ('motley', 'Motley'),        # Changeling groups
        ('krewe', 'Krewe'),          # Geist groups
        ('cell', 'Cell'),            # Hunter cells
        ('mysterycult', 'Mystery Cult'), # Mystery Cults (Mortal/any)
        ('agency', 'Agency'),        # Mortal organizations
        ('cult', 'Cult'),            # Mummy cults
        ('other', 'Other'),          # Generic groups
    ]
    
    def at_object_creation(self):
        """Called when the group is first created."""
        super().at_object_creation()
        
        # Set default attributes
        self.db.group_type = 'other'
        self.db.description = ''
        self.db.notes = ''
        self.db.is_public = True
        self.db.leader = None
        self.db.members = []
        self.db.member_data = {}  # Store member titles, roles, etc.
        self.db.created_at = self.date_created
        
        # Group merits and stats
        self.db.merits = {}  # Store group-specific merits
        self.db.stats = {}   # Store additional group stats
        self.db.tactics = []  # Store known tactics (for Hunter cells)
        
        # Totem system (for packs and similar groups)
        self.db.totem = {
            'name': '',
            'concept': '',
            'aspiration': '',
            'ban': '',
            'rank': 1,
            'attributes': {'power': 0, 'finesse': 0, 'resistance': 0},
            'essence': {'current': 0, 'max': 0},
            'influence': {},  # Dict of influence types and dots
            'numina': [],  # List of numina names
            'advantage': {},  # The advantage granted to pack members
            'notes': ''
        }
        
        # Mystery Cult benefits (for cabals)
        # Stores what benefits are granted at each initiation level
        self.db.mystery_cult_benefits = {
            1: {'type': '', 'name': '', 'description': ''},
            2: {'type': '', 'name': '', 'description': ''},
            3: {'type': '', 'name': '', 'description': ''},
            4: {'type': '', 'name': '', 'description': ''},
            5: {'type': '', 'name': '', 'description': ''}
        }
        
        # Auto-assign group ID
        self._assign_group_id()
        
        # Create associated channel
        self._create_group_channel()
    
    def _assign_group_id(self):
        """Assign a unique group ID."""
        # Get all existing group IDs
        existing_ids = []
        for obj in Group.objects.all():
            if hasattr(obj, 'db') and obj.db.group_id:
                existing_ids.append(obj.db.group_id)
        
        # Find the lowest available ID
        group_id = 1
        while group_id in existing_ids:
            group_id += 1
        
        self.db.group_id = group_id
    
    def _create_group_channel(self):
        """Create the associated channel for this group."""
        channel_name = self.channel_name
        
        if ChannelDB.objects.filter(db_key=channel_name).exists():
            logger.log_info(f"Channel '{channel_name}' already exists for group '{self.name}'")
            return
        
        # Make sure group_id is available
        if not hasattr(self.db, 'group_id') or self.db.group_id is None:
            logger.log_err(f"Cannot create channel for group '{self.name}' - group_id not set")
            return
        
        # Create channel with appropriate locks
        lock_string = (
            f"control:perm(Admin);"
            f"listen:group_member({self.db.group_id}) or perm(Admin);"
            f"send:group_member({self.db.group_id}) or perm(Admin)"
        )
        
        try:
            channel = utils_create.create_channel(
                channel_name,
                desc=f"Group channel for {self.name}",
                locks=lock_string
            )
            logger.log_info(f"Created channel '{channel_name}' for group '{self.name}'")
        except Exception as e:
            logger.log_err(f"Failed to create channel '{channel_name}': {str(e)}")
    
    @property
    def channel_name(self):
        """Returns the channel name for this group."""
        return ''.join(c for c in self.name if c.isalnum())
    
    @property
    def group_id(self):
        """Returns the group ID."""
        return self.db.group_id
    
    @property
    def group_type(self):
        """Returns the group type."""
        return self.db.group_type
    
    @group_type.setter
    def group_type(self, value):
        """Set the group type."""
        valid_types = [choice[0] for choice in self.GROUP_TYPES]
        if value in valid_types:
            self.db.group_type = value
        else:
            raise ValueError(f"Invalid group type. Must be one of: {', '.join(valid_types)}")
    
    def get_group_type_display(self):
        """Get the display name for the group type."""
        type_dict = dict(self.GROUP_TYPES)
        return type_dict.get(self.db.group_type, 'Other')
    
    @property
    def description(self):
        """Returns the group description."""
        return self.db.description
    
    @description.setter
    def description(self, value):
        """Set the group description."""
        self.db.description = value
    
    @property
    def notes(self):
        """Returns the group notes."""
        return self.db.notes
    
    @notes.setter
    def notes(self, value):
        """Set the group notes."""
        self.db.notes = value
    
    @property
    def is_public(self):
        """Returns whether the group is public."""
        return self.db.is_public
    
    @is_public.setter
    def is_public(self, value):
        """Set the group's public status."""
        self.db.is_public = bool(value)
    
    @property
    def leader(self):
        """Returns the group leader."""
        return self.db.leader
    
    @leader.setter
    def leader(self, character):
        """Set the group leader."""
        if character and not self.is_member(character):
            self.add_member(character)
        self.db.leader = character
    
    @property
    def members(self):
        """Returns a list of group members."""
        # Clean up any None entries that might have accumulated
        members = [member for member in self.db.members if member]
        self.db.members = members
        return members
    
    def is_member(self, character):
        """Check if a character is a member of this group."""
        return character in self.members
    
    def add_member(self, character):
        """Add a character to the group."""
        if not self.is_member(character):
            self.db.members.append(character)
            
            # Initialize member data if not exists
            if character not in self.db.member_data:
                self.db.member_data[character] = {
                    'title': '',
                    'role': '',
                    'joined_at': character.db.last_login or self.db.created_at
                }
            
            # Update character's group attribute
            if not character.attributes.has('groups'):
                character.attributes.add('groups', [])
            
            groups = character.attributes.get('groups', [])
            if self.name not in groups:
                groups.append(self.name)
                character.attributes.add('groups', groups)
            
            # Add to channel
            channel = ChannelDB.objects.filter(db_key=self.channel_name).first()
            if channel:
                channel.connect(character)
            
            logger.log_info(f"Added {character.name} to group '{self.name}'")
            return True
        return False
    
    def remove_member(self, character):
        """Remove a character from the group."""
        if self.is_member(character):
            self.db.members.remove(character)
            
            # Remove member data
            if character in self.db.member_data:
                del self.db.member_data[character]
            
            # Clear leader if this was the leader
            if self.db.leader == character:
                self.db.leader = None
            
            # Update character's group attribute
            if character.attributes.has('groups'):
                groups = character.attributes.get('groups', [])
                if self.name in groups:
                    groups.remove(self.name)
                    character.attributes.add('groups', groups)
            
            # Remove from channel
            channel = ChannelDB.objects.filter(db_key=self.channel_name).first()
            if channel:
                channel.disconnect(character)
            
            logger.log_info(f"Removed {character.name} from group '{self.name}'")
            return True
        return False
    
    def get_member_title(self, character):
        """Get a member's title in the group."""
        if character in self.db.member_data:
            return self.db.member_data[character].get('title', '')
        return ''
    
    def set_member_title(self, character, title):
        """Set a member's title in the group."""
        if self.is_member(character):
            if character not in self.db.member_data:
                self.db.member_data[character] = {}
            self.db.member_data[character]['title'] = title
            return True
        return False
    
    def get_member_role(self, character):
        """Get a member's role in the group."""
        if character in self.db.member_data:
            return self.db.member_data[character].get('role', '')
        return ''
    
    def set_member_role(self, character, role):
        """Set a member's role in the group."""
        if self.is_member(character):
            if character not in self.db.member_data:
                self.db.member_data[character] = {}
            self.db.member_data[character]['role'] = role
            return True
        return False
    
    def get_member_count(self):
        """Get the number of members in the group."""
        return len(self.members)
    
    def get_online_members(self):
        """Get list of online members."""
        return [member for member in self.members if member.has_account]
    
    def get_online_count(self):
        """Get the number of online members."""
        return len(self.get_online_members())
    
    # Merit Management
    def set_merit(self, merit_name, rating):
        """Set a group merit rating."""
        if not self.db.merits:
            self.db.merits = {}
        self.db.merits[merit_name] = int(rating)
    
    def get_merit(self, merit_name):
        """Get a group merit rating."""
        if not self.db.merits:
            return 0
        return self.db.merits.get(merit_name, 0)
    
    def remove_merit(self, merit_name):
        """Remove a group merit."""
        if self.db.merits and merit_name in self.db.merits:
            del self.db.merits[merit_name]
    
    def get_all_merits(self):
        """Get all group merits."""
        if not self.db.merits:
            return {}
        return dict(self.db.merits)
    
    # Tactics Management (for Hunter cells)
    def add_tactic(self, tactic_name):
        """Add a tactic to the cell's known tactics."""
        if not self.db.tactics:
            self.db.tactics = []
        
        if tactic_name not in self.db.tactics:
            self.db.tactics.append(tactic_name)
            return True
        return False
    
    def remove_tactic(self, tactic_name):
        """Remove a tactic from the cell's known tactics."""
        if not self.db.tactics:
            return False
        
        if tactic_name in self.db.tactics:
            self.db.tactics.remove(tactic_name)
            return True
        return False
    
    def get_all_tactics(self):
        """Get all known tactics."""
        if not self.db.tactics:
            return []
        return list(self.db.tactics)
    
    def has_tactic(self, tactic_name):
        """Check if the cell knows a specific tactic."""
        if not self.db.tactics:
            return False
        return tactic_name in self.db.tactics
    
    # Totem Management
    def calculate_totem_points(self, debug=False):
        """Calculate total totem points from member contributions."""
        total = 0
        for member in self.members:
            if not hasattr(member, 'db'):
                if debug:
                    logger.log_info(f"Member {member} has no db attribute")
                continue
                
            if not member.db.stats:
                if debug:
                    logger.log_info(f"Member {member.name} has no stats")
                continue
            
            merits = member.db.stats.get('merits', {})
            if debug:
                logger.log_info(f"Member {member.name} merits: {list(merits.keys())}")
            
            # Try both capitalized and lowercase versions
            totem_merit = merits.get('Totem')
            if totem_merit is None:
                totem_merit = merits.get('totem')
            
            if totem_merit is None:
                if debug:
                    logger.log_info(f"Member {member.name} has no totem merit")
                continue
            
            # Extract the numeric value
            totem_value = 0
            # Check for dict-like attributes (works with dict and _SaverDict)
            if hasattr(totem_merit, '__getitem__') and hasattr(totem_merit, 'keys'):
                # Try 'dots' first (your system)
                if 'dots' in totem_merit:
                    totem_value = totem_merit['dots']
                    if debug:
                        logger.log_info(f"Member {member.name} totem dots: {totem_value}")
                # Then try 'rating' (fallback)
                elif 'rating' in totem_merit:
                    totem_value = totem_merit['rating']
                    if debug:
                        logger.log_info(f"Member {member.name} totem rating: {totem_value}")
            else:
                totem_value = totem_merit
                if debug:
                    logger.log_info(f"Member {member.name} totem value: {totem_value}")
            
            # Convert to int safely
            try:
                totem_int = int(totem_value)
                total += totem_int
                if debug:
                    logger.log_info(f"Added {totem_int} from {member.name}, total now {total}")
            except (ValueError, TypeError) as e:
                # If conversion fails, skip this member
                if debug:
                    logger.log_info(f"Failed to convert {totem_value} to int for {member.name}: {e}")
                continue
        return total
    
    def set_totem_attribute(self, attribute, value):
        """Set a totem attribute (power, finesse, or resistance)."""
        if not self.db.totem:
            self.db.totem = {
                'name': '', 'concept': '', 'aspiration': '', 'ban': '',
                'rank': 1, 'attributes': {'power': 0, 'finesse': 0, 'resistance': 0},
                'essence': {'current': 0, 'max': 0}, 'influence': {},
                'numina': [], 'advantage': {}, 'notes': ''
            }
        
        attribute = attribute.lower()
        if attribute in ['power', 'finesse', 'resistance']:
            self.db.totem['attributes'][attribute] = int(value)
            self._recalculate_totem_derived_stats()
    
    def _recalculate_totem_derived_stats(self):
        """Recalculate totem's derived stats based on attributes."""
        if not self.db.totem:
            return
        
        attrs = self.db.totem['attributes']
        total_attrs = sum(attrs.values())
        
        # Determine rank based on total attributes
        if total_attrs <= 5:
            rank = 1
        elif total_attrs <= 10:
            rank = 2
        elif total_attrs <= 15:
            rank = 3
        elif total_attrs <= 20:
            rank = 4
        else:
            rank = 5
        
        self.db.totem['rank'] = rank
        
        # Calculate max essence (lower of totem points or rank maximum)
        totem_points = self.calculate_totem_points()
        rank_max_essence = {1: 10, 2: 15, 3: 20, 4: 25, 5: 50}
        self.db.totem['essence']['max'] = min(totem_points, rank_max_essence.get(rank, 10))
        
        # Corpus = Power + Resistance (spirits use this as health)
        # Willpower = Finesse + Resistance
        # Size is typically 3-5 for spirits
        # Defense = Finesse or Resistance (whichever is lower)
        # Initiative = Finesse + Resistance
    
    def add_totem_numen(self, numen_name):
        """Add a numen to the totem."""
        if not self.db.totem:
            self.db.totem = {
                'name': '', 'concept': '', 'aspiration': '', 'ban': '',
                'rank': 1, 'attributes': {'power': 0, 'finesse': 0, 'resistance': 0},
                'essence': {'current': 0, 'max': 0}, 'influence': {},
                'numina': [], 'advantage': {}, 'notes': ''
            }
        
        if numen_name not in self.db.totem['numina']:
            self.db.totem['numina'].append(numen_name)
    
    def remove_totem_numen(self, numen_name):
        """Remove a numen from the totem."""
        if self.db.totem and numen_name in self.db.totem['numina']:
            self.db.totem['numina'].remove(numen_name)
    
    def set_totem_property(self, property_name, value):
        """Set a totem property (name, concept, aspiration, ban, notes)."""
        if not self.db.totem:
            self.db.totem = {
                'name': '', 'concept': '', 'aspiration': '', 'ban': '',
                'rank': 1, 'attributes': {'power': 0, 'finesse': 0, 'resistance': 0},
                'essence': {'current': 0, 'max': 0}, 'influence': {},
                'numina': [], 'advantage': {}, 'notes': ''
            }
        
        if property_name in ['name', 'concept', 'aspiration', 'ban', 'notes']:
            self.db.totem[property_name] = value
    
    def set_totem_influence(self, influence_type, dots):
        """Set totem influence."""
        if not self.db.totem:
            self.db.totem = {
                'name': '', 'concept': '', 'aspiration': '', 'ban': '',
                'rank': 1, 'attributes': {'power': 0, 'finesse': 0, 'resistance': 0},
                'essence': {'current': 0, 'max': 0}, 'influence': {},
                'numina': [], 'advantage': {}, 'notes': ''
            }
        
        self.db.totem['influence'][influence_type] = int(dots)
    
    def set_totem_advantage(self, advantage_type, advantage_name, rating=1):
        """Set the advantage granted by the totem to pack members."""
        if not self.db.totem:
            self.db.totem = {
                'name': '', 'concept': '', 'aspiration': '', 'ban': '',
                'rank': 1, 'attributes': {'power': 0, 'finesse': 0, 'resistance': 0},
                'essence': {'current': 0, 'max': 0}, 'influence': {},
                'numina': [], 'advantage': {}, 'notes': ''
            }
        
        self.db.totem['advantage'] = {
            'type': advantage_type,  # 'attribute', 'skill', 'specialty', or 'merit'
            'name': advantage_name,
            'rating': int(rating)
        }
    
    def get_totem_info(self):
        """Get formatted totem information."""
        if not self.db.totem or not self.db.totem.get('name'):
            return None
        
        return dict(self.db.totem)
    
    # Mystery Cult Management
    def set_mystery_benefit(self, level, benefit_type, name, description=''):
        """Set a mystery cult benefit at a specific initiation level."""
        if not self.db.mystery_cult_benefits:
            self.db.mystery_cult_benefits = {
                1: {'type': '', 'name': '', 'description': ''},
                2: {'type': '', 'name': '', 'description': ''},
                3: {'type': '', 'name': '', 'description': ''},
                4: {'type': '', 'name': '', 'description': ''},
                5: {'type': '', 'name': '', 'description': ''}
            }
        
        if level < 1 or level > 5:
            return False
        
        valid_types = ['specialty', 'merit', 'skill', 'other']
        if benefit_type.lower() not in valid_types:
            return False
        
        self.db.mystery_cult_benefits[level] = {
            'type': benefit_type.lower(),
            'name': name,
            'description': description
        }
        return True
    
    def get_mystery_benefit(self, level):
        """Get mystery cult benefit at a specific level."""
        if not self.db.mystery_cult_benefits:
            return None
        return self.db.mystery_cult_benefits.get(level, None)
    
    def get_all_mystery_benefits(self):
        """Get all mystery cult benefits."""
        if not self.db.mystery_cult_benefits:
            return {}
        return dict(self.db.mystery_cult_benefits)
    
    def clear_mystery_benefit(self, level):
        """Clear a mystery cult benefit at a specific level."""
        if not self.db.mystery_cult_benefits:
            return False
        
        if level < 1 or level > 5:
            return False
        
        self.db.mystery_cult_benefits[level] = {
            'type': '',
            'name': '',
            'description': ''
        }
        return True
    
    def get_character_mystery_benefits(self, character):
        """
        Get the benefits a character should have based on their Mystery Cult Initiation level.
        Returns a list of benefits the character is entitled to.
        """
        if not hasattr(character, 'db') or not character.db.stats:
            return []
        
        merits = character.db.stats.get('merits', {})
        
        # Try all possible variations
        initiation_merit = merits.get('Mystery Cult Initiation')
        if initiation_merit is None:
            initiation_merit = merits.get('mystery cult initiation')
        if initiation_merit is None:
            initiation_merit = merits.get('mystery_cult_initiation')  # With underscores
        
        if initiation_merit is None:
            return []
        
        # Extract the numeric value
        initiation_level = 0
        # Check for dict-like attributes (works with dict and _SaverDict)
        if hasattr(initiation_merit, '__getitem__') and hasattr(initiation_merit, 'keys'):
            # Try 'dots' first (your system)
            if 'dots' in initiation_merit:
                initiation_level = initiation_merit['dots']
            # Then try 'rating' (fallback)
            elif 'rating' in initiation_merit:
                initiation_level = initiation_merit['rating']
        else:
            initiation_level = initiation_merit
        
        # Convert to int safely
        try:
            initiation_level = int(initiation_level)
        except (ValueError, TypeError):
            return []
        
        if initiation_level <= 0:
            return []
        
        benefits = []
        for level in range(1, min(initiation_level + 1, 6)):
            benefit = self.get_mystery_benefit(level)
            if benefit and benefit.get('name'):
                benefits.append((level, benefit))
        
        return benefits
    
    def delete(self):
        """Override delete to clean up associated data."""
        # Remove all members (this handles attribute cleanup)
        for member in self.members[:]:  # Copy list to avoid modification during iteration
            self.remove_member(member)
        
        # Delete associated channel
        channel = ChannelDB.objects.filter(db_key=self.channel_name).first()
        if channel:
            # Disconnect any remaining subscribers
            for subscriber in channel.subscriptions.all():
                channel.disconnect(subscriber)
            channel.delete()
            logger.log_info(f"Deleted channel '{self.channel_name}'")
        
        # Call parent delete
        super().delete()
        logger.log_info(f"Deleted group '{self.name}' (ID #{self.db.group_id})")


# Convenience functions for group management
def create_group(name, group_type='other', description='', creator=None):
    """
    Create a new group.
    
    Args:
        name (str): Name of the group
        group_type (str): Type of group (default: 'other')
        description (str): Group description
        creator (Character): Character creating the group
        
    Returns:
        Group: The created group object
    """
    # Check if group with this name already exists
    existing = Group.objects.filter(db_key=name).first()
    if existing:
        raise ValueError(f"A group named '{name}' already exists.")
    
    # Create the group
    group = create_object(
        typeclass="typeclasses.groups.Group",
        key=name,
        location=None  # Groups don't have a physical location
    )
    
    # Set initial properties
    group.group_type = group_type
    group.description = description
    
    if creator:
        group.leader = creator
    
    return group


def get_group_by_id(group_id):
    """
    Get a group by its ID.
    
    Args:
        group_id (int): The group ID
        
    Returns:
        Group or None: The group object if found
    """
    for group in Group.objects.all():
        if hasattr(group, 'db') and group.db.group_id == group_id:
            return group
    return None


def get_group_by_name(name):
    """
    Get a group by its name (case-insensitive).
    
    Args:
        name (str): The group name
        
    Returns:
        Group or None: The group object if found
    """
    return Group.objects.filter(db_key__iexact=name).first()


def get_all_groups():
    """
    Get all groups.
    
    Returns:
        QuerySet: All group objects
    """
    return Group.objects.all()


def get_public_groups():
    """
    Get all public groups.
    
    Returns:
        list: List of public group objects
    """
    all_groups = Group.objects.all()
    return [group for group in all_groups if group.is_public]


def get_character_groups(character):
    """
    Get all groups a character belongs to.
    
    Args:
        character: The character object
        
    Returns:
        list: List of group objects the character belongs to
    """
    all_groups = Group.objects.all()
    return [group for group in all_groups if group.is_member(character)] 