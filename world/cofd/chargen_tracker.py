"""
Character Generation Tracker for Chronicles of Darkness.

This module handles the calculation of character generation points and template-specific
chargen requirements. Used by ChargenRoom to display progress.
"""

from world.cofd.stat_dictionary import (
    POWER_ATTRIBUTES, FINESSE_ATTRIBUTES, RESISTANCE_ATTRIBUTES,
    MENTAL_SKILLS, PHYSICAL_SKILLS, SOCIAL_SKILLS
)


def calculate_chargen_points(character):
    """
    Calculate character generation points for a character.
    
    Returns a dictionary with:
    - attributes_spent, attributes_available
    - skills_spent, skills_available  
    - specialties_spent, specialties_available
    - merits_spent, merits_available
    - attribute categories (mental, physical, social) with points and priority
    - skill categories (mental, physical, social) with points and priority
    
    Args:
        character: The character object to calculate points for
        
    Returns:
        dict: Point allocation information
    """
    stats = getattr(character.db, 'stats', {})
    if not stats:
        return None
        
    # Mortal base starting points
    # Attributes: 5/4/3 dots to ADD to starting values (all attrs start at 1)
    # Skills: 11/7/4 dots to distribute among categories (all skills start at 0)
    MORTAL_ATTR_POINTS = 12  # 5 + 4 + 3 = 12 total dots to add
    MORTAL_SKILL_POINTS = 22  # 11 + 7 + 4 = 22 total dots to distribute
    MORTAL_SPECIALTY_POINTS = 3
    MORTAL_MERIT_POINTS = 10
    
    # Attribute categories for chargen (Mental/Physical/Social)
    # Note: Power/Finesse/Resistance categories are imported and available from stat_dictionary
    MENTAL_ATTRIBUTES = ['intelligence', 'wits', 'resolve']
    PHYSICAL_ATTRIBUTES = ['strength', 'dexterity', 'stamina']
    SOCIAL_ATTRIBUTES = ['presence', 'manipulation', 'composure']
    
    attributes = stats.get('attributes', {})
    skills = stats.get('skills', {})
    other = stats.get('other', {})
    
    # Get favored stat (the one that gets a free dot)
    favored_stat = other.get('favored_stat', None)
    
    # Calculate attribute points by category (above starting 1)
    attr_mental = sum(max(0, attributes.get(attr, 1) - 1) for attr in MENTAL_ATTRIBUTES)
    attr_physical = sum(max(0, attributes.get(attr, 1) - 1) for attr in PHYSICAL_ATTRIBUTES)
    attr_social = sum(max(0, attributes.get(attr, 1) - 1) for attr in SOCIAL_ATTRIBUTES)
    
    # Calculate skill points by category
    skill_mental = sum(skills.get(skill, 0) for skill in MENTAL_SKILLS)
    skill_physical = sum(skills.get(skill, 0) for skill in PHYSICAL_SKILLS)
    skill_social = sum(skills.get(skill, 0) for skill in SOCIAL_SKILLS)
    
    # Subtract favored stat from totals if set (this is a free dot)
    if favored_stat:
        # Check if it's an attribute (could be in any category)
        all_attributes = MENTAL_ATTRIBUTES + PHYSICAL_ATTRIBUTES + SOCIAL_ATTRIBUTES
        if favored_stat in all_attributes:
            # Determine which category this attribute is in
            if favored_stat in MENTAL_ATTRIBUTES:
                attr_mental = max(0, attr_mental - 1)
            elif favored_stat in PHYSICAL_ATTRIBUTES:
                attr_physical = max(0, attr_physical - 1)
            elif favored_stat in SOCIAL_ATTRIBUTES:
                attr_social = max(0, attr_social - 1)
        # Check if it's a skill
        else:
            if favored_stat in MENTAL_SKILLS:
                skill_mental = max(0, skill_mental - 1)
            elif favored_stat in PHYSICAL_SKILLS:
                skill_physical = max(0, skill_physical - 1)
            elif favored_stat in SOCIAL_SKILLS:
                skill_social = max(0, skill_social - 1)
    
    # Determine attribute priorities (5/4/3)
    # These are dots to ADD to the starting values (not total dots)
    attr_categories = [
        ('Mental', attr_mental),
        ('Physical', attr_physical),
        ('Social', attr_social)
    ]
    attr_categories_sorted = sorted(attr_categories, key=lambda x: x[1], reverse=True)
    attr_priorities = {}
    for i, (cat_name, points) in enumerate(attr_categories_sorted):
        if i == 0:
            priority = 'Primary (5)'
            expected = 5  # 5 dots to add to starting values
        elif i == 1:
            priority = 'Secondary (4)'
            expected = 4  # 4 dots to add to starting values
        else:
            priority = 'Tertiary (3)'
            expected = 3  # 3 dots to add to starting values
        attr_priorities[cat_name] = {'points': points, 'priority': priority, 'expected': expected}
    
    # Determine skill priorities (11/7/4)
    skill_categories = [
        ('Mental', skill_mental),
        ('Physical', skill_physical),
        ('Social', skill_social)
    ]
    skill_categories_sorted = sorted(skill_categories, key=lambda x: x[1], reverse=True)
    skill_priorities = {}
    for i, (cat_name, points) in enumerate(skill_categories_sorted):
        if i == 0:
            priority = 'Primary (11)'
            expected = 11
        elif i == 1:
            priority = 'Secondary (7)'
            expected = 7
        else:
            priority = 'Tertiary (4)'
            expected = 4
        skill_priorities[cat_name] = {'points': points, 'priority': priority, 'expected': expected}
    
    # Calculate total points
    attr_spent = attr_mental + attr_physical + attr_social
    skill_spent = skill_mental + skill_physical + skill_social
    
    # Calculate specialties
    specialties = stats.get('specialties', {})
    specialty_count = 0
    for skill, specs in specialties.items():
        if isinstance(specs, list):
            specialty_count += len(specs)
        elif isinstance(specs, int):
            specialty_count += specs
            
    # Calculate merits
    merits = stats.get('merits', {})
    merit_spent = 0
    for merit_name, merit_data in merits.items():
        try:
            # Try dict-style access first
            if 'dots' in merit_data:
                dots = merit_data['dots']
                merit_spent += int(dots)
            elif isinstance(merit_data, int):
                merit_spent += merit_data
        except (KeyError, TypeError, AttributeError, ValueError):
            # Skip if we can't read the merit data
            pass
    
    # Get template for template-specific tracking
    template = stats.get('other', {}).get('template', 'Mortal')
    
    # Base result dictionary
    result = {
        'attributes_spent': attr_spent,
        'attributes_available': MORTAL_ATTR_POINTS,
        'attribute_categories': attr_priorities,
        'skills_spent': skill_spent,
        'skills_available': MORTAL_SKILL_POINTS,
        'skill_categories': skill_priorities,
        'specialties_spent': specialty_count,
        'specialties_available': MORTAL_SPECIALTY_POINTS,
        'merits_spent': merit_spent,
        'merits_available': MORTAL_MERIT_POINTS,
        'template': template,
        'favored_stat': favored_stat
    }
    
    # Check for Mortal+ templates first (they have template_type)
    if template.lower() in ['mortal+', 'mortal plus']:
        mortalplus_data = calculate_mortalplus_chargen(character, stats, merits)
        result['mortalplus'] = mortalplus_data
    # Add template-specific tracking
    elif template.lower() == 'vampire':
        vampire_data = calculate_vampire_chargen(character, stats, merits)
        result['vampire'] = vampire_data
    elif template.lower() == 'werewolf':
        werewolf_data = calculate_werewolf_chargen(character, stats, merits)
        result['werewolf'] = werewolf_data
    elif template.lower() == 'changeling':
        changeling_data = calculate_changeling_chargen(character, stats, merits)
        result['changeling'] = changeling_data
    elif template.lower() == 'mage':
        mage_data = calculate_mage_chargen(character, stats, merits)
        result['mage'] = mage_data
    elif template.lower() == 'deviant':
        deviant_data = calculate_deviant_chargen(character, stats, merits)
        result['deviant'] = deviant_data
    elif template.lower() in ['sin-eater', 'geist', 'bound']:
        geist_data = calculate_geist_chargen(character, stats, merits)
        result['geist'] = geist_data
    elif template.lower() == 'hunter':
        hunter_data = calculate_hunter_chargen(character, stats, merits)
        result['hunter'] = hunter_data
    elif template.lower() in ['mummy', 'arisen']:
        mummy_data = calculate_mummy_chargen(character, stats, merits)
        result['mummy'] = mummy_data
    elif template.lower() == 'promethean':
        promethean_data = calculate_promethean_chargen(character, stats, merits)
        result['promethean'] = promethean_data
    
    return result


