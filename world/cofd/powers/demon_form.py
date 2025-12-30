"""
Demon Demonic Form Traits for Chronicles of Darkness.
Includes Modifications, Technologies, Propulsions, and Processes.

At character creation, a demon has:
- 3 Modifications
- 2 Technologies
- 1 Propulsion
- 1 Process

Demonic form traits are semantic and chosen from a list.
Modifications and some propulsions are one-time picks.
Technologies and Processes must be activated when used.
"""

# Modifications - One-time picks
DEMON_MODIFICATIONS = {
    "advanced_optics": {
        "name": "Advanced Optics",
        "appearance": "Glass lenses replace eyes.",
        "system": "Spend a turn focusing and gain a +3 equipment bonus on any rolls that would benefit from magnification (Eg, Investigation, Larceny or Science). Blind to anything not in field of view.",
        "source": "FoH 121"
    },
    "armored_plates": {
        "name": "Armored Plates",
        "appearance": "Well hinged armored plates.",
        "system": "Armor 3/2, Defense/Speed -1.",
        "source": "DTD 196"
    },
    "blade_hand": {
        "name": "Blade Hand",
        "appearance": "An integrated transforming body weapon.",
        "system": "Reflexively summon or dismiss the blade hand. 4L rating weapon, initiative penalty -3.",
        "source": "DTD 197"
    },
    "claws_and_fangs": {
        "name": "Claws and Fangs",
        "appearance": "Metal or bone claws, needles, etc.",
        "system": "2L rating weapon, no initiative penalty. Can be used to grapple.",
        "source": "DTD 197"
    },
    "component_indicators": {
        "name": "Component Indicators",
        "appearance": "Pale blue rubbery covered with pores and bumps.",
        "system": "Perform comprehensive chemical testing by touching a sample for a minute. Identify things like DNA, molecular components, etc etc. Can interpret the data if necessary with an Intelligence + Science roll.",
        "source": "FoH 122"
    },
    "detachable_limbs": {
        "name": "Detachable Limbs",
        "appearance": "Gaps between joints. Leaks oil when detached.",
        "system": "Detach any individual limb at each joint, including the torso. Each limb is under full control and can act independently. Can spend 1 Aether to instantly regrow a limb (torso counts as two) destroying the originally detached limb. Can reattach the detached limbs as an instant action, as well.",
        "source": "FoH 122"
    },
    "electrical_sight": {
        "name": "Electrical Sight",
        "appearance": "Staticky pupils.",
        "system": "See electrical signals and currents. Roll Intelligence + Composure to zero in on, interpret and eavesdrop on a given signal.",
        "source": "DTD 197"
    },
    "emp_field": {
        "name": "EMP Field",
        "appearance": "Wires and circuits and a metallic sheen.",
        "system": "Spend an instant action and one Aether to roll Intelligence + Primum. Short out and disable all electrical devices within 5 feet per success.",
        "source": "DTD 197"
    },
    "fast_attack": {
        "name": "Fast Attack",
        "appearance": "Red swirling tattoos over hands and arms.",
        "system": "+2 initiative. After successfully striking someone, as long as the demon continues to attack that person she may reset her initiative to act before her target. Initiative reverts when no longer fighting that specific person.",
        "source": "DTD 197"
    },
    "huge_size": {
        "name": "Huge Size",
        "appearance": "Huge size.",
        "system": "+4 size.",
        "source": "DTD 197"
    },
    "inhuman_intelligence": {
        "name": "Inhuman Intelligence",
        "appearance": "Visible alterations to head and cranium.",
        "system": "+2 to Intelligence rolls.",
        "source": "DTD 197"
    },
    "inhuman_strength": {
        "name": "Inhuman Strength",
        "appearance": "Bulging or unnatural steel muscles.",
        "system": "+2 to Strength rolls.",
        "source": "DTD 198"
    },
    "inhuman_reflexes": {
        "name": "Inhuman Reflexes",
        "appearance": "Mechanical hinges or actuator pistons.",
        "system": "+2 to Dexterity rolls.",
        "source": "DTD 198"
    },
    "lighting": {
        "name": "Lighting",
        "appearance": "Torches, LEDs or other sources of light in the body.",
        "system": "Eliminates any penalties from darkness when active. Can blind a target (causing Blindness tilt) as an instant action unless resisted by Wits + Composure - Primum.",
        "source": "FoH 123"
    },
    "limb_retractor": {
        "name": "Limb Retractor",
        "appearance": "Slight increase in size of withdrawn area. Missing limbs look kinda like lumps, like the navel.",
        "system": "Reflexively draw Arms, Legs or the head into the Abdomen, protecting it from outside harm. Can pull objects of Size 2 or less into the body to be hidden as well.",
        "source": "FoH 123"
    },
    "low_density": {
        "name": "Low Density",
        "appearance": "Feet look spidery or like a bundle of roots.",
        "system": "Walk on sand, snow or liquids without difficulty. Ignore \"Flooded\" and \"Ice\" tilts. May still require Dexterity + Athletics checks in very extreme conditions.",
        "source": "FoH 123"
    },
    "mental_resistance": {
        "name": "Mental Resistance",
        "appearance": "Faint blue and icy to the touch.",
        "system": "+2 to resist supernatural powers.",
        "source": "DTD 198"
    },
    "nauseating_musk": {
        "name": "Nauseating Musk",
        "appearance": "Blood-coloured sweat droplets all over skin. Odour of garbage within about 10 yards.",
        "system": "As an instant action, inflicts the \"Sick\" tilt on any creature within 10 yards which have a sense of smell.",
        "source": "FoH 123"
    },
    "night_vision": {
        "name": "Night Vision",
        "appearance": "Pupils fill with green light or fluid.",
        "system": "See in the dark as if broad daylight, and +2 to Perception rolls.",
        "source": "DTD 198"
    },
    "olfactory_enhancements": {
        "name": "Olfactory Enhancements",
        "appearance": "Instead of a nose, has a wire mesh with flashing olfactory detectors behind it.",
        "system": "+3 bonus to Wits checks that benefit from a sharp sense of smell. \"Red herring\" scents do not deceive or inconvenience. Can track a scent with a Wits + Survival roll.",
        "source": "FoH 123"
    },
    "radio_suite": {
        "name": "Radio Suite",
        "appearance": "A radio-type device is embedded into the skin, as well as aerials with the appearance of veins.",
        "system": "Mastery over radio signals. Tune in and listen to all broadcasts with perfect clarity, interrupt any radio frequency or broadcast either voice or anything the Demon can hear over the frequency.",
        "source": "FoH 124"
    },
    "resistors": {
        "name": "Resistors",
        "appearance": "Glass and ceramic resistors connected by copper wiring adorn the body.",
        "system": "Ignore the first source of damage suffered. The resistors shatter and are not restored until the Demon's health pool is completely refilled.",
        "source": "FoH 124"
    },
    "rivet_arm": {
        "name": "Rivet Arm",
        "appearance": "An entire arm becomes a large projectile tool.",
        "system": "Reflexively summon or dismiss the rivet arm. Gun rolls Wits + Firearms to attack, with a 3L damage rating, no initiative penalty, and infinite ammunition and clip size. +2 to relevant building projects.",
        "source": "DTD 198"
    },
    "sense_the_angelic": {
        "name": "Sense the Angelic",
        "appearance": "Hair-tendrils like copper wire.",
        "system": "Roll Wits + Investigation to notice the influence of an angelic Numen within the past 24 hours. If the effect has been encountered before, identify it as such.",
        "source": "DTD 198"
    },
    "slippery_body": {
        "name": "Slippery Body",
        "appearance": "Oily residue.",
        "system": "+3 to Defense against grapples. +3 to escape a grapple. Can squeeze through tight spaces as if -1 size.",
        "source": "DTD 198"
    },
    "sonic_acuity": {
        "name": "Sonic Acuity",
        "appearance": "Altered or filtered ears.",
        "system": "Hear sounds of all frequencies and volumes without disorientation or pain. Can concentrate to hear sounds through solid walls. +3 to Perception via hearing. Cannot be surprised or Deafened.",
        "source": "DTD 199"
    },
    "spurs": {
        "name": "Spurs",
        "appearance": "Spurs over the demon's ankles.",
        "system": "Climb vertical surfaces. +3 to climbing. Climb 20 feet instead of 10. 1L rating weapon, no initiative penalty.",
        "source": "DTD 199"
    },
    "steel_frame": {
        "name": "Steel Frame",
        "appearance": "Steel rivets stick out of the skin, ringing vital areas and joints.",
        "system": "The Demon's bones cannot be broken unless the source can bend steel (Durability 3, Size 0-2, Structure 3-5). Ignore \"Arm Wrack\", \"Leg Wrack\" tilts and wound penalties. Always have access to brass knuckles due to rivets on the fist (0L, +/-0 Initiative).",
        "source": "FoH 124"
    },
    "tough_as_stone": {
        "name": "Tough as Stone",
        "appearance": "Skin like stone.",
        "system": "Spend one Aether to downgrade all damage from an attack by one level (aggravated to lethal, lethal to bashing). Cannot stack on one attack, but can be used against multiple attacks in the same round.",
        "source": "DTD 199"
    },
    "unyielding_vice": {
        "name": "Unyielding Vice",
        "appearance": "Pneumatic pumps, hoses and pistons adorn the hand.",
        "system": "The demon's grip is near-unbreakable and can grasp onto anything that would not physically destroy the hand. Gain +5 in grapples as well.",
        "source": "FoH 124"
    },
    # Demon Translation Guide Modifications
    "casts_no_reflection": {
        "name": "Casts No Reflection",
        "appearance": "Body distorts light and is hard to process visually.",
        "system": "Visage is not captured by reflective surfaces or recording media.",
        "source": "DTG 40"
    },
    "conjuration": {
        "name": "Conjuration",
        "appearance": "Pseudo-magnetic mesh on palms of hands.",
        "system": "Apply the benefits of the Quick Draw and Sleight of Hand Merits through teleporting objects short distances.",
        "source": "DTG 40"
    },
    "damage_resistance": {
        "name": "Damage Resistance",
        "appearance": "",
        "system": "Ignore wound penalties.",
        "source": "DTG 40, DTF 211"
    },
    "dead_reckoning": {
        "name": "Dead Reckoning",
        "appearance": "Translucent HUD eyelids.",
        "system": "Apply the rote quality to Streetwise and Survival actions to self-orient.",
        "source": "DTG 40"
    },
    "enhanced_ability_attribute_mod": {
        "name": "Enhanced Ability/Attribute",
        "appearance": "",
        "system": "Add Primum to all rolls with chosen skill, or +2 to all rolls with chosen attribute.",
        "source": "DTG 40, DTF 211"
    },
    "ghost_sight": {
        "name": "Ghost Sight",
        "appearance": "Extra pair of pupilless eyes.",
        "system": "Perceive ghosts and spirits in Twilight.",
        "source": "DTG 40"
    },
    "immune_to_bashing_damage": {
        "name": "Immune To Bashing Damage",
        "appearance": "",
        "system": "Immune to attacks that only deal bashing damage.",
        "source": "DTG 40, DTF 188"
    },
    "immune_to_falling_damage": {
        "name": "Immune To Falling Damage",
        "appearance": "",
        "system": "Negate all damage incurred from falls.",
        "source": "DTG 40, DTF 185"
    },
    "multiple_eyes": {
        "name": "Multiple Eyes",
        "appearance": "Covered in eyes or lenses.",
        "system": "Ignore the Blindness Tilt and Blind Condition except when they represent total lack of visibility in the demon's surroundings. +2 to Perception rolls using vision.",
        "source": "DTG 41"
    },
    "quills": {
        "name": "Quills",
        "appearance": "Spiky.",
        "system": "Armor +1/0. Inflict 1L damage when struck by a Brawl or Melee attack that did not roll an exceptional success.",
        "source": "DTG 41"
    },
    "relentless": {
        "name": "Relentless",
        "appearance": "Geodesic metal torso.",
        "system": "Ignore suffocation, hunger, thirst, tiring and fatigue.",
        "source": "DTG 41"
    },
    "weather_sense": {
        "name": "Weather Sense",
        "appearance": "Head-mounted array of microwave domes.",
        "system": "Detect current or future weather within (10 x Primum) miles.",
        "source": "DTG 42"
    },
}

