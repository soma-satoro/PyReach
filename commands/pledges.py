"""
Pledge command for Changeling: The Lost 2nd Edition.

This command handles all pledge types: Sealing, Oath, and Bargain.
Based on CTL 2e core book, pages 210-215.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.search import search_object
from evennia.utils import evtable
from world.cofd.pledges import (
    Pledge, PledgeHandler, get_next_pledge_id, validate_pledge_participants,
    PLEDGE_TYPE_SEALING, PLEDGE_TYPE_OATH, PLEDGE_TYPE_BARGAIN,
    OATH_SOCIETAL, OATH_PERSONAL, OATH_HOSTILE,
    STATUS_ACTIVE, STATUS_FULFILLED, STATUS_BROKEN, STATUS_RELEASED,
    SEALING_CONSEQUENCES_BASIC, SEALING_CONSEQUENCES_STRONG
)
from world.conditions import Condition, STANDARD_CONDITIONS


class CmdPledge(MuxCommand):
    """
    Manage pledges between characters.
    
    Usage:
        +pledge - List all your pledges
        +pledge <#> - View details of a specific pledge
        +pledge/list [<character>] - List pledges (own or another's)
        +pledge/seal <character>=<statement> - Seal someone's statement
        +pledge/seal/strong <character>=<statement> - Seal with Willpower (strengthened)
        +pledge/oath <character>[,<character2>,...]=<type> - Begin oath creation
        +pledge/bargain <character>=<description> - Begin bargain creation
        +pledge/text <#>=<verbiage> - Set the pledge text/verbiage
        +pledge/notes <#>=<notes> - Set pledge notes/biography
        +pledge/benefit <#>=<benefit> - Set pledge benefit
        +pledge/consequence <#>=<consequence> - Set consequence for breaking
        +pledge/finalize <#> - Finalize and activate a pledge
        +pledge/break <#> - Break a pledge
        +pledge/fulfill <#> - Fulfill a pledge
        +pledge/release <#> - Release a sealing (sealer only)
        
    Oath Types:
        societal - Joining motley, court, or freehold
        personal - Lovers, friends, protectors
        hostile - Sworn enemies, duels
        
    Examples:
        +pledge/seal Bob=I promise to return your book
        +pledge/oath Alice,Bob=personal
        +pledge/text 3=I swear by moon and stars to stand by you
        +pledge/bargain John=Clean his house weekly
        
    See also: +help pledges
    """
    
    key = "+pledge"
    aliases = ["pledge"]
    locks = "cmd:all()"
    help_category = "Changeling"
    
    def _ensure_glamour_initialized(self, character):
        """
        Ensure glamour_current is initialized for changelings.
        Returns True if glamour is available, False otherwise.
        """
        # Check if glamour_current is None
        if character.db.glamour_current is None:
            # Try to initialize from advantages
            advantages = character.db.stats.get("advantages", {})
            max_glamour = advantages.get("glamour", 0)
            
            if max_glamour > 0:
                # Initialize current to max
                character.db.glamour_current = max_glamour
                return True
            else:
                # No Wyrd set yet
                return False
        
        return True
    
    def func(self):
        """Execute the command."""
        caller = self.caller
        
        # Check if caller is a changeling for most operations
        template = caller.db.stats.get("other", {}).get("template", "Mortal")
        
        # Basic display - no args
        if not self.switches and not self.args:
            self.list_pledges(caller, include_inactive=False)
            return
        
        # View specific pledge
        if not self.switches and self.args:
            try:
                pledge_id = self.args.strip()
                self.view_pledge(pledge_id)
            except ValueError:
                caller.msg("|rInvalid pledge ID. Use +pledge to see your pledges.|n")
            return
        
        # Route to appropriate switch handler
        switch = self.switches[0] if self.switches else None
        
        if switch == "list":
            self.pledge_list()
        elif switch == "seal":
            if template.lower() != "changeling":
                caller.msg("|rOnly changelings can seal statements.|n")
                return
            if "strong" in self.switches:
                self.pledge_seal(strengthened=True)
            else:
                self.pledge_seal(strengthened=False)
        elif switch == "oath":
            if template.lower() != "changeling":
                caller.msg("|rOnly changelings can swear oaths.|n")
                return
            self.pledge_oath()
        elif switch == "bargain":
            if template.lower() != "changeling":
                caller.msg("|rOnly changelings can make bargains.|n")
                return
            self.pledge_bargain()
        elif switch == "text":
            self.set_pledge_text()
        elif switch == "notes":
            self.set_pledge_notes()
        elif switch == "benefit":
            self.set_pledge_benefit()
        elif switch == "consequence":
            self.set_pledge_consequence()
        elif switch == "finalize":
            self.finalize_pledge()
        elif switch == "break":
            self.break_pledge()
        elif switch == "fulfill":
            self.fulfill_pledge()
        elif switch == "release":
            self.release_pledge()
        else:
            caller.msg("|rUnknown switch. See |w+help +pledge|r for usage.|n")
    
    def list_pledges(self, character, include_inactive=False):
        """List all pledges for a character."""
        caller = self.caller
        pledges = character.pledges.get_all_pledges(include_inactive=include_inactive)
        
        if not pledges:
            if character == caller:
                caller.msg("|yYou have no pledges.|n")
            else:
                caller.msg(f"|y{character.name} has no pledges.|n")
            return
        
        # Build pledge list display
        header = f"|g{'=' * 78}|n"
        title = f"|wPledges for {character.name}|n"
        
        output = [header, title.center(78), header]
        
        for pledge in pledges:
            status_color = "|g" if pledge.status == STATUS_ACTIVE else "|r"
            type_display = pledge.pledge_type.capitalize()
            if pledge.pledge_type == PLEDGE_TYPE_OATH and pledge.oath_subtype:
                type_display += f" ({pledge.oath_subtype.capitalize()})"
            
            output.append(f" |w#{pledge.pledge_id}|n - {type_display} - {status_color}{pledge.status.capitalize()}|n")
            
            # Show brief verbiage if present
            if pledge.verbiage:
                verbiage_brief = pledge.verbiage[:60] + "..." if len(pledge.verbiage) > 60 else pledge.verbiage
                output.append(f"      \"{verbiage_brief}\"")
        
        output.append(header)
        output.append("|xUse |w+pledge <#>|x to view details of a specific pledge.|n")
        
        caller.msg("\n".join(output))
    
    def view_pledge(self, pledge_id):
        """View detailed information about a specific pledge."""
        caller = self.caller
        pledge = caller.pledges.get_pledge(pledge_id)
        
        if not pledge:
            caller.msg(f"|rPledge #{pledge_id} not found.|n")
            return
        
        # Build detailed display
        header = f"|g{'=' * 78}|n"
        output = [header]
        
        # Title
        title = f"|wPledge #{pledge.pledge_id}: {pledge.get_display_name()}|n"
        output.append(title.center(88))  # Account for color codes
        output.append(header)
        
        # Status
        status_color = "|g" if pledge.status == STATUS_ACTIVE else "|r"
        output.append(f"|wStatus:|n {status_color}{pledge.status.capitalize()}|n")
        
        # Type
        type_display = pledge.pledge_type.capitalize()
        if pledge.pledge_type == PLEDGE_TYPE_OATH and pledge.oath_subtype:
            type_display += f" ({pledge.oath_subtype.capitalize()})"
        output.append(f"|wType:|n {type_display}")
        
        # Participants
        participant_names = []
        for dbref in pledge.participants:
            try:
                char = search_object(f"#{dbref}", exact=True)
                if char:
                    participant_names.append(char[0].name)
            except:
                participant_names.append(f"Unknown (#{dbref})")
        
        output.append(f"|wParticipants:|n {', '.join(participant_names)}")
        
        # Created
        output.append(f"|wCreated:|n {pledge.created_at.strftime('%Y-%m-%d %H:%M')}")
        
        # Verbiage
        if pledge.verbiage:
            output.append(f"\n|wPledge Text:|n")
            output.append(f'"{pledge.verbiage}"')
        
        # Notes
        if pledge.notes:
            output.append(f"\n|wNotes:|n")
            output.append(pledge.notes)
        
        # Benefits
        if pledge.benefits:
            output.append(f"\n|wBenefits:|n")
            for key, value in pledge.benefits.items():
                output.append(f"  - {value}")
        
        # Consequences
        if pledge.consequences:
            output.append(f"\n|wConsequences for Breaking:|n")
            for key, value in pledge.consequences.items():
                output.append(f"  - {value}")
        
        # Strengthened (for sealings)
        if pledge.pledge_type == PLEDGE_TYPE_SEALING:
            output.append(f"\n|wStrengthened:|n {'Yes (Willpower spent)' if pledge.strengthened else 'No'}")
        
        output.append(header)
        
        caller.msg("\n".join(output))
    
    def pledge_list(self):
        """List pledges for self or another character."""
        caller = self.caller
        
        if not self.args:
            # List own pledges
            self.list_pledges(caller, include_inactive=True)
            return
        
        # Search for target character
        target_name = self.args.strip()
        results = search_object(target_name, typeclass='typeclasses.characters.Character')
        
        if not results:
            caller.msg(f"|rCould not find character: {target_name}|n")
            return
        
        if len(results) > 1:
            caller.msg(f"|rMultiple matches for: {target_name}. Please be more specific.|n")
            return
        
        target = results[0]
        
        # Check permissions - staff can view anyone, players can only view own
        if target != caller and not caller.check_permstring("Admin"):
            caller.msg("|rYou can only view your own pledges.|n")
            return
        
        self.list_pledges(target, include_inactive=True)
    
    def pledge_seal(self, strengthened=False):
        """
        Seal a character's statement.
        
        Args:
            strengthened (bool): Whether this is a strengthened sealing
        """
        caller = self.caller
        
        if not self.args or "=" not in self.args:
            caller.msg("|rUsage: +pledge/seal <character>=<statement>|n")
            return
        
        # Parse args
        target_name, statement = self.args.split("=", 1)
        target_name = target_name.strip()
        statement = statement.strip()
        
        if not statement:
            caller.msg("|rYou must specify a statement to seal.|n")
            return
        
        # Search for target
        results = search_object(target_name, typeclass='typeclasses.characters.Character')
        
        if not results:
            caller.msg(f"|rCould not find character: {target_name}|n")
            return
        
        if len(results) > 1:
            caller.msg(f"|rMultiple matches for: {target_name}. Please be more specific.|n")
            return
        
        target = results[0]
        
        # Check if target is another changeling (they can resist)
        target_template = target.db.stats.get("other", {}).get("template", "Mortal")
        is_target_changeling = target_template.lower() == "changeling"
        
        # Ensure glamour is initialized and check cost
        if not self._ensure_glamour_initialized(caller):
            caller.msg("|rYou don't have Wyrd set yet. Set your Wyrd stat first with |w+stat wyrd=<value>|n")
            return
        
        glamour_current = caller.db.glamour_current
        if glamour_current < 1:
            caller.msg("|rYou don't have enough Glamour to seal a statement. Cost: 1 Glamour.|n")
            return
        
        # Check Willpower cost for strengthened sealing
        willpower_current = caller.db.willpower_current
        if strengthened:
            if willpower_current is None or willpower_current < 1:
                caller.msg("|rYou don't have enough Willpower to strengthen the sealing. Cost: 1 Willpower + 1 Glamour.|n")
                return
        
        # Spend resources
        caller.db.glamour_current -= 1
        cost_msg = "1 Glamour"
        
        if strengthened:
            caller.db.willpower_current -= 1
            cost_msg = "1 Glamour and 1 Willpower"
        
        # Create the sealing
        pledge_id = get_next_pledge_id(caller)
        
        # Build consequences dict
        consequences = {}
        if strengthened:
            consequences["type"] = "strengthened"
            consequences["description"] = "Choose from strengthened consequences when broken"
        else:
            consequences["type"] = "basic"
            consequences["description"] = "Choose from basic consequences when broken"
        
        pledge = Pledge(
            pledge_id=pledge_id,
            pledge_type=PLEDGE_TYPE_SEALING,
            participants=[str(caller.id), str(target.id)],
            created_by=str(caller.id),
            verbiage=f"{target.name} stated: '{statement}'",
            strengthened=strengthened,
            consequences=consequences,
            status=STATUS_ACTIVE
        )
        
        # Add to both characters
        caller.pledges.add_pledge(pledge)
        target.pledges.add_pledge(pledge)
        
        # Notify both parties
        caller.msg(f"|gYou spend {cost_msg} and seal {target.name}'s statement:|n")
        caller.msg(f'  "{statement}"')
        caller.msg(f"|gPledge #{pledge_id} created. The Wyrd binds their words.|n")
        
        if is_target_changeling:
            target.msg(f"|y{caller.name} attempts to seal your words:|n")
            target.msg(f'  "{statement}"')
            target.msg("|yAs a changeling, you could counter this with 1 Glamour using |w+pledge/counter {pledge_id}|y|n")
            target.msg("|yOr allow it to demonstrate your intent to keep your word.|n")
        else:
            target.msg(f"|y{caller.name} has sealed your statement with fae magic:|n")
            target.msg(f'  "{statement}"')
            target.msg("|yYou feel a strange weight upon your words.|n")
    
    def pledge_oath(self):
        """Begin creating an oath between fae creatures."""
        caller = self.caller
        
        if not self.args or "=" not in self.args:
            caller.msg("|rUsage: +pledge/oath <character>[,<character2>,...]=<type>|n")
            caller.msg("|rTypes: societal, personal, hostile|n")
            return
        
        # Parse args
        participants_str, oath_type = self.args.split("=", 1)
        participants_str = participants_str.strip()
        oath_type = oath_type.strip().lower()
        
        # Validate oath type
        if oath_type not in [OATH_SOCIETAL, OATH_PERSONAL, OATH_HOSTILE]:
            caller.msg("|rInvalid oath type. Must be: societal, personal, or hostile|n")
            return
        
        # Parse participants
        participant_names = [name.strip() for name in participants_str.split(",")]
        
        # Validate participants
        success, targets, error = validate_pledge_participants(caller, participant_names, PLEDGE_TYPE_OATH)
        
        if not success:
            caller.msg(f"|r{error}|n")
            return
        
        # Ensure glamour is initialized and check cost
        if not self._ensure_glamour_initialized(caller):
            caller.msg("|rYou don't have Wyrd set yet. Set your Wyrd stat first with |w+stat wyrd=<value>|n")
            return
        
        glamour_current = caller.db.glamour_current
        if glamour_current < 1:
            caller.msg("|rYou don't have enough Glamour to swear an oath. Cost: 1 Glamour.|n")
            return
        
        # Create the oath (in draft status initially)
        pledge_id = get_next_pledge_id(caller)
        
        participant_ids = [str(caller.id)] + [str(t.id) for t in targets]
        
        pledge = Pledge(
            pledge_id=pledge_id,
            pledge_type=PLEDGE_TYPE_OATH,
            participants=participant_ids,
            created_by=str(caller.id),
            oath_subtype=oath_type,
            status="draft"  # Not active until finalized
        )
        
        # Add to caller only (others will get it when finalized)
        caller.pledges.add_pledge(pledge)
        
        # Inform caller
        caller.msg(f"|gOath #{pledge_id} created ({oath_type} oath).|n")
        caller.msg(f"|gParticipants: {caller.name}, {', '.join([t.name for t in targets])}|n")
        caller.msg("|gUse the following commands to complete the oath:|n")
        caller.msg(f"|w  +pledge/text {pledge_id}=<oath verbiage>|n")
        caller.msg(f"|w  +pledge/notes {pledge_id}=<additional notes>|n")
        caller.msg(f"|w  +pledge/benefit {pledge_id}=<benefit choice>|n")
        caller.msg(f"|w  +pledge/consequence {pledge_id}=<consequence>|n")
        caller.msg(f"|w  +pledge/finalize {pledge_id}|n")
        caller.msg("|xFinalizing will spend 1 Glamour from each participant.|n")
    
    def pledge_bargain(self):
        """Begin creating a bargain with a mortal."""
        caller = self.caller
        
        if not self.args or "=" not in self.args:
            caller.msg("|rUsage: +pledge/bargain <character>=<description>|n")
            return
        
        # Parse args
        target_name, description = self.args.split("=", 1)
        target_name = target_name.strip()
        description = description.strip()
        
        if not description:
            caller.msg("|rYou must specify what service you'll provide.|n")
            return
        
        # Validate participant
        success, targets, error = validate_pledge_participants(caller, [target_name], PLEDGE_TYPE_BARGAIN)
        
        if not success:
            caller.msg(f"|r{error}|n")
            return
        
        target = targets[0]
        
        # Ensure glamour is initialized and check cost
        if not self._ensure_glamour_initialized(caller):
            caller.msg("|rYou don't have Wyrd set yet. Set your Wyrd stat first with |w+stat wyrd=<value>|n")
            return
        
        glamour_current = caller.db.glamour_current
        if glamour_current < 1:
            caller.msg("|rYou don't have enough Glamour to make a bargain. Cost: 1 Glamour.|n")
            return
        
        # Create the bargain (in draft status initially)
        pledge_id = get_next_pledge_id(caller)
        
        pledge = Pledge(
            pledge_id=pledge_id,
            pledge_type=PLEDGE_TYPE_BARGAIN,
            participants=[str(caller.id), str(target.id)],
            created_by=str(caller.id),
            verbiage=f"Service: {description}",
            status="draft"  # Not active until finalized
        )
        
        # Add to caller only
        caller.pledges.add_pledge(pledge)
        
        # Inform caller
        caller.msg(f"|gBargain #{pledge_id} created.|n")
        caller.msg(f"|gWith: {target.name}|n")
        caller.msg(f"|gService: {description}|n")
        caller.msg("|gUse the following commands to complete the bargain:|n")
        caller.msg(f"|w  +pledge/text {pledge_id}=<full bargain terms>|n")
        caller.msg(f"|w  +pledge/notes {pledge_id}=<additional notes>|n")
        caller.msg(f"|w  +pledge/finalize {pledge_id}|n")
        caller.msg("|xFinalizing will spend 1 Glamour and grant the Obliged Condition.|n")
    
    def set_pledge_text(self):
        """Set the verbiage/text of a pledge."""
        caller = self.caller
        
        if not self.args or "=" not in self.args:
            caller.msg("|rUsage: +pledge/text <#>=<verbiage>|n")
            return
        
        pledge_id, verbiage = self.args.split("=", 1)
        pledge_id = pledge_id.strip()
        verbiage = verbiage.strip()
        
        pledge = caller.pledges.get_pledge(pledge_id)
        
        if not pledge:
            caller.msg(f"|rPledge #{pledge_id} not found.|n")
            return
        
        if pledge.status != "draft" and pledge.status != STATUS_ACTIVE:
            caller.msg("|rYou can only set text for draft or active pledges.|n")
            return
        
        if pledge.created_by != str(caller.id):
            caller.msg("|rYou can only modify pledges you created.|n")
            return
        
        pledge.verbiage = verbiage
        caller.pledges._save_pledges()
        
        caller.msg(f"|gPledge #{pledge_id} text updated.|n")
    
    def set_pledge_notes(self):
        """Set biographical notes for a pledge."""
        caller = self.caller
        
        if not self.args or "=" not in self.args:
            caller.msg("|rUsage: +pledge/notes <#>=<notes>|n")
            return
        
        pledge_id, notes = self.args.split("=", 1)
        pledge_id = pledge_id.strip()
        notes = notes.strip()
        
        pledge = caller.pledges.get_pledge(pledge_id)
        
        if not pledge:
            caller.msg(f"|rPledge #{pledge_id} not found.|n")
            return
        
        if pledge.status != "draft" and pledge.status != STATUS_ACTIVE:
            caller.msg("|rYou can only set notes for draft or active pledges.|n")
            return
        
        if pledge.created_by != str(caller.id):
            caller.msg("|rYou can only modify pledges you created.|n")
            return
        
        pledge.notes = notes
        caller.pledges._save_pledges()
        
        caller.msg(f"|gPledge #{pledge_id} notes updated.|n")
    
    def set_pledge_benefit(self):
        """Set the benefit for a pledge."""
        caller = self.caller
        
        if not self.args or "=" not in self.args:
            caller.msg("|rUsage: +pledge/benefit <#>=<benefit>|n")
            return
        
        pledge_id, benefit = self.args.split("=", 1)
        pledge_id = pledge_id.strip()
        benefit = benefit.strip()
        
        pledge = caller.pledges.get_pledge(pledge_id)
        
        if not pledge:
            caller.msg(f"|rPledge #{pledge_id} not found.|n")
            return
        
        if pledge.status != "draft":
            caller.msg("|rYou can only set benefits for draft pledges.|n")
            return
        
        if pledge.created_by != str(caller.id):
            caller.msg("|rYou can only modify pledges you created.|n")
            return
        
        # Add benefit to pledge
        if not pledge.benefits:
            pledge.benefits = {}
        
        benefit_key = f"benefit_{len(pledge.benefits) + 1}"
        pledge.benefits[benefit_key] = benefit
        caller.pledges._save_pledges()
        
        caller.msg(f"|gBenefit added to Pledge #{pledge_id}.|n")
    
    def set_pledge_consequence(self):
        """Set the consequence for breaking a pledge."""
        caller = self.caller
        
        if not self.args or "=" not in self.args:
            caller.msg("|rUsage: +pledge/consequence <#>=<consequence>|n")
            return
        
        pledge_id, consequence = self.args.split("=", 1)
        pledge_id = pledge_id.strip()
        consequence = consequence.strip()
        
        pledge = caller.pledges.get_pledge(pledge_id)
        
        if not pledge:
            caller.msg(f"|rPledge #{pledge_id} not found.|n")
            return
        
        if pledge.status != "draft":
            caller.msg("|rYou can only set consequences for draft pledges.|n")
            return
        
        if pledge.created_by != str(caller.id):
            caller.msg("|rYou can only modify pledges you created.|n")
            return
        
        # Add consequence to pledge
        if not pledge.consequences:
            pledge.consequences = {}
        
        consequence_key = f"consequence_{len(pledge.consequences) + 1}"
        pledge.consequences[consequence_key] = consequence
        caller.pledges._save_pledges()
        
        caller.msg(f"|gConsequence added to Pledge #{pledge_id}.|n")
    
    def finalize_pledge(self):
        """Finalize and activate a pledge."""
        caller = self.caller
        
        if not self.args:
            caller.msg("|rUsage: +pledge/finalize <#>|n")
            return
        
        pledge_id = self.args.strip()
        pledge = caller.pledges.get_pledge(pledge_id)
        
        if not pledge:
            caller.msg(f"|rPledge #{pledge_id} not found.|n")
            return
        
        if pledge.status != "draft":
            caller.msg("|rOnly draft pledges can be finalized.|n")
            return
        
        if pledge.created_by != str(caller.id):
            caller.msg("|rYou can only finalize pledges you created.|n")
            return
        
        # Validate pledge has minimum required information
        if not pledge.verbiage:
            caller.msg("|rPledge must have text/verbiage before finalizing. Use |w+pledge/text|n")
            return
        
        # Ensure glamour is initialized and check cost
        if not self._ensure_glamour_initialized(caller):
            caller.msg("|rYou don't have Wyrd set yet. Set your Wyrd stat first with |w+stat wyrd=<value>|n")
            return
        
        glamour_current = caller.db.glamour_current
        if glamour_current < 1:
            caller.msg("|rYou don't have enough Glamour to finalize this pledge.|n")
            return
        
        caller.db.glamour_current -= 1
        
        # Activate the pledge
        pledge.status = STATUS_ACTIVE
        caller.pledges._save_pledges()
        
        # Add pledge to other participants
        for participant_id in pledge.participants:
            if participant_id != str(caller.id):
                try:
                    participant = search_object(f"#{participant_id}", exact=True)[0]
                    participant.pledges.add_pledge(pledge)
                    
                    # Notify participant
                    participant.msg(f"|g{caller.name} has finalized a pledge with you.|n")
                    participant.msg(f"|wPledge #{pledge_id}: {pledge.get_display_name()}|n")
                    participant.msg(f'"{pledge.verbiage}"')
                    participant.msg(f"|xUse |w+pledge {pledge_id}|x to view full details.|n")
                except:
                    pass
        
        # Apply appropriate conditions
        if pledge.pledge_type == PLEDGE_TYPE_BARGAIN:
            obliged_condition = STANDARD_CONDITIONS.get('obliged')
            if obliged_condition:
                caller.conditions.add(obliged_condition)
        
        caller.msg(f"|gPledge #{pledge_id} has been finalized and is now active!|n")
        caller.msg("|gThe Wyrd binds you to your word.|n")
    
    def break_pledge(self):
        """Break a pledge and suffer consequences."""
        caller = self.caller
        
        if not self.args:
            caller.msg("|rUsage: +pledge/break <#>|n")
            return
        
        pledge_id = self.args.strip()
        success, message, consequences = caller.pledges.break_pledge(pledge_id)
        
        if not success:
            caller.msg(f"|r{message}|n")
            return
        
        # Display consequences
        caller.msg(f"|r{message}|n")
        caller.msg("|rYou suffer the consequences of breaking your word:|n")
        
        if consequences:
            for key, value in consequences.items():
                caller.msg(f"|r  - {value}|n")
        
        caller.msg("|rThe Wyrd takes note of your betrayal.|n")
    
    def fulfill_pledge(self):
        """Fulfill a pledge and gain benefits."""
        caller = self.caller
        
        if not self.args:
            caller.msg("|rUsage: +pledge/fulfill <#>|n")
            return
        
        pledge_id = self.args.strip()
        success, message = caller.pledges.fulfill_pledge(pledge_id)
        
        if not success:
            caller.msg(f"|r{message}|n")
            return
        
        caller.msg(f"|g{message}|n")
    
    def release_pledge(self):
        """Release a sealing (sealer only)."""
        caller = self.caller
        
        if not self.args:
            caller.msg("|rUsage: +pledge/release <#>|n")
            return
        
        pledge_id = self.args.strip()
        pledge = caller.pledges.get_pledge(pledge_id)
        
        if not pledge:
            caller.msg(f"|rPledge #{pledge_id} not found.|n")
            return
        
        if pledge.created_by != str(caller.id):
            caller.msg("|rYou can only release sealings you created.|n")
            return
        
        success, message = caller.pledges.release_pledge(pledge_id)
        
        if not success:
            caller.msg(f"|r{message}|n")
            return
        
        # Notify the sealed party
        for participant_id in pledge.participants:
            if participant_id != str(caller.id):
                try:
                    participant = search_object(f"#{participant_id}", exact=True)[0]
                    participant.msg(f"|g{caller.name} has released you from a sealing.|n")
                    participant.msg(f"|gYou are no longer bound by: '{pledge.verbiage}'|n")
                except:
                    pass
        
        caller.msg(f"|g{message}|n")
