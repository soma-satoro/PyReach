"""
Template System Setup for Chronicles of Darkness.
Handles initial installation and configuration of the template system.
"""

import os
from django.core.management.base import BaseCommand
from world.cofd.template_registry import template_registry
from world.cofd.template_models import TemplateDefinition


def setup_template_system(mark_as_system=False):
    """
    Set up the template system by installing all built-in templates.
    
    Args:
        mark_as_system (bool): Whether to mark templates as system templates
    
    Returns:
        tuple: (installed_count, error_count, messages)
    """
    print("Setting up Chronicles of Darkness template system...")
    
    # Install all built-in templates
    installed_count, error_count, messages = template_registry.install_builtin_templates(
        installer=None, mark_as_system=mark_as_system
    )
    
    # Display results
    for message in messages:
        if "Error" in message or "Exception" in message:
            print(f"ERROR: {message}")
        else:
            print(f"SUCCESS: {message}")
    
    print(f"\nTemplate System Setup Complete:")
    print(f"  Templates installed: {installed_count}")
    print(f"  Errors encountered: {error_count}")
    
    if installed_count > 0:
        print("Built-in templates are now available for use.")
    
    return installed_count, error_count, messages


class Command(BaseCommand):
    """
    Django management command to set up the template system.
    
    Usage: python manage.py setup_templates
    """
    help = 'Set up the Chronicles of Darkness template system'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--system',
            action='store_true',
            help='Mark templates as system templates (prevents uninstalling)',
        )
    
    def handle(self, *args, **options):
        mark_as_system = options.get('system', False)
        
        self.stdout.write(
            self.style.SUCCESS('Setting up Chronicles of Darkness template system...')
        )
        
        installed_count, error_count, messages = setup_template_system(mark_as_system)
        
        if error_count == 0:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully installed {installed_count} templates')
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f'Installed {installed_count} templates with {error_count} errors'
                )
            )


def create_example_template():
    """
    Create an example custom template to demonstrate the system.
    """
    example_template = {
        'name': 'example_custom',
        'display_name': 'Example Custom',
        'description': 'An example custom template demonstrating the template system.',
        'bio_fields': ['virtue', 'vice', 'custom_field'],
        'integrity_name': 'Integrity',
        'starting_integrity': 7,
        'field_validations': {
            'custom_field': {
                'valid_values': ['option1', 'option2', 'option3']
            }
        },
        'version': '1.0',
        'author': 'Template System Example'
    }
    
    success, message, template_obj = template_registry.install_template_from_dict(
        example_template, installer=None
    )
    
    if success:
        print(f"Created example template: {template_obj.display_name}")
    else:
        print(f"Error creating example template: {message}")
    
    return success, message


def generate_template_documentation():
    """
    Generate documentation for all installed templates.
    """
    templates = template_registry.get_all_templates()
    
    doc = "# Template System Documentation\n\n"
    doc += f"Total Templates: {len(templates)}\n\n"
    
    for template in sorted(templates, key=lambda t: t.name):
        doc += f"## {template.display_name}\n\n"
        doc += f"- **Name**: {template.name}\n"
        doc += f"- **Version**: {template.version}\n"
        doc += f"- **Author**: {template.author or 'Unknown'}\n"
        doc += f"- **Integrity Stat**: {template.integrity_name}\n"
        doc += f"- **Starting Integrity**: {template.starting_integrity}\n"
        doc += f"- **System Template**: {'Yes' if template.is_system else 'No'}\n"
        
        if template.description:
            doc += f"- **Description**: {template.description}\n"
        
        bio_fields = template.get_bio_fields()
        if bio_fields:
            doc += f"- **Bio Fields**: {', '.join(bio_fields)}\n"
        
        if template.field_validations:
            doc += "- **Field Validations**:\n"
            for field, validation in template.field_validations.items():
                valid_values = validation.get('valid_values', [])
                if valid_values:
                    doc += f"  * {field}: {', '.join(valid_values)}\n"
        
        doc += "\n"
    
    return doc


