"""
Cover Identity Management for Demon Characters

This module handles the creation and management of Cover Identities for Demon: The Descent characters.
Each Demon can maintain multiple cover identities based on their Primum rating.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.evmore import EvMore
from utils.search_helpers import search_character


class CmdCover(MuxCommand):
    """
    Manage cover identities for Demon characters.
    
    Usage:
        +cover - List all your cover identities
        +cover <id or name> - View detailed information about a specific cover
        +cover <character> - Staff: View another character's covers
        +cover/new <name> - Create a new cover identity
        +cover/name <id or name>=<new name> - Change cover name
        +cover/age <id or name>=<age> - Set cover age
        +cover/gender <id or name>=<gender> - Set cover gender
        +cover/occupation <id or name>=<occupation> - Set cover occupation
        +cover/primary <id or name> - Set as primary cover identity
        
    Staff Commands:
        +cover/rating <character>/<id or name>=<rating> - Set cover rating
        +cover/delete <character>=<id or name> - Delete a cover identity
    
    Raising Cover with XP:
        Use the XP system to raise cover ratings:
        +xp/spend cover:<id>=<new rating>
        
        Example: +xp/spend cover:1=8
        Cost: (new rating - current rating) × 3 XP per dot
    """
    
    key = "+cover"
    aliases = ["cover"]
    help_category = "Demon"
    
    def func(self):
        """Execute the command"""
        # Determine target character
        target = self.caller
        is_staff = self.caller.check_permstring("Builder")
        
        # Handle switches
        if self.switches:
            switch = self.switches[0].lower()
            
            # Staff-only switches that target other characters
            if switch in ["rating", "delete"]:
                # These require staff and use different syntax
                if not is_staff:
                    self.caller.msg("|rOnly staff can use this switch.|n")
                    return
                
                if switch == "rating":
                    self.set_cover_rating_staff()
                elif switch == "delete":
                    self.delete_cover_staff()
                return
            
            # Regular switches (operate on caller)
            template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
            if template.lower() != "demon":
                self.caller.msg("|rOnly Demon characters can use cover identities.|n")
                self.caller.msg(f"Your template is: {template}")
                return
            
            if switch == "new":
                self.create_cover()
            elif switch == "name":
                self.set_cover_field("name")
            elif switch == "age":
                self.set_cover_field("age")
            elif switch == "gender":
                self.set_cover_field("gender")
            elif switch == "occupation":
                self.set_cover_field("occupation")
            elif switch == "primary":
                self.set_primary_cover()
            else:
                self.caller.msg(f"|rInvalid switch: {switch}|n")
                self.caller.msg("Valid switches: new, name, age, gender, occupation, rating, delete, primary")
            return
        
        # No switches - show covers
        if self.args:
            # Could be viewing a specific cover, or staff viewing another character
            # Try to find as a character first (if staff)
            if is_staff:
                target_char = search_character(self.caller, self.args.strip(), quiet=True)
                if target_char:
                    # Verify target is a Demon
                    target_template = target_char.db.stats.get("other", {}).get("template", "Mortal")
                    if target_template.lower() != "demon":
                        self.caller.msg(f"|r{target_char.name} is not a Demon (template: {target_template})|n")
                        return
                    # Found a character - list their covers
                    self.list_covers(target_char)
                    return
            
            # Not a character or not staff - treat as cover identifier for self
            template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
            if template.lower() != "demon":
                self.caller.msg("|rOnly Demon characters can use cover identities.|n")
                self.caller.msg(f"Your template is: {template}")
                return
            
            self.show_cover(self.args.strip(), self.caller)
        else:
            # Show all covers for self
            template = self.caller.db.stats.get("other", {}).get("template", "Mortal")
            if template.lower() != "demon":
                self.caller.msg("|rOnly Demon characters can use cover identities.|n")
                self.caller.msg(f"Your template is: {template}")
                return
            
            self.list_covers(self.caller)
    
    def get_max_covers(self, character=None):
        """Calculate maximum number of covers based on Primum."""
        if character is None:
            character = self.caller
        
        primum = character.db.stats.get("advantages", {}).get("primum", 1)
        
        if primum <= 4:
            return primum
        elif primum <= 6:
            return 5
        elif primum <= 8:
            return 6
        else:  # 9-10
            return 7
    
    def initialize_covers(self, character=None):
        """Initialize cover identities storage if it doesn't exist."""
        if character is None:
            character = self.caller
        
        if not hasattr(character.db, 'cover_identities') or character.db.cover_identities is None:
            character.db.cover_identities = {}
        if not hasattr(character.db, 'next_cover_id') or character.db.next_cover_id is None:
            character.db.next_cover_id = 1
        if not hasattr(character.db, 'primary_cover_id'):
            character.db.primary_cover_id = None
    
    def create_cover(self):
        """Create a new cover identity."""
        if not self.args:
            self.caller.msg("Usage: +cover/new <name>")
            return
        
        self.initialize_covers()
        
        # Check if at max covers
        max_covers = self.get_max_covers()
        current_covers = len(self.caller.db.cover_identities)
        
        if current_covers >= max_covers:
            primum = self.caller.db.stats.get("advantages", {}).get("primum", 1)
            self.caller.msg(f"|rYou already have {current_covers} cover identities (maximum for Primum {primum}).|n")
            self.caller.msg(f"Increase your Primum or delete an existing cover to create a new one.")
            return
        
        cover_name = self.args.strip()
        
        # Check if name already exists
        for cover_id, cover_data in self.caller.db.cover_identities.items():
            if cover_data['name'].lower() == cover_name.lower():
                self.caller.msg(f"|rYou already have a cover identity named '{cover_name}'.|n")
                return
        
        # Create new cover
        cover_id = self.caller.db.next_cover_id
        self.caller.db.cover_identities[cover_id] = {
            'name': cover_name,
            'age': None,
            'gender': None,
            'occupation': None,
            'rating': 7  # Default Cover rating
        }
        self.caller.db.next_cover_id += 1
        
        # If this is the first cover, make it primary
        if self.caller.db.primary_cover_id is None:
            self.caller.db.primary_cover_id = cover_id
            primary_msg = " (set as primary)"
        else:
            primary_msg = ""
        
        self.caller.msg(f"|gCreated cover identity #{cover_id}: |w{cover_name}|n{primary_msg}")
        self.caller.msg(f"Use |y+cover/age {cover_id}=<age>|n, |y+cover/gender {cover_id}=<gender>|n, etc. to set details.")
    
    def find_cover(self, identifier, character=None):
        """Find a cover by ID or name."""
        if character is None:
            character = self.caller
        
        self.initialize_covers(character)
        
        # Try as ID first
        try:
            cover_id = int(identifier)
            if cover_id in character.db.cover_identities:
                return cover_id, character.db.cover_identities[cover_id]
        except ValueError:
            pass
        
        # Try as name (case-insensitive, underscore/space flexible)
        search_name = identifier.lower().replace("_", " ")
        for cover_id, cover_data in character.db.cover_identities.items():
            cover_name = cover_data['name'].lower().replace("_", " ")
            if cover_name == search_name or cover_name.replace(" ", "_") == search_name.replace(" ", "_"):
                return cover_id, cover_data
        
        return None, None
    
    def set_cover_field(self, field):
        """Set a field on a cover identity."""
        if not self.args or "=" not in self.args:
            self.caller.msg(f"Usage: +cover/{field} <id or name>=<value>")
            return
        
        identifier, value = self.args.split("=", 1)
        identifier = identifier.strip()
        value = value.strip()
        
        cover_id, cover_data = self.find_cover(identifier)
        if not cover_data:
            self.caller.msg(f"|rCover identity '{identifier}' not found.|n")
            self.caller.msg("Use |y+cover|n to see your cover identities.")
            return
        
        # Validate age if setting age
        if field == "age":
            try:
                age_val = int(value)
                if age_val < 0 or age_val > 200:
                    self.caller.msg("|rAge must be between 0 and 200.|n")
                    return
            except ValueError:
                self.caller.msg("|rAge must be a number.|n")
                return
        
        # Set the field
        cover_data[field] = value
        self.caller.db.cover_identities[cover_id] = cover_data
        
        field_display = field.replace("_", " ").title()
        self.caller.msg(f"|gSet {field_display} for cover #{cover_id} ({cover_data['name']}) to: |w{value}|n")
    
    def set_cover_rating_staff(self):
        """Set cover rating (staff only) - Format: character/cover=rating."""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("|rOnly staff can directly set cover ratings.|n")
            self.caller.msg("Use |w+xp/spend cover:<id>=<rating>|n to raise your own covers with XP.")
            return
        
        if not self.args or "/" not in self.args or "=" not in self.args:
            self.caller.msg("Usage: +cover/rating <character>/<id or name>=<rating>")
            self.caller.msg("Example: +cover/rating John/1=8")
            return
        
        # Parse character/cover=rating
        char_cover, value = self.args.split("=", 1)
        char_name, cover_identifier = char_cover.split("/", 1)
        char_name = char_name.strip()
        cover_identifier = cover_identifier.strip()
        value = value.strip()
        
        # Find target character
        target = search_character(self.caller, char_name)
        if not target:
            return
        
        # Verify target is a Demon
        template = target.db.stats.get("other", {}).get("template", "Mortal")
        if template.lower() != "demon":
            self.caller.msg(f"|r{target.name} is not a Demon (template: {template})|n")
            return
        
        # Find the cover
        cover_id, cover_data = self.find_cover(cover_identifier, target)
        if not cover_data:
            self.caller.msg(f"|rCover identity '{cover_identifier}' not found on {target.name}.|n")
            self.caller.msg(f"Use |w+cover {target.name}|n to see their covers.")
            return
        
        # Validate rating
        try:
            rating = int(value)
            if rating < 0 or rating > 10:
                self.caller.msg("|rCover rating must be between 0 and 10.|n")
                return
        except ValueError:
            self.caller.msg("|rCover rating must be a number.|n")
            return
        
        old_rating = cover_data['rating']
        
        # Set the rating
        cover_data['rating'] = rating
        target.db.cover_identities[cover_id] = cover_data
        
        self.caller.msg(f"|gSet {target.name}'s Cover #{cover_id} ({cover_data['name']}) from {old_rating} to {rating}.|n")
        target.msg(f"|y{self.caller.name} has set your Cover '{cover_data['name']}' rating to {rating}.|n")
    
    def delete_cover_staff(self):
        """Delete a cover identity (staff only) - Format: character=cover."""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("|rOnly staff can delete cover identities.|n")
            return
        
        if not self.args or "=" not in self.args:
            self.caller.msg("Usage: +cover/delete <character>=<id or name>")
            self.caller.msg("Example: +cover/delete John=1")
            return
        
        # Parse character=cover
        char_name, cover_identifier = self.args.split("=", 1)
        char_name = char_name.strip()
        cover_identifier = cover_identifier.strip()
        
        # Find target character
        target = search_character(self.caller, char_name)
        if not target:
            return
        
        # Verify target is a Demon
        template = target.db.stats.get("other", {}).get("template", "Mortal")
        if template.lower() != "demon":
            self.caller.msg(f"|r{target.name} is not a Demon (template: {template})|n")
            return
        
        # Find the cover
        cover_id, cover_data = self.find_cover(cover_identifier, target)
        if not cover_data:
            self.caller.msg(f"|rCover identity '{cover_identifier}' not found on {target.name}.|n")
            self.caller.msg(f"Use |w+cover {target.name}|n to see their covers.")
            return
        
        cover_name = cover_data['name']
        del target.db.cover_identities[cover_id]
        
        # If this was primary, clear primary
        if target.db.primary_cover_id == cover_id:
            target.db.primary_cover_id = None
            # Set a new primary if covers remain
            if target.db.cover_identities:
                new_primary = min(target.db.cover_identities.keys())
                target.db.primary_cover_id = new_primary
                self.caller.msg(f"|ySet cover #{new_primary} as new primary for {target.name}.|n")
                target.msg(f"|yCover #{new_primary} is now your primary cover.|n")
        
        self.caller.msg(f"|gDeleted {target.name}'s cover identity #{cover_id}: {cover_name}|n")
        target.msg(f"|y{self.caller.name} has deleted your cover identity: {cover_name}|n")
    
    def set_primary_cover(self):
        """Set a cover as the primary identity."""
        if not self.args:
            self.caller.msg("Usage: +cover/primary <id or name>")
            return
        
        cover_id, cover_data = self.find_cover(self.args.strip())
        if not cover_data:
            self.caller.msg(f"|rCover identity '{self.args}' not found.|n")
            return
        
        self.caller.db.primary_cover_id = cover_id
        self.caller.msg(f"|gSet cover #{cover_id} ({cover_data['name']}) as your primary identity.|n")
    
    def show_cover(self, identifier, character=None):
        """Show detailed information about a specific cover."""
        if character is None:
            character = self.caller
        
        cover_id, cover_data = self.find_cover(identifier, character)
        if not cover_data:
            self.caller.msg(f"|rCover identity '{identifier}' not found.|n")
            if character == self.caller:
                self.caller.msg("Use |y+cover|n to see your cover identities.")
            else:
                self.caller.msg(f"Use |y+cover {character.name}|n to see their covers.")
            return
        
        output = []
        output.append("|y" + "=" * 78 + "|n")
        
        is_primary = (cover_id == character.db.primary_cover_id)
        primary_text = " |g(PRIMARY)|n" if is_primary else ""
        
        if character == self.caller:
            title = f"COVER IDENTITY #{cover_id}{primary_text}"
        else:
            title = f"{character.name.upper()}'S COVER #{cover_id}{primary_text}"
        
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        output.append(f"|wName:|n {cover_data['name']}")
        output.append(f"|wAge:|n {cover_data['age'] if cover_data['age'] else '<not set>'}")
        output.append(f"|wGender:|n {cover_data['gender'] if cover_data['gender'] else '<not set>'}")
        output.append(f"|wOccupation:|n {cover_data['occupation'] if cover_data['occupation'] else '<not set>'}")
        output.append(f"|wCover Rating:|n {cover_data['rating']}/10")
        output.append("")
        
        output.append("|xCover rating represents how well-established this identity is.|n")
        output.append("|xIt can be damaged by breaking points and raised with XP.|n")
        output.append("")
        output.append("|y" + "=" * 78 + "|n")
        
        self.caller.msg("\n".join(output))
    
    def list_covers(self, character=None):
        """List all cover identities."""
        if character is None:
            character = self.caller
        
        self.initialize_covers(character)
        
        if not character.db.cover_identities:
            if character == self.caller:
                self.caller.msg("|yYou have no cover identities yet.|n")
                self.caller.msg("Use |w+cover/new <name>|n to create one.")
            else:
                self.caller.msg(f"|y{character.name} has no cover identities yet.|n")
            return
        
        output = []
        output.append("|y" + "=" * 78 + "|n")
        title = f"{character.name}'s COVER IDENTITIES"
        output.append("|y" + title.center(78) + "|n")
        output.append("|y" + "=" * 78 + "|n")
        output.append("")
        
        primum = character.db.stats.get("advantages", {}).get("primum", 1)
        max_covers = self.get_max_covers(character)
        current_covers = len(character.db.cover_identities)
        
        output.append(f"|wCurrent Covers:|n {current_covers}/{max_covers} (Primum {primum})")
        output.append("")
        
        # Sort by ID
        for cover_id in sorted(character.db.cover_identities.keys()):
            cover_data = character.db.cover_identities[cover_id]
            
            is_primary = (cover_id == character.db.primary_cover_id)
            primary_marker = " |g[PRIMARY]|n" if is_primary else ""
            
            output.append(f"|c#{cover_id}|n - |w{cover_data['name']}|n{primary_marker}")
            
            details = []
            if cover_data.get('age'):
                details.append(f"Age: {cover_data['age']}")
            if cover_data.get('gender'):
                details.append(f"Gender: {cover_data['gender']}")
            if cover_data.get('occupation'):
                details.append(f"Occupation: {cover_data['occupation']}")
            details.append(f"Cover: {cover_data['rating']}/10")
            
            if details:
                output.append(f"     {', '.join(details)}")
            output.append("")
        
        if character == self.caller:
            output.append("|xUse |w+cover <id or name>|x for detailed information.|n")
            output.append("|xUse |w+cover/primary <id>|x to set your primary identity.|n")
        else:
            output.append("|xUse |w+cover/rating {0}/<id>=<rating>|x to set ratings (staff).|n".format(character.name))
            output.append("|xUse |w+cover/delete {0}=<id>|x to delete covers (staff).|n".format(character.name))
        
        output.append("|y" + "=" * 78 + "|n")
        
        text = "\n".join(output)
        EvMore(self.caller, text, always_page=False, session=self.session, justify_kwargs=False, exit_on_lastpage=True)
