from evennia.utils.utils import lazy_property
from evennia.typeclasses.attributes import AttributeProperty
from evennia.utils.dbserialize import dbserialize, dbunserialize
from evennia.utils import logger
from datetime import datetime, timedelta

class Condition:
    """
    A class representing a condition that can be applied to characters.
    """
    def __init__(self, name, description, duration=None, is_persistent=False, 
                 effects=None, resolution_method=None, possible_sources=None, beat=None):
        self.name = name
        self.description = description
        self.duration = duration  # None for permanent, timedelta for temporary
        self.is_persistent = is_persistent
        self.effects = effects or {}  # Dictionary of effects this condition applies
        self.resolution_method = resolution_method  # How this condition can be resolved
        self.possible_sources = possible_sources  # Possible sources of this condition
        self.beat = beat  # Beat information for this condition
        self.applied_at = datetime.now()
        
    def is_expired(self):
        """Check if the condition has expired"""
        if self.duration is None or self.is_persistent:
            return False
        return datetime.now() > (self.applied_at + self.duration)
    
    def to_dict(self):
        """Convert condition to a dictionary for storage"""
        return {
            'name': self.name,
            'description': self.description,
            'duration': self.duration.total_seconds() if self.duration else None,
            'is_persistent': self.is_persistent,
            'effects': self.effects,
            'resolution_method': self.resolution_method,
            'possible_sources': self.possible_sources,
            'beat': self.beat,
            'applied_at': self.applied_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a condition from a dictionary"""
        condition = cls(
            name=data['name'],
            description=data['description'],
            duration=timedelta(seconds=data['duration']) if data['duration'] else None,
            is_persistent=data['is_persistent'],
            effects=data.get('effects'),
            resolution_method=data.get('resolution_method'),
            possible_sources=data.get('possible_sources'),
            beat=data.get('beat')
        )
        condition.applied_at = datetime.fromisoformat(data['applied_at'])
        return condition

class ConditionHandler:
    """
    A handler for managing conditions on characters.
    """
    def __init__(self, obj):
        self.obj = obj
        self._conditions = {}
        self._load_conditions()
    
    def _load_conditions(self):
        """Load conditions from the object's attributes"""
        conditions_data = self.obj.attributes.get('conditions', default={})
        for name, data in conditions_data.items():
            try:
                self._conditions[name] = Condition.from_dict(data)
            except Exception as e:
                logger.error(f"Error loading condition {name}: {e}")
    
    def _save_conditions(self):
        """Save conditions to the object's attributes"""
        conditions_data = {name: condition.to_dict() 
                          for name, condition in self._conditions.items()}
        self.obj.attributes.add('conditions', conditions_data)
    
    def add(self, condition):
        """Add a condition to the object"""
        self._conditions[condition.name] = condition
        self._save_conditions()
        self.obj.msg(f"You have gained the condition: {condition.name}")
    
    def remove(self, condition_name):
        """Remove a condition from the object"""
        if condition_name in self._conditions:
            del self._conditions[condition_name]
            self._save_conditions()
            self.obj.msg(f"You have lost the condition: {condition_name}")
            return True
        return False
    
    def get(self, condition_name):
        """Get a specific condition"""
        return self._conditions.get(condition_name)
    
    def all(self):
        """Get all conditions"""
        return list(self._conditions.values())
    
    def check_expired(self):
        """Check and remove expired conditions"""
        expired = [name for name, condition in self._conditions.items() 
                  if condition.is_expired()]
        for name in expired:
            self.remove(name)
        return expired
    
    def has(self, condition_name):
        """Check if object has a specific condition"""
        return condition_name in self._conditions

# Dictionary of standard conditions
STANDARD_CONDITIONS = {
    # Temporary Conditions
    'an_eye_for_disorder': Condition(
        name="An Eye For Disorder",
        description="",
        is_persistent=False
    ),
    'angel_empathy': Condition(
        name="Angel Empathy",
        description="",
        is_persistent=False
    ),
    'atavism': Condition(
        name="Atavism",
        description="You suffer ancient, ancestral memories that rouse anger and violent urges; the cause of these memories must be destroyed.",
        is_persistent=False
    ),
    'ban': Condition(
        name="Ban",
        description="Your character suffers from a powerful spiritual compulsion that demands specific behavior.",
        is_persistent=False
    ),
    'berserk': Condition(
        name="Berserk",
        description="Your character has had a spark of berserk rage lit within her.",
        is_persistent=False
    ),
    'bestial': Condition(
        name="Bestial",
        description="Your character acts on primal, physical impulses. Frightening things make him run. He meets aggressive threats with violence and anger. Take a –2 die penalty to all rolls to resist frenzy or physical impulse. As well, take a –2 die penalty to Defense due to impulsive action. Any rolls to compel your character to impulsive, aggressive action or escape achieve exceptional success on three successes instead of five. This could apply to Disciplines such as Nightmare, or Dominate under the right circumstances.\n\nThis Condition fades naturally after a number of nights equal to the Blood Potency of the vampire who caused it. In the case of the predatory aura, this is the vampire who won the conflict. In the case of testing for detachment, this is the vampire's own Blood Potency.\n\nAfter resolving Bestial, your character cannot be subject to this Condition again for a full month.",
        is_persistent=False,
        possible_sources="A monstrous predatory aura conflict, facing a breaking point.",
        beat="n/a",
        resolution_method="Cause damage in someone's last three Health boxes."
    ),
    'blackballed': Condition(
        name="Blackballed",
        description="Your character has been ostracized from a social group.",
        is_persistent=False
    ),
    'bonded': Condition(
        name="Bonded",
        description="Your character has bonded with an animal, granting a bonus on interactions with it.",
        is_persistent=False
    ),
    'captivated': Condition(
        name="Captivated",
        description="Your character is enthralled by something or someone.",
        is_persistent=False
    ),
    'competitive': Condition(
        name="Competitive",
        description="Your character must assert dominance and superiority. Either she gives it her all, or she falters. Any time she's in direct competition with another character, she suffers a –2 die penalty on any rolls where she doesn't spend Willpower. This includes contested and extended rolls. As well, any rolls to tempt or coerce her into competition achieve exceptional success on three successes instead of five.\n\nThis Condition fades naturally after a number of nights equal to the Blood Potency of the vampire who caused it. In the case of the predatory aura, this is the vampire who won the conflict. In the case of testing for detachment, this is the vampire's own Blood Potency.\n\nAfter resolving Competitive, your character cannot be subject to this Condition again for a full month.",
        is_persistent=False,
        possible_sources="A challenging predatory aura conflict, facing a breaking point.",
        beat="n/a",
        resolution_method="Win or lose a competition where someone reaches a breaking point."
    ),
    'confused': Condition(
        name="Confused",
        description="Your character cannot think straight, either because of some mental power or good old-fashioned cranial trauma. You take a –2 die penalty on all Intelligence and Wits rolls.",
        is_persistent=False,
        possible_sources="A blow to the head, dramatic failure when using some Auspex powers.",
        beat="n/a",
        resolution_method="Take half an hour to focus and clear your mind. Take any amount of lethal damage."
    ),
    'cowed': Condition(
        name="Cowed",
        description="Your character has been put in her place through the violence and dominance of another.",
        is_persistent=False
    ),
    'cunning': Condition(
        name="Cunning",
        description="Your character is Cunning. She beguiles, tricks, sneaks and charms.",
        is_persistent=False
    ),
    'delusion': Condition(
        name="Delusion",
        description="Your character cannot make sense of the world she perceives, and because of this, she avoids that which would make her question.",
        is_persistent=False
    ),
    'demoralized': Condition(
        name="Demoralized",
        description="Your character is demoralized and hesitant in the face of the enemy.",
        is_persistent=False
    ),
    'deprived': Condition(
        name="Deprived",
        description="Your character suffers from an addiction. She is unable to get her fix, however, leaving her irritable, anxious, and unable to focus. Remove one from her Stamina, Resolve, and Composure dice pools. This does not influence derived traits; it only influences dice pools that use these Attributes.",
        is_persistent=False,
        possible_sources="Your character is Addicted but cannot get a fix.",
        beat="n/a",
        resolution_method="Your character indulges her addiction."
    ),
    'despondent': Condition(
        name="Despondent",
        description="Your character feels the hunter's approach in his blood and in his bones, and its only a matter of time before death claims him.",
        is_persistent=False
    ),
    'disoriented': Condition(
        name="Disoriented",
        description="Your character has lost their sense of direction and balance.",
        is_persistent=False
    ),
    'distracted': Condition(
        name="Distracted",
        description="Constant confusion and distractions buffet your character from all sides. She cannot take extended actions, and suffers a –2 die penalty to all rolls involving perception, concentration, and precision.\n\nThis Condition does not grant a Beat when resolved.",
        is_persistent=False,
        possible_sources="Being in a swarm.",
        beat="n/a",
        resolution_method="Leaving the swarm."
    ),
    'dominated': Condition(
        name="Dominated",
        description="A vampire has given your character a specific command that she cannot go against. You don't have a choice whether or not to follow the command — your will is no longer your own. If your task has a natural end, such as \"Follow that man until he enters an apartment then call me with the address,\" you resolve the Condition once you complete it; otherwise it ends at sunrise. Once you resolve this Condition, you can't quite remember what happened while you were under the vampire's spell.",
        is_persistent=False,
        possible_sources="The Dominate Discipline.",
        beat="n/a",
        resolution_method="Take more bashing or lethal damage than your Stamina. Experience a breaking point when following the command, and succeed at the related Resolve + Composure roll. Follow the vampire's command."
    ),
    'drained': Condition(
        name="Drained",
        description="Your character has been fed from extensively, and suffers from blood loss. He suffers a –2 die penalty to any physical actions, and rolls to stabilize and survive injuries. As well, after any scene where he exerts himself physically, he must make a Stamina roll or fall unconscious for an hour or more. The Drained penalty does not apply to the Stamina roll, but any wound penalties do apply. Taking damage, being fed from, or spending Willpower on a physical roll applies as physical exertion for this Condition.",
        is_persistent=False,
        possible_sources="A vampire's feeding.",
        beat="n/a",
        resolution_method="All lethal damage healed through normal means."
    ),
    'easy_prey': Condition(
        name="Easy Prey",
        description="Through carelessness or ignorance, your character leaves a clear trail for any hunter to follow.",
        is_persistent=False
    ),
    'ecstatic': Condition(
        name="Ecstatic",
        description="Your Beast has been temporarily sated through the use of blood sorcery. For as long as the Beast is quiet, the character may feed as though her Blood Potency were three dots less than her rating (minimum one), and has a +2 die bonus to avoid frenzy.",
        is_persistent=False,
        possible_sources="Exceptional success on a Crúac ritual.",
        beat="n/a",
        resolution_method="Feeding, sleeping, or resisting a frenzy."
    ),
    'embarrassing_secret': Condition(
        name="Embarrassing Secret",
        description="Your character has a secret that could come back to haunt him. If the secret is let out, this Condition becomes the Notoriety Condition.",
        is_persistent=False
    ),
    'enraptured': Condition(
        name="Enraptured",
        description="Your character has witnessed divinity and feels the madness of faith deep within his soul.",
        is_persistent=False
    ),
    'ergi': Condition(
        name="Ergi",
        description="Your character has been accused of being unmanly, or of passive homosexuality. In Viking culture, this is a grave insult. He has until the next Thing meets to kill his accuser or face him in a duel.",
        is_persistent=False
    ),
    'essence_overload': Condition(
        name="Essence Overload",
        description="Your character has attempted to channel immensely powerful forces through her Essence, and has lost control.",
        is_persistent=False
    ),
    'euphoric': Condition(
        name="Euphoric",
        description="Your character glimpsed Rabid Wolf's radiant madness and understands his role as prey in the hunt.",
        is_persistent=False
    ),
    'exhausted': Condition(
        name="Exhausted",
        description="Your character has been run ragged and desperately needs a good rest.",
        is_persistent=False
    ),
    'flagged': Condition(
        name="Flagged",
        description="Your character has been marked for special attention.",
        is_persistent=False
    ),
    'frantic': Condition(
        name="Frantic",
        description="Your character has glimpsed the passion Rabid Wolf embodies with his every moment. He will put his full effort into every action until exhausted, as Gurim-Ur demands nothing less.",
        is_persistent=False
    ),
    'frightened': Condition(
        name="Frightened",
        description="Something's scared you to the point where you lose rational thought. Maybe you've just looked down at a hundred-story drop, or seen a tarantula the size of your fist crawling up your leg. Whatever the case, you need to leave right now. Your only priority is getting the fuck away from the thing that's frightened you — the hell with your stuff, your friends, and your allies. If someone tries to stop you from escaping, you'll fight your way past them. You can't approach the source of your fear or act against it — and if the only way out involves going near the source of your fear, you'll collapse on the ground in terror.\n\nSupernatural creatures prone to loss of control, including vampires, must roll to avoid frenzy. This Condition lasts until the end of the scene; suppressing its effects for a turn costs a point of Willpower.",
        is_persistent=False,
        possible_sources="The Nightmare Discipline, coming face to face with a phobia.",
        beat="n/a",
        resolution_method="The character escapes from the source of his fear."
    ),
    'futuristic_visionary': Condition(
        name="Futuristic Visionary",
        description="New technologies and tales of scientific marvels galvanize your character into a flurry of inventiveness.",
        is_persistent=False
    ),
    'glorious': Condition(
        name="Glorious",
        description="Your character is Glorious. She's faced down superior opponents, committed great acts of courage, and lived to tell the tale.",
        is_persistent=False
    ),
    'guilty': Condition(
        name="Guilty",
        description="Your character is experiencing deep-seated feelings of guilt and remorse. This Condition is commonly applied after a successful detachment roll, p. 108. While the character is under the effects of this Condition, he receives a –2 die penalty to any Resolve or Composure rolls to defend against Subterfuge, Empathy, or Intimidation rolls.",
        is_persistent=False,
        possible_sources="Encountering a breaking point, some Ghoul Merits.",
        beat="n/a",
        resolution_method="The character confesses his crimes and makes restitution for whatever he did."
    ),
    'honorable': Condition(
        name="Honorable",
        description="Your character is Honorable. She wields honesty the way some Uratha wield their claws.",
        is_persistent=False
    ),
    'humbled': Condition(
        name="Humbled",
        description="Your character has felt the touch of the divine and trembled. She feels unworthy and wretched. For as long as the Condition lasts, she suffers a –2 die penalty to Resolve rolls and may not regain Willpower from her Requiem.",
        is_persistent=False,
        possible_sources="Dramatic failure on a Theban Sorcery ritual.",
        beat="n/a",
        resolution_method="The character regains Willpower using her Mask."
    ),
    'i_know_someone': Condition(
        name="I Know Someone",
        description="Your character has a useful contact.",
        is_persistent=False
    ),
    'impostor': Condition(
        name="Impostor",
        description="Your character is pretending to be someone they're not.",
        is_persistent=False
    ),
    'informed': Condition(
        name="Informed",
        description="Your character has investigated a subject thoroughly and may shed this Condition to raise by one step the result of a related roll.",
        is_persistent=False
    ),
    'isolated': Condition(
        name="Isolated",
        description="Your character has been split from his crew, drawn and called out, cornered and quartered.",
        is_persistent=False
    ),
    'inspired': Condition(
        name="Inspired",
        description="Your character is deeply inspired. When your character takes an action pertaining to that inspiration, you may resolve this Condition. An exceptional success on that roll requires only three successes instead of five and you gain a point of Willpower.",
        is_persistent=False,
        possible_sources="Exceptional success with Crafts or Expression, the Inspiring Merit, the Auspex Discipline.",
        beat="n/a",
        resolution_method="You spend inspiration to spur yourself to greater success, resolving the Condition as described above."
    ),
    'instinctive': Condition(
        name="Instinctive",
        description="The primal nature of the hunter calls to your character.",
        is_persistent=False
    ),
    'intoxicated': Condition(
        name="Intoxicated",
        description="Your character is drunk, drugged, or otherwise dulled to the world around her. While she's probably not hallucinating, her inhibitions and reactions are both lower than they should be. Your character suffers a –2 die penalty to all Dexterity and Wits dice pools. Characters using Social maneuvering against her face two fewer Doors than usual.",
        is_persistent=False,
        possible_sources="Heavy drinking or drug use.",
        beat="n/a",
        resolution_method="You sleep it off, or face a breaking point."
    ),
    'invisible_predator': Condition(
        name="Invisible Predator",
        description="Your character has so successfully infiltrated her prey's domain that he is oblivious to her presence.",
        is_persistent=False
    ),
    'jaded': Condition(
        name="Jaded",
        description="Your character has no interest in the ways of the living. He eschews mortal society and only acts to better himself. Because of this, his Beast takes tighter hold on his actions. Any rolls to resist frenzy suffer his Humanity dots as a cap, and he cannot spend Willpower to hold back frenzy. He may still ride the wave.",
        is_persistent=False,
        possible_sources="Detachment failure.",
        beat="n/a",
        resolution_method="Meaningful interaction with a Touchstone."
    ),
    'languid': Condition(
        name="Languid",
        description="Your character feels the draw of torpor. His actions grow sluggish each night that passes, until eventually he falls to the sleep of ages. Every night that passes with this Condition, levy a cumulative –1 die penalty on all actions. As well, rising from daysleep requires a point of Vitae for each dot of Blood Potency.",
        is_persistent=False,
        possible_sources="Losing a Touchstone.",
        beat="n/a",
        resolution_method="Falling to torpor."
    ),
    'lethargic': Condition(
        name="Lethargic",
        description="Your character is drained and lethargic, feeling the weight of sleeplessness. With this Condition, your character cannot spend Willpower. As well, for every six hours he goes without sleeping, take a cumulative –1 die penalty to all actions. At every six-hour interval, make a Stamina + Resolve roll (with the penalty) to resist falling asleep until the sun next sets.",
        is_persistent=False,
        possible_sources="Fighting daysleep.",
        beat="n/a",
        resolution_method="Sleeping a full day."
    ),
    'leveraged': Condition(
        name="Leveraged",
        description="Your character has been blackmailed or tricked into doing another's bidding.",
        is_persistent=False
    ),
    'lost': Condition(
        name="Lost",
        description="Your character has no idea where he is and cannot seek his goal without first finding his way.",
        is_persistent=False
    ),
    'lost_cohesion': Condition(
        name="Lost Cohesion",
        description="The packmates just can't seem to communicate properly, or understand each other's intentions.",
        is_persistent=False
    ),
    'lost_hunters': Condition(
        name="Lost Hunters",
        description="The pack has somehow lost touch with its instincts, feeling out-of-touch with both the wolf and human aspects of its nature.",
        is_persistent=False
    ),
    'lost_tracker': Condition(
        name="Lost Tracker",
        description="Your character has lost faith in her abilities because she failed to find her prey.",
        is_persistent=False
    ),
    'mesmerized': Condition(
        name="Mesmerized",
        description="Your character's will is subordinate to that of a vampire. You're not obviously hypnotized — you're a bit quiet and reserved compared to normal, but nothing out of the ordinary. When the vampire who inflicted this Condition gives you a command, you cannot resist. If it's something that you wouldn't normally do, you might look like you've been hypnotized or that you're sleepwalking, but otherwise you look and act normally. If you resolve this Condition, gain a +3 die bonus to resist further attempts to Mesmerize you in the same scene; you also can't quite remember what happened while you were under the vampire's spell. This Condition fades naturally after a scene, which does not count as resolving the Condition.",
        is_persistent=False,
        possible_sources="The Dominate Discipline.",
        beat="n/a",
        resolution_method="Take any amount of bashing or lethal damage. Experience a breaking point as part of a vampire's command."
    ),
    'monstrous_servant': Condition(
        name="Monstrous Servant",
        description="Your character is master to a Geryo.",
        is_persistent=False
    ),
    'moon_taint': Condition(
        name="Moon Taint",
        description="Your character as been infected with the warping taint of Luna.",
        is_persistent=False
    ),
    'mystified': Condition(
        name="Mystified",
        description="Your character faced an Ithaeur, and now he feels the dread of the spirit wilds wherever he goes.",
        is_persistent=False
    ),
    'notoriety': Condition(
        name="Notoriety",
        description="Your character is ostracized by the public for a perceived wrong. Social rolls are made at a penalty, as is Social Maneuvering.",
        is_persistent=False
    ),
    'obsession': Condition(
        name="Obsession",
        description="Something's on your character's mind and she just can't shake it. She gains the 9-again quality on all rolls related to pursuing her obsession. On rolls that are unrelated to her obsession, she loses the 10-again quality. Obsession can be a temporary quality per Storyteller approval.",
        is_persistent=False,
        possible_sources="The Acute Senses Merit.",
        beat="Character fails to fulfill an obligation due to pursuing her obsession.",
        resolution_method="The character sheds or purges her fixation."
    ),
    'oblivious': Condition(
        name="Oblivious",
        description="Your character is not paying attention to what's going on around her. Her mind is wandering. She might be daydreaming or just staring off into space, but although she's completely aware of her surroundings she's not processing consciously what's happening in them. All of her Perception rolls are reduced to a chance die until this Condition is resolved.",
        is_persistent=False,
        possible_sources="The Acute Senses Merit.",
        beat="n/a",
        resolution_method="The character is alerted by a loud noise or is attacked."
    ),
    'outlaw': Condition(
        name="Outlaw",
        description="Your character has been declared an outlaw by the Thing and banished from society. Perhaps you can't pay a weregild, or refused an honorable challenge to a duel.",
        is_persistent=False
    ),
    'paranoid': Condition(
        name="Paranoid",
        description="Your character has been reduced to a state of rampant paranoia.",
        is_persistent=False
    ),
    'plugged_in': Condition(
        name="Plugged In",
        description="Your character is connected to a network or system.",
        is_persistent=False
    ),
    'punk_generation': Condition(
        name="Punk Generation",
        description="Your character has been wronged by someone more privileged than she.",
        is_persistent=False
    ),
    'prepared_for_anything': Condition(
        name="Prepared for Anything",
        description="Your character is ready for any situation.",
        is_persistent=False
    ),
    'pure': Condition(
        name="Pure",
        description="Your character is Pure. She adheres to the Oath of the Moon in all things. She's known to put her ancestral duties above everything in her life.",
        is_persistent=False
    ),
    'raptured': Condition(
        name="Raptured",
        description="Your character is filled with the glory of God's admonishment, the grace of her damnation. She finds an unsettling harmony with her Beast, due to the fire of Longinus's words. She does not need to use Willpower to ride the wave, and can ride the wave on three successes instead of five.",
        is_persistent=False,
        possible_sources="The Anointed Merit.",
        beat="n/a",
        resolution_method="Falling to frenzy or riding the wave."
    ),
    'reception': Condition(
        name="Reception",
        description="Your character has opened to the spirit world, as a result of her experience with Lunacy.",
        is_persistent=False
    ),
    'reluctant_aggressor': Condition(
        name="Reluctant Aggressor",
        description="Your character really doesn't want to hurt her victim, but she's going to anyway. She may be under immense peer pressure, it may be her duty, or perhaps she's coerced into the violence. Whatever the case, although she sees the victim's humanity, she's going to force herself to make him suffer. The character must spend a point of Willpower each turn to attempt an attack. She can defend herself as normal even if she can't (or won't) spend the Willpower.",
        is_persistent=False,
        possible_sources="The Peacemaker Merit.",
        beat="n/a",
        resolution_method="The character doesn't encounter her victim or his associates for a chapter, or the victim is the aggressor in targeting the character, her friends, or allies. If the Condition fades after a chapter, it does not award a Beat."
    ),
    'resigned': Condition(
        name="Resigned",
        description="Your character faced down his hunter, and the frightening beast has shown him the essence of doom.",
        is_persistent=False
    ),
    'sated': Condition(
        name="Sated",
        description="Your character gave her Beast an outlet that stopped it from driving her to frenzy. Until she resolves this Condition, she has a +1 die modifier to rolls to resist Frenzy.",
        is_persistent=False,
        possible_sources="The Animalism Discipline.",
        beat="n/a",
        resolution_method="Frenzy, or resist significant provocation to frenzy (a situation with a modifier of –3 or more to resist)."
    ),
    'scarred': Condition(
        name="Scarred",
        description="Your character was subject to a violent bite from Kindred fangs. He's disturbed, angry, paranoid, and prone to lashing out. With this Condition, take a –2 die penalty to any rolls to resist fear, such as with the Nightmare Discipline or the Intimidation Skill. As well, any creature exhibiting a predatory aura attempting to frighten or intimidate your character receives a +2 die bonus.",
        is_persistent=False,
        possible_sources="A violent bite from a vampire.",
        beat="n/a",
        resolution_method="Lash out physically, causing three or more levels of lethal damage to someone."
    ),
    'shadow_paranoia': Condition(
        name="Shadow Paranoia",
        description="Your character has been afflicted with a supernatural panic; she is jumpy and on edge, afraid that every shadow might contain sharp teeth and sudden death.",
        is_persistent=False
    ),
    'shaken': Condition(
        name="Shaken",
        description="Something has severely frightened your character. Any time your character is taking an action where that fear might hinder her, you may opt to fail the roll and resolve this Condition.",
        is_persistent=False,
        possible_sources="Facing a breaking point, the Auspex Discipline.",
        beat="n/a",
        resolution_method="The character gives into her fear and fails a roll as described above."
    ),
    'shadowlashed': Condition(
        name="Shadowlashed",
        description="Your character failed to master the laws of the Shadow and now suffers for her hubris.",
        is_persistent=False
    ),
    'spooked': Condition(
        name="Spooked",
        description="Your character has seen something supernatural — not overt enough to terrify her, but unmistakably otherworldly. How your character responds to this is up to you, but it captivates her and dominates her focus.",
        is_persistent=False,
        possible_sources="The Unseen Sense Merit, the Wet Dream Devotion.",
        beat="n/a",
        resolution_method="This Condition is resolved when your character's fear and fascination causes her to do something that hinders the group or complicates things (she goes off alone to investigate a strange noise, stays up all night researching, runs away instead of holding her ground, etc.)."
    ),
    'steadfast': Condition(
        name="Steadfast",
        description="Your character is confident and resolved. When you've failed a roll, you may choose to resolve this Condition to instead treat the action as if you'd rolled a single success. If the roll is a chance die, you may choose to resolve this Condition and roll a single regular die instead.",
        is_persistent=False,
        possible_sources="Encountering a breaking point.",
        beat="n/a",
        resolution_method="Your character's confidence carries him through and the worst is avoided; the Condition is resolved as described above."
    ),
    'stumbled': Condition(
        name="Stumbled",
        description="Your character has hit a complication while attempting a blood sorcery ritual. Each successive roll in the extended action is at a –3 die penalty.\n\nThis Condition does not grant a Beat when resolved.",
        is_persistent=False,
        possible_sources="Dramatic failure on a blood sorcery ritual.",
        beat="n/a",
        resolution_method="The ritual ends."
    ),
    'surrounded': Condition(
        name="Surrounded",
        description="Your character has no safe place to go, no ally can be trusted, all eyes are watching him.",
        is_persistent=False
    ),
    'surveilled': Condition(
        name="Surveilled",
        description="Your character is being watched.",
        is_persistent=False
    ),
    'swaggering': Condition(
        name="Swaggering",
        description="Your character faced the full bore of a Rahu's essence. He's sure that he can win in the face of the Rahu's fury.",
        is_persistent=False
    ),
    'swooning': Condition(
        name="Swooning",
        description="Your character is attracted to someone and is vulnerable where they are concerned. He may have the proverbial \"butterflies in his stomach\" or just be constantly aware of the object of his affection. A character may have multiple instances of this Condition, reflecting affection for multiple characters. He suffers a –2 die penalty to any rolls that would adversely affect the specified character, who also gains +2 die bonus on any Social rolls against him. If the specified character is attempting Social maneuvering on the Swooning character, the impression level is considered one higher (maximum of perfect; see p. 174).",
        is_persistent=False,
        possible_sources="Be on the receiving end of an exceptional success of a Persuasion or Subterfuge roll, dramatic failure on using the Majesty Discipline, fed on non-violently by a vampire, have another character help you fulfill your Vice (if mortal).",
        beat="n/a",
        resolution_method="Your character does something for his love interest that puts him in danger, or he opts to fail a roll to resist a Social action by the specified character."
    ),
    'symbolic_focus': Condition(
        name="Symbolic Focus",
        description="Your character is filled with the symbolic power of the rite that she has invoked, becoming a channel for it.",
        is_persistent=False
    ),
    'tainted': Condition(
        name="Tainted",
        description="Your character committed diablerie, and now retains traces of her victim's soul. Once per chapter, the victim can come back to haunt your character and try to force her destruction. This brief burst penalizes any one dice pool by the victim's Blood Potency dots, or adds to a dice pool opposing your character. This takes the form of subtle manifestations, or whispers that urge and distract. Your character may have multiple instances of this Condition, reflecting different victims.",
        is_persistent=False,
        possible_sources="Diablerie.",
        beat="n/a",
        resolution_method="A number of months pass equal to the victim's Blood Potency score. Every level of aggravated damage your character takes reduces this time by one month."
    ),
    'tasked': Condition(
        name="Tasked",
        description="Your character's clan, covenant, or family tasked her with a duty, and the responsibility carries weight. Take the 8-again quality on all rolls relating to the task. Any rolls not pertaining to the task lose the 10-again quality.",
        is_persistent=False,
        possible_sources="Dynasty Membership Merit.",
        beat="n/a",
        resolution_method="Complete the task; fail the task."
    ),
    'tempted': Condition(
        name="Tempted",
        description="Your character came close to losing control. Her Beast came at her, and she refused the call. Now, the Beast remains close to the surface. She gets a –1 die penalty to any rolls to resist frenzy. Until she sheds this Condition, each time she resists frenzy, the penalty increases by one. For example, after three successful resistances, note this Condition as \"Tempted –3\" on your character sheet.",
        is_persistent=False,
        possible_sources="Successfully resisted frenzy.",
        beat="n/a",
        resolution_method="Kill. Fall to frenzy. Have a meaningful connection with a Touchstone."
    ),
    'unware': Condition(
        name="Unware",
        description="Your character has been dazed and confused, distracted and internalized.",
        is_persistent=False
    ),
    'untraceable': Condition(
        name="Untraceable",
        description="Through care and attention to detail, your character leaves little evidence of her passage for others to follow.",
        is_persistent=False
    ),
    'wanton': Condition(
        name="Wanton",
        description="Your character wants, for the sake of wanting. He's distracted with temptations of excess and indulgence. Any Composure or Resolve rolls to resist temptation suffer a –2 die penalty. As well, the character that brought forth this Condition achieves exceptional success on three successes instead of five when making any rolls to tempt your character. This could apply to Majesty rolls as well as mundane social rolls.\n\nThis Condition fades naturally after a number of nights equal to the Blood Potency of the vampire who caused it. In the case of the predatory aura, this is the vampire who won the conflict. In the case of testing for detachment, this is the vampire's own Blood Potency.\n\nAfter resolving Wanton, your character cannot be subject to this Condition again for a full month.",
        is_persistent=False,
        possible_sources="A seductive predatory aura conflict, facing a breaking point.",
        beat="n/a",
        resolution_method="Indulge in something that constitutes a breaking point."
    ),
    'wise': Condition(
        name="Wise",
        description="Your character is Wise. She seeks the intelligent, reason answer in all things.",
        is_persistent=False
    ),
    'wracked': Condition(
        name="Wracked",
        description="Every part of your character hurts.",
        is_persistent=False
    ),
    
    # Persistent Conditions
    'addicted': Condition(
        name="Addicted (Persistent)",
        description="Your character is addicted to something, whether drugs, gambling or other destructive behaviors. Some addictions are more dangerous than others, but the nature of addiction is that it slowly takes over your life, impeding functionality. If you are addicted, you need to indulge your addiction regularly to keep it under control. A specific addiction should be chosen upon taking this Condition; characters can take this Condition multiple times for different addictions. Being unable to feed your addiction can result in the Deprived Condition.",
        is_persistent=True,
        possible_sources="Alcoholism, substance abuse, Vitae Addiction.",
        beat="Your character chooses to get a fix rather than fulfill an obligation.",
        resolution_method="Regain a dot of Integrity, lose another dot of Integrity, or achieve an exceptional success on a breaking point."
    ),
    'amnesia': Condition(
        name="Amnesia (Persistent)",
        description="Your character is missing a portion of her memory. An entire period of her life is just gone. This causes massive difficulties with friends and loved ones.",
        is_persistent=True,
        possible_sources="Physical or psychological trauma, the Dominate Discipline.",
        beat="Something problematic arises, such as a forgotten arrest warrant or old enemy.",
        resolution_method="You regain your memory and learn the truth. Depending on the circumstances, this may constitute a breaking point at a level determined by the Storyteller."
    ),
    'awestruck': Condition(
        name="Awestruck (Persistent)",
        description="Your character sees before her a glorious and terrifying figure, and something in her brain kicks her to kneel and grovel.",
        is_persistent=True
    ),
    'betrayed': Condition(
        name="Betrayed (Persistent)",
        description="Your character has been betrayed by someone they trusted.",
        is_persistent=True
    ),
    'blind': Condition(
        name="Blind (Persistent)",
        description="Your character cannot see, affecting any sight-based rolls.",
        is_persistent=True
    ),
    'blown': Condition(
        name="Blown (Persistent)",
        description="Your character's cover has been compromised.",
        is_persistent=True
    ),
    'broken': Condition(
        name="Broken (Persistent)",
        description="Whatever you did or saw, something inside you snapped. You can barely muster up the will to do your job anymore, and anything more emotionally intense than a raised voice makes you flinch and back down. Apply a –2 die penalty to all Social rolls and rolls involving Resolve, and a –5 die penalty to all use of the Intimidation Skill.",
        is_persistent=True,
        possible_sources="Tremendous psychological trauma, the Nightmare Discipline, some Ghoul Merits.",
        beat="You back down from a confrontation or fail a roll due to this Condition.",
        resolution_method="Regain a dot of Integrity, lose another dot of Integrity, or achieve an exceptional success on a breaking point."
    ),
    'charmed': Condition(
        name="Charmed (Persistent)",
        description="You've been charmed by a vampire's supernatural force of personality. You don't want to believe that anything he says is a lie, and you can't read his true intentions. The vampire adds his Majesty dots to Manipulation rolls against you, and any Wits + Empathy or Subterfuge rolls you make to detect his lies or uncover his true motives suffer a penalty equal to his Majesty dots. Using supernatural means to detect his lies become a Clash of Wills.\n\nYou want to do things for the vampire, to make him happy. If he asks, you'll do favors for him like he was one of your best friends — giving him a place to crash, lending him your car keys, or revealing secrets that you really shouldn't. You don't feel tricked or ripped off unless you resolve the Condition. It expires normally (without resolving) after one hour per dot of the vampire's Blood Potency.",
        is_persistent=True,
        possible_sources="The Majesty Discipline.",
        beat="You divulge a secret or perform a favor for the vampire.",
        resolution_method="The vampire attempts to seriously harm you or someone close to you, you make a significant financial or physical sacrifice for him."
    ),
    'connected': Condition(
        name="Connected (Persistent)",
        description="Your character has made inroads with a group, gaining a bonus on actions related to it.",
        is_persistent=True
    ),
    'crippled': Condition(
        name="Crippled (Persistent)",
        description="Your character either cannot or has difficulty walking. His Speed trait is limited and he requires a wheelchair to travel.",
        is_persistent=True
    ),
    'delusional': Condition(
        name="Delusional (Persistent)",
        description="You believe something that isn't actually true — maybe you think that someone is poisoning your food, that a doppelganger has replaced your daughter, or that something lives in the shadows of your apartment. You don't actually hallucinate images that reinforce your delusion; you may believe that you're covered in spiders, but just looking at yourself is enough to clarify matters. Germs, on the other hand.…\n\nYou can't truly repress your belief, but spending a point of Willpower lets you come up with an explanation (albeit one that sounds psychotic when you explain it to someone else) as to why your delusion does not apply to a specific situation.",
        is_persistent=True,
        possible_sources="The Nightmare Discipline.",
        beat="You adhere to your paranoid belief despite evidence to the contrary.",
        resolution_method="You completely disprove your delusion, or destroy the vampire who is the source of your paranoia."
    ),
    'dependent': Condition(
        name="Dependent (Persistent)",
        description="Your character has become obsessed with a mortal. This obsession is for both attention and for blood. She suffers all the effects of a second-stage blood bond (see p. 100) as if she were bound to the mortal.",
        is_persistent=True,
        possible_sources="Daeva clan bane.",
        beat="Your character suffers loss because she avoided responsibility for her obsession.",
        resolution_method="Death of the mortal."
    ),
    'disabled': Condition(
        name="Disabled (Persistent)",
        description="Your character has a permanent disability.",
        is_persistent=True
    ),
    'enervated': Condition(
        name="Enervated (Persistent)",
        description="The character is in the second stage of soul loss. Her instinctive efforts to shore up her Willpower by giving into her urges have failed, her Integrity has gone and her Willpower is now fading. In addition to the effects of Soulless, she can no longer regain Willpower through her Virtue, only her Vice. Indulging herself brings diminishing returns — whenever she does so, her permanent Willpower drops by one dot before she regains Willpower points to the new maximum.",
        is_persistent=True,
        possible_sources="Soul loss.",
        beat="Lose a dot of permanent Willpower.",
        resolution_method="The character regains her soul."
    ),
    'enslaved': Condition(
        name="Enslaved (Persistent)",
        description="You're totally in thrall to the vampire who inflicted this Condition. You can no longer tell when her instructions end and commands issued by Dominate begin. She tells you to do something and you do it. She tells you what you remember, and you remember it. This Condition counts as the Mesmerized Condition for the purpose of the Dominate Discipline. She doesn't have to look at you to issue a command as long as you can hear her voice. You do not apply your Resolve as a penalty to the vampire's dice pool for Entombed Command and Possession.",
        is_persistent=True,
        possible_sources="The Dominate Discipline.",
        beat="You're made to do something that you wouldn't normally do.",
        resolution_method="Kill the vampire who controls you. Undo her mental control by supernatural means."
    ),
    'enthralled': Condition(
        name="Enthralled (Persistent)",
        description="You're fanatically loyal to a vampire, willing to go to any length for him. You'll happily take actions that threaten your own life — ramming a speeding truck head-on, jumping in front of a gun-wielding psycho, or handing over your spouse and children for the vampire to play with. The compulsion lasts for one night for each dot of the vampire's Blood Potency.\n\nYou need to spend a point of Willpower just to take an action that goes against your master's commands. Doing so is an immediate breaking point at Humanity 1. If you fail, you chicken out at the last minute; only if you succeed can you do something that the vampire doesn't want you to do.",
        is_persistent=True,
        possible_sources="The Majesty Discipline.",
        beat="You put yourself in harm's way to protect the vampire.",
        resolution_method="You take serious harm (more lethal damage than your Stamina) when protecting the vampire, or you succeed at a breaking point roll related to the Condition."
    ),
    'false_memories': Condition(
        name="False Memories (Persistent)",
        description="The way you remember things doesn't match up with how they happened. You might remember a son who didn't exist, your alcoholic father abusing you despite being raised an orphan, or never getting married. You believe your memories to be true no matter what; even conclusive proof has a hard time getting through to you. Being faced with proof that your memory is fake is a breaking point for you at a level set by the Storyteller.",
        is_persistent=True,
        possible_sources="The Dominate Discipline.",
        beat="Your character trusts someone or takes a risky action based on his faked memories alone.",
        resolution_method="Face proof that your memory is false and succeed at the breaking point."
    ),
    'fugue': Condition(
        name="Fugue (Persistent)",
        description="Something terrible happened. Rather than deal with it or let it break you, your mind shuts it out. You are prone to blackouts and lost time. Whenever circumstances become too similar to the situation that led to the character gaining this Condition, the player rolls Resolve + Composure. If you fail the roll, the Storyteller controls your character for the next scene; your character, left to his own devices, will seek to avoid the conflict and get away from the area.",
        is_persistent=True,
        possible_sources="Psychological trauma, encountering a breaking point, some Ghoul Merits.",
        beat="You enter a fugue state as described above.",
        resolution_method="Regain a dot of Integrity, lose another dot of Integrity, or achieve an exceptional success on a breaking point."
    ),
    'hunted': Condition(
        name="Hunted (Persistent)",
        description="Your character is being pursued by something dangerous.",
        is_persistent=True
    ),
    'hunting_nature_human': Condition(
        name="Hunting Nature: Human (Persistent)",
        description="The pack values preparation and practice over blind instinct.",
        is_persistent=True
    ),
    'hunting_nature_werewolf': Condition(
        name="Hunting Nature: Werewolf (Persistent)",
        description="The pack has incorporated the strengths of both wolf and human into its hunting.",
        is_persistent=True
    ),
    'hunting_nature_wolf': Condition(
        name="Hunting Nature: Wolf (Persistent)",
        description="The pack values instinct over reason, the thrill of the chase, and the freedom of acting without the constant need for thought.",
        is_persistent=True
    ),
    'lured': Condition(
        name="Lured (Persistent)",
        description="Your character has been lured into an action; she is absolutely convinced she saw or heard something over there that she needs to check out, or has seen something she wants to investigate, becoming completely focused on it.",
        is_persistent=True
    ),
    'madness': Condition(
        name="Madness (Persistent)",
        description="Your character has been jarred loose from reality by way of some supernatural experience. He occasionally faces a penalty to Social or Mental rolls.",
        is_persistent=True
    ),
    'mute': Condition(
        name="Mute (Persistent)",
        description="Your character cannot speak and must communicate in some other manner.",
        is_persistent=True
    ),
    'radiation_poisoning': Condition(
        name="Radiation Poisoning (Persistent)",
        description="Your character has been exposed to atomic radiation and suffers radiation poisoning. Symptoms can include nausea and vomiting, anemia, red and blistering skin, dizziness, and seizures.",
        is_persistent=True
    ),
    'siskur_dah': Condition(
        name="Siskur-Dah (Persistent)",
        description="Your character is on the Siskur-Dah, the Sacred Hunt. She gains a specific benefit depending on the ritemaster's tribe.",
        is_persistent=True
    ),
    'soulless': Condition(
        name="Soulless (Persistent)",
        description="The character is in the first stage of soul loss. Without a soul, she can't attempt abjuration, warding, or binding (see The World of Darkness Rulebook or The God-Machine Chronicle). She is also more susceptible to possession — any dice pools to resist being taken over by another entity are at a –2 die penalty. The effects on Integrity and Willpower, though, are more severe. For as long as she has this Condition, she does not regain Willpower through surrender or rest, and her use of Virtue and Vice is reversed — she may regain one Willpower point per scene by fulfilling her Virtue without having to risk herself, and regains full Willpower once per chapter by fulfilling her Vice in a way that poses a threat to herself. Regaining Willpower through Vice, though, is now a breaking point with a –5 die penalty unless the character has reached Integrity 1. For a vampire, it is a breaking point at Humanity 2.",
        is_persistent=True,
        possible_sources="Soul loss.",
        beat="The character loses Integrity because she indulged her Vice.",
        resolution_method="The character regains her soul."
    ),
    'subservient': Condition(
        name="Subservient (Persistent)",
        description="A vampire has pressed down on your will, and you find it hard to resist doing what she wants even when she doesn't use her supernatural powers of command. She can give you commands as though you were Mesmerized even when you do not have that Condition. You can spend a Willpower point to resist her commands, but she can just Mesmerize you and order you that way. She still needs to use Dominate to alter your memory.\n\nThis Condition fades naturally after a week unless the vampire applies it to you again during that time.",
        is_persistent=True,
        possible_sources="The Dominate Discipline.",
        beat="The vampire makes you do something that you wouldn't normally do.",
        resolution_method="Take more lethal damage than you have Stamina when following the vampire's command. Experience a breaking point when following the command and succeed at the roll."
    ),
    'thrall': Condition(
        name="Thrall (Persistent)",
        description="The character has fully succumbed to the effects of soullessness. She may not spend Willpower points for any reason, may not use her Defense in combat, may not spend Experiences, and suffers all the effects of the Broken Condition (p. 301) as well. The player should only continue playing a character with this Condition if there's a chance of regaining the soul.",
        is_persistent=True,
        possible_sources="Soul loss.",
        beat="The character is victimized as a result of her Condition.",
        resolution_method="The character regains her soul."
    ),
    'uncalled': Condition(
        name="Uncalled (Persistent)",
        description="Your character has not been called to their true purpose.",
        is_persistent=True
    )
} 