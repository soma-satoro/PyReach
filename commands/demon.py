"""
Demonic Form Management for Demon Characters

This module handles the creation and display of demonic forms for Demon: The Descent characters.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.evmore import EvMore
from utils.search_helpers import search_character


class CmdDemon(MuxCommand):
    """
    View and manage your demonic form.
    
    Usage:
        +demon - View your demonic form
        +demon <character> - View someone else's demonic form (if visible)
        +demon/desc <description> - Set your demonic form description
        +demon/modification <trait> - Add a modification
        +demon/technology <trait> - Add a technology
        +demon/propulsion <trait> - Add a propulsion
        +demon/process <trait> - Add a process
        +demon/remove <type>=<trait> - Remove a trait (when swapping at Primum increase)
        +demon/swap <type>=<old trait>:<new trait> - Swap a trait
        
    Your demonic form represents your true nature as a Demon.
    
    Form Trait Limits:
        Starting (chargen):
            - 3 Modifications
            - 2 Technologies
            - 1 Propulsion
            - 1 Process
            
        Primum Bonuses:
            - Primum 3: Gain 4th Modification
            - Primum 6: Gain 3rd Technology
            - Primum 10: Gain 2nd Process
            
        When Primum Increases:
            - Can swap up to 2 form abilities for new ones (same type)
            - Use +demon/swap to replace traits
    """
    
    key = "+demon"
    aliases = ["demon", "demonform"]
    help_category = "Demon"
    
    def func(self):
        """Execute the command"""
        # Determine target
        if self.args and not self.switches:
            target = search_character(self.caller, self.args.strip())
            if not target:
                return
        else:
            target = self.caller
        
        # Check if target is a Demon
        template = target.db.stats.get("other", {}).get("template", "Mortal")
        if template.lower() != "demon":
            if target == self.caller:
                self.caller.msg("|rOnly Demon characters have a demonic form.|n")
                self.caller.msg(f"Your template is: {template}")
            else:
                self.caller.msg(f"|r{target.name} is not a Demon.|n")
            return
        
        # Handle switches
        if self.switches:
            switch = self.switches[0].lower()
            
            if switch == "desc":
                self.set_description()
            elif switch == "modification":
                self.add_trait("modifications")
            elif switch == "technology":
                self.add_trait("technologies")
            elif switch == "propulsion":
                self.add_trait("propulsion")
            elif switch == "process":
                self.add_trait("process")
            elif switch == "remove":
                self.remove_trait()
            elif switch == "swap":
                self.swap_trait()
            else:
                self.caller.msg(f"|rInvalid switch: {switch}|n")
                self.caller.msg("Valid switches: desc, modification, technology, propulsion, process, remove, swap")
            return
        
        # No switches - show demonic form
        self.show_demonic_form(target)
    
    def get_max_traits(self, trait_type):
        """Get maximum number of traits allowed for a given type based on Primum."""
        primum = self.caller.db.stats.get("advantages", {}).get("primum", 1)
        
        if trait_type == "modifications":
            # Base 3, +1 at Primum 3
            return 3 if primum < 3 else 4
        elif trait_type == "technologies":
            # Base 2, +1 at Primum 6
            return 2 if primum < 6 else 3
        elif trait_type == "propulsion":
            # Always 1
            return 1
        elif trait_type == "process":
            # Base 1, +1 at Primum 10
            return 1 if primum < 10 else 2
        return 0
    
    def initialize_demon_form(self):
        """Initialize demon form storage if it doesn't exist."""
        if not hasattr(self.caller.db, 'demon_form_stats'):
            self.caller.db.demon_form_stats = {
                'description': None,
                'modifications': [],
                'technologies': [],
                'propulsion': [],
                'process': []
            }
    
    def set_description(self):
        """Set the demonic form description."""
        if not self.args:
            self.caller.msg("Usage: +demon/desc <description>")
            self.caller.msg("Describe what your demonic form looks like.")
            return
        
        self.initialize_demon_form()
        
        description = self.args.strip()
        self.caller.db.demon_form_stats['description'] = description
        
        self.caller.msg("|gDemonic form description set.|n")
        self.caller.msg(f"|wDescription:|n {description}")
    
    def add_trait(self, trait_type):
        """Add a trait to the demonic form."""
        if not self.args:
            trait_display = trait_type.rstrip('s').title()  # Remove plural 's' for display
            self.caller.msg(f"Usage: +demon/{trait_display.lower()} <trait name>")
            return
        
        self.initialize_demon_form()
        
        trait_name = self.args.strip()
        
        # Check if character is approved (only staff can modify approved characters)
        is_npc = hasattr(self.caller, 'db') and self.caller.db.is_npc
        is_approved = self.caller.db.approved if not is_npc else False
        is_staff = self.caller.check_permstring("Builder")
        
        if is_approved and not is_staff:
            self.caller.msg("|rYour character is approved.|n")
            self.caller.msg("Contact staff to modify demonic form traits.")
            self.caller.msg("|xNote: Demonic form traits cannot be purchased with XP.|n")
            return
        
        # Check current count against maximum
        current_count = len(self.caller.db.demon_form_stats[trait_type])
        max_count = self.get_max_traits(trait_type)
        
        if current_count >= max_count:
            primum = self.caller.db.stats.get("advantages", {}).get("primum", 1)
            trait_display = trait_type.rstrip('s').title()
            self.caller.msg(f"|rYou already have {current_count} {trait_display}s (maximum for Primum {primum}).|n")
            self.caller.msg(f"Use |w+demon/swap {trait_type}=<old>:<new>|n to replace an existing trait.")
            return
        
        # Check if trait already exists
        if trait_name in self.caller.db.demon_form_stats[trait_type]:
            self.caller.msg(f"|yYou already have that {trait_type.rstrip('s')}.|n")
            return
        
        # Add the trait
        self.caller.db.demon_form_stats[trait_type].append(trait_name)
        trait_display = trait_type.rstrip('s').title()
        self.caller.msg(f"|gAdded {trait_display}: |w{trait_name}|n")
        self.caller.msg(f"|xCurrent {trait_display}s: {current_count + 1}/{max_count}|n")
    
    def remove_trait(self):
        """Remove a trait from the demonic form."""
        if not self.args or "=" not in self.args:
            self.caller.msg("Usage: +demon/remove <type>=<trait name>")
            self.caller.msg("Types: modifications, technologies, propulsion, process")
            return
        
        self.initialize_demon_form()
        
        trait_type, trait_name = self.args.split("=", 1)
        trait_type = trait_type.strip().lower()
        trait_name = trait_name.strip()
        
        # Validate trait type
        valid_types = ['modifications', 'technologies', 'propulsion', 'process']
        if trait_type not in valid_types:
            self.caller.msg(f"|rInvalid trait type: {trait_type}|n")
            self.caller.msg(f"Valid types: {', '.join(valid_types)}")
            return
        
        # Check if character is approved
        is_npc = hasattr(self.caller, 'db') and self.caller.db.is_npc
        is_approved = self.caller.db.approved if not is_npc else False
        is_staff = self.caller.check_permstring("Builder")
        
        if is_approved and not is_staff:
            self.caller.msg("|rYour character is approved.|n")
            self.caller.msg("Use |w+demon/swap|n to replace traits when your Primum increases.")
            return
        
        # Remove the trait
        if trait_name in self.caller.db.demon_form_stats[trait_type]:
            self.caller.db.demon_form_stats[trait_type].remove(trait_name)
            trait_display = trait_type.rstrip('s').title()
            self.caller.msg(f"|gRemoved {trait_display}: |w{trait_name}|n")
        else:
            self.caller.msg(f"|yYou don't have that {trait_type.rstrip('s')}.|n")
    
    def swap_trait(self):
        """Swap one trait for another (when Primum increases)."""
        if not self.args or "=" not in self.args or ":" not in self.args:
            self.caller.msg("Usage: +demon/swap <type>=<old trait>:<new trait>")
            self.caller.msg("Example: +demon/swap modifications=Wings:Claws")
            return
        
        self.initialize_demon_form()
        
        trait_type, traits = self.args.split("=", 1)
        trait_type = trait_type.strip().lower()
        
        if ":" not in traits:
            self.caller.msg("Usage: +demon/swap <type>=<old trait>:<new trait>")
            return
        
        old_trait, new_trait = traits.split(":", 1)
        old_trait = old_trait.strip()
        new_trait = new_trait.strip()
        
        # Validate trait type
        valid_types = ['modifications', 'technologies', 'propulsion', 'process']
        if trait_type not in valid_types:
            self.caller.msg(f"|rInvalid trait type: {trait_type}|n")
            self.caller.msg(f"Valid types: {', '.join(valid_types)}")
            return
        
        # Check if old trait exists
        if old_trait not in self.caller.db.demon_form_stats[trait_type]:
            self.caller.msg(f"|rYou don't have '{old_trait}' to swap.|n")
            return
        
        # Check if new trait already exists
        if new_trait in self.caller.db.demon_form_stats[trait_type]:
            self.caller.msg(f"|yYou already have '{new_trait}'.|n")
            return
        
        # Swap the traits
        self.caller.db.demon_form_stats[trait_type].remove(old_trait)
        self.caller.db.demon_form_stats[trait_type].append(new_trait)
        
        trait_display = trait_type.rstrip('s').title()
        self.caller.msg(f"|gSwapped {trait_display}:|n")
        self.caller.msg(f"  Removed: |r{old_trait}|n")
        self.caller.msg(f"  Added: |g{new_trait}|n")
    
    def show_demonic_form(self, target):
        """Display the demonic form."""
        # Check if demon form exists
        if not hasattr(target.db, 'demon_form_stats') or not target.db.demon_form_stats:
            if target == self.caller:
                self.caller.msg("|yYou haven't defined your demonic form yet.|n")
                self.caller.msg("Use |w+demon/desc <description>|n to describe your form.")
                self.caller.msg("")
                self.caller.msg("|wStarting Traits (Chargen):|n")
                self.caller.msg("  • 3 Modifications")
                self.caller.msg("  • 2 Technologies")
                self.caller.msg("  • 1 Propulsion")
                self.caller.msg("  • 1 Process")
            else:
                self.caller.msg(f"|y{target.name} hasn't defined their demonic form yet.|n")
            return
        
        demon_form = target.db.demon_form_stats
        
        # Get Primum and calculate maximums (if viewing self)
        if target == self.caller:
            primum = self.caller.db.stats.get("advantages", {}).get("primum", 1)
            max_mods = self.get_max_traits("modifications")
            max_techs = self.get_max_traits("technologies")
            max_prop = self.get_max_traits("propulsion")
            max_proc = self.get_max_traits("process")
        else:
            primum = target.db.stats.get("advantages", {}).get("primum", 1)
            max_mods = 3 if primum < 3 else 4
            max_techs = 2 if primum < 6 else 3
            max_prop = 1
            max_proc = 1 if primum < 10 else 2
        
        output = []
        output.append("|y" + "=" * 78 + "|n")
        title = f"{target.name}'s DEMONIC FORM"
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        # Description
        if demon_form.get('description'):
            output.append("|wDescription:|n")
            output.append(f"{demon_form['description']}")
            output.append("")
        
        # Modifications
        mods_count = len(demon_form.get('modifications', []))
        output.append(f"|wModifications ({mods_count}/{max_mods}):|n")
        if demon_form.get('modifications'):
            for mod in demon_form['modifications']:
                output.append(f"  • {mod}")
        else:
            output.append("  None yet")
        output.append("")
        
        # Technologies
        techs_count = len(demon_form.get('technologies', []))
        output.append(f"|wTechnologies ({techs_count}/{max_techs}):|n")
        if demon_form.get('technologies'):
            for tech in demon_form['technologies']:
                output.append(f"  • {tech}")
        else:
            output.append("  None yet")
        output.append("")
        
        # Propulsion
        prop_count = len(demon_form.get('propulsion', []))
        output.append(f"|wPropulsion ({prop_count}/{max_prop}):|n")
        if demon_form.get('propulsion'):
            for prop in demon_form['propulsion']:
                output.append(f"  • {prop}")
        else:
            output.append("  None yet")
        output.append("")
        
        # Process
        proc_count = len(demon_form.get('process', []))
        output.append(f"|wProcess ({proc_count}/{max_proc}):|n")
        if demon_form.get('process'):
            for proc in demon_form['process']:
                output.append(f"  • {proc}")
        else:
            output.append("  None yet")
        output.append("")
        
        output.append("|xYour demonic form is your true nature as an angel that Fell.|n")
        output.append("|xTraits are set at chargen and modified when Primum increases.|n")
        
        if target == self.caller:
            output.append("")
            output.append("|wPrimum Bonuses:|n")
            if primum >= 3:
                output.append("  |g✓|n Primum 3: 4th Modification")
            else:
                output.append("  |x○|n Primum 3: 4th Modification (not yet)")
            
            if primum >= 6:
                output.append("  |g✓|n Primum 6: 3rd Technology")
            else:
                output.append("  |x○|n Primum 6: 3rd Technology (not yet)")
            
            if primum >= 10:
                output.append("  |g✓|n Primum 10: 2nd Process")
            else:
                output.append("  |x○|n Primum 10: 2nd Process (not yet)")
        
        output.append("")
        output.append("|y" + "=" * 78 + "|n")
        
        text = "\n".join(output)
        EvMore(self.caller, text, always_page=False, session=self.session, justify_kwargs=False, exit_on_lastpage=True)
