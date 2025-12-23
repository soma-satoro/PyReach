from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.cofd.stat_dictionary import (
    attribute_dictionary, skill_dictionary, 
    advantage_dictionary, anchor_dictionary
)

class CmdCharacter(MuxCommand):
    """
    Create and manage your character in the Chronicles of Darkness system.
    
    Usage:
        +char/create - Start character creation
        +char/attributes <category> <attribute> <value> - Set attribute value
        +char/skills <category> <skill> <value> - Set skill value
        +char/specialty <skill> <specialty> - Add a skill specialty
        +char/anchor <type> <name> - Set virtue or vice
        +char/aspiration <number> <description> - Set an aspiration
        +char/finish - Complete character creation
        
    Categories:
        attributes: mental, physical, social
        skills: mental, physical, social
    """
    key = "+char"
    aliases = ["+character"]
    help_category = "Chargen & Character Info"
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            self.caller.msg("Usage: +char/create, +char/attributes, +char/skills, +char/specialty, +char/anchor, +char/aspiration, or +char/finish")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "create":
            self.start_creation()
        elif switch == "attributes":
            self.set_attribute()
        elif switch == "skills":
            self.set_skill()
        elif switch == "specialty":
            self.add_specialty()
        elif switch == "anchor":
            self.set_anchor()
        elif switch == "aspiration":
            self.set_aspiration()
        elif switch == "finish":
            self.finish_creation()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def start_creation(self):
        """Start the character creation process"""
        if self.caller.db.creation_started:
            self.caller.msg("Character creation already in progress.")
            return
            
        # Initialize character creation tracking
        self.caller.db.creation_started = True
        self.caller.db.attributes = {
            "mental": {"intelligence": 1, "wits": 1, "resolve": 1},
            "physical": {"strength": 1, "dexterity": 1, "stamina": 1},
            "social": {"presence": 1, "manipulation": 1, "composure": 1}
        }
        self.caller.db.skills = {
            "mental": {},
            "physical": {},
            "social": {}
        }
        self.caller.db.specialties = []
        self.caller.db.anchors = {"virtue": None, "vice": None}
        self.caller.db.aspirations = [None, None, None]
        
        self.caller.msg("Character creation started. Begin by setting your attributes.")
        self.caller.msg("Use +char/attributes <category> <attribute> <value>")
        self.caller.msg("Categories: mental, physical, social")
        self.caller.msg("Attributes: intelligence, wits, resolve, strength, dexterity, stamina, presence, manipulation, composure")
    
    def set_attribute(self):
        """Set an attribute value"""
        if not self.caller.db.creation_started:
            self.caller.msg("Start character creation first with +char/create")
            return
            
        try:
            category, attribute, value = self.args.split()
            value = int(value)
        except ValueError:
            self.caller.msg("Usage: +char/attributes <category> <attribute> <value>")
            return
            
        if category not in ["mental", "physical", "social"]:
            self.caller.msg("Invalid category. Use: mental, physical, social")
            return
            
        if attribute not in self.caller.db.attributes[category]:
            self.caller.msg(f"Invalid attribute for {category} category")
            return
            
        if not 1 <= value <= 5:
            self.caller.msg("Attribute values must be between 1 and 5")
            return
            
        self.caller.db.attributes[category][attribute] = value
        self.caller.msg(f"Set {attribute} to {value}")
    
    def set_skill(self):
        """Set a skill value"""
        if not self.caller.db.creation_started:
            self.caller.msg("Start character creation first with +char/create")
            return
            
        try:
            category, skill, value = self.args.split()
            value = int(value)
        except ValueError:
            self.caller.msg("Usage: +char/skills <category> <skill> <value>")
            return
            
        if category not in ["mental", "physical", "social"]:
            self.caller.msg("Invalid category. Use: mental, physical, social")
            return
            
        if skill not in skill_dictionary:
            self.caller.msg("Invalid skill name")
            return
            
        if not 0 <= value <= 5:
            self.caller.msg("Skill values must be between 0 and 5")
            return
            
        self.caller.db.skills[category][skill] = value
        self.caller.msg(f"Set {skill} to {value}")
    
    def add_specialty(self):
        """Add a skill specialty"""
        if not self.caller.db.creation_started:
            self.caller.msg("Start character creation first with +char/create")
            return
            
        try:
            skill, specialty = self.args.split(" ", 1)
        except ValueError:
            self.caller.msg("Usage: +char/specialty <skill> <specialty>")
            return
            
        if skill not in skill_dictionary:
            self.caller.msg("Invalid skill name")
            return
            
        if len(self.caller.db.specialties) >= 3:
            self.caller.msg("You can only have 3 skill specialties")
            return
            
        self.caller.db.specialties.append((skill, specialty))
        self.caller.msg(f"Added specialty '{specialty}' to {skill}")
    
    def set_anchor(self):
        """Set virtue or vice"""
        if not self.caller.db.creation_started:
            self.caller.msg("Start character creation first with +char/create")
            return
            
        try:
            anchor_type, name = self.args.split(" ", 1)
        except ValueError:
            self.caller.msg("Usage: +char/anchor <type> <name>")
            return
            
        if anchor_type not in ["virtue", "vice"]:
            self.caller.msg("Anchor type must be 'virtue' or 'vice'")
            return
            
        self.caller.db.anchors[anchor_type] = name
        self.caller.msg(f"Set {anchor_type} to {name}")
    
    def set_aspiration(self):
        """Set an aspiration"""
        if not self.caller.db.creation_started:
            self.caller.msg("Start character creation first with +char/create")
            return
            
        try:
            number, description = self.args.split(" ", 1)
            number = int(number)
        except ValueError:
            self.caller.msg("Usage: +char/aspiration <number> <description>")
            return
            
        if not 1 <= number <= 3:
            self.caller.msg("Aspiration number must be 1, 2, or 3")
            return
            
        self.caller.db.aspirations[number-1] = description
        self.caller.msg(f"Set aspiration {number} to: {description}")
    
    def finish_creation(self):
        """Complete character creation"""
        if not self.caller.db.creation_started:
            self.caller.msg("Start character creation first with +char/create")
            return
            
        # Verify all required elements are set
        if None in self.caller.db.anchors.values():
            self.caller.msg("You must set both virtue and vice")
            return
            
        if None in self.caller.db.aspirations:
            self.caller.msg("You must set all three aspirations")
            return
            
        # Calculate derived stats
        resolve = self.caller.db.attributes["mental"]["resolve"]
        composure = self.caller.db.attributes["social"]["composure"]
        strength = self.caller.db.attributes["physical"]["strength"]
        dexterity = self.caller.db.attributes["physical"]["dexterity"]
        stamina = self.caller.db.attributes["physical"]["stamina"]
        
        # Set derived stats
        self.caller.db.willpower = resolve + composure
        self.caller.db.health = 5 + stamina  # Size 5 for humans
        self.caller.db.speed = strength + dexterity + 5
        self.caller.db.defense = min(
            self.caller.db.attributes["mental"]["wits"],
            dexterity
        ) + self.caller.db.skills["physical"].get("athletics", 0)
        self.caller.db.initiative_mod = dexterity + composure
        
        # Set integrity
        self.caller.db.integrity = 7  # Starting value for mortals
        
        # Clear creation flags
        del self.caller.db.creation_started
        
        self.caller.msg("Character creation complete!")
        self.caller.msg(f"Willpower: {self.caller.db.willpower}")
        self.caller.msg(f"Health: {self.caller.db.health}")
        self.caller.msg(f"Speed: {self.caller.db.speed}")
        self.caller.msg(f"Defense: {self.caller.db.defense}")
        self.caller.msg(f"Initiative Modifier: {self.caller.db.initiative_mod}")
        self.caller.msg(f"Integrity: {self.caller.db.integrity}") 