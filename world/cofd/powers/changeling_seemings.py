"""
Changeling: The Lost Seemings and Entitlements
Detailed seeming and entitlement information for Chronicles of Darkness 2nd Edition.
Based on Changeling: The Lost 2nd Edition core book and supplements.
"""

# ============================================================================
# SEEMINGS
# ============================================================================

ALL_SEEMINGS = {
    "beast": {
        "name": "Beast",
        "regalia": "Steed",
        "bonus_attribute": "Resistance",
        "blessing": "While unafraid, or for Glamour per three turns, deal lethal damage unarmed and take +3 to Initiative and Speed.",
        "curse": "Risk Clarity damage at half Wyrd when hasty or careless decisions harm others.",
        "description": "Grims and Savages who roamed Faerie under the heart and skin of an animal",
        "book": "CTL 2e 22"
    },
    "darkling": {
        "name": "Darkling",
        "regalia": "Mirror",
        "bonus_attribute": "Finesse",
        "blessing": "Spend Willpower, and with witnesses Glamour, to touch and become the insubstantial for three turns.",
        "curse": "Risk Clarity damage at half Wyrd when a secret you know turns out false.",
        "description": "Wisps and Mountebanks who knew safety in Faerie by disappearing into darkness",
        "book": "CTL 2e 24"
    },
    "elemental": {
        "name": "Elemental",
        "regalia": "Sword",
        "bonus_attribute": "Resistance",
        "blessing": "When surrounded by your element and either half-full of Willpower or for Glamour, act through it up to three yards away.",
        "curse": "Risk Clarity damage at half Wyrd when browbeat or coerced into a course of action.",
        "description": "Sprites and Torrents infused with and molded by the materials and environment of Faerie",
        "book": "CTL 2e 26"
    },
    "fairest": {
        "name": "Fairest",
        "regalia": "Crown",
        "bonus_attribute": "Power",
        "blessing": "While in harmony or for Glamour, you may spend Willpower on another character's behalf.",
        "curse": "Risk Clarity damage at half Wyrd when your actions are responsible for harming your allies.",
        "description": "Sovereigns and Muses touched by the heights of Faerie's glory, beauty, and cruelty",
        "book": "CTL 2e 28"
    },
    "ogre": {
        "name": "Ogre",
        "regalia": "Shield",
        "bonus_attribute": "Power",
        "blessing": "When you strike on someone else's behalf, or for Glamour, inflict Beaten Down for three turns.",
        "curse": "Risk Clarity damage at half Wyrd when those who aren't your enemies cower from you.",
        "description": "Bruisers and Gargoyles who endure the marks of blunt brutality",
        "book": "CTL 2e 30"
    },
    "wizened": {
        "name": "Wizened",
        "regalia": "Jewel",
        "bonus_attribute": "Finesse",
        "blessing": "With appropriate tools, or for Glamour, make Build Equipment rolls to work one material into another.",
        "curse": "Risk Clarity damage at half Wyrd when taken off-guard by unpleasant surprise.",
        "description": "Hatters and Domovye worn down by the crafts and labors of their Durance",
        "book": "CTL 2e 32"
    },
}

# ============================================================================
# ENTITLEMENTS
# ============================================================================

