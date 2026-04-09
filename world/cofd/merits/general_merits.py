from world.cofd.stat_types import Merit

# Mental Merits
mental_merits = [
    Merit(
        name="Area of Expertise",
        min_value=1,
        max_value=1,
        description="Uncommonly specialized in one area, +2 specialty bonus instead of +1",
        merit_type="mental",
        prerequisite="resolve:2,skill_specialty:1"
    ),
    Merit(
        name="Common Sense",
        min_value=3,
        max_value=3,
        description="Ask Storyteller questions about courses of action once per chapter",
        merit_type="mental"
    ),
    Merit(
        name="Danger Sense",
        min_value=2,
        max_value=2,
        description="+2 modifier to detect impending ambush",
        merit_type="mental"
    ),
    Merit(
        name="Direction Sense",
        min_value=1,
        max_value=1,
        description="Always aware of location and direction, never get lost",
        merit_type="mental"
    ),
    Merit(
        name="Eidetic Memory",
        min_value=2,
        max_value=2,
        description="Perfect recall, +2 bonus to remember minute facts",
        merit_type="mental"
    ),
    Merit(
        name="Encyclopedic Knowledge",
        min_value=2,
        max_value=2,
        description="Limitless factoids about chosen skill area",
        merit_type="mental"
    ),
    Merit(
        name="Eye for the Strange",
        min_value=2,
        max_value=2,
        description="Identify supernatural vs natural causes of events",
        merit_type="mental",
        prerequisite="resolve:2,occult:1"
    ),
    Merit(
        name="Fast Reflexes",
        min_value=1,
        max_value=3,
        description="+1 Initiative per dot",
        merit_type="mental",
        prerequisite="[wits:3,dexterity:3]"
    ),
    Merit(
        name="Good Time Management",
        min_value=1,
        max_value=1,
        description="Halve time between extended action rolls",
        merit_type="mental",
        prerequisite="[academics:2,science:2]"
    ),
    Merit(
        name="Holistic Awareness",
        min_value=1,
        max_value=1,
        description="Non-traditional healing methods without medical equipment",
        merit_type="mental"
    ),
    Merit(
        name="Indomitable",
        min_value=2,
        max_value=2,
        description="+2 dice to resist supernatural mental influence",
        merit_type="mental",
        prerequisite="resolve:3"
    ),
    Merit(
        name="Interdisciplinary Specialty",
        min_value=1,
        max_value=1,
        description="Apply specialty bonus to other skills when justified",
        merit_type="mental",
        prerequisite="skill:3,specialty:1"
    ),
    Merit(
        name="Investigative Aide",
        min_value=1,
        max_value=1,
        description="Exceptional success on 3 instead of 5 when uncovering clues",
        merit_type="mental",
        prerequisite="chosen_skill:3"
    ),
    Merit(
        name="Investigative Prodigy",
        min_value=1,
        max_value=5,
        description="Uncover multiple clues in single action",
        merit_type="mental",
        prerequisite="wits:3,investigation:3"
    ),
    Merit(
        name="Language",
        min_value=1,
        max_value=10,
        description="Fluency in additional language (1 language per dot)",
        merit_type="mental"
    ),
    Merit(
        name="Library",
        min_value=1,
        max_value=3,
        description="Add dots to extended rolls involving chosen Mental Skill",
        merit_type="mental"
    ),
    Merit(
        name="Meditative Mind",
        min_value=1,
        max_value=4,
        description="Enhanced meditation benefits",
        merit_type="mental"
    ),
    Merit(
        name="Multilingual",
        min_value=1,
        max_value=10,
        description="Conversational in additional languages (2 languages per dot)",
        merit_type="mental"
    ),
    Merit(
        name="Patient",
        min_value=1,
        max_value=1,
        description="Two additional rolls above Attribute + Skill in extended actions",
        merit_type="mental"
    ),
    Merit(
        name="Professional Training",
        min_value=1,
        max_value=5,
        description="(*) Networking: Gain two dots of Contacts related to your chosen Profession. (**) Continuing Education: Rolls with your Asset Skills gain 9-again. (***) Breadth of Knowledge: Choose a third Asset Skill and gain two Specialties among your Asset Skills. (****) On the Job Training: Gain one dot in an Asset Skill; whenever you purchase a new Asset Skill dot, gain a Beat. (*****) The Routine: Spend Willpower before rolling an Asset Skill to make it a rote action.",
        merit_type="mental"
    ),
    Merit(
        name="Tolerance for Biology",
        min_value=1,
        max_value=1,
        description="No rolls needed to withstand biologically strange sights",
        merit_type="mental",
        prerequisite="resolve:3"
    ),
    Merit(
        name="Trained Observer",
        min_value=1,
        max_value=3,
        description="9-again (or 8-again at 3 dots) on Perception rolls",
        merit_type="mental",
        prerequisite="[wits:3,composure:3]"
    ),
    Merit(
        name="Vice-Ridden",
        min_value=2,
        max_value=2,
        description="Character has two Vices",
        merit_type="mental"
    ),
    Merit(
        name="Virtuous",
        min_value=2,
        max_value=2,
        description="Character has two Virtues",
        merit_type="mental"
    ),
    Merit(
        name="Lucid Dreamer",
        min_value=2,
        max_value=2,
        description="You may roll Resolve + Composure while asleep to dream lucidly, and may wake up at will",
        merit_type="mental",
        prerequisite="resolve:3"
    ),
    Merit(
        name="Object Fetishism",
        min_value=1,
        max_value=5,
        description="You obsess over a given possession relating to a chosen Specialty. Recover Willpower each session from your obsession, and spending Willpower to roll that Specialty exaggerates both failure and success",
        merit_type="mental"
    ),
    Merit(
        name="Scarred",
        min_value=1,
        max_value=1,
        description="Suffer a Persistent Condition which prevents you from recovering Integrity, but inures you from a particular breaking point",
        merit_type="mental",
        prerequisite="integrity:5"
    )
]

