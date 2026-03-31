"""
Data classes for Chronicles of Darkness stat types.
These are used for stat dictionaries and configuration.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Stat:
    """Base stat data class for attributes and skills."""
    name: str
    min_value: int = 0
    max_value: int = 5
    temp_value: int = 0
    description: str = ""
    att_type: Optional[str] = None  # For attributes: power, finesse, resistance
    skill_type: Optional[str] = None  # For skills: mental, physical, social
    unskilled: Optional[int] = None  # Penalty when untrained


@dataclass
class Pool:
    """Resource pool data class (health, willpower, etc)."""
    name: str
    min_value: int = 0
    max_value: int = 10
    temp_value: int = 0
    description: str = ""


@dataclass
class Advantage:
    """Derived stat data class."""
    name: str
    min_value: int = 0
    max_value: int = 10
    temp_value: int = 0
    description: str = ""
    adv_base: str = ""  # Formula for calculating the advantage


@dataclass
class Anchor:
    """Character anchor data class (virtue, vice, etc)."""
    name: str
    min_value: int = 0
    max_value: int = 10
    temp_value: int = 0
    description: str = "" 

@dataclass
class Merit:
    """Merit data class."""
    name: str
    min_value: int = 1
    max_value: int = 5
    temp_value: int = 0
    description: str = ""
    merit_type: str = ""  # Merit type (e.g., "physical", "social", "mental", "style", "fighting", "supernatural")
    cost: int = 0  # Cost in experience points
    # Prerequisite shorthand examples:
    # - "strength:2" (specific stat; can resolve from attributes/skills/advantages)
    # - "[brawl:1,weaponry:1]" (OR group)
    # - "social_skill:2" / "mental_attribute:3" (category-any)
    # - "brawl_specialty:1", "weapon_specialty:1", "specialty:1" (specialties)
    # - "mentor:2" (base merit; instance counts)
    # - "mantle:autumn:3" (specific merit instance)
    # - "resolve:@dots" (dynamic threshold tied to purchased merit dots)
    prerequisite: str = ""
    

