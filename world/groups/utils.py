"""
Group utility functions for automatic assignment and character attribute management.
Updated to work with TypeClass-based groups instead of Django models.
"""

from evennia import logger
from evennia.comms.models import ChannelDB
from typeclasses.groups import (
    Group, create_group, get_group_by_name, get_group_by_id, 
    get_all_groups, get_character_groups
)


def get_character_characteristics(character):
    """
    Extract relevant characteristics from a character for group assignment.
    Returns a dict with template, clan, covenant, etc.
    """
    if not hasattr(character, 'db') or not character.db.stats:
        return {}
    
    stats = character.db.stats
    other = stats.get('other', {})
    
    characteristics = {
        'template': other.get('template', '').lower(),
    }
    
    # Add template-specific bio fields
    if characteristics['template'] == 'vampire':
        characteristics['clan'] = other.get('clan', '').lower()
        characteristics['covenant'] = other.get('covenant', '').lower()
    elif characteristics['template'] == 'mage':
        characteristics['path'] = other.get('path', '').lower()
        characteristics['order'] = other.get('order', '').lower()
    elif characteristics['template'] == 'werewolf':
        characteristics['auspice'] = other.get('auspice', '').lower()
        characteristics['tribe'] = other.get('tribe', '').lower()
    elif characteristics['template'] == 'changeling':
        characteristics['seeming'] = other.get('seeming', '').lower()
        characteristics['court'] = other.get('court', '').lower()
    elif characteristics['template'] == 'hunter':
        characteristics['organization'] = other.get('organization', '').lower()
        characteristics['creed'] = other.get('creed', '').lower()
    
    return characteristics


def get_automatic_groups_for_character(character):
    """
    Determine which groups a character should automatically be assigned to
    based on their characteristics.
    """
    characteristics = get_character_characteristics(character)
    
    if not characteristics.get('template'):
        return []
    
    auto_groups = []
    
    # Template-based groups
    template = characteristics['template']
    if template:
        auto_groups.append(template.title())
    
    # Vampire-specific groups
    if template == 'vampire':
        clan = characteristics.get('clan')
        covenant = characteristics.get('covenant')
        
        if clan:
            auto_groups.append(clan.title())
        
        if covenant and covenant != 'unaligned':
            # Handle multi-word covenants
            covenant_map = {
                'carthian movement': 'Carthian Movement',
                'circle of the crone': 'Circle of the Crone',
                'invictus': 'Invictus',
                'lancea et sanctum': 'Lancea et Sanctum',
                'ordo dracul': 'Ordo Dracul'
            }
            auto_groups.append(covenant_map.get(covenant, covenant.title()))
    
    # Mage-specific groups
    elif template == 'mage':
        path = characteristics.get('path')
        order = characteristics.get('order')
        
        if path:
            auto_groups.append(path.title())
        
        if order and order not in ['seers of the throne']:  # Exclude hostile orders
            order_map = {
                'adamantine arrow': 'Adamantine Arrow',
                'guardians of the veil': 'Guardians of the Veil',
                'mysterium': 'Mysterium',
                'silver ladder': 'Silver Ladder',
                'free council': 'Free Council'
            }
            auto_groups.append(order_map.get(order, order.title()))
    
    # Werewolf-specific groups
    elif template == 'werewolf':
        auspice = characteristics.get('auspice')
        tribe = characteristics.get('tribe')
        
        if auspice:
            auto_groups.append(auspice.title())
        
        if tribe and tribe != 'ghost wolves':
            tribe_map = {
                'blood talons': 'Blood Talons',
                'bone shadows': 'Bone Shadows',
                'hunters in darkness': 'Hunters in Darkness',
                'iron masters': 'Iron Masters',
                'storm lords': 'Storm Lords'
            }
            auto_groups.append(tribe_map.get(tribe, tribe.title()))
    
    # Changeling-specific groups
    elif template == 'changeling':
        seeming = characteristics.get('seeming')
        court = characteristics.get('court')
        
        if seeming:
            auto_groups.append(seeming.title())
        
        if court and court != 'courtless':
            court_map = {
                'spring': 'Spring Court',
                'summer': 'Summer Court',
                'autumn': 'Autumn Court',
                'winter': 'Winter Court'
            }
            auto_groups.append(court_map.get(court, court.title()))
    
    # Hunter-specific groups
    elif template == 'hunter':
        organization = characteristics.get('organization')
        if organization:
            auto_groups.append(organization.title())
    
    return auto_groups


