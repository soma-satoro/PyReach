"""
Template Registry System for Chronicles of Darkness.
Provides centralized management of character templates using Python dictionaries.
"""

import importlib
import os
from django.conf import settings
from evennia.utils import logger
from .template_models import TemplateDefinition, TemplateUsage


class TemplateRegistry:
    """
    Central registry for managing character templates.
    Handles loading, validation, and access to template definitions.
    """
    
    def __init__(self):
        self._cache = {}
        self._loaded = False
    
    def _load_templates(self):
        """Load all active templates from the database."""
        if self._loaded:
            return
        
        try:
            templates = TemplateDefinition.objects.filter(is_active=True)
            self._cache = {template.name.lower(): template for template in templates}
            self._loaded = True
        except Exception as e:
            logger.log_err(f"Error loading templates: {e}")
            self._cache = {}
            self._loaded = False
    
    def get_template(self, name):
        """
        Get a template definition by name.
        
        Args:
            name (str): Template name
            
        Returns:
            TemplateDefinition or None
        """
        self._load_templates()
        return self._cache.get(name.lower().replace(" ", "_"))
    
    def get_all_templates(self, legacy_mode=None):
        """
        Get all active templates, optionally filtered by legacy mode.
        
        Args:
            legacy_mode (bool, optional): Filter by legacy mode. None = all templates
        
        Returns:
            list: List of TemplateDefinition objects
        """
        self._load_templates()
        templates = list(self._cache.values())
        
        if legacy_mode is not None:
            # Filter templates based on legacy mode
            filtered_templates = []
            for template in templates:
                # Check if template has legacy_mode field in description or other metadata
                is_legacy = self._is_legacy_template(template)
                if legacy_mode and is_legacy:
                    filtered_templates.append(template)
                elif not legacy_mode and not is_legacy:
                    filtered_templates.append(template)
            return filtered_templates
        
        return templates
    
    def get_template_names(self, legacy_mode=None):
        """
        Get list of all active template names, optionally filtered by legacy mode.
        
        Args:
            legacy_mode (bool, optional): Filter by legacy mode. None = all templates
        
        Returns:
            list: List of template names
        """
        templates = self.get_all_templates(legacy_mode)
        return [template.name for template in templates]
    
    def _is_legacy_template(self, template):
        """
        Check if a template is a legacy template.
        
        Args:
            template: TemplateDefinition object
            
        Returns:
            bool: True if template is legacy
        """
        # Check if template name starts with 'legacy_'
        if template.name.startswith('legacy_'):
            return True
        
        # Check if template has legacy_mode flag in field_validations or other metadata
        if hasattr(template, 'field_validations') and template.field_validations:
            if template.field_validations.get('legacy_mode', False):
                return True
        
        # Check description for legacy indicators
        if 'legacy' in template.description.lower() or '1st edition' in template.description.lower():
            return True
            
        return False
    
    def is_valid_template(self, name):
        """
        Check if a template name is valid and active.
        
        Args:
            name (str): Template name to check
            
        Returns:
            bool: True if template exists and is active
        """
        return self.get_template(name) is not None
    
    def get_bio_fields(self, template_name):
        """
        Get bio fields for a template.
        
        Args:
            template_name (str): Name of template
            
        Returns:
            list: List of bio field names
        """
        template = self.get_template(template_name)
        if template:
            return template.get_bio_fields()
        return ["virtue", "vice"]  # Default fallback
    
    def get_integrity_name(self, template_name):
        """
        Get the integrity stat name for a template.
        
        Args:
            template_name (str): Name of template
            
        Returns:
            str: Integrity stat name
        """
        template = self.get_template(template_name)
        if template:
            return template.integrity_name
        return "Integrity"  # Default fallback
    
    def get_starting_integrity(self, template_name):
        """
        Get starting integrity value for a template.
        
        Args:
            template_name (str): Name of template
            
        Returns:
            int: Starting integrity value
        """
        template = self.get_template(template_name)
        if template:
            return template.starting_integrity
        return 7  # Default fallback
    
    def validate_field(self, template_name, field_name, value):
        """
        Validate a field value for a template.
        
        Args:
            template_name (str): Name of template
            field_name (str): Name of field to validate
            value (str): Value to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        template = self.get_template(template_name)
        if template:
            return template.validate_field_value(field_name, value)
        return True, None  # Default: allow any value
    
    def install_template_from_dict(self, template_data, installer=None):
        """
        Install a new template from a Python dictionary.
        
        Args:
            template_data (dict): Template configuration dictionary
            installer: Character installing the template
            
        Returns:
            tuple: (success, message, template_obj)
        """
        try:
            # Validate required fields
            required_fields = ['name', 'display_name']
            for field in required_fields:
                if field not in template_data:
                    return False, f"Missing required field: {field}", None
            
            # Check if template already exists
            existing = TemplateDefinition.objects.filter(name__iexact=template_data['name']).first()
            if existing:
                return False, f"Template '{template_data['name']}' already exists", None
            
            # Create template
            template = TemplateDefinition.objects.create(
                name=template_data['name'].lower(),
                display_name=template_data['display_name'],
                description=template_data.get('description', ''),
                bio_fields=template_data.get('bio_fields', []),
                integrity_name=template_data.get('integrity_name', 'Integrity'),
                starting_integrity=template_data.get('starting_integrity', 7),
                field_validations=template_data.get('field_validations', {}),
                version=template_data.get('version', '1.0'),
                author=template_data.get('author', ''),
                is_system=template_data.get('is_system', False),
                installed_by=installer
            )
            
            # Clear cache to force reload
            self._cache = {}
            self._loaded = False
            
            return True, f"Successfully installed template '{template.display_name}'", template
            
        except Exception as e:
            logger.log_err(f"Error installing template: {e}")
            return False, f"Error installing template: {e}", None
    
    def install_template_from_module(self, module_name, installer=None):
        """
        Install a template from a Python module.
        
        Args:
            module_name (str): Name of Python module containing template
            installer: Character installing the template
            
        Returns:
            tuple: (success, message, template_obj)
        """
        try:
            # Try to import the module
            try:
                module = importlib.import_module(module_name)
            except ImportError:
                # If direct import fails, try to reload the templates package
                try:
                    # Clear any cached imports and try to reload
                    import sys
                    if module_name in sys.modules:
                        importlib.reload(sys.modules[module_name])
                        module = sys.modules[module_name]
                    else:
                        # Try forcing a reload of the templates package
                        if 'world.cofd.templates' in sys.modules:
                            importlib.reload(sys.modules['world.cofd.templates'])
                        # Now try to import again
                        module = importlib.import_module(module_name)
                except ImportError as e:
                    return False, f"Could not import module '{module_name}': {e}", None
            
            # Look for template definitions in the module
            template_dicts = []
            for attr_name in dir(module):
                if attr_name.startswith('_'):
                    continue
                attr = getattr(module, attr_name)
                if (isinstance(attr, dict) and 
                    attr.get('name') and 
                    attr.get('display_name')):
                    template_dicts.append(attr)
            
            if not template_dicts:
                return False, f"No valid template definitions found in module '{module_name}'", None
            
            # Install the first template found (or could install all)
            template_data = template_dicts[0]
            return self.install_template_from_dict(template_data, installer)
            
        except Exception as e:
            logger.log_err(f"Error installing template from module: {e}")
            return False, f"Error installing template from module: {e}", None
    
    def load_builtin_templates(self):
        """
        Load all built-in template definitions from the templates package.
        
        Returns:
            list: List of loaded template dictionaries
        """
        try:
            # Force reload of templates module to ensure fresh import
            import sys
            import importlib
            
            # Clear the templates module cache
            templates_modules_to_clear = [
                key for key in sys.modules.keys() 
                if key.startswith('world.cofd.templates')
            ]
            for mod_key in templates_modules_to_clear:
                del sys.modules[mod_key]
            
            # Now import fresh
            from world.cofd.templates import get_all_template_definitions
            templates = get_all_template_definitions()
            
            if not templates:
                logger.log_err("No templates found in get_all_template_definitions() - check template registration")
            
            return list(templates.values())
        except ImportError as e:
            logger.log_err(f"Import error loading builtin templates: {e}")
            import traceback
            logger.log_err(traceback.format_exc())
            return []
        except Exception as e:
            logger.log_err(f"Error loading builtin templates: {e}")
            import traceback
            logger.log_err(traceback.format_exc())
            return []
    
    def install_builtin_templates(self, installer=None, mark_as_system=False):
        """
        Install all built-in templates that aren't already installed.
        
        Args:
            installer: Character installing the templates
            mark_as_system (bool): Whether to mark templates as system templates
            
        Returns:
            tuple: (installed_count, error_count, messages)
        """
        builtin_templates = self.load_builtin_templates()
        
        installed_count = 0
        error_count = 0
        messages = []
        
        for template_data in builtin_templates:
            try:
                # Check if already exists
                existing = TemplateDefinition.objects.filter(
                    name__iexact=template_data['name']
                ).first()
                
                if existing:
                    messages.append(f"Template '{template_data['name']}' already exists, skipping.")
                    continue
                
                # Optionally mark as system template
                template_data_copy = template_data.copy()
                if mark_as_system:
                    template_data_copy['is_system'] = True
                
                success, message, template_obj = self.install_template_from_dict(
                    template_data_copy, installer
                )
                
                if success:
                    messages.append(f"Installed: {template_obj.display_name}")
                    installed_count += 1
                else:
                    messages.append(f"Error installing {template_data['name']}: {message}")
                    error_count += 1
                    
            except Exception as e:
                messages.append(f"Exception installing {template_data.get('name', 'unknown')}: {e}")
                error_count += 1
        
        return installed_count, error_count, messages
    
    def uninstall_template(self, name, uninstaller=None, force=False):
        """
        Uninstall a template.
        
        Args:
            name (str): Template name to uninstall
            uninstaller: Character uninstalling the template
            force (bool): Force uninstall even if it's a system template
            
        Returns:
            tuple: (success, message)
        """
        try:
            template = TemplateDefinition.objects.filter(name__iexact=name).first()
            if not template:
                return False, f"Template '{name}' not found"
            
            if template.is_system and not force:
                return False, f"Cannot uninstall system template '{template.display_name}'. Use force=True to override."
            
            # Check if any characters are using this template (only if not forcing)
            if not force:
                usage_count = TemplateUsage.objects.filter(template=template).count()
                if usage_count > 0:
                    return False, f"Cannot uninstall template '{template.display_name}' - {usage_count} characters are using it"
            else:
                # If forcing, remove all usage records
                TemplateUsage.objects.filter(template=template).delete()
            
            # Delete the template
            template_name = template.display_name
            template.delete()
            
            # Force clear cache to ensure reload
            self.clear_cache()
            
            return True, f"Successfully uninstalled template '{template_name}'"
            
        except Exception as e:
            logger.log_err(f"Error uninstalling template: {e}")
            return False, f"Error uninstalling template: {e}"
    
    def export_template_to_dict(self, name):
        """
        Export a template to a Python dictionary.
        
        Args:
            name (str): Template name to export
            
        Returns:
            tuple: (success, message, data)
        """
        try:
            template = TemplateDefinition.objects.filter(name__iexact=name).first()
            if not template:
                return False, f"Template '{name}' not found", None
            
            # Create export data
            export_data = {
                'name': template.name,
                'display_name': template.display_name,
                'description': template.description,
                'bio_fields': template.bio_fields,
                'integrity_name': template.integrity_name,
                'starting_integrity': template.starting_integrity,
                'field_validations': template.field_validations,
                'version': template.version,
                'author': template.author,
                'exported_from': 'template_registry',
                'export_version': '1.0'
            }
            
            return True, "Template data prepared for export", export_data
            
        except Exception as e:
            logger.log_err(f"Error exporting template: {e}")
            return False, f"Error exporting template: {e}", None
    
    def create_template_module_code(self, template_dict):
        """
        Generate Python module code for a template dictionary.
        
        Args:
            template_dict (dict): Template dictionary
            
        Returns:
            str: Python module code
        """
        name = template_dict.get('name', 'template')
        display_name = template_dict.get('display_name', 'Template')
        
        code = f'''"""
{display_name} Template Definition for Chronicles of Darkness.
{template_dict.get('description', '')}
"""

from . import register_template

# {display_name} template definition
{name.upper()}_TEMPLATE = {repr(template_dict)}

# Register the template
register_template({name.upper()}_TEMPLATE)
'''
        return code
    
    def assign_template(self, character, template_name, assigner=None):
        """
        Assign a template to a character and track usage.
        
        Args:
            character: Character object
            template_name (str): Template to assign
            assigner: Character making the assignment
            
        Returns:
            tuple: (success, message)
        """
        try:
            template = self.get_template(template_name)
            if not template:
                return False, f"Template '{template_name}' not found"
            
            # Remove existing usage record if any
            TemplateUsage.objects.filter(character=character).delete()
            
            # Create new usage record
            TemplateUsage.objects.create(
                character=character,
                template=template,
                assigned_by=assigner
            )
            
            return True, f"Assigned template '{template.display_name}' to {character.name}"
            
        except Exception as e:
            logger.log_err(f"Error assigning template: {e}")
            return False, f"Error assigning template: {e}"
    
    def clear_cache(self):
        """Force reload of template cache."""
        self._cache = {}
        self._loaded = False
        
        # Also clear Django's query cache
        try:
            from django.core.cache import cache
            cache.clear()
        except:
            pass
    
    def force_reload(self):
        """Force a complete reload of all templates from database."""
        self.clear_cache()
        
        # Force reload from database
        try:
            templates = TemplateDefinition.objects.filter(is_active=True)
            self._cache = {template.name.lower(): template for template in templates}
            self._loaded = True
        except Exception as e:
            logger.log_err(f"Error force reloading templates: {e}")
            self._cache = {}
            self._loaded = False


# Global registry instance
template_registry = TemplateRegistry() 