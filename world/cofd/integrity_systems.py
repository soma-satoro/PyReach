"""
Integrity Systems for Chronicles of Darkness Templates

This module contains breaking points data for different supernatural templates.
Each template has its own integrity trait (Humanity, Clarity, Harmony, etc.)
with specific breaking points that trigger degeneration rolls.
"""

# Vampire Breaking Points (Humanity)
VAMPIRE_BREAKING_POINTS = {
    10: {
        "dice": 5,
        "breaks": [
            "One night without human contact.",
            "Lying in defense of the Masquerade.",
            "Spending more than one Vitae in a night.",
        ]
    },
    9: {
        "dice": 5,
        "breaks": [
            "Watching humans eat a meal.",
            "Committing a superhuman feat of physical prowess.",
            "Feeding from the unwilling or unknowing.",
            "Urging another's behavior with a Discipline.",
            "Spending an hour in the sun.",
        ]
    },
    8: {
        "dice": 4,
        "breaks": [
            "Creating a ghoul.",
            "Rejected by a human.",
            "Riding the wave of frenzy.",
            "Depriving another of consent with a Discipline.",
            "Spending most of a day in the sun.",
        ]
    },
    7: {
        "dice": 4,
        "breaks": [
            "One week active without human contact.",
            "Surviving something that would hospitalize a human.",
            "Injuring someone over blood.",
        ]
    },
    6: {
        "dice": 3,
        "breaks": [
            "Falling into torpor.",
            "Feeding from a child.",
            "Reading your own obituary.",
            "Experiencing a car crash or other immense physical trauma.",
        ]
    },
    5: {
        "dice": 3,
        "breaks": [
            "Two weeks active without human contact.",
            "Reaching Blood Potency 3.",
            "Death of a mortal family member.",
            "Joining a covenant to the point of gaining Status for it.",
        ]
    },
    4: {
        "dice": 2,
        "breaks": [
            "Learning a dot of Crúac",
            "Impassioned violence.",
            "Spending a year or more in torpor.",
            "Surviving a century.",
            "Accidentally killing.",
        ]
    },
    3: {
        "dice": 2,
        "breaks": [
            "One month active without human contact.",
            "Reaching Blood Potency 6.",
            "Death of a mortal spouse or child.",
            "Impassioned killing.",
        ]
    },
    2: {
        "dice": 1,
        "breaks": [
            "One year active without human contact.",
            "Premeditated killing.",
            "Seeing a culture that didn't exist when you were alive.",
            "Surviving 500 years.",
            "Creating a revenant.",
        ]
    },
    1: {
        "dice": 0,
        "breaks": [
            "One decade active without human contact.",
            "Heinous, spree, or mass murder.",
            "Killing your Touchstone.",
        ]
    },
}

# Werewolf Breaking Points (Harmony)
# Organized by direction (Flesh vs Spirit) and threshold levels
WEREWOLF_BREAKING_POINTS = {
    "toward_flesh": {
        "name": "Toward Flesh",
        "description": "Actions that push you toward your human/physical nature",
        "breaks": [
            {"action": "Defiling a locus.", "penalty": -1},
            {"action": "Refusing to participate in Siskur-Dah.", "penalty": -1},
            {"action": "Staying out of the Hisil for a week.", "penalty": -1},
            {"action": "Using a silver weapon against another werewolf.", "penalty": -1},
            {"action": "Violating the Oath of the Moon. (Forsaken only)", "penalty": -2},
            {"action": "Staying out of the Hisil for a month.", "penalty": -3},
        ]
    },
    "toward_spirit": {
        "name": "Toward Spirit",
        "description": "Actions that push you toward your spiritual nature",
        "breaks": [
            {"action": "Killing a human or wolf.", "penalty": -1},
            {"action": "Staying in the Hisil for a week.", "penalty": -1},
            {"action": "Hunting humans or wolves for food.", "penalty": -2},
            {"action": "Killing a packmate.", "penalty": -2},
            {"action": "Eating human or wolf flesh for Essence.", "penalty": -3},
            {"action": "Staying in the Hisil for a month.", "penalty": -3},
        ]
    },
    "low_harmony": {
        "name": "Harmony 3 or Lower",
        "threshold": 3,
        "description": "Additional breaking points when Harmony is 3 or lower",
        "breaks": [
            {"action": "Allowing a spirit safe passage into the physical world.", "penalty": -1},
            {"action": "Eating processed food.", "penalty": -1},
            {"action": "Mating with a human.", "penalty": -1},
            {"action": "Staying out of the Hisil for a day.", "penalty": -1},
        ]
    },
    "high_harmony": {
        "name": "Harmony 8 or More",
        "threshold": 8,
        "description": "Additional breaking points when Harmony is 8 or higher",
        "breaks": [
            {"action": "Inflicting Lunacy on a loved one.", "penalty": -1},
            {"action": "Leading the Siskur-Dah.", "penalty": -1},
            {"action": "Spending more than two days away from your pack.", "penalty": -1},
            {"action": "Staying in the Hisil for a full day.", "penalty": -1},
        ]
    },
}