def calculate_vampire_chargen(character, stats, merits):
    """
    Calculate vampire-specific chargen tracking.
    
    Returns:
        dict: Vampire chargen information
    """
    # Clan favored attributes mapping
    CLAN_FAVORED_ATTRIBUTES = {
        'daeva': ['dexterity', 'manipulation'],
        'gangrel': ['composure', 'stamina'],
        'mekhet': ['intelligence', 'wits'],
        'nosferatu': ['composure', 'strength'],
        'ventrue': ['presence', 'resolve']
    }
    
    # In-clan disciplines by clan
    CLAN_DISCIPLINES = {
        'daeva': ['celerity', 'majesty', 'vigor'],
        'gangrel': ['animalism', 'protean', 'resilience'],
        'mekhet': ['auspex', 'celerity', 'obfuscate'],
        'nosferatu': ['nightmare', 'obfuscate', 'vigor'],
        'ventrue': ['animalism', 'dominate', 'resilience']
    }
    
    # Get character's clan
    bio = stats.get('bio', {})
    clan = bio.get('clan', '').lower()
    
    # Check for favored attribute bonus
    favored_attrs = CLAN_FAVORED_ATTRIBUTES.get(clan, [])
    other = stats.get('other', {})
    favored_attr_used = other.get('favored_stat', None)
    
    # Check if favored stat is set and is one of the valid clan attributes
    has_favored_attr = (favored_attr_used is not None and 
                       favored_attr_used in favored_attrs)
    
    # Get disciplines
    powers = stats.get('powers', {})
    disciplines = {}
    discipline_dots = 0
    in_clan_dots = 0
    out_of_clan_dots = 0
    covenant_power_dots = 0
    
    # Define all disciplines
    ALL_DISCIPLINES = [
        'animalism', 'auspex', 'bloodworking', 'cachexy', 'celerity',
        'dominate', 'majesty', 'nightmare', 'obfuscate', 'praestantia',
        'protean', 'resilience', 'vigor', 'crochan', 'dead_signal',
        'chary', 'vitiate'
    ]
    
    COVENANT_POWERS = ['cruac', 'theban_sorcery', 'coil']
    
    in_clan = CLAN_DISCIPLINES.get(clan, [])
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower().replace(' ', '_')
        
        # Check if it's a discipline
        if power_lower in ALL_DISCIPLINES:
            dots = power_value if isinstance(power_value, int) else 1
            disciplines[power_name] = dots
            discipline_dots += dots
            
            if power_lower in in_clan:
                in_clan_dots += dots
            else:
                out_of_clan_dots += dots
        
        # Check if it's a covenant power
        elif power_lower in COVENANT_POWERS:
            dots = power_value if isinstance(power_value, int) else 1
            disciplines[power_name] = dots
            discipline_dots += dots
            covenant_power_dots += dots
    
    # Blood Potency tracking
    blood_potency = stats.get('other', {}).get('blood_potency', 1)
    bp_from_merits = max(0, blood_potency - 1)  # Subtract the free dot
    bp_merit_cost = bp_from_merits * 5  # 5 merits per dot
    
    # Check for Mask and Dirge (stored in bio, not anchors)
    bio = stats.get('bio', {})
    anchors = stats.get('anchors', {})
    
    # Check bio first (modern storage), then anchors (legacy storage)
    has_mask = (('mask' in bio and bio['mask'] and bio['mask'] != '<not set>') or 
                ('mask' in anchors and anchors['mask'] and anchors['mask'] != '<not set>'))
    has_dirge = (('dirge' in bio and bio['dirge'] and bio['dirge'] != '<not set>') or 
                 ('dirge' in anchors and anchors['dirge'] and anchors['dirge'] != '<not set>'))
    
    # Check for Touchstone Merit
    has_touchstone_merit = 'touchstone' in [m.lower() for m in merits.keys()]
    
    # Get covenant from bio (already retrieved above)
    covenant = bio.get('covenant', None)
    covenant_status = None
    covenant_status_dots = 0
    
    # Check for Covenant Status - can be either:
    # 1. "covenant status" merit (old format)
    # 2. "status:<covenant_name>" instanced merit (new format)
    for merit_name, merit_data in merits.items():
        merit_lower = merit_name.lower()
        
        # Check for old format
        if 'covenant status' in merit_lower:
            covenant_status = merit_name
            # Extract dots value
            try:
                if 'dots' in merit_data:
                    covenant_status_dots = int(merit_data['dots'])
            except (KeyError, ValueError, TypeError, AttributeError):
                covenant_status_dots = 0
            break
        
        # Check for new instanced format: status:carthian_movement, status:invictus, etc.
        if merit_lower.startswith('status:'):
            # Extract the instance name
            instance = merit_lower.split(':', 1)[1] if ':' in merit_lower else None
            
            # Check if instance matches a vampire covenant
            covenant_keywords = [
                'carthian', 'circle', 'crone', 'invictus', 'ordo', 'dracul', 
                'lancea', 'sanctum', 'belial', 'brood', 'vii', 'unaligned'
            ]
            
            if instance and any(keyword in instance for keyword in covenant_keywords):
                covenant_status = merit_name
                # Extract dots value
                try:
                    if 'dots' in merit_data:
                        covenant_status_dots = int(merit_data['dots'])
                except (KeyError, ValueError, TypeError, AttributeError):
                    covenant_status_dots = 0
                break
    
    return {
        'clan': clan,
        'favored_attributes': favored_attrs,
        'has_favored_attr_bonus': has_favored_attr,
        'favored_attr_used': favored_attr_used,
        'disciplines': disciplines,
        'discipline_dots_total': discipline_dots,
        'discipline_dots_available': 3,
        'in_clan_dots': in_clan_dots,
        'out_of_clan_dots': out_of_clan_dots,
        'covenant_power_dots': covenant_power_dots,
        'in_clan_disciplines': in_clan,
        'blood_potency': blood_potency,
        'bp_merit_cost': bp_merit_cost,
        'has_mask': has_mask,
        'has_dirge': has_dirge,
        'has_touchstone_merit': has_touchstone_merit,
        'covenant': covenant,
        'covenant_status': covenant_status,
        'covenant_status_dots': covenant_status_dots
    }


def calculate_werewolf_chargen(character, stats, merits):
    """
    Calculate werewolf-specific chargen tracking.
    
    Returns:
        dict: Werewolf chargen information
    """
    # Auspice skills and renown mapping
    AUSPICE_DATA = {
        'cahalith': {
            'skills': ['crafts', 'expression', 'persuasion'],
            'renown': 'glory',
            'moon_gift': 'Gibbous Moon'
        },
        'elodoth': {
            'skills': ['empathy', 'investigation', 'politics'],
            'renown': 'honor',
            'moon_gift': 'Half Moon'
        },
        'irraka': {
            'skills': ['larceny', 'stealth', 'subterfuge'],
            'renown': 'cunning',
            'moon_gift': 'New Moon'
        },
        'ithaeur': {
            'skills': ['animal_ken', 'medicine', 'occult'],
            'renown': 'wisdom',
            'moon_gift': 'Crescent Moon'
        },
        'rahu': {
            'skills': ['brawl', 'intimidation', 'survival'],
            'renown': 'purity',
            'moon_gift': 'Full Moon'
        }
    }
    
    # Tribe gifts and renown
    TRIBE_DATA = {
        'blood_talons': {
            'gifts': ['inspiration', 'rage', 'strength'],
            'renown': 'glory'
        },
        'bone_shadows': {
            'gifts': ['death', 'elemental', 'insight'],
            'renown': 'wisdom'
        },
        'hunters_in_darkness': {
            'gifts': ['nature', 'stealth', 'warding'],
            'renown': 'purity'
        },
        'iron_masters': {
            'gifts': ['knowledge', 'shaping', 'technology'],
            'renown': 'cunning'
        },
        'storm_lords': {
            'gifts': ['evasion', 'dominance', 'weather'],
            'renown': 'honor'
        },
        'ghost_wolf': {
            'gifts': [],
            'renown': None
        }
    }
    
    # Get character's auspice and tribe
    bio = stats.get('bio', {})
    auspice = bio.get('auspice', '').lower()
    tribe = bio.get('tribe', '').lower().replace(' ', '_')
    
    auspice_info = AUSPICE_DATA.get(auspice, {})
    tribe_info = TRIBE_DATA.get(tribe, {})
    
    # Check for auspice skill bonus
    auspice_skills = auspice_info.get('skills', [])
    other = stats.get('other', {})
    auspice_skill_used = other.get('favored_stat', None)
    
    # Check if favored stat is set and is one of the valid auspice skills
    has_auspice_skill_bonus = (auspice_skill_used is not None and 
                               auspice_skill_used in auspice_skills)
    
    # Calculate Renown
    renown = stats.get('renown', {
        'glory': 0,
        'honor': 0,
        'cunning': 0,
        'purity': 0,
        'wisdom': 0
    })
    
    total_renown = sum(renown.values())
    expected_renown = 3 if tribe != 'ghost_wolf' else 2
    
    # Check for proper renown distribution
    auspice_renown = auspice_info.get('renown')
    tribe_renown = tribe_info.get('renown')
    
    has_auspice_renown = renown.get(auspice_renown, 0) >= 1 if auspice_renown else False
    has_tribe_renown = renown.get(tribe_renown, 0) >= 1 if tribe_renown else True  # Ghost wolves don't need tribe renown
    
    # Check if any renown is at 3+ (shouldn't be at chargen)
    has_excessive_renown = any(r >= 3 for r in renown.values())
    
    # Get Gifts
    powers = stats.get('powers', {})
    gifts = {}
    gift_facets = 0
    has_moon_gift = False
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower().replace(' ', '_')
        if 'gift' in power_lower or power_lower in ['inspiration', 'rage', 'strength', 'death', 
                                                     'elemental', 'insight', 'nature', 'stealth',
                                                     'warding', 'knowledge', 'shaping', 'technology',
                                                     'evasion', 'dominance', 'weather']:
            gifts[power_name] = power_value
            if isinstance(power_value, int):
                gift_facets += power_value
            else:
                gift_facets += 1
            
            # Check for moon gift
            if auspice_info.get('moon_gift', '').lower() in power_name.lower():
                has_moon_gift = True
    
    # Get Rites
    rites = {}
    rite_dots = 0
    for power_name, power_value in powers.items():
        power_lower = power_name.lower()
        if 'rite' in power_lower and 'rite_' in power_lower:
            rites[power_name] = power_value
            if isinstance(power_value, int):
                rite_dots += power_value
            else:
                rite_dots += 1
    
    # Calculate rites from merits (merit dots traded for rites)
    # Base is 2 dots, anything above that came from merits
    rites_from_merits = max(0, rite_dots - 2)
    
    # Primal Urge tracking
    other = stats.get('other', {})
    primal_urge = other.get('primal_urge', 1)
    pu_from_merits = max(0, primal_urge - 1)
    pu_merit_cost = pu_from_merits * 5
    
    # Check for Bone and Blood (stored in bio, not anchors)
    # Get bio (might already be retrieved earlier in the function)
    bio = stats.get('bio', {})
    anchors = stats.get('anchors', {})
    
    # Check bio first (modern storage), then anchors (legacy storage)
    has_bone = (('bone' in bio and bio['bone'] and bio['bone'] != '<not set>') or 
                ('bone' in anchors and anchors['bone'] and anchors['bone'] != '<not set>'))
    has_blood = (('blood' in bio and bio['blood'] and bio['blood'] != '<not set>') or 
                 ('blood' in anchors and anchors['blood'] and anchors['blood'] != '<not set>'))
    
    # Check for required merits
    has_totem = any('totem' in m.lower() for m in merits.keys())
    has_first_tongue = any('first tongue' in m.lower() or 'language' in m.lower() for m in merits.keys())
    
    # Touchstone check (need to check via command, not stored in stats typically)
    # We'll just note that they need to use +touchstone command
    
    return {
        'auspice': auspice,
        'tribe': tribe,
        'auspice_skills': auspice_skills,
        'has_auspice_skill_bonus': has_auspice_skill_bonus,
        'auspice_skill_used': auspice_skill_used,
        'tribe_gifts': tribe_info.get('gifts', []),
        'renown': renown,
        'total_renown': total_renown,
        'expected_renown': expected_renown,
        'auspice_renown': auspice_renown,
        'tribe_renown': tribe_renown,
        'has_auspice_renown': has_auspice_renown,
        'has_tribe_renown': has_tribe_renown,
        'has_excessive_renown': has_excessive_renown,
        'gifts': gifts,
        'gift_facets': gift_facets,
        'has_moon_gift': has_moon_gift,
        'moon_gift_name': auspice_info.get('moon_gift', 'Unknown'),
        'rites': rites,
        'rite_dots': rite_dots,
        'rites_from_merits': rites_from_merits,
        'primal_urge': primal_urge,
        'pu_merit_cost': pu_merit_cost,
        'has_bone': has_bone,
        'has_blood': has_blood,
        'has_totem': has_totem,
        'has_first_tongue': has_first_tongue
    }


