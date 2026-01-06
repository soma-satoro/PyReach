"""
Pledge System for Changeling: The Lost 2nd Edition.

Handles three types of pledges:
- Sealing: Binding a statement or promise
- Oath: Larger pledge with other fae creatures
- Bargain: Pledge with mortal beings

Based on CTL 2e core book, pages 210-215.
"""

from datetime import datetime
from evennia.utils import logger
from evennia.utils.utils import lazy_property


# Pledge Types
PLEDGE_TYPE_SEALING = "sealing"
PLEDGE_TYPE_OATH = "oath"
PLEDGE_TYPE_BARGAIN = "bargain"

# Oath Subtypes
OATH_SOCIETAL = "societal"
OATH_PERSONAL = "personal"
OATH_HOSTILE = "hostile"

# Pledge Status
STATUS_ACTIVE = "active"
STATUS_FULFILLED = "fulfilled"
STATUS_BROKEN = "broken"
STATUS_RELEASED = "released"

# Sealing Consequences (Basic)
SEALING_CONSEQUENCES_BASIC = {
    "willpower_loss": "Loss of one Willpower point",
    "bashing_damage": "One point of bashing damage",
    "one_die_penalty_scene": "A one-die penalty to all rolls for one scene",
    "two_die_skill_penalty": "A two-die penalty on a specific Skill for one scene",
    "three_die_one_roll": "A three-die penalty for one specific roll",
    "minor_supernatural": "A minor supernatural effect for one scene"
}

# Sealing Consequences (Strengthened)
SEALING_CONSEQUENCES_STRONG = {
    "no_willpower_regain": "Loss of ability to regain Willpower for one day",
    "lethal_damage": "One point of lethal damage",
    "three_bashing_damage": "Three points of bashing damage",
    "no_willpower_spend": "Loss of ability to spend Willpower for one scene",
    "two_die_penalty_all": "A two-die penalty on all rolls for one scene",
    "three_die_skill_penalty": "A three-die penalty to all rolls with a specific Skill for one scene",
    "five_die_one_roll": "A five-die penalty to one specific roll",
    "contract_activation": "Use of one of the changeling's Contracts on the target"
}


