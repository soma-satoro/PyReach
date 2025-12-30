"""
Werewolf: The Forsaken Tribes and Lodges
Detailed tribe and lodge information for Chronicles of Darkness 2nd Edition.
Based on Werewolf: The Forsaken 2nd Edition and supplemental materials.
"""

# ============================================================================
# TRIBES OF THE MOON (FORSAKEN)
# ============================================================================

TRIBES_OF_THE_MOON = {
    "blood_talons": {
        "name": "Blood Talons",
        "first_tongue": "Suthar Anzuth",
        "hunt_focus": "Werewolves",
        "primary_renown": "Glory",
        "tribal_gifts": ["Inspiration", "Rage", "Strength"],
        "description": "Merciless, elemental apex predators",
        "tribal_oath": "Cannot provide surrender terms, you would not accept yourself",
        "book": "WTF 2e 34"
    },
    "bone_shadows": {
        "name": "Bone Shadows",
        "first_tongue": "Hirfathra Hissu",
        "hunt_focus": "Ephemera",
        "primary_renown": "Wisdom",
        "tribal_gifts": ["Death", "Elements", "Insight"],
        "description": "Students of the Shadow who balance the scales of flesh and spirit",
        "tribal_oath": "Pay all Shadow denizens in kind",
        "book": "WTF 2e 37"
    },
    "hunters_in_darkness": {
        "name": "Hunters in Darkness",
        "first_tongue": "Meninna",
        "hunt_focus": "Hosts",
        "primary_renown": "Purity",
        "tribal_gifts": ["Nature", "Stealth", "Warding"],
        "description": "Stalkers who guard and memorize every facet of their territory",
        "tribal_oath": "Do not allow any sacred place in your territory to be violated",
        "book": "WTF 2e 40"
    },
    "iron_masters": {
        "name": "Iron Masters",
        "first_tongue": "Farsil Luhal",
        "hunt_focus": "Humans",
        "primary_renown": "Cunning",
        "tribal_gifts": ["Knowledge", "Shaping", "Technology"],
        "description": "Cunning shepherds who adapt to flow with the herd",
        "tribal_oath": "Honor everything in your territory",
        "book": "WTF 2e 43"
    },
    "storm_lords": {
        "name": "Storm Lords",
        "first_tongue": "Iminir",
        "hunt_focus": "Ridden",
        "primary_renown": "Honor",
        "tribal_gifts": ["Evasion", "Dominance", "Weather"],
        "description": "Hard-willed leaders who hold both themselves and others to strict standards",
        "tribal_oath": "No one should be tending or witnessing your weakness",
        "book": "WTF 2e 46"
    },
}

# ============================================================================
# PURE TRIBES
# ============================================================================

PURE_TRIBES = {
    "fire_touched": {
        "name": "Fire-Touched",
        "first_tongue": "Izidakh",
        "hunt_focus": "Apostates",
        "primary_renown": "Wisdom",
        "secondary_renown": "Cunning/Glory",
        "tribal_gifts": ["Disease", "Fervor", "Insight", "Inspiration"],
        "description": "Zealous, fervid priests of the Shadow",
        "tribal_oath": "Never allow a falsehood to remain unchallenged",
        "book": "DEC 78, NH-SM 15"
    },
    "ivory_claws": {
        "name": "Ivory Claws",
        "first_tongue": "Tzuumfin",
        "hunt_focus": "Bastards",
        "primary_renown": "Purity",
        "secondary_renown": "Honor/Glory",
        "tribal_gifts": ["Agony", "Blood", "Dominance", "Warding"],
        "description": "Exploitative blood purists punishing sins of the father",
        "tribal_oath": "Follow personal concept of purity truest to self",
        "book": "DEC 78, NH-SM 15"
    },
    "predator_kings": {
        "name": "Predator Kings",
        "first_tongue": "Ninna Farakh",
        "hunt_focus": "The complacent",
        "primary_renown": "Glory",
        "secondary_renown": "Purity/Wisdom",
        "tribal_gifts": ["Hunger", "Nature", "Rage", "Strength"],
        "description": "Savage predators who reject any delicacy as weakness",
        "tribal_oath": "Honor nothing of human craft",
        "book": "DEC 78, NH-SM 15"
    },
}

# ============================================================================
# OTHER TRIBES
# ============================================================================

