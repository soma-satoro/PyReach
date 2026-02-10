"""
Census command for tracking approved character demographics.

Shows counts of approved characters by template and bio fields.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia import ObjectDB
from datetime import datetime, timedelta
from django.utils import timezone
from collections import defaultdict
from world.reality_systems import get_template


class CmdCensus(MuxCommand):
    """
    Display a census of approved characters by template.
    
    Usage:
        +census                           - Show general census by template
        +census/template <template name>  - Show detailed breakdown for a template
        +census/all                       - (Staff) Show all approved chars (no filters)
        +census/debug                     - (Staff) Show why chars are filtered out
        
    Shows counts of all approved characters who have been approved for 6+ hours.
    
    Template breakdowns show:
        Vampire: Clan, Covenant
        Werewolf: Tribe, Auspice
        Mage: Path, Order
        Changeling: Seeming, Court
        Geist: Burden
        Hunter: Organization
        Deviant: Clade, Origin
        Demon: Incarnation, Agenda
        Mummy: Guild, Decree
        Mortal+: Template Type
        Promethean: Lineage, Refinement
        
    Examples:
        +census                    - View general census
        +census/template Werewolf  - View werewolf demographics
        +census/template vampire   - View vampire demographics (case insensitive)
        +census/all                - (Staff) List all approved characters
        +census/debug              - (Staff) Show detailed filtering information
    """
    
    key = "+census"
    aliases = ["census"]
    help_category = "Chargen & Character Info"
    
    # Map templates to their demographic fields (exact field names from bio_fields in templates)
    TEMPLATE_FIELDS = {
        "vampire": ["clan", "covenant"],
        "werewolf": ["auspice", "tribe"],
        "mage": ["path", "order"],
        "changeling": ["seeming", "court"],
        "geist": ["burden"],
        "hunter": ["organization"],
        "deviant": ["clade", "origin"],
        "demon": ["incarnation", "agenda"],
        "mummy": ["guild", "decree"],
        "mortal+": ["template_type"],
        "mortal plus": ["template_type"],
        "promethean": ["lineage", "refinement"],
        "mortal": []  # Mortals have no special census tracking
    }
    
    def func(self):
        """Execute the census command"""
        # Get switch and args
        switch = self.switches[0].lower() if self.switches else None
        
        if switch == "template":
            if not self.args:
                self.caller.msg("Usage: +census/template <template name>")
                return
            self.show_template_census(self.args.strip())
        elif switch == "all":
            # Staff-only: Show all approved characters without restrictions
            if not self.caller.check_permstring("Builder"):
                self.caller.msg("|rYou don't have permission to use that switch.|n")
                return
            self.show_all_approved()
        elif switch == "debug":
            # Staff-only: Show detailed filtering info
            if not self.caller.check_permstring("Builder"):
                self.caller.msg("|rYou don't have permission to use that switch.|n")
                return
            self.show_debug_info()
        else:
            self.show_general_census()
    
    def show_all_approved(self):
        """Staff-only: Show all approved characters without time restrictions"""
        all_chars = ObjectDB.objects.filter(db_typeclass_path__icontains="characters.Character")
        
        self.caller.msg(f"|cTotal characters found: {all_chars.count()}|n")
        
        approved_chars = []
        for char in all_chars:
            if hasattr(char, 'db'):
                approved = getattr(char.db, 'approved', None)
                if approved is True:
                    template = get_template(char)
                    approved_chars.append(char)
        
        if not approved_chars:
            self.caller.msg("|rNo approved characters found at all.|n")
            self.caller.msg("|xSearched all characters with typeclass containing 'characters.Character'|n")
            return
        
        self.caller.msg(f"|gFound {len(approved_chars)} approved characters:|n")
        self.caller.msg("")
        
        # Show detailed list and count by template
        template_counts = defaultdict(int)
        for char in approved_chars:
            template = get_template(char)
            self.caller.msg(f"  {char.name}: Template={template}")
            template_counts[template] += 1
        
        self.caller.msg("|wApproved characters by template:|n")        
        for template, count in sorted(template_counts.items()):
            self.caller.msg(f"  {template}: {count}")
        
        self.caller.msg("\n|yUse '+census' for the normal filtered view.|n")
    
    def show_debug_info(self):
        """Staff-only: Show detailed filtering information"""
        all_chars = ObjectDB.objects.filter(db_typeclass_path__icontains="characters.Character")
        
        self.caller.msg("|c" + "="*78 + "|n")
        self.caller.msg("|wCENSUS DEBUG INFORMATION|n")
        self.caller.msg("|c" + "="*78 + "|n")
        self.caller.msg(f"\nTotal characters in database: {all_chars.count()}")
        
        # Current time for comparison
        now = timezone.now()
        six_hours_ago = now - timedelta(hours=6)
        
        approved_count = 0
        passed_approval_time = 0
        final_eligible = 0
        
        for char in all_chars:
            # Check approval
            if not hasattr(char, 'db'):
                continue
                
            approved = getattr(char.db, 'approved', None)
            if approved is not True:
                continue
            approved_count += 1
            
            # Check approval time
            approved_date = None
            try:
                from world.roster.models import RosterMember  # type: ignore
                roster_member = RosterMember.objects.filter(character=char).first()
                if roster_member and hasattr(roster_member, 'approved_date'):
                    approved_date = roster_member.approved_date
            except ImportError:
                pass
            except Exception:
                pass
            
            if not approved_date and hasattr(char, 'db_date_created'):
                approved_date = char.db_date_created
            
            approval_time_ok = True
            if approved_date:
                if not timezone.is_aware(approved_date):
                    try:
                        approved_date = timezone.make_aware(approved_date)
                    except:
                        approved_date = None
                
                if approved_date and approved_date > six_hours_ago:
                    time_diff = approved_date - six_hours_ago
                    self.caller.msg(f"  |y{char.name}|n: Approved |rtoo recently|n ({time_diff.total_seconds()/3600:.1f} hours too soon)")
                    approval_time_ok = False
                    continue
            
            if approval_time_ok:
                passed_approval_time += 1
                final_eligible += 1
                template = get_template(char)
                self.caller.msg(f"  |g{char.name}|n: Template={template} - |gPASSED ALL FILTERS|n")
        
        self.caller.msg("")
        self.caller.msg("|c" + "-"*78 + "|n")
        self.caller.msg(f"Approved: {approved_count}")
        self.caller.msg(f"Approved 6+ hours ago: {passed_approval_time}")
        self.caller.msg(f"|gFinal eligible count: {final_eligible}|n")
        self.caller.msg("|c" + "="*78 + "|n")
    
    def get_eligible_characters(self):
        """
        Get all eligible characters for the census.
        
        Returns:
            list: List of Character objects that meet the criteria
        """
        eligible = []
        
        # Get all character objects
        all_chars = ObjectDB.objects.filter(db_typeclass_path__icontains="characters.Character")
        
        # Current time for comparison
        now = timezone.now()
        six_hours_ago = now - timedelta(hours=6)
        
        for char in all_chars:
            # Must be approved (check the persistent attribute as a boolean)
            if not hasattr(char, 'db'):
                continue
            
            # Check approved attribute - must be explicitly True
            approved = getattr(char.db, 'approved', None)
            if approved is not True:
                continue
            
            # That's it! No account check needed - if they're approved, show them
            
            # Try to get approval date for 6+ hour check (optional, lenient)
            # If we can't determine approval date, we'll allow the character through
            try:
                approved_date = None
                try:
                    from world.roster.models import RosterMember  # type: ignore
                    roster_member = RosterMember.objects.filter(character=char).first()
                    if roster_member and hasattr(roster_member, 'approved_date'):
                        approved_date = roster_member.approved_date
                except ImportError:
                    pass
                except Exception:
                    pass
                
                # If no approval date found, check db_date_created as fallback
                if not approved_date and hasattr(char, 'db_date_created'):
                    approved_date = char.db_date_created
                
                # Only filter by approval time if we have a valid date
                if approved_date:
                    # Convert to timezone-aware if needed
                    if not timezone.is_aware(approved_date):
                        try:
                            approved_date = timezone.make_aware(approved_date)
                        except:
                            approved_date = None
                    
                    # Check if approved for 6+ hours
                    if approved_date and approved_date > six_hours_ago:
                        continue
            except Exception:
                # If any error with date checking, just allow through
                pass
            
            # No longer filtering by last login - show all approved characters regardless of connection status
            
            # Character meets criteria
            eligible.append(char)
        
        return eligible
    
    def show_general_census(self):
        """Display the general census grouped by template"""
        eligible = self.get_eligible_characters()
        
        # Check if any characters found
        if not eligible:
            self.caller.msg("|yNo approved characters found for census.|n")
            self.caller.msg("|xNote: Characters must have db.approved=True and be approved for 6+ hours.|n")
            return
        
        # Count by template
        template_counts = defaultdict(int)
        for char in eligible:
            template = get_template(char)
            template_counts[template] += 1
        
        # Sort templates alphabetically
        sorted_templates = sorted(template_counts.items())
        
        # Build output
        output = []
        header_text = "Approved Character Census"
        # Total width is 80, calculate padding for symmetric header
        total_width = 80
        # Format: ====> Text <====
        text_and_arrows = f"> {header_text} <"
        equals_count = total_width - len(text_and_arrows)
        left_equals = equals_count // 2
        right_equals = equals_count - left_equals
        output.append("|g" + "=" * left_equals + ">|n |w" + header_text + "|n |g<" + "=" * right_equals + "|n")
        
        # Format in columns (3 columns of ~26 chars each)
        line = ""
        col_width = 26
        col_count = 0
        
        for template, count in sorted_templates:
            entry = f"{template}: {count}"
            line += entry.ljust(col_width)
            col_count += 1
            
            if col_count >= 3:
                output.append(" " + line)
                line = ""
                col_count = 0
        
        # Add remaining entries
        if line:
            output.append(" " + line)
        
        output.append("")
        output.append("|g" + "=" * 80 + "|n")
        
        self.caller.msg("\n".join(output))
    
    def show_template_census(self, template_name):
        """
        Display detailed census for a specific template.
        
        Args:
            template_name (str): Name of the template to show
        """
        # Normalize template name
        template_name = template_name.lower().strip()
        
        # Check if we have fields defined for this template
        if template_name not in self.TEMPLATE_FIELDS:
            self.caller.msg(f"|rTemplate '{template_name}' not recognized or doesn't have census tracking.|n")
            self.caller.msg(f"|yAvailable templates:|n {', '.join(sorted(self.TEMPLATE_FIELDS.keys()))}")
            return
        
        eligible = self.get_eligible_characters()
        
        # Filter to only this template
        template_chars = []
        for char in eligible:
            char_template = get_template(char).lower()
            if char_template == template_name:
                template_chars.append(char)
        
        if not template_chars:
            self.caller.msg(f"|yNo approved {template_name.title()} characters found in the census.|n")
            return
        
        # Get the fields to display
        fields = self.TEMPLATE_FIELDS[template_name]
        
        # Build output
        output = []
        
        # Header with template name
        template_display = template_name.replace("_", " ").title()
        header_text = f"Approved {template_display} Census"
        # Total width is 80, calculate padding for symmetric header
        total_width = 80
        # Format: ====> Text <====
        text_and_arrows = f"> {header_text} <"
        equals_count = total_width - len(text_and_arrows)
        left_equals = equals_count // 2
        right_equals = equals_count - left_equals
        output.append("|g" + "=" * left_equals + ">|n |w" + header_text + "|n |g<" + "=" * right_equals + "|n")
        
        # For each field, count the values
        for field in fields:
            field_counts = defaultdict(int)
            
            for char in template_chars:
                # Get bio field value
                if not hasattr(char.db, 'stats') or not char.db.stats:
                    continue
                
                bio = char.db.stats.get("bio", {})
                if not bio:
                    continue
                
                value = bio.get(field, "Unknown")
                if not value or value == "":
                    value = "Unknown"
                
                # Format the value for display
                if isinstance(value, str):
                    # Replace underscores with spaces and title case
                    value = value.replace("_", " ").title()
                
                field_counts[value] += 1
            
            # Sort by value name
            sorted_values = sorted(field_counts.items())
            
            # Display this field's section
            field_display = field.replace("_", " ").title()
            output.append(f"|g----> {field_display} <" + "-" * (72 - len(field_display)) + "|n")
            
            # Format in columns (3 columns of ~26 chars each)
            line = ""
            col_width = 26
            col_count = 0
            
            for value, count in sorted_values:
                entry = f"{value}: {count}"
                line += entry.ljust(col_width)
                col_count += 1
                
                if col_count >= 3:
                    output.append(" " + line)
                    line = ""
                    col_count = 0
            
            # Add remaining entries
            if line:
                output.append(" " + line)
            
            output.append("")
        
        output.append("|g" + "=" * 80 + "|n")
        
        self.caller.msg("\n".join(output))
