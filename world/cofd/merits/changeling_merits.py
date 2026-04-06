from world.cofd.stat_types import Merit

# Changeling-Specific Merits
changeling_merits = [
    Merit(
        name="Acute Senses",
        min_value=1,
        max_value=1,
        description="The changeling's senses are especially acute, even by the standards of high Clarity. Her sight, hearing, and sense of smell operate at twice the distance and accuracy of mortal senses. She can't see in pitch darkness (for that, she needs Contract magic), but she can see much more clearly than humans can. Add the character's Wyrd rating as dice to any perception-based rolls. This bonus supersedes the one normally granted by maximum Clarity. Also, add the bonus to any rolls made to remember or identify details.",
        merit_type="changeling",
        prerequisite="wits:3"
    ),
    Merit(
        name="Arcadian Metabolism",
        min_value=2,
        max_value=2,
        description="Your character is particularly well-suited to time in Arcadia and the Hedge. Maybe he was abducted at an early age and knows more of Arcadia than Earth, or he glutted himself on rare goblin fruit for the entirety of his captivity. In the Hedge, increase his natural healing rates: Bashing damage heals at one point per minute and lethal damage heals at one point per day. Aggravated damage healing is unaffected.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Brownie's Boon",
        min_value=1,
        max_value=1,
        description="Like the shoemaker's elves, your character completes tasks with a casual disregard for time. Reduce the interval for any mundane extended action roll she makes while no one watches her by half. The character may spend a Glamour to halve the interval again, working at four times her normal speed for that roll. Exceptional success on an individual roll can decrease the time it takes to complete that roll to an eighth of the usual interval, if the player chooses the time reduction benefit.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Cloak of Leaves",
        min_value=1,
        max_value=3,
        description="Your character has learned to embrace his worries and fears, and use them as a shield against the supernatural. Anyone using a supernatural ability to cause damage or inflict physical Tilts upon the character suffers a penalty equal to his dots in this Merit. Supernatural abilities include Contracts, kith blessings, vampire Disciplines, mage spells, and any other innate ability used by a supernatural creature.",
        merit_type="supernatural",
        prerequisite="mantle:autumn:3"
    ),
    Merit(
        name="Cold Hearted",
        min_value=3,
        max_value=3,
        description="Your character has taken her pain, and the pain of others, and crafted them into a barrier against further suffering. She may spend a Willpower to ignore the effects of a single Clarity Condition once per scene. She still has the Condition and doesn't heal any Clarity damage, but she does not suffer the ill effects of the Condition. If her actions during the scene would resolve the Condition, it resolves normally.",
        merit_type="changeling",
        prerequisite="mantle:winter:3"
    ),
    Merit(
        name="Court Goodwill",
        min_value=1,
        max_value=5,
        description="Court Goodwill represents a changeling's influence and respect in a court that isn't his own. It allows him to have serious ties to as many courts as he likes, in addition to the one he has sworn magical allegiance to. Each instance of Court Goodwill represents a specific court, but you may take the Merit as many times as there are courts available. A changeling gains access to a court's Mantle effects at two dots lower than his dots in that court's Goodwill. Dots in Court Goodwill also function like dots in the Allies Merit, except that attempts to block another character's Merit use fail automatically against a character with any Mantle dots in the same court. Finally, each court in which a character has Court Goodwill comes with a single dot of Mentor, a changeling who serves as the character's court liaison.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Defensive Dreamscaping",
        min_value=2,
        max_value=2,
        description="Your character is adept at manipulating the dream in a hand-to-hand fight. A gust of wind carries her out of the way of an attack, an eidolon leaps in front of a bullet for her, or her opponent's blade dulls when it strikes. Add half her Wyrd (rounded down) to her Defense in dreams.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Diviner",
        min_value=1,
        max_value=5,
        description="Your character can dig within his dreams for prophetic answers to primordial truths, as all humanity is and has always been connected through its dreams via the Dreaming Roads. He must enter a dream state, through either the Gate of Ivory or Horn, into his own Bastion. Then, he may ask the Storyteller a yes or no question about something he wishes to divine from his dreams. She must answer accurately, but can use 'maybe' if the answer is truly neither yes nor no. Depending on the answer, you may ask additional, related questions, up to your Merit dots. You can ask that many total questions per chapter.",
        merit_type="changeling",
        prerequisite="composure:3,wits:3"
    ),
    Merit(
        name="Dream Warrior",
        min_value=1,
        max_value=1,
        description="Your character's extensive training in oneiromancy allows her to benefit from the flexibility of the dream. By blending dreamscaping and martial techniques, strikes land faster as the dream bends to aid her blows. Whenever you allocate any successes generated with a Brawl or Weaponry attack (depending on which Specialty you have) to a subtle oneiromantic shift, gain one bonus success to spend on that shift as long as you spend it to impact the fight in some direct way. If you have a Specialty in both Skills, you gain these benefits on both types of attack.",
        merit_type="changeling",
        prerequisite="wyrd:2,presence:3,[brawl_specialty:1,weaponry_specialty:1]"
    ),
    Merit(
        name="Dreamweaver",
        min_value=3,
        max_value=3,
        description="As his connection to the Wyrd grows stronger, so does the changeling's control over dreams. Once per scene, you may spend a Willpower point to make three successes count as an exceptional success on a dreamweaving roll (p. 217).",
        merit_type="changeling",
        prerequisite="wyrd:3"
    ),
    Merit(
        name="Dull Beacon",
        min_value=1,
        max_value=5,
        description="Your character's Mask is far less obtrusive when she drops it. Reduce her Wyrd by her Dull Beacon dots when determining the distance at which she alerts fae creatures and opens Hedge gateways when dropping her Mask (p. 83). If this would effectively reduce her to Wyrd 0, she no longer opens gates or alerts fae creatures at all until her Wyrd increases.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Elemental Warrior",
        min_value=1,
        max_value=5,
        description="Choose one physical element. (*) Wind Cuts to the Bone: Exceptional success on elemental attack on threshold of three instead of five. (**) Defensive Flurry: Dodging adds half Wyrd (rounded down) as bonus dice and can apply against Firearms. (***) Hungry Leaping Flames: Spend Glamour to make elemental attack, increasing range by ten yards and potentially wreaking environmental effects. (****) Antaean Endurance: While immersed in or fortified on element, add half Wyrd as temporary Health and bonus dice to resist fatigue, poison, unconsciousness. (*****) Wrath of Titans: Spend Glamour to inflict Blinded, Deafened, or Knocked Down Tilts with strikes for the scene",
        merit_type="style",
        prerequisite="[dexterity:3,wits:3],[brawl:2,firearms:2,weaponry:2],elemental_weapon_or_primal_glory_or_elemental_seeming"
    ),
    Merit(
        name="Enchanting Performance",
        min_value=1,
        max_value=3,
        description="(*) Limerick: Hurl an insult and roll Presence + Expression - Composure to penalize a target's Social rolls on others by your successes for the scene. (**) Poem: When you open a Door by an expressive performance, spend Glamour to open another. (***) Sonnet: Spend Glamour to deliver a performance with an Expression roll, taking the rote quality. Success renders an audience member Inspired",
        merit_type="style",
        prerequisite="presence:3,expression:3"
    ),
    Merit(
        name="Fae Mount",
        min_value=1,
        max_value=5,
        description="Your character has befriended a creature of the Hedge to serve as his steed. Through a special song or gesture, the mount comes to its master anywhere in the Hedge, except to the Hollow of a changeling who prohibits it. Additionally, each dot of this Merit allows the creature one special ability. The mount is a creature of the Hedge with abilities that scale with the Merit rating, from simple transportation to combat assistance and special supernatural abilities.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Faerie Favor",
        min_value=3,
        max_value=3,
        description="The Gentry's promises bind them to a greater degree than those of the Lost do, and your character possesses such a promise. She is entitled to a favor from one of the True Fae. She may have gained this favor through anything from knowing a clever riddle to a dark deed done at the cost of another changeling's freedom. However she earned it, she has a bauble, song, or phrase that represents the favor, and when she breaks, sings, or utters it, the True Fae appears. The favor can be many things: the capture of a rival the changeling has tracked to his Hollow, a week of freedom from a Huntsman on the changeling's heels, safe passage to somewhere in the Hedge or mortal world, etc. After the character calls in the favor, she gains dots in any combination of Merits appropriate to the power of the Gentry. Drawback: The character gains the Notoriety Condition among the Lost when she calls in the favor.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Fair Harvest",
        min_value=1,
        max_value=2,
        description="Your character favors a particular flavor of Glamour. Choose a specific emotion when taking this Merit. With one dot, any rolls to harvest that emotion enjoy the 8-again quality. Rolls to harvest any other emotion do not benefit from the 10-again quality. At two dots, harvesting the favored emotion becomes even more efficient and effective.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Firebrand",
        min_value=2,
        max_value=2,
        description="Your character has the spirit of Summer within him, and channels that wrath into others. Once per scene, when your character goads someone into a fight, he regains a single Willpower point.",
        merit_type="changeling",
        prerequisite="mantle:summer:3"
    ),
    Merit(
        name="Frightful Incantation",
        min_value=4,
        max_value=4,
        description="Can use Mantle and Mein in place of a hecatomb, opening Doors up to Mantle rating each story",
        merit_type="changeling",
        prerequisite="hedge_sorcerer:1,mantle:2,resolve:2"
    ),
    Merit(
        name="Gentrified Bearing",
        min_value=2,
        max_value=2,
        description="Your character was molded in the image of her Keeper, stole some essential spark of its fire, or learned to emulate its otherness. Regardless of how she obtained this mixed blessing, hobgoblins tend to mistake her for a True Fae - if only for a moment. When dealing with hobgoblins, Intimidation rolls add the character's Wyrd rating in dice, to a maximum of +5. While most hobgoblins don't look too closely at a True Fae, a wise changeling shows caution with her demands. Even a successful ruse is unlikely to fool the same creature twice.",
        merit_type="changeling",
        prerequisite="wyrd:2"
    ),
    Merit(
        name="Glamour Fasting",
        min_value=1,
        max_value=1,
        description="Your character can endure without Glamour longer than others. As long as he has Willpower remaining, he doesn't suffer from deprivation when he drops to Glamour 0 (or below his Wyrd, for high-Wyrd changelings) until one full chapter has passed since he last had any Glamour.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Goblin Bounty",
        min_value=1,
        max_value=5,
        description="The Lost has access to a regular bounty of goblin fruit and oddments. She may personally cultivate them, or scavenge them from a secret place in the Hedge that only she knows about. She has access to three times her dots in this Merit of common goblin fruits and oddments per chapter. Depending on her Wyrd, she may not be able to carry them with her all at once, but the rest are stored somewhere safe and do not require a special scene to access.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Grounded",
        min_value=3,
        max_value=3,
        description="Your character's connection to the Spring Court makes him sure of himself and his perceptions. Even when he is at his weakest and most vulnerable, the verdant life of Spring protects him. He has an armor rating of 1 against all Clarity attacks that deal mild damage.",
        merit_type="changeling",
        prerequisite="mantle:spring:3"
    ),
    Merit(
        name="Hedge Brawler",
        min_value=2,
        max_value=2,
        description="Your character is adept at fighting within the Hedge. You may take a dice penalty on a violent action designated for Hedgespinning between -1 and -3 to gain that number of extra successes if the action is successful. You can only use these successes for shaping Hedge details; this can't turn a normal success into an exceptional one.",
        merit_type="changeling",
        prerequisite="brawl:2"
    ),
    Merit(
        name="Hedge Sorcerer",
        min_value=4,
        max_value=4,
        description="You can perform Hedge Sorcery rituals",
        merit_type="changeling",
        prerequisite="occult:1,mentor:2"
    ),
    Merit(
        name="Hedgewise",
        min_value=2,
        max_value=2,
        description="+2 to ken even magically concealed Hedgeways, and 9-Again to Hedgespinning",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Hedge Duelist",
        min_value=1,
        max_value=3,
        description="These maneuvers work in the Hedge. (*) Thousand Falling Leaves: Half your normal damage on an attack to inflict -1 Defense on the target. (**) Emerald Shield: Receive 2/0 magical Armor. (***) Bite Like Thorns: Add a foe's wound penalties as bonus attack dice",
        merit_type="style",
        prerequisite="[presence:2,manipulation:2],[brawl:2,weaponry:2],social_skill:2"
    ),
    Merit(
        name="Hedge Sense",
        min_value=1,
        max_value=1,
        description="The character is especially skilled at finding her way in the Hedge. Gain a two-die bonus to all rolls to navigate the Hedge, and to find Icons, food, shelter, or goblin fruit there.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Hob Kin",
        min_value=1,
        max_value=1,
        description="Your character has established a kind of kinship with hobgoblins. It may be a matter of resemblance to a True Fae they fear, or something about his kith that encourages this behavior, but they show him a respect generally unheard of by the Lost. It isn't much like the respect of friends or peers, but they treat him less ruthlessly than they do outsiders. Increase his starting impression with non-hostile hobgoblin characters by one level on the chart for Social maneuvering. Additionally, if the character has the Hollow Merit, he may take the enhancement Hob Alarm.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Hollow",
        min_value=1,
        max_value=5,
        description="While Safe Place represents a mundane-but-secure lair outside the Hedge, Hollow is your character's secret, private bit of real estate inside the Hedge. It may be something as simple as a closet door that opens into a quiet, hollowed-out tree, or as elaborate as a knock that opens any unlocked door into a lavish, gothic mansion. These locations are as varied as the Hedge itself. The character has cleared away any imposing Thorns that might cause trouble in her pocket of personal reality. While a changeling is inside her Hollow, any attempts to learn her personal information suffer the Merit's rating as a dice penalty, as if she had the Anonymity Merit at an equal rating. Attempts to pursue or track her, both supernatural and mundane, suffer the same penalty. Only an entity whose Wyrd exceeds the Merit's rating may force the entrance to the Hollow. Additionally you can take up to your Hollow merit rating in benefits.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Lethal Mien",
        min_value=2,
        max_value=2,
        description="The Hedge warped some element of your character's fae mien, and left him with wicked nails, sharp teeth, or some other offensive trait. The changeling can inflict lethal damage while unarmed. If another power already gives him the capacity for lethal blows, such as the Beast seeming blessing, add one to his unarmed weapon modifier instead. The character may choose whether to use the benefit of these claws, fangs, spurs, or other dangerous element at will.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Librarian",
        min_value=3,
        max_value=3,
        description="Your impression level is one higher at the first social interaction with librarians and scholars, you keep or lose the bonus depending on your behaviour on subsequent encounters. Gain two additional dice on rolls about researching written accounts",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Mantle",
        min_value=1,
        max_value=5,
        description="When a changeling joins a court, she accepts all its blessings and embodies it, the same way she does her own seeming and kith. Mantle represents the mystical connection a changeling has to the elements and emotions of her chosen court. As her Mantle rises, she becomes a better representation of what it is to be a courtier. A changeling with a high Mantle embodies the ideals of the court, and others who belong to the court recognize her dedication and give her respect, even if it's grudging. As a character's Mantle increases, her fae mien changes to reflect it, showing both figurative and literal signs of the season. The Mantle demands a level of respect. Add your character's Mantle rating to any Social rolls you make against other members of her court and characters with the appropriate Court Goodwill. A character may learn the Contracts of her court as long as she meets the Contract's Mantle prerequisite. Members of each court gain an additional way to harvest Glamour. Each court also grants its own specific benefits at each Mantle rating.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Manymask",
        min_value=3,
        max_value=3,
        description="A changeling is usually stuck with the same Mask he left the Hedge with, an immutable combination of remembered human traits. Some changelings develop control over the appearance of their Masks. The character may spend a point of Glamour to change his Mask permanently. He may make one change per chapter per dot of Wyrd he possesses to any of the following: eye color, hair color, facial structure, or skin tone; or he may remove notable scars or other features such as birthmarks, freckles, etc. At Wyrd 5+ he may create an entirely new Mask once per chapter by spending one Glamour, mostly unbeholden to his existing features. While he can even change the sex of his Mask, height and build remain immutably tied to the shape that lies beneath.",
        merit_type="changeling",
        prerequisite="wyrd:2,manipulation:3"
    ),
    Merit(
        name="Magic Dreams",
        min_value=5,
        max_value=5,
        description="May use Hedge Sorcery in dreams, substituting oneiromancy for Hedgespinning",
        merit_type="changeling",
        prerequisite="hedge_sorcerer:1,occult:3"
    ),
    Merit(
        name="Market Sense",
        min_value=1,
        max_value=1,
        description="Understanding the value of a product is hard enough in the mortal world, but in the Hedge, relative worth is even more questionable. How does one weigh the importance of a dozen cherished memories against a music box that only plays near ghosts? Goblins make all sorts of strange requests in exchange for Contracts, but your character knows how to navigate these exchanges better than others. Once per chapter, you may reduce your character's Goblin Debt by one.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Noblesse Oblige",
        min_value=1,
        max_value=3,
        description="Your character knows how to harness the power of his Mantle to inspire others. Any time your character is in charge of a group of people who share his court, either through Mantle or Court Goodwill, he can grant benefits to the group (but not to himself) for a scene by spending a Willpower point. The benefit conferred depends on the court. Drawbacks: Being the leader is not easy. It means that you are responsible for those under you and they look to you for guidance. Those under your character's command gain a two-die bonus to Social rolls against him.",
        merit_type="changeling",
        prerequisite="mantle:1"
    ),
    Merit(
        name="Blood Liege",
        min_value=3,
        max_value=3,
        description="Swear yourself to a vampire, gain a two dot mentor. Once a lunar month, the vampire may give you a relatively task to be completed in good faith. May cancel this merit to cause a huntsman or true fae to divert their attention to the vampire",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Pandemoniacal",
        min_value=1,
        max_value=3,
        description="The changeling is more adept at inciting Bedlam than her fellows. Add the Merit's rating as a dice bonus to any rolls she makes to incite Bedlam (see p. 110).",
        merit_type="changeling",
        prerequisite="wyrd:6"
    ),
    Merit(
        name="Parallel Lives",
        min_value=3,
        max_value=3,
        description="The changeling is deeply connected to his fetch. Each experiences occasional flashes of the other's emotional state when something affects one of them strongly, and gains two bonus dice to use Empathy or magic to read the other's intentions, or to enter his Bastion. By spending a point of Willpower, either can ride along with the other's senses for a number of minutes equal to his Wyrd rating, losing his Defense and the ability to perceive the world around him as he does. Either of them can also spend a Willpower point to send a vague message via thought to the other; it comes across not in words, but fleeting impressions and snippets of images, and can only encompass fairly simple ideas. A fetch could warn his changeling of a Huntsman's impending arrival, but without any detail about when or how. Whenever the fetch uses this connection to make the changeling's life more dangerous or inconvenient, gain a Beat.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Rigid Mask",
        min_value=3,
        max_value=3,
        description="For your character, the protection of the Mask extends far beyond the usual mortal camouflage. Perhaps she can sense the subtle magic that turns her smile into her Mask's smile, or her true face is strongly connected to the one that lets her interact with humanity. No one fooled by the Mask knows when she's lying or what she's feeling unless she allows it. Mortals automatically fail rolls to notice these things, as do polygraphs and other mundane lie-detecting devices. Supernatural creatures must engage in a Clash of Wills to notice her lies. Drawback: Intentionally dropping your character's Mask deals her a point of lethal damage in addition to the normal rules.",
        merit_type="changeling",
        prerequisite="subterfuge:2"
    ),
    Merit(
        name="Stable Trod",
        min_value=1,
        max_value=5,
        description="Your character's freehold has secured and maintained a trod with a rating equal to his Merit dots in Stable Trod. The trod bestows two additional advantages to those who have Hollows along it or travel it frequently: Hollows along the trod gain an extra one-dot Hollow enhancement. The enhancement is the same for all such Hollows. This can benefit a number of Hollows equal to the Stable Trod Merit rating. This enhancement can bring the number of Hollow enhancements above the normal maximum a Hollow's rating allows. Goblin fruit trees cultivated along the trod produce additional fruit. You may roll your character's dots in Stable Trod as a dice pool once per story. Each success produces one additional generic fruit, which contains a point of Glamour.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Token",
        min_value=1,
        max_value=10,
        description="Your character or motley has one or more tokens - mystical items suffused with the power and danger of Faerie. Perhaps she made off with her Keeper's most prized possession as she fled out of spite, or found that twigs from the Hedge caught in her clothes became magical matchsticks upon her escape. Perhaps she traded away her name for an enchanted mirror at a Goblin Market. Perhaps she took the riding crop as a trophy when she killed the Huntsman, and now she's driven to hunt her own kind. Whatever the case, choose one or more tokens with a total dot rating equal to her rating in this Merit. She may have more than five dots in this Merit, but no single token may have a rating higher than five. You can purchase an oath-forged token by adding one dot to its effective rating; thus, you can't purchase a five-dot oath-forged token with this Merit. You can purchase a stolen token at an effective rating of one dot lower than the token's rating.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Touchstone",
        min_value=1,
        max_value=5,
        description="Your character has multiple Touchstones. Each dot in the Touchstone Merit allows for an additional Touchstone. Write each one beside the next available box to the right of the rightmost box with an associated Touchstone. If the last Clarity box already has a Touchstone, you cannot purchase this Merit again. For more on Touchstones, see p. 98. Drawbacks: Losing attachment with Touchstones speeds the loss of Clarity. As well, if your character's last Touchstone dies or is destroyed, his memories and nightmares of his durance intensify.",
        merit_type="changeling",
        prerequisite="changeling"
    ),
    Merit(
        name="Warded Dreams",
        min_value=1,
        max_value=3,
        description="Whether through active mental discipline or natural stubbornness, your character's dream Bastion is particularly well fortified against intrusion. Each dot in Warded Dreams increases the Bastion's Fortification rating by one.",
        merit_type="changeling",
        prerequisite="resolve:@dots"
    ),
    Merit(
        name="Workshop",
        min_value=1,
        max_value=5,
        description="Your character maintains, within her Hollow, a variety of equipment and tools that can help with the creation of natural and supernatural items. Whether in the form of a forge with metallurgy tools, an artist's loft, a laboratory filled with beakers and crucibles, or an orchard outfitted with the best gardening implements, your character's Hollow is outfitted with precisely the right things she needs to have on hand to create. Each dot in this Merit represents equipment for one particular Craft Specialty. Thus, a Hollow with a three-dot Workshop Merit might include equipment for blacksmithing, weaving, and goblin fruit farming. Whenever a changeling uses the Workshop for Building Equipment or other Crafts rolls with one of these Specialties, she gains a bonus equal to her Merit dots to her rolls. Possible Workshop Specialties include (but are not limited to) Calligraphy, Carpentry, Blacksmithing, Automotive, Painting, or Goblin Fruit Farming.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    # Hollow Features
    Merit(
        name="Easy Access",
        min_value=3,
        max_value=3,
        description="The Hollow has no fixed entrance, and is instead entered (and later exited) through any unlocked door with Glamour and a small ritual.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    Merit(
        name="Escape Route",
        min_value=1,
        max_value=2,
        description="The Hollow has a secondary exit into the material realm, which with two dots may be accessed from anywhere in the Hollow.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    Merit(
        name="Hidden Entry",
        min_value=2,
        max_value=2,
        description="Penalize rolls to find the Hollow's entrance by -2. When all characters sharing the Hollow are within, the entrance disappears.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    Merit(
        name="Hob Alarm",
        min_value=1,
        max_value=1,
        description="Each story, take one Goblin Debt to preserve a domestic guard of friendly hobs. Ambush in the Hollow does not strip Defense and applies Hollow as bonus dice to actions in the first turn of combat.",
        merit_type="changeling",
        prerequisite="hollow:1,hob_kin:1"
    ),
    Merit(
        name="Home Turf",
        min_value=3,
        max_value=3,
        description="Apply Hollow as a bonus to Initiative and Defense against intruders.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    Merit(
        name="Luxury Goods",
        min_value=1,
        max_value=1,
        description="Once a session, roll Hollow as a dice pool and distribute successes among amenities by Availability or Hedgespun items by rating.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    Merit(
        name="Phantom Phone Booth",
        min_value=1,
        max_value=1,
        description="A magical fixture can make outgoing calls to publically listed numbers outside the Hedge.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    Merit(
        name="Route Zero",
        min_value=1,
        max_value=1,
        description="A one-dot trod passes through the Hollow. It may link allied Hollows, or once a day, may be traversed with a Hedge navigation roll to recover Willpower.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    Merit(
        name="Shadow Garden",
        min_value=1,
        max_value=1,
        description="A plot of soil infinitely replenishes copies of goblin fruit without their magical properties, which only temporarily stave off hunger.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    Merit(
        name="Size Matters",
        min_value=1,
        max_value=2,
        description="The Hollow is large enough to sustain up to six residents, or with two dots, the size of a small town.",
        merit_type="changeling",
        prerequisite="hollow:1"
    ),
    # Shared Bastion Features (for Motleys)
    Merit(
        name="Buttressed Dreaming",
        min_value=1,
        max_value=1,
        description="Penalize Clash of Wills to force open Bastion by merit rating.",
        merit_type="changeling",
        prerequisite="motley_membership:1"
    ),
    Merit(
        name="Fixed Doorway",
        min_value=3,
        max_value=3,
        description="Door in the Motley's hollow functions as a Gate of Horn leading to and from the Shared Bastion.",
        merit_type="changeling",
        prerequisite="motley_membership:1,hollow:1"
    ),
    Merit(
        name="Guardian Eidolon",
        min_value=1,
        max_value=1,
        description="Spend Willpower to activate the guardian for the scene, gaining immunity to surprise and adding dots in the merit on the first round of an action scene.",
        merit_type="changeling",
        prerequisite="motley_membership:1"
    ),
    Merit(
        name="Illusory Armory",
        min_value=2,
        max_value=2,
        description="Once per chapter, spend glamour to summon an unimportant prop with rating equal to twice glamour spent (max +5). Spend willpower to summon additional props.",
        merit_type="changeling",
        prerequisite="motley_membership:1"
    ),
    Merit(
        name="Permanent Armory",
        min_value=1,
        max_value=1,
        description="Maintain mundane 'real' items in shared bastion, or magic items by spending Willpower each chapter.",
        merit_type="changeling",
        prerequisite="motley_membership:1"
    ),
    Merit(
        name="Raised Defenses",
        min_value=1,
        max_value=1,
        description="Whenever any motley mate is in the Shared Bastion, all members double the bonuses against the attacks or circumstances normally granted by the merit.",
        merit_type="changeling",
        prerequisite="motley_membership:1"
    ),
    Merit(
        name="Subtle Speech",
        min_value=2,
        max_value=2,
        description="Phantom Eidolons of Motley Members can receive messages, but Changelings with clarity damage might suffer further damage as their sense of reality is befuddled.",
        merit_type="changeling",
        prerequisite="motley_membership:1"
    ),

    # Entitlement Merits
    # Baron of the Lesser Ones
    Merit(
        name="Baron's Bond",
        min_value=4,
        max_value=4,
        description="You are a Baron of the Lesser Ones. You are a diplomat and mediator accepted among hobgoblins. \n\n This merit provides the following blessing options:\n\n- Gain half Wyrd as Allies among a subset of hobgoblins.\n - Glamour regain \n - Enhanced new specialty. \n -Gain Allies (Wyrd/2, rounded up) for a particular group of hobgoblins, such as all merchantsof a specific Goblin Market, or all briarwolves; these Allies remember favors previous Barons did for them. (Conditional) \n\n - Gain a hostile oath (Changeling, p. 214) to one specific changeling, whether the character knows that changeling already or not, leftover from unresolved enmity resulting from a predecessor's actions as Baron. Definitively fulfilling this oath refills all spent Willpower. \n\n - Touchstone: A mortal the Baron rescued from danger in the Hedge. \n\n - Curse: Clarity attacks suffered while favoring hobgoblin interests over changeling ones add damage dice equal to ranks invested in this Merit. \n\n - Beat: The Baron resolves a conflict with goblins, peacefully or otherwise, in a way that personally inconveniences himself or his motley.",
        merit_type="changeling",
        prerequisite="entitlement:baron_of_the_lesser_ones,empathy:2,[intimidation:2,persuasion:2],gentrified_bearing:1,hob_kin:1,interdisciplinary_specialty:goblins"
    ),
    # Dauphines of Wayward Children
    Merit(
        name="Dauphine's Gift",
        min_value=4,
        max_value=4,
        description="You are a Dauphine of Wayward Children. You are a cooperative caretaker for youth without homes.\n\n This merit provides the following blessing options:\n\n- Glamour gain\n - Enhanced new Specialty\n - Additional Thread\n - Gain a token with a rating equal to (Wyrd/2, rounded up) that your character inherited, representing a gift from one of her title's previous wards. The gift was a mundane object but becoming part of the entitlement granted it power. Use the rules on p. 55 to design this token with the Storyteller or use an example from either chapter 4 of this book or starting on p. 224 of the Changeling core book. \n\n - The Dauphine's non-changeling wards all gain the Lucid Dreamer Merit (Changeling, p. 123). She always treats their Bastions as possessing Fortitude 1 (Changeling, p. 221). Successful mundane actions inside a ward's Bastion gain one additional success that can only be used to generate dreamweaving shifts; if this would give the player enough successes for an exceptional success, it counts as such. (Conditional) \n\n - Touchstone: One of the Dauphine's mortal wards. (Conditional) \n\n - Curse: Clarity attacks suffered as a result of losing a ward for any reason, including because they grew up or left of their own accord, add damage dice equal to ranks invested in this Merit. \n\n - Beat: The Dauphine abandons an important responsibility or suffers harm to herself or her motley in the process of chasing and collecting a new ward",
        merit_type="changeling",
        prerequisite="entitlement:dauphines_of_wayward_children,presence:2,[manipulation:2,composure:2],persuasion:2,[empathy:2,intimidation:2],wyrd:3"
    ),
    # Master of Keys
    Merit(
        name="Key Mastery",
        min_value=4,
        max_value=4,
        description="You are a Master of Keys. You are an inquisitive seeker charged with unlocking the discovery of secrets and revelations. \n\n This merit provides the following blessing options:\n\n- Glamour gain\n - Enhanced new Specialty\n - Additional Thread\n - Gain one dot of the Safe Place Merit (Changeling, p. 125), which contains a 2-dot Library (Changeling, p. 123) for a Mental Skill of the player's choice. The Master can use the Last Key to make any door in the mundane world lead there, as a form of portaling (Changeling, p. 109). (Conditional)\n\n - If the Master spends an extra Glamour when portaling into or out of the Hedge through a closeable portal, he may specify a new Key that opens the dormant Hedgeway he leaves behind, as long as it's something that could be researched and is possible for mortals to possess or do. The old Key no longer works. \n\n - Touchstone: A mortal whose secret the Master knows and keeps. (Conditional) \n\n - Curse: Clarity attacks suffered while choosing to keep a secret when its revelation would aid him, or an ally, add damage dice equal to ranks invested in this Merit. \n\n - Beat: Upon investing at least one dot in this Merit, the Master gains an additional Aspiration tied to pursuing a dangerous secret. Once he fulfills it, he replaces it at the end of the chapter with a new one.",
        merit_type="changeling",
        prerequisite="entitlement:master_of_keys, investigation:2, empathy:2, any Merit pertaining to uncovering secrets (e.g. Diviner, Hedge Sense, Trained Observer, etc.)"
    ),
]

# Create dictionary for easy lookup
changeling_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in changeling_merits}
