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
        description="Choose one physical element (such as wind, flame, or wood); all effects apply only to that element. (*) Wind Cuts to the Bone: Exceptional success on purely elemental damage rolls occurs on three successes instead of five. (**) Defensive Flurry: Add half Wyrd (rounded down) to Dodge pool after doubling Defense, and you may Dodge Firearms attacks. (***) Hungry Leaping Flames: Spend Glamour to make melee attacks from 10 yards away and extend ranged attack bands by 10 yards for the scene; elemental effects may disturb scenery. (****) Antaean Endurance: While in significant contact with the chosen element, gain extra Health boxes equal to half Wyrd and same bonus to rolls resisting fatigue, toxins, or unconsciousness. (*****) Wrath of Titans: Spend Glamour to have successful attacks inflict Blinded, Deafened, or Knocked Down (chosen on activation) for the scene.",
        merit_type="style",
        prerequisite="[dexterity:3,wits:3],[brawl:2,firearms:2,weaponry:2],elemental_weapon_or_primal_glory_or_elemental_seeming"
    ),
    Merit(
        name="Enchanting Performance",
        min_value=1,
        max_value=3,
        description="(*) Limerick: Roll Presence + Expression resisted by target Composure when delivering a cutting invective; target suffers penalty equal to your successes on Social rolls against observers (other than you) for the scene, up to -5. (**) Poem: When you successfully open a Door using Expression for performance, spend Glamour to open another Door immediately. (***) Sonnet: Spend Glamour to apply rote quality to your next mundane performance-related Expression roll; on success one audience target gains Inspired, and on exceptional success all viewers gain Inspired.",
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
        description="These maneuvers only function in the Hedge proper. (*) Thousand Falling Leaves: You may inflict -1 Defense on one opponent attack in exchange for dealing only half normal damage on a successful hit. (**) Emerald Shield: Gain armor rating 2/0, stacking with worn armor but not with armor from Hedgespinning or Contracts. (***) Bite Like Thorns: Add bonus attack dice equal to the wound penalty your foe currently suffers.",
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
    Merit(
        name="Unscathed",
        min_value=4,
        max_value=4,
        description="You bear the title of Thorn Dancer and carry the memory of prior dancers in your bones.\n\nAdditional Prerequisites: Socialize 2, Athletics 3, Expression 2, at least one specialty relating to movement.\n\nThis merit provides the following blessing options:\n\n- Glamour gain: Regain 1 Glamour whenever you regain Willpower through your Needle in direct pursuit of your role. You may spend it immediately or store it in your heraldry token (up to Wyrd). Stored Glamour empties at story end.\n- Enhanced new Specialty: Gain a new Specialty tied to the title's duty. Rolls using that Specialty achieve exceptional success on three successes.\n- Additional Thread: Once per chapter, accept the Shaken Condition to recall a predecessor's trauma and gain that predecessor's Thread in addition to your own for the chapter.\n- Gain Arcadian Metabolism and Hob Kin automatically.\n- Clarity attacks made against you in the Hedge are at -2 dice instead of -1.\n\nTouchstone: The first song that made the Thorn Dancer cry after taking up the title.\n\nCurse: Clarity attacks suffered anywhere other than the Hedge add damage dice equal to ranks invested in this Merit.\n\nBeat: The Thorn Dancer willingly helps someone cross an enemy-infested region of the Hedge without payment or oath.",
        merit_type="changeling",
        prerequisite="entitlement:thorn_dancer,socialize:2,athletics:3,expression:2,movement_specialty:1"
    ),
    Merit(
        name="Third Eye",
        min_value=4,
        max_value=4,
        description="You bear the title of Fisher and read fate and hidden truths where others see noise.\n\nAdditional Prerequisites: Computer 3, Investigation 2, Wyrd 3.\n\nThis merit provides the following blessing options:\n\n- Glamour gain: Regain 1 Glamour whenever you regain Willpower through your Needle in direct pursuit of your role. You may spend it immediately or store it in your heraldry token (up to Wyrd). Stored Glamour empties at story end.\n- Enhanced new Specialty: Gain a new Specialty tied to the title's duty. Rolls using that Specialty achieve exceptional success on three successes.\n- Additional Thread: Once per chapter, accept the Shaken Condition to recall a predecessor's trauma and gain that predecessor's Thread in addition to your own for the chapter.\n- Know the precise wording of any fates or destinies connected to those you meet; Investigation rolls to uncover secrets gain 8-again.\n- As an oracle in direct pursuit of duty, make Presence + Expression to command attention (small group -1, small crowd -2, large crowd -3) and gain the Connected (Persistent) Condition.\n\nTouchstone: A mortal supplicant who keeps returning for advice.\n\nCurse: You suffer a Clarity attack when one of your own secrets is revealed, even voluntarily.\n\nBeat: The Fisher connects a secret to the individual trying to keep it hidden.",
        merit_type="changeling",
        prerequisite="entitlement:fisher,computer:3,investigation:2,wyrd:3"
    ),
    Merit(
        name="Breaker of Chains",
        min_value=4,
        max_value=4,
        description="You bear the title of Spiderborn, rider between paths, breaker of bargains and chains.\n\nAdditional Prerequisites: Resolve 3.\n\nThis merit provides the following blessing options:\n\n- Glamour gain: Regain 1 Glamour whenever you regain Willpower through your Needle in direct pursuit of your role. You may spend it immediately or store it in your heraldry token (up to Wyrd). Stored Glamour empties at story end.\n- Enhanced new Specialty: Gain a new Specialty tied to the title's duty. Rolls using that Specialty achieve exceptional success on three successes.\n- Additional Thread: Once per chapter, accept the Shaken Condition to recall a predecessor's trauma and gain that predecessor's Thread in addition to your own for the chapter.\n- Gain Indomitable automatically. If you already possess it, gain +2 dice to resist supernatural mental influence.\n- When trying to find your way in the Hedge, spend 1 Glamour to be led not where you want to go, but where you are needed most.\n\nTouchstone: A mortal from before taking the title who reminds the Spiderborn how much they have changed, and why their true home is now in the Hedge.\n\nCurse: Clarity attacks suffered while refusing to assist another changeling in the Hedge add damage dice equal to ranks invested in this Merit.\n\nBeat: Whenever the Spiderborn frees another from a dangerous bargain or makes the Hedge safer for Lost, take a Beat.",
        merit_type="changeling",
        prerequisite="entitlement:spiderborn,resolve:3"
    ),
    Merit(
        name="College of Worms Mantle",
        min_value=1,
        max_value=5,
        description="""You are aligned with the College of Worms and bear its omen-ridden mantle.

This merit provides the following blessing options:

- Glamour gain.

- (*) Gain bonus dice equal to Mantle on mundane Wits + Composure rolls to notice things out of place or outside expected patterns.

- (**) A pair of cracked glasses manifests as your mark. Once per scene, roll a chance die to search for omens. On success, gain a +2 equipment bonus for a future roll (or grant it to an ally you can warn), or apply it to Initiative for yourself and one ally. Dramatic failure inflicts Obsession or Spooked.

- (***) Gain the Eye for the Strange Merit.

- (****) Spend a scene interpreting omens in a district or similar area; roll Intelligence + Occult (with Safe Place/Security penalties where appropriate) to locate hidden supernatural sites. Success gives a general area; exceptional success gives the exact location or means of entry. Dramatic failure alerts those who claim the place.

- (*****) Once per story, spend 1 Glamour and 1 Willpower to return to shortly before the current scene began with foreknowledge of its events. Allies gain +2 equipment bonus on their first action if they re-enter the scene with you. You suffer a 4-die Clarity attack.""",
        merit_type="changeling",
        prerequisite="entitlement:college_of_worms"
    ),
    Merit(
        name="The Icebound Kiss",
        min_value=4,
        max_value=4,
        description="""You bear the title from the Duchy of the Icebound Heart.

Additional Prerequisites: Manipulation 3, Wyrd 3, Politics or Socialize 2, Intimidation or Persuasion 3.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain a Retainer (Wyrd/2, rounded up) with ties to Royals, Politicians, or Business once per story.

- Spend a Glamour while rolling Persuasion, Socialize, or Intimidation to remove two Doors during social interactions.

Touchstone: Someone who broke your heart in the past.

Curse: Suffer a Clarity attack when you show compassion to whoever you are testing.

Beat: You put yourself or someone you love in physical danger, or suffer physical harm, in order to break your target's heart.""",
        merit_type="changeling",
        prerequisite="entitlement:duchy_of_the_icebound_heart,manipulation:3,wyrd:3,[politics:2,socialize:2],[intimidation:3,persuasion:3]"
    ),
    Merit(
        name="Chevalier's Oath",
        min_value=4,
        max_value=4,
        description="""You bear the title of a Tolltaker Knight.

Additional Prerequisites: Composure 3, Brawl or Weaponry 2, Intimidation 2.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain a token or Hollow with a rating equal to Wyrd/2 (rounded up), representing payment to a predecessor for difficult work.

- Spend a Willpower before engaging your quarry in combat. The target's Defense is halved (rounded up) and they suffer -2 Initiative while under your contract. You may only have one such target at a time.

Touchstone: An item taken from the Knight's first bounty.

Curse: Clarity attacks suffered when someone is harmed by keeping a promise add damage dice equal to ranks invested in this Merit.

Beat: The Knight's reputation causes someone to think poorly of him.""",
        merit_type="changeling",
        prerequisite="entitlement:tolltaker_knights,composure:3,[brawl:2,weaponry:2],intimidation:2"
    ),
    Merit(
        name="Thorn Threnody",
        min_value=4,
        max_value=4,
        description="""You bear the title from the Margravate of the Brim.

Additional Prerequisites: Brawl or Weaponry 3, Survival 2, Wyrd 2+.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- In a Hedge chase, reduce the base successes needed to prevail by double your Wyrd.

- Gain Interdisciplinary Specialty focused on the Hedge (with one free Hedge Specialty), ignoring normal Skill prerequisite.

Touchstone: A mortal whose life improved because of the March Lady's aid.

Curse: Clarity attacks suffered when someone you promised to protect or guide is physically injured add damage dice equal to ranks invested in this Merit.

Beat: The Margrave assists an ungrateful person or one who questioned her ability.""",
        merit_type="changeling",
        prerequisite="entitlement:margravate_of_the_brim,[brawl:3,weaponry:3],survival:2,wyrd:2"
    ),
    Merit(
        name="Sage's Expertise",
        min_value=4,
        max_value=4,
        description="""You bear the title of a Noble Sage of the Unknown Reaches.

Additional Prerequisites: Role-specific baseline requirements, plus Occult.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Contacts equal to Wyrd/2 (rounded up), each representing a different non-fae supernatural community with prior positive ties to your office.

- Gain a Barfly-like effect that applies to gatherings of non-fae supernatural creatures, ignoring that Merit's normal prerequisites.

Touchstone: A mortal scholar of folklore, mythology, or monster-focused culture.

Curse: Clarity attacks suffered from breaking promises to non-fae supernatural beings add damage dice equal to ranks invested in this Merit.

Beat: You place gathering information about other supernatural beings above your motley, freehold, or court.""",
        merit_type="changeling",
        prerequisite="entitlement:noble_sages_of_the_unknown_reaches,occult:2"
    ),
    Merit(
        name="Iridescence of Wealth",
        min_value=4,
        max_value=4,
        description="""You bear title and privilege within the Satrapy of Pearls.

Additional Prerequisites: Persuasion 3, Manipulation 3, Resources 4.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Court Goodwill (Wyrd/2, rounded up) that applies to all major local Courts, twice per story.

- In a new Freehold, you gain Notoriety; if you later remove it, regain all Willpower.

Touchstone: A person who gave you something you cannot repay.

Curse: Failure to fulfill a deal causes Clarity damage equal to Wyrd/2 (rounded down).

Beat: The Satrap knowingly makes an unfair deal in someone else's favor.""",
        merit_type="changeling",
        prerequisite="entitlement:satrapy_of_pearls,persuasion:3,manipulation:3,resources:4"
    ),
    Merit(
        name="Scarecrow's Duty",
        min_value=4,
        max_value=4,
        description="""You bear the title of a Scarecrow Minister.

Additional Prerequisites: Composure 3, Empathy 2 with a fear-relevant Specialty, Intimidation 3.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- On successful Empathy against a sapient target, roll Wyrd; each success reveals one fear the subject carries.

- Whenever you successfully harvest Glamour from fear, gain additional points equal to Presence.

Touchstone: A mortal the Minister (past or present) protected from the supernatural by frightening them away.

Curse: Clarity attacks suffered after gaining fear-derived Conditions add damage dice equal to ranks invested in this Merit.

Beat: The Minister sacrifices personal goals or relationships to strengthen a cautionary legend.""",
        merit_type="changeling",
        prerequisite="entitlement:scarecrow_minister,composure:3,empathy:2,intimidation:3"
    ),
    Merit(
        name="Laity of the Blackbird",
        min_value=1,
        max_value=1,
        description="""You carry the condition-sign of the Blackbird's laity.

This merit provides the following blessing option:

- Once per chapter, add Wyrd to Empathy, Persuasion, or Socialize rolls used to determine what is wrong in a situation or what troubles someone.""",
        merit_type="changeling",
        prerequisite="condition:laity_of_the_blackbird"
    ),
    Merit(
        name="Bishop's Benevolence",
        min_value=4,
        max_value=4,
        description="""You bear the title of Bishop of Blackbirds.

Additional Prerequisites: Empathy 2, Wits 3, Composure 3.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain a Wyrd/2-dot Retainer flock (blackbirds, crows, ravens, or similar) that recognizes mental Conditions and can communicate with you.

- When someone confesses wrongdoing and details amends, you may seal the statement without cost. If that confession addresses a prior Clarity/Integrity break and is fulfilled, the subject recovers that damage and you regain 1 Willpower.

Touchstone: A mortal whose mental anguish has been eased by the Bishop.

Curse: Clarity attacks resulting from actions that caused Clarity/Integrity breaks in others add damage dice equal to ranks invested in this Merit.

Beat: The Bishop enters physical danger to bolster another's Clarity/Integrity.""",
        merit_type="changeling",
        prerequisite="entitlement:bishop_of_blackbirds,empathy:2,wits:3,composure:3"
    ),
    Merit(
        name="Magistrate's Discretion",
        min_value=4,
        max_value=4,
        description="""You bear title and burden among the Magistrates of the Wax Mask.

Additional Prerequisites: Composure 3, Socialize 2, Subterfuge 3.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Wyrd/2 (rounded up) as bonus on Composure- or Subterfuge-based rolls to avoid reacting to witnessed events and to later deny witnessing them.

- While not actively drawing attention in a scene, simple Perception-based attempts to notice you only succeed on exceptional success.

Touchstone: A solitary hobby the Magistrate pursues alone.

Curse: Clarity attacks suffered while favoring personal needs over client duty add damage dice equal to ranks invested in this Merit.

Beat: The Magistrate sacrifices personal safety in the name of professionalism.""",
        merit_type="changeling",
        prerequisite="entitlement:magistrates_of_the_wax_mask,composure:3,socialize:2,subterfuge:3"
    ),
    Merit(
        name="Heart of the Brambles",
        min_value=4,
        max_value=4,
        description="""You bear title and instinct as a Magus of the Gilded Thorns.

Additional Prerequisites: Composure 3, Stealth 2, Hedge Sense, Wyrd 2+.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Wyrd/2 (rounded up) bonus on Hedge navigation rolls. At Wyrd 3, you can see through Hedge gates without opening them. At Wyrd 6, you can look down a trod and see what waits at its end.

- Spend 1 Glamour to obscure a Hedge traveler's tracks; trackers are misled unless they achieve exceptional success. This can mislead Huntsmen until the traveler exits the Hedge.

Touchstone: A lush mortal-world garden, usually with a bramble at its center.

Curse: Clarity attacks suffered from lack of human contact add damage dice equal to ranks invested in this Merit.

Beat: The Magus denies shelter to a fleeing changeling, or aids a Huntsman/True Fae pursuing one.""",
        merit_type="changeling",
        prerequisite="entitlement:magus_of_the_gilded_thorns,composure:3,stealth:2,hedge_sense:1,wyrd:2"
    ),
    Merit(
        name="The Best Around",
        min_value=4,
        max_value=4,
        description="""You bear title within the Sacred Band of the Golden Standard.

Additional Prerequisites: Presence 3, Wyrd 2, one chosen Skill 3+ with suitable Specialty.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Once per chapter, gain Wyrd/2 (rounded up) points to spend on your chosen Skill: force exceptional success on three successes (including retroactively), or remove 10-again from an opponent's relevant contested pool. Points do not roll over.

- Once per chapter, when you succeed with the chosen Skill, you may bestow Inspired on everyone who personally witnessed it.

Touchstone: A mortal fan (or small fan club) inspired by seeing your impossible task.

Curse: Failing or dramatically failing with your chosen Skill triggers a Clarity attack with dice equal to ranks invested in this Merit.

Beat: You succeed at an incredible challenge that defies others' expectations.""",
        merit_type="changeling",
        prerequisite="entitlement:sacred_band_of_the_golden_standard,presence:3,wyrd:2"
    ),
    Merit(
        name="Squire's Vow",
        min_value=4,
        max_value=4,
        description="""You bear title as a Squire of the Broken Bough.

Additional Prerequisites: Composure 3, Resolve 3, Weaponry 2.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- When sworn to another's cause, gain bonus Willpower equal to Wyrd/2 (rounded up) until spent.

- Once per scene, spend Willpower to inflict Frightened on someone who has witnessed your death.

Touchstone: Your current client is always your current Touchstone.

Curse: Clarity attacks suffered because someone broke a formal oath or pledge to you add damage dice equal to ranks invested in this Merit.

Beat: The Squire suffers hardship or injury while championing another's cause.""",
        merit_type="changeling",
        prerequisite="entitlement:squire_of_the_broken_bough,composure:3,resolve:3,weaponry:2"
    ),
    Merit(
        name="Judge's Zeal",
        min_value=4,
        max_value=4,
        description="""You bear title as an Adjudicator of the Wheel.

Additional Prerequisites: Resolve 3, Investigation 2, Trained Observer 1.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- When using Kenning, spend 1 Glamour to glimpse one observed subject's likely future up to Wyrd/2 days ahead (rounded up).

- You may hold a hostile oath on another's behalf (between you and a third party who aggrieved the swearer). You can maintain only one such instance at a time.

Touchstone: A mortal a previous Judge failed to help.

Curse: Clarity attacks suffered while prioritizing duty over health, relationships, or core responsibilities add damage dice equal to ranks invested in this Merit.

Beat: The Adjudicator rights an injustice at personal or allied expense.""",
        merit_type="changeling",
        prerequisite="entitlement:adjudicator_of_the_wheel,resolve:3,investigation:2,trained_observer:1"
    ),
    Merit(
        name="Diviner's Foresight",
        min_value=4,
        max_value=4,
        description="""You bear title among the Diviners of Worms.

Additional Prerequisites: Occult 2, Diviner 3, Trained Observer 1.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Read omens to gain Common Sense-like guidance with a bonus equal to Wyrd/2 (rounded up).

- Gain an enhanced Danger Sense against immediate threats, including environmental danger. If your Instrument was activated in the same scene, this bonus doubles.

Touchstone: A mortal once protected by your prophecies.

Curse: Clarity attacks suffered when others reject your prophecies add damage dice equal to ranks invested in this Merit.

Beat: You offer aid that endangers or severely inconveniences yourself or your motley without expectation of reward.""",
        merit_type="changeling",
        prerequisite="entitlement:diviners_of_worms,occult:2,diviner:3,trained_observer:1"
    ),
    Merit(
        name="Hunting Truth and Hiding Loss",
        min_value=4,
        max_value=4,
        description="""You bear title as Duchess of Truth and Loss.

Additional Prerequisites: Wits 3, Investigation 2, must have killed a fetch.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Wyrd/2 (rounded up) bonus on Investigation, Survival, and Perception to locate those actively concealing themselves.

- Touch a dead/dying fetch and spend 1 Glamour to prevent disintegration for one lunar month. Presenting the preserved body to that fetch's changeling heals one point of minor Clarity damage and refreshes all Willpower.

Touchstone: An object instrumental in the death of the first fetch you killed.

Curse: Clarity attacks suffered because others defend your quarry add damage dice equal to ranks invested in this Merit.

Beat: Gain a Beat the first time in a scene you take lethal from a fetch's attack or fail to resist an Echo.""",
        merit_type="changeling",
        prerequisite="entitlement:duchess_of_truth_and_loss,wits:3,investigation:2,must_have_killed_a_fetch:1"
    ),
    Merit(
        name="Plutomancer's Privilege",
        min_value=4,
        max_value=4,
        description="""You bear title as Guildmaster of Goldspinners.

Additional Prerequisites: Academics with a Specialty in Finance or Business, Resources 3.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Mental Merit dots equal to Wyrd/2 (rounded up), distributed as desired.

- Spend 1 Glamour to identify who nearby is most desperate for money (not necessarily who needs it most).

Touchstone: A personally cherished pre-title item with no significant monetary value.

Curse: Clarity attacks suffered after witnessing a broken promise add damage dice equal to ranks invested in this Merit.

Beat: The Guildmaster knowingly accepts a deal less favorable than possible.""",
        merit_type="changeling",
        prerequisite="entitlement:guildmaster_of_goldspinners,academics_specialty_finance_or_business:1,resources:3"
    ),
    Merit(
        name="Threadmender",
        min_value=4,
        max_value=4,
        description="""You bear title as a Paragon of Story Heroes.

Additional Prerequisites: Wits 3, Academics 2, Persuasion or Subterfuge 2.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Allies equal to Wyrd/2 (rounded up), representing those current or previous Paragons helped avert disaster.

- Spend 1 Glamour during a pivotal scene moment to deliver a short speech that cannot be interrupted (supernatural silencing attempts provoke Clash of Wills). Chosen listeners within line of sight hear and understand you.

Touchstone: An item representing a story especially important to the Paragon.

Curse: Clarity attacks suffered in the Hedge add damage dice equal to ranks invested in this Merit.

Beat: You act against your own interest to steer another's narrative toward a positive outcome.""",
        merit_type="changeling",
        prerequisite="entitlement:paragon_of_story_heroes,wits:3,academics:2,[persuasion:2,subterfuge:2]"
    ),
    Merit(
        name="Spark of Metamorphosis",
        min_value=4,
        max_value=4,
        description="""You bear title as Castellan of the Broken Cage.

Additional Prerequisites: Manipulation 3, Empathy or Socialize 2, Wyrd 2+.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Allies equal to Wyrd/2 (rounded up), representing previous chrysalids transformed under this office.

- You always know when someone lies to you about what they consciously desire. Unconscious desire registers as a fainter signal.

Touchstone: A previous chrysalid whose life transformed under the Castellan's influence.

Curse: Clarity attacks taken when a chrysalid suffers negative consequences because of the Castellan's attention add damage dice equal to ranks invested in this Merit.

Beat: The Castellan is confronted by someone in a chrysalid's life.""",
        merit_type="changeling",
        prerequisite="entitlement:castellan_of_the_broken_cage,manipulation:3,[empathy:2,socialize:2],wyrd:2"
    ),
    Merit(
        name="Echo's Memory",
        min_value=4,
        max_value=4,
        description="""You bear title as an Eternal Echo.

Additional Prerequisites: Resolve 3, Academics 2, Expression 2.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Your memory cannot be altered by mystical or mundane means. Gain Wyrd/2 (rounded up) bonus on rolls to resist being forced to reveal what you know.

- Gain Eidetic Memory. If you already possess it, gain two Merit dots to spend instead. Spend 1 Glamour to double this bonus for the scene.

Touchstone: The mortal family of a changeling whose story was recorded in living memory.

Curse: Clarity attacks suffered as a result of discovering lies about important events add damage dice equal to ranks invested in this Merit.

Beat: The Echo hears a morally reprehensible story (or one told by an enemy) without judging the teller.""",
        merit_type="changeling",
        prerequisite="entitlement:eternal_echo,resolve:3,academics:2,expression:2"
    ),
    Merit(
        name="Symphony for the Senses",
        min_value=4,
        max_value=4,
        description="""You bear title among the Knights of the Knowledge of the Tongue.

Additional Prerequisites: Stamina 3, Crafts 3 with a Specialty in Cooking.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Merit dots equal to Wyrd/2 (rounded up) in any mix of Contacts or Allies, reflecting culinary diplomacy and social inroads.

- Gain +5 on rolls to find or identify ingredients, including goblin fruit and animals you have cooked before.

Touchstone: A favorite mundane cooking tool or recipe book.

Curse: Clarity attacks suffered when disaster results from a dish you cooked add damage dice equal to ranks invested in this Merit.

Beat: The Knight incurs personal harm while seeking rare ingredients.""",
        merit_type="changeling",
        prerequisite="entitlement:knights_of_the_knowledge_of_the_tongue,stamina:3,crafts:3"
    ),
    Merit(
        name="Benediction of the Orchard",
        min_value=4,
        max_value=4,
        description="""You bear title as Legate of the Black Apple.

Additional Prerequisites: Two Social Skills at 4+, combined Composure + Resolve of at least 7, Wyrd 3+.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Gain Merit dots equal to Wyrd/2 (rounded up) split among Fae Mount, Hedge Sense, Hedgewise, and Hob Kin.

- Spend 1 Glamour to grant one person +3 on actions to resist fear or intimidation for one scene.

Touchstone: A mortal saved from the Gentry as a child by the Legate (or predecessor).

Curse: Clarity attacks suffered when dealing with someone the Legate could not help add damage dice equal to ranks invested in this Merit.

Beat: The Legate suffers serious physical injury or Clarity damage while carrying out duty.""",
        merit_type="changeling",
        prerequisite="entitlement:legate_of_the_black_apple,combined_composure_resolve:7,wyrd:3"
    ),
    Merit(
        name="Primordial Incarnation",
        min_value=4,
        max_value=4,
        description="""You bear title in the Lost Pantheon.

Additional Prerequisites: Presence 3, Occult 2 with Specialty in the appropriate deity, Wyrd 3+.

This merit provides the following blessing options:

- Glamour gain.

- Enhanced new Specialty.

- Additional Thread.

- Spend 2 Glamour to consecrate one occupied Hollow as a temple. Entry requires an offering or a successful Resolve + Composure roll penalized by Wyrd/2 (rounded up). Only one such temple can be active at a time.

- Spend 1 Willpower to imbue an object with your deity's element for the scene. The element can be consumed/used normally. Once per day, a Sprite aligned with that element can absorb it to heal one level of superficial Clarity damage.

Touchstone: A maintained icon of your deity (relic, statue, or sacred object) that anchors your duty.

Curse: Clarity attacks suffered when others scorn, disbelieve, or ignore your deity add damage dice equal to ranks invested in this Merit.

Beat: You place your deity's domain above motley, court, or freehold needs, or are harmed while doing so.""",
        merit_type="changeling",
        prerequisite="entitlement:lost_pantheon,presence:3,occult:2,wyrd:3"
    ),
]

# Create dictionary for easy lookup
changeling_merits_dict = {
    merit.name.lower().replace(" ", "_").replace("-", "_").replace("'", "").replace("(", "").replace(")", ""): merit
    for merit in changeling_merits
}
