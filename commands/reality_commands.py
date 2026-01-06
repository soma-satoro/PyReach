"""
Reality System Commands

Commands for interacting with different realities:
- Fae Reality (Mask/Mien)
- Shadow/Hisil
- Hedge
- Loci
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.evtable import EvTable
from evennia.utils import utils
from evennia.utils.search import search_object
from world.reality_systems import *
from utils.text import process_special_characters
from world.utils.dice_utils import roll_dice
from datetime import timedelta
from django.utils import timezone


def roll_and_format(dice_pool, difficulty=8):
    """
    Helper function to roll dice and format the result.
    
    Args:
        dice_pool (int): Number of dice to roll
        difficulty (int): Difficulty target
        
    Returns:
        dict: Result dictionary with keys 'roll_display', 'successes', 'rolls'
    """
    rolls, successes, ones = roll_dice(dice_pool, difficulty=difficulty)
    
    # Format the roll display
    roll_display = ", ".join(str(r) for r in rolls)
    
    return {
        'roll_display': roll_display,
        'successes': successes,
        'ones': ones,
        'rolls': rolls
    }


class CmdMien(MuxCommand):
    """
    Set or view your Mien (true fae appearance).
    
    Usage:
      +mien - View your current Mien
      +mien <description> - Set your Mien description
      
    Changelings and Fae-Touched have a Mien that represents their true fae nature.
    This description is visible to other Changelings, Fae-Touched, and those
    enchanted by pledges (unless you strengthen your Mask).
    
    Changeling players MUST set their Mien. Other Changelings will see a note
    that you need to set your Mien until you do so.
    
    Examples:
      +mien
      +mien Her eyes glow with an ethereal silver light, and delicate antlers
            sprout from her temples. Her skin has a faint verdant hue, like
            fresh spring leaves.
    """
    
    key = "+mien"
    aliases = ["mien"]
    locks = "cmd:all()"
    help_category = "Character"
    
    def func(self):
        caller = self.caller
        
        # Check if character can have a Mien
        if not has_mien(caller):
            caller.msg("Only Changelings and Fae-Touched have Miens.")
            return
        
        # View current Mien
        if not self.args:
            current_mien = get_mien_description(caller)
            if current_mien:
                caller.msg(f"|wYour Mien:|n\n{current_mien}")
            else:
                caller.msg("You have not set your Mien yet.")
                if get_template(caller) == "Changeling":
                    caller.msg("|yNote:|n As a Changeling, you MUST set your Mien. "
                             "Other Changelings will see an OOC note until you do.")
            return
        
        # Set Mien
        description = self.args.strip()
        
        # Process special characters
        description = process_special_characters(description)
        
        # Set the Mien
        set_mien_description(caller, description)
        caller.msg("|gMien set successfully.|n")
        caller.msg(f"Your Mien is now:\n{description}")


class CmdMask(MuxCommand):
    """
    Strengthen or shed your Mask.
    
    Usage:
      +mask - View your current Mask status
      +mask/strengthen - Strengthen your Mask (costs 1 Glamour, lasts one scene)
      +mask/shed - Shed your Mask (costs 1 Glamour, lasts one scene)
      +mask/clear - Clear your Mask modifications (end the scene)
      
    Changelings can manipulate their Mask (human appearance) by spending Glamour:
    
    Strengthen Mask:
      You appear completely human to everyone, including other Changelings and
      Fae-Touched. They see your normal description instead of your Mien.
      Costs 1 Glamour and lasts for one scene.
      
    Shed Mask:
      Your Mien becomes visible to everyone, including mortals who normally
      couldn't see it. Everyone sees your Mien instead of your normal description.
      Costs 1 Glamour and lasts for one scene.
      
    Examples:
      +mask
      +mask/strengthen
      +mask/shed
      +mask/clear
    """
    
    key = "+mask"
    aliases = ["mask"]
    locks = "cmd:all()"
    help_category = "Character"
    
    def func(self):
        caller = self.caller
        
        # Only Changelings can manipulate their Mask
        if get_template(caller) != "Changeling":
            caller.msg("Only Changelings can manipulate their Mask.")
            return
        
        # View current status
        if not self.switches:
            strengthened = getattr(caller.db, 'mask_strengthened', False)
            shed = getattr(caller.db, 'mask_shed', False)
            
            if strengthened:
                caller.msg("|wMask Status:|n Strengthened (appears human to all)")
            elif shed:
                caller.msg("|wMask Status:|n Shed (Mien visible to all)")
            else:
                caller.msg("|wMask Status:|n Normal (Mien visible to fae-aware)")
            return
        
        switch = self.switches[0].lower()
        
        if switch == "strengthen":
            # Check if already strengthened
            if getattr(caller.db, 'mask_strengthened', False):
                caller.msg("Your Mask is already strengthened.")
                return
            
            # Check for shed mask
            if getattr(caller.db, 'mask_shed', False):
                caller.msg("You must clear your shed Mask first.")
                return
            
            # Check Glamour
            glamour_current = caller.db.stats.get("glamour_current", 0)
            if glamour_current < 1:
                caller.msg("You need at least 1 Glamour to strengthen your Mask.")
                return
            
            # Spend Glamour
            caller.db.stats["glamour_current"] = glamour_current - 1
            
            # Set strengthened
            caller.db.mask_strengthened = True
            caller.db.mask_shed = False
            
            caller.msg("|gYou strengthen your Mask, appearing completely human to all.|n")
            caller.msg("This will last for one scene. Use '+mask/clear' to end it early.")
            caller.msg(f"Glamour: {glamour_current - 1}/{caller.db.stats.get('advantages', {}).get('glamour', 10)}")
            
        elif switch == "shed":
            # Check if already shed
            if getattr(caller.db, 'mask_shed', False):
                caller.msg("Your Mask is already shed.")
                return
            
            # Check for strengthened mask
            if getattr(caller.db, 'mask_strengthened', False):
                caller.msg("You must clear your strengthened Mask first.")
                return
            
            # Check Glamour
            glamour_current = caller.db.stats.get("glamour_current", 0)
            if glamour_current < 1:
                caller.msg("You need at least 1 Glamour to shed your Mask.")
                return
            
            # Spend Glamour
            caller.db.stats["glamour_current"] = glamour_current - 1
            
            # Set shed
            caller.db.mask_shed = True
            caller.db.mask_strengthened = False
            
            caller.msg("|gYou shed your Mask, revealing your Mien to all.|n")
            caller.msg("This will last for one scene. Use '+mask/clear' to end it early.")
            caller.msg(f"Glamour: {glamour_current - 1}/{caller.db.stats.get('advantages', {}).get('glamour', 10)}")
            
        elif switch == "clear":
            # Clear both
            was_modified = getattr(caller.db, 'mask_strengthened', False) or getattr(caller.db, 'mask_shed', False)
            
            caller.db.mask_strengthened = False
            caller.db.mask_shed = False
            
            if was_modified:
                caller.msg("|gYour Mask returns to normal.|n")
            else:
                caller.msg("Your Mask is already normal.")
        else:
            caller.msg("Valid switches: /strengthen, /shed, /clear")


class CmdReach(MuxCommand):
    """
    Step sideways across the Gauntlet or peek into the Shadow.
    
    Usage:
      +reach - Attempt to cross the Gauntlet (enter or leave Shadow)
      +reach/peek - Look across the Gauntlet without crossing
      +reach/essence - Spend 1 Essence to cross faster (Werewolves only)
      +reach/help - Show detailed help about Gauntlet mechanics
      
    Werewolves and Mages with Spirit 3+ can step sideways across the Gauntlet
    to enter the Shadow (Hisil). The difficulty depends on your Harmony/Gnosis,
    the local Gauntlet strength, and other factors.
    
    Werewolves with Harmony 3 or lower don't need a Locus to enter the Shadow.
    Werewolves with Harmony 8 or higher don't need a Locus to enter the Flesh.
    Mages must use the Reaching spell (Spirit 3) to cross.
    
    Modifiers:
      - Gauntlet strength (varies by location)
      - Staring into reflective surface: +1
      - Crossing into Shadow during day: -2
      - Crossing into Flesh during day: +2
      
    Examples:
      +reach
      +reach/peek
      +reach/essence
    """
    
    key = "+reach"
    aliases = ["reach"]
    locks = "cmd:all()"
    help_category = "Supernatural"
    
    def func(self):
        caller = self.caller
        location = caller.location
        
        if not location:
            caller.msg("You must be in a location to use this command.")
            return
        
        # Check help switch
        if self.switches and self.switches[0].lower() == "help":
            self.show_detailed_help()
            return
        
        # Check if character can cross or peek
        if not self.switches or self.switches[0].lower() not in ["peek"]:
            if not can_cross_gauntlet(caller):
                caller.msg("You don't have the ability to cross the Gauntlet.")
                caller.msg("Werewolves and Mages with Spirit 3+ can step sideways.")
                return
        else:
            if not can_peek_across_gauntlet(caller):
                caller.msg("You don't have the ability to see across the Gauntlet.")
                caller.msg("Werewolves and Mages with Spirit 1+ can peek into the Shadow.")
                return
        
        # Handle peek
        if self.switches and self.switches[0].lower() == "peek":
            self.handle_peek()
            return
        
        # Handle essence spending
        spend_essence = self.switches and self.switches[0].lower() == "essence"
        
        # Handle crossing
        self.handle_crossing(spend_essence)
    
    def show_detailed_help(self):
        """Show detailed help about Gauntlet mechanics."""
        help_text = """