# Technologies - Must be activated when used
DEMON_TECHNOLOGIES = {
    "abruption_jets": {
        "name": "Abruption Jets",
        "appearance": "Small vents that glow blue when active.",
        "system": "Can reflexively spend 1 Aether and completely stop moving, regardless of speed, power or direction. The Demon suffers no harm from the rapid change in velocity.",
        "source": "FoH 124"
    },
    "acidic_spit": {
        "name": "Acidic Spit",
        "appearance": "Corrosive mucus or ichor.",
        "system": "Spit acid up to 10 yards away as a Dexterity + Athletics - Defense attack with a weapon rating of 0A, damaging armor by 2 Durability. Also works while biting!",
        "source": "DTD 199"
    },
    "adhesive": {
        "name": "Adhesive",
        "appearance": "Narrow tubes extend from the Demon's fingers.",
        "system": "Exude an adhesive from the fingers. Can be used as a tool which grants a +3 equipment bonus when appropriate, which includes climbing. Can be used in a grapple as a restraining bond with durability equal to Primum. Any adhesive attached to the Demon's skin can be dissolved as a reflexive action. Can touch an object and dissolve any adhesive, mortar or sealant within 1 yard for the cost of 1 Aether.",
        "source": "FoH 124"
    },
    "aura_sight": {
        "name": "Aura Sight",
        "appearance": "Glowy eyes.",
        "system": "Reflexively roll Wits + Investigation to ask a question per success of the Storyteller through interpreting body language and supernatural qualities.",
        "source": "DTD 199"
    },
    "barbed_tail": {
        "name": "Barbed Tail",
        "appearance": "Poisonous prehensile tail.",
        "system": "Close combat attacks with Dexterity + Athletics - Defense. Success deals no damage but inflicts the Poisoned tilt.",
        "source": "DTD 200"
    },
    "blind_sense": {
        "name": "Blind Sense",
        "appearance": "Black or absent eyes.",
        "system": "Sense anything within twenty feet regardless of barriers. Undeterred by invisibility. Roll Wits + Investigation + Primum vs. Dexterity + Stealth to pierce stealth.",
        "source": "DTD 200"
    },
    "clairvoyant_sight": {
        "name": "Clairvoyant Sight",
        "appearance": "Milky pupils.",
        "system": "Concentrate on a person or place to see the subject across any distance with perfect clarity. If concentration is interrupted, suffer the Captivated condition.",
        "source": "DTD 200"
    },
    "collapsible": {
        "name": "Collapsible",
        "appearance": "Parts of the body exhibit TV static.",
        "system": "Can shrink to as small as Size 1 as an instant action. Gain a +3 bonus to any action that would benefit from the decreased size. Spend 1 Aether to shrink to a mere 9 inches in height. Can return to normal size as an instant action and the size changing provided by this technology does not alter attributes or health.",
        "source": "FoH 125"
    },
    "demonic_horns": {
        "name": "Demonic Horns",
        "appearance": "They're horns.",
        "system": "Head butt using Strength + Brawl with a damage rating of 1L. Success also inflicts the Stunned tilt.",
        "source": "DTD 201"
    },
    "electric_jolt": {
        "name": "Electric Jolt",
        "appearance": "Visible electric current.",
        "system": "Discharge electricity as an instant action, to power a device or disable it for 10 minutes. Spend one Aether to concentrate a full electric field as 2/0 armor. Successful touch attacks with the electric field have a 6B damage rating with no initiative penalty.",
        "source": "DTD 201"
    },
    "electrical_resistance": {
        "name": "Electrical Resistance",
        "appearance": "Resistant materials.",
        "system": "Immunity to electrocution.",
        "source": "DTD 201"
    },
    "environmental_resistance": {
        "name": "Environmental Resistance",
        "appearance": "Mutating Teflon.",
        "system": "Immunity to environmental tilts.",
        "source": "DTD 202"
    },
    "essence_drain": {
        "name": "Essence Drain",
        "appearance": "Fingers and palms turn black and oily.",
        "system": "Make a touch attack against an angel or demon with Wits + Occult + Primum - Resolve to steal a point of Essence or Aether per success, absorbing it as Aether. Possibly works on other supernatural beings?",
        "source": "DTD 202"
    },
    "fire_resistance": {
        "name": "Fire Resistance",
        "appearance": "Heat resistant materials.",
        "system": "Immunity to fire and heat-related environmental tilts.",
        "source": "DTD 202"
    },
    "frost_aura": {
        "name": "Frost Aura",
        "appearance": "Thin sheet of ice or cloud of frost.",
        "system": "Spend one Aether as an instant action to cause the Extreme Cold tilt across a small house or large room for one hour, lasting on victims until they receive medical attention for hypothermia.",
        "source": "DTD 202"
    },
    "fluid_form": {
        "name": "Fluid Form",
        "appearance": "You're the T-1000.",
        "system": "Reduce dice penalties to actions from conditions or tilts by 1. Does not affect demonic conditions.",
        "source": "DTD 202"
    },
    "inhuman_beauty": {
        "name": "Inhuman Beauty",
        "appearance": "Otherworldly wonder.",
        "system": "+2 to Social rolls benefitting from looks. Reflexively roll Presence + Intimidation vs. Composure to inflict your choice of Inspired or Swooning on all who see you.",
        "source": "DTD 202"
    },
    "glory_and_terror": {
        "name": "Glory and Terror",
        "appearance": "Otherworldly terror.",
        "system": "+3 to Intimidation rolls. Reflexively roll Presence + Intimidation to inflict the Insensate tilt on a target per success, which can be used as hard leverage.",
        "source": "DTD 203"
    },
    "laser_cutter": {
        "name": "Laser Cutter",
        "appearance": "A small heavily wired box that makes whirring noises.",
        "system": "When used, ignores 5 Durability or Armour. Does 3 Structure or 3L per turn of use. Against objects, it has a Dexterity + Crafts roll. Against living beings, it requires a Dexterity + Firearms roll, which ignores defence unless the target would gain defence against firearms. Damage is reduced by 1 for each five feet in distance the target is from the demon.",
        "source": "FoH 125"
    },
    "mantle_of_fire": {
        "name": "Mantle of Fire",
        "appearance": "Fire as hair and jets of fire shoot out from the shoulders.",
        "system": "Anything that comes into contact with the Demon suffers 2L a turn. Can subdue the effect as a reflexive action. Can also spend 1 Aether to enhance the effect to do one of three things: Create thick smoke covering 30 yards inflicting penalties based on distance, double the flaming intensity to improve damage to 4L or cause the mantle to explode as if it were a 2L explosion.",
        "source": "FoH 125"
    },
    "mind_reading": {
        "name": "Mind Reading",
        "appearance": "Coppery sclera.",
        "system": "Reflexively roll Wits + Persuasion + Primum vs. Resolve + Supernatural Tolerance to read surface thoughts as long as concentration holds. Digging for specific knowledge costs one Willpower and requires Wits + Subterfuge - Resolve as an extended action.",
        "source": "DTD 203"
    },
    "mirrored_skin": {
        "name": "Mirrored Skin",
        "appearance": "Mirrored scales.",
        "system": "Invisible while standing still, though detected by non-sight-based senses. Unimpeded by other demonic form abilities. +3 to Stealth rolls and a -1 penalty to rolls to notice the demon while sneaking.",
        "source": "DTD 203"
    },
    "multiversal_antenna": {
        "name": "Multiversal Antenna",
        "appearance": "A massive antenna sticking outside of the Demon's head with radar dishes and coils.",
        "system": "Allows a Demon to sense Splinter fractures and similar divergent timelines. Allows you to ask questions about a target (be it place, person or fracture) and how the alternate timeline could be different compared to the current situation. Spend 1 Aether and roll Wits + Occult + Primum.",
        "source": "Iface 28"
    },
    "savant_core": {
        "name": "Savant Core",
        "appearance": "Computer type system embedded in the body.",
        "system": "The core contains a Skill with 5-dots. The demon can access this functionality with an instant action, replacing their current score with that of the Savant Core.",
        "source": "FoH 125"
    },
    "shielded_compartment": {
        "name": "Shielded Compartment",
        "appearance": "Small safe-door embedded in the chest.",
        "system": "A 1-foot cubed pocket dimension exists inside the Demon which can be used to store objects. Objects stored inside cannot be detected by mundane or supernatural means. The door cannot be opened by another unless the Demon is unconscious. Opening the door requires an extended Wits + Larceny with successes exceeding the Demon's Strength + Primum.",
        "source": "FoH 126"
    },
    # Demon Translation Guide Technologies
    "affirm": {
        "name": "Affirm",
        "appearance": "Psychoactive crystal forehead light array.",
        "system": "Spend one Aether to restore a point of Willpower or grant Inspired or Steadfast to a subject with no Supernatural Tolerance.",
        "source": "DTG 39"
    },
    "beckon": {
        "name": "Beckon",
        "appearance": "Pheromonal facial glands.",
        "system": "Roll Presence + Expression - target's Composure to inflict Swooning.",
        "source": "DTG 39"
    },
    "enhanced_ability_attribute_tech": {
        "name": "Enhanced Ability/Attribute",
        "appearance": "",
        "system": "Spend 1 aether to add Primum to all rolls involving skills of one category (physical, mental, or social) until the end of the scene.",
        "source": "DTG 40, DPG 98"
    },
    "eyes_of_fate": {
        "name": "Eyes of Fate",
        "appearance": "Feathery antennae.",
        "system": "Spend one Aether to intuit an ongoing or imminent event relevant to the demon within his Primum in miles.",
        "source": "DTG 40"
    },
    "frenzy": {
        "name": "Frenzy",
        "appearance": "Spinal injection tubes.",
        "system": "Spend one Aether to invoke Demonic Rage. Take 8-Again on attack rolls for the duration.",
        "source": "DTG 40"
    },
    "the_host": {
        "name": "The Host",
        "appearance": "Serrated sawblade skin.",
        "system": "When grappling, reflexively bite the opponent with Strength + Brawl, at a 2L weapon rating.",
        "source": "DTG 40"
    },
    "immune_to_poisons": {
        "name": "Immune To Poisons",
        "appearance": "",
        "system": "Immune to damage and impairment from all toxins and drugs.",
        "source": "DTG 41, DTF 209"
    },
    "mirage": {
        "name": "Mirage",
        "appearance": "Body undulates across perceived distances.",
        "system": "Apply Defense against Firearms attacks, even taken unaware.",
        "source": "DTG 41"
    },
    "mist": {
        "name": "Mist",
        "appearance": "Smoke vents behind jaw.",
        "system": "Spend one Aether and roll Stamina + Science to obscure a radius of a yard per success with smoke, for up to a scene.",
        "source": "DTG 41"
    },
    "reapers_breath": {
        "name": "Reaper's Breath",
        "appearance": "Forearm-mounted gas grenade launchers.",
        "system": "Spend one Aether to suffuse an area (Primum) yards in diameter with poisonous gas, to which the demon is immune, for up to a scene.",
        "source": "DTG 41"
    },
    "rend_the_soul": {
        "name": "Rend the Soul",
        "appearance": "Tendrils that conduct existential dread.",
        "system": "Spend one Aether and roll Presence + Science - the target's Resolve. Inflict Stunned on success, and if the target is an ordinary human, also either Beaten Down or, for a day per success, Broken or Madness.",
        "source": "DTG 41"
    },
    "sense_the_hidden": {
        "name": "Sense the Hidden",
        "appearance": "Rotating silver rosary collar.",
        "system": "Spend one Aether and roll Wits + Medicine to locate all life of Size 1 or greater within a yard per success, for one scene.",
        "source": "DTG 41"
    },
    "touch_of_death": {
        "name": "Touch of Death",
        "appearance": "Taser fingers.",
        "system": "Roll Dexterity + Brawl - Defense to inflict Stunned.",
        "source": "DTG 41"
    },
    "toxins": {
        "name": "Toxins",
        "appearance": "Hollow plastic fingernails.",
        "system": "Spend one Aether as an instant action to secrete a moderate Poisoned or Sick Tilt with Brawl and Weaponry attacks for the scene, or two Aether to inflict a grave Tilt.",
        "source": "DTG 41-42"
    },
}

