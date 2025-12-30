"""
Demon Embeds and Exploits for Chronicles of Darkness.
Embeds are minor supernatural abilities grouped by Incarnation.
Exploits are powerful reality-warping abilities that cost Aether.

At character creation:
- Choose 4 Embeds and/or Exploits (total)
- Must choose at least 1 Embed from Incarnation's list
- Choose 1 Embed as the First Key
- Exploits must have suitable prerequisites
"""

# ==================== EMBEDS ====================
# Embeds are organized by Incarnation

# Cacophony (Destroyer Incarnation)
EMBEDS_CACOPHONY = {
    "apple_of_discord": {
        "name": "Apple of Discord",
        "description": "Make an object irresistibly desirable to all humans present. Causes anyone affected to gain the obsessed condition and will actively work to gain the object and prevent anyone else having it.",
        "pool": "Manipulation + Expression Vs. Integrity",
        "source": "FoH 93"
    },
    "anarchism": {
        "name": "Anarchism",
        "description": "Causes a target to no longer care about social repercussions for their actions. Causes all appeals to peers, law or authority to be ignored.",
        "pool": "Manipulation + Politics - Composure",
        "source": "FoH 94"
    },
    "breakdown": {
        "name": "Breakdown",
        "description": "When the target tries to use a skill selected by the Embed user, they will instead use a different skill from the same category (Social, Physical, Mental).",
        "pool": "Wits + Medicine - Resolve",
        "source": "FoH 94"
    },
    "bystander_effect": {
        "name": "Bystander Effect",
        "description": "Attack someone in plain few without anyone else choosing to intervene.",
        "pool": "Manipulation + Intimidation",
        "source": "DtD 125"
    },
    "cause_and_effect": {
        "name": "Cause and Effect",
        "description": "Invoking the Butterfly effect and providing an unrelated stimulus, the Demon causes a small event of nearly any sort to take place in their presence.",
        "pool": "Wits + [any Skill]",
        "source": "DtD 125"
    },
    "combustion": {
        "name": "Combustion",
        "description": "The Demon renders almost any object flammable or prone to explosion.",
        "pool": "Wits + Science",
        "source": "DtD 126"
    },
    "cool_heads_prevail": {
        "name": "Cool Heads Prevail",
        "description": "Prevents or ends a combat immediately, as those involved relax.",
        "pool": "Manipulation + Empathy -Composure",
        "source": "DtD 126"
    },
    "deafen": {
        "name": "Deafen",
        "description": "Literally deafens a select victim.",
        "pool": "Manipulation + Medicine - Stamina",
        "source": "DtD 126"
    },
    "devils_advocate": {
        "name": "Devil's Advocate",
        "description": "Causes a victim to reflexively take the opposite stance to a person's most recently stated position.",
        "pool": "Manipulation + Subterfuge - Resolve",
        "source": "DtD 126"
    },
    "fire_drill": {
        "name": "Fire Drill",
        "description": "Activates alarms or sirens in the nearby area, penalising the perception rolls of anyone who does not know it is a false alarm by the Demon's Primum.",
        "pool": "Wits + Science",
        "source": "FoH 94"
    },
    "fractal_reality": {
        "name": "Fractal Reality",
        "description": "Encodes an action that has previously been performed to happen again under the same circumstances. Requires an exceptional success or a success on a chance die to perform. Repeating that action (performing an action with the same skill) will automatically cause an exceptional success on a single success. All future uses after that are penalised with no 10-again.",
        "pool": "Wits + Science",
        "source": "FoH 95"
    },
    "hesitation": {
        "name": "Hesitation",
        "description": "Forces a target to react slowly, potentially penalizing initiative.",
        "pool": "Manipulation + Intimidation - Resolve",
        "source": "DtD 127"
    },
    "hush": {
        "name": "Hush",
        "description": "Silences a combat, allowing it to take place unheard by those nearby.",
        "pool": "Dexterity + Brawl - Defense",
        "source": "DtD 127"
    },
    "just_bruised": {
        "name": "Just Bruised",
        "description": "Allows the demon to mitigate the damage taken from almost any source.",
        "pool": "Wits + Medicine",
        "source": "DtD 128"
    },
    "knockout_punch": {
        "name": "Knockout Punch",
        "description": "Knock out a victim with a single blow for a defined period.",
        "pool": "Dexterity + Brawl - Defense",
        "source": "DtD 129"
    },
    "left_or_right": {
        "name": "Left or Right?",
        "description": "Force the outcome of an event that contains only two possibilities, such as a coin flip.",
        "pool": "Manipulation + Science",
        "source": "DtD 129"
    },
    "lucky_break": {
        "name": "Lucky Break",
        "description": "The demon achieves a specific desired ends through random chance.",
        "pool": "Manipulation + Occult",
        "source": "DtD 129"
    },
    "merciless_gunman": {
        "name": "Merciless Gunman",
        "description": "Enables the demon to casually massacre large numbers of individuals quickly with a firearm.",
        "pool": "Dexterity + Firearms",
        "source": "DtD 130"
    },
    "no_quarter": {
        "name": "No Quarter",
        "description": "The demon intensifies a fight, causing all those involved to aim to kill or maim their opponents, refusing to back down.",
        "pool": "Manipulation + Brawl vs. Resolve",
        "source": "DtD 130"
    },
    "on_the_mend": {
        "name": "On the Mend",
        "description": "Heals a target, potentially even of aggravated damage.",
        "pool": "Wits + Medicine",
        "source": "DtD 131"
    },
    "password_entropy": {
        "name": "Password Entropy",
        "description": "When entering a password in a computer or machine, you will enter the correct password.",
        "pool": "Wits + Computer",
        "source": "FoH 95"
    },
    "play_possum": {
        "name": "Play Possum",
        "description": "Die for a number of hours equal to Primum, after which time come back to life. Damage taken after 'dying' is restored, but wounds suffered prior remain.",
        "pool": "Manipulation + Medicine",
        "source": "FoH 96"
    },
    "raw_materials": {
        "name": "Raw Materials",
        "description": "The demon breaks an object, causing a new object of similar size but of the demon's choosing to appear in the location by happenstance not long after.",
        "pool": "Manipulation + Crafts",
        "source": "DtD 131"
    },
    "ripple": {
        "name": "Ripple",
        "description": "Causes a ripple effect with the entire scene suffering misfortune and extra damage. Any damage taken will be suffered again next turn with the same severity and half the total amount of damage from a secondary but related source.",
        "pool": "Wits + Science",
        "source": "FoH 96"
    },
    "sabotage": {
        "name": "Sabotage",
        "description": "With a touch, the demon cripples a device such that it will no longer function until repaired.",
        "pool": "Dexterity + Crafts",
        "source": "DtD 131"
    },
    "shatter": {
        "name": "Shatter",
        "description": "Allows the demon to utterly destroy small objects with a touch.",
        "pool": "Wits + Crafts",
        "source": "DtD 131"
    },
    "shifty_eyes": {
        "name": "Shifty Eyes",
        "description": "Causes a victim to distrust another chosen individual.",
        "pool": "Manipulation + Subterfuge - Resolve",
        "source": "DtD 132"
    },
    "special_someone": {
        "name": "Special Someone",
        "description": "Allows the demon to stumble upon an individual matching certain desired criteria, though never a specific person.",
        "pool": "Wits + Empathy",
        "source": "DtD 132"
    },
    "trip": {
        "name": "Trip",
        "description": "Causes someone to trip over and suffer the \"Knocked Down\" tilt.",
        "pool": "Wits + Athletics - Dexterity",
        "source": "FoH 96"
    },
    "victory_at_any_price": {
        "name": "Victory at any Price",
        "description": "Increase the number of successes on the prior roll by one. The result of the \"Victory at any Price\" roll determines the toll the Demon pays in blood for use of this ability.",
        "pool": "Wits + Science",
        "source": "FoH 97"
    }
}

