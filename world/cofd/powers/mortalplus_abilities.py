"""
Wolf-Blooded Tells and Psychic Abilities for Mortal+ Characters
Chronicles of Darkness 2nd Edition
"""

# Wolf-Blooded Tells (Inherited traits from werewolf ancestry)
WOLFBLOODED_TELLS = {
    "a_wolfs_meat": {
        "name": "A Wolf's Meat",
        "description": ("The Wolf-Blooded is vulnerable to silver. She suffers aggravated damage from silver just "
                       "as a werewolf does. Silver also blocks any regeneration just as it would to a werewolf. "
                       "Furthermore, she breaks out in itchy red rashes if she comes in physical contact with silver."),
        "boon": ("The Wolf-Blooded's meat is different, more like her stronger cousins. She regenerates just like "
                "a werewolf with Primal Urge 1. The Wolf-Blooded can spend a Willpower point to heal lethal damage."),
        "book": "Signs of the Moon"
    },
    "anger_issues": {
        "name": "Anger Issues",
        "description": ("Plenty of Wolf-Blooded have bad tempers. For this Wolf-Blooded, that temper isn't just a problem, "
                       "it's potentially deadly. This Wolf-Blooded has a specific Kuruth trigger. She can remain in Wasu-Im "
                       "for 15 minutes, but spends the same duration in Basu-Im."),
        "boon": ("The Wolf-Blooded takes Dalu form in both stages of Kuruth, and has all the benefits of that form, "
                "including heightened traits and regeneration."),
        "book": "Signs of the Moon"
    },
    "bite": {
        "name": "Bite",
        "description": ("The Wolf-Blooded has a thick jaw. When she's described, people use words like 'square' and 'brick' "
                       "and probably 'tough' even if she's otherwise not much of a brawler. She looks like she can take it "
                       "on the chin. Her teeth are remarkably white, strong, and sharp. Any attempt to be underestimated or "
                       "appear innocent are penalized. The Wolf-Blooded suffers a -3 penalty on any such roll."),
        "boon": ("Her teeth aren't just sharp, they're dangerously sharp. And by way of that unusual biology, she can "
                "distend her jaw and deliver a devastating bite to anything or anyone she can get her mouth around. Not "
                "only can she perform a bite attack without grappling, she deals +1 lethal damage when she succeeds."),
        "book": "Signs of the Moon"
    },
    "bitten": {
        "name": "Bitten",
        "description": ("Whether the cause or the result of being a Wolf-Blooded, a werewolf has bitten the character. The "
                       "events that lead up to the bite could have come up in a thousand ways, but in the end, it has left "
                       "the Wolf-Blooded with a terrible, unnatural scar at the site of the bite that's never quite healed "
                       "right. Werewolves and other creatures that can track by scent have a +3 bonus to follow her."),
        "boon": ("The blood that slowly leaks from the bite wound creates visions when tasted by anyone. The vision grants "
                "the character knowledge of where to find the body of the nearest and most recent victim of a werewolf attack "
                "in the area. If no one has died in the area, it will instead reveal living victims of attack."),
        "book": "Signs of the Moon"
    },
    "clever_fingers": {
        "name": "Clever Fingers",
        "description": ("There's something strange about the Wolf-Blood's hands. Her fingers are too long, her index finger "
                       "is longer than her middle, they are all the same length, or they are unusually jointed. Whatever the "
                       "manifestation, her hands twitch and move strangely. They flitter about when the Wolf-Blooded talks, "
                       "and fold in odd ways when the character can manage to keep them still."),
        "boon": ("Something about the way those fingers move, and the general postures and movement common to these Wolf-Blooded, "
                "make her naturally beneficial to have around during a ritual. The Wolf-Blooded can perform natural mudras. "
                "Rituals just go smoother when she's involved. When working a ritual, she uses the Advanced Action mechanic. "
                "This includes rituals she leads, and rituals where she supports another."),
        "book": "Signs of the Moon"
    },
    "devil_inside": {
        "name": "Devil Inside",
        "description": ("The Wolf-Blooded has an edge of evil about him. He isn't inherently demonic, satanic, or even evil, "
                       "but others perceive him that way. He may have strange birthmarks, a single eyebrow, or other classic "
                       "signs of demonic affiliation, but he's really just a Wolf-Blooded."),
        "boon": ("Just as Wolf-Blooded influenced the mythology that rose up around werewolves, the mythology that's risen up "
                "around werewolves has, on occasion, affected the Tells of Wolf-Blooded. In this case, in specific, exposure "
                "to prominent religious iconography when it's presented forcefully to or at the Wolf-Blooded causes him to "
                "shift into a Dalu form. He remains in Dalu until he leaves the scene, and enjoys the physical benefits granted. "
                "Brandishing crosses or even offering the Wolf-Blooded a religious pamphlet is enough."),
        "book": "Signs of the Moon"
    },
    "evil_eye": {
        "name": "Evil Eye",
        "description": ("One of the Wolf-Blooded's eyes is different -- it may be red, white, or pale blue, but it stands out "
                       "as not normal in the character's face. She can try to hide it or conceal it, but that's always awkward "
                       "with eyes."),
        "boon": ("Just like the legends say, the Evil Eye can produce something like a curse if the Wolf-Blooded stares at "
                "someone. Determine a specific action. Spend a point of Willpower and roll Manipulation + Occult. The victim "
                "can resist with Resolve + Primal Urge. If successful, the next time the victim engages in that action, it's "
                "automatically a dramatic failure, though the victim receives a Beat. Successive uses of the Evil Eye on a "
                "given character suffer a cumulative -1 penalty."),
        "book": "Signs of the Moon"
    },
    "exciting": {
        "name": "Exciting",
        "description": ("The Wolf-Blooded gives off a sort of invigorating scent when he sweats that is as compelling as it "
                       "addictive. The character is often physically attractive, but these two things are not necessarily "
                       "synonymous."),
        "boon": ("Once per scene, engaging with the Wolf-Blooded in any physically exhausting activity (so long as skin to "
                "skin touching happens between Wolf-Blooded and the other character) has a euphoric quality for both. This can "
                "be anything from willing sexual contact to a rough game of basketball. The moment that sweat is exchanged, "
                "both characters gain a point of Willpower. However, the scent and feeling is addictive. The next time the "
                "character who isn't the Wolf-Blooded can share the same experience, no matter how inconvenient it might be, "
                "they must, or lose a point of Willpower until the Wolf-Blooded again willingly engages in the activity."),
        "book": "Signs of the Moon"
    },
    "familiar": {
        "name": "Familiar",
        "description": ("The Wolf-Blooded is never alone for long. Be it a spirit or an animal, the Wolf-Blooded is always "
                       "followed by a familiar creature she did not invite into her life. Each time the familiar is hurt, "
                       "the Wolf-Blooded takes the first point of damage instead of the familiar."),
        "boon": ("The familiar is a smart example of its type, but doesn't exhibit unnatural intelligence. It is loyal to "
                "the Wolf-Blooded. If a spirit, the familiar is a Hursih. If an animal, it can be anything up to the size "
                "of a small dog. It's not hostile to the Wolf-Blooded, but doesn't always help her. When the Wolf-Blooded "
                "takes damage, the first point is instead dealt to the familiar — unless that would kill the creature."),
        "book": "Signs of the Moon"
    },
    "fuck_ugly": {
        "name": "Fuck Ugly",
        "description": ("The Wolf-Blooded's arms are too long. She's hairy, though the hair might be well groomed or "
                       "particularly soft, healthy, and silky. She's hunched and has an overbite. Her brow grows together. "
                       "She has fangs instead of teeth. The end result is, she's in no way attractive or appealing, and tends "
                       "to put people off if they only have a surface interaction with her. Any first impression roll made by "
                       "the character doesn't benefit from 10-again."),
        "boon": ("There is something tragic in the Wolf-Blooded's condition, and that point of sympathy can go a long way "
                "for the character if people look past the surface. As a result, any time after the first meeting, the "
                "Wolf-Blooded can spend a Willpower point to add another character's Empathy score to any social action "
                "against that character."),
        "book": "Signs of the Moon"
    },
    "horse": {
        "name": "Horse",
        "description": ("The Wolf-Blooded often hears the whispers of spirits, and can invite them to speak through her. If "
                       "she does so, she suffers from the spirit's ban either from dusk to dawn of that day, or dawn to dusk."),
        "boon": ("The Wolf-Blooded can invite spirits in Twilight to speak through her. Doing so is not possession, and does "
                "not give the spirit a chance to Fetter to her. She can also become Resonant or Open to a particular spirit. "
                "No roll is necessary, only a willingness on the part of the Wolf-Blooded and an interest on the part of the "
                "spirit."),
        "book": "Signs of the Moon"
    },
    "host_ache": {
        "name": "Host-Ache",
        "description": ("Sometimes, the Wolf-Blooded just aches. Her head hurts, her stomach throbs, or she experiences cramps. "
                       "Nose bleeds are common, as is spontaneous menstruation. There's nothing random about the aches and pains, "
                       "though -- they are in direct relation to the presence of Hosts. For some reason, the Wolf-Blooded is "
                       "unusually sensitive to the existence of the shartha, and her pain grows increasingly uncomfortable the "
                       "closer she gets to the alien presence."),
        "boon": ("The Wolf-Blooded needs no roll to sense Hosts. If a Host is within 10 miles, the ache begins and may confer "
                "a -2 to Composure rolls. Using the pain to 'track' the Host is possible, but requires Stamina + Survival rolls "
                "in place of the usual tracking rolls. Failed rolls can be turned into dramatic failures if the player wishes, "
                "in which case the Wolf-Blooded suffers actual damage in proportion to the strength of the Host she's tracking."),
        "book": "Signs of the Moon"
    },
    "liars_skin": {
        "name": "Liar's Skin",
        "description": ("Slashing the Wolf-Blooded's skin does not reveal tissue or bone, but thick fur. He'll still bleed, "
                       "but the blood will spill over matted wolf fur that smells strongly of the woods and fresh raw meat. "
                       "Anyone seeing the fur beneath the flesh suffers Lunacy as though seeing a werewolf's Urshul form."),
        "boon": "The additional layer of flesh gives the Wolf-Blooded 1/1 armor at all times.",
        "book": "Signs of the Moon"
    },
    "marker": {
        "name": "Marker",
        "description": ("There's something about the Wolf-Blooded's secretions that are unique to him. He leaves his mark, "
                       "literally, through sweat, tears, blood, or other bodily fluids. A sweaty handprint can leave an "
                       "impression on even human senses. Stronger secretions leave a stronger impression."),
        "boon": ("The Wolf-Blooded can 'mark' any area that she has access to via the Safe Place Merit. Anyone entering that "
                "area may make a Resolve + Composure roll as a reflexive action in order to enter the marked area. On a success, "
                "they become aware this area 'belongs' to the Wolf-Blooded; if they fail, they suffer the Demoralized condition. "
                "Furthermore, if the owner of a Safe Place Merit in the area fails to contest the 'mark' for a month, it causes "
                "them to temporarily lose one dot of the Safe Place Merit."),
        "book": "Signs of the Moon"
    },
    "moon_marked": {
        "name": "Moon Marked",
        "description": ("The Wolf-Blooded has a tattoo-like birthmark somewhere on his body that is visible only when a certain "
                       "moon-phase is in the sky. It's usually in a place that's hard to hide, or else the character feels very "
                       "uncomfortable covering the mark, and must spend a point of Willpower to hide it when the corresponding "
                       "moon is in the sky."),
        "boon": ("When the Mark is visible because it's corresponding moon is in the sky, the Wolf-Blooded can inflict that "
                "auspice's Hunter's Aspect on a victim."),
        "book": "Signs of the Moon"
    },
    "phantom_pack": {
        "name": "Phantom Pack",
        "description": ("The Wolf-Blooded belongs to a pack that exists only for her. A pack of phantom wolves, possibly spirits "
                       "or ghosts, lurk at her periphery at all times. They won't invade human space and so won't appear in her "
                       "classes or workplace, but they'll make their presence known with howls and glinting eyes through a window "
                       "even if she's inside."),
        "boon": ("A Wolf-Blooded with a Phantom Pack is never really alone. She gets a +2 to any rolls to resist fear, and she "
                "can purchase the Pack Dynamics Merit but does not suffer the drawbacks."),
        "book": "Signs of the Moon"
    },
    "piercing_eyes": {
        "name": "Piercing Eyes",
        "description": ("The characters eyes, literally, pierce the Twilight. She has unusually colored, uncommonly vibrant eyes "
                       "that catch the light in the way a wolf's might at night. They are difficult to conceal, and the shine "
                       "happens even if she's wearing contact lenses. She can see things that normal people think aren't there, "
                       "and can't stop seeing them."),
        "boon": ("Her eyes see through to the other side. She can perceive all manner of Twilight creatures. Ghosts, spirits, "
                "and angels are as clearly visible to her as other human beings are to everyone else. She cannot deactivate "
                "this ability."),
        "book": "Signs of the Moon"
    },
    "second_skin": {
        "name": "Second Skin",
        "description": ("The Wolf-Blooded was born with the pelt of a wolf. Not attached to her, but a living skin that rushed "
                       "from her mother at the same time as the Wolf-Blooded. It breathes, in a way, has a sort of heartbeat, "
                       "and is clearly alive. It doesn't think, but it does feel, and the Wolf-Blooded has a sense for its "
                       "feelings. They're connected on a deep level, and the Wolf-Blooded cares for the pelt. She will feed it "
                       "and keep it safe, and every week she must let it run. If she wears the pelt once a week, she's fine. If "
                       "seven days have passed and she has not run with her pelt, she must roll Resolve + Composure when in a "
                       "stressful situation, with a cumulative -1 to the roll for every week that's passed. If she fails, she "
                       "must flee the scene, running back to her pelt so she can let it loose."),
        "boon": ("When the Wolf-Blooded puts her sibling pelt on her bare skin, she transforms into Urhan form. She has all of "
                "the benefits of that form, including enhanced traits and regeneration like a werewolf. As long as she has her "
                "pelt, she can transform at any time."),
        "book": "Signs of the Moon"
    },
    "shape_shifted": {
        "name": "Shape-Shifted",
        "description": ("The full moon controls the Wolf-Blooded's body just like in the old myths. For the night before, of, "
                       "and following the full moon, at night, the Wolf-Blooded goes through a painful transformation and takes "
                       "an Urshul form. She can't resist the transformation. It simply happens at twilight, and ends at dawn."),
        "boon": ("While in Urshul, the Wolf-Blooded enjoys all the benefits of the form including enhanced traits and "
                "regeneration; she also causes Lunacy like a werewolf."),
        "book": "Signs of the Moon"
    },
    "shadow_twin": {
        "name": "Shadow Twin",
        "description": ("You should have been a twin, but your twin didn't make it to birth. Instead, she went to the Shadow "
                       "and grew up there. You have a deep connection."),
        "boon": ("At a locus, you and she may switch places, allowing you to Reach. Of course, she is your twin, with her own "
                "will and her own mind. She prefers her life in the Shadow, and she may not always be happy about the exchange."),
        "book": "Signs of the Moon"
    },
    "skinner": {
        "name": "Skinner",
        "description": ("The Wolf-Blooded's skin is unusually thin and pink and has a shine to it at all times. It almost looks "
                       "like the top layers of his dermis never grew in, or like he's been skinned. His skin weeps fluid even "
                       "when it's covered up by makeup or clothes."),
        "boon": ("The Wolf-Blooded's skin can accept the skin of others easily and readily. If the Wolf-Blooded has the skin of "
                "another human being of roughly the same height and weight, he can attach that skin to his own body and take on "
                "the appearance of the person to whom the skin once belonged. The false skin confers no supernatural ability to "
                "mimic the previous owner of the skin. This skin lasts as long as the Wolf-Blooded keeps it on, but falls apart "
                "when he takes it off."),
        "book": "Signs of the Moon"
    },
    "spirit_double": {
        "name": "Spirit Double",
        "description": ("When under stress, or frustration — or sometimes just at random — the Wolf-Blooded doesn't sleep. "
                       "Instead, her spirit leaves her body and runs around causing mischief and violence, as if her id were "
                       "in control. Her spirit runs wild any time the character falls asleep with half of her total Willpower "
                       "or less. In the morning, she's sore and achy, but often fulfilled. She wakes with only fuzzy memories "
                       "of what she's done the night before."),
        "boon": ("While the character is bodiless, she is driven by her Vice. She can interact with the world like a normal "
                "person, but is actually disembodied. Any physical damage to her doesn't hurt her, it simply discorporates her "
                "spirit, sending it back to her sleeping body. While in this state, fulfilling her Vice grants her two points "
                "of Willpower instead of one, and fulfilling her Virtue grants her nothing."),
        "book": "Signs of the Moon"
    },
    "strong_scent": {
        "name": "Strong Scent",
        "description": ("The Wolf-Blooded has a noticeable scent about her. It's unmistakable and unmistakably her. It's not a "
                       "bad smell, just a potent one that allows even the human nose to identify her by scent alone."),
        "boon": ("The Wolf-Blooded isn't the center of attention because of her healthy scent, but people are aware of her. As "
                "a result, any attempt to notice anything about her other than her scent and that her presence in the scene has "
                "a -2 modifier. She could be lying, stealing, or cheating, but no one is paying attention to that."),
        "book": "Signs of the Moon"
    },
    "third_nipple": {
        "name": "Third Nipple",
        "description": ("In the Dark Ages, they might have called it a witch's teat, while modern medicine would just call it "
                       "vestigial. The Wolf-Blooded has a third nipple somewhere on his chest. Sometimes, the nipple weeps milk "
                       "or blood. The Wolf-Blooded, like witches of old, can use his extra nipple to feed spirits, which might "
                       "have given rise to the image of a familiar in the old days."),
        "boon": "By spending a point of Willpower and suffering a point of bashing damage, he may leak a point of Essence.",
        "book": "Signs of the Moon"
    },
    "tongues": {
        "name": "Tongues",
        "description": ("Sometimes strange, profane, and alien words fall out of the Wolf-Blooded's mouth instead of the language "
                       "she's trying to speak. Anytime a character fails a roll that involves speaking or singing, he can turn it "
                       "into a dramatic failure. He takes a Beat and suffers the results of stumbling mutters accidentally said in "
                       "the language of the Shadow. To humans, it sounds horrific and impossible. To werewolves and spirits, it "
                       "seems impossible that a human mouth could form the words that the Wolf-Blooded just has."),
        "boon": "The Wolf-Blooded can force herself to speak in tongues. By spending a point of Willpower, she can speak in the First Tongue for the rest of the scene.",
        "book": "Signs of the Moon"
    },
    "waystone": {
        "name": "Waystone",
        "description": ("The Wolf-Blooded is a sort of vortex where the line between Flesh and Spirit is weak. Spirits and "
                       "creatures of flesh that seek the Twilight tend to be drawn to the Wolf-Blooded unconsciously."),
        "boon": ("The Wolf-Blooded is a one-dot locus for the purposes of spirits and others Reaching across to the opposite side. "
                "She can shut off the hole she creates by her existence, but doing so requires concentration and opens her up to "
                "possession by giving her the Open Condition."),
        "book": "Signs of the Moon"
    },
    "wolf_sign": {
        "name": "Wolf Sign",
        "description": ("It isn't the Wolf-Blood's doing, but whenever he stays in a place for too long, signs of wolves and wolf "
                       "activities appear over time. Tracks, scat, leaves, and dead rabbits appear any place he stays for more than "
                       "a few hours. Any naturalist looking at his apartment would think he's housing a pack of wolves, no matter "
                       "how impossible that might be."),
        "boon": ("Aside from causing the Wolf-Blooded to need to learn a great deal about cleaning mud out of carpets, he's "
                "impossible to track by scent. The wolves -- that don't exist -- have no consistent smell, but whatever they leave "
                "behind can baffle the scent of anyone trying to find the Wolf-Blooded specifically."),
        "book": "Signs of the Moon"
    }
}