# Propulsions - One-time picks (some)
DEMON_PROPULSIONS = {
    "aquatic": {
        "name": "Aquatic",
        "appearance": "Flippers and aerodynamic shapes for the body. Membranes cover orifices when submerged.",
        "system": "Can swim underwater with a species factor of 10. Can spend 1 Aether to turn into the liquid. In liquid form, the Demon cannot be harmed, even if state changes (e.g. freezing the body of water) would render her unable to act. The demon cannot 'divide' and can only move through full bodies of water that could support the size. Reforming depends on how much liquid is present, but costs 1 Aether.",
        "source": "FoH 126"
    },
    "burrowing": {
        "name": "Burrowing",
        "appearance": "Drills are part of the hands and feet.",
        "system": "Can burrow underground. Move through loose material at speed, Durability 1 at half speed, Durability 2 at one quarter speed. Durability 3 materials can be burrowed through at a speed of 1 and requires 1 Aether a minute. Can be used as a weapon, statistically identical to a Chainsaw (5L, -6Init, Str 4, Sz 3, 9-Again, 2 Handed).",
        "source": "FoH 126"
    },
    "long_limbs": {
        "name": "Long Limbs",
        "appearance": "Elongated, graceful spindles.",
        "system": "+2 to Athletics rolls (but not Defense). +5 to Speed.",
        "source": "DTD 204"
    },
    "phasing": {
        "name": "Phasing",
        "appearance": "A low hum of electricity and faint transparency.",
        "system": "Spend one Aether to become incorporeal and travel through objects at half Speed, reverting to corporeal form after passing through. Cannot carry objects or people with you. Incorporeality confers a -2 penalty to attacks against you.",
        "source": "DTD 204"
    },
    "plasma_drive": {
        "name": "Plasma Drive",
        "appearance": "Visible plasma veins and tubing.",
        "system": "Don't tire from dodging or athletic feats. No penalties to Defense from multiple attackers in a round. +2 to Defense in single combat. May apply Defense against ranged attacks. May spend one Aether reflexively to run and take an action as normal, without losing Defense.",
        "source": "DTD 204"
    },
    "spatial_distortion": {
        "name": "Spatial Distortion",
        "appearance": "You look two-dimensional.",
        "system": "Warp space as an instant action to achieve the effects of smaller size. Spend one Aether and roll Intelligence + Occult to become nearly invisible through sheer thinness for a number of turns equal to successes. Finding the demon requires contesting this roll with Wits + Investigation.",
        "source": "DTD 204"
    },
    "teleportation": {
        "name": "Teleportation",
        "appearance": "Tracery that reacts when teleporting.",
        "system": "Reflexively spend one Aether to teleport anywhere within line of sight. Cannot bring people or anything of significant size with you.",
        "source": "DTD 204"
    },
    "tether": {
        "name": "Tether",
        "appearance": "Grappling appendage.",
        "system": "Make a touch attack with Strength + Athletics to grapple up to 20 yards away and ratchet yourself to the target object at running speed. Can carry up to another person with you. Can pull a target with Strength + Athletics - Defense, rendering the person grappled, and enabling the demon to pull the target closer as a grappling maneuver each turn. May hold or restrain, but not perform other maneuvers.",
        "source": "DTD 204"
    },
    "tread": {
        "name": "Tread",
        "appearance": "Legs appear as a cluster of treaded wheels.",
        "system": "Ignores environmental penalties from ground-based obstacles and is not slowed at all when carrying objects up to Strength. Can also perform a car-crash attack, with the tread having a handling of 2, with a Dexterity + Athletics + Handling - Defence roll. Crashing into other vehicles causes half of structure damage as Lethal to the Demon instead.",
        "source": "FoH 127"
    },
    "urban_fluidity": {
        "name": "Urban Fluidity",
        "appearance": "Moves between objects in a near-imperceptible blur.",
        "system": "As an replacement for a character's standard movement, can move directly in a straight line instantly to a man-made object, standing on it as if gravity were irrelevant.",
        "source": "FoH 127"
    },
    "wings": {
        "name": "Wings",
        "appearance": "Wings.",
        "system": "You can fly. Add a species factor of 10 to your Speed while flying.",
        "source": "DTD 205"
    },
}

