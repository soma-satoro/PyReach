"""
Shapeshifting system for Werewolf: The Forsaken and Changing Breeds characters.

This module implements shapeshifting for:
- Werewolf: The Forsaken (CofD 2e) - five forms of the Uratha
- Changing Breeds (Legacy Mode) - various animal-shifter types

It handles attribute modifications, derived stat recalculation, and restrictions
on stat modifications while shifted.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from world.utils.formatting import footer
from world.cofd.kith_utils import has_kith
from world.cofd.chrysalis_animals import CHRYSALIS_FORMS, normalize_chrysalis_form_name
from utils.search_helpers import search_character


# Import Changing Breeds data for legacy mode support
try:
    from world.cofd.powers.changing_breeds_data import (
        get_breed_forms, 
        get_breed_info, 
        list_all_breeds,
        get_form_list
    )
    CHANGING_BREEDS_AVAILABLE = True
except ImportError:
    CHANGING_BREEDS_AVAILABLE = False


# Form definitions with their stat modifiers
WEREWOLF_FORMS = {
    "hishu": {
        "display_name": "Hishu",
        "description": "Human form: the natural camouflage among humanity",
        "strength": 0,
        "dexterity": 0,
        "stamina": 0,
        "manipulation": 0,
        "size": 0,
        "perception_bonus": 1,
        "special_abilities": [
            "Sheep's Clothing: Pursuers suffer Primal Urge penalty when tracking in crowds"
        ]
    },
    "dalu": {
        "display_name": "Dalu",
        "description": "Near-Human form: a hulking, powerful human hunter",
        "strength": 1,
        "dexterity": 0,
        "stamina": 1,
        "manipulation": -1,
        "size": 1,
        "perception_bonus": 2,
        "special_abilities": [
            "Teeth and Claws: Unarmed attacks deal lethal damage",
            "Defense vs Firearms: Apply Defense against Firearms",
            "Lunacy: +2 to Lunacy roll",
            "Badass Motherfucker: Intimidate crowds with Presence + Primal Urge"
        ]
    },
    "gauru": {
        "display_name": "Gauru",
        "description": "War form: the devastating nightmare of legend",
        "strength": 3,
        "dexterity": 1,
        "stamina": 2,
        "manipulation": 0,  # Gauru auto-fails non-Intimidation Social rolls
        "size": 2,
        "perception_bonus": 3,
        "special_abilities": [
            "Regeneration: Heal all bashing and lethal damage each turn",
            "Teeth and Claws: +2L damage, +3 Initiative",
            "Defense vs Firearms: Apply Defense against Firearms",
            "Lunacy: -2 to Lunacy roll (more terrifying)",
            "Rage: Must attack each turn or fall to Kuruth",
            "Primal Fear: Lesser enemies use Down and Dirty combat",
            "WARNING: Limited duration = Stamina + Primal Urge turns"
        ]
    },
    "urshul": {
        "display_name": "Urshul",
        "description": "Near-Wolf form: a horse-sized dire wolf",
        "strength": 2,
        "dexterity": 2,
        "stamina": 2,
        "manipulation": -1,
        "size": 1,
        "perception_bonus": 3,
        "speed_bonus": 3,  # Species speed factor
        "special_abilities": [
            "Teeth and Claws: Claws +1L, Bite +2L",
            "Defense vs Firearms: Apply Defense against Firearms",
            "Lunacy: Inflicts Lunacy",
            "Weaken the Prey: Apply Tilt (Arm Wrack/Leg Wrack/Knocked Down) once per scene"
        ]
    },
    "urhan": {
        "display_name": "Urhan",
        "description": "Wolf form: a natural wolf for stealth and tracking",
        "strength": 0,
        "dexterity": 2,
        "stamina": 1,
        "manipulation": -1,
        "size": -1,
        "perception_bonus": 4,
        "speed_bonus": 3,  # Species speed factor
        "special_abilities": [
            "Teeth: Bite attacks +1L damage",
            "Chase Down: Spend 1 Essence to pre-empt actions",
            "Enhanced Tracking: +4 dice to Perception (wolf senses)"
        ]
    }
}


class CmdShift(MuxCommand):
    """
    Shift between available shapeshifter forms.
    
    Usage:
        +shift <form>
        +shift/list
        +shift/info <form>
        +shift/chrysalis <animal>
        +shift/chrysalis
        +shift/remove <name>=<animal>   (staff)
        
    Switches:
        /list - Show all available forms and your current form
        /info - Show detailed information about a specific form
        /chrysalis - Select/view Chrysalis animal forms
        /remove - Staff removes a selected Chrysalis form
        
    Forms:
        Hishu   - Human form (default)
        Dalu    - Near-Man form
        Gauru   - War form (limited duration!)
        Urshul  - Near-Wolf form  
        Urhan   - Wolf form
        Human/Swarm - Swarmflight changeling forms
        
    Examples:
        +shift gauru        - Transform into the mighty Gauru war form
        +shift hishu        - Return to human form
        +shift swarm        - Swarmflight changeling enters swarm form
        +shift human        - Swarmflight changeling returns to human form
        +shift/list         - See all forms and current form
        +shift/info urshul  - Learn about the Urshul form
        
    Notes:
        - Werewolves, legacy Changing Breeds, Swarmflight Changelings, and Chrysalis users can shapeshift
        - Swarmflight must set permanent swarm size with +stat swarm_size=0 or +stat swarm_size=1
        - Chrysalis requires known contract 'Chrysalis' (Royal, Steed)
        - Chrysalis base picks: 2 animals (Size 1-7)
        - Beast seeming or bought Beast benefit for Chrysalis: +2 animal picks
        - Ogre seeming or bought Ogre benefit for Chrysalis: size cap increases to 15
        - Chrysalis picks are permanent unless staff removes one
        - Example Chrysalis flow: +shift/chrysalis shark, then +shift shark
        - Hishu is the default form for all werewolves
        - Your stats are temporarily modified while in other forms
        - You cannot spend XP or use +stat while not in Hishu form
        - Derived stats (Health, Speed, Defense, Initiative) automatically update
        - Gauru form has a limited duration and risks Kuruth (Death Rage)
    """
    
    key = "+shift"
    aliases = ["shift"]
    help_category = "Roleplaying Tools"
    
    def func(self):
        """Execute the shift command"""
        caller = self.caller

        if "remove" in self.switches:
            self._remove_chrysalis_form(caller)
            return

        if "chrysalis" in self.switches:
            self._handle_chrysalis_selection(caller)
            return
        
        # Check if character can shapeshift
        if not self._is_shapeshifter(caller):
            caller.msg(
                "|rYou must be a Werewolf, legacy Changing Breed, Swarmflight Changeling, "
                "or a Chrysalis user with selected forms to use shapeshifting.|n"
            )
            return
        
        # Get available forms for this character
        forms_dict = self._get_forms_for_character(caller)
        if not forms_dict:
            caller.msg("|rNo forms available for your character type.|n")
            return
        
        # Handle switches
        if "list" in self.switches:
            self._show_forms_list(caller, forms_dict)
            return
        
        if "info" in self.switches:
            self._show_form_info(caller, forms_dict)
            return
        
        # No arguments - show current form
        if not self.args:
            self._show_current_form(caller, forms_dict)
            return
        
        # Shift to the specified form
        target_form = self._normalize_key(self.args.strip())
        if target_form not in forms_dict:
            for form_key, form_data in forms_dict.items():
                if self._normalize_key(form_data.get("display_name", "")) == target_form:
                    target_form = form_key
                    break
        
        if target_form not in forms_dict:
            caller.msg(f"|rUnknown form '{self.args}'. Valid forms: {', '.join(forms_dict.keys())}|n")
            caller.msg("Use |w+shift/list|n to see all available forms.")
            return
        
        # Perform the shift
        self._perform_shift(caller, target_form, forms_dict)

    def _normalize_key(self, value):
        return str(value).strip().lower().replace(" ", "_").replace("-", "_")

    def _resolve_chrysalis_form_key(self, value):
        """Resolve user input to a Chrysalis form key."""
        key = normalize_chrysalis_form_name(value)
        if key in CHRYSALIS_FORMS:
            return key
        for form_key, data in CHRYSALIS_FORMS.items():
            display_norm = normalize_chrysalis_form_name(data.get("display_name", ""))
            if key == display_norm or key in display_norm or display_norm in key:
                return form_key
        return key

    def _has_chrysalis_contract(self, character):
        powers = (character.db.stats or {}).get("powers", {}) or {}
        return powers.get("contract:chrysalis") == "known"

    def _has_contract_benefit(self, character, contract_key, seeming_key):
        powers = (character.db.stats or {}).get("powers", {}) or {}
        benefit_key = f"contract_benefit:{contract_key}:{seeming_key}"
        return powers.get(benefit_key) == "known"

    def _get_chrysalis_limits(self, character):
        """Return (max_forms, size_cap) for this character's Chrysalis setup."""
        stats = character.db.stats or {}
        bio = stats.get("bio", {}) or {}
        seeming = self._normalize_key(bio.get("seeming", ""))

        max_forms = 2
        if seeming == "beast" or self._has_contract_benefit(character, "chrysalis", "beast"):
            max_forms += 2

        size_cap = 7
        if seeming == "ogre" or self._has_contract_benefit(character, "chrysalis", "ogre"):
            size_cap = 15

        return max_forms, size_cap

    def _get_selected_chrysalis_forms(self, character):
        selected_raw = getattr(character.db, "chrysalis_forms", None)
        if selected_raw is None:
            selected = []
        elif isinstance(selected_raw, (list, tuple, set)):
            selected = list(selected_raw)
        else:
            try:
                selected = list(selected_raw)
            except TypeError:
                selected = []
        normalized = []
        for entry in selected:
            key = normalize_chrysalis_form_name(entry)
            if key and key in CHRYSALIS_FORMS and key not in normalized:
                normalized.append(key)
        if normalized != selected:
            character.db.chrysalis_forms = normalized
        return normalized

    def _build_chrysalis_forms_dict(self, character):
        """
        Build +shift forms from selected Chrysalis animals.
        Includes a human base form for proper reversion.
        """
        if not self._has_chrysalis_contract(character):
            return {}

        selected = self._get_selected_chrysalis_forms(character)
        if not selected:
            return {}

        forms = {
            "human": {
                "display_name": "Human",
                "description": "Your standard changeling form.",
                "strength": 0,
                "dexterity": 0,
                "stamina": 0,
                "manipulation": 0,
                "size": 0,
                "special_abilities": [],
            }
        }

        for key in selected:
            animal = CHRYSALIS_FORMS.get(key)
            if not animal:
                continue
            description = (
                f"Chrysalis form: {animal.get('movement', 'land')} movement; "
                f"{animal.get('senses', 'mundane senses')}."
            )
            if animal.get("mythical"):
                description += " Mythical body only (no supernatural powers)."
            if animal.get("aquatic"):
                description += " Aquatic respiration applies while shifted."

            forms[key] = {
                "display_name": animal["display_name"],
                "description": description,
                "strength_absolute": animal["strength"],
                "dexterity_absolute": animal["dexterity"],
                "stamina_absolute": animal["stamina"],
                "size_absolute": animal["size"],
                "speed_absolute": animal["speed"],
                "health_absolute": animal["health"],
                "movement": animal.get("movement", "land"),
                "senses": animal.get("senses", "mundane senses"),
                "special_abilities": [
                    "Physical attributes replaced by animal profile.",
                    "Uses animal mundane senses and movement modes.",
                    "No supernatural powers granted by form."
                ],
            }

        return forms

    def _handle_chrysalis_selection(self, caller):
        """Handle +shift/chrysalis selection and status display."""
        if not self._has_chrysalis_contract(caller):
            caller.msg("|rYou must know the Chrysalis contract to set animal forms.|n")
            return

        max_forms, size_cap = self._get_chrysalis_limits(caller)
        selected = self._get_selected_chrysalis_forms(caller)

        if not self.args:
            caller.msg(footer(78, char="="))
            caller.msg("|cCHRYSALIS FORMS|n")
            caller.msg(footer(78, char="="))
            caller.msg(f"Slots: {len(selected)}/{max_forms}  |  Size Cap: {size_cap}")
            if selected:
                names = ", ".join(CHRYSALIS_FORMS[k]["display_name"] for k in selected)
                caller.msg(f"Selected: {names}")
            else:
                caller.msg("Selected: None")
            available = []
            for key, data in CHRYSALIS_FORMS.items():
                if data.get("size", 0) <= size_cap:
                    name = data["display_name"]
                    if key in selected:
                        name = f"{name}*"
                    available.append(name)
            if available:
                caller.msg("")
                caller.msg("|wAvailable forms ( * = selected ):|n")
                caller.msg(", ".join(sorted(available)))
            caller.msg("Use |w+shift/chrysalis <animal>|n to select a form.")
            caller.msg("Selected forms are permanent unless staff removes one with +shift/remove.")
            caller.msg(footer(78, char="="))
            return

        if len(selected) >= max_forms:
            caller.msg("|rYou have already filled all available Chrysalis form slots.|n")
            return

        requested_key = self._resolve_chrysalis_form_key(self.args)
        animal = CHRYSALIS_FORMS.get(requested_key)
        if not animal:
            caller.msg(f"|rUnknown Chrysalis animal '{self.args}'.|n")
            return
        if animal["size"] > size_cap:
            caller.msg(f"|r{animal['display_name']} is Size {animal['size']} and exceeds your Chrysalis cap of {size_cap}.|n")
            return
        if requested_key in selected:
            caller.msg(f"|y{animal['display_name']} is already selected.|n")
            return

        selected.append(requested_key)
        caller.db.chrysalis_forms = selected
        caller.msg(f"|gAdded Chrysalis form: {animal['display_name']}.|n")
        caller.msg(f"Slots used: {len(selected)}/{max_forms}")

    def _remove_chrysalis_form(self, caller):
        """Staff-only: remove a selected Chrysalis form from a character."""
        if not caller.check_permstring("Admin"):
            caller.msg("|rOnly staff can use +shift/remove.|n")
            return
        if not self.args or "=" not in self.args:
            caller.msg("Usage: +shift/remove <name>=<animal form>")
            return

        target_name, animal_name = [part.strip() for part in self.args.split("=", 1)]
        target = search_character(caller, target_name)
        if not target:
            return

        selected = self._get_selected_chrysalis_forms(target)

        animal_key = self._resolve_chrysalis_form_key(animal_name)
        if animal_key not in selected:
            caller.msg(f"|r{target.name} does not have '{animal_name}' selected.|n")
            return

        selected.remove(animal_key)
        target.db.chrysalis_forms = selected
        caller.msg(f"|gRemoved Chrysalis form '{animal_name}' from {target.name}.|n")
        target.msg(f"|yStaff removed your Chrysalis form: {animal_name}. You may select a replacement with +shift/chrysalis.|n")
    
    def _is_werewolf(self, character):
        """Check if character is a werewolf"""
        if not character.db.stats:
            return False
        
        template = character.db.stats.get("other", {}).get("template", "").lower()
        return template == "werewolf"
    
    def _is_shapeshifter(self, character):
        """Check if character can shapeshift (werewolf or changing breed)"""
        if not character.db.stats:
            return False
        
        template = character.db.stats.get("other", {}).get("template", "").lower()
        
        # Standard werewolf
        if template == "werewolf":
            return True

        # Changeling Swarmflight kith.
        if template == "changeling" and has_kith(character, "swarmflight"):
            return True

        # Changeling Chrysalis contract with at least one selected form.
        if template == "changeling":
            powers = (character.db.stats or {}).get("powers", {}) or {}
            selected = self._get_selected_chrysalis_forms(character)
            if powers.get("contract:chrysalis") == "known" and len(selected) > 0:
                return True
        
        # Check if they're a changing breed (legacy mode)
        if self._is_legacy_mode() and CHANGING_BREEDS_AVAILABLE:
            breed = character.db.stats.get("other", {}).get("breed", "").lower()
            if breed:
                breed_info = get_breed_info(breed)
                return breed_info is not None
        
        return False
    
    def _is_legacy_mode(self):
        """Check if legacy mode is active"""
        try:
            from commands.CmdLegacy import is_legacy_mode
            return is_legacy_mode()
        except:
            return False
    
    def _get_forms_for_character(self, character):
        """
        Get the forms dictionary for this character's type.
        Returns WEREWOLF_FORMS for werewolves, or breed-specific forms for Changing Breeds.
        """
        template = character.db.stats.get("other", {}).get("template", "").lower()
        
        # Standard Werewolf: The Forsaken
        if template == "werewolf":
            return WEREWOLF_FORMS

        if template == "changeling":
            forms = {}

            # Changeling Swarmflight kith.
            if has_kith(character, "swarmflight"):
                swarm_size = (character.db.stats.get("other", {}) or {}).get("swarm_size", 1)
                try:
                    swarm_size = int(swarm_size)
                except (TypeError, ValueError):
                    swarm_size = 1
                if swarm_size not in (0, 1):
                    swarm_size = 1
                forms["human"] = {
                    "display_name": "Human",
                    "description": "Your standard changeling form.",
                    "strength": 0,
                    "dexterity": 0,
                    "stamina": 0,
                    "manipulation": 0,
                    "size": 0,
                    "special_abilities": [],
                }
                forms["swarm"] = {
                    "display_name": "Swarm",
                    "description": "Your Swarmflight kith swarm form.",
                    "strength": 0,
                    "dexterity": 0,
                    "stamina": 0,
                    "manipulation": 0,
                    "size_absolute": swarm_size,
                    # Speed should use size while in swarm form.
                    "speed_override": "size_based",
                    "special_abilities": [
                        "Swarm form uses your chosen permanent size (0 or 1)."
                    ],
                }

            chrysalis_forms = self._build_chrysalis_forms_dict(character)
            for key, value in chrysalis_forms.items():
                forms[key] = value

            if forms:
                return forms
        
        # Changing Breeds (legacy mode)
        if self._is_legacy_mode() and CHANGING_BREEDS_AVAILABLE:
            breed = character.db.stats.get("other", {}).get("breed", "").lower()
            if breed:
                breed_forms = get_breed_forms(breed)
                if breed_forms:
                    return breed_forms
        
        return None
    
    def _get_current_form(self, character):
        """Get the character's current form (defaults to Hishu or Human)"""
        if not hasattr(character.db, 'current_form') or character.db.current_form is None:
            # Default to hishu for werewolves, human for changing breeds
            forms_dict = self._get_forms_for_character(character)
            if forms_dict:
                if "hishu" in forms_dict:
                    character.db.current_form = "hishu"
                elif "human" in forms_dict:
                    character.db.current_form = "human"
                else:
                    # Default to first form in the list
                    character.db.current_form = list(forms_dict.keys())[0]
            else:
                character.db.current_form = "hishu"
        return character.db.current_form
    
    def _show_current_form(self, caller, forms_dict):
        """Show the character's current form"""
        current_form = self._get_current_form(caller)
        form_data = forms_dict[current_form]
        
        caller.msg(f"\n|wYou are currently in |c{form_data['display_name']}|w form.|n")
        caller.msg(f"|w{form_data['description']}|n\n")
    
    def _show_forms_list(self, caller, forms_dict):
        """Show a list of all available forms"""
        current_form = self._get_current_form(caller)
        
        # Get breed info if changing breed
        template = caller.db.stats.get("other", {}).get("template", "").lower()
        breed = caller.db.stats.get("other", {}).get("breed", "").lower()
        
        if template == "werewolf":
            title = "WEREWOLF FORMS"
        elif breed:
            breed_display = breed.replace("_", " ").title()
            title = f"{breed_display.upper()} FORMS"
        else:
            title = "AVAILABLE FORMS"
        
        lines = [
            footer(78, char="="),
            f"|c{title}|n",
            footer(78, char="="),
            ""
        ]
        
        for form_key, form_data in forms_dict.items():
            current_marker = " |g(CURRENT)|n" if form_key == current_form else ""
            lines.append(f"|w{form_data['display_name']:12}|n - {form_data['description']}{current_marker}")
        
        lines.extend([
            "",
            "|wUse |c+shift <form>|w to change forms.|n",
            "|wUse |c+shift/info <form>|w for detailed information.|n",
            footer(78, char="=")
        ])
        
        caller.msg("\n".join(lines))
    
    def _show_form_info(self, caller, forms_dict):
        """Show detailed information about a specific form"""
        if not self.args:
            caller.msg("|rYou must specify a form. Usage: +shift/info <form>|n")
            return
        
        form_name = self.args.strip().lower()
        
        if form_name not in forms_dict:
            caller.msg(f"|rUnknown form '{self.args}'. Valid forms: {', '.join(forms_dict.keys())}|n")
            return
        
        form_data = forms_dict[form_name]
        current_form = self._get_current_form(caller)
        
        lines = [
            footer(78, char="="),
            f"|c{form_data['display_name'].upper()} FORM|n",
            footer(78, char="="),
            "",
            f"|w{form_data['description']}|n",
            ""
        ]
        
        # Show stat modifiers
        lines.append("|wAttribute Modifiers:|n")
        showed_any = False
        for attr in ["strength", "dexterity", "stamina", "manipulation"]:
            absolute_key = f"{attr}_absolute"
            if absolute_key in form_data:
                lines.append(f"  {attr.title():15} set to {form_data[absolute_key]}")
                showed_any = True
                continue
            modifier = form_data.get(attr, 0)
            if modifier != 0:
                sign = "+" if modifier > 0 else ""
                lines.append(f"  {attr.title():15} {sign}{modifier}")
                showed_any = True
        
        if "size_absolute" in form_data:
            lines.append(f"  Size:           set to {form_data['size_absolute']}")
            showed_any = True
        else:
            size_mod = form_data.get("size", 0)
            if size_mod != 0:
                sign = "+" if size_mod > 0 else ""
                lines.append(f"  Size:           {sign}{size_mod}")
                showed_any = True

        if "speed_absolute" in form_data:
            lines.append(f"  Speed:          set to {form_data['speed_absolute']}")
            showed_any = True
        if "health_absolute" in form_data:
            lines.append(f"  Health:         set to {form_data['health_absolute']}")
            showed_any = True
        if not showed_any:
            lines.append("  No attribute changes.")
        
        lines.append("")
        
        # Show perception bonus
        perc_bonus = form_data.get("perception_bonus", 0)
        if perc_bonus > 0:
            lines.append(f"|wPerception:|n +{perc_bonus} dice to Perception rolls using wolf senses")
            lines.append("")
        
        # Show special abilities
        if form_data.get("special_abilities"):
            lines.append("|wSpecial Abilities:|n")
            for ability in form_data["special_abilities"]:
                lines.append(f"  * {ability}")
            lines.append("")

        if form_data.get("movement"):
            lines.append(f"|wMovement Modes:|n {form_data['movement']}")
        if form_data.get("senses"):
            lines.append(f"|wMundane Senses:|n {form_data['senses']}")
        if form_data.get("aquatic"):
            lines.append("|wAquatic Adaptation:|n You gain aquatic respiration while in this form.")
        if form_data.get("movement") or form_data.get("senses") or form_data.get("aquatic"):
            lines.append("")
        
        # Show if this is the current form
        if form_name == current_form:
            lines.append("|g>>> You are currently in this form <<<|n")
            lines.append("")
        
        lines.append(footer(78, char="="))
        
        caller.msg("\n".join(lines))
    
    def _perform_shift(self, caller, target_form, forms_dict):
        """Perform the actual shapeshifting"""
        current_form = self._get_current_form(caller)
        
        # Check if already in target form
        if current_form == target_form:
            form_data = forms_dict[target_form]
            caller.msg(f"|yYou are already in {form_data['display_name']} form.|n")
            return
        
        # Determine the base form (hishu for werewolves, human for changing breeds)
        base_form = "hishu" if "hishu" in forms_dict else "human"
        
        # Store base attributes if shifting from base form for the first time
        # Check both that attribute doesn't exist AND that it's not None
        if current_form == base_form and (not hasattr(caller.db, 'base_attributes') or caller.db.base_attributes is None):
            self._store_base_stats(caller)
        
        # If returning to base form, restore base stats
        if target_form == base_form:
            self._restore_base_stats(caller)
        else:
            # Apply the new form's modifiers
            self._apply_form_modifiers(caller, target_form, current_form, forms_dict)
        
        # Update current form
        caller.db.current_form = target_form
        
        # Recalculate derived stats
        caller.calculate_derived_stats()
        self._apply_form_derived_overrides(caller, target_form, forms_dict)
        
        # Show transformation message
        form_data = forms_dict[target_form]
        caller.msg(f"\n|gYou shift into |c{form_data['display_name']}|g form!|n")
        caller.msg(f"|w{form_data['description']}|n")
        
        # Show stat changes
        self._show_stat_changes(caller, target_form, forms_dict)
        
        # Announce to room
        if caller.location:
            caller.location.msg_contents(
                f"|y{caller.name} undergoes a dramatic transformation, shifting into {form_data['display_name']} form!|n",
                exclude=[caller]
            )
        
        # Show warning for Gauru form (werewolves only)
        if target_form == "gauru":
            stamina = caller.db.stats.get("attributes", {}).get("stamina", 1)
            primal_urge = caller.db.stats.get("advantages", {}).get("primal_urge", 1)
            duration = stamina + primal_urge
            
            caller.msg(f"\n|rWARNING: Gauru form is limited to {duration} turns (Stamina + Primal Urge).|n")
            caller.msg("|rYou must attack each turn or risk falling into Kuruth (Death Rage)!|n")
    
    def _store_base_stats(self, caller):
        """Store the character's base statistics before shifting"""
        if not caller.db.stats:
            return
        
        attrs = caller.db.stats.get("attributes", {})
        other = caller.db.stats.get("other", {})
        
        # Store base attributes
        caller.db.base_attributes = {
            "strength": attrs.get("strength", 1),
            "dexterity": attrs.get("dexterity", 1),
            "stamina": attrs.get("stamina", 1),
            "manipulation": attrs.get("manipulation", 1)
        }
        
        # Store base size
        caller.db.base_size = other.get("size", 5)

        # Store base speed so special forms can cleanly revert.
        caller.db.base_speed = caller.db.stats.get("advantages", {}).get("speed")
        caller.db.base_advantages = {
            "health": caller.db.stats.get("advantages", {}).get("health"),
            "speed": caller.db.stats.get("advantages", {}).get("speed"),
            "defense": caller.db.stats.get("advantages", {}).get("defense"),
            "initiative": caller.db.stats.get("advantages", {}).get("initiative"),
        }
    
    def _restore_base_stats(self, caller):
        """Restore the character's base statistics when returning to Hishu"""
        if not hasattr(caller.db, 'base_attributes') or not caller.db.base_attributes:
            # No base stats stored, nothing to restore
            return
        
        # Restore attributes
        if "attributes" not in caller.db.stats:
            caller.db.stats["attributes"] = {}
        
        for attr, value in caller.db.base_attributes.items():
            caller.db.stats["attributes"][attr] = value
        
        # Restore size
        if "other" not in caller.db.stats:
            caller.db.stats["other"] = {}
        
        caller.db.stats["other"]["size"] = caller.db.base_size

        # Restore speed if we previously overrode it in a shifted form.
        if "advantages" not in caller.db.stats:
            caller.db.stats["advantages"] = {}
        if hasattr(caller.db, "base_speed") and caller.db.base_speed is not None:
            caller.db.stats["advantages"]["speed"] = caller.db.base_speed
        
        # Mark stats as modified so Evennia persists the changes
        caller.db.stats = caller.db.stats
    
    def _apply_form_modifiers(self, caller, target_form, current_form, forms_dict):
        """Apply stat modifiers for the new form (handles both modifiers and absolute values)"""
        # Determine base form
        base_form = "hishu" if "hishu" in forms_dict else "human"
        
        # If currently not in base form, we need to remove current modifiers first
        if current_form != base_form:
            # Restore to base, then apply new modifiers
            self._restore_base_stats(caller)
        
        # Ensure base_attributes exists (safety check for characters created before this system)
        if not hasattr(caller.db, 'base_attributes') or caller.db.base_attributes is None:
            self._store_base_stats(caller)
        
        # Get target form data
        form_data = forms_dict[target_form]
        
        # Apply attribute modifiers
        if "attributes" not in caller.db.stats:
            caller.db.stats["attributes"] = {}
        
        attrs = caller.db.stats["attributes"]
        base = caller.db.base_attributes
        
        # Apply modifiers or absolute values for each attribute
        for attr in ["strength", "dexterity", "stamina", "manipulation"]:
            # Check for absolute value first (Changing Breeds feature)
            absolute_key = f"{attr}_absolute"
            if absolute_key in form_data:
                # SET to absolute value
                attrs[attr] = form_data[absolute_key]
            elif attr in form_data:
                # ADD modifier to base value
                modifier = form_data[attr]
                base_value = base.get(attr, 1)
                new_value = base_value + modifier
                
                # Ensure attributes don't go below 1
                if new_value < 1:
                    new_value = 1
                
                attrs[attr] = new_value
        
        # Apply size modifier or absolute value
        if "other" not in caller.db.stats:
            caller.db.stats["other"] = {}
        
        if "size_absolute" in form_data:
            # SET to absolute value
            caller.db.stats["other"]["size"] = form_data["size_absolute"]
        elif "size" in form_data:
            # ADD modifier to base
            size_modifier = form_data["size"]
            caller.db.stats["other"]["size"] = caller.db.base_size + size_modifier
        
        # Mark stats as modified so Evennia persists the changes
        caller.db.stats = caller.db.stats
    
    def _show_stat_changes(self, caller, form, forms_dict):
        """Show the stat changes from the transformation"""
        form_data = forms_dict[form]
        
        changes = []
        
        # Show attribute changes
        absolute_changes = []
        for attr in ["strength", "dexterity", "stamina", "manipulation"]:
            absolute_key = f"{attr}_absolute"
            if absolute_key in form_data:
                absolute_changes.append(f"{attr.title()}={form_data[absolute_key]}")
                continue
            modifier = form_data.get(attr, 0)
            if modifier != 0:
                sign = "+" if modifier > 0 else ""
                changes.append(f"{attr.title()} {sign}{modifier}")
        
        # Show size change
        if "size_absolute" in form_data:
            absolute_changes.append(f"Size={form_data['size_absolute']}")
        else:
            size_mod = form_data.get("size", 0)
            if size_mod != 0:
                sign = "+" if size_mod > 0 else ""
                changes.append(f"Size {sign}{size_mod}")
        
        if changes:
            caller.msg(f"\n|wAttribute changes:|n {', '.join(changes)}")
        if absolute_changes:
            caller.msg(f"|wAbsolute profile:|n {', '.join(absolute_changes)}")
        
        # Show derived stat updates
        attrs = caller.db.stats.get("attributes", {})
        advantages = caller.db.stats.get("advantages", {})
        other = caller.db.stats.get("other", {})
        
        health = caller.db.stats.get("advantages", {}).get("health", other.get("size", 5) + attrs.get("stamina", 1))
        speed = caller.db.stats.get("advantages", {}).get("speed", attrs.get("strength", 1) + attrs.get("dexterity", 1) + 5)
        
        # Add speed bonus for wolf forms
        if form in ["urshul", "urhan"]:
            speed += form_data.get("speed_bonus", 0)
        
        defense = min(attrs.get("wits", 1), attrs.get("dexterity", 1))
        initiative = attrs.get("dexterity", 1) + attrs.get("composure", 1)
        
        caller.msg(f"|wDerived stats:|n Health: {health}, Speed: {speed}, Defense: {defense}, Initiative: {initiative}")

    def _apply_form_derived_overrides(self, caller, target_form, forms_dict):
        """
        Apply derived-stat overrides needed by specific forms.
        """
        form_data = forms_dict.get(target_form, {})
        if form_data.get("speed_override") == "size_based":
            attrs = caller.db.stats.get("attributes", {})
            size = caller.db.stats.get("other", {}).get("size", 5)
            speed = attrs.get("strength", 1) + attrs.get("dexterity", 1) + size
            if "advantages" not in caller.db.stats:
                caller.db.stats["advantages"] = {}
            caller.db.stats["advantages"]["speed"] = speed
            caller.db.stats = caller.db.stats
            return

        if "speed_absolute" in form_data or "health_absolute" in form_data:
            if "advantages" not in caller.db.stats:
                caller.db.stats["advantages"] = {}
            if "speed_absolute" in form_data:
                caller.db.stats["advantages"]["speed"] = int(form_data["speed_absolute"])
            if "health_absolute" in form_data:
                caller.db.stats["advantages"]["health"] = int(form_data["health_absolute"])
            caller.db.stats = caller.db.stats
    
    def _can_modify_stats_while_shifted(self, caller):
        """Check if character can modify stats (only in Hishu form)"""
        current_form = self._get_current_form(caller)
        return current_form == "hishu"


