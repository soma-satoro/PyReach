"""
Hunter: The Vigil 
Complete listing of all tactics from Hunter the Vigil 2nd Edition
including requirements, dice pools, and book references.
"""

# ============================================================================
# MENTAL TACTICS
# ============================================================================

MENTAL_TACTICS = {
    "field medicine": {
        "name": "Field Medicine",
        "category": "mental",
        "requirements": {
            "primary": "Medicine 2",
            "special": "The target's rightmost Health box must be filled with lethal damage"
        },
        "primary_pool": "Dexterity + Medicine",
        "secondary_pools": [
            {"pool": "Dexterity + Medicine", "min_actors": 0, "max_actors": 2},
            {"pool": "Strength + Brawl or Weaponry, or Dexterity + Firearms", "min_actors": 1, "max_actors": 2},
            {"pool": "Dexterity + Stealth", "min_actors": 0, "max_actors": 2}
        ],
        "description": "Patch up an ally so they don't die right away.",
        "book": "TTF 8",
        "tags": ["healing", "support", "medical"]
    },
    "identification": {
        "name": "Identification",
        "category": "mental",
        "requirements": {
            "primary": "Occult 2"
        },
        "primary_pool": "Intelligence + Occult vs. Manipulation + Subterfuge + Potency",
        "secondary_pools": [
            {"pool": "Wits + Investigation", "min_actors": 0, "max_actors": 3},
            {"pool": "Wits + Stealth", "min_actors": 0, "max_actors": 1},
            {"pool": "Wits + Occult", "min_actors": 0, "max_actors": 3}
        ],
        "special": "At least one secondary actor must roll Investigation or Stealth.",
        "description": "Identify if a target is supernatural, becoming Informed.",
        "book": "HTV 2e 155",
        "tags": ["information", "detection", "occult"]
    },
    "monster lore": {
        "name": "Monster Lore",
        "category": "mental",
        "requirements": {
            "primary": "A specific type of monster",
            "secondary": "Relevant Social Merit 2"
        },
        "primary_pool": "Intelligence + Occult",
        "secondary_pools": [
            {"pool": "Presence or Manipulation + Socialize", "min_actors": 0, "max_actors": 3},
            {"pool": "Resolve + Academics or Investigation or Computer", "min_actors": 1, "max_actors": 3},
            {"pool": "Strength or Presence + Intimidation or Streetwise", "min_actors": 0, "max_actors": 2}
        ],
        "description": "Learn a single weakness, common power, and piece of information on the origin of a monster type. Primary actor becomes Informed.",
        "book": "HTV 2e 156",
        "tags": ["information", "research", "knowledge"]
    },
    "profiling": {
        "name": "Profiling",
        "category": "mental",
        "requirements": {
            "primary": "Investigation 2, Empathy 2",
            "secondary": "Skill rolled 2"
        },
        "primary_pool": "Intelligence + Investigation vs. Wits + Subterfuge or Investigation + Potency",
        "secondary_pools": [
            {"pool": "Presence or Manipulation + Persuasion", "min_actors": 0, "max_actors": 2},
            {"pool": "Intelligence + Computer", "min_actors": 0, "max_actors": 2},
            {"pool": "Wits + Stealth or Expression", "min_actors": 0, "max_actors": 1},
            {"pool": "Intelligence + Academics or Occult", "min_actors": 1, "max_actors": 3}
        ],
        "description": "Building on already gathered knowledge, learn a monster's Potency, one mental or social trait rating, human guise and any Anchors and Aspirations.",
        "book": "HTV 2e 156",
        "tags": ["information", "investigation", "profiling"]
    },
    "sweep": {
        "name": "Sweep",
        "category": "mental",
        "requirements": {},
        "primary_pool": "Wits + Composure vs. Wits + Stealth + Potency",
        "secondary_pools": [
            {"pool": "Strength + Athletics or Dexterity + Larceny", "min_actors": 1, "max_actors": 5},
            {"pool": "Wits + Investigation or Survival", "min_actors": 0, "max_actors": 5}
        ],
        "description": "Search a location, finding any traps or ambushers, gaining a bonus to investigating the area if there are none.",
        "book": "HTV 2e 157",
        "tags": ["investigation", "security", "detection"]
    },
}

