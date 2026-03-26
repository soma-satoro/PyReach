from world.cofd.stat_types import Merit

# Deviant: The Renegades Specific Merits
deviant_merits = [
    Merit(
        name="Bleeding Heart",
        min_value=3,
        max_value=3,
        description="Through sheer bloody-minded tenacity, your character has managed to hold on to part of her humanity, allowing her to behave as though she still had a Virtue (chosen at the time you purchase this Merit). Once per chapter, when your character acts in accordance with that Virtue, roll Resolve + Composure. Success means that she regains all her Willpower as though she has acted on a Virtue (p. 95). The character does not otherwise count as having the Virtue.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Blood on My Hands",
        min_value=3,
        max_value=3,
        description="Through spite and ill will, your character has managed to hold on to part of her humanity, allowing her to behave as though she still had a Vice (chosen at the time you purchase this Merit). Once per scene, when your character acts in accordance with that Vice, roll Resolve + Composure. Success means that she regains a point of Willpower as though she had acted on her Vice (p. 95). The character does not otherwise count as having the Vice.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Good Samaritan",
        min_value=2,
        max_value=2,
        description="Despite the suffering the Divergence has caused him, or perhaps because of it, your character feels compelled to use his experiences and remarkable abilities to help Baselines and protect them from the Web of Pain. He enjoys a +2 bonus to Intimidation and Persuasion rolls to warn a Baseline away from a conspiracy's agents or projects. Additionally, take a Beat whenever you risk conspiracy attention by using a Variation to aid a Baseline who is not a Loyalty Touchstone.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Human Prey",
        min_value=2,
        max_value=2,
        description="Humans share the fight, flight, and freeze response that prey animals share, but your character has been afraid for his life too many times, and this has made it almost impossible for him to respond to violent situations in any other way. Whenever violence breaks out in the character's presence, immediately before you roll Initiative, you may choose to react with one of the prey responses: Fight: Your fear manifests as a berserk frenzy. You suffer the Insane Tilt (p. 317) but add 1 to your Strength. Flight: You only wish to flee your attackers. You suffer the Beaten Down Tilt. However, you enjoy the 8-again quality on any actions you take to leave the area affected by the violence. Freeze: Your panic manifests as inaction, whether it freezes you in your tracks or sends you cowering in terror. You suffer either the Stunned Tilt or the Insensate Tilt, but you regain a point of Willpower.",
        merit_type="mental",
        prerequisite=""
    ),
    Merit(
        name="Hypervigilance",
        min_value=1,
        max_value=1,
        description="Your character is constantly on the lookout, scanning her environment for the curling of fingers, the flash of a barrel, a raised voice. You enjoy the 8-again quality on reflexive Wits + Composure rolls for your character to detect an impending ambush, snare, or trap. Drawback: If you achieve an exceptional success on a roll to detect a source of danger, your character suffers the Spooked Condition (p. 323).",
        merit_type="mental",
        prerequisite=""
    ),
    Merit(
        name="Investigative Aide",
        min_value=1,
        max_value=1,
        description="Your character has one particular knack that can contribute amazingly to an investigation. Choose a Skill when purchasing this Merit; when making rolls to uncover Clues (p. 210), she achieves exceptional success on three successes instead of five. As well, Clues that come from her use of that Skill start with one additional element. You may purchase this Merit multiple times, to enhance different Skills.",
        merit_type="mental",
        prerequisite="chosen_skill:3"
    ),
    Merit(
        name="Investigative Prodigy",
        min_value=1,
        max_value=5,
        description="Your character investigates instinctively, and can intuit details and connections in a scene without much time. He's a veritable Sherlock Holmes. Instead of simply uncovering Clues or not uncovering Clues when investigating (p. 210), your character discovers multiple Clues in a single action. Your character can uncover Clues equal to his successes or his Merit dots, whichever is lower, as an instant action. Only the first Clue benefits from additional elements; other Clues established with this Merit receive only a single element each.",
        merit_type="mental",
        prerequisite="wits:3,investigation:3"
    ),
    Merit(
        name="Shared Suffering",
        min_value=2,
        max_value=2,
        description="Your character feels a deep sympathy for her fellow Broken. She enjoys a +2 bonus on Empathy and Medicine rolls to aid a fellow Deviant. In addition, whenever you preserve from destruction a Remade who is not in your cohort, you take a Beat. This includes showing mercy to an enemy Deviant when it would be more expedient not to do so.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Freediving",
        min_value=1,
        max_value=1,
        description="Your character can hold her breath for remarkably long. She calculates how long she can hold her breath safely using Athletics + Stamina instead of Stamina and achieves an exceptional success on three successes instead of five on Resolve + Stamina rolls to resist the gasp reflex.",
        merit_type="physical",
        prerequisite="athletics:2"
    ),
    Merit(
        name="Stabilizer",
        min_value=1,
        max_value=3,
        description="Your character possesses an item or receives a treatment that holds off Instability. It may be a device that creates a dampening field around her, or a serum that repairs damaged cells. Not only does it grant her peace of mind, it also allows her some measure of control over her Instability. Each dot of this Merit reduces the Instability penalty on Scar Resistance rolls by one, to a minimum penalty of 0 (p. 87). Drawback: If the character loses the item or misses a treatment, she loses the benefits of this Merit until she can retrieve the object or resume treatment. If the object or treatment is lost permanently, the Sanctity of Merits applies normally.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Air of Menace",
        min_value=2,
        max_value=2,
        description="Your character has survived dozens of fights, and each one has taken its toll. He carries scars, features that have healed crookedly, and an attitude that unsettles others. The character gains +2 dice to rolls that use fear and menace to force compliance, such as with Intimidation rolls. Opponents less menacing than the character also think twice before provoking him. Opponents with Intimidation dots fewer than the character's must spend a point of Willpower to initiate combat against him. Drawback: Though people may try to overcome their prejudices, appearance still drives many human opinions. In social maneuvers, the character's first impression is downgraded one step for people who do not know him, and even for those who do he must overcome an additional Door.",
        merit_type="social",
        prerequisite="intimidation:2"
    ),
    Merit(
        name="Armed and Extremely Dangerous",
        min_value=3,
        max_value=3,
        description="Your character had an unusually bloody escape from her conspiracy. Whether she gunned her way through legions of guards and scientists with a stolen automatic weapon, or shredded the facility with nothing but a scalpel and a pair of forceps, she is a fugitive in every sense of the word. Her conspiracy treats her at best with extreme caution, and at worst as a bogeyman, a tale that they tell to new recruits. Any members of the conspiracy your character meets will either call for backup or flee outright. Agents of a conspiracy who encounter the Deviant without having prepared themselves for the confrontation suffer the Beaten Down Tilt (p. 314) when they realize their predicament, unless they outnumber her and her allies by at least the rating of her highest Magnitude Variation. Drawback: While the conspiracy will only rarely send agents to collect the Broken, when it does, it will send well-equipped, heavily armed hit squads, ready to bring her in dead or alive, regardless of the casualties they might suffer. Agents sent to engage her (or her cohort) as part of a conspiracy action are immune to the Beaten Down Tilt in the current scene.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Lifeline",
        min_value=2,
        max_value=4,
        description="The Deviant can divide his passion between more people than can most Broken. At two dots, the Remade may have a maximum of six Touchstones (and associated Conviction and Loyalty traits) at a time, instead of five. At four, this is instead seven Touchstones. If purchasing this Merit during character creation, the character's player may assign an additional Conviction or Loyalty Touchstone to each of these bonus slots, increasing Conviction/Loyalty accordingly. Otherwise, the character must establish and affirm a new Touchstone to fill them.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Living Progenitor",
        min_value=3,
        max_value=5,
        description="Deviants often have a complicated relationship with their Progenitors, one that frequently mimics that of child with parent, created with creator, or victim with abuser. Your character's Progenitor still lives, and he knows it. Work together with your Storyteller to decide what sort of person your Progenitor is - how often he worked on you, if he spoke to or cared for you, etc. You must assign the Progenitor as one of your character's Touchstones. At three dots, the Broken cannot sever this connection to his Progenitor. The Touchstone may fluctuate between Loyalty and Conviction, but it never becomes Wavering or fades, no matter how many times the Deviant Falters. Only death can end this relationship. At five dots, your love/hate relationship intensifies: If your Progenitor was one of your Conviction Touchstones at the beginning of the chapter, and you have him at your mercy, you may let him go free instead of killing him. This still counts as Faltering, but you heal a minor, medium, or major Instability after resolving the Faltering roll. If your Progenitor was one of your Loyalty Touchstones at the beginning of the chapter, and you healed at least one minor or medium Instability during the chapter by coming to his aid, you heal an additional minor or medium Instability at the end of the chapter. However, if he died during the chapter, you suffer a major Instability. Restriction: This Merit is only available at character creation except with an in-character explanation and Storyteller approval.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Manticore Companion",
        min_value=1,
        max_value=5,
        description="Manticores (p. 65) are the animal versions of Remade, the lab rats on whom different Divergences are tested. Mostly, they work for conspiracies, serving as spies, pets, or hunters of particularly troublesome or valuable Renegades. Sometimes, though, things don't go as planned. For whatever reason, your character has a Manticore that follows her around and that she cares for. A one-dot Manticore is basically a pet parakeet - it can do tricks and even talk, but isn't sentient and screams at the most inconvenient times. A three-dot Manticore is a smart parrot who understands nuance and meaning and may even speak several different languages and perform perfect mimicry over the phone. A five-dot Manticore is a sun conure who is nearly sapient and devoted to the Deviant. Manticores manifest one or more Variations. As a rule of thumb, purchase Variations for the Manticore as though its Merit dot rating were a Scar being used to support those Variations. Drawback: This Merit is distinct from Allies in that the Manticore is a particularly smart animal and is not truly sapient. Your character may need to take care of it with special equipment, feed it, and clean up its droppings.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Prized Experiment",
        min_value=3,
        max_value=3,
        description="Maybe your character was her Progenitor's child, who he was forced to experiment on to save her from a rare disease. Maybe high-ranking members of the conspiracy just grew attached to her as they drowned and revived her regularly, asking her to tell them what she saw 'on the other side.' Maybe she possesses powers that make her much more valuable alive. Whatever the reason, conspiracy members take great care not to hurt her, handling her with all the delicacy of a Ming dynasty vase. If a conspiracy's agent takes an action that causes the Deviant lethal damage, the conspiracy suffers a point of bashing damage to its Association (p. 233). If the damage to the Broken is aggravated, the damage to Association is lethal, instead. If the Remade dies, regardless of the cause, the current active conspiracy suffers a point of aggravated damage to its Association. This protection does not extend to the Deviant's associates. Drawback: The conspiracy will still come after your character, and it will expend considerable resources toward catching her without damaging her.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
    Merit(
        name="Voice of the Wild",
        min_value=2,
        max_value=3,
        description="Your character feels more at home communicating with animals than with other humans. Your character receives a +2 bonus to Animal Ken rolls to soothe animals and Manticores. At three dots, your character can also communicate with Manticores as though she and they shared a common language, even if the Manticore is neither sapient nor capable of speech.",
        merit_type="deviant",
        prerequisite="deviant"
    ),
]

# Create dictionary for easy lookup
deviant_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in deviant_merits}

