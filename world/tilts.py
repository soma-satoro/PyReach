from evennia.utils.utils import lazy_property
from evennia.typeclasses.attributes import AttributeProperty
from evennia.utils.dbserialize import dbserialize, dbunserialize
from evennia.utils import logger
from datetime import datetime, timedelta

class Tilt:
    """
    A class representing a tilt that can be applied to characters or scenes during combat.
    """
    def __init__(self, name, description, tilt_type="personal", duration=None, 
                 effects=None, resolution_method=None, condition_equivalent=None):
        self.name = name
        self.description = description
        self.tilt_type = tilt_type  # "personal" or "environmental"
        self.duration = duration  # None for until resolved, number for turns/rounds
        self.effects = effects or ""  # Narrative description of effects this tilt applies
        self.resolution_method = resolution_method  # How this tilt can be resolved
        self.condition_equivalent = condition_equivalent  # What condition this becomes outside combat
        self.applied_at = datetime.now()
        self.turns_remaining = duration  # Track remaining duration
        
    def advance_turn(self):
        """Advance the tilt by one turn, reducing duration if applicable"""
        if self.turns_remaining is not None and self.turns_remaining > 0:
            self.turns_remaining -= 1
            return self.turns_remaining <= 0
        return False
    
    def is_expired(self):
        """Check if the tilt has expired"""
        if self.turns_remaining is None:
            return False
        return self.turns_remaining <= 0
    
    def to_dict(self):
        """Convert tilt to a dictionary for storage"""
        return {
            'name': self.name,
            'description': self.description,
            'tilt_type': self.tilt_type,
            'duration': self.duration,
            'effects': self.effects,
            'resolution_method': self.resolution_method,
            'condition_equivalent': self.condition_equivalent,
            'applied_at': self.applied_at.isoformat(),
            'turns_remaining': self.turns_remaining
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a tilt from a dictionary"""
        tilt = cls(
            name=data['name'],
            description=data['description'],
            tilt_type=data['tilt_type'],
            duration=data['duration'],
            effects=data['effects'],
            resolution_method=data['resolution_method'],
            condition_equivalent=data.get('condition_equivalent')
        )
        tilt.applied_at = datetime.fromisoformat(data['applied_at'])
        tilt.turns_remaining = data.get('turns_remaining')
        return tilt

class TiltHandler:
    """
    A handler for managing tilts on characters during combat.
    """
    def __init__(self, obj):
        self.obj = obj
        self._tilts = {}
        self._load_tilts()
    
    def _load_tilts(self):
        """Load tilts from the object's attributes"""
        tilts_data = self.obj.attributes.get('combat_tilts', default={})
        for name, data in tilts_data.items():
            try:
                self._tilts[name] = Tilt.from_dict(data)
            except Exception as e:
                logger.error(f"Error loading tilt {name}: {e}")
    
    def _save_tilts(self):
        """Save tilts to the object's attributes"""
        tilts_data = {name: tilt.to_dict() 
                     for name, tilt in self._tilts.items()}
        self.obj.attributes.add('combat_tilts', tilts_data)
    
    def add(self, tilt):
        """Add a tilt to the object"""
        self._tilts[tilt.name] = tilt
        self._save_tilts()
        self.obj.msg(f"You are affected by the tilt: {tilt.name}")
    
    def remove(self, tilt_name):
        """Remove a tilt from the object"""
        if tilt_name in self._tilts:
            tilt = self._tilts[tilt_name]
            del self._tilts[tilt_name]
            self._save_tilts()
            self.obj.msg(f"You are no longer affected by the tilt: {tilt_name}")
            
            # Check if this tilt should become a condition outside combat
            if tilt.condition_equivalent and not self._is_in_combat():
                self._convert_to_condition(tilt)
            return True
        return False
    
    def get(self, tilt_name):
        """Get a specific tilt"""
        return self._tilts.get(tilt_name)
    
    def all(self):
        """Get all tilts"""
        return list(self._tilts.values())
    
    def personal_tilts(self):
        """Get all personal tilts"""
        return [tilt for tilt in self._tilts.values() if tilt.tilt_type == "personal"]
    
    def advance_turn(self):
        """Advance all tilts by one turn and remove expired ones"""
        expired = []
        for name, tilt in list(self._tilts.items()):
            if tilt.advance_turn():
                expired.append(name)
                self.remove(name)
        return expired
    
    def has(self, tilt_name):
        """Check if object has a specific tilt"""
        return tilt_name in self._tilts
    
    def clear_all(self):
        """Clear all tilts (when leaving combat)"""
        for tilt_name in list(self._tilts.keys()):
            self.remove(tilt_name)
    
    def _is_in_combat(self):
        """Check if the object is currently in combat"""
        return hasattr(self.obj.location, 'combat_tracker') and \
               self.obj in self.obj.location.combat_tracker.participants
    
    def _convert_to_condition(self, tilt):
        """Convert a tilt to its equivalent condition"""
        if tilt.condition_equivalent:
            # Import here to avoid circular imports
            from world.conditions import STANDARD_CONDITIONS
            
            if tilt.condition_equivalent in STANDARD_CONDITIONS:
                condition = STANDARD_CONDITIONS[tilt.condition_equivalent]
                self.obj.conditions.add(condition)
                self.obj.msg(f"The tilt {tilt.name} has become the condition {condition.name}")

class EnvironmentalTiltHandler:
    """
    A handler for managing environmental tilts that affect an entire combat scene.
    """
    def __init__(self, location):
        self.location = location
        self._tilts = {}
        self._load_tilts()
    
    def _load_tilts(self):
        """Load environmental tilts from the location's attributes"""
        tilts_data = self.location.attributes.get('environmental_tilts', default={})
        for name, data in tilts_data.items():
            try:
                self._tilts[name] = Tilt.from_dict(data)
            except Exception as e:
                logger.error(f"Error loading environmental tilt {name}: {e}")
    
    def _save_tilts(self):
        """Save environmental tilts to the location's attributes"""
        tilts_data = {name: tilt.to_dict() 
                     for name, tilt in self._tilts.items()}
        self.location.attributes.add('environmental_tilts', tilts_data)
    
    def add(self, tilt):
        """Add an environmental tilt to the location"""
        self._tilts[tilt.name] = tilt
        self._save_tilts()
        self.location.msg_contents(f"The area is affected by: {tilt.name}")
    
    def remove(self, tilt_name):
        """Remove an environmental tilt from the location"""
        if tilt_name in self._tilts:
            del self._tilts[tilt_name]
            self._save_tilts()
            self.location.msg_contents(f"The area is no longer affected by: {tilt_name}")
            return True
        return False
    
    def get(self, tilt_name):
        """Get a specific environmental tilt"""
        return self._tilts.get(tilt_name)
    
    def all(self):
        """Get all environmental tilts"""
        return list(self._tilts.values())
    
    def advance_turn(self):
        """Advance all environmental tilts by one turn and remove expired ones"""
        expired = []
        for name, tilt in list(self._tilts.items()):
            if tilt.advance_turn():
                expired.append(name)
                self.remove(name)
        return expired
    
    def has(self, tilt_name):
        """Check if location has a specific environmental tilt"""
        return tilt_name in self._tilts
    
    def clear_all(self):
        """Clear all environmental tilts (when combat ends)"""
        for tilt_name in list(self._tilts.keys()):
            self.remove(tilt_name)

# Dictionary of standard tilts
STANDARD_TILTS = {
    # Personal Tilts
    'arm_wrack': Tilt(
        name="Arm Wrack",
        description="Your arm burns with pain and then goes numb. It could be dislocated, sprained, or broken, but whatever's wrong with it means you can't move your limb.",
        tilt_type="personal",
        effects="You drop whatever you're holding in that arm and can't use it to attack opponents. Unless you have the Ambidextrous Merit, you suffer off-hand penalties for any rolls that require manual dexterity. If both arms are affected, you're down to a chance die on any rolls that require manual dexterity, and -3 to all other Physical actions.",
        resolution_method="If the Tilt is inflicted as a result of an attack, mark an X under the leftmost Health box affected by that attack. The Tilt ends when the damage that caused it has healed. If the damage that inflicts this Tilt is aggravated, the character loses the use of his arm (or completely loses his arm) permanently. Caused by: A targeted blow to the arm (-2 penalty) that deals more damage than the character's Stamina, or a targeted blow to the hand that does any damage.",
        condition_equivalent="disabled_persistent"
    ),
    'beaten_down': Tilt(
        name="Beaten Down", 
        description="The character has had the fight knocked out of him.",
        tilt_type="personal",
        effects="The character cannot take active part in the fight without extra effort. The player must spend a point of Willpower each time he wants the character to take a violent action in the fight. He can still run, Dodge, and apply Defense. The Storyteller should judge whether the action is aggressive enough to require the expenditure.",
        resolution_method="The character surrenders and gives the aggressor what he wants. At this point, the character regains a point of Willpower and takes a Beat, but can take no further action in the fight. Caused by: The character suffers bashing damage in excess of his Stamina or any amount of lethal damage.",
        condition_equivalent="humbled"
    ),
    'blinded': Tilt(
        name="Blinded",
        description="The character's eyes are damaged or removed.",
        tilt_type="personal", 
        effects="The character suffers a -3 penalty to any rolls that rely on vision - including attack rolls - and halves his Defense if one eye is blinded. That penalty increases to -5 and loss of all Defense if both eyes are affected.",
        resolution_method="If an attack against the character's eye does any points of damage, mark an X under the leftmost Health box affected by that attack. If the damage inflicted is aggravated the character loses vision in that eye permanently. Otherwise, the condition ends when the damage that caused the Tilt is healed. Caused by: Damage to the eyes (specified attack with -5 penalty), or temporary blindness from Dexterity + Athletics -3 (slashing brow, throwing sand, kicking up dirt).",
        condition_equivalent="blind"
    ),
    'deafened': Tilt(
        name="Deafened",
        description="The character can't hear. Maybe he's suffering intense tinnitus, can only hear the roaring of blood in his ears, or has been deafened by a gunshot.",
        tilt_type="personal",
        effects="If the character is deaf in one ear, he suffers a -3 penalty to hearing-based Perception rolls. A character who is struck deaf in both ears only gets a chance die on hearing-based Perception rolls, and suffers a -2 penalty to all combat-related dice rolls - suddenly losing the ability to hear the people around you is tremendously disorienting.",
        resolution_method="Deafness caused by loud noises fades after (10 - the victim's Stamina + Resolve) turns. If an attack against the character's ear does any points of damage, mark an X under the leftmost Health box affected by that attack. If the damage inflicted is Aggravated the character loses hearing in the ear permanently. Otherwise, the condition ends when the damage that caused the Tilt is healed. Caused by: Loud noises within 10 feet or targeted attack on ear (-4 penalty)."
    ),
    'drugged': Tilt(
        name="Drugged",
        description="The character's mind is addled by mind-altering substances, such as alcohol or drugs.",
        tilt_type="personal",
        effects="A generic narcotic can be represented with one set of modifiers: the character suffers a -2 modifier to Speed (and static Defense, if used) and a -3 penalty to all rolls in combat, including Defense and Perception. The character also ignores wound penalties.",
        resolution_method="A generic narcotic lasts for (10 - the victim's Stamina + Resolve) hours. Medical help, such as pumping the victim's stomach or flushing his system, halves this time. Caused by: Voluntary drug use or Dexterity + Weaponry attack with -1 modifier for improvised weapon.",
        condition_equivalent="intoxicated"
    ),
    'immobilized': Tilt(
        name="Immobilized",
        description="Something holds the character fast, preventing him from moving. This could be a grappling opponent, a straightjacket wrapped with heavy chains, or a coffin secured on the outside with a padlock.",
        tilt_type="personal",
        effects="The character can't do anything but wriggle helplessly. He can't apply Defense against incoming attacks, and can't take combat-related actions. If someone's holding him down, he can spend a point of Willpower to deliver a head butt or similar attack, but even that might not free him.",
        resolution_method="An Immobilized target can break free by escaping from a grapple or snapping whatever binds her. If grappled, the character can struggle as normal but can only select the Break Free move on a success. If held by an item, the character must make a Strength + Athletics roll penalized by the item's Durability. If a character's arms and legs are both bound, he suffers a -2 penalty; this increases to -4 if he's hogtied. Each roll, successful or not, deals a point of bashing damage. Caused by: Restrain grappling move or being bound/trapped."
    ),
    'insane': Tilt(
        name="Insane",
        description="The character suffers from a panic attack, sudden imbalance, or a full-on psychotic break. Her pulse races, her mind cannot focus on what she wants. The world's an unstable place, and she's unable to keep her balance.",
        tilt_type="personal",
        effects="Someone suffering a psychotic break isn't the sort of person to go down without a fight. Her stated intent might be irrational or just plain impossible, and she might have fewer ethical problems with using extreme violence to get what she wants. The character gains a +1 bonus to all combat rolls, but takes actions after everyone else (if two characters suffer from the Insane Tilt, both act after everyone else but compare Initiative as normal). A character suffering from this Tilt cannot spend Willpower in combat, and suffers a -3 penalty to all Social rolls.",
        resolution_method="The specific effects of this Tilt don't normally last beyond the end of the scene. A character can try to force her mind to a state of balance by sitting and focusing. She rolls Resolve + Composure as an instant action, contested by a dice pool of (10 - her Willpower). She can't take any other actions that turn, and doesn't apply Defense. Caused by: Witnessing horrific events, failed Resolve + Composure roll when facing extraordinary circumstances, orchestrated psychological manipulation, or supernatural mind-affecting powers.",
        condition_equivalent="madness_persistent"
    ),
    'insensate': Tilt(
        name="Insensate",
        description="The character shuts down, either due to extreme fear or sudden pleasure. He may huddle in a corner, cringe away from sudden noises, or stare into space as waves of pleasure lap over him.",
        tilt_type="personal",
        effects="The character can't take any actions until the Tilt is resolved. He can apply Defense to incoming attacks, and if he takes any damage from an attack, he's knocked free of whatever fogged his brain.",
        resolution_method="The Tilt wears off at the end of the scene. The victim can spend a point of Willpower before then to act normally for one turn. A successful attack will also end the Tilt. If a character has been knocked insensible by drugs, then when this Tilt ends it is replaced with the Drugged Tilt. Caused by: Supernatural powers (vampire mind tricks, werewolf terror), extreme amounts of alcohol or hallucinogenic drugs (Dexterity + Weaponry -1 to administer)."
    ),
    'knocked_down': Tilt(
        name="Knocked Down",
        description="Something knocks the character to the floor, either toppling her with a powerful blow to the chest or taking one of her legs out from under her.",
        tilt_type="personal",
        effects="The character is knocked off her feet. If she hasn't already acted this turn, she loses her action. Once she's on the ground, a character is considered prone. The character can still apply Defense against incoming attacks, and can attempt to attack from the ground at a -2 penalty.",
        resolution_method="The easiest way to end this Tilt is to stand up, which takes an action. A character who hasn't yet acted can make a Dexterity + Athletics roll, minus any weapon modifier, instead of her normal action. If successful, she avoids the effects of this Tilt altogether. Caused by: Melee weapon with +2 damage or firearm with +3 damage, or targeted attack against legs (-2 modifier) that halves total damage."
    ),
    'leg_wrack': Tilt(
        name="Leg Wrack", 
        description="Your leg feels like it's going to snap clean off whenever you move; when you stop moving you feel a burning numbness that encourages you to avoid action.",
        tilt_type="personal",
        effects="If your leg is broken, sprained, or dislocated, halve your Speed and suffer a -2 penalty on Physical rolls that require movement (and Defense). If both of your legs are wracked, you fall over - taking the Knocked Down Tilt - and cannot get up. Your Speed is reduced to 1; if you want to move at all, you cannot take any other action. Physical rolls that require movement are reduced to a chance die.",
        resolution_method="If the Tilt is inflicted as a result of an attack, mark an X under the leftmost Health box affected by that attack. The Tilt ends when that damage that caused it has healed. If the damage that inflicts this Tilt is aggravated, the character loses use of his leg permanently. Caused by: A targeted blow to the leg (-2 penalty) that deals more damage than the character's Stamina.",
        condition_equivalent="crippled_persistent"
    ),
    'poisoned': Tilt(
        name="Poisoned",
        description="You've got poison inside you. It's tearing you apart from the inside, burning like acid in your gut and making your head swim.",
        tilt_type="personal",
        effects="This Tilt applies a general sense of being poisoned to a character without worrying about Toxicity during combat. For the purposes of this Tilt, a poison is either 'moderate' or 'grave' - a moderate poison causes one point of bashing damage per turn of combat, while a grave poison ups that to one point of lethal damage per turn. If the Storyteller cares to continue the effects of the poison outside of combat, he can apply the standard rules for handling poisons and toxins when combat is complete.",
        resolution_method="Short of immediate medical attention, all a victim can do is struggle on. Roll Stamina + Resolve as a reflexive action each turn that your character is poisoned. If your character intends to act (takes a non-reflexive action), the roll suffers a -3 penalty. Success counteracts the damage for one turn only. Caused by: Injection via Dexterity + Weaponry attack with -1 modifier for improvised weapon, environmental exposure, or ingestion."
    ),
    'sick': Tilt(
        name="Sick",
        description="Your stomach churns. You retch and heave but only succeed in bringing up bile. Sweat beads on your brow as you spike a fever. Your muscles ache with every movement. You're wracked with hot and cold flushes as a sickness gnaws away at your insides.",
        tilt_type="personal",
        effects="This Tilt applies a general sickness to a character without worrying about the specific illness. For the purposes of this Tilt, a sickness is either 'moderate' or 'grave.' A moderate sickness, such as a cold, asthma, the flu, or just a bad hangover, causes a -1 penalty to all actions during combat. That penalty increases by one every two turns (the first two turns, the character suffers a -1 penalty, the next two turns the penalty is -2, and so on up to a maximum of -5 on turn nine). A grave sickness, such as pneumonia, heavy metal poisoning, or aggressive cancer, inflicts the same dice penalties as a mild sickness. In addition, the physical stress of fighting or even defending oneself from an attacker while gravely ill inflicts a point of bashing damage per turn of combat.",
        resolution_method="This Tilt reflects the effects of sickness as they specifically applies to combat. The penalties inflicted by this Tilt fade at a rate of one point per turn once the character has a chance to rest, but any damage inflicted remains until the character can heal. Caused by: Deliberate exposure to disease, supernatural abilities, or pre-existing illness.",
        condition_equivalent="deprived"
    ),
    'stunned': Tilt(
        name="Stunned",
        description="Your character is dazed and unable to think straight. Maybe her vision blurs. If she's stunned as a result of a blow to the head, she's probably got a concussion.",
        tilt_type="personal",
        duration=1,
        effects="A character with the Stunned Tilt loses her next action, and halves her Defense until she can next act.",
        resolution_method="The effects of this Tilt normally only last for a single turn. The character can end the Tilt during her own action by reflexively spending a point of Willpower to gather her wits, though she suffers a -3 modifier to any actions she takes that turn. Caused by: Any attack that targets the head and deals at least as much damage as her Size. Weapons with 'stun' special ability double the weapon modifier for determining this. Attacks to the head count Size as one lower."
    ),
    
    # Environmental Tilts
    'blizzard': Tilt(
        name="Blizzard",
        description="Heavy snowfall carpets the ground and is whipped up by howling winds into a barrage of whirling white.",
        tilt_type="environmental",
        effects="Blizzards make it very hard to see for any real distance. Rolls to see things close to the character's person, out to an arm's length away, suffer a -1 penalty. Each additional 10 yards inflicts an additional -1 penalty (cumulative) on all visual Perception rolls. This penalty also applies to ranged attack rolls. Moving through snow is difficult. Every four inches of snow applies a -1 penalty to appropriate Physical rolls, including combat rolls, Athletics, and the like. The Blizzard Tilt rarely applies by itself - the Storyteller may also inflict any or all of the Extreme Cold, Heavy Winds, or Ice Tilts.",
        resolution_method="Without supernatural powers, characters can't end a blizzard. The best they can manage is to escape the weather or wait for it to stop. Proper equipment (such as goggles and snow boots) can add +1 to +3 to a roll, offsetting some of the penalties. If someone is causing this Tilt through a supernatural power, it's possible that the characters could disrupt his concentration."
    ),
    'earthquake': Tilt(
        name="Earthquake",
        description="Everything shudders and shakes, and rents tear the ground wide open.",
        tilt_type="environmental",
        duration=20,  # max 20 turns (1 minute)
        effects="Earthquakes don't last long, but they don't have to. When the earthquake's actually occurring, all Dexterity-based dice pools (and Defense) suffer a -1 to -5 penalty, depending on the earthquake's severity. Characters take between one and three points of lethal damage per turn of the earthquake's duration, though a reflexive Stamina + Athletics roll can downgrade that damage to bashing - or cancel it entirely on an exceptional success.",
        resolution_method="Earthquakes are, fortunately, very quick events. It's very rare for one to last more than a minute (20 turns), so waiting them out is the best course of action. Caused by: Natural seismic activity or tremendous supernatural power."
    ),
    'extreme_cold': Tilt(
        name="Extreme Cold",
        description="Bone-chilling winds bite through the character, or trudging through knee-deep snow takes all of the sensation from his limbs. Any time the temperature gets down below zero degrees Celsius (32 degrees Fahrenheit), a character can suffer from the cold's effects. This Tilt can sometimes be personal, as a result of a medical condition like hypothermia or a supernatural power.",
        tilt_type="environmental",
        effects="When the temperature is below freezing, characters can't heal bashing damage - the extreme temperature deals damage at the same rate normal characters heal it (a cut might turn to frostbite, for instance). Supernatural beings and characters who heal faster than normal instead halve their normal healing rate. For every hour that a character is continuously affected by this Tilt, he accrues a -1 penalty to all rolls. When that penalty hits -5, he instead suffers a point of lethal damage per hour.",
        resolution_method="The best way to escape the freezing cold is to find a source of warmth, either a building with working heat, or warm clothing. A character who has hypothermia requires medical attention. Caused by: Being in a frozen environment (Arctic tundra, walk-in freezer, etc.) or being thrown into a freezing lake."
    ),
    'extreme_heat': Tilt(
        name="Extreme Heat", 
        description="The character might be stumbling through the desert with the sun beating down on him, or running through the steam tunnels surrounding an old boiler room. This Tilt can also be personal, the result of a debilitating fever that spikes his temperature far above the norm. Extreme heat is normally anything above 40 degrees Celsius (104 degrees Fahrenheit), whether internal or external.",
        tilt_type="environmental",
        effects="When the temperature is far above normal, characters can't heal bashing damage - the extreme temperature deals damage at the same rate normal characters heal it (a cut might heal, but it's replaced by sunburn or sunstroke). Supernatural beings and characters who heal faster than normal instead halve their normal healing rate. For every hour that a character is continuously affected by this Tilt, he accrues a -1 penalty to all rolls. When that penalty hits -5, he instead suffers a point of lethal damage per hour.",
        resolution_method="The key to ending this Tilt is simple: get out of the heat. In a desert or similar environment, finding shade is paramount. Elsewhere, the character needs to escape whatever is causing the abnormal temperatures. Caused by: Environmental factors (desert at noon, sauna, forge) or fever from infection."
    ),
    'flooded': Tilt(
        name="Flooded",
        description="Some liquid - brackish water, mud, gore, or raw sewage - has risen enough to impede the character's progress.",
        tilt_type="environmental",
        effects="Each foot of liquid inflicts a -2 penalty to all Physical dice pools. If the water goes up over her head, the character has to swim (Dexterity + Athletics), with a penalty appropriate for the speed of the flooding. Alternatively, she can try to hold her breath (Stamina + Composure) if she cannot get her head above the rising waters.",
        resolution_method="Characters can escape flooding by getting to high ground, which is enough to mitigate this Tilt. A long-term fix would require draining the floodwaters, but each flood requires its own solution. Caused by: Heavy rain, sudden snowmelt, broken water main, smashing up a water heater, blowing up a small dam, or supernatural effects."
    ),
    'heavy_rain': Tilt(
        name="Heavy Rain",
        description="Torrential rain lashes down in knives, bouncing high off the sidewalk. The sound of rain on the ground is a constant hammering rumble that goes on without end, like dropping ball bearings on a tin roof. Thick gray curtains of water obscure vision.",
        tilt_type="environmental",
        effects="Heavy rains - approaching tropical storm levels or worse - cause a Perception penalty of -3 dice to both vision and hearing. Rain's hard to see through, but it's also loud. If the rains carry on for an hour or more, the Flooded Tilt will soon follow. This Tilt is often accompanied by Heavy Winds; a character trapped out in Heavy Rains might come under the effects of Extreme Cold.",
        resolution_method="The best way out of the rain is to get indoors. Unless it's the start of some sodden apocalypse, the characters can wait for the weather to ease. Caused by: Natural weather patterns or supernatural powers (cloud-seeding aircraft)."
    ),
    'heavy_winds': Tilt(
        name="Heavy Winds",
        description="Howling winds buffet at the characters, whipping street furniture into the air and tearing the roofs from buildings. Powerful winds can toss cars around like toys. Anyone out in the winds feels like they're taking a beating just walking down the street.",
        tilt_type="environmental", 
        effects="Heavy winds are loud, so characters suffer a -3 modifier to aural Perception rolls. Also, the wind inflicts a penalty to all Physical rolls when out in the winds, including Drive rolls. Grade the wind from one to five; one is tropical-storm level (around 40 MPH), three is hurricane level (around 80 MPH), and five is tornado level (150+ MPH). The wind's grade represents the penalty applied to Physical dice rolls. Characters outside in the maelstrom also take damage from flying debris, taking bashing damage each turn equal to the wind's rating. Characters can make a reflexive Dexterity + Athletics roll to avoid damage.",
        resolution_method="Getting out of the wind is the best way to end this Tilt. Sometimes that's as easy as sheltering in an automobile, as long as nobody tries to drive. Buildings provide more permanent shelter. Caused by: Natural weather (siroccos, tornados, wind shears)."
    ),
    'ice': Tilt(
        name="Ice",
        description="The ground's covered in a mirror-smooth layer of ice that sends wheels spinning and people's feet flying out from under them. The ice can be so thin as to be nearly invisible, or it can be a thick layer that's the only thing keeping the characters from sinking into a frozen lake.",
        tilt_type="environmental",
        effects="When a character can't trust her footing, divide her Speed in half, and all Physical rolls (and Defense) suffer a -2 penalty. Attempting to move at full Speed increases the Physical penalty to -4. Any dramatic failure on a Physical roll inflicts the Knocked Down Tilt. Driving on ice is a real pain; halve Acceleration, and characters suffer a -5 penalty to Drive rolls.",
        resolution_method="Characters can use heat or fire to melt ice, or throw down copious quantities of salt or grit to increase traction. This Tilt doesn't just apply to icy conditions, but to any surface that's slick and slippery, including a spill of industrial lubricant or just a well-polished wooden or linoleum floor. Characters can use a Dexterity + Crafts roll to cover an area in industrial cleaner or mix up chemicals into a lubricant. If the Extreme Cold Tilt is in effect, even covering the area with water will do the trick."
    )
} 