class Pledge:
    """
    Represents a single pledge with all its details.
    """
    def __init__(self, pledge_id, pledge_type, participants, created_by, 
                 verbiage="", notes="", benefits=None, consequences=None,
                 status=STATUS_ACTIVE, created_at=None, oath_subtype=None,
                 strengthened=False, target_skill=None, contract_used=None):
        """
        Initialize a pledge.
        
        Args:
            pledge_id (str): Unique identifier for the pledge
            pledge_type (str): Type of pledge (sealing, oath, bargain)
            participants (list): List of character dbrefs involved
            created_by (str): Dbref of character who created the pledge
            verbiage (str): Custom text of the pledge
            notes (str): Biographical/additional notes
            benefits (dict): Benefits granted by the pledge
            consequences (dict): Consequences for breaking the pledge
            status (str): Current status of the pledge
            created_at (datetime): When the pledge was created
            oath_subtype (str): For oaths - societal, personal, or hostile
            strengthened (bool): For sealings - whether strengthened with Willpower
            target_skill (str): For skill-specific penalties
            contract_used (str): For contract-based consequences
        """
        self.pledge_id = pledge_id
        self.pledge_type = pledge_type
        self.participants = participants if participants else []
        self.created_by = created_by
        self.verbiage = verbiage
        self.notes = notes
        self.benefits = benefits if benefits else {}
        self.consequences = consequences if consequences else {}
        self.status = status
        self.created_at = created_at if created_at else datetime.now()
        self.oath_subtype = oath_subtype
        self.strengthened = strengthened
        self.target_skill = target_skill
        self.contract_used = contract_used
        
    def to_dict(self):
        """Convert pledge to dictionary for storage."""
        return {
            'pledge_id': self.pledge_id,
            'pledge_type': self.pledge_type,
            'participants': self.participants,
            'created_by': self.created_by,
            'verbiage': self.verbiage,
            'notes': self.notes,
            'benefits': self.benefits,
            'consequences': self.consequences,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'oath_subtype': self.oath_subtype,
            'strengthened': self.strengthened,
            'target_skill': self.target_skill,
            'contract_used': self.contract_used
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a pledge from a dictionary."""
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        return cls(**data)
    
    def is_active(self):
        """Check if the pledge is still active."""
        return self.status == STATUS_ACTIVE
    
    def is_participant(self, character_dbref):
        """Check if a character is a participant in this pledge."""
        return character_dbref in self.participants
    
    def get_display_name(self):
        """Get a display name for the pledge."""
        if self.pledge_type == PLEDGE_TYPE_SEALING:
            return f"Sealing #{self.pledge_id}"
        elif self.pledge_type == PLEDGE_TYPE_OATH:
            subtype_display = self.oath_subtype.capitalize() if self.oath_subtype else "Unknown"
            return f"{subtype_display} Oath #{self.pledge_id}"
        elif self.pledge_type == PLEDGE_TYPE_BARGAIN:
            return f"Bargain #{self.pledge_id}"
        return f"Pledge #{self.pledge_id}"


class PledgeHandler:
    """
    Handler for managing pledges on a character.
    """
    def __init__(self, obj):
        """
        Initialize the pledge handler.
        
        Args:
            obj: The character object this handler is attached to
        """
        self.obj = obj
        self._pledges = {}
        self._load_pledges()
    
    def _load_pledges(self):
        """Load pledges from the object's attributes."""
        pledges_data = self.obj.attributes.get('pledges', default={})
        for pledge_id, data in pledges_data.items():
            try:
                self._pledges[pledge_id] = Pledge.from_dict(data)
            except Exception as e:
                logger.error(f"Error loading pledge {pledge_id}: {e}")
    
    def _save_pledges(self):
        """Save pledges to the object's attributes."""
        pledges_data = {
            pledge_id: pledge.to_dict() 
            for pledge_id, pledge in self._pledges.items()
        }
        self.obj.attributes.add('pledges', pledges_data)
    
    def add_pledge(self, pledge):
        """
        Add a pledge to the character.
        
        Args:
            pledge (Pledge): The pledge to add
        """
        self._pledges[pledge.pledge_id] = pledge
        self._save_pledges()
        return pledge
    
    def get_pledge(self, pledge_id):
        """
        Get a specific pledge by ID.
        
        Args:
            pledge_id (str): The pledge ID to retrieve
            
        Returns:
            Pledge or None: The pledge if found, None otherwise
        """
        return self._pledges.get(pledge_id)
    
    def remove_pledge(self, pledge_id):
        """
        Remove a pledge from the character.
        
        Args:
            pledge_id (str): The pledge ID to remove
            
        Returns:
            bool: True if removed, False if not found
        """
        if pledge_id in self._pledges:
            del self._pledges[pledge_id]
            self._save_pledges()
            return True
        return False
    
    def get_all_pledges(self, include_inactive=False):
        """
        Get all pledges for this character.
        
        Args:
            include_inactive (bool): Whether to include non-active pledges
            
        Returns:
            list: List of Pledge objects
        """
        if include_inactive:
            return list(self._pledges.values())
        return [p for p in self._pledges.values() if p.is_active()]
    
    def get_pledges_by_type(self, pledge_type, include_inactive=False):
        """
        Get all pledges of a specific type.
        
        Args:
            pledge_type (str): The type of pledges to retrieve
            include_inactive (bool): Whether to include non-active pledges
            
        Returns:
            list: List of Pledge objects
        """
        pledges = self.get_all_pledges(include_inactive=include_inactive)
        return [p for p in pledges if p.pledge_type == pledge_type]
    
    def update_pledge_status(self, pledge_id, new_status):
        """
        Update the status of a pledge.
        
        Args:
            pledge_id (str): The pledge ID to update
            new_status (str): The new status
            
        Returns:
            bool: True if updated, False if not found
        """
        pledge = self.get_pledge(pledge_id)
        if pledge:
            pledge.status = new_status
            self._save_pledges()
            return True
        return False
    
    def break_pledge(self, pledge_id):
        """
        Mark a pledge as broken and apply consequences.
        
        Args:
            pledge_id (str): The pledge ID to break
            
        Returns:
            tuple: (success: bool, message: str, consequences: dict)
        """
        pledge = self.get_pledge(pledge_id)
        if not pledge:
            return False, "Pledge not found.", {}
        
        if not pledge.is_active():
            return False, "Pledge is not active.", {}
        
        # Update status
        pledge.status = STATUS_BROKEN
        self._save_pledges()
        
        # Apply oathbreaker condition if it's an oath
        if pledge.pledge_type == PLEDGE_TYPE_OATH:
            from world.conditions import Condition
            oathbreaker = Condition(
                name="Oathbreaker",
                description="You have broken a sworn oath. The Wyrd marks you as unfaithful.",
                is_persistent=True,
                resolution_method="Make recompense to all offended parties including the Wyrd itself."
            )
            self.obj.conditions.add(oathbreaker)
        
        return True, f"Pledge {pledge.get_display_name()} has been broken.", pledge.consequences
    
    def fulfill_pledge(self, pledge_id):
        """
        Mark a pledge as fulfilled and apply benefits.
        
        Args:
            pledge_id (str): The pledge ID to fulfill
            
        Returns:
            tuple: (success: bool, message: str)
        """
        pledge = self.get_pledge(pledge_id)
        if not pledge:
            return False, "Pledge not found."
        
        if not pledge.is_active():
            return False, "Pledge is not active."
        
        # Update status
        pledge.status = STATUS_FULFILLED
        self._save_pledges()
        
        # For sealings, grant a Beat
        if pledge.pledge_type == PLEDGE_TYPE_SEALING:
            current_beats = self.obj.db.stats.get("other", {}).get("beats", 0)
            self.obj.db.stats["other"]["beats"] = current_beats + 1
            
        return True, f"Pledge {pledge.get_display_name()} has been fulfilled. You gain a Beat!"
    
    def release_pledge(self, pledge_id):
        """
        Release a pledge (only for sealings - sealer releases the subject).
        
        Args:
            pledge_id (str): The pledge ID to release
            
        Returns:
            tuple: (success: bool, message: str)
        """
        pledge = self.get_pledge(pledge_id)
        if not pledge:
            return False, "Pledge not found."
        
        if pledge.pledge_type != PLEDGE_TYPE_SEALING:
            return False, "Only sealings can be released by the sealer."
        
        if not pledge.is_active():
            return False, "Pledge is not active."
        
        # Update status
        pledge.status = STATUS_RELEASED
        self._save_pledges()
        
        return True, f"Pledge {pledge.get_display_name()} has been released."
    
    def get_active_bargains_count(self):
        """
        Get the count of active bargains for this character.
        Used to determine stealth bonuses vs Huntsmen.
        
        Returns:
            int: Number of active bargains
        """
        return len(self.get_pledges_by_type(PLEDGE_TYPE_BARGAIN, include_inactive=False))


def get_next_pledge_id(character):
    """
    Generate the next available pledge ID for a character.
    
    Args:
        character: The character object
        
    Returns:
        str: The next pledge ID
    """
    handler = PledgeHandler(character)
    all_pledges = handler.get_all_pledges(include_inactive=True)
    
    if not all_pledges:
        return "1"
    
    # Get all numeric IDs and find the max
    numeric_ids = []
    for pledge in all_pledges:
        try:
            numeric_ids.append(int(pledge.pledge_id))
        except ValueError:
            pass
    
    if numeric_ids:
        return str(max(numeric_ids) + 1)
    return "1"


def validate_pledge_participants(caller, target_names, pledge_type):
    """
    Validate that all participants can engage in the specified pledge type.
    
    Args:
        caller: The character creating the pledge
        target_names (list): List of target character names
        pledge_type (str): Type of pledge being created
        
    Returns:
        tuple: (success: bool, targets: list, error_message: str)
    """
    from evennia.utils.search import search_object
    
    targets = []
    
    for name in target_names:
        # Search for the character
        results = search_object(name, typeclass='typeclasses.characters.Character')
        
        if not results:
            return False, [], f"Could not find character: {name}"
        
        if len(results) > 1:
            return False, [], f"Multiple matches for: {name}. Please be more specific."
        
        target = results[0]
        targets.append(target)
        
        # Validate based on pledge type
        if pledge_type == PLEDGE_TYPE_OATH:
            # Oaths can only be sworn with fae creatures (changelings)
            template = target.db.stats.get("other", {}).get("template", "Mortal")
            if template.lower() != "changeling" and not target.db.is_npc:
                return False, [], f"{target.name} is not a changeling and cannot swear oaths."
        
        elif pledge_type == PLEDGE_TYPE_BARGAIN:
            # Bargains are with mortal beings
            template = target.db.stats.get("other", {}).get("template", "Mortal")
            if template.lower() == "changeling":
                return False, [], f"{target.name} is a changeling. Use oaths for fae-to-fae pledges."
    
    return True, targets, ""
