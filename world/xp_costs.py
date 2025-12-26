"""
XP Cost Calculator for Chronicles of Darkness Templates

This module calculates experience costs for various abilities based on
character template, affinity, and other factors.
"""

# =============================================================================
# GENERAL COSTS (All Templates)
# =============================================================================

GENERAL_COSTS = {
    'merit': 1,  # per dot
    'skill_specialty': 1,  # per specialty
    'lost_willpower': 1,  # per dot restored
    'attribute': 4,  # per dot
    'skill': 2,  # per dot
    'integrity': 2,  # per dot
}

# =============================================================================
# WEREWOLF COSTS
# =============================================================================

WEREWOLF_COSTS = {
    'affinity_gift': 3,
    'non_affinity_gift': 5,
    'additional_facet': 2,
    'wolf_gift_facet': 1,
    'renown': 3,  # per dot
    'rite': 1,
    'primal_urge': 5,  # per dot
}

# Auspice Affinity Gifts
WEREWOLF_AUSPICE_AFFINITIES = {
    'cahalith': ['gibbous_moon', 'inspiration', 'knowledge'],
    'elodoth': ['half_moon', 'insight', 'warding'],
    'irraka': ['new_moon', 'evasion', 'stealth'],
    'ithaeur': ['crescent_moon', 'elemental', 'shaping'],
    'rahu': ['full_moon', 'dominance', 'strength'],
}

# Tribe Affinity Gifts
WEREWOLF_TRIBE_AFFINITIES = {
    'blood_talons': ['inspiration', 'rage', 'strength'],
    'bone_shadows': ['death', 'elemental', 'insight'],
    'hunters_in_darkness': ['nature', 'stealth', 'warding'],
    'iron_masters': ['knowledge', 'shaping', 'technology'],
    'storm_lords': ['evasion', 'dominance', 'weather'],
    'ghost_wolves': [],  # No tribal affinities
}

# =============================================================================
# CHANGELING COSTS
# =============================================================================

CHANGELING_COSTS = {
    'common_contract': 3,
    'royal_contract': 4,
    'favored_common_contract': 2,
    'favored_royal_contract': 3,
    'goblin_contract': 2,
    'out_of_seeming_benefit': 1,
    'wyrd': 5,  # per dot
}

# Kith Favored Regalia
CHANGELING_KITH_REGALIA = {
    'beast': 'steed',
    'darkling': 'mirror',
    'elemental': 'sword',
    'fairest': 'crown',
    'ogre': 'shield',
    'wizened': 'jewels',
}

# Contract-to-Regalia mapping
# This maps contract names to which regalia they belong to
CHANGELING_CONTRACT_REGALIA = {
    # Crown Contracts
    'sovereign_voice': 'crown',
    'grand_entrance': 'crown',
    'words_of_kings': 'crown',
    'noble_bearing': 'crown',
    'mantle_of_authority': 'crown',
    
    # Jewels Contracts
    'sleight_of_hand': 'jewels',
    'hidden_prize': 'jewels',
    'master_artisan': 'jewels',
    'perfect_fit': 'jewels',
    'exquisite_craftsmanship': 'jewels',
    
    # Mirror Contracts
    'reflections_of_the_past': 'mirror',
    'glimpse_of_fortunes_wheel': 'mirror',
    'reading_the_mortal_coil': 'mirror',
    'the_eye_of_fate': 'mirror',
    'vision_of_things_to_come': 'mirror',
    
    # Shield Contracts
    'armor_of_elements_fury': 'shield',
    'beasts_keen_senses': 'shield',
    'might_of_the_terrible_brute': 'shield',
    'trolls_recovery': 'shield',
    'ogres_rending_grasp': 'shield',
    
    # Steed Contracts
    'footsteps_of_the_fog': 'steed',
    'travelers_speed': 'steed',
    'wings_of_mercury': 'steed',
    'riders_of_the_storm': 'steed',
    'the_eternal_journey': 'steed',
    
    # Sword Contracts
    'cloak_of_night': 'sword',
    'impenetrable_veil': 'sword',
    'lightfoot_step': 'sword',
    'murkblur': 'sword',
    'shadow_scry': 'sword',
}

