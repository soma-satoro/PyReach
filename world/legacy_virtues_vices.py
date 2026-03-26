"""
Legacy Virtue and Vice definitions for Chronicles/World of Darkness 1st Edition
"""

LEGACY_VIRTUES = {
    "charity": {
        "name": "Charity",
        "description": "Charity is generosity, sharing, giving instead of receiving. It is altruism in its purest form, and rarely found in people that walk the streets of modern times.",
        "willpower_condition": "The character risks him or herself to help another in spite of any losses that may be suffered.",
        "other_names": ["Compassion", "Mercy"],
        "possessed_by": ["Philanthropists", "Saints", "Soup-Kitchen Workers"]
    },
    "faith": {
        "name": "Faith", 
        "description": "Faith is belief. It offers a much-needed rock in a selfish, chaotic world, and can often give a person a feeling of stability as the sands crumble beneath that person's feet.",
        "willpower_condition": "A character is able to forge meaning out of chaos and instability.",
        "other_names": ["Belief", "Conviction", "Humility", "Loyalty"],
        "possessed_by": ["Detectives", "Philosophers", "Scientists", "Priests", "True Believers"]
    },
    "fortitude": {
        "name": "Fortitude",
        "description": "Fortitude is possessed by those who wish to temper themselves in a crucible of fire. Every gain, every long-held belief or ability or skill is absolutely useless unless it is tested to the very extremes.",
        "willpower_condition": "The character is able to withstand pressure to sway from a chosen course or diverge from long-held ideals.",
        "other_names": ["Courage", "Integrity", "Mettle", "Stoicism"],
        "possessed_by": ["Detectives", "Philosophers", "Scientists", "Priests", "True Believers"]
    },
    "hope": {
        "name": "Hope",
        "description": "No matter what happens, it may be overcome. No matter how horrid things are, there will be a dawn to crash through the tearing darkness. This is at the heart of all those who hold the Virtue of Hope.",
        "willpower_condition": "The character refuses to allow others give in to despair and horror.",
        "other_names": ["Dreamer", "Optimist", "Utopian"],
        "possessed_by": ["Anti-Globalization Activists", "Entrepreneurs", "Martyrs", "Visionaries"]
    },
    "justice": {
        "name": "Justice",
        "description": "The innocent must be protected and atrocities and cruelties must be punished. The cost is negligible; justice must be given for those who cannot acquire it themselves.",
        "willpower_condition": "The character does The Right Thing(TM) regardless of how it may set that character back.",
        "other_names": ["Condemnatory", "Righteous"],
        "possessed_by": ["Critics", "Judges", "Parents", "Role-Models"]
    },
    "prudence": {
        "name": "Prudence",
        "description": "Prudence is wisdom and restraint. It is the ability to see through foolish courses of action and choose one that might be better-suited in the long run.",
        "willpower_condition": "The character refuses to take a course of action even if by doing that action, the character would benefit significantly.",
        "other_names": ["Patience", "Vigilance"],
        "possessed_by": ["Businessmen", "Doctors", "Priests", "Scientists"]
    },
    "temperance": {
        "name": "Temperance",
        "description": "Temperance is moderation and balance in all things. It is never wise to indulge in one extreme or the other.",
        "willpower_condition": "The character resists urges to indulge in any sort of excess behavior whatsoever.",
        "other_names": ["Chastity", "Even-Temperament", "Frugality"],
        "possessed_by": ["Clergy", "Police Officers", "Social Workers"]
    }
}

LEGACY_VICES = {
    "envy": {
        "name": "Envy",
        "description": "Envy is greed. Envy means one covets. Envy means one desires that which others have.",
        "willpower_condition": "The character steals from a rival, or thwarts a rival in some way.",
        "other_names": ["Covetousness", "Jealousy", "Paranoia"],
        "possessed_by": ["Celebrities", "Executives", "Politicians"]
    },
    "gluttony": {
        "name": "Gluttony",
        "description": "Gluttony is indulgence. It may not necessarily be indulging in food, but indulging in drugs, drink...excesses of any kind.",
        "willpower_condition": "The character indulges in his or her addictions or excesses at risk of harm to his or herself or a loved one.",
        "other_names": ["Addictive Personality", "Conspicuous Consumer", "Epicurean"],
        "possessed_by": ["Celebrities", "Junkies", "Thieves"]
    },
    "greed": {
        "name": "Greed",
        "description": "Much like Envy, Greed is the epitome of desire. Those afflicted by Greed WANT. They want and they want and they will never be sated.",
        "willpower_condition": "Something is acquired at the expense of another.",
        "other_names": ["Avarice", "Parsimony"],
        "possessed_by": ["CEO's", "Stock Brokers", "Lawyers"]
    },
    "lust": {
        "name": "Lust",
        "description": "Desire. Uncontrolled desire. This is the embodiment of Lust. It need not be sexual; humans are afflicted with many desires beyond that of the flesh, though it may encompass that as well.",
        "willpower_condition": "The character satisfies his or her passion or lust in a way that victimizes another person.",
        "other_names": ["Lasciviousness", "Impetuousness", "Impatience"],
        "possessed_by": ["Movie Producers", "Politicians", "Rock Stars"]
    },
    "pride": {
        "name": "Pride",
        "description": "Pride is self-confidence gone awry and morphed into a tumor, a cancerous lesion that boils and bubbles over into something greater.",
        "willpower_condition": "The character exerts his or her own wants (not needs) over others at some potential risk to his or herself.",
        "other_names": ["Arrogance", "Ego Complex", "Vanity"],
        "possessed_by": ["Corporate Executives", "Movie Stars", "Street Thugs"]
    },
    "sloth": {
        "name": "Sloth",
        "description": "Sloth is laziness and lack of gumption. Why do something oneself if others can do so instead?.",
        "willpower_condition": "The character avoids completing a task, but it is successfully achieved nonetheless.",
        "other_names": ["Apathy", "Cowardice", "Ignorance"],
        "possessed_by": ["Couch Potatoes", "Trust-Fund Heirs", "Welfare Cheats"]
    },
    "wrath": {
        "name": "Wrath",
        "description": "Wrath is uncontrolled, undirected anger and fury.",
        "willpower_condition": "The character unleashes his anger in a situation that is completely unwarranted and inappropriate; if the fight has already begun, no willpower is gained.",
        "other_names": ["Anti-Social Tendencies", "Hot-Headedness", "Poor Anger Management", "Sadism"],
        "possessed_by": ["Bullies", "Sergeants", "Street Thugs"]
    }
}

def get_legacy_virtue_list():
    """Get a list of all legacy virtue names"""
    return list(LEGACY_VIRTUES.keys())

def get_legacy_vice_list():
    """Get a list of all legacy vice names"""
    return list(LEGACY_VICES.keys())

def get_virtue_info(virtue_name):
    """Get detailed information about a specific virtue"""
    virtue_name = virtue_name.lower()
    return LEGACY_VIRTUES.get(virtue_name)

def get_vice_info(vice_name):
    """Get detailed information about a specific vice"""
    vice_name = vice_name.lower()
    return LEGACY_VICES.get(vice_name)

def is_valid_virtue(virtue_name):
    """Check if a virtue name is valid"""
    return virtue_name.lower() in LEGACY_VIRTUES

def is_valid_vice(vice_name):
    """Check if a vice name is valid"""
    return vice_name.lower() in LEGACY_VICES