# Physical Merits
physical_merits = [
    Merit(
        name="Ambidextrous",
        min_value=3,
        max_value=3,
        description="No -2 penalty for using off hand",
        merit_type="physical"
    ),
    Merit(
        name="Automotive Genius",
        min_value=1,
        max_value=1,
        description="Triple Crafts dots for vehicle modifications",
        merit_type="physical",
        prerequisite="crafts:3,drive:1,science:1"
    ),
    Merit(
        name="Crack Driver",
        min_value=2,
        max_value=3,
        description="Enhanced driving abilities",
        merit_type="physical",
        prerequisite="drive:3"
    ),
    Merit(
        name="Demolisher",
        min_value=1,
        max_value=3,
        description="Ignore object Durability points equal to Merit dots",
        merit_type="physical",
        prerequisite="[strength:3,intelligence:3]"
    ),
    Merit(
        name="Double Jointed",
        min_value=2,
        max_value=2,
        description="Automatically escape mundane bonds",
        merit_type="physical",
        prerequisite="dexterity:3"
    ),
    Merit(
        name="Fleet of Foot",
        min_value=1,
        max_value=3,
        description="+1 Speed per dot, pursuers at -1 per dot",
        merit_type="physical",
        prerequisite="athletics:2"
    ),
    Merit(
        name="Giant",
        min_value=3,
        max_value=3,
        description="Size 6, +1 Health",
        merit_type="physical"
    ),
    Merit(
        name="Greyhound",
        min_value=1,
        max_value=1,
        description="Exceptional success on 3 instead of 5 in chases",
        merit_type="physical",
        prerequisite="athletics:3,wits:3,stamina:3"
    ),
    Merit(
        name="Hardy",
        min_value=1,
        max_value=3,
        description="Add dots to rolls resisting disease, poison, deprivation",
        merit_type="physical",
        prerequisite="stamina:3"
    ),
    Merit(
        name="Iron Stamina",
        min_value=1,
        max_value=3,
        description="Eliminate negative modifiers from fatigue/injury",
        merit_type="physical",
        prerequisite="[stamina:3,resolve:3]"
    ),
    Merit(
        name="Quick Draw",
        min_value=1,
        max_value=1,
        description="Drawing/holstering chosen weapon is reflexive",
        merit_type="physical",
        prerequisite="wits:3,weapon_specialty:1"
    ),
    Merit(
        name="Relentless",
        min_value=1,
        max_value=1,
        description="Opponents need +2 successes in chases",
        merit_type="physical",
        prerequisite="athletics:2,stamina:3"
    ),
    Merit(
        name="Seizing the Edge",
        min_value=2,
        max_value=2,
        description="Always have Edge in first turn of chase",
        merit_type="physical",
        prerequisite="wits:3,composure:3"
    ),
    Merit(
        name="Sleight of Hand",
        min_value=2,
        max_value=2,
        description="One reflexive Larceny action per turn",
        merit_type="physical",
        prerequisite="larceny:3"
    ),
    Merit(
        name="Small-Framed",
        min_value=2,
        max_value=2,
        description="Size 4, -1 Health, +2 to hide",
        merit_type="physical"
    )
]

# Social Merits
social_merits = [
    Merit(
        name="Allies",
        min_value=1,
        max_value=5,
        description="Organizational connections that provide favors",
        merit_type="social"
    ),
    Merit(
        name="Alternate Identity",
        min_value=1,
        max_value=3,
        description="Established false identity with documentation",
        merit_type="social"
    ),
    Merit(
        name="Anonymity",
        min_value=1,
        max_value=5,
        description="Paper trail searches suffer -1 per dot",
        merit_type="social"
    ),
    Merit(
        name="Barfly",
        min_value=2,
        max_value=2,
        description="Blend into bar environments, rolls to identify as outsider penalized",
        merit_type="social",
        prerequisite="socialize:2"
    ),
    Merit(
        name="Closed Book",
        min_value=1,
        max_value=5,
        description="Add Merit dots as additional Doors in Social Maneuvering",
        merit_type="social",
        prerequisite="manipulation:3,resolve:3"
    ),
    Merit(
        name="Contacts",
        min_value=1,
        max_value=5,
        description="Information sources in various spheres",
        merit_type="social"
    ),
    Merit(
        name="Fame",
        min_value=1,
        max_value=3,
        description="Public recognition, bonus dice to impressed Social rolls",
        merit_type="social"
    ),
    Merit(
        name="Fixer",
        min_value=2,
        max_value=2,
        description="Reduce service Availability by one dot",
        merit_type="social",
        prerequisite="contacts:2,wits:3"
    ),
    Merit(
        name="Hobbyist Clique",
        min_value=2,
        max_value=2,
        description="9-again quality and +2 dice on chosen Skill",
        merit_type="social",
        prerequisite="clique_membership:1,chosen_skill:2"
    ),
    Merit(
        name="Inspiring",
        min_value=3,
        max_value=3,
        description="Grant Inspired Condition to listeners",
        merit_type="social",
        prerequisite="presence:3"
    ),
    Merit(
        name="Iron Will",
        min_value=2,
        max_value=2,
        description="Use Resolve instead of Willpower in Social contests",
        merit_type="social",
        prerequisite="resolve:4"
    ),
    Merit(
        name="Mentor",
        min_value=1,
        max_value=5,
        description="Teacher/advisor with chosen Skills or Resources",
        merit_type="social"
    ),
    Merit(
        name="Mystery Cult Initiation",
        min_value=1,
        max_value=5,
        description="Membership in esoteric organization",
        merit_type="social"
    ),
    Merit(
        name="Pusher",
        min_value=1,
        max_value=1,
        description="Improve Impression when mark accepts soft leverage",
        merit_type="social",
        prerequisite="persuasion:2"
    ),
    Merit(
        name="Resources",
        min_value=1,
        max_value=5,
        description="Disposable income for purchases",
        merit_type="social"
    ),
    Merit(
        name="Retainer",
        min_value=1,
        max_value=5,
        description="Loyal assistant/servant",
        merit_type="social"
    ),
    Merit(
        name="Safe Place",
        min_value=1,
        max_value=5,
        description="You've secured a place from intrusion. Apply your Safe Place rating as an Initiative bonus while there, and a penalty to break in. With Crafts you can install traps, forcing intruders to roll Dexterity + Larceny - Safe Place to avoid up to your Safe Place in lethal damage.",
        merit_type="social"
    ),
    Merit(
        name="Hiding Place",
        min_value=3,
        max_value=3,
        description="You have a place that is always secure. If found out, gain a new one at the start of the next chapter. Cannot be shared.",
        merit_type="social"
    ),
    Merit(
        name="Small Unit Tactics",
        min_value=2,
        max_value=2,
        description="Grant Willpower bonus to multiple allies in coordinated actions",
        merit_type="social",
        prerequisite="presence:3"
    ),
    Merit(
        name="Spin Doctor",
        min_value=1,
        max_value=1,
        description="Reduce Tainted Clue penalties",
        merit_type="social",
        prerequisite="manipulation:3,subterfuge:2"
    ),
    Merit(
        name="Staff",
        min_value=1,
        max_value=5,
        description="Crew that automatically succeeds at mundane tasks",
        merit_type="social"
    ),
    Merit(
        name="Status",
        min_value=1,
        max_value=5,
        description="Standing in organization, can block others' Merits",
        merit_type="social"
    ),
    Merit(
        name="Striking Looks",
        min_value=1,
        max_value=2,
        description="Bonus dice to Social rolls influenced by appearance",
        merit_type="social"
    ),
    Merit(
        name="Sympathetic",
        min_value=2,
        max_value=2,
        description="Accept Condition to eliminate two Doors in Social Maneuvering",
        merit_type="social"
    ),
    Merit(
        name="Table Turner",
        min_value=1,
        max_value=1,
        description="Preempt Social Maneuvering with own action",
        merit_type="social",
        prerequisite="composure:3,manipulation:3,wits:3"
    ),
    Merit(
        name="Takes One to Know One",
        min_value=1,
        max_value=1,
        description="+2 and 9-again when investigating crime matching Vice",
        merit_type="social"
    ),
    Merit(
        name="Taste",
        min_value=1,
        max_value=1,
        description="Identify details in artistry and craftsmanship",
        merit_type="social",
        prerequisite="crafts:2,specialty:1"
    ),
    Merit(
        name="True Friend",
        min_value=3,
        max_value=3,
        description="Unbreakable relationship, regain Willpower from interaction",
        merit_type="social"
    ),
    Merit(
        name="Untouchable",
        min_value=1,
        max_value=1,
        description="Investigation rolls suffer Incomplete Clue unless exceptional success",
        merit_type="social",
        prerequisite="manipulation:3,subterfuge:2"
    ),
    Merit(
        name="Tutelage",
        min_value=3,
        max_value=3,
        description="As either the student or teacher, meet your counterpart for a lesson once per story. The student gains 1 experience to be used towards purchasing the topic of the lesson, in exchange for a favor the teacher calls in. The Teacher gains a 1 experience reduction to the next purchase, in exchange for some kind of social trouble the student brings upon them",
        merit_type="social"
    )
]

