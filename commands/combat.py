"""
Chronicles of Darkness Combat Commands - Refactored Version
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
# from .combat_core import CombatTracker, WeaponData  # Disabled - module doesn't exist
from .base import BasePyReachCommand, BuilderMixin
from world.utils.permission_utils import check_builder_permission

# Combat system implementation
from world.utils.dice_utils import roll_dice, RollType
from world.equipment_database import WEAPON_DATABASE as WEAPON_DATA, WeaponData, ArmorData
import secrets
from utils.search_helpers import search_character

def search_combat_target(caller, target_name):
    """
    Search for a combat target with proper validation.
    
    Combat targets must be:
    1. In the same location as the caller
    2. Currently online (has active session)
    3. In combat
    
    Args:
        caller: Character performing the search
        target_name: Name or alias to search for
        
    Returns:
        Character object or None if not found/invalid
    """
    # Use local search only (same room)
    target = search_character(caller, target_name, global_search=False)
    if not target:
        return None
    
    # Check if target is in same location
    if target.location != caller.location:
        caller.msg(f"{target.name} is not in the same location as you.")
        return None
    
    # Check if target is online
    if not target.sessions.all():
        caller.msg(f"{target.name} is not currently online.")
        return None
    
    return target

class CombatTracker:
    """Full combat tracker implementation for Chronicles of Darkness"""
    
    def __init__(self, location):
        self.location = location
        self.participants = {}  # character: {data}
        self.initiative_order = []
        self.current_actor = None
        self.round_number = 1
        self.turn_number = 1
        self.teams = {}  # team_number: [characters]
        self.next_team = 1
        
    def add_participant(self, character, team=None):
        """Add a character to combat"""
        if character in self.participants:
            return  # Already in combat
            
        # Auto-assign team if not specified
        if team is None:
            team = self.next_team
            self.next_team += 1
            
        # Initialize team if needed
        if team not in self.teams:
            self.teams[team] = []
            
        # Add to team
        self.teams[team].append(character)
        
        # Initialize participant data
        self.participants[character] = {
            'team': team,
            'initiative': 0,
            'has_acted': False,
            'defense_applied': 0,
            'conditions': [],
            'prone': False,
            'in_cover': False,
            'cover_rating': 0,
            'all_out_attack': False,
            'dodge_applied': False,
            'actions_taken': 0,
            'grappling_with': None,
            'grapple_controller': None,
            'grapple_actions': {
                'control_weapon': False,
                'held': False,
                'restrained': False,
                'taking_cover': False
            }
        }
        
        # Announce to location
        self.location.msg_contents(f"{character.name} joins combat on team {team}!")
        
    def remove_participant(self, character):
        """Remove a character from combat"""
        if character not in self.participants:
            return
            
        # Remove from team
        team = self.participants[character]['team']
        if team in self.teams and character in self.teams[team]:
            self.teams[team].remove(character)
            
        # Remove from participants
        del self.participants[character]
        
        # Remove from initiative order
        if character in self.initiative_order:
            self.initiative_order.remove(character)
            
        # Update current actor if needed
        if self.current_actor == character:
            self.advance_turn()
            
        # Announce to location
        self.location.msg_contents(f"{character.name} leaves combat.")
        
    def get_team(self, character):
        """Get character's team number"""
        if character in self.participants:
            return self.participants[character]['team']
        return None
        
    def roll_initiative(self, character):
        """Roll initiative for a character"""
        if character not in self.participants:
            # Auto-add character to combat if not already participating
            self.add_participant(character)
            
        # Get initiative attribute from advantages (pre-calculated)
        init_attr = character.db.stats.get("advantages", {}).get("initiative", 0)
        
        # If not found in advantages, calculate from Dex + Composure
        if init_attr == 0:
            dex = character.db.stats.get("attributes", {}).get("dexterity", 1)
            composure = character.db.stats.get("attributes", {}).get("composure", 1)
            init_attr = dex + composure
        
        # Roll 1d10 + initiative
        roll = secrets.randbelow(10) + 1
        total_initiative = roll + init_attr
        
        # Store initiative
        self.participants[character]['initiative'] = total_initiative
        
        # Update initiative order
        self.update_initiative_order()
        
        return roll, init_attr
        
    def update_initiative_order(self):
        """Update the initiative order based on current initiatives"""
        # Sort by initiative (highest first)
        self.initiative_order = sorted(
            self.participants.keys(),
            key=lambda char: self.participants[char]['initiative'],
            reverse=True
        )
        
        # Set current actor to first in order if not set
        if not self.current_actor and self.initiative_order:
            self.current_actor = self.initiative_order[0]
            
    def advance_turn(self):
        """Advance to the next character's turn"""
        if not self.initiative_order:
            return
            
        # Find current actor index
        if self.current_actor in self.initiative_order:
            current_index = self.initiative_order.index(self.current_actor)
            next_index = (current_index + 1) % len(self.initiative_order)
        else:
            next_index = 0
            
        # If we've cycled through everyone, advance round
        if next_index == 0:
            self.advance_round()
        else:
            self.turn_number += 1
            
        # Set next actor
        self.current_actor = self.initiative_order[next_index]
        
        # Reset per-turn flags for new actor
        self.reset_turn_flags(self.current_actor)
        
        # Check if current actor is in a grapple
        if self.is_grappling(self.current_actor):
            grapple_partner = self.get_grapple_partner(self.current_actor)
            
            # Determine who has higher initiative for automatic contest
            current_init = self.participants[self.current_actor]['initiative']
            partner_init = self.participants[grapple_partner]['initiative']
            
            if current_init >= partner_init:
                # Current actor has higher/equal initiative, resolve contest
                self.location.msg_contents(
                    f"Round {self.round_number}, Turn {self.turn_number}: "
                    f"{self.current_actor.name}'s turn! (Grappling with {grapple_partner.name})"
                )
                
                winner, successes = self.resolve_grapple_contest(self.current_actor, grapple_partner)
                
                # Winner gets to choose grapple action
                if winner == self.current_actor:
                    self.location.msg_contents(
                        f"{self.current_actor.name} may now choose a grapple action. "
                        f"Use: +combat/break, +combat/control, +combat/damage, +combat/disarm, "
                        f"+combat/prone, +combat/hold, +combat/restrain, or +combat/takecover"
                    )
                else:
                    # Partner won, they get to act instead
                    self.current_actor = winner
                    self.location.msg_contents(
                        f"{winner.name} wins the grapple contest and may choose a grapple action!"
                    )
            else:
                # Partner has higher initiative, they should have acted already
                self.location.msg_contents(
                    f"Round {self.round_number}, Turn {self.turn_number}: "
                    f"{self.current_actor.name}'s turn! (Grappling with {grapple_partner.name})"
                )
        else:
            # Normal turn announcement
            self.location.msg_contents(
                f"Round {self.round_number}, Turn {self.turn_number}: "
                f"{self.current_actor.name}'s turn!"
            )
        
    def advance_round(self):
        """Advance to the next round"""
        self.round_number += 1
        self.turn_number = 1
        
        # Reset per-round flags for all participants
        for character in self.participants:
            self.participants[character]['has_acted'] = False
            self.participants[character]['actions_taken'] = 0
            self.participants[character]['all_out_attack'] = False
            self.participants[character]['dodge_applied'] = False
            
        self.location.msg_contents(f"Beginning Round {self.round_number}")
        
    def reset_turn_flags(self, character):
        """Reset per-turn flags for a character"""
        if character in self.participants:
            self.participants[character]['has_acted'] = False
            
    def get_defense(self, character):
        """Calculate character's current Defense rating"""
        if character not in self.participants:
            return 0
            
        # Base Defense = min(Wits, Dexterity) + Athletics
        wits = character.db.stats.get("attributes", {}).get("wits", 1)
        dex = character.db.stats.get("attributes", {}).get("dexterity", 1)
        athletics = character.db.stats.get("skills", {}).get("athletics", 0)
        
        base_defense = min(wits, dex) + athletics
        
        # Apply modifiers
        data = self.participants[character]
        
        # Prone reduces Defense
        if data.get('prone'):
            base_defense = max(0, base_defense - 2)
            
        # Cover provides Defense bonus against ranged attacks
        if data.get('in_cover'):
            base_defense += data.get('cover_rating', 0)
            
        # All-out attack removes Defense
        if data.get('all_out_attack'):
            base_defense = 0
            
        # Dodge doubles Defense (applied once per turn)
        if data.get('dodge_applied'):
            base_defense *= 2
            
        return max(0, base_defense)
    
    def initiate_grapple(self, attacker, defender):
        """Initiate a grapple between two characters"""
        # Roll contested Strength + Brawl
        attacker_str = attacker.db.stats.get("attributes", {}).get("strength", 1)
        attacker_brawl = attacker.db.stats.get("skills", {}).get("brawl", 0)
        attacker_pool = attacker_str + attacker_brawl
        
        defender_str = defender.db.stats.get("attributes", {}).get("strength", 1)
        defender_brawl = defender.db.stats.get("skills", {}).get("brawl", 0)
        defender_pool = defender_str + defender_brawl
        
        # Apply wound penalties
        attacker_wounds = self._get_wound_penalty(attacker)
        defender_wounds = self._get_wound_penalty(defender)
        attacker_pool += attacker_wounds
        defender_pool += defender_wounds
        
        # Roll dice
        from world.utils.dice_utils import roll_dice, RollType
        attacker_rolls, attacker_successes, attacker_ones = roll_dice(attacker_pool)
        defender_rolls, defender_successes, defender_ones = roll_dice(defender_pool)
        
        # Determine winner
        if attacker_successes > defender_successes:
            winner = attacker
            loser = defender
            winner_successes = attacker_successes
        elif defender_successes > attacker_successes:
            winner = defender
            loser = attacker
            winner_successes = defender_successes
        else:
            # Tie - no grapple established
            self.location.msg_contents(
                f"{attacker.name} and {defender.name} struggle but neither gains control! "
                f"({attacker_successes} vs {defender_successes} successes)"
            )
            return None
            
        # Set grapple state
        self.participants[attacker]['grappling_with'] = defender
        self.participants[defender]['grappling_with'] = attacker
        self.participants[winner]['grapple_controller'] = True
        self.participants[loser]['grapple_controller'] = False
        
        self.location.msg_contents(
            f"{winner.name} successfully grapples {loser.name}! "
            f"({winner_successes} successes) {winner.name} controls the grapple."
        )
        
        return winner
    
    def resolve_grapple_contest(self, char1, char2):
        """Resolve the ongoing grapple contest between two characters"""
        # Roll contested Strength + Brawl for both
        char1_str = char1.db.stats.get("attributes", {}).get("strength", 1)
        char1_brawl = char1.db.stats.get("skills", {}).get("brawl", 0)
        char1_pool = char1_str + char1_brawl
        
        char2_str = char2.db.stats.get("attributes", {}).get("strength", 1)
        char2_brawl = char2.db.stats.get("skills", {}).get("brawl", 0)
        char2_pool = char2_str + char2_brawl
        
        # Apply wound penalties
        char1_wounds = self._get_wound_penalty(char1)
        char2_wounds = self._get_wound_penalty(char2)
        char1_pool += char1_wounds
        char2_pool += char2_wounds
        
        # Roll dice
        from world.utils.dice_utils import roll_dice, RollType
        char1_rolls, char1_successes, char1_ones = roll_dice(char1_pool)
        char2_rolls, char2_successes, char2_ones = roll_dice(char2_pool)
        
        # Determine winner
        if char1_successes > char2_successes:
            winner = char1
            loser = char2
            winner_successes = char1_successes
        elif char2_successes > char1_successes:
            winner = char2
            loser = char1
            winner_successes = char2_successes
        else:
            # Tie - current controller maintains control
            current_controller = char1 if self.participants[char1].get('grapple_controller') else char2
            winner = current_controller
            loser = char2 if current_controller == char1 else char1
            winner_successes = char1_successes if current_controller == char1 else char2_successes
            
        # Update control
        self.participants[winner]['grapple_controller'] = True
        self.participants[loser]['grapple_controller'] = False
        
        self.location.msg_contents(
            f"Grapple contest: {winner.name} controls the grapple! "
            f"({char1.name}: {char1_successes}, {char2.name}: {char2_successes} successes)"
        )
        
        return winner, winner_successes
    
    def break_grapple(self, character):
        """Break a character free from grapple"""
        grapple_partner = self.participants[character].get('grappling_with')
        if not grapple_partner:
            return False
            
        # Clear grapple state for both characters
        self.participants[character]['grappling_with'] = None
        self.participants[character]['grapple_controller'] = None
        self.participants[character]['grapple_actions'] = {
            'control_weapon': False,
            'held': False,
            'restrained': False,
            'taking_cover': False
        }
        
        self.participants[grapple_partner]['grappling_with'] = None
        self.participants[grapple_partner]['grapple_controller'] = None
        self.participants[grapple_partner]['grapple_actions'] = {
            'control_weapon': False,
            'held': False,
            'restrained': False,
            'taking_cover': False
        }
        
        self.location.msg_contents(f"{character.name} breaks free from the grapple!")
        return True
    
    def is_grappling(self, character):
        """Check if character is currently grappling"""
        return self.participants[character].get('grappling_with') is not None
    
    def get_grapple_partner(self, character):
        """Get the character this character is grappling with"""
        return self.participants[character].get('grappling_with')
    
    def is_grapple_controller(self, character):
        """Check if character controls the grapple"""
        return self.participants[character].get('grapple_controller', False)
        
    def end_combat(self):
        """End combat and clean up"""
        self.location.msg_contents("Combat has ended!")
        
        # Clear combat tracker from location
        if hasattr(self.location, 'combat_tracker'):
            del self.location.combat_tracker
            
        # Reset participant flags
        for character in self.participants:
            # Clear combat-specific attributes
            if hasattr(character.db, 'in_combat'):
                del character.db.in_combat

