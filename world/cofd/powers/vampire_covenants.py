"""
Vampire: The Requiem Covenants
Detailed covenant information for Chronicles of Darkness 2nd Edition.
Based on Vampire: The Requiem 2nd Edition and supplemental materials.
"""

# ============================================================================
# MAJOR COVENANTS
# ============================================================================

MAJOR_COVENANTS = {
    "carthian_movement": {
        "name": "Carthian Movement",
        "nickname": "Firebrands",
        "description": "The Revolution applies mortal solutions to immortal problems with modern and experimental government.",
        "advantage": "Carthian Law",
        "full_description": "The Carthian Movement is a modern covenant that rejects the old ways in favor of democracy, meritocracy, and progressive ideals. They experiment with mortal governance structures adapted for immortal society.",
        "book": "VTR 2e 32"
    },
    "circle_of_the_crone": {
        "name": "Circle of the Crone",
        "nickname": "Acolytes",
        "description": "The Mother's Army venerates female divinity, painful change, and the old ways remixed for the modern world.",
        "advantage": "Crúac",
        "full_description": "The Circle of the Crone practices ancient blood sorcery and pagan spirituality, worshipping the dark mother goddess and embracing transformation through pain and sacrifice.",
        "book": "VTR 2e 35"
    },
    "invictus": {
        "name": "Invictus",
        "nickname": "Establishment",
        "description": "The Conspiracy of Silence safeguards the Masquerade with hierarchy and tradition.",
        "advantage": "Invictus Oaths",
        "full_description": "The Invictus is the covenant of aristocrats and oligarchs, maintaining power through tradition, oaths, and carefully cultivated social structures.",
        "book": "VTR 2e 38"
    },
    "lancea_et_sanctum": {
        "name": "Lancea et Sanctum",
        "nickname": "Sanctified",
        "description": "The Church Eternal preaches a dark faith; they are both wolves and shepherds.",
        "advantage": "Theban Sorcery",
        "full_description": "The Lancea et Sanctum is the covenant of dark Christianity, believing vampires are part of God's plan as predators and tests for humanity.",
        "book": "VTR 2e 41"
    },
    "ordo_dracul": {
        "name": "Ordo Dracul",
        "nickname": "Defiant",
        "description": "The Order of the Dragon struggles to transcend the Curses through eldritch alchemies and rites.",
        "advantage": "Mysteries of the Dragon",
        "full_description": "The Ordo Dracul seeks to transcend the limitations of vampirism through study of the Coils of the Dragon and other esoteric practices.",
        "book": "VTR 2e 44"
    },
    "belials_brood": {
        "name": "Belial's Brood",
        "nickname": "Claimed",
        "description": "Spontaneous clutches of ur-predators run riot, embracing monstrosity.",
        "advantage": "Triadic Evolution",
        "full_description": "Belial's Brood rejects humanity entirely, embracing the Beast and viewing vampirism as evolution rather than curse.",
        "book": "NH-SB 56"
    },
    "vii": {
        "name": "VII",
        "nickname": "Them",
        "description": "The bogeymen of the All Night Society. Unknown yet feared by all the other covenants.",
        "advantage": "Unknown",
        "full_description": "VII is a mysterious covenant that hunts other vampires. Little is known about their true nature or goals.",
        "book": "VTR 2e 47"
    },
}

# ============================================================================
# REGIONAL COVENANTS
# ============================================================================

