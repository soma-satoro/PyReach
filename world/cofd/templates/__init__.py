"""
Template Registration System for Chronicles of Darkness.
This module automatically registers all template definitions when imported.
"""

# Registry for template definitions
_template_definitions = {}

def register_template(template_dict):
    """
    Register a template definition.
    
    Args:
        template_dict (dict): Template definition dictionary
    """
    name = template_dict.get('name')
    if name:
        _template_definitions[name] = template_dict

def get_template_definition(name):
    """Get a specific template definition by name."""
    return _template_definitions.get(name.lower())

def get_all_template_definitions():
    """Get all registered template definitions."""
    return _template_definitions.copy()

# Import all template modules to auto-register them
from . import mortal
from . import vampire
from . import mage
from . import changeling
from . import werewolf
from . import geist
# from . import beast  # Beast template disabled, incomplete
from . import deviant
from . import demon
from . import hunter
from . import promethean
from . import mummy
from . import mortal_plus

# Import legacy template modules for 1st Edition support
from . import legacy_vampire
from . import legacy_mage
from . import legacy_changeling
from . import legacy_werewolf
from . import legacy_geist
from . import legacy_promethean
from . import legacy_hunter
from . import legacy_changingbreeds


# Template power list utilities
def get_template_primary_powers(template_name):
    """
    Get primary powers (rated 1-5) for a template.
    
    Args:
        template_name (str): Name of the template
        
    Returns:
        list: List of primary power names, or empty list if not found
    """
    template_name = template_name.lower()
    
    # Map template names to their modules
    template_modules = {
        'vampire': vampire,
        'mage': mage,
        'werewolf': werewolf,
        'changeling': changeling,
        'geist': geist,
        'promethean': promethean,
        'demon': demon,
        'hunter': hunter,
        'deviant': deviant,
        'mummy': mummy,
        'legacy_vampire': legacy_vampire,
        'legacy_mage': legacy_mage,
        'legacy_werewolf': legacy_werewolf,
        'legacy_changeling': legacy_changeling,
        'legacy_geist': legacy_geist,
        'legacy_promethean': legacy_promethean,
        'legacy_hunter': legacy_hunter,
        'legacy_changingbreeds': legacy_changingbreeds,
    }
    
    module = template_modules.get(template_name)
    if module and hasattr(module, 'get_primary_powers'):
        return module.get_primary_powers()
    
    # Fallback: try to get from template definition
    template_def = get_template_definition(template_name)
    if template_def and 'power_systems' in template_def:
        return template_def['power_systems']
    
    return []


def get_template_secondary_powers(template_name):
    """
    Get secondary powers (individual abilities) for a template.
    
    Args:
        template_name (str): Name of the template
        
    Returns:
        list: List of secondary power names, or empty list if not found
    """
    template_name = template_name.lower()
    
    # Map template names to their modules
    template_modules = {
        'vampire': vampire,
        'mage': mage,
        'werewolf': werewolf,
        'changeling': changeling,
        'geist': geist,
        'promethean': promethean,
        'demon': demon,
        'hunter': hunter,
        'deviant': deviant,
        'mummy': mummy,
        'legacy_vampire': legacy_vampire,
        'legacy_mage': legacy_mage,
        'legacy_werewolf': legacy_werewolf,
        'legacy_changeling': legacy_changeling,
        'legacy_geist': legacy_geist,
        'legacy_promethean': legacy_promethean,
        'legacy_hunter': legacy_hunter,
        'legacy_changingbreeds': legacy_changingbreeds,
    }
    
    module = template_modules.get(template_name)
    if module and hasattr(module, 'get_secondary_powers'):
        return module.get_secondary_powers()
    
    return []


def get_template_all_powers(template_name):
    """
    Get all powers for a template (for validation).
    
    Args:
        template_name (str): Name of the template
        
    Returns:
        list: List of all power names, or empty list if not found
    """
    template_name = template_name.lower()
    
    # Map template names to their modules
    template_modules = {
        'vampire': vampire,
        'mage': mage,
        'werewolf': werewolf,
        'changeling': changeling,
        'geist': geist,
        'promethean': promethean,
        'demon': demon,
        'hunter': hunter,
        'deviant': deviant,
        'mummy': mummy,
        'legacy_vampire': legacy_vampire,
        'legacy_mage': legacy_mage,
        'legacy_werewolf': legacy_werewolf,
        'legacy_changeling': legacy_changeling,
        'legacy_geist': legacy_geist,
        'legacy_promethean': legacy_promethean,
        'legacy_hunter': legacy_hunter,
        'legacy_changingbreeds': legacy_changingbreeds,
    }
    
    module = template_modules.get(template_name)
    if module and hasattr(module, 'get_all_powers'):
        return module.get_all_powers()
    
    # Fallback: combine primary and secondary
    primary = get_template_primary_powers(template_name)
    secondary = get_template_secondary_powers(template_name)
    return primary + secondary


def is_power_from_any_template(power_name):
    """
    Check if a power belongs to any template and return which template(s).
    
    Args:
        power_name (str): Name of the power to check
        
    Returns:
        tuple: (is_power, template_list) where is_power is bool and template_list is list of template names
    """
    power_name = power_name.lower()
    matching_templates = []
    
    # List of all templates to check
    all_templates = [
        'vampire', 'legacy_vampire',
        'mage', 'legacy_mage',
        'werewolf', 'legacy_werewolf',
        'changeling', 'legacy_changeling',
        'geist', 'legacy_geist',
        'promethean', 'legacy_promethean',
        'demon', 'hunter', 'legacy_hunter',
        'deviant', 'mummy',
        'legacy_changingbreeds'
    ]
    
    for template in all_templates:
        template_powers = get_template_all_powers(template)
        if power_name in template_powers:
            matching_templates.append(template)
    
    return (len(matching_templates) > 0, matching_templates) 