# Changeling Breaking Points (Clarity)
# Organized by dice pool (severity of the breaking point)
CHANGELING_BREAKING_POINTS = {
    1: {
        "dice": 1,
        "breaks": [
            "Told your experiences are unreal by someone who seems convincing, but whom you don't know.",
            "Changing someone else via the Dream Infiltrator (p. 337) Condition.",
            "Spending all your Glamour in one day.",
            "Going one full day without human or changeling contact.",
            "Breaking a mundane promise.",
            "Meeting your fetch for the first time.",
        ]
    },
    2: {
        "dice": 2,
        "breaks": [
            "Told your experiences are unreal by a figure whose authority you believe in.",
            "Changing someone else via the Dream Intruder (p. 338) Condition.",
            "Eating nothing but goblin fruit for a full day.",
            "Having someone break a mundane promise to you.",
            "Discover that someone lied to you about something minor.",
            "Actively searching out memories of your durance.",
            "Taking psychotropic drugs.",
            "Gaining a non-Clarity Condition that confuses your senses or badly jars you, such as Lost or Spooked.",
            "Having someone else tamper with your dreams.",
            "Going a week without human or changeling contact.",
        ]
    },
    3: {
        "dice": 3,
        "breaks": [
            "Told your experiences are unreal by someone you trust.",
            "Being the victim of a non-fae supernatural power that confuses your senses, makes you question your surroundings or perceptions, or reenacts something your Keeper did to you.",
            "Going two weeks without human or changeling contact.",
            "Killing someone else's fetch.",
            "Reaching Wyrd 3.",
            "Having someone break a formal oath or pledge to you.",
            "Having a mortal shun or disparage you.",
            "Losing a Touchstone.",
        ]
    },
    4: {
        "dice": 4,
        "breaks": [
            "Presented with \"evidence\" your experiences are unreal.",
            "Accidentally killing a human.",
            "Breaking formal oaths or pledges.",
            "Changing someone else via the Dream Assailant (p. 336) Condition.",
            "Discovering that someone lied to you about something important.",
            "Death of a family member.",
            "Killing another changeling.",
            "Killing your own fetch.",
            "Going a month without human or changeling contact.",
            "Kidnapping or keeping someone captive.",
            "Reenacting or reliving a memory from your durance.",
            "Reaching Wyrd 6.",
        ]
    },
    5: {
        "dice": 5,
        "breaks": [
            "Subjected to \"deprogramming\" or other extended, tormenting efforts to persuade you your experiences are unreal.",
            "Premeditated killing of a human.",
            "Going a year or more without human or changeling contact.",
            "Torturing someone.",
            "Using Glamour to force someone to change their behavior.",
            "Brainwashing someone via repeated dream manipulation.",
            "Spending time in Arcadia.",
            "Prolonged or intimate contact with a True Fae.",
            "Killing your Touchstone.",
            "Reaping Glamour.",
            "Reaching Wyrd 10.",
        ]
    },
}

# Mage Breaking Points (Wisdom)
# TODO: Add Mage Wisdom breaking points

# Geist Breaking Points (Synergy)
# TODO: Add Geist Synergy breaking points

# Demon Breaking Points (Cover)
# TODO: Add Demon Cover breaking points

# Promethean Breaking Points (Humanity)
# TODO: Add Promethean Humanity breaking points

# Hunter Breaking Points (Integrity)
# TODO: Add Hunter Integrity breaking points

# Mummy Breaking Points (Memory)
# TODO: Add Mummy Memory breaking points

# Deviant Breaking Points (Conviction)
# TODO: Add Deviant Conviction breaking points