def format_covenant_name(covenant):
    """
    Format covenant name with proper capitalization and full name.
    Handles abbreviations and variations.
    
    Args:
        covenant (str): Raw covenant name from database
        
    Returns:
        str: Properly formatted covenant name
    """
    if not covenant:
        return None
    
    # Covenant full name mapping
    covenant_names = {
        'carthian_movement': 'The Carthian Movement',
        'carthian': 'The Carthian Movement',
        'circle_of_the_crone': 'The Circle of the Crone',
        'circle': 'The Circle of the Crone',
        'crone': 'The Circle of the Crone',
        'crones': 'The Circle of the Crone',
        'invictus': 'The Invictus',
        'ordo_dracul': 'The Ordo Dracul',
        'ordo': 'The Ordo Dracul',
        'dracul': 'The Ordo Dracul',
        'lancea_et_sanctum': 'Lancea et Sanctum',
        'lancea_sanctum': 'Lancea et Sanctum',
        'lancea': 'Lancea et Sanctum',
        'belials_brood': "Belial's Brood",
        'belial': "Belial's Brood",
        'vii': 'VII',
        'seven': 'VII',
        'unaligned': 'Unaligned'
    }
    
    covenant_lower = covenant.lower().replace(' ', '_')
    return covenant_names.get(covenant_lower, covenant.replace('_', ' ').title())


def format_tribe_name(tribe):
    """
    Format tribe name with proper capitalization.
    Handles abbreviations and variations.
    
    Args:
        tribe (str): Raw tribe name from database
        
    Returns:
        str: Properly formatted tribe name
    """
    if not tribe:
        return None
    
    # Tribe name mapping
    tribe_names = {
        'blood_talons': 'Blood Talons',
        'bone_shadows': 'Bone Shadows',
        'hunters_in_darkness': 'Hunters in Darkness',
        'iron_masters': 'Iron Masters',
        'storm_lords': 'Storm Lords',
        'ghost_wolf': 'Ghost Wolf',
        'ghost_wolves': 'Ghost Wolf'
    }
    
    tribe_lower = tribe.lower().replace(' ', '_')
    return tribe_names.get(tribe_lower, tribe.replace('_', ' ').title())


def calculate_changeling_chargen(character, stats, merits):
    """
    Calculate changeling-specific chargen tracking.
    
    Returns:
        dict: Changeling chargen information
    """
    # Seeming favored attribute categories
    SEEMING_CATEGORIES = {
        'beast': 'resistance',
        'darkling': 'finesse',
        'elemental': 'resistance',
        'fairest': 'power',
        'ogre': 'power',
        'wizened': 'finesse'
    }
    
    # Seeming favored regalia
    SEEMING_REGALIA = {
        'beast': 'den',
        'darkling': 'mirror',
        'elemental': 'stone',
        'fairest': 'crown',
        'ogre': 'sword',
        'wizened': 'artifice'
    }
    
    # Get character's seeming and kith
    bio = stats.get('bio', {})
    seeming = bio.get('seeming', '').lower()
    kith = bio.get('kith', '')
    court = bio.get('court', '')
    
    # Get favored attribute category
    attribute_category = SEEMING_CATEGORIES.get(seeming, None)
    
    # Check for favored attribute bonus
    other = stats.get('other', {})
    favored_attr_used = other.get('favored_stat', None)
    
    # Determine valid favored attributes based on seeming
    from world.cofd.stat_dictionary import (
        POWER_ATTRIBUTES, FINESSE_ATTRIBUTES, RESISTANCE_ATTRIBUTES
    )
    
    favored_attrs = []
    if attribute_category == 'power':
        favored_attrs = POWER_ATTRIBUTES
    elif attribute_category == 'finesse':
        favored_attrs = FINESSE_ATTRIBUTES
    elif attribute_category == 'resistance':
        favored_attrs = RESISTANCE_ATTRIBUTES
    
    has_favored_attr = (favored_attr_used is not None and favored_attr_used in favored_attrs)
    
    # Get favored regalia
    seeming_regalia = SEEMING_REGALIA.get(seeming, None)
    favored_regalia = other.get('favored_regalia', None)  # Second chosen regalia
    
    # Check for Needle and Thread
    anchors = stats.get('anchors', {})
    has_needle = (('needle' in bio and bio['needle'] and bio['needle'] != '<not set>') or 
                  ('needle' in anchors and anchors['needle'] and anchors['needle'] != '<not set>'))
    has_thread = (('thread' in bio and bio['thread'] and bio['thread'] != '<not set>') or 
                  ('thread' in anchors and anchors['thread'] and anchors['thread'] != '<not set>'))
    
    # Get Contracts
    powers = stats.get('powers', {})
    contracts = {}
    common_contracts = 0
    royal_contracts = 0
    favored_regalia_contracts = 0
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower()
        if power_name.startswith('contract:') and power_value == 'known':
            contracts[power_name] = power_value
            
            # Check if it's royal or common (would need contract data to determine)
            # For now, count all contracts
            common_contracts += 1
    
    # Wyrd tracking
    wyrd = stats.get('advantages', {}).get('wyrd', 1)
    wyrd_from_merits = max(0, wyrd - 1)  # Subtract the free dot
    wyrd_merit_cost = wyrd_from_merits * 5  # 5 merits per dot
    
    # Check for Touchstone Merit
    has_touchstone_merit = any('touchstone' in m.lower() for m in merits.keys())
    
    # Check for Mantle (free dot from court)
    has_mantle = any('mantle' in m.lower() for m in merits.keys())
    mantle_dots = 0
    for merit_name, merit_data in merits.items():
        if 'mantle' in merit_name.lower():
            try:
                if 'dots' in merit_data:
                    mantle_dots = int(merit_data['dots'])
                    break
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
    
    return {
        'seeming': seeming,
        'kith': kith,
        'court': court,
        'attribute_category': attribute_category,
        'favored_attributes': favored_attrs,
        'has_favored_attr_bonus': has_favored_attr,
        'favored_attr_used': favored_attr_used,
        'seeming_regalia': seeming_regalia,
        'favored_regalia': favored_regalia,
        'has_needle': has_needle,
        'has_thread': has_thread,
        'contracts': contracts,
        'common_contracts': common_contracts,
        'royal_contracts': royal_contracts,
        'contracts_available': 4,  # 4 Common + 2 Royal
        'royal_available': 2,
        'favored_regalia_contracts': favored_regalia_contracts,
        'wyrd': wyrd,
        'wyrd_merit_cost': wyrd_merit_cost,
        'has_touchstone_merit': has_touchstone_merit,
        'has_mantle': has_mantle,
        'mantle_dots': mantle_dots
    }


