from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from evennia.comms.models import ChannelDB
from evennia.utils import create
from world.groups.utils import (
    assign_character_to_group, 
    remove_character_from_group,
    ensure_group_channel_exists,
    auto_assign_character_groups,
    get_character_groups
)
from typeclasses.groups import (
    Group, create_group, get_group_by_id, get_group_by_name, 
    get_all_groups, get_public_groups
)
from django.db.models import Q
from evennia.objects.models import ObjectDB
from evennia.utils.utils import time_format, crop
from django.utils import timezone
from utils.search_helpers import search_character
from world.utils.formatting import header, footer, divider

class CmdGroups(MuxCommand):
    """
    Commands to create and manage player groups.
    
    Usage:
        +groups                    - List all public groups
        +group <id>                - View detailed information about a group
        +group/create <name>       - Create a new group (staff only)
        +group/destroy <id>        - Destroy a group (staff only)
        +group/type <id>=<type>    - Set group type (staff only)
        +group/leader <id>=<char>  - Set the leader of a group (staff only)
        +group/desc <id>=<text>    - Set a group's description (staff or leader)
        +group/note <id>=<text>    - Set a group's private notes (staff or leader)
        +group/title <id>/<char>=<title> - Set a character's title in the group
        +group/add <id>=<char>     - Add a character to a group (staff or leader)
        +group/remove <id>=<char>  - Remove a character from a group (staff or leader)
        +group/private <id>        - Set a group as private (staff or leader)
        +group/public <id>         - Set a group as public (staff or leader)
        +group/auto <char>         - Manually trigger automatic group assignment for a character
        +group/show <char>         - Show all groups a character belongs to
        +group/sync                - Sync all characters' group attributes (staff only)
        +group/sync <char>         - Sync a specific character's group attributes (staff only)
        +group/syncchannels        - Ensure all group channels exist and have proper locks (staff only)
        +group/synccleanup         - Remove orphaned group attributes (staff only)
        +group/test <character>    - Test group assignment for a character
        
    Mystery Cult Commands (for mysterycult type groups):
        +group/set <id>/<level>=<type>:<name>[:<desc>] - Set Mystery Cult benefit (staff/leader)
        +group/clear <id>/<level>  - Clear Mystery Cult benefit (staff/leader)
        +group/check <id>=<char>   - Check what benefits a character should have
        +group/template <name>     - View example mystery cult template
        
    Cell Tactics Commands (for cell type groups):
        +group/tactics <id>        - View all known tactics for a cell
        +group/tactics/add <id>=<tactic> - Add a tactic to the cell (staff/leader)
        +group/tactics/rem <id>=<tactic> - Remove a tactic from the cell (staff/leader)
        +group/tactics/list        - List all available tactics
        
    Group Types:
        coterie - Vampire groups
        pack - Werewolf groups
        cabal - Mage groups
        motley - Changeling groups
        krewe - Geist groups
        cell - Hunter cells
        mysterycult - Mystery Cults (Mortal/any template)
        agency - Mortal organizations
        cult - Mummy cults
        other - Generic groups
    """
    
    key = "+group"
    aliases = ["+groups"]
    locks = "cmd:all()"
    help_category = "Group Management"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
    def list_groups(self):
        """List all public groups."""
        groups = get_public_groups()
        
        if not groups:
            self.caller.msg("No groups have been created yet.")
            return
        
        # Create table
        table = evtable.EvTable(
            "|wID|n", "|wName|n", "|wType|n", "|wMembers|n", "|wLeader|n",
            border="cells", width=78
        )
        
        for group in groups:
            member_count = group.get_member_count()
            leader_name = group.leader.name if group.leader else "None"
            
            table.add_row(
                f"#{group.group_id}",
                group.name,
                group.get_group_type_display(),
                str(member_count),
                leader_name
            )
        
        self.caller.msg(str(table))
    
    def view_group(self, group_id):
        """View detailed information about a group."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check access
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_member = group.is_member(self.caller)
        is_leader = group.leader == self.caller
        
        if not group.is_public and not is_staff and not is_member:
            self.caller.msg(f"Group #{group_id} is private and you don't have access to view it.")
            return
        
        # Build output
        output = [f"|y{group.name}|n (#{group.group_id})"]
        output.append(f"Type: {group.get_group_type_display()}")
        output.append(f"Leader: {group.leader.name if group.leader else 'None'}")
        output.append("")
        
        if group.description:
            output.append("|wDescription:|n")
            output.append(group.description)
            output.append("")
        
        # Members
        members = group.members
        if members:
            output.append("|wMembers:|n")
            for member in members:
                member_line = f"  {member.name}"
                title = group.get_member_title(member)
                if title:
                    member_line += f" - {title}"
                if member == group.leader:
                    member_line += " |y(Leader)|n"
                output.append(member_line)
            output.append("")
        
        # Group merits
        merits = group.get_all_merits()
        if merits:
            output.append("|wGroup Merits:|n")
            for merit_name, rating in merits.items():
                dots = "•" * rating
                output.append(f"  {merit_name}: {dots} ({rating})")
            output.append("")
        
        # Totem info (if pack)
        if group.group_type == 'pack':
            totem_info = group.get_totem_info()
            if totem_info and totem_info.get('name'):
                totem_points = group.calculate_totem_points()
                output.append("|wTotem:|n")
                output.append(f"  {totem_info['name']} (Rank {'•' * totem_info['rank']})")
                if totem_info.get('concept'):
                    output.append(f"  {totem_info['concept']}")
                output.append(f"  {totem_points} totem points from pack members")
                if totem_info.get('advantage'):
                    adv = totem_info['advantage']
                    output.append(f"  Pack Advantage: {adv.get('type', 'Unknown').title()} - {adv.get('name', 'None')}")
                output.append("")
        
        # Mystery Cult benefits (if mysterycult)
        if group.group_type == 'mysterycult':
            benefits = group.get_all_mystery_benefits()
            has_benefits = any(benefits.get(level, {}).get('name') for level in range(1, 6))
            
            if has_benefits:
                output.append("|wMystery Cult Initiation Benefits:|n")
                for level in range(1, 6):
                    benefit = benefits.get(level, {})
                    if benefit.get('name'):
                        benefit_type = benefit.get('type', 'other').title()
                        benefit_name = benefit.get('name', '')
                        output.append(f"  Level {level} ({benefit_type}): {benefit_name}")
                output.append("  Use +mysterycult for full details")
                output.append("")
        
        # Cell Tactics (if cell)
        if group.group_type == 'cell':
            tactics = group.get_all_tactics()
            if tactics:
                output.append("|wKnown Tactics:|n")
                tactic_count = len(tactics)
                # Show first few tactics
                display_tactics = tactics[:5]
                for tactic in display_tactics:
                    output.append(f"  • {tactic}")
                if tactic_count > 5:
                    output.append(f"  ... and {tactic_count - 5} more")
                output.append(f"  Use +group/tactics {group.group_id} for full list")
                output.append("")
        
        # Private notes (if accessible)
        if group.notes and (is_staff or is_member):
            output.append("|wPrivate Notes:|n")
            output.append(group.notes)
        
        self.caller.msg("\n".join(output))
    
    def create_group(self, name):
        """Create a new group."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to create groups.")
            return
        
        # Check if group already exists
        if get_group_by_name(name):
            self.caller.msg(f"A group named '{name}' already exists.")
            return
        
        # Create the group using TypeClass function
        try:
            group = create_group(name=name, creator=self.caller)
            self.caller.msg(f"Created group '{name}' with ID #{group.group_id}.")
            self.caller.msg(f"Created channel '{group.channel_name}' for group.")
        except ValueError as e:
            self.caller.msg(f"Error creating group: {str(e)}")
    
    def destroy_group(self, group_id):
        """Destroy a group."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to destroy groups.")
            return
        
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Store info for messages
        group_name = group.name
        
        # Delete the group (handles all cleanup automatically)
        group.delete()
        
        self.caller.msg(f"Destroyed group '{group_name}' (ID #{group_id}).")
    
    def set_group_type(self, group_id, group_type):
        """Set the type of a group."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to set group types.")
            return
        
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        valid_types = [choice[0] for choice in Group.GROUP_TYPES]
        if group_type not in valid_types:
            self.caller.msg(f"Invalid group type. Valid types: {', '.join(valid_types)}")
            return
        
        try:
            group.group_type = group_type
            self.caller.msg(f"Set group '{group.name}' type to {group.get_group_type_display()}.")
        except ValueError as e:
            self.caller.msg(f"Error setting group type: {str(e)}")
    
    def set_leader(self, group_id, character_name):
        """Set the leader of a group."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to set group leaders.")
            return
        
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Find character
        character = search_character(self.caller, character_name)
        if not character:
            return
        
        # Set leader (TypeClass handles adding as member if needed)
        old_leader = group.leader.name if group.leader else "None"
        group.leader = character
        
        self.caller.msg(f"Set {character.name} as leader of '{group.name}' (was {old_leader}).")
    
    def set_description(self, group_id, description):
        """Set a group's description."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to set group descriptions.")
            return
        
        group.description = description
        self.caller.msg(f"Set description for group '{group.name}'.")
    
    def set_notes(self, group_id, notes):
        """Set a group's private notes."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to set group notes.")
            return
        
        group.notes = notes
        self.caller.msg(f"Set private notes for group '{group.name}'.")
    
    def set_title(self, group_id, character_name, title):
        """Set a character's title in a group."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to set member titles.")
            return
        
        # Find character
        character = search_character(self.caller, character_name)
        if not character:
            return
        
        # Check membership
        if not group.is_member(character):
            self.caller.msg(f"{character.name} is not a member of group '{group.name}'.")
            return
        
        old_title = group.get_member_title(character) or "None"
        if group.set_member_title(character, title):
            self.caller.msg(f"Set title for {character.name} in '{group.name}' to '{title}' (was '{old_title}').")
        else:
            self.caller.msg(f"Failed to set title for {character.name}.")
    
    def add_character(self, group_id, character_name):
        """Add a character to a group."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to add members to this group.")
            return
        
        # Find character
        character = search_character(self.caller, character_name)
        if not character:
            return
        
        # Use utility function to handle all assignment tasks
        if assign_character_to_group(character, group, auto_assigned=False):
            self.caller.msg(f"Added {character.name} to group '{group.name}' and channel '{group.channel_name}'.")
        else:
            self.caller.msg(f"{character.name} is already a member of '{group.name}'.")
    
    def remove_character(self, group_id, character_name):
        """Remove a character from a group."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to remove members from this group.")
            return
        
        # Find character
        character = search_character(self.caller, character_name)
        if not character:
            return
        
        # Check membership
        if not group.is_member(character):
            self.caller.msg(f"{character.name} is not a member of '{group.name}'.")
            return
        
        # Check if leader
        if group.leader == character:
            self.caller.msg(f"{character.name} is the leader. Set a new leader first.")
            return
        
        # Use utility function to handle all removal tasks
        if remove_character_from_group(character, group):
            self.caller.msg(f"Removed {character.name} from group '{group.name}' and channel '{group.channel_name}'.")
        else:
            self.caller.msg(f"Failed to remove {character.name} from group '{group.name}'.")
    
    def set_privacy(self, group_id, is_public):
        """Set a group as public or private."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to change group privacy.")
            return
        
        if group.is_public == is_public:
            self.caller.msg(f"Group '{group.name}' is already {'public' if is_public else 'private'}.")
            return
        
        group.is_public = is_public
        
        self.caller.msg(f"Set group '{group.name}' to {'public' if is_public else 'private'}.")
    
    def assign_auto_groups(self, character_name):
        """Manually trigger automatic group assignment for a character."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to assign automatic groups.")
            return
        
        # Find character
        character = search_character(self.caller, character_name)
        if not character:
            return
        
        try:
            assigned_groups = auto_assign_character_groups(character)
            if assigned_groups:
                self.caller.msg(f"Auto-assigned {character.name} to groups: {', '.join(assigned_groups)}")
                character.msg(f"You have been automatically assigned to the following groups: {', '.join(assigned_groups)}")
            else:
                self.caller.msg(f"No automatic group assignments made for {character.name}")
        except Exception as e:
            self.caller.msg(f"Error assigning groups: {str(e)}")

    def show_character_groups(self, character_name):
        """Show all groups a character belongs to."""
        # Find character
        character = search_character(self.caller, character_name)
        if not character:
            return
        
        # Get groups
        groups = get_character_groups(character)
        
        if not groups:
            self.caller.msg(f"{character.name} is not a member of any groups.")
            return
        
        # Create table
        table = evtable.EvTable(
            "|wGroup|n", "|wType|n", "|wTitle|n", "|wRole|n",
            border="cells", width=78
        )
        
        for group in groups:
            # Get membership info
            title = group.get_member_title(character)
            role = group.get_member_role(character)
            
            # Check if leader
            if group.leader == character:
                role = "Leader" if not role else f"Leader, {role}"
            
            table.add_row(
                group.name,
                group.get_group_type_display(),
                title,
                role
            )
        
        output = [f"|y{character.name}'s Group Memberships|n"]
        output.append(str(table))
        
        # Show character attributes
        if character.attributes.has('groups'):
            char_groups = character.attributes.get('groups', [])
            output.append("")
            output.append(f"|wCharacter Group Attributes:|n {', '.join(char_groups)}")
        
        self.caller.msg("\n".join(output))

    def sync_character_groups(self, character):
        """Sync a single character's group attributes."""
        from world.groups.utils import sync_character_group_attributes
        try:
            synced_groups = sync_character_group_attributes(character)
            return synced_groups
        except Exception as e:
            self.caller.msg(f"Error syncing {character.name}: {str(e)}")
            return []
    
    def sync_all_characters(self):
        """Sync all characters' group attributes."""
        from typeclasses.characters import Character
        from evennia.utils.search import search_object
        
        all_chars = search_object("", typeclass=Character)
        synced_count = 0
        
        self.caller.msg(f"Syncing group attributes for {len(all_chars)} characters...")
        
        for char in all_chars:
            try:
                synced_groups = self.sync_character_groups(char)
                if synced_groups:
                    synced_count += 1
                    self.caller.msg(f"  {char.name}: {', '.join(synced_groups)}")
            except Exception as e:
                self.caller.msg(f"  Error with {char.name}: {str(e)}")
        
        self.caller.msg(f"Completed. Synced {synced_count} characters.")

    def test_groups(self):
        if not self.args:
            self.caller.msg("Usage: +testgroups <character>")
            return
        
        # Find character
        character = search_character(self.caller, self.args.strip())
        if not character:
            return
        
        self.caller.msg(f"Testing group assignment for {character.name}")
        
        # Show character stats
        if hasattr(character, 'db') and character.db.stats:
            stats = character.db.stats
            other = stats.get('other', {})
            template = other.get('template', 'Unknown')
            self.caller.msg(f"Template: {template}")
            
            if template.lower() == 'vampire':
                clan = other.get('clan', 'Unknown')
                covenant = other.get('covenant', 'Unknown')
                self.caller.msg(f"Clan: {clan}, Covenant: {covenant}")
        
        # Test auto assignment
        try:
            assigned_groups = auto_assign_character_groups(character)
            if assigned_groups:
                self.caller.msg(f"Auto-assigned to groups: {', '.join(assigned_groups)}")
            else:
                self.caller.msg("No automatic group assignments made")
        except Exception as e:
            self.caller.msg(f"Error in assignment: {str(e)}")
            import traceback
            self.caller.msg(traceback.format_exc())
        
        # Show current groups
        try:
            current_groups = get_character_groups(character)
            if current_groups:
                group_names = [g.name for g in current_groups]
                self.caller.msg(f"Current groups: {', '.join(group_names)}")
            else:
                self.caller.msg("Not a member of any groups")
        except Exception as e:
            self.caller.msg(f"Error getting groups: {str(e)}")
        
        # Show attributes
        if character.attributes.has('groups'):
            attr_groups = character.attributes.get('groups', [])
            self.caller.msg(f"Group attributes: {', '.join(attr_groups)}")
        else:
            self.caller.msg("No group attributes set")

    def sync_channels(self):
        """Ensure all group channels exist with proper locks."""
        groups = get_all_groups()
        created_count = 0
        updated_count = 0
        
        self.caller.msg(f"Checking channels for {len(groups)} groups...")
        
        for group in groups:
            try:
                channel_name = group.channel_name
                channel = ChannelDB.objects.filter(db_key=channel_name).first()
                
                if not channel:
                    # Force recreation
                    group._create_group_channel()
                    created_count += 1
                    self.caller.msg(f"  Created channel for {group.name}")
                else:
                    # Check locks
                    expected_lock = (
                        f"control:perm(Admin);"
                        f"listen:group_member({group.group_id}) or perm(Admin);"
                        f"send:group_member({group.group_id}) or perm(Admin)"
                    )
                    if str(channel.locks) != expected_lock:
                        channel.locks.clear()
                        channel.locks.add(expected_lock)
                        updated_count += 1
                        self.caller.msg(f"  Updated locks for {group.name} channel")
            except Exception as e:
                self.caller.msg(f"  Error with {group.name}: {str(e)}")
        
        self.caller.msg(f"Completed. Created {created_count} new channels, updated {updated_count} locks.")
    
    def cleanup_orphaned_attributes(self):
        """Remove group attributes that don't correspond to actual memberships."""
        from typeclasses.characters import Character
        from evennia.utils.search import search_object
        
        all_chars = search_object("", typeclass=Character)
        cleaned_count = 0
        
        self.caller.msg(f"Cleaning up orphaned group attributes for {len(all_chars)} characters...")
        
        for char in all_chars:
            try:
                if char.attributes.has('groups'):
                    attr_groups = char.attributes.get('groups', [])
                    actual_groups = get_character_groups(char)
                    actual_group_names = [g.name for g in actual_groups]
                    
                    # Find orphaned attributes
                    orphaned = [g for g in attr_groups if g not in actual_group_names]
                    if orphaned:
                        # Update to only include actual memberships
                        char.attributes.add('groups', actual_group_names)
                        cleaned_count += 1
                        self.caller.msg(f"  {char.name}: Removed orphaned groups: {', '.join(orphaned)}")
                        
            except Exception as e:
                self.caller.msg(f"  Error with {char.name}: {str(e)}")
        
        self.caller.msg(f"Completed. Cleaned {cleaned_count} characters.")

    def func(self):
        """Execute the command."""
        if not self.args:
            if self.cmdstring == "+groups":
                self.list_groups()
                return
            
            self.caller.msg("Usage: +group <id> or +groups")
            return
        
        # Parse switches
        if self.switches:
            switch = self.switches[0]
            
            # Sync functionality (staff only)
            if switch == "sync":
                if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
                    self.caller.msg("You don't have permission to sync groups.")
                    return
                
                if self.args.strip():
                    # Sync specific character
                    character = search_character(self.caller, self.args.strip())
                    if not character:
                        return
                    
                    synced_groups = self.sync_character_groups(character)
                    if synced_groups:
                        self.caller.msg(f"Synced {character.name}: {', '.join(synced_groups)}")
                    else:
                        self.caller.msg(f"No groups found for {character.name}")
                else:
                    # Sync all characters
                    self.sync_all_characters()
                return
            
            if switch == "syncchannels":
                if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
                    self.caller.msg("You don't have permission to sync channels.")
                    return
                self.sync_channels()
                return
            
            if switch == "synccleanup":
                if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
                    self.caller.msg("You don't have permission to cleanup group data.")
                    return
                self.cleanup_orphaned_attributes()
                return
            
            if switch == "test":
                if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
                    self.caller.msg("You don't have permission to test groups.")
                    return
                self.test_groups()
                return
            
            # Mystery Cult template view
            if switch == "template":
                from world.groups.group_data import EXAMPLE_MYSTERY_CULTS
                
                template_name = self.args.strip().lower()
                
                output = ["|wExample Mystery Cults:|n"]
                output.append("")
                
                if template_name == "mammon" or template_name == "chosen of mammon":
                    cult = EXAMPLE_MYSTERY_CULTS['Chosen of Mammon']
                    output.append("|yChosen of Mammon|n")
                    output.append(cult['description'])
                    output.append("")
                    output.append("|wInitiation Benefits:|n")
                    for level, benefit in cult['benefits'].items():
                        output.append(f"  {level}: {benefit}")
                elif template_name == "sisters" or template_name == "machine gun" or template_name == "bomb":
                    cult = EXAMPLE_MYSTERY_CULTS['Sisters of the Machine Gun, Brothers of the Bomb']
                    output.append("|ySisters of the Machine Gun, Brothers of the Bomb|n")
                    output.append(cult['description'])
                    output.append("")
                    output.append("|wInitiation Benefits:|n")
                    for level, benefit in cult['benefits'].items():
                        output.append(f"  {level}: {benefit}")
                else:
                    output.append("Available templates:")
                    output.append("  mammon - Chosen of Mammon")
                    output.append("  sisters - Sisters of the Machine Gun, Brothers of the Bomb")
                
                self.caller.msg("\n".join(output))
                return
            
            # Mystery Cult check
            if switch == "check":
                if "=" not in self.args:
                    self.caller.msg("Usage: +group/check <id>=<character>")
                    return
                
                group_id, character_name = self.args.split("=", 1)
                try:
                    group_id = int(group_id.strip())
                except ValueError:
                    self.caller.msg("Group ID must be a number.")
                    return
                
                group = get_group_by_id(group_id)
                if not group:
                    self.caller.msg(f"Group #{group_id} does not exist.")
                    return
                
                if group.group_type != 'mysterycult':
                    self.caller.msg(f"Group '{group.name}' is not a Mystery Cult. Use +group/check only for Mystery Cult type groups.")
                    return
                
                character = search_character(self.caller, character_name.strip())
                if not character:
                    return
                
                if not group.is_member(character):
                    self.caller.msg(f"{character.name} is not a member of '{group.name}'.")
                    return
                
                benefits = group.get_character_mystery_benefits(character)
                
                output = [f"|wMystery Cult Benefits for {character.name}|n"]
                output.append(f"Cult: {group.name} (#{group.group_id})")
                output.append("")
                
                if not benefits:
                    output.append(f"{character.name} has no Mystery Cult Initiation merit or it is at 0 dots.")
                else:
                    output.append(f"|wBenefits {character.name} should have:|n")
                    for level, benefit in benefits:
                        benefit_type = benefit.get('type', 'other').title()
                        benefit_name = benefit.get('name', '')
                        benefit_desc = benefit.get('description', '')
                        
                        output.append(f"Level {level} ({benefit_type}): {benefit_name}")
                        if benefit_desc:
                            output.append(f"  {benefit_desc}")
                
                self.caller.msg("\n".join(output))
                return
            
            # Mystery Cult clear
            if switch == "clear":
                if "/" not in self.args:
                    self.caller.msg("Usage: +group/clear <id>/<level>")
                    return
                
                group_id, level_str = self.args.split("/", 1)
                
                try:
                    group_id = int(group_id.strip())
                    level = int(level_str.strip())
                except ValueError:
                    self.caller.msg("Group ID and level must be numbers.")
                    return
                
                group = get_group_by_id(group_id)
                if not group:
                    self.caller.msg(f"Group #{group_id} does not exist.")
                    return
                
                if group.group_type != 'mysterycult':
                    self.caller.msg(f"Group '{group.name}' is not a Mystery Cult. Use +group/clear only for Mystery Cult type groups.")
                    return
                
                is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
                is_leader = group.leader == self.caller
                
                if not is_staff and not is_leader:
                    self.caller.msg("You don't have permission to modify Mystery Cult benefits.")
                    return
                
                if group.clear_mystery_benefit(level):
                    self.caller.msg(f"Cleared Level {level} benefit for '{group.name}'.")
                else:
                    self.caller.msg("Failed to clear benefit. Level must be 1-5.")
                return
            
            # Cell Tactics
            if switch == "tactics":
                from world.groups.group_data import CELL_TACTICS
                
                # List all available tactics
                if "list" in self.switches:
                    output = ["|wAvailable Cell Tactics:|n"]
                    output.append("")
                    
                    # Group by type
                    investigation = []
                    physical = []
                    social = []
                    
                    for tactic_name, tactic_data in CELL_TACTICS.items():
                        tactic_type = tactic_data.get('type', 'other')
                        tactic_entry = f"|y{tactic_name}|n - {tactic_data['description'][:60]}..."
                        
                        if tactic_type == 'investigation':
                            investigation.append(tactic_entry)
                        elif tactic_type == 'physical':
                            physical.append(tactic_entry)
                        elif tactic_type == 'social':
                            social.append(tactic_entry)
                    
                    output.append("|wInvestigation Tactics:|n")
                    output.extend(investigation)
                    output.append("")
                    output.append("|wPhysical Tactics:|n")
                    output.extend(physical)
                    output.append("")
                    output.append("|wSocial Tactics:|n")
                    output.extend(social)
                    output.append("")
                    output.append("Use +group/tactics/add to add tactics to your cell.")
                    
                    self.caller.msg("\n".join(output))
                    return
                
                # Add tactic
                if "add" in self.switches:
                    if "=" not in self.args:
                        self.caller.msg("Usage: +group/tactics/add <id>=<tactic>")
                        return
                    
                    group_id, tactic_name = self.args.split("=", 1)
                    try:
                        group_id = int(group_id.strip())
                    except ValueError:
                        self.caller.msg("Group ID must be a number.")
                        return
                    
                    group = get_group_by_id(group_id)
                    if not group:
                        self.caller.msg(f"Group #{group_id} does not exist.")
                        return
                    
                    if group.group_type != 'cell':
                        self.caller.msg(f"Group '{group.name}' is not a Hunter cell. Use +group/tactics only for cells.")
                        return
                    
                    is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
                    is_leader = group.leader == self.caller
                    
                    if not is_staff and not is_leader:
                        self.caller.msg("You don't have permission to modify cell tactics.")
                        return
                    
                    tactic_name = tactic_name.strip()
                    
                    # Validate it's a real tactic
                    if tactic_name not in CELL_TACTICS:
                        self.caller.msg(f"Unknown tactic '{tactic_name}'. Use +group/tactics/list to see available tactics.")
                        return
                    
                    if group.add_tactic(tactic_name):
                        self.caller.msg(f"Added tactic '{tactic_name}' to cell '{group.name}'.")
                    else:
                        self.caller.msg(f"Cell '{group.name}' already knows the '{tactic_name}' tactic.")
                    return
                
                # Remove tactic
                if "rem" in self.switches:
                    if "=" not in self.args:
                        self.caller.msg("Usage: +group/tactics/rem <id>=<tactic>")
                        return
                    
                    group_id, tactic_name = self.args.split("=", 1)
                    try:
                        group_id = int(group_id.strip())
                    except ValueError:
                        self.caller.msg("Group ID must be a number.")
                        return
                    
                    group = get_group_by_id(group_id)
                    if not group:
                        self.caller.msg(f"Group #{group_id} does not exist.")
                        return
                    
                    if group.group_type != 'cell':
                        self.caller.msg(f"Group '{group.name}' is not a Hunter cell. Use +group/tactics only for cells.")
                        return
                    
                    is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
                    is_leader = group.leader == self.caller
                    
                    if not is_staff and not is_leader:
                        self.caller.msg("You don't have permission to modify cell tactics.")
                        return
                    
                    tactic_name = tactic_name.strip()
                    
                    if group.remove_tactic(tactic_name):
                        self.caller.msg(f"Removed tactic '{tactic_name}' from cell '{group.name}'.")
                    else:
                        self.caller.msg(f"Cell '{group.name}' doesn't know the '{tactic_name}' tactic.")
                    return
                
                # View tactics (no other switches)
                if not self.switches or self.switches == ['tactics']:
                    try:
                        group_id = int(self.args.strip())
                    except ValueError:
                        self.caller.msg("Group ID must be a number.")
                        return
                    
                    group = get_group_by_id(group_id)
                    if not group:
                        self.caller.msg(f"Group #{group_id} does not exist.")
                        return
                    
                    if group.group_type != 'cell':
                        self.caller.msg(f"Group '{group.name}' is not a Hunter cell. Use +group/tactics only for cells.")
                        return
                    
                    tactics = group.get_all_tactics()
                    
                    if not tactics:
                        self.caller.msg(f"Cell '{group.name}' has no tactics set.")
                        self.caller.msg("Use +group/tactics/add to add tactics, or +group/tactics/list to see available tactics.")
                        return
                    
                    output = [f"|wKnown Tactics for {group.name}|n (#{group.group_id})"]
                    output.append("")
                    
                    # Organize by type
                    investigation_tactics = []
                    physical_tactics = []
                    social_tactics = []
                    
                    for tactic_name in tactics:
                        if tactic_name in CELL_TACTICS:
                            tactic_data = CELL_TACTICS[tactic_name]
                            tactic_type = tactic_data.get('type', 'other')
                            
                            if tactic_type == 'investigation':
                                investigation_tactics.append(tactic_name)
                            elif tactic_type == 'physical':
                                physical_tactics.append(tactic_name)
                            elif tactic_type == 'social':
                                social_tactics.append(tactic_name)
                    
                    if investigation_tactics:
                        output.append("|wInvestigation Tactics:|n")
                        for tactic in investigation_tactics:
                            output.append(f"  • {tactic}")
                        output.append("")
                    
                    if physical_tactics:
                        output.append("|wPhysical Tactics:|n")
                        for tactic in physical_tactics:
                            output.append(f"  • {tactic}")
                        output.append("")
                    
                    if social_tactics:
                        output.append("|wSocial Tactics:|n")
                        for tactic in social_tactics:
                            output.append(f"  • {tactic}")
                        output.append("")
                    
                    output.append(f"Total: {len(tactics)} tactics")
                    
                    self.caller.msg("\n".join(output))
                    return
            
            # Auto assignment
            if switch == "auto":
                self.assign_auto_groups(self.args.strip())
                return
            
            # Show character groups
            if switch == "show":
                self.show_character_groups(self.args.strip())
                return
            
            # Create
            if switch == "create":
                self.create_group(self.args.strip())
                return
            
            # Destroy
            if switch == "destroy":
                try:
                    group_id = int(self.args.strip())
                    self.destroy_group(group_id)
                except ValueError:
                    self.caller.msg("Group ID must be a number.")
                return
            
            # Private/Public
            if switch in ["private", "public"]:
                try:
                    group_id = int(self.args.strip())
                    self.set_privacy(group_id, switch == "public")
                except ValueError:
                    self.caller.msg("Group ID must be a number.")
                return
            
            # Title (special format)
            if switch == "title":
                if "/" in self.args and "=" in self.args:
                    group_char, title = self.args.split("=", 1)
                    parts = group_char.split("/", 1)
                    
                    if len(parts) == 2:
                        try:
                            group_id = int(parts[0].strip())
                            character_name = parts[1].strip()
                            self.set_title(group_id, character_name, title.strip())
                        except ValueError:
                            self.caller.msg("Group ID must be a number.")
                        return
                
                self.caller.msg("Usage: +group/title <id>/<char>=<title>")
                return
            
            # Mystery Cult set (special format with level)
            if switch == "set":
                if "/" not in self.args or "=" not in self.args:
                    self.caller.msg("Usage: +group/set <id>/<level>=<type>:<name>[:<description>]")
                    return
                
                group_level, benefit_info = self.args.split("=", 1)
                parts = group_level.split("/", 1)
                
                if len(parts) != 2:
                    self.caller.msg("Usage: +group/set <id>/<level>=<type>:<name>[:<description>]")
                    return
                
                try:
                    group_id = int(parts[0].strip())
                    level = int(parts[1].strip())
                except ValueError:
                    self.caller.msg("Group ID and level must be numbers.")
                    return
                
                group = get_group_by_id(group_id)
                if not group:
                    self.caller.msg(f"Group #{group_id} does not exist.")
                    return
                
                if group.group_type != 'mysterycult':
                    self.caller.msg(f"Group '{group.name}' is not a Mystery Cult. Use +group/set only for Mystery Cult type groups.")
                    return
                
                is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
                is_leader = group.leader == self.caller
                
                if not is_staff and not is_leader:
                    self.caller.msg("You don't have permission to modify Mystery Cult benefits.")
                    return
                
                if level < 1 or level > 5:
                    self.caller.msg("Level must be between 1 and 5.")
                    return
                
                benefit_parts = benefit_info.split(":")
                if len(benefit_parts) < 2:
                    self.caller.msg("Usage: +group/set <id>/<level>=<type>:<name>[:<description>]")
                    self.caller.msg("Types: specialty, merit, skill, other")
                    return
                
                benefit_type = benefit_parts[0].strip()
                benefit_name = benefit_parts[1].strip()
                benefit_desc = benefit_parts[2].strip() if len(benefit_parts) > 2 else ''
                
                valid_types = ['specialty', 'merit', 'skill', 'other']
                if benefit_type.lower() not in valid_types:
                    self.caller.msg(f"Type must be one of: {', '.join(valid_types)}")
                    return
                
                if group.set_mystery_benefit(level, benefit_type, benefit_name, benefit_desc):
                    self.caller.msg(f"Set Level {level} benefit for '{group.name}': {benefit_type.title()} - {benefit_name}")
                else:
                    self.caller.msg("Failed to set benefit.")
                return
            
            # Commands with = format
            if "=" in self.args:
                group_id, value = self.args.split("=", 1)
                try:
                    group_id = int(group_id.strip())
                except ValueError:
                    self.caller.msg("Group ID must be a number.")
                    return
                
                value = value.strip()
                
                if switch == "type":
                    self.set_group_type(group_id, value)
                elif switch == "leader":
                    self.set_leader(group_id, value)
                elif switch == "desc":
                    self.set_description(group_id, value)
                elif switch == "note":
                    self.set_notes(group_id, value)
                elif switch == "add":
                    self.add_character(group_id, value)
                elif switch == "remove":
                    self.remove_character(group_id, value)
                else:
                    self.caller.msg(f"Unknown switch: {switch}")
                
                return
            
            self.caller.msg(f"Invalid format for switch '{switch}'.")
            return
        
        # View group
        try:
            group_id = int(self.args.strip())
            self.view_group(group_id)
        except ValueError:
            self.caller.msg("Group ID must be a number.") 