class CmdCombat(BasePyReachCommand, BuilderMixin):
    """
    Chronicles of Darkness Combat System
    
    Usage:
        +combat/init [modifier] - Roll initiative
        +combat/status - Show combat status
        +combat/next - Advance to next turn (staff/participants)
        +combat/join [team] - Join combat (optionally specify team number)
        +combat/leave - Leave combat
        +combat/end - End combat (staff only)
        
        Attack Actions:
        +combat/attack <target> [weapon] - Make an attack
        +combat/unarmed <target> - Unarmed attack
        +combat/melee <target> [weapon] - Melee weapon attack
        +combat/ranged <target> [weapon] - Ranged weapon attack
        +combat/thrown <target> <weapon> - Thrown weapon attack
        
        Special Actions:
        +combat/allout <target> [weapon] - All-out attack (+2 dice, lose Defense)
        +combat/charge <target> [weapon] - Charge attack (move + attack, lose Defense)
        +combat/dodge - Dodge (double Defense, use action)
        +combat/aim [target] - Aim at target (+1 dice next turn, up to +3)
        +combat/grapple <target> - Initiate grapple
        +combat/disarm <target> - Attempt to disarm target
        +combat/touch <target> - Touch target (no damage)
        
        Grapple Actions (when grappling):
        +combat/break - Break free from grapple
        +combat/control - Control weapon in grapple
        +combat/damage - Deal damage in grapple
        +combat/restrain - Restrain opponent
        +combat/takecover - Use opponent as human shield
        +combat/prone - Drop both to ground
        +combat/hold - Hold opponent (remove Defense)
        
        Ranged Combat:
        +combat/autofire <targets> - Autofire at multiple targets
        +combat/burst/short <target> - Short burst (+1 dice)
        +combat/burst/medium <targets> - Medium burst (+2 dice, 1-3 targets)
        +combat/burst/long <targets> - Long burst (+3 dice, multiple targets)
        +combat/cover <targets> - Covering fire
        +combat/reload - Reload weapon
        
        Movement & Position:
        +combat/move [distance] - Move up to Speed
        +combat/run - Move at double Speed (give up action)
        +combat/prone - Drop prone (-2 ranged Defense, +2 melee Defense)
        +combat/rise - Stand up from prone
        +combat/takecover [rating] - Take cover
        +combat/leavecover - Leave cover
        
        Equipment:
        +combat/wield <weapon> - Ready a weapon
        +combat/drop <weapon> - Drop weapon (reflexive)
        +combat/draw <weapon> - Draw weapon (instant action)
        +combat/wear <armor> - Don armor
        +combat/remove <armor> - Remove armor
        
        Other Actions:
        +combat/delay - Delay action until later in turn
        +combat/wait - Wait and see (end turn)
        +combat/willpower - Spend Willpower (+3 dice or +2 Defense)
        +combat/surprise <target> - Attempt surprise attack
    """
    
    key = "+combat"
    aliases = ["+fight", "+init"]
    help_category = "Automated Combat System"
    
    def func(self):
        """Execute the command"""
        # Get or create combat tracker for this location
        if not hasattr(self.caller.location, 'combat_tracker'):
            self.caller.location.combat_tracker = CombatTracker(self.caller.location)
            
        self.combat = self.caller.location.combat_tracker
        
        if not self.switches:
            self.caller.msg("Use +combat/help for combat commands. Common: /init, /status, /join")
            return
            
        switch = self.switches[0].lower()
        
        # Basic combat management
        if switch == "init":
            self.roll_initiative()
        elif switch == "status":
            self.show_combat_status()
        elif switch == "join":
            self.join_combat()
        elif switch == "leave":
            self.leave_combat()
        elif switch == "next":
            self.advance_turn()
        elif switch == "end":
            self.end_combat()
        elif switch == "help":
            self.show_help()
            
        # Attack actions
        elif switch == "attack":
            self.attack()
        elif switch == "unarmed":
            self.unarmed_attack()
        elif switch == "melee":
            self.melee_attack()
        elif switch == "ranged":
            self.ranged_attack()
        elif switch == "thrown":
            self.thrown_attack()
            
        # Special combat actions
        elif switch == "allout":
            self.all_out_attack()
        elif switch == "charge":
            self.charge_attack()
        elif switch == "dodge":
            self.dodge()
        elif switch == "aim":
            self.aim()
        elif switch == "grapple":
            self.grapple()
        elif switch == "disarm":
            self.disarm()
        elif switch == "touch":
            self.touch_attack()
            
        # Grapple actions
        elif switch == "break":
            self.grapple_break()
        elif switch == "control":
            self.grapple_control()
        elif switch == "damage":
            self.grapple_damage()
        elif switch == "restrain":
            self.grapple_restrain()
        elif switch == "takecover":
            self.grapple_takecover()
        elif switch == "prone":
            self.grapple_prone()
        elif switch == "hold":
            self.grapple_hold()
            
        # Ranged combat
        elif switch == "autofire":
            self.autofire()
        elif switch == "burst":
            self.burst_fire()
        elif switch == "cover":
            self.covering_fire()
        elif switch == "reload":
            self.reload()
            
        # Movement and positioning
        elif switch == "move":
            self.move()
        elif switch == "run":
            self.run()
        elif switch == "prone":
            self.go_prone()
        elif switch == "rise":
            self.rise()
        elif switch == "takecover":
            self.take_cover()
        elif switch == "leavecover":
            self.leave_cover()
            
        # Equipment management
        elif switch == "wield":
            self.wield_weapon()
        elif switch == "drop":
            self.drop_weapon()
        elif switch == "draw":
            self.draw_weapon()
        elif switch == "wear":
            self.wear_armor()
        elif switch == "remove":
            self.remove_armor()
            
        # Other actions
        elif switch == "delay":
            self.delay_action()
        elif switch == "wait":
            self.wait()
        elif switch == "willpower":
            self.spend_willpower()
        elif switch == "surprise":
            self.surprise_attack()
            
        else:
            self.caller.msg("Invalid combat command. Use +combat/help for available commands.")
    
    def roll_initiative(self):
        """Roll initiative for combat"""
        modifier = 0
        if self.args:
            try:
                modifier = int(self.args)
            except ValueError:
                self.caller.msg("Initiative modifier must be a number.")
                return
        
        # Auto-join combat if not already participating
        if self.caller not in self.combat.participants:
            self.combat.add_participant(self.caller)
            self.caller.msg("You join combat!")
                
        roll, init_attr = self.combat.roll_initiative(self.caller)
        if init_attr is None:
            init_attr = 0
        total_mod = init_attr + modifier
        total_initiative = roll + total_mod
        
        self.caller.msg(f"Initiative: {total_initiative} ({roll} + {total_mod})")
        
    def show_combat_status(self):
        """Show current combat status"""
        if not self.combat.participants:
            self.caller.msg("No active combat in this location.")
            return
            
        table = evtable.EvTable("Character", "Team", "Initiative", "Status")
        
        for char in self.combat.initiative_order:
            data = self.combat.participants[char]
            status_parts = []
            
            if data.get('prone'):
                status_parts.append("Prone")
            if data.get('in_cover'):
                status_parts.append(f"Cover {data['cover_rating']}")
            if data.get('grappling_with'):
                partner = data['grappling_with']
                if data.get('grapple_controller'):
                    status_parts.append(f"|gGrappling {partner.name} (Controller)|n")
                else:
                    status_parts.append(f"|rGrappling {partner.name}|n")
            
            # Add grapple action status
            grapple_actions = data.get('grapple_actions', {})
            if grapple_actions.get('control_weapon'):
                status_parts.append("Weapon Control")
            if grapple_actions.get('held'):
                status_parts.append("Held")
            if grapple_actions.get('restrained'):
                status_parts.append("Restrained")
            if grapple_actions.get('taking_cover'):
                status_parts.append("Human Shield")
                
            status = ", ".join(status_parts) if status_parts else "Normal"
            
            name = char.name
            if char == self.combat.current_actor:
                name = f"|y{name}*|n"
                
            team = data['team']
            team_display = f"|c{team}|n" if team else "None"
                
            table.add_row(name, team_display, data['initiative'], status)
            
        output = [f"Combat Status - Round {self.combat.round_number}, Turn {self.combat.turn_number}"]
        output.append(str(table))
        
        self.caller.msg("\n".join(output))
        
    def join_combat(self):
        """Join combat"""
        team = None
        if self.args:
            try:
                team = int(self.args)
            except ValueError:
                self.caller.msg("Team number must be a number.")
                return
                
        self.combat.add_participant(self.caller, team)
        assigned_team = self.combat.get_team(self.caller)
        self.caller.msg(f"You join combat on team {assigned_team}!")
        
    def leave_combat(self):
        """Leave combat"""
        self.combat.remove_participant(self.caller)
        self.caller.msg("You leave combat.")
        
    def advance_turn(self):
        """Advance to next turn (staff or participants only)"""
        # Check if caller is in combat or is staff
        if self.caller not in self.combat.participants:
            if not self.check_builder_access():
                self.caller.msg("You must be in combat or have builder access to advance turns.")
                return
        
        self.combat.advance_turn()
        
    def end_combat(self):
        """End combat"""
        if not self.check_builder_access():
            return
            
        self.combat.end_combat()
        
    def show_help(self):
        """Show combat help"""
        output = [
            "|cChronicles of Darkness Combat Commands|n",
            "",
            "|yBasic Commands:|n",
            "+combat/join [team] - Join combat (optionally specify team)",
            "+combat/init [modifier] - Roll initiative", 
            "+combat/status - Show combat status and turn order",
            "+combat/next - Advance to next turn",
            "+combat/leave - Leave combat",
            "+combat/end - End combat (staff only)",
            "",
            "|yAttack Commands:|n",
            "+combat/attack <target> [weapon] - Generic attack",
            "+combat/unarmed <target> - Unarmed attack",
            "+combat/melee <target> [weapon] - Melee weapon attack",
            "+combat/ranged <target> [weapon] - Ranged weapon attack",
            "+combat/allout <target> [weapon] - All-out attack (+2 dice, lose Defense)",
            "+combat/charge <target> [weapon] - Charge attack (move + attack)",
            "+combat/dodge - Dodge (double Defense, use action)",
            "+combat/aim [target] - Aim for bonus dice",
            "",
            "|yGrappling Commands:|n",
            "+combat/grapple <target> - Initiate grapple (Strength + Brawl contest)",
            "+combat/break - Break free from grapple (reflexive)",
            "+combat/control - Control weapons in grapple",
            "+combat/damage - Deal bashing damage in grapple",
            "+combat/disarm - Disarm opponent (requires weapon control)",
            "+combat/hold - Hold opponent (removes Defense)",
            "+combat/restrain - Restrain with equipment (requires hold)",
            "+combat/prone - Throw both to ground",
            "+combat/takecover - Use opponent as human shield",
            "",
            "|yExample Usage:|n",
            "+combat/join 1 - Join team 1",
            "+combat/init 2 - Roll initiative with +2 modifier",
            "+combat/attack John sword - Attack John with a sword",
            "+combat/grapple Jane - Attempt to grapple Jane",
            "+combat/status - Check who's turn it is",
        ]
        
        self.caller.msg("\n".join(output))
    
    # ========================================
    # ATTACK ACTIONS
    # ========================================
    
    def attack(self):
        """Generic attack command - determines weapon type automatically"""
        if not self.args:
            self.caller.msg("Usage: +combat/attack <target> [weapon]")
            return
            
        # Check if it's caller's turn
        if not self._check_turn():
            return
            
        parts = self.args.split()
        target_name = parts[0]
        weapon_name = " ".join(parts[1:]) if len(parts) > 1 else None
        
        # Find target (local search only, must be online)
        target = search_combat_target(self.caller, target_name)
        if not target:
            return
            
        # Check if target is in combat
        if target not in self.combat.participants:
            self.caller.msg(f"{target.name} is not in combat.")
            return
            
        # Determine weapon
        weapon = self._get_weapon(weapon_name)
        if weapon is None:
            return
            
        # Perform attack based on weapon type
        if weapon.weapon_type == "ranged":
            self._perform_ranged_attack(target, weapon)
        elif weapon.weapon_type == "thrown":
            self._perform_thrown_attack(target, weapon)
        else:
            self._perform_melee_attack(target, weapon)
    
    def unarmed_attack(self):
        """Unarmed combat attack"""
        if not self.args:
            self.caller.msg("Usage: +combat/unarmed <target>")
            return
            
        if not self._check_turn():
            return
            
        target = search_combat_target(self.caller, self.args)
        if not target:
            return
            
        if target not in self.combat.participants:
            self.caller.msg(f"{target.name} is not in combat.")
            return
            
        weapon = WEAPON_DATA["unarmed"]
        self._perform_melee_attack(target, weapon)
    
    def melee_attack(self):
        """Melee weapon attack"""
        if not self.args:
            self.caller.msg("Usage: +combat/melee <target> [weapon]")
            return
            
        if not self._check_turn():
            return
            
        parts = self.args.split()
        target_name = parts[0]
        weapon_name = " ".join(parts[1:]) if len(parts) > 1 else None
        
        target = self.caller.search(target_name)
        if not target:
            return
            
        if target not in self.combat.participants:
            self.caller.msg(f"{target.name} is not in combat.")
            return
            
        weapon = self._get_weapon(weapon_name, weapon_type="melee")
        if weapon is None:
            return
            
        self._perform_melee_attack(target, weapon)
    
    def ranged_attack(self):
        """Ranged weapon attack"""
        if not self.args:
            self.caller.msg("Usage: +combat/ranged <target> [weapon]")
            return
            
        if not self._check_turn():
            return
            
        parts = self.args.split()
        target_name = parts[0]
        weapon_name = " ".join(parts[1:]) if len(parts) > 1 else None
        
        target = self.caller.search(target_name)
        if not target:
            return
            
        if target not in self.combat.participants:
            self.caller.msg(f"{target.name} is not in combat.")
            return
            
        weapon = self._get_weapon(weapon_name, weapon_type="ranged")
        if weapon is None:
            return
            
        self._perform_ranged_attack(target, weapon)
    
    def thrown_attack(self):
        """Thrown weapon attack"""
        if not self.args:
            self.caller.msg("Usage: +combat/thrown <target> <weapon>")
            return
            
        if not self._check_turn():
            return
            
        parts = self.args.split()
        if len(parts) < 2:
            self.caller.msg("Usage: +combat/thrown <target> <weapon>")
            return
            
        target_name = parts[0]
        weapon_name = " ".join(parts[1:])
        
        target = self.caller.search(target_name)
        if not target:
            return
            
        if target not in self.combat.participants:
            self.caller.msg(f"{target.name} is not in combat.")
            return
            
        weapon = self._get_weapon(weapon_name, weapon_type="thrown")
        if weapon is None:
            return
            
        self._perform_thrown_attack(target, weapon)
    
    # ========================================
    # SPECIAL COMBAT ACTIONS
    # ========================================
    
    def all_out_attack(self):
        """All-out attack: +2 dice but lose Defense"""
        if not self.args:
            self.caller.msg("Usage: +combat/allout <target> [weapon]")
            return
            
        if not self._check_turn():
            return
            
        # Check if already used Defense this turn
        if self.combat.participants[self.caller].get('defense_applied', 0) > 0:
            self.caller.msg("You cannot perform an all-out attack after applying Defense.")
            return
            
        parts = self.args.split()
        target_name = parts[0]
        weapon_name = " ".join(parts[1:]) if len(parts) > 1 else None
        
        target = self.caller.search(target_name)
        if not target:
            return
            
        if target not in self.combat.participants:
            self.caller.msg(f"{target.name} is not in combat.")
            return
            
        weapon = self._get_weapon(weapon_name)
        if weapon is None:
            return
            
        # Set all-out attack flag
        self.combat.participants[self.caller]['all_out_attack'] = True
        
        # Perform attack with +2 dice bonus
        if weapon.weapon_type == "ranged":
            self._perform_ranged_attack(target, weapon, dice_bonus=2, special="All-Out Attack")
        elif weapon.weapon_type == "thrown":
            self._perform_thrown_attack(target, weapon, dice_bonus=2, special="All-Out Attack")
        else:
            self._perform_melee_attack(target, weapon, dice_bonus=2, special="All-Out Attack")
    
    def charge_attack(self):
        """Charge attack: move + attack but lose Defense"""
        if not self.args:
            self.caller.msg("Usage: +combat/charge <target> [weapon]")
            return
            
        if not self._check_turn():
            return
            
        # Check if already used Defense this turn
        if self.combat.participants[self.caller].get('defense_applied', 0) > 0:
            self.caller.msg("You cannot charge after applying Defense.")
            return
            
        parts = self.args.split()
        target_name = parts[0]
        weapon_name = " ".join(parts[1:]) if len(parts) > 1 else None
        
        target = self.caller.search(target_name)
        if not target:
            return
            
        if target not in self.combat.participants:
            self.caller.msg(f"{target.name} is not in combat.")
            return
            
        weapon = self._get_weapon(weapon_name)
        if weapon is None:
            return
            
        # Only melee/unarmed weapons can charge
        if weapon.weapon_type not in ["melee", "unarmed"]:
            self.caller.msg("You can only charge with melee weapons or unarmed attacks.")
            return
            
        # Set charge flag (removes Defense)
        self.combat.participants[self.caller]['all_out_attack'] = True
        
        # Move up to twice Speed and attack
        speed = self.caller.db.stats.get("advantages", {}).get("speed", 5)
        
        self.caller.location.msg_contents(
            f"{self.caller.name} charges at {target.name}, moving up to {speed * 2} yards!"
        )
        
        self._perform_melee_attack(target, weapon, special="Charge")
    
    def dodge(self):
        """Dodge: double Defense but use action"""
        if not self._check_turn():
            return
            
        # Set dodge flag
        self.combat.participants[self.caller]['dodge_applied'] = True
        
        # Calculate doubled Defense
        defense = self.combat.get_defense(self.caller)
        
        self.caller.location.msg_contents(
            f"{self.caller.name} takes a defensive stance, doubling their Defense to {defense}!"
        )
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
        self.caller.msg("You spend your action to dodge. Your Defense is doubled until your next turn.")
    
    def aim(self):
        """Aim at target for bonus next turn"""
        if not self.args:
            self.caller.msg("Usage: +combat/aim [target]")
            return
            
        if not self._check_turn():
            return
            
        target = search_combat_target(self.caller, self.args) if self.args else None
        
        # Get current aim bonus
        current_aim = self.combat.participants[self.caller].get('aim_bonus', 0)
        target_aimed_at = self.combat.participants[self.caller].get('aim_target')
        
        # Check if aiming at same target
        if target and target_aimed_at and target != target_aimed_at:
            self.caller.msg("You lose your accumulated aim bonus by switching targets.")
            current_aim = 0
            
        # Maximum +3 aim bonus
        if current_aim >= 3:
            self.caller.msg("You are already at maximum aim bonus (+3).")
            return
            
        # Set aim data
        new_aim = current_aim + 1
        self.combat.participants[self.caller]['aim_bonus'] = new_aim
        if target:
            self.combat.participants[self.caller]['aim_target'] = target
            
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
        
        target_name = target.name if target else "carefully"
        self.caller.location.msg_contents(
            f"{self.caller.name} aims {target_name} (+{new_aim} dice to next attack)."
        )
    
    # ========================================
    # HELPER METHODS
    # ========================================
    
    def _check_turn(self):
        """Check if it's the caller's turn"""
        if self.caller not in self.combat.participants:
            self.caller.msg("You are not in combat.")
            return False
            
        if self.combat.current_actor != self.caller:
            self.caller.msg("It's not your turn.")
            return False
            
        if self.combat.participants[self.caller].get('has_acted'):
            self.caller.msg("You have already acted this turn.")
            return False
            
        return True
    
    def _get_weapon(self, weapon_name=None, weapon_type=None):
        """Get weapon data for attack"""
        if weapon_name:
            # Look for specific weapon in database
            weapon_name = weapon_name.lower().replace(" ", "_")
            if weapon_name in WEAPON_DATA:
                weapon = WEAPON_DATA[weapon_name]
                if weapon_type and weapon.weapon_type != weapon_type:
                    self.caller.msg(f"{weapon.name} is not a {weapon_type} weapon.")
                    return None
                return weapon
            else:
                # Try to find weapon in character's equipment
                if hasattr(self.caller.db, 'equipment') and self.caller.db.equipment:
                    for eq_name, eq_data in self.caller.db.equipment.items():
                        if eq_data.get('type') == 'weapon' and eq_name.lower() == weapon_name:
                            # Convert equipment data to WeaponData object
                            return self._equipment_to_weapon_data(eq_name, eq_data)
                
                self.caller.msg(f"Unknown weapon: {weapon_name}")
                self.caller.msg("Use '+gear' to see your equipment or check available weapons.")
                return None
        else:
            # Use wielded weapon or unarmed
            wielded = self.caller.db.wielded_weapon
            if wielded:
                # First check database
                wielded_key = wielded.lower().replace(" ", "_")
                if wielded_key in WEAPON_DATA:
                    weapon = WEAPON_DATA[wielded_key]
                    if weapon_type and weapon.weapon_type != weapon_type:
                        self.caller.msg(f"Your wielded weapon is not a {weapon_type} weapon.")
                        return None
                    return weapon
                # Then check equipment
                elif hasattr(self.caller.db, 'equipment') and self.caller.db.equipment:
                    if wielded in self.caller.db.equipment:
                        eq_data = self.caller.db.equipment[wielded]
                        if eq_data.get('type') == 'weapon':
                            return self._equipment_to_weapon_data(wielded, eq_data)
            
            # Default to unarmed
            weapon = WEAPON_DATA["unarmed"]
            if weapon_type and weapon_type != "melee":
                self.caller.msg("You need a weapon for that type of attack.")
                return None
            return weapon
    
    def _equipment_to_weapon_data(self, name, equipment_data):
        """Convert equipment data to WeaponData object"""
        return WeaponData(
            name=name,
            damage=equipment_data.get('damage', 0),
            initiative_mod=equipment_data.get('initiative', 0),
            weapon_type=self._determine_weapon_type(equipment_data),
            size=equipment_data.get('size', 1),
            strength_req=equipment_data.get('strength', 1),
            availability=equipment_data.get('availability', 1),
            tags=equipment_data.get('tags', ''),
            capacity=equipment_data.get('capacity', 'single')
        )
    
    def _determine_weapon_type(self, equipment_data):
        """Determine weapon type from equipment data"""
        range_type = equipment_data.get('range', 'melee')
        if range_type in ['long', 'medium', 'extreme']:
            return "ranged"
        elif range_type in ['thrown', 'close'] or 'thrown' in equipment_data.get('tags', ''):
            return "thrown"
        else:
            return "melee"
    
    def _perform_melee_attack(self, target, weapon, dice_bonus=0, special=None):
        """Perform a melee attack"""
        # Calculate attack pool using weapon's method
        base_pool = weapon.get_attack_dice_pool(self.caller)
        
        # Apply weapon attack modifiers (accurate, inaccurate)
        weapon_attack_mod = weapon.get_attack_modifier()
        
        # Apply Defense if weapon type allows it
        current_defense = 0
        if weapon.applies_defense():
            target_defense = self.combat.get_defense(target)
            defense_applied = self.combat.participants[target].get('defense_applied', 0)
            current_defense = max(0, target_defense - defense_applied)
        
        # Calculate final dice pool
        final_pool = base_pool + dice_bonus + weapon_attack_mod - current_defense
        
        # Get wound penalties
        wound_penalty = self._get_wound_penalty(self.caller)
        final_pool += wound_penalty
        
        # Get weapon's special roll types (8-again, 9-again, etc.)
        roll_types = weapon.get_roll_type_modifiers()
        
        # Roll attack
        from world.utils.dice_utils import roll_dice, RollType
        rolls, successes, ones = roll_dice(final_pool, roll_types=roll_types)
        
        # Apply Defense reduction for next attack (only if Defense applied)
        if weapon.applies_defense():
            self.combat.participants[target]['defense_applied'] = defense_applied + 1
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
        
        # Format attack message
        attack_desc = f"{weapon.name} attack"
        if special:
            attack_desc = f"{special} {attack_desc}"
            
        if successes > 0:
            # Hit! Calculate damage: successes + weapon damage rating
            damage = successes + weapon.get_damage_rating()
            
            # Determine damage type (lethal for weapons, bashing for unarmed)
            damage_type = "bashing" if weapon.name == "Unarmed" else "lethal"
            
            self._apply_damage(target, damage, damage_type, weapon)
            
            # Check for weapon-caused tilts
            self._check_weapon_tilts(target, weapon, damage)
            
            defense_text = f" vs Defense {current_defense}" if current_defense > 0 else ""
            weapon_mods = []
            if weapon_attack_mod != 0:
                weapon_mods.append(f"{weapon_attack_mod:+d} weapon")
            if roll_types != {RollType.TEN_AGAIN}:
                roll_type_names = []
                if RollType.EIGHT_AGAIN in roll_types:
                    roll_type_names.append("8-again")
                elif RollType.NINE_AGAIN in roll_types:
                    roll_type_names.append("9-again")
                weapon_mods.append(", ".join(roll_type_names))
            
            mod_text = f" ({', '.join(weapon_mods)})" if weapon_mods else ""
            
            self.caller.location.msg_contents(
                f"{self.caller.name}'s {attack_desc} hits {target.name} for {damage} {damage_type} damage! "
                f"({successes} successes + {weapon.get_damage_rating()} weapon damage{defense_text}){mod_text}"
            )
        else:
            defense_text = f" vs Defense {current_defense}" if current_defense > 0 else ""
            self.caller.location.msg_contents(
                f"{self.caller.name}'s {attack_desc} misses {target.name}. "
                f"({successes} successes{defense_text})"
            )
    
    def _perform_ranged_attack(self, target, weapon, dice_bonus=0, special=None):
        """Perform a ranged attack"""
        # Calculate attack pool using weapon's method (Dexterity + Firearms)
        base_pool = weapon.get_attack_dice_pool(self.caller)
        
        # Apply weapon attack modifiers (accurate, inaccurate)
        weapon_attack_mod = weapon.get_attack_modifier()
        
        # Apply Defense if weapon allows it (slow weapons allow full Defense)
        current_defense = 0
        if weapon.applies_defense():
            target_defense = self.combat.get_defense(target)
            defense_applied = self.combat.participants[target].get('defense_applied', 0)
            current_defense = max(0, target_defense - defense_applied)
        
        # Calculate final dice pool
        final_pool = base_pool + dice_bonus + weapon_attack_mod - current_defense
        
        # Apply range penalties
        
        # Get wound penalties
        wound_penalty = self._get_wound_penalty(self.caller)
        final_pool += wound_penalty
        
        # Get weapon's special roll types (8-again, 9-again, etc.)
        roll_types = weapon.get_roll_type_modifiers()
        
        # Roll attack
        from world.utils.dice_utils import roll_dice, RollType
        rolls, successes, ones = roll_dice(final_pool, roll_types=roll_types)
        
        # Apply Defense reduction for next attack (only if Defense applied)
        if weapon.applies_defense():
            self.combat.participants[target]['defense_applied'] = defense_applied + 1
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
        
        # Format attack message
        attack_desc = f"{weapon.name} attack"
        if special:
            attack_desc = f"{special} {attack_desc}"
            
        if successes > 0:
            # Hit! Calculate damage: successes + weapon damage rating
            damage = successes + weapon.get_damage_rating()
            self._apply_damage(target, damage, "lethal", weapon)
            
            # Check for weapon-caused tilts
            self._check_weapon_tilts(target, weapon, damage)
            
            defense_text = f" vs Defense {current_defense}" if current_defense > 0 else ""
            weapon_mods = []
            if weapon_attack_mod != 0:
                weapon_mods.append(f"{weapon_attack_mod:+d} weapon")
            if roll_types != {RollType.TEN_AGAIN}:
                roll_type_names = []
                if RollType.EIGHT_AGAIN in roll_types:
                    roll_type_names.append("8-again")
                elif RollType.NINE_AGAIN in roll_types:
                    roll_type_names.append("9-again")
                weapon_mods.append(", ".join(roll_type_names))
            
            mod_text = f" ({', '.join(weapon_mods)})" if weapon_mods else ""
            
            self.caller.location.msg_contents(
                f"{self.caller.name}'s {attack_desc} hits {target.name} for {damage} lethal damage! "
                f"({successes} successes + {weapon.get_damage_rating()} weapon damage{defense_text}){mod_text}"
            )
        else:
            defense_text = f" vs Defense {current_defense}" if current_defense > 0 else ""
            self.caller.location.msg_contents(
                f"{self.caller.name}'s {attack_desc} misses {target.name}. "
                f"({successes} successes{defense_text})"
            )
    
    def _perform_thrown_attack(self, target, weapon, dice_bonus=0, special=None):
        """Perform a thrown weapon attack"""
        # Calculate attack pool using weapon's method (Dexterity + Athletics)
        base_pool = weapon.get_attack_dice_pool(self.caller)
        
        # Apply weapon attack modifiers (accurate, inaccurate)
        weapon_attack_mod = weapon.get_attack_modifier()
        
        # Apply Defense (thrown weapons are subject to Defense)
        target_defense = self.combat.get_defense(target)
        defense_applied = self.combat.participants[target].get('defense_applied', 0)
        current_defense = max(0, target_defense - defense_applied)
        
        # Calculate final dice pool
        final_pool = base_pool + dice_bonus + weapon_attack_mod - current_defense
        
        # Get wound penalties
        wound_penalty = self._get_wound_penalty(self.caller)
        final_pool += wound_penalty
        
        # Get weapon's special roll types (8-again, 9-again, etc.)
        roll_types = weapon.get_roll_type_modifiers()
        
        # Roll attack
        from world.utils.dice_utils import roll_dice, RollType
        rolls, successes, ones = roll_dice(final_pool, roll_types=roll_types)
        
        # Apply Defense reduction for next attack
        self.combat.participants[target]['defense_applied'] = defense_applied + 1
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
        
        # Format attack message
        attack_desc = f"thrown {weapon.name} attack"
        if special:
            attack_desc = f"{special} {attack_desc}"
            
        if successes > 0:
            # Hit! Calculate damage: successes + weapon damage rating
            damage = successes + weapon.get_damage_rating()
            self._apply_damage(target, damage, "lethal", weapon)
            
            # Check for weapon-caused tilts
            self._check_weapon_tilts(target, weapon, damage)
            
            weapon_mods = []
            if weapon_attack_mod != 0:
                weapon_mods.append(f"{weapon_attack_mod:+d} weapon")
            if roll_types != {RollType.TEN_AGAIN}:
                roll_type_names = []
                if RollType.EIGHT_AGAIN in roll_types:
                    roll_type_names.append("8-again")
                elif RollType.NINE_AGAIN in roll_types:
                    roll_type_names.append("9-again")
                weapon_mods.append(", ".join(roll_type_names))
            
            mod_text = f" ({', '.join(weapon_mods)})" if weapon_mods else ""
            
            self.caller.location.msg_contents(
                f"{self.caller.name}'s {attack_desc} hits {target.name} for {damage} lethal damage! "
                f"({successes} successes + {weapon.get_damage_rating()} weapon damage vs Defense {current_defense}){mod_text}"
            )
        else:
            self.caller.location.msg_contents(
                f"{self.caller.name}'s {attack_desc} misses {target.name}. "
                f"({successes} successes vs Defense {current_defense})"
            )
    
    def _get_wound_penalty(self, character):
        """Get wound penalty from health damage"""
        return 0
    
    def _apply_damage(self, target, damage, damage_type, weapon=None):
        """Apply damage to target"""
        self.caller.location.msg_contents(
            f"{target.name} takes {damage} {damage_type} damage!"
        )
    
    def _check_weapon_tilts(self, target, weapon, damage):
        """Check if weapon causes tilts and apply them"""
        tilt_messages = []
        
        # Check if target has tilt system
        if not hasattr(target, 'tilts'):
            return
            
        # Apply weapon-caused tilts
        if weapon.causes_tilt("burning"):
            try:
                from world.tilts import STANDARD_TILTS
                if 'burning' in STANDARD_TILTS:
                    burning_tilt = STANDARD_TILTS['burning']
                    target.tilts.add(burning_tilt)
                    tilt_messages.append(f"{target.name} catches fire!")
            except ImportError:
                tilt_messages.append(f"{target.name} would catch fire! (Tilt system not available)")
                
        if weapon.causes_tilt("bleeding"):
            try:
                from world.tilts import STANDARD_TILTS
                if 'bleeding' in STANDARD_TILTS:
                    bleeding_tilt = STANDARD_TILTS['bleeding']
                    target.tilts.add(bleeding_tilt)
                    tilt_modifier = weapon.get_tilt_modifier("bleeding")
                    tilt_messages.append(f"{target.name} begins bleeding! (Tilt modifier: {tilt_modifier})")
            except ImportError:
                tilt_messages.append(f"{target.name} would bleed! (Tilt system not available)")
                
        if weapon.causes_tilt("knockdown"):
            try:
                from world.tilts import STANDARD_TILTS
                if 'knocked_down' in STANDARD_TILTS:
                    knockdown_tilt = STANDARD_TILTS['knocked_down']
                    target.tilts.add(knockdown_tilt)
                    tilt_modifier = weapon.get_tilt_modifier("knockdown")
                    tilt_messages.append(f"{target.name} is knocked down! (Tilt modifier: {tilt_modifier})")
            except ImportError:
                tilt_messages.append(f"{target.name} would be knocked down! (Tilt system not available)")
                
        if weapon.causes_tilt("stunned"):
            try:
                from world.tilts import STANDARD_TILTS
                if 'stunned' in STANDARD_TILTS:
                    stunned_tilt = STANDARD_TILTS['stunned']
                    target.tilts.add(stunned_tilt)
                    tilt_modifier = weapon.get_tilt_modifier("stunned")
                    tilt_messages.append(f"{target.name} is stunned! (Tilt modifier: {tilt_modifier})")
            except ImportError:
                tilt_messages.append(f"{target.name} would be stunned! (Tilt system not available)")
            
        if tilt_messages:
            self.caller.location.msg_contents(" ".join(tilt_messages))
    
    # ========================================
    # PLACEHOLDER METHODS (to be implemented)
    # ========================================
    
    def grapple(self):
        """Initiate grapple"""
        if not self.args:
            self.caller.msg("Usage: +combat/grapple <target>")
            return
            
        if not self._check_turn():
            return
            
        target = search_combat_target(self.caller, self.args)
        if not target:
            return
            
        if target not in self.combat.participants:
            self.caller.msg(f"{target.name} is not in combat.")
            return
            
        if target == self.caller:
            self.caller.msg("You cannot grapple yourself.")
            return
            
        # Check if either character is already grappling
        if self.combat.is_grappling(self.caller):
            current_partner = self.combat.get_grapple_partner(self.caller)
            self.caller.msg(f"You are already grappling with {current_partner.name}.")
            return
            
        if self.combat.is_grappling(target):
            target_partner = self.combat.get_grapple_partner(target)
            self.caller.msg(f"{target.name} is already grappling with {target_partner.name}.")
            return
            
        # Initiate grapple
        winner = self.combat.initiate_grapple(self.caller, target)
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
        
        if winner:
            if winner == self.caller:
                self.caller.msg(
                    "You successfully initiate the grapple! Choose your grapple action: "
                    "+combat/break, +combat/control, +combat/damage, +combat/disarm, "
                    "+combat/prone, +combat/hold, +combat/restrain, or +combat/takecover"
                )
            else:
                self.caller.msg(f"{target.name} reverses your grapple attempt and now controls the grapple!")
    
    def disarm(self):
        """Disarm opponent in grapple"""
        if not self.combat.is_grappling(self.caller):
            self.caller.msg("You can only disarm in a grapple.")
            return
            
        if not self.combat.is_grapple_controller(self.caller):
            self.caller.msg("You do not control the grapple.")
            return
            
        # Must have control of weapons first
        if not self.combat.participants[self.caller]['grapple_actions'].get('control_weapon'):
            self.caller.msg("You must Control Weapon before you can Disarm your opponent.")
            return
            
        partner = self.combat.get_grapple_partner(self.caller)
        self.caller.location.msg_contents(
            f"{self.caller.name} disarms {partner.name}, removing their weapon from the grapple entirely!"
        )
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
    
    def touch_attack(self):
        """Touch attack - placeholder"""
        self.caller.msg("Touch attack system not yet implemented.")
    
    def grapple_break(self):
        """Break from grapple - reflexive action"""
        if not self.combat.is_grappling(self.caller):
            self.caller.msg("You are not currently grappling.")
            return
            
        # Break free is reflexive and automatic
        self.combat.break_grapple(self.caller)
        
        # Since it's reflexive, caller can take another action
        self.caller.msg("You break free from the grapple! You may take another action this turn.")
    
    def grapple_control(self):
        """Control weapon in grapple"""
        if not self.combat.is_grappling(self.caller):
            self.caller.msg("You are not currently grappling.")
            return
            
        if not self.combat.is_grapple_controller(self.caller):
            self.caller.msg("You do not control the grapple.")
            return
            
        # Set control weapon flag
        self.combat.participants[self.caller]['grapple_actions']['control_weapon'] = True
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
        
        partner = self.combat.get_grapple_partner(self.caller)
        self.caller.location.msg_contents(
            f"{self.caller.name} controls weapons in the grapple with {partner.name}!"
        )
        self.caller.msg("You now control weapons in the grapple. You can draw weapons or turn your opponent's weapon against them.")
    
    def grapple_damage(self):
        """Deal damage in grapple"""
        if not self.combat.is_grappling(self.caller):
            self.caller.msg("You are not currently grappling.")
            return
            
        if not self.combat.is_grapple_controller(self.caller):
            self.caller.msg("You do not control the grapple.")
            return
            
        partner = self.combat.get_grapple_partner(self.caller)
        
        # Roll Strength + Brawl for damage
        strength = self.caller.db.stats.get("attributes", {}).get("strength", 1)
        brawl = self.caller.db.stats.get("skills", {}).get("brawl", 0)
        dice_pool = strength + brawl
        
        # Apply wound penalties
        wound_penalty = self._get_wound_penalty(self.caller)
        dice_pool += wound_penalty
        
        # Roll for successes
        from world.utils.dice_utils import roll_dice, RollType
        rolls, successes, ones = roll_dice(dice_pool)
        
        # Calculate damage
        base_damage = successes
        
        # Add weapon modifier if controlling weapons
        if self.combat.participants[self.caller]['grapple_actions'].get('control_weapon'):
            weapon_modifier = 1
            base_damage += weapon_modifier
            weapon_text = f" (+{weapon_modifier} weapon modifier)"
        else:
            weapon_text = ""
            
        # Apply damage
        if base_damage > 0:
            self._apply_damage(partner, base_damage, "bashing")
            self.caller.location.msg_contents(
                f"{self.caller.name} deals {base_damage} bashing damage to {partner.name} in the grapple! "
                f"({successes} successes{weapon_text})"
            )
        else:
            self.caller.location.msg_contents(
                f"{self.caller.name} fails to damage {partner.name} in the grapple. ({successes} successes)"
            )
            
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
    
    def grapple_restrain(self):
        """Restrain opponent in grapple"""
        if not self.combat.is_grappling(self.caller):
            self.caller.msg("You are not currently grappling.")
            return
            
        if not self.combat.is_grapple_controller(self.caller):
            self.caller.msg("You do not control the grapple.")
            return
            
        # Must have succeeded at Hold first
        if not self.combat.participants[self.caller]['grapple_actions'].get('held'):
            self.caller.msg("You must successfully Hold your opponent before you can Restrain them.")
            return
            
        partner = self.combat.get_grapple_partner(self.caller)
        
        # Set restrained flag
        self.combat.participants[partner]['grapple_actions']['restrained'] = True
        
        # Apply Immobilized Tilt (placeholder - would integrate with tilt system)
        self.caller.location.msg_contents(
            f"{self.caller.name} restrains {partner.name}! {partner.name} suffers the Immobilized Tilt."
        )
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
        
        # Can leave grapple if using equipment
        self.caller.msg("You have restrained your opponent. If you used equipment (zip ties, etc.), you may leave the grapple.")
    
    def grapple_takecover(self):
        """Use opponent as human shield"""
        if not self.combat.is_grappling(self.caller):
            self.caller.msg("You are not currently grappling.")
            return
            
        if not self.combat.is_grapple_controller(self.caller):
            self.caller.msg("You do not control the grapple.")
            return
            
        partner = self.combat.get_grapple_partner(self.caller)
        
        # Set taking cover flag
        self.combat.participants[self.caller]['grapple_actions']['taking_cover'] = True
        
        self.caller.location.msg_contents(
            f"{self.caller.name} uses {partner.name} as a human shield! "
            f"Ranged attacks against {self.caller.name} will automatically hit {partner.name} instead."
        )
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
    
    def grapple_prone(self):
        """Drop both characters prone in grapple"""
        if not self.combat.is_grappling(self.caller):
            self.caller.msg("You are not currently grappling.")
            return
            
        if not self.combat.is_grapple_controller(self.caller):
            self.caller.msg("You do not control the grapple.")
            return
            
        partner = self.combat.get_grapple_partner(self.caller)
        
        # Set both characters prone
        self.combat.participants[self.caller]['prone'] = True
        self.combat.participants[partner]['prone'] = True
        
        self.caller.location.msg_contents(
            f"{self.caller.name} throws both themselves and {partner.name} to the ground! "
            f"Both characters are now prone. They must Break Free before rising."
        )
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
    
    def grapple_hold(self):
        """Hold opponent in place"""
        if not self.combat.is_grappling(self.caller):
            self.caller.msg("You are not currently grappling.")
            return
            
        if not self.combat.is_grapple_controller(self.caller):
            self.caller.msg("You do not control the grapple.")
            return
            
        partner = self.combat.get_grapple_partner(self.caller)
        
        # Set held flag
        self.combat.participants[self.caller]['grapple_actions']['held'] = True
        
        self.caller.location.msg_contents(
            f"{self.caller.name} holds {partner.name} in place! "
            f"Neither character can apply Defense against incoming attacks."
        )
        
        # Mark as having acted
        self.combat.participants[self.caller]['has_acted'] = True
    
    def autofire(self):
        """Autofire - placeholder"""
        self.caller.msg("Autofire system not yet implemented.")
    
    def burst_fire(self):
        """Burst fire - placeholder"""
        self.caller.msg("Burst fire system not yet implemented.")
    
    def covering_fire(self):
        """Covering fire - placeholder"""
        self.caller.msg("Covering fire system not yet implemented.")
    
    def reload(self):
        """Reload weapon - placeholder"""
        self.caller.msg("Reload system not yet implemented.")
    
    def move(self):
        """Move in combat - placeholder"""
        self.caller.msg("Movement system not yet implemented.")
    
    def run(self):
        """Run in combat - placeholder"""
        self.caller.msg("Movement system not yet implemented.")
    
    def go_prone(self):
        """Go prone - placeholder"""
        self.caller.msg("Prone system not yet implemented.")
    
    def rise(self):
        """Rise from prone - placeholder"""
        self.caller.msg("Prone system not yet implemented.")
    
    def take_cover(self):
        """Take cover - placeholder"""
        self.caller.msg("Cover system not yet implemented.")
    
    def leave_cover(self):
        """Leave cover - placeholder"""
        self.caller.msg("Cover system not yet implemented.")
    
    def wield_weapon(self):
        """Wield a weapon"""
        if not self.args:
            self.caller.msg("Usage: +combat/wield <weapon>")
            return
            
        weapon_name = self.args.strip()
        
        # Check if weapon exists in database or equipment
        weapon_key = weapon_name.lower().replace(" ", "_")
        if weapon_key in WEAPON_DATA:
            # Set wielded weapon
            self.caller.db.wielded_weapon = weapon_name
            self.caller.msg(f"You ready {WEAPON_DATA[weapon_key].name} for combat.")
            self.caller.location.msg_contents(
                f"{self.caller.name} readies {WEAPON_DATA[weapon_key].name}.",
                exclude=[self.caller]
            )
        elif hasattr(self.caller.db, 'equipment') and self.caller.db.equipment:
            # Check character's equipment
            for eq_name, eq_data in self.caller.db.equipment.items():
                if eq_data.get('type') == 'weapon' and eq_name.lower() == weapon_name.lower():
                    self.caller.db.wielded_weapon = eq_name
                    self.caller.msg(f"You ready {eq_name} for combat.")
                    self.caller.location.msg_contents(
                        f"{self.caller.name} readies {eq_name}.",
                        exclude=[self.caller]
                    )
                    return
            self.caller.msg(f"You don't have {weapon_name}.")
        else:
            self.caller.msg(f"Unknown weapon: {weapon_name}")
    
    def drop_weapon(self):
        """Drop weapon (reflexive action)"""
        if not self.caller.db.wielded_weapon:
            self.caller.msg("You are not wielding a weapon.")
            return
            
        weapon_name = self.caller.db.wielded_weapon
        self.caller.db.wielded_weapon = None
        
        self.caller.msg(f"You drop {weapon_name}. (Reflexive action)")
        self.caller.location.msg_contents(
            f"{self.caller.name} drops {weapon_name}.",
            exclude=[self.caller]
        )
    
    def draw_weapon(self):
        """Draw weapon (instant action)"""
        if not self.args:
            self.caller.msg("Usage: +combat/draw <weapon>")
            return
            
        if not self._check_turn():
            return
            
        weapon_name = self.args.strip()
        
        # Check if weapon exists
        weapon_key = weapon_name.lower().replace(" ", "_")
        if weapon_key in WEAPON_DATA or (hasattr(self.caller.db, 'equipment') and 
                                        any(eq_data.get('type') == 'weapon' and eq_name.lower() == weapon_name.lower() 
                                            for eq_name, eq_data in self.caller.db.equipment.items())):
            
            # Drawing a weapon is an instant action
            self.caller.db.wielded_weapon = weapon_name
            self.combat.participants[self.caller]['has_acted'] = True
            
            self.caller.msg(f"You draw {weapon_name}. (Instant action)")
            self.caller.location.msg_contents(
                f"{self.caller.name} draws {weapon_name}.",
                exclude=[self.caller]
            )
        else:
            self.caller.msg(f"You don't have {weapon_name}.")
    
    def wear_armor(self):
        """Wear armor - placeholder"""
        self.caller.msg("Armor system not yet fully implemented.")
    
    def remove_armor(self):
        """Remove armor - placeholder"""
        self.caller.msg("Armor system not yet fully implemented.")
    
    def delay_action(self):
        """Delay action - placeholder"""
        self.caller.msg("Delay system not yet implemented.")
    
    def wait(self):
        """Wait/end turn - placeholder"""
        if not self._check_turn():
            return
            
        self.combat.participants[self.caller]['has_acted'] = True
        self.caller.location.msg_contents(f"{self.caller.name} waits and ends their turn.")
    
    def spend_willpower(self):
        """Spend Willpower - placeholder"""
        self.caller.msg("Willpower system not yet implemented.")
    
    def surprise_attack(self):
        """Surprise attack - placeholder"""
        self.caller.msg("Surprise system not yet implemented.")