def calculate_mage_chargen(character, stats, merits):
    """
    Calculate mage-specific chargen tracking.
    
    Returns:
        dict: Mage chargen information
    """
    # Path Ruling and Inferior Arcana
    PATH_ARCANA = {
        'acanthus': {'ruling': ['fate', 'time'], 'inferior': 'forces'},
        'mastigos': {'ruling': ['mind', 'space'], 'inferior': 'matter'},
        'moros': {'ruling': ['death', 'matter'], 'inferior': 'spirit'},
        'obrimos': {'ruling': ['forces', 'prime'], 'inferior': 'death'},
        'thyrsus': {'ruling': ['life', 'spirit'], 'inferior': 'mind'}
    }
    
    # Order Rote Skills
    ORDER_ROTE_SKILLS = {
        'adamantine_arrow': ['athletics', 'intimidation', 'medicine'],
        'arrow': ['athletics', 'intimidation', 'medicine'],
        'guardians_of_the_veil': ['investigation', 'stealth', 'subterfuge'],
        'guardians': ['investigation', 'stealth', 'subterfuge'],
        'mysterium': ['investigation', 'occult', 'survival'],
        'silver_ladder': ['expression', 'persuasion', 'subterfuge'],
        'ladder': ['expression', 'persuasion', 'subterfuge'],
        'free_council': ['crafts', 'persuasion', 'science'],
        'council': ['crafts', 'persuasion', 'science'],
        'seers_of_the_throne': ['investigation', 'occult', 'persuasion'],
        'seers': ['investigation', 'occult', 'persuasion']
    }
    
    # Get character's path and order
    bio = stats.get('bio', {})
    path = bio.get('path', '').lower()
    order = bio.get('order', '').lower().replace(' ', '_')
    
    path_info = PATH_ARCANA.get(path, {})
    ruling_arcana = path_info.get('ruling', [])
    inferior_arcanum = path_info.get('inferior', None)
    rote_skills = ORDER_ROTE_SKILLS.get(order, [])
    
    # Check for favored attribute bonus (Composure, Resolve, or Stamina)
    other = stats.get('other', {})
    favored_attr_used = other.get('favored_stat', None)
    
    valid_favored = ['composure', 'resolve', 'stamina']
    has_favored_attr = (favored_attr_used is not None and favored_attr_used in valid_favored)
    
    # Get Arcana
    powers = stats.get('powers', {})
    arcana = {}
    arcana_dots = 0
    ruling_dots = 0
    has_both_ruling = False
    has_inferior = False
    max_arcanum_dots = 0
    
    ALL_ARCANA = ['death', 'fate', 'forces', 'life', 'matter', 'mind', 'prime', 'space', 'spirit', 'time']
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower().replace(' ', '_')
        
        # Check if it's an arcanum
        if power_lower in ALL_ARCANA:
            dots = power_value if isinstance(power_value, int) else 1
            arcana[power_name] = dots
            arcana_dots += dots
            max_arcanum_dots = max(max_arcanum_dots, dots)
            
            # Check if it's ruling
            if power_lower in ruling_arcana:
                ruling_dots += dots
            
            # Check if it's inferior
            if power_lower == inferior_arcanum:
                has_inferior = True
    
    # Check if both ruling arcana have at least 1 dot
    ruling_check = []
    for arcanum in ruling_arcana:
        has_dot = any(p.lower().replace(' ', '_') == arcanum for p, v in arcana.items() if v > 0)
        ruling_check.append(has_dot)
    has_both_ruling = all(ruling_check) if len(ruling_check) == 2 else False
    
    # Gnosis tracking
    gnosis = stats.get('advantages', {}).get('gnosis', 1)
    gnosis_from_merits = max(0, gnosis - 1)  # Subtract the free dot
    gnosis_merit_cost = gnosis_from_merits * 5  # 5 merits per dot
    
    # Get mage-specific stats
    mage_stats = getattr(character.db, 'mage_stats', {})
    
    # Check for nimbus descriptions
    has_immediate_nimbus = bool(mage_stats.get('immediate_nimbus', ''))
    has_long_term_nimbus = bool(mage_stats.get('long_term_nimbus', ''))
    has_signature_nimbus = bool(mage_stats.get('signature_nimbus', ''))
    
    # Dedicated tool
    dedicated_tool = mage_stats.get('dedicated_tool', None)
    has_dedicated_tool = bool(dedicated_tool)
    
    # Obsessions
    obsessions = mage_stats.get('obsessions', [])
    obsessions_count = len(obsessions) if isinstance(obsessions, list) else 0
    expected_obsessions = 1 if gnosis <= 2 else 2
    
    # Praxes
    praxes = mage_stats.get('praxes', [])
    praxes_count = len(praxes) if isinstance(praxes, list) else 0
    expected_praxes = gnosis
    
    # Rotes (stored as powers or separate?)
    rotes_count = 0
    for power_name in powers.keys():
        if 'rote:' in power_name.lower():
            rotes_count += 1
    
    # Check for Order Status Merit (free from order)
    has_order_status = False
    order_status_dots = 0
    for merit_name, merit_data in merits.items():
        merit_lower = merit_name.lower()
        if 'order status' in merit_lower or ('status:' in merit_lower and any(ord in merit_lower for ord in ['arrow', 'guardian', 'mysterium', 'ladder', 'council', 'seer'])):
            has_order_status = True
            try:
                if 'dots' in merit_data:
                    order_status_dots = int(merit_data['dots'])
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
            break
    
    # Check for High Speech Merit (free from order)
    has_high_speech = any('high speech' in m.lower() or 'language' in m.lower() for m in merits.keys())
    
    # Check for free Occult dot from order
    skills = stats.get('skills', {})
    occult_dots = skills.get('occult', 0)
    
    return {
        'path': path,
        'order': order,
        'ruling_arcana': ruling_arcana,
        'inferior_arcanum': inferior_arcanum,
        'rote_skills': rote_skills,
        'has_favored_attr_bonus': has_favored_attr,
        'favored_attr_used': favored_attr_used,
        'arcana': arcana,
        'arcana_dots': arcana_dots,
        'arcana_available': 6,
        'ruling_dots': ruling_dots,
        'has_both_ruling': has_both_ruling,
        'has_inferior': has_inferior,
        'max_arcanum_dots': max_arcanum_dots,
        'gnosis': gnosis,
        'gnosis_merit_cost': gnosis_merit_cost,
        'has_immediate_nimbus': has_immediate_nimbus,
        'has_long_term_nimbus': has_long_term_nimbus,
        'has_signature_nimbus': has_signature_nimbus,
        'dedicated_tool': dedicated_tool,
        'has_dedicated_tool': has_dedicated_tool,
        'obsessions': obsessions,
        'obsessions_count': obsessions_count,
        'expected_obsessions': expected_obsessions,
        'praxes': praxes,
        'praxes_count': praxes_count,
        'expected_praxes': expected_praxes,
        'rotes_count': rotes_count,
        'rotes_available': 3,
        'has_order_status': has_order_status,
        'order_status_dots': order_status_dots,
        'has_high_speech': has_high_speech,
        'occult_dots': occult_dots
    }


def calculate_deviant_chargen(character, stats, merits):
    """
    Calculate deviant-specific chargen tracking.
    
    Returns:
        dict: Deviant chargen information
    """
    # Origin bonus variations mapping
    ORIGIN_DATA = {
        'autourgic': {'bonus_type': 'overt', 'bonus_stat': 'loyalty', 'name': 'Elect'},
        'elect': {'bonus_type': 'overt', 'bonus_stat': 'loyalty', 'name': 'Elect'},
        'epimorph': {'bonus_type': 'subtle', 'bonus_stat': 'loyalty', 'name': 'Volunteers'},
        'volunteer': {'bonus_type': 'subtle', 'bonus_stat': 'loyalty', 'name': 'Volunteers'},
        'exomorph': {'bonus_type': 'overt', 'bonus_stat': 'conviction', 'name': 'Unwilling'},
        'unwilling': {'bonus_type': 'overt', 'bonus_stat': 'conviction', 'name': 'Unwilling'},
        'genotypal': {'bonus_type': 'subtle', 'bonus_stat': 'conviction', 'name': 'Born'},
        'born': {'bonus_type': 'subtle', 'bonus_stat': 'conviction', 'name': 'Born'},
        'pathological': {'bonus_type': 'any', 'bonus_stat': 'choice', 'name': 'Accidents'},
        'accident': {'bonus_type': 'any', 'bonus_stat': 'choice', 'name': 'Accidents'}
    }
    
    # Clade names
    CLADE_NAMES = {
        'cephalist': 'Psychic',
        'psychic': 'Psychic',
        'chimeric': 'Hybrid',
        'hybrid': 'Hybrid',
        'coactive': 'Infused',
        'infused': 'Infused',
        'invasive': 'Cyborg',
        'cyborg': 'Cyborg',
        'mutant': 'Grotesque',
        'grotesque': 'Grotesque'
    }
    
    # Get character's origin and clade
    bio = stats.get('bio', {})
    origin = bio.get('origin', '').lower()
    clade = bio.get('clade', '').lower()
    form = bio.get('form', '')  # Optional
    
    origin_info = ORIGIN_DATA.get(origin, {})
    clade_display = CLADE_NAMES.get(clade, clade.title())
    
    # Get Variations and Scars
    powers = stats.get('powers', {})
    variations = {}
    scars = {}
    variation_magnitude = 0
    scar_magnitude = 0
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower()
        
        # Check if it's a variation
        if power_name.startswith('variation:'):
            dots = power_value if isinstance(power_value, int) else 1
            variations[power_name] = dots
            variation_magnitude += dots
        
        # Check if it's a scar
        elif power_name.startswith('scar:'):
            dots = power_value if isinstance(power_value, int) else 1
            scars[power_name] = dots
            scar_magnitude += dots
    
    # Loyalty and Conviction
    other = stats.get('other', {})
    loyalty = other.get('loyalty', 1)
    conviction = other.get('conviction', 3)
    
    # Touchstones for Loyalty and Conviction
    # Check both 'touchstones' dict and individual touchstone fields
    loyalty_touchstones = []
    conviction_touchstones = []
    
    touchstones_data = other.get('touchstones', {})
    for ts_name, ts_data in touchstones_data.items():
        if isinstance(ts_data, dict):
            ts_type = ts_data.get('type', '').lower()
            if ts_type == 'loyalty':
                loyalty_touchstones.append(ts_name)
            elif ts_type == 'conviction':
                conviction_touchstones.append(ts_name)
    
    # Acclimation tracking
    acclimation = other.get('acclimation', 0)
    acclimation_from_merits = acclimation  # All acclimation comes from merits
    acclimation_merit_cost = acclimation * 5  # 5 merits per dot
    
    # Forms (optional, stored in bio)
    forms_list = []
    if form:
        # Could be a string or list
        if isinstance(form, str):
            forms_list = [form]
        elif isinstance(form, list):
            forms_list = form
    
    return {
        'origin': origin,
        'origin_name': origin_info.get('name', origin.title()),
        'origin_bonus_type': origin_info.get('bonus_type', None),
        'origin_bonus_stat': origin_info.get('bonus_stat', None),
        'clade': clade,
        'clade_display': clade_display,
        'form': forms_list,
        'variations': variations,
        'variation_magnitude': variation_magnitude,
        'scars': scars,
        'scar_magnitude': scar_magnitude,
        'loyalty': loyalty,
        'conviction': conviction,
        'loyalty_touchstones': loyalty_touchstones,
        'conviction_touchstones': conviction_touchstones,
        'loyalty_touchstones_needed': loyalty,
        'conviction_touchstones_needed': conviction,
        'acclimation': acclimation,
        'acclimation_merit_cost': acclimation_merit_cost
    }