# List of Tell names for easy access
ALL_TELLS = list(WOLFBLOODED_TELLS.keys())

# Psychic Merits (These are purchased as Merits, not bio fields)
PSYCHIC_MERITS = [
    "Aura Reading", "Automatic Writing", "Biokinesis", "Clairvoyance",
    "Medium", "Numbing Touch", "Psychokinesis", "Psychometry",
    "Telekinesis", "Telepathy", "Animal Possession", "Apportation",
    "Biomimicry", "Doppelganger", "Incite Ecosystem", "Invoke Spirit",
    "Mind Control", "Phantasmagoria", "Psychic Concealment", "Psychic Onslaught",
    "Psychic Poltergeist", "Psychokinetic Combat", "Psychokinetic Resistance",
    "Sojourner", "Tactical Telepathy", "Technopathy", "Telekinetic Evasion"
]


# Helper functions for Tell lookup
def get_tell(tell_key):
    """
    Get a specific Wolf-Blooded Tell by key.
    
    Args:
        tell_key (str): Tell key (e.g., 'piercing_eyes')
        
    Returns:
        dict: Tell data or None if not found
    """
    return WOLFBLOODED_TELLS.get(tell_key.lower().replace(" ", "_"))


def get_all_tells():
    """Get all Wolf-Blooded Tells."""
    return WOLFBLOODED_TELLS.copy()


def list_tell_names():
    """Get list of all Tell names for validation."""
    return [tell_data['name'] for tell_data in WOLFBLOODED_TELLS.values()]