def create_custom_template_example():
    """
    Create an example custom template module to show users how to create their own.
    """
    example_template_code = '''"""
Example Custom Template Definition for Chronicles of Darkness.
This is an example of how to create a custom template. Edit this file to create your own template.
"""

from . import register_template

# Valid options for custom fields
CUSTOM_FIELD1_OPTIONS = ["option1", "option2", "option3"]
CUSTOM_FIELD2_OPTIONS = ["choice_a", "choice_b", "choice_c", "choice_d"]

# Example custom template definition
EXAMPLE_CUSTOM_TEMPLATE = {
    "name": "example_custom",
    "display_name": "Example Custom Template",
    "description": ("This is an example of how to create a custom template. "
                   "Edit this file to create your own template."),
    "bio_fields": ["virtue", "vice", "custom_field1", "custom_field2"],
    "integrity_name": "Integrity",
    "starting_integrity": 7,
    "field_validations": {
        "custom_field1": {
            "valid_values": CUSTOM_FIELD1_OPTIONS
        },
        "custom_field2": {
            "valid_values": CUSTOM_FIELD2_OPTIONS
        }
    },
    "version": "1.0",
    "author": "Your Name Here",
    "game_line": "Your Game Line",
    "notes": "Customize this template to fit your needs. Remember to change the name and display_name fields."
}

# Register the template
register_template(EXAMPLE_CUSTOM_TEMPLATE)
'''
    
    # Save example to templates directory
    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    templates_dir = os.path.join(current_dir, 'world', 'cofd', 'templates')
    example_path = os.path.join(templates_dir, 'example_custom.py')
    
    try:
        with open(example_path, 'w', encoding='utf-8') as f:
            f.write(example_template_code)
        print(f"Created example template file: {example_path}")
        return True
    except Exception as e:
        print(f"Error creating example template: {e}")
        return False


def create_template_readme():
    """
    Create a README file for the templates directory.
    """
    readme_content = '''# Chronicles of Darkness - Template Definitions

This directory contains character template definitions as Python modules.

## Creating Custom Templates

1. **Copy an existing template** as a starting point:
   ```bash
   cp vampire.py my_template.py
   ```

2. **Edit the template file**:
   - Change the template dictionary values
   - Update validation rules as needed
   - Modify bio fields for your template
   - Update metadata (author, version, etc.)

3. **Import in __init__.py**:
   Add your module to the imports in `__init__.py`:
   ```python
   from . import my_template
   ```

4. **Install the template**:
   Use the in-game command:
   ```
   +template install builtin
   ```

## Template Structure

Templates are Python dictionaries with the following structure:

```python
MY_TEMPLATE = {
    "name": "template_name",           # Unique identifier (lowercase)
    "display_name": "Template Name",   # Human-readable name
    "description": "Template description",
    "bio_fields": ["field1", "field2"],
    "integrity_name": "Integrity",
    "starting_integrity": 7,
    "field_validations": {
        "field1": {
            "valid_values": ["option1", "option2"]
        }
    },
    "version": "1.0",
    "author": "Your Name"
}
```

## Benefits of Python Templates

- **Native Integration**: No JSON parsing overhead
- **IDE Support**: Syntax highlighting and error checking
- **Comments**: Can include documentation and comments
- **Variables**: Can use Python variables for lists and constants
- **Validation**: Python syntax checking catches errors early

## Available Templates

- `mortal.py` - Basic human template
- `vampire.py` - Vampire: The Requiem template
- `mage.py` - Mage: The Awakening template
- `changeling.py` - Changeling: The Lost template
- `example_custom.py` - Example custom template

## Management Commands

- `+template list` - List installed templates
- `+template builtin` - List available built-in templates
- `+template install builtin` - Install all built-in templates
- `+template export <template>` - Get Python code for a template
'''
    
    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    templates_dir = os.path.join(current_dir, 'world', 'cofd', 'templates')
    readme_path = os.path.join(templates_dir, 'README.md')
    
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"Created template README: {readme_path}")
        return True
    except Exception as e:
        print(f"Error creating README: {e}")
        return False


def setup_template_system():
    """
    Complete setup of the template system.
    """
    print("=" * 60)
    print("CHRONICLES OF DARKNESS TEMPLATE SYSTEM SETUP")
    print("=" * 60)
    
    # Install default templates
    setup_template_system()
    
    # Create example custom template
    create_custom_template_example()
    
    # Create README documentation
    create_template_readme()
    
    # Clear template cache to ensure fresh load
    template_registry.clear_cache()
    
    print("\nTemplate system setup complete!")
    print("\nAvailable commands:")
    print("  +template list                 - List all installed templates")
    print("  +template builtin              - List built-in template definitions")
    print("  +template info <template>      - Show template information")
    print("  +template install builtin      - Install all built-in templates")
    print("  +template export <template>    - Export template as Python code")
    print("\nTo create custom templates:")
    print("  1. Create a Python module in world/cofd/templates/")
    print("  2. Import the module in world/cofd/templates/__init__.py")
    print("  3. Use +template install builtin to register the new template")
    print("  4. Use +template list to verify installation")
    
    return True


if __name__ == "__main__":
    # Allow script to be run directly
    setup_template_system() 