def ensure_group_exists(group_name, group_type='other', description=''):
    """
    Ensure a group exists, creating it if necessary.
    Returns the Group object.
    """
    # Try to find existing group
    group = get_group_by_name(group_name)
    if group:
        return group
    
    # Create the group using TypeClass function
    try:
        group = create_group(
            name=group_name,
            group_type=group_type,
            description=description or f"Auto-created group for {group_name}"
        )
        group.is_public = True
        
        logger.log_info(f"Auto-created group '{group_name}' with ID #{group.group_id}")
        return group
    except ValueError as e:
        logger.log_err(f"Failed to create group '{group_name}': {str(e)}")
        return None


def ensure_group_channel_exists(group):
    """
    Ensure a channel exists for the given group.
    This is now handled automatically by the Group TypeClass.
    """
    # The TypeClass handles channel creation automatically,
    # but we can force recreation if needed
    channel_name = group.channel_name
    
    if not ChannelDB.objects.filter(db_key=channel_name).exists():
        group._create_group_channel()


def assign_character_to_group(character, group, auto_assigned=True):
    """
    Assign a character to a group and handle all related tasks.
    """
    # Use the TypeClass method to add the member
    if group.add_member(character):
        if auto_assigned:
            logger.log_info(f"Auto-assigned {character.name} to group '{group.name}'")
        else:
            logger.log_info(f"Manually assigned {character.name} to group '{group.name}'")
        return True
    
    return False  # Already a member


def remove_character_from_group(character, group):
    """
    Remove a character from a group and handle all related cleanup.
    """
    # Use the TypeClass method to remove the member
    return group.remove_member(character)


def auto_assign_character_groups(character):
    """
    Automatically assign a character to appropriate groups based on their characteristics.
    This should be called when a character is approved.
    """
    auto_groups = get_automatic_groups_for_character(character)
    assigned_groups = []
    
    for group_name in auto_groups:
        # Determine group type based on name
        group_type = determine_group_type(group_name)
        
        # Ensure group exists
        group = ensure_group_exists(group_name, group_type)
        if not group:
            continue
        
        # Assign character to group
        if assign_character_to_group(character, group, auto_assigned=True):
            assigned_groups.append(group_name)
    
    return assigned_groups


def determine_group_type(group_name):
    """
    Determine the appropriate group type based on the group name.
    
    Sphere-level groups (Vampire, Mage, Changeling, etc.) use 'sphere' type.
    Specific sub-groups (clans, covenants, orders, etc.) use their specific types.
    """
    name_lower = group_name.lower()
    
    # Template/Sphere names - these are the top-level groups
    sphere_names = ['vampire', 'werewolf', 'mage', 'changeling', 'hunter', 'geist', 
                    'mummy', 'demon', 'deviant', 'promethean', 'mortal+', 'mortal']
    
    if name_lower in sphere_names:
        return 'sphere'
    
    # Vampire sub-groups (covenants and clans)
    vampire_covenants = ['carthian movement', 'circle of the crone', 'invictus', 
                        'lancea et sanctum', 'ordo dracul']
    vampire_clans = ['daeva', 'gangrel', 'mekhet', 'nosferatu', 'ventrue']
    
    if name_lower in vampire_covenants or name_lower in vampire_clans:
        return 'coterie'
    
    # Werewolf sub-groups (tribes and auspices)
    werewolf_tribes = ['blood talons', 'bone shadows', 'hunters in darkness', 
                      'iron masters', 'storm lords', 'ghost wolves']
    werewolf_auspices = ['cahalith', 'elodoth', 'irraka', 'ithaeur', 'rahu']
    
    if name_lower in werewolf_tribes or name_lower in werewolf_auspices:
        return 'pack'
    
    # Mage sub-groups (orders and paths)
    mage_orders = ['adamantine arrow', 'guardians of the veil', 'mysterium', 
                  'silver ladder', 'free council']
    mage_paths = ['acanthus', 'mastigos', 'moros', 'obrimos', 'thyrsus']
    
    if name_lower in mage_orders or name_lower in mage_paths:
        return 'cabal'
    
    # Changeling sub-groups (courts and seemings)
    changeling_courts = ['spring court', 'summer court', 'autumn court', 'winter court']
    changeling_seemings = ['beast', 'darkling', 'elemental', 'fairest', 'ogre', 'wizened']
    
    if name_lower in changeling_courts or name_lower in changeling_seemings:
        return 'motley'
    
    # Default for any other groups
    return 'other'


def sync_character_group_attributes(character):
    """
    Sync the character's group attributes with their actual memberships.
    This is useful for cleanup/maintenance.
    """
    actual_groups = [group.name for group in get_character_groups(character)]
    character.attributes.add('groups', actual_groups)
    
    return actual_groups 