class CmdForm(MuxCommand):
    """
    Quick alias to check your current werewolf form.
    
    Usage:
        +form
        
    Shows your current werewolf form and basic information.
    Use +shift for full shapeshifting commands.
    """
    
    key = "+form"
    aliases = ["form"]
    help_category = "Chargen & Character Info"
    
    def func(self):
        """Execute the form command"""
        caller = self.caller
        
        # Check if character is a werewolf
        template = caller.db.stats.get("other", {}).get("template", "").lower() if caller.db.stats else ""
        
        if template != "werewolf":
            caller.msg("|rYou are not a Werewolf.|n")
            return
        
        # Get current form
        current_form = getattr(caller.db, 'current_form', 'hishu')
        if current_form not in WEREWOLF_FORMS:
            current_form = 'hishu'
            caller.db.current_form = current_form
        
        form_data = WEREWOLF_FORMS[current_form]
        
        # Display current form
        lines = [
            "",
            footer(78, char="="),
            f"|cCurrent Form: {form_data['display_name']}|n",
            footer(78, char="="),
            f"|w{form_data['description']}|n",
            ""
        ]
        
        # Show active modifiers if not in Hishu
        if current_form != "hishu":
            mods = []
            for attr in ["strength", "dexterity", "stamina", "manipulation"]:
                modifier = form_data.get(attr, 0)
                if modifier != 0:
                    sign = "+" if modifier > 0 else ""
                    mods.append(f"{attr.title()} {sign}{modifier}")
            
            size_mod = form_data.get("size", 0)
            if size_mod != 0:
                sign = "+" if size_mod > 0 else ""
                mods.append(f"Size {sign}{size_mod}")
            
            if mods:
                lines.append("|wActive Modifiers:|n " + ", ".join(mods))
                lines.append("")
        
        lines.extend([
            "|wUse |c+shift <form>|w to change forms.|n",
            "|wUse |c+shift/list|w to see all available forms.|n",
            footer(78, char="=")
        ])
        
        caller.msg("\n".join(lines))


