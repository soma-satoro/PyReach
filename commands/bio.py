from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.ansi import ANSIString
from evennia.utils.evmore import EvMore
from world.reality_systems import get_template
from utils.text import apply_text_formatting
import re

# Bio questions by template type
BIO_QUESTIONS = {
    "vampire": [
        "Who were you before the Embrace (job, family life, major goals)?",
        "What was your most vivid memory of your human life?",
        "Do you have unfinished business or lingering connections with anyone from your past?",
        "Why did your sire choose you, or do you not know their reasons?",
        "How did the Embrace happen?",
        "How do you feel about your sire now?",
        "What's your preferred prey, hunting method, and feeding ground?",
        "How do you fit (or not fit) your Clan's stereotypes?",
        "How do you view other Kindred (Covenants, Clans, the Prince)?",
        "What are your biggest fears? What motivates you?",
        "What brings you to the city?",
        "How strict are you about maintaining the Masquerade?",
    ],
    "werewolf": [
        "What was your life like before your First Change?",
        "How did your First Change happen?",
        "Who taught you about being Uratha, and what do you think of them?",
        "How do you view your role in your pack?",
        "What is your relationship with the Shadow like?",
        "How do you balance your human life with your Uratha duties?",
        "What are your thoughts on the Pure?",
        "What's your hunting style and territory preferences?",
        "How do you feel about spirits and the spiritual world?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this territory?",
        "How do you view other supernatural creatures?",
    ],
    "changeling": [
        "What was your life like before you were taken?",
        "How were you taken, and what do you remember?",
        "What was your time in Arcadia like? What did you do there?",
        "How did you escape, and what did it cost you?",
        "What happened when you returned? Was your fetch still around?",
        "How do you feel about your Keeper now?",
        "What's your relationship with your Court like?",
        "How has the Durance changed you physically and mentally?",
        "What do you do to maintain your Clarity?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this Freehold?",
        "How do you view the Hedge and True Fae now?",
    ],
    "mage": [
        "What was your life like before your Awakening?",
        "How did you Awaken, and what did you see in the Watchtower?",
        "Who was your mentor, and what did they teach you?",
        "How do you view your Path and its implications?",
        "What is your relationship with your Order?",
        "What are your thoughts on the Exarchs and the Abyss?",
        "How do you use magic in your daily life?",
        "What's your sanctum like?",
        "How do you balance your magical life with your mundane existence?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this Consilium?",
        "How do you view Sleepers and the Lie?",
    ],
    "geist": [
        "What was your life like before you died?",
        "How did you die?",
        "What was it like meeting your geist?",
        "What kind of relationship do you have with your geist?",
        "How has death and rebirth changed your perspective?",
        "What's your relationship with ghosts like?",
        "How do you feel about the Underworld?",
        "What role do you play in your krewe, if you have one?",
        "How do you use your powers?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this city?",
        "How do you view the living and the dead now?",
    ],
    "demon": [
        "What was your life like in the God-Machine?",
        "How and why did you Fall?",
        "Who did you share part of yourself with when you first Fell?",
        "Who doesn't know, but suspects you're not human?",
        "Who could give you up to the angels right now, if they really wanted to?",
        "Who would you trust the truest part of yourself with if you absolutely had to?",
        "Who thinks they have something on you, when all they really have is smoke and mirrors?",
        "What's your relationship with your Incarnation and Agenda?",
        "How do you maintain your various Covers?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this city?",
        "How do you view angels and the Infrastructure?",
    ],
    "promethean": [
        "What were you created from, and who created you?",
        "What was your Awakening like?",
        "What are you seeking through the Pilgrimage?",
        "Who or what is your guide on the Pilgrimage?",
        "How do mortals react to you?",
        "What's your relationship with the Disquiet?",
        "How do you deal with Torment and Wasteland?",
        "What role do you play in your throng, if you have one?",
        "How has the Pilgrimage changed you?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this location?",
        "How do you view humanity and mortality?",
    ],
    "hunter": [
        "What was your life like before you learned about monsters?",
        "How did you first encounter the supernatural?",
        "Who recruited you, or did you figure it out yourself?",
        "What's your relationship with your compact or conspiracy?",
        "How do you balance hunting with your normal life?",
        "What tactics do you prefer when dealing with monsters?",
        "How do you feel about the different types of supernatural creatures?",
        "What resources do you have access to?",
        "How do you justify the Hunt to yourself?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this city?",
        "How do you view other hunters and their methods?",
    ],
    "mummy": [
        "What was your life like in your first life?",
        "How did you die and become a mummy?",
        "What was your purpose in your cult?",
        "What's your relationship with your Judge?",
        "How have you changed through your many lives?",
        "What are your thoughts on the Deceived?",
        "How do you use your Utterances and Affinities?",
        "What role do you play in your guild, if any?",
        "How do you balance your immortal nature with your mortal vessel?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this time and place?",
        "How do you view the modern world?",
    ],
    "deviant": [
        "What was your life like before you were changed?",
        "How were you transformed? Who or what did this to you?",
        "What's your relationship with your Origin?",
        "How do you manage your Instability and Scars?",
        "What are your thoughts on Progenitors?",
        "How do you use your Variations and Adaptations?",
        "What's your relationship with the Devoted, if any?",
        "How does Baseline society view you?",
        "How do you balance your monstrous nature with your humanity?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this city?",
        "How do you view other Remade?",
    ],
    "mortal": [
        "What is your background and upbringing?",
        "What do you do for a living?",
        "Do you have family or close relationships?",
        "What are your goals and ambitions?",
        "Have you encountered the supernatural?",
        "What are your strengths and weaknesses?",
        "What is your daily life like?",
        "What communities or groups are you part of?",
        "How do you spend your free time?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this city?",
        "What do you believe about the world?",
    ],
    "mortal+": [
        "What is your background and upbringing?",
        "What do you do for a living?",
        "Do you have family or close relationships?",
        "How did you discover your supernatural abilities?",
        "How do you use your powers in daily life?",
        "Do others know about your abilities? How do they react?",
        "What are your goals and ambitions?",
        "How do you view the supernatural world?",
        "How do you spend your free time?",
        "What are your biggest fears? What motivates you?",
        "What brings you to this city?",
        "How do you balance your mortal and supernatural sides?",
    ],
}

