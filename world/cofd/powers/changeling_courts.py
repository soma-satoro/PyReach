"""
Changeling: The Lost 2nd Edition Courts for Chronicles of Darkness.
"""

# ============================================================================
# COURTS
# ============================================================================

ALL_COURTS = {
    "spring": {
        "name": "Spring",
        "description": "Desire is a ﬂame. It’s the fuel in the engine of ambition. It’s the warm rich red of passion and the pale insistent blue of hunger. It’s a will-o-wisp dancing just out of reach, leading the foolish to bad ends. You can’t live without its warmth and heat, but feed it too much and it’ll burn you to ashes. The other courts don’t understand, of course. They reject the philosophy of desire. They may call it selfsh, or shortsighted, or shallow. Why spend your time chasing pleasures, they may say, with the Others scratching at the threshold? Why don’t you understand what’s important? Those are foolish questions. The Spring Court knows exactly what’s important. Passion feeds ambition and art. Hunger is an understanding of your needs. But most important, desire is the food of life. With laughter and joy and pleasure, changelings live — without these things, they simply survive. Desire is the key to taking your life back or building a new, full life. It’s an alluring philosophy, and it draws many Lost who don’t want to dwell on the past. And with the Bargain, it even refutes the power of the Gentry. Fuck you, it says, we don’t need you. You didn’t break us. You can’t break us. We’ll live and love and enjoy ourselves and forget you ever existed.",
        "mantle_benefits": {
            "0": "The character gains a Glamour point whenever he oversteps his bounds to satisfy his personal desires.",
            "1": "Gain bonus dice equal to your character’s Mantle dots to mundane rolls to seduce or attract someone.",
            "2": "Gain bonus dice equal to your character’s Mantle dots when taking mundane actions that encourage or bring about over-indulgence.",
            "3": "Gain bonus dice equal to your character’s Mantle dots during mundane teamwork actions to help an ally achieve her goals.",
            "4": "Regain an additional Willpower point when you would regain one through your character’s Needle Merit.",
            "5": "Once per chapter, you may convert a single Clarity Condition into a different, beneficial Condition of your choice. When you do, regain one Clarity. Your character may use this to convert an ally’s Clarity Condition instead.",
        },
        "book": "CTL 2e p.35"
    },
    "summer": {
        "name": "Summer",
        "description": "Wrath is rejection. Wrath doesn’t accept that things are the way they are, and there’s nothing to do about it. When someone shoves a knife into you, wrath is the urge to pull that knife out and stab right back. Let Spring and Autumn and Winter all try to avoid or mitigate their pain. Summer channels wrath to scream through bloodﬂecked lips, no more! Nobody spends much time debating whether or not they belong with the Iron Spear. Summer Courtiers are those who drew a line and chose to push back. Maybe it was their own pain: loss, wounds, failure, humiliation. Maybe it was someone else’s. But something awakened that fury in them, a wrath pure enough that they stopped thinking about ﬂight and decided to fght. It’s not always healthy, of course. Wrath doesn’t make you happy, even if it dulls the pain and gives you something else to think about. It might lead you to sacrifce yourself for an empty promise of vengeance. But nothing gives a hunter pause like a beast that has decided it’s not going to be prey any more. There were other things that Summer had to offer, so long ago. But the Bargain with Summer was paid in wrath. It’s the oath of the blazing sun destroying shadows. It’s the vigilance of the longest day. It’s the spike in violence when the sun sets.",
        "mantle_benefits": {
            "0": "Your character gains a Glamour point whenever she enacts her wrath and successfully furthers a goal.",
            "1": "Gain bonus dice equal to your character’s Mantle dots to mundane rolls to intimidate or cow someone.",
            "2": "Gain bonus dice equal to your character’s Mantle dots to mundane attack rolls when actively defending her freehold against a fae threat.",
            "3": "Gain general and ballistic armor equal to your character’s Mantle dots, which stacks with worn armor, when acting as a protector, bodyguard, or champion for someone else.",
            "4": "Automatically succeed on attempts to break through mundane barriers or otherwise deal with inanimate impediments.",
            "5": "When defending a member of your character’s freehold, her mundane attacks deal aggravated damage.",
        },
        "book": "CTL 2e p.39",
    },
    "autumn": {
        "name": "Autumn",
        "description": "Fear is a line in the dust. It’s a boundary, an invisible wall. Fear keeps your enemy from crossing your threshold. Fear keeps your allies from presuming too much. Fear is a fortress, and the Leaden Mirror knows all the secrets in its foundations. The Ashen Court has a complicated relationship with their signature passion. Some of them revel in the rush; others consider terror the most rational weapon in a frightening world. Obviously, they all know how what it’s like to live in constant dread, thanks to the durance — but that could be said to be true of every Lost. The difference is that it takes a certain amount of introspection to swear the Autumn vow. Spring and Summer might suppress their old fears, and Winter may hide from them. But Autumn has to come to terms with those old scars. Why, then, doesn’t the Ashen Court play more like the Summer Court? Why do they treat the dread of knives and gasoline and broken glass as secondary at best? The answer’s pragmatic — as terrifying as the threat of violence is, it works best on mortals. The True Fae play by different rules. They don’t even reliably have bodies to break or blood to spill. To get at what frightens one of the Gentry, you have to threaten the rules they play by. And that requires sorcery. Nothing terrifies one of the grand gameplayers like the realization that what they’d mistaken for a pawn has its hands on the rulebook. Autumn had many gifts to offer, but the Ashen Court chose fear. It was a power that flowed from lengthening nights and dead leaves falling from skeletal branches, of ripe fruits rotting on the ground. Autumn granted the understanding that death itself is not as frightening as dying. Animals fatten up before winter, driven by the secret understanding of starvation. Rich greens wither away into sere browns. Mortals honor their ghosts and light lanterns against the deepening dark. Horror movies and Halloween are florid offerings to Autumn’s ancient and subtle truth: the unconscious dread that perhaps this will be the year you won’t see the coming of spring. The immortal Gentry don’t understand mortality in these terms — but who better than the Autumn Court to instruct them?",  
        "mantle_benefits": {
            "0": "Your character gains a Glamour point whenever he overcomes his fear to investigate something new and dangerous.",
            "1": "Gain bonus dice equal to your character’s Mantle dots to mundane rolls to investigate the True Fae or Faerie.",
            "2": "Gain bonus dice equal to your character’s Mantle dots to mundane rolls to intimidate or otherwise instill fear in someone.",
            "3": "Reduce the Glamour cost of Contracts by one when using them to subvert a True Fae or something from Faerie.",
            "4": "Once per story, reduce your character’s Goblin Debt by his Mantle rating.",
            "5": "After a magical effect affects your character, you may spend 2 Glamour to mimic that effect exactly, and may choose a new target. You must do this within the same scene that he was affected.",
        },
        "book": "CTL 2e p.43",
    },
    "winter": {
        "name": "Winter",
        "description": "Sorrow is a cage. It keeps a person from moving. It roots them in place, cold and unyielding. But people also willingly lock themselves within it. They embrace the bars’ strength, for they’re just as strong as the love for what was lost. They close the door to keep other people out, as if they were sharks. The Winter Court knows that sorrow can be crippling, but also inspiring. You just have to be certain you’re the one holding the keys. It’s easy for a changeling to be drawn to sorrow. All you had to do was love enough. The Lost return home to find lovers in a false person’s arms, parents dead and gone, children grown and unhappy. The life’s work you built may be shuttered and lightless. The art you created may be destroyed or stolen. The Winter Court doesn’t offer the same strength as Summer and Autumn, or the same abandon and hope as Spring, but it has never lacked for numbers. Those who join the Silent Arrow don’t want to forget. Sorrow’s strength is twofold. Turn it against your enemies, and you strike at their will to fight. Turn it inward, against yourself, and you can see through false hopes and useless temptations. The Silent Arrow keeps loss, regret, guilt, and despair in their quiver. They’re dangerous things to handle, but they have to be. So many of the Gentry aren’t prepared for the pain that comes with losing something you truly loved — because so many of the Gentry weren’t capable of truly loving in the first place. Winter has always been the season of sorrow. Light is in shorter supply, and darkness comes early. The modern understanding of seasonal affective disorder offers a more scientific illustration of a relationship with Winter that some people have always endured. The longer the night, the easier it is to mourn.",
        "mantle_benefits": {
            "0": "Your character gains a Glamour point whenever she helps someone come to terms with their grief.",
            "1": "Enemies suffer a penalty equal to your character’s Mantle dots to rolls to notice her when she’s deliberately spying.",
            "2": "Gain bonus dice equal to your character’s Mantle dots when obscuring the truth.",
            "3": "When your character surrenders in a fight, gain bonus dice equal to her Mantle dots to any subsequent Social actions for the rest of the scene.",
            "4": "Spend a Glamour point to bind someone in their own misery. For the rest of the scene, any time the target enters a fight, they suffer the Beaten Down Tilt and must spend 2 Willpower to end it.",
            "5": "Your character ignores wound penalties. For each health box filled with lethal or aggravated damage, gain a one-die bonus on Physical actions, to a maximum of +5.",
        },
        "book": "CTL 2e p.47",
    },
    "courtless": {
        "name": "Courtless",
        "description": "Courtless Changelings have not pledged to a Court for whatever reason. This tends to make them a little suspicious in the eyes of their Freehold-mates, given that the Courts were designed to help protect the Lost from the Gentry.",
        "mantle_benefits": {
            "None": "The Courtless are the changelings who reject court politics.",
        },
        "book": "N/A"
    },
    "morning": {
        "name": "Society of Morning",
        "description": "The Society of Morning holds domain over birth, growth, and discovery of the new. They are the most likely to actively search for changelings stumbling out of Arcadia, and to pump them for stories about their experiences or knowledge gained there. They are messengers and seekers after novelty for its own sake. They are eager to find information, confident that its usefulness will be made clear in the course of its discovery. Restless pursuit has yielded distressing news, though. They have reason to believe societies from Beijing are attempting to infiltrate all three of the Hong Kong societies",
        "mantle_benefits": {
            "0": "The Morning Mantle is as bright and sharp as a sunrise. The air around the courtier smells of new things — doors and windows thrown open for the first time, in a long-empty house. The courtier herself flickers, dancing in place like a flame, eager to be moving, eager to consume. Your character gains a Glamour point whenever she gains new knowledge through reckless pursuit.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls for gathering information on a subject new to her.",
            "2": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls related to instability or impermanence.",
            "3": "Regain a point of Willpower when your character tells a truth that implicates a coworker or friend.",
            "4": "Automatically succeed on attempts to persuade another changeling to share information relevant to the safety of the freehold that they defend against mundanely; this prompts a Clash of Wills against supernatural defenses.",
            "5": "Once per chapter, your character may deflect one of her negative Clarity Conditions onto someone else by revealing an unknown truth about them; this doesn’t heal any Clarity damage for her or grant a Beat, and the target doesn’t take any Clarity damage.",
        },
        "book": "CTL 2e p.279"
    },
    "day": {
        "name": "Society of Day",
        "description": "The Society of Day holds domain over marriage, fruition, and moderation of opposing forces. They are the most likely to be mediators in changeling conflicts, and the architects of large-scale projects. The most involved in day-to-day maintenance of Hong Kong, they tend to cultivate the sources Morning changelings use to gain new knowledge, and find a place for those people in the 89th Pavilion. Many changelings have Day to thank for their homes and jobs. Many changelings owe Day favors. Changelings who join the Society of Day tend to be practical and ambitious, but overconfident.",
        "mantle_benefits": {
            "0": "The Day Mantle is warm and thrumming, welcoming but demanding. The ground beneath the courtier’s feet feels sturdier. The air smells strongly of industry and sweat and ripe fruit. No matter how relentless the pace, the courtier himself seems peaceful and measured — planted solidly in the earth. Your character gains a Glamour point whenever he successfully resolves a conflict between two changelings.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to continue a project someone else started.",
            "2": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to repair something that was nearly thrown away.",
            "3": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to mediate between hostile parties.",
            "4": "Reduce the Glamour cost of Contracts by one when using them to extend or improve an existing public work.",
            "5": "The industry of the world turns on your finger. Once per chapter, automatically find whatever minor or uncommon mundane tools are necessary for the task at hand.",
        },
        "book": "CTL 2e p.279"
    },
    "night": {
        "name": "Society of Night",
        "description": "The Society of Night holds domain over death, retreat, and the stillness of contemplation. What Morning seeks and Day maintains, Night uses. They search the records created by Morning and Day to think up new defenses, new weapons. They take point in pursuit of Huntsmen and the Fae, and often shadow the Morning changelings who deliberately return to the Hedge. Night does not need to actively recruit; the most martially inclined changelings find them. Individual Night members often work more closely with changelings from other societies than they do with one another. Changelings who join the Society of Night tend to be persistent and intelligent, but controlling and critical.",
        "mantle_benefits": {
            "0": "The Night Mantle is luminous and studded with stars. A dry chill flls the air and presses into your bones, pausing the frantic heat of the day. The courtier may shake in the wind, but her hand never falters while acting in the darkness. Your character gains a Glamour point whenever she follows a hunt to its logical conclusion.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to research a problem her freehold has encountered before.",
            "2": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to shadow or investigate a new informant.",
            "3": "Regain a Willpower point when your character deliberately makes a difficult choice that inflicts a Condition on her.",
            "4": "Gain bonus dice equal to your character’s Mantle dots when concealing a defensive fact about herself or her freehold.",
            "5": "When attacking a target your character has previously pursued out of premeditated violence, she deals aggravated damage.",
        },
        "book": "CTL 2e p.281"
    },
    "high_tide": {
        "name": "High Tide",
        "description": "The waves pound away at the shore, destroying carefully built sandcastles, washing forgotten sandals and buckets out to sea. When the tide comes in, land yields to water, and when it recedes, it takes a bit of the beach with it. Those who swear fealty to it are forces of nature themselves, with strong personalities and implacable wills. Some of its members confront their foes like strong waves, knocking down anyone who dares stand in their paths. Others prefer to wait, working their will so subtly their opponents don’t realize they’ve lost until the tide’s already on its way out. Changelings who join this court are often the first line of defense against the True Fae and their minions.",
        "mantle_benefits": {
            "0": "The Mantle of a High Tide courtier evokes the smell of salt and the cries of seagulls. Warm sea breezes stir the air around her. Your character gains a Glamour point whenever she opens someone’s last Door in Social maneuvering (p. 191).",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to inflict Tilts on opponents.",
            "2": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to undermine someone’s authority or respect among their peers.",
            "3": "Once per chapter, you may reroll a mundane roll that uses a Power Attribute and choose which result to keep.",
            "4": "Automatically succeed on attempts to break through mundane barriers or otherwise deal with inanimate impediments.",
            "5": "Enemies of lower Wyrd than your character take a two-die penalty to attacks against her.",
        },
        "book": "CTL 2e p.161"
    },
    "low_tide": {
        "name": "Low Tide",
        "description": "The water is as far from shore as it ever gets, the sea fled for a time. Clams push toward the surface for a bit of air, only to be dug up and cooked for a delicious dinner. The sands lay uncovered; debris left behind by the tide dries in the sun. The Court of Low Tide attracts changelings of a gentler disposition, but equating “gentle” with “weak” is unwise. Lost who join this court are adept at digging up secrets and exposing them, bringing down their foes without ever having to confront them in person. This court also handles the majority of the dealings with other supernatural beings, keeping track of what is taken from the land and what is owed as a result.",
        "mantle_benefits": {
            "0": "The Mantles of Low Tide courtiers often manifest as a briny seaweed scent on the wind. They leave the impression of footprints in wet sand in their wake. Your character gains a Glamour point whenever she successfully uses secrets to foil someone’s plans.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to investigate someone’s dirty secrets.",
            "2": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to blackmail or coerce someone using information she dug up herself.",
            "3": "Regain a Willpower point whenever your character definitively profits from her position as a gobetween for other parties.",
            "4": "All clues your character turns up in an investigation gain an additional element (p. 195).",
            "5": "Another character with a Leveraged Condition (p. 342) that your character inflicted must capitulate to two of her demands before they can resolve it.",
        },
        "book": "CTL 2e p.161"
    },
    "flood_tide": {
        "name": "Flood Tide",
        "description": "Just as the tide goes out, it comes in again. The sea swells and encroaches, sandbars disappear, and the beaches feel more crowded as sunbathers are pushed closer together. Where Ebb Tide is the calm after the storm, Flood Tide is the feeling of clouds gathering beforehand and the air growing heavy with the promise of rain. Members of the Court of Flood Tide are perpetually engaged. Whether it’s planning gatherings for the other courts, checking up on the newly freed Lost, or following up on the freehold’s needs, these changelings always have a full calendar. Other courts joke that when the Huntsmen come looking for them, the Lost of the Flood Tide are simply too busy to get caught. The real truth is that the Flood Tide courtiers never stop running.",
        "mantle_benefits": {
            "0": "The Mantle for a Flood Tide courtier is a sharp spring breeze and the creak of boats against their moorings. Your character gains a Glamour point whenever a plan he built as equipment (p. 196) goes off without a hitch.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to find a safehouse or shelter away from home.",
            "2": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to make friends in a new place he’s never been.",
            "3": "Once per chapter, you may spend a Willpower point to grant your character additional dots of the Etiquette Merit (p. 122) equal to her Mantle dots, to a maximum of fve, for the scene.",
            "4": "Once per chapter, you may reroll a mundane roll that uses a Finesse Attribute and choose which result to keep.",
            "5": "Once per chapter, you may spend a Willpower point in place of Glamour to use portaling (p. 109)",
        },
        "book": "CTL 2e p.161"
    },
    "coins": {
        "name": "Court of Coins",
        "description": "The simplest transactions are completed with cold, hard cash, though that cash might more closely resemble lost doubloons or pennies gathered from the depths of a specifc wishing fountain in Poughkeepsie. Coins have a specifc value, and a trader can count them and bite them to test their realness. Change also jingles in a pocket or purse, signifying to anyone listening for its clinking, clattering song that the carrier has riches to spend. Members of the Court of Coins are the most straightforward of the freehold’s Lost, preferring to deal in specifics and absolutes. They rarely hide behind ruses, wanting to deal straight with anyone who cares to trade with them, and expecting the same in return.",
        "mantle_benefits": {
            "0": "The Mantle of a Coin Courtier carries with it the sound of coins shaken in deep pockets, or bills counted out from a drawer. They smell of copper and paper and ink. Your character gains a Glamour point whenever she successfully hunts down someone who owes her something and gets it.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to persuade someone to make an oath (p. 212).",
            "2": "Gain bonus dice equal to your character’s Mantle dots to mundane rolls to figure out whether someone is trying to cheat her.",
            "3": "Once per chapter, you may spend a Willpower point to grant your character additional dots of the Resources Merit (p. 124) equal to her Mantle dots, to a maximum of fve, for the scene.",
            "4": "Once per story, reduce your character’s Goblin Debt by his Mantle rating.",
            "5": "Once per scene, you may spend a Willpower point to learn the current heart’s desire of any character present.",

        },
        "book": "CTL 2e p.161"
    },
    "barter": {
        "name": "Court of Barter",
        "description": "The farmer will let you sleep in her barn if you brush the horses. The hitchhiker tells stories to the driver who takes her from Boston to Albany, keeping him awake and entertained as the long miles pass. For a week’s worth of the Fairest’s beauty, the hag will help her fnd her longlost love. People have bartered since time immemorial, trading their surplus to those with needed skills, and letting their trash transmute into another’s treasure. Changelings who join the Court of Barter realize that everything has value, even if it’s hard to see. It’s this court that takes in most of the newly escaped Lost, guiding them away from the stalls in Tumbledown where less unscrupulous merchants sense their desperation for information, or vengeance, or word of lost families. The Barter Court makes itself available to witness bargains, letting the entrants know whether their deal is fair or not. While this is generally met with approval, some sellers take it as an insult that their clients distrust them so openly.",
        "mantle_benefits": {
            "0": "The Mantle for a Barterer manifests in even tones and calming scents. They leave drips of sealing wax in their wake. Your character gains a Glamour point whenever he successfully intercedes on someone else’s behalf in an unfair deal.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to read someone’s situation from their behavior.",
            "2": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to make deals and agreements in Tumbledown.",
            "3": "Regain a Willpower point whenever you resolve the Oathbreaker Condition (p. 343), or when someone else resolves it due to your inﬂuence or meddling.",
            "4": "Once per chapter, when the Storyteller spends your Goblin Debt to impose a Condition, you may replace the Condition with another of the same general type (mental, physical, emotional, etc.).",
            "5": "Once per chapter, you may ask the Storyteller if someone your character is dealing with has left a loophole or catch that could disadvantage him in a deal.",
        },
        "book": "CTL 2e p.161"
    },
    "favors": {
        "name": "Court of Favors",
        "description": "Jill never carries cash, but she’s got great credit. Give her a few days and she’ll make it up to you. If the Pie Man parts with one of his goblin-fruit tarts, Ash promises she’ll bring him the fnest berries from a secret shrub in the Hedge only she can fnd. Favors are a currency built on risk and trust on the parts of both seller and buyer. The seller trusts they’ll recoup their investment; the buyer trusts that, when the bill comes due, they’re not forced to pay more than what their purchase was worth. The Lost who swear to the Court of Favors tend to be shrewd listeners and smooth talkers. They promise just enough, and know when to walk away from a bad deal. Whatever it is their business partner needs, the changeling knows a guy who can get it for him. Their networks are vast, and they rarely tolerate oathbreakers in their ranks.",
        "mantle_benefits": {
            "0": "The Mantle for a Favors courtier is the sound of bells tolling or hands clasping to seal a bargain. They leave the impression of a small, metallic footprint in their wake. Your character gains a Glamour point whenever she successfully trades with someone.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to persuade someone to make a bargain (p. 214).",
            "2": "Gain the benefits of the Fixer Merit (p. 122) even if your character doesn’t qualify.",
            "3": "Other characters take a dice penalty equal to your character’s Mantle dots to mundane rolls to swindle her or lie to her about a deal or promise.",
            "4": "Once per chapter, you may accept a point of Goblin Debt to pawn off an obligation from a bargain onto another changeling without being personally involved.",
            "5": "Once per chapter, you may reroll any mundane action that would pay off a favor your character owes and choose which result to keep.",
        },
        "book": "CTL 2e p.161"
    },
    "shady_deals": {
        "name": "Court of Shady Deals",
        "description": "The gentle-natured man would never do harm to another living being, but oh, how his neighbor snores at night. If only someone would pinch his nose shut. Sure, you don’t have the Snowdrop Crown in your backpack, but if it were to fnd its way there, and then to Tumbledown, well…don’t you want to know if your daughter still dreams about her father? What’s one more throat cut, after all the lives your Keeper made you take? Members of the Court of Shady Deals are willing to take on the jobs most others would reject outright. They do the hard jobs, the ones that require cold logic, steady hands, and no aversion to blood. They do what’s necessary. They’re not sorry. The Lost who swear to this court are also the freehold’s defenders. If the Huntsmen come near, they know where to hide the bodies.",
        "mantle_benefits": {
            "0": "The Mantle for a Shady Deal courtier is the sound of knives rasping on whetstone. They leave the impression of a small, metallic footprint in their wake. Your character gains a Glamour point whenever he successfully hides evidence of a dirty deed when someone comes looking for it.",
            "1": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to pick a lock or break into a place he doesn’t belong.",
            "2": "Gain bonus dice equal to your character’s Mantle dots on mundane rolls to escape a sticky situation unnoticed.",
            "3": "Your character may use Goblin Contracts without incurring Goblin Debt a number of times per chapter equal to his Mantle rating.",
            "4": "You may spend a Willpower point to ignore all the effects of the Oathbreaker Condition for one turn.",
            "5": "Once per chapter, you may reroll a surprise attack roll and choose which result to keep.",
        },
        "book": "CTL 2e p.161"
    },
}

def get_court(court_name):
    """Get a specific court by name."""
    return ALL_COURTS.get(court_name.lower().replace(" ", "_"))

def get_all_courts():
    """Get all courts."""
    return ALL_COURTS.copy()

def get_court_benefits(court_name):
    """Get the benefits of a specific court."""
    return ALL_COURTS.get(court_name.lower().replace(" ", "_")).get("mantle_benefits")