ALL_ENTITLEMENTS = {
    "baron_of_the_lesser_ones": {
        "name": "Baron of the Lesser Ones",
        "description": "Diplomat and mediator accepted among hobgoblins.",
        "prerequisites": "Empathy:2, Intimidation or Persuasion:2, any of Gentrified Bearing, Hob Kin, or Interdisciplinary Specialty (Goblins)",
        "curse": "Bonus damage dice to breaking points favoring hobgoblins.",
        "token": "A signet ring which helps to navigate and make deliveries into and through the Hedge.",
        "blessings": [
            "Gain half Wyrd as Allies among a subset of hobgoblins.",
            "Swear a hostile oath against a changeling from a predecessor's work. Recover all Willpower by fulfilling the oath."
        ],
        "book": "OAT 37"
    },
    "dauphines_of_wayward_children": {
        "name": "Dauphines of Wayward Children",
        "description": "Three cooperative caretakers for youth without homes.",
        "prerequisites": {
            "Sophomore": "Presence:2, Persuasion:2, Wyrd:3",
            "Chaperone": "Manipulation:2, Empathy:2, Wyrd:3",
            "Dowager": "Composure:2, Intimidation:2, Wyrd:3"
        },
        "curse": "Bonus damage dice to breaking points from losing a ward.",
        "token": "A lily brooch with which to locate wards and children in need. It provides bonuses to the caretaker's role among the three and can allow wards to pierce the Mask.",
        "blessings": [
            "Inherit a gift from a past ward which becomes a Token rated at half Wyrd.",
            "Non-changeling wards gain the Lucid Dreamer Merit. Treat their Bastion Fortification as 1, and dreamweave there with an extra phantom success."
        ],
        "book": "OAT 40"
    },
    "master_of_keys": {
        "name": "Master of Keys",
        "description": "Inquisitive seeker charged with unlocking the discovery of secrets and revelations.",
        "prerequisites": "Investigation:2, Empathy:2, any Merit used to uncover secrets",
        "curse": "Bonus damage dice to breaking points from holding back a secret.",
        "token": "The key to unlock your final doom still in wait. It tarnishes for a night when exposed to those who would end you, and grants the rote quality to rolls to access things locked away.",
        "blessings": [
            "Portal from any door to a free Safe Place with a two-dot Library.",
            "Spend Glamour when portaling through a Hedgeway to change its Key."
        ],
        "book": "OAT 44"
    },
    "modiste_of_elfhame": {
        "name": "Modiste of Elfhame",
        "description": "Luxurious tailor and witch that infuses their creations with the magic of the Hedge.",
        "prerequisites": "Crafts:2, Expression:2, Hollow:1+, Hedge Sorcerer",
        "curse": "Bonus damage dice to breaking points while pursuing materials for garments.",
        "token": "Bone sewing needle that grows in size and can be used as a substitute for hecatombs during Hedge Sorcery.",
        "blessings": [
            "Gain half Wyrd as Workshop (specialties based on garment crafting) which is always stocked with mundane supplies for crafting clothing.",
            "Garments crafted by the Modiste give wearers the effect of Striking Looks:1 while worn."
        ],
        "book": "Hedge 72"
    },
    "thorn_dancer": {
        "name": "Thorn Dancer",
        "description": "Graceful dancer that glides through the Thorns, exploring for their own amusement or leading others.",
        "prerequisites": "Socialize:2, Athletics:3, Expression:2, any movement based skill specialty",
        "curse": "Bonus damage dice to breaking points while not in the Hedge.",
        "token": "Gladiatorial boots/sandals that protect the wearer from extreme environments, falls, and Conditions from the Thorns. Can spend Willpower to extend to others.",
        "blessings": [
            "Gain Arcadian Metabolism and Hob Kin Merits.",
            "Reduce Clarity damage by an additional die while in the Hedge."
        ],
        "book": "Hedge 148"
    },
    "sibylline_fishers": {
        "name": "Sibylline Fishers",
        "description": "Digital oracles that trawl the BriarNet and beyond for secrets given by the Hedge.",
        "prerequisites": "Computers:3, Investigation:2, Wyrd:3",
        "curse": "Prompts a Clarity attack when their own secrets are revealed, even voluntarily.",
        "token": "A Token computer program that can operate on any internet-capable device that generates prophesies of the past, present, and future.",
        "blessings": [
            "8-again to Investigation rolls to find secrets.",
            "Can speak with the authority of an oracle to try to gain the Connected condition with a group of listeners."
        ],
        "book": "Hedge 151"
    },
    "spiderborn_riders": {
        "name": "Spiderborn Riders",
        "description": "Nomadic free spirits that reject all authority, roaming the Hedge freeing others from chains.",
        "prerequisites": "Resolve:3",
        "curse": "Bonus damage dice to breaking points when refusing to help other people in the Hedge.",
        "token": "Cut-off biker vests with individualized patches, always featuring a spiderweb and lightning bolt. Allows the wearer to know the pledges of another and helps intimidate the servants of the Fae.",
        "blessings": [
            "Gain Indomitable Merit, if already possessed, gain additional bonus dice against mental influence.",
            "Spend Glamour while navigating the Hedge to be lead to where they are needed most."
        ],
        "book": "Hedge 154"
    },
    "college_of_worms": {
        "name": "College of Worms",
        "description": "Diviners of Worms who read omens and warn others from danger.",
        "prerequisites": "Occult:2, Diviner:3, Trained Observer:1",
        "curse": "Bonus damage dice to Clarity attacks when prophecies are dismissed.",
        "token": "A pair of cracked-lens glasses carried by every Diviner.",
        "blessings": [
            "Regain Glamour when others evade danger due to your warning.",
            "Gain enhanced omen reading, danger sense, and temporal foresight."
        ],
        "book": "Homebrew/Fan Work"
    },
    "duchy_of_the_icebound_heart": {
        "name": "Duchy of the Icebound Heart",
        "description": "Heartbreak courtiers who weaponize social distance and emotional precision.",
        "prerequisites": "Manipulation:3, Wyrd:3, Politics or Socialize:2, Intimidation or Persuasion:3",
        "curse": "Clarity attack when showing compassion to those being tested.",
        "token": "A heraldry token tied to old heartbreak and royal favor.",
        "blessings": [
            "Gain Retainer dots tied to royalty, politics, or business.",
            "Spend Glamour on social rolls to remove two Doors."
        ],
        "book": "Homebrew/Fan Work"
    },
    "tolltaker_knights": {
        "name": "Tolltaker Knights",
        "description": "Contract-bound hunters who extract payment and keep difficult promises.",
        "prerequisites": "Composure:3, Brawl or Weaponry:2, Intimidation:2",
        "curse": "Bonus damage dice to Clarity attacks when promises cause collateral harm.",
        "token": "A token or Hollow inherited as payment for a predecessor's difficult assignment.",
        "blessings": [
            "Mark a quarry in combat, halving Defense and penalizing Initiative.",
            "Carry title threads, specialties, and heraldic memory."
        ],
        "book": "Homebrew/Fan Work"
    },
    "margravate_of_the_brim": {
        "name": "Margravate of the Brim",
        "description": "March Ladies who guide others through the Hedge and survive impossible pursuits.",
        "prerequisites": "Brawl or Weaponry:3, Survival:2, Wyrd:2+",
        "curse": "Bonus damage dice to Clarity attacks when those under your protection are harmed.",
        "token": "A heraldry sigil of route-marking thorns and trail-song.",
        "blessings": [
            "Reduce chase success thresholds in the Hedge by double Wyrd.",
            "Gain Interdisciplinary Specialty focused on the Hedge."
        ],
        "book": "Homebrew/Fan Work"
    },
    "noble_sages_of_the_unknown_reaches": {
        "name": "Noble Sages of the Unknown Reaches",
        "description": "Archivists, diplomats, and banes who negotiate with non-fae supernatural communities.",
        "prerequisites": "Role-specific mental/social prerequisites plus Occult.",
        "curse": "Bonus damage dice to Clarity attacks for breaking promises to non-fae supernaturals.",
        "token": "A heraldic record-seal of shared supernatural accords.",
        "blessings": [
            "Gain Contacts among non-fae supernatural communities.",
            "Gain a Barfly-like effect for supernatural gatherings."
        ],
        "book": "Homebrew/Fan Work"
    },
    "satrapy_of_pearls": {
        "name": "Satrapy of Pearls",
        "description": "Courtly dealmakers who trade influence, wealth, and obligations.",
        "prerequisites": "Persuasion:3, Manipulation:3, Resources:4",
        "curse": "Failing to fulfill a deal causes Clarity damage.",
        "token": "A pearl-mark token recognized by local courts and brokers.",
        "blessings": [
            "Gain broad Court Goodwill in major courts, twice per story.",
            "Convert cleared Notoriety from first impressions into full Willpower recovery."
        ],
        "book": "Homebrew/Fan Work"
    },
    "scarecrow_minister": {
        "name": "Scarecrow Minister",
        "description": "Fear-keepers who preserve cautionary legends and read fear in others.",
        "prerequisites": "Composure:3, Empathy:2 (Fear), Intimidation:3",
        "curse": "Bonus damage dice to Clarity attacks when fear-derived Conditions affect the Minister.",
        "token": "A ministerial token tied to urban legends and warding tales.",
        "blessings": [
            "On successful Empathy, learn fears by rolling Wyrd.",
            "Gain additional Glamour when harvesting fear."
        ],
        "book": "Homebrew/Fan Work"
    },
    "bishop_of_blackbirds": {
        "name": "Bishop of Blackbirds",
        "description": "Confessors of sorrow accompanied by dark-feathered witnesses.",
        "prerequisites": "Empathy:2, Wits:3, Composure:3",
        "curse": "Bonus damage dice to Clarity attacks from causing others Clarity/Integrity breaks.",
        "token": "A laity condition and blackbird signs recognized by the flock.",
        "blessings": [
            "Gain Wyrd-scaled Retainer flock that senses mental Conditions.",
            "Seal confessions to support atonement and recovery."
        ],
        "book": "Homebrew/Fan Work"
    },
    "magistrates_of_the_wax_mask": {
        "name": "Magistrates of the Wax Mask",
        "description": "Professional discretion-keepers who witness without being seen.",
        "prerequisites": "Composure:3, Socialize:2, Subterfuge:3",
        "curse": "Bonus damage dice to Clarity attacks when favoring personal needs over client duty.",
        "token": "A wax-mark token of contractual silence.",
        "blessings": [
            "Gain Wyrd/2 bonus to keeping composure and plausible denial.",
            "Remain unnoticed except on exceptional Perception while not drawing attention."
        ],
        "book": "Homebrew/Fan Work"
    },
    "magus_of_the_gilded_thorns": {
        "name": "Magus of the Gilded Thorns",
        "description": "Hedge navigators and misleaders who can mask a traveler's path.",
        "prerequisites": "Composure:3, Stealth:2, Hedge Sense, Wyrd:2+",
        "curse": "Bonus damage dice to Clarity attacks from prolonged lack of human contact.",
        "token": "A gilded thorn token tuned to trods and gates.",
        "blessings": [
            "Gain Wyrd-scaled navigation bonuses and deeper Hedge sight.",
            "Spend Glamour to obscure and mislead tracks, even against Huntsmen."
        ],
        "book": "Homebrew/Fan Work"
    },
    "sacred_band_of_the_golden_standard": {
        "name": "Sacred Band of the Golden Standard",
        "description": "Legendary exemplars defined by a chosen signature Skill.",
        "prerequisites": "Presence:3, Wyrd:2, chosen Skill 3+ with suitable Specialty",
        "curse": "Failing a task with the chosen Skill triggers Clarity attack dice equal to merit ranks.",
        "token": "A heraldry badge tied to public renown and impossible feats.",
        "blessings": [
            "Spend chapter points to force exceptional success thresholds or suppress 10-again.",
            "Bestow Inspired on witnesses after signature successes."
        ],
        "book": "Homebrew/Fan Work"
    },
    "squire_of_the_broken_bough": {
        "name": "Squire of the Broken Bough",
        "description": "Cause-bound champions who endure harm for clients and vows.",
        "prerequisites": "Composure:3, Resolve:3, Weaponry:2",
        "curse": "Bonus damage dice to Clarity attacks when formal oaths to the Squire are broken.",
        "token": "A vow-mark token tied to the Squire's current cause.",
        "blessings": [
            "Gain temporary Willpower reserve equal to Wyrd/2 when sworn to a cause.",
            "Spend Willpower to inflict Frightened on witnesses of the Squire's death."
        ],
        "book": "Homebrew/Fan Work"
    },
    "adjudicator_of_the_wheel": {
        "name": "Adjudicator of the Wheel",
        "description": "Judges of fate and oath redress who intervene in injustice.",
        "prerequisites": "Resolve:3, Investigation:2, Trained Observer:1",
        "curse": "Bonus damage dice to Clarity attacks when duty eclipses health and relationships.",
        "token": "A judicial wheel-token bearing unresolved verdicts.",
        "blessings": [
            "Spend Glamour with Kenning to glimpse likely futures up to Wyrd/2 days.",
            "Swear third-party hostile oaths on behalf of aggrieved petitioners."
        ],
        "book": "Homebrew/Fan Work"
    },
    "diviners_of_worms": {
        "name": "Diviners of Worms",
        "description": "Omen readers who wield common sense and danger-sight through pattern and prophecy.",
        "prerequisites": "Occult:2, Diviner:3, Trained Observer:1",
        "curse": "Bonus damage dice to Clarity attacks when prophecies are ignored.",
        "token": "A cracked-lens instrument for reading signs in ordinary debris.",
        "blessings": [
            "Gain Common Sense-like guidance with Wyrd/2 bonus.",
            "Gain enhanced Danger Sense against immediate threats, including environmental danger."
        ],
        "book": "Homebrew/Fan Work"
    },
    "duchess_of_truth_and_loss": {
        "name": "Duchess of Truth and Loss",
        "description": "Fetch hunters who preserve certainty and pursue concealed quarry.",
        "prerequisites": "Wits:3, Investigation:2, must have killed a fetch",
        "curse": "Bonus damage dice to Clarity attacks when others defend the Duchess's quarry.",
        "token": "A keepsake from the first fetch hunt that anchored the title.",
        "blessings": [
            "Gain Wyrd/2 bonus to locating those actively hiding.",
            "Spend Glamour to preserve fetch remains for one lunar month to aid closure."
        ],
        "book": "Homebrew/Fan Work"
    },
    "guildmaster_of_goldspinners": {
        "name": "Guildmaster of Goldspinners",
        "description": "Plutomancers who weave influence through debt, value, and leverage.",
        "prerequisites": "Academics (Finance/Business), Resources:3",
        "curse": "Bonus damage dice to Clarity attacks after witnessing broken promises.",
        "token": "A humble personal keepsake that grounds value beyond wealth.",
        "blessings": [
            "Gain Wyrd/2 Mental Merit dots distributed as desired.",
            "Spend Glamour to sense who nearby is most desperate for money."
        ],
        "book": "Homebrew/Fan Work"
    },
    "paragon_of_story_heroes": {
        "name": "Paragon of Story Heroes",
        "description": "Threadmenders who shape narratives toward survivable outcomes.",
        "prerequisites": "Wits:3, Academics:2, Persuasion or Subterfuge:2",
        "curse": "Bonus damage dice to Clarity attacks suffered in the Hedge.",
        "token": "A story-symbol item central to the Paragon's guiding narrative.",
        "blessings": [
            "Gain Allies representing people aided by prior paragons.",
            "Spend Glamour to deliver an uninterruptible dramatic speech heard by chosen listeners."
        ],
        "book": "Homebrew/Fan Work"
    },
    "castellan_of_the_broken_cage": {
        "name": "Castellan of the Broken Cage",
        "description": "Catalysts of transformation who recognize buried desires and risky change.",
        "prerequisites": "Manipulation:3, Empathy or Socialize:2, Wyrd:2+",
        "curse": "Bonus damage dice to Clarity attacks when a chrysalid is harmed by the Castellan's influence.",
        "token": "A prison-key token split into transformed halves.",
        "blessings": [
            "Gain Allies representing successful former chrysalids.",
            "Automatically sense lies about conscious desire and faint cues for unconscious desire."
        ],
        "book": "Homebrew/Fan Work"
    },
    "eternal_echo": {
        "name": "Eternal Echo",
        "description": "Witnesses who preserve history and resist tampering with memory.",
        "prerequisites": "Resolve:3, Academics:2, Expression:2",
        "curse": "Bonus damage dice to Clarity attacks from discovering major lies about important events.",
        "token": "A preserved record-link to living stories of the Lost.",
        "blessings": [
            "Gain Wyrd/2 bonus to resist involuntary disclosure and memory coercion.",
            "Gain Eidetic Memory; if already owned, gain two alternative Merit dots."
        ],
        "book": "Homebrew/Fan Work"
    },
    "knights_of_the_knowledge_of_the_tongue": {
        "name": "Knights of the Knowledge of the Tongue",
        "description": "Sensory chefs who broker alliances and stories through food.",
        "prerequisites": "Stamina:3, Crafts:3 (Cooking)",
        "curse": "Bonus damage dice to Clarity attacks when a cooked dish causes disaster.",
        "token": "A favorite mundane cooking tool or recipe book.",
        "blessings": [
            "Gain Wyrd/2 Contacts or Allies from feasts and culinary diplomacy.",
            "Gain +5 to locating or identifying ingredients, including known goblin fruit and known animals."
        ],
        "book": "Homebrew/Fan Work"
    },
    "legate_of_the_black_apple": {
        "name": "Legate of the Black Apple",
        "description": "Hedgeward envoys who fortify courage and negotiate perilous paths.",
        "prerequisites": "Two Social Skills 4+, combined Composure+Resolve 7+, Wyrd:3+",
        "curse": "Bonus damage dice to Clarity attacks when faced with someone the Legate failed to help.",
        "token": "A mark of rescue tied to children saved from the Gentry.",
        "blessings": [
            "Gain Wyrd/2 dots in Fae Mount, Hedge Sense, Hedgewise, and/or Hob Kin.",
            "Spend Glamour to grant +3 for one scene on resisting fear or intimidation."
        ],
        "book": "Homebrew/Fan Work"
    },
    "lost_pantheon": {
        "name": "Lost Pantheon",
        "description": "Ancients who embody a deity's domain and sanctify contested places.",
        "prerequisites": "Presence:3, Occult:2 (deity specialty), Wyrd:3+",
        "curse": "Bonus damage dice to Clarity attacks when others scorn, deny, or ignore the deity.",
        "token": "A sacred icon of the deity that anchors duty and identity.",
        "blessings": [
            "Spend Glamour to consecrate one Hollow as a demanding temple.",
            "Spend Willpower to imbue an object with deity-linked element for scene-long effects."
        ],
        "book": "Homebrew/Fan Work"
    },
}

