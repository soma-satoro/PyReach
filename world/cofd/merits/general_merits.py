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
        description="Reflexively issue commands for trained raptor. May spend Willpower to enhance raptor's rolls. (*) Predator's Vigil: Raptor's presence inflicts Shaken on animals its Size or smaller. (**) Flyby: Bird contests Presence + Intimidation vs Resolve + Composure to inflict -3 action penalty. (***) Retrieve Item: Command bird to bring object, can exceptionally Disarm opponent. (****) Rake the Eyes: Bird attacks at -1 to blind target",
        merit_type="style",
        prerequisite="wits:3,animal_ken:3,bonded_condition:1"
    ),
    Merit(
        name="K-9",
        min_value=1,
        max_value=4,
        description="Issue commands to trained dog Size 3 or larger. (*) Detection: Dog takes rote quality to track chosen scent type with Wits + Survival. (**) Targeted Bite: Command dog to make called shots in combat, reducing penalty by -2. (***) Tactical Positioning: When fighting one opponent in tandem, choose roles each turn. One takes +1 Defense, other +2 to attack. Ignore penalties for firing into melee around dog. (****) Takedown Bite: Command dog to initiate biting grapple, immediately Holding or Dropping Prone",
        merit_type="style",
        prerequisite="wits:3,animal_ken:3,bonded_condition:1"
    ),
    # Social Styles
    Merit(
        name="Etiquette",
        min_value=1,
        max_value=5,
        description="(*) The Smile: +2 bonus to Socialize with those sharing culture in specific social context. (**) The Trappings: Ignore the first penalty from absence of equipment or appropriate clothing. (***) The Code: Rolls to research a culture take half the time and grant an exceptional success on three successes instead of five. (****) The Flexible Mind: Spend Willpower to ignore all untrained penalties when dealing with a new culture for the scene. (*****) The Cosmopolitan: No untrained penalties when using Etiquette with unfamiliar cultures",
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
        max_value=3,
        description="(*) Sprawl: While grappling, your opponent cannot use Drop Prone or Take Cover moves. (**) Takedown: With a normal roll, you may knock target prone instead of establishing grapple, and may inflict bashing equal to successes. (***) Joint Lock: Use Joint Lock move in grapple; next turn opponent suffers bashing equal to your successes. Can lead into Restrain, and your successful overpowering maneuvers inflict +1 lethal in addition to normal effects.",
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
        description="(*) Focused Attack: Reduce penalties for specified targets by 1 and ignore 1 point of armor. (**) Defensive Strike: Add 1 or 2 to Defense and subtract the same from attack dice; only usable on turns you attack and not with Dodge. (***) Whirlwind Strike: While Defense is available and you are not Dodging, enemies entering arm's reach take 1 bashing per turn while in range; spend Willpower to make this 2 bashing until next turn. (****) The Hand As Weapon: Unarmed strikes inflict lethal damage. (*****) The Touch of Death: Unarmed strikes count as weapons with damage rating 2.",
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
        description="At one dot, can perform short bursts with revolvers. At three dots, can make a medium burst with revolvers, but doesn't gain an attack bonus. At five dots, with offhand revolver, medium burst can hit targets not close together, for an additional -2 penalty",
        merit_type="fighting",
        prerequisite="wits:3,firearms:3"
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
        max_value=5,
        description="(*) Arcing Fire: Ignore cover bonus from objects shorter than you. (**) Arrow Storm: Aim at two targets within short range with a single roll at -2, inflicting damage on both. (***) Arrowcatch: Catch or deflect a projectile as reflexive action with Dexterity + Athletics, Defense applies. Success reduces damage by one per two successes. (****) Precision Shot: Spend Willpower and aim for two turns to take rote quality on attack roll. (*****) Deadly Precision: Reduce target number for exceptional success on aimed shots by one",
        merit_type="style",
        prerequisite="composure:3,dexterity:3,athletics:2,archery:2"
    ),
    Merit(
        name="Chain Weapons",
        min_value=1,
        max_value=5,
        description="(*) Whip Crack: Take a -1 penalty to inflict the Deafened Tilt with an attack. (**) Disarm: Spend Willpower on a called shot to Disarm, don't take called shot penalties. (***) Grapple: Can initiate grapples at one yard per weapon Size. (****) Watchful Devil: Penalize opponents' Defense or Dodge within weapon reach by dots in this Merit minus one. (*****) Snake Charmer: Can make two attacks per turn, second at -3 penalty",
        merit_type="style",
        prerequisite="dexterity:3,weaponry:3"
    ),
    Merit(
        name="Powered Projectile",
        min_value=1,
        max_value=5,
        description="Crossbows and other powered projectile weapons. (*) Armor Piercing: Ignore two points of armor. (**) Penetration: Reduce effective Durability of objects by dots in Powered Projectile. (***) Precise Aim: Take +1 to aimed shots instead of +2, but need only aim for one turn for three-turn bonus. (****) Punching Bolt: On all-out attacks, roll weapon damage twice and use higher result. (*****) Full Draw: Spend one Willpower and aim for two turns to inflict devastating attacks with 8-again quality",
        merit_type="style",
        prerequisite="composure:3,dexterity:3,athletics:2"
    ),
    Merit(
        name="Spear and Bayonet",
        min_value=1,
        max_value=5,
        description="(*) Thrust and Defend: Add weapon bonus to Defense when you make an attack with spear. (**) Fending Strike: Knock Down when successes exceed target's Strength. (***) Bayonet Drill: Firearms with fixed bayonets have no penalty for moving while aiming and firing. (****) Hold Them Back: With a readied action, strike anyone moving into reach, using better of Defense or Weaponry. (*****) Skewer: Ignore two points of Durability in armor and cover",
        merit_type="style",
        prerequisite="strength:3,athletics:2,weaponry:2"
    ),
    Merit(
        name="Staff Fighting",
        min_value=1,
        max_value=5,
        description="(*) Defense Bonus: Add one to Defense when using staff. (**) Thwack!: Attacks inflict a temporary -1 penalty and knocking back opponent one yard per net success. (***) Crack: Spend Willpower to reduce opponent's armor by one per Staff Fighting dot for remainder of scene. (****) Bring To Bear: Attacks with staff gain 9-again quality. (*****) Whirlwind: Spend Willpower to make feint and attack in single turn",
        merit_type="style",
        prerequisite="wits:3,athletics:2,weaponry:2"
    ),
    Merit(
        name="Strength Performance",
        min_value=1,
        max_value=4,
        description="(*) Strength Tricks: Take +1 to nonviolent feats of strength, +2 when using Expression or Intimidation. (**) Lifting: Receive rote quality on Strength + Stamina feats and combat actions to demolish structures. (***) Push/Pull: Double effective Strength to shift objects across plane, or quintuple with wheels. (****) Stronger Than You: Successful Strength rolls add an additional free success",
        merit_type="style",
        prerequisite="strength:3,stamina:2,athletics:2"
    ),
    Merit(
        name="Systema",
        min_value=1,
        max_value=3,
        description="(*) Rolling: Ignore penalties to attack from prone, roll Dexterity to mitigate bashing damage from impacts. (**) Balance: Contest attempts to bring you prone with two free successes. (***) Combat Posture: Knock Down when you roll victim's Strength in successes to strike them in melee, or add damage point if already Knocking Down",
        merit_type="style",
        prerequisite="dexterity:3,wits:2,athletics:3"
    ),
    Merit(
        name="Thrown Weapons",
        min_value=1,
        max_value=2,
        description="Throw Size 0-1 edged weapons. (*) Practiced Toss: Add Athletics as Initiative bonus while wielding thrown weapons. (**) Impalement Arts: Sacrifice Defense to inflict Impaled Tilt on called shot",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2,quick_draw_thrown:1"
    ),
    Merit(
        name="Two Weapon Fighting",
        min_value=1,
        max_value=4,
        description="Use complementary weapons up to Size 2, doesn't compensate for offhand penalties. (*) Balanced Grip: Don't sum Initiative penalties if off-hand weapon penalty isn't greater than main hand. (**) Protective Striking: Add off-hand weapon rating (minimum +1) to Defense against first attack in turn. (***) Dual Swipe: All-out attacks with both weapons ignore point of Defense and add off-hand weapon rating (minimum +1). Incompatible with Double Strike. (****) Double Strike: Spend Willpower to strike two targets simultaneously. Apply higher Defense plus one to both attacks",
        merit_type="style",
        prerequisite="wits:3,weaponry:3,fighting_finesse:1"
    ),
    Merit(
        name="Weapon and Shield",
        min_value=1,
        max_value=4,
        description="Use one-handed weapon from behind carried shield. (*) Shield Bash: Add shield's Size as bonus dice when dodging. Dodge successes in excess inflict bashing damage. (**) Boar's Snout: Can make all-out attacks without sacrificing shield Defense bonus, adding +1 Defense to allies also using this maneuver. (***) Pin Weapon: Disarm assailants on missed melee attacks. (****) Tortoise Shell: Treat shield as protective cover with Durability equal to its Size, +1 for each adjacent shielded ally",
        merit_type="style",
        prerequisite="strength:3,stamina:3,weaponry:2"
    )
]

# Combine all merits
all_merits = mental_merits + physical_merits + social_merits + supernatural_merits + style_merits

# Create dictionary for easy lookup
merits_dict = {merit.name.lower().replace(" ", "_"): merit for merit in all_merits}