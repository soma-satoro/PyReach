"""
Template Administration Commands for Chronicles of Darkness.
Provides admin commands for managing character templates using Python dictionaries.
"""

import os
import importlib
from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.utils import class_from_module
from world.cofd.template_registry import template_registry
from world.cofd.template_models import TemplateDefinition


class CmdTemplate(MuxCommand):
    """
    Manage character templates.
    
    Usage:
        +template[/switch] [arguments]
    
    Switches:
        /list                          - List all installed templates
        /builtin                       - List available built-in template definitions  
        /info <template>               - Show detailed info about a template
        /install builtin               - Install all built-in templates
        /install module <module>       - Install template from Python module
        /uninstall <template>          - Uninstall a template
        /force_uninstall <template>    - Force uninstall a template (even system templates)
        /clear                         - Remove ALL templates (force uninstall everything)
        /reset                         - Clear all templates and reinstall built-ins fresh
        /export <template>             - Export template as Python code
        /reload                        - Reload template cache
        /force_reload                  - Force complete reload from database
        /create <template>             - Create a new template interactively
        /usage                         - Show template usage statistics
        /diagnose                      - Run diagnostic checks on template system
    
    Examples:
        +template/list
        +template/info vampire
        +template/install builtin
        +template/install module hunter           # Install hunter.py from templates folder
        +template/install module world.cofd.templates.custom_template  # Full module path
        +template/uninstall custom_template
        +template/force_uninstall vampire
        +template/clear
        +template/reset
        +template/export vampire
        +template/reload
        +template/force_reload
        +template/create my_template
        +template/usage
        +template/builtin
        +template/diagnose
        
    Note: For module installation, you can use just the filename (e.g., 'hunter' for hunter.py)
    or the full Python module path. The command will try common variations automatically.
    """
    
    key = "+template"
    aliases = ["template", "+templates", "templates"]
    help_category = "Admin Commands"
    locks = "cmd:perm(Builder)"
    
    def func(self):
        """Main command dispatcher using switches."""
        
        # If no switches, show help
        if not self.switches:
            self.caller.msg(self.__doc__)
            return
        
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_templates()
        elif switch == "builtin":
            self.list_builtin_templates()
        elif switch == "info":
            if not self.args:
                self.caller.msg("Usage: +template/info <template>")
                return
            self.show_template_info(self.args.strip())
        elif switch == "install":
            if not self.args:
                self.caller.msg("Usage: +template/install <builtin|module> [module_name]")
                return
            self.install_template(self.args.strip().split())
        elif switch == "uninstall":
            if not self.args:
                self.caller.msg("Usage: +template/uninstall <template>")
                return
            self.uninstall_template(self.args.strip(), force=False)
        elif switch == "force_uninstall":
            if not self.args:
                self.caller.msg("Usage: +template/force_uninstall <template>")
                return
            self.uninstall_template(self.args.strip(), force=True)
        elif switch == "clear":
            self.clear_all_templates()
        elif switch == "reset":
            self.reset_template_system()
        elif switch == "export":
            if not self.args:
                self.caller.msg("Usage: +template/export <template>")
                return
            self.export_template(self.args.strip())
        elif switch == "reload":
            self.reload_templates()
        elif switch == "force_reload":
            self.force_reload_templates()
        elif switch == "create":
            if not self.args:
                self.caller.msg("Usage: +template/create <template>")
                return
            self.create_template_interactive(self.args.strip())
        elif switch == "usage":
            self.show_template_usage()
        elif switch == "diagnose":
            self.diagnose_template_system()
        else:
            self.caller.msg(f"Unknown switch '{switch}'. Use +template for help.")
    
    def list_templates(self):
        """List all installed templates."""
        templates = template_registry.get_all_templates()
        
        if not templates:
            self.caller.msg("No templates are currently installed.")
            return
        
        self.caller.msg("|wInstalled Templates:|n")
        self.caller.msg("-" * 50)
        
        for template in sorted(templates, key=lambda t: t.name):
            status = "|gActive|n" if template.is_active else "|rInactive|n"
            system = " |y(System)|n" if template.is_system else ""
            self.caller.msg(f"  {template.display_name:<15} [{template.name:<12}] {status}{system}")
            if template.description:
                self.caller.msg(f"    {template.description[:60]}...")
        
        self.caller.msg(f"\nTotal: {len(templates)} templates")
    
    def list_builtin_templates(self):
        """List available built-in template definitions."""
        builtin_templates = template_registry.load_builtin_templates()
        
        if not builtin_templates:
            self.caller.msg("No built-in templates found.")
            return
        
        self.caller.msg("|wBuilt-in Template Definitions:|n")
        self.caller.msg("-" * 50)
        
        for template_data in builtin_templates:
            name = template_data.get('name', 'unknown')
            display_name = template_data.get('display_name', 'Unknown')
            description = template_data.get('description', '')
            
            # Check if already installed
            existing = template_registry.get_template(name)
            status = " |g(Installed)|n" if existing else " |y(Available)|n"
            
            self.caller.msg(f"  {display_name:<15} [{name:<12}]{status}")
            if description:
                self.caller.msg(f"    {description[:60]}...")
        
        self.caller.msg(f"\nTotal: {len(builtin_templates)} built-in templates")
        self.caller.msg("Use '+template/install builtin' to install all available templates.")
    
    def show_template_info(self, template_name):
        """Show detailed information about a template."""
        template = template_registry.get_template(template_name)
        
        if not template:
            self.caller.msg(f"Template '{template_name}' not found.")
            return
        
        self.caller.msg(f"|wTemplate Information: {template.display_name}|n")
        self.caller.msg("=" * 50)
        self.caller.msg(f"Name: {template.name}")
        self.caller.msg(f"Display Name: {template.display_name}")
        self.caller.msg(f"Version: {template.version}")
        self.caller.msg(f"Author: {template.author or 'Unknown'}")
        self.caller.msg(f"Active: {'Yes' if template.is_active else 'No'}")
        self.caller.msg(f"System Template: {'Yes' if template.is_system else 'No'}")
        self.caller.msg(f"Created: {template.created_at.strftime('%Y-%m-%d %H:%M')}")
        self.caller.msg(f"Updated: {template.updated_at.strftime('%Y-%m-%d %H:%M')}")
        
        if template.description:
            self.caller.msg(f"\nDescription:\n{template.description}")
        
        bio_fields = template.get_bio_fields()
        if bio_fields:
            self.caller.msg(f"\nBio Fields: {', '.join(bio_fields)}")
        
        self.caller.msg(f"\nIntegrity Stat: {template.integrity_name}")
        self.caller.msg(f"Starting Integrity: {template.starting_integrity}")
        
        # Show field validations if any
        if template.field_validations:
            self.caller.msg("\nField Validations:")
            for field, validation in template.field_validations.items():
                valid_values = validation.get('valid_values', [])
                if valid_values:
                    self.caller.msg(f"  {field}: {', '.join(valid_values)}")
        
        # Show usage statistics
        from world.cofd.template_models import TemplateUsage
        usage_count = TemplateUsage.objects.filter(template=template).count()
        self.caller.msg(f"\nCharacters using this template: {usage_count}")
    
    def install_template(self, args):
        """Install a template from various sources."""
        if not args:
            self.caller.msg("Usage: +template/install <builtin|module> [module_name]")
            return
        
        install_type = args[0].lower()
        
        if install_type == "builtin":
            self.install_builtin_templates()
        elif install_type == "module":
            if len(args) < 2:
                self.caller.msg("Usage: +template/install module <module_name>")
                return
            self.install_template_from_module(args[1])
        else:
            self.caller.msg("Install type must be 'builtin' or 'module'")
    
    def install_builtin_templates(self):
        """Install all built-in templates."""
        self.caller.msg("Installing built-in templates...")
        
        # Don't mark as system templates by default
        installed_count, error_count, messages = template_registry.install_builtin_templates(
            self.caller, mark_as_system=False
        )
        
        # Display results
        for message in messages:
            if "Error" in message or "Exception" in message:
                self.caller.msg(f"|r{message}|n")
            else:
                self.caller.msg(f"|g{message}|n")
        
        self.caller.msg(f"\n|wInstallation Summary:|n")
        self.caller.msg(f"Templates installed: {installed_count}")
        self.caller.msg(f"Errors encountered: {error_count}")
        
        if installed_count > 0:
            self.caller.msg(f"|gBuilt-in templates are now available for use.|n")
            self.caller.msg(f"|yNote: Templates can be uninstalled with +template/uninstall if needed.|n")
    
    def install_template_from_module(self, module_name):
        """Install a template from a Python module."""
        # Try different module path variations
        module_variations = []
        
        # Add the provided module name as-is first
        module_variations.append(module_name)
        
        # If it doesn't contain dots, try adding the templates path
        if '.' not in module_name:
            module_variations.extend([
                f"world.cofd.templates.{module_name}",
                f"world.cofd.templates.{module_name.lower()}",
                f"exordium.world.cofd.templates.{module_name}",
                f"exordium.world.cofd.templates.{module_name.lower()}"
            ])
        
        # Try each variation
        for variant in module_variations:
            success, message, template_obj = template_registry.install_template_from_module(
                variant, self.caller
            )
            
            if success:
                self.caller.msg(f"|gSuccess:|n {message}")
                self.caller.msg(f"Template '{template_obj.display_name}' has been installed and is ready for use.")
                return
            
            # Don't show error for each attempt, just continue to next variation
            
        # If we get here, none of the variations worked
        self.caller.msg(f"|rError installing template:|n Could not find module '{module_name}' in any expected location.")
        self.caller.msg(f"|yTried paths:|n")
        for variant in module_variations:
            self.caller.msg(f"  - {variant}")
        self.caller.msg(f"|yTip:|n Make sure the template file exists in world/cofd/templates/ and is imported in __init__.py")
    
    def uninstall_template(self, template_name, force=False):
        """Uninstall a template."""
        success, message = template_registry.uninstall_template(template_name, self.caller, force=force)
        if success:
            self.caller.msg(f"|gSuccess:|n {message}")
        else:
            self.caller.msg(f"|rError:|n {message}")
            if "system template" in message.lower() and not force:
                self.caller.msg(f"|yTip:|n Use +template/force_uninstall {template_name} to force uninstall system templates.")
    
    def clear_all_templates(self):
        """Remove all templates from the system."""
        self.caller.msg("|yWarning:|n This will remove ALL templates from the system!")
        
        templates = template_registry.get_all_templates()
        if not templates:
            self.caller.msg("No templates to remove.")
            return
        
        removed_count = 0
        error_count = 0
        
        for template in templates:
            # Force uninstall all templates
            success, message = template_registry.uninstall_template(template.name, self.caller, force=True)
            if success:
                self.caller.msg(f"|gRemoved:|n {template.display_name}")
                removed_count += 1
            else:
                self.caller.msg(f"|rError removing {template.display_name}:|n {message}")
                error_count += 1
        
        self.caller.msg(f"\n|wClear Summary:|n")
        self.caller.msg(f"Templates removed: {removed_count}")
        self.caller.msg(f"Errors encountered: {error_count}")
        
        if removed_count > 0:
            self.caller.msg(f"|gAll templates have been cleared from the system.|n")
    
    def reset_template_system(self):
        """Clear all templates and reinstall built-ins fresh."""
        self.caller.msg("|yResetting template system:|n Clearing all templates and reinstalling built-ins...")
        
        # Force clear cache first
        template_registry.clear_cache()
        
        # Clear all existing templates from database directly
        from world.cofd.template_models import TemplateDefinition, TemplateUsage
        
        # Remove all usage records first
        TemplateUsage.objects.all().delete()
        
        # Get count before deletion
        removed_count = TemplateDefinition.objects.count()
        
        # Delete all templates
        TemplateDefinition.objects.all().delete()
        
        self.caller.msg(f"|gCleared {removed_count} existing templates from database.|n")
        
        # Force reload cache to ensure clean state
        template_registry.force_reload()
        
        # Then reinstall built-in templates (without system flag)
        self.caller.msg("Reinstalling built-in templates...")
        installed_count, error_count, messages = template_registry.install_builtin_templates(
            self.caller, mark_as_system=False
        )
        
        # Display results
        for message in messages:
            if "Error" in message or "Exception" in message:
                self.caller.msg(f"|r{message}|n")
            else:
                self.caller.msg(f"|g{message}|n")
        
        # Final force reload to ensure everything is fresh
        template_registry.force_reload()
        
        self.caller.msg(f"\n|wReset Summary:|n")
        self.caller.msg(f"Templates cleared: {removed_count}")
        self.caller.msg(f"Templates reinstalled: {installed_count}")
        self.caller.msg(f"Errors encountered: {error_count}")
        
        if installed_count > 0:
            self.caller.msg(f"|gTemplate system has been reset with fresh installations.|n")
            self.caller.msg(f"|yNote: All templates are now regular templates (not system) and can be uninstalled.|n")
    
    def export_template(self, template_name):
        """Export a template as Python module code."""
        success, message, export_data = template_registry.export_template_to_dict(template_name)
        
        if success:
            # Generate Python module code
            module_code = template_registry.create_template_module_code(export_data)
            
            self.caller.msg(f"|wTemplate Export - Python Module Code:|n")
            self.caller.msg("=" * 60)
            self.caller.msg(module_code)
            self.caller.msg("=" * 60)
            self.caller.msg(f"|gSave this code to a .py file in world/cofd/templates/ to create a reusable template.|n")
        else:
            self.caller.msg(f"|rError:|n {message}")
    
    def reload_templates(self):
        """Reload the template cache."""
        template_registry.clear_cache()
        self.caller.msg("|gTemplate cache cleared and will be reloaded on next access.|n")
    
    def force_reload_templates(self):
        """Force complete reload from database."""
        template_registry.force_reload()
        self.caller.msg("|gTemplate cache force reloaded from database.|n")
    
    def create_template_interactive(self, template_name):
        """Create a new template interactively."""
        # Basic template creation - could be expanded to use EvMenu for complex creation
        self.caller.msg(f"|wCreating new template: {template_name}|n")
        self.caller.msg("This is a basic template creator. For complex templates, create a Python module in world/cofd/templates/")
        
        # Create a basic template structure
        template_data = {
            "name": template_name.lower(),
            "display_name": template_name.title(),
            "description": f"Custom template: {template_name}",
            "bio_fields": ["virtue", "vice"],
            "integrity_name": "Integrity",
            "starting_integrity": 7,
            "field_validations": {},
            "version": "1.0",
            "author": str(self.caller)
        }
        
        success, message, template_obj = template_registry.install_template_from_dict(template_data, self.caller)
        if success:
            self.caller.msg(f"|gSuccess:|n {message}")
            self.caller.msg("Use +template/info to view the template, or +template/export to get Python module code.")
        else:
            self.caller.msg(f"|rError:|n {message}")
    
    def show_template_usage(self):
        """Show template usage statistics."""
        from world.cofd.template_models import TemplateUsage
        from collections import defaultdict
        
        # Get usage counts per template
        usage_counts = defaultdict(int)
        for usage in TemplateUsage.objects.all():
            usage_counts[usage.template.display_name] += 1
        
        self.caller.msg("|wTemplate Usage Statistics:|n")
        self.caller.msg("-" * 40)
        
        if not usage_counts:
            self.caller.msg("No templates are currently in use.")
            return
        
        total_characters = sum(usage_counts.values())
        
        for template_name, count in sorted(usage_counts.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_characters * 100) if total_characters > 0 else 0
            self.caller.msg(f"  {template_name:<15} {count:>3} characters ({percentage:>5.1f}%)")
        
        self.caller.msg(f"\nTotal characters with templates: {total_characters}")
    
    def diagnose_template_system(self):
        """Run diagnostic checks on the template system."""
        self.caller.msg("|wTemplate System Diagnostics:|n")
        self.caller.msg("=" * 60)
        
        # Check 1: Registry cache status
        self.caller.msg("\n|w1. Registry Cache Status:|n")
        self.caller.msg(f"   Loaded: {template_registry._loaded}")
        self.caller.msg(f"   Cached templates: {len(template_registry._cache)}")
        if template_registry._cache:
            self.caller.msg(f"   Cached names: {', '.join(template_registry._cache.keys())}")
        
        # Check 2: Database templates
        self.caller.msg("\n|w2. Database Templates:|n")
        try:
            db_templates = TemplateDefinition.objects.all()
            self.caller.msg(f"   Total in database: {db_templates.count()}")
            self.caller.msg(f"   Active: {TemplateDefinition.objects.filter(is_active=True).count()}")
            self.caller.msg(f"   Inactive: {TemplateDefinition.objects.filter(is_active=False).count()}")
            if db_templates.exists():
                for tpl in db_templates[:5]:  # Show first 5
                    self.caller.msg(f"   - {tpl.name} ({tpl.display_name}) [Active: {tpl.is_active}]")
                if db_templates.count() > 5:
                    self.caller.msg(f"   ... and {db_templates.count() - 5} more")
        except Exception as e:
            self.caller.msg(f"|r   ERROR: Database tables don't exist!|n")
            self.caller.msg(f"   {str(e)}")
            self.caller.msg(f"|y   You need to run: evennia makemigrations world|n")
            self.caller.msg(f"|y   Then run: evennia migrate|n")
        
        # Check 3: Load builtin templates
        self.caller.msg("\n|w3. Built-in Template Definitions:|n")
        try:
            import sys
            import importlib
            
            # Force reload of templates module
            templates_modules_to_clear = [
                key for key in sys.modules.keys() 
                if key.startswith('world.cofd.templates')
            ]
            self.caller.msg(f"   Clearing {len(templates_modules_to_clear)} cached template modules")
            for mod_key in templates_modules_to_clear:
                del sys.modules[mod_key]
            
            # Now import fresh
            from world.cofd.templates import get_all_template_definitions
            builtin_templates = get_all_template_definitions()
            
            self.caller.msg(f"   Found {len(builtin_templates)} built-in template definitions")
            if builtin_templates:
                for name, template_data in builtin_templates.items():
                    display_name = template_data.get('display_name', 'Unknown')
                    self.caller.msg(f"   - {name}: {display_name}")
            else:
                self.caller.msg(f"|r   WARNING: No built-in templates found!|n")
                self.caller.msg(f"|y   This means templates are not registering during import.|n")
        except Exception as e:
            self.caller.msg(f"|r   ERROR loading built-in templates: {e}|n")
            import traceback
            for line in traceback.format_exc().split('\n'):
                if line.strip():
                    self.caller.msg(f"     {line}")
        
        # Check 4: Template module imports
        self.caller.msg("\n|w4. Template Module Import Test:|n")
        template_modules = [
            'mortal', 'vampire', 'mage', 'changeling', 'werewolf', 'geist',
            'deviant', 'demon', 'hunter', 'promethean', 'mummy', 'mortal_plus',
            'legacy_vampire', 'legacy_mage', 'legacy_changeling', 'legacy_werewolf',
            'legacy_geist', 'legacy_promethean', 'legacy_hunter', 'legacy_changingbreeds'
        ]
        
        import_results = {'success': [], 'failed': []}
        
        for module_name in template_modules:
            try:
                module = importlib.import_module(f'world.cofd.templates.{module_name}')
                import_results['success'].append(module_name)
            except Exception as e:
                import_results['failed'].append((module_name, str(e)))
        
        self.caller.msg(f"   Successfully imported: {len(import_results['success'])}")
        self.caller.msg(f"   Failed imports: {len(import_results['failed'])}")
        
        if import_results['failed']:
            self.caller.msg("\n   |rFailed imports:|n")
            for module_name, error in import_results['failed']:
                self.caller.msg(f"   - {module_name}: {error[:80]}")
        
        # Check 5: Recommendations
        self.caller.msg("\n|w5. Recommendations:|n")
        if not builtin_templates:
            self.caller.msg("|r   CRITICAL: Built-in templates not registering!|n")
            if import_results['failed']:
                self.caller.msg("|y   - Fix the failed template imports listed above|n")
            self.caller.msg("|y   - Check evennia.log for detailed error messages|n")
            self.caller.msg("|y   - Run 'evennia reload' to reload all Python code|n")
        elif db_templates.count() == 0:
            self.caller.msg("|y   - No templates in database. Run +template/install builtin|n")
        elif template_registry._cache and db_templates.count() > 0:
            self.caller.msg("|g   - Template system appears to be working correctly|n")
        
        self.caller.msg("\n" + "=" * 60) 