# Extended entitlement writeups for +lookup detail views.
# These capture setting context (privileges/duties, mien, succession, and token notes)
# beyond the short reference blurb.
ENTITLEMENT_EXTENDED_NOTES = {
    "castellan_of_the_broken_cage": {
        "privileges_and_duties": "The Castellan pushes chosen 'chrysalids' to break from social constraints and transform their lives, often without consent. She is typically not overtly political, but freeholds still seek her out for hard-to-change individuals. Others may regard her as helpful, arrogant, or dangerously meddlesome.",
        "mask_mien": "The title emphasizes metamorphosis: shifting irises, insect-like features, and an iridescent aura in mien, with subtler signs under the Mask.",
        "bequeathal": "Outgoing Castellans traditionally test candidates through chained challenges and riddles. Successors inherit emotional and mnemonic residue from prior chrysalid interventions.",
        "token_details": "Lepidopteran Locket: tracks a current chrysalid and grants influence bonuses when urging risk, novelty, and convention-breaking growth. Catch requires a meaningful visible change in surroundings; drawback penalizes repeated actions in-scene.",
    },
    "duchy_of_the_icebound_heart": {
        "privileges_and_duties": "The title-holder specializes in heartbreak, emotional leverage, and social precision. They are powerful in social influence but often feared for their methods.",
        "mask_mien": "Cold glamour, remote beauty, and frost-kissed details are common signs. Presence intensifies longing and fixation in social encounters.",
        "bequeathal": "Traditionally linked to wounded heirs and emotionally scarred successors; inherited obligations often include political promises and unresolved social fallout.",
        "token_details": "Winter's Heart: tracks and pressures emotional targets, reveals social bonds as visible thread-like links, and grants seductive/manipulative leverage. Catch requires burning the written name of someone truly loved.",
    },
    "eternal_echo": {
        "privileges_and_duties": "The Echo preserves Lost stories so no changeling is forgotten. They frequently travel freehold to freehold, serving as witness, archivist, and memory-keeper.",
        "mask_mien": "Mien shifts toward deep-listening and recall: dark reflective eyes, hyper-attentive hearing, and an audible whispering undertone when invoking memory.",
        "bequeathal": "Successors are selected through long vetting and oathbound transfer rites. New Echoes often endure severe cognitive strain while integrating inherited records.",
        "token_details": "Record of the Lost: stores and replays audio-memory, allows permanent scene recording, and supports selective memory transfer between bearer and record. Catch requires confessing an untold truth.",
    },
    "knights_of_the_knowledge_of_the_tongue": {
        "privileges_and_duties": "Epicurean knights feed the Lost and pursue extraordinary culinary mastery, often competing fiercely with each other. They value quality, rarity, and innovation over convention.",
        "mask_mien": "Members present as vivid, healthy, and sensorially focused. Mien commonly includes supernatural palate markers (for example, blue tongue) and persistent food-adjacent aura.",
        "bequeathal": "Candidates are tested through rigorous cooking and tasting gauntlets emphasizing technique and creativity. Retired title-holders often remain as mentors.",
        "token_details": "Magical Measuring Spoons: grant rote quality on cooking actions and can infuse dishes with temporary magical benefits. Catch requires eating three bites of hated food.",
    },
    "legate_of_the_black_apple": {
        "privileges_and_duties": "The Legate negotiates directly with the Gentry for better terms where others cannot. They are respected for results but often viewed with suspicion and emotional distance.",
        "mask_mien": "A venerable, severe presence with fermented-apple undertones, immaculate but muted dress, and a formal bearing under pressure.",
        "bequeathal": "Legates maintain apprentices over time, testing diplomacy, restraint, and survivability. Successors may inherit active obligations and dangerous precedent.",
        "token_details": "Apple Pendant: compels response from named True Fae Titles and opens a narrow truce-window for negotiation. Also grants duty-focused Wits/Manipulation bonuses and a defensive Glamour option.",
    },
    "lost_pantheon": {
        "privileges_and_duties": "Ancients embody chosen deity domains, maintain sacred sites and elemental fonts, and uphold mythic obligations in both Hedge and mortal contexts.",
        "mask_mien": "Mien manifests deity-specific iconography and increasingly godlike presence. The title emphasizes awe, terror, or reverence depending on divine aspect.",
        "bequeathal": "Succession may be deliberate (through trained acolytes and ritual passing) or rediscovered via dormant medallions after unattended gaps.",
        "token_details": "Celestial Medallions: reinforce divine first-impression authority, empower consecration effects, and facilitate acolyte-aided sacrificial empowerment mechanics.",
    },
    "magistrates_of_the_wax_mask": {
        "privileges_and_duties": "A high-discretion service title that fills practical freehold gaps (logistics, labor, covert tasks) while preserving deniability and professional neutrality.",
        "mask_mien": "Mien tends wax-like and mutable; Mask tends neat but subtly marked by residue and crafted concealment.",
        "bequeathal": "Successors are selected for discretion and operational composure. Some lineages actively conceal the title's inner mechanisms from outsiders.",
        "token_details": "Wax Masks: animate role-bound effigies and permit temporary command hierarchies. Catches and drawbacks reflect blood-cost, wage-cost, and exposure risk.",
    },
    "magus_of_the_gilded_thorns": {
        "privileges_and_duties": "The Magus serves as interlocutor, navigator, and custodian for Hedge intent, routes, and hidden pathways. Others seek guidance but rarely receive full transparency.",
        "mask_mien": "Wood/thorn/soil motifs, shifting contour, and plantlike elements become more pronounced with tenure; presentation can read as wild, uncanny, or liminal.",
        "bequeathal": "Only one Magus is generally recognized at a time. Loss of Hedge favor can strip title-access, memory links, and advanced spin-related capability.",
        "token_details": "Thorned Crown: alters hedge-gate routing behavior, obscures position from tracking, and imposes communication distortion effects under Willpower spend.",
    },
    "margravate_of_the_brim": {
        "privileges_and_duties": "The Margrave secures, scouts, and stabilizes Hedge-facing freehold risk, especially during foundation, upheaval, or route collapse.",
        "mask_mien": "Competence-forward presentation with predatory or wilderness-coded details, thorn-marked scar memory, and high-contrast eye changes in mien.",
        "bequeathal": "Candidates are tested through solo threat conquest, route mapping, and safe escort duties. Sudden succession through combat death is common.",
        "token_details": "Petrified Blade: grants nearest-gate route awareness, Hedge directionality support, and combat utility against hostile Hedge denizens.",
    },
    "noble_sages_of_the_unknown_reaches": {
        "privileges_and_duties": "A triadic office (Archivist, Diplomat, Bane) devoted to knowledge and management of non-fae supernatural entities and communities.",
        "mask_mien": "Each role manifests distinct mien shifts: scholarly sensitivity (Archivist), social magnetism (Diplomat), and threat-vigilance (Bane).",
        "bequeathal": "Roles are inherited separately as vacancies arise. Retirements are constrained by cross-role witnessing and continuity requirements.",
        "token_details": "Arcane Rings (brass/silver/steel): grant role-tuned bonuses to research, engagement, and confrontation, plus true-nature verification on direct gaze.",
    },
    "scarecrow_minister": {
        "privileges_and_duties": "The Minister weaponizes fear and urban legend to keep mortals and Lost away from genuinely predatory supernatural danger.",
        "mask_mien": "Burlap, straw, and scarecrow-coded motifs intensify over time; presentation can shift from subtle warning-sign to overt nightmare iconography.",
        "bequeathal": "Successors are selected for resilience and judgment under terror-work pressures. Legacy memory transfer often includes morally complex operations.",
        "token_details": "Bugbear Mask: shapes fear-forms, boosts intimidation/rumor propagation, and can mirror known fears at Glamour cost.",
    },
    "tolltaker_knights": {
        "privileges_and_duties": "The Knight enforces consequence for oathbreakers and unjust escapees, emphasizing proof, precision, and contract scope discipline.",
        "mask_mien": "Quiet-footed, judgment-heavy presence with lantern-coded symbolism and aura of measured inevitability.",
        "bequeathal": "Title commonly transfers through death-linked vision chains, though some lineages cultivate successors through duty training and trial contracts.",
        "token_details": "Luminous Lodestar: tracks contracted quarry by proximity-shifting light and grants investigation/tracking bonuses tied to claim validation and pursuit.",
    },
    "adjudicator_of_the_wheel": {
        "privileges_and_duties": "The Judge addresses perceived small-scale injustice through calibrated intervention, timing, and probability manipulation rather than overt spectacle.",
        "mask_mien": "Mask trends toward ordinary anonymity; mien emphasizes pathways, branching outcomes, and precision under pressure.",
        "bequeathal": "Most Judges serve until death. Voluntary succession requires intensive testing under engineered adversity and pattern-recognition pressure.",
        "token_details": "Wheel of Fortune: grants justice-focused investigation support and limited narrative 'twists' per story, constrained to in-presence interventions.",
    },
    "bishop_of_blackbirds": {
        "privileges_and_duties": "The Bishop tends Clarity and mental burden across Lost populations, often collecting owed favors to reinforce long-term social stabilization.",
        "mask_mien": "Blackbird-coded avian features deepen over tenure; mien and tone emphasize attentiveness, sorrow literacy, and difficult pastoral authority.",
        "bequeathal": "Candidates require strong baseline stability; transfer usually occurs through formal blessing rites or token-led succession after death.",
        "token_details": "Argent Aspersorium: transfers Conditions and Clarity burden from subjects to bearer, supports perceptual clarity blessings, and stores selected personal burden.",
    },
    "diviners_of_worms": {
        "privileges_and_duties": "Diviners broadcast portent, identify threat trajectories, and translate omens for freeholds despite frequent skepticism or interpretive conflict.",
        "mask_mien": "Worm-mark motifs and cracked-lens signifiers denote office, with omen sensitivity escalating physical/behavioral tells during stress or revelation.",
        "bequeathal": "The title is fate-driven and often involuntary at onset. Candidates are typically obsession-led seekers pulled toward Instrument alignment.",
        "token_details": "Diviner's Instrument: supports non-dream divination queries, chapter-limited ritual research uplift, and scene-level prophetic persuasion boosts.",
    },
    "duchess_of_truth_and_loss": {
        "privileges_and_duties": "The Duchess identifies and removes fetches with emphasis on certainty, operational discretion, and aftermath containment.",
        "mask_mien": "Predatory detailing and doll-like eye motifs are common markers; mien sharpens hunter presentation while Mask preserves social passability.",
        "bequeathal": "Succession favors proven fetch-solvers who can operate quietly and without theatrical ego. Emergency transfer can occur through token rediscovery.",
        "token_details": "False Face of Truth: infallible fetch/human/changeling identification from sample input, anti-fetch tracking veil, and strong anti-concealment utility.",
    },
    "guildmaster_of_goldspinners": {
        "privileges_and_duties": "The Guildmaster brokers binding value contracts and liquidity support for changelings, with strict enforcement and explicit payment terms.",
        "mask_mien": "Polished but restrained wealth-signaling under Mask; mien gradually acquires gilded and threadlike features over tenure.",
        "bequeathal": "Successors are selected for composure, negotiation precision, and ethical steadiness under desperation economics.",
        "token_details": "Spindle's Talon: converts sealed bargains into temporary wealth generation and boosts bargain/contract action thresholds.",
    },
    "paragon_of_story_heroes": {
        "privileges_and_duties": "The Paragon nudges emergent narratives toward survivable, constructive outcomes without openly confronting the Wyrd's narrative momentum.",
        "mask_mien": "Bright, high-contrast presentation and audible/visual story-signifiers emphasize charismatic intervention and scene-pivot influence.",
        "bequeathal": "Apprentices complete practical narrative-correction trials before inheriting. New holders often report Hedge hostility toward repeated story intervention.",
        "token_details": "Scroll of Shifting Threads: reads active narrative vectors, reveals relevant influences, and supports chapter-limited rote planning toward declared goals.",
    },
    "squire_of_the_broken_bough": {
        "privileges_and_duties": "The Squire takes up others' causes where victims cannot pursue vengeance alone, repeatedly risking death and Clarity in service.",
        "mask_mien": "Wear-and-tear visuals and blood-mark echoes signal martyrdom, attrition, and repeated return from violent duty.",
        "bequeathal": "The title seeks broken candidates with little personal future left; acceptance binds the holder to a brutal duty cycle.",
        "token_details": "Broken Blade: provides high durability and death-return functionality tied to activation state, with severe long-term mental cost per resurrection.",
    },
    "satrapy_of_pearls": {
        "privileges_and_duties": "The Satrap arbitrates and manipulates value itself, from contracts to social worth, with enormous macro-social impact potential.",
        "mask_mien": "Deliberately opulent signifiers under Mask; mien carries pearlescent eyes and gilded complexion details denoting market sovereignty.",
        "bequeathal": "Successions are often cultivated through long patronage ('Shining of the Pearl') and practical value-manipulation proving trials.",
        "token_details": "Eyes of the Market: exchange selected dots for Pearl-of-Experience equivalents and expose aspiration leverage vectors at Glamour/Willpower cost.",
    },
    "college_of_worms": {
        "privileges_and_duties": "A divinatory fraternity focused on actionable warning systems against Gentry and supernatural threat emergence; interpretation remains politically fraught.",
        "mask_mien": "Cracked-lens insignia and omen-sensitivity markers identify full members; initiation tracks apprenticeship rigor and fate-read discipline.",
        "bequeathal": "Membership is instructional and oathbound; the deeper Bargain compels warning behaviors and occasional symbolic compliance acts.",
        "token_details": "College practices often overlap with Diviner instruments and omen-procedure tooling rather than a single universal inherited relic.",
    },
}

for _entitlement_key, _notes in ENTITLEMENT_EXTENDED_NOTES.items():
    if _entitlement_key in ALL_ENTITLEMENTS:
        ALL_ENTITLEMENTS[_entitlement_key].update(_notes)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_seeming(seeming_name):
    """Get a specific seeming by name."""
    seeming_key = seeming_name.lower().replace(" ", "_")
    return ALL_SEEMINGS.get(seeming_key)

def get_all_seemings():
    """Get all seeming data."""
    return ALL_SEEMINGS.copy()

def get_entitlement(entitlement_name):
    """Get a specific entitlement by name."""
    entitlement_key = (
        entitlement_name.lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("'", "")
    )
    return ALL_ENTITLEMENTS.get(entitlement_key)

def get_all_entitlements():
    """Get all entitlement data."""
    return ALL_ENTITLEMENTS.copy()

