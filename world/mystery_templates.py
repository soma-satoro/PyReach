"""
Mystery Templates

Pre-built mystery templates that staff can quickly deploy and customize.
These provide examples and starting points for common mystery types.
"""

from typeclasses.mysteries import MysteryManager


class MysteryTemplate:
    """Base class for mystery templates."""
    
    def __init__(self, title, description, category="general", difficulty=1):
        self.title = title
        self.description = description
        self.category = category
        self.difficulty = difficulty
        self.clues = []
        self.prerequisites = {}
        self.conditions = {}
        self.revelations = {}
        self.access_restrictions = {}
    
    def add_clue(self, name, description, tags=None, elements=None):
        """Add a clue to the template."""
        clue_data = {
            'name': name,
            'description': description,
            'tags': tags or [],
            'elements': elements or []
        }
        self.clues.append(clue_data)
        return len(self.clues) - 1  # Return index for referencing
    
    def set_prerequisite(self, clue_index, prereq_indices):
        """Set prerequisites for a clue."""
        self.prerequisites[clue_index] = prereq_indices
    
    def set_condition(self, clue_index, conditions):
        """Set discovery conditions for a clue."""
        self.conditions[clue_index] = conditions
    
    def add_revelation(self, trigger_id, required_clue_indices, revelation_text, unlock_indices=None):
        """Add a revelation trigger."""
        self.revelations[trigger_id] = {
            'required_clues': required_clue_indices,
            'revelation': revelation_text,
            'unlock_clues': unlock_indices or []
        }
    
    def create_mystery(self, created_by):
        """Create the actual mystery from this template."""
        mystery = MysteryManager.create_mystery(
            title=self.title,
            description=self.description,
            created_by=created_by,
            category=self.category,
            difficulty=self.difficulty
        )
        
        # Add clues
        clue_id_map = {}  # Map template indices to actual clue IDs
        for i, clue_data in enumerate(self.clues):
            clue_id = mystery.add_clue(
                name=clue_data['name'],
                description=clue_data['description'],
                tags=clue_data['tags'],
                elements=clue_data['elements']
            )
            clue_id_map[i] = clue_id
        
        # Set prerequisites
        for clue_index, prereq_indices in self.prerequisites.items():
            if clue_index in clue_id_map:
                prereq_ids = [clue_id_map[i] for i in prereq_indices if i in clue_id_map]
                mystery.set_clue_prerequisites(clue_id_map[clue_index], prereq_ids)
        
        # Set conditions
        for clue_index, conditions in self.conditions.items():
            if clue_index in clue_id_map:
                mystery.db.clues[clue_id_map[clue_index]]['discovery_conditions'] = conditions
        
        # Add revelations
        for trigger_id, revelation_data in self.revelations.items():
            required_ids = [clue_id_map[i] for i in revelation_data['required_clues'] if i in clue_id_map]
            unlock_ids = [clue_id_map[i] for i in revelation_data.get('unlock_clues', []) if i in clue_id_map]
            mystery.add_revelation_trigger(
                trigger_id,
                required_ids,
                revelation_data['revelation'],
                unlock_ids
            )
        
        # Apply access restrictions
        for restriction_type, values in self.access_restrictions.items():
            setattr(mystery.db, restriction_type, values)
        
        return mystery


# Predefined Mystery Templates