|wGauntlet Mechanics|n

The Gauntlet is the barrier between the material world and the Shadow (Hisil).

|cGauntlet Strength:|n
  0 - Verge (no Gauntlet, worlds merge)
  1 - Locus (thin barrier, +2 dice)
  2 - Wilderness (0 modifier)
  3 - Small towns/villages (-1 dice)
  4 - City suburbs (-2 dice)
  5 - Dense urban (-3 dice)

|cWerewolf Crossing:|n
  Enter Shadow: Roll 10 - Harmony + Gauntlet modifier
  Enter Flesh: Roll Harmony + Gauntlet modifier
  
  - Harmony 3 or lower: No Locus needed to enter Shadow
  - Harmony 8 or higher: No Locus needed to enter Flesh
  - Spending Essence: Narr narrates faster crossing, no mechanical effect

|cMage Crossing:|n
  - Requires Spirit 3 (Reaching spell)
  - Spirit 4 (World Walker): Can bring others across
  - Roll Gnosis + Spirit vs Gauntlet Strength

|cModifiers:|n
  - Reflective surface: +1
  - Crossing to Shadow during day: -2
  - Crossing to Flesh during day: +2

|cPeeking:|n
  - Werewolves can always peek
  - Mages with Spirit 1+ (Exorcist's Eye spell)
  - See Hisil description and entities there
"""
        self.caller.msg(help_text)
    
    def handle_peek(self):
        """Handle peeking across the Gauntlet."""
        caller = self.caller
        location = caller.location
        
        # Check if already peeking
        if is_peeking_shadow(caller):
            # Stop peeking
            set_peeking_state(caller, False)
            caller.msg("|gYou stop peering into the Shadow.|n")
            return
        
        # Start peeking
        set_peeking_state(caller, True)
        caller.msg("|gYou peer across the Gauntlet into the Shadow...|n")
        
        # Show Hisil description
        hisil_desc = getattr(location.db, 'hisil_desc', None)
        if hisil_desc:
            caller.msg(f"\n|wThe Shadow:|n\n{hisil_desc}")
        else:
            caller.msg("\nYou see a shadowy reflection of the material world, "
                      "but no specific details have been set for this location.")
        
        # Show characters/objects in Shadow
        in_shadow = [obj for obj in location.contents 
                    if hasattr(obj, 'has_account') and obj.has_account 
                    and is_in_shadow(obj)]
        
        if in_shadow:
            caller.msg("\n|wPresences in the Shadow:|n")
            for obj in in_shadow:
                caller.msg(f"  {obj.get_display_name(caller)}")
    
    def handle_crossing(self, spend_essence=False):
        """Handle crossing the Gauntlet."""
        caller = self.caller
        location = caller.location
        template = get_template(caller)
        
        # Determine if entering or leaving Shadow
        currently_in_shadow = is_in_shadow(caller)
        entering_shadow = not currently_in_shadow
        
        # Check for Locus requirement
        gauntlet_strength, gauntlet_mod = get_gauntlet_rating(location)
        needs_locus = True
        
        if template == "Werewolf":
            harmony = get_harmony(caller)
            
            if entering_shadow and harmony <= 3:
                needs_locus = False
            elif not entering_shadow and harmony >= 8:
                needs_locus = False
            
            if needs_locus and not is_locus(location):
                caller.msg("You need to be at a Locus to cross the Gauntlet with your current Harmony.")
                if entering_shadow:
                    caller.msg(f"(Harmony {harmony}: Need Harmony 3 or lower to cross anywhere)")
                else:
                    caller.msg(f"(Harmony {harmony}: Need Harmony 8 or higher to cross anywhere)")
                return
        elif template == "Mage":
            # Mages always need to check for successful spell casting
            # For now, we'll just require a roll
            pass
        
        # Handle essence spending for Werewolves
        if spend_essence:
            if template != "Werewolf":
                caller.msg("Only Werewolves can spend Essence to cross faster.")
                return
            
            essence_current = caller.db.stats.get("essence_current", 0)
            if essence_current < 1:
                caller.msg("You don't have enough Essence.")
                return
            
            caller.db.stats["essence_current"] = essence_current - 1
            caller.msg("|gYou spend 1 Essence to hasten your crossing.|n")
            caller.msg("(This is a narrative effect - the crossing happens more quickly in-story)")
            essence_max = caller.db.stats.get("advantages", {}).get("essence", 10)
            caller.msg(f"Essence: {essence_current - 1}/{essence_max}")
        
        # Calculate dice pool
        if template == "Werewolf":
            dice_pool, modifiers_text = calculate_gauntlet_pool(caller, location, entering_shadow)
            
            caller.msg("|wCrossing the Gauntlet|n")
            caller.msg(modifiers_text)
            
            # Make the roll
            if dice_pool <= 0:
                caller.msg("\n|rYour dice pool is 0 or negative. You cannot cross.|n")
                return
            
            result = roll_and_format(dice_pool, difficulty=8)
            successes = result.get('successes', 0)
            
            caller.msg(f"\nRolling {dice_pool} dice: {result.get('roll_display', '')}")
            caller.msg(f"Successes: {successes}")
            
            if successes < 1:
                caller.msg("|rYou fail to cross the Gauntlet.|n")
                return
            
            # Success!
            self.complete_crossing(entering_shadow)
            
        elif template == "Mage":
            # Mages use the Reaching spell
            caller.msg("|wAttempting to use Reaching spell...|n")
            
            # Get Spirit rating
            powers = caller.db.stats.get("powers", {})
            arcana = powers.get("arcana", {})
            spirit_level = arcana.get("spirit", 0)
            if isinstance(spirit_level, dict):
                spirit_level = spirit_level.get("dots", 0)
            
            if spirit_level < 3:
                caller.msg("|rYou need Spirit 3 to cast Reaching.|n")
                return
            
            # Get Gnosis
            gnosis = caller.db.stats.get("advantages", {}).get("gnosis", 1)
            if isinstance(gnosis, dict):
                gnosis = gnosis.get("dots", 1)
            
            # Calculate dice pool: Gnosis + Spirit
            dice_pool = gnosis + spirit_level
            
            caller.msg(f"Dice pool: Gnosis ({gnosis}) + Spirit ({spirit_level}) = {dice_pool}")
            caller.msg(f"Target: Gauntlet Strength {gauntlet_strength}")
            
            # Make the roll
            result = roll_and_format(dice_pool, difficulty=8)
            successes = result.get('successes', 0)
            
            caller.msg(f"\nRolling {dice_pool} dice: {result.get('roll_display', '')}")
            caller.msg(f"Successes: {successes}")
            
            if successes < gauntlet_strength:
                caller.msg(f"|rYou need {gauntlet_strength} successes to cross. You failed.|n")
                return
            
            # Success!
            self.complete_crossing(entering_shadow)
    
    def complete_crossing(self, entering_shadow):
        """Complete the crossing after a successful roll."""
        caller = self.caller
        location = caller.location
        
        # Toggle Shadow state
        set_shadow_state(caller, entering_shadow)
        
        # Clear peeking state
        set_peeking_state(caller, False)
        
        # Announce
        if entering_shadow:
            caller.msg("\n|gYou step sideways into the Shadow!|n")
            caller.msg("The material world fades, replaced by the spirit realm.")
            
            # Show Hisil description
            hisil_desc = getattr(location.db, 'hisil_desc', None)
            if hisil_desc:
                caller.msg(f"\n{hisil_desc}")
            
            # Announce to others in Shadow
            for obj in location.contents:
                if obj != caller and hasattr(obj, 'has_account') and obj.has_account:
                    if is_in_shadow(obj):
                        obj.msg(f"{caller.name} steps into the Shadow.")
        else:
            caller.msg("\n|gYou step back into the material world!|n")
            caller.msg("The Shadow fades, replaced by the physical realm.")
            
            # Announce to others in material world
            for obj in location.contents:
                if obj != caller and hasattr(obj, 'has_account') and obj.has_account:
                    if not is_in_shadow(obj):
                        obj.msg(f"{caller.name} steps out of the Shadow.")


class CmdLocus(MuxCommand):
    """
    View and interact with Loci (places of spiritual power).
    
    Usage:
      +locus - View Locus information for current location
      +locus/create <level>=<resonance> - Create a Locus here (Staff only)
      +locus/draw <amount> - Draw essence/mana from this Locus
      +locus/refresh - Force a refresh of Locus essence (Staff only)
      +locus/list - List all Loci in the game (Staff only)
      
    Loci are places where the Gauntlet is thin (strength 1) and spiritual
    energy collects. Werewolves and Mages can draw Essence/Mana from Loci
    when in the Shadow.
    
    Locus Levels: 1-5
    Essence Generation: Level × 3 per day
    
    Examples:
      +locus
      +locus/create 3=rage
      +locus/draw 5
      +locus/refresh
    """
    
    key = "+locus"
    aliases = ["locus"]
    locks = "cmd:all()"
    help_category = "Supernatural"
    
    def func(self):
        caller = self.caller
        location = caller.location
        
        if not location:
            caller.msg("You must be in a location to use this command.")
            return
        
        # Handle different switches
        if not self.switches:
            self.show_locus_info()
        elif self.switches[0].lower() == "create":
            self.create_locus()
        elif self.switches[0].lower() == "draw":
            self.draw_from_locus()
        elif self.switches[0].lower() == "refresh":
            self.refresh_locus()
        elif self.switches[0].lower() == "list":
            self.list_all_loci()
        else:
            caller.msg("Valid switches: /create, /draw, /refresh, /list")
    
    def show_locus_info(self):
        """Show information about the Locus at current location."""
        caller = self.caller
        location = caller.location
        
        if not is_locus(location):
            caller.msg("This location is not a Locus.")
            return
        
        locus_data = get_locus_data(location)
        if not locus_data:
            caller.msg("Error: This location is marked as a Locus but has no data.")
            return
        
        level = locus_data['level']
        resonance = locus_data['resonance']
        current = locus_data['essence_current']
        maximum = locus_data['essence_max']
        last_refresh = locus_data.get('last_refresh', 'Unknown')
        
        caller.msg(f"|w{location.name} - Locus|n")
        caller.msg(f"Level: {level}")
        caller.msg(f"Resonance: {resonance}")
        caller.msg(f"Essence: {current}/{maximum}")
        caller.msg(f"Generation: {level * 3} essence per day")
        
        if isinstance(last_refresh, datetime):
            time_since = timezone.now() - last_refresh
            hours = int(time_since.total_seconds() / 3600)
            caller.msg(f"Last refresh: {hours} hours ago")
        
        caller.msg("\nGauntlet Strength: 1 (+2 dice to cross)")
        
        if not is_in_shadow(caller):
            caller.msg("\n|yYou must be in the Shadow to draw from this Locus.|n")
    
    def create_locus(self):
        """Create a Locus at the current location."""
        caller = self.caller
        location = caller.location
        
        # Check permissions
        if not caller.check_permstring("builders"):
            caller.msg("You need builder permissions to create Loci.")
            return
        
        if is_locus(location):
            caller.msg("This location is already a Locus.")
            return
        
        if not self.args or "=" not in self.args:
            caller.msg("Usage: +locus/create <level>=<resonance>")
            caller.msg("Example: +locus/create 3=rage")
            return
        
        level_str, resonance = self.args.split("=", 1)
        level_str = level_str.strip()
        resonance = resonance.strip()
        
        try:
            level = int(level_str)
        except ValueError:
            caller.msg("Level must be a number between 1 and 5.")
            return
        
        if level < 1 or level > 5:
            caller.msg("Level must be between 1 and 5.")
            return
        
        if not resonance:
            caller.msg("You must specify a resonance type.")
            return
        
        # Create the Locus
        success = create_locus(location, level, resonance)
        
        if success:
            caller.msg(f"|gLocus created successfully!|n")
            caller.msg(f"Level: {level}")
            caller.msg(f"Resonance: {resonance}")
            caller.msg(f"Maximum Essence: {level * 3}")
            caller.msg(f"Generation: {level * 3} essence per day")
            caller.msg("\nGauntlet strength automatically set to 1.")
        else:
            caller.msg("Failed to create Locus.")
    
    def draw_from_locus(self):
        """Draw essence/mana from the Locus."""
        caller = self.caller
        location = caller.location
        
        if not is_locus(location):
            caller.msg("This location is not a Locus.")
            return
        
        if not self.args:
            caller.msg("Usage: +locus/draw <amount>")
            return
        
        try:
            amount = int(self.args.strip())
        except ValueError:
            caller.msg("Amount must be a number.")
            return
        
        if amount < 1:
            caller.msg("Amount must be at least 1.")
            return
        
        # Attempt to draw
        success, message = draw_from_locus(location, caller, amount)
        caller.msg(message)
        
        if success:
            # Show updated status
            locus_data = get_locus_data(location)
            template = get_template(caller)
            pool_name = "essence" if template == "Werewolf" else "mana"
            current_pool = caller.db.stats.get(pool_name + "_current", 0)
            max_pool = caller.db.stats.get("advantages", {}).get(pool_name, 10)
            
            caller.msg(f"Locus Essence: {locus_data['essence_current']}/{locus_data['essence_max']}")
            caller.msg(f"Your {pool_name.title()}: {current_pool}/{max_pool}")
    
    def refresh_locus(self):
        """Force a refresh of Locus essence."""
        caller = self.caller
        location = caller.location
        
        # Check permissions
        if not caller.check_permstring("builders"):
            caller.msg("You need builder permissions to force refresh.")
            return
        
        if not is_locus(location):
            caller.msg("This location is not a Locus.")
            return
        
        amount = refresh_locus_essence(location)
        
        if amount > 0:
            caller.msg(f"|gLocus refreshed! Added {amount} essence.|n")
            locus_data = get_locus_data(location)
            caller.msg(f"Current Essence: {locus_data['essence_current']}/{locus_data['essence_max']}")
        else:
            caller.msg("Locus was not due for refresh (less than 24 hours since last refresh).")
    
    def list_all_loci(self):
        """List all Loci in the game."""
        caller = self.caller
        
        # Check permissions
        if not caller.check_permstring("builders"):
            caller.msg("You need builder permissions to list all Loci.")
            return
        
        # Find all Loci
        from evennia.utils.search import search_tag
        loci = search_tag("locus", category="supernatural")
        
        if not loci:
            caller.msg("No Loci found in the game.")
            return
        
        table = EvTable("Location", "Level", "Resonance", "Essence", "DB#", border="cells")
        
        for loc in loci:
            if not hasattr(loc, 'db'):
                continue
            
            locus_data = get_locus_data(loc)
            if not locus_data:
                continue
            
            level = locus_data['level']
            resonance = locus_data['resonance']
            current = locus_data['essence_current']
            maximum = locus_data['essence_max']
            
            table.add_row(
                loc.name,
                level,
                resonance,
                f"{current}/{maximum}",
                f"#{loc.id}"
            )
        
        caller.msg(f"|wLoci in the Game:|n\n{table}")


class CmdHedge(MuxCommand):
    """
    Enter or leave the Hedge.
    
    Usage:
      +hedge - Enter the Hedge through any exit (costs 1 Glamour)
      +hedge <direction> - Enter the Hedge via specific direction
      +hedge/gate - View information about Hedge Gates
      +hedge/open <exit> - Open a Hedge Gate (costs time)
      
    The Hedge is the realm between the mortal world and Arcadia. Only Changelings
    can open portals to the Hedge, spending 1 Glamour to do so. The Hedge is not
    overlaid on the mortal world like the Shadow - it's a separate realm entirely.
    
    Hedge Gates are special exits visible only to Changelings and Fae-Touched.
    Once opened, they close for 3 IC months unless reset by staff.
    
    Examples:
      +hedge
      +hedge north
      +hedge/gate
      +hedge/open gate
    """
    
    key = "+hedge"
    aliases = ["hedge"]
    locks = "cmd:all()"
    help_category = "Supernatural"
    
    def func(self):
        caller = self.caller
        
        if get_template(caller) != "Changeling":
            caller.msg("Only Changelings can enter the Hedge.")
            return
        
        # Handle switches
        if self.switches:
            switch = self.switches[0].lower()
            if switch == "gate":
                self.show_hedge_gates()
                return
            elif switch == "open":
                self.open_hedge_gate()
                return
        
        # Check if already in Hedge
        if is_in_hedge(caller):
            caller.msg("You are already in the Hedge.")
            caller.msg("Use normal exits to navigate or return to the mortal world.")
            return
        
        # Check Glamour
        glamour_current = caller.db.stats.get("glamour_current", 0)
        if glamour_current < 1:
            caller.msg("You need at least 1 Glamour to enter the Hedge.")
            return
        
        # Spend Glamour
        caller.db.stats["glamour_current"] = glamour_current - 1
        
        # Find the Hedge entrance (should be set by staff)
        # For now, we'll look for a room tagged as hedge
        from evennia.utils.search import search_tag
        hedge_rooms = search_tag("hedge", category="reality")
        
        if not hedge_rooms:
            caller.msg("There is no Hedge entrance configured. Contact staff.")
            return
        
        # Use the first hedge room (staff should set up a proper entrance grid)
        hedge_entrance = hedge_rooms[0]
        
        caller.msg("|gYou tear open a portal to the Hedge...|n")
        
        # Move to Hedge
        caller.move_to(hedge_entrance, quiet=False, move_type="hedge_portal")
        
        glamour_max = caller.db.stats.get("advantages", {}).get("glamour", 10)
        caller.msg(f"\nGlamour: {glamour_current - 1}/{glamour_max}")
    
    def show_hedge_gates(self):
        """Show information about Hedge Gates in the current room."""
        caller = self.caller
        location = caller.location
        
        if not location:
            caller.msg("You must be in a location to view Hedge Gates.")
            return
        
        # Find hedge gates in this room
        hedge_gates = [exit_obj for exit_obj in location.exits if is_hedge_gate(exit_obj)]
        
        if not hedge_gates:
            caller.msg("There are no Hedge Gates in this location.")
            return
        
        caller.msg("|wHedge Gates:|n")
        for gate in hedge_gates:
            dest_name = gate.destination.name if gate.destination else "Unknown"
            
            if is_hedge_gate_closed(gate):
                closed_until = gate.db.gate_closed_until
                time_left = closed_until - timezone.now()
                days_left = time_left.days
                caller.msg(f"  {gate.name} -> {dest_name} |r(Closed for {days_left} more days)|n")
            else:
                caller.msg(f"  {gate.name} -> {dest_name} |g(Open)|n")
    
    def open_hedge_gate(self):
        """Open a Hedge Gate."""
        caller = self.caller
        location = caller.location
        
        if not self.args:
            caller.msg("Usage: +hedge/open <exit>")
            return
        
        exit_name = self.args.strip()
        
        # Find the exit
        exit_obj = caller.search(exit_name, location=location, typeclass="typeclasses.exits.Exit")
        if not exit_obj:
            return
        
        # Check if it's a hedge gate
        if not is_hedge_gate(exit_obj):
            caller.msg("That is not a Hedge Gate.")
            return
        
        # Attempt to open
        success, message = open_hedge_gate(exit_obj)
        caller.msg(message)
        
        if success:
            # Allow passage
            dest = exit_obj.destination
            if dest:
                caller.msg(f"The gate opens. You may now travel to {dest.name}.")
                caller.msg("The gate will close for 3 IC months after you pass through.")
