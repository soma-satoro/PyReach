"""
Commands for managing Storyteller flags and permissions.

Storytellers are trusted players who can run stories and manage NPCs
without needing full staff permissions.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable, search
from world.utils.permission_utils import check_admin_permission, check_storyteller_permission


class CmdStoryteller(MuxCommand):
    """
    Manage Storyteller flags for players.
    
    Usage:
        +storyteller/list - List all current storytellers
        +storyteller/add <character> - Grant Storyteller flag
        +storyteller/remove <character> - Remove Storyteller flag
        +storyteller/check [character] - Check if character has Storyteller flag
        +storyteller/info - Show information about Storyteller permissions
        
    Storyteller Permissions:
        - Create and manage mysteries
        - Create and control NPCs
        - Use building commands in designated areas
        - Access storytelling tools
        
    Only Admin+ can grant or remove Storyteller flags.
    
    Examples:
        +storyteller/add Alice
        +storyteller/remove Bob
        +storyteller/check Alice
        +storyteller/list
    """
    
    key = "+storyteller"
    aliases = ["+st", "+storytellers"]
    help_category = "Admin Commands"
    locks = "cmd:perm(Admin)"
    
    def func(self):
        """Execute the command."""
        if not self.switches:
            self.show_info()
            return
            
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_storytellers()
        elif switch == "add":
            self.add_storyteller()
        elif switch == "remove":
            self.remove_storyteller()
        elif switch == "check":
            self.check_storyteller()
        elif switch == "info":
            self.show_info()
        else:
            self.caller.msg("Invalid switch. Use +storyteller without arguments for help.")
    
    def show_info(self):
        """Show information about Storyteller permissions."""
        info_text = """
|c+storyteller|n - Storyteller Management System

|yWhat is a Storyteller?|n
Storytellers are trusted players who can run stories and manage game content
without needing full staff permissions. They have access to specialized tools
for creating engaging roleplay experiences.

|yStoryteller Permissions:|n
• |wMystery System|n - Create and manage investigation mysteries
• |wNPC Management|n - Create, control, and manage NPCs
• |wStory Tools|n - Access to various storytelling commands
• |wBuilding Access|n - Limited building permissions in designated areas

|yCommands Available:|n
  |w+storyteller/list|n - List all current storytellers
  |w+storyteller/add <character>|n - Grant Storyteller flag (Admin only)
  |w+storyteller/remove <character>|n - Remove Storyteller flag (Admin only)
  |w+storyteller/check [character]|n - Check Storyteller status

|yFor Storytellers:|n
Once you have the Storyteller flag, you can use:
• |w+mystery|n commands to create investigations
• |w+npc|n commands to manage NPCs
• |w+clueobj|n commands to place discoverable clues
• Various other storytelling tools