class MissingPersonTemplate(MysteryTemplate):
    """Template for missing person investigations."""
    
    def __init__(self):
        super().__init__(
            title="Missing Person Investigation",
            description="Someone has disappeared under mysterious circumstances. Investigate their last known whereabouts and uncover what happened.",
            category="crime",
            difficulty=2
        )
        
        # Basic clues
        clue_0 = self.add_clue(
            "Last Known Location",
            "The missing person was last seen at a specific location. What were they doing there?",
            tags=["incomplete"]
        )
        
        clue_1 = self.add_clue(
            "Personal Belongings",
            "Items left behind that might provide clues about their state of mind or destination.",
            tags=["incomplete"]
        )
        
        clue_2 = self.add_clue(
            "Witness Account",
            "Someone saw something unusual around the time of disappearance.",
            tags=["incomplete"]
        )
        
        clue_3 = self.add_clue(
            "Paper and Digital Trail",
            "Phone records, letters, account activity, or other traces of their recent movements.",
            tags=["critical"]
        )
        
        clue_4 = self.add_clue(
            "Motive Discovery",
            "Why might someone want to disappear or be taken? Personal, professional, or supernatural reasons.",
            tags=["critical"]
        )
        
        # Set prerequisites - need basic evidence before understanding motive
        self.set_prerequisite(3, [0, 1])  # Digital trail needs location and belongings
        self.set_prerequisite(4, [2, 3])  # Motive needs witness and digital evidence
        
        # Set discovery conditions
        self.set_condition(0, {"skill_roll": {"skill": "investigation", "attribute": "wits", "difficulty": 2}})
        self.set_condition(2, {"attribute_minimum": {"attribute": "manipulation", "minimum": 2}})
        self.set_condition(3, {"merit_required": {"merit": "contacts"}})
        self.set_condition(4, {"skill_roll": {"skill": "investigation", "attribute": "wits", "difficulty": 4}})
        
        # Add revelation
        self.add_revelation(
            "truth_revealed",
            [2, 3, 4],
            "The evidence points to whether this was voluntary disappearance, kidnapping, or something supernatural."
        )


class OccultMysteryTemplate(MysteryTemplate):
    """Template for supernatural/occult investigations."""
    
    def __init__(self):
        super().__init__(
            title="Occult Investigation",
            description="Strange events and supernatural phenomena require investigation by those who understand the hidden world.",
            category="supernatural",
            difficulty=3
        )
        
        # Occult-specific clues
        clue_0 = self.add_clue(
            "Strange Phenomena",
            "Unexplained events that normal people might dismiss but you recognize as supernatural.",
            tags=["supernatural", "incomplete"]
        )
        
        clue_1 = self.add_clue(
            "Occult Symbols",
            "Mystical symbols or ritualistic markings that provide clues about the type of supernatural activity.",
            tags=["supernatural", "critical"]
        )
        
        clue_2 = self.add_clue(
            "Supernatural Witness",
            "Someone who has supernatural senses or knowledge provides crucial information.",
            tags=["supernatural"]
        )
        
        clue_3 = self.add_clue(
            "Ritual Components",
            "Physical evidence of supernatural rituals or spell components.",
            tags=["supernatural", "incomplete"]
        )
        
        clue_4 = self.add_clue(
            "Ancient Knowledge",
            "Historical or mythological information that explains the supernatural events.",
            tags=["supernatural", "critical"]
        )
        
        # Prerequisites - need to understand phenomena before recognizing ritual
        self.set_prerequisite(1, [0])
        self.set_prerequisite(3, [1])
        self.set_prerequisite(4, [1, 2])
        
        # Conditions - requires occult knowledge
        self.set_condition(0, {"skill_roll": {"skill": "investigation", "difficulty": 2}})
        self.set_condition(1, {"merit_required": {"merit": "occult"}})
        self.set_condition(2, {"attribute_minimum": {"attribute": "wits", "minimum": 3}})
        self.set_condition(3, {"skill_roll": {"skill": "occult", "difficulty": 3}})
        self.set_condition(4, {"skill_roll": {"skill": "academics", "difficulty": 4}})
        
        # Revelation
        self.add_revelation(
            "supernatural_truth",
            [1, 3, 4],
            "The supernatural forces at work become clear, revealing the true nature of the threat and how to counter it."
        )
        
        # Restrict to supernatural templates
        self.access_restrictions['allowed_templates'] = [
            'vampire', 'werewolf', 'mage', 'changeling', 'mummy', 'demon', 'hunter', 'geist'
        ]