# Vampire Banes
VAMPIRE_BANES = {
    "bells": {
        "name": "Bells",
        "description": "Cannot stand the sound of bells. Takes (10 - Humanity) bashing damage per minute exposed, provokes frenzy.",
    },
    "blood_of_the_unwilling": {
        "name": "Blood of the Unwilling",
        "description": "Takes no sustenance from unwilling/unknowing vessels. First (10 - Humanity) Vitae provide no nourishment.",
    },
    "crossroads": {
        "name": "Crossroads",
        "description": "Confused when passing through crossroads. All dice pools capped by Humanity for the scene.",
    },
    "face_of_hunger": {
        "name": "Face of Hunger",
        "description": "When below 5 Vitae, appears as a corpse. Humanity caps Social actions and frenzy resistance.",
    },
    "grave_soil": {
        "name": "Grave Soil",
        "description": "Must sleep with soil from place of death. Without it, all pools capped by Humanity for the night.",
    },
    "hated_by_beasts": {
        "name": "Hated by Beasts",
        "description": "Animals despise you. Animal Ken and Animalism suffer (10 - Humanity) penalty.",
    },
    "holy_day": {
        "name": "Holy Day",
        "description": "One day per week is holy. Cannot resist daysleep. Cannot awaken unless body suffers (10 - Humanity) damage.",
    },
    "invitation": {
        "name": "Invitation",
        "description": "Cannot enter private dwelling uninvited. Takes (10 - Humanity) bashing damage if entering. Cannot heal while inside.",
    },
    "open_wounds": {
        "name": "Open Wounds",
        "description": "Wounds stay open until daysleep. Can heal Health with Vitae, but wounds don't close until after sleeping.",
    },
    "plague_of_purity": {
        "name": "Plague of Purity",
        "description": "Pure of heart are repulsive. Touch by human with Integrity 8+ causes (10 - Humanity) bashing damage.",
    },
    "rat_king": {
        "name": "Rat King/Queen",
        "description": "Attracts vermin constantly. Fail all Social rolls except Intimidation. Spend Willpower to send away for Humanity minutes.",
    },
    "repulsion": {
        "name": "Repulsion",
        "description": "A substance is abhorrent (garlic, salt, roses, silver). Cannot approach within (10 - Humanity) feet without Willpower. If in wound, takes (10 - Humanity) bashing damage.",
    },
}

# Vampire-specific Conditions for Humanity loss
VAMPIRE_HUMANITY_CONDITIONS = {
    # Dramatic Failure
    "jaded": "Jaded",
    
    # Failure and Success
    "bestial": "Bestial",
    "competitive": "Competitive", 
    "wanton": "Wanton",
    
    # Exceptional Success
    "inspired": "Inspired",
}

# Master breaking points dictionary by template
BREAKING_POINTS_BY_TEMPLATE = {
    "vampire": {
        "name": "Humanity",
        "data": VAMPIRE_BREAKING_POINTS,
        "description": "Humanity measures a vampire's connection to mortal life and restraint of the Beast.",
        "type": "descending",  # Higher integrity = more dice
        "uses_banes": True,  # Vampires can take Banes
        "conditions": VAMPIRE_HUMANITY_CONDITIONS,
        "banes": VAMPIRE_BANES,
    },
    "changeling": {
        "name": "Clarity",
        "data": CHANGELING_BREAKING_POINTS,
        "description": "Clarity measures a changeling's grip on reality and resistance to madness.",
        "type": "severity",  # Organized by severity of breaking point
    },
    "werewolf": {
        "name": "Harmony",
        "data": WEREWOLF_BREAKING_POINTS,
        "description": "Harmony measures a werewolf's balance between flesh and spirit.",
        "type": "dual",  # Organized by direction (flesh vs spirit) with thresholds
    },
    # Add more templates here as they are implemented
}


def get_breaking_points(template):
    """
    Get breaking points data for a specific template.
    
    Args:
        template (str): The template name (e.g., "vampire", "werewolf")
        
    Returns:
        dict: Breaking points data with 'name', 'data', and 'description' keys,
              or None if template has no breaking points defined
    """
    return BREAKING_POINTS_BY_TEMPLATE.get(template.lower())


def get_integrity_name(template):
    """
    Get the integrity trait name for a template.
    
    Args:
        template (str): The template name
        
    Returns:
        str: The integrity trait name (e.g., "Humanity", "Clarity", "Harmony")
             or "Integrity" as default
    """
    bp_data = get_breaking_points(template)
    if bp_data:
        return bp_data["name"]
    return "Integrity"


def get_breaking_points_for_level(template, level):
    """
    Get breaking points for a specific integrity level.
    
    Args:
        template (str): The template name
        level (int): The integrity level (1-10)
        
    Returns:
        dict: Breaking points data for that level with 'dice' and 'breaks' keys,
              or None if not found
    """
    bp_data = get_breaking_points(template)
    if bp_data and "data" in bp_data:
        return bp_data["data"].get(level)
    return None
