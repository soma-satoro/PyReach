from world.cofd.stat_types import Merit

# Minor Template (Mortal+) Merits
# These are templates linked to major supernaturals or independent quasi-supernatural humans
#
# IMPORTANT: The template type (Ghoul, Dhampir, Wolf-Blooded, etc.) is NOT a merit.
# It is set via the character's template_type field in the Mortal+ template system.
# See PyReach/world/cofd/templates/mortal_plus.py for valid template_type values.
#
# The merits in this file are SPECIFIC to each template type:
# - ghoul_merits are available when template_type="Ghoul"
# - dhampir_merits are available when template_type="Dhampir"
# - etc.
#
# General supernatural merits (like Aura Reading, Biokinesis, etc.) are available
# to ALL mortals and are included in the general_supernatural_merits list.

# GENERAL SUPERNATURAL MERITS (Available to All Mortals)
general_supernatural_merits = [
    Merit(
        name="Accursed Harbinger",
        min_value=3,
        max_value=3,
        description="When an undirected curse settles upon you, roll Resolve + Composure to serve as a carrier for the curse rather than suffering it yourself",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Animal Possession",
        min_value=2,
        max_value=4,
        description="Spend Willpower and roll Resolve + Animal Ken to enter a projecting trance and control a Bonded animal for a scene. With four dots, control any animal",
        merit_type="supernatural",
        prerequisite="animal_ken:3"
    ),
    Merit(
        name="Animal Speech",
        min_value=1,
        max_value=2,
        description="You can fluently understand the communication of a particular kind of animal. With two dots, they can understand your communication. +3 to relevant Animal Ken rolls",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Apportation",
        min_value=3,
        max_value=5,
        description="Spend Willpower and roll Resolve + Occult to teleport an object or being up to Size 2, or with five dots, Size 5, inflicting Structure or bashing damage from the strain",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Assertive Implement",
        min_value=1,
        max_value=4,
        description="You possess a living weapon with its own will. Apply your dots in Assertive Implement as a bonus or penalty to wield it, as befits its whims. It regenerates Structure damage and can attack on its own given the opportunity",
        merit_type="supernatural",
        prerequisite="manipulation:3,occult:3,[weaponry:2,firearms:2]"
    ),
    Merit(
        name="Biomimicry",
        min_value=1,
        max_value=4,
        description="Spend Willpower and suffer lethal damage to mutate natural weaponry, propulsive venom, heavy 2/1 Armor, or camouflage pigmentation for a scene",
        merit_type="supernatural",
        prerequisite="biokinesis:1"
    ),
    Merit(
        name="Bless Amulet",
        min_value=1,
        max_value=3,
        description="Spend Willpower and roll Resolve + Composure with abjuration modifiers to ritually imbue a charm with protection against ephemeral possession and Claiming, for a duration determined by Merit rating",
        merit_type="supernatural",
        prerequisite="occult:3"
    ),
    Merit(
        name="Camera Obscura",
        min_value=3,
        max_value=3,
        description="Spend Willpower to focus a camera and perceive entities felt through the Unseen Sense, Opening their influence for a scene. While focused, roll Wits + Expression - Defense to inflict photographic bashing damage",
        merit_type="supernatural",
        prerequisite="[unseen_sense_ghosts:1,unseen_sense_spirits:1]"
    ),
    Merit(
        name="Citywalker",
        min_value=3,
        max_value=3,
        description="You can roll Resolve + Streetwise to walk occult correspondences from city to city, with penalties proportional to how unfamiliar your destination is to you",
        merit_type="supernatural",
        prerequisite="streetwise:2"
    ),
    Merit(
        name="Consecrate Weapon",
        min_value=4,
        max_value=4,
        description="Spend Willpower and roll Resolve + Composure - weapon rating with abjuration modifiers to ritually bless a weapon. It deals lethal damage to ephemeral entities, even in Twilight, for one turn per success",
        merit_type="supernatural",
        prerequisite="resolve:3,occult:4"
    ),
    Merit(
        name="Curse Effigy",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Wits + Occult - Resolve to spend a night crafting a sympathetic effigy of a victim. Spend rolled successes to inflict harmful Personal Tilts, distract and harry the victim, or make lethal attacks with Intelligence + Medicine - Stamina + Tolerance",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Dark Passenger",
        min_value=2,
        max_value=2,
        description="You have a sinister second mouth on the back of your head. It whispers secrets in threes, one of which is a lie, warns you of ambushes, and insists on being fed hourly",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Doppelganger",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Manipulation + Subterfuge to copy a subject down to the flesh, penalizing attempts to distinguish you by Biokinesis for a scene per success",
        merit_type="supernatural",
        prerequisite="subterfuge:3,biokinesis:1"
    ),
    Merit(
        name="Evil Eye",
        min_value=2,
        max_value=2,
        description="Sacrifice Defense to paralyze with your gaze, contesting Wits + Occult vs Resolve + Composure",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Hardened Exorcist",
        min_value=1,
        max_value=1,
        description="Add your Occult to your effective Integrity for abjuration modifiers, and ignore Vice penalties",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Hidden Variable",
        min_value=2,
        max_value=2,
        description="Around infrastructure, take a bonus die to attacks. Ignore 2 Durability or Armor when attacking infrastructure",
        merit_type="supernatural",
        prerequisite="unseen_sense_god_machine:1"
    ),
    Merit(
        name="Incite Ecosystem",
        min_value=1,
        max_value=5,
        description="Spend Willpower and roll Presence + Animal Ken to mark a subject as a threat to an animal or swarm per success. Commanding animals of Size greater than your dots in this Merit inflicts penalties",
        merit_type="supernatural",
        prerequisite="animal_ken:3"
    ),
    Merit(
        name="Invoke Spirit",
        min_value=2,
        max_value=2,
        description="A trauma has attracted a Rank 1 spirit riding you, protecting you but Urging you to recapitulate the trauma",
        merit_type="supernatural",
        prerequisite="resolve:3,medium:1"
    ),
    Merit(
        name="Potent Psyche",
        min_value=1,
        max_value=5,
        description="You can spend Willpower equal to dots in this Merit to take your Integrity as armor against a supernatural attack or influence for a turn",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Soul Jar",
        min_value=4,
        max_value=4,
        description="Spend Willpower and roll Resolve + Occult to ritually preserve your soul in a vessel. While in the jar, you're immune to death but your body becomes catatonic. Breaking the jar kills you instantly",
        merit_type="supernatural",
        prerequisite="occult:3"
    ),
    Merit(
        name="Sojourner",
        min_value=3,
        max_value=3,
        description="You can survive in the Shadow or Underworld for extended periods. Roll Stamina + Survival to resist environmental damage from these realms",
        merit_type="supernatural",
        prerequisite=""
    ),
    Merit(
        name="Spirit Familiar",
        min_value=3,
        max_value=3,
        description="You have bonded with a spirit familiar that can assist you. The spirit has Rank 1 and can manifest in Twilight near you",
        merit_type="supernatural",
        prerequisite="medium:1"
    ),
    Merit(
        name="Psychic Resistance",
        min_value=2,
        max_value=2,
        description="Add +2 to Resolve or Composure to resist psychic powers",
        merit_type="supernatural",
        prerequisite="resolve:3"
    ),
]

