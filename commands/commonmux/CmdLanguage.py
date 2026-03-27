from evennia.utils import evtable
from evennia.commands.default.muxcommand import MuxCommand
from world.utils.language_data import AVAILABLE_LANGUAGES
from evennia.utils.search import search_object
from world.utils.formatting import header, footer, divider, section_header, format_stat
from world.utils.ansi_utils import wrap_ansi
from evennia.utils.ansi import ANSIString
from collections.abc import Mapping

# This dictionary should be populated with all available languages
class CmdLanguage(MuxCommand):
    """
    Set your speaking language, view known languages, or add a new language.

    Usage:
      +language
      +language <language>
      +language none
      +language/add <language>
      +language/all
      +language/set <character>=<language1>,<language2>,...  (Staff only)
      +language/rem <language>         (Remove a language from yourself)
      +language/rem <name>=<language>  (Staff only - Remove from others)
      +language/view <name>            (Staff only - View character's languages)
      +language/native <language>        (Set your native language)

    Examples:
      +language
      +language Spanish
      +language none
      +language/add French
      +language/all
      +language/set Bob=English,Spanish,French
      +language/view Bob
    """

    key = "+language"
    aliases = ["+lang", "+languages"]
    locks = "cmd:all()"
    help_category = "Roleplaying Tools"

    LANGUAGE_SOURCE = "language"
    MULTILINGUAL_SOURCE = "multilingual"

    def _extract_merit_dots(self, merit_data):
        """Extract numeric dots from merit storage."""
        if isinstance(merit_data, Mapping):
            for key in ("dots", "perm"):
                if key in merit_data:
                    try:
                        return int(merit_data.get(key, 0) or 0)
                    except (TypeError, ValueError):
                        return 0
            return 0
        if isinstance(merit_data, int):
            return merit_data
        return 0

    def _is_free_language(self, language, native_language):
        """English and native language are always free."""
        return language == "English" or (native_language != "English" and language == native_language)

    def _parse_language_source(self, raw_source):
        """Normalize language source aliases."""
        source = (raw_source or "").strip().lower().replace(" ", "_")
        if source in ("", "lang", "language", "readwrite", "read_write", "literacy"):
            return self.LANGUAGE_SOURCE
        if source in ("multilingual", "multi", "conversation", "conversational"):
            return self.MULTILINGUAL_SOURCE
        return None

    def _parse_add_language_args(self):
        """
        Parse add args as:
          +language/add <language>
          +language/add <language>/multilingual
        """
        raw = (self.args or "").strip()
        if not raw:
            return None, None

        if "/" not in raw:
            return raw.title(), self.LANGUAGE_SOURCE

        lang_part, source_part = raw.rsplit("/", 1)
        source = self._parse_language_source(source_part)
        if not source:
            # Treat entire input as language if slash wasn't a source suffix.
            return raw.title(), self.LANGUAGE_SOURCE
        return lang_part.strip().title(), source

    def _get_language_proficiencies(self, target, languages, native_language):
        """
        Return and normalize per-language source mapping.

        Stored as target.db.language_proficiencies:
          { "Spanish": "language"|"multilingual", ... }
        """
        prof = getattr(target.db, "language_proficiencies", None) or {}
        if isinstance(prof, Mapping):
            prof = dict(prof)
        else:
            prof = {}

        changed = False
        valid_languages = set(languages)

        # Keep only currently known languages.
        for lang in list(prof.keys()):
            if lang not in valid_languages:
                del prof[lang]
                changed = True

        # Ensure all known languages have a source.
        for lang in languages:
            if self._is_free_language(lang, native_language):
                if prof.get(lang) != self.LANGUAGE_SOURCE:
                    prof[lang] = self.LANGUAGE_SOURCE
                    changed = True
                continue
            source = self._parse_language_source(prof.get(lang))
            if source is None:
                # Backward compatibility: legacy additions default to full Language literacy.
                prof[lang] = self.LANGUAGE_SOURCE
                changed = True

        if changed:
            target.db.language_proficiencies = prof
        return prof

    def _iter_merit_entries(self, merits):
        """
        Yield (merit_key, merit_data) pairs from supported merit layouts.

        Supports both:
        - flat: merits[merit_key] = merit_data
        - nested: merits[category][merit_key] = merit_data
        """
        if not isinstance(merits, Mapping):
            return

        for merit_key, merit_data in merits.items():
            if not isinstance(merit_key, str):
                continue

            # Flat merit layout
            if isinstance(merit_data, (int, float)) or (
                isinstance(merit_data, Mapping) and any(k in merit_data for k in ("dots", "perm"))
            ):
                yield merit_key, merit_data
                continue

            # Nested merit layout by category
            if isinstance(merit_data, Mapping):
                for nested_key, nested_data in merit_data.items():
                    if not isinstance(nested_key, str):
                        continue
                    if isinstance(nested_data, (int, float)) or (
                        isinstance(nested_data, Mapping) and any(k in nested_data for k in ("dots", "perm"))
                    ):
                        yield nested_key, nested_data

    def _calculate_language_point_breakdown(self, target):
        """Return (language_points, multilingual_points)."""
        stats = getattr(target.db, "stats", {}) or {}
        merits = stats.get("merits", {}) or {}
        language_points = 0
        multilingual_points = 0

        if not isinstance(merits, Mapping):
            return 0, 0

        for merit_key, merit_data in self._iter_merit_entries(merits):
            normalized_key = merit_key.strip().lower().replace(" ", "_")
            if normalized_key.startswith("merit:"):
                normalized_key = normalized_key.split(":", 1)[1]
            base_key = normalized_key.split(":", 1)[0]
            dots = self._extract_merit_dots(merit_data)
            if dots <= 0:
                continue
            if base_key == "language":
                language_points += dots
            elif base_key == "multilingual":
                multilingual_points += dots * 2

        return language_points, multilingual_points

    def _calculate_language_points(self, target):
        """Return total language points from both merits."""
        language_points, multilingual_points = self._calculate_language_point_breakdown(target)
        return language_points + multilingual_points

    def _count_used_language_slots(self, languages, native_language, proficiencies):
        """
        Count used points by source for non-free languages.

        Returns:
            tuple[int, int]: (used_language_points, used_multilingual_points)
        """
        used_language = 0
        used_multilingual = 0
        for lang in languages:
            if self._is_free_language(lang, native_language):
                continue
            source = self._parse_language_source(proficiencies.get(lang))
            if source == self.MULTILINGUAL_SOURCE:
                used_multilingual += 1
            else:
                used_language += 1
        return used_language, used_multilingual

    def func(self):
        """Execute command."""
        if "check" in self.switches:
            # Add a new switch to manually check and adjust languages
            self.validate_languages()
            self.list_languages()
            return
        
        if not self.args and not self.switches:
            # Display languages
            self.list_languages()
            return
        
        if "native" in self.switches:
            if not self.args:
                self.caller.msg("Usage: +language/native <language>")
                return
            
            # Only allow setting native language if not approved
            if self.caller.db.approved:
                self.caller.msg("You can only set your native language during character generation.")
                return
            
            language = self.args.strip().title()
            
            # Check if the language is valid
            found = False
            proper_language = None
            for lang_key, proper_lang in AVAILABLE_LANGUAGES.items():
                if lang_key.lower() == language.lower() or proper_lang.lower() == language.lower():
                    found = True
                    proper_language = proper_lang
                    break
            
            if not found:
                self.caller.msg(f"'{language}' is not a valid language. Use +languages/all to see available languages.")
                return
            
            # Set the native language
            old_native = self.caller.db.native_language or "English"
            self.caller.db.native_language = proper_language
            
            # Get current languages and ensure both English and the native language are included
            languages = self.caller.get_languages()
            
            # Remove the old native language if it's not English
            if old_native != "English" and old_native in languages:
                languages.remove(old_native)
            
            # Ensure English and new native language are included
            if "English" not in languages:
                languages.append("English")
            if proper_language not in languages:
                languages.append(proper_language)
            
            # Update the character's languages
            self.caller.db.languages = languages
            
            self.caller.msg(f"You have set {proper_language} as your native language.")
            if old_native != "English" and old_native != proper_language:
                self.caller.msg(f"Removed {old_native} from your known languages.")
            
            # Show updated language list
            self.list_languages()
            return

        if "set" in self.switches:
            self.do_set_languages()
        elif "rem" in self.switches:
            self.remove_language()
        elif "all" in self.switches:
            self.list_all_languages()
        elif "view" in self.switches:
            self.view_character_languages()
        elif not self.args:
            self.list_languages()
        elif "add" in self.switches:
            self.add_language()
        elif self.args.lower() == "none":
            self.set_speaking_language(None)
        else:
            self.set_speaking_language(self.args.lower().capitalize())

    def list_languages(self):
        """Display the character's known languages and current speaking language."""
        languages = self.caller.get_languages()
        current = self.caller.get_speaking_language()
        native_language = self.caller.db.native_language or "English"
        proficiencies = self._get_language_proficiencies(self.caller, languages, native_language)
        
        output = [
            header("Languages", width=78),
            section_header("Known Languages", width=78),
        ]
        
        # Format languages list with wrapping
        if languages:
            wrapped_languages = wrap_ansi(f"|w{', '.join(languages)}|n", width=76, left_padding=0)
            output.append(wrapped_languages)
        else:
            output.append("None")
        
        # Add current speaking language
        output.extend([
            section_header("Currently Speaking", width=78),
            current if current else "None"
        ])

        # Literacy breakdown
        read_write_languages = [lang for lang in languages if self._parse_language_source(proficiencies.get(lang)) != self.MULTILINGUAL_SOURCE]
        conversational_languages = [lang for lang in languages if self._parse_language_source(proficiencies.get(lang)) == self.MULTILINGUAL_SOURCE]
        output.extend([
            section_header("Read/Write Languages", width=78),
            ", ".join(read_write_languages) if read_write_languages else "None",
            section_header("Conversational Languages", width=78),
            ", ".join(conversational_languages) if conversational_languages else "None",
        ])

        # Merit points section
        language_points, multilingual_points = self._calculate_language_point_breakdown(self.caller)
        total_points = language_points + multilingual_points
        used_language, used_multilingual = self._count_used_language_slots(languages, native_language, proficiencies)
        used_languages = used_language + used_multilingual
        points_remaining = total_points - used_languages
        output.extend([
            section_header("Merit Points", width=78),
            f"Total points: {total_points} (from Language and Multilingual merits)",
            f"Language points: {language_points} total, {max(0, language_points - used_language)} remaining",
            f"Multilingual points: {multilingual_points} total, {max(0, multilingual_points - used_multilingual)} remaining",
            f"Native language: {native_language}",
            f"Languages used: {used_languages}",
            f"Points remaining: {points_remaining}"
        ])
        
        output.append(footer(78))
        
        # Send only the formatted output
        self.caller.msg("\n".join(output))

    def set_speaking_language(self, language):
        try:
            self.caller.set_speaking_language(language)
            if language:
                self.caller.msg(f"|cLANGUAGE>|n Now speaking in |w{language}|n.")
            else:
                self.caller.msg("|cLANGUAGE>|n You are no longer speaking in any specific language.")
        except ValueError as e:
            self.caller.msg(str(e))

    def add_language(self):
        """Add a new language to the character."""
        if not self.args:
            self.caller.msg("Usage: +language/add <language>[/multilingual]")
            return

        language, source = self._parse_add_language_args()
        if not language:
            self.caller.msg("Usage: +language/add <language>[/multilingual]")
            return

        if language not in AVAILABLE_LANGUAGES.values():
            self.caller.msg(f"'{language}' is not a valid language. Use +languages/all to see available languages.")
            return

        languages = self.caller.get_languages()
        native_language = self.caller.db.native_language or "English"
        proficiencies = self._get_language_proficiencies(self.caller, languages, native_language)
        language_points, multilingual_points = self._calculate_language_point_breakdown(self.caller)
        used_language, used_multilingual = self._count_used_language_slots(languages, native_language, proficiencies)

        if language in languages:
            existing_source = self._parse_language_source(proficiencies.get(language)) or self.LANGUAGE_SOURCE

            # Allow upgrading an existing conversational language to read/write.
            if existing_source == self.MULTILINGUAL_SOURCE and source == self.LANGUAGE_SOURCE:
                if used_language >= language_points:
                    self.caller.msg("You don't have enough Language points remaining to upgrade this language to read/write.")
                    return
                proficiencies[language] = self.LANGUAGE_SOURCE
                self.caller.db.language_proficiencies = proficiencies
                self.caller.msg(
                    f"Upgraded {language} to Language (read/write). "
                    "Its Multilingual point has been refunded."
                )
                return

            if existing_source == self.LANGUAGE_SOURCE:
                self.caller.msg(f"You already know {language} as a read/write language.")
            else:
                self.caller.msg(f"You already know {language} as a conversational language.")
            return

        if source == self.MULTILINGUAL_SOURCE and used_multilingual >= multilingual_points:
            self.caller.msg("You don't have enough Multilingual points remaining.")
            return
        if source == self.LANGUAGE_SOURCE and used_language >= language_points:
            self.caller.msg("You don't have enough Language points remaining.")
            return

        # Add the language
        languages.append(language)
        self.caller.db.languages = languages
        proficiencies[language] = source
        self.caller.db.language_proficiencies = proficiencies
        
        source_label = "Language (read/write)" if source == self.LANGUAGE_SOURCE else "Multilingual (conversational)"
        self.caller.msg(f"You have learned {language} via {source_label}.")

    def do_set_languages(self):
        """
        Staff command to set languages on a character.
        Usage: +language/set <character>=<language1>,<language2>,...
        Adds specified languages to character's existing languages.
        """
        if not (self.caller.check_permstring("builders") or 
                self.caller.check_permstring("admin") or 
                self.caller.check_permstring("staff")):
            self.caller.msg("You don't have permission to set languages.")
            return
            
        if not self.lhs or not self.rhs:
            self.caller.msg("Usage: +language/set <character>=<language1>,<language2>,...\n"
                          "Example: +language/set Bob=French,Spanish")
            return
            
        # Search for both online and offline characters
        matches = search_object(self.lhs.strip(), 
                                     typeclass='typeclasses.characters.Character')
        if not matches:
            self.caller.msg(f"Could not find character '{self.lhs}'.")
            return
        target = matches[0]
            
        current_languages = target.get_languages()
        new_languages = current_languages.copy()
        invalid_languages = []
        
        # Process each language
        for lang in self.rhs.split(','):
            lang = lang.strip()
            
            if not lang or lang.lower() == "english":  # Skip empty or English
                continue
                
            # Try to find the proper case version
            found = False
            for available_lang in AVAILABLE_LANGUAGES.values():
                if available_lang.lower() == lang.lower():
                    if available_lang not in new_languages:
                        new_languages.append(available_lang)
                    found = True
                    break
                    
            if not found:
                invalid_languages.append(lang)
        
        if invalid_languages:
            self.caller.msg(f"Warning: The following languages were not recognized: {', '.join(invalid_languages)}\n"
                          f"Available languages are: {', '.join(AVAILABLE_LANGUAGES.values())}")
            return
            
        # Set the languages
        target.db.languages = new_languages
        native_language = target.db.native_language or "English"
        proficiencies = self._get_language_proficiencies(target, new_languages, native_language)
        for lang in new_languages:
            if lang not in proficiencies:
                proficiencies[lang] = self.LANGUAGE_SOURCE
        target.db.language_proficiencies = proficiencies
        
        self.caller.msg(f"Set {target.name}'s languages to: {', '.join(new_languages)}")
        target.msg(f"Your known languages have been set to: {', '.join(new_languages)}")

    def list_all_languages(self):
        """Display all available languages organized by region."""
        # Define categories and their languages
        categories = {
            "Common Languages": [
                "English", "Spanish", "French", "German", "Italian", "Portuguese", "Mandarin",
                "Cantonese", "Japanese", "Korean", "Arabic", "Hindi", "Russian"
            ],
            "African Languages": [
                "Amharic", "Hausa", "Igbo", "Lingala", "Oromo", "Somali",
                "Swahili", "Twi", "Wolof", "Yoruba", "Zulu", "Afrikaans", "Bambara", 
                "Bemba", "Chichewa", "Ganda", "Kikuyu", "Kinyarwanda", "Luganda", 
                "Luo", "Makonde", "Maltese", "Mbumba", "Ndebele", "Nyanja", "Shona", 
                "Swati", "Tswana", "Venda", "Xhosa"
            ],
            "European Languages": [
                "Albanian", "Armenian", "Azerbaijani", "Belarusian", "Bosnian", "Bulgarian",
                "Croatian", "Czech", "Danish", "Dutch", "Estonian", "Finnish", "French",
                "German", "Greek", "Hungarian", "Icelandic", "Irish", "Italian", "Latvian",
                "Lithuanian", "Macedonian", "Maltese", "Moldovan", "Montenegrin", "Norwegian",
                "Polish", "Portuguese", "Romanian", "Russian", "Serbian", "Slovak", "Slovenian",
                "Swedish", "Ukrainian"
            ],
            "Asian Languages": [
                "Burmese", "Bengali", "Mandarin", "Cantonese", "Gujarati", "Malay", 
                "Punjabi", "Tamil", "Telugu", "Hindi", "Indonesian"
            ],
            "Middle Eastern Languages": [
                "Arabic", "Hebrew", "Kurdish", "Armenian", "Syriac", "Pashto", "Turkish",
                "Urdu", "Farsi"
            ],
            "Indigenous American Languages": [
                "Navajo", "Quechua", "Inuit", "Apache", "Cherokee", "Chamorro", "Chickasaw", 
                "Choctaw", "Comanche", "Cree", "Haida", "Haudenosaunee", "Iroquois", "Kiowa", 
                "Lakota", "Maya", "Pueblo", "Tlingit", "Turtle", "Yaqui", "Zuni"
            ],
            "Pacific Languages": [
                "Hawaiian", "Maori", "Samoan", "Tahitian", "Tongan", "Fijian"
            ],
            "Ancient Languages": [
                "Latin", "Ancient Greek", "Ancient Egyptian", "Old English", "Old Norse",
                "Sanskrit", "Akkadian", "Sumerian", "Babylonian", "Phoenician", "Aramaic",
                "Coptic", "Elamite", "Hittite", "Minoan", "Mycenaean"
            ],
            "Supernatural Languages": [
                "Enochian", "Spirit Speech", "First Tongue", "High Speech", "Animal Speech"
            ]
        }
        
        # Create the display table
        from evennia.utils import evtable
        
        # Header
        self.caller.msg("|wAvailable Languages:|n")
        self.caller.msg("=" * 78)
        
        # Display each category
        for category_name, languages in categories.items():
            if languages:  # Only show categories that have languages
                self.caller.msg(f"\n|y{category_name}:|n")
                
                # Sort languages alphabetically within each category
                languages.sort()
                
                # Create columns (3 columns of approximately equal size)
                table = evtable.EvTable(border=None)
                col_width = 25  # Adjust this if needed
                
                # Split languages into columns
                col1 = languages[::3]
                col2 = languages[1::3]
                col3 = languages[2::3]
                
                # Add columns to table
                table.add_column(*col1, width=col_width)
                if col2:  # Only add column if there are languages for it
                    table.add_column(*col2, width=col_width)
                if col3:  # Only add column if there are languages for it
                    table.add_column(*col3, width=col_width)
                
                # Display the table
                self.caller.msg(table)
        
        self.caller.msg("\n" + "=" * 78)

    def remove_language(self):
        """
        Remove a language from a character.
        Players can only remove languages from themselves.
        Staff can remove languages from any character.
        """
        if not self.args:
            self.caller.msg("Usage: +language/rem <language> or +language/rem <name>=<language>")
            return

        # Check if this is a staff removing language from another player
        is_staff = (
            self.caller.check_permstring("builders")
            or self.caller.check_permstring("admin")
            or self.caller.check_permstring("staff")
        )

        if "=" in self.args:
            if not is_staff:
                self.caller.msg("You don't have permission to set languages.")
                return
            
            target_name, language = self.args.split("=", 1)
            matches = search_object(target_name.strip(), 
                                      typeclass='typeclasses.characters.Character')
            if not matches:
                self.caller.msg(f"Could not find character '{target_name}'.")
                return
            target = matches[0]
        else:
            target = self.caller
            language = self.args

        if target == self.caller and self.caller.db.approved and not is_staff:
            self.caller.msg("Approved characters cannot remove languages. You can still add languages if you have points.")
            return

        language = language.strip()
        
        # Can't remove English
        if language.lower() == "english":
            self.caller.msg("You cannot remove English.")
            return

        # Get current languages
        current_languages = target.get_languages()
        native_language = target.db.native_language or "English"
        proficiencies = self._get_language_proficiencies(target, current_languages, native_language)
        
        # Try to find the proper case version
        found = False
        for lang_key, proper_lang in AVAILABLE_LANGUAGES.items():
            if lang_key.lower() == language.lower():
                if proper_lang in current_languages:
                    current_languages.remove(proper_lang)
                    target.db.languages = current_languages
                    proficiencies.pop(proper_lang, None)
                    target.db.language_proficiencies = proficiencies
                    
                    # If they were speaking the removed language, reset to English
                    if target.get_speaking_language() == proper_lang:
                        target.db.speaking_language = "English"
                        target.msg(f"Your speaking language has been reset to English.")
                    
                    # Notify both staff and target
                    if target == self.caller:
                        self.caller.msg(f"You have removed {proper_lang} from your known languages.")
                    else:
                        self.caller.msg(f"You have removed {proper_lang} from {target.name}'s known languages.")
                        target.msg(f"{proper_lang} has been removed from your known languages.")
                else:
                    self.caller.msg(f"{target.name if target != self.caller else 'You'} does not know {proper_lang}.")
                found = True
                break
        
        if not found:
            self.caller.msg(f"Invalid language. Available languages are: {', '.join(AVAILABLE_LANGUAGES.values())}")

    def view_character_languages(self):
        """
        Staff command to view a character's languages.
        Usage: +language/view <character>
        """
        if not (self.caller.check_permstring("builders") or 
                self.caller.check_permstring("admin") or 
                self.caller.check_permstring("staff")):
            self.caller.msg("You don't have permission to view character languages.")
            return

        if not self.args:
            self.caller.msg("Usage: +language/view <character>")
            return

        # Search for both online and offline characters
        matches = search_object(self.args.strip(), 
                              typeclass='typeclasses.characters.Character')
        if not matches:
            self.caller.msg(f"Could not find character '{self.args}'.")
            return
        
        target = matches[0]
        languages = target.get_languages()
        current = target.get_speaking_language()
        native_language = target.db.native_language or "English"
        proficiencies = self._get_language_proficiencies(target, languages, native_language)
        
        output = [
            header(f"{target.name}'s Languages", width=78),
            section_header("Known Languages", width=78),
        ]
        
        # Format languages list with wrapping
        if languages:
            wrapped_languages = wrap_ansi(f"|w{', '.join(languages)}|n", width=76, left_padding=0)
            output.append(wrapped_languages)
        else:
            output.append("None")
        
        # Add current speaking language
        output.extend([
            section_header("Currently Speaking", width=78),
            current if current else "None"
        ])

        read_write_languages = [lang for lang in languages if self._parse_language_source(proficiencies.get(lang)) != self.MULTILINGUAL_SOURCE]
        conversational_languages = [lang for lang in languages if self._parse_language_source(proficiencies.get(lang)) == self.MULTILINGUAL_SOURCE]
        output.extend([
            section_header("Read/Write Languages", width=78),
            ", ".join(read_write_languages) if read_write_languages else "None",
            section_header("Conversational Languages", width=78),
            ", ".join(conversational_languages) if conversational_languages else "None",
        ])

        # Merit points section
        language_points, multilingual_points = self._calculate_language_point_breakdown(target)
        total_points = language_points + multilingual_points
        used_language, used_multilingual = self._count_used_language_slots(languages, native_language, proficiencies)
        used_languages = used_language + used_multilingual
        points_remaining = total_points - used_languages
        output.extend([
            section_header("Merit Points", width=78),
            f"Total points: {total_points} (from Language and Multilingual merits)",
            f"Language points: {language_points} total, {max(0, language_points - used_language)} remaining",
            f"Multilingual points: {multilingual_points} total, {max(0, multilingual_points - used_multilingual)} remaining",
            f"Native language: {native_language}",
            f"Languages used: {used_languages}",
            f"Points remaining: {points_remaining}"
        ])
        
        output.append(footer(78))
        
        # Send only the formatted output
        self.caller.msg("\n".join(output))

    def validate_languages(self, caller=None):
        """
        Validate and adjust languages based on current merit points.
        Returns True if languages were adjusted, False otherwise.
        """
        target = caller or self.caller
        languages = target.get_languages()
        native_language = target.db.native_language or "English"
        proficiencies = self._get_language_proficiencies(target, languages, native_language)
        
        # Always keep English and native language
        allowed_languages = ["English"]
        if native_language != "English":
            allowed_languages.append(native_language)

        language_points, multilingual_points = self._calculate_language_point_breakdown(target)
        remaining_language_points = language_points
        remaining_multilingual_points = multilingual_points

        # Add languages in order until each pool is exhausted.
        languages_removed = []
        final_languages = allowed_languages.copy()
        final_proficiencies = {lang: self.LANGUAGE_SOURCE for lang in allowed_languages}
        
        for lang in languages:
            # Skip if it's already in our allowed list
            if lang in allowed_languages:
                continue

            source = self._parse_language_source(proficiencies.get(lang)) or self.LANGUAGE_SOURCE
            if source == self.MULTILINGUAL_SOURCE:
                if remaining_multilingual_points > 0:
                    final_languages.append(lang)
                    final_proficiencies[lang] = self.MULTILINGUAL_SOURCE
                    remaining_multilingual_points -= 1
                else:
                    languages_removed.append(lang)
            else:
                if remaining_language_points > 0:
                    final_languages.append(lang)
                    final_proficiencies[lang] = self.LANGUAGE_SOURCE
                    remaining_language_points -= 1
                else:
                    languages_removed.append(lang)
        
        if languages_removed:
            # Update the character's languages
            target.db.languages = final_languages
            target.db.language_proficiencies = final_proficiencies
            target.msg(f"Removed {', '.join(languages_removed)} to stay within language point limits.")
            return True
        
        target.db.language_proficiencies = final_proficiencies
        return False

    def update_merit(self, merit_name, new_value):
        """Update a merit's value and validate languages if necessary."""
        # Store old values for comparison
        old_value = self.db.stats.get('merits', {}).get(merit_name, {}).get('perm', 0)
        
        # If Language merit value decreased, validate languages
        if merit_name.lower() == 'language' and new_value < old_value:
            # Avoid circular import by calling validation directly
            if self.validate_languages():
                self.list_languages()  # Only show if changes were made