# Instrumental (Guardian Incarnation)
EMBEDS_INSTRUMENTAL = {
    "ambush": {
        "name": "Ambush",
        "description": "Prepare a perfect ambush for some victims, gaining surprise for the first round of a combat.",
        "pool": "Wits + Stealth",
        "source": "DtD 132"
    },
    "call_out": {
        "name": "Call Out",
        "description": "Weakens the desire of a target's allies to continue fighting. The target's allies will easily suffer the beaten down tilt, run away or surrender after minor damage.",
        "pool": "Manipulation + Intimidation vs. Presence + Supernatural Tolerance",
        "source": "FoH 97"
    },
    "check_backdrop": {
        "name": "Check Backdrop",
        "description": "The demon curses a combat with imprecision and confusion, such that all firearm attacks that do not take at least one turn aiming will automatically miss.",
        "pool": "Manipulation + Firearms",
        "source": "DtD 133"
    },
    "data_retrieval": {
        "name": "Data Retrieval",
        "description": "Become capable of viewing any data that a device has ever recorded or observed, but only at the time point that you specify.",
        "pool": "Wits + Computer",
        "source": "FoH 97"
    },
    "data_wipe": {
        "name": "Data Wipe",
        "description": "Deletes electronic data more completely, penalises any attempts to recover the data by the Demon's Primum.",
        "pool": "Wits + Computer",
        "source": "FoH 98"
    },
    "download_knowledge": {
        "name": "Download Knowledge",
        "description": "Temporarily grants bonus Skill dots to a Demon.",
        "pool": "Wits + Computers",
        "source": "DtD 133"
    },
    "efficiency": {
        "name": "Efficiency",
        "description": "Enables the demon to perform extended actions and tasks with greatly increased speed.",
        "pool": "Wits + Academics",
        "source": "DtD 133"
    },
    "ellipses": {
        "name": "Ellipses",
        "description": "Causes a victim to get engrossed in some distracting activity.",
        "pool": "Manipulation + Expression",
        "source": "DtD 133"
    },
    "freeze_assets": {
        "name": "Freeze Assets",
        "description": "Perfectly blocks a victim from being capable of spending or acquiring any form of money for one day.",
        "pool": "Manipulation + Academics - Resources",
        "source": "DtD 134"
    },
    "fulcrum_point": {
        "name": "Fulcrum Point",
        "description": "Moves even very large objects a short distance with a simple push.",
        "pool": "Wits + Science",
        "source": "DtD 135"
    },
    "functional_identity": {
        "name": "Functional Identity",
        "description": "Change the functional purpose of a tool, allowing you to use its bonuses towards a different purpose.",
        "pool": "Wits + Crafts",
        "source": "FoH 98"
    },
    "fungible_knowledge": {
        "name": "Fungible Knowledge",
        "description": "Swaps the demon's skill ratings for a scene.",
        "pool": "Wits + Academics",
        "source": "DtD 135"
    },
    "high_of_birth": {
        "name": "High of Birth",
        "description": "Retroactively alters a human's fate so that they become wealthy or gifted and gain merits. A week later, the God Machine will send an angel to investigate the individual.",
        "pool": "Manipulation + Politics",
        "source": "FoH 98"
    },
    "knock_off": {
        "name": "Knock-Off",
        "description": "Dramatically change the value of an object, or change an equipment bonus.",
        "pool": "Dexterity + Larceny",
        "source": "FoH 99"
    },
    "like_i_built_it": {
        "name": "Like I Built It",
        "description": "Grants the demon the ability to perfectly use and understand an object or structure, gaining bonus dice to its use.",
        "pool": "Wits + Craft",
        "source": "DtD 135"
    },
    "the_map_is_not_the_territory": {
        "name": "The Map Is Not The Territory",
        "description": "Inhibits a victim's ability to gain any sort of knowledge or benefit from printed materials.",
        "pool": "Manipulation + Academics - Intelligence",
        "source": "DtD 136"
    },
    "miles_away": {
        "name": "Miles Away",
        "description": "Fills the demon's ears with a comforting sound, that grants bonuses to resist distraction or suffering.",
        "pool": "Wits + Expression",
        "source": "DtD 136"
    },
    "momentum": {
        "name": "Momentum",
        "description": "Allows the demon to use any other character's action to springboard their own, granting bonus dice based off that character's roll.",
        "pool": "Wits + Science",
        "source": "DtD 136"
    },
    "open_sesame": {
        "name": "Open Sesame",
        "description": "Manipulates probability so that the Demon will \"discover\" that a door, window or other entrance to somewhere is unlocked.",
        "pool": "Wits + Larceny - Special Penalties",
        "source": "FoH 99"
    },
    "read_hostility": {
        "name": "Read Hostility",
        "description": "Grants the ability to the demon or others to sense hostile intentions of new arrivals to the scene.",
        "pool": "Wits + Subterfuge",
        "source": "DtD 137"
    },
    "right_tools_right_job": {
        "name": "Right Tools, Right Job",
        "description": "Allows the demon to use virtually any tool for any task.",
        "pool": "Wits + Craft",
        "source": "DtD 137"
    },
    "shift_consequences": {
        "name": "Shift Consequences",
        "description": "Transfer the burden of some baleful effect, such as harm or embarrassment, from a beneficiary to someone or something else.",
        "pool": "Manipulation + Occult - Varies",
        "source": "DtD 137"
    },
    "soup_up": {
        "name": "Soup Up",
        "description": "Improves a vehicle's stats to closely resemble that often depicted in Hollywood.",
        "pool": "Dexterity + Drive - Special Penalties",
        "source": "FoH 99"
    },
    "strike_first": {
        "name": "Strike First",
        "description": "Moves a demon to the top of the Initiative order, even if they were surprised.",
        "pool": "Wits + Brawl",
        "source": "DtD 138"
    },
    "synthesis": {
        "name": "Synthesis",
        "description": "Scans a scene, psychometrically determining the cause of recent changes.",
        "pool": "Wits + Investigation",
        "source": "DtD 138"
    },
    "tag_and_release": {
        "name": "Tag & Release",
        "description": "Marks a person or object, allowing the demon to unerringly be capable of finding it for several days.",
        "pool": "Dexterity + Expression",
        "source": "DtD 138"
    },
    "tools_into_toys": {
        "name": "Tools Into Toys",
        "description": "Penalizes the use of tools in a task, possibly even rendering it impossible.",
        "pool": "Manipulation + Craft",
        "source": "DtD 139"
    },
    "trivia": {
        "name": "Trivia",
        "description": "Changes the nature of Trivia in the world so that it becomes truth.",
        "pool": "Manipulation + Expression",
        "source": "FoH 100"
    },
    "turn_blade": {
        "name": "Turn Blade",
        "description": "Significantly reduces the damage from incoming melee weapons.",
        "pool": "Wits + Weaponry",
        "source": "DtD 139"
    },
    "wasted_time": {
        "name": "Wasted Time",
        "description": "Makes an action take twice as long to complete, due to hiccups and small issues that go wrong.",
        "pool": "Wits + Science",
        "source": "FoH 100"
    }
}