class CmdRoster(MuxCommand):
    """
    View the roster (member list) of a group.
    
    Usage:
        +roster                    - List all groups you can view rosters for
        +roster <group name>       - View the roster for a specific group
        +roster <group id>         - View the roster for a group by ID
        +roster/all                - List all public group rosters (staff only)
        
    This command shows both online and offline members of groups you have access to.
    You can view rosters for:
    - Public groups (anyone can view)
    - Private groups you're a member of
    - Any group (if you're staff)
    
    The roster shows member names, online status, group titles, and roles.
    """
    
    key = "+roster"
    locks = "cmd:all()"
    help_category = "Group Management"
    switch_options = ("all",)
    
    def list_available_groups(self):
        """List all groups the player can view rosters for."""
        # Get all public groups
        public_groups = get_public_groups()
        
        # Get private groups the player is a member of
        private_groups = []
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            all_groups = get_all_groups()
            private_groups = [g for g in all_groups if not g.is_public and g.is_member(self.caller)]
        else:
            # Staff can see all groups
            all_groups = get_all_groups()
            private_groups = [g for g in all_groups if not g.is_public]
        
        all_groups = list(public_groups) + list(private_groups)
        
        if not all_groups:
            self.caller.msg("No groups available to view rosters for.")
            return
        
        # Build output with consistent formatting
        output = []
        output.append(header("Available Group Rosters", width=78))
        output.append("|wID     Name                 Type          Access    Members|n")
        output.append("|r" + "-" * 78 + "|n")
        
        for group in all_groups:
            member_count = group.get_member_count()
            access_type = "Public" if group.is_public else "Private"
            
            # Format columns with proper spacing
            id_str = f"#{group.group_id}".ljust(6)
            name_str = crop(group.name, width=20).ljust(20)
            type_str = crop(group.get_group_type_display(), width=13).ljust(13)
            access_str = access_type.ljust(9)
            members_str = str(member_count)
            
            output.append(f" {id_str} {name_str} {type_str} {access_str} {members_str}")
        
        output.append("|r" + "-" * 78 + "|n")
        output.append("Use '+roster <name>' or '+roster <id>' to view a specific roster.")
        output.append(footer(width=78))
        
        self.caller.msg("\n".join(output))
    
    def view_group_roster(self, group_identifier):
        """View the roster for a specific group."""
        # Try to find group by ID first, then by name
        group = None
        try:
            group_id = int(group_identifier)
            group = get_group_by_id(group_id)
        except ValueError:
            # Try by name (case-insensitive)
            group = get_group_by_name(group_identifier)
        
        if not group:
            self.caller.msg(f"Group '{group_identifier}' not found.")
            return
        
        # Check access permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_member = group.is_member(self.caller)
        
        if not group.is_public and not is_staff and not is_member:
            self.caller.msg(f"Group '{group.name}' is private and you don't have access to view its roster.")
            return
        
        # Get all members for this group
        members = group.members
        
        if not members:
            self.caller.msg(f"Group '{group.name}' has no members.")
            return
        
        # Build output with consistent formatting
        output = []
        output.append(header(f"{group.name} Roster (#{group.group_id})", width=78))
        output.append(f"|wType:|n {group.get_group_type_display()}")
        output.append(f"|wAccess:|n {'Public' if group.is_public else 'Private'}")
        output.append(f"|wTotal Members:|n {len(members)}")
        
        if group.description:
            output.append("")
            output.append(f"|wDescription:|n {group.description}")
        
        output.append("")
        output.append("|wName              Status    Title         Role          Last Seen|n")
        output.append("|r" + "-" * 78 + "|n")
        
        for member in members:
            # Determine online status
            if member.has_account:
                status = "|gOnline|n"
                last_seen = "Now"
            else:
                status = "|rOffline|n"
                # Try to get last login time
                if hasattr(member, 'db') and member.db.last_login:
                    try:
                        last_login = member.db.last_login
                        if hasattr(last_login, 'strftime'):
                            last_seen = last_login.strftime("%Y-%m-%d")
                        else:
                            last_seen = str(last_login)[:10]  # First 10 chars if it's a string
                    except:
                        last_seen = "Unknown"
                else:
                    last_seen = "Unknown"
            
            # Get title and role
            title = group.get_member_title(member) or ""
            role = group.get_member_role(member) or ""
            
            # Check if leader
            if group.leader == member:
                if role:
                    role = f"Leader, {role}"
                else:
                    role = "Leader"
            
            # Format columns - use plain status string for spacing calculation
            name_str = crop(member.name, width=17).ljust(17)
            # Status is 8 chars visible ("Online" or "Offline") + ANSI codes
            status_display = status.ljust(17)  # Accounts for ANSI codes
            title_str = crop(title, width=13).ljust(13)
            role_str = crop(role, width=13).ljust(13)
            
            output.append(f" {name_str} {status_display} {title_str} {role_str} {last_seen}")
        
        # Show online count
        online_count = group.get_online_count()
        output.append("|r" + "-" * 78 + "|n")
        output.append(f"|wOnline Now:|n {online_count}/{len(members)} members")
        output.append(footer(width=78))
        
        self.caller.msg("\n".join(output))
    
    def list_all_rosters(self):
        """List all public group rosters (staff only)."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to view all rosters.")
            return
        
        groups = get_all_groups()
        
        if not groups:
            self.caller.msg("No groups exist.")
            return
        
        output = ["|wAll Group Rosters:|n"]
        
        for group in groups:
            members = group.members
            online_count = group.get_online_count()
            total_count = len(members)
            
            access_type = "Public" if group.is_public else "Private"
            output.append(f"|w{group.name}|n (#{group.group_id}) - {group.get_group_type_display()}")
            output.append(f"  {access_type} | {online_count}/{total_count} online | {total_count} total members")
            
            if total_count > 0:
                # Show online members
                online_members = [m.name for m in group.get_online_members()]
                if online_members:
                    output.append(f"  |gOnline:|n {', '.join(online_members)}")
                else:
                    output.append(f"  |rNo members currently online|n")
            
            output.append("")
        
        self.caller.msg("\n".join(output))
    
    def func(self):
        """Execute the command."""
        # Handle switches
        if "all" in self.switches:
            self.list_all_rosters()
            return
        
        # No arguments - list available groups
        if not self.args:
            self.list_available_groups()
            return
        
        # View specific group roster
        self.view_group_roster(self.args.strip())


class CmdGroupMerit(MuxCommand):
    """
    Manage group-specific merits.
    
    Usage:
        +groupmerit <group id>                  - View all merits for a group
        +groupmerit/set <group id>=<merit>:<rating> - Set a group merit (staff or leader)
        +groupmerit/remove <group id>=<merit>   - Remove a group merit (staff or leader)
        +groupmerit/list <group type>           - List available merits for a group type
        +groupmerit/calc <group id>             - Calculate merit contributions from members
        
    Group-specific merits vary by type:
    - Packs: Den, Directed Rage, Magnanimous Totem, Moon's Grace, Territorial Advantage
    - Krewes: Krewe Allies, Cenote, Krewe Contacts, Krewe Library, Krewe Resources, etc.
    - Cults: Cult Allies, Devotees, Fanatical, Ritualistic Cult, Secretive, Wayward Cult, etc.
    - Mystery Cults: Mystery Cult Initiation (with benefits at each level)
    - Cells: Safe Place, plus Cell Tactics for combat coordination
    - Motleys: Motley Hollow, Motley Workshop, Motley Token, Stable Trod, etc.
    - Cabals: (Mage groups - add cabal-specific merits as needed)
    
    Examples:
        +groupmerit 1
        +groupmerit/set 1=Den:3
        +groupmerit/remove 1=Den
        +groupmerit/list pack
    """
    
    key = "+groupmerit"
    aliases = ["+gmerit"]
    locks = "cmd:all()"
    help_category = "Group Management"
    
    def func(self):
        """Execute the command."""
        from world.groups.group_data import GROUP_TYPE_MERITS
        
        if not self.args and not self.switches:
            self.caller.msg("Usage: +groupmerit <group id> or use /list to see available merits")
            return
        
        # List available merits for a group type
        if "list" in self.switches:
            group_type = self.args.strip().lower()
            if group_type not in GROUP_TYPE_MERITS:
                self.caller.msg(f"Unknown group type. Available: {', '.join(GROUP_TYPE_MERITS.keys())}")
                return
            
            merits = GROUP_TYPE_MERITS[group_type]
            output = [f"|wAvailable Merits for {group_type.title()}:|n"]
            output.append("")
            
            for merit_name, merit_data in merits.items():
                rating_range = f"{'•' * merit_data['min']} to {'•' * merit_data['max']}"
                output.append(f"|y{merit_name}|n ({rating_range})")
                output.append(f"  {merit_data['description']}")
                if 'effects' in merit_data:
                    for rating, effect in merit_data['effects'].items():
                        output.append(f"  {rating} dots: {effect}")
                if 'prerequisites' in merit_data:
                    output.append(f"  Prerequisites: {', '.join(merit_data['prerequisites'])}")
                output.append(f"  Source: {merit_data['source']}")
                output.append("")
            
            self.caller.msg("\n".join(output))
            return
        
        # Get group
        try:
            group_id = int(self.args.split("=")[0].strip() if "=" in self.args else self.args.strip())
        except ValueError:
            self.caller.msg("Group ID must be a number.")
            return
        
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions for modifying commands
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        # View merits
        if not self.switches:
            merits = group.get_all_merits()
            
            if not merits:
                self.caller.msg(f"Group '{group.name}' has no merits set.")
                return
            
            output = [f"|wMerits for {group.name}|n (#{group.group_id})"]
            output.append("")
            
            for merit_name, rating in merits.items():
                dots = "•" * rating
                output.append(f"{merit_name}: {dots} ({rating})")
            
            self.caller.msg("\n".join(output))
            return
        
        # Set merit
        if "set" in self.switches:
            if not is_staff and not is_leader:
                self.caller.msg("You don't have permission to set group merits.")
                return
            
            if "=" not in self.args:
                self.caller.msg("Usage: +groupmerit/set <group id>=<merit>:<rating>")
                return
            
            _, merit_info = self.args.split("=", 1)
            if ":" not in merit_info:
                self.caller.msg("Usage: +groupmerit/set <group id>=<merit>:<rating>")
                return
            
            merit_name, rating = merit_info.split(":", 1)
            merit_name = merit_name.strip()
            
            try:
                rating = int(rating.strip())
            except ValueError:
                self.caller.msg("Rating must be a number.")
                return
            
            if rating < 0 or rating > 5:
                self.caller.msg("Rating must be between 0 and 5.")
                return
            
            group.set_merit(merit_name, rating)
            self.caller.msg(f"Set {merit_name} to {rating} dots for group '{group.name}'.")
            return
        
        # Remove merit
        if "remove" in self.switches:
            if not is_staff and not is_leader:
                self.caller.msg("You don't have permission to remove group merits.")
                return
            
            if "=" not in self.args:
                self.caller.msg("Usage: +groupmerit/remove <group id>=<merit>")
                return
            
            _, merit_name = self.args.split("=", 1)
            merit_name = merit_name.strip()
            
            group.remove_merit(merit_name)
            self.caller.msg(f"Removed {merit_name} from group '{group.name}'.")
            return
        
        # Calculate contributions
        if "calc" in self.switches:
            # Show which members contribute to group merits via their character sheets
            output = [f"|wMerit Contributions for {group.name}|n"]
            output.append("")
            
            for member in group.members:
                if hasattr(member, 'db') and member.db.stats:
                    merits = member.db.stats.get('merits', {})
                    relevant_merits = []
                    
                    # Check for merits that might contribute to group
                    for merit_name, merit_value in merits.items():
                        rating = 0
                        
                        # Check for dict-like attributes (works with dict and _SaverDict)
                        if hasattr(merit_value, '__getitem__') and hasattr(merit_value, 'keys'):
                            # Try 'dots' first, then 'rating'
                            if 'dots' in merit_value:
                                rating = merit_value['dots']
                            elif 'rating' in merit_value:
                                rating = merit_value['rating']
                        else:
                            rating = merit_value
                        
                        # Convert to int safely
                        try:
                            rating = int(rating)
                        except (ValueError, TypeError):
                            continue
                        
                        # Check both capitalized and lowercase merit names
                        merit_lower = merit_name.lower()
                        if rating > 0 and merit_lower in ['totem', 'den', 'safe place', 'cult']:
                            relevant_merits.append(f"{merit_name.title()} {rating}")
                    
                    if relevant_merits:
                        output.append(f"{member.name}: {', '.join(relevant_merits)}")
            
            if len(output) == 2:
                output.append("No members have relevant merits.")
            
            self.caller.msg("\n".join(output))
            return


class CmdTotem(MuxCommand):
    """
    Manage pack totems (for werewolf packs).
    
    Usage:
        +totem <group id>                       - View totem information
        +totem/name <group id>=<name>           - Set totem name (staff or leader)
        +totem/concept <group id>=<concept>     - Set totem concept (staff or leader)
        +totem/aspiration <group id>=<text>     - Set totem aspiration (staff or leader)
        +totem/ban <group id>=<text>            - Set totem ban (staff or leader)
        +totem/attr <group id>=<power>/<finesse>/<resistance> - Set totem attributes (staff or leader)
        +totem/influence <group id>=<type>:<dots> - Set totem influence (staff or leader)
        +totem/numen/add <group id>=<numen>     - Add a numen (staff or leader)
        +totem/numen/remove <group id>=<numen>  - Remove a numen (staff or leader)
        +totem/numen/list                       - List available numina
        +totem/advantage <group id>=<type>:<name>:<rating> - Set pack advantage (staff or leader)
        +totem/calc <group id>                  - Calculate totem points from members
        +totem/calc/debug <group id>            - Calculate with detailed debug output
        +totem/notes <group id>=<text>          - Set totem notes (staff or leader)
        
    The totem is built from the combined Totem merit dots of pack members.
    Total totem points determine attributes, rank, and advantages granted to the pack.
    
    Examples:
        +totem 1
        +totem/name 1=Silver Wind
        +totem/concept 1=Swift storm spirit
        +totem/attr 1=3/4/2
        +totem/numen/add 1=Speed
        +totem/advantage 1=attribute:Dexterity:1
    """
    
    key = "+totem"
    locks = "cmd:all()"
    help_category = "Group Management"
    
    def func(self):
        """Execute the command."""
        from world.groups.group_data import (
            SPIRIT_NUMINA, get_advantage_experience, get_numina_count,
            MAX_ESSENCE_BY_RANK, get_rank_from_attributes
        )
        
        if not self.args and not self.switches:
            self.caller.msg("Usage: +totem <group id> or use /calc to calculate totem points")
            return
        
        # List numina
        if "numen" in self.switches and "list" in self.switches:
            output = ["|wAvailable Spirit Numina:|n"]
            output.append("")
            
            for numen_name, numen_data in SPIRIT_NUMINA.items():
                cost = numen_data.get('cost', 'Variable')
                output.append(f"|y{numen_name}|n")
                output.append(f"  Cost: {cost}")
                output.append(f"  {numen_data['description']}")
                if 'prerequisites' in numen_data:
                    output.append(f"  Prerequisites: {', '.join(numen_data['prerequisites'])}")
                if numen_data.get('reaching'):
                    output.append(f"  |c(Reaching)|n")
                output.append("")
                
                # Break into pages if too long
                if len(output) > 40:
                    self.caller.msg("\n".join(output))
                    output = []
            
            if output:
                self.caller.msg("\n".join(output))
            return
        
        # Get group
        try:
            group_id = int(self.args.split("=")[0].strip() if "=" in self.args else self.args.strip())
        except ValueError:
            self.caller.msg("Group ID must be a number.")
            return
        
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        # Calculate totem points
        if "calc" in self.switches:
            # Enable debug if requested
            debug_mode = "debug" in self.switches
            totem_points = group.calculate_totem_points(debug=debug_mode)
            available_exp = get_advantage_experience(totem_points)
            max_numina = get_numina_count(totem_points)
            
            output = [f"|wTotem Points for {group.name}|n"]
            output.append("")
            output.append(f"Total Totem Points: {totem_points}")
            output.append(f"Available Advantage Experiences: {available_exp}")
            output.append(f"Maximum Numina: {max_numina}")
            output.append("")
            output.append("|wMember Contributions:|n")
            if debug_mode:
                output.append("(Debug mode enabled - check server logs)")
            
            for member in group.members:
                if debug_mode:
                    output.append(f"  Checking {member.name}...")
                
                if not hasattr(member, 'db'):
                    if debug_mode:
                        output.append(f"    No db attribute")
                    continue
                
                if not member.db.stats:
                    if debug_mode:
                        output.append(f"    No stats")
                    continue
                
                merits = member.db.stats.get('merits', {})
                if debug_mode:
                    output.append(f"    Merit keys: {list(merits.keys())}")
                
                # Try both capitalized and lowercase versions
                totem_merit = merits.get('Totem')
                if totem_merit is None:
                    totem_merit = merits.get('totem')
                
                if totem_merit is None:
                    if debug_mode:
                        output.append(f"    No totem merit found")
                    continue
                
                if debug_mode:
                    output.append(f"    Found totem merit: {type(totem_merit)}")
                    if hasattr(totem_merit, 'keys'):
                        output.append(f"    Merit dict keys: {list(totem_merit.keys())}")
                
                # Extract the numeric value
                totem_value = 0
                # Check for dict-like attributes (works with dict and _SaverDict)
                if hasattr(totem_merit, '__getitem__') and hasattr(totem_merit, 'keys'):
                    # Try 'dots' first (your system)
                    if 'dots' in totem_merit:
                        totem_value = totem_merit['dots']
                        if debug_mode:
                            output.append(f"    Using 'dots': {totem_value} (type: {type(totem_value)})")
                    # Then try 'rating' (fallback)
                    elif 'rating' in totem_merit:
                        totem_value = totem_merit['rating']
                        if debug_mode:
                            output.append(f"    Using 'rating': {totem_value}")
                else:
                    totem_value = totem_merit
                    if debug_mode:
                        output.append(f"    Using direct value: {totem_value}")
                
                try:
                    totem_value = int(totem_value)
                    if totem_value > 0:
                        output.append(f"  {member.name}: {totem_value} dots")
                except (ValueError, TypeError) as e:
                    if debug_mode:
                        output.append(f"    ERROR converting to int: {e}")
                    continue
            
            self.caller.msg("\n".join(output))
            return
        
        # View totem
        if not self.switches:
            totem_info = group.get_totem_info()
            
            if not totem_info or not totem_info.get('name'):
                self.caller.msg(f"Group '{group.name}' does not have a totem set up yet.")
                self.caller.msg("Use +totem/name to begin setting up the totem.")
                return
            
            totem_points = group.calculate_totem_points()
            attrs = totem_info['attributes']
            total_attrs = sum(attrs.values())
            rank = totem_info['rank']
            
            # Calculate derived stats
            corpus = attrs['power'] + attrs['resistance']
            willpower = attrs['finesse'] + attrs['resistance']
            defense = min(attrs['finesse'], attrs['resistance'])
            initiative = attrs['finesse'] + attrs['resistance']
            
            output = [f"|y{totem_info['name']}|n"]
            output.append(f"Totem for {group.name} (#{group.group_id})")
            output.append("")
            
            if totem_info.get('concept'):
                output.append(f"|wConcept:|n {totem_info['concept']}")
            
            if totem_info.get('aspiration'):
                output.append(f"|wAspiration:|n {totem_info['aspiration']}")
            
            if totem_info.get('ban'):
                output.append(f"|wBan:|n {totem_info['ban']}")
            
            output.append("")
            output.append(f"|wRank:|n {'•' * rank} ({rank})")
            output.append(f"|wTotem Points:|n {totem_points}")
            output.append("")
            
            output.append("|wAttributes:|n")
            output.append(f"  Power: {attrs['power']}")
            output.append(f"  Finesse: {attrs['finesse']}")
            output.append(f"  Resistance: {attrs['resistance']}")
            output.append(f"  Total: {total_attrs}")
            output.append("")
            
            output.append("|wDerived Stats:|n")
            output.append(f"  Corpus: {corpus}")
            output.append(f"  Willpower: {willpower}")
            output.append(f"  Defense: {defense}")
            output.append(f"  Initiative: {initiative}")
            output.append(f"  Essence: {totem_info['essence']['current']}/{totem_info['essence']['max']}")
            output.append("")
            
            if totem_info.get('influence'):
                output.append("|wInfluence:|n")
                for inf_type, dots in totem_info['influence'].items():
                    output.append(f"  {inf_type}: {'•' * dots} ({dots})")
                output.append("")
            
            if totem_info.get('numina'):
                output.append("|wNumina:|n")
                for numen in totem_info['numina']:
                    output.append(f"  • {numen}")
                max_numina = get_numina_count(totem_points)
                output.append(f"  ({len(totem_info['numina'])}/{max_numina} numina)")
                output.append("")
            
            if totem_info.get('advantage'):
                adv = totem_info['advantage']
                output.append("|wPack Advantage:|n")
                output.append(f"  {adv.get('type', 'Unknown').title()}: {adv.get('name', 'None')}")
                if adv.get('rating', 0) > 1:
                    output.append(f"  Rating: {adv.get('rating')}")
                output.append("")
            
            if totem_info.get('notes'):
                output.append("|wNotes:|n")
                output.append(totem_info['notes'])
            
            self.caller.msg("\n".join(output))
            return
        
        # Modification commands require permission
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to modify the totem.")
            return
        
        # Set name
        if "name" in self.switches:
            if "=" not in self.args:
                self.caller.msg("Usage: +totem/name <group id>=<name>")
                return
            
            _, name = self.args.split("=", 1)
            group.set_totem_property('name', name.strip())
            self.caller.msg(f"Set totem name to '{name.strip()}' for group '{group.name}'.")
            return
        
        # Set concept
        if "concept" in self.switches:
            if "=" not in self.args:
                self.caller.msg("Usage: +totem/concept <group id>=<concept>")
                return
            
            _, concept = self.args.split("=", 1)
            group.set_totem_property('concept', concept.strip())
            self.caller.msg(f"Set totem concept for group '{group.name}'.")
            return
        
        # Set aspiration
        if "aspiration" in self.switches:
            if "=" not in self.args:
                self.caller.msg("Usage: +totem/aspiration <group id>=<text>")
                return
            
            _, aspiration = self.args.split("=", 1)
            group.set_totem_property('aspiration', aspiration.strip())
            self.caller.msg(f"Set totem aspiration for group '{group.name}'.")
            return
        
        # Set ban
        if "ban" in self.switches:
            if "=" not in self.args:
                self.caller.msg("Usage: +totem/ban <group id>=<text>")
                return
            
            _, ban = self.args.split("=", 1)
            group.set_totem_property('ban', ban.strip())
            self.caller.msg(f"Set totem ban for group '{group.name}'.")
            return
        
        # Set attributes
        if "attr" in self.switches:
            if "=" not in self.args:
                self.caller.msg("Usage: +totem/attr <group id>=<power>/<finesse>/<resistance>")
                return
            
            _, attr_string = self.args.split("=", 1)
            parts = attr_string.split("/")
            
            if len(parts) != 3:
                self.caller.msg("Usage: +totem/attr <group id>=<power>/<finesse>/<resistance>")
                return
            
            try:
                power = int(parts[0].strip())
                finesse = int(parts[1].strip())
                resistance = int(parts[2].strip())
            except ValueError:
                self.caller.msg("Attributes must be numbers.")
                return
            
            totem_points = group.calculate_totem_points()
            total_attrs = power + finesse + resistance
            
            if total_attrs > totem_points:
                self.caller.msg(f"Total attributes ({total_attrs}) cannot exceed totem points ({totem_points}).")
                return
            
            # Check that no single attribute has more than half the total
            if power > totem_points // 2 or finesse > totem_points // 2 or resistance > totem_points // 2:
                self.caller.msg(f"No single attribute can have more than half the total totem points ({totem_points // 2}).")
                return
            
            # Each attribute must have at least 1
            if power < 1 or finesse < 1 or resistance < 1:
                self.caller.msg("Each attribute must have at least 1 dot.")
                return
            
            group.set_totem_attribute('power', power)
            group.set_totem_attribute('finesse', finesse)
            group.set_totem_attribute('resistance', resistance)
            
            self.caller.msg(f"Set totem attributes for '{group.name}': Power {power}, Finesse {finesse}, Resistance {resistance}")
            return
        
        # Set influence
        if "influence" in self.switches:
            if "=" not in self.args or ":" not in self.args:
                self.caller.msg("Usage: +totem/influence <group id>=<type>:<dots>")
                return
            
            _, influence_info = self.args.split("=", 1)
            influence_type, dots = influence_info.split(":", 1)
            
            try:
                dots = int(dots.strip())
            except ValueError:
                self.caller.msg("Dots must be a number.")
                return
            
            if dots < 1 or dots > 5:
                self.caller.msg("Influence dots must be between 1 and 5.")
                return
            
            group.set_totem_influence(influence_type.strip(), dots)
            self.caller.msg(f"Set totem influence {influence_type.strip()} to {dots} dots for group '{group.name}'.")
            return
        
        # Add numen
        if "numen" in self.switches and "add" in self.switches:
            if "=" not in self.args:
                self.caller.msg("Usage: +totem/numen/add <group id>=<numen>")
                return
            
            _, numen_name = self.args.split("=", 1)
            numen_name = numen_name.strip()
            
            # Check if it's a valid numen
            if numen_name not in SPIRIT_NUMINA:
                self.caller.msg(f"Unknown numen '{numen_name}'. Use +totem/numen/list to see available numina.")
                return
            
            # Check if we've reached the limit
            totem_points = group.calculate_totem_points()
            max_numina = get_numina_count(totem_points)
            totem_info = group.get_totem_info()
            current_numina = len(totem_info.get('numina', [])) if totem_info else 0
            
            if current_numina >= max_numina:
                self.caller.msg(f"Totem already has maximum numina ({max_numina}) for {totem_points} totem points.")
                return
            
            group.add_totem_numen(numen_name)
            self.caller.msg(f"Added numen '{numen_name}' to totem for group '{group.name}'.")
            return
        
        # Remove numen
        if "numen" in self.switches and "remove" in self.switches:
            if "=" not in self.args:
                self.caller.msg("Usage: +totem/numen/remove <group id>=<numen>")
                return
            
            _, numen_name = self.args.split("=", 1)
            group.remove_totem_numen(numen_name.strip())
            self.caller.msg(f"Removed numen '{numen_name.strip()}' from totem for group '{group.name}'.")
            return
        
        # Set advantage
        if "advantage" in self.switches:
            if "=" not in self.args or self.args.count(":") < 1:
                self.caller.msg("Usage: +totem/advantage <group id>=<type>:<name>[:<rating>]")
                self.caller.msg("Types: attribute, skill, specialty, merit")
                return
            
            _, adv_info = self.args.split("=", 1)
            parts = adv_info.split(":")
            
            if len(parts) < 2:
                self.caller.msg("Usage: +totem/advantage <group id>=<type>:<name>[:<rating>]")
                return
            
            adv_type = parts[0].strip().lower()
            adv_name = parts[1].strip()
            adv_rating = 1
            
            if len(parts) >= 3:
                try:
                    adv_rating = int(parts[2].strip())
                except ValueError:
                    self.caller.msg("Rating must be a number.")
                    return
            
            if adv_type not in ['attribute', 'skill', 'specialty', 'merit']:
                self.caller.msg("Type must be: attribute, skill, specialty, or merit")
                return
            
            group.set_totem_advantage(adv_type, adv_name, adv_rating)
            self.caller.msg(f"Set pack advantage to {adv_type} '{adv_name}' (rating {adv_rating}) for group '{group.name}'.")
            return
        
        # Set notes
        if "notes" in self.switches:
            if "=" not in self.args:
                self.caller.msg("Usage: +totem/notes <group id>=<text>")
                return
            
            _, notes = self.args.split("=", 1)
            group.set_totem_property('notes', notes.strip())
            self.caller.msg(f"Set totem notes for group '{group.name}'.")
            return