|yNote:|n Only Admins can grant or remove Storyteller flags.
        """
        self.caller.msg(info_text)
    
    def list_storytellers(self):
        """List all current storytellers."""
        from evennia.objects.models import ObjectDB
        
        # Find all characters with storyteller flag
        storytellers = []
        
        # Check characters
        characters = ObjectDB.objects.filter(db_typeclass_path__icontains="characters")
        for char in characters:
            if hasattr(char, 'db') and char.db.storyteller:
                storytellers.append(char)
        
        # Check accounts (if they have storyteller flag)
        from evennia.accounts.models import AccountDB
        accounts = AccountDB.objects.all()
        for account in accounts:
            if hasattr(account, 'db') and account.db.storyteller:
                # Find their active character if any
                if account.character:
                    storytellers.append(account.character)
        
        # Remove duplicates
        storytellers = list(set(storytellers))
        
        if not storytellers:
            self.caller.msg("No storytellers are currently active.")
            return
        
        table = evtable.EvTable(
            "|cCharacter|n", "|cAccount|n", "|cOnline|n", "|cLast Login|n",
            border="table", align="l"
        )
        
        for char in storytellers:
            account_name = char.account.key if char.account else "None"
            online_status = "Yes" if char.sessions.all() else "No"
            
            # Get last login time
            if char.account:
                last_login = char.account.last_login.strftime('%Y-%m-%d %H:%M') if char.account.last_login else "Never"
            else:
                last_login = "Unknown"
            
            table.add_row(
                char.name,
                account_name,
                online_status,
                last_login
            )
        
        self.caller.msg(f"|cActive Storytellers:|n\n{table}")
    
    def add_storyteller(self):
        """Grant Storyteller flag to a character."""
        if not check_admin_permission(self.caller):
            self.caller.msg("Only Admins can grant Storyteller flags.")
            return
        
        if not self.args:
            self.caller.msg("Usage: +storyteller/add <character>")
            return
        
        target = self.caller.search(self.args.strip(), global_search=True)
        if not target:
            return
        
        # Handle both single object and list returns from search
        if isinstance(target, list):
            if not target:
                return
            target = target[0]
        
        # Check if it's a character
        if not hasattr(target, 'db') or not hasattr(target, 'account'):
            self.caller.msg("Target must be a player character.")
            return
        
        # Check if already a storyteller
        if check_storyteller_permission(target):
            self.caller.msg(f"{target.name} already has Storyteller permissions.")
            return
        
        # Grant the flag
        target.db.storyteller = True
        
        # Also set it on the account for persistence
        if target.account:
            target.account.db.storyteller = True
        
        # Log the action
        self.caller.msg(f"|gGranted Storyteller flag to {target.name}.|n")
        
        # Notify the target if online
        if target.sessions.all():
            target.msg(f"|yYou have been granted Storyteller permissions by {self.caller.name}!|n")
            target.msg(f"|yYou can now use +mystery, +npc, and other storytelling commands.|n")
            target.msg(f"|yUse +storyteller/info to see your new permissions.|n")
        
        # Notify other staff
        from evennia.utils.utils import make_iter
        staff_accounts = [acc for acc in search.search_account("*") 
                         if acc.check_permstring("staff") or acc.check_permstring("admin")]
        
        for staff in staff_accounts:
            if staff.character and staff.character != self.caller and staff.character.sessions.all():
                staff.character.msg(f"|ySTAFF:|n {self.caller.name} granted Storyteller to {target.name}")
    
    def remove_storyteller(self):
        """Remove Storyteller flag from a character."""
        if not check_admin_permission(self.caller):
            self.caller.msg("Only Admins can remove Storyteller flags.")
            return
        
        if not self.args:
            self.caller.msg("Usage: +storyteller/remove <character>")
            return
        
        target = self.caller.search(self.args.strip(), global_search=True)
        if not target:
            return
        
        # Handle both single object and list returns from search
        if isinstance(target, list):
            if not target:
                return
            target = target[0]
        
        # Check if it's a character
        if not hasattr(target, 'db') or not hasattr(target, 'account'):
            self.caller.msg("Target must be a player character.")
            return
        
        # Check if they have storyteller permissions
        if not check_storyteller_permission(target):
            self.caller.msg(f"{target.name} does not have Storyteller permissions.")
            return
        
        # Remove the flag
        target.db.storyteller = False
        
        # Also remove from account
        if target.account:
            target.account.db.storyteller = False
        
        # Log the action
        self.caller.msg(f"|rRemoved Storyteller flag from {target.name}.|n")
        
        # Notify the target if online
        if target.sessions.all():
            target.msg(f"|rYour Storyteller permissions have been removed by {self.caller.name}.|n")
            target.msg(f"|rYou no longer have access to storytelling commands.|n")
        
        # Notify other staff
        staff_accounts = [acc for acc in search.search_account("*") 
                         if acc.check_permstring("staff") or acc.check_permstring("admin")]
        
        for staff in staff_accounts:
            if staff.character and staff.character != self.caller and staff.character.sessions.all():
                staff.character.msg(f"|ySTAFF:|n {self.caller.name} removed Storyteller from {target.name}")
    
    def check_storyteller(self):
        """Check if a character has Storyteller permissions."""
        if self.args:
            target = self.caller.search(self.args.strip(), global_search=True)
            if not target:
                return
            
            # Handle both single object and list returns from search
            if isinstance(target, list):
                if not target:
                    return
                target = target[0]
        else:
            target = self.caller
        
        has_storyteller = check_storyteller_permission(target)
        has_staff = target.check_permstring("staff") or target.check_permstring("admin") or target.check_permstring("builders")
        
        output = [f"|cStoryteller Status for {target.name}:|n"]
        
        if has_staff:
            output.append(f"|gStaff Permissions:|n Yes (inherits all storyteller permissions)")
        elif has_storyteller:
            output.append(f"|gStoryteller Flag:|n Yes")
        else:
            output.append(f"|rStoryteller Flag:|n No")
        
        if has_storyteller or has_staff:
            output.append("")
            output.append("|yAvailable Commands:|n")
            output.append("• +mystery - Create and manage investigation mysteries")
            output.append("• +npc - Create and control NPCs")
            output.append("• +clueobj - Place discoverable clue objects")
            output.append("• Various other storytelling tools")
        
        self.caller.msg("\n".join(output))


class CmdStorytellerWho(MuxCommand):
    """
    Quick command to see who has storytelling permissions online.
    
    Usage:
        +stwho
        
    Shows all online storytellers and staff members.
    """
    
    key = "+stwho"
    aliases = ["+storytellerwho"]
    help_category = "Information"
    locks = "cmd:all()"
    
    def func(self):
        """Execute the command."""
        from evennia.objects.models import ObjectDB
        
        online_storytellers = []
        online_staff = []
        
        # Check all online sessions
        from evennia.server.sessionhandler import SESSIONS
        for session in SESSIONS.get_sessions():
            if session.character:
                char = session.character
                
                # Check if staff
                if (char.check_permstring("staff") or 
                    char.check_permstring("admin") or 
                    char.check_permstring("builders")):
                    online_staff.append(char)
                # Check if storyteller (but not staff)
                elif check_storyteller_permission(char):
                    online_storytellers.append(char)
        
        output = ["|cOnline Story Staff:|n"]
        
        if online_staff:
            output.append(f"|yStaff ({len(online_staff)}):|n")
            for char in online_staff:
                idle_time = char.idle_time
                if idle_time < 60:
                    idle_str = f"{int(idle_time)}s"
                elif idle_time < 3600:
                    idle_str = f"{int(idle_time/60)}m"
                else:
                    idle_str = f"{int(idle_time/3600)}h"
                output.append(f"  {char.name} (idle {idle_str})")
        
        if online_storytellers:
            output.append(f"|yStorytellers ({len(online_storytellers)}):|n")
            for char in online_storytellers:
                idle_time = char.idle_time
                if idle_time < 60:
                    idle_str = f"{int(idle_time)}s"
                elif idle_time < 3600:
                    idle_str = f"{int(idle_time/60)}m"
                else:
                    idle_str = f"{int(idle_time/3600)}h"
                output.append(f"  {char.name} (idle {idle_str})")
        
        if not online_staff and not online_storytellers:
            output.append("No staff or storytellers are currently online.")
        
        self.caller.msg("\n".join(output))