# Mundane (Psychopomp Incarnation)
EMBEDS_MUNDANE = {
    "alibi": {
        "name": "Alibi",
        "description": "Allows the demon to briefly dislocate from her cover, performing actions elsewhere and unsuspected.",
        "pool": "Manipulation + Stealth",
        "source": "DtD 139"
    },
    "associate_and_integrate": {
        "name": "Associate and Integrate",
        "description": "Change a single fact about the relationship between two people. Can be detected by unseen sense.",
        "pool": "Manipulation + Socialise (Vs. Resolve + Composure)",
        "source": "FoH 100"
    },
    "authorized": {
        "name": "Authorized",
        "description": "Allows the demon to convince anyone that they have the legal right to be where they are doing what they are doing.",
        "pool": "Manipulation + Intimidation - Intelligence",
        "source": "DtD 140"
    },
    "clothes_make_the_man": {
        "name": "Clothes Make the Man",
        "description": "Change total dots in the target skill to three and one speciality OR gain three specialities and one extra dot in the target skill temporarily, but the demon is branded an Impostor.",
        "pool": "Wits + Persuasion Vs. Wits + Target Skill",
        "source": "FoH 101"
    },
    "cuckoos_egg": {
        "name": "Cuckoo's Egg",
        "description": "Allows the demon to replace an object with another of comparable size, while forcing the owner to fail to notice.",
        "pool": "Dexterity + Larceny",
        "source": "DtD 140"
    },
    "deep_cover": {
        "name": "Deep Cover",
        "description": "Allows for the Spoof ability to make the user appear as another Supernatural type. Allows the ability to determine the flavour of supernatural after the first time experiencing being observed magically.",
        "pool": "Manipulation + Occult",
        "source": "FoH 101"
    },
    "diversion": {
        "name": "Diversion",
        "description": "Forces some targets to look away from a desired area, and to not look back for some time.",
        "pool": "Manipulation + Expression",
        "source": "DtD 140"
    },
    "dont_i_know_you": {
        "name": "Don't I Know You?",
        "description": "Causes a target to find the demon a reminder of familiar faces, improving the demon's social standing with the target.",
        "pool": "Manipulation + Subterfuge - Resolve",
        "source": "DtD 141"
    },
    "earworm": {
        "name": "Earworm",
        "description": "Infects a victim with a consuming thought, which penalizes perception and focus.",
        "pool": "Manipulation + Expression - Composure",
        "source": "DtD 142"
    },
    "going_native": {
        "name": "Going Native",
        "description": "Temporarily turn yourself into a human.",
        "pool": "Wits + Socialise",
        "source": "FoH 102"
    },
    "homogeneous_memory": {
        "name": "Homogeneous Memory",
        "description": "Manipulates the memories of participants in a previous scene, forcing all witnesses to believe a cover story to explain its events chosen by the demon.",
        "pool": "Manipulation + Subterfuge - Resolve",
        "source": "DtD 142"
    },
    "identity_theft": {
        "name": "Identity Theft",
        "description": "Forces a victim into a deep sleep for several hours, while the demon usurps their identity.",
        "pool": "Manipulation + Subterfuge",
        "source": "DtD 142"
    },
    "idle_conversation": {
        "name": "Idle Conversation",
        "description": "Prevents listeners from mundanely eavesdropping on the demon's conversations.",
        "pool": "Manipulation + Socialize",
        "source": "DtD 143"
    },
    "in_my_pocket": {
        "name": "In My Pocket",
        "description": "Allows the demon to produce a random instance of virtually any desired object from their pocket, provided it has not been established as not being there already.",
        "pool": "Dexterity + Larceny",
        "source": "DtD 143"
    },
    "interference": {
        "name": "Interference",
        "description": "Jams the ability of angels and the God-Machine to detect demons in an area.",
        "pool": "Manipulation + Subterfuge",
        "source": "DtD 144"
    },
    "last_place_you_look": {
        "name": "Last Place You Look",
        "description": "Allows the demon to detect hidden objects in an area and grants bonuses to find them, though it does not inform the demon what those objects might be.",
        "pool": "Wits + Larceny",
        "source": "DtD 144"
    },
    "like_the_movies": {
        "name": "Like the Movies",
        "description": "After having scored an exceptional success or a failure on an action, contrived circumstance allows for a dramatic turnaround, or change in the user's fortunes. The change in fortune results in that action having been performed with a single success, but with a narrative twist. The narrative twist is beneficial if it was an exceptional success, but negative if it was a failure previously.",
        "pool": "Wits + Academics",
        "source": "FoH 102"
    },
    "living_recorder": {
        "name": "Living Recorder",
        "description": "Allows the demon to specify a target individual to be a \"living recorder\" for specific duration. The demon can later touch the recorder and experience all that they did during this period.",
        "pool": "Manipulation + Investigation",
        "source": "DtD 145"
    },
    "lost_in_the_crowd": {
        "name": "Lost in the Crowd",
        "description": "Enables the demon to remain perfectly undetectable by mundane means so long as they hide in a crowd of at least ten people.",
        "pool": "Wits + Stealth",
        "source": "DtD 145"
    },
    "meaninglessness": {
        "name": "Meaninglessness",
        "description": "Curses a victim such that they lose the ability to comprehend all attempts at communication, in any medium, for a short time.",
        "pool": "Manipulation + Academics",
        "source": "DtD 145"
    },
    "mistaken_identity": {
        "name": "Mistaken Identity",
        "description": "Causes the Demon and the target to be mistaken for each other for a number of hours.",
        "pool": "Manipulation + Persuasion - Composure",
        "source": "FoH 103"
    },
    "never_here": {
        "name": "Never Here",
        "description": "Targets of this Embed are forced to forget the demon was even present in a previous scene at all, instead coming up with their own explanations for events she caused there.",
        "pool": "Manipulation + Stealth - Resolve",
        "source": "DtD 146"
    },
    "occams_razor": {
        "name": "Occam's Razor",
        "description": "Forcing onlookers and the general area to try to rationalize what they witness, the demon gains a bonus to compromise rolls for manifesting obviously supernatural effects like Exploits and Demonic Transformations.",
        "pool": "Manipulation + Persuasion",
        "source": "DtD 146"
    },
    "partitioned_memory": {
        "name": "Partitioned Memory",
        "description": "Causes a brief psychic split. The demon can feed fabricated information to a telepathic read, and can multitask a pair of Mental actions.",
        "pool": "Wits + Subterfuge",
        "source": "DSG 100"
    },
    "persistent_legend": {
        "name": "Persistent Legend",
        "description": "Allows a Legend to remain active permanently, instead of disappearing at the end of a scene.",
        "pool": "Wits + Academics",
        "source": "FoH 103"
    },
    "quick_change": {
        "name": "Quick Change",
        "description": "Instantly transforms the demon's outfit to meet desired specifications.",
        "pool": "Manipulation + Subterfuge",
        "source": "DtD 146"
    },
    "the_voting_dead": {
        "name": "The Voting Dead",
        "description": "Assume the identity of a dead person, which for the period which the Embed is active replaces the real identity of your cover.",
        "pool": "Manipulation + Politics",
        "source": "FoH 103"
    },
    "unperson": {
        "name": "Unperson",
        "description": "For one scene, strips a victim of their ability to identify themselves to anyone, even those intimately familiar with them.",
        "pool": "Manipulation + Subterfuge - Composure",
        "source": "DtD 147"
    },
    "wave_function_collapse": {
        "name": "Wave Function Collapse",
        "description": "Traps a supernatural being in their current form, preventing them from changing. Demon (or non-human supernatural) forms cannot turn into humans, human-forms cannot turn into demon forms temporarily and Demons in cover cannot separate from their cover in any way.",
        "pool": "Dexterity + Brawl Vs. Stamina + Supernatural Tolerance",
        "source": "FoH 104"
    },
    "without_a_trace": {
        "name": "Without a Trace",
        "description": "Vaporizes all physical traces of the demon from a scene.",
        "pool": "Manipulation + Investigation",
        "source": "DtD 147"
    },
    "you_can_tell_me": {
        "name": "You Can Tell Me",
        "description": "Causes the target to speak nothing but the whole truth about a subject.",
        "pool": "Manipulation + Empathy - Composure",
        "source": "FoH 105"
    }
}

