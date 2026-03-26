from world.cofd.stat_types import Merit

# Geist: The Sin-Eaters Specific Merits
geist_merits = [
    # Core Sin-Eater Merits
    Merit(
        name="Architect",
        min_value=1,
        max_value=5,
        description="Extended actions to create something you care about making last distribute Merit dots as bonus dice across their rolls, and bonus dice grant the roll 8-Again. The Abiding also increase their maximum number of rolls",
        merit_type="mental",
        prerequisite="geist"
    ),
    Merit(
        name="Dread Geist",
        min_value=3,
        max_value=3,
        description="Your geist starts at Rank 4",
        merit_type="supernatural",
        prerequisite="geist"
    ),
    Merit(
        name="Grave Goods",
        min_value=1,
        max_value=5,
        description="You've hoarded the ghosts of equipment, tangible to (and consumable by) Sin-Eaters and ghosts. Each chapter, draw on up to your Merit rating in Availability's worth. The Hungry also recover Willpower from acquisition once per chapter",
        merit_type="supernatural",
        prerequisite="geist"
    ),
    Merit(
        name="Manic States",
        min_value=1,
        max_value=5,
        description="Once per chapter, ignore the negative effects of your Condition for a scene, and stock your Merit rating as bonus dice to apply to rolls, which grant the rolls 8-Again. After the scene, lose 10-Again until your next dramatic failure or exceptional success. The Bereaved also achieve exceptional success on rolls using bonus dice on a threshold of three instead of five",
        merit_type="supernatural",
        prerequisite="geist,negative_persistent_condition:1"
    ),
    Merit(
        name="Memento",
        min_value=3,
        max_value=3,
        description="You possess a given Memento - a supernatural item tied to death and the Underworld",
        merit_type="supernatural",
        prerequisite="geist"
    ),
    Merit(
        name="Reconciler",
        min_value=1,
        max_value=3,
        description="Social Maneuvering to resolve matters and set things aright opens a Door for each Merit dot. The Kindly recover Willpower and gain a beat when they accomplish such maneuvers",
        merit_type="social",
        prerequisite="geist"
    ),
    Merit(
        name="Sympathetic",
        min_value=2,
        max_value=2,
        description="As the Universal Social Merit. The Bereaved inflict the same Condition on the other party",
        merit_type="social",
        prerequisite="geist"
    ),
    # Style Merit
    Merit(
        name="Retribution",
        min_value=1,
        max_value=5,
        description="These maneuvers must be made while avenging harm done to those you feel responsible for. The Vengeful take 8-Again to Retribution maneuvers. (-) Unerring Pursuit: When tracking or pursuing guilty parties, gain +2 bonus to Speed and relevant rolls. (--) And Taking Names: Deal +2 damage with non-combat actions such as traps and car crashes. When making all-out attack, convert attack bonus into half its dice in bonus weapon rating, even unarmed. (---) Fight Through: +2 General Armor. (----) Eye for an Eye: Your first strike on a guilty party inflicts one Condition or Tilt they had inflicted on those you cared for. (-----) Guns Blazing: Make all-out attacks without sacrificing Defense, and may double all-out bonus by sacrificing Defense",
        merit_type="style",
        prerequisite="geist"
    ),
    # Location-based Merits
    Merit(
        name="Bound Possessions",
        min_value=1,
        max_value=5,
        description="Your character has possessions bound to his geist. These items are tied to his supernatural nature and can be called back to him. Each dot in this Merit represents one significant item or a collection of minor items that the character can summon or dismiss at will",
        merit_type="supernatural",
        prerequisite="geist"
    ),
]

# Create dictionary for easy lookup
geist_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in geist_merits}