OTHER_TRIBES = {
    "ghost_wolves": {
        "name": "Ghost Wolves",
        "first_tongue": "Thihirtha Numea",
        "hunt_focus": "Personal values",
        "primary_renown": "None",
        "tribal_gifts": [],
        "description": "Tyros and iconoclasts who reject or are ignorant of Uratha cultures",
        "tribal_oath": "None",
        "book": "WTF 2e 49"
    },
    "bale_hounds": {
        "name": "Bale Hounds",
        "first_tongue": "Asah Gadar",
        "hunt_focus": "Enemies of the Maeljin",
        "primary_renown": "Varies",
        "tribal_gifts": ["As for their Tribe/Auspice before corruption"],
        "description": "Corrupted Uratha who serve the Maeljin",
        "tribal_oath": "Varies",
        "book": "NH-SM 33"
    },
}

# ============================================================================
# LODGES
# ============================================================================

ALL_LODGES = {
    "cull": {
        "name": "Cull",
        "description": "A profane lodge using a twisted form of Daoism",
        "book": "Pack 75"
    },
    "cherufe": {
        "name": "Cherufe",
        "description": "Transports and trades powerful Fetishes and Talons in Chile",
        "book": "Pack 76"
    },
    "dream_eaters": {
        "name": "Dream Eaters",
        "description": "Drug Fueled wolves prone to excess",
        "book": "Pack 80"
    },
    "dreaming_lodge": {
        "name": "Dreaming Lodge",
        "description": "Organized Australian Uratha community, ancient beyond even the tribes",
        "book": "WTF 2e 266-267"
    },
    "eaters_of_the_dead": {
        "name": "Eaters of the Dead",
        "description": "Carrion-eating Ghost Wolves with ambitions of founding a tribe to hunt the dead",
        "blessing": "Spend Willpower to purge physical or supernatural afflictions or taints",
        "ban": "Leave no kill to rot",
        "sacred_hunt": "Undead prey lose a point of supernatural fuel when bitten, or suffer aggravated damage if exhausted",
        "access": "Lodge Sorcery (Merit), Carrion Feast (Rite)",
        "book": "Pack 90-91"
    },
    "hollow_rivers": {
        "name": "Hollow Rivers",
        "description": "A void-eaten lodge",
        "book": "Pack 75"
    },
    "jaw_hags": {
        "name": "Jaw Hags",
        "description": "Collecting essences of various resonances to barter with",
        "book": "Pack 76"
    },
    "lodge_of_arms": {
        "name": "Lodge of Arms",
        "description": "Wardens who hunt humans well equipped for combat",
        "book": "Pack 77"
    },
    "lodge_of_the_blue_moon": {
        "name": "Lodge of the Blue Moon",
        "description": "A wound-tainted lodge",
        "book": "Pack 75"
    },
    "lodge_of_the_cage": {
        "name": "Lodge of the Cage",
        "description": "Jailers of mages, who have a stronghold that imprisons and breaks their prey to be unleashed as shock troops",
        "book": "Pack 76"
    },
    "lodge_of_the_chronicle": {
        "name": "Lodge of the Chronicle",
        "description": "A venerable tradition of Cahalith who preserve the knowledge of the People so that it will not be lost in the hunt",
        "book": "WTF 2e 53"
    },
    "lodge_of_the_clocktower": {
        "name": "Lodge of the Clocktower",
        "description": "Their prey meddles with time",
        "book": "Pack 78"
    },
    "lodge_of_crows": {
        "name": "Lodge of Crows",
        "description": "Howlers who hunt through contacts and influence",
        "book": "Pack 77"
    },
    "lodge_of_death": {
        "name": "Lodge of Death",
        "description": "Seekers who hunt anything active beyond their natural lifespan, including ghosts and the undead",
        "book": "Pack 77"
    },
    "lodge_of_the_einherjar": {
        "name": "Lodge of the Einherjar",
        "description": "Colorado-based Forsaken who unearth and retell lost tales of the glorious dead",
        "book": "WTF 2e 51"
    },
    "lodge_of_the_embers": {
        "name": "Lodge of the Embers",
        "description": "Fire Spirit focused that has their own totem imprisoned",
        "book": "Pack 80"
    },
    "lodge_of_the_field": {
        "name": "Lodge of the Field",
        "description": "Polish cult of holy cannibals who gorge themselves on Essence for the gods",
        "book": "WTF 2e 274-277"
    },
    "lodge_of_the_firefly": {
        "name": "Lodge of the Firefly",
        "description": "At war with a Mosquito based Host",
        "book": "Pack 75"
    },
    "lodge_of_gargoyles": {
        "name": "Lodge of Gargoyles",
        "description": "Urban Irraka who specialize in killing with ranged weapons from high above",
        "book": "WTF 2e 53"
    },
    "lodge_of_garm": {
        "name": "Lodge of Garm",
        "description": "Zealous Forsaken sworn to the art of slaying werewolves",
        "blessing": "Spending Willpower to enhance an attack against a werewolf adds an extra +2 dice",
        "ban": "Never retreat before the rest of your pack",
        "sacred_hunt": "Sense whether the prey has high Primal Urge, and if so, retain Defense on all-out attacks",
        "access": "Lodge Armory, Uma Suguthkuth (Merits)",
        "book": "Pack 82-83"
    },
    "lodge_of_harbingers": {
        "name": "Lodge of Harbingers",
        "description": "Seekers who hunt down traveling spirits",
        "book": "Pack 77"
    },
    "lodge_of_harmony": {
        "name": "Lodge of Harmony",
        "description": "Chasers who seek out Hosts before they can cause any damage",
        "book": "Pack 77"
    },
    "lodge_of_the_hook_hand": {
        "name": "Lodge of the Hook Hand",
        "description": "Hunters in Darkness who craft and alter folklore and urban legends to guide the human herds",
        "book": "WTF 2e 51"
    },
    "lodge_of_the_hundred_days": {
        "name": "Lodge of the Hundred Days",
        "description": "Rwandan Uratha who labor to resolve the Wounds left behind by genocide",
        "book": "WTF 2e 51"
    },
    "lodge_of_irkalla": {
        "name": "Lodge of Irkalla",
        "description": "Hunters of humans in the belief to bring back Urfarah by slaying as many humans as possible",
        "book": "Pack 78"
    },
    "lodge_of_lightning": {
        "name": "Lodge of Lightning",
        "description": "Wardens dealing with humans who move society in dangerous ways",
        "book": "Pack 77"
    },
    "lodge_of_muspell": {
        "name": "Lodge of Muspell",
        "description": "Norse Fire-Touched, pledged to Muspellheim and branded with crude runes",
        "book": "DE 167"
    },
    "lodge_of_prophecy": {
        "name": "Lodge of Prophecy",
        "description": "Seekers who divine where dangerous and powerful spirits will appear",
        "book": "Pack 77"
    },
    "lodge_of_the_roman_ritual": {
        "name": "Lodge of the Roman Ritual",
        "description": "Catholic priests who exorcise spirits and provide hospice care for their former hosts",
        "book": "WTF 2e 52"
    },
    "lodge_of_the_screaming_moon": {
        "name": "Lodge of the Screaming Moon",
        "description": "Cultists of terror who hunt sources of fear in order to surpass them",
        "blessing": "Intimidation achieves exceptional success on a threshold of three instead of five, and reaps Essence from slain prey",
        "ban": "Either slain prey must scream or the slayer must howl",
        "sacred_hunt": "Spend Essence to ignore supernatural infliction of fear that would impede the hunt",
        "access": "Lodge Lorehouse, Lodge Sorcery (Merits), Banshee Howl (Rite)",
        "book": "Pack 86-87"
    },
    "lodge_of_scrolls": {
        "name": "Lodge of Scrolls",
        "description": "Wardens who take on humans armed with knowledge or occult power",
        "book": "Pack 77"
    },
    "lodge_of_the_seasons": {
        "name": "Lodge of the Seasons",
        "description": "Chasers who heal the damage done by Hosts through the world's natural cycles",
        "book": "Pack 77"
    },
    "lodge_of_the_seven_venoms": {
        "name": "Lodge of the Seven Venoms",
        "description": "Shard eaters who rose to power after Hurricane Katrina",
        "book": "Pack 78"
    },
    "lodge_of_the_shield": {
        "name": "Lodge of the Shield",
        "description": "Iron Masters embedded in human law enforcement, organized to cover for one another and trade favors",
        "book": "WTF 2e 51-52"
    },
    "lodge_of_sleepless_earth": {
        "name": "Lodge of Sleepless Earth",
        "description": "Hunters in Darkness who identify with their territory, changing its form like they change their own",
        "book": "WTF 2e 68"
    },
    "lodge_of_swords": {
        "name": "Lodge of Swords",
        "description": "Destroyers who hunt entire packs of werewolves rather than individuals",
        "book": "Pack 77"
    },
    "lodge_of_the_throne": {
        "name": "Lodge of The Throne",
        "description": "Based in Thailand",
        "book": "Pack 77"
    },
    "lodge_of_thunder": {
        "name": "Lodge of Thunder",
        "description": "Howlers after the Hive-Claimed",
        "book": "Pack 77"
    },
    "lodge_of_the_unmasked": {
        "name": "Lodge of the Unmasked",
        "description": "Cultists who excel at hunting down prey that can change their human disguise",
        "book": "Pack 75"
    },
    "lodge_of_voices": {
        "name": "Lodge of Voices",
        "description": "Bone Shadows that are a bastion of knowledge about the most ancient of spirits",
        "book": "Pack 76"
    },
    "lodge_of_winter": {
        "name": "Lodge of Winter",
        "description": "Howlers after anyone possessed, breaking their bindings in possible",
        "book": "Pack 77"
    },
    "lodge_of_wires": {
        "name": "Lodge of Wires",
        "description": "Iron Masters who study the changes reflected in the Shadow by advancing technology",
        "book": "WTF 2e 51"
    },
    "lodge_of_wrath": {
        "name": "Lodge of Wrath",
        "description": "Chasers who focus on protecting sacred places",
        "book": "Pack 77"
    },
    "matagot": {
        "name": "Matagot",
        "description": "A European and African variant of the Wendigo",
        "book": "Pack 78"
    },
    "prince_bishops_wolves": {
        "name": "Prince Bishop's Wolves",
        "description": "Guardians standing vigil over a bound spirit in County Durham",
        "book": "Pack 77"
    },
    "temple_of_apollo": {
        "name": "Temple of Apollo",
        "description": "Blasphemous human sacrifice cult pretending at class and culture",
        "blessing": "Ignore penalties to force Doors by exploiting a target's Vice or Blood",
        "ban": "Kill outsiders who tread on temple ground",
        "sacred_hunt": "Sense those who intrude on temple ground, and use Facets to hunt them at no Essence cost; use heavy solar activity to consume human souls",
        "access": "Lodge Connections, Lodge Sorcery, Lodge Stronghold (Merits), Glorious Lyre (Fetish)",
        "book": "Pack 88-89"
    },
    "tenders_of_the_fang": {
        "name": "Tenders of the Fang",
        "description": "Using their wolf blooded to save their victims souls",
        "book": "Pack 74"
    },
    "thousand_steel_teeth": {
        "name": "Thousand Steel Teeth",
        "description": "Forsaken road warriors hunting the highways",
        "blessing": "Spending Willpower to work on a vehicle or take it into action grants the rote quality",
        "ban": "Sleep at least a mile away from where last you slept",
        "sacred_hunt": "Track prey travelling by vehicle, and take only bashing damage from ramming, crashes or road tumbling",
        "access": "Lodge Connections (Merit), Iron Leviathan Harpoon, Nomad Chain, Roadkiller (Fetishes)",
        "book": "Pack 84-85"
    },
    "tindalosi": {
        "name": "Tindalosi",
        "description": "Bitter enemies of the Lodge of the Clocktower despite having the same goals",
        "book": "Pack 78"
    },
    "wendigo": {
        "name": "Wendigo",
        "description": "Destroyers using stealth to hunt the most vulnerable werewolves to spread terror",
        "book": "Pack 77"
    },
    "wily_crows": {
        "name": "Wily Crows",
        "description": "Those that capture fetches, fae-touched, and changelings for bargaining",
        "book": "Pack 76"
    },
}

# ============================================================================
# COMBINED TRIBE DATA
# ============================================================================

ALL_TRIBES_DETAILED = {
    **TRIBES_OF_THE_MOON,
    **PURE_TRIBES,
    **OTHER_TRIBES
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_tribe(tribe_name):
    """Get a specific tribe by name."""
    tribe_key = tribe_name.lower().replace(" ", "_")
    return ALL_TRIBES_DETAILED.get(tribe_key)

def get_all_tribes():
    """Get all tribe data."""
    return ALL_TRIBES_DETAILED.copy()

def get_tribes_of_the_moon():
    """Get only the Forsaken tribes (Tribes of the Moon)."""
    return TRIBES_OF_THE_MOON.copy()

def get_pure_tribes():
    """Get only the Pure tribes."""
    return PURE_TRIBES.copy()

def get_lodge(lodge_name):
    """Get a specific lodge by name."""
    lodge_key = lodge_name.lower().replace(" ", "_")
    return ALL_LODGES.get(lodge_key)

def get_all_lodges():
    """Get all lodge data."""
    return ALL_LODGES.copy()

