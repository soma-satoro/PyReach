"""
Changing Breeds Favors and Aspects for World of Darkness 1st Edition.
Complete descriptions of all shapeshifter abilities.
"""

# ==============================================================================
# FAVORS (Innate breed abilities)
# ==============================================================================

CHANGING_BREED_FAVORS = {
    "aquatic": {
        "name": "Aquatic",
        "cost": "** to ***",
        "description": "Born for water, a creature with this Favor has fins, sleek skin or scales, and the breathing and muscular development that makes him native to water. He can dive and swim as naturally as a land-based beast walks. In water, his Movement trait reflects swimming, not walking; in fact, his land-based Move may be half of the normal trait... assuming he can move on land at all in anything but his human form.",
        "system": "For two dots, the character can swim like a fish in his animal forms; for three, he can dive in human form as well. A character with this Favor can dive 100 feet for each point of Stamina he possesses (in that form) if his Nahual is native to land, 1,000 feet per point if his Nahual is native to water. This trait is free for water-based creatures.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "bioluminescence": {
        "name": "Bioluminescence",
        "cost": "*",
        "description": "In the deep canyons of the ocean, sunlight never goes. Nevertheless, weird constellations of light drift and circulate in the darkness, as bioluminescent fish live out their lives in the abyss. Likewise, lightning bugs pulse with incandescent glows. A character with this Favor emits light from some portion of his body--or perhaps all of it.",
        "system": "The light is roughly equal to that of a powerful flashlight; in game terms, the light eliminates up to two points of dice penalties for acting in darkness. The character can turn this Favor on or off at will, as a reflexive action, and the Favor costs no Essence to employ. The store of luminescent chemicals must 'recharge' after each usage (10 minutes). The effect lasts for one scene. In darkness, other characters gain a +2 bonus to attack the feral while he glows. For creatures with natural bioluminescence, this Favor is free.",
        "forms": ["All forms"]
    },
    
    "darksight": {
        "name": "Darksight",
        "cost": "*",
        "description": "Many werebeasts see in the dark as easily as humans see on a bright, cloudless day. They never receive penalties for operating in darkness; in fact, this ability gives them the additional advantage of a +2 bonus to all Stealth rolls when they move through darkness.",
        "system": "This perception in always 'on' in any form, and costs no Essence to employ. Darksight also helps a character in visually-adverse conditions, such as dense fog, smoke or a heavy downpour, by halving all of her sight-based penalties (rounding down).",
        "forms": ["All forms"]
    },
    
    "echolocation": {
        "name": "Echolocation",
        "cost": "• or •••",
        "description": "A character with Echolocation can use sonic echoes to 'read' his immediate surroundings without actually having to see them. He can ignore all visually-based penalties such as darkness, fog, smoke or blindness.",
        "system": "One-dot version: Ignore all visually-based penalties. Three-dot version: Additionally, cannot be surprised unless asleep, and has permanent +1 bonus to Defense due to heightened awareness of incoming attacks. This Favor is free for dolphins and bats.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "extra_limbs": {
        "name": "Extra Limbs",
        "cost": "* for first limb, * per set of two afterward",
        "description": "Trunks. Tentacles. Tails. Animals have the strangest ways of making up for opposable thumbs. With the basic level of this Favor, the character gets a limb that's capable of acting as a 'hand' without fingers.",
        "system": "A character with multiple limbs can get one extra action (limb only, no movement/dodging) for every two limbs after the first. A multi-armed feral adds +1 to Defense for every limb after the third. He can attack multiple opponents on the same basis. No off-hand penalties apply. This trait is free for animals that normally possess multiple limbs. Cannot be used in Man-Guise except for bizarre mutations.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "fang_and_claw": {
        "name": "Fang and Claw",
        "cost": "* to *****",
        "description": "Sharp talons, claws, teeth, horns, hooves, antlers, stingers or other 'primary weapons' allow this creature to inflict lethal damage with her hand-to-hand attacks.",
        "system": "Free breed favor: claws/teeth add +1 die to hand-to-hand attacks; horns/antlers add +2 dice. For *: add an additional die to the attack, OR buy the attack for a beast that doesn't usually get it free, OR allow use in Man-Guise. For **: sheathe claws even if species cannot normally do so. For ***: sheathe claws in human form and add +1 to attacks when employed.",
        "forms": ["Varies by purchase"]
    },
    
    "limbless": {
        "name": "Limbless",
        "cost": "-*",
        "description": "For serpents, fish and other limbless creatures, the world can be a challenging place. This Favor reflects an animal form that lacks arms, legs or other appendages that can manipulate the character's surroundings outside of basic movement.",
        "system": "In her beast-form, this character is either waterbound or reduced to slithering for movement. Of course, in the right environment, this feral may be very fast indeed...",
        "forms": ["Primal Beast", "Dire Beast"]
    },
    
    "many_legged": {
        "name": "Many-Legged",
        "cost": "••••",
        "description": "The scutter of dozens, if not hundreds, of not-so-tiny feet alerts a potential victim of this shapechanger that he's playing Fly to a nightmarish Spider...",
        "system": "This Favor adds +4 to the character's normal Species Factor when figuring its Speed trait, and allows the character to walk on sheer surfaces (per Wallwalking Favor). Free to creatures with many sets of legs. Restricted to insectine or arachnid beings. Sight of this invokes the Delusion with -2 penalty to witness's resistance roll.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "musk": {
        "name": "Musk",
        "cost": "***",
        "description": "Similar to skunks and polecats, certain ferals can spray blasts of revolting musk or urine.",
        "system": "All characters within 300 feet must make Composure rolls or suffer dizziness and nausea. Roll Dexterity + Feral Heart; successes = number of characters hit in 15'x15' area. Characters sprayed directly take -3 penalty to Composure roll. Each character within 300 feet suffers -3 penalty to dice pools, and Defense/Speed/Initiative have one level subtracted. Must spend an Essence point to activate. Serious effects last one scene, but stench lingers for days.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "natural_armor": {
        "name": "Natural Armor",
        "cost": "* to *****",
        "description": "Thick skin, scales, a shell or a carapace protect this feral from many forms of harm. Depending on the beast, this armor could be all-encompassing or limited to certain areas.",
        "system": "Free version: 1/1 armor rating (not bulletproof unless breed listing says otherwise). For *: armor becomes bulletproof. For ***: armor is 2/1. For ****: armor is 3/2. For *****: armor is 4/3. Generally applies only to Primal, Dire, War forms. Player may choose to have it apply to human form as well (but suffers -2 penalty to Social rolls where normal appearance would help).",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast", "optionally Man-Guise"]
    },
    
    "needleteeth": {
        "name": "Needleteeth",
        "cost": "***",
        "description": "The shapechanger has strong, sharp teeth capable of biting through very tough materials.",
        "system": "When using his teeth to damage an object, he can ignore up to two points of that object's Durability while in Primal, Dire or War forms. No additional damage is done to living creatures, although the visual is pretty terrifying.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "quills": {
        "name": "Quills",
        "cost": "** to *****",
        "description": "Sharp spines jut from the shapechanger's skin. This Favor reflects their effects when those spines meet an opponent's flesh.",
        "system": "Opponent struck by quills makes contested roll: opponent's Stamina vs. feral's Dexterity + Feral Heart. If feral wins, subtract opponent's armor from total = bashing damage (doesn't heal until quills removed). Removing quills: 1 minute per Health point + 1 lethal damage. For **: bristling quills. For ***: can fire them up to 15 feet (Dexterity + Feral Heart roll). For each additional point (up to +3): quills larger, add +1 die to quill-based dice pool. Quills can be poisoned with Venomous Favor. Free for beasts whose species normally has quills.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "razorskin": {
        "name": "Razorskin",
        "cost": "*** or ****",
        "description": "Of the many frightening aspects of sharks, perhaps the most overlooked is their rough, sandpapery scales. A shapeshifter with Razorskin has this quality in spades. Her skin can tear someone to ribbons.",
        "system": "When enemy makes successful Brawl attack (or is grabbed/pressed against skin), he automatically takes 1 lethal damage. If using a weapon, weapon sustains 2 Structure damage. Character must spend 1 Essence to activate for one scene (3-dot version). Four-dot version: power is always on. Works in all forms except Man-Guise.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast", "Throwback"]
    },
    
    "size": {
        "name": "Size",
        "cost": "••••",
        "description": "Many animals dwarf human beings. Others scurry in Man's shadow. Per the systems given in the World of Darkness Rulebook, a creature's Size trait determines that character's Health dots.",
        "system": "The base Size for a character's species is free. Upgrading one additional level above the base Size costs ****. Cannot be raised further without Storyteller approval. Size ranges: 1 (toad, sparrow, bat), 2 (cat, hare, crow, rat), 3 (fox, owl, hawk, coyote), 4 (dog, wolf, goat, eagle), 5 (human, large dog, leopard, hyena, python), 6 (deer, jaguar, dolphin), 7 (bear, horse, lion, alligator), 8 (tiger, grizzly bear), 9 (cattle, boar), 10 (moose, giant swine), 11 (wildebeast), 12 (bison, tiger shark), 13 (rhino, hippopotamus), 14 (Asian elephant, great white shark), 15 (African elephant, orca).",
        "forms": ["Primal Beast", "War-Beast"]
    },
    
    "speed": {
        "name": "Speed",
        "cost": "Free",
        "description": "Most animals are either painfully slow or incredibly fast. People fall in the middle. A feral character favors her animal species when she's in beast-form, but uses her human speed otherwise.",
        "system": "Speed Factor by species: 1 (tortoise, insect), 3 (hare, rat), 5 (human, bear), 8 (wolf, dog, cat), 10 (hawk, tiger), 12 (horse, leopard), 15 (cheetah, gazelle). Unless otherwise specified, War-Beast Speed is based on human form, not animal species.",
        "forms": ["Varies"]
    },
    
    "water_breath": {
        "name": "Water Breath",
        "cost": "*",
        "description": "The character can hold her breath or breathe underwater for as many hours as she has Feral Heart dots.",
        "system": "Costs one point of Willpower to use. Duration: hours equal to Feral Heart dots.",
        "forms": ["All forms"]
    },
    
    "webbing": {
        "name": "Webbing",
        "cost": "••••",
        "description": "Silky in texture and steely in toughness, these strands can support hundreds of pounds of weight. A creature with this Favor can spin massive webs involving hundreds of feet of complex material.",
        "system": "Roll Dexterity + Crafts + Feral Heart. Total successes = Structure of webbing (Durability always 3). Large/elaborate webs may be extended action. To weave character into web, contested Strength + Athletics vs. weaving roll. Trapped victim must overcome double web's Structure to break free. Unbound characters can cut/burn through (overcome Structure): blunt weapons have no effect, edged add +1 die, leverage tools add +3 dice, fire inflicts double damage in 10'x10' area per turn.",
        "forms": ["Primal Beast", "War-Beast"]
    },
    
    "wings": {
        "name": "Wings",
        "cost": "••••",
        "description": "This Favor's self-explanatory: if you have wings, you can fly. Most often, this Favor reflects full bone-and-muscle wings. Certain animals have loose skin that catches the air, allowing for limited flight.",
        "system": "No roll needed in Primal Beast form unless attempting difficult maneuver, hindered, or contending with severe weather (Dexterity + Athletics). In War-Beast form must make Dexterity + Athletics roll every turn to fly/glide. Cannot fly in human form, but can jump twice as far as normal due to light bone structure. Free for creatures that normally have wings, costs four dots for ones that don't.",
        "forms": ["Primal Beast", "War-Beast (difficult)"]
    }
}

