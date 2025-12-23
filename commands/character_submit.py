"""
Character submission command for staff approval.
Allows players to submit their completed character for staff review.
"""

from evennia.commands.default.muxcommand import MuxCommand
from world.jobs.models import Job, Queue
from world.cofd.template_registry import template_registry
from evennia.utils import logger


class CmdSubmit(MuxCommand):
    """
    Submit your character for staff approval.
    
    Usage:
        +submit
        
    This command creates a job in your template's request category for staff
    to review and approve your character. It includes a complete snapshot of
    all points spent during character generation.
    
    Template to Category Mapping:
        - Vampire -> VAMP
        - Werewolf -> WERE
        - Mage -> MAGE
        - Changeling -> LING
        - Geist -> GEIST
        - Promethean -> PROM
        - Demon -> DEMON
        - Hunter -> HUNT
        - Mummy -> MUMMY
        - Deviant -> DVNT
        - Mortal -> MORT
        - Mortal+ -> M+
        - Core (All other templates) -> CORE
        
    You can only submit your own character, and only if it hasn't been
    approved yet.
    """
    
    key = "+submit"
    aliases = ["submit"]
    locks = "cmd:all()"
    help_category = "Chargen & Character Info"
    
    # Template to category mapping
    TEMPLATE_CATEGORY_MAP = {
        "vampire": "VAMP",
        "werewolf": "WERE",
        "mage": "MAGE",
        "changeling": "LING",
        "geist": "GEIST",
        "promethean": "PROM",
        "demon": "DEMON",
        "hunter": "HUNT",
        "mummy": "MUMMY",
        "deviant": "DVNT",
        "mortal": "MORT",
        "mortal_plus": "M+",
        "mortal+": "M+",
    }
    
    def func(self):
        """Execute the submit command."""
        caller = self.caller
        
        # Check if the caller is a character
        if not hasattr(caller, 'db') or not hasattr(caller.db, 'stats'):
            caller.msg("You must be a character to submit for approval.")
            return
        
        # Check if already approved
        if caller.db.approved:
            caller.msg("Your character has already been approved!")
            return
        
        # Get character stats
        stats = caller.db.stats
        if not stats:
            caller.msg("You don't have any stats set. Please set up your character first.")
            return
        
        # Get template
        template = stats.get("other", {}).get("template", "Mortal")
        template_lower = template.lower().replace(" ", "_")
        
        # Determine category based on template
        category = self.TEMPLATE_CATEGORY_MAP.get(template_lower, "CORE")
        
        # Create the snapshot
        snapshot = self._create_character_snapshot(caller, stats, template)
        
        # Create the job title
        title = f"Character Approval: {caller.name} ({template})"
        
        # Create the job description
        description = f"Character approval request for {caller.name}\n\n"
        description += snapshot
        
        try:
            # Get or create the queue for this category
            queue, created = Queue.objects.get_or_create(
                name=category,
                defaults={'automatic_assignee': None}
            )
            
            # Create the job
            job = Job.objects.create(
                title=title,
                description=description,
                requester=caller.account,
                queue=queue,
                status='open'
            )
            
            # Notify the player
            caller.msg(f"|gCharacter submission successful!|n")
            caller.msg(f"Job #{job.id} has been created in the {category} queue.")
            caller.msg(f"Staff will review your character and approve it when ready.")
            caller.msg(f"Use |w+jobs {job.id}|n to view the job status.")
            
            # Log the submission
            logger.log_info(f"{caller.name} submitted character for approval (Job #{job.id})")
            
        except Exception as e:
            caller.msg(f"|rError creating job: {e}|n")
            logger.log_err(f"Error creating character submission job: {e}")
    
    def _create_character_snapshot(self, character, stats, template):
        """
        Create a detailed snapshot of character stats for the job.
        
        Args:
            character: The character object
            stats: The character's stats dictionary
            template: The character's template
            
        Returns:
            str: Formatted snapshot of character stats
        """
        lines = []
        lines.append("=" * 78)
        lines.append("CHARACTER SNAPSHOT")
        lines.append("=" * 78)
        lines.append("")
        
        # Basic Information
        lines.append("--- BASIC INFORMATION ---")
        lines.append(f"Character Name: {character.name}")
        lines.append(f"Template: {template}")
        
        bio = stats.get("bio", {})
        if bio.get("full_name"):
            lines.append(f"Full Name: {bio.get('full_name')}")
        if bio.get("concept"):
            lines.append(f"Concept: {bio.get('concept')}")
        if bio.get("birthdate"):
            lines.append(f"Birthdate: {bio.get('birthdate')}")
        lines.append("")
        
        # Template-specific bio fields
        bio_fields = template_registry.get_bio_fields(template)
        if bio_fields:
            lines.append("--- TEMPLATE INFORMATION ---")
            for field in bio_fields:
                value = bio.get(field, "")
                if value and value != "<not set>":
                    field_display = field.replace("_", " ").title()
                    lines.append(f"{field_display}: {value}")
            lines.append("")
        
        # Attributes
        attributes = stats.get("attributes", {})
        if attributes:
            lines.append("--- ATTRIBUTES ---")
            attr_total = 0
            
            # Mental
            lines.append("Mental:")
            for attr in ["intelligence", "wits", "resolve"]:
                value = attributes.get(attr, 1)
                attr_total += value - 1  # Start at 1, so subtract baseline
                lines.append(f"  {attr.title()}: {value}")
            
            # Physical
            lines.append("Physical:")
            for attr in ["strength", "dexterity", "stamina"]:
                value = attributes.get(attr, 1)
                attr_total += value - 1
                lines.append(f"  {attr.title()}: {value}")
            
            # Social
            lines.append("Social:")
            for attr in ["presence", "manipulation", "composure"]:
                value = attributes.get(attr, 1)
                attr_total += value - 1
                lines.append(f"  {attr.title()}: {value}")
            
            lines.append(f"Total Attribute Dots: {attr_total + 9} (including 9 free dots)")
            lines.append("")
        
        # Skills
        skills = stats.get("skills", {})
        if skills:
            lines.append("--- SKILLS ---")
            skill_total = 0
            
            # Mental skills
            mental_skills = ["crafts", "investigation", "medicine", "occult", "politics", "science"]
            lines.append("Mental:")
            for skill in mental_skills:
                value = skills.get(skill, 0)
                if value > 0:
                    skill_total += value
                    lines.append(f"  {skill.title()}: {value}")
            
            # Physical skills
            physical_skills = ["athletics", "brawl", "drive", "firearms", "larceny", 
                             "stealth", "survival", "weaponry"]
            lines.append("Physical:")
            for skill in physical_skills:
                value = skills.get(skill, 0)
                if value > 0:
                    skill_total += value
                    lines.append(f"  {skill.title()}: {value}")
            
            # Social skills
            social_skills = ["animal_ken", "empathy", "expression", "intimidation", 
                           "persuasion", "socialize", "streetwise", "subterfuge"]
            lines.append("Social:")
            for skill in social_skills:
                value = skills.get(skill, 0)
                if value > 0:
                    skill_total += value
                    display_name = skill.replace("_", " ").title()
                    lines.append(f"  {display_name}: {value}")
            
            lines.append(f"Total Skill Dots: {skill_total}")
            lines.append("")
        
        # Specialties
        specialties = stats.get("specialties", {})
        if specialties:
            lines.append("--- SPECIALTIES ---")
            for skill, spec_list in specialties.items():
                skill_display = skill.replace("_", " ").title()
                if isinstance(spec_list, list):
                    for spec in spec_list:
                        lines.append(f"{skill_display}: {spec}")
                else:
                    lines.append(f"{skill_display}: {spec_list}")
            lines.append("")
        
        # Merits
        merits = stats.get("merits", {})
        if merits:
            lines.append("--- MERITS ---")
            merit_total = 0
            for merit_name, merit_data in merits.items():
                if isinstance(merit_data, dict):
                    dots = merit_data.get("dots", 0)
                else:
                    dots = merit_data
                merit_total += dots
                display_name = merit_name.replace("_", " ").title()
                lines.append(f"{display_name}: {dots}")
            lines.append(f"Total Merit Dots: {merit_total}")
            lines.append("")
        
        # Advantages (derived stats)
        advantages = stats.get("advantages", {})
        if advantages:
            lines.append("--- ADVANTAGES ---")
            for adv in ["willpower", "health", "speed", "defense", "initiative"]:
                value = advantages.get(adv, 0)
                lines.append(f"{adv.title()}: {value}")
            
            # Template-specific power stats
            power_stats = ["blood_potency", "primal_urge", "gnosis", "wyrd", 
                          "azoth", "synergy", "primum", "satiety", "sekhem", "deviation"]
            for stat in power_stats:
                if stat in advantages:
                    value = advantages[stat]
                    display_name = stat.replace("_", " ").title()
                    lines.append(f"{display_name}: {value}")
            
            # Resource pools
            pools = ["vitae", "essence", "mana", "glamour", "pyros", "plasm", 
                    "aether", "lair", "pillars", "instability"]
            for pool in pools:
                if pool in advantages:
                    value = advantages[pool]
                    lines.append(f"{pool.title()}: {value}")
            lines.append("")
        
        # Powers (supernatural abilities)
        powers = stats.get("powers", {})
        if powers:
            lines.append("--- POWERS ---")
            
            # Group powers by type
            power_groups = {}
            for power_name, power_value in powers.items():
                # Try to determine power type from name
                if ":" in power_name:
                    power_type, _ = power_name.split(":", 1)
                    if power_type not in power_groups:
                        power_groups[power_type] = []
                    power_groups[power_type].append((power_name, power_value))
                else:
                    # Generic powers
                    if "generic" not in power_groups:
                        power_groups["generic"] = []
                    power_groups["generic"].append((power_name, power_value))
            
            for power_type, power_list in power_groups.items():
                if power_type != "generic":
                    lines.append(f"{power_type.title()}:")
                for power_name, power_value in power_list:
                    display_name = power_name.replace("_", " ").title()
                    if isinstance(power_value, dict):
                        dots = power_value.get("dots", 0)
                        lines.append(f"  {display_name}: {dots}")
                    else:
                        lines.append(f"  {display_name}: {power_value}")
            lines.append("")
        
        # Other stats
        other = stats.get("other", {})
        if other:
            lines.append("--- OTHER ---")
            integrity_name = template_registry.get_integrity_name(template)
            integrity_value = other.get("integrity", 7)
            lines.append(f"{integrity_name}: {integrity_value}")
            lines.append(f"Size: {other.get('size', 5)}")
            lines.append(f"Beats: {other.get('beats', 0)}")
            lines.append(f"Experience: {other.get('experience', 0)}")
            lines.append("")
        
        # Aspirations
        if hasattr(character.db, 'aspirations') and character.db.aspirations:
            aspirations = [asp for asp in character.db.aspirations if asp]
            if aspirations:
                lines.append("--- ASPIRATIONS ---")
                for i, asp in enumerate(aspirations, 1):
                    lines.append(f"{i}. {asp}")
                lines.append("")
        
        lines.append("=" * 78)
        lines.append("END OF CHARACTER SNAPSHOT")
        lines.append("=" * 78)
        
        return "\n".join(lines)


# Command set to hold the submit command
from evennia.commands.cmdset import CmdSet

class CharacterSubmitCmdSet(CmdSet):
    """
    Command set for character submission.
    """
    key = "CharacterSubmit"
    
    def at_cmdset_creation(self):
        """Add the submit command to the set."""
        self.add(CmdSubmit())

