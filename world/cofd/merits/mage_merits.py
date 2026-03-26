from world.cofd.stat_types import Merit

# Mage-Specific Merits
mage_merits = [
    Merit(
        name="Adamant Hand",
        min_value=2,
        max_value=2,
        description="Your character has studied extensively in the Adamantine Arrow martial arts. This allows her to use combat techniques as Yantras for instant spells. When taking this Merit, choose Athletics, Weaponry, or Brawl, which your character must have three or more dots in. This Merit allows use of that Skill in combat as a reflexive Order tool Yantra, adding dice to a spell cast on subsequent turns, or to a spell cast reflexively in the same turn as the combat action. You may purchase this Merit multiple times to reflect the other styles.",
        merit_type="supernatural",
        prerequisite="adamantine_arrow_status:1,athletics:3"
    ),
    Merit(
        name="Artifact",
        min_value=3,
        max_value=10,
        description="Your character possesses an Artifact, an item from the Supernal World which is both a physical symbol of magic and a unique item independently empowered to create sorcerous effects. These items possess their own Mana stores, and have their own effective Gnosis and Arcana with which to generate effects. The base cost is equal to the highest Arcanum used, or three, whichever is higher. Each additional effect adds to the cost, but only half the highest Arcanum used (rounded up). The item can store Mana equal to twice the dot rating. The item's effective Gnosis is equal to half the dot rating, rounded up. Every Artifact is also a Path tool Yantra worth +1 dice for mages of the Path of the Artifacts' highest Arcanum.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Astral Adept",
        min_value=3,
        max_value=3,
        description="Your character is deeply in tune with her own soul, and may enter the Astral Realms without a place of power. In addition to the access methods listed on p. 249, your character may perform a ceremony to attune herself to the astral, then spend a Willpower point to allow her to meditate into the realms. Decide what form your ceremony takes when buying this Merit; many mages use a Legacy Oblation, while Sleepwalkers might require special drugs, exercises, or chants.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Between the Ticks",
        min_value=2,
        max_value=2,
        description="Your character has perceived the depths of Time, and thus can act with the utmost precision, performing an action perfectly for ideal timing, or ideal efficiency. With this Merit, once per scene you can subtract -1 from your character's Initiative for the turn to add a die to her action for the turn, or subtract a die from her action to add +1 to her Initiative.",
        merit_type="supernatural",
        prerequisite="wits:3,time:1"
    ),
    Merit(
        name="Cabal Theme",
        min_value=1,
        max_value=1,
        description="Your character is part of a deeply themed cabal. All members of the cabal are counted as having one dot higher in the Shadow Name Merit for purposes of persona Yantras, even if they do not possess the Merit at all, or if it would take Shadow Name above three dots.",
        merit_type="social",
        prerequisite="cabal_membership"
    ),
    Merit(
        name="Consilium Status",
        min_value=1,
        max_value=5,
        description="This Merit grants all the advantages of the Status Merit, except it applies to the city's Consilium. This affords certain protections and advantages under the Lex Magica. Your character's position affords her certain access to her Consilium's stores. She can access Artifacts, Imbued Items, mentors, libraries, Grimoires, and other magical resources. Consider your character's Status dots as Resources for the purpose of procuring these magical resources. The Orders are both global organizations and locally compartmentalized. If a character uses Order Status in a Caucus other than her home one, reduce her effective rating in this Merit by -1 if the Caucus is a member of the same Consilium or Assembly, -2 if it is a member of the same Convocation, and -3 if it is unrelated.",
        merit_type="social",
        prerequisite="awakened"
    ),
    Merit(
        name="Order Status",
        min_value=1,
        max_value=5,
        description="This Merit grants all the advantages of the Status Merit, except it applies to your character's local Order Caucus. This affords certain protections and advantages under the Lex Magica. Your character's position affords her certain access to her Caucus's stores. She can access Artifacts, Imbued Items, mentors, libraries, Grimoires, and other magical resources. Order Status unlocks certain Merits and advantages unique to that group. As well, certain spells are taught to Order members; learning them outside the Order can be difficult at best, dangerous at worst. Usually, Order Status comes with a position of responsibility. Finally, Seers of the Throne Status adds to the character's Resources for acquiring mundane items and services. Sleepwalkers may only buy the first dot of a single version of this Merit.",
        merit_type="social",
        prerequisite="awakened"
    ),
    Merit(
        name="Destiny",
        min_value=1,
        max_value=5,
        description="Your character's thread stands out in the skein of Fate. Like the hero of an epic she is destined for great triumphs, but she also has a Doom that hangs over her head and threatens to turn her tale into a tragedy. Each chapter, you have a pool of Destiny equal to your dots in this Merit. Each time you use a point of Destiny you may either gain the rote quality on a single mundane roll chosen before you roll the dice or reroll a single mundane action after you see the result of the roll. You may spend a point of Willpower when invoking your Destiny to affect a spellcasting roll. Drawback: Your character has a Doom. Whenever you spend Willpower to avoid the Doom, you add two dice instead of three. However, whenever you spend Willpower on an action that will further the Doom but the roll fails, you immediately regain the spent Willpower.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Dream",
        min_value=1,
        max_value=5,
        description="Once per chapter, your character can dig within her dreams for prophetic answers to primordial truths. She may enter her own dreams without a meditation roll when she sleeps, and if she has a basic understanding of something she wishes to divine from her dreams, you may use this Merit. Your character must sleep or meditate for at least four hours. Then, ask the Storyteller a yes or no question about the topic at hand. He must answer accurately, but can use 'maybe' if the answer is truly neither yes nor no. Depending on the answer, you may ask additional questions, until you have asked questions equal to your Dream Merit dots.",
        merit_type="supernatural",
        prerequisite="composure:3,wits:3"
    ),
    Merit(
        name="Egregore",
        min_value=1,
        max_value=5,
        description="This Merit reflects a deeper inclusion into Mysterium secrets than the Mysterium Status Merit normally grants. Mystery Initiation opens the doors to the communal experience of living magic the Mysterium calls the egregore. Mysteriorum Arche (-): In a teamwork spellcasting roll in which the character is participating, she does not suffer the -3 penalty to contribute without the necessary Arcanum rating, and adds an automatic success if a full participant. Mysteriorum Anima (--): Your character's full Mysterium Status applies to all Mysterium Caucuses, not just her local one. Mysteriorum Barathrum (---): She does not require physical access to any Library held by her cabal or Mysterium Caucus, and once per chapter may gain the Informed Condition regarding the local Mysterium's membership. Mysteriorum Calamitas (----): The first magical tool your character uses in a spell counts as a Dedicated Magical Tool. Mysteriorum Focus (-----): When she's in an Order Sanctum, she's considered to have a Medium sympathetic connection to all members of the Order.",
        merit_type="supernatural",
        prerequisite="mysterium_status:1"
    ),
    Merit(
        name="Enhanced Item",
        min_value=1,
        max_value=10,
        description="Your character owns an item enhanced by indefinite Duration spells, which permanently modify the item's properties. Each dot purchased reflects one dot worth of spells the item contains. This Merit is not limited to the normal five dots. However, any purchased dots beyond the fifth count as a half-dot of spells. So, an Enhanced Item with nine dots actually contains up to seven dots' worth of spells. If a spell uses multiple Arcana, use the highest to determine the cost for this Merit. Additionally, dots can be spent to directly enhance the item. A dot can provide +1 to the item's bonus as a tool, a point of Structure, or a point of Durability. This Merit can be combined with the Imbued Item Merit, but it cannot be combined with the Artifact Merit.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Familiar",
        min_value=2,
        max_value=4,
        description="Your character has been bonded to a Familiar, an ephemeral entity (a ghost, spirit, or Goetia) that has agreed to partner her in exchange for safety from bleeding Essence. Design your familiar with the rules for ephemeral entities in Chapter Six; it may be wholly in Twilight or Fettered to an item or animal. Two dots in this Merit indicate a Rank 1 entity. Four dots indicate a Rank 2 entity.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Fast Spells",
        min_value=2,
        max_value=2,
        description="Your character's Aimed spells streak out with the speed of bullets. Subjects may not apply their Defense against your Aimed Spell rolls unless they use a Supernatural power that allows them to use Defense against firearms.",
        merit_type="supernatural",
        prerequisite="firearms:2,time:1"
    ),
    Merit(
        name="Grimoire",
        min_value=1,
        max_value=5,
        description="Your character has discovered a Grimoire. If she is capable of casting the spells described, she may use the Grimoire to learn those rotes with Experiences, or cast following the Grimoire's instructions to gain the rote quality (see p. 214). Each dot in this Merit allows for the Grimoire to contain two rotes of any Arcanum rating.",
        merit_type="mental",
        prerequisite="awakened"
    ),
    Merit(
        name="Hallow",
        min_value=1,
        max_value=5,
        description="Your character has secured a Hallow, a nexus of magical energies that seeps Mana into the world. A Hallow produces one Mana per dot in the Merit per day. When choosing this Merit, determine how the Hallow leaks Mana into the world. Mana that is not harvested congeals quickly into tass. Left to its devices, the Hallow can store three times its dot rating in tass before it becomes 'dormant' and stops producing Mana until all of the tass is harvested. As with Sanctum and Safe Place, a Hallow can be shared between a cabal.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="High Speech",
        min_value=1,
        max_value=1,
        description="The character can use High Speech as a Yantra in spellcasting (see p. 120).",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Imbued Item",
        min_value=1,
        max_value=10,
        description="An Imbued Item is an item storing a spell that does not have an indefinite duration, and Mana with which to cast that spell. When creating an Imbued Item for your game, choose a spell. The item contains that spell, and a user (even a Sleeper) may trigger the spell if she knows the method of triggering. Each dot purchased reflects one dot worth of the spell the item contains. If a spell uses multiple Arcana, use the highest to determine the cost for this Merit. By default, an Imbued Item has a single point of Mana. Points in this Merit (in excess of those required by the imbued spell) purchase a 'battery' of two additional Mana each. This Merit can be combined with the Enhanced Item Merit, but it cannot be combined with the Artifact Merit.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Infamous Mentor",
        min_value=1,
        max_value=5,
        description="Your character's Mentor is of particularly strong repute. This may be negative or positive. When taking this Merit, determine the Mentor's Order and Consilium Status. They should be close to the Mentor dot rating. As well, choose Social Merits equal to twice the Infamous Mentor dots. Your character can access these Merits and Status, so long as she's willing to name-drop her Mentor and live with the consequences. Most characters will grudgingly acquiesce to a Mentor's Status, but will later look down upon the student for leaning on the Mentor's reputation.",
        merit_type="social",
        prerequisite="mentor:1"
    ),
    Merit(
        name="Lex Magica",
        min_value=2,
        max_value=2,
        description="The laws of the Pentacle are symbolic concepts designed by people who make symbols real. A thearch acting in an official, titled capacity gains certain advantages with this Merit: First, add her Silver Ladder Status or Consilium Status (whichever she's acting with) to her Doors when a character attempts to outmaneuver her socially. Second, characters cannot use Willpower to increase dice pools on Social actions or magic which would influence her behavior. Lastly, your character may use her Silver Ladder Status or Consilium Status (whichever is higher) as a Yantra in spells directly enforcing the Lex Magica's laws. The dice bonus for the Yantra is half the Merit dots used, rounded up.",
        merit_type="supernatural",
        prerequisite="silver_ladder_status:1"
    ),
    Merit(
        name="Mana Sensitivity",
        min_value=1,
        max_value=1,
        description="Your character's awakened eye has sensed Mana enough that her mundane senses have begun picking up the cues of its presence. Hallows and stored Mana trigger her Peripheral Mage Sight, even without an active magical effect.",
        merit_type="supernatural",
        prerequisite="prime:1,wits:3"
    ),
    Merit(
        name="Masque",
        min_value=1,
        max_value=5,
        description="The Guardians must adopt Masques, personas, in order to detach from the grim necessities of their work and stay in cover. Their ancient practices allow these Masques to become different people almost entirely. Adopting a Masque requires spending a point of Willpower, which cannot be replenished so long as the character maintains the identity. Shedding a Masque requires a full minute to get 'out of character.' Identity (-): Choose a Virtue and Vice different than that of your character. While in the Masque, your character benefits from those traits instead of her own. Competency (--): Choose Skill Specialties equal to the Masque Merit dots. Your character uses those Specialties instead of her own while in the Masque. Diffusion (---): Choose a new Signature Nimbus. While in the Masque, your character uses that Nimbus instead of her own. The Code (----): Choose two Acts of Hubris your character would normally suffer. While in the Masque, your character does not risk Wisdom for those acts. Immersion (-----): Choose up to five Merit dots. When your character dons her Masque, she gains access to these Merits.",
        merit_type="style",
        prerequisite="guardians_of_the_veil_status:1"
    ),
    Merit(
        name="Mystery Cult Influence",
        min_value=3,
        max_value=5,
        description="Your character has influence over a Mystery Cult without actually being a subordinate member. Perhaps your character is a 'power behind the throne' or even worshiped as a deity. Your character benefits from the same level of Mystery Cult Initiation, without having to be tied to the cult. This means fewer responsibilities to the cult, plausible deniability if they're revealed, and the ability to step away at any time.",
        merit_type="social",
        prerequisite="awakened"
    ),
    Merit(
        name="Occultation",
        min_value=1,
        max_value=3,
        description="Your character is unnoticeable and inoffensive on a mystical level. Any time a character tries to read your character's aura, or otherwise use magic to discern bits of truth within her, subtract your Merit dots from their pool. This Merit allows a mage to hide that, to metaphysically sweep that under a rug. Your character's Signature Nimbus is faint, vague, and couched in more symbolism and oblique references than other mages'. When someone attempts to scrutinize her Nimbus to identify her or track her, subtract your Merit dots from their rolls. The Withstanding level of sympathy for spells targeting the character has a minimum of her Occultation dots. Drawback: If your character ever gains the Fame Merit, or becomes noticed by the public at large, you can lose this Merit.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Potent Nimbus",
        min_value=1,
        max_value=2,
        description="Your character's Nimbus has distinct and powerful effects on witnesses. At one dot, add two to your character's effective Gnosis when determining her Nimbus Tilt. At two dots, add four to her effective Gnosis for that purpose. Additionally, add your dots in this Merit to any rolls to flare your character's Nimbus.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Potent Resonance",
        min_value=2,
        max_value=2,
        description="Your character's Signature Nimbus is particularly overbearing. Whenever a character scrutinizes her Signature Nimbus with Mage Sight, he's subject to the effects of her Immediate Nimbus and its corresponding Tilt.",
        merit_type="supernatural",
        prerequisite="gnosis:3"
    ),
    Merit(
        name="Prelacy",
        min_value=1,
        max_value=4,
        description="A successful Seer who has served her patron Exarch well can cast spells in his name. She hears the Tyrants' voices in her sleep. She understands their demands directly. A black iron portal forms deep within her Oneiros, and her daimon, the Goetia representing her drive to further herself, becomes twisted by the Exarch's agenda. Chosen Vessel (-): your character gains the Persistent Mystery Commands Condition. Sword (--): The character may use the patron Exarch's symbolism as a patron Yantra in spellcasting, worth half her Prelacy dots in dice (round up). Crown (---): The character gains an Attainment based on her Exarch's symbolism. Temple (----): If one of your character's soul stones is incorporated into a Demesne, the Demesne becomes a Supernal Verge keyed to her Exarch. Drawback: Once the Exarchs have given a command, they expect it to be carried out without delay. The character may only earn Arcane Beats from their other Obsessions in a chapter when they have already earned one for following the one granted by Mystery Commands.",
        merit_type="style",
        prerequisite="seers_of_the_throne_status:3"
    ),
    Merit(
        name="Sanctum",
        min_value=1,
        max_value=5,
        description="Your character has a Sanctum, in which she can safely practice her art away from prying eyes. This might be a dark cave, an apartment, a pocket dimension, or any other secure location she can claim. This Merit must be tied to a Safe Place Merit, and similarly can be shared within a cabal. Add her Merit dots to her Gnosis within the Sanctum for determining spell control. She can leave the Sanctum and retain those benefits on previously cast spells. But if she's exceeded her Gnosis and adds any additional, controlled spells, the benefit goes away and she must Reach as if she'd cast each of those spells without the benefit. For an additional three dots (which do not count toward the 1-5 limit), your character's Sanctum includes a Demesne.",
        merit_type="supernatural",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Shadow Name",
        min_value=1,
        max_value=3,
        description="Your character has a particularly developed magical persona, and is almost a different person when acting as a mage than in her mundane life. When purchasing this Merit, determine the Shadow Name and its symbolism. The character may use those symbols as a persona tool in spellcasting, worth this Merit's dots. Additionally, apply dots in this Merit as a Withstand rating to spells that attempt to identify her or cast on her using the Sympathetic Range Attainment when in her mundane persona, to spells using the Temporal Sympathy Attainment targeting a time when she was in her mundane persona, and as a dice penalty to mundane skill rolls relating to identifying her as the same person as her magical self.",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Techne",
        min_value=2,
        max_value=2,
        description="Your character uses Libertine practices in order to use cultural magical styles, sciences, and art forms as magical tools. Pick a focus for your character - for example, computer networking. Your character treats the focus as an Order tool for the Free Council as long as she includes it during spellcasting, and may further treat the presence of Sleepers engaging in the focus as a separate Order tool, as long as the spell is not obvious. If all mages casting a spell under the teamwork rules have this Merit representing the same focus, the leader's spellcasting roll gains 8-Again. This Merit may be bought multiple times to represent different fields of study.",
        merit_type="supernatural",
        prerequisite="free_council_status:1"
    ),
    Merit(
        name="Astral Intruder",
        min_value=3,
        max_value=3,
        description="Make a Clash of Wills to meditate into the Oneiros of a mage whose soul stone you possess, instead of your own",
        merit_type="supernatural",
        prerequisite="astral_adept:1,resolve:3"
    ),
    Merit(
        name="Awakened Status",
        min_value=1,
        max_value=5,
        description="Hold status in a Consilium or Order. You may temporarily requisition dots of Alternate Identity, Retainer, Imbued Item, Artifact, Grimoire, Mentor, Hallow, Sanctum, Library, Advanced Library, Safe Place, Familiar, and Resources",
        merit_type="social",
        prerequisite="awakened"
    ),
    Merit(
        name="Broad Dedication",
        min_value=1,
        max_value=1,
        description="Instill your nimbus into a specific Yantra that aligns with your spellcasting, making your Dedicated Tool any kind of Yantra",
        merit_type="supernatural",
        prerequisite="prime:1"
    ),
    Merit(
        name="Cognoscente",
        min_value=2,
        max_value=2,
        description="Your character has perfected the art of scribing grimoires. Anyone casting from his tomes may do so without the doubled ritual casting time. He may also imprint his own signature nimbus into the rote imago when scribing the spell. Doing so causes the rote to show his own nimbus instead of hiding the caster's. Once per story, gain +2 to a Social roll that relies on this fame and enjoy the benefits of Occultation ---",
        merit_type="supernatural",
        prerequisite="prime:3,[academics:2,occult:2]"
    ),
    Merit(
        name="Daimonomikon",
        min_value=1,
        max_value=5,
        description="Your character possesses a Daimonomikon for a particular legacy. Each dot corresponds to the Attainment within the Legacy that can be learned from the Daimonomikon",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Dominant Soul",
        min_value=1,
        max_value=5,
        description="When your character has another mage's soul stone you can counterspell any Arcanum from its owner, applying Merit dots as your Arcanum rating. If used as a Yantra during a Prime dispellation, reduce Withstand by dots in this Merit",
        merit_type="supernatural",
        prerequisite="composure:3"
    ),
    Merit(
        name="Echo Chamber",
        min_value=4,
        max_value=4,
        description="See flashbacks of a soul stone's owner. Gain exceptional success off 3 dice for active mage sight to investigate a mystery based on the soul stone's Path. Once per story, meditate on the soul stone to ask yes or no questions about the mystery",
        merit_type="supernatural",
        prerequisite="empathy:2"
    ),
    Merit(
        name="Enriched Item",
        min_value=2,
        max_value=4,
        description="Your character owns an item with a natural enhancement or one permanently altered through multiple uses of the same enchantment",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Epiphany Stone",
        min_value=4,
        max_value=4,
        description="Spend Mana while using active mage sight to roll Clash of Wills to check if you are under some form of illusion, hallucination, forced astral journey or other supernatural power that separates you from reality",
        merit_type="supernatural",
        prerequisite="[dream:1,astral_adept:1],mind:2"
    ),
    Merit(
        name="Fire Keeper",
        min_value=1,
        max_value=1,
        description="Environmental causes can't fully snuff flames in your presence unless you will it",
        merit_type="supernatural",
        prerequisite="ancient_obrimos"
    ),
    Merit(
        name="Fluent High Speech",
        min_value=3,
        max_value=3,
        description="You may converse at length in High Speech. Persuasion and Intimidation rolls with mages and supernal entities that use the High Speech gain +2, and Expression rolls are not reduced to chance dice. Participating in a supernal summoning reduces the target number by two",
        merit_type="supernatural",
        prerequisite="awakened,presence:4,expression:3"
    ),
    Merit(
        name="Invested Mana",
        min_value=1,
        max_value=10,
        description="Your character owns tass invested with Mana equal to dots in this Merit. The Mana stored in these vessels doesn't count toward your character's maximum Mana pool",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Legacy Attainments",
        min_value=1,
        max_value=3,
        description="Your character has joined a Legacy and learned some of its magical secrets. Each dot in this Merit represents one Attainment learned from the Legacy. Prerequisites and experience costs for Legacy Attainments are described on p. 188",
        merit_type="supernatural",
        prerequisite="gnosis:2"
    ),
    Merit(
        name="Mana Retention",
        min_value=3,
        max_value=3,
        description="Your character's soul clings to Mana. Add two to her maximum Mana. Additionally, she may spend a point of Willpower instead of allowing a point of Mana to bleed from her Pattern each turn",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Mana Sensitivity",
        min_value=1,
        max_value=1,
        description="Your character's awakened eye has sensed Mana enough that her mundane senses have begun picking up the cues of its presence. Hallows and stored Mana trigger her Peripheral Mage Sight, even without an active magical effect",
        merit_type="supernatural",
        prerequisite="prime:1,wits:3"
    ),
    Merit(
        name="Path Natural",
        min_value=1,
        max_value=1,
        description="Choose one of your two Path's Inferior Arcana. You may spend Arcane Experiences on that Arcanum",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Prime Speaker",
        min_value=1,
        max_value=1,
        description="Your Shadow Name has power in the Temenos. When you use your Shadow Name, Divine and Mythological entities from your Shadow Name's mythology treat the initial impression in Social Maneuvering as one step better. If your Shadow Name reflects a well-known Mythological or Divine entity, enjoy +2 bonus to summon said Goetia",
        merit_type="supernatural",
        prerequisite="shadow_name:1"
    ),
    Merit(
        name="Sky's Whispers",
        min_value=1,
        max_value=1,
        description="Read the open sky as an instant action to predict the day's weather and take +3 to endure it",
        merit_type="supernatural",
        prerequisite="ancient_acanthus"
    ),
    Merit(
        name="Soul Dealer",
        min_value=1,
        max_value=5,
        description="Your character has contacts in the Black Market soul trade or is a soul trader himself. Once per story your character can obtain a soul stone as though you were a member of any order status one for one to dots in this merit",
        merit_type="social",
        prerequisite="streetwise:3"
    ),
    Merit(
        name="Soul Stone",
        min_value=1,
        max_value=2,
        description="Your character owns another Mage's soul stone. One dot is equal or lesser Gnosis to your own. 2 dots is greater",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Spirit Warden",
        min_value=2,
        max_value=2,
        description="Spirits must spend Willpower to attack you for a scene",
        merit_type="supernatural",
        prerequisite="ancient_thyrsus"
    ),
    Merit(
        name="Stalwart Soul",
        min_value=1,
        max_value=2,
        description="A soul stone created by you gains Durability equal to twice your dots in this merit and gains the same bonus to withstand against spells that would harm or destroy it",
        merit_type="supernatural",
        prerequisite="composure:3"
    ),
    Merit(
        name="Supernal Taxonomy",
        min_value=2,
        max_value=2,
        description="You possess a deep understanding of Active Mage Sight. When observing phenomena in either similar effect or origin to one already scrutinized she can recognize the similarity",
        merit_type="mental",
        prerequisite="intelligence:2,occult:3"
    ),
    Merit(
        name="Supernal Watcher",
        min_value=2,
        max_value=4,
        description="You have gained the attention of a supernal entity at rank 1 for 2 dots and rank 2 for 4 dots. When summoning your watcher you only need 5 successes, they appear when using Active mage sight and you may use it as a Path tool Yantra",
        merit_type="supernatural",
        prerequisite="awakened"
    ),
    Merit(
        name="Trail Walker",
        min_value=2,
        max_value=2,
        description="Double your rate of travel across forests",
        merit_type="physical",
        prerequisite="ancient_mastigos"
    ),
]

# Create dictionary for easy lookup
mage_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in mage_merits}