# Processes - Must be activated when used
DEMON_PROCESSES = {
    "aegis_protocol": {
        "name": "Aegis Protocol",
        "appearance": "Grow a small shield from your hand.",
        "system": "Reflexively summon or dismiss the aegis. Grants partial concealment and +2 to Defense with no initiative penalty. Can shield bash with a damage rating of 1L. Spend one Aether to reflexively expand the shield into an armored barrier, gaining 2/2 armor that stacks with any other armor.",
        "source": "DTD 205"
    },
    "amorphous": {
        "name": "Amorphous",
        "appearance": "Skin looks like soft, poorly worked putty.",
        "system": "When in full demonic form only, the demon can spend Aether to substitute parts of its demonic form as an instant action. 1 Aether allows the replacement of a technology with another technology or a modification with another modification. 2 Aether allows for replacement of propulsion with another propulsion. Reverting to cover restores all substituted form abilities to their original ones. Spending 1 Aether allows for reversion of one or more changed form abilities to their original form. The Demon can only substitute their original form abilities, they have to revert changed form abilities if they wish to change them to a different form later.",
        "source": "FoH 127"
    },
    "body_modification": {
        "name": "Body Modification",
        "appearance": "Scarification and fissures.",
        "system": "Reflexively reallocate Physical Attribute dots. Must obey Primum restrictions on Attribute maximums, and cannot reduce any Attribute to zero dots.",
        "source": "DTD 205"
    },
    "cavernous_maw": {
        "name": "Cavernous Maw",
        "appearance": "Glasgow smile with unhinging jaws.",
        "system": "Eat anything. Larger objects take 2 Structure damage per bite until destroyed. As a bite attack, weapon rating of 2A.",
        "source": "DTD 205"
    },
    "corruption_aura": {
        "name": "Corruption Aura",
        "appearance": "Tangible noxious aura.",
        "system": "Spend one Aether and roll Presence + Occult as an instant action to concentrate the aura, dealing one Structure damage to large structures every five minutes, or every other round for smaller objects. The demon's possessions are immune.",
        "source": "DTD 205"
    },
    "dataform": {
        "name": "Dataform",
        "appearance": "Capacitors, microprocessors and metal gates cover the skin.",
        "system": "As an Instant action, spend 1 Aether to transform into data, with an upkeep of 1 Aether per turn to maintain it. If touching some form of technology that can facilitate data transmission, the Demon can be downloaded or uploaded as fast as the technology allows. When travelling, can only determine location by data identifiers such as IP Addresses, but can interpret the information as geographical with a Wits + Computer roll at a -2 penalty.",
        "source": "FoH 128"
    },
    "eliminator_cannon": {
        "name": "Eliminator Cannon",
        "appearance": "Transform one entire arm into a Mortar/Grenade launcher.",
        "system": "Fire a concussion or fragmentation grenade as an action using Dexterity + Firearms. The grenades have 75/150/300 range, blast area of 3, and 3L or 3B damage as determined by the Demon. Alternatively, spend 1 Aether to create a triggered or timed explosive. The explosive has a blast area of 4 and a damage of 3 + Primum. Trigger is performed by spending 1 Aether and has no range limit, provided the Demon is still on the same plane of existence as the explosive. Up to 2 x Primum undetonated explosives can be maintained, if more are created one randomly dissolves.",
        "source": "FoH 128"
    },
    "extra_mechanical_limbs": {
        "name": "Extra Mechanical Limbs",
        "appearance": "Extra mechanical limbs.",
        "system": "Can operate the extra limbs independently without penalty. +3 to Strength rolls benefitting from the focused use of all the character's arms. +3 to Defense if at least two hands are free. Extra limbs deal lethal instead of bashing damage with unarmed attacks.",
        "source": "DTD 206"
    },
    "insect_swarm": {
        "name": "Insect Swarm",
        "appearance": "You are a swarm of creepy crawlies.",
        "system": "Reflexively spend one Aether to discorporate into a mobile swarm; reincorporate into a single mass of demon reflexively at no cost. In swarm form, the demon only dies if every bug is killed. The demon becomes a Swarm environmental tilt. Losing at least half the demon's mass from separation or damage causes the demon to fall unconscious when reincorporated.",
        "source": "DTD 206"
    },
    "magnesium_flare": {
        "name": "Magnesium Flare",
        "appearance": "Illuminate a five feet radius.",
        "system": "Spend one Aether and roll Presence + Intimidation vs. Wits + Athletics as an instant action to focus the magnesium flare against people. Blind those who see you and fail to resist. You can be seen from a distance away.",
        "source": "DTD 206"
    },
    "memory_theft": {
        "name": "Memory Theft",
        "appearance": "You've got a USB cord to jack into people's heads.",
        "system": "Control a grapple and jack into the target's brain to incapacitate them without causing damage. Spend one Aether and roll Manipulation + Subterfuge - Composure as an extended action to download an hour's worth of memories. Can attempt to alter memories or induce amnesia.",
        "source": "DTD 207"
    },
    "multiple_images": {
        "name": "Multiple Images",
        "appearance": "Hash mark tattoos incorporate into duplicate images of the demon.",
        "system": "Reflexively spend one Aether and roll Manipulation + Intimidation + Primum vs. Composure + Supernatural Tolerance to display a legion of mirage-demons, inducing the Insane tilt and taking partial concealment against anyone who fails to distinguish the real demon from the duplicate images.",
        "source": "DTD 207"
    },
    "nanobot_composition": {
        "name": "Nanobot Composition",
        "appearance": "Active body part breaks down into a cloud of microscopic machines.",
        "system": "Can create simple objects and machines from the body. Cannot change size, but can reconfigure the body's shape into different configurations. Can reflexively spend 1 Aether to disperse a part of the body, ignoring a single attack or direct source of harm. Dispersed body parts can only be hurt with things that attack areas, like fire.",
        "source": "FoH 128"
    },
    "quill_burst": {
        "name": "Quill Burst",
        "appearance": "Quills.",
        "system": "Spend one Aether to roll Strength + Athletics as an attack against everyone in a ten foot radius. Each target hit takes 1L damage and suffers from the Poisoned tilt until the quill is removed. Armor prevents damage as normal and in doing so prevents the tilt. Removing the quill requires medical attention.",
        "source": "DTD 207"
    },
    "rain_of_fire": {
        "name": "Rain of Fire",
        "appearance": "Radiate heat.",
        "system": "Spend one Aether to roll Intelligence + Primum as an instant action to call down a rain of flame for (Primum) turns. Direct the flames with Wits + Occult - Defense, causing 3L damage.",
        "source": "DTD 208"
    },
    "voice_of_the_angel": {
        "name": "Voice of the Angel",
        "appearance": "Your voice is autotuned.",
        "system": "Spend one Aether and roll Presence + Expression + Primum - Composure to shriek, dealing successes in bashing damage to those who can hear you and ignoring armor. Those who take damage are also Deafened.",
        "source": "DTD 208"
    },
    "wound_healing": {
        "name": "Wound Healing",
        "appearance": "Riddled with scars or welts.",
        "system": "Heal either 1B or 1L per turn, reflexively.",
        "source": "DTD 208"
    },
    # Demon Translation Guide Processes
    "aura_of_dread": {
        "name": "Aura of Dread",
        "appearance": "Psychoactive black discs cover the body.",
        "system": "Spend one Aether to inflict Insensate on targets within (Primum) yards, for up to a scene.",
        "source": "DTG 39"
    },
    "aura_of_entropy": {
        "name": "Aura of Entropy",
        "appearance": "Nuclear rods project from the shoulders and back.",
        "system": "Deal 1B every 2 rounds to organic targets within Primum yards.",
        "source": "DTG 39"
    },
    "aura_of_misfortune": {
        "name": "Aura of Misfortune",
        "appearance": "Protruding sonic ring around the crown of the head.",
        "system": "Spend one Aether and roll Presence + Occult as an instant action. Downgrades failures to dramatic failures and exceptional successes to successes within (Primum) yards.",
        "source": "DTG 39"
    },
    "aura_of_vitality": {
        "name": "Aura of Vitality",
        "appearance": "Medical ovipositor.",
        "system": "Spend one Aether to heal a target of non-aggravated damage, at a rate of (Primum) points of either bashing damage removed, or lethal reduced to bashing, per turn.",
        "source": "DTG 39"
    },
    "cloak_of_shadows": {
        "name": "Cloak of Shadows",
        "appearance": "Arcane brands cause viewers to avert their gaze.",
        "system": "Spend one Aether to activate for a scene. While active, take the rote quality on Stealth rolls, and apply the effects of the Blindness Tilt to attacks directed at you.",
        "source": "DTG 40"
    },
    "deathgrip": {
        "name": "Deathgrip",
        "appearance": "Body is composed of sandlike granules.",
        "system": "Resurrect when killed a day later with no Aether. If no body is left intact to reform, this also costs a dot of Willpower.",
        "source": "DTG 40"
    },
    "enhanced_ability_attribute_proc": {
        "name": "Enhanced Ability/Attribute",
        "appearance": "",
        "system": "Choose mental, physical, social, power, finesse, or resistance. Gain +2 to all rolls with that category of attributes.",
        "source": "DTG 40, DPG 98"
    },
    "extra_actions": {
        "name": "Extra Actions",
        "appearance": "",
        "system": "Spend 1 Aether as a reflexive action to move to the top of the initiative order, or if already at top of the initiative order instead take an instant action at the end of the current turn.",
        "source": "DTG 40, DTF 178"
    },
    "fiery_blood": {
        "name": "Fiery Blood",
        "appearance": "Smoky breath, skin nearly burns to touch.",
        "system": "Projects lava over (Primum) yards from the demon when she suffers lethal or aggravated damage. For each turn of exposure, the lava flow inflicts a point of lethal damage per times the demon has suffered lethal or aggravated wounds this scene. Can be halted reflexively.",
        "source": "DTG 40"
    },
    "nimble_hunter": {
        "name": "Nimble Hunter",
        "appearance": "Elongated snout and backwards-facing knees.",
        "system": "Has the effects of Olfactory Enhancements, plus while in natural surroundings, take the rote quality to Athletics, Stealth and Survival rolls.",
        "source": "DTG 41"
    },
    "suns_bounty": {
        "name": "Sun's Bounty",
        "appearance": "Solar arrays that unfold like wings.",
        "system": "Activate and deactivate as an instant action. While active, you are Immobilized, but recover a point of Aether per turn of exposure to bright sunlight, or per minute of exposure to typical artificial lighting. Spend one Aether when activating to partially deploy, freeing mobility but reducing rates to by the minute or hour.",
        "source": "DTG 41"
    },
}

# Categorize all demon form traits
ALL_DEMON_MODIFICATIONS = list(DEMON_MODIFICATIONS.keys())
ALL_DEMON_TECHNOLOGIES = list(DEMON_TECHNOLOGIES.keys())
ALL_DEMON_PROPULSIONS = list(DEMON_PROPULSIONS.keys())
ALL_DEMON_PROCESSES = list(DEMON_PROCESSES.keys())

