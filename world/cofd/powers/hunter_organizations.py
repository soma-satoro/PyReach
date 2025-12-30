"""
Hunter: The Vigil Organizations - Compacts and Conspiracies
Complete listing of all hunter organizations with status benefits.
Based on Hunter: The Vigil 2nd Edition and Tooth and Nail.
"""

# ============================================================================
# COMPACTS
# ============================================================================

ALL_COMPACTS = {
    "ashwood_abbey": {
        "name": "Ashwood Abbey",
        "type": "compact",
        "description": "A decadent Hellfire Club dedicated to experiencing everything that life (or unlife) has to offer.",
        "status_benefits": {
            1: "Receive the Barfly Merit.",
            3: "Use local chapterhouse as a Safe Place ** with Home Security, Arsenal, and Escape Hatch.",
            5: "Receive Contacts among lawyers, vice, arms traffic, and the Abbey."
        },
        "book": "HTV 2e 265 / TF 12"
    },
    "crimson_halo": {
        "name": "Crimson Halo",
        "type": "compact",
        "description": "Sex workers protecting the victimized from supernatural and human monsters alike.",
        "status_benefits": {
            1: "Take a free Persuasion or Streetwise specialty.",
            3: "Receive the Sympathetic merit.",
            5: "Receive three dots of Allies or Contacts."
        },
        "book": "TF 14"
    },
    "crossroads_convoy": {
        "name": "Crossroads Convoy",
        "type": "compact",
        "description": "Travelers who have pledged to keep the roads safe for all.",
        "status_benefits": {
            1: "Receive the Back Road Atlas or Direction Sense merits.",
            3: "Receive two dots of Contacts.",
            5: "Receive three separate one-dot Safe Places."
        },
        "book": "TF 16"
    },
    "eden_covenant": {
        "name": "Eden Covenant",
        "type": "compact",
        "description": "A compact divided between those dedicated to helping the families of those replaced by monsters, and an extremist preacher's crusade against monsters who would become human.",
        "status_benefits": {
            1: "Take 8-Again on Identification or Profiling Tactic rolls.",
            3: "Receive the Sympathetic merit.",
            5: "Receive the Inspiring merit."
        },
        "book": "TF 18"
    },
    "keepers_of_the_source": {
        "name": "Keepers of the Source",
        "type": "compact",
        "description": "Environmental activists convinced that witches are causing Mother Earth pain by siphoning the Source.",
        "status_benefits": {
            1: "Take a free Expression, Occult, or Politics specialty.",
            3: "Receive the Unseen Sense merit for the Source.",
            5: "Receive three dots between Allies, Contacts, and Resources."
        },
        "book": "TF 20"
    },
    "las_guadanas": {
        "name": "Las Guadanas",
        "type": "compact",
        "description": "Criminal syndicate Death cult dedicated to eliminating the dead and undead who have cheated the Lady.",
        "status_benefits": {
            1: "Take a free Larceny or Streetwise specialty.",
            3: "Receive two dots of Resources - crime does, in fact, pay.",
            5: "Receive the Medium merit."
        },
        "book": "TF 22"
    },
    "the_long_night": {
        "name": "The Long Night",
        "type": "compact",
        "description": "Christian hunters who fight to save souls amid what they believe is the Great Tribulation.",
        "status_benefits": {
            1: "Receive Evangelism as a free specialty.",
            3: "Receive two dots in Allies (Long Night).",
            5: "Aides serve as three dots of Staff or Retainer."
        },
        "book": "HTV 2e 20"
    },
    "the_loyalists_of_thule": {
        "name": "The Loyalists of Thule",
        "type": "compact",
        "description": "Paranoid academics haunted by history, hoping to shepherd occult knowledge.",
        "status_benefits": {
            1: "Gain extra Willpower from a successful Academics or Occult risk.",
            3: "Receive a two-dot Mentor.",
            5: "Receive Contacts among specialists in three monstrous phenomena."
        },
        "book": "HTV 2e 22"
    },
    "network_zero": {
        "name": "Network Zero",
        "type": "compact",
        "description": "Network Zero uses radio, television and Internet resources to publicize monsters to the world.",
        "status_benefits": {
            1: "Take a free Computer or Crafts specialty.",
            3: "Take two dots of social media Contacts.",
            5: "Receive a dot of Safe Place."
        },
        "book": "HTV 2e 24"
    },
    "night_watch": {
        "name": "Night Watch",
        "type": "compact",
        "description": "The Night Watch protects neighborhoods from things that go bump in the night.",
        "status_benefits": {
            1: "Take a free Brawl, Firearms, Streetwise, or Weaponry specialty.",
            3: "Take two dots of Retainers.",
            5: "Receive three dots of Allies."
        },
        "book": "TF 24"
    },
    "nine_stars": {
        "name": "Nine Stars",
        "type": "compact",
        "description": "A fraternity of police putting their lives and jobs at risk to investigate and stem an upswell of slasher killings.",
        "status_benefits": {
            1: "Take a free Investigation or Occult specialty.",
            3: "Take 8-Again on Tactic rolls.",
            5: "Receive the effects of Trained Observer:3."
        },
        "book": "HTV 2e 26"
    },
    "null_mysteriis": {
        "name": "Null Mysteriis",
        "type": "compact",
        "description": "Scientists who pursue the supernatural in an attempt to understand it.",
        "status_benefits": {
            1: "Receive an Academics, Occult, or Science specialty in the paranormal.",
            3: "Receive a dot each of Allies and Contacts among Null Mysteriis.",
            5: "Raise Academics, Occult, or Science to five dots."
        },
        "book": "HTV 2e 28"
    },
    "recalibrators": {
        "name": "Recalibrators",
        "type": "compact",
        "description": "Recalibrators cover up evidence of monstrous activity to keep them from the public's eye.",
        "status_benefits": {
            1: "Receive the Cover Tracks, Spin Doctor, or Untouchable merits.",
            3: "Receive two dots of Allies or Contacts you've extorted.",
            5: "Receive three dots of Retainers or Staff."
        },
        "book": "TF 26"
    },
    "sworn": {
        "name": "SWORN",
        "type": "compact",
        "description": "Community patrols protecting underserved indigenous neighborhoods.",
        "status_benefits": {
            1: "Receive a free specialty in Investigation, Streetwise, or Stealth.",
            3: "Receive a two-dot Mentor.",
            5: "Distribute three dots among Allies, Contacts, and Resources."
        },
        "book": "HTV 2e 30"
    },
    "the_union": {
        "name": "The Union",
        "type": "compact",
        "description": "Ragtag monster hunters from blue-collar labor backgrounds, putting their hands to work to keep their streets safe.",
        "status_benefits": {
            1: "Take 8-Again to apply your work experience to Teamwork and Tactics rolls.",
            3: "Receive two dots in Allies (The Union).",
            5: "Receive two dots of Resources."
        },
        "book": "HTV 2e 32"
    },
}