class CmdCombatHelp(BasePyReachCommand):
    """
    Get quick combat help and action reference.
    """
    
    key = "+chelp"
    aliases = ["+combathelp"]
    help_category = "Automated Combat System"
    
    def func(self):
        """Execute the command"""
        output = [
            "|cChronicles of Darkness Combat Quick Reference|n",
            "",
            "|yBasic Combat Flow:|n",
            "1. Join combat: +combat/join [team]",
            "2. Roll initiative: +combat/init",
            "3. Take actions on your turn",
            "",
            "|yCommon Commands:|n",
            "+combat/status - Show combat status",
            "+combat/join - Join combat",
            "+combat/leave - Leave combat",
            "+combat/end - End combat (staff only)"
        ]
        
        self.caller.msg("\n".join(output))

class CmdWeapons(BasePyReachCommand):
    """
    List available weapons from the equipment database.
    """
    
    key = "+weapons"
    aliases = ["+weaponlist"]
    help_category = "Automated Combat System"
    
    def func(self):
        """Execute the command"""
        from world.equipment_database import WEAPON_DATABASE, WEAPON_TAG_DESCRIPTIONS
        
        output = ["|cAvailable Weapons (Chronicles of Darkness: Hurt Locker)|n"]
        
        # Categorize weapons
        categories = {
            "Unarmed": [],
            "Melee - Bladed": [],
            "Melee - Blunt": [],
            "Melee - Exotic": [],
            "Melee - Polearms": [],
            "Ranged - Archery": [],
            "Ranged - Firearms": [],
            "Ranged - Nonlethal": [],
            "Thrown Weapons": [],
            "Explosives": []
        }
        
        for weapon_key, weapon in WEAPON_DATABASE.items():
            weapon_str = f"|y{weapon.name}|n - Dmg:{weapon.damage} Init:{weapon.initiative_mod:+d} Str:{weapon.strength_req} Size:{weapon.size}"
            if weapon.tags:
                weapon_str += f" |c({weapon.tags})|n"
            
            # Categorize weapons
            if weapon_key == "unarmed":
                categories["Unarmed"].append(weapon_str)
            elif weapon.weapon_type == "thrown":
                categories["Thrown Weapons"].append(weapon_str)
            elif weapon.weapon_type == "ranged":
                if any(arch in weapon_key for arch in ["bow", "crossbow"]):
                    categories["Ranged - Archery"].append(weapon_str)
                elif any(nonlethal in weapon_key for nonlethal in ["pepper", "stun"]):
                    categories["Ranged - Nonlethal"].append(weapon_str)
                elif any(explosive in weapon_key for explosive in ["grenade", "molotov"]):
                    categories["Explosives"].append(weapon_str)
                else:
                    categories["Ranged - Firearms"].append(weapon_str)
            elif weapon.weapon_type == "melee":
                if any(blade in weapon_key for blade in ["axe", "sword", "knife", "machete", "rapier", "hatchet"]):
                    categories["Melee - Bladed"].append(weapon_str)
                elif any(blunt in weapon_key for blunt in ["brass", "club", "nightstick", "nunchaku", "sap", "sledge"]):
                    categories["Melee - Blunt"].append(weapon_str)
                elif any(pole in weapon_key for pole in ["spear", "staff"]):
                    categories["Melee - Polearms"].append(weapon_str)
                else:
                    categories["Melee - Exotic"].append(weapon_str)
        
        # Display categories
        for category, weapons in categories.items():
            if weapons:
                output.append(f"\n|g{category}:|n")
                for weapon in sorted(weapons):
                    output.append(f"  {weapon}")
        
        output.append(f"\n|yUsage:|n")
        output.append("  +combat/wield <weapon> - Ready weapon for combat")
        output.append("  +combat/attack <target> <weapon> - Attack with specific weapon")
        output.append("  +equipment/add <weapon_name> weapon - Add weapon to inventory")
        
        self.caller.msg("\n".join(output))

class CmdEquippedGear(BasePyReachCommand):
    """
    View your currently equipped weapons and armor.
    """
    
    key = "+gear"
    aliases = ["+equipped"]
    help_category = "Automated Combat System"
    
    def func(self):
        """Execute the command"""
        target = self.caller
        if self.args:
            # Gear viewing can work globally (not combat action)
            target = search_character(self.caller, self.args)
            if not target:
                return
            
        output = [f"Equipped gear for {target.name}:"]
        
        # Show wielded weapon
        wielded_weapon = target.db.wielded_weapon
        if wielded_weapon:
            output.append(f"Wielded: {wielded_weapon}")
        else:
            output.append("Wielded: None (unarmed)")
            
        # Show worn armor
        worn_armor = target.db.worn_armor
        if worn_armor:
            output.append(f"Armor: {worn_armor}")
        else:
            output.append("Armor: None")
            
        self.caller.msg("\n".join(output))