# =============================================================================
# DEMON COSTS
# =============================================================================

DEMON_COSTS = {
    'embed': 2,
    'exploit': 2,
    'primum': 5,  # per dot
    'cover': 3,  # per dot
}

# =============================================================================
# GEIST COSTS
# =============================================================================

GEIST_COSTS = {
    'affinity_haunt': 3,  # per dot
    'non_affinity_haunt': 4,  # per dot
    'ceremony': 2,
    'synergy': 5,  # per dot
}

# Burden Affinity Haunts
GEIST_BURDEN_AFFINITIES = {
    'the_abiding': ['the_caul', 'the_memoria', 'the_tomb'],
    'the_bereaved': ['the_curse', 'the_oracle', 'the_shroud'],
    'the_hungry': ['the_boneyard', 'the_caul', 'the_marionette'],
    'the_kindly': ['the_dirge', 'the_marionette', 'the_shroud'],
    'the_vengeful': ['the_dirge', 'the_marionette', 'the_shroud'],
}

# =============================================================================
# HUNTER COSTS
# =============================================================================

HUNTER_COSTS = {
    'endowment': 3,
}

# =============================================================================
# DEVIANT COSTS
# =============================================================================

DEVIANT_COSTS = {
    'variation': 4,  # per dot (must have entangled Scar)
    'acclimation': 5,  # (must meet criteria)
}

# =============================================================================
# VAMPIRE COSTS
# =============================================================================

VAMPIRE_COSTS = {
    'clan_discipline': 3,  # per dot
    'out_of_clan_discipline': 4,  # per dot
    'coil_in_mystery': 3,  # per dot
    'coil_out_mystery': 4,  # per dot
    'cruac': 4,  # per dot
    'theban_sorcery': 4,  # per dot
    'blood_ritual': 2,
    'scale_of_dragon': 2,
    'humanity': 2,  # per dot
    'blood_potency': 5,  # per dot
}

# Clan In-Clan Disciplines
VAMPIRE_CLAN_DISCIPLINES = {
    'daeva': ['celerity', 'majesty', 'vigor'],
    'gangrel': ['animalism', 'protean', 'resilience'],
    'mekhet': ['auspex', 'celerity', 'obfuscate'],
    'nosferatu': ['nightmare', 'obfuscate', 'vigor'],
    'ventrue': ['animalism', 'dominate', 'resilience'],
}

# Bloodline In-Clan Disciplines (in addition to clan)
VAMPIRE_BLOODLINE_DISCIPLINES = {
    'parliamentarians': ['animalism', 'auspex', 'celerity', 'majesty'],
    'penumbrae': ['auspex', 'celerity', 'cruac', 'vigor'],
    'scions_of_the_first_city': ['animalism', 'auspex', 'obfuscate', 'resilience'],
    'jharana': ['auspex', 'dead_signal', 'celerity', 'vigor'],
    'liderc': ['celerity', 'majesty', 'obfuscate', 'vigor'],
    'vilseduire': ['majesty', 'nightmare', 'obfuscate', 'resilience'],
    'kerberos': ['animalism', 'majesty', 'protean', 'resilience'],
    'nosoi': ['dominate', 'obfuscate', 'protean', 'resilience'],
    'ankou': ['auspex', 'celerity', 'obfuscate', 'vigor'],
    'icelus': ['auspex', 'dominate', 'obfuscate', 'resilience'],
    'khaibit': ['auspex', 'celerity', 'obfuscate', 'vigor'],
    'morbus': ['auspex', 'celerity', 'cachexy', 'obfuscate'],
    'bron': ['animalism', 'crochan', 'dominate', 'resilience'],
    'vardvyle': ['dominate', 'obfuscate', 'protean', 'resilience'],
}

# =============================================================================
# PROMETHEAN COSTS
# =============================================================================

PROMETHEAN_COSTS = {
    'azoth_normal': 5,  # per dot, normal XP
    'azoth_vitriol': 4,  # per dot, vitriol XP
    'pilgrimage': 3,  # vitriol XP only
    'calcify_alembic': 2,  # vitriol XP only
    'create_athanor': 1,  # vitriol XP only
}

# =============================================================================
# MUMMY COSTS
# =============================================================================

