"""
Changeling Template Definition for Chronicles of Darkness.
Changeling: The Lost template with Seeming, Court, and Kith validations.
"""

from . import register_template

# Valid seemings for Changeling characters
CHANGELING_SEEMINGS = [
    "beast", "darkling", "elemental", "fairest", "ogre", "wizened"
]

# Valid courts for Changeling characters  
CHANGELING_COURTS = [
    "spring", "summer", "autumn", "winter", "courtless",
    "morning", "day", "night", "barter", "coins", "favors", "shady_deals",
    "high_tide", "low_tide", "flood_tide", "ebb_tide"
]

# Valid kiths for Changeling characters (2nd Edition)
CHANGELING_KITHS = [
    # Base Changeling: The Lost 2nd Edition kiths
    "artist", "bright_one", "chatelaine", "gristlegrinder", "helldiver", "hunterheart", 
    "leechfinger", "mirrorskin", "nightsinger", "notary", "playmate", "snowskin",
    
    # Kith & Kin - Crown kiths
    "absinthial", "climacteric", "concubus", "draconic", "flowering", "ghostheart", 
    "moonborn", "uttervoice",
    
    # Kith & Kin - Jewels kiths
    "delver", "glimmerwisp", "manikin", "oculus", "polychromatic", "veneficus", "witchtooth",
    
    # Kith & Kin - Mirror kiths
    "bricoleur", "cloakskin", "doppelganger", "lethipomp", "lullescent", "riddleseeker", 
    "sideromancer", "spiegelbild",
    
    # Kith & Kin - Shield kiths
    "asclepian", "bridgeguard", "librorum", "liminal", "reborn", "stoneflesh", "wisewitch",
    
    # Kith & Kin - Steed kiths
    "airtouched", "chalomot", "chevalier", "farwalker", "flickerflash", "levinquick", 
    "swarmflight", "swimmerskin",
    
    # Kith & Kin - Sword kiths
    "bearskin", "beastcaller", "cyclopean", "plaguesmith", "razorhand", "sandharrowed", 
    "valkyrie", "venombite",
    
    # Kith & Kin - Additional kiths
    "apoptosome", "becquerel", "blightbent", "enkrateia", "gravewight", "shadowsoul", 
    "telluric", "whisperwisp",
    
    # Dark Eras 2 kiths
    "nymph", "dryad", "cleverquick"
]

# Valid entitlements for Changeling characters
CHANGELING_ENTITLEMENTS = [ 
    "Baron of the Lesser Ones", "Dauphines of Wayward Children", "Master of Keys", "Modiste of Elfhame", "Thorn Dancer", "Sibylline Fishers", "Spiderborn Riders"
]

