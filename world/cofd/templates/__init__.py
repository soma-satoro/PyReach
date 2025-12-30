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
        # Debug logging
        from evennia.utils import logger
        logger.log_info(f"Registered template: {name} ({template_dict.get('display_name', 'Unknown')})")

def get_template_definition(name):
    """Get a specific template definition by name."""
    # Normalize name: lowercase, convert spaces and + to underscores
    normalized = name.lower().replace(" ", "_")
    if normalized == "mortal+":
        normalized = "mortal_plus"
    return _template_definitions.get(normalized)

def get_all_template_definitions():
    """Get all registered template definitions."""
    # Debug logging
    from evennia.utils import logger
    logger.log_info(f"Template definitions registry contains {len(_template_definitions)} templates: {list(_template_definitions.keys())}")
    return _template_definitions.copy()

def get_bio_fields(template_name):
    """
    Get bio fields for a template.
    
    Args:
        template_name (str): Name of the template
        
    Returns:
        list: List of bio field names
    """
    # get_template_definition handles all normalization
    template_def = get_template_definition(template_name)
    
    if template_def and "bio_fields" in template_def:
        return template_def["bio_fields"]
    return ["virtue", "vice"]

def get_integrity_name(template_name):
    """
    Get the integrity stat name for a template.
    
    Args:
        template_name (str): Name of the template
        
    Returns:
        str: Integrity stat name
    """
    # get_template_definition handles normalization
    template_def = get_template_definition(template_name)
    if template_def and "integrity_name" in template_def:
        return template_def["integrity_name"]
    return "Integrity"

def get_starting_integrity(template_name):
    """
    Get starting integrity value for a template.
    
    Args:
        template_name (str): Name of the template
        
    Returns:
        int: Starting integrity value
    """
    # get_template_definition handles normalization
    template_def = get_template_definition(template_name)
    if template_def and "starting_integrity" in template_def:
        return template_def["starting_integrity"]
    return 7

def validate_field(template_name, field_name, value):
    """
    Validate a field value for a template.
    
    Args:
        template_name (str): Name of the template
        field_name (str): Name of field to validate
        value (str): Value to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # get_template_definition handles normalization
    template_def = get_template_definition(template_name)
    if template_def and "field_validations" in template_def:
        validations = template_def["field_validations"]
        if field_name in validations:
            valid_values = validations[field_name].get("valid_values", [])
            if valid_values and value.lower() not in [v.lower() for v in valid_values]:
                return False, f"Invalid {field_name}: {value}. Valid values: {', '.join(valid_values)}"
    return True, None

def get_template_names():
    """
    Get list of all registered template names.
    
    Returns:
        list: List of template names
    """
    return list(_template_definitions.keys())

# Import all template modules to auto-register them
# Use try/except blocks to catch and log import errors without breaking the whole system

try:
    from . import mortal
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing mortal template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import vampire
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing vampire template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import mage
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing mage template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import changeling
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing changeling template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import werewolf
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing werewolf template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import geist
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing geist template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

# try:
#     from . import beast  # Beast template disabled, incomplete
# except Exception as e:
#     from evennia.utils import logger
#     logger.log_err(f"Error importing beast template: {e}")

try:
    from . import deviant
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing deviant template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import demon
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing demon template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import hunter
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing hunter template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import promethean
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing promethean template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import mummy
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing mummy template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import mortal_plus
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing mortal_plus template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

# Import legacy template modules for 1st Edition support
try:
    from . import legacy_vampire
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing legacy_vampire template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import legacy_mage
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing legacy_mage template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import legacy_changeling
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing legacy_changeling template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import legacy_werewolf
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing legacy_werewolf template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import legacy_geist
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing legacy_geist template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import legacy_promethean
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing legacy_promethean template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import legacy_hunter
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing legacy_hunter template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())

try:
    from . import legacy_changingbreeds
except Exception as e:
    from evennia.utils import logger
    logger.log_err(f"Error importing legacy_changingbreeds template: {e}")
    import traceback
    logger.log_err(traceback.format_exc())


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