MUMMY_COSTS = {
    'affinity': 4,
    'utterance': 4,
    'defining_pillar': 2,  # per dot
    'other_pillar': 3,  # per dot
    'memory': 3,  # per dot, reminisce XP only
    'cult_attribute': 6,  # per dot (Reach, Grasp)
    'cult_merit': 1,  # per dot
    'dominance': 5,  # per dot
}

# =============================================================================
# MAGE COSTS
# =============================================================================

MAGE_COSTS = {
    'arcanum_to_limit': 4,  # per dot (can use normal or arcane XP)
    'arcanum_above_limit': 5,  # per dot (normal XP only)
    'gnosis': 5,  # per dot (can use normal or arcane XP)
    'rote': 1,  # (can use normal or arcane XP)
    'praxis': 1,  # (arcane XP only)
    'wisdom': 2,  # per dot (arcane XP only)
}

# Path Ruling and Inferior Arcana
MAGE_PATH_ARCANA = {
    'acanthus': {
        'ruling': ['time', 'fate'],
        'inferior': ['forces']
    },
    'mastigos': {
        'ruling': ['space', 'mind'],
        'inferior': ['matter']
    },
    'moros': {
        'ruling': ['matter', 'arcanum_death'],
        'inferior': ['spirit']
    },
    'obrimos': {
        'ruling': ['forces', 'prime'],
        'inferior': ['arcanum_death']
    },
    'thyrsus': {
        'ruling': ['life', 'spirit'],
        'inferior': ['mind']
    },
}

# Arcanum Limits before gnosis increase is needed
MAGE_ARCANUM_LIMITS = {
    'ruling': 5,
    'common': 4,
    'inferior': 2,
}

# =============================================================================
# MORTAL+ COSTS
# =============================================================================

# Dhampir
DHAMPIR_COSTS = {
    'twist': 1,  # per dot
    'in_clan_theme': 1,  # per dot
    'out_of_clan_theme': 2,  # per dot
    'malison': 3,
}

# Fae-Touched (same as Changeling contracts)
FAE_TOUCHED_COSTS = {
    'common_contract': 3,
    'royal_contract': 4,
    'favored_common_contract': 2,
    'favored_royal_contract': 3,
    'goblin_contract': 2,
}

# Ghoul/Revenant (same as Vampire disciplines)
GHOUL_COSTS = {
    'clan_discipline': 3,  # per dot
    'out_of_clan_discipline': 4,  # per dot
    'coil_in_mystery': 3,  # per dot
    'coil_out_mystery': 4,  # per dot
    'cruac': 4,  # per dot
    'theban_sorcery': 4,  # per dot
    'blood_ritual': 2,
    'scale_of_dragon': 2,
}