REGIONAL_COVENANTS = {
    # Esoteric
    "esoteric_order_of_the_golden_star": {
        "name": "Esoteric Order of the Golden Star",
        "region": "Various",
        "description": "An opportunistic cult of personality disguised as a tradition of blood sorcery.",
        "advantage": "None",
        "book": "NH-SB 65"
    },
    
    # Athens, Greece
    "17n": {
        "name": "17N",
        "region": "Athens, Greece",
        "description": "Liberals trying to rebuild Greece, even if that means burning it all down and starting anew.",
        "advantage": "Unspecified",
        "book": "VTR 2e 241"
    },
    "alecto": {
        "name": "Alecto",
        "region": "Athens, Greece",
        "description": "Traditionalists who look inward to classical Greece and yearn for benevolent tyranny.",
        "advantage": "Unspecified",
        "book": "VTR 2e 241"
    },
    "kataraomenon": {
        "name": "Kataraomenon",
        "region": "Athens, Greece",
        "description": "Apollonian cultists who have blended their pagan traditions with Greek Orthodox Christianity.",
        "advantage": "Unspecified",
        "book": "VTR 2e 241"
    },
    "ypochtreosi": {
        "name": "Ypochtreosi",
        "region": "Athens, Greece",
        "description": "Iron-fisted pragmatic modernists who keep the domain stable through festivals, bribes, and skulduggery.",
        "advantage": "Unspecified",
        "book": "VTR 2e 241"
    },
    
    # Beijing, China
    "bureau_of_childer": {
        "name": "Bureau of Childer",
        "region": "Beijing, China",
        "description": "A bureaucracy empowered to keep track of childer and police the Embrace.",
        "advantage": "Unspecified",
        "book": "VTR 2e 244"
    },
    "bureau_of_silence": {
        "name": "Bureau of Silence",
        "region": "Beijing, China",
        "description": "An anonymous council which takes responsibility for the Masquerade and embeds itself into mortal politics.",
        "advantage": "Unspecified",
        "book": "VTR 2e 244"
    },
    "dragons_path": {
        "name": "Dragon's Path",
        "region": "Beijing, China",
        "description": "Students of the Mysteries who take power from the Beast by denying its hunger.",
        "advantage": "Unspecified",
        "book": "VTR 2e 244"
    },
    "way_of_the_dragon": {
        "name": "Way of the Dragon",
        "region": "Beijing, China",
        "description": "Students of the Mysteries who align their will with the Beast.",
        "advantage": "Unspecified",
        "book": "VTR 2e 244"
    },
    
    # Berlin, Germany
    "revolutionary_council": {
        "name": "Revolutionary Council",
        "region": "Berlin, Germany",
        "description": "Effectively Carthians by another name, inheriting the legacy of East Berlin's only Kindred state covenant.",
        "advantage": "Unspecified",
        "book": "VTR 2e 248"
    },
    "watchful_eyes": {
        "name": "Watchful Eyes",
        "region": "Berlin, Germany",
        "description": "A fanatical network of cells tasked by the markgraf to eliminate an unseen threat to Berlin's Kindred.",
        "advantage": "Unspecified",
        "book": "VTR 2e 248"
    },
    
    # Tokyo, Japan
    "hototogisu": {
        "name": "Hototogisu",
        "region": "Tokyo, Japan",
        "description": "Mortal intruders to the politics of the zaibatsu covenants, who exert influence over Kindred politics while honing occult means to defeat vampiric power.",
        "advantage": "Mystery Cult Initiation",
        "book": "VTR 2e 266"
    },
    "maeda_group": {
        "name": "Maeda Group",
        "region": "Tokyo, Japan",
        "description": "The muscle of the zaibatsu, legbreakers and assassins forced by changing times to shift investments from agriculture and retail into organized crime.",
        "advantage": "Mind of Infinite Immutability",
        "book": "VTR 2e 267"
    },
    "takahashi_family": {
        "name": "Takahashi Family",
        "region": "Tokyo, Japan",
        "description": "A technocratic zaibatsu organized in a pyramid structure, entangled with industry and the Hototogisu.",
        "advantage": "Free Retainers, Herd, and Haven",
        "book": "VTR 2e 268"
    },
    "ume_house": {
        "name": "Ume House",
        "region": "Tokyo, Japan",
        "description": "A spiritualist zaibatsu covenant that makes practical inroads into other concerns by selling the use of its ancient Kigan sorcery.",
        "advantage": "Kigan",
        "book": "VTR 2e 268"
    },
}

# ============================================================================
# HISTORICAL COVENANTS
# ============================================================================