# Breaking point questions (same for all templates)
BREAKING_POINT_QUESTIONS = [
    "What is the worst thing your character has ever done?",
    "What is the worst thing your character can imagine himself doing?",
    "What is the worst thing your character can imagine someone else doing?",
    "What has your character forgotten?",
    "What is the most traumatic thing that has happened to your character? (not related to being Embraced, Lost, First Changed, etc.)",
]

# Templates that use integrity breaking points (not splat-specific mechanics)
INTEGRITY_TEMPLATES = ["mortal", "mortal+", "hunter"]


class CmdBio(MuxCommand):
    """
    Manage your character's background and biography.
    
    Usage:
        +bio                              - View your current bio
        +bio <character>                  - View another character's bio (staff only)
        +bio/q1 <text>                    - Answer bio question 1
        +bio/q2 <text>                    - Answer bio question 2
        ... (continues for all questions in your template)
        +bio/bp1 <text>                   - Answer breaking point question 1
        +bio/bp2 <text>                   - Answer breaking point question 2
        ... (continues for all 5 breaking point questions)
        +bio/pref <text>                  - Set your RP preferences and genres
        +bio/story <text>                 - Set your free-form character story
        +bio/touchstone <name>            - Add a touchstone
        +bio/touchstone/remove <#>        - Remove a touchstone by number
        
    Bio questions are specific to your character's template (Vampire, Werewolf, etc.).
    Breaking point questions help establish your character's moral boundaries.
    
    For templates that don't use Integrity (vampires, werewolves, changelings, etc.),
    breaking point questions are for background information only, not mechanics.
    
    Touchstones are people, things, or organizations that link your character to
    their humanity (or Clarity, Harmony, etc.). They provide mechanical benefits
    when resisting integrity loss.
    
    Examples:
        +bio                              - View your bio
        +bio John                          - Staff: View John's bio
        +bio/q1 I was a detective before the Embrace
        +bio/bp1 I killed someone in self-defense
        +bio/pref I enjoy political intrigue and social scenes. I prefer to avoid graphic violence.
        +bio/touchstone My sister Sarah
        +bio/touchstone/remove 2
        +bio/story This is my character's full background story...
    """
    
    key = "+bio"
    aliases = ["+background", "+biography"]
    help_category = "Chargen & Character Info"
    
    def func(self):
        """Execute the command"""
        # No switches - viewing bio
        if not self.switches:
            target = self.get_target()
            if not target:
                return
            
            # Initialize bio data if it doesn't exist
            self.initialize_bio_data(target)
            self.show_bio(target)
            return
        
        # With switches - always edit your own bio (target is self.caller)
        target = self.caller
        
        # Initialize bio data if it doesn't exist
        self.initialize_bio_data(target)
        
        # Handle switches
        switch = self.switches[0].lower()
        
        # Question switches (q1, q2, q3, etc.)
        if switch.startswith("q") and len(switch) > 1 and switch[1:].isdigit():
            self.set_question(target, int(switch[1:]))
            return
        
        # Breaking point switches (bp1, bp2, etc.)
        if switch.startswith("bp") and len(switch) > 2 and switch[2:].isdigit():
            self.set_breaking_point(target, int(switch[2:]))
            return
        
        # Other switches
        if switch == "pref":
            self.set_preference(target)
        elif switch == "story":
            self.set_story(target)
        elif switch == "touchstone":
            # Check for nested switch (touchstone/remove)
            if len(self.switches) > 1 and self.switches[1].lower() == "remove":
                self.remove_touchstone(target)
            else:
                self.add_touchstone(target)
        else:
            self.caller.msg("Invalid switch. See |whelp +bio|n for usage.")
    
    def get_target(self):
        """Get the target character for the bio command."""
        # No args means self
        if not self.args:
            return self.caller
        
        # Args provided - check if staff
        if not self.caller.check_permstring("Admin"):
            self.caller.msg("|rYou can only view your own bio. Staff can view others' bios.|n")
            return None
        
        # Search for character
        from utils.search_helpers import search_character
        target = search_character(self.caller, self.args.strip())
        return target
    
    def initialize_bio_data(self, character):
        """Initialize bio data structure if it doesn't exist."""
        if not hasattr(character.db, "bio_data") or character.db.bio_data is None:
            character.db.bio_data = {
                "questions": {},
                "breaking_points": {},
                "rp_preferences": "",
                "story": "",
                "touchstones": [],
            }
        else:
            # Ensure all keys exist and have proper types
            if "questions" not in character.db.bio_data or character.db.bio_data["questions"] is None:
                character.db.bio_data["questions"] = {}
            if "breaking_points" not in character.db.bio_data or character.db.bio_data["breaking_points"] is None:
                character.db.bio_data["breaking_points"] = {}
            if "rp_preferences" not in character.db.bio_data or character.db.bio_data["rp_preferences"] is None:
                character.db.bio_data["rp_preferences"] = ""
            if "story" not in character.db.bio_data or character.db.bio_data["story"] is None:
                character.db.bio_data["story"] = ""
            if "touchstones" not in character.db.bio_data or character.db.bio_data["touchstones"] is None:
                character.db.bio_data["touchstones"] = []
    
    def show_bio(self, target):
        """Display the character's bio."""
        template = get_template(target).lower()
        bio_data = target.db.bio_data
        
        # Defensive: ensure bio_data structure is valid
        if not bio_data:
            bio_data = {
                "questions": {},
                "breaking_points": {},
                "rp_preferences": "",
                "story": "",
                "touchstones": [],
            }
            target.db.bio_data = bio_data
        
        output = []
        
        # Get the appropriate questions for this template
        questions = BIO_QUESTIONS.get(template, BIO_QUESTIONS["mortal"])
        
        # Bio Questions header
        # Show character name when staff views another character
        if target == self.caller:
            output.append("|g<====================>|n |wYour Background Questions|n |g<====================>|n")
        else:
            # Calculate padding for centered text with character name
            total_width = 80
            header_text = f"{target.name}'s Background Questions"
            available_space = total_width - len(header_text) - 4  # -4 for < > and spaces
            left_pad = available_space // 2
            right_pad = available_space - left_pad
            output.append(f"|g<{'=' * left_pad}>|n |w{header_text}|n |g<{'=' * right_pad}>|n")
        output.append("")
        
        questions_dict = bio_data.get("questions", {}) or {}
        for i, question in enumerate(questions, 1):
            answer = questions_dict.get(f"q{i}", "")
            output.append(f"|c{i}.|n {question}")
            if answer:
                # Wrap long answers
                wrapped = self.wrap_text(answer, indent="   ")
                output.append(f"   |g{wrapped}|n")
            else:
                output.append(f"   |x(Not answered)|n")
            output.append("")
        
        # Breaking Point Questions
        output.append("|g<=================>|n |wBreaking Point Questions|n |g<=================>|n")
        
        # Add note for non-Integrity templates
        if template not in INTEGRITY_TEMPLATES:
            output.append("|y(Your template uses different integrity mechanics, this is for background only.)|n")
        
        output.append("")
        
        breaking_points_dict = bio_data.get("breaking_points", {}) or {}
        for i, question in enumerate(BREAKING_POINT_QUESTIONS, 1):
            answer = breaking_points_dict.get(f"bp{i}", "")
            output.append(f"|c{i}.|n {question}")
            if answer:
                wrapped = self.wrap_text(answer, indent="   ")
                output.append(f"   |g{wrapped}|n")
            else:
                output.append(f"   |x(Not answered)|n")
            output.append("")
        
        # RP Preferences
        output.append("|g<============================>|n |wRP Preferences|n |g<============================>|n")
        output.append("")
        pref = bio_data.get("rp_preferences", "") or ""
        if pref:
            wrapped = self.wrap_text(pref, indent="")
            output.append(f"|g{wrapped}|n")
        else:
            output.append("|x(Not set)|n")
        output.append("")
        
        # Touchstones
        output.append("|g<===============================>|n |wTouchstones|n |g<===============================>|n")
        output.append("")
        touchstones = bio_data.get("touchstones", []) or []
        if touchstones:
            for i, touchstone in enumerate(touchstones, 1):
                output.append(f"|c{i}.|n {touchstone}")
        else:
            output.append("|x(No touchstones set)|n")
        output.append("")
        
        # Free-form Story
        output.append("|g<==========================>|n |wCharacter Story|n |g<==========================>|n")
        output.append("")
        story = bio_data.get("story", "") or ""
        if story:
            wrapped = self.wrap_text(story, indent="")
            output.append(f"|g{wrapped}|n")
        else:
            output.append("|x(No story written)|n")
        output.append("")
        
        # Footer
        output.append("|g<" + "=" * 78 + ">|n")
        
        # Send output with pagination (40 lines per page)
        text = "\n".join(output)
        EvMore(self.caller, text, always_page=False, session=self.session, justify_kwargs=False, exit_on_lastpage=True)
    
    def set_question(self, target, question_num):
        """Set an answer to a bio question."""
        if not self.args:
            self.caller.msg("Usage: +bio/q<number> <answer>")
            return
        
        template = get_template(target).lower()
        questions = BIO_QUESTIONS.get(template, BIO_QUESTIONS["mortal"])
        
        if question_num < 1 or question_num > len(questions):
            self.caller.msg(f"|rInvalid question number. Your template has {len(questions)} questions.|n")
            return
        
        # Ensure bio_data structure exists
        self.initialize_bio_data(target)
        
        # Ensure questions dict exists
        if target.db.bio_data["questions"] is None:
            target.db.bio_data["questions"] = {}
        
        # Process special characters and store the answer
        processed_text = apply_text_formatting(self.args.strip())
        target.db.bio_data["questions"][f"q{question_num}"] = processed_text
        
        self.caller.msg(f"|gSet answer for question {question_num}.|n")
        self.caller.msg(f"|cQuestion:|n {questions[question_num - 1]}")
        self.caller.msg(f"|cYour Answer:|n {processed_text}")
    
    def set_breaking_point(self, target, bp_num):
        """Set an answer to a breaking point question."""
        if not self.args:
            self.caller.msg("Usage: +bio/bp<number> <answer>")
            return
        
        if bp_num < 1 or bp_num > len(BREAKING_POINT_QUESTIONS):
            self.caller.msg(f"|rInvalid breaking point question number. There are {len(BREAKING_POINT_QUESTIONS)} questions.|n")
            return
        
        # Ensure bio_data structure exists
        self.initialize_bio_data(target)
        
        # Ensure breaking_points dict exists
        if target.db.bio_data["breaking_points"] is None:
            target.db.bio_data["breaking_points"] = {}
        
        # Process special characters and store the answer
        processed_text = apply_text_formatting(self.args.strip())
        target.db.bio_data["breaking_points"][f"bp{bp_num}"] = processed_text
        
        template = get_template(target).lower()
        note = ""
        if template not in INTEGRITY_TEMPLATES:
            note = "\n|y(Note: This is for background only - your template uses different integrity mechanics)|n"
        
        self.caller.msg(f"|gSet answer for breaking point question {bp_num}.|n{note}")
        self.caller.msg(f"|cQuestion:|n {BREAKING_POINT_QUESTIONS[bp_num - 1]}")
        self.caller.msg(f"|cYour Answer:|n {processed_text}")
    
    def set_preference(self, target):
        """Set RP preferences."""
        if not self.args:
            self.caller.msg("Usage: +bio/pref <your RP preferences>")
            return
        
        # Ensure bio_data structure exists
        self.initialize_bio_data(target)
        
        # Process special characters and store preferences
        processed_text = apply_text_formatting(self.args.strip())
        target.db.bio_data["rp_preferences"] = processed_text
        self.caller.msg("|gSet your RP preferences.|n")
        self.caller.msg(f"|cPreferences:|n {processed_text}")
    
    def set_story(self, target):
        """Set free-form character story."""
        if not self.args:
            self.caller.msg("Usage: +bio/story <your character's story>")
            return
        
        # Ensure bio_data structure exists
        self.initialize_bio_data(target)
        
        # Process special characters and store story
        processed_text = apply_text_formatting(self.args.strip())
        target.db.bio_data["story"] = processed_text
        self.caller.msg("|gSet your character story.|n")
        preview = processed_text[:200] + ('...' if len(processed_text) > 200 else '')
        self.caller.msg(f"|cStory:|n {preview}")
    
    def add_touchstone(self, target):
        """Add a touchstone."""
        if not self.args:
            self.caller.msg("Usage: +bio/touchstone <touchstone description>")
            return
        
        # Ensure bio_data structure exists
        self.initialize_bio_data(target)
        
        # Ensure touchstones list exists
        if target.db.bio_data["touchstones"] is None:
            target.db.bio_data["touchstones"] = []
        
        # Process special characters and store touchstone
        processed_text = apply_text_formatting(self.args.strip())
        target.db.bio_data["touchstones"].append(processed_text)
        
        num = len(target.db.bio_data["touchstones"])
        self.caller.msg(f"|gAdded touchstone #{num}: {processed_text}|n")
    
    def remove_touchstone(self, target):
        """Remove a touchstone by number."""
        if not self.args or not self.args.strip().isdigit():
            self.caller.msg("Usage: +bio/touchstone/remove <number>")
            return
        
        # Ensure bio_data structure exists
        self.initialize_bio_data(target)
        
        num = int(self.args.strip())
        touchstones = target.db.bio_data.get("touchstones", []) or []
        
        if num < 1 or num > len(touchstones):
            self.caller.msg(f"|rInvalid touchstone number. You have {len(touchstones)} touchstones.|n")
            return
        
        removed = touchstones.pop(num - 1)
        target.db.bio_data["touchstones"] = touchstones
        
        self.caller.msg(f"|gRemoved touchstone: {removed}|n")
    
    def wrap_text(self, text, width=78, indent=""):
        """Wrap text to a specified width with optional indent."""
        # Handle pre-existing newlines from %r substitutions
        paragraphs = text.split('\n')
        wrapped_paragraphs = []
        
        for paragraph in paragraphs:
            if not paragraph.strip():
                # Preserve blank lines
                wrapped_paragraphs.append("")
                continue
                
            words = paragraph.split()
            lines = []
            current_line = indent
            
            for word in words:
                # Check if adding this word would exceed width
                test_line = current_line + (" " if current_line != indent else "") + word
                if len(ANSIString(test_line)) > width and current_line != indent:
                    lines.append(current_line)
                    current_line = indent + word
                else:
                    if current_line == indent:
                        current_line += word
                    else:
                        current_line += " " + word
            
            if current_line:
                lines.append(current_line)
            
            wrapped_paragraphs.extend(lines)
        
        return "\n".join(wrapped_paragraphs)