# Proximi
PROXIMI_COSTS = {
    'blessing': 1,  # per dot (max 30 total dots across all blessings)
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_werewolf_affinity_gifts(character):
    """Get list of affinity gifts for a werewolf character."""
    stats = character.db.stats
    auspice = stats.get('bio', {}).get('auspice', '').lower()
    tribe = stats.get('bio', {}).get('tribe', '').lower()
    
    affinity_gifts = []
    
    if auspice in WEREWOLF_AUSPICE_AFFINITIES:
        affinity_gifts.extend(WEREWOLF_AUSPICE_AFFINITIES[auspice])
    
    if tribe in WEREWOLF_TRIBE_AFFINITIES:
        affinity_gifts.extend(WEREWOLF_TRIBE_AFFINITIES[tribe])
    
    return affinity_gifts


def get_geist_affinity_haunts(character):
    """Get list of affinity haunts for a Sin-Eater character."""
    stats = character.db.stats
    burden = stats.get('bio', {}).get('burden', '').lower()
    
    if burden in GEIST_BURDEN_AFFINITIES:
        return GEIST_BURDEN_AFFINITIES[burden]
    return []


def get_changeling_favored_regalia(character):
    """Get list of favored regalia for a Changeling character."""
    stats = character.db.stats
    kith = stats.get('bio', {}).get('kith', '').lower()
    
    favored_regalia = []
    
    if kith in CHANGELING_KITH_REGALIA:
        favored_regalia.append(CHANGELING_KITH_REGALIA[kith])
    
    second_regalia = stats.get('bio', {}).get('favored_regalia', '').lower()
    if second_regalia and second_regalia not in favored_regalia:
        favored_regalia.append(second_regalia)
    
    return favored_regalia


def is_changeling_contract_favored(character, contract_name):
    """Check if a contract belongs to a favored regalia."""
    contract_normalized = contract_name.lower().replace(' ', '_')
    contract_regalia = CHANGELING_CONTRACT_REGALIA.get(contract_normalized)
    
    if not contract_regalia:
        return False
    
    favored_regalia = get_changeling_favored_regalia(character)
    return contract_regalia in favored_regalia


def get_vampire_clan_disciplines(character):
    """Get list of in-clan disciplines for a vampire character."""
    stats = character.db.stats
    clan = stats.get('bio', {}).get('clan', '').lower()
    bloodline = stats.get('bio', {}).get('bloodline', '').lower()
    
    disciplines = []
    
    if clan in VAMPIRE_CLAN_DISCIPLINES:
        disciplines.extend(VAMPIRE_CLAN_DISCIPLINES[clan])
    
    if bloodline in VAMPIRE_BLOODLINE_DISCIPLINES:
        disciplines = VAMPIRE_BLOODLINE_DISCIPLINES[bloodline].copy()
    
    return disciplines


def get_mage_arcanum_type(character, arcanum):
    """Determine if an arcanum is ruling, common, or inferior for a mage."""
    stats = character.db.stats
    path = stats.get('bio', {}).get('path', '').lower()
    
    arcanum_normalized = arcanum.lower()
    if arcanum_normalized == 'death':
        arcanum_normalized = 'arcanum_death'
    
    if path not in MAGE_PATH_ARCANA:
        return 'common'
    
    path_data = MAGE_PATH_ARCANA[path]
    
    if arcanum_normalized in path_data['ruling']:
        return 'ruling'
    elif arcanum_normalized in path_data['inferior']:
        return 'inferior'
    else:
        return 'common'


def get_mage_arcanum_limit(character, arcanum):
    """Get the gnosis-based limit for an arcanum."""
    arcanum_type = get_mage_arcanum_type(character, arcanum)
    return MAGE_ARCANUM_LIMITS[arcanum_type]


def calculate_xp_cost(character, stat_type, stat_name, current_dots, target_dots, **kwargs):
    """
    Calculate XP cost for raising a stat.
    
    Args:
        character: The character object
        stat_type: Type of stat (e.g., 'gift', 'discipline', 'arcanum', 'merit')
        stat_name: Name of the specific stat
        current_dots: Current rating
        target_dots: Target rating
        **kwargs: Additional parameters (e.g., instance for merits)
    
    Returns:
        tuple: (cost, xp_type) where xp_type is 'normal', 'arcane', 'vitriol', or 'reminisce'
    """
    stats = character.db.stats
    template = stats.get('other', {}).get('template', 'Mortal').lower()
    dots_to_buy = target_dots - current_dots
    
    if dots_to_buy <= 0:
        return (0, 'normal')
    
    # General costs (all templates)
    if stat_type == 'merit':
        return (dots_to_buy * GENERAL_COSTS['merit'], 'normal')
    elif stat_type == 'skill_specialty':
        return (GENERAL_COSTS['skill_specialty'], 'normal')
    elif stat_type == 'lost_willpower':
        return (dots_to_buy * GENERAL_COSTS['lost_willpower'], 'normal')
    elif stat_type == 'attribute':
        return (dots_to_buy * GENERAL_COSTS['attribute'], 'normal')
    elif stat_type == 'skill':
        return (dots_to_buy * GENERAL_COSTS['skill'], 'normal')
    elif stat_type == 'integrity':
        return (dots_to_buy * GENERAL_COSTS['integrity'], 'normal')
    
    # Template-specific costs
    if template == 'werewolf':
        return _calculate_werewolf_cost(character, stat_type, stat_name, dots_to_buy)
    elif template == 'changeling':
        return _calculate_changeling_cost(character, stat_type, stat_name, dots_to_buy)
    elif template == 'vampire':
        return _calculate_vampire_cost(character, stat_type, stat_name, dots_to_buy)
    elif template == 'mage':
        return _calculate_mage_cost(character, stat_type, stat_name, current_dots, target_dots)
    elif template == 'demon':
        return _calculate_demon_cost(character, stat_type, stat_name, dots_to_buy)
    elif template == 'geist':
        return _calculate_geist_cost(character, stat_type, stat_name, dots_to_buy)
    elif template == 'hunter':
        return _calculate_hunter_cost(character, stat_type, stat_name, dots_to_buy)
    elif template == 'deviant':
        return _calculate_deviant_cost(character, stat_type, stat_name, dots_to_buy)
    elif template == 'promethean':
        return _calculate_promethean_cost(character, stat_type, stat_name, dots_to_buy)
    elif template == 'mummy':
        return _calculate_mummy_cost(character, stat_type, stat_name, dots_to_buy, **kwargs)
    elif template == 'mortal+':
        return _calculate_mortal_plus_cost(character, stat_type, stat_name, dots_to_buy)
    
    return (0, 'normal')  # Unknown template/stat


def _calculate_werewolf_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate werewolf-specific costs."""
    if stat_type == 'gift':
        affinity_gifts = get_werewolf_affinity_gifts(character)
        # Normalize gift name for comparison
        gift_normalized = stat_name.lower().replace(' ', '_')
        if gift_normalized in affinity_gifts:
            return (dots_to_buy * WEREWOLF_COSTS['affinity_gift'], 'normal')
        else:
            return (dots_to_buy * WEREWOLF_COSTS['non_affinity_gift'], 'normal')
    elif stat_type == 'renown':
        return (dots_to_buy * WEREWOLF_COSTS['renown'], 'normal')
    elif stat_type == 'rite':
        return (WEREWOLF_COSTS['rite'], 'normal')
    elif stat_type == 'primal_urge':
        return (dots_to_buy * WEREWOLF_COSTS['primal_urge'], 'normal')
    return (0, 'normal')


def _calculate_changeling_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate changeling-specific costs."""
    if stat_type == 'contract':
        is_favored = is_changeling_contract_favored(character, stat_name)
        is_royal = 'royal' in stat_name.lower()
        
        if is_favored:
            if is_royal:
                cost = CHANGELING_COSTS['favored_royal_contract']
            else:
                cost = CHANGELING_COSTS['favored_common_contract']
        else:
            if is_royal:
                cost = CHANGELING_COSTS['royal_contract']
            else:
                cost = CHANGELING_COSTS['common_contract']
        
        return (dots_to_buy * cost, 'normal')
    elif stat_type == 'goblin_contract':
        return (dots_to_buy * CHANGELING_COSTS['goblin_contract'], 'normal')
    elif stat_type == 'wyrd':
        return (dots_to_buy * CHANGELING_COSTS['wyrd'], 'normal')
    return (0, 'normal')


def _calculate_vampire_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate vampire-specific costs."""
    if stat_type == 'discipline':
        clan_disciplines = get_vampire_clan_disciplines(character)
        discipline_normalized = stat_name.lower().replace(' ', '_')
        if discipline_normalized in clan_disciplines:
            return (dots_to_buy * VAMPIRE_COSTS['clan_discipline'], 'normal')
        else:
            return (dots_to_buy * VAMPIRE_COSTS['out_of_clan_discipline'], 'normal')
    elif stat_type == 'cruac':
        # Special case: Penumbrae bloodline gets discount
        bloodline = character.db.stats.get('bio', {}).get('bloodline', '').lower()
        if bloodline == 'penumbrae':
            return (dots_to_buy * 3, 'normal')
        return (dots_to_buy * VAMPIRE_COSTS['cruac'], 'normal')
    elif stat_type == 'theban_sorcery':
        return (dots_to_buy * VAMPIRE_COSTS['theban_sorcery'], 'normal')
    elif stat_type == 'blood_ritual':
        return (VAMPIRE_COSTS['blood_ritual'], 'normal')
    elif stat_type == 'coil':
        return (dots_to_buy * VAMPIRE_COSTS['coil_in_mystery'], 'normal')
    elif stat_type == 'scale':
        return (VAMPIRE_COSTS['scale_of_dragon'], 'normal')
    elif stat_type == 'humanity':
        return (dots_to_buy * VAMPIRE_COSTS['humanity'], 'normal')
    elif stat_type == 'blood_potency':
        return (dots_to_buy * VAMPIRE_COSTS['blood_potency'], 'normal')
    return (0, 'normal')


def _calculate_mage_cost(character, stat_type, stat_name, current_dots, target_dots):
    """Calculate mage-specific costs."""
    if stat_type == 'arcanum':
        arcanum_type = get_mage_arcanum_type(character, stat_name)
        limit = MAGE_ARCANUM_LIMITS[arcanum_type]
        gnosis = character.db.stats.get('advantages', {}).get('gnosis', 1)
        
        # Calculate cost per dot based on whether it's below or above limit
        total_cost = 0
        for dot in range(current_dots + 1, target_dots + 1):
            if dot <= limit:
                total_cost += MAGE_COSTS['arcanum_to_limit']
            else:
                # Above limit requires normal XP only
                total_cost += MAGE_COSTS['arcanum_above_limit']
        
        # Can use arcane XP for dots up to limit
        if target_dots <= limit:
            return (total_cost, 'arcane_or_normal')
        else:
            # Mixed spending needed - calculate separately
            return (total_cost, 'mixed')
    elif stat_type == 'gnosis':
        dots_to_buy = target_dots - current_dots
        return (dots_to_buy * MAGE_COSTS['gnosis'], 'arcane_or_normal')
    elif stat_type == 'rote':
        return (MAGE_COSTS['rote'], 'arcane_or_normal')
    elif stat_type == 'praxis':
        return (MAGE_COSTS['praxis'], 'arcane_only')
    elif stat_type == 'wisdom':
        dots_to_buy = target_dots - current_dots
        return (dots_to_buy * MAGE_COSTS['wisdom'], 'arcane_only')
    return (0, 'normal')


def _calculate_demon_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate demon-specific costs."""
    if stat_type == 'embed':
        return (DEMON_COSTS['embed'], 'normal')
    elif stat_type == 'exploit':
        return (DEMON_COSTS['exploit'], 'normal')
    elif stat_type == 'primum':
        return (dots_to_buy * DEMON_COSTS['primum'], 'normal')
    elif stat_type == 'cover':
        return (dots_to_buy * DEMON_COSTS['cover'], 'normal')
    return (0, 'normal')


def _calculate_geist_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate geist-specific costs."""
    if stat_type == 'haunt':
        affinity_haunts = get_geist_affinity_haunts(character)
        haunt_normalized = stat_name.lower().replace(' ', '_')
        if haunt_normalized in affinity_haunts:
            return (dots_to_buy * GEIST_COSTS['affinity_haunt'], 'normal')
        else:
            return (dots_to_buy * GEIST_COSTS['non_affinity_haunt'], 'normal')
    elif stat_type == 'ceremony':
        return (GEIST_COSTS['ceremony'], 'normal')
    elif stat_type == 'synergy':
        return (dots_to_buy * GEIST_COSTS['synergy'], 'normal')
    return (0, 'normal')


def _calculate_hunter_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate hunter-specific costs."""
    if stat_type == 'endowment':
        return (HUNTER_COSTS['endowment'], 'normal')
    return (0, 'normal')


def _calculate_deviant_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate deviant-specific costs."""
    if stat_type == 'variation':
        return (dots_to_buy * DEVIANT_COSTS['variation'], 'normal')
    elif stat_type == 'acclimation':
        return (DEVIANT_COSTS['acclimation'], 'normal')
    return (0, 'normal')


def _calculate_promethean_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate promethean-specific costs."""
    if stat_type == 'azoth':
        # Can use either normal or vitriol XP
        normal_cost = dots_to_buy * PROMETHEAN_COSTS['azoth_normal']
        vitriol_cost = dots_to_buy * PROMETHEAN_COSTS['azoth_vitriol']
        return (normal_cost, 'normal_or_vitriol', vitriol_cost)
    elif stat_type == 'pilgrimage':
        return (dots_to_buy * PROMETHEAN_COSTS['pilgrimage'], 'vitriol_only')
    elif stat_type == 'calcify_alembic':
        return (PROMETHEAN_COSTS['calcify_alembic'], 'vitriol_only')
    elif stat_type == 'create_athanor':
        return (PROMETHEAN_COSTS['create_athanor'], 'vitriol_only')
    return (0, 'normal')


def _calculate_mummy_cost(character, stat_type, stat_name, dots_to_buy, **kwargs):
    """Calculate mummy-specific costs."""
    if stat_type == 'affinity':
        return (MUMMY_COSTS['affinity'], 'normal')
    elif stat_type == 'utterance':
        return (MUMMY_COSTS['utterance'], 'normal')
    elif stat_type == 'pillar':
        # Check if this is the defining pillar
        defining_pillar = character.db.stats.get('bio', {}).get('defining_pillar', '').lower()
        pillar_normalized = stat_name.lower().replace(' ', '_')
        if pillar_normalized == defining_pillar:
            return (dots_to_buy * MUMMY_COSTS['defining_pillar'], 'normal')
        else:
            return (dots_to_buy * MUMMY_COSTS['other_pillar'], 'normal')
    elif stat_type == 'memory':
        return (dots_to_buy * MUMMY_COSTS['memory'], 'reminisce_only')
    elif stat_type == 'cult_attribute':
        return (dots_to_buy * MUMMY_COSTS['cult_attribute'], 'normal')
    elif stat_type == 'cult_merit':
        return (dots_to_buy * MUMMY_COSTS['cult_merit'], 'normal')
    elif stat_type == 'dominance':
        return (dots_to_buy * MUMMY_COSTS['dominance'], 'normal')
    return (0, 'normal')


def _calculate_mortal_plus_cost(character, stat_type, stat_name, dots_to_buy):
    """Calculate mortal+ specific costs based on template_type."""
    stats = character.db.stats
    template_type = stats.get('bio', {}).get('template_type', '').lower()
    
    if template_type == 'dhampir':
        if stat_type == 'twist':
            return (dots_to_buy * DHAMPIR_COSTS['twist'], 'normal')
        elif stat_type == 'theme':
            return (dots_to_buy * DHAMPIR_COSTS['in_clan_theme'], 'normal')
        elif stat_type == 'malison':
            return (DHAMPIR_COSTS['malison'], 'normal')
    
    elif template_type == 'fae_touched':
        if stat_type == 'contract':
            # Fae-Touched use same favored regalia system as Changelings
            is_favored = is_changeling_contract_favored(character, stat_name)
            is_royal = 'royal' in stat_name.lower()
            
            if is_favored:
                if is_royal:
                    cost = FAE_TOUCHED_COSTS['favored_royal_contract']
                else:
                    cost = FAE_TOUCHED_COSTS['favored_common_contract']
            else:
                if is_royal:
                    cost = FAE_TOUCHED_COSTS['royal_contract']
                else:
                    cost = FAE_TOUCHED_COSTS['common_contract']
            
            return (dots_to_buy * cost, 'normal')
        elif stat_type == 'goblin_contract':
            return (dots_to_buy * FAE_TOUCHED_COSTS['goblin_contract'], 'normal')
    
    elif template_type in ['ghoul', 'revenant']:
        if stat_type == 'discipline':
            return (dots_to_buy * GHOUL_COSTS['clan_discipline'], 'normal')
        elif stat_type == 'cruac':
            return (dots_to_buy * GHOUL_COSTS['cruac'], 'normal')
        elif stat_type == 'theban_sorcery':
            return (dots_to_buy * GHOUL_COSTS['theban_sorcery'], 'normal')
        elif stat_type == 'blood_ritual':
            return (GHOUL_COSTS['blood_ritual'], 'normal')
        elif stat_type == 'coil':
            return (dots_to_buy * GHOUL_COSTS['coil_in_mystery'], 'normal')
        elif stat_type == 'scale':
            return (GHOUL_COSTS['scale_of_dragon'], 'normal')
    
    elif template_type == 'proximi':
        if stat_type == 'blessing':
            return (dots_to_buy * PROXIMI_COSTS['blessing'], 'normal')
    
    return (0, 'normal')

