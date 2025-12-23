from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create, evtable
from typeclasses.npcs import NPC, MinorNPC, MajorNPC, BossNPC
from world.utils.permission_utils import check_storyteller_permission, check_staff_permission

class CmdNPC(MuxCommand):
    """
    Manage NPCs (Non-Player Characters).
    
    Usage:
        +npc/list - List all NPCs in current location
        +npc/create <name> <type> - Create a basic NPC (staff only)
        +npc/generate <name> <archetype> [type] - Create NPC with random stats
        +npc/puppet <npc> - Start puppeting an NPC
        +npc/unpuppet - Stop puppeting current NPC
        +npc/control <npc> - Add yourself as NPC controller
        +npc/release <npc> - Remove yourself as NPC controller
        +npc/stats <npc> - View NPC character sheet
        +npc/damage <npc> <amount> <type> - Apply damage to NPC
        +npc/heal <npc> <amount> [type] - Heal NPC
        +npc/destroy <npc> - Destroy an NPC (staff only)
        +npc/archetypes [template] - List available archetypes
        
    NPC Types:
        standard - Basic NPC (default)
        minor - Weak NPC (crowds, minions)
        major - Important NPC (recurring characters)
        boss - Powerful NPC (major antagonists)
        
    Archetype Examples:
        mortal_tank, mortal_dex, mortal_social, mortal_mental
        vampire_tank, vampire_dex, vampire_social, vampire_mental
        werewolf_tank
        
    Examples:
        +npc/create Guard standard
        +npc/generate "Vampire Elder" vampire_social boss
        +npc/puppet Guard
        +npc/stats Guard
    """
    
    key = "+npc"
    aliases = []
    help_category = "Roleplaying Tools"
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            self.caller.msg("Usage: +npc/list, +npc/create, +npc/generate, +npc/puppet, etc. See help for more.")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_npcs()
        elif switch == "create":
            self.create_npc()
        elif switch == "generate":
            self.generate_npc()
        elif switch == "puppet":
            self.puppet_npc()
        elif switch == "unpuppet":
            self.unpuppet_npc()
        elif switch == "control":
            self.control_npc()
        elif switch == "release":
            self.release_npc()
        elif switch == "stats":
            self.view_stats()
        elif switch == "damage":
            self.damage_npc()
        elif switch == "heal":
            self.heal_npc()
        elif switch == "destroy":
            self.destroy_npc()
        elif switch == "archetypes":
            self.list_archetypes()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def list_npcs(self):
        """List all NPCs in current location"""
        if not self.caller.location:
            self.caller.msg("You are not in a valid location.")
            return
        
        npcs = [obj for obj in self.caller.location.contents 
                if hasattr(obj, 'db') and obj.db.is_npc]
        
        if not npcs:
            self.caller.msg("No NPCs in this location.")
            return
        
        table = evtable.EvTable(
            "|wName|n", "|wType|n", "|wTemplate|n", "|wCreator|n", "|wPuppeted|n", "|wHealth|n",
            border="cells", width=100
        )
        
        for npc in npcs:
            # Get health info
            health_damage = npc.db.health_damage or {}
            total_damage = sum(health_damage.values())
            max_health = npc.db.stats.get("advantages", {}).get("health", 7)
            health_display = f"{max_health - total_damage}/{max_health}"
            
            # Get other info
            template = npc.db.stats.get("other", {}).get("template", "Mortal")
            creator = npc.db.creator.name if npc.db.creator else "None"
            puppeted = "Yes" if npc.account else "No"
            
            table.add_row(
                npc.name,
                npc.db.npc_type.title(),
                template,
                creator,
                puppeted,
                health_display
            )
        
        self.caller.msg(str(table))
    
    def create_npc(self):
        """Create a new basic NPC"""
        if not (check_staff_permission(self.caller, "Builder") or check_storyteller_permission(self.caller)):
            self.caller.msg("You don't have permission to create NPCs. You need Staff or Storyteller permissions.")
            return
        
        try:
            name, npc_type = self.args.split()
        except ValueError:
            self.caller.msg("Usage: +npc/create <name> <type>")
            return
        
        # Map types to typeclasses
        typeclass_map = {
            "standard": NPC,
            "minor": MinorNPC,
            "major": MajorNPC,
            "boss": BossNPC
        }
        
        if npc_type not in typeclass_map:
            self.caller.msg(f"Invalid NPC type. Valid types: {', '.join(typeclass_map.keys())}")
            return
        
        # Create the NPC
        npc = create.create_object(
            typeclass=typeclass_map[npc_type],
            key=name,
            location=self.caller.location
        )
        
        # Set creator
        npc.set_creator(self.caller)
        
        self.caller.msg(f"Created {npc_type} NPC '{name}'. Use +stat commands to set stats.")
        self.caller.location.msg_contents(
            f"{name} appears.",
            exclude=[self.caller]
        )
    
    def generate_npc(self):
        """Generate an NPC with random stats based on archetype"""
        if not (check_staff_permission(self.caller, "Builder") or check_storyteller_permission(self.caller)):
            self.caller.msg("You don't have permission to generate NPCs. You need Staff or Storyteller permissions.")
            return
        
        try:
            parts = self.args.split()
            if len(parts) < 2:
                raise ValueError
            name = parts[0]
            archetype = parts[1]
            npc_type = parts[2] if len(parts) > 2 else "standard"
        except ValueError:
            self.caller.msg("Usage: +npc/generate <name> <archetype> [type]")
            return
        
        # Map types to typeclasses
        typeclass_map = {
            "standard": NPC,
            "minor": MinorNPC,
            "major": MajorNPC,
            "boss": BossNPC
        }
        
        if npc_type not in typeclass_map:
            self.caller.msg(f"Invalid NPC type. Valid types: {', '.join(typeclass_map.keys())}")
            return
        
        # Import archetype system
        try:
            from world.cofd.npc_archetypes import get_archetype, list_all_archetypes
        except ImportError:
            self.caller.msg("Archetype system not available.")
            return
        
        # Get the archetype
        archetype_obj = get_archetype(archetype)
        if not archetype_obj:
            available = ', '.join(list_all_archetypes()[:10])  # Show first 10
            self.caller.msg(f"Invalid archetype '{archetype}'. Use +npc/archetypes to see available options.")
            self.caller.msg(f"Examples: {available}...")
            return
        
        # Create the NPC
        npc = create.create_object(
            typeclass=typeclass_map[npc_type],
            key=name,
            location=self.caller.location
        )
        
        # Set creator
        npc.set_creator(self.caller)
        
        # Generate stats based on archetype
        success = npc.generate_random_stats(archetype, archetype_obj.template)
        
        if success:
            self.caller.msg(f"Generated {npc_type} {archetype_obj.template} NPC '{name}' using {archetype} archetype.")
            self.caller.msg(f"Template: {archetype_obj.template}, Focus: {archetype_obj.focus}")
            self.caller.msg(f"Description: {archetype_obj.description}")
            self.caller.location.msg_contents(
                f"{name} appears.",
                exclude=[self.caller]
            )
        else:
            self.caller.msg("Failed to generate NPC stats. Check archetype and template.")
            npc.delete()
    
    def puppet_npc(self):
        """Start puppeting an NPC"""
        if not self.args:
            self.caller.msg("Usage: +npc/puppet <npc>")
            return
            
        npc = self.caller.search(self.args, location=self.caller.location)
        if not npc:
            return
        
        if not hasattr(npc, 'db') or not npc.db.is_npc:
            self.caller.msg("That is not an NPC.")
            return
        
        # Check if already puppeting something
        if hasattr(self.caller, 'account') and self.caller.account.character != self.caller:
            self.caller.msg("You are already puppeting an NPC. Use +npc/unpuppet first.")
            return
        
        # Start puppeting
        success = npc.start_puppeting(self.caller.account)
        if not success:
            return
            
        # Notify location
        self.caller.location.msg_contents(
            f"{self.caller.name} starts controlling {npc.name}.",
            exclude=[self.caller]
        )
    
    def unpuppet_npc(self):
        """Stop puppeting current NPC"""
        if not hasattr(self.caller, 'account'):
            self.caller.msg("You don't have an account to unpuppet from.")
            return
            
        if not hasattr(self.caller, 'db') or not self.caller.db.is_npc:
            self.caller.msg("You are not currently puppeting an NPC.")
            return
        
        account = self.caller.account
        npc_name = self.caller.name
        location = self.caller.location
        
        # Stop puppeting
        success = self.caller.stop_puppeting(account)
        
        if success:
            # Notify location from the account's new character
            if account.character:
                location.msg_contents(
                    f"{account.character.name} stops controlling {npc_name}.",
                    exclude=[account.character]
                )
    
    def control_npc(self):
        """Add yourself as an NPC controller"""
        if not self.args:
            self.caller.msg("Usage: +npc/control <npc>")
            return
            
        npc = self.caller.search(self.args, location=self.caller.location)
        if not npc:
            return
        
        if not hasattr(npc, 'db') or not npc.db.is_npc:
            self.caller.msg("That is not an NPC.")
            return
        
        # Check permissions
        if not (check_staff_permission(self.caller, "Builder") or 
                check_storyteller_permission(self.caller) or
                npc.db.creator == self.caller or 
                self.caller in npc.db.controllers):
            self.caller.msg("You don't have permission to control that NPC.")
            return
        
        success = npc.add_controller(self.caller)
        if not success:
            self.caller.msg(f"You already have control permissions for {npc.name}.")
    
    def release_npc(self):
        """Remove yourself as an NPC controller"""
        if not self.args:
            self.caller.msg("Usage: +npc/release <npc>")
            return
            
        npc = self.caller.search(self.args, location=self.caller.location)
        if not npc:
            return
        
        if not hasattr(npc, 'db') or not npc.db.is_npc:
            self.caller.msg("That is not an NPC.")
            return
        
        success = npc.remove_controller(self.caller)
        if not success:
            self.caller.msg(f"You don't have control permissions for {npc.name}.")
    
    def view_stats(self):
        """View NPC character sheet"""
        if not self.args:
            self.caller.msg("Usage: +npc/stats <npc>")
            return
            
        npc = self.caller.search(self.args)
        if not npc:
            return
        
        if not hasattr(npc, 'db') or not npc.db.is_npc:
            self.caller.msg("That is not an NPC.")
            return
        
        # Use the same stat display as player characters
        # Import the stat command's list functionality
        try:
            from commands.stats import CmdStat
            stat_cmd = CmdStat()
            stat_cmd.caller = self.caller
            stat_cmd.args = npc.name
            stat_cmd.list_stats()
        except ImportError:
            # Fallback to basic display
            self._basic_stat_display(npc)
    
    def _basic_stat_display(self, npc):
        """Basic stat display if full system unavailable"""
        output = [f"|y{npc.name}|n - {npc.db.npc_type.title()} NPC"]
        output.append(f"Threat Level: {npc.db.threat_level}")
        output.append(f"Creator: {npc.db.creator.name if npc.db.creator else 'None'}")
        output.append(f"Controllers: {', '.join([c.name for c in npc.db.controllers]) if npc.db.controllers else 'None'}")
        output.append("")
        
        # Show basic stats if available
        if npc.db.stats:
            attrs = npc.db.stats.get("attributes", {})
            if attrs:
                output.append("|wAttributes:|n")
                for attr, value in attrs.items():
                    output.append(f"  {attr.title()}: {value}")
                output.append("")
        
        self.caller.msg("\n".join(output))
    
    def damage_npc(self):
        """Apply damage to an NPC"""
        try:
            parts = self.args.split()
            npc_name = parts[0]
            amount = int(parts[1])
            damage_type = parts[2] if len(parts) > 2 else "bashing"
        except (ValueError, IndexError):
            self.caller.msg("Usage: +npc/damage <npc> <amount> [type]")
            return
        
        npc = self.caller.search(npc_name)
        if not npc:
            return
        
        if not hasattr(npc, 'db') or not npc.db.is_npc:
            self.caller.msg("That is not an NPC.")
            return
        
        if damage_type not in ["bashing", "lethal", "aggravated"]:
            self.caller.msg("Invalid damage type. Use: bashing, lethal, or aggravated")
            return
        
        # Apply damage
        npc.take_damage(amount, damage_type)
        
        # Calculate remaining health
        health_damage = npc.db.health_damage or {}
        total_damage = sum(health_damage.values())
        max_health = npc.db.stats.get("advantages", {}).get("health", 7)
        health_remaining = max_health - total_damage
        
        self.caller.msg(f"Applied {amount} {damage_type} damage to {npc.name}.")
        self.caller.msg(f"{npc.name} has {health_remaining}/{max_health} health remaining.")
    
    def heal_npc(self):
        """Heal an NPC"""
        try:
            parts = self.args.split()
            npc_name = parts[0]
            amount = int(parts[1])
            damage_type = parts[2] if len(parts) > 2 else None
        except (ValueError, IndexError):
            self.caller.msg("Usage: +npc/heal <npc> <amount> [type]")
            return
        
        npc = self.caller.search(npc_name)
        if not npc:
            return
        
        if not hasattr(npc, 'db') or not npc.db.is_npc:
            self.caller.msg("That is not an NPC.")
            return
        
        if damage_type and damage_type not in ["bashing", "lethal", "aggravated"]:
            self.caller.msg("Invalid damage type. Use: bashing, lethal, or aggravated")
            return
        
        # Heal damage
        npc.heal_damage(amount, damage_type)
        
        # Calculate remaining health
        health_damage = npc.db.health_damage or {}
        total_damage = sum(health_damage.values())
        max_health = npc.db.stats.get("advantages", {}).get("health", 7)
        health_remaining = max_health - total_damage
        
        heal_msg = f"Healed {amount} damage from {npc.name}"
        if damage_type:
            heal_msg += f" ({damage_type})"
        heal_msg += "."
        
        self.caller.msg(heal_msg)
        self.caller.msg(f"{npc.name} has {health_remaining}/{max_health} health remaining.")
    
    def destroy_npc(self):
        """Destroy an NPC"""
        if not (check_staff_permission(self.caller, "Builder") or check_storyteller_permission(self.caller)):
            self.caller.msg("You don't have permission to destroy NPCs. You need Staff or Storyteller permissions.")
            return
        
        if not self.args:
            self.caller.msg("Usage: +npc/destroy <npc>")
            return
            
        npc = self.caller.search(self.args)
        if not npc:
            return
        
        if not hasattr(npc, 'db') or not npc.db.is_npc:
            self.caller.msg("That is not an NPC.")
            return
        
        npc_name = npc.name
        npc.location.msg_contents(f"{npc_name} disappears.")
        npc.delete()
        self.caller.msg(f"Destroyed NPC '{npc_name}'.")
    
    def list_archetypes(self):
        """List available NPC archetypes"""
        try:
            from world.cofd.npc_archetypes import ARCHETYPE_REGISTRY, get_archetypes_by_template
        except ImportError:
            self.caller.msg("Archetype system not available.")
            return
        
        # Filter by template if specified
        if self.args:
            template = self.args.strip()
            archetypes = get_archetypes_by_template(template)
            if not archetypes:
                self.caller.msg(f"No archetypes found for template '{template}'.")
                return
            output = [f"|wArchetypes for {template.title()}:|n"]
        else:
            output = ["|wAvailable NPC Archetypes:|n"]
            archetypes = []
            # Group by template
            template_groups = {}
            for archetype in ARCHETYPE_REGISTRY.values():
                template = archetype.template
                if template not in template_groups:
                    template_groups[template] = []
                if archetype not in template_groups[template]:  # Avoid duplicates
                    template_groups[template].append(archetype)
            
            for template, template_archetypes in template_groups.items():
                output.append(f"\n|c{template}:|n")
                for arch in template_archetypes:
                    output.append(f"  {arch.name.lower()} - {arch.description}")
            
            self.caller.msg("\n".join(output))
            return
        
        # Display archetypes for specific template
        for arch in archetypes:
            output.append(f"  {arch.name.lower()} - {arch.description}")
        
        self.caller.msg("\n".join(output)) 