# ============================================================================
# PHYSICAL TACTICS
# ============================================================================

PHYSICAL_TACTICS = {
    "called shot": {
        "name": "Called Shot",
        "category": "physical",
        "requirements": {},
        "primary_pool": "Strength + Weaponry or Dexterity + Firearms - target's Defense",
        "secondary_pools": [
            {"pool": "Manipulation + Persuasion or Subterfuge", "min_actors": 1, "max_actors": 2},
            {"pool": "Strength + Brawl", "min_actors": 1, "max_actors": 2}
        ],
        "description": "While taking a called shot penalty, the primary actor attacks with +1 weapon modifier and inflicts a tilt and initiative penalty.",
        "book": "HTV 2e 157",
        "tags": ["combat", "attack", "precision"]
    },
    "capture": {
        "name": "Capture",
        "category": "physical",
        "requirements": {},
        "primary_pool": "Dexterity + Survival or Crafts vs. Dexterity or Strength + Athletics or Brawl + Potency",
        "secondary_pools": [
            {"pool": "Wits + Athletics", "min_actors": 1, "max_actors": 3},
            {"pool": "Strength + Brawl", "min_actors": 1, "max_actors": 3}
        ],
        "description": "Immobilize a target, penalizing any attempts to break free.",
        "book": "HTV 2e 157",
        "tags": ["combat", "restraint", "control"]
    },
    "controlled immolation": {
        "name": "Controlled Immolation",
        "category": "physical",
        "requirements": {},
        "primary_pool": "Stamina + Athletics or Firearms vs. Stamina + Athletics + Potency",
        "secondary_pools": [
            {"pool": "Wits + Brawl or Weaponry", "min_actors": 1, "max_actors": 4},
            {"pool": "Wits + Survival or Science", "min_actors": 1, "max_actors": 5}
        ],
        "description": "For every turn the Cell continues to roll and succeed, the target is burning and Blinded, and the fire does not spread elsewhere.",
        "book": "HTV 2e 158",
        "tags": ["combat", "fire", "control"]
    },
    "corral": {
        "name": "Corral",
        "category": "physical",
        "requirements": {},
        "primary_pool": "Strength or Manipulation + Intimidation vs. Composure + Empathy + Potency",
        "secondary_pools": [
            {"pool": "Wits + Composure", "min_actors": 1, "max_actors": 5},
            {"pool": "Manipulation + Subterfuge or Survival", "min_actors": 1, "max_actors": 3}
        ],
        "description": "Herd a target to a specific location.",
        "book": "HTV 2e 158",
        "tags": ["combat", "positioning", "control"]
    },
    "harvest": {
        "name": "Harvest",
        "category": "physical",
        "requirements": {
            "any": "Occult 2, Specialty related to the target's type"
        },
        "primary_pool": "Dexterity + Medicine vs. Strength + Athletics or Brawl + Potency",
        "secondary_pools": [
            {"pool": "Strength + Brawl", "min_actors": 1, "max_actors": 3},
            {"pool": "Intelligence + Occult", "min_actors": 1, "max_actors": 2}
        ],
        "special": "If the target's type has been studied before, the Occult roll is not necessary.",
        "description": "Extract a sample from the target for every turn of success.",
        "book": "HTV 2e 159",
        "tags": ["extraction", "medical", "occult"]
    },
    "infiltration": {
        "name": "Infiltration",
        "category": "physical",
        "requirements": {
            "primary": "Stealth 3+",
            "secondary": "2+ in Skills used for this Tactic"
        },
        "primary_pool": "Wits + Composure vs. Wits + Composure + Potency",
        "secondary_pools": [
            {"pool": "Dexterity + Stealth", "min_actors": 1, "max_actors": 5},
            {"pool": "Presence + Expression or Intimidation", "min_actors": 1, "max_actors": 1}
        ],
        "description": "The primary actor enters the monster's inner sanctum. She may make up to 3 Investigation, Larceny, or Occult rolls before needing to exit.",
        "book": "TTF 8",
        "tags": ["stealth", "infiltration", "reconnaissance"]
    },
    "lure": {
        "name": "Lure",
        "category": "physical",
        "requirements": {
            "any": "Occult 2",
            "special": "Enticing agent"
        },
        "primary_pool": "Wits + Composure vs. Wits + Composure + Potency",
        "secondary_pools": [
            {"pool": "Presence + Persuasion or Subterfuge", "min_actors": 1, "max_actors": 1},
            {"pool": "Manipulation + Occult or Streetwise", "min_actors": 1, "max_actors": 2},
            {"pool": "Dexterity + Larceny", "min_actors": 0, "max_actors": 2}
        ],
        "description": "Lure a target in, Surprising it.",
        "book": "HTV 2e 159",
        "tags": ["ambush", "surprise", "trap"]
    },
    "scatter": {
        "name": "Scatter",
        "category": "physical",
        "requirements": {},
        "primary_pool": "Wits + Composure vs. Wits + Composure + Potency",
        "secondary_pools": [
            {"pool": "Dexterity + Stealth", "min_actors": 1, "max_actors": 5},
            {"pool": "Presence + Expression or Intimidation", "min_actors": 1, "max_actors": 1}
        ],
        "description": "While someone distracts the target, all others escape the scene and the Primary actor becomes Informed on the target.",
        "book": "HTV 2e 159",
        "tags": ["escape", "distraction", "information"]
    },
}