# ============================================================================
# CONSPIRACIES
# ============================================================================

ALL_CONSPIRACIES = {
    "aegis_kai_doru": {
        "name": "Aegis Kai Doru",
        "type": "conspiracy",
        "endowments": "Relics",
        "description": "Greek for 'Shield and Spear,' the Aegis Kai Doru searches the world for legendary artifacts to harness in its nigh-timeless battle against the forces of darkness.",
        "status_benefits": {
            1: "Investigation rolls seeking relics gain +2.",
            3: "Academics rolls pertaining to relics and archaeology gain +1.",
            5: "Receive the Gut Feeling Merit."
        },
        "book": "HTV 2e 268 / TF 28"
    },
    "the_ascending_ones": {
        "name": "The Ascending Ones",
        "type": "conspiracy",
        "endowments": "Elixirs",
        "description": "Alchemists who carry on a legacy of fighting back the darkness since ancient Egypt. They now struggle to adapt to modern conditions.",
        "status_benefits": {
            1: "Once per session, take 8-Again on a roll to recover Willpower.",
            3: "Receive two dots of Resources.",
            5: "Receive an initiate as a three-dot Retainer."
        },
        "book": "HTV 2e 34"
    },
    "asclepeion": {
        "name": "Asclepeion",
        "type": "conspiracy",
        "endowments": "Enkoimesis",
        "description": "Medics gifted extraordinary powers of healing by Asklepios, which they use to support other hunters.",
        "status_benefits": {
            1: "Receive a one-dot safe space with the Infirmary feature.",
            3: "Treat failed rolls to preform emergency medical care as having a single success.",
            5: "Receive three dots between Allies or Contacts among other hunters."
        },
        "book": "TF 30"
    },
    "campion_wildlife_services": {
        "name": "Campion Wildlife Services",
        "type": "conspiracy",
        "endowments": "Animal Control Kit",
        "description": "A wildlife control service that focuses on the subdual, capture, and euthanization of animalistic monsters.",
        "status_benefits": {
            1: "Receive a free specialty in Animal Ken, Occult, or Science.",
            3: "Receive two dots of Custom Gear Broker, or increase your existing rating by 1.",
            5: "Receive three dots between Allies, Contacts, and Resources."
        },
        "book": "TF 32"
    },
    "the_cheiron_group": {
        "name": "The Cheiron Group",
        "type": "conspiracy",
        "endowments": "Thaumatechnology",
        "description": "An international medical conglomerate that secretly finances a Field Projects Division to capture and render monsters for active ingredients.",
        "status_benefits": {
            1: "Receive a free specialty in Academics, Computer, or Investigation.",
            3: "Receive two dots of Allies within the Cheiron Group.",
            5: "Receive three dots of Resources."
        },
        "book": "HTV 2e 36"
    },
    "the_council_of_bones": {
        "name": "The Council of Bones",
        "type": "conspiracy",
        "endowments": "Perispiritism",
        "description": "A secret society of spiritualists safeguarding an ancient reaper's mark. They gather in secret to silence their enemies and cleanse death of the undead.",
        "status_benefits": {
            1: "Receive a free specialty in Occult or Investigation.",
            3: "Receive two dots of Contacts among other conspiracies.",
            5: "Receive a three-dot ghostly Retainer."
        },
        "book": "HTV 2e 38"
    },
    "enigmatics": {
        "name": "Enigmatics",
        "type": "conspiracy",
        "endowments": "Inspiration",
        "description": "Artists chasing wonder and inspiration in the shadows.",
        "status_benefits": {
            1: "Receive a free specialty in Crafts or Expression reflecting your favored artistic medium.",
            3: "Receive two dots of Allies, Mentor, or Resources reflecting a patron.",
            5: "Receive the Inspiring merit and gain the ability to use it through art, substituting Crafts for expression."
        },
        "book": "TF 34"
    },
    "the_lucifuge": {
        "name": "The Lucifuge",
        "type": "conspiracy",
        "endowments": "Castigations",
        "description": "Descendants of infernal bloodlines who wield the darkness against itself.",
        "status_benefits": {
            1: "Take a free specialty in a particular type of supernatural creature.",
            3: "You may call on two extra dots of Resources by requisitioning tools for the Vigil.",
            5: "Take the Lady Lucifuge as a four-dot Mentor."
        },
        "book": "HTV 2e 40"
    },
    "malleus_maleficarum": {
        "name": "Malleus Maleficarum",
        "type": "conspiracy",
        "endowments": "Benedictions",
        "description": "In the Middle Ages, the Malleus Maleficarum wielded the power of the Catholic Church against vampires. Even today, the order still carries on its secret war against Satan's children.",
        "status_benefits": {
            1: "Receive a free specialty in Occult, Investigation, or Streetwise.",
            3: "Receive a free dot of Status (Malleus Maleficarum).",
            5: "Receive three dots of Resources."
        },
        "book": "HTV 2e 42"
    },
    "operation_nebula": {
        "name": "Operation Nebula",
        "type": "conspiracy",
        "endowments": "Xenotechnology",
        "description": "Hunters who know the truth is out there - aliens have invaded. Most hunters don't take them seriously until they generate a cloaking field with a power cell pulled from a cryptid's corpse.",
        "status_benefits": {
            1: "Receive a dot in the Alternate Identity merit.",
            3: "Receive the Natural Tinkerer merit.",
            5: "Receive three dots of Contacts representing experts in fields."
        },
        "book": "TF 36"
    },
    "survivors_club": {
        "name": "Survivors Club",
        "type": "conspiracy",
        "endowments": "The Horror Within",
        "description": "Survivors of Slashers who channel the darkness within themselves to save others.",
        "status_benefits": {
            1: "Receive a free Academics, Investigation, or Occult specialty.",
            3: "Receive a two-dot retainer reflecting another club member.",
            5: "Receive three dots between Allies, Contacts, and Touchstone."
        },
        "book": "TF 38"
    },
    "task_force_valkyrie": {
        "name": "Task Force: VALKYRIE",
        "type": "conspiracy",
        "endowments": "Advanced Armory",
        "description": "This covert government anti-monster brigade draws from both military and intelligence communities. VALKYRIE agents are dispatched to control extranormal threats and suppress public knowledge.",
        "status_benefits": {
            1: "Receive a free Weaponry specialty.",
            3: "Receive two dots of Allies in VALKYRIE.",
            5: "Receive Contacts among high-level experts in three classified fields."
        },
        "book": "HTV 2e 44"
    },
    "vanguard_serial_crimes_unit": {
        "name": "Vanguard Serial Crimes Unit",
        "type": "conspiracy",
        "endowments": "Teleinformatics",
        "description": "The agents of VASCU assist police investigations and apprehensions of supernatural killers, using specially induced psychic abilities.",
        "status_benefits": {
            1: "Receive a free psychic specialty in Occult.",
            3: "Receive a free dot of Status in government or law enforcement.",
            5: "Receive the effects of the Tactical Insight Merit. If you possess the Merit, you may reroll a Tactic once per session."
        },
        "book": "HTV 2e 46"
    },
    "watchers": {
        "name": "Watchers",
        "type": "conspiracy",
        "endowments": "Lives Remembered",
        "description": "Reincarnated hunters preparing for the next Time of Monsters after living through the last one in a past life sixteen centuries ago.",
        "status_benefits": {
            1: "Receive a free specialty in any skill.",
            3: "Receive two dots of the Library merit.",
            5: "Receive three dots between Allies, Contacts, and Retainer."
        },
        "book": "TF 40"
    },
    "white_hare_society": {
        "name": "White Hare Society",
        "type": "conspiracy",
        "endowments": "Infusion",
        "description": "Explorers of alternate dimensions who know how to alchemically infuse themselves with their power.",
        "status_benefits": {
            1: "Receive an Academics or Occult specialty in your favored otherworld.",
            3: "Receive the Direction Sense merit and a Lucky Charm.",
            5: "Take 8-Again to apply tactics in your favored otherworld, or when instructed by another explorer in theirs."
        },
        "book": "TF 42"
    },
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_organization(org_name):
    """
    Get organization data by name (searches both compacts and conspiracies).
    
    Args:
        org_name (str): Name of the organization
        
    Returns:
        dict or None: Organization data if found
    """
    org_key = org_name.lower().replace(" ", "_").replace(":", "")
    
    # Check compacts first
    if org_key in ALL_COMPACTS:
        return ALL_COMPACTS[org_key]
    
    # Check conspiracies
    if org_key in ALL_CONSPIRACIES:
        return ALL_CONSPIRACIES[org_key]
    
    return None

def get_all_organizations():
    """Get all organizations (both compacts and conspiracies)."""
    return {**ALL_COMPACTS, **ALL_CONSPIRACIES}

def get_compact_names():
    """Get list of all compact names for validation."""
    return list(ALL_COMPACTS.keys())

def get_conspiracy_names():
    """Get list of all conspiracy names for validation."""
    return list(ALL_CONSPIRACIES.keys())

def get_all_organization_names():
    """Get list of all organization names (both compacts and conspiracies)."""
    return list(ALL_COMPACTS.keys()) + list(ALL_CONSPIRACIES.keys())

def get_organization_summary(org_name):
    """
    Get a formatted summary of an organization.
    
    Args:
        org_name (str): Name of the organization
        
    Returns:
        str: Formatted summary or error message
    """
    org_data = get_organization(org_name)
    if not org_data:
        return f"Organization '{org_name}' not found."
    
    summary = []
    summary.append(f"=== {org_data['name']} ===")
    summary.append(f"Type: {org_data['type'].title()}")
    
    if org_data.get('endowments'):
        summary.append(f"Endowments: {org_data['endowments']}")
    
    summary.append(f"\n{org_data['description']}")
    
    summary.append(f"\nStatus Benefits:")
    for level, benefit in sorted(org_data['status_benefits'].items()):
        dots = "*" * level
        summary.append(f"  {dots} - {benefit}")
    
    summary.append(f"\nSource: {org_data['book']}")
    
    return "\n".join(summary)
