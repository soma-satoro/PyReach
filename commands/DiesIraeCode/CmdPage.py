"""
Page command - allows paging by both account and character name
"""
from evennia.commands.default.comms import CmdPage as DefaultCmdPage
from evennia import search_object, search_account
from evennia.utils import create
from evennia.utils.utils import make_iter
from evennia.comms.models import Msg
from evennia.utils.search import search_object
from typeclasses.characters import Character
from django.contrib.auth.models import User as AccountDB
from utils.search_helpers import search_character

class CmdPage(DefaultCmdPage):
    """
    send a private message to another account

    Usage:
      page[/switches] [<account/character>,<account/character>,... = <message>]
      tell        ''
      page <number>
      page/idle [<message>]        - Set or remove an idle message

    Switch:
      last - shows who you last messaged
      list - show your last <number> of tells/pages (default)
      idle - set or remove an idle message

    Send a message to target user (if online). If no
    argument is given, you will get a list of your latest messages.
    You can page either by account name or by character name.
    """
    key = "page"
    aliases = ["tell", "p"]
    help_category = "Comms"
    # Add idle to the allowed switches
    switch_options = ("last", "list", "idle")

    def func(self):
        """Implement function using the parent"""
        caller = self.caller

        # Handle idle message setting/removal
        if "idle" in self.switches:
            # Remove any = signs from the args as they're not needed for idle messages
            idle_message = self.args.split("=", 1)[0] if self.args else ""
            if not idle_message.strip():
                # Remove idle message if it exists
                if caller.attributes.has("idle_message"):
                    caller.attributes.remove("idle_message")
                    self.msg("Idle message removed.")
                else:
                    self.msg("You don't have an idle message set.")
                return
            # Set new idle message
            caller.attributes.add("idle_message", idle_message.strip())
            self.msg(f"Idle message set to: {idle_message.strip()}")
            return

        # Get the messages we've sent (not to channels)
        pages_we_sent = Msg.objects.get_messages_by_sender(caller).exclude(
            db_receivers_accounts__in=[caller]).order_by("-db_date_created")

        if "last" in self.switches:
            if pages_we_sent:
                recv = ",".join(obj.key for obj in pages_we_sent[0].receivers)
                self.msg(f"You last paged |c{recv}|n:{pages_we_sent[0].message}")
                return
            else:
                self.msg("You haven't paged anyone yet.")
                return

        # Handle message history display
        if self.args and "=" not in self.args:
            if self.args.isdigit():
                # Show message history
                number = int(self.args)
                pages = pages_we_sent[:number]
                if pages:
                    try:
                        formatted_pages = []
                        for msg in pages:
                            try:
                                receivers = ",".join(obj.key for obj in msg.receivers)
                            except AttributeError:
                                # Handle case where receivers might be stored as strings
                                receivers = ",".join(str(obj) for obj in msg.receivers)
                            formatted_pages.append(
                                "|w%s|n |c%s|n: %s" % (
                                    msg.date_created.strftime("%Y-%m-%d %H:%M:%S"),
                                    receivers,
                                    msg.message
                                )
                            )
                        msg = "\n".join(formatted_pages)
                        self.msg(f"Your last {len(pages)} pages:\n{msg}\nEnd of message history.")
                    except Exception as e:
                        # If any error occurs, still try to show what we can
                        self.msg(f"Error displaying full history: {str(e)}\nShowing what we can:")
                        for msg in pages:
                            try:
                                receivers = ",".join(str(obj) for obj in msg.receivers)
                                self.msg("|w%s|n |c%s|n: %s" % (
                                    msg.date_created.strftime("%Y-%m-%d %H:%M:%S"),
                                    receivers,
                                    msg.message
                                ))
                            except:
                                continue
                        self.msg("End of message history.")
                else:
                    self.msg("You haven't paged anyone yet.")
                return
            else:
                # No = sign, just a message - send to last person(s) paged
                if pages_we_sent:
                    # Get all recipients from the last message
                    last_recipients = pages_we_sent[0].receivers
                    # Get their character names
                    recipient_names = []
                    for recipient in last_recipients:
                        if hasattr(recipient, 'puppet') and recipient.puppet:
                            recipient_names.append(recipient.puppet.name)
                        else:
                            recipient_names.append(recipient.key)
                    # Recursively call the command with the properly formatted string
                    self.caller.execute_cmd(f"page {','.join(recipient_names)}={self.args}")
                    return
                else:
                    self.msg("You haven't paged anyone yet.")
                    return

        # Parse the message for new pages
        if "=" not in self.args:
            self.msg("Usage: page <character>[,<character2>,...]=<message>")
            return
            
        targets, message = self.args.split("=", 1)
        message = message.strip()
        
        # Split recipients by spaces or commas
        recipient_list = [r.strip() for r in targets.replace(",", " ").split()]
        
        # Process the recipients
        account_recipients = []
        offline_recipients = []
        failed_recipients = []
        
        for recipient in recipient_list:
            # Use our new search helper
            target = search_character(self.caller, recipient, quiet=True)
            
            if target:
                # Try to get the account through different methods
                account = None
                if hasattr(target, 'account') and target.account:
                    account = target.account
                elif hasattr(target, 'player'):  # Some systems use 'player' instead of 'account'
                    account = target.player
                
                if not account:
                    offline_recipients.append(target.name)
                    continue
                    
                # Check if the account is actually connected
                if not account.sessions.count():
                    offline_recipients.append(target.name)
                    continue

                # Check for idle message
                if account.attributes.has("idle_message"):
                    idle_msg = account.attributes.get("idle_message")
                    self.msg(f"Idle response from {account.puppet.name if account.puppet else account.name}: {idle_msg}")
                    # Notify the idle user that their message was sent
                    account.msg(f"Idle message sent to {caller.name}: {idle_msg}")
                    
                # If we get here, the character has a valid, connected account
                account_recipients.append(account)
                continue

            # If we get here, we couldn't find the recipient
            failed_recipients.append(recipient)

        if not account_recipients and (offline_recipients or failed_recipients):
            # No valid online recipients found
            if failed_recipients:
                self.msg(f"Could not find: {', '.join(failed_recipients)}")
            if offline_recipients:
                self.msg(f"Currently offline: {', '.join(offline_recipients)}")
            return

        # Get caller's character name if available
        caller_name = caller.name
        # Get caller's alias if available
        caller_alias = caller.attributes.get("alias", None)
        caller_display = f"{caller_name}({caller_alias})" if caller_alias else caller_name

        # Tell the accounts they got a message
        received = []
        for target in account_recipients:
            if not target.access(caller, "msg"):
                self.msg(f"You are not allowed to page {target}.")
                continue
            
            # Get the character name if available
            char = target.puppet if target.puppet else target
            char_name = char.name
            # Get character's alias if available
            char_alias = char.attributes.get("alias", None)
            char_display = f"{char_name}({char_alias})" if char_alias else char_name
            
            # Format recipients list for header
            other_recipients = []
            for t in account_recipients:
                if t != target:
                    t_char = t.puppet if t.puppet else t
                    t_name = t_char.name
                    t_alias = t_char.attributes.get("alias", None)
                    t_display = f"{t_name}({t_alias})" if t_alias else t_name
                    other_recipients.append(t_display)
            
            # Format the header
            if other_recipients:
                others = f"{', '.join(other_recipients[:-1])} and {other_recipients[-1]}" if len(other_recipients) > 1 else other_recipients[0]
                header = f"From afar, (To {char_display} and {others}),"
            else:
                header = f"From afar,"
            
            # Format and send the message
            if message.startswith(":"):
                formatted_message = f"{header} {caller_display} {message[1:].strip()}"
            else:
                formatted_message = f"{header} {caller_display} pages: {message}"
                
            target.msg(formatted_message)
            received.append(f"|c{char_display}|n")

        # Format the confirmation message
        if received:
            if len(received) == 1:
                if message.startswith(":"):
                    self.msg(f"Long distance to {received[0]}: {caller_display} {message[1:].strip()}")
                else:
                    # Get the character name for the confirmation message
                    t_char = account_recipients[0].puppet if account_recipients[0].puppet else account_recipients[0]
                    char_name = t_char.name
                    char_alias = t_char.attributes.get("alias", None)
                    char_display = f"{char_name}({char_alias})" if char_alias else char_name
                    self.msg(f"You paged {char_display} with: '{message}'")
            else:
                # Get character names for all recipients
                char_displays = []
                for t in account_recipients:
                    t_char = t.puppet if t.puppet else t
                    t_name = t_char.name
                    t_alias = t_char.attributes.get("alias", None)
                    t_display = f"{t_name}({t_alias})" if t_alias else t_name
                    char_displays.append(t_display)
                    
                if message.startswith(":"):
                    self.msg(f"To ({', '.join(char_displays)}): {caller_display} {message[1:].strip()}")
                else:
                    self.msg(f"To ({', '.join(char_displays)}) you paged: '{message}'")

        # Report any offline/not-found users
        if offline_recipients:
            self.msg(f"Currently offline: {', '.join(offline_recipients)}")
        if failed_recipients:
            self.msg(f"Could not find: {', '.join(failed_recipients)}")

        # Create persistent message object for history
        if account_recipients:
            target_perms = " or ".join([f"id({target.id})" for target in account_recipients + [caller]])
            create.create_message(
                caller,
                message,
                receivers=account_recipients,
                locks=(
                    f"read:{target_perms} or perm(Admin);"
                    f"delete:id({caller.id}) or perm(Admin);"
                    f"edit:id({caller.id}) or perm(Admin)"
                ),
                tags=[("page", "comms")],
            )