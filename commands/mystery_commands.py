"""
Unified Mystery Investigation System

This system combines player investigation commands and staff mystery management
into a single cohesive command structure, following the established patterns
used throughout the PyReach codebase.
"""

import secrets
from evennia.commands.default.muxcommand import MuxCommand
from typeclasses.mysteries import MysteryManager, Mystery, ClueObject
from world.utils.permission_utils import check_mystery_permission, format_permission_error
from world.utils.formatting import header, format_simple_table
from utils.search_helpers import search_character


class CmdMystery(MuxCommand):
    """
    Unified Mystery Investigation System
    
    Player Investigation Commands:
        +mystery                          - List active mysteries you can participate in
        +mystery <mystery_id>             - View mystery details and your progress
        +mystery/progress [mystery_id]    - Show your investigation progress
        +mystery/examine <object>         - Carefully examine an object for clues (Resolve + Composure)
        +mystery/search                   - Search your current area for hidden clues (Wits + Investigation)
        +mystery/interview <character>    - Interview someone for information
        +mystery/research <topic>         - Research a topic (requires library/resources)
        +mystery/occult <topic>           - Research occult topics (requires occult resources)
        +mystery/share <character> = <mystery_id>/<clue_name> - Share a mystery clue with another character
        +mystery/collaborate <character>  - Begin collaborating on investigations
        +mystery/clue <clue_name>         - View details of a discovered clue
        
    Staff Mystery Management Commands:
        +mystery/create <title> = <description>
        +mystery/list [category]          - List all mysteries (staff view)
        +mystery/view <mystery_id>        - View mystery details (staff view)
        +mystery/edit <mystery_id>/<field> = <value>
        +mystery/delete <mystery_id>
        +mystery/status <mystery_id> = <active|solved|suspended>
        
        +mystery/addclue <mystery_id> = <name>/<description>
        +mystery/editclue <mystery_id>/<clue_id> = <field>/<value>
        +mystery/delclue <mystery_id>/<clue_id>
        +mystery/prereq <mystery_id>/<clue_id> = <prerequisite_clue_ids>
        +mystery/leads <mystery_id>/<clue_id> = <leads_to_clue_ids>
        +mystery/cluetype <mystery_id>/<clue_id> = <type>
        +mystery/methods <mystery_id>/<clue_id> = <method1,method2>
        
        +mystery/conditions <mystery_id>/<clue_id> = <conditions_json>
        +mystery/skillroll <mystery_id>/<clue_id> = <skill>/<attribute>/<difficulty>
        +mystery/revelation <mystery_id>/<trigger_id> = <required_clues>/<revelation>
        +mystery/access <mystery_id> = <templates|characters|areas>
        
        +mystery/discovered <mystery_id> [character]
        +mystery/grant <character> = <mystery_id>/<clue_id>
        +mystery/revoke <character> = <mystery_id>/<clue_id>
        +mystery/staffprogress [mystery_id] - Show detailed progress (staff view)
        +mystery/participant <mystery_id> = <character> - Add character as participant
        
        +mystery/templates                - List available mystery templates
        +mystery/template <template_name> = [custom_title] - Create from template
        
    Staff Clue Object Commands:
        +mystery/clueobj/create <name> = <mystery_id>/<clue_id>
        +mystery/clueobj/edit <object> = <field>/<value>
        +mystery/clueobj/list [here]
        +mystery/clueobj/delete <object>
        
    Examples:
        Player: +mystery, +mystery/search, +mystery/examine desk
        Staff: +mystery/create The Missing Heir = A wealthy family's heir has vanished
        Staff: +mystery/addclue 1 = Torn Letter/A letter with half the address torn off
    """
    
    key = "+mystery"
    aliases = ["+investigation", "+inv", "+mysteries", "+mystadmin"]
    help_category = "Roleplaying Tools"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()
        
        # Check if this is a clue object subcommand
        self.is_clueobj_cmd = False
        if self.switches and len(self.switches) >= 2 and self.switches[0].lower() == "clueobj":
            self.is_clueobj_cmd = True
            # Shift the switches so clueobj/create becomes just create for processing
            self.clueobj_switch = self.switches[1].lower()
    
    def _search_object(self, search_term):
        """
        Search for an object (item, furniture, etc.) in caller's context.
        Tries both spaces and underscores for flexible matching.

        Args:
            search_term (str): The term to search for

        Returns:
            Object or None: The found object, or None if not found
        """
        target = self.caller.search(search_term)
        if not target and ' ' in search_term:
            target = self.caller.search(search_term.replace(' ', '_'))
        if not target and '_' in search_term:
            target = self.caller.search(search_term.replace('_', ' '))
        if target:
            return target[0] if isinstance(target, list) else target
        return None
    
    def func(self):
        """Execute the command"""
        # Handle clue object commands first
        if self.is_clueobj_cmd:
            self.handle_clueobj_commands()
            return
            
        # No switches - default behavior
        if not self.switches:
            if self.args:
                # +mystery <mystery_id> - view specific mystery
                self.view_mystery()
            else:
                # +mystery - list mysteries available to player
                self.list_mysteries_player()
            return
            
        switch = self.switches[0].lower()
        
        # Player commands (no permission check needed)
        player_switches = {
            "progress": self.show_progress,
            "examine": self.examine_for_clues,
            "search": self.search_for_clues,
            "interview": self.interview,
            "research": self.research,
            "occult": self.occult_research,
            "share": self.share_clue,
            "collaborate": self.collaborate,
            "clue": self.view_clue,
        }
        if switch in player_switches:
            player_switches[switch]()
            return
        
        # Staff commands (require permission check)
        if switch in ["create", "list", "view", "edit", "delete", "status", "addclue", "editclue", 
                       "delclue", "prereq", "leads", "cluetype", "methods", "conditions", "skillroll", "revelation", 
                       "access", "discovered", "grant", "revoke", "templates", "template", "staffprogress", "participant"]:
            if not check_mystery_permission(self.caller):
                self.caller.msg(format_permission_error("Staff or Storyteller"))
                return
                
            if switch == "create":
                self.create_mystery()
            elif switch == "list":
                self.list_mysteries_staff()
            elif switch == "view":
                self.view_mystery_staff()
            elif switch == "edit":
                self.edit_mystery()
            elif switch == "delete":
                self.delete_mystery()
            elif switch == "status":
                self.set_status()
            elif switch == "addclue":
                self.add_clue()
            elif switch == "editclue":
                self.edit_clue()
            elif switch == "delclue":
                self.delete_clue()
            elif switch == "prereq":
                self.set_prerequisites()
            elif switch == "leads":
                self.set_leads()
            elif switch == "cluetype":
                self.set_clue_type()
            elif switch == "methods":
                self.set_clue_methods()
            elif switch == "conditions":
                self.set_conditions()
            elif switch == "skillroll":
                self.set_skillroll()
            elif switch == "revelation":
                self.add_revelation()
            elif switch == "access":
                self.set_access()
            elif switch == "discovered":
                self.show_discovered()
            elif switch == "grant":
                self.grant_clue()
            elif switch == "revoke":
                self.revoke_clue()
            elif switch == "templates":
                self.list_templates()
            elif switch == "template":
                self.create_from_template()
            elif switch == "staffprogress":
                self.show_staff_progress()
            elif switch == "participant":
                self.add_participant()
        else:
            self.caller.msg("Invalid switch. See 'help +mystery' for usage.")
    
    # =============================================================================
    # PLAYER INVESTIGATION METHODS
    # =============================================================================
    
    def list_mysteries_player(self):
        """List active mysteries the character can participate in."""
        mysteries = MysteryManager.get_active_mysteries()
        
        if not mysteries:
            self.caller.msg("No active mysteries are available.")
            return
        
        # Filter mysteries this character can access
        accessible_mysteries = []
        for mystery in mysteries:
            # Check template restrictions
            if mystery.db.allowed_templates:
                char_template = getattr(self.caller.db, 'template', None)
                if char_template not in mystery.db.allowed_templates:
                    continue
            
            # Check character restrictions
            if mystery.db.allowed_characters and self.caller.id not in mystery.db.allowed_characters:
                continue
                
            accessible_mysteries.append(mystery)
        
        if not accessible_mysteries:
            self.caller.msg("No mysteries are available for your character.")
            return

        headers = ["ID", "Title", "Category", "Difficulty", "Your Progress"]
        rows = []
        for mystery in accessible_mysteries:
            discovered_clues = mystery.get_discovered_clues(self.caller)
            total_clues = len(mystery.db.clues)
            progress = f"{len(discovered_clues)}/{total_clues}"
            rows.append((
                mystery.id,
                (mystery.db.title or "")[:25],
                mystery.db.category or "",
                f"{mystery.db.difficulty}/5",
                progress
            ))
        table = format_simple_table(headers, rows)
        self.caller.msg(f"\n{header('Active Mysteries')}\n{table}")
    
    def view_mystery(self):
        """View details of a specific mystery and the character's progress."""
        if not self.args:
            self.caller.msg("Usage: +mystery <mystery_id>")
            return
        
        try:
            mystery_id = int(self.args.strip())
        except ValueError:
            self.caller.msg("Mystery ID must be a number.")
            return
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        # Check if character can access this mystery
        if hasattr(mystery.db, 'access_rules') and mystery.db.access_rules:
            if not (isinstance(mystery.db.access_rules, dict) and mystery.db.access_rules.get('type') == 'open'):
                if not mystery._check_access_rules(self.caller):
                    self.caller.msg("You cannot access this mystery.")
                    return
        
        # Check legacy template restrictions
        if mystery.db.allowed_templates:
            char_template = self.caller.db.stats.get('other', {}).get('template', 'mortal').lower()
            if char_template not in [t.lower() for t in mystery.db.allowed_templates]:
                self.caller.msg("You cannot access this mystery.")
                return
        
        discovered_clues = mystery.get_discovered_clues(self.caller)
        available_clues = mystery.get_available_clues(self.caller)
        
        output = [
            header(mystery.db.title, char="="),
            f"|yDescription:|n {mystery.db.description}",
            f"|yCategory:|n {mystery.db.category}",
            f"|yDifficulty:|n {mystery.db.difficulty}/5",
            f"|yYour Progress:|n {len(discovered_clues)}/{len(mystery.db.clues)} clues discovered",
            ""
        ]
        
        if discovered_clues:
            output.append("|yDiscovered Clues:|n")
            for clue_id in discovered_clues:
                clue = mystery.db.clues.get(clue_id, {})
                output.append(f"  |w{clue.get('name', 'Unknown')}|n - {clue.get('description', '')[:50]}...")
            output.append("")
        
        if available_clues:
            output.append(f"|yAvailable to Discover:|n {len(available_clues)} clue(s)")
            output.append("|yHint:|n Try using +mystery/search, /examine, or /interview to find clues.")
        else:
            if len(discovered_clues) < len(mystery.db.clues):
                output.append("|yNext Steps:|n You may need to discover more clues before new ones become available.")
        
        self.caller.msg("\n".join(output))
    
    def show_progress(self):
        """Show investigation progress across all mysteries."""
        mystery_clues = self.caller.mysteries.get_all() if hasattr(self.caller, 'mysteries') else getattr(self.caller.db, 'mystery_clues', {})
        if not mystery_clues:
            self.caller.msg("You haven't discovered any mystery clues yet.")
            return
        
        output = ["|cYour Investigation Progress:|n"]
        
        for mystery_id, clue_ids in mystery_clues.items():
            mystery = self._get_mystery(str(mystery_id))
            if mystery:
                total_clues = len(mystery.db.clues)
                discovered_count = len(clue_ids)
                percentage = int((discovered_count / total_clues) * 100) if total_clues > 0 else 0
                
                output.append(f"|w{mystery.db.title}|n")
                output.append(f"  Progress: {discovered_count}/{total_clues} clues ({percentage}%)")
                output.append(f"  Category: {mystery.db.category}")
                output.append("")
        
        self.caller.msg("\n".join(output))
    
    def examine_for_clues(self):
        """Examine an object for clues."""
        if not self.args:
            self.caller.msg("Usage: +mystery/examine <object>")
            return
        
        search_term = self.args.strip()
        target = self._search_object(search_term)

        if not target:
            return

        # Check if this is a clue object
        if isinstance(target, ClueObject):
            # Let the clue object handle the examination
            target.at_examine(self.caller)
        else:
            self.caller.msg(f"|yYou carefully examine {target.name} for clues...|n")
            
            # Use the general mystery discovery logic
            discovered_clues = self._attempt_mystery_discovery("examine", target)
            
            if discovered_clues:
                self.caller.msg(f"|gYour careful examination reveals:|n {', '.join(discovered_clues)}")
            else:
                hint_msg = self._get_method_hint("examine")
                self.caller.msg(f"Your examination of {target.name} reveals nothing unusual.")
                if hint_msg:
                    self.caller.msg(hint_msg)
    
    def search_for_clues(self):
        """Search the current area for hidden clues."""
        if not self.caller.location:
            self.caller.msg("You need to be somewhere to search.")
            return
        
        area_name = self.caller.location.name
        self.caller.msg(f"|yYou begin searching {area_name} for hidden clues...|n")
        
        # Use the general mystery discovery logic
        discovered_clues = self._attempt_mystery_discovery("search")
        
        if discovered_clues:
            self.caller.msg(f"|yYour search uncovered:|n {', '.join(discovered_clues)}")
        else:
            # Check if there are clues that require different methods
            hint_msg = self._get_method_hint("search")
            if hint_msg:
                self.caller.msg(f"|yYou search {area_name} thoroughly but find nothing of interest.|n")
                self.caller.msg(hint_msg)
            else:
                self.caller.msg(f"|yYou search {area_name} thoroughly but find nothing of interest.|n")
    
    def interview(self):
        """Interview a character for information using the mystery system."""
        if not self.args:
            self.caller.msg("Usage: +mystery/interview <character>")
            return
        
        search_term = self.args.strip()
        target = search_character(self.caller, search_term)

        if not target:
            return

        if target == self.caller:
            self.caller.msg("You can't interview yourself.")
            return
        
        self.caller.msg(f"|yYou begin interviewing {target.name}...|n")
        
        # Use the general mystery discovery logic
        discovered_clues = self._attempt_mystery_discovery("interview", target)
        
        if discovered_clues:
            self.caller.msg(f"|g{target.name} reveals something interesting:|n {', '.join(discovered_clues)}")
            target.msg(f"|yYou shared information with {self.caller.name}.|n")
        else:
            # Check if this is a PC vs NPC
            if target.has_account:
                # Regular PC - initiate social RP
                self.caller.msg(f"|y{target.name} doesn't seem to know anything about your current investigations.|n")
                target.msg(f"|y{self.caller.name} wants to interview you about ongoing investigations.|n")
            else:
                # NPC with no relevant information
                self.caller.msg(f"|r{target.name} doesn't seem willing to share information with you.|n")
    
    def research(self):
        """Research a topic for clues using the mystery system."""
        if not self.args:
            self.caller.msg("Usage: +mystery/research <topic>")
            return
        
        topic = self.args.strip()
        
        # Check if character is in a location with research capabilities
        location = self.caller.location
        can_research = False
        
        if location:
            # Check for library, computer, or other research tools
            research_tags = getattr(location.db, 'tags', []) or []
            if 'library' in research_tags or 'computer' in research_tags or 'research' in research_tags:
                can_research = True
        
        if not can_research:
            self.caller.msg("You need to be in a library, have access to a computer, or be in another location with research capabilities.")
            return
        
        self.caller.msg(f"|yYou begin researching '{topic}'...|n")
        
        # Use the general mystery discovery logic
        discovered_clues = self._attempt_mystery_discovery("research", research_topic=topic)
        
        if discovered_clues:
            self.caller.msg(f"|gYour research on '{topic}' uncovers:|n {', '.join(discovered_clues)}")
        else:
            self.caller.msg(f"|yYour research on '{topic}' provides some general background but no specific clues.|n")
    
    def occult_research(self):
        """Research occult topics for clues using the mystery system."""
        if not self.args:
            self.caller.msg("Usage: +mystery/occult <topic>")
            return
        
        topic = self.args.strip()
        
        # Check if character is in a location with occult research capabilities
        location = self.caller.location
        can_research = False
        
        if location:
            # Check for occult library, grimoire, or other occult research tools
            research_tags = getattr(location.db, 'tags', []) or []
            if 'occult_library' in research_tags or 'grimoire' in research_tags or 'occult_research' in research_tags:
                can_research = True
            # Also allow regular libraries for basic occult research
            elif 'library' in research_tags or 'research' in research_tags:
                can_research = True
        
        if not can_research:
            self.caller.msg("You need to be in an occult library, have access to grimoires, or be in another location with occult research capabilities.")
            return
        
        self.caller.msg(f"|yYou begin researching occult aspects of '{topic}'...|n")
        
        # Use the general mystery discovery logic with occult method
        discovered_clues = self._attempt_mystery_discovery("occult", research_topic=topic)
        
        if discovered_clues:
            self.caller.msg(f"|gYour occult research on '{topic}' reveals:|n {', '.join(discovered_clues)}")
        else:
            self.caller.msg(f"|yYour occult research on '{topic}' provides some esoteric knowledge but no specific clues.|n")
    
    def view_clue(self):
        """View details of a discovered clue."""
        if not self.args:
            self.caller.msg("Usage: +mystery/clue <clue_name>")
            return
        
        clue_name = self.args.strip().lower()
        
        # Check mystery clues that this character has discovered
        mystery_clues = getattr(self.caller.db, 'mystery_clues', {})
        found_clue = None
        
        if not mystery_clues:
            self.caller.msg("You haven't discovered any mystery clues yet.")
            return
        
        for mystery_id, clue_ids in mystery_clues.items():
            mystery = self._get_mystery(str(mystery_id))
            if mystery:
                # Check if mystery has clues data
                if not hasattr(mystery.db, 'clues') or mystery.db.clues is None:
                    self.caller.msg(f"|rError:|n Mystery {mystery_id} has corrupted clue data.")
                    continue
                    
                for clue_id in clue_ids:
                    clue = mystery.db.clues.get(clue_id, {})
                    if clue and clue.get('name', '').lower() == clue_name:
                        found_clue = (mystery, clue_id, clue)
                        break
            else:
                self.caller.msg(f"|rError:|n Mystery {mystery_id} not found.")
                continue
            if found_clue:
                break
        
        if found_clue:
            mystery, clue_id, clue = found_clue
            output = [
                f"|c=== {clue['name']} ===|n",
                f"|yMystery:|n {mystery.db.title}",
                f"|yDescription:|n {clue['description']}",
                ""
            ]
            
            # Show tags if any
            if clue.get('tags'):
                output.append(f"|yTags:|n {', '.join(clue['tags'])}")
            
            # Show leads if any
            if clue.get('leads_to'):
                lead_names = []
                for lead_id in clue['leads_to']:
                    lead_clue = mystery.db.clues.get(lead_id, {})
                    lead_names.append(lead_clue.get('name', lead_id))
                output.append(f"|yLeads to:|n {', '.join(lead_names)}")
            
            # Show revelation if character has discovered it and it exists
            if clue.get('revelation'):
                output.append(f"|yRevelation:|n {clue['revelation']}")
            
            self.caller.msg("\n".join(output))
        else:
            # Show available clues from all mysteries for easier reference
            all_available_clues = []
            for mystery_id, clue_ids in mystery_clues.items():
                mystery = self._get_mystery(str(mystery_id))
                if mystery and hasattr(mystery.db, 'clues') and mystery.db.clues:
                    for clue_id in clue_ids:
                        clue = mystery.db.clues.get(clue_id, {})
                        if clue:
                            all_available_clues.append(f"{mystery.db.title}: {clue['name']}")
            
            self.caller.msg(f"You don't have a mystery clue named '{clue_name}'.")
            if all_available_clues:
                self.caller.msg(f"|yYour discovered clues:|n")
                for clue_info in all_available_clues:
                    self.caller.msg(f"  {clue_info}")
            else:
                self.caller.msg("Use +mystery/progress to see your discovered clues.")
    
    def share_clue(self):
        """Share a mystery clue with another character."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/share <character> = <mystery_id>/<clue_name>")
            return
        
        char_name, clue_path = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +mystery/share <character> = <mystery_id>/<clue_name>")
            return
        
        mystery_id_str, clue_name = [x.strip() for x in clue_path.split("/", 1)]

        target = search_character(self.caller, char_name)
        if not target:
            return
        
        # Get the specific mystery
        try:
            mystery_id = int(mystery_id_str)
        except ValueError:
            self.caller.msg("Mystery ID must be a number.")
            return
        
        mystery = self._get_mystery(mystery_id_str)
        if not mystery:
            return
        
        # Check if the caller has discovered this clue in this mystery
        mystery_clues = getattr(self.caller.db, 'mystery_clues', {})
        if mystery_id not in mystery_clues:
            self.caller.msg(f"You haven't discovered any clues in mystery '{mystery.db.title}'.")
            return
        
        # Find the specific clue by name
        found_clue = None
        for clue_id in mystery_clues[mystery_id]:
            clue = mystery.db.clues.get(clue_id, {})
            if clue.get('name', '').lower() == clue_name.lower():
                found_clue = (clue_id, clue)
                break
        
        if not found_clue:
            available_clues = [mystery.db.clues[cid]['name'] for cid in mystery_clues[mystery_id]]
            self.caller.msg(f"You don't have a clue named '{clue_name}' in mystery '{mystery.db.title}'.")
            self.caller.msg(f"Your discovered clues: {', '.join(available_clues)}")
            return
        
        clue_id, clue = found_clue
        
        # Grant the clue to the target character
        success, msg = mystery.discover_clue(target, clue_id, "shared")
        if success:
            self.caller.msg(f"|gYou shared the mystery clue '{clue['name']}' from '{mystery.db.title}' with {target.name}.|n")
            target.msg(f"|y{self.caller.name} shared a mystery clue with you:|n {msg}")
        else:
            self.caller.msg(f"|rCouldn't share clue:|n {msg}")
    
    def collaborate(self):
        """Start a collaboration with another investigator."""
        if not self.args:
            self.caller.msg("Usage: +mystery/collaborate <character>")
            return
        
        search_term = self.args.strip()
        target = search_character(self.caller, search_term)

        if not target:
            return

        if target == self.caller:
            self.caller.msg("You can't collaborate with yourself.")
            return
        
        # Initialize collaboration tracking
        if not hasattr(self.caller.db, 'collaborations'):
            self.caller.db.collaborations = []
        if not hasattr(target.db, 'collaborations'):
            target.db.collaborations = []
        
        if target.id not in self.caller.db.collaborations:
            self.caller.db.collaborations.append(target.id)
            target.db.collaborations.append(self.caller.id)
            
            self.caller.msg(f"|gYou begin collaborating with {target.name} on investigations.|n")
            target.msg(f"|y{self.caller.name} wants to collaborate with you on investigations.|n")
            target.msg(f"|yYou can now share clues more easily and get bonuses when investigating together.|n")
        else:
            self.caller.msg(f"You're already collaborating with {target.name}.")
    
    # =============================================================================
    # STAFF MYSTERY MANAGEMENT METHODS
    # =============================================================================
    
    def create_mystery(self):
        """Create a new mystery."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/create <title> = <description>")
            return
            
        title, description = [x.strip() for x in self.args.split("=", 1)]
        
        mystery = MysteryManager.create_mystery(
            title=title,
            description=description,
            created_by=self.caller.id
        )
        
        if not mystery:
            self.caller.msg("|rError:|n Failed to create mystery. Check server logs for details.")
            return
            
        self.caller.msg(f"|gCreated mystery:|n {title} (ID: {mystery.id})")
        self.caller.msg(f"|yDescription:|n {description}")
    
    def list_mysteries_staff(self):
        """List all mysteries (staff view)."""
        category = self.args.strip() if self.args else None
        mysteries = MysteryManager.get_active_mysteries()
        
        if category:
            mysteries = [m for m in mysteries if m.db.category == category]
        
        if not mysteries:
            self.caller.msg("No mysteries found.")
            return

        headers = ["ID", "Title", "Category", "Progress", "Status"]
        rows = []
        for mystery in mysteries:
            title = mystery.db.title or f"Untitled Mystery #{mystery.id}"
            rows.append((
                mystery.id,
                title[:30],
                mystery.db.category or "",
                f"{mystery.db.completion_percentage}%",
                mystery.db.status or ""
            ))
        table = format_simple_table(headers, rows)
        self.caller.msg(f"\n{header('Active Mysteries (Staff View)')}\n{table}")
    
    def view_mystery_staff(self):
        """View detailed mystery information (staff view)."""
        if not self.args:
            self.caller.msg("Usage: +mystery/view <mystery_id>")
            return
            
        mystery_id = self.args.strip()
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        # Basic info
        output = [
            header(f"Mystery: {mystery.db.title}", char="="),
            f"|yID:|n {mystery.id}",
            f"|yDescription:|n {mystery.db.description}",
            f"|yCategory:|n {mystery.db.category}",
            f"|yDifficulty:|n {mystery.db.difficulty}/5",
            f"|yStatus:|n {mystery.db.status}",
            f"|yProgress:|n {mystery.db.completion_percentage}%",
            f"|yCreated:|n {mystery.db.created_date.strftime('%Y-%m-%d %H:%M')}",
            ""
        ]
        
        # Clues
        if mystery.db.clues:
            output.append("|yClues:|n")
            for clue_id, clue in mystery.db.clues.items():
                discovered_count = len(clue['discovered_by'])
                tags = ", ".join(clue['tags']) if clue['tags'] else "None"
                prereqs = ", ".join(clue['prerequisite_clues']) if clue['prerequisite_clues'] else "None"
                
                clue_type = clue.get('clue_type', 'general')
                required_methods = clue.get('required_methods', [])
                methods_str = ', '.join(required_methods) if required_methods else 'any'
                
                output.append(f"  |w{clue_id}:|n {clue['name']}")
                output.append(f"    Description: {clue['description'][:50]}...")
                output.append(f"    Type: {clue_type} | Methods: {methods_str}")
                output.append(f"    Discovered by: {discovered_count} character(s)")
                output.append(f"    Tags: {tags}")
                output.append(f"    Prerequisites: {prereqs}")
                output.append("")
        else:
            output.append("|yClues:|n None")
        
        # Access restrictions
        if mystery.db.allowed_templates:
            output.append(f"|yAllowed Templates:|n {', '.join(mystery.db.allowed_templates)}")
        if mystery.db.allowed_characters:
            output.append(f"|yAllowed Characters:|n {len(mystery.db.allowed_characters)} specific")
        if mystery.db.restricted_areas:
            output.append(f"|yRestricted Areas:|n {', '.join(mystery.db.restricted_areas)}")
        
        self.caller.msg("\n".join(output))
    
    def add_clue(self):
        """Add a clue to a mystery."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/addclue <mystery_id> = <name>/<description>")
            return
            
        mystery_id, clue_info = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_info:
            self.caller.msg("Usage: +mystery/addclue <mystery_id> = <name>/<description>")
            return
            
        name, description = [x.strip() for x in clue_info.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        clue_id = mystery.add_clue(name, description)
        self.caller.msg(f"|gAdded clue to {mystery.db.title}:|n {name} (ID: {clue_id})")
    
    def set_prerequisites(self):
        """Set prerequisite clues for a clue."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/prereq <mystery_id>/<clue_id> = <prerequisite_clue_ids>")
            return
            
        clue_path, prereqs = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +mystery/prereq <mystery_id>/<clue_id> = <prerequisite_clue_ids>")
            return
            
        mystery_id, clue_id = [x.strip() for x in clue_path.split("/", 1)]
        prereq_list = [x.strip() for x in prereqs.split(",") if x.strip()]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue {clue_id} not found in mystery {mystery_id}")
            return
        
        mystery.set_clue_prerequisites(clue_id, prereq_list)
        self.caller.msg(f"|gSet prerequisites for {clue_id}:|n {', '.join(prereq_list)}")
    
    def set_skillroll(self):
        """Set skill roll conditions using shorthand syntax: skill/attribute/difficulty."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/skillroll <mystery_id>/<clue_id> = <skill>/<attribute>/<difficulty>")
            return
        
        path, skillroll_str = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in path:
            self.caller.msg("Usage: +mystery/skillroll <mystery_id>/<clue_id> = <skill>/<attribute>/<difficulty>")
            return
        
        mystery_id, clue_id = [x.strip() for x in path.split("/", 1)]
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue '{clue_id}' not found in mystery.")
            return
        
        # Parse skill/attribute/difficulty
        parts = skillroll_str.split("/")
        if len(parts) != 3:
            self.caller.msg("Format: <skill>/<attribute>/<difficulty>")
            self.caller.msg("Example: larceny/dexterity/2")
            return
        
        skill, attribute, difficulty_str = [x.strip() for x in parts]
        
        try:
            difficulty = int(difficulty_str)
        except ValueError:
            self.caller.msg("Difficulty must be a number.")
            return
        
        # Create the skill_roll condition
        skill_roll_condition = {
            "skill_roll": {
                "skill": skill,
                "attribute": attribute,
                "difficulty": difficulty
            }
        }
        
        # Update or create discovery conditions
        if 'discovery_conditions' not in mystery.db.clues[clue_id]:
            mystery.db.clues[clue_id]['discovery_conditions'] = {}
        
        mystery.db.clues[clue_id]['discovery_conditions'].update(skill_roll_condition)
        
        self.caller.msg(f"|gSet skill roll for {clue_id}: {attribute.title()} + {skill.title()} (difficulty {difficulty})|n")
    
    def grant_clue(self):
        """Manually grant a clue to a character."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/grant <character> = <mystery_id>/<clue_id>")
            return
            
        char_name, clue_path = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +mystery/grant <character> = <mystery_id>/<clue_id>")
            return
            
        mystery_id, clue_id = [x.strip() for x in clue_path.split("/", 1)]
        
        character = search_character(self.caller, char_name)
        if not character:
            return
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        success, msg = mystery.discover_clue(character, clue_id, "staff_grant")
        if success:
            self.caller.msg(f"|gGranted clue to {character.name}:|n {msg}")
            character.msg(f"|yA staff member has granted you a clue:|n {msg}")
        else:
            self.caller.msg(f"|rFailed to grant clue:|n {msg}")
    
    def show_staff_progress(self):
        """Show detailed mystery progress (staff view)."""
        if self.args:
            mystery_id = self.args.strip()
            mystery = self._get_mystery(mystery_id)
            if not mystery:
                return
            mysteries = [mystery]
        else:
            mysteries = MysteryManager.get_active_mysteries()
        
        for mystery in mysteries:
            total_clues = len(mystery.db.clues)
            discovered_count = len(set().union(*mystery.db.discovered_clues.values())) if mystery.db.discovered_clues else 0
            
            self.caller.msg(f"|c{mystery.db.title}|n (ID: {mystery.id})")
            self.caller.msg(f"  Progress: {mystery.db.completion_percentage}% ({discovered_count}/{total_clues} clues discovered)")
            self.caller.msg(f"  Participants: {len(mystery.db.discovered_clues)} characters")
            self.caller.msg("")
    
    # =============================================================================
    # CLUE OBJECT MANAGEMENT METHODS
    # =============================================================================
    
    def handle_clueobj_commands(self):
        """Handle clue object subcommands."""
        if not check_mystery_permission(self.caller):
            self.caller.msg(format_permission_error("Staff or Storyteller"))
            return
            
        switch = self.clueobj_switch
        
        if switch == "create":
            self.create_clue_object()
        elif switch == "edit":
            self.edit_clue_object()
        elif switch == "list":
            self.list_clue_objects()
        elif switch == "delete":
            self.delete_clue_object()
        else:
            self.caller.msg("Invalid clue object command.")
    
    def create_clue_object(self):
        """Create a new clue object."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/clueobj/create <name> = <mystery_id>/<clue_id>")
            return
            
        name, clue_path = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +mystery/clueobj/create <name> = <mystery_id>/<clue_id>")
            return
            
        mystery_id, clue_id = [x.strip() for x in clue_path.split("/", 1)]
        
        # Create the clue object
        clue_obj, errors = ClueObject.create(
            name,
            location=self.caller.location,
            home=self.caller.location
        )
        
        if errors:
            self.caller.msg(f"|rError:|n Failed to create clue object: {errors}")
            return
        
        clue_obj.db.mystery_id = mystery_id
        clue_obj.db.clue_id = clue_id
        clue_obj.db.desc = f"This appears to be related to an ongoing investigation."
        
        self.caller.msg(f"|gCreated clue object:|n {name} linked to {mystery_id}/{clue_id}")
    
    # =============================================================================
    # SHARED UTILITY METHODS
    # =============================================================================
    
    def _attempt_mystery_discovery(self, method_type, target_object=None, research_topic=None):
        """
        Attempt to discover mystery clues using specified method.
        
        Args:
            method_type (str): Type of discovery method ('search', 'examine', 'interview', 'research')
            target_object (Object, optional): Specific object being examined/interviewed
            research_topic (str, optional): Topic being researched
            
        Returns:
            list: Names of discovered clues
        """
        # Get mysteries that have clues available
        mysteries = MysteryManager.get_active_mysteries()
        available_clues = []
        
        for mystery in mysteries:
            mystery_available = mystery.get_available_clues(self.caller)
            for clue_id in mystery_available:
                clue = mystery.db.clues[clue_id]
                
                # Check if clue can be discovered by this method
                required_methods = clue.get('required_methods', [])
                skill_hints = clue.get('skill_hints', [])
                location_hints = clue.get('location_hints', [])
                
                # Method filtering - check required methods first
                if required_methods and method_type not in required_methods:
                    continue
                
                # Location filtering (not applicable for research/occult)
                if method_type not in ['research', 'occult'] and location_hints and self.caller.location:
                    room_key = self.caller.location.key.lower()
                    room_tags = [t.lower() if isinstance(t, str) else str(t).lower()
                                 for t in (getattr(self.caller.location.db, 'tags', None) or [])]
                    hint_set = {h.lower() if isinstance(h, str) else str(h).lower() for h in location_hints}
                    if hint_set and room_key not in hint_set and not (hint_set & set(room_tags)):
                        continue
                
                # Legacy skill hints filtering (for backward compatibility)
                if skill_hints and method_type not in skill_hints:
                    continue
                    
                # Object-specific filtering for examine
                if target_object and method_type == 'examine':
                    object_hints = clue.get('object_hints', [])
                    if object_hints:
                        target_key = target_object.key.lower()
                        hint_keys = {h.lower() if isinstance(h, str) else str(h).lower() for h in object_hints}
                        if target_key not in hint_keys:
                            continue
                # NPC/character-specific filtering for interview
                if target_object and method_type == 'interview':
                    social_hints = clue.get('social_hints', [])
                    if social_hints:
                        target_key = target_object.key.lower()
                        hint_keys = {h.lower() if isinstance(h, str) else str(h).lower() for h in social_hints}
                        if target_key not in hint_keys:
                            continue
                
                # Topic-specific filtering for research and occult
                if research_topic and method_type in ['research', 'occult']:
                    clue_desc = clue.get('description', '').lower()
                    clue_name = clue.get('name', '').lower()
                    if research_topic.lower() not in clue_desc and research_topic.lower() not in clue_name:
                        continue
                
                available_clues.append((mystery, clue_id, clue))
        
        if not available_clues:
            return []
        
        # Determine skill/attribute to use based on method
        attribute, skill, skill_category = self._get_skill_for_method(method_type, available_clues)
        
        # Get attribute and skill values
        attr_value = self._get_attribute_value(attribute)
        
        # Special handling for examine method (Resolve + Composure)
        if method_type == 'examine' and skill == 'composure':
            skill_value = self._get_attribute_value('composure')
            dice_pool = attr_value + skill_value
        else:
            skill_value = self._get_skill_value(skill, skill_category)
            dice_pool = attr_value + skill_value
        
        self.caller.msg(f"Rolling {attribute.title()} + {skill.title()}: {dice_pool} dice")
        
        # Make the roll
        successes = sum(1 for _ in range(dice_pool) if secrets.randbelow(10) + 1 >= 8)
        
        if successes == 0:
            return []
        
        # Determine how many clues to discover
        if successes >= 3:
            self.caller.msg(f"|gExceptional Success! ({successes} successes)|n")
            clues_to_discover = min(2, len(available_clues))
        else:
            self.caller.msg(f"|gSuccess! ({successes} successes)|n")
            clues_to_discover = 1
        
        # Attempt to discover clues
        discovered = []
        for i in range(min(clues_to_discover, len(available_clues))):
            mystery, clue_id, clue = available_clues[i]
            
            # Check if specific clue's difficulty requirements are met
            discovery_conditions = clue.get('discovery_conditions', {})
            if 'skill_roll' in discovery_conditions:
                required_difficulty = discovery_conditions['skill_roll'].get('difficulty', 2)
                if successes < required_difficulty:
                    continue
            
            success, msg = mystery.discover_clue(self.caller, clue_id, method_type)
            if success:
                discovered.append(clue['name'])
        
        return discovered
    
    def _get_skill_for_method(self, method_type, available_clues):
        """Determine the skill/attribute combination based on investigation method."""
        # Method-specific skill combinations
        method_skills = {
            'examine': ('resolve', 'composure', 'mental'),  # Perception check
            'search': ('wits', 'investigation', 'mental'),
            'interview': (self._get_best_social_attribute(), 'persuasion', 'social'),
            'research': ('intelligence', 'academics', 'mental'),
            'occult': ('intelligence', 'occult', 'mental')
        }
        
        # Get default skill for this method
        if method_type in method_skills:
            if method_type == 'examine':
                # Special case: Resolve + Composure (both attributes)
                resolve_val = self._get_attribute_value('resolve')
                composure_val = self._get_attribute_value('composure')
                # Return composure as the "skill" since we'll add resolve + composure
                return 'resolve', 'composure', 'mental'
            else:
                attribute, skill, skill_category = method_skills[method_type]
                return attribute, skill, skill_category
        
        # Check if any clues have specific skill requirements that override defaults
        for mystery, clue_id, clue in available_clues:
            discovery_conditions = clue.get('discovery_conditions', {})
            if 'skill_roll' in discovery_conditions:
                skill_req = discovery_conditions['skill_roll']
                skill = skill_req.get('skill', 'investigation')
                attribute = skill_req.get('attribute', 'wits')
                
                # Determine skill category
                if skill in ['investigation', 'academics', 'computer', 'crafts', 'medicine', 'occult', 'science']:
                    skill_category = "mental"
                elif skill in ['athletics', 'brawl', 'drive', 'firearms', 'larceny', 'stealth', 'survival', 'weaponry']:
                    skill_category = "physical"
                elif skill in ['animal_ken', 'empathy', 'expression', 'intimidation', 'persuasion', 'socialize', 'streetwise', 'subterfuge']:
                    skill_category = "social"
        return attribute, skill, skill_category
        
        # Default fallback
        return 'wits', 'investigation', 'mental'
    
    def _get_attribute_value(self, attribute):
        """Get the value of an attribute from the character."""
        # Check if character has modern stats structure (like Soma)
        if hasattr(self.caller.db, 'stats') and self.caller.db.stats:
            attributes = self.caller.db.stats.get("attributes", {})
            if attributes and attribute in attributes:
                return attributes.get(attribute, 1)
        
        # Check legacy attribute structure (categorized)
        if hasattr(self.caller.db, 'attributes') and self.caller.db.attributes:
            # Check if it's the old categorized structure
            if isinstance(self.caller.db.attributes, dict):
                mental_attrs = self.caller.db.attributes.get("mental", {})
                physical_attrs = self.caller.db.attributes.get("physical", {})
                social_attrs = self.caller.db.attributes.get("social", {})
                
                if attribute in mental_attrs:
                    return mental_attrs.get(attribute, 1)
                elif attribute in physical_attrs:
                    return physical_attrs.get(attribute, 1)
                elif attribute in social_attrs:
                    return social_attrs.get(attribute, 1)
        else:
                    # Try to get wits as default from mental
                    return mental_attrs.get("wits", 1)
        
        # Check for individual attribute storage (very legacy)
        if hasattr(self.caller.db, attribute):
            return getattr(self.caller.db, attribute, 1)
        
        # Final fallback - return 1
        return 1
    
    def _get_best_social_attribute(self):
        """Get the higher of Presence or Manipulation for social rolls."""
        presence = self._get_attribute_value('presence')
        manipulation = self._get_attribute_value('manipulation')
        return 'presence' if presence >= manipulation else 'manipulation'
    
    def _get_skill_value(self, skill, skill_category):
        """Get the value of a skill from the character."""
        # Check if character has modern stats structure (like Soma)
        if hasattr(self.caller.db, 'stats') and self.caller.db.stats:
            skills = self.caller.db.stats.get("skills", {})
            if skills and skill in skills:
                return skills.get(skill, 0)
        
        # Final fallback - return 0
        return 0
    
    def _get_method_hint(self, attempted_method):
        """Get a hint about what methods might work for available clues."""
        mysteries = MysteryManager.get_active_mysteries()
        available_methods = set()
        
        for mystery in mysteries:
            mystery_available = mystery.get_available_clues(self.caller)
            for clue_id in mystery_available:
                clue = mystery.db.clues[clue_id]
                required_methods = clue.get('required_methods', [])
                if required_methods:
                    available_methods.update(required_methods)
        
        # Remove the method they just tried
        available_methods.discard(attempted_method)
        
        if available_methods:
            method_list = sorted(list(available_methods))
            return f"|cHint:|n Try using +mystery/{' or +mystery/'.join(method_list)} for other types of clues."
        
        return None
    
    def _get_mystery(self, mystery_id):
        """Get a mystery by ID."""
        try:
            mystery_id = int(mystery_id)
        except ValueError:
            self.caller.msg("Mystery ID must be a number.")
            return None
        
        # Scripts need to be searched differently than objects
        from evennia.scripts.models import ScriptDB
        try:
            mystery = ScriptDB.objects.get(id=mystery_id)
            
            # Verify it's actually a Mystery with the expected methods
            if not hasattr(mystery, 'can_discover_clue'):
                self.caller.msg(f"Object {mystery_id} is not a mystery script.")
                return None
            return mystery
        except ScriptDB.DoesNotExist:
            self.caller.msg(f"Mystery {mystery_id} not found.")
            return None
    
    # =============================================================================
    # PLACEHOLDER METHODS FOR MISSING FUNCTIONALITY
    # =============================================================================
    
    def edit_mystery(self):
        """Edit mystery properties: description, category, or difficulty."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/edit <mystery_id>/<field> = <value>")
            self.caller.msg("Fields: desc, category, diff")
            return
            
        path, value = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in path:
            self.caller.msg("Usage: +mystery/edit <mystery_id>/<field> = <value>")
            return
            
        mystery_id, field = [x.strip() for x in path.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        field = field.lower()
        
        if field == "desc":
            mystery.db.description = value
            self.caller.msg(f"Updated description for '{mystery.db.title}'.")
        elif field == "category":
            mystery.db.category = value
            self.caller.msg(f"Updated category for '{mystery.db.title}' to '{value}'.")
        elif field == "diff":
            try:
                difficulty = int(value)
                if difficulty < 1 or difficulty > 10:
                    self.caller.msg("Difficulty must be between 1 and 10.")
                    return
                mystery.db.difficulty = difficulty
                self.caller.msg(f"Updated difficulty for '{mystery.db.title}' to {difficulty}.")
            except ValueError:
                self.caller.msg("Difficulty must be a number between 1 and 10.")
        else:
            self.caller.msg("Valid fields: desc, category, diff")
    
    def delete_mystery(self):
        """Delete a mystery entirely, including all associated clues and clue objects."""
        if not self.args:
            self.caller.msg("Usage: +mystery/delete <mystery_id>")
            return
            
        mystery_id = self.args.strip()
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        mystery_title = mystery.db.title
        
        # Delete any associated clue objects first
        from typeclasses.mysteries import ClueObject
        clue_objects = ClueObject.objects.all()
        deleted_objects = 0
        
        for obj in clue_objects:
            if hasattr(obj.db, 'mystery_id') and str(obj.db.mystery_id) == str(mystery_id):
                obj.delete()
                deleted_objects += 1
        
        # Delete the mystery script itself
        mystery.delete()
        
        self.caller.msg(f"Deleted mystery '{mystery_title}' (ID: {mystery_id}).")
        if deleted_objects > 0:
            self.caller.msg(f"Also deleted {deleted_objects} associated clue object(s).")
    
    def set_status(self):
        """Set mystery status: Active, Hold, Complete, Cancelled."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/status <mystery_id> = <status>")
            self.caller.msg("Valid statuses: Active, Hold, Complete, Cancelled")
            return
            
        mystery_id, status = [x.strip() for x in self.args.split("=", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        valid_statuses = ["active", "hold", "complete", "cancelled"]
        status_lower = status.lower()
        
        if status_lower not in valid_statuses:
            self.caller.msg(f"Invalid status. Valid statuses: {', '.join([s.title() for s in valid_statuses])}")
            return
            
        mystery.db.status = status_lower
        self.caller.msg(f"Set status of '{mystery.db.title}' to {status.title()}.")
    
    def edit_clue(self):
        """Edit clue properties: description, tags, prerequisites, object or NPC hints."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/editclue <mystery_id>/<clue_id> = <field>/<value>")
            self.caller.msg("Fields: desc, tags, prereq, obj, social, location")
            self.caller.msg("  obj - object keys that reveal clue when examined")
            self.caller.msg("  social - NPC/char keys that reveal clue when interviewed")
            self.caller.msg("  location - room keys or room tags (library, crime_scene) where clue can be found")
            return
            
        path, edit_info = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in path:
            self.caller.msg("Usage: +mystery/editclue <mystery_id>/<clue_id> = <field>/<value>")
            return
            
        if "/" not in edit_info:
            self.caller.msg("Usage: +mystery/editclue <mystery_id>/<clue_id> = <field>/<value>")
            return
            
        mystery_id, clue_id = [x.strip() for x in path.split("/", 1)]
        field, value = [x.strip() for x in edit_info.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue '{clue_id}' not found in mystery {mystery_id}.")
            return
            
        clue = mystery.db.clues[clue_id]
        field = field.lower()
        
        if field == "desc":
            clue['description'] = value
            self.caller.msg(f"Updated description for clue '{clue['name']}'.")
        elif field == "tags":
            # Parse comma-separated tags
            tags = [tag.strip() for tag in value.split(",") if tag.strip()]
            clue['tags'] = tags
            self.caller.msg(f"Updated tags for clue '{clue['name']}' to: {', '.join(tags)}")
        elif field == "prereq":
            prereqs = [prereq.strip() for prereq in value.split(",") if prereq.strip()]
            clue['prerequisite_clues'] = prereqs
            self.caller.msg(f"Updated prerequisites for clue '{clue['name']}' to: {', '.join(prereqs)}")
        elif field == "obj":
            objects = [o.strip() for o in value.split(",") if o.strip()]
            clue['object_hints'] = objects
            self.caller.msg(f"Updated object hints for clue '{clue['name']}' to: {', '.join(objects)}")
        elif field == "social":
            npcs = [n.strip() for n in value.split(",") if n.strip()]
            clue['social_hints'] = npcs
            self.caller.msg(f"Updated social/NPC hints for clue '{clue['name']}' to: {', '.join(npcs)}")
        elif field == "location":
            locations = [l.strip() for l in value.split(",") if l.strip()]
            clue['location_hints'] = locations
            self.caller.msg(f"Updated location hints for clue '{clue['name']}' to: {', '.join(locations)}")
        else:
            self.caller.msg("Valid fields: desc, tags, prereq, obj, social, location")
    
    def delete_clue(self):
        """Delete a clue from a mystery."""
        if "/" not in self.args:
            self.caller.msg("Usage: +mystery/delclue <mystery_id>/<clue_id>")
            return
            
        mystery_id, clue_id = [x.strip() for x in self.args.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue '{clue_id}' not found in mystery {mystery_id}.")
            return
            
        clue_name = mystery.db.clues[clue_id]['name']
        
        # Remove the clue
        del mystery.db.clues[clue_id]
        
        # Clean up any references to this clue in other clues' prerequisites or leads
        for other_clue_id, other_clue in mystery.db.clues.items():
            if clue_id in other_clue.get('prerequisite_clues', []):
                other_clue['prerequisite_clues'].remove(clue_id)
            if clue_id in other_clue.get('leads_to', []):
                other_clue['leads_to'].remove(clue_id)
        
        # Clean up any character discovery records
        for char_id, discovered_clues in mystery.db.discovered_clues.items():
            if clue_id in discovered_clues:
                discovered_clues.remove(clue_id)
        
        self.caller.msg(f"Deleted clue '{clue_name}' (ID: {clue_id}) from mystery '{mystery.db.title}'.")
    
    def set_leads(self):
        """Set which clues lead to other clues."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/leads <mystery_id>/<first_clue_id> = <second_clue_id>[,<third_clue_id>,...]")
            return
            
        path, leads_str = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in path:
            self.caller.msg("Usage: +mystery/leads <mystery_id>/<first_clue_id> = <second_clue_id>[,<third_clue_id>,...]")
            return
            
        mystery_id, clue_id = [x.strip() for x in path.split("/", 1)]
        leads_list = [x.strip() for x in leads_str.split(",") if x.strip()]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue '{clue_id}' not found in mystery {mystery_id}.")
            return
            
        # Validate that all lead clues exist
        invalid_leads = []
        for lead_clue in leads_list:
            if lead_clue not in mystery.db.clues:
                invalid_leads.append(lead_clue)
        
        if invalid_leads:
            self.caller.msg(f"Invalid clue IDs: {', '.join(invalid_leads)}")
            return
            
        mystery.db.clues[clue_id]['leads_to'] = leads_list
        clue_name = mystery.db.clues[clue_id]['name']
        
        if leads_list:
            lead_names = [mystery.db.clues[lead_id]['name'] for lead_id in leads_list]
            self.caller.msg(f"Set leads for '{clue_name}' to: {', '.join(lead_names)}")
        else:
            self.caller.msg(f"Cleared all leads for '{clue_name}'.")
    
    def set_clue_type(self):
        """Set the type of a clue (determines required discovery methods)."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/cluetype <mystery_id>/<clue_id> = <type>")
            self.caller.msg("Valid types: academic, occult, physical, hidden, social, general")
            return
            
        path, clue_type = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in path:
            self.caller.msg("Usage: +mystery/cluetype <mystery_id>/<clue_id> = <type>")
            return
            
        mystery_id, clue_id = [x.strip() for x in path.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        success, msg = mystery.set_clue_type(clue_id, clue_type.lower())
        if success:
            clue_name = mystery.db.clues[clue_id]['name']
            required_methods = mystery.db.clues[clue_id]['required_methods']
            self.caller.msg(f"Set type for '{clue_name}' to {clue_type}.")
            if required_methods:
                self.caller.msg(f"Required methods: {', '.join(required_methods)}")
            else:
                self.caller.msg("Can be discovered by any method.")
        else:
            self.caller.msg(f"Error: {msg}")
    
    def set_clue_methods(self):
        """Manually set required discovery methods for a clue."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/methods <mystery_id>/<clue_id> = <method1,method2>")
            self.caller.msg("Valid methods: examine, search, interview, research, occult")
            return
            
        path, methods_str = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in path:
            self.caller.msg("Usage: +mystery/methods <mystery_id>/<clue_id> = <method1,method2>")
            return
            
        mystery_id, clue_id = [x.strip() for x in path.split("/", 1)]
        methods_list = [x.strip() for x in methods_str.split(",") if x.strip()]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        success, msg = mystery.set_clue_required_methods(clue_id, methods_list)
        if success:
            clue_name = mystery.db.clues[clue_id]['name']
            if methods_list:
                self.caller.msg(f"Set required methods for '{clue_name}': {', '.join(methods_list)}")
            else:
                self.caller.msg(f"Cleared required methods for '{clue_name}' - can be discovered by any method.")
        else:
            self.caller.msg(f"Error: {msg}")
    
    def set_conditions(self):
        """Set discovery conditions for a clue."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/conditions <mystery_id>/<clue_id> = <conditions>")
            self.caller.msg("Examples:")
            self.caller.msg("  skill:investigation:3 (requires Investigation 3+)")
            self.caller.msg("  template:vampire (requires Vampire template)")
            self.caller.msg("  clan:ventrue (requires Ventrue clan)")
            self.caller.msg("  participant (visible to mystery participants only)")
            self.caller.msg("  open (visible to anyone)")
            return
            
        path, conditions_str = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in path:
            self.caller.msg("Usage: +mystery/conditions <mystery_id>/<clue_id> = <conditions>")
            return
            
        mystery_id, clue_id = [x.strip() for x in path.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue '{clue_id}' not found in mystery {mystery_id}.")
            return
            
        # Parse conditions
        conditions = {}
        condition_parts = [x.strip() for x in conditions_str.split(",")]
        
        for condition in condition_parts:
            if condition.lower() == "open":
                conditions['access_level'] = 'open'
            elif condition.lower() == "participant":
                conditions['access_level'] = 'participant'
            elif ":" in condition:
                parts = condition.split(":")
                if len(parts) == 3 and parts[0].lower() == "skill":
                    # skill:investigation:3
                    skill_name, level = parts[1], parts[2]
                    try:
                        level = int(level)
                        if 'skill_requirements' not in conditions:
                            conditions['skill_requirements'] = {}
                        conditions['skill_requirements'][skill_name] = level
                    except ValueError:
                        self.caller.msg(f"Invalid skill level: {level}")
                        return
                elif len(parts) == 2:
                    # template:vampire or clan:ventrue
                    req_type, req_value = parts[0].lower(), parts[1].lower()
                    if req_type in ['template', 'clan', 'tribe', 'order', 'kith', 'seeming', 'auspice', 'covenant']:
                        if 'bio_requirements' not in conditions:
                            conditions['bio_requirements'] = {}
                        conditions['bio_requirements'][req_type] = req_value
                    else:
                        self.caller.msg(f"Unknown requirement type: {req_type}")
                        return
            else:
                self.caller.msg(f"Invalid condition format: {condition}")
                return
        
        mystery.db.clues[clue_id]['discovery_conditions'] = conditions
        clue_name = mystery.db.clues[clue_id]['name']
        self.caller.msg(f"Set discovery conditions for '{clue_name}': {conditions_str}")
    
    def add_revelation(self):
        """Add revelation information for exceptional success on a clue."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/revelation <mystery_id>/<clue_id> = <revelation_text>")
            return
            
        path, revelation_text = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in path:
            self.caller.msg("Usage: +mystery/revelation <mystery_id>/<clue_id> = <revelation_text>")
            return
            
        mystery_id, clue_id = [x.strip() for x in path.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue '{clue_id}' not found in mystery {mystery_id}.")
            return
            
        mystery.db.clues[clue_id]['revelation'] = revelation_text
        clue_name = mystery.db.clues[clue_id]['name']
        self.caller.msg(f"Set revelation for '{clue_name}': {revelation_text[:50]}{'...' if len(revelation_text) > 50 else ''}")
    
    def set_access(self):
        """Set access restrictions for the entire mystery."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/access <mystery_id> = <access_rules>")
            self.caller.msg("Examples:")
            self.caller.msg("  group:vampires (requires membership in 'vampires' group)")
            self.caller.msg("  template:vampire (requires Vampire template)")
            self.caller.msg("  clan:ventrue (requires Ventrue clan)")
            self.caller.msg("  skill:investigation:3 (requires Investigation 3+)")
            self.caller.msg("  open (accessible to anyone)")
            return
            
        mystery_id, access_str = [x.strip() for x in self.args.split("=", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        # Parse access rules
        access_rules = []
        rule_parts = [x.strip() for x in access_str.split(",")]
        
        for rule in rule_parts:
            if rule.lower() == "open":
                mystery.db.allowed_templates = []
                mystery.db.allowed_characters = []
                mystery.db.access_rules = {'type': 'open'}
                self.caller.msg(f"Set '{mystery.db.title}' to open access.")
                return
            elif ":" in rule:
                parts = rule.split(":")
                if len(parts) == 2:
                    rule_type, rule_value = parts[0].lower(), parts[1].lower()
                    if rule_type == "group":
                        access_rules.append({'type': 'group', 'value': rule_value})
                    elif rule_type in ['template', 'clan', 'tribe', 'order', 'kith', 'seeming', 'auspice', 'covenant']:
                        access_rules.append({'type': rule_type, 'value': rule_value})
                elif len(parts) == 3 and parts[0].lower() == "skill":
                    skill_name, level = parts[1], parts[2]
                    try:
                        level = int(level)
                        access_rules.append({'type': 'skill', 'skill': skill_name, 'level': level})
                    except ValueError:
                        self.caller.msg(f"Invalid skill level: {level}")
                        return
        
        mystery.db.access_rules = access_rules
        self.caller.msg(f"Set access rules for '{mystery.db.title}': {access_str}")
    
    def show_discovered(self):
        """Show discovered clues for a mystery."""
        if not self.args:
            self.caller.msg("Usage: +mystery/discovered <mystery_id> [character]")
            return
            
        args = self.args.strip().split()
        mystery_id = args[0]
        character_name = args[1] if len(args) > 1 else None
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        if character_name:
            # Show discoveries for specific character
            character = search_character(self.caller, character_name)
            if not character:
                return
            
            discovered_clues = mystery.get_discovered_clues(character)
            if not discovered_clues:
                self.caller.msg(f"{character.name} hasn't discovered any clues in {mystery.db.title}.")
                return
                
            output = [f"|c{character.name}'s discoveries in {mystery.db.title}:|n"]
            for clue_id in discovered_clues:
                clue = mystery.db.clues.get(clue_id, {})
                output.append(f"  |w{clue.get('name', 'Unknown')}|n - {clue.get('description', '')[:50]}...")
            
            self.caller.msg("\n".join(output))
        else:
            # Show all discoveries for the mystery
            if not mystery.db.discovered_clues:
                self.caller.msg(f"No clues have been discovered in {mystery.db.title}.")
                return
                
            output = [f"|cAll discoveries in {mystery.db.title}:|n"]
            
            for char_id, clue_ids in mystery.db.discovered_clues.items():
                from evennia.utils import search
                character = search.search_object(f"#{char_id}")
                char_name = character[0].name if character else f"Character #{char_id}"
                
                output.append(f"\n|w{char_name}:|n")
                for clue_id in clue_ids:
                    clue = mystery.db.clues.get(clue_id, {})
                    output.append(f"  - {clue.get('name', 'Unknown')}")
            
            self.caller.msg("\n".join(output))
    
    def revoke_clue(self):
        """Revoke a clue from a character."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/revoke <character> = <mystery_id>/<clue_id>")
            return
            
        char_name, clue_path = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +mystery/revoke <character> = <mystery_id>/<clue_id>")
            return
            
        mystery_id, clue_id = [x.strip() for x in clue_path.split("/", 1)]
        
        character = search_character(self.caller, char_name)
        if not character:
            return
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue '{clue_id}' not found in mystery {mystery_id}.")
            return
            
        char_id = character.id
        clue_name = mystery.db.clues[clue_id]['name']
        
        # Remove from mystery's discovered clues
        if char_id in mystery.db.discovered_clues and clue_id in mystery.db.discovered_clues[char_id]:
            mystery.db.discovered_clues[char_id].remove(clue_id)
            
            # Remove from character's personal clue list
            if hasattr(character.db, 'mystery_clues') and character.db.mystery_clues and mystery.id in character.db.mystery_clues:
                if clue_id in character.db.mystery_clues[mystery.id]:
                    character.db.mystery_clues[mystery.id].remove(clue_id)
            
            # Remove from clue's discovered_by list
            if char_id in mystery.db.clues[clue_id]['discovered_by']:
                mystery.db.clues[clue_id]['discovered_by'].remove(char_id)
            
            self.caller.msg(f"Revoked clue '{clue_name}' from {character.name}.")
            character.msg(f"A staff member has revoked the mystery clue '{clue_name}' from you.")
        else:
            self.caller.msg(f"{character.name} doesn't have the clue '{clue_name}'.")
    
    def add_participant(self):
        """Add a character as a participant in a mystery."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/participant <mystery_id> = <character>")
            return
            
        mystery_id, char_name = [x.strip() for x in self.args.split("=", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        character = search_character(self.caller, char_name)
        if not character:
            return
        
        # Initialize participants list if it doesn't exist
        if not hasattr(mystery.db, 'participants') or mystery.db.participants is None:
            mystery.db.participants = []
            
        char_id = character.id
        if char_id not in mystery.db.participants:
            mystery.db.participants.append(char_id)
            self.caller.msg(f"Added {character.name} as a participant in '{mystery.db.title}'.")
            character.msg(f"You have been added as a participant in the mystery '{mystery.db.title}'.")
        else:
            self.caller.msg(f"{character.name} is already a participant in '{mystery.db.title}'.")
    
    def list_templates(self):
        """List mystery templates."""
        self.caller.msg("Mystery templates functionality not yet implemented.")
    
    def create_from_template(self):
        """Create mystery from template."""
        self.caller.msg("Template creation functionality not yet implemented.")
    
    def edit_clue_object(self):
        """Edit a clue object's properties."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/clueobj/edit <object> = <field>/<value>")
            return
            
        obj_name, edit_info = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in edit_info:
            self.caller.msg("Usage: +mystery/clueobj/edit <object> = <field>/<value>")
            return
            
        field, value = [x.strip() for x in edit_info.split("/", 1)]
        
        clue_obj = self.caller.search(obj_name)
        if not clue_obj or not isinstance(clue_obj, ClueObject):
            self.caller.msg("Clue object not found.")
            return
        
        # Whitelist allowed clue object fields for security
        allowed_fields = {'discovery_message', 'skill_required', 'difficulty', 'hidden'}
        if field not in allowed_fields:
            self.caller.msg(f"|rField '{field}' is not allowed. Valid fields: {', '.join(allowed_fields)}|n")
            return
            
        if field == 'difficulty':
            try:
                value = int(value)
            except ValueError:
                self.caller.msg("Difficulty must be a number.")
                return
        elif field == 'hidden':
            value = value.lower() in ['true', '1', 'yes']
        
        setattr(clue_obj.db, field, value)
        self.caller.msg(f"|gUpdated {obj_name}.{field} to:|n {value}")
    
    def list_clue_objects(self):
        """List clue objects in the area."""
        if self.args and self.args.strip().lower() == "here":
            objects = [obj for obj in self.caller.location.contents if isinstance(obj, ClueObject)]
        else:
            objects = ClueObject.objects.all()
        
        if not objects:
            self.caller.msg("No clue objects found.")
            return

        headers = ["Name", "Location", "Mystery/Clue", "Discovered"]
        rows = []
        for obj in objects:
            location_name = obj.location.name if obj.location else "None"
            mystery_clue = f"{obj.db.mystery_id}/{obj.db.clue_id}"
            discovered_count = len(obj.db.discovered_by)
            rows.append((obj.name, location_name, mystery_clue, discovered_count))
        table = format_simple_table(headers, rows)
        self.caller.msg(f"\n{header('Clue Objects')}\n{table}")
    
    def delete_clue_object(self):
        """Delete a clue object."""
        if not self.args:
            self.caller.msg("Usage: +mystery/clueobj/delete <object>")
            return
            
        obj_name = self.args.strip()
        clue_obj = self.caller.search(obj_name)
        
        if not clue_obj or not isinstance(clue_obj, ClueObject):
            self.caller.msg("Clue object not found.")
            return
            
        clue_obj = clue_obj[0] if isinstance(clue_obj, list) else clue_obj
        obj_name = getattr(clue_obj, 'name', clue_obj.key) if clue_obj else 'unknown'

        clue_obj.delete()
        self.caller.msg(f"|gDeleted clue object:|n {obj_name}")