# Vocal (Messenger Incarnation)
EMBEDS_VOCAL = {
    "across_a_crowded_room": {
        "name": "Across a Crowded Room",
        "description": "Enables the demon to whisper to any target or targets he can see.",
        "pool": "Manipulation + Subterfuge",
        "source": "DtD 148"
    },
    "animal_communication": {
        "name": "Animal Communication",
        "description": "Issues a task to an animal.",
        "pool": "Manipulation + Animal Ken",
        "source": "DtD 148"
    },
    "animal_messenger": {
        "name": "Animal Messenger",
        "description": "Tasks an animal with delivering a message to a specific person, who will be able to comprehend the creature's expression.",
        "pool": "Manipulation + Animal Ken",
        "source": "DtD 148"
    },
    "borrowed_expertise": {
        "name": "Borrowed Expertise",
        "description": "Allows the demon to lend out their skill dots and specialties to other people.",
        "pool": "Manipulation + [Granted Skill]",
        "source": "DtD 149"
    },
    "common_misconception": {
        "name": "Common Misconception",
        "description": "Causes a target to operate based on faulty information that \"everyone knows\", penalizing a skill roll.",
        "pool": "Manipulation + Science",
        "source": "DtD 149"
    },
    "eavesdrop": {
        "name": "Eavesdrop",
        "description": "Enables the demon to understand any conversation he can see.",
        "pool": "Wits + Empathy",
        "source": "DtD 149"
    },
    "everybody_knows": {
        "name": "Everybody Knows",
        "description": "Sparks a vile rumor about a victim, which rapidly spreads memetically.",
        "pool": "Manipulation + Subterfuge",
        "source": "DtD 150"
    },
    "find_the_leak": {
        "name": "Find the Leak",
        "description": "Informs the demon of who in a group would most desire to talk about a particular topic, and grants bonuses to encourage them to do so.",
        "pool": "Wits + Empathy",
        "source": "DtD 150"
    },
    "freudian_slip": {
        "name": "Freudian Slip",
        "description": "Forces a mortal to make an honest and heartfelt response to the last thing the demon said.",
        "pool": "Manipulation + Empathy (-Composure)",
        "source": "DtD 150"
    },
    "hearts_desire": {
        "name": "Heart's Desire",
        "description": "Informs the demon of the target's Aspirations, Virtue, and Vice.",
        "pool": "Wits + Empathy - Composure",
        "source": "DtD 151"
    },
    "imagine": {
        "name": "Imagine",
        "description": "Causes a spark of clarity in humans that allows them to see the world free of the God Machine and grants conditions appropriate to such a life-changing event.",
        "pool": "Manipulation + Persuasion",
        "source": "FoH 105"
    },
    "the_look": {
        "name": "The Look",
        "description": "When in eye contact, gives a look that causes total body paralysis while maintained. The victim will slowly die of organ failure or pass out if The Look is maintained for an extended period, but external damage breaks the effect.",
        "pool": "Manipulation + Intimidation - Stamina",
        "source": "FoH 105"
    },
    "loose_lips": {
        "name": "Loose Lips",
        "description": "Use social activity to cause a target to speak freely about information that they would not otherwise share, removing Doors. The victim passes out with only a hazy memory of the interaction afterwards.",
        "pool": "Manipulation + Socialise - Stamina",
        "source": "FoH 106"
    },
    "marco_polo": {
        "name": "Marco Polo",
        "description": "The demon whispers a short tune or phrase which anyone present is forced to complete, ruining stealth and ambushes.",
        "pool": "Manipulation + Persuasion - Composure",
        "source": "DtD 151"
    },
    "mercury_retrograde": {
        "name": "Mercury Retrograde",
        "description": "Forces a miscommunication in a conversation between two targets, which the demon then gets bonuses to exploit.",
        "pool": "Manipulation + Subterfuge - Wits",
        "source": "DtD 151"
    },
    "muse": {
        "name": "Muse",
        "description": "Instills an idea in a target, and grants the demon bonuses to encourage the target to act on it.",
        "pool": "Manipulation + Expression - Resolve",
        "source": "DtD 152"
    },
    "the_only_word_that_matters": {
        "name": "The Only Word That Matters",
        "description": "Causes a person to only say what the Demon wants them to say. Can either apply generally to everything the target says, or can be coded for specific trigger events.",
        "pool": "Manipulation + Expression - Composure",
        "source": "FoH 106"
    },
    "recurring_hallucinations": {
        "name": "Recurring Hallucinations",
        "description": "Curses a victim with nightmarish hallucinations that last for days, penalizing all Mental and Social rolls and forcing regular breaking points.",
        "pool": "Manipulation + Occult - Resolve",
        "source": "DtD 152"
    },
    "remote_link_up": {
        "name": "Remote Link-Up",
        "description": "Allows a Demon to create sensory links between another individual or a group of individual that allows them to share their natural senses (e.g. vision or hearing.)",
        "pool": "Wits + Socialise",
        "source": "FoH 107"
    },
    "rhetoric": {
        "name": "Rhetoric",
        "description": "Causes the target to temporarily support the Demon's argument in a debate, removing a Door and being temporarily sympathetic to the Demon's point of view.",
        "pool": "Wits + Subterfuge",
        "source": "FoH 107"
    },
    "social_dynamics": {
        "name": "Social Dynamics",
        "description": "Grants the demon knowledge of the dynamics and status of all those within a group, granting bonuses to social interactions that exploits this knowledge.",
        "pool": "Wits + Socialize",
        "source": "DtD 153"
    },
    "social_engineering": {
        "name": "Social Engineering",
        "description": "Manipulates a target into divulging information that they shouldn't under normal circumstances. The information also provides a +1 bonus to a later, related Computer, Investigation or Persuasion roll.",
        "pool": "Manipulation + Persuasion",
        "source": "FoH 107"
    },
    "special_message": {
        "name": "Special Message",
        "description": "Instills a secret message into a medium such as a song or a work of art, intended for a particular recipient, who will understand the message when they are exposed to the media in question.",
        "pool": "Manipulation + Expression",
        "source": "DtD 153"
    },
    "strength_through_adversity": {
        "name": "Strength Through Adversity",
        "description": "Causes a target to suffer incredible hardship that lasts for several days and escalates over that period. Once the effect ends, the hardship disappears but the target may come out ahead having laboured under conditions that are resolved.",
        "pool": "Manipulation + Intimidation - Resolve",
        "source": "FoH 108"
    },
    "sum_of_all_fears": {
        "name": "Sum of all Fears",
        "description": "Learn a target's fears, breaking points, loved ones, derangements or Conditions that could be exploited to scare them.",
        "pool": "Wits + Empathy - Composure",
        "source": "FoH 108"
    },
    "tower_of_babel": {
        "name": "Tower of Babel",
        "description": "Curses all those present on the scene with the inability to communicate with anyone else for a few turns.",
        "pool": "Manipulation + Socialize",
        "source": "DtD 154"
    },
    "trick_of_the_light": {
        "name": "Trick of the Light",
        "description": "Causes a single target to see a fleeting and vague illusion of the demon's specifications.",
        "pool": "Manipulation + Investigation - Wits",
        "source": "DtD 154"
    },
    "trust_no_one": {
        "name": "Trust No One",
        "description": "Inflicts a victim with crippling paranoia, preventing them from making use of merits that depend on others, or even to interact casually with friends.",
        "pool": "Manipulation + Subterfuge - Resolve",
        "source": "DtD 155"
    },
    "voice_of_the_machine": {
        "name": "Voice of the Machine",
        "description": "Allows the demon to listen in to what the God-Machine is saying in an area, which may inform what angels are up to or other such knowledge.",
        "pool": "Wits + Craft",
        "source": "DtD 155"
    },
    "vox": {
        "name": "Vox",
        "description": "Change your voice to perfectly imitate any other voice or mimic other sounds previously heard as the Demon sees fit.",
        "pool": "Manipulation + Expression",
        "source": "FoH 109"
    }
}