HISTORICAL_COVENANTS = {
    "camarilla": {
        "name": "Camarilla",
        "era": "Ancient Rome",
        "description": "The earliest Kindred state to rule over vast territories, with jurisdiction over the dead of the Roman republic and later empire.",
        "advantage": "Unspecified",
        "book": "VTR 2e 74"
    },
    "childrens_crusade": {
        "name": "Children's Crusade",
        "era": "12th-18th Century",
        "description": "Kindred tradition from the 12th to the 18th Century organized vampires Embraced as children into this covenant, until its secrets were discovered and it was destroyed.",
        "advantage": "Unspecified",
        "book": "VTR 2e 50"
    },
    "gallows_post": {
        "name": "Gallows Post",
        "era": "Late Medieval Europe",
        "description": "Part messenger service, part gang of highwayman, they maintained safe passage between cities for the dead of late medieval Europe.",
        "advantage": "Hangman's Code",
        "book": "VTR 2e 50 / DE 266 / DEC 92"
    },
    "legion_of_the_dead": {
        "name": "Legion of the Dead",
        "era": "High Medieval",
        "description": "Between the fall of the Camarilla and the High Medieval, the Kindred's professional armies devolved into this rowdy legion for hire, rich with cursed relics and spoils of war.",
        "advantage": "Unspecified",
        "book": "VTR 2e 50"
    },
    "tenth_choir": {
        "name": "Tenth Choir",
        "era": "Historical",
        "description": "Blasphemers who drink the blood of angels and flaunt the Blood as the power to murder God.",
        "advantage": "Therion",
        "book": "VTR 2e 51 / DE2 352"
    },
    
    # Abbasid Caliphate 832 CE
    "ahl_al_mumit": {
        "name": "Ahl al-Mumit",
        "era": "Abbasid Caliphate 832 CE",
        "description": "Wrathful and righteous soldiers that hunt those who revel in their monstrosity.",
        "advantage": "Theban Sorcery",
        "book": "DE2 139"
    },
    "al_amin": {
        "name": "al-Amin",
        "era": "Abbasid Caliphate 832 CE",
        "description": "Record keepers and traditionalists who teach the Kindred's place under the law.",
        "advantage": "Shahrayad's Tale",
        "book": "DE2 139"
    },
    "firawn": {
        "name": "Fir'awn",
        "era": "Abbasid Caliphate 832 CE",
        "description": "Apostates and pagans who seek wisdom in old and strange ways.",
        "advantage": "Crúac",
        "book": "DE2 140"
    },
    "jaliniyya": {
        "name": "Jaliniyya",
        "era": "Abbasid Caliphate 832 CE",
        "description": "Students of occult sciences who pursue practical applications of blood alchemy.",
        "advantage": "Kimiya",
        "book": "DE2 140"
    },
    
    # Britannia 400-500 CE
    "circles_of_mor": {
        "name": "Circles of Mor",
        "era": "Britannia 400-500 CE",
        "description": "Cells of vicious eldritch predators practicing rites of power and cruelty.",
        "advantage": "Crúac",
        "book": "DE2 110"
    },
    "legion_of_the_green": {
        "name": "Legion of the Green",
        "era": "Britannia 400-500 CE",
        "description": "Feudal knights errant who fought against and alongside fae courts.",
        "advantage": "Invictus Oaths",
        "book": "DE2 108"
    },
    "weihan_cynn": {
        "name": "Weihan Cynn",
        "era": "Britannia 400-500 CE",
        "description": "An ancient and archaic British covenant of Woods-Witches who forged deals with other creatures of the night.",
        "advantage": "Contracts with the Uncanny",
        "book": "DE 270"
    },
}

# ============================================================================
# COMBINED COVENANT DATA
# ============================================================================

ALL_COVENANTS_DETAILED = {
    **MAJOR_COVENANTS,
    **REGIONAL_COVENANTS,
    **HISTORICAL_COVENANTS
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_covenant(covenant_name):
    """Get a specific covenant by name."""
    covenant_key = covenant_name.lower().replace(" ", "_").replace("'", "")
    return ALL_COVENANTS_DETAILED.get(covenant_key)

def get_all_covenants():
    """Get all covenant data."""
    return ALL_COVENANTS_DETAILED.copy()

def get_major_covenants():
    """Get only the major covenants."""
    return MAJOR_COVENANTS.copy()

def get_regional_covenants():
    """Get regional covenants."""
    return REGIONAL_COVENANTS.copy()

def get_historical_covenants():
    """Get historical covenants."""
    return HISTORICAL_COVENANTS.copy()