# ============================================================================
# SOCIAL TACTICS
# ============================================================================

SOCIAL_TACTICS = {
    "adrenaline rush": {
        "name": "Adrenaline Rush",
        "category": "social",
        "requirements": {},
        "primary_pool": "Presence + Expression",
        "secondary_pools": [
            {"pool": "Resolve + Occult", "min_actors": 0, "max_actors": 6},
            {"pool": "Resolve + Empathy", "min_actors": 0, "max_actors": 6}
        ],
        "special": "At least one secondary action must be taken.",
        "description": "A Cell becomes immune to losing consciousness from Bashing damage, do not suffer wound penalties, and gain a bonus to resisting fear.",
        "book": "HTV 2e 160",
        "tags": ["buff", "support", "morale"]
    },
    "bluff": {
        "name": "Bluff",
        "category": "social",
        "requirements": {
            "primary": "Intimidation, Persuasion, or Socialize 3+"
        },
        "primary_pool": "Presence + Intimidation, Persuasion, or Socialize vs. Composure + Empathy + Potency of lead gatekeeper",
        "secondary_pools": [
            {"pool": "Intelligence + Computer", "min_actors": 0, "max_actors": 1},
            {"pool": "Manipulation + Subterfuge vs. Composure + Empathy", "min_actors": 1, "max_actors": 5},
            {"pool": "Composure + Intimidation", "min_actors": 1, "max_actors": 3}
        ],
        "description": "The primary actor bluffs her way past any gatekeepers, convincing them that the target is expecting her, or that she's someone they'd get in trouble for turning away.",
        "book": "TTF 9",
        "tags": ["deception", "infiltration", "social"]
    },
    "expose": {
        "name": "Expose",
        "category": "social",
        "requirements": {
            "special": "Knowledge of the target's identity"
        },
        "primary_pool": "Wits + Presence or Manipulation vs. Manipulation + Subterfuge + Potency",
        "secondary_pools": [
            {"pool": "Wits + Investigation or Stealth", "min_actors": 1, "max_actors": 4},
            {"pool": "Wits + Socialize", "min_actors": 1, "max_actors": 3}
        ],
        "description": "The target is inflicted with the Leveraged or Notoriety Condition as they are blackmailed or publicly exposed.",
        "book": "HTV 2e 160",
        "tags": ["blackmail", "exposure", "social attack"]
    },
    "freeing mind": {
        "name": "Freeing Mind",
        "category": "social",
        "requirements": {
            "special": "Target must be supernaturally affected"
        },
        "primary_pool": "Manipulation + Intimidation or Subterfuge vs. subject's Composure + Resolve + monster's Potency",
        "secondary_pools": [
            {"pool": "Presence + Persuasion or Empathy", "min_actors": 1, "max_actors": 2},
            {"pool": "Wits + Brawl or Weaponry or Intimidation", "min_actors": 0, "max_actors": 3, "note": "ND"}
        ],
        "special": "Secondary actors using the Wits based pool prevent any interruptions or complications instead of adding dice to the primary actor's pool.",
        "description": "Break or suppress a monster's power on the target, helping the subject permanently end any suppressed effect.",
        "book": "HTV 2e 160",
        "tags": ["deprogramming", "support", "anti-supernatural"]
    },
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_all_tactics():
    """Get all tactics (mental, physical, and social)."""
    return {
        **MENTAL_TACTICS,
        **PHYSICAL_TACTICS,
        **SOCIAL_TACTICS
    }

def get_tactic(tactic_name):
    """
    Look up a tactic by name (case-insensitive).
    Returns the tactic data or None if not found.
    """
    tactic_key = tactic_name.lower().strip()
    all_tactics = get_all_tactics()
    return all_tactics.get(tactic_key)

def get_tactics_by_category(category):
    """
    Get all tactics of a specific category.
    Valid categories: 'mental', 'physical', 'social'
    """
    category_map = {
        "mental": MENTAL_TACTICS,
        "physical": PHYSICAL_TACTICS,
        "social": SOCIAL_TACTICS
    }
    return category_map.get(category.lower(), {})

def get_tactics_by_tag(tag):
    """
    Get all tactics with a specific tag.
    """
    all_tactics = get_all_tactics()
    matching_tactics = {}
    
    for key, tactic_data in all_tactics.items():
        if tag.lower() in [t.lower() for t in tactic_data.get("tags", [])]:
            matching_tactics[key] = tactic_data
    
    return matching_tactics

def format_requirements(tactic_data):
    """
    Format requirements for display.
    """
    reqs = tactic_data.get("requirements", {})
    if not reqs:
        return "None"
    
    formatted = []
    if "primary" in reqs:
        formatted.append(f"Primary: {reqs['primary']}")
    if "secondary" in reqs:
        formatted.append(f"Secondary: {reqs['secondary']}")
    if "any" in reqs:
        formatted.append(f"Any: {reqs['any']}")
    if "special" in reqs:
        formatted.append(f"Special: {reqs['special']}")
    
    return ", ".join(formatted) if formatted else "None"

def format_secondary_pools(pools):
    """
    Format secondary actor pools for display.
    """
    if not pools:
        return "None"
    
    formatted = []
    for pool_data in pools:
        actors = f"({pool_data['min_actors']}/{pool_data['max_actors']})"
        note = f" [{pool_data['note']}]" if 'note' in pool_data else ""
        formatted.append(f"  * {pool_data['pool']} {actors}{note}")
    
    return "\n".join(formatted)

def get_tactic_summary(tactic_name):
    """
    Get a formatted summary of a tactic.
    """
    tactic_data = get_tactic(tactic_name)
    if not tactic_data:
        return f"Tactic '{tactic_name}' not found."
    
    summary = []
    summary.append(f"=== {tactic_data['name']} ===")
    summary.append(f"Category: {tactic_data['category'].title()}")
    
    requirements = format_requirements(tactic_data)
    summary.append(f"\nRequirements: {requirements}")
    
    summary.append(f"\nPrimary Pool: {tactic_data['primary_pool']}")
    
    summary.append(f"\nSecondary Pools:")
    summary.append(format_secondary_pools(tactic_data.get('secondary_pools', [])))
    
    if 'special' in tactic_data:
        summary.append(f"\nSpecial: {tactic_data['special']}")
    
    summary.append(f"\nDescription: {tactic_data['description']}")
    summary.append(f"\nSource: {tactic_data['book']}")
    
    if "tags" in tactic_data:
        summary.append(f"Tags: {', '.join(tactic_data['tags'])}")
    
    return "\n".join(summary)

# ============================================================================
# VALIDATION LISTS
# ============================================================================

# All valid tactic names for validation
ALL_TACTICS = list(get_all_tactics().keys())

# Tactics by category
ALL_MENTAL_TACTICS = list(MENTAL_TACTICS.keys())
ALL_PHYSICAL_TACTICS = list(PHYSICAL_TACTICS.keys())
ALL_SOCIAL_TACTICS = list(SOCIAL_TACTICS.keys())

# Book abbreviations
BOOK_ABBREVIATIONS = {
    "HTV 2e": "Hunter: The Vigil 2nd Edition",
    "TTF": "Tooth and Nail (The Hunt supplement)"
}