# Supernatural Merits
supernatural_merits = [
    Merit(
        name="Aura Reading",
        min_value=3,
        max_value=3,
        description="Perceive auras to read emotional state and supernatural nature",
        merit_type="supernatural"
    ),
    Merit(
        name="Automatic Writing",
        min_value=2,
        max_value=2,
        description="Spirit possession for mysterious clues",
        merit_type="supernatural"
    ),
    Merit(
        name="Biokinesis",
        min_value=1,
        max_value=5,
        description="Shift Physical Attributes, enhanced healing",
        merit_type="supernatural"
    ),
    Merit(
        name="Clairvoyance",
        min_value=3,
        max_value=3,
        description="Project senses to another location",
        merit_type="supernatural"
    ),
    Merit(
        name="Cursed",
        min_value=2,
        max_value=2,
        description="Aware of fate, +2 to resist fear, extra Beats when near death",
        merit_type="supernatural"
    ),
    Merit(
        name="Laying on Hands",
        min_value=3,
        max_value=3,
        description="Faith healing at cost to self",
        merit_type="supernatural"
    ),
    Merit(
        name="Medium",
        min_value=3,
        max_value=3,
        description="Communicate with and influence ghosts",
        merit_type="supernatural",
        prerequisite="empathy:2"
    ),
    Merit(
        name="Mind of a Madman",
        min_value=2,
        max_value=2,
        description="8-again investigating specific culprit, traumatic dreams",
        merit_type="supernatural",
        prerequisite="empathy:3"
    ),
    Merit(
        name="Numbing Touch",
        min_value=1,
        max_value=5,
        description="Psychic paralysis and Willpower drain",
        merit_type="supernatural"
    ),
    Merit(
        name="Omen Sensitivity",
        min_value=3,
        max_value=3,
        description="Interpret signs for yes/no questions, causes obsession",
        merit_type="supernatural"
    ),
    Merit(
        name="Psychokinesis",
        min_value=3,
        max_value=5,
        description="Manipulate specific force (fire, cold, electricity, etc.)",
        merit_type="supernatural"
    ),
    Merit(
        name="Psychometry",
        min_value=3,
        max_value=3,
        description="Read emotional impressions from objects",
        merit_type="supernatural"
    ),
    Merit(
        name="Telekinesis",
        min_value=1,
        max_value=5,
        description="Move objects with mind, dots = effective Strength",
        merit_type="supernatural"
    ),
    Merit(
        name="Telepathy",
        min_value=3,
        max_value=5,
        description="Read surface thoughts, send messages at 5 dots",
        merit_type="supernatural"
    ),
    Merit(
        name="Thief of Fate",
        min_value=3,
        max_value=3,
        description="Steal luck from touched targets",
        merit_type="supernatural"
    ),
    Merit(
        name="Unseen Sense",
        min_value=2,
        max_value=2,
        description="Sixth sense for chosen supernatural creature type",
        merit_type="supernatural"
    ),
    Merit(
        name="Esoteric Armory",
        min_value=1,
        max_value=5,
        description="You've collected enough esoterica to supply the banes of ephemeral entities with a Rank up to your rating in this Merit",
        merit_type="supernatural"
    )
]