def calculate_geist_chargen(character, stats, merits):
    """
    Calculate Sin-Eater/Geist-specific chargen tracking.
    
    Returns:
        dict: Geist chargen information
    """
    # Burden Haunt affinities
    BURDEN_HAUNTS = {
        'hungry': ['boneyard', 'marionette', 'caul'],
        'bereaved': ['curse', 'oracle', 'shroud'],
        'vengeful': ['curse', 'memoria', 'rage'],
        'abiding': ['caul', 'memoria', 'tomb'],
        'kindly': ['dirge', 'marionette', 'shroud']
    }
    
    # Get character's burden (stored in bio for Sin-Eaters, not anchors)
    bio = stats.get('bio', {})
    burden = bio.get('burden', '').lower()
    
    # Note: Mummy also has "burden" but it's stored in anchors (like virtue/vice)
    # Sin-Eater burden is a template choice (like clan), so it's in bio
    
    haunt_affinities = BURDEN_HAUNTS.get(burden, [])
    
    # Check for Root and Bloom
    anchors = stats.get('anchors', {})
    has_root = (('root' in bio and bio['root'] and bio['root'] != '<not set>') or 
                ('root' in anchors and anchors['root'] and anchors['root'] != '<not set>'))
    has_bloom = (('bloom' in bio and bio['bloom'] and bio['bloom'] != '<not set>') or 
                 ('bloom' in anchors and anchors['bloom'] and anchors['bloom'] != '<not set>'))
    
    # Get Haunts
    powers = stats.get('powers', {})
    haunts = {}
    haunt_dots = 0
    affinity_dots = 0
    
    ALL_HAUNTS = ['boneyard', 'caul', 'curse', 'dirge', 'marionette', 'memoria', 'oracle', 'rage', 'shroud', 'tomb']
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower().replace(' ', '_')
        
        # Check if it's a haunt
        if power_lower in ALL_HAUNTS or power_name.startswith('haunt:'):
            dots = power_value if isinstance(power_value, int) else 1
            haunts[power_name] = dots
            haunt_dots += dots
            
            # Check if it's an affinity haunt
            if power_lower in haunt_affinities:
                affinity_dots += dots
    
    # Get Keys
    keys = []
    for power_name in powers.keys():
        power_lower = power_name.lower()
        if 'key' in power_lower or power_name.startswith('key:'):
            keys.append(power_name)
    
    has_key = len(keys) > 0
    
    # Get Ceremonies
    ceremonies = []
    for power_name in powers.keys():
        if power_name.startswith('ceremony:'):
            ceremonies.append(power_name)
    
    # Synergy tracking
    synergy = stats.get('advantages', {}).get('synergy', 1)
    synergy_from_merits = max(0, synergy - 1)  # Subtract the free dot
    synergy_merit_cost = synergy_from_merits * 5  # 5 merits per dot
    
    # Check for Tolerance for Biology Merit (free)
    has_tolerance_biology = any('tolerance for biology' in m.lower() or 'tolerance' in m.lower() for m in merits.keys())
    
    # Touchstone
    has_touchstone_merit = any('touchstone' in m.lower() for m in merits.keys())
    
    # Check for Geist stats (from +stat/geist command)
    geist_stats = getattr(character.db, 'geist_stats', {})
    
    # Geist name
    geist_name = geist_stats.get('geist_name', None)
    has_geist_name = bool(geist_name)
    
    # Geist Remembrance
    remembrance = geist_stats.get('remembrance', None)
    has_remembrance = bool(remembrance)
    
    # Geist Remembrance Trait
    remembrance_trait = geist_stats.get('remembrance_trait', None)
    has_remembrance_trait = bool(remembrance_trait)
    
    # Geist Attributes (Power, Finesse, Resistance)
    geist_power = geist_stats.get('power', 1)
    geist_finesse = geist_stats.get('finesse', 1)
    geist_resistance = geist_stats.get('resistance', 1)
    
    geist_attr_spent = (geist_power - 1) + (geist_finesse - 1) + (geist_resistance - 1)
    geist_attr_available = 12
    
    # Geist Virtue and Vice
    geist_virtue = geist_stats.get('virtue', None)
    geist_vice = geist_stats.get('vice', None)
    has_geist_virtue = bool(geist_virtue)
    has_geist_vice = bool(geist_vice)
    
    # Geist Crisis Point
    crisis_point = geist_stats.get('crisis_point', None)
    has_crisis_point = bool(crisis_point)
    
    # Geist Rank
    geist_rank = geist_stats.get('rank', 3)
    
    # Geist Ban and Bane
    geist_ban = geist_stats.get('ban', None)
    geist_bane = geist_stats.get('bane', None)
    has_ban = bool(geist_ban)
    has_bane = bool(geist_bane)
    
    # Geist Innate Key
    innate_key = geist_stats.get('innate_key', None)
    has_innate_key = bool(innate_key)
    
    return {
        'burden': burden,
        'haunt_affinities': haunt_affinities,
        'has_root': has_root,
        'has_bloom': has_bloom,
        'haunts': haunts,
        'haunt_dots': haunt_dots,
        'haunt_available': 3,
        'affinity_dots': affinity_dots,
        'keys': keys,
        'has_key': has_key,
        'ceremonies': ceremonies,
        'ceremonies_count': len(ceremonies),
        'synergy': synergy,
        'synergy_merit_cost': synergy_merit_cost,
        'has_tolerance_biology': has_tolerance_biology,
        'has_touchstone_merit': has_touchstone_merit,
        'geist_name': geist_name,
        'has_geist_name': has_geist_name,
        'remembrance': remembrance,
        'has_remembrance': has_remembrance,
        'remembrance_trait': remembrance_trait,
        'has_remembrance_trait': has_remembrance_trait,
        'geist_power': geist_power,
        'geist_finesse': geist_finesse,
        'geist_resistance': geist_resistance,
        'geist_attr_spent': geist_attr_spent,
        'geist_attr_available': geist_attr_available,
        'geist_virtue': geist_virtue,
        'geist_vice': geist_vice,
        'has_geist_virtue': has_geist_virtue,
        'has_geist_vice': has_geist_vice,
        'crisis_point': crisis_point,
        'has_crisis_point': has_crisis_point,
        'geist_rank': geist_rank,
        'geist_ban': geist_ban,
        'geist_bane': geist_bane,
        'has_ban': has_ban,
        'has_bane': has_bane,
        'innate_key': innate_key,
        'has_innate_key': has_innate_key
    }


def calculate_hunter_chargen(character, stats, merits):
    """
    Calculate Hunter-specific chargen tracking.
    
    Returns:
        dict: Hunter chargen information
    """
    # Get character's organization and tier
    bio = stats.get('bio', {})
    other = stats.get('other', {})
    
    organization = bio.get('organization', '')
    profession = bio.get('profession', '')  # Often used for tier 1 cells
    tier = other.get('tier', 1)  # Default to tier 1
    
    # Determine organization type
    org_type = None
    if tier == 1:
        org_type = 'Cell'
    elif tier == 2:
        org_type = 'Compact'
    elif tier == 3:
        org_type = 'Conspiracy'
    
    # Get Tactics
    tactics = other.get('tactics', [])
    if not isinstance(tactics, list):
        tactics = []
    tactics_count = len(tactics)
    expected_tactics = 3  # Base 3 tactics for the cell
    
    # Get Endowments (Tier 3 only)
    powers = stats.get('powers', {})
    endowments = []
    for power_name in powers.keys():
        if power_name.startswith('endowment:'):
            endowments.append(power_name)
    
    endowments_count = len(endowments)
    expected_endowments = 2 if tier == 3 else 0
    
    # Check for Status Merit (free 1 dot for tier 2+)
    has_status = False
    status_dots = 0
    status_merit_name = None
    
    for merit_name, merit_data in merits.items():
        merit_lower = merit_name.lower()
        
        # Check for compact/conspiracy status or instanced status matching organization
        if 'status' in merit_lower:
            # Could be "compact status", "conspiracy status", or "status:organization_name"
            if organization and organization.lower().replace(' ', '_') in merit_lower:
                has_status = True
                status_merit_name = merit_name
                try:
                    if 'dots' in merit_data:
                        status_dots = int(merit_data['dots'])
                except (KeyError, ValueError, TypeError, AttributeError):
                    pass
                break
            elif 'compact status' in merit_lower or 'conspiracy status' in merit_lower:
                has_status = True
                status_merit_name = merit_name
                try:
                    if 'dots' in merit_data:
                        status_dots = int(merit_data['dots'])
                except (KeyError, ValueError, TypeError, AttributeError):
                    pass
                break
    
    # Hunter doesn't have a supernatural power stat by default
    # Some conspiracy endowments might grant special traits
    
    return {
        'tier': tier,
        'org_type': org_type,
        'organization': organization,
        'profession': profession,
        'tactics': tactics,
        'tactics_count': tactics_count,
        'expected_tactics': expected_tactics,
        'endowments': endowments,
        'endowments_count': endowments_count,
        'expected_endowments': expected_endowments,
        'has_status': has_status,
        'status_dots': status_dots,
        'status_merit_name': status_merit_name
    }