# ==============================================================================
# ASPECTS (Purchased supernatural abilities)
# ==============================================================================

CHANGING_BREED_ASPECTS = {
    # A
    "alarming_alacrity": {
        "name": "Alarming Alacrity",
        "cost": "* to *****",
        "description": "With the expenditure of a Willpower point, the werebeast can double his Speed for as many turns as he has points in this Aspect.",
        "system": "Spend 1 Willpower. Double Speed for turns equal to Aspect dots. Can be used in any form.",
        "forms": ["All forms"]
    },
    
    "asthmatic_reaction": {
        "name": "Asthmatic Reaction",
        "cost": "***",
        "description": "Many folks are allergic to animals... or, more often, to animal saliva. This trick takes advantage of that reaction.",
        "system": "Spend 1 Essence, roll Dexterity + Athletics to spit at opponent (Defense applies). If hits, no immediate damage. Next turn: -3 penalty to all rolls. Second turn: -2 penalty. Third turn: -1 penalty. Fourth turn: penalty vanishes but takes 2 bashing damage from wracking coughs.",
        "forms": ["All forms"]
    },
    
    "aww": {
        "name": "Aww!!!",
        "cost": "* to *****",
        "description": "Some critters are too cute for words, even if they can rip your arm off. A feral with this talent can cute her way out of most kinds of trouble.",
        "system": "Add +1 bonus per dot to all Social rolls that emphasize adorable qualities. Can be used in any form but grants only half bonus in human shape.",
        "forms": ["All forms, half bonus in Man-Guise"]
    },
    
    # B
    "bare_necessities": {
        "name": "Bare Necessities",
        "cost": "• or •••",
        "description": "Shapeshifters can't afford to be modest. With this Aspect, a character's clothes, pocketed possessions and anything else touching her skin effectively transforms with her.",
        "system": "One-dot: clothes and pocketed items transform with you. Three-dot: can take additional items (Size 1-2) like weapons or backpacks. Complex mechanical items may malfunction (Stamina + Feral Heart roll). Up to 4 small items (Size 1) can be carried in garment/purse/backpack.",
        "forms": ["All forms"]
    },
    
    "beast_magic": {
        "name": "Beast Magic",
        "cost": "* to ***",
        "description": "Select werebeasts pursue forbidden arts of magic. These formidable creatures employ arcane secrets and ominous tools to mimic the spells of human wizards.",
        "system": "Can purchase specific mage spells (not Arcana). Each spell is separate Aspect. Roll Wits + Occult to cast, spend 1 Essence. Cannot buy spell with more dots than Occult Skill. Cannot combine spells or have more than one operating at once. Maximum spell level: •••. Cannot have Feral Heart higher than 3. Cannot select Spirit Gifts Aspect. Cost: • = 5 XP, •• = 15 XP, ••• = 30 XP.",
        "forms": ["All forms"]
    },
    
    "beast_surge": {
        "name": "Beast Surge",
        "cost": "***",
        "description": "By staring into another shapeshifter's eyes, the werebeast with this trick can try to 'surge the beast' and drive the other feral into one of his animal forms.",
        "system": "Staring contest: contested Composure + Feral Heart rolls. Each roll = 30 seconds. Lasts until challenger backs down or defender shifts to Primal form. Each can spend Willpower to keep going. If defender loses, transforms (probably unhappily).",
        "forms": ["All forms"]
    },
    
    "birth_blessing": {
        "name": "Birth Blessing",
        "cost": "*",
        "description": "A fabled gift of magical beasts, this Aspect allows a feral to help a would-be mother (animal or human) bear healthy children.",
        "system": "Kiss mother's belly or kneel at foot of bed in animal form. Spend 1 Essence. Blessed character has extraordinarily healthy pregnancy and offspring. Child's later birth and health are plot developments.",
        "forms": ["All forms"]
    },
    
    "blank_burrow": {
        "name": "Blank Burrow",
        "cost": "••••",
        "description": "Ducking into a hole, niche or other hiding place, a trickster literally disappears from there and reappears in another niche nearby.",
        "system": "New hiding-place must be within 50 feet of original, large and dark enough to accommodate shapechanger in current form. Spend 1 Essence to 'skip' the space. Works in any shape except War-Beast. TRICKSTERS ONLY.",
        "forms": ["Man-Guise, Primal Beast, Dire Beast, Throwback"]
    },
    
    "blend_in": {
        "name": "Blend In",
        "cost": "*",
        "description": "Like a hare in winter, this character can shift her skin or fur to blend in with the dominant surroundings.",
        "system": "Gradual change (day or so): costs nothing. Almost-instant shift (1-2 turns): spend 1 Essence. Either way, adds +2 to all dice pools involving sneaking/hiding in surroundings. Free for breeds whose counterparts shift colors seasonally.",
        "forms": ["Primal Beast", "War-Beast"]
    },
    
    "brave_escape": {
        "name": "Brave Escape",
        "cost": "***",
        "description": "A common trick among foxes and hares on the run, this Aspect grants the werebeast a sudden burst of bravado. He seems to swell with power.",
        "system": "Roll Wits + Intimidation + Feral Heart, add 3 automatic successes. Next turn, double Move for each Feral Heart dot, then run away or hide. Requires no Essence. Can be performed in any shape. TRICKSTERS ONLY.",
        "forms": ["All forms"]
    },
    
    "burrowing": {
        "name": "Burrowing",
        "cost": "** or ***",
        "description": "With thick claws or teeth, this beast may dig through barriers, packing the displaced earth so tightly that it forms a tunnel around her as she goes.",
        "system": "Two-dot: burrow at half Move through soft earth, quarter Move through thick/difficult terrain. Three-dot: can burrow through stone (at half Move) and metal (1 Structure point per turn). No Defense while digging. Cannot be used in Man-Guise. Throwback form: 2 (soft) or 1 (difficult) per turn, inflicts 1 bashing damage per turn.",
        "forms": ["Primal Beast", "War-Beast", "limited Throwback"]
    },
    
    # C
    "carnivore_puissance": {
        "name": "Carnivore's Puissance",
        "cost": "**",
        "description": "In the World of Darkness, many ancient myths are grounded in brutal truth. This Aspect allows a werebeast to regain Essence by devouring hearts.",
        "system": "Essence regained = half of prey's Size (round up). Dog's heart = 2 Essence, bear's heart = 4 Essence. Heart must be eaten raw and fresh. No benefit from consuming shapechanger hearts. Devouring human or 'own kind' heart is Harmony violation. Once per game session.",
        "forms": ["All forms"]
    },
    
    "catwalk": {
        "name": "Catwalk",
        "cost": "* to *****",
        "description": "Padding softly on bare feet, the feral moves with hardly a sound.",
        "system": "Add +1 per dot to stealth and balance dice pools while moving on feet (not climbing/swinging/swimming). Always on, costs no Essence, works in any form. In human form, provides animal-like toughness to soles.",
        "forms": ["All forms"]
    },
    
    "clamber": {
        "name": "Clamber",
        "cost": "* to *****",
        "description": "Like a monkey, this character climbs and clambers about with surety and grace.",
        "system": "Add +1 per dot to climbing, grasping and swinging dice pools. Always on, costs no Essence, works in any form. Must have strong, flexible fingers, toes and possibly tail. Beasts with hooves or 'walking paws' cannot learn this (talons okay if they can grip).",
        "forms": ["All forms"]
    },
    
    "clever_monkey": {
        "name": "Clever Monkey",
        "cost": "* to *****",
        "description": "The agile mind of this shapechanger can assess a situation and fit together (literally or otherwise) the pieces involved.",
        "system": "Add +1 bonus per dot to Intelligence dice pools for solving puzzles, navigating mazes and problem-solving. Problem must have obvious 'pieces' and clear goal. Helps repair engines, master sudoku or solve logical mysteries. Works in all forms.",
        "forms": ["All forms"]
    },
    
    "culling_the_weak": {
        "name": "Culling the Weak",
        "cost": "**",
        "description": "Carnivorous beasts fill their bellies by picking off the weak and infirm when stalking prey. A shapeshifter with this Aspect is able to bring that instinct to bear in her own life.",
        "system": "Spend 1 Essence, roll Wits + Empathy. Can assess one group at a time to determine weakest character. Exceptional success may detect illnesses (not diagnose). Successful Strength + Subterfuge roll allows healthy character to feign weakness.",
        "forms": ["All forms"]
    },
    
    # D
    "durga_blessing": {
        "name": "Durga's Blessing",
        "cost": "** or ***",
        "description": "When the goddess Durga rode into battle on her tiger, she conferred her immortal ferocity upon his descendants. This Aspect lets a character heal aggravated damage to himself.",
        "system": "For 1 Essence, regenerate 1 Health point lost to aggravated damage. If can spend more than 1 Essence per turn, may do so. Healing limited by Feral Heart dots; points healed in one battle cannot exceed Feral Heart. Bashing/lethal unaffected. Weretigers pay 2 dots, all others pay 3 dots. Manifests as bright orange glow around wounds.",
        "forms": ["All forms"]
    },
    
    # E
    "earthbond": {
        "name": "Earthbond",
        "cost": "**",
        "description": "Animals are extremely attuned to their surroundings. This Aspect allows a feral to be even more attuned than usual.",
        "system": "Half action to scan surroundings, Wits + Composure roll to spot threats/trespassers/meals within 500 feet. Natural surroundings: +3 bonus. Urban: +2 bonus. Known territory: additional +1. Maximum bonus/penalty: +5/-5. Works in any form, costs no Essence.",
        "forms": ["All forms"]
    },
    
    "exoskeleton": {
        "name": "Exoskeleton",
        "cost": "**",
        "description": "Bugs crunch when you step on them because they wear their skeletons on the outside. A character can cause his skin to harden with a waxy, brown residue.",
        "system": "Spend 1 Essence. Gain additional armor 1/1. Lowers Defense and Speed by -1 each. Lasts one scene. Stacks with natural armor of hybrid form. Available in any form. Looks and feels utterly disgusting.",
        "forms": ["All forms"]
    },
    
    "extraordinary_specimen": {
        "name": "Extraordinary Specimen",
        "cost": "*",
        "description": "A feral with this Aspect embodies her totem animal: one of the biggest and strongest representatives of her race.",
        "system": "Primal form (and Dire form if has one) increases Strength and Size by 1.",
        "forms": ["Primal Beast", "Dire Beast"]
    },
    
    # F
    "foretelling": {
        "name": "Foretelling",
        "cost": "**",
        "description": "Looking into a possible future, this creature receives visions of what might transpire. These visions are vague and unreliable, but somewhat accurate regardless.",
        "system": "Storyteller describes vivid impressions connected with character/setting/event. Storyteller secretly rolls Wits + Empathy + Feral Heart to determine accuracy (more successes = more accurate). This is free, reflexive action. Storyteller not obligated to reveal accuracy or make Foretelling come true literally. Prophecy is uncertain, open to interpretation.",
        "forms": ["All forms"]
    },
    
    "fortune_favor": {
        "name": "Fortune's Favor",
        "cost": "** or ***",
        "description": "A famous boon for hares and crows, this Aspect confers good luck.",
        "system": "Feral concentrates on person/animal and wishes them well. Spend 1 Willpower to make something good happen for favored character (Storyteller's choice): winning lottery ticket, bank error in favor, new job/promotion, or +4 bonus to critical roll. Two-dot: only on another character. Three-dot: can use on self. Player has no influence over stroke of luck.",
        "forms": ["All forms"]
    },
    
    # G
    "grave_misfortune": {
        "name": "Grave Misfortune",
        "cost": "**",
        "description": "A reversal of Fortune's Favor, this Aspect lets the werebeast grant bad luck instead.",
        "system": "Same mechanics as Fortune's Favor, except bestows bad luck. Werebeast experiences smaller yet significant bad luck as well. Examples: expensive bank error, police visit, -4 penalty to important roll.",
        "forms": ["All forms"]
    },
    
    "gross_eater": {
        "name": "Gross Eater",
        "cost": "• or ••",
        "description": "This character will never starve to death. She can eat anything organic, living or dead.",
        "system": "One-dot: can eat anything organic (from shrieking rodent to bio-hazardous waste to corpses to fecal matter) and gain normal nourishment. Two-dot: can derive sustenance from inorganic matter (doesn't protect from damage eating such stuff may cause—eating beer bottles prevents starvation but causes digestive trauma).",
        "forms": ["All forms"]
    },
    
    # H
    "hare_heart": {
        "name": "Hare Heart",
        "cost": "-*",
        "description": "Timid or easily upset, this character risks going Berserk under stress.",
        "system": "When rolling Resolve + Composure to avoid Berserk fit, reduce dice pool by -1. Far more likely to rabbit run than fly into tiger storm. To stand and fight, must spend 1 Willpower to enter tiger storm. (See also Tiger Heart Aspect.)",
        "forms": ["All forms"]
    },
    
    "hound_honor": {
        "name": "Hound's Honor",
        "cost": "* to *****",
        "description": "Many animals have incredibly fine senses of smell. With this Aspect, the werebeast (who may or may not be canine) can identify, recognize or track a particular scent.",
        "system": "Add +1 per dot to perception, tracking or identification dice pools where character follows his nose. Strong odors, pollution, smoke or perfume negate bonus and may cause nausea.",
        "forms": ["All forms"]
    },
    
    "hybrid_forms": {
        "name": "Hybrid Forms",
        "cost": "••••",
        "description": "Most ferals have only three shapes: Man-Guise, War-Beast and Primal Beast. This Aspect grants two additional forms: the Throwback and the Dire Beast.",
        "system": "Grants access to Throwback and Dire Beast forms. See 'Hybrid Forms' for details about these manifestations.",
        "forms": ["Grants new forms"]
    },
    
    "hypnotic_allure": {
        "name": "Hypnotic Allure",
        "cost": "***",
        "description": "Some people can captivate crowds with the strength of their personalities, physical magnetism or simply the fluid motions of their bodies or minds.",
        "system": "Roll Presence + Persuasion. Storyteller counters with Resolve + Composure (for crowd, use highest in group or overall impression). If character wins, all Social rolls to sway affected people get bonus equal to successes. Range: yards equal to Feral Heart. Lasts one full scene, cannot be turned off. Affects supernatural beings (use Composure + appropriate trait).",
        "forms": ["Man-Guise"]
    },
    
    # I
    "invisible_marking": {
        "name": "Invisible Marking",
        "cost": "*",
        "description": "Many animals mark their territory or the places they've been, whether with urine, musk or pheromone trails. A character with this Aspect can also mark places with a mystical connection.",
        "system": "Press fingers or rub cheek against surface, leaving almost undetectable excretion. Only members of shapechanger's breed/band can detect (Wits + Survival roll). Can leave simple mark (presence) or customize with single word/name. Reflexive action, costs no Essence.",
        "forms": ["All forms"]
    },
    
    # K
    "keen_sense": {
        "name": "Keen Sense",
        "cost": "• or ••",
        "description": "Animals live and die by their senses. With this Aspect, a single sense becomes incredibly acute.",
        "system": "One-dot: +2 bonus to reflexive perception rolls (Wits + Composure only). Two-dot: that advantage PLUS ignore up to 3 dice of distance-related penalties (sight, smell, hearing only). Always active, costs no Essence. Must be bought separately for each sense (sight, hearing, smell, taste, touch, energy awareness).",
        "forms": ["All forms"]
    },
    
    # L
    "leap": {
        "name": "Leap",
        "cost": "* to ***",
        "description": "Certain animals can leap great distances. This Aspect allows a character to double, triple or quadruple her usual jumping distance.",
        "system": "One dot: double jumping distance. Two dots: triple distance. Three dots: quadruple distance. In human form, leaping distance becomes half beast-form distance. See 'Jumping' in WoD Rulebook for details.",
        "forms": ["All forms, half distance in Man-Guise"]
    },
    
    "long_life": {
        "name": "Long Life",
        "cost": "• or ••",
        "description": "Like Old Man Possum, this character should enjoy an especially long lifespan.",
        "system": "One-dot: adds 50% to feral's usual lifespan (~40 years for most people). Two-dot: effectively doubles natural lifespan... assuming nobody cuts it short.",
        "forms": ["All forms"]
    },
    
    # M
    "magnificence": {
        "name": "Magnificence",
        "cost": "**",
        "description": "A staggering example of his breed, this feral seems more like a totem spirit than an actual beast. His fur or scales shine, his eyes glow; an aura of sublime presence surrounds him at all times.",
        "system": "Add +4 bonus to Social rolls where werebeast makes powerful impression—only when in animal shapes. People and animals instinctively revere character.",
        "forms": ["Primal Beast", "War-Beast", "Dire Beast"]
    },
    
    "mercy_touch": {
        "name": "Mercy's Touch",
        "cost": "***",
        "description": "Although mercy is in short supply in the feral world, certain animals are renowned for healing powers. With this Aspect, a feral licks, lays paw upon or wraps himself around a sick or wounded friend.",
        "system": "Spend 1 Essence, roll Composure + Medicine. Result = Health points restored from lethal damage, healed at 1 point per 5 minutes of uninterrupted consolation. Does nothing for bashing/aggravated. Can heal poison/disease damage if takes twice usual time. Works in all forms. Can heal only as many Health points as Feral Heart dots.",
        "forms": ["All forms"]
    },
    
    "mimic": {
        "name": "Mimic",
        "cost": "• or •••",
        "description": "Nature's imposters can impersonate another creature's voice, coloration or scent. Using this trick, a feral can do the same.",
        "system": "One-dot: mimic single element (appearance, sound OR scent). Two dots: two elements. Three dots: all three. Roll Wits + Animal Ken + Feral Heart to succeed. Can mimic human (specific impersonation requires additional Wits + Subterfuge + Feral Heart roll). Lasts 2 turns per Feral Heart dot. To uncover: contested Wits + Subterfuge (good light gives +3 to spot appearance). Works in any form for sounds/scents. Cannot dramatically change appearance (hyena could pass for dog, but not person/bird/lizard).",
        "forms": ["Varies"]
    },
    
    "mindmap": {
        "name": "Mindmap",
        "cost": "***",
        "description": "This feral is never truly lost. No matter where she is, she can find familiar ground eventually.",
        "system": "Can find way home from anywhere eventually. To speed process: roll Intelligence + Composure + Feral Heart (more successes = quicker path). Could take hours or days if lost in Outback/Amazon. As long as able to follow instincts, will always find way home.",
        "forms": ["All forms"]
    },
    
    "mindspeech": {
        "name": "Mindspeech",
        "cost": "**",
        "description": "Reaching across space and language, a feral with this Aspect can 'talk' and 'listen' without saying or hearing a word. An instinctive telepathy allows him to speak within a single character's head.",
        "system": "Reflexive, costs no Essence, works in any form. Must make eye contact to begin. Retain only within 100 feet. Grants +2 bonus to Empathy rolls. Speech is as intelligible as if speaking aloud (language barriers still apply).",
        "forms": ["All forms"]
    },
    
    "mother_fury": {
        "name": "Mother's Fury",
        "cost": "* to *****",
        "description": "Nothing is more dangerous than a mother bear defending her cubs. This Aspect channels that ferocity to defend a feral's kin or other innocents.",
        "system": "Add +1 per dot to hand-to-hand dice pools when defending character's family, lover or children in general. Lasts 1 turn per Feral Heart dot. Character need not be female/mother. Defended character must be helpless against attack, cannot be another werebeast/supernatural (unless character's own child).",
        "forms": ["All forms"]
    },
    
    # N
    "nine_lives": {
        "name": "Nine Lives",
        "cost": "*****",
        "description": "With this Aspect, a character can survive death. When the shapechanger receives an aggravated level of damage in her last Health box and would normally die, she dies... but only briefly.",
        "system": "Death duration: 10 - Harmony = hours dead. Costs 1 Feral Heart dot to resurrect. If only had 1 Feral Heart at death, resurrection impossible. First resurrection: no roll needed. Each after: Resolve + Composure with cumulative -1 penalty. Body has Structure = Stamina in human form. Damage to Structure prevents resurrection. Upon resurrection, aggravated becomes lethal, begins healing normally.",
        "forms": ["All forms"]
    },
    
    # P
    "pack_bond": {
        "name": "Pack Bond",
        "cost": "***",
        "description": "Many creatures move and think as though they're a single unit when gathered in a group. This Aspect provides bonuses shared by all members of a particular feral species or their intimate companions.",
        "system": "Can transfer 1 Essence or 1 Willpower as reflexive action to another of same species (line of sight required, common band required). Only 1 point per turn. Empathic communication for 10 seconds (both within 1 mile, previous contact required, costs 1 Willpower from both). Distress signal to all same species within 10 miles (cannot pick recipients, costs 1 Willpower, reveals precise location, continues until shut off or death).",
        "forms": ["All forms"]
    },
    
    "partial_change": {
        "name": "Partial Change",
        "cost": "**",
        "description": "If you can shapechange, it's often helpful to change a small portion of your shape rather than your entire body. This trick lets a feral adjust a single feature of her current form into a single feature from one of her other shapes.",
        "system": "Roll Stamina + Survival + Feral Heart (success = change for scene, change back requires another roll). OR spend 1 Essence and transform automatically (each shift requires 1 Essence). Failed roll changes wrong body part. Really weird sight (Delusion for humans, animals freak out). Common for tricksters/predators.",
        "forms": ["All forms"]
    },
    
    "pearl_of_great_price": {
        "name": "Pearl of Great Price",
        "cost": "**",
        "description": "The classic bait-and-switch trick has a con artist swapping worthless junk for an apparently precious item. This trick does the same thing, projecting an illusion of value onto something worth nothing at all.",
        "system": "Roll Intelligence + Subterfuge + Feral Heart to instill 'pearl' with illusionary value. Then roll or roleplay the con. Mark makes contested Intelligence + Subterfuge (+ Feral Heart if supernatural). If mark loses, utterly convinced pearl is what trickster says. Enchantment wears off in ~1 hour. TRICKSTERS ONLY.",
        "forms": ["All forms"]
    },
    
    "piggyback_passenger": {
        "name": "Piggyback Passenger",
        "cost": "***",
        "description": "Some shapechangers are able to tap into their connection with the animal world a little more deeply than most. Can sense presence of every animal of less-than-human intelligence within a square mile (excludes insects).",
        "system": "Spend 1 Willpower to piggyback on senses of any bird/mammal within range (fish requires 1 Willpower + 1 Essence). Experience everything animal does (pain, fear, instinctive impulses). Cannot control animal. Lasts 1 hour, can tune out anytime.",
        "forms": ["All forms"]
    },
    
    # R
    "resilient_form": {
        "name": "Resilient Form",
        "cost": "*+",
        "description": "Shapeshifters whose beast-forms are small and fragile (birds, rats, lizards) may take this Aspect to toughen themselves up while in animal form.",
        "system": "Each point adds 1 Health while in animal shapes (Primal, Dire, War-Beast), up to maximum of human Health trait. Useless to characters with higher animal-form Health ratings.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "righting_reflex": {
        "name": "Righting Reflex",
        "cost": "* to ***",
        "description": "A common belief states that a falling cat always lands on his feet. This trick reflects that talent.",
        "system": "One-dot: halve fall damage (round up), even at terminal velocity. Two-dot: same PLUS +2 to Defense while in Primal/Dire form. Three-dot: can use trick in human form as well. Reflects natural grace and balance of cats. Equally graceful creatures allowed. Bulky creatures cannot employ (no matter how clever, bull falls like bull).",
        "forms": ["Varies by dots"]
    },
    
    # S
    "sense_of_familiarity": {
        "name": "Sense of Familiarity",
        "cost": "**",
        "description": "By employing this trick—an extension of the Delusion—a feral can engage in strange, even supernatural, activity without drawing unwanted attention. Potential witnesses either don't notice or convince themselves it fits the natural order.",
        "system": "Running around in animal form: roll Wits + Subterfuge - bystander's Resolve. Success = nobody detects anything strange. Overtly supernatural actions: same roll - highest Resolve. Success = feral doesn't provoke strong/fearful reaction (may become dreamlike fascination or rationalized). Must activate (not reflexive). If presence damages environment (rhino in mall): spend 1 Essence. Stealthy beast (crow, cat): no Essence cost. Violent/extreme actions cannot be obscured. Gift for tricksters, not cloak for murderers.",
        "forms": ["Primal Beast", "Dire Beast", "War-Beast"]
    },
    
    "sexual_dimorphism": {
        "name": "Sexual Dimorphism",
        "cost": "**",
        "description": "This Aspect reflects the way some animals use physical appearance to successfully attract mating partners. A character with Sexual Dimorphism retains some of those traits in all forms.",
        "system": "Character gains +2 to any Social roll when dealing with opposite sex... including Intimidation rolls. Examples: bird with extravagant plumage takes particular care in dress/appearance in human form; another may like to sing, preen or display physical prowess.",
        "forms": ["All forms"]
    },
    
    "shadow_bond": {
        "name": "Shadow Bond",
        "cost": "***",
        "description": "Most ferals, unlike their cousins the Uratha, are creatures of this world. Most... but not all. This Aspect allows a werebeast to cross through the spiritual Gauntlet, reaching the Shadow.",
        "system": "Must be at spiritual locus. Enter trance or gaze into reflective surface, fade to Shadow in ~30 seconds. Roll Intelligence + Presence + Feral Heart. Spend 1 Essence = instant trip; otherwise 10 turns. During crossing, immune to attacks from either side. Modifiers: dense urban -3, suburb/town -2, small town/village -1, wilderness +0, daylight -2, ••-••• locus +1, ••••+ locus +2, reflective surface +1. Smells odd to other ferals afterward.",
        "forms": ["All forms"]
    },
    
    "skin_double": {
        "name": "Skin Double",
        "cost": "••••",
        "description": "An infamous trick among hyenas, cats and foxes, this dreadful gift allows a shapechanger to kill a person and assume his identity. First, the feral stalks and downs her prey, harming his skin as little as possible. Using terrible rites, she skins the body (sometimes while victim still lives), then prepares the hide with her own blood, urine, tears, saliva and sweat.",
        "system": "Donning skin becomes almost-perfect likeness. Probably Harmony violation. Spend 1 Essence to adopt persona. Spend another each time removing/replacing skin (2 points per shift) to maintain charade even with physical differences. All disguise rolls receive 4 bonus successes. Some flaw reveals animal nature (paw foot, eye sheen, tendency to eat raw meat). Perception roll may notice something wrong. Eerie and powerful. Should never displace/impersonate player characters (except with player's covert agreement for fun roleplay).",
        "forms": ["All forms"]
    },
    
    "slumber_touch": {
        "name": "Slumber's Touch",
        "cost": "***",
        "description": "A favorite trickster secret, this power lets the shapechanger put people to sleep.",
        "system": "Spend 1 Essence, roll Resolve + Stamina + Feral Heart. Send 1 character to sleep per success. All targets must be within ~100 feet of each other and within 300 feet of werebeast. If targets inclined to sleep anyway, automatic. To resist: contested Resolve + Stamina (+ mystical Resistance if night-folk). Sleep is natural, lasts ~1 hour, characters awaken refreshed.",
        "forms": ["All forms"]
    },
    
    "snatch_and_carry": {
        "name": "Snatch and Carry",
        "cost": "**",
        "description": "Normally, a feral in beast-form has to leave her human possessions behind. This trick lets her take a single item along for the run.",
        "system": "Item must be 'prepared' in advance (with blood/urine/saliva) at cost of 1 Essence. Hold in hand or wear while transforming. Item blends with body, reappears when return to that form.",
        "forms": ["All forms"]
    },
    
    "spinebite": {
        "name": "Spinebite",
        "cost": "*****",
        "description": "Cats are brutally efficient killers—among the best in the natural world. When going for the kill, cats often go for the neck in an effort to sever the spinal cord or tear out the windpipe.",
        "system": "Spend 1 Willpower, make attack roll at target's exposed neck (suffer -3 dice penalty for targeted attack). Success = all damage to neck is aggravated. Neck torn open, arteries likely cut. Powerful, nasty attack. Once per scene. Must have long sharp claws, teeth or talons.",
        "forms": ["Primal Beast", "War-Beast"]
    },
    
    "spirit_animal": {
        "name": "Spirit Animal",
        "cost": "*+",
        "description": "Sometimes a shapeshifter attracts the favor of an animal or spirit outside her Nahual breed. The secondary animal confers its favor to the shapechanger in the form of dice added to a single Skill.",
        "system": "Favored Skill chosen when purchased, must reflect aspect of animal's nature (salamander might add to Athletics when climbing/swimming). Must call upon spirit animal's favor: spend 1 Essence to gain bonus to that Skill for one scene. Each dot = +1 bonus to dice pool. Each animal kingdom/type counts as separate Aspect.",
        "forms": ["All forms"]
    },
    
    "spirit_gift": {
        "name": "Spirit Gift",
        "cost": "*+",
        "description": "Feral werebeasts are creatures of the mortal realm; even so, a handful of them (usually Wind-Dancers or other mystics) interact with the spirits of Nature. At times, these entities offer Gifts, arcane blessings that confer otherworldly powers.",
        "system": "Can select Gifts from Werewolf: The Forsaken, provided character has at least 1 dot in Language (First Tongue) and working relationship with spirit realm. Each dot purchases single Gift of that rating; Gifts over ••• cost 2 dots each. Cannot purchase if have Beast Magic Aspect. Spirits are jealous.",
        "forms": ["All forms"]
    },
    
    "spirit_secrets": {
        "name": "Spirit Secrets",
        "cost": "***",
        "description": "Some tricksters can mimic the power of spirit powers—in game terms, Numina. Crows, spiders and hares love to steal such secrets; several creation myths are based on such thefts in ancient times.",
        "system": "Must find, stalk and trick spirit into giving up secret. Pay Willpower or Essence cost as Numen would, make Wits + Intelligence roll to understand trick. Not all Numina make sense for shapechanger (Storyteller discretion). Possibilities: Animal Control, Blast (elemental surge), Harrow, Gauntlet Breach, Materialize (conjure spirits), Phantasm, Terrify, Wilds Sense. Each Numen costs 3 Aspect dots.",
        "forms": ["All forms"]
    },
    
    "spirit_sight": {
        "name": "Spirit Sight",
        "cost": "**",
        "description": "Tradition holds that certain animals—often crows, larks, hares and horses—guard the passage to the Otherworld. Wind-Dancer mystics continue that tradition.",
        "system": "Roll Intelligence + Occult + Feral Heart. Success = spot area of spiritual power or disturbance (generally ghosts, although malignant spirits may be involved). Can peer past Gauntlet and recognize heart of matter. Circumstances modify roll per Shadow Bond Aspect chart.",
        "forms": ["All forms"]
    },
    
    "spook_the_herd": {
        "name": "Spook the Herd",
        "cost": "***",
        "description": "A beast using this Aspect moves people the way a bulldozer moves earth. With a series of aggressive movements, he can drive crowds before him in a frenzy of terror.",
        "system": "Roll Presence + Intimidation vs. highest Composure within 100 yards. Success = crowd flees, using any means necessary. Flee for turns equal to beast's Strength + Intimidation. Night-folk and shapechangers not immune; supernatural creatures use Composure + appropriate Resistance trait.",
        "forms": ["All forms"]
    },
    
    "stampede_rush": {
        "name": "Stampede Rush",
        "cost": "** or ***",
        "description": "Bulls and elk appear to be massive, unwieldy creatures. However, they're capable of sudden, astonishing bursts of devastating speed.",
        "system": "Two-dot: all-out attack gains +4 bonus instead of usual +2. Three-dot: gains +6. Against objects (doors/walls): Strength + Stamina roll gains +1 bonus (2-dot) or +3 bonus (3-dot). Lose Defense for duration of turn. Two-dot costs nothing, three-dot costs 1 Essence per attack. Must be in animal form with hooves, horns, antlers or very thick skull.",
        "forms": ["Primal Beast", "War-Beast"]
    },
    
    "stash": {
        "name": "Stash",
        "cost": "* to *****",
        "description": "Whether she's a squirrel stashing nuts or a dog hiding a bone, the average animal has a gift for hiding things.",
        "system": "Add +1 per dot to dice pools when hiding something (including herself). Hidden item/person must remain silent and motionless, reasonable hiding place must exist. Generally works for objects Size 5 or smaller (hard to hide car unless in parking lot). Given enough space and cover, bonus still applies.",
        "forms": ["All forms"]
    },
    
    "swarm_flock_form": {
        "name": "Swarm/Flock Form",
        "cost": "••••",
        "description": "In a hideous spill of legs and bodies, the feral breaks apart into dozens or hundreds of tiny bats, rats or, worst of all, insects... The swarm shares a hive mind and common Health trait.",
        "system": "Requires Composure + Feral Heart roll. Almost instantaneous. Costs 1 Essence to scatter, another to re-form. If too little Essence left, trapped in scattered state. No defense against mental/spiritual assaults. Normal humans/animals suffer Delusion with -2 penalty. Supernatural characters roll Composure + mystical defense or get rattled (cannot act until after next turn). Familiarity breeds contempt—startling power works only once on given victim. Attack hitting most/all creatures affects feral normally. Almost impossible to hit all at once without explosion/flood/collapse.",
        "forms": ["Primal Beast"]
    },
    
    "sweet_voiced_fiend": {
        "name": "Sweet-Voiced Fiend",
        "cost": "*",
        "description": "This shapechanger is as dangerous with his words as he is with his claws. He always thinks of just the right thing to say, and his voice goes down like wine.",
        "system": "Reduce any penalties with Persuasion and Subterfuge attempts, as well as appropriate Expression rolls, by -2. Doesn't add anything extra, but helps compensate for ferocious disposition.",
        "forms": ["All forms"]
    },
    
    "swift_wing": {
        "name": "Swift Wing",
        "cost": "***",
        "description": "At the cost of one Willpower point, a winged shapechanger can move at up to three times her normal speed when making a Brawl or Weaponry attack from the air.",
        "system": "Spend 1 Willpower. Move up to 3x normal speed when making Brawl/Weaponry attack from air (see 'Charging'). Can still apply single die of Defense against first incoming attack. Reflects devastating speed predatory birds bring to attack as they drop like missiles from sky.",
        "forms": ["Primal Beast with wings", "War-Beast with wings"]
    },
    
    # T
    "tar_baby": {
        "name": "Tar Baby",
        "cost": "***",
        "description": "With a few found objects, a bit of sticky stuff and a heart full of spite, the trickster whips up a semi-convincing simulacrum of a person or animal.",
        "system": "Requires Wits + Crafts + Feral Heart roll, 1 Essence, 5+ minutes with materials. Exhale breath into face, leave scene. 'Tar baby' passes for living thing in dim light. Cannot move, but exudes faint aura of mockery. Decoy captures attention. Aura goads mock-ee: roll Wits + Composure at -2. Failure = state of agitation bordering on fury. Each failure requires another roll at increasing penalty, drives character deeper into apoplexy. By third attempt, notices only tar baby. If victim strikes it, collapses into vile goo (psychic embodiment of toxic thoughts). Must construct in Man-Guise or Throwback (need hands with jointed fingers). Lasts ~1 day, then degenerates. TRICKSTERS ONLY.",
        "forms": ["Man-Guise", "Throwback"]
    },
    
    "tell": {
        "name": "Tell",
        "cost": "-*",
        "description": "A tell is an identifying characteristic—physical or psychological—that betrays a feral's identity to anyone perceptive enough to pick up on it.",
        "system": "Could be lazy eye manifesting in all forms, tendency to sneeze when nervous, heavy musk or stink of offal. Character meeting werebeast for first time gets reflexive Wits + Composure roll (-2 dice). Success = notices characteristic. If meets again in altered form, another roll to notice tell. Second success = may make connection. Failed second roll allowed again if someone calls attention to it. Tell is immediate perception, doesn't linger after shapechanger gone.",
        "forms": ["All forms"]
    },
    
    "territory_bond": {
        "name": "Territory Bond",
        "cost": "*** to *****",
        "description": "A wise beast knows her territory. With this Aspect, a werebeast becomes so attuned to her homelands that she can literally move her world.",
        "system": "Three-dot: intuitive sense of home (recognize by scent/taste, find way back from great distance, sense when something wrong if within 100 miles—Wits + Composure + Feral Heart). Reflexive, costs no Essence. Four-dot: spy on domain. Within 10 miles, spend 1 Willpower, roll Wits + Composure + Feral Heart for flashes of information. Five-dot: turn land to purpose. Spend 2 Willpower, usual roll, alter landscape (mists rise, sounds echo, trails disappear/shift, winds/weather shift, roots trip, etc.). Contested roll vs. trespasser's Wits + Composure + Survival to determine if invaders lost.",
        "forms": ["All forms"]
    },
    
    "tiger_heart": {
        "name": "Tiger Heart",
        "cost": "*",
        "description": "When this feral goes Berserk, people die. A player who rolls this character's Resolve + Composure to avoid a Berserk fit first reduces his dice pool by –1.",
        "system": "Reduce dice pool by -1 when rolling Resolve + Composure to avoid Berserk fit. Won't rabbit run unless about to die (maybe not even then). To run away before that point, must spend 1 Willpower to overcome urge to kill. (See also Hare Heart Aspect.)",
        "forms": ["All forms"]
    },
    
    "totem_guardian": {
        "name": "Totem Guardian",
        "cost": "**+",
        "description": "Most ferals view their Nahual as their inner totem spirit. Some, however, look outside as well as inside for spiritual guidance. This Aspect allows a werebeast (and perhaps her band) to bond with a spirit-beast totem.",
        "system": "Non-Uratha shapechangers can purchase Totem Merit from Werewolf: The Forsaken. Point cost is DOUBLE werewolf cost (each dot costs 2 points rather than 1). Totem spirit rarely materializes. May teach new Aspects, relay knowledge. Always chooses its followers (never other way around). May chase through dreams, appear in vision quest, manifest as real animal. Must match animal half of shapechanger (werebear with grizzly/polar bear). Usually has proper name providing clue about personality.",
        "forms": ["All forms"]
    },
    
    "toss_the_scent": {
        "name": "Toss the Scent",
        "cost": "*",
        "description": "This simple yet effective trick casts the feral's innate scent in another direction, thus throwing a hunter off her trail.",
        "system": "Roll Wits + Subterfuge + Feral Heart. Result = distance in yards scent travels away from feral. Crafty trickster can set scent on another character. By time pursuer and new 'target' hash things out, trickster long gone. TRICKSTERS ONLY.",
        "forms": ["All forms"]
    },
    
    "truth_sense": {
        "name": "Truth Sense",
        "cost": "* to *****",
        "description": "With a profoundly disconcerting gaze, some werebeasts can look directly at (or worse, utterly away from) a person and discern the truth in his words or intentions.",
        "system": "Add +1 bonus per dot to dice pools when trying to catch lie, spot con, debunk tall tale or look through illusion in immediate vicinity (~200 feet). Works only in direct personal contact. To spot lie in pre-recorded conversations/video feeds, bonus is only +1 unless watches repeatedly (then half usual benefit).",
        "forms": ["All forms"]
    },
    
    "twisted_tongue": {
        "name": "Twisted Tongue",
        "cost": "*",
        "description": "Truly ambitious shapechangers may feel that the inability to speak while in animal form is too limiting. This Aspect affords the ability to speak in animal form any language they know in human form.",
        "system": "Can speak in animal form any language known in human form. Only basic speech possible (animals don't have words for complex/uniquely human concepts like 'accelerator'). Animal language remains bound by species' perspective on reality (bird may have many words for 'high' but none for 'deep').",
        "forms": ["Primal Beast", "War-Beast", "Dire Beast"]
    },
    
    # U
    "unnerving_cry": {
        "name": "Unnerving Cry",
        "cost": "**",
        "description": "A wolf's howl carries across the city, echoing through the alleyways and shredding itself over the fire escapes and streetlamps. Everyone who hears it falters in their tracks.",
        "system": "Spend 1 Willpower, roll Presence + Feral Heart (instant action). Anyone within 200 yards must resist with Resolve roll (supernatural creatures add Feral Heart or appropriate resistance). Failure = victim's next action suffers -2 dice penalty. Exceptional success increases penalty to -4 dice.",
        "forms": ["All forms"]
    },
    
    "unsettling_eye": {
        "name": "Unsettling Eye",
        "cost": "*",
        "description": "Characters with Unsettling Eye can use this Aspect reflexively whenever the player makes an Intimidation roll. The character looks into his opponent's soul with the full strength of his inner beast.",
        "system": "Reflexive whenever making Intimidation roll. Effectively doubles character's Intimidation dice pool. Activation free. Lasts only one scene. Opponent has subconscious vision of being stared down by spider, wolf, shark or other terror.",
        "forms": ["All forms"]
    },
    
    "unspeakable": {
        "name": "Unspeakable",
        "cost": "••• or •••••",
        "description": "Hideous beyond description, this creature drives people screaming with her mere presence. She might be a shambling twisted mockery of a beast, or an animal so ferocious that even the most strong-hearted mortals flee.",
        "system": "Three-dot: add 1 automatic success to intimidate/frighten attempts, lower Delusion resistance dice pool by -1. Five-dot: add 2 automatic successes, lower Delusion pool by -2. Applies only to War and animal forms (probably no beauty queen in human form either).",
        "forms": ["Primal Beast", "War-Beast", "Dire Beast"]
    },
    
    # V
    "venomous": {
        "name": "Venomous",
        "cost": "*** or ****",
        "description": "This deadly talent makes a feral's claws, fangs, spines or stinger venomous for a brief period of time. The effects on the victim can range from a burning itch to convulsions and death.",
        "system": "Player must decide which attack (fangs OR claws) carries venom when selecting Aspect (may buy twice for both). Three-dot: spend 1 Essence (reflexive), gain advantage for 1 turn. Toxicity 5, effects delivered as lethal damage on top of attack successes. Attack roll must succeed for venom to work. Venom remains in bloodstream for hours equal to Feral Heart. Effects persist hourly unless victim succeeds at Stamina + Resolve roll. Four-dot: damage done only once (no hourly recurrence), damage is aggravated rather than lethal.",
        "forms": ["Primal Beast", "War-Beast"]
    },
    
    # W
    "wallwalking": {
        "name": "Wallwalking",
        "cost": "**",
        "description": "With hooked toes or sticky pads, a feral with this Aspect can walk up and across sheer surfaces.",
        "system": "Add +2 bonus to climbing dice pools. Allows character to hang on to surfaces too steep or smooth to climb. Always on, costs no Essence, can be used in any form.",
        "forms": ["All forms"]
    },
    
    "war_heart": {
        "name": "War Heart",
        "cost": "*****",
        "description": "This shapeshifter is in his natural element when in battle. The anger he carries around inside him flourishes in combat.",
        "system": "Actually gains strength from damage received. For every point of lethal damage character takes in one turn, gains +1 Strength the following turn (max +5). After that turn, Strength point is lost. Speed trait affected accordingly. Always activated, Strength gain is reflexive. Does not protect from damage, regenerates as normal. Natural for Heart-Rippers.",
        "forms": ["All forms"]
    },
    
    "warrior_restoration": {
        "name": "Warrior's Restoration",
        "cost": "**",
        "description": "For predatory breeds who fight a lot, or clever creatures whose recovery powers keep 'em kicking in a hostile world, this Aspect is essential.",
        "system": "Doubles usual healing rate. Heals 1 bashing damage per turn (rather than every 2 turns). Heals 1 lethal damage every 15 minutes unless Essence spent. Abilities to spend Essence and heal aggravated damage remain unaffected. Combined with Quick Healer Merit: regenerate lethal at 1 point per 8 minutes, aggravated at 1 point per 4 days.",
        "forms": ["All forms"]
    },
    
    "weatherskin": {
        "name": "Weatherskin",
        "cost": "*",
        "description": "Through acclimation, fur or sheer toughness, a feral with this Aspect resists the effects of extreme temperatures.",
        "system": "Feels weather but short of fire or ice, harsh climates do no harm. Essentially immune to debilitation through heat or cold. See 'Temperature Extremes' in WoD Rulebook for details.",
        "forms": ["All forms"]
    },
    
    "weaver_wisdom": {
        "name": "Weaver's Wisdom",
        "cost": "* to *****",
        "description": "Like a beaver with prime woodland, a shapechanger with this Aspect excels at building and designing things.",
        "system": "Add +1 bonus per dot to dice pools based on construction, craftwork or architectural design. Does not offer bonuses to advanced/abstract technology (computer networks, astrophysics, biotech). To employ Wisdom, feral must get hands dirty with something she can take apart or put together. Staple of Root-Weaver accord.",
        "forms": ["All forms"]
    },
    
    "wild_cry": {
        "name": "The Wild Cry",
        "cost": "* to *****",
        "description": "Animals don't 'speak' as humans do, but animals communicate rather eloquently. With this Aspect, a werebeast communicates with other animals in ways they understand.",
        "system": "For *: empathic bond with one animal kingdom (mammals, reptiles, insects, fish, birds). For **: communicate with one general type (cats, corvids, cattle). For ***: communicate with large numbers of those animals (herds, flocks, schools). For ****: call animals to aid (perform minor service; fighters may fight but won't fight to death). For *****: animals perform task until deed completed, feral dismisses them, or all dead (if feral attacks them, bond immediately broken). Roll Wits + Presence + Feral Heart. Each animal kingdom/type counts as separate Aspect. Number affected depends on Feral Heart rating and animal Size. Works in all forms, costs no Essence. Using to hunt food or recruit cannon fodder is Harmony violation.",
        "forms": ["All forms"]
    }
}

# Summary lists for quick reference
ALL_FAVOR_NAMES = list(CHANGING_BREED_FAVORS.keys())
ALL_ASPECT_NAMES = list(CHANGING_BREED_ASPECTS.keys())
TRICKSTER_ONLY_ASPECTS = ["blank_burrow", "brave_escape", "pearl_of_great_price", "tar_baby", "toss_the_scent"]