# Valid changeling contracts (2nd Edition) - Individual contract powers
CHANGELING_CONTRACTS = [
    # Crown Contracts
    "hostile_takeover", "mask_of_superiority", "paralyzing_presence", "summon_the_loyal_servant", "tumult",
    # Royal Crown Contracts
    "discreet_summons", "masterminds_gambit", "pipes_of_the_beastcaller", "the_royal_court", "spinning_wheel",
    # Jewels Contracts
    "blessing_of_perfection", "changing_fortunes", "light_shy", "murkblur", "trivial_reworking",
    # Royal Jewels Contracts
    "changeling_hours", "dance_of_the_toys", "hidden_reality", "stealing_the_solid_reflection", "tatterdemalions_workshop",
    # Mirror Contracts
    "glimpse_of_a_distant_mirror", "know_the_competition", "portents_and_visions", "read_lucidity", "walls_have_ears",
    # Royal Mirror Contracts
    "props_and_scenery", "reflections_of_the_past", "riddle_kith", "skinmask", "unravel_the_tapestry",
    # Shield Contracts
    "cloak_of_night", "fae_cunning", "shared_burden", "thorns_and_brambles", "trapdoor_spiders_trick",
    # Royal Shield Contracts
    "fortifying_presence", "hedgewall", "pure_clarity", "vow_of_no_compromise", "whispers_of_morning",
    # Steed Contracts
    "boon_of_the_scuttling_spider", "dreamsteps", "nevertread", "pathfinder", "seven_league_leap",
    # Royal Steed Contracts
    "chrysalis", "flickering_hours", "leaping_toward_nightfall", "mirror_walk", "talon_and_wing",
    # Sword Contracts
    "elemental_weapon", "might_of_the_terrible_brute", "overpowering_dread", "primal_glory", "touch_of_wrath",
    # Royal Sword Contracts
    "elemental_fury", "oathbreakers_punishment", "red_revenge", "relentless_pursuit", "thief_of_reason",
    # Chalice Contracts
    "filling_the_cup", "frail_as_the_dying_word", "sleeps_sweet_embrace", "curses_cure", "dreamers_phalanx",
    # Royal Chalice Contracts
    "closing_deaths_door", "feast_of_plenty", "still_waters_run_deep", "poison_the_well", "shared_cup",
    # Coin Contracts
    "book_of_black_and_red", "give_and_take", "beggar_knight", "coin_mark", "grease_the_wheels",
    # Royal Coin Contracts
    "blood_debt", "exchange_of_gilded_contracts", "golden_promise", "grand_revel_of_the_harvest", "thirty_pieces",
    # Scepter Contracts
    "burning_ambition", "jealous_vengeance", "litany_of_rivals", "knights_oath", "unmask_the_dark_horse",
    # Royal Scepter Contracts
    "a_benevolent_hand", "fake_it_til_you_make_it", "tempters_quest", "curse_of_hidden_strings", "spare_not_the_rod",
    # Stars Contracts
    "pole_star", "straight_on_til_morning", "cynosure", "shooting_star", "retrograde",
    # Royal Stars Contracts
    "frozen_star", "star_light_star_bright", "light_of_ancient_stars", "pinch_of_stardust",
    # Thorn Contracts
    "briars_herald", "by_the_pricking_of_my_thumbs", "thistles_rebuke", "the_gouging_curse", "embrace_of_nettles",
    # Royal Thorn Contracts
    "acanthas_fury", "awaken_portal", "crown_of_thorns", "shrikes_larder", "witchs_brambles",
    # Spring Contracts
    "cupids_arrow", "dreams_of_the_earth", "gift_of_warm_breath", "springs_kiss", "wyrd_faced_stranger",
    # Royal Spring Contracts
    "blessing_of_spring", "gift_of_warm_blood", "pandoras_gift", "prince_of_ivy", "waking_the_inner_fae",
    # Summer Contracts
    "baleful_sense", "child_of_the_hearth", "helios_light", "high_summers_zeal", "vigilance_of_ares",
    # Royal Summer Contracts
    "fiery_tongue", "flames_of_summer", "helios_judgment", "solstice_revelation", "sunburnt_heart",
    # Autumn Contracts
    "autumns_fury", "last_harvest", "tale_of_the_baba_yaga", "twilights_harbinger", "witches_intuition",
    # Royal Autumn Contracts
    "famines_bulwark", "mien_of_the_baba_yaga", "riding_the_falling_leaves", "sorcerers_rebuke", "tasting_the_harvest",
    # Winter Contracts
    "the_dragon_knows", "heart_of_ice", "ice_queens_call", "slipknot_dreams", "touch_of_winter",
    # Royal Winter Contracts
    "ermines_winter_coat", "fallow_fields", "field_of_regret", "mantle_of_frost", "winters_curse",
    # Retaliation Contracts
    "peacemakers_draw", "draw_likeness",
    # Goblin Contracts
    "blessing_of_forgetfulness", "distill_the_hidden", "glib_tongue", "goblins_eye", "goblins_luck",
    "huntsmans_clarion", "lost_visage", "mantle_mask", "sight_of_truth_and_lies", "uncanny", "wayward_guide", "wyrd_debt",
    # Independent Arcadian Contracts
    "coming_darkness", "pomp_and_circumstance", "shadow_puppet", "steal_influence", "earths_gentle_movements",
    "dread_companion", "cracked_mirror", "listen_with_winds_ears", "momentary_respite", "earths_impenetrable_walls"
]

# Changeling template definition
CHANGELING_TEMPLATE = {
    "name": "changeling",
    "display_name": "Changeling", 
    "description": ("Changelings are humans who were taken to the realm of the True Fae and "
                   "transformed, eventually escaping back to the mortal world. They are organized "
                   "by their Seemings (what they became) and Courts (seasonal affiliations)."),
    "bio_fields": ["needle", "thread", "seeming", "court", "kith", "keeper", "motley", "entitlement"],
    "integrity_name": "Clarity",
    "starting_integrity": 7,
    "supernatural_power_stat": "wyrd",
    "starting_power_stat": 1,
    "resource_pool": "glamour",
    "power_systems": CHANGELING_CONTRACTS,
    "anchors": ["needle", "thread"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "changeling"],
    "field_validations": {
        "seeming": {
            "valid_values": CHANGELING_SEEMINGS
        },
        "court": {
            "valid_values": CHANGELING_COURTS
        },
        "kith": {
            "valid_values": CHANGELING_KITHS
        },
        "entitlement": {
            "valid_values": CHANGELING_ENTITLEMENTS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Changeling: The Lost",
    "notes": "Enhanced Changeling template with Wyrd, Contracts, and Glamour pool"
}

# Register the template
register_template(CHANGELING_TEMPLATE)


# Power list helper functions
def get_primary_powers():
    """Get list of primary changeling powers (contracts - individual abilities)."""
    return CHANGELING_CONTRACTS.copy()


def get_secondary_powers():
    """Get list of secondary changeling powers (none - all powers are contracts)."""
    return []


def get_all_powers():
    """Get all changeling powers for validation."""
    return CHANGELING_CONTRACTS.copy() 