# RITUAL SORCERY MERITS (Available to Mortals who learn magic)
ritual_sorcery_merits = [
    Merit(
        name="Ritual Sorcerer",
        min_value=3,
        max_value=3,
        description="You have learned how to perform sorcerous rites. For each dot of Resolve, you may learn one Closed Rite or master one Open Rite",
        merit_type="supernatural",
        prerequisite="mental_attribute:3,occult:3,occult_specialty:1"
    ),
    Merit(
        name="Forbidden Rites",
        min_value=1,
        max_value=5,
        description="You can attempt an additional Closed Rite for each dot of this Merit at extreme ritual costs and a -2 penalty",
        merit_type="supernatural",
        prerequisite="ritual_sorcerer:1,library_occult:2,sorcerous_knowledge:1"
    ),
    Merit(
        name="Sorcerous Knowledge",
        min_value=1,
        max_value=5,
        description="For each dot, you may learn or create one Closed Rite or master one Open Rite",
        merit_type="supernatural",
        prerequisite="ritual_sorcerer:1,occult:1"
    ),
    Merit(
        name="Sorcerous Prodigy",
        min_value=3,
        max_value=3,
        description="Dots of Resolve or Sorcerous Knowledge used to master Open Rites each master a second Open Rite",
        merit_type="supernatural",
        prerequisite="ritual_sorcerer:1,sorcerous_knowledge:2"
    ),
]

# VAMPIRE-LINKED: Ghouls & Dhampir
# Note: Template type is set via template_type field, not as a merit
# These merits are available when template_type="Ghoul"

ghoul_merits = [
    Merit(
        name="Vital Resilience",
        min_value=1,
        max_value=5,
        description="You may spend Vitae to add this Merit to your effective Stamina to resist sickness or poison for a scene",
        merit_type="physical",
        prerequisite="template_type:ghoul"
    ),
    Merit(
        name="Vital Strength",
        min_value=1,
        max_value=5,
        description="You may spend Vitae to add this Merit to your effective Strength for a scene",
        merit_type="physical",
        prerequisite="template_type:ghoul"
    ),
    Merit(
        name="Vital Swiftness",
        min_value=1,
        max_value=5,
        description="You may spend Vitae to add this Merit to your effective Dexterity for a scene",
        merit_type="physical",
        prerequisite="template_type:ghoul"
    ),
    Merit(
        name="Vital Tenacity",
        min_value=1,
        max_value=5,
        description="You may spend Vitae to add this Merit to your effective Wits for a scene",
        merit_type="mental",
        prerequisite="template_type:ghoul"
    ),
]

# Template type is set via template_type field
# These merits are available when template_type="Dhampir"

dhampir_merits = [
    Merit(
        name="Blood Affinity",
        min_value=1,
        max_value=1,
        description="Once per scene, spend Willpower and roll Composure + Resolve to sense the presence of vampires",
        merit_type="supernatural",
        prerequisite="template_type:dhampir"
    ),
    Merit(
        name="Blood Drain",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Strength + Resolve to bite and drain blood from a victim. You cannot sustain yourself on blood alone",
        merit_type="supernatural",
        prerequisite="template_type:dhampir"
    ),
    Merit(
        name="Daywalker",
        min_value=2,
        max_value=2,
        description="You suffer no penalties from sunlight and are immune to effects that specifically target vampires due to their undead nature",
        merit_type="supernatural",
        prerequisite="template_type:dhampir"
    ),
    Merit(
        name="Half-Damned",
        min_value=1,
        max_value=5,
        description="You have a limited pool of Vitae equal to your dots in this Merit. You may spend it to fuel certain vampire powers or to heal as vampires do",
        merit_type="supernatural",
        prerequisite="template_type:dhampir"
    ),
    Merit(
        name="Predatory Aspect",
        min_value=2,
        max_value=2,
        description="You can project a lesser version of the predatory aura. Roll Presence + Intimidation to inflict the Shaken Condition on mortals",
        merit_type="social",
        prerequisite="template_type:dhampir"
    ),
]

# WEREWOLF-LINKED: Wolf-Blooded
# Template type is set via template_type="Wolf-blooded"
# Wolf-Blooded have werewolf heritage and access to Tells

wolf_blooded_merits = [
    # Moon Birth Merits (based on lunar phase at birth)
    Merit(
        name="Crescent Moon's Birth",
        min_value=2,
        max_value=2,
        description="Grant +3 Durability and +3 Structure when you help craft a fetish",
        merit_type="supernatural",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Full Moon's Birth",
        min_value=2,
        max_value=2,
        description="Once per scene, you can spend Willpower to lead a coordinated action, granting +3 dice and 8-Again to participants up to your Presence",
        merit_type="social",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Gibbous Moon's Birth",
        min_value=2,
        max_value=2,
        description="Take 8-Again and perform extended actions twice as fast when rolling a chosen Mental Skill",
        merit_type="mental",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Half Moon's Birth",
        min_value=2,
        max_value=2,
        description="Take +2 when rolling a breaking point in your territory. Once per session, you can take 8-Again and bonus dice equal to your Safe Place on one roll",
        merit_type="social",
        prerequisite="template_type:wolf-blooded,safe_place:1"
    ),
    Merit(
        name="No Moon's Birth",
        min_value=2,
        max_value=2,
        description="When you scout on instructions from a pack leader or parental figure, you leave no scent, cannot be followed home, and your point of origin or allegiance can't be ascertained",
        merit_type="supernatural",
        prerequisite="template_type:wolf-blooded"
    ),
    # Firstborn Blood Merits (Heritage from specific Firstborn)
    Merit(
        name="Fenris-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Take 8-Again to craft or wield silver weapons",
        merit_type="physical",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Hikaon-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Ignore total darkness penalties. When denied a sense, take +2 to compensate with other senses",
        merit_type="physical",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Kamduis-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Roll Intelligence + Occult to create a mark that can trap a ghost for an hour per success",
        merit_type="supernatural",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Sagrim-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Take 8-Again and add Safe Place as bonus dice to roll Crafts or Computer to set up security measures",
        merit_type="mental",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Skolis-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Immunity to Urging, and to being supernaturally forced to appear weak or defeated",
        merit_type="supernatural",
        prerequisite="template_type:wolf-blooded"
    ),
    # Pack and General Merits
    Merit(
        name="Pack Bond",
        min_value=1,
        max_value=3,
        description="You're respected as an important member of the pack. You can buy one dot of Totem, or up to five dots with Pack Bond •••",
        merit_type="social",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Raised by Wolves",
        min_value=1,
        max_value=1,
        description="You grew up among werewolves. Ignore Resistance rolls to withstand the bizarre or grotesque things you see",
        merit_type="mental",
        prerequisite="template_type:wolf-blooded"
    ),
    Merit(
        name="Tell",
        min_value=3,
        max_value=3,
        description="You have a Wolf-Blooded Tell - a supernatural ability that marks you as touched by the spirit world. Wolf-Blooded inherit these from werewolf ancestry, but any mortal can manifest a Tell through prolonged exposure to werewolves or spiritual transformation. This merit can be taken multiple times with different Tells. Use instance notation: Tell:Piercing Eyes, Tell:Shape Shifted, Tell:Second Skin, etc. Each instance costs 3 dots. See +lookup tells for all available Wolf-Blooded Tells and their effects",
        merit_type="supernatural",
        prerequisite=""
    ),
]

# MAGE-LINKED: Proximi & Alchemists
# Template type is set via template_type="Proximus"
# Proximi get access to limited magical abilities based on their family bloodline

proximi_merits = [
    Merit(
        name="Proximi Bloodline",
        min_value=1,
        max_value=1,
        description="You belong to a specific Proximi family with unique magical traditions. Your family determines which Blessing you can access",
        merit_type="supernatural",
        prerequisite="template_type:proximus"
    ),
]

# CHANGELING-LINKED: Fae-Touched
# Template type is set via template_type="Fae-Touched"

fae_touched_merits = [
    Merit(
        name="Broken Mirror",
        min_value=2,
        max_value=2,
        description="You can spend Glamour to swap places with your reflection in a mirror",
        merit_type="supernatural",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Dreamer's Gaze",
        min_value=1,
        max_value=1,
        description="Stare down and contest Presence + Composure vs Resolve + Composure to enter the Bastion of someone you share a pledge with. May inflict Clarity damage",
        merit_type="supernatural",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Favored Promise",
        min_value=1,
        max_value=3,
        description="Apply as bonus dice to uphold a particular type of promise (Clemency, Debt, Love, Loyalty, Protection, Provision, or Service)",
        merit_type="social",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Find the Oathbreaker",
        min_value=2,
        max_value=2,
        description="Spend Glamour and roll Wits + Wyrd to track down someone who has violated a pledge",
        merit_type="supernatural",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Keeper of the Bargain",
        min_value=3,
        max_value=3,
        description="Willpower spent to contest attempts to sway you to break a sealing or oath adds four dice instead of three and reduces the exceptional threshold from five to three",
        merit_type="supernatural",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Promise of Clemency",
        min_value=1,
        max_value=3,
        description="You swore to forgive a particular wrong or crime. Apply as bonus dice to resist emotional influence based on that wrong",
        merit_type="social",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Promise of Debt",
        min_value=1,
        max_value=3,
        description="You swore to repay a debt you owed someone. Apply as bonus dice to help settle a debt",
        merit_type="social",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Promise of Love",
        min_value=1,
        max_value=3,
        description="You swore unending love. Apply as bonus dice to contest attempts to manipulate your feelings about another",
        merit_type="social",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Promise of Loyalty",
        min_value=3,
        max_value=3,
        description="You swore to stand by another's side. Remove a Door when Social Maneuvering through your relationship or shared history with another",
        merit_type="social",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Promise of Protection",
        min_value=1,
        max_value=5,
        description="You swore to keep someone safe. When fighting to protect someone, apply as an Initiative bonus, and reduce the Defense penalty from multiple attacks by one",
        merit_type="social",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Promise to Provide",
        min_value=3,
        max_value=3,
        description="You swore someone would always have a home with you. Spend Glamour when offering your hospitality. A guest who accepts must spend Willpower to betray that hospitality, but recovers Willpower if they don't",
        merit_type="social",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Promise to Serve",
        min_value=1,
        max_value=3,
        description="You swore a service in someone's stead. Apply as bonus teamwork successes",
        merit_type="social",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Punish the Oathbreaker",
        min_value=2,
        max_value=2,
        description="Exercise Loopholes to use your Contracts against a found oathbreaker alone",
        merit_type="supernatural",
        prerequisite="template_type:fae-touched,find_the_oathbreaker:1"
    ),
    Merit(
        name="Sense Vows",
        min_value=1,
        max_value=1,
        description="Spend Glamour to sense whether a character was pledgebound within the current story",
        merit_type="supernatural",
        prerequisite="template_type:fae-touched"
    ),
    Merit(
        name="Twice Shy",
        min_value=3,
        max_value=3,
        description="Can use Dreamer's Gaze on the promise-bound Changeling's fetch",
        merit_type="supernatural",
        prerequisite="template_type:fae-touched,dreamers_gaze:1"
    ),
]

# GEIST-LINKED: Ghosts
# Template type is set via template_type="Ghost"
# specific merits from Geist 2e