# Combined Embeds Dictionary
ALL_EMBEDS = {
    **EMBEDS_CACOPHONY,
    **EMBEDS_INSTRUMENTAL,
    **EMBEDS_MUNDANE,
    **EMBEDS_VOCAL
}

# Embeds by Incarnation for easy lookup
EMBEDS_BY_INCARNATION = {
    "destroyer": EMBEDS_CACOPHONY,
    "guardian": EMBEDS_INSTRUMENTAL,
    "psychopomp": EMBEDS_MUNDANE,
    "messenger": EMBEDS_VOCAL
}

# ==================== EXPLOITS ====================
# Exploits are powerful reality-warping abilities that cost Aether

DEMON_EXPLOITS = {
    "addictive_presence": {
        "name": "Addictive Presence",
        "cost": "*",
        "pool": "Presence + Socialize + Primum",
        "description": "Render a target Addicted to your presence.",
        "source": "DTD 158"
    },
    "affliction": {
        "name": "Affliction",
        "cost": "*",
        "pool": "Strength + Medicine + Primum vs (Stamina or Resolve) + Tolerance",
        "description": "Inflict interesting new physical or mental afflictions.",
        "source": "DTD 159"
    },
    "allies_into_gold": {
        "name": "Allies into Gold",
        "cost": "*",
        "pool": "Intelligence + Socialize + Primum",
        "description": "Shift the context of relationships in the form of Social Merits.",
        "source": "DTD 159"
    },
    "animate": {
        "name": "Animate",
        "cost": "*",
        "pool": "Presence + Crafts + Primum",
        "description": "Animate an object as a servant for a scene.",
        "source": "DTD 161"
    },
    "behind_the_curtain": {
        "name": "Behind the Curtain",
        "cost": "●●",
        "pool": "Intelligence + Computer + Primum",
        "description": "Travel from God-Machine Infrastructure to other Infrastructure anywhere in the world.",
        "source": "DTD 161"
    },
    "break_the_dam": {
        "name": "Break the Dam",
        "cost": "*",
        "pool": "Presence + Science + Primum - Stamina",
        "description": "Bursts a container of liquid, causing Environmental Tilts. Can also target a living being for lethal damage.",
        "source": "FoH 110"
    },
    "break_to_heal": {
        "name": "Break to Heal",
        "cost": "*",
        "pool": "Strength + Medicine + Primum",
        "description": "Smash an object and transfer its former integrity to another person in the form of healing.",
        "source": "DTD 162"
    },
    "context_matters": {
        "name": "Context Matters",
        "cost": "●●/●●●●●",
        "pool": "Presence + Persuasion + Primum",
        "description": "Ease compromise risks by providing at least five witnesses with an alibi or explanation.",
        "source": "FoH 111"
    },
    "decoy": {
        "name": "Decoy",
        "cost": "*",
        "pool": "Presence + Stealth + Primum",
        "description": "Independently colocate as a material Cover and a demonic form in astral Twilight.",
        "source": "Iface 123"
    },
    "deep_pockets": {
        "name": "Deep Pockets",
        "cost": "*",
        "pool": "Strength + Larceny + Primum",
        "description": "Pull a specific handheld item out of your pocket, even if it wasn't there.",
        "source": "DTD 162"
    },
    "demon_car": {
        "name": "Demon Car",
        "cost": "●+",
        "pool": "Strength + Drive + Primum",
        "description": "Merge your demonic form with any vehicle.",
        "source": "FoH 111"
    },
    "demon_house": {
        "name": "Demon House",
        "cost": "*",
        "pool": "Presence + Stealth + Primum",
        "description": "Merge with a building indefinitely.",
        "source": "DTD 162"
    },
    "devour_infrastructure": {
        "name": "Devour Infrastructure",
        "cost": "*",
        "pool": "Strength + Survival + Primum",
        "description": "Break down a small part of infrastructure, siphoning Aether equal to Primum, but suffer regular compromises.",
        "source": "FoH 112"
    },
    "disintegrate": {
        "name": "Disintegrate",
        "cost": "●(●)",
        "pool": "Strength + Brawl + Primum",
        "description": "Disintegrate an object.",
        "source": "DTD 163"
    },
    "echoing_death": {
        "name": "Echoing Death",
        "cost": "●●",
        "pool": "Strength + Brawl + Primum",
        "description": "Strike someone dead and, in so doing, undo their previous actions within the last few minutes.",
        "source": "DTD 163"
    },
    "ephemeral_cover": {
        "name": "Ephemeral Cover",
        "cost": "*",
        "pool": "Strength + Occult + Primum - Defense",
        "description": "Tear a ghost or spirit apart as raw materials to create an ephemeral Cover.",
        "source": "DTD 164"
    },
    "everybody_hates_him": {
        "name": "Everybody Hates Him",
        "cost": "*",
        "pool": "Intelligence + Intimidation + Primum",
        "description": "Render a person into an automatic scapegoat.",
        "source": "DTD 164"
    },
    "extispicy": {
        "name": "Extispicy",
        "cost": "*",
        "pool": "Intelligence + Occult + Primum",
        "description": "Read the future in butchered entrails.",
        "source": "DTD 165"
    },
    "eye_for_an_eye": {
        "name": "Eye for an Eye",
        "cost": "● (●/attack)",
        "pool": "Strength + Medicine + Primum - Damage",
        "description": "Take the wounds out of a target and transfuse them as a brawling or throwing attack.",
        "source": "Iface 97"
    },
    "force_relationship": {
        "name": "Force Relationship",
        "cost": "*",
        "pool": "Presence + Empathy + Primum",
        "description": "Fabricate relationships between people.",
        "source": "DTD 165"
    },
    "four_minutes_ago": {
        "name": "Four Minutes Ago",
        "cost": "●●",
        "pool": "Intelligence + Stealth + Primum",
        "description": "Retroactively leave the scene four minutes ago.",
        "source": "DTD 166"
    },
    "frozen_in_time": {
        "name": "Frozen in Time",
        "cost": "*",
        "pool": "Intelligence + Science + Primum - Stamina",
        "description": "Lock a target frozen in time.",
        "source": "DTD 166"
    },
    "halo": {
        "name": "Halo",
        "cost": "●●",
        "pool": "Presence + Medicine + Primum",
        "description": "Create a balming, healing, soporific light.",
        "source": "DTD 167"
    },
    "hellfire": {
        "name": "Hellfire",
        "cost": "*",
        "pool": "Presence + Firearms + Primum",
        "description": "Fire demonic supernatural flame out of a gun.",
        "source": "DTD 167"
    },
    "hellhounds": {
        "name": "Hellhounds",
        "cost": "●/Size",
        "pool": "Intelligence + Animal Ken + Primum",
        "description": "Twist an animal into a cryptid servant that needs Aether to survive longer than a scene.",
        "source": "DTD 167"
    },
    "incendiary": {
        "name": "Incendiary",
        "cost": "● (●/turn)",
        "pool": "Strength + Science + Primum",
        "description": "Throw fire. Literally throw it.",
        "source": "DTD 168"
    },
    "inflict_stigmata": {
        "name": "Inflict Stigmata",
        "cost": "*",
        "pool": "Presence + Occult + Primum",
        "description": "Transform a human into a stigmatic.",
        "source": "DTD 168"
    },
    "living_installation": {
        "name": "Living Installation",
        "cost": "●●",
        "pool": "Intelligence + Medicine + Primum",
        "description": "Install a gadget into a living being.",
        "source": "FoH 112"
    },
    "living_shadow": {
        "name": "Living Shadow",
        "cost": "*",
        "pool": "Intelligence + Stealth + Primum",
        "description": "Become a shadow travelling across surfaces and between hosts.",
        "source": "DTD 169"
    },
    "merge": {
        "name": "Merge",
        "cost": "●/demon",
        "pool": "Strength + Occult + Primum",
        "description": "Funnel demonic form abilities into one demon, who becomes an amalgam creature.",
        "source": "DTD 169"
    },
    "murder_by_improbability": {
        "name": "Murder by Improbability",
        "cost": "*",
        "pool": "Intelligence + Academics + Primum vs Presence + Tolerance",
        "description": "Induce catastrophic bad luck, spontaneously killing an ordinary human or cursing supernatural beings in combat.",
        "source": "DTD 170"
    },
    "newtons_nightmares": {
        "name": "Newton's Nightmares",
        "cost": "●●●",
        "pool": "Intelligence + Science + Primum",
        "description": "Amplify, reduce, or redirect the effects of gravity, friction or inertia.",
        "source": "FoH 112"
    },
    "open_and_shut_case": {
        "name": "Open-and-Shut Case",
        "cost": "*",
        "pool": "Presence + Investigation + Primum",
        "description": "Links a crime to a random scapegoat or a scapegoat to a random crime, temporarily railroading prosecution of the suspect.",
        "source": "FoH 114"
    },
    "play_on_words": {
        "name": "Play on Words",
        "cost": "●●",
        "pool": "Presence + Expression + Primum",
        "description": "Actualize a spoken word's double meaning.",
        "source": "DTD 170"
    },
    "possession": {
        "name": "Possession",
        "cost": "*",
        "pool": "Intelligence + Persuasion + Primum - Resolve",
        "description": "Possess a human being, occupying and controlling their body.",
        "source": "DTD 171"
    },
    "rain_of_blood": {
        "name": "Rain of Blood",
        "cost": "●●●",
        "pool": "Strength + Occult + Primum",
        "description": "Cause a plague of unnatural inclement weather, which may induce stigmatics.",
        "source": "DtD 172"
    },
    "raise_dead": {
        "name": "Raise Dead",
        "cost": "●/day",
        "pool": "Presence + Medicine + Primum",
        "description": "Resurrect a dead human whose soul has not been annihilated or moved on.",
        "source": "DTD 172"
    },
    "raze_infrastructure": {
        "name": "Raze Infrastructure",
        "cost": "*",
        "pool": "Presence + Streetwise + Primum",
        "description": "Destroy Infrastructure, in a very literal and messy way.",
        "source": "DTD 173"
    },
    "reality_enforcement": {
        "name": "Reality Enforcement",
        "cost": "●●●",
        "pool": "Presence + Academics + Primum",
        "description": "Disconnect beings related to the God-Machine from the occult principles that enable their supernatural powers.",
        "source": "DTD 173"
    },
    "riot": {
        "name": "Riot",
        "cost": "*",
        "pool": "Presence + Persuasion + Primum",
        "description": "Cause a spontaneous, aimless riot.",
        "source": "DTD 174"
    },
    "rip_the_gates": {
        "name": "Rip the Gates",
        "cost": "*",
        "pool": "Strength + Occult + Primum",
        "description": "Tear open a rift into or out of the Astral Realms, the Hedge, the Shadow or the Underworld.",
        "source": "DTD 174"
    },
    "sermon": {
        "name": "Sermon",
        "cost": "●/speech",
        "pool": "Presence + Persuasion + Primum",
        "description": "Dictate the morals and ethics of your audience and elicit their devotion.",
        "source": "DTD 175"
    },
    "show_of_power": {
        "name": "Show of Power",
        "cost": "*",
        "pool": "Presence + Occult + Primum vs Wits + Tolerance",
        "description": "Mimic a supernatural power that you have observed.",
        "source": "FoH 114"
    },
    "solitary_confinement": {
        "name": "Solitary Confinement",
        "cost": "*",
        "pool": "Strength + Occult + Primum - Resolve + Tolerance",
        "description": "Trap someone in a dimensional oubliette of total sensory deprivation.",
        "source": "DTD 176"
    },
    "soul_brand": {
        "name": "Soul Brand",
        "cost": "*",
        "pool": "Presence + Expression + Primum - Tolerance",
        "description": "Place a mark on a target's soul, visible through the aura. Those around the target subconsciously intuit they are under protection.",
        "source": "FoH 115"
    },
    "stalking_horse": {
        "name": "Stalking Horse",
        "cost": "*",
        "pool": "Presence + Expression + Primum vs Composure + Tolerance",
        "description": "Expose someone to others as exemplary of a trait, regardless of whether they actually exhibit it.",
        "source": "DTD 176"
    },
    "stimulus_response": {
        "name": "Stimulus/Response",
        "cost": "*",
        "pool": "Intelligence + Empathy + Primum vs Resolve + Tolerance",
        "description": "Induce a reflexive association between the demon's expenditure of Aether and an action the target has performed.",
        "source": "DTD 176"
    },
    "stop": {
        "name": "Stop",
        "cost": "●●",
        "pool": "Intelligence + Science + Primum",
        "description": "Stops time for a moment, creating a space where the demon can move and use Embeds, but nothing else can move or be harmed.",
        "source": "FoH 115"
    },
    "summon": {
        "name": "Summon",
        "cost": "●/day",
        "pool": "Presence + Streetwise + Primum",
        "description": "Initiate circumstances that will bring somebody you know to you.",
        "source": "DTD 177"
    },
    "swarm": {
        "name": "Swarm",
        "cost": "*",
        "pool": "Presence + Animal Ken + Primum",
        "description": "Conjure and command a swarm of creepy crawlies.",
        "source": "DTD 177"
    },
    "swift_resolution": {
        "name": "Swift Resolution",
        "cost": "●●●",
        "pool": "Intelligence + Academics + Primum",
        "description": "Instantly decide a conflict or sequence of events in favor of the most likely probability.",
        "source": "DTD 178"
    },
    "terrible_avatar": {
        "name": "Terrible Avatar",
        "cost": "*",
        "pool": "Strength + Occult + Primum",
        "description": "Split your demonic form off as an independent actor.",
        "source": "FoH 116"
    },
    "two_places_at_once": {
        "name": "Two Places at Once",
        "cost": "●●●",
        "pool": "Presence + Science + Primum",
        "description": "Entangle two separate areas that the demon has visited in the past day into a single disorienting space.",
        "source": "FoH 116"
    },
    "ultimatum": {
        "name": "Ultimatum",
        "cost": "●●",
        "pool": "Intelligence + Science + Primum vs Resolve",
        "description": "Task an individual with a single commandment, on pain of deadly transmutation.",
        "source": "FoH 116"
    },
    "urban_legend": {
        "name": "Urban Legend",
        "cost": "●/roll",
        "pool": "Intelligence + Expression + Primum",
        "description": "Actualizes the cast of an urban legend as flimsy actors who can be used as facades.",
        "source": "FoH 117"
    },
    "visions_of_heaven_and_hell": {
        "name": "Visions of Heaven and Hell",
        "cost": "●●",
        "pool": "Presence + Intimidation + Primum vs Resolve + Tolerance",
        "description": "Projects a dramatic vision of either divine judgment and triumph or agony and terror.",
        "source": "FoH 118"
    },
    "walls_of_jericho": {
        "name": "Walls of Jericho",
        "cost": "●●●",
        "pool": "Strength + Intimidation + Primum",
        "description": "Briefly strips the benefits of Defense, Armor and concealment from present foes.",
        "source": "FoH 119"
    },
    "the_word": {
        "name": "The Word",
        "cost": "*",
        "pool": "Presence + Intimidation + Primum - Resolve",
        "description": "Issue a short, simple command that is obeyed, even if it has nothing to do with voluntary actions.",
        "source": "DTD 179"
    }
}

# List of all Embed names
ALL_EMBED_NAMES = list(ALL_EMBEDS.keys())

# List of all Exploit names
ALL_EXPLOIT_NAMES = list(DEMON_EXPLOITS.keys())