class SectConspiracyTemplate(MysteryTemplate):
    """Template for sect, covenant, or order conspiracy investigations."""
    
    def __init__(self):
        super().__init__(
            title="Sect Conspiracy",
            description=(
                "Investigate covert influence, resource laundering, and backroom alliances "
                "between factions in the supernatural community."
            ),
            category="political",
            difficulty=3
        )
        
        clue_0 = self.add_clue(
            "Resource Irregularities",
            "Suspicious use of havens, influence, boons, or funds tied to a hidden agenda.",
            tags=["incomplete"]
        )
        
        clue_1 = self.add_clue(
            "Insider Testimony",
            "Someone inside the faction hierarchy provides partial but valuable information.",
            tags=["critical"]
        )
        
        clue_2 = self.add_clue(
            "Ledger and Correspondence Trail",
            "Letters, ledgers, and encrypted notes reveal the conspiracy's operational scope.",
            tags=["incomplete"]
        )
        
        clue_3 = self.add_clue(
            "Power Brokers",
            "Identification of the key conspirators and what each one gains from the plot.",
            tags=["critical"]
        )
        
        clue_4 = self.add_clue(
            "Proof of Breach",
            "Concrete proof of acts that violate local laws, compacts, or sect doctrine.",
            tags=["critical"]
        )
        
        # Prerequisites
        self.set_prerequisite(1, [0])
        self.set_prerequisite(2, [0, 1])
        self.set_prerequisite(3, [1, 2])
        self.set_prerequisite(4, [2, 3])
        
        # Conditions
        self.set_condition(0, {"skill_roll": {"skill": "investigation", "difficulty": 2}})
        self.set_condition(1, {"merit_required": {"merit": "contacts"}})
        self.set_condition(2, {"skill_roll": {"skill": "computer", "difficulty": 3}})
        self.set_condition(3, {"attribute_minimum": {"attribute": "intelligence", "minimum": 3}})
        self.set_condition(4, {"skill_roll": {"skill": "investigation", "difficulty": 4}})
        
        # Revelation
        self.add_revelation(
            "conspiracy_exposed",
            [3, 4],
            "The full scope of the faction conspiracy is revealed, exposing the sponsor, beneficiaries, and vulnerable points."
        )


class HistoricalMysteryTemplate(MysteryTemplate):
    """Template for historical mysteries and archaeological discoveries."""
    
    def __init__(self):
        super().__init__(
            title="Historical Mystery",
            description="Uncover secrets from the past that have relevance to present events.",
            category="historical",
            difficulty=2
        )
        
        clue_0 = self.add_clue(
            "Historical Document",
            "An old document, diary, or record that provides the first clue to past events.",
            tags=["incomplete"]
        )
        
        clue_1 = self.add_clue(
            "Archaeological Evidence",
            "Physical artifacts or locations that support the historical account.",
            tags=["incomplete"]
        )
        
        clue_2 = self.add_clue(
            "Expert Opinion",
            "A historian, archaeologist, or other expert provides crucial context.",
            tags=["critical"]
        )
        
        clue_3 = self.add_clue(
            "Modern Connection",
            "How the historical events connect to current situations or people.",
            tags=["critical"]
        )
        
        clue_4 = self.add_clue(
            "Hidden Truth",
            "The real story behind the historical events, often different from official records.",
            tags=["critical"]
        )
        
        # Prerequisites
        self.set_prerequisite(1, [0])
        self.set_prerequisite(2, [0, 1])
        self.set_prerequisite(3, [2])
        self.set_prerequisite(4, [2, 3])
        
        # Conditions
        self.set_condition(0, {"skill_roll": {"skill": "investigation", "difficulty": 2}})
        self.set_condition(1, {"skill_roll": {"skill": "academics", "difficulty": 2}})
        self.set_condition(2, {"merit_required": {"merit": "contacts"}})
        self.set_condition(3, {"attribute_minimum": {"attribute": "intelligence", "minimum": 2}})
        self.set_condition(4, {"skill_roll": {"skill": "academics", "difficulty": 4}})
        
        # Revelation
        self.add_revelation(
            "historical_truth",
            [3, 4],
            "The true historical events are revealed, showing how the past continues to influence the present."
        )


# Registry of available templates
MYSTERY_TEMPLATES = {
    'missing_person': MissingPersonTemplate,
    'occult': OccultMysteryTemplate,
    'sect_conspiracy': SectConspiracyTemplate,
    'historical': HistoricalMysteryTemplate,
}


def get_template(template_name):
    """Get a mystery template by name."""
    if template_name in MYSTERY_TEMPLATES:
        return MYSTERY_TEMPLATES[template_name]()
    return None


def list_templates():
    """List all available mystery templates."""
    return list(MYSTERY_TEMPLATES.keys())


def create_mystery_from_template(template_name, created_by, custom_title=None, custom_description=None):
    """Create a mystery from a template with optional customization."""
    template = get_template(template_name)
    if not template:
        return None
    
    if custom_title:
        template.title = custom_title
    if custom_description:
        template.description = custom_description
    
    return template.create_mystery(created_by)