# Helper function to check if character can modify stats (for use in other commands)
def can_modify_stats_while_shifted(character):
    """
    Check if a character can modify their stats based on their current form.
    Only base form (Hishu for werewolves, Human for changing breeds) allows stat modification.
    
    Args:
        character: The character to check
        
    Returns:
        tuple: (can_modify: bool, reason: str)
    """
    # Non-shapeshifters can always modify stats (other restrictions may apply)
    if not character.db.stats:
        return True, ""
    
    template = character.db.stats.get("other", {}).get("template", "").lower()
    
    # Check if they're a shapeshifter
    is_werewolf = (template == "werewolf")
    is_swarmflight = (template == "changeling" and has_kith(character, "swarmflight"))
    has_chrysalis_forms = False
    if template == "changeling":
        powers = (character.db.stats or {}).get("powers", {}) or {}
        selected_raw = getattr(character.db, "chrysalis_forms", None)
        if selected_raw is None:
            selected = []
        elif isinstance(selected_raw, (list, tuple, set)):
            selected = list(selected_raw)
        else:
            try:
                selected = list(selected_raw)
            except TypeError:
                selected = []
        normalized = []
        for entry in selected:
            key = normalize_chrysalis_form_name(entry)
            if key and key in CHRYSALIS_FORMS and key not in normalized:
                normalized.append(key)
        has_chrysalis_forms = powers.get("contract:chrysalis") == "known" and len(normalized) > 0
    
    # Check for changing breed in legacy mode
    is_changing_breed = False
    base_form_name = "hishu"
    base_form_display = "human"
    
    if CHANGING_BREEDS_AVAILABLE:
        try:
            from commands.CmdLegacy import is_legacy_mode
            if is_legacy_mode():
                breed = character.db.stats.get("other", {}).get("breed", "").lower()
                if breed:
                    breed_info = get_breed_info(breed)
                    if breed_info:
                        is_changing_breed = True
                        base_form_name = "human"
                        base_form_display = "human"
        except:
            pass
    
    # Non-shapeshifters can modify stats
    if not is_werewolf and not is_changing_breed and not is_swarmflight and not has_chrysalis_forms:
        return True, ""
    
    # Determine base form name
    if is_werewolf:
        base_form_name = "hishu"
        base_form_display = "Hishu (human)"
    elif is_swarmflight or has_chrysalis_forms:
        base_form_name = "human"
        base_form_display = "human"
    
    # Check current form
    current_form = getattr(character.db, 'current_form', base_form_name)
    
    if current_form != base_form_name:
        # Get the display name of current form
        if is_werewolf:
            form_display = WEREWOLF_FORMS.get(current_form, {}).get("display_name", current_form)
        else:
            breed = character.db.stats.get("other", {}).get("breed", "").lower()
            breed_forms = get_breed_forms(breed)
            if breed_forms:
                form_display = breed_forms.get(current_form, {}).get("display_name", current_form)
            else:
                form_display = current_form
        
        return False, f"You cannot modify stats while in {form_display} form. Use +shift {base_form_name} to return to {base_form_display} form first."
    
    return True, ""