def calculate_mummy_chargen(character, stats, merits):
    """
    Calculate Mummy/Arisen-specific chargen tracking.
    
    Returns:
        dict: Mummy chargen information
    """
    # Decree bonus affinities and defining pillars
    DECREE_DATA = {
        'ashem': {'pillar': 'sheut', 'affinity': 'jackals_shade', 'name': 'Jackals'},
        'jackal': {'pillar': 'sheut', 'affinity': 'jackals_shade', 'name': 'Jackals'},
        'deshret': {'pillar': 'ba', 'affinity': 'soaring_falcon', 'name': 'Falcons'},
        'falcon': {'pillar': 'ba', 'affinity': 'soaring_falcon', 'name': 'Falcons'},
        'kheru': {'pillar': 'ab', 'affinity': 'lions_pride', 'name': 'Lions'},
        'lion': {'pillar': 'ab', 'affinity': 'lions_pride', 'name': 'Lions'},
        'nesrem': {'pillar': 'ka', 'affinity': 'guardian_bull', 'name': 'Bulls'},
        'bull': {'pillar': 'ka', 'affinity': 'guardian_bull', 'name': 'Bulls'},
        'usheb': {'pillar': 'ren', 'affinity': 'serpents_tongue', 'name': 'Serpents'},
        'serpent': {'pillar': 'ren', 'affinity': 'serpents_tongue', 'name': 'Serpents'}
    }
    
    # Guild vessel types
    GUILD_VESSELS = {
        'maa-kep': 'Amulets',
        'maa_kep': 'Amulets',
        'mesen-nebu': 'Regia',
        'mesen_nebu': 'Regia',
        'sesha-hebsu': 'Texts',
        'sesha_hebsu': 'Texts',
        'su-menent': 'Uter',
        'su_menent': 'Uter',
        'tef-aabhi': 'Effigies',
        'tef_aabhi': 'Effigies'
    }
    
    # Get character's decree, guild, and judge
    bio = stats.get('bio', {})
    decree = bio.get('decree', '').lower()
    guild = bio.get('guild', '').lower().replace('-', '_')
    judge = bio.get('judge', '')
    
    decree_info = DECREE_DATA.get(decree, {})
    defining_pillar = decree_info.get('pillar', None)
    decree_affinity = decree_info.get('affinity', None)
    decree_name = decree_info.get('name', decree.title())
    guild_vessel = GUILD_VESSELS.get(guild, None)
    
    # Check for Balance and Burden (Mummy's version - stored as anchors)
    anchors = stats.get('anchors', {})
    has_balance = 'balance' in anchors and anchors['balance'] and anchors['balance'] != '<not set>'
    has_burden = 'burden' in anchors and anchors['burden'] and anchors['burden'] != '<not set>'
    
    # Get Pillars (Ab, Ba, Ka, Ren, Sheut)
    other = stats.get('other', {})
    pillars = {
        'ab': other.get('ab', 0),
        'ba': other.get('ba', 0),
        'ka': other.get('ka', 0),
        'ren': other.get('ren', 0),
        'sheut': other.get('sheut', 0)
    }
    
    pillar_total = sum(pillars.values())
    pillar_available = 9
    
    # Check if defining pillar is highest
    defining_pillar_dots = pillars.get(defining_pillar, 0) if defining_pillar else 0
    max_pillar_dots = max(pillars.values()) if pillars.values() else 0
    defining_pillar_is_highest = (defining_pillar_dots == max_pillar_dots and max_pillar_dots > 0)
    
    # Get Affinities
    powers = stats.get('powers', {})
    affinities = []
    soul_affinities = []
    
    for power_name in powers.keys():
        power_lower = power_name.lower()
        if power_name.startswith('affinity:') or 'affinity' in power_lower:
            affinities.append(power_name)
            # Check if it's a soul affinity (would need data to determine)
            if any(soul in power_lower for soul in ['ab_', 'ba_', 'ka_', 'ren_', 'sheut_']):
                soul_affinities.append(power_name)
    
    affinities_count = len(affinities)
    expected_affinities = 4  # 1 decree + 1 guild + 2 soul
    
    # Get Utterances
    utterances = []
    has_dreams_of_dead_gods = False
    
    for power_name in powers.keys():
        power_lower = power_name.lower()
        if 'utterance' in power_lower or power_name.startswith('utterance:'):
            utterances.append(power_name)
            if 'dreams_of_dead_gods' in power_lower or 'dreams of dead gods' in power_lower:
                has_dreams_of_dead_gods = True
    
    utterances_count = len(utterances)
    expected_utterances = 3  # 2 chosen + Dreams of Dead Gods
    
    # Memory stat
    memory = other.get('memory', 3)
    
    # Sekhem stat
    sekhem = other.get('sekhem', 10)
    
    # Check for free merits: Cult and Tomb
    has_cult = any('cult' in m.lower() for m in merits.keys())
    has_tomb = any('tomb' in m.lower() for m in merits.keys())
    
    cult_dots = 0
    tomb_dots = 0
    for merit_name, merit_data in merits.items():
        if 'cult' in merit_name.lower():
            try:
                if 'dots' in merit_data:
                    cult_dots = int(merit_data['dots'])
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
        elif 'tomb' in merit_name.lower():
            try:
                if 'dots' in merit_data:
                    tomb_dots = int(merit_data['dots'])
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
    
    # Touchstones (Mummy only needs 1 to start)
    # Would check character's touchstone data
    
    return {
        'decree': decree,
        'decree_name': decree_name,
        'guild': guild,
        'guild_vessel': guild_vessel,
        'judge': judge,
        'defining_pillar': defining_pillar,
        'decree_affinity': decree_affinity,
        'has_balance': has_balance,
        'has_burden': has_burden,
        'pillars': pillars,
        'pillar_total': pillar_total,
        'pillar_available': pillar_available,
        'defining_pillar_dots': defining_pillar_dots,
        'defining_pillar_is_highest': defining_pillar_is_highest,
        'affinities': affinities,
        'affinities_count': affinities_count,
        'expected_affinities': expected_affinities,
        'soul_affinities': soul_affinities,
        'utterances': utterances,
        'utterances_count': utterances_count,
        'expected_utterances': expected_utterances,
        'has_dreams_of_dead_gods': has_dreams_of_dead_gods,
        'memory': memory,
        'sekhem': sekhem,
        'has_cult': has_cult,
        'cult_dots': cult_dots,
        'has_tomb': has_tomb,
        'tomb_dots': tomb_dots
    }


def calculate_promethean_chargen(character, stats, merits):
    """
    Calculate Promethean-specific chargen tracking.
    
    Returns:
        dict: Promethean chargen information
    """
    # Lineage Bestowments (2 options per lineage)
    LINEAGE_BESTOWMENTS = {
        'frankenstein': ['Unnatural Strength', 'Unholy Fortitude'],
        'galateid': ['Mesmerizing Appearance', 'Uncanny Presence'],
        'osiris': ['Revivification', 'Shed the Coil'],
        'tammuz': ['Unholy Fortitude', 'Uncanny Resilience'],
        'ulgan': ['Ephemeral Flesh', 'Shapeshifting'],
        'unfleshed': ['Body Thief', 'Uncanny Resilience'],
        'extempore': ['Any']  # Wild card, can choose any
    }
    
    # Refinement Transmutations (basic refinements)
    REFINEMENT_TRANSMUTATIONS = {
        'aurum': ['deception', 'mesmerism'],
        'cuprum': ['disquietism', 'sensorium'],
        'ferrum': ['corporeum', 'vitality'],
        'mercurius': ['alchemicus', 'metamorphosis'],
        'stannum': ['vulcanus', 'contamination']
    }
    
    # Get character's lineage and refinement
    bio = stats.get('bio', {})
    lineage = bio.get('lineage', '').lower()
    refinement = bio.get('refinement', '').lower()
    role = bio.get('role', '')  # Current Role within the Refinement
    
    bestowment_options = LINEAGE_BESTOWMENTS.get(lineage, [])
    refinement_transmutations = REFINEMENT_TRANSMUTATIONS.get(refinement, [])
    
    # Check for Elpis and Torment
    anchors = stats.get('anchors', {})
    has_elpis = 'elpis' in anchors and anchors['elpis'] and anchors['elpis'] != '<not set>'
    has_torment = 'torment' in anchors and anchors['torment'] and anchors['torment'] != '<not set>'
    
    # Get Bestowment (should have 1)
    powers = stats.get('powers', {})
    bestowments = []
    for power_name in powers.keys():
        power_lower = power_name.lower()
        if power_name.startswith('bestowment:') or any(best.lower().replace(' ', '_') in power_lower for best in ['unnatural_strength', 'unholy_fortitude', 'mesmerizing_appearance', 'uncanny_presence', 'revivification', 'shed_the_coil', 'uncanny_resilience', 'ephemeral_flesh', 'shapeshifting', 'body_thief']):
            bestowments.append(power_name)
    
    has_bestowment = len(bestowments) > 0
    
    # Get Transmutations/Alembics
    alembics = []
    transmutations = {}
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower()
        
        # Check for Alembics (manifestations of transmutations)
        if power_name.startswith('alembic:'):
            alembics.append(power_name)
        
        # Check for Transmutations
        if any(trans in power_lower for trans in ['corporeum', 'deception', 'disquietism', 'mesmerism', 'sensorium', 'vitality', 'alchemicus', 'metamorphosis', 'vulcanus', 'contamination']):
            dots = power_value if isinstance(power_value, int) else 1
            transmutations[power_name] = dots
    
    alembics_count = len(alembics)
    expected_alembics = 2  # One per Refinement transmutation
    
    # Azoth tracking
    azoth = stats.get('advantages', {}).get('azoth', 1)
    # Azoth always starts at 1, no merit cost
    
    # Pilgrimage tracking
    other = stats.get('other', {})
    pilgrimage = other.get('pilgrimage', 1)
    # Pilgrimage starts at 1, raised with Vitriol XP
    
    # Pyros (fuel) - starts at half max (Azoth * 10 / 2)
    max_pyros = azoth * 10
    starting_pyros = (max_pyros + 1) // 2  # Round up
    pyros = other.get('pyros', starting_pyros)
    
    # Touchstones (need 1 associated with role/pilgrimage)
    has_touchstone_merit = any('touchstone' in m.lower() for m in merits.keys())
    
    # Pilgrimage questions (answered via +bio or stored somewhere)
    # These would typically be stored in character's bio or background
    
    return {
        'lineage': lineage,
        'refinement': refinement,
        'role': role,
        'bestowment_options': bestowment_options,
        'bestowments': bestowments,
        'has_bestowment': has_bestowment,
        'refinement_transmutations': refinement_transmutations,
        'has_elpis': has_elpis,
        'has_torment': has_torment,
        'alembics': alembics,
        'alembics_count': alembics_count,
        'expected_alembics': expected_alembics,
        'transmutations': transmutations,
        'azoth': azoth,
        'pilgrimage': pilgrimage,
        'pyros': pyros,
        'max_pyros': max_pyros,
        'has_touchstone_merit': has_touchstone_merit
    }


def calculate_mortalplus_chargen(character, stats, merits):
    """
    Calculate Mortal+ template chargen tracking.
    Routes to specific sub-function based on template_type.
    
    Returns:
        dict: Mortal+ chargen information
    """
    bio = stats.get('bio', {})
    template_type = bio.get('template_type', '').lower()
    
    if template_type == 'ghoul':
        return calculate_ghoul_chargen(character, stats, merits)
    elif template_type == 'revenant':
        return calculate_revenant_chargen(character, stats, merits)
    elif template_type == 'dhampir':
        return calculate_dhampir_chargen(character, stats, merits)
    elif template_type in ['wolf-blooded', 'wolf_blooded', 'wolfblooded']:
        return calculate_wolfblooded_chargen(character, stats, merits)
    elif template_type == 'psychic':
        return calculate_psychic_chargen(character, stats, merits)
    elif template_type == 'atariya':
        return calculate_atariya_chargen(character, stats, merits)
    elif template_type == 'infected':
        return calculate_infected_chargen(character, stats, merits)
    elif template_type == 'plain':
        return calculate_plain_chargen(character, stats, merits)
    elif template_type in ['lost boy', 'lost_boy', 'lostboy']:
        return calculate_lostboy_chargen(character, stats, merits)
    elif template_type in ['psychic vampire', 'psychic_vampire', 'psychicvampire']:
        return calculate_psychicvampire_chargen(character, stats, merits)
    elif template_type in ['immortal', 'endless']:
        return calculate_immortal_chargen(character, stats, merits)
    elif template_type == 'proximus':
        return calculate_proximus_chargen(character, stats, merits)
    elif template_type == 'sleepwalker':
        return calculate_sleepwalker_chargen(character, stats, merits)
    elif template_type in ['fae-touched', 'fae_touched', 'faetouched']:
        return calculate_faetouched_chargen(character, stats, merits)
    else:
        # Generic Mortal+ without specific type
        return {
            'template_type': template_type,
            'has_type': bool(template_type)
        }