ghost_merits = [
    Merit(
        name="Brain Eater",
        min_value=1,
        max_value=1,
        description="Touch human corpses from Twilight. Eat organs for Memories left behind by death",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Dead Meat",
        min_value=1,
        max_value=1,
        description="Inhabit your dead body, substituting Health for Corpus. Healing non-bashing Health damage and resisting the degredation of your body requires raw meat by the pound. You must spend Willpower to gain people's attention nonviolently",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Deep Memory",
        min_value=1,
        max_value=1,
        description="Add your Resistance to your maximum stock of Memories before suffering Memory Bleed",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Wake",
        min_value=1,
        max_value=5,
        description="The living still mourn you enough to provide a point of Essence each chapter for each dot of Wake",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    # Iconography Merits: A ghost can only have ONE of these
    Merit(
        name="Ajna",
        min_value=1,
        max_value=1,
        description="You manifest a perceptive eye where an eye should not be. Gain a +3 Perception bonus, but double any penalties from sensory overload",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Banda",
        min_value=1,
        max_value=1,
        description="You have the uncanny sway of the ghede. Gain a +3 bonus to benefit from stealing the spotlight, but suffer a -2 Stealth penalty",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Crowned",
        min_value=1,
        max_value=1,
        description="You are surmounted by a glory of spectral light. When those around you roll to resist breaking points or crisis points, they gain a bonus die, but you lose Essence",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Immaculate Heart",
        min_value=1,
        max_value=1,
        description="Your ribcage is open, exposing a still-beating heart. Gain a +3 bonus to earn trust, but suffer -2 to guard your feelings",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Pierced",
        min_value=1,
        max_value=1,
        description="You remain forever impaled by weapons or openly wounded. The first time you take damage in a scene, you ignore it, but you also suffer a permanent -1 wound penalty",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Shackled",
        min_value=1,
        max_value=1,
        description="Chains or bindings weigh you down and suggest pain. You can recover two Essence from the presence of an Anchor once per chapter, but your Speed is permanently halved",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Veined",
        min_value=1,
        max_value=1,
        description="Veins pulse visibly through your Corpus and beyond. Spend Essence like a ghost of one Rank higher, but the first time in a scene you suffer damage, suffer an additional point",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
    Merit(
        name="Waters",
        min_value=1,
        max_value=1,
        description="Water always pours and drips from you. Spend Essence to adopt a pool of water as an Anchor for a scene, and while submerged in that pool, nothing can coerce you to leave it",
        merit_type="supernatural",
        prerequisite="template_type:ghost"
    ),
]

# MUMMY-LINKED: Immortals & Witnesses
# Template type is set via template_type="Immortal"
# Various immortality types: blood bather, body thief, spirit immortal, etc.

immortal_merits = [
    Merit(
        name="Dead Celebrity",
        min_value=1,
        max_value=3,
        description="You possessed Fame in a previous era. Apply as a Social bonus to appeal to your 'resemblance' to your famed self",
        merit_type="social",
        prerequisite="template_type:immortal"
    ),
    Merit(
        name="Endless Potency",
        min_value=1,
        max_value=5,
        description="Choose an Attribute. You may spend Sekhem, Pillars, or for your immortality's favored Attribute, Willpower to channel Endless Potency as bonus Attribute dots for one scene",
        merit_type="supernatural",
        prerequisite="template_type:immortal"
    ),
    Merit(
        name="Enigma",
        min_value=1,
        max_value=5,
        description="Fate conspires to erase evidence of your life left behind. Investigation takes a -2 penalty and requires an additional clue for each dot of Enigma",
        merit_type="supernatural",
        prerequisite="template_type:immortal,fame:0"
    ),
    Merit(
        name="Fount of Vitality",
        min_value=4,
        max_value=4,
        description="Recover from wounds like the Arisen rather than like mortals",
        merit_type="supernatural",
        prerequisite="template_type:immortal,[sekhem:3,invested:1]"
    ),
    Merit(
        name="Grave Robber",
        min_value=5,
        max_value=5,
        description="Disturb the tombs of the Arisen without waking them. Stealing an entombed relic wakes the mummy after two hours and taints their investigation to track the relic down",
        merit_type="supernatural",
        prerequisite="template_type:immortal"
    ),
    Merit(
        name="Lineal Inheritor",
        min_value=3,
        max_value=3,
        description="One of your parents passed away while invested with the Pillar of a mummy's soul. You now benefit from investment, and the mummy must perform the Rite of Investment on you to withdraw it",
        merit_type="supernatural",
        prerequisite="template_type:immortal"
    ),
    Merit(
        name="Relic Sensitivity",
        min_value=2,
        max_value=2,
        description="Sense vessels of Sekhem through kepher",
        merit_type="supernatural",
        prerequisite="template_type:immortal"
    ),
    Merit(
        name="Resplendent Soul",
        min_value=3,
        max_value=3,
        description="Gain one permanent Pillar dot. Its point may be replenished from vestiges or meditation, substituting Composure for Memory",
        merit_type="supernatural",
        prerequisite="template_type:immortal,sekhem:2"
    ),
    Merit(
        name="Supernatural Resistance",
        min_value=1,
        max_value=5,
        description="Add this Merit's rating to your Supernatural Tolerance",
        merit_type="supernatural",
        prerequisite="template_type:immortal"
    ),
    Merit(
        name="Tenacious Eternity",
        min_value=4,
        max_value=4,
        description="You may make a substitution in either the Bath, Blood, or Preparation of your bathing ritual. Spend Willpower to permanently alter your ritual",
        merit_type="supernatural",
        prerequisite="template_type:immortal,blood_bather:1"
    ),
    # Note: Witness merits are in mummy_merits.py
]

# WEREWOLF-LINKED: Hosts (Spirit-Ridden)
# Template type is set via template_type="Host"
# CLARIFICATION: Hosts are spirit-possessed mortals, linked to Werewolf (not Demon)
# Different from Stigmatics (God-Machine marked) or Demon-Blooded

host_merits = [
    # NOTE: Specific merits from Werewolf: The Forsaken 2nd Edition
    # Hosts are mortals who share their body with spirits (Ridden/Claimed)
    # They have symbiotic relationships with their spirit passengers
    # Common host abilities:
    # - Spirit Powers: Access to spirit Numina
    # - Enhanced Attributes: Spirit-boosted capabilities
    # - Shared Senses: Perceive through spirit senses
    # - Spirit Communication: Direct link to spirit world
    # Source: WTF 2e Chapter on Hosts/Spirit-Claimed
    # To be added from source material
]

# Template type is set via template_type="Demon-Blooded"
# Demon-Blooded can be offspring or fractals

demon_blooded_merits = [
    Merit(
        name="Ambient Aether",
        min_value=1,
        max_value=2,
        description="You can gather and spend Aether. Fractals buy for one dot, offspring two",
        merit_type="supernatural",
        prerequisite="template_type:demon_blooded"
    ),
    Merit(
        name="Aether Pool",
        min_value=2,
        max_value=2,
        description="Gain a five-point Aether pool",
        merit_type="supernatural",
        prerequisite="template_type:demon_blooded,ambient_aether:1"
    ),
    Merit(
        name="Eidetic Memory",
        min_value=1,
        max_value=1,
        description="As the general Merit, at reduced cost for demon-blooded",
        merit_type="mental",
        prerequisite="template_type:demon_blooded"
    ),
    Merit(
        name="Infrastructure Proficiency",
        min_value=2,
        max_value=3,
        description="Find your way through infrastructure, intuit how it works, and identify linchpins. Costs two dots for fractals or three for others",
        merit_type="mental",
        prerequisite="template_type:demon_blooded"
    ),
    Merit(
        name="Instinctive Deflection",
        min_value=2,
        max_value=2,
        description="Roll Wits + Resolve to avoid compromise",
        merit_type="supernatural",
        prerequisite="template_type:demon_blooded"
    ),
    Merit(
        name="Quantum Understanding",
        min_value=3,
        max_value=3,
        description="Contest Wits + Composure vs Tolerance to read a demon's Liar's Tongue",
        merit_type="supernatural",
        prerequisite="template_type:demon_blooded"
    ),
    Merit(
        name="Unknown",
        min_value=1,
        max_value=1,
        description="Begin play without a Cipher Condition, but with only one Embed and no Interlocks. Character creation only",
        merit_type="supernatural",
        prerequisite="template_type:demon_blooded"
    ),
    # Nephilim Merits (specific type of demon-blooded)
    Merit(
        name="Unseen Sense (Angels)",
        min_value=2,
        max_value=2,
        description="As a stigmatic's Unseen Sense, and you may roll Wits + Occult to sense the presence of Aether sources, including angels and demons",
        merit_type="supernatural",
        prerequisite="template_type:demon_blooded"
    ),
    Merit(
        name="Voice of Hell",
        min_value=2,
        max_value=2,
        description="Spend Aether for fluency in a language for one scene",
        merit_type="supernatural",
        prerequisite="template_type:demon_blooded"
    ),
]

# Template type is set via template_type="Stigmatic"
# Stigmatics bear God-Machine marks

stigmatic_merits = [
    Merit(
        name="Potent Blood",
        min_value=1,
        max_value=1,
        description="Bleed a point of lethal damage every other day. Consecrating with the blood confers +2 to a supernatural action, and demons recover a point of Aether by ingesting it. Vampires who feed from you temporarily gain the effects of Unseen Sense (God-Machine)",
        merit_type="supernatural",
        prerequisite="template_type:stigmatic"
    ),
    Merit(
        name="Sleeve Integrator",
        min_value=1,
        max_value=5,
        description="Spend Willpower to merge with a demon, allowing her to use your life as a Cover for up to a day, with a rating equal to your Integrity. Afterwards, you gain access to one of the demon's Embeds per dot in this Merit",
        merit_type="supernatural",
        prerequisite="template_type:stigmatic,integrity:5"
    ),
    Merit(
        name="Sympathetic Demon",
        min_value=2,
        max_value=2,
        description="You have a demon friend. Once per session, you can declare the demon's convenient arrival. You suffer any damage the demon suffers",
        merit_type="social",
        prerequisite="template_type:stigmatic"
    ),
    Merit(
        name="Pact Sense",
        min_value=3,
        max_value=3,
        description="You can sense the aspects of reality stitched together by demonic pacts",
        merit_type="supernatural",
        prerequisite="template_type:stigmatic"
    ),
]

# INDEPENDENT MORTAL+ TEMPLATES
# These are not linked to specific major templates
# Template type determines which merit lists are available

# Template type is set via template_type="Atariya"
# Exceptionally lucky mortals
atariya_merits = [
    Merit(
        name="Damn Lucky",
        min_value=1,
        max_value=4,
        description="Spend Willpower to prevent harm, up to your Damn Lucky rating in lethal damage or twice your rating in bashing per scene. You may choose to inflict the averted misfortune on another within the scene",
        merit_type="supernatural",
        prerequisite="template_type:atariya"
    ),
    Merit(
        name="All-In",
        min_value=3,
        max_value=3,
        description="Spend Willpower to reduce an action's dice pool to a special 8-Again chance die. On success, add half the removed dice as bonus successes",
        merit_type="supernatural",
        prerequisite="template_type:atariya,damn_lucky:1,resolve:3"
    ),
    Merit(
        name="Count Down",
        min_value=1,
        max_value=1,
        description="Your character has knowledge of their ability to cheat death and how many uses remain, but living with that knowledge inflicts a Persistent Condition",
        merit_type="supernatural",
        prerequisite="template_type:atariya,damn_lucky:1,nine_lives:1"
    ),
    Merit(
        name="Easy Come, Easy Go",
        min_value=1,
        max_value=1,
        description="Unlikely circumstances permit you to exchange up to five Merit dots per session",
        merit_type="supernatural",
        prerequisite="template_type:atariya,damn_lucky:1"
    ),
    Merit(
        name="Luck Flows Up",
        min_value=2,
        max_value=2,
        description="As the Thief of Fate Merit, at reduced cost",
        merit_type="supernatural",
        prerequisite="template_type:atariya,damn_lucky:1"
    ),
    Merit(
        name="Mr. Lucky",
        min_value=1,
        max_value=1,
        description="You notice a smiling apparition present when danger is looming. Ignore perception penalties to notice ambushes, and a successful such roll is always exceptional",
        merit_type="supernatural",
        prerequisite="template_type:atariya,damn_lucky:1"
    ),
    Merit(
        name="Nine Lives",
        min_value=1,
        max_value=5,
        description="Character creation only. Redeem a dot of this Merit to cheat death",
        merit_type="supernatural",
        prerequisite="template_type:atariya,damn_lucky:1"
    ),
    Merit(
        name="See the Flow",
        min_value=1,
        max_value=5,
        description="Gain a sense for the odds in or against a character's favor in an endeavor. Spend Willpower to nudge toward or away from those odds with dice modifiers, up to your See the Flow rating in dice per scene",
        merit_type="supernatural",
        prerequisite="template_type:atariya,damn_lucky:1"
    ),
]

# Template type is set via template_type="Dreamer"
# Sleeper agents with subliminal training - use Memory resource
dreamer_merits = [
    # Style Merits
    Merit(
        name="Subliminal Conditioning",
        min_value=1,
        max_value=5,
        description="(•) Basic Control: Store temporary Memory when facing breaking point, up to Resolve. Spend Memory to ignore penalties to harm another. Suffer Missing Time when out of Memory. (••) Extended Awareness: Spend Memory for rote quality on perception roll. (•••) Steady on Target: Spend Memory to prevent collateral damage. (••••) Between the Lines: Store extra Memory on successful breaking point roll. (•••••) New Parameters: Spend Memory to trigger Missing Time with designated target. Dispatch mortal through Down and Dirty Combat",
        merit_type="style",
        prerequisite="template_type:dreamer"
    ),
    Merit(
        name="Field Handler",
        min_value=1,
        max_value=5,
        description="(•) Pencil Pusher: Handler provides Field Handler rating as auxiliary Contacts or Resources once a story. (••) Clock Watcher: Handler provides Mentor or Ally once a story. (•••) Company Man: Handler calls on supernatural influences to remove threats once a story. (••••) Bought Out: Use dirt on handler to call on aid a second time each story. (•••••) Friend Inside: Handler sympathetic to your troubles, will intervene to protect you even at cost of mission once per story",
        merit_type="style",
        prerequisite="template_type:dreamer"
    ),
    # Regular Merits
    Merit(
        name="Déjà Vu",
        min_value=1,
        max_value=3,
        description="Recover Memory when you experience a Physical Condition or Tilt. With two dots, recover Memory from dramatic failure. With three dots, recover Memory from lethal damage",
        merit_type="supernatural",
        prerequisite="template_type:dreamer"
    ),
    Merit(
        name="Memory Palace",
        min_value=1,
        max_value=5,
        description="Increase your maximum Memory storage by your Memory Palace rating",
        merit_type="mental",
        prerequisite="template_type:dreamer"
    ),
    Merit(
        name="Mephistopheles",
        min_value=2,
        max_value=2,
        description="Advancing your conditioned mission fulfills your Vice and confers a point of Memory for the scene",
        merit_type="social",
        prerequisite="template_type:dreamer"
    ),
    Merit(
        name="Not a Bug But a Feature",
        min_value=2,
        max_value=3,
        description="Spend Memory to extrude a strange organic variation on a chosen device or weapon up to Size 1 (or with three dots, Size 3), or to regenerate its charge or ammunition",
        merit_type="supernatural",
        prerequisite="template_type:dreamer,the_treatment:1"
    ),
    Merit(
        name="Realpolitik",
        min_value=1,
        max_value=3,
        description="Apply as bonus dice to pass as a follower of a political group, or by spending Memory, as a leader",
        merit_type="social",
        prerequisite="template_type:dreamer"
    ),
    Merit(
        name="The Treatment",
        min_value=1,
        max_value=5,
        description="Choose a catalytic substance and a Skill category. Spend Memory and apply the catalyst to increase one of those Skills by your Treatment rating for a scene, at the cost of lethal damage",
        merit_type="supernatural",
        prerequisite="template_type:dreamer"
    ),
    Merit(
        name="A Word from Our Sponsor",
        min_value=2,
        max_value=3,
        description="Your conditioned personality has stored independent accounts and resource caches. Spend Memory to recall enough to access an account or contact. With three dots, the network extends into the criminal underground",
        merit_type="social",
        prerequisite="template_type:dreamer"
    ),
]

# Template type is set via template_type="Infected"
# Carriers of supernatural sickness
infected_merits = [
    Merit(
        name="Carrier",
        min_value=1,
        max_value=5,
        description="Effectively gain Unseen Sense (Suitable Breeding Grounds). Pass on the Infection with a Stamina + Carrier + Infection Condition roll",
        merit_type="supernatural",
        prerequisite="template_type:infected"
    ),
    Merit(
        name="Bloodkin",
        min_value=1,
        max_value=1,
        description="Reduce a target's Doors in a social maneuver if they share the same lineage of the Infection",
        merit_type="social",
        prerequisite="template_type:infected,carrier:1"
    ),
    Merit(
        name="Bulletman Syndrome",
        min_value=5,
        max_value=5,
        description="Gain 1/1 armor per dot of Stamina. If symptoms are acute or greater, unarmed attacks deal lethal damage at increasing modifiers. Double healing times for lethal and aggravated damage",
        merit_type="physical",
        prerequisite="template_type:infected,carrier:5"
    ),
    Merit(
        name="The New Flesh",
        min_value=1,
        max_value=5,
        description="At one dot, halve all healing times. At three, heal one lethal per scene, (Stamina) times a day. At five, aggravated damage heals at the same rate as lethal. Penalise social rolls",
        merit_type="supernatural",
        prerequisite="template_type:infected,carrier:1"
    ),
    Merit(
        name="Patient Zero",
        min_value=2,
        max_value=2,
        description="Force the Infection into a short dormancy, effectively becoming a normal human person for a time",
        merit_type="supernatural",
        prerequisite="template_type:infected,carrier:2"
    ),
    Merit(
        name="Proud Parent",
        min_value=1,
        max_value=1,
        description="Treat spreading the Infection as fulfilling a Virtue, at the cost of a breaking point if something befalls the new Infected",
        merit_type="social",
        prerequisite="template_type:infected,carrier:1"
    ),
    Merit(
        name="Virulent",
        min_value=2,
        max_value=4,
        description="(••) The Bug: Attempt to inflict a target with the moderate Sick Tilt for a scene. (•••) The Virus: Inflict grave Sick Tilt for a scene. (••••) The Pestilence: Inflict Poison Tilt for a scene",
        merit_type="style",
        prerequisite="template_type:infected,carrier:2"
    ),
]

# Template type is set via template_type="Lost Boy"
# High-tech soldiers with implants dependent on Serum
lost_boys_merits = [
    # Style Merit - Core Protocol System
    Merit(
        name="The Protocol",
        min_value=1,
        max_value=5,
        description="(•) Mk 1: Unlocks augmentation Merits. Receive monthly Serum. Withdrawal advances after a month without Serum until weekly lethal damage. (••) Mk 2: Withdrawal advances after a week until daily damage. (•••) Mk 3: Withdrawal advances daily until half-daily damage. (••••) Mk 4: Withdrawal advances half-daily until quarter-daily damage. (•••••) Mk 5: Withdrawal advances quarter-daily until quarter-daily damage",
        merit_type="style",
        prerequisite="template_type:lost_boy"
    ),
    Merit(
        name="Jumper",
        min_value=1,
        max_value=3,
        description="(•) Improved: Jump with effective (Strength × 2), half falling damage. While Deprived, suffer lethal to jump with additional (Strength × 2). (••) Enhanced: Jump with effective (Strength × 4), take half falling damage as bashing. (•••) Superior: Jump with effective (Strength × 6), ignore falling damage",
        merit_type="style",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    Merit(
        name="Protocol Fixer",
        min_value=1,
        max_value=5,
        description="(•) 1 dose: Delta Protocol handler provides Serum weekly, or with Status (Lost Boys Network), Lost Boy contact provides counterfeit Serum. (••) 3 doses weekly. (•••) 6 doses weekly. (••••) 10 doses weekly. (•••••) 14 doses weekly",
        merit_type="social",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    # Augmentation Merits
    Merit(
        name="Archangel System",
        min_value=5,
        max_value=5,
        description="Spend Willpower to activate luminous neuromuscular lattice for scene. At scene end, advance withdrawal and convert lethal to aggravated. While active: Ignore physical Tilts, wound penalties, multiple assailant penalties. Stack +1/+1 Armor, +1 Defense, +2 Initiative, +5 Speed. Heal one bashing per turn, keep Defense during one action. Attacks inflict +1 damage or Knocked Down, lethal unarmed. While Deprived: +2/+2 Armor, heal two bashing per turn, attacks inflict both +1 damage and Knocked Down",
        merit_type="supernatural",
        prerequisite="template_type:lost_boy,the_protocol:5"
    ),
    Merit(
        name="Augmented Resilience",
        min_value=1,
        max_value=3,
        description="Increase your effective Stamina by dots in this Merit. While Deprived, gain 2/1 Armor",
        merit_type="physical",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    Merit(
        name="Augmented Speed",
        min_value=1,
        max_value=5,
        description="Apply this Merit as a bonus to Initiative and Speed. While Deprived, double the Speed bonus",
        merit_type="physical",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    Merit(
        name="Cloaking Device",
        min_value=3,
        max_value=3,
        description="While holding your breath, your body refracts light, hiding you from cameras, motion sensors, and thermal detectors. Penalize attempts to spot you by -5. While Deprived, you also may suffer lethal damage to activate the Cloaking Device for three turns once per scene",
        merit_type="supernatural",
        prerequisite="template_type:lost_boy,the_protocol:3"
    ),
    Merit(
        name="Holdout Storage",
        min_value=1,
        max_value=3,
        description="A cavity in your body can store items up to your Merit rating in Size, which you may withdraw as an instant action. While Deprived, suffer lethal damage to withdraw reflexively",
        merit_type="physical",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    Merit(
        name="Implanted Interface",
        min_value=2,
        max_value=2,
        description="Your nervous system has an integrated computer with wireless access, providing a +3 equipment bonus. Suffer lethal damage to overclock to a +5 bonus for the scene",
        merit_type="mental",
        prerequisite="template_type:lost_boy,the_protocol:2"
    ),
    Merit(
        name="Last-Chance",
        min_value=5,
        max_value=5,
        description="Roll Resolve + Composure as an instant action to deploy a traumatic internal weapon, which in turn rolls Stamina + Firearms + 5 as a 3L firearms attack against everyone for 10 meters. Suffer five aggravated damage and roll five dice for additional lethal damage. While Deprived, the attack has a 4L rating and 3 Armor Piercing",
        merit_type="supernatural",
        prerequisite="template_type:lost_boy,the_protocol:5"
    ),
    Merit(
        name="Pulse Generator",
        min_value=1,
        max_value=5,
        description="Once per scene, your touch can reflexively inflict Stunned and your Merit rating in bashing damage, or against electronics, twice your Merit rating in Structure damage, ignoring Durability. While Deprived, suffer lethal damage to recharge the Generator",
        merit_type="supernatural",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    Merit(
        name="Strength Augmentation",
        min_value=1,
        max_value=3,
        description="Increase your effective Strength by dots in this Merit. While Deprived, suffer lethal damage to also gain +1 Strength for the scene",
        merit_type="physical",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    Merit(
        name="Sub-Dermal Armor",
        min_value=2,
        max_value=4,
        description="Stack +1/+1 Armor, or with ••••, +2/+2 Armor. While Deprived, stack an additional +1/+1 Armor",
        merit_type="physical",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    Merit(
        name="Uncanny Perception",
        min_value=1,
        max_value=3,
        description="Apply this Merit as a bonus to Perception and aimed attacks. While Deprived, double the bonus, but suffer lethal damage and sensory blowout from extreme stimuli",
        merit_type="mental",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
    Merit(
        name="Voice Box",
        min_value=1,
        max_value=1,
        description="Perfectly mimic voices you've studied in person. While Deprived, mimic voices you've heard recorded or in passing",
        merit_type="social",
        prerequisite="template_type:lost_boy,the_protocol:1"
    ),
]

# Template type is set via template_type="Plain"
# Radical pacifists with supernatural abilities to quell violence
plain_merits = [
    Merit(
        name="Plain Reader",
        min_value=1,
        max_value=1,
        description="You've devoted your soul to radical pacifism. All acts of violence cause breaking points, but recover Willpower",
        merit_type="supernatural",
        prerequisite="template_type:plain"
    ),
    Merit(
        name="The Consequences of Violence",
        min_value=1,
        max_value=1,
        description="When you are struck and harmed unprovoked and do not respond in kind, your assailant then treats all acts of violence as breaking points",
        merit_type="supernatural",
        prerequisite="template_type:plain"
    ),
    Merit(
        name="I'm Bleeding on You",
        min_value=1,
        max_value=1,
        description="When you suffer damage by violence, each point penalizes further attacks by witnesses for the scene",
        merit_type="supernatural",
        prerequisite="template_type:plain"
    ),
    Merit(
        name="Most Infected Thing I've Ever Seen",
        min_value=2,
        max_value=2,
        description="You may convert damage taken into a Condition reflecting an ongoing Tilt from injury. Intensive care resolves Conditions formed by less than five points. Conditions formed by five points or more are Persistent",
        merit_type="supernatural",
        prerequisite="template_type:plain"
    ),
    Merit(
        name="Over Before It Started",
        min_value=1,
        max_value=1,
        description="Once per session, you may intervene to force all violence onto yourself. Roll the number of assailants and take successes as lethal damage, but recover all Willpower",
        merit_type="supernatural",
        prerequisite="template_type:plain"
    ),
    Merit(
        name="Phantom Pain",
        min_value=1,
        max_value=1,
        description="When an assailant damages you, you may inflict an equal number of points of temporary psychological damage. This damage does not injure, kill, or last longer than a scene, but wound penalties inflict Beaten Down, falling unconscious inflicts Guilty or similar Conditions, and 'dying' inflicts a Persistent Condition",
        merit_type="supernatural",
        prerequisite="template_type:plain,i_m_bleeding_on_you:1"
    ),
    Merit(
        name="The Push",
        min_value=1,
        max_value=5,
        description="You may protect a third party from violent aggressors by pushing them back, step by step. The aggressors may not attack your charges and must accumulate your Merit rating in successes on Resolve + Composure rolls, one per step, to attack you. On the sixth step without being attacked, you force them to withdraw",
        merit_type="supernatural",
        prerequisite="template_type:plain"
    ),
    Merit(
        name="You Are Being Recorded",
        min_value=1,
        max_value=1,
        description="Announce your recorded evidence of violence and roll Presence + Expression. For the rest of the scene, no one can act violently until they successfully contest your roll with Resolve + Composure - (additional people recording)",
        merit_type="supernatural",
        prerequisite="template_type:plain"
    ),
]

# Template type is set via template_type="Psychic"
# Psychics have access to various psychic powers
# These are specific merit names that are psychic-focused (from general_merits.py)
PSYCHIC_MERIT_NAMES = [
    "Aura Reading", "Automatic Writing", "Biokinesis", "Clairvoyance", 
    "Medium", "Numbing Touch", "Psychokinesis", "Psychometry", 
    "Telekinesis", "Telepathy", "Animal Possession", "Apportation", 
    "Biomimicry", "Doppelganger", "Incite Ecosystem", "Invoke Spirit", 
    "Mind Control", "Phantasmagoria", "Psychic Concealment", "Psychic Onslaught", 
    "Psychic Poltergeist", "Psychokinetic Combat", "Psychokinetic Resistance", 
    "Sojourner", "Tactical Telepathy", "Technopathy", "Telekinetic Evasion"
]

psychic_merits = [
    # NOTE: Psychics use the supernatural merits from general_merits.py
    # The specific psychic merit names are listed in PSYCHIC_MERIT_NAMES above
    # No template_type-specific merits for basic Psychics
]

# Template type is set via template_type="Psychic Vampire"
# Psychics who drain life essence
psychic_vampire_merits = [
    Merit(
        name="Psychic Vampirism",
        min_value=1,
        max_value=5,
        description="(•) Amateur: Touch to drain, inflict bashing, gain Ephemera. (••) Dilettante: Inflict Willpower loss. (•••) Practiced: Inflict lethal damage for more Ephemera. (••••) Accomplished: Efficient Willpower drain. (•••••) Virtuoso: Drain lethal and Willpower for maximum Ephemera",
        merit_type="style",
        prerequisite="template_type:psychic_vampire"
    ),
    Merit(
        name="Breath Stealer",
        min_value=1,
        max_value=3,
        description="Use psychic vampirism through breath. (•) Kiss: Close proximity. (••) Touch: Arm's length. (•••) Reach: Willpower in meters distance",
        merit_type="style",
        prerequisite="template_type:psychic_vampire,psychic_vampirism:1"
    ),
    Merit(
        name="Euphoric Touch",
        min_value=1,
        max_value=3,
        description="Modify psychic vampirism effects. (•) Numbing Touch: Reduce wound penalties. (••) Sensual Touch: Inflict Swooned Condition. (•••) Addicting Touch: Inflict Addicted Condition",
        merit_type="style",
        prerequisite="template_type:psychic_vampire,psychic_vampirism:1"
    ),
    Merit(
        name="Burst of Speed",
        min_value=1,
        max_value=1,
        description="Spend Ephemera to gain bonuses to Defense, Initiative, and Speed for a turn",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire"
    ),
    Merit(
        name="Ephemeral Battery",
        min_value=1,
        max_value=5,
        description="Increases the maximum amount of Ephemera you can store, up to Resolve + Ephemeral Battery dots",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire"
    ),
    Merit(
        name="Nocturnal Supremacy",
        min_value=2,
        max_value=5,
        description="While suffering penalties during the day, you gain various nighttime benefits, such as enhanced attributes or senses, depending on the number of dots",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire"
    ),
    Merit(
        name="Psychic Infection",
        min_value=1,
        max_value=1,
        description="When your psychic vampirism fills wound penalties or drains the last Willpower from a subject, you can roll Psychic Vampirism to potentially inflict the Psychic Vampirism ability on them",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire,psychic_vampirism:1"
    ),
    Merit(
        name="Psychic Seduction",
        min_value=1,
        max_value=1,
        description="Allows you to overwrite a victim's Vice with one of your choice, making recovery more challenging for them",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire,psychic_vampirism:1"
    ),
    Merit(
        name="Psychic Transference",
        min_value=2,
        max_value=2,
        description="By connecting a victim and a beneficiary, you can transfer the benefits of Ephemera expenditure to another individual",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire,psychic_vampirism:1"
    ),
    Merit(
        name="Shapechanging",
        min_value=2,
        max_value=3,
        description="Enables transformation into chosen animals by spending Ephemera",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire"
    ),
    Merit(
        name="Soul Eater",
        min_value=2,
        max_value=2,
        description="Allows your psychic vampirism to affect ghosts or spirits",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire,psychic_vampirism:1"
    ),
    Merit(
        name="Unearthly Beauty",
        min_value=1,
        max_value=2,
        description="Spend Ephemera to gain the benefits of Striking Looks, with enhanced effects at higher levels",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire"
    ),
    Merit(
        name="Vampiric Potency",
        min_value=1,
        max_value=5,
        description="Spend Ephemera to temporarily increase a chosen Attribute, up to your Merit rating in bonus dots",
        merit_type="supernatural",
        prerequisite="template_type:psychic_vampire"
    ),
]

# Template type is set via template_type="Skinthieves"
# Mortals who steal animal shapes by wearing their skins
skinthief_merits = [
    Merit(
        name="Skinthief",
        min_value=3,
        max_value=3,
        description="You know how to skin a particular type of prey in an occult manner, enchanting it so that you can wear it and become the prey. This costs an amount of Willpower proportional to the longevity of the skin. While in the skinned form, you use the prey's Physical Attributes and Size, and gain their instinctive ways as a Vice. Ephemeral skinned forms exist in Twilight, are vulnerable to the prey's ban and bane, and substitute Willpower or lethal damage for Essence costs. Breaking points incurred in the skinned form aren't rolled until after changing back, at a -1 penalty",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves,animal_ken:1,occult:2"
    ),
    Merit(
        name="Animal Speech",
        min_value=1,
        max_value=2,
        description="You can understand the communication of your prey animal, and can communicate in kind in that form. With two dots, your prey animal can understand your communication even in human form",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves"
    ),
    Merit(
        name="Bare Necessities",
        min_value=2,
        max_value=3,
        description="You can absorb clothes you're wearing into your skinned form when changing shape, rather than leaving them behind. With three dots, you can add a small amount of equipment",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves"
    ),
    Merit(
        name="Essence Pool",
        min_value=1,
        max_value=5,
        description="You have a pool of Essence the size of your dots in this Merit, from which you can spend only one point a turn. You can restore Essence by feeding on resonance in skinned form, or meditating and spending three Willpower",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves,skinthief:3"
    ),
    Merit(
        name="Hybrid Form",
        min_value=2,
        max_value=4,
        description="Substitute for your skinned form for two dots, or supplement it with for four dots, a fierce human-hybrid form. The Hybrid Form has a Strength and a Size equal to the greater Strength or Size of the two forms, plus one",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves"
    ),
    Merit(
        name="Renewable Skins",
        min_value=1,
        max_value=1,
        description="You can renew an old skin with the same ritual time and Willpower cost, without having to hunt a new skin",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves"
    ),
    Merit(
        name="Resilient Form",
        min_value=1,
        max_value=5,
        description="If your skinned form has less Health than your human form, add a dot of Health per dot in this Merit to make up the difference",
        merit_type="physical",
        prerequisite="template_type:skinthieves"
    ),
    Merit(
        name="Spirit Powers",
        min_value=1,
        max_value=1,
        description="You can use a dot of your prey's Influence and one of its Numina or Manifestations. You may take this Merit multiple times for multiple Influence dots and Numina or Manifestations",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves,skinthief:3"
    ),
    Merit(
        name="Strong Instincts",
        min_value=1,
        max_value=1,
        description="Calculate Defense in skinned form with the higher, not lower, of your Dexterity and Wits",
        merit_type="physical",
        prerequisite="template_type:skinthieves"
    ),
    Merit(
        name="Quick Change",
        min_value=1,
        max_value=1,
        description="You can don and doff your skin reflexively",
        merit_type="physical",
        prerequisite="template_type:skinthieves"
    ),
    Merit(
        name="Twisted Tongue",
        min_value=1,
        max_value=1,
        description="You can speak human tongues in skinned form",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves,skinthief:3"
    ),
    Merit(
        name="Unshared Flesh",
        min_value=3,
        max_value=3,
        description="Track injuries separately for your human and skinned form. An injured form doesn't heal while you're in the other form",
        merit_type="supernatural",
        prerequisite="template_type:skinthieves"
    ),
]

# Combine all minor template merits
all_minor_template_merits = (
    general_supernatural_merits + ritual_sorcery_merits +
    ghoul_merits + dhampir_merits + wolf_blooded_merits + 
    proximi_merits + alchemist_merits + fae_touched_merits + 
    ghost_merits + immortal_merits + host_merits + 
    demon_blooded_merits + stigmatic_merits + atariya_merits + 
    dreamer_merits + infected_merits + lost_boys_merits + 
    plain_merits + psychic_merits + psychic_vampire_merits + 
    skinthief_merits
)

# Create dictionary for easy lookup
minor_template_merits_dict = {
    merit.name.lower().replace(" ", "_").replace("-", "_"): merit 
    for merit in all_minor_template_merits
}

# Export alias for consistency with other merit files
minor_template_merits = all_minor_template_merits