# Style/Fighting Merits
style_merits = [
    # Mental Styles
    Merit(
        name="Unintended Applications",
        min_value=1,
        max_value=5,
        description="(*) Improvised... Weapon?: +2 to Intimidation when brandishing something claimed as deadly. (**) Achilles Fuse: Pinpoint weak point in a structure. (***) Creative Discount: Jury-rig an asset up to two dots higher than Resources in Availability, for hour's work per Size. (****) Gremlin: Disable a device without leaving evidence, can disable complicated devices from distance with equipment. (*****) Jury-Rig: Spend Willpower and roll Wits + Crafts or Science to make anything whose Availability doesn't exceed successes, right away for objects under Size 6",
        merit_type="style",
        prerequisite="wits:3,[crafts:2,science:2]"
    ),
    # Physical Styles
    Merit(
        name="Aggressive Driving",
        min_value=1,
        max_value=4,
        description="(*) Powerslide: Take a hard turn for bonus successes in contested pursuit by rolling Dexterity + Drive + Handling, taking Structure damage. (**) Bump and Run: Roll Dexterity + Drive + Handling - Defense to brush bumper and cause traction loss. (***) J-turn: Once a scene, when caught, spend Willpower and roll Dexterity + Drive + Handling - 2 to swerve and restart chase in opposite direction. (****) Swoop and Squat: When you have lead greater than pursuer's Wits in successes, may brake and force pursuer to roll Resolve + Composure + Handling to avoid crash",
        merit_type="style",
        prerequisite="resolve:3,drive:3,fast_reflexes:3"
    ),
    Merit(
        name="Drone Control",
        min_value=1,
        max_value=3,
        description="(*) Remote Immersion: Take 9-Again to perception actions using remote device. (**) Interface: Spend Willpower to perform additional non-combat action through device this turn. (***) Overclock: Inflict Structure damage for +2 bonus to device's physical actions this turn",
        merit_type="style",
        prerequisite="intelligence:3,computer:3,drive:2"
    ),
    Merit(
        name="Falconry",
        min_value=1,
        max_value=4,
        description="(*) Predator's Vigil: Creatures of equal or smaller Size than your bird in its immediate vicinity gain Shaken for actions other than hiding or fleeing. (**) Flyby: Bird makes Presence + Intimidation contested by Resolve + Composure; success inflicts -3 to target's next action. (***) Retrieve Item: Bird retrieves an object up to its Size, including Disarm attempts from opponents; successful Disarm is treated as exceptional success. (****) Rake the Eyes: Bird attacks at -1 and on success inflicts Blinded Tilt.",
        merit_type="style",
        prerequisite="wits:3,animal_ken:3,bonded_condition:1"
    ),
    Merit(
        name="K-9",
        min_value=1,
        max_value=4,
        description="(*) Detection: Choose one category (Drugs, Explosives, Tracks, People, Corpses); with your guidance, dog gains rote on Wits + Survival to detect that category. (**) Targeted Bite: Reduce penalties to attack specified targets by 2. (***) Tactical Positioning: Against one opponent while fighting side by side, one of you gains +1 Defense and the other gains +2 to attacks; choose each turn, and you never take penalties to avoid shooting your dog. (****) Takedown Bite: On successful bite, dog may apply Drop Prone or Hold and initiate grapple against targets up to double dog's Size.",
        merit_type="style",
        prerequisite="wits:3,animal_ken:3,bonded_condition:1"
    ),
    # Social Styles
    Merit(
        name="Etiquette",
        min_value=1,
        max_value=5,
        description="(*) Bless His Heart: Use Socialize instead of the lower of Resolve/Composure to determine your starting Doors in Social interactions. (**) Losing Your Religion: When verbally tearing down a target, gain 8-again and +2 dice, then move interaction one step down on the impressions chart. (***) In High Cotton: Apply one relevant Status or Fame Merit to rolls contesting Social interactions. (****) Half-Cocked: In a new Social interaction with good, excellent, or perfect impression, ignore subject Resolve and Composure on the first roll. (*****) Grace Under Fire: If someone opens all your Doors and you offer an alternative, their player chooses three Conditions and you choose which one you receive.",
        merit_type="style",
        prerequisite="composure:3,socialize:2"
    ),
    Merit(
        name="Pusher",
        min_value=1,
        max_value=5,
        description="(*) Unsolicited Advice: Roll Manipulation + Persuasion or Expression to tell someone advice, contest Resolve + Composure. Success inflicts Leveraged Condition. (**) Incredible Truths: When generating Leveraged, learn a piece of information about target's Aspirations or Integrity. (***) Pressure: Each uncovered piece of information about Aspirations or Integrity grants Door during Social Maneuvering. (****) Saturation: Once per chapter per target, apply Informed Condition about target. (*****) Svengali: When you know two pieces of information and have inflicted Leveraged in past week, spend Willpower in Social Maneuvering to convert impression to one step better",
        merit_type="style",
        prerequisite="manipulation:3,persuasion:2"
    ),
    Merit(
        name="Fast-Talking",
        min_value=1,
        max_value=5,
        description="(*) Always Be Closing: When a mark contests or resists your Social interactions, apply -1 to their Resolve or Composure. (**) Jargon: Apply one relevant Specialty to any Social roll, even if the Specialty is not tied to the Skill in use. (***) Devil's Advocacy: Reroll one failed Subterfuge roll per scene. (****) Salting: When you open a Door using conversation, spend Willpower to immediately open another Door. (*****) The Nigerian Scam: If a target regains Willpower from Vice while you are present, roll Manipulation + Subterfuge to open a Door regardless of interval or impression level.",
        merit_type="style",
        prerequisite="manipulation:3,subterfuge:2"
    ),
    # Combat Styles
    Merit(
        name="Armed Defense",
        min_value=1,
        max_value=5,
        description="(*) Cover the Angles: When Dodging, reduce multiple-attacker Defense penalties by 1. (**) Weak Spot: Against armed attackers, if your Defense reduces their attack pool to 0 (or your Dodge roll reduces successes to 0), you disarm them. (***) Aggressive Defense: While Dodging, if you beat an attacker's roll, inflict 1 lethal per extra success (weapon bonus does not apply). Drawback: Spend 1 Willpower at turn start and cannot combine with Press the Advantage or Weak Spot. (****) Iron Guard: At turn start, reduce weapon bonus (min 0) to raise Defense by equal amount; if Dodging, add full weapon bonus after doubling Defense pool. (*****) Press the Advantage: While Dodging, if your Defense roll reduces an attack to 0 successes, make an immediate unarmed counterattack at -2.",
        merit_type="style",
        prerequisite="dexterity:3,weaponry:2,defensive_combat:weaponry:1"
    ),
    Merit(
        name="Close Quarters Combat",
        min_value=1,
        max_value=5,
        description="(*) Firing Lines: As a reaction to ranged attack, run to cover within twice Speed instead of dropping prone (lose your action this turn). (**) Hard Surfaces: In a grapple, use Damage move to bounce target off hard surface, dealing lethal, then end grapple. (***) Armored Coffin: When grappling, add target's general armor rating to your pool and ignore their armor on Damage moves; cannot combine with Hard Surfaces. (****) Prep Work: Surprise attack Dexterity + Stealth roll becomes rote. Drawback: Cannot be used for sniper attacks; ambush must use Brawl or Weaponry. (*****) Turnabout: Disarm attempts step up one result level (failure drops weapon, success takes weapon, exceptional also inflicts 2 bashing).",
        merit_type="style",
        prerequisite="wits:3,athletics:2,brawl:3"
    ),
    Merit(
        name="Defensive Combat",
        min_value=1,
        max_value=1,
        description="Must be purchased as an instance: Defensive Combat (Brawl) or Defensive Combat (Weaponry). Defense uses Athletics or the chosen skill, whichever is higher. If both instances are taken, use the highest of Athletics, Brawl, or Weaponry.",
        merit_type="fighting",
        prerequisite="[brawl:1,weaponry:1]"
    ),
    Merit(
        name="Fighting Finesse",
        min_value=2,
        max_value=2,
        description="Use Dexterity instead of Strength for chosen weapon",
        merit_type="fighting",
        prerequisite="dexterity:3,weapon_specialty:1"
    ),
    Merit(
        name="Firefight",
        min_value=1,
        max_value=3,
        description="(*) Shoot First: If your gun is drawn, add Firearms to Initiative; with Quick Draw, you can draw and fire with this bonus on first combat turn. (**) Suppressive Fire: With Covering Fire, opponents cannot gain aiming benefits against you; you may apply Defense against Firearms attacks in addition to cover, and may use Suppressive Fire with semi-automatic weapons. (***) Secondary Target: Trade direct hit for collateral impact; attack deals bashing instead of lethal and ignores all cover penalties; weapon damage does not add.",
        merit_type="style",
        prerequisite="composure:3,dexterity:3,athletics:2,firearms:2"
    ),
    Merit(
        name="Grappling",
        min_value=1,
        max_value=5,
        description="(*) Standing Throw: Inflict Knocked Down as a grappling maneuver; if you remain standing, opponent automatically breaks free. (**) Small Joint Manipulation: Take -2 to attack to inflict bashing damage per two successes (min 1) and Agony; targeted hand can no longer hold objects until damage heals. (***) Ippon: Additional prerequisite Takedown maneuver; when using Drop Prone with Takedown, double damage only for Stunned Tilt determination. (****) Dynamic Guard: While prone, reduce opponent's grapple pool by your Dexterity; you cannot stand while using this maneuver. (****) Lock Flow: Additional prerequisite Joint Lock maneuver; gain +2 to grapple rolls when declaring joint lock in advance. (*****) Tap or Snap: Additional prerequisite Joint Lock maneuver; on successful grapple turn after Joint Lock, opponent chooses Beaten Down or Arm/Leg Wrack plus lethal damage equal to successes. (*****) Positional Dominance: On successful grapple, inflict bashing per two successes (min 1) in addition to maneuver effects; optional each time.",
        merit_type="style",
        prerequisite="stamina:3,strength:2,athletics:2,brawl:2"
    ),
    Merit(
        name="Heavy Weapons",
        min_value=1,
        max_value=5,
        description="(*) Sure Strike: Remove three dice from attack pool (to min 0) to add +1 weapon damage for the turn; remove after environmental and Defense penalties. (**) Threat Range: If you do not move or Dodge, any character entering your proximity takes 1 lethal and suffers Defense penalty equal to your weapon damage for one turn. (***) Bring the Pain: Sacrifice Defense and make standard attack; damage dealt also becomes penalty to victim's actions next turn. (****) Warding Stance: Spend Willpower reflexively to add weapon damage rating as armor for the turn (not vs Firearms). (*****) Rending: Spend Willpower before attack to add 1 aggravated damage on successful hit in addition to weapon damage (Willpower does not add dice).",
        merit_type="style",
        prerequisite="stamina:3,strength:3,athletics:2,weaponry:2"
    ),
    Merit(
        name="Improvised Weaponry",
        min_value=1,
        max_value=3,
        description="(*) Always Armed: Make reflexive Wits + Weaponry to grab an improvised weapon almost anywhere; default item is +0 damage, -1 initiative, Size 1, Durability 2, Structure 4, and ignores improvised weapon penalty. Exceptional success increases weapon modifier and Size by 1 but initiative penalty becomes -2. (**) In Harm's Way: With an Always Armed weapon, treat its Structure as general armor against one Brawl or Weaponry attack; blocked damage also damages weapon, bypassing Durability. (***) Breaking Point: On all-out attack with Always Armed weapon, reduce its Structure (min 0); every 2 Structure spent adds +1 weapon modifier for that attack. If Structure reaches 0, weapon is destroyed after attack.",
        merit_type="style",
        prerequisite="wits:3,weaponry:1"
    ),
    Merit(
        name="Iron Skin",
        min_value=2,
        max_value=4,
        description="Armor against bashing, downgrade lethal damage",
        merit_type="fighting",
        prerequisite="[martial_arts:2,street_fighting:2],stamina:3"
    ),
    Merit(
        name="Light Weapons",
        min_value=1,
        max_value=5,
        description="(*) Rapidity: Sacrifice weapon damage rating to add Weaponry to Initiative for the turn; weapon damage becomes 0 that turn. (**) Thrust: Trade Defense for attack dice one-for-one; cannot be used after Defense was already applied and cannot be used with all-out attack. (***) Feint: If attack would deal no damage, your next attack ignores Defense equal to weapon damage plus prior successes and gains extra damage equal to those successes. (****) Flurry: While Defense is available and you are not Dodging, enemies entering your proximity take 1 lethal (once per turn while they remain in range). (*****) Vital Shot: Sacrifice Defense for turn; on successful attack, inflict 1 aggravated damage in addition to weapon damage.",
        merit_type="style",
        prerequisite="[wits:3,fighting_finesse:1],dexterity:3,athletics:2,weaponry:2"
    ),
    Merit(
        name="Marksmanship",
        min_value=1,
        max_value=4,
        description="(*) Through the Crosshairs: Maximum aiming bonus becomes Composure + Firearms instead of 3. (**) Precision Shot: Reduce weapon damage one-for-one to reduce called-shot penalty by same amount. (***) A Shot Rings Out: Fire into crowds without risk of hitting unintended targets; misses go wide. (****) Ghost: Firearms score is a penalty to rolls to notice your vantage point or investigate where you were shooting from.",
        merit_type="style",
        prerequisite="composure:3,resolve:3,firearms:2"
    ),
    Merit(
        name="Martial Arts",
        min_value=1,
        max_value=5,
        description="(*) Leg Kick: Reduce Defense by 1 to focus low attacks; if Brawl attack inflicts at least one damage, inflict Leg Wrack without leg-targeting penalty. (**) Cutting Elbow: Attack penalty to inflict Blinded from scalp blood is only -2 when attack inflicts at least one bashing against human-like anatomy. (***) Trapping: On successful Brawl hit, set aside up to Brawl successes and add them to next turn's Brawl attack; if all set aside, first hit deals no damage but establishes contact. (****) Inch Force: Once per turn when grabbed, make immediate reflexive Strength + Brawl - Defense counterattack; if successes exceed opponent Strength, break free and inflict normal Brawl damage. (*****) High Momentum Strike: If you have higher Initiative and opponent's Brawl/Weaponry strike scores 0 successes, make immediate spinning/leaping counterattack; on hit, knock opponent down and add Brawl dots to damage.",
        merit_type="style",
        prerequisite="resolve:3,dexterity:3,athletics:2,brawl:2"
    ),
    Merit(
        name="Parkour",
        min_value=1,
        max_value=5,
        description="(*) Flow: In a foot chase, subtract Parkour dots from successes needed to pursue or evade; ignore environmental penalties to Athletics up to Parkour dots. (**) Cat Leap: Gain one automatic success on Dexterity + Athletics to mitigate falling damage; add Parkour to removable damage threshold (not terminal velocity). (***) Wall Run: Scale 10 feet + 5 feet per Athletics dot as an instant action without a roll before traditional climbing. (****) Expert Traceur: Spend Willpower to make one Athletics run/jump/climb roll rote; you cannot apply Defense on that turn. (*****) Freeflow: After successful meditation, take one Athletics action reflexively per turn; spend Willpower in a foot chase Athletics roll to gain three successes instead of three dice.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2"
    ),
    Merit(
        name="Police Tactics",
        min_value=1,
        max_value=3,
        description="(*) Compliance Hold: Gain +2 to overpowering rolls to disarm or immobilize an opponent. (**) Weapon Retention: Opponents trying to disarm you or turn your weapon against you must exceed your Weaponry in successes. (***) Speed Cuff: Against an immobilized target, apply restraints (handcuffs, cable ties, similar) reflexively.",
        merit_type="style",
        prerequisite="brawl:2,weaponry:1"
    ),
    Merit(
        name="Stunt Driver",
        min_value=1,
        max_value=4,
        description="(*) Defensive Driving: Subtract Drive dots from attempts to hit your moving vehicle. (**) Speed Demon: Each success on acceleration rolls increases Speed by 10 instead of 5. (***) Drift: Never need maneuvering roll to turn at high speeds. (****) Clipping: When voluntarily ramming another character or vehicle, ignore damage to your own vehicle equal to Wits before Durability.",
        merit_type="style",
        prerequisite="dexterity:3,drive:3,wits:3"
    ),
    Merit(
        name="Street Fighting",
        min_value=1,
        max_value=5,
        description="(*) Duck and Weave: Reflexively take -1 to all actions this turn to use higher of Wits or Dexterity for Defense. (**) Knocking the Wind Out: On successful unarmed attack, opponent takes -1 to their next roll. (***) Kick 'Em While They're Down: If attack successes exceed opponent Stamina, may apply Knocked Down Tilt; when close enough as they rise from prone, reflexively deal 2 bashing. (****) One-Two Punch: On successful attack, spend Willpower to deal +2 bashing. (*****) Last-Ditch Effort: When about to be hit or overpowered while suffering wound penalties, spend Willpower and sacrifice Defense to make immediate attack before opponent resolves action.",
        merit_type="style",
        prerequisite="stamina:3,composure:3,brawl:2,streetwise:2"
    ),
    Merit(
        name="Unarmed Defense",
        min_value=1,
        max_value=5,
        description="(*) Like a Book: Against unarmed opponents while not Dodging, increase Defense by half Brawl (round down). (**) Studied Style: Attacks from one chosen opponent do not reduce Defense; if your Defense reduces their attack pool to 0, their further attacks against you lose 10-again. (***) Redirect: While Dodging, if your Defense roll reduces an attack to 0 successes, force that attacker to roll same attack against another attacker. Drawback: Only one redirect per turn and cannot redirect against same attacker. (****) Joint Strike: Roll Strength + Brawl instead of Defense; if you exceed attacker successes, inflict 1 bashing per extra success and Arm Wrack or Leg Wrack Tilt. Drawback: Spend 1 Willpower to use. (*****) Like the Breeze: While Dodging, if your Defense roll reduces an opponent attack to 0 successes, inflict Knocked Down Tilt. Drawback: Must declare at start of turn before other attacks.",
        merit_type="style",
        prerequisite="dexterity:3,brawl:2,defensive_combat:brawl:1"
    ),
    Merit(
        name="Cheap Shot",
        min_value=2,
        max_value=2,
        description="Dirty tricks to remove opponent's Defense",
        merit_type="fighting",
        prerequisite="street_fighting:3,subterfuge:2"
    ),
    Merit(
        name="Choke Hold",
        min_value=2,
        max_value=2,
        description="Unconsciousness through grappling",
        merit_type="fighting",
        prerequisite="brawl:2"
    ),
    Merit(
        name="Shiv",
        min_value=1,
        max_value=2,
        description="Conceal small weapons, use with Brawl",
        merit_type="fighting",
        prerequisite="street_fighting:2,weaponry:1"
    ),
    Merit(
        name="Armed Restraint",
        min_value=2,
        max_value=2,
        description="Use a hooking pole when grappling to instantly Hold and penalize your opponent by its weapon rating",
        merit_type="fighting",
        prerequisite="staff_fighting:3"
    ),
    Merit(
        name="Body as Weapon",
        min_value=2,
        max_value=2,
        description="Unarmed strikes add one point of bashing damage on a successful hit",
        merit_type="fighting",
        prerequisite="stamina:3,brawl:2"
    ),
    Merit(
        name="Boot Party",
        min_value=2,
        max_value=2,
        description="Attack a prone target at -3 to deal lethal damage unarmed",
        merit_type="fighting",
        prerequisite="brawl:2"
    ),
    Merit(
        name="Clinch Strike",
        min_value=1,
        max_value=1,
        description="Use the Damage maneuver instantly in a grapple",
        merit_type="fighting",
        prerequisite="brawl:2"
    ),
    Merit(
        name="Ground and Pound",
        min_value=3,
        max_value=3,
        description="Take the rote quality to strike a prone target with Brawl, falling prone yourself",
        merit_type="fighting",
        prerequisite="brawl:2"
    ),
    Merit(
        name="Ground Fighter",
        min_value=3,
        max_value=3,
        description="Deny close combat bonuses from being prone, and gain the Stand Up grapple maneuver",
        merit_type="fighting",
        prerequisite="wits:3,dexterity:3,brawl:2"
    ),
    Merit(
        name="Gunslinger",
        min_value=1,
        max_value=5,
        description="(*) Quick Fan: You can perform a short burst with a revolver as though it were an automatic weapon. (***) Adjusted Fan: You can perform a medium burst with a revolver using only three rounds. You gain no attack bonus, still suffer multiple-target penalties, and cannot make multiple attacks against the same target in the same turn. (*****) Cross-Fan: If wielding two revolvers, you may target multiple opponents who are not close together as long as both are within short range. This is otherwise identical to the three-dot effect, but the multiple-target penalty increases by 2.",
        merit_type="fighting",
        prerequisite="wits:3,firearms:3,firearms_specialty:1"
    ),
    Merit(
        name="Headbutt",
        min_value=1,
        max_value=1,
        description="Gain the Headbutt grapple maneuver: inflict Stunned",
        merit_type="fighting",
        prerequisite="brawl:2"
    ),
    Merit(
        name="Iron Chin",
        min_value=2,
        max_value=4,
        description="Don't suffer Beaten Down from bashing damage. With four dots, never suffer Beaten Down",
        merit_type="fighting",
        prerequisite="resolve:3,stamina:3"
    ),
    Merit(
        name="Killer Instinct",
        min_value=1,
        max_value=3,
        description="You can take an instant action to size up a target's most vulnerable parts, which also counts as an aiming action. When attacking the target afterward, each dot of this Merit can ignore 1/1 Armor, ignore a point of Defense, or convert a point of bashing to lethal damage",
        merit_type="fighting",
        prerequisite="composure:3,wits:3,medicine:1"
    ),
    Merit(
        name="Loaded for Bear",
        min_value=1,
        max_value=2,
        description="Gain extra reloads on weapons, including single shot weapons",
        merit_type="fighting",
        prerequisite="athletics:1,survival:1"
    ),
    Merit(
        name="Phalanx Fighter",
        min_value=2,
        max_value=2,
        description="Wield a spear with a shield, substituting it in Weapon and Shield maneuvers",
        merit_type="fighting",
        prerequisite="weapon_and_shield:2,spear_and_bayonet:1"
    ),
    Merit(
        name="Retain Weapon",
        min_value=2,
        max_value=2,
        description="Reduce successes on a Control Weapon or Disarm maneuver against you by your Brawl",
        merit_type="fighting",
        prerequisite="wits:2,brawl:2"
    ),
    Merit(
        name="Subduing Strikes",
        min_value=1,
        max_value=1,
        description="You can pull blows with a weapon to deal bashing damage without spending Willpower",
        merit_type="fighting",
        prerequisite="weaponry:2"
    ),
    Merit(
        name="Transfer Maneuver",
        min_value=1,
        max_value=3,
        description="Cross-apply a Brawling maneuver to a Weaponry Style, or vice-versa",
        merit_type="fighting",
        prerequisite="intelligence:2,wits:3,brawl:2,weaponry:2"
    ),
    Merit(
        name="Trigger Discipline",
        min_value=1,
        max_value=1,
        description="Increase a firearm's effective capacity, or allow an additional long burst at high capacity",
        merit_type="fighting",
        prerequisite="wits:2,firearms:2"
    ),
    Merit(
        name="Trunk Squeeze",
        min_value=2,
        max_value=2,
        description="Gain the Trunk Squeeze grapple maneuver: deal bashing damage and cumulatively penalize the opponent's contesting rolls",
        merit_type="fighting",
        prerequisite="brawl:2"
    ),
    # Additional Combat Styles
    Merit(
        name="Bowmanship",
        min_value=1,
        max_value=4,
        description="(*) Arcing Fire: Double range increments when using a bow. (**) Bullseye: Lower bow damage to any value 0+ to gain +1 and 8-again on a specified-target attack roll. (***) Out of Nowhere: After attacking while unseen, reflexively roll Dexterity + Stealth; target rolls Wits + Composure minus your successes, and failure inflicts Shaken. (****) Death from Above: Reduce Concealment by adding 10 yards per point to shot range; if cover is vertically protective, subtract Durability from damage as normal.",
        merit_type="style",
        prerequisite="dexterity:3,firearms:2,trained_observer:1"
    ),
    Merit(
        name="Chain Weapons",
        min_value=1,
        max_value=2,
        description="(*) Imposing Defense: Sacrifice Defense; inflict weapon damage rating + 1 bashing to any opponent attempting unarmed or melee attack against you that turn. (**) Bring Down the House: Attack an overhead object (penalized by object Size); on success, all characters in range take bashing equal to object Structure, and those with turns available may Dodge to reduce damage.",
        merit_type="style",
        prerequisite="strength:3,dexterity:3,athletics:2,weaponry:2"
    ),
    Merit(
        name="Powered Projectile",
        min_value=1,
        max_value=4,
        description="(*) Quick Reload: Reload one turn faster, to a minimum of reflexive. (**) Intercept Shot: On a turn spent aiming, attack a thrown object at -2 plus normal small-target penalties; on hit, deflect it random direction by yards equal to damage. (***) Penetration: Add +2 to weapon's armor piercing on next attack. Drawback: Lose Defense on any turn you use this maneuver. (****) Skewer: Reduce specified-target penalty by 2, and inflicted Tilts require victim to roll Stamina + Strength - inflicted damage to remove projectile before resolving Tilt.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2,firearms:2"
    ),
    Merit(
        name="Spear and Bayonet",
        min_value=1,
        max_value=3,
        description="(*) Firm Footing: Opponents making all-out or charge attacks against you take your weapon damage automatically before their attack roll; armor applies to this automatic damage, but then does not apply to your attacks that turn. (**) Keep at Bay: Choose opponent with shorter weapon; if they do anything but back away or Dodge, they lose Defense against your next attack. Drawback: Spend Willpower to activate. (***) Strike and Develop: Lethal attacks with your weapon cause bleed-out for one lethal per turn for turns equal to attack successes; subsequent attacks add turns but bleeding never exceeds one lethal per turn. Drawback: Lose Defense on turns using this maneuver.",
        merit_type="style",
        prerequisite="strength:3,dexterity:2,weaponry:2"
    ),
    Merit(
        name="Staff Fighting",
        min_value=1,
        max_value=4,
        description="(*) Short Grip: Change grip reflexively once per turn; gain +1 attack and lose staff's +1 Defense bonus. (**) Thwack Weapon: Disarm with Strength + Weaponry contested by Strength + Athletics; success drops weapon at feet, exceptional knocks it away by yards equal to successes. (***) Vaulting Defense: Spend Willpower to add your Melee dots to Defense against one attack per turn. (****) Tornado Strike: Treat staff attack as autofire medium burst against up to three targets in range.",
        merit_type="style",
        prerequisite="strength:2,dexterity:3,weaponry:2"
    ),
    Merit(
        name="Strength Performance",
        min_value=1,
        max_value=4,
        description="(*) Strength Tricks: Gain +2 to Performance and Intimidation where strength feats can be demonstrated, plus +1 to other non-combat feats of Strength. (**) Lifting: Gain rote on Strength + Stamina feat rolls; also applies when damaging relatively immobile inanimate objects with a pool no larger than Strength + Stamina. (***) Push/Pull: Double effective Strength for lateral movement, or multiply Strength by 5 if friction is minimized (such as wheels). (****) Stronger Than You: On successful Strength-related rolls, add +1 success to total, including combat.",
        merit_type="style",
        prerequisite="strength:3,stamina:2,athletics:2"
    ),
    Merit(
        name="Systema",
        min_value=1,
        max_value=3,
        description="(*) Rolling: Ignore usual -2 penalty to attacks while prone and roll Dexterity to remove bashing from falls/impacts, one per success. (**) Balance: Attempts to inflict Knocked Down or Drop Prone must achieve two additional successes. (***) Combat Posture: Brawl/Weaponry attacks inflict Knocked Down when successes equal or exceed victim Strength; if attack already inflicts Knocked Down, add one damage.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:3,wits:2"
    ),
    Merit(
        name="Thrown Weapons",
        min_value=1,
        max_value=2,
        description="(*) Practiced Toss: Add Athletics to Initiative when using a thrown weapon. (**) Impalement Arts: If you deal damage to specified target arm, leg, or hand with thrown weapon, inflict Impaled Tilt. Drawback: Lose Defense on turns using this maneuver.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2,quick_draw_thrown:1"
    ),
    Merit(
        name="Two Weapon Fighting",
        min_value=1,
        max_value=4,
        description="(*) Balanced Grip: Ignore Initiative penalties from dual weapons when off-hand weapon penalty is equal to or lower than main-hand. (**) Protective Striking: Add off-hand weapon bonus to Defense against first attack each turn (or +1 if off-hand bonus is 0). (***) Dual Swipe: As part of all-out melee attack, add off-hand weapon bonus (or +1) to attack roll and reduce target Defense by 1; cannot combine with Double Strike. (****) Double Strike: Spend Willpower and target two enemies in close range; apply highest Defense and an extra -1 penalty to pool, then apply each weapon's damage separately to one target each.",
        merit_type="style",
        prerequisite="wits:3,fighting_finesse:2,weaponry:3"
    ),
    Merit(
        name="Weapon and Shield",
        min_value=1,
        max_value=4,
        description="(*) Shield Bash: When Dodging, add shield Size to pool; if you reduce attack successes to 0, extra successes inflict bashing. (**) Boar's Snout: While using shield and one-handed weapon, you may all-out attack and still keep shield Size bonus to Defense; allies doing this same turn each add +1 Defense. (***) Pin Weapon: If opponent misses melee attack against you, they are automatically disarmed. (****) Tortoise Shell: While using shield, count as behind cover with Durability equal to shield Size plus one per nearby shield-wielding ally.",
        merit_type="style",
        prerequisite="strength:3,stamina:3,weaponry:2"
    ),
    Merit(
        name="Avoidance",
        min_value=1,
        max_value=4,
        description="(*) Insignificance: At combat start, roll Manipulation + Stealth minus highest Composure in room; on success, unless opponent perceives no other threats, you cannot be direct target until you attack or act threateningly. (***) Coattails: While Dodging, designate a close ally who has not attacked yet this turn and go prone; if attack hits you, ally may choose to take the damage. (***) Whack-a-Mole: Once per turn, contest Manipulation + Persuasion + Avoidance against an opponent's unarmed/melee attack roll; if you win, attack deals no damage and attacker suffers Arm Wrack. (****) Play Dead: After taking lethal damage, roll Manipulation + Subterfuge; opponents need contested Wits + Composure to notice you are still alive.",
        merit_type="style",
        prerequisite="manipulation:3,athletics:2,stealth:2"
    ),
    Merit(
        name="Berserker",
        min_value=1,
        max_value=3,
        description="(*) The Red Mist: Spend Willpower to inflict Insane Tilt on yourself for the scene. (**) War Cry: Instead of attacking, roll contested Strength + Intimidation versus Resolve + Composure; if you win, opponent takes penalty equal to your successes on any action other than Dodging next turn. (***) Manic Brutality: All-out unarmed attacks gain +1 to hit specified targets; with a weapon, you may substitute weapon Durability for weapon bonus. Drawback: If using weapon, all damage dealt to opponent is also applied to weapon Structure.",
        merit_type="style",
        prerequisite="strength:3,iron_stamina:3"
    ),
    Merit(
        name="Boxing",
        min_value=1,
        max_value=5,
        description="(*) Head Protection: Increase Defense by 1 against unarmed or Brawl-skill weapon attacks, and attackers take additional -1 to head shots. (**) Defensive Jab: When opponent misses Brawl/Weaponry attack, inflict 1 bashing ignoring armor; if Dodging, inflict 1 bashing per two successes exceeding opponent's successes (min 1). (***) Knockout Artist: Treat target Size as 1 lower for Stunned Tilt; when taking true head specified-target penalty, treat Size as 2 lower for Stunned. (****) Combination: On successful Brawl strike, roll Dexterity dots and add successes to damage. (*****) Out for the Count: When you inflict Stunned, it lasts turns equal to damage inflicted and causes unconsciousness unless victim spends Willpower.",
        merit_type="style",
        prerequisite="strength:2,dexterity:2,stamina:2,brawl:2,athletics:2"
    ),
    Merit(
        name="Combat Archery",
        min_value=1,
        max_value=5,
        description="(*) Rapid Nock: As long as arrows are in reach, you may make a bow attack every turn without separate nocking action and ignore bow Initiative penalty. (**) Reflex Aiming: Ignore penalties for firing bow into close combat. (***) Parthian Shot: On first close-range attack against you in a turn, Dodge as normal; successes above opponent's are applied as bow attack successes against that opponent. (****) Rain of Arrows: Attack with bow as autofire medium burst, with three arrows hitting up to three targets. Drawback: Triple all medium and long range penalties. (*****) Trick Shot: Fire bow while simultaneously taking an Athletics action, including Movement Style maneuvers, with -2 to both rolls.",
        merit_type="style",
        prerequisite="strength:3,athletics:2,quick_draw_bow:1"
    ),
    Merit(
        name="Kino Mutai",
        min_value=1,
        max_value=4,
        description="(*) Trained Bite: In a successful grapple, use Damage maneuver to inflict +2 bashing; supernatural bite attacks add +1 of their normal damage type. (**) Ripping: If grapple successes exceed opponent Resolve, use Ripping maneuver to inflict Agony and 1 bashing. (***) Trained Gouge: In grapple, if you win with at least three successes, inflict Blinded Tilt that persists until opponent breaks free, restrains you, or disables your arm. (****) Continuous Bite: In grapple, your Damage maneuver inflicts lethal damage by tearing flesh.",
        merit_type="style",
        prerequisite="dexterity:2,resolve:3,brawl:2"
    ),
    Merit(
        name="Mounted Combat",
        min_value=1,
        max_value=4,
        description="(*) Steady Saddle: Gain +3 to rolls to stay mounted during combat. (**) Fixed Charge: Gain both charge and all-out attack benefits, moving up to twice mount Speed; both rider and mount lose Defense for turn. (***) Skirmishing: Mount moves half Speed before and half after attack as one move; attack takes -2, rider and mount gain +2 Defense. (****) Rearing Beast: Instead of attacking, roll Wits + Animal Ken and add successes to mount's attack rolls.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2,animal_ken:2"
    ),
    Merit(
        name="Brute Force",
        min_value=1,
        max_value=5,
        description="Requires Size 5+ to use. Prometheans in Torment gain +1 die to Brute Force rolls. Brute Force attacks use bare hands or fist-based weapons only. (*) Falling Pillar: Make an all-out attack with 8-again; if damage equals or exceeds target Stamina, inflict Knocked Down. (**) Crush and Bite: In grapple, replace normal bite to inflict lethal equal to grapple successes and cause one additional lethal next turn from bleeding (if target can bleed). (***) Juggernaut: If you can charge at least 10 feet, any successful unarmed attack inflicts Knocked Down. (****) Bone Cracker: Make an all-out limb-targeted attack (which removes normal +2 all-out bonus). If damage equals or exceeds target Stamina, inflict +1 lethal and Arm Wrack or Leg Wrack. Cannot combine with Falling Pillar. (*****) Colossus: During all-out attacks, gain 1/2 armor (cumulative with worn armor), cannot suffer Knocked Down or similar Tilts, and attempts to grapple or forcibly move you suffer a dice penalty equal to your Strength.",
        merit_type="style",
        prerequisite="strength:3,brawl:2"
    ),
    Merit(
        name="Disabling Tactics",
        min_value=1,
        max_value=3,
        description="(*) Breaking the Branch: Reduce penalties for attacks targeting arm, hand, or leg by 2. (**) Cast Like Sand: After a successful damaging weapon hit, spend Willpower to inflict Knocked Down. (***) Strike the Rising Dog: When someone in striking distance tries to stand from prone, spend Willpower to make a reflexive Weaponry attack; if successful, they fail to rise in addition to taking normal damage.",
        merit_type="style",
        prerequisite="strength:3,weaponry:2"
    ),
    Merit(
        name="Relentless Assault",
        min_value=1,
        max_value=5,
        description="Applies only to Brawl attacks and can be used in Kuruth. (*) Drop of a Hat: In the first turn of a fight, gain +3 Initiative if you make an all-out attack. (**) Eye of the Tiger: Choose one target; when making an all-out attack against that target, you retain Defense against that target. (***) Dig Deep: Before an attack roll, remove one die to increase claws/teeth weapon modifier by +1. (****) Grin and Bear It: Any turn you make an all-out attack, gain 1/1 armor against all attacks for that turn (stacks with other armor). (*****) The Warpath: When you fill an opponent's last Health box with lethal or aggravated damage, make an immediate additional attack against another target in reach; if this second attack deals damage, you immediately enter Basu-Im without a chance to resist.",
        merit_type="style",
        prerequisite="strength:3,stamina:3,brawl:2"
    )
]

# Combine all merits
all_merits = mental_merits + physical_merits + social_merits + supernatural_merits + style_merits

# Create dictionary for easy lookup
merits_dict = {merit.name.lower().replace(" ", "_").replace("-", "_").replace("'", ""): merit for merit in all_merits}