def calculate_ghoul_chargen(character, stats, merits):
    """Calculate Ghoul-specific chargen tracking."""
    bio = stats.get('bio', {})
    
    # Clan from regnant (subtype field)
    clan = bio.get('subtype', '') or bio.get('clan', '')
    
    # Disciplines (2 dots from regnant's in-clan)
    powers = stats.get('powers', {})
    disciplines = {}
    discipline_dots = 0
    
    CLAN_DISCIPLINES = {
        'daeva': ['celerity', 'majesty', 'vigor'],
        'gangrel': ['animalism', 'protean', 'resilience'],
        'mekhet': ['auspex', 'celerity', 'obfuscate'],
        'nosferatu': ['nightmare', 'obfuscate', 'vigor'],
        'ventrue': ['animalism', 'dominate', 'resilience']
    }
    
    in_clan = CLAN_DISCIPLINES.get(clan.lower(), [])
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower().replace(' ', '_')
        # Check disciplines
        if power_lower in ['animalism', 'auspex', 'celerity', 'dominate', 'majesty', 'nightmare', 'obfuscate', 'protean', 'resilience', 'vigor']:
            dots = power_value if isinstance(power_value, int) else 1
            disciplines[power_name] = dots
            discipline_dots += dots
    
    # Blood Potency (always 0 for ghouls)
    blood_potency = stats.get('advantages', {}).get('blood_potency', 0)
    
    return {
        'template_type': 'ghoul',
        'clan': clan,
        'in_clan_disciplines': in_clan,
        'disciplines': disciplines,
        'discipline_dots': discipline_dots,
        'discipline_available': 2,
        'blood_potency': blood_potency
    }


def calculate_revenant_chargen(character, stats, merits):
    """Calculate Revenant-specific chargen tracking."""
    bio = stats.get('bio', {})
    anchors = stats.get('anchors', {})
    
    # Clan (family lineage)
    clan = bio.get('subtype', '') or bio.get('clan', '')
    
    # Mask, Dirge, Touchstone
    has_mask = (('mask' in bio and bio['mask'] and bio['mask'] != '<not set>') or 
                ('mask' in anchors and anchors['mask'] and anchors['mask'] != '<not set>'))
    has_dirge = (('dirge' in bio and bio['dirge'] and bio['dirge'] != '<not set>') or 
                 ('dirge' in anchors and anchors['dirge'] and anchors['dirge'] != '<not set>'))
    
    has_touchstone_merit = any('touchstone' in m.lower() for m in merits.keys())
    
    # Disciplines (3 dots, 1 must be physical, none unique)
    powers = stats.get('powers', {})
    disciplines = {}
    discipline_dots = 0
    physical_discipline_dots = 0
    
    PHYSICAL_DISCIPLINES = ['celerity', 'protean', 'resilience', 'vigor']
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower().replace(' ', '_')
        if power_lower in ['animalism', 'auspex', 'celerity', 'dominate', 'majesty', 'nightmare', 'obfuscate', 'protean', 'resilience', 'vigor']:
            dots = power_value if isinstance(power_value, int) else 1
            disciplines[power_name] = dots
            discipline_dots += dots
            
            if power_lower in PHYSICAL_DISCIPLINES:
                physical_discipline_dots += dots
    
    # Blood Potency (1 for revenants)
    blood_potency = stats.get('advantages', {}).get('blood_potency', 1)
    
    return {
        'template_type': 'revenant',
        'clan': clan,
        'disciplines': disciplines,
        'discipline_dots': discipline_dots,
        'discipline_available': 3,
        'physical_discipline_dots': physical_discipline_dots,
        'blood_potency': blood_potency,
        'has_mask': has_mask,
        'has_dirge': has_dirge,
        'has_touchstone_merit': has_touchstone_merit
    }


def calculate_dhampir_chargen(character, stats, merits):
    """Calculate Dhampir-specific chargen tracking."""
    bio = stats.get('bio', {})
    
    # Parent clan (subtype field)
    parent_clan = bio.get('subtype', '') or bio.get('clan', '')
    
    # Clan themes (3 total, 1 dot each from parent clan)
    CLAN_THEMES = {
        'daeva': ['attention', 'desire', 'submission'],
        'gangrel': ['adaptation', 'release', 'subsistence'],
        'mekhet': ['identity', 'paranoia', 'secrets'],
        'nosferatu': ['grotesquerie', 'solitude', 'terror'],
        'ventrue': ['birthright', 'control', 'victory']
    }
    
    parent_themes = CLAN_THEMES.get(parent_clan.lower(), [])
    
    # Get Themes and Twists
    powers = stats.get('powers', {})
    themes = {}
    twists = {}
    twist_dots = 0
    
    for power_name, power_value in powers.items():
        power_lower = power_name.lower()
        
        # Check for themes
        if power_name.startswith('theme:'):
            dots = power_value if isinstance(power_value, int) else 1
            themes[power_name] = dots
        
        # Check for twists
        if power_name.startswith('twist:'):
            dots = power_value if isinstance(power_value, int) else 1
            twists[power_name] = dots
            twist_dots += dots
    
    # Check parent themes have dots
    parent_themes_set = all(
        any(theme in p.lower() for p in themes.keys())
        for theme in parent_themes
    )
    
    # Destiny, Doom, Affliction (bio fields)
    destiny = bio.get('destiny', '')
    doom = bio.get('doom', '')
    affliction = bio.get('affliction', '')
    
    # Check for required merits
    has_blood_sense = any('blood sense' in m.lower() for m in merits.keys())
    has_omen_sensitivity = any('omen sensitivity' in m.lower() for m in merits.keys())
    has_thief_of_fate = any('thief of fate' in m.lower() for m in merits.keys())
    
    # Malisons (purchased with merit dots)
    malisons = []
    for power_name in powers.keys():
        if power_name.startswith('malison:'):
            malisons.append(power_name)
    
    return {
        'template_type': 'dhampir',
        'parent_clan': parent_clan,
        'parent_themes': parent_themes,
        'themes': themes,
        'parent_themes_set': parent_themes_set,
        'twists': twists,
        'twist_dots': twist_dots,
        'twist_available': 3,
        'destiny': destiny,
        'doom': doom,
        'affliction': affliction,
        'has_blood_sense': has_blood_sense,
        'has_omen_sensitivity': has_omen_sensitivity,
        'has_thief_of_fate': has_thief_of_fate,
        'malisons': malisons
    }


def calculate_wolfblooded_chargen(character, stats, merits):
    """Calculate Wolf-Blooded-specific chargen tracking."""
    bio = stats.get('bio', {})
    
    # Tell (subtype field)
    tell = bio.get('subtype', '') or bio.get('tell', '')
    
    return {
        'template_type': 'wolf-blooded',
        'tell': tell,
        'has_tell': bool(tell)
    }


def calculate_psychic_chargen(character, stats, merits):
    """Calculate Psychic-specific chargen tracking."""
    # Psychics primarily use merits for their abilities
    psychic_merits = []
    psychic_merit_dots = 0
    
    PSYCHIC_MERIT_NAMES = [
        'aura reading', 'automatic writing', 'biokinesis', 'clairvoyance',
        'medium', 'numbing touch', 'psychokinesis', 'psychometry',
        'telekinesis', 'telepathy', 'animal possession', 'apportation',
        'biomimicry', 'doppelganger', 'incite ecosystem', 'invoke spirit',
        'mind control', 'phantasmagoria', 'psychic concealment', 'psychic onslaught',
        'psychic poltergeist', 'psychokinetic combat', 'psychokinetic resistance',
        'sojourner', 'tactical telepathy', 'technopathy', 'telekinetic evasion'
    ]
    
    for merit_name, merit_data in merits.items():
        merit_lower = merit_name.lower()
        if any(psychic in merit_lower for psychic in PSYCHIC_MERIT_NAMES):
            psychic_merits.append(merit_name)
            try:
                if 'dots' in merit_data:
                    psychic_merit_dots += int(merit_data['dots'])
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
    
    return {
        'template_type': 'psychic',
        'psychic_merits': psychic_merits,
        'psychic_merit_dots': psychic_merit_dots
    }


def calculate_atariya_chargen(character, stats, merits):
    """Calculate Atariya-specific chargen tracking."""
    # Atariya must have Damn Lucky Merit
    has_damn_lucky = any('damn lucky' in m.lower() for m in merits.keys())
    
    return {
        'template_type': 'atariya',
        'has_damn_lucky': has_damn_lucky
    }


def calculate_infected_chargen(character, stats, merits):
    """Calculate Infected-specific chargen tracking."""
    # Infected start with Carrier Merit
    has_carrier = any('carrier' in m.lower() for m in merits.keys())
    
    # Check for Latent Symptoms condition (would be in conditions, not merits)
    # This is typically tracked separately
    
    return {
        'template_type': 'infected',
        'has_carrier': has_carrier
    }


def calculate_plain_chargen(character, stats, merits):
    """Calculate Plain-specific chargen tracking."""
    # Plain get Plain Reader Merit for free
    has_plain_reader = any('plain reader' in m.lower() for m in merits.keys())
    
    # Other Plain Merits they might have
    plain_merits = []
    for merit_name in merits.keys():
        if 'plain' in merit_name.lower() and 'reader' not in merit_name.lower():
            plain_merits.append(merit_name)
    
    return {
        'template_type': 'plain',
        'has_plain_reader': has_plain_reader,
        'plain_merits': plain_merits
    }


def calculate_lostboy_chargen(character, stats, merits):
    """Calculate Lost Boy (Delta Protocol) chargen tracking."""
    # Lost Boys get Protocol Merit for free (1 dot)
    has_protocol = any('protocol' in m.lower() for m in merits.keys())
    protocol_dots = 0
    
    for merit_name, merit_data in merits.items():
        if 'protocol' in merit_name.lower():
            try:
                if 'dots' in merit_data:
                    protocol_dots = int(merit_data['dots'])
                    break
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
    
    # Protocol augmentation merits
    protocol_merits = []
    for merit_name in merits.keys():
        merit_lower = merit_name.lower()
        if 'protocol' in merit_lower and merit_lower != 'protocol':
            protocol_merits.append(merit_name)
    
    return {
        'template_type': 'lost_boy',
        'has_protocol': has_protocol,
        'protocol_dots': protocol_dots,
        'protocol_merits': protocol_merits
    }


def calculate_psychicvampire_chargen(character, stats, merits):
    """Calculate Psychic Vampire chargen tracking."""
    bio = stats.get('bio', {})
    
    # Psychic Vampires get Psychic Vampirism Merit for free (1 dot)
    has_psychic_vampirism = any('psychic vampirism' in m.lower() for m in merits.keys())
    vampirism_dots = 0
    
    for merit_name, merit_data in merits.items():
        if 'psychic vampirism' in merit_name.lower():
            try:
                if 'dots' in merit_data:
                    vampirism_dots = int(merit_data['dots'])
                    break
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
    
    # Check for Ephemeral Battery
    has_ephemeral_battery = any('ephemeral battery' in m.lower() for m in merits.keys())
    
    # Ephemera storage
    other = stats.get('other', {})
    attributes = stats.get('attributes', {})
    resolve = attributes.get('resolve', 1)
    
    ephemera = other.get('ephemera', 0)
    max_ephemera = resolve  # Base storage is Resolve dots
    
    # Check if tied to a relic (bonus dot in other merits)
    has_relic = bio.get('psychic_relic', False)
    
    return {
        'template_type': 'psychic_vampire',
        'has_psychic_vampirism': has_psychic_vampirism,
        'vampirism_dots': vampirism_dots,
        'has_ephemeral_battery': has_ephemeral_battery,
        'ephemera': ephemera,
        'max_ephemera': max_ephemera,
        'has_relic': has_relic
    }


def calculate_immortal_chargen(character, stats, merits):
    """Calculate Immortal (Endless) chargen tracking."""
    bio = stats.get('bio', {})
    
    # Immortality method (stored as subtype)
    subtype = bio.get('subtype', '').lower().replace(' ', '_')
    
    # Immortal types and favored attributes
    IMMORTAL_TYPES = {
        'blood_bather': {'favored_attr': 'presence', 'name': 'Blood Bather'},
        'body_thief': {'favored_attr': 'manipulation', 'name': 'Body Thief'},
        'mystical_thief': {'favored_attr': 'manipulation', 'name': 'Body Thief (Mystical)'},
        'psychic_thief': {'favored_attr': 'manipulation', 'name': 'Body Thief (Psychic)'},
        'eternal': {'favored_attr': 'stamina', 'name': 'Eternal'},
        'reborn': {'favored_attr': 'intelligence', 'name': 'Reborn'}
    }
    
    immortal_info = IMMORTAL_TYPES.get(subtype, {})
    immortal_name = immortal_info.get('name', subtype.replace('_', ' ').title())
    favored_attribute = immortal_info.get('favored_attr', None)
    
    # Check for favored attribute bonus
    other = stats.get('other', {})
    favored_attr_used = other.get('favored_stat', None)
    
    # Immortals get a free dot in their favored attribute
    has_favored_attr = (favored_attr_used == favored_attribute)
    
    # Sekhem (Immortal power stat)
    sekhem = other.get('sekhem', 1)
    
    # Endless Potency Merits (1 free dot in favored attribute's potency)
    has_endless_potency = False
    potency_dots = 0
    
    for merit_name, merit_data in merits.items():
        merit_lower = merit_name.lower()
        if 'endless potency' in merit_lower and favored_attribute and favored_attribute in merit_lower:
            has_endless_potency = True
            try:
                if 'dots' in merit_data:
                    potency_dots = int(merit_data['dots'])
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
            break
    
    # Relic (Eternals get 1 free dot)
    has_relic = any('relic' in m.lower() for m in merits.keys())
    relic_dots = 0
    
    if subtype == 'eternal':
        for merit_name, merit_data in merits.items():
            if 'relic' in merit_name.lower():
                try:
                    if 'dots' in merit_data:
                        relic_dots = int(merit_data['dots'])
                        break
                except (KeyError, ValueError, TypeError, AttributeError):
                    pass
    
    # Investment (if part of mummy cult)
    investment = bio.get('investment', '')  # Which Arisen invested in them
    invested_pillars = other.get('invested_pillars', {})  # Pillars invested by the Arisen
    
    has_investment = bool(investment)
    
    # Virtue and Vice
    anchors = stats.get('anchors', {})
    has_virtue = 'virtue' in anchors and anchors['virtue'] and anchors['virtue'] != '<not set>'
    has_vice = 'vice' in anchors and anchors['vice'] and anchors['vice'] != '<not set>'
    
    # Curse/Method description (stored in bio or other)
    curse_method = bio.get('curse', '') or bio.get('method', '')
    has_curse_method = bool(curse_method)
    
    return {
        'template_type': 'immortal',
        'subtype': subtype,
        'immortal_name': immortal_name,
        'favored_attribute': favored_attribute,
        'has_favored_attr': has_favored_attr,
        'favored_attr_used': favored_attr_used,
        'sekhem': sekhem,
        'has_endless_potency': has_endless_potency,
        'potency_dots': potency_dots,
        'has_relic': has_relic,
        'relic_dots': relic_dots,
        'investment': investment,
        'has_investment': has_investment,
        'invested_pillars': invested_pillars,
        'has_virtue': has_virtue,
        'has_vice': has_vice,
        'curse_method': curse_method,
        'has_curse_method': has_curse_method
    }


def calculate_proximus_chargen(character, stats, merits):
    """Calculate Proximus-specific chargen tracking."""
    bio = stats.get('bio', {})
    
    # Parent Path (stored as path or subtype)
    parent_path = bio.get('path', '') or bio.get('subtype', '')
    
    # Path Ruling Arcana
    PATH_ARCANA = {
        'acanthus': {'ruling': ['fate', 'time']},
        'mastigos': {'ruling': ['mind', 'space']},
        'moros': {'ruling': ['death', 'matter']},
        'obrimos': {'ruling': ['forces', 'prime']},
        'thyrsus': {'ruling': ['life', 'spirit']}
    }
    
    path_info = PATH_ARCANA.get(parent_path.lower(), {})
    ruling_arcana = path_info.get('ruling', [])
    
    # Blessing Arcana (ruling + 1 chosen, stored somewhere)
    other = stats.get('other', {})
    chosen_arcanum = other.get('blessing_arcanum', None)
    
    blessing_arcana = ruling_arcana.copy()
    if chosen_arcanum:
        blessing_arcana.append(chosen_arcanum.lower())
    
    # Blessings (purchased as merits)
    blessings = []
    blessing_dots = 0
    
    for merit_name, merit_data in merits.items():
        if merit_name.startswith('blessing:'):
            blessings.append(merit_name)
            try:
                if 'dots' in merit_data:
                    blessing_dots += int(merit_data['dots'])
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
    
    max_blessings = 30  # Up to 30 dots worth of Blessings
    
    # Mana capacity
    mana = other.get('mana', 0)
    max_mana = 5  # Always 5 for Proximi
    
    # Familial Curse (stored in bio or other)
    curse = bio.get('curse', '') or other.get('familial_curse', '')
    has_curse = bool(curse)
    
    # Dynasty name (family name)
    dynasty = bio.get('dynasty', '') or bio.get('family', '')
    has_dynasty = bool(dynasty)
    
    return {
        'template_type': 'proximus',
        'parent_path': parent_path,
        'ruling_arcana': ruling_arcana,
        'chosen_arcanum': chosen_arcanum,
        'blessing_arcana': blessing_arcana,
        'blessings': blessings,
        'blessing_dots': blessing_dots,
        'max_blessings': max_blessings,
        'mana': mana,
        'max_mana': max_mana,
        'curse': curse,
        'has_curse': has_curse,
        'dynasty': dynasty,
        'has_dynasty': has_dynasty
    }


def calculate_sleepwalker_chargen(character, stats, merits):
    """Calculate Sleepwalker-specific chargen tracking."""
    # Sleepwalker merit (1 dot, free)
    has_sleepwalker = any('sleepwalker' in m.lower() for m in merits.keys())
    
    # Count Sleepwalker-specific merits
    sleepwalker_merits = []
    SLEEPWALKER_MERIT_NAMES = [
        'banner-bearer', 'deadpan', 'fitful slumber', 'loved', 'proxy voice',
        'relic attuned', 'ritual martyr', 'ritual savvy', 'slippery'
    ]
    
    for merit_name in merits.keys():
        merit_lower = merit_name.lower().replace('_', '-')
        if any(sw_merit in merit_lower for sw_merit in SLEEPWALKER_MERIT_NAMES):
            sleepwalker_merits.append(merit_name)
    
    return {
        'template_type': 'sleepwalker',
        'has_sleepwalker': has_sleepwalker,
        'sleepwalker_merits': sleepwalker_merits
    }


def calculate_faetouched_chargen(character, stats, merits):
    """Calculate Fae-Touched-specific chargen tracking."""
    bio = stats.get('bio', {})
    other = stats.get('other', {})
    
    # Promise (stored in bio or other)
    promise = bio.get('promise', '') or other.get('promise', '')
    has_promise = bool(promise)
    
    # Promise type (Clemency, Debt, Love, Loyalty, Protection, Provision, Service)
    promise_type = other.get('promise_type', '')
    
    # Wyrd (always 0 for fae-touched)
    wyrd = stats.get('advantages', {}).get('wyrd', 0)
    
    # Glamour
    glamour = other.get('glamour', 0)
    max_glamour = 10  # Always 10 for fae-touched
    
    # Favored Regalia (choose 1)
    favored_regalia = other.get('favored_regalia', None)
    
    # Contracts (2 Common from favored Regalia)
    powers = stats.get('powers', {})
    contracts = []
    contract_count = 0
    
    for power_name in powers.keys():
        power_lower = power_name.lower()
        if power_name.startswith('contract:') or 'contract' in power_lower:
            contracts.append(power_name)
            contract_count += 1
    
    expected_contracts = 2
    
    # Court Goodwill (for Court Contracts)
    court_goodwill = {}
    for merit_name, merit_data in merits.items():
        merit_lower = merit_name.lower()
        if 'court goodwill' in merit_lower or ('goodwill' in merit_lower and any(court in merit_lower for court in ['spring', 'summer', 'autumn', 'winter'])):
            try:
                if 'dots' in merit_data:
                    court_goodwill[merit_name] = int(merit_data['dots'])
            except (KeyError, ValueError, TypeError, AttributeError):
                pass
    
    # Starting Conditions (Madness, Arcadian Dreams, Hedge Addiction)
    # These would be tracked separately but noted here
    
    # Fae-Touched specific merits
    faetouched_merits = []
    for merit_name in merits.keys():
        merit_lower = merit_name.lower()
        # Promise merits
        if 'promise' in merit_lower or 'dreamer' in merit_lower or 'oathbreaker' in merit_lower:
            faetouched_merits.append(merit_name)
    
    return {
        'template_type': 'fae-touched',
        'promise': promise,
        'has_promise': has_promise,
        'promise_type': promise_type,
        'wyrd': wyrd,
        'glamour': glamour,
        'max_glamour': max_glamour,
        'favored_regalia': favored_regalia,
        'contracts': contracts,
        'contract_count': contract_count,
        'expected_contracts': expected_contracts,
        'court_goodwill': court_goodwill,
        'faetouched_merits': faetouched_merits
    }
