"""
Promethean: The Created Template Definition for Chronicles of Darkness.
Prometheans are artificial beings seeking to become truly human through the Great Work.
"""

from . import register_template
from world.cofd.powers.promethean_powers import (
    PROMETHEAN_LINEAGES, PROMETHEAN_BESTOWMENTS, PROMETHEAN_REFINEMENTS,
    PROMETHEAN_TRANSMUTATIONS, PROMETHEAN_ALEMBICS, ALL_ALEMBICS, PROMETHEAN_DISTILLATIONS
)


# Promethean template definition
PROMETHEAN_TEMPLATE = {
    "name": "promethean",
    "display_name": "Promethean",
    "description": "Prometheans are artificial beings created from dead matter, seeking to complete the Great Work and become truly human.",
    "bio_fields": ["elpis", "torment", "lineage", "refinement", "creator", "pilgrimage", "throng", "athanor"],
    "integrity_name": "Humanity",
    "starting_integrity": 3,
    "supernatural_power_stat": "azoth",
    "starting_power_stat": 1,
    "resource_pool": "pyros",
    # Individual Alembics are purchased, not dots in Transmutations
    "power_systems": ALL_ALEMBICS + PROMETHEAN_BESTOWMENTS,
    "individual_powers": True,  # Flag indicating powers are purchased individually
    "power_categories": PROMETHEAN_TRANSMUTATIONS,  # For organization/display
    "anchors": ["elpis", "torment"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "promethean"],
    "field_validations": {
        "lineage": {
            "valid_values": PROMETHEAN_LINEAGES
        },
        "refinement": {
            "valid_values": PROMETHEAN_REFINEMENTS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Promethean: The Created",
    "notes": "Promethean template with Azoth, individual Alembics (Transmutations), Bestowments, Pyros pool, and Athanor system"
}

# Register the template
register_template(PROMETHEAN_TEMPLATE)


# Power list helper functions
def get_primary_powers():
    """Get list of primary Promethean powers (Alembics - individual Transmutation powers)."""
    # Convert alembic display names to stored format (alembic:name_with_underscores)
    result = []
    for name in ALL_ALEMBICS:
        clean_name = name.lower().replace(' ', '_').replace("'", '')
        result.append(f'alembic:{clean_name}')
    return result


def get_secondary_powers():
    """Get list of secondary Promethean powers (Bestowments)."""
    # Convert bestowment display names to stored format (bestowment:name_with_underscores)
    result = []
    for name in PROMETHEAN_BESTOWMENTS:
        clean_name = name.lower().replace(' ', '_').replace("'", '')
        result.append(f'bestowment:{clean_name}')
    return result


def get_all_powers():
    """Get all Promethean powers for validation."""
    # Return both primary (alembics) and secondary (bestowments) in prefixed format
    return get_primary_powers() + get_secondary_powers()

