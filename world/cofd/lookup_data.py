"""
Consolidated data structure for the character creation lookup system.
This module combines all stat types and provides enhanced lookup functionality.
"""

from world.cofd.stat_dictionary import (
    attribute_dictionary, skill_dictionary, 
    advantage_dictionary, anchor_dictionary
)
from world.cofd.merits.general_merits import all_merits as general_merits
from world.cofd.merits.vampire_merits import vampire_merits
from world.cofd.merits.mage_merits import mage_merits
from world.cofd.merits.werewolf_merits import werewolf_merits
from world.cofd.merits.changeling_merits import changeling_merits
from world.cofd.merits.geist_merits import geist_merits
from world.cofd.merits.demon_merits import demon_merits
from world.cofd.merits.deviant_merits import deviant_merits
from world.cofd.merits.hunter_merits import hunter_merits
from world.cofd.merits.mummy_merits import mummy_merits
from world.cofd.merits.promethean_merits import promethean_merits
from world.cofd.merits.minor_template_merits import (
    minor_template_merits, PSYCHIC_MERIT_NAMES,
    ghoul_merits, dhampir_merits, atariya_merits, psychic_vampire_merits,
    general_supernatural_merits
)
from world.cofd.templates.vampire import VAMPIRE_CLANS, VAMPIRE_BLOODLINES, VAMPIRE_COVENANTS, VAMPIRE_DISCIPLINES
from world.cofd.powers.vampire_clans import get_all_clans, get_all_bloodlines
from world.cofd.powers.vampire_covenants import get_all_covenants
from world.cofd.powers.vampire_disciplines import (
    ALL_DISCIPLINE_POWERS, DISCIPLINE_POWER_CATEGORIES,
    ALL_COILS, COILS_BY_MYSTERY,
    ALL_BLOODLINE_DISCIPLINES, BLOODLINE_DISCIPLINES_BY_BLOODLINE,
    ALL_DEVOTIONS, DEVOTIONS_BY_TYPE
)
from world.cofd.powers.vampire_rituals import (
    ALL_SCALES, SCALES_BY_MYSTERY,
    ALL_THEBAN, THEBAN_BY_RANK,
    ALL_CRUAC, CRUAC_BY_RANK,
    ALL_BLOODLINE_DEVOTIONS_EXTENDED, PENUMBRAE_CRUAC
)
from world.cofd.templates.mage import MAGE_PATHS, MAGE_ORDERS, MAGE_ARCANA, LEGACIES_BY_PATH, LEGACIES_BY_ORDER, UNLINKED_LEGACIES, ALL_LEGACIES
from world.cofd.powers.mage_paths import get_all_paths
from world.cofd.powers.mage_orders_detailed import get_all_orders_detailed
from world.cofd.powers.mage_legacies_detailed import get_all_legacies as get_all_legacies_detailed
from world.cofd.templates.demon import DEMON_INCARNATIONS, DEMON_AGENDAS, DEMON_EMBEDS, DEMON_EXPLOITS_LIST
from world.cofd.powers.demon_form import (
    DEMON_MODIFICATIONS, DEMON_TECHNOLOGIES, DEMON_PROPULSIONS, DEMON_PROCESSES,
    ALL_DEMON_MODIFICATIONS, ALL_DEMON_TECHNOLOGIES, ALL_DEMON_PROPULSIONS, ALL_DEMON_PROCESSES
)
from world.cofd.powers.demon_powers import (
    ALL_EMBEDS, DEMON_EXPLOITS,
    EMBEDS_BY_INCARNATION, EMBEDS_CACOPHONY, EMBEDS_INSTRUMENTAL, EMBEDS_MUNDANE, EMBEDS_VOCAL,
    ALL_EMBED_NAMES, ALL_EXPLOIT_NAMES
)
from world.cofd.templates.mortal_plus import ALL_MORTAL_PLUS_TYPES, PSYCHIC_POWERS
from world.cofd.templates.werewolf import WEREWOLF_AUSPICES, WEREWOLF_TRIBES, WEREWOLF_LODGES
from world.cofd.powers.werewolf_gifts import ALL_WEREWOLF_GIFTS
from world.cofd.powers.werewolf_auspices import get_all_auspices
from world.cofd.powers.werewolf_tribes import get_all_tribes, get_all_lodges
from world.cofd.powers.changeling_contracts import ALL_CHANGELING_CONTRACTS
from world.cofd.powers.changeling_kiths import ALL_KITHS
from world.cofd.powers.changeling_seemings import get_all_seemings, get_all_entitlements
from world.cofd.templates.changeling import CHANGELING_SEEMINGS, CHANGELING_COURTS, CHANGELING_KITHS, CHANGELING_ENTITLEMENTS
from world.cofd.templates.promethean import PROMETHEAN_TEMPLATE
from world.cofd.powers.promethean_powers import (
    PROMETHEAN_TRANSMUTATIONS, PROMETHEAN_ALEMBICS, 
    PROMETHEAN_BESTOWMENTS, PROMETHEAN_LINEAGES
)
from world.cofd.templates.legacy_promethean import ATHANORS_BY_LINEAGE
from world.cofd.promethean_anchors import ELPIDES, TORMENTS, ALL_ELPIDES, ALL_TORMENTS
from world.cofd.powers.hunter_endowments import ADVANCED_ARMORY, ANIMAL_CONTROL_KIT, BENEDICTION, CASTIGATION, DREAMSCAPE, ELIXIR, ENKOIMESIS, GOETIC_GOSPEL, HORROR_WITHIN, INFUSION, INK, INSPIRATION, LIVES_REMEMBERED, PERISPIRITISM, RELIC, RITES_DU_CHEVAL, RITES_OF_DENIAL, SEITOKUTEN, TELEINFORMATICS, THAUMATECHNOLOGY, XENOTECHNOLOGY
from world.cofd.templates.hunter import HUNTER_CONSPIRACIES, HUNTER_COMPACTS, HUNTER_TACTICS, HUNTER_ENDOWMENTS
from world.cofd.powers.hunter_tactics import get_all_tactics, MENTAL_TACTICS, PHYSICAL_TACTICS, SOCIAL_TACTICS
from world.cofd.powers.hunter_organizations import ALL_COMPACTS, ALL_CONSPIRACIES, get_all_organizations
from world.cofd.templates.mummy import (
    MUMMY_GUILDS, MUMMY_DECREES, MUMMY_JUDGES,
    MUMMY_AFFINITIES_DATA, MUMMY_UTTERANCES_DATA,
    ALL_AFFINITY_NAMES, ALL_UTTERANCE_NAMES
)
from world.cofd.templates.geist import GEIST_BURDENS, GEIST_KREWE_TYPES, GEIST_HAUNTS, GEIST_KEYS, GEIST_CEREMONIES
from world.cofd.powers.geist_powers import ALL_HAUNTS, GEIST_KEY_DETAILS
from world.cofd.templates.deviant import DEVIANT_ORIGINS, DEVIANT_CLADES, DEVIANT_SCARS, DEVIANT_VARIATIONS, DEVIANT_ADAPTATIONS
from world.cofd.templates.mortal_plus import (
    ALL_MORTAL_PLUS_TYPES, PSYCHIC_POWERS, PROXIMUS_FAMILIES,
    DEMON_BLOODED_LEVELS, GAME_LINE_HERITAGE, WOLF_BLOODED_TELLS
)
from world.cofd.powers.changing_breeds_favors import (
    CHANGING_BREED_FAVORS, CHANGING_BREED_ASPECTS,
    ALL_FAVOR_NAMES, ALL_ASPECT_NAMES, TRICKSTER_ONLY_ASPECTS
)
from world.cofd.templates.legacy_changingbreeds import (
    LEGACY_CHANGING_BREEDS, CHANGING_BREED_CATEGORIES,
    CHANGING_BREED_ACCORDS, ACCORD_SPECIALTIES, RESPECT_TYPES
)
import re


class LookupData:
    """Consolidated data structure for character creation lookups."""
    
    def __init__(self):
        self.attributes = attribute_dictionary
        self.skills = skill_dictionary
        self.advantages = advantage_dictionary
        self.anchors = anchor_dictionary
        self.general_merits = general_merits
        self.vampire_merits = vampire_merits
        self.mage_merits = mage_merits
        self.werewolf_merits = werewolf_merits
        self.changeling_merits = changeling_merits
        self.geist_merits = geist_merits
        self.demon_merits = demon_merits
        self.deviant_merits = deviant_merits
        self.hunter_merits = hunter_merits
        self.mummy_merits = mummy_merits
        self.promethean_merits = promethean_merits
        self.minor_template_merits = minor_template_merits
        self.ghoul_merits = ghoul_merits
        self.dhampir_merits = dhampir_merits
        self.atariya_merits = atariya_merits
        self.psychic_vampire_merits = psychic_vampire_merits
        self.general_supernatural_merits = general_supernatural_merits
        self.psychic_merit_names = PSYCHIC_MERIT_NAMES
        self.all_merits = (general_merits + vampire_merits + mage_merits + werewolf_merits + 
                          changeling_merits + geist_merits + demon_merits + deviant_merits +
                          hunter_merits + mummy_merits + promethean_merits + minor_template_merits)
        
        # Template-specific data
        self.vampire_data = {
            'clans': VAMPIRE_CLANS,
            'bloodlines': VAMPIRE_BLOODLINES,
            'covenants': VAMPIRE_COVENANTS,
            'disciplines': VAMPIRE_DISCIPLINES,
            'discipline_powers': ALL_DISCIPLINE_POWERS,
            'discipline_power_categories': DISCIPLINE_POWER_CATEGORIES,
            'coils': ALL_COILS,
            'coils_by_mystery': COILS_BY_MYSTERY,
            'bloodline_disciplines': ALL_BLOODLINE_DISCIPLINES,
            'bloodline_disciplines_by_bloodline': BLOODLINE_DISCIPLINES_BY_BLOODLINE,
            'devotions': ALL_DEVOTIONS,
            'devotions_by_type': DEVOTIONS_BY_TYPE,
            'scales': ALL_SCALES,
            'scales_by_mystery': SCALES_BY_MYSTERY,
            'theban': ALL_THEBAN,
            'theban_by_rank': THEBAN_BY_RANK,
            'cruac': ALL_CRUAC,
            'cruac_by_rank': CRUAC_BY_RANK,
            'bloodline_devotions_extended': ALL_BLOODLINE_DEVOTIONS_EXTENDED,
            'penumbrae_cruac': PENUMBRAE_CRUAC,
            'clans_detailed': get_all_clans(),
            'bloodlines_detailed': get_all_bloodlines(),
            'covenants_detailed': get_all_covenants()
        }
        
        self.mage_data = {
            'paths': MAGE_PATHS,
            'orders': MAGE_ORDERS,
            'arcana': MAGE_ARCANA,
            'legacies_by_path': LEGACIES_BY_PATH,
            'legacies_by_order': LEGACIES_BY_ORDER,
            'unlinked_legacies': UNLINKED_LEGACIES,
            'all_legacies': ALL_LEGACIES,
            'paths_detailed': get_all_paths(),
            'orders_detailed': get_all_orders_detailed(),
            'legacies_detailed': get_all_legacies_detailed()
        }
        
        self.demon_data = {
            'incarnations': DEMON_INCARNATIONS,
            'agendas': DEMON_AGENDAS,
            'embeds': ALL_EMBEDS,
            'exploits': DEMON_EXPLOITS,
            'embed_names': ALL_EMBED_NAMES,
            'exploit_names': ALL_EXPLOIT_NAMES,
            'embeds_by_incarnation': EMBEDS_BY_INCARNATION,
            'embeds_cacophony': EMBEDS_CACOPHONY,
            'embeds_instrumental': EMBEDS_INSTRUMENTAL,
            'embeds_mundane': EMBEDS_MUNDANE,
            'embeds_vocal': EMBEDS_VOCAL,
            'modifications': DEMON_MODIFICATIONS,
            'technologies': DEMON_TECHNOLOGIES,
            'propulsions': DEMON_PROPULSIONS,
            'processes': DEMON_PROCESSES,
            'modification_names': ALL_DEMON_MODIFICATIONS,
            'technology_names': ALL_DEMON_TECHNOLOGIES,
            'propulsion_names': ALL_DEMON_PROPULSIONS,
            'process_names': ALL_DEMON_PROCESSES
        }
        
        self.mortal_plus_data = {
            'types': ALL_MORTAL_PLUS_TYPES,
            'psychic_powers': PSYCHIC_POWERS,
            'demon_blooded_levels': DEMON_BLOODED_LEVELS,
            'game_line_heritage': GAME_LINE_HERITAGE,
            'wolf_blooded_tells': WOLF_BLOODED_TELLS,
            'proximus_families': PROXIMUS_FAMILIES,
        }
        
        # Mummy data
        self.mummy_data = {
            'guilds': MUMMY_GUILDS,
            'decrees': MUMMY_DECREES,
            'judges': MUMMY_JUDGES,
            'utterances': MUMMY_UTTERANCES_DATA,
            'affinities': MUMMY_AFFINITIES_DATA,
            'utterance_names': ALL_UTTERANCE_NAMES,
            'affinity_names': ALL_AFFINITY_NAMES
        }
        
        # Geist data
        self.geist_data = {
            'burdens': GEIST_BURDENS,
            'krewe_types': GEIST_KREWE_TYPES,
            'haunts': GEIST_HAUNTS,
            'haunts_detailed': ALL_HAUNTS,
            'keys': GEIST_KEYS,
            'keys_detailed': GEIST_KEY_DETAILS,
            'ceremonies': GEIST_CEREMONIES
        }
        
        # Deviant data
        from world.cofd.templates.deviant import (
            DEVIANT_ORIGINS, DEVIANT_CLADES, DEVIANT_VARIATIONS, DEVIANT_SCARS
        )
        from world.cofd.powers.deviant_data import (
            ALL_VARIATIONS, ALL_SCARS, DEVIANT_FORMS,
            DEVIANT_ORIGINS_DETAILED, DEVIANT_CLADES_DETAILED,
            DEVIANT_ADAPTATIONS, ADAPTATION_CATEGORIES
        )
        
        self.deviant_data = {
            'origins': DEVIANT_ORIGINS,
            'origins_detailed': DEVIANT_ORIGINS_DETAILED,
            'clades': DEVIANT_CLADES,
            'clades_detailed': DEVIANT_CLADES_DETAILED,
            'scars': DEVIANT_SCARS,
            'scars_detailed': ALL_SCARS,
            'variations': DEVIANT_VARIATIONS,
            'variations_detailed': ALL_VARIATIONS,
            'adaptations': DEVIANT_ADAPTATIONS,
            'adaptation_categories': ADAPTATION_CATEGORIES,
            'forms': DEVIANT_FORMS
        }
        
        self.changing_breeds_data = {
            'breeds': LEGACY_CHANGING_BREEDS,
            'categories': CHANGING_BREED_CATEGORIES,
            'accords': CHANGING_BREED_ACCORDS,
            'accord_specialties': ACCORD_SPECIALTIES,
            'respect_types': RESPECT_TYPES,
            'favors': CHANGING_BREED_FAVORS,
            'aspects': CHANGING_BREED_ASPECTS,
            'favor_names': ALL_FAVOR_NAMES,
            'aspect_names': ALL_ASPECT_NAMES,
            'trickster_aspects': TRICKSTER_ONLY_ASPECTS
        }
        
        # Werewolf data
        self.werewolf_data = {
            'auspices': WEREWOLF_AUSPICES,
            'tribes': WEREWOLF_TRIBES,
            'lodges': WEREWOLF_LODGES,
            'gifts': ALL_WEREWOLF_GIFTS,
            'auspices_detailed': get_all_auspices(),
            'tribes_detailed': get_all_tribes(),
            'lodges_detailed': get_all_lodges()
        }
        
        # Changeling data
        self.changeling_data = {
            'seemings': CHANGELING_SEEMINGS,
            'contracts': ALL_CHANGELING_CONTRACTS,
            'courts': CHANGELING_COURTS,
            'kiths': CHANGELING_KITHS,
            'kiths_detailed': ALL_KITHS,
            'seemings_detailed': get_all_seemings(),
            'entitlements': CHANGELING_ENTITLEMENTS,
            'entitlements_detailed': get_all_entitlements()
        }
        
        # Promethean data
        self.promethean_data = {
            'transmutations': PROMETHEAN_TRANSMUTATIONS,
            'alembics': PROMETHEAN_ALEMBICS,
            'bestowments': PROMETHEAN_BESTOWMENTS,
            'lineages': PROMETHEAN_LINEAGES,
            'athanors': ATHANORS_BY_LINEAGE,
            'elpides': ELPIDES,
            'torments': TORMENTS,
            'elpis_names': ALL_ELPIDES,
            'torment_names': ALL_TORMENTS
        }
        
        # Hunter data - need to build the endowments dict from imported modules
        hunter_endowments = {
            **ADVANCED_ARMORY,
            **ANIMAL_CONTROL_KIT,
            **BENEDICTION,
            **CASTIGATION,
            **DREAMSCAPE,
            **ELIXIR,
            **ENKOIMESIS,
            **GOETIC_GOSPEL,
            **HORROR_WITHIN,
            **INFUSION,
            **INK,
            **INSPIRATION,
            **LIVES_REMEMBERED,
            **PERISPIRITISM,
            **RELIC,
            **RITES_DU_CHEVAL,
            **RITES_OF_DENIAL,
            **SEITOKUTEN,
            **TELEINFORMATICS,
            **THAUMATECHNOLOGY,
            **XENOTECHNOLOGY
        }
        
        self.hunter_data = {
            'endowments': hunter_endowments,
            'conspiracies': HUNTER_CONSPIRACIES,
            'compacts': HUNTER_COMPACTS,
            'tactics': HUNTER_TACTICS,
            'tactics_detailed': get_all_tactics(),
            'mental_tactics': MENTAL_TACTICS,
            'physical_tactics': PHYSICAL_TACTICS,
            'social_tactics': SOCIAL_TACTICS,
            'compacts_detailed': ALL_COMPACTS,
            'conspiracies_detailed': ALL_CONSPIRACIES,
            'organizations': get_all_organizations()
        }
        
        # Skill specialties
        self.specialties = {
            # Mental Skills
            'academics': ['Anthropology', 'Art History', 'English', 'History', 'Law', 'Literature', 'Religion', 'Research', 'Translation'],
            'computer': ['Data Retrieval', 'Graphics', 'Hacking', 'Internet', 'Programming', 'Security', 'Social Media'],
            'crafts': ['Automotive', 'Cosmetics', 'Fashion', 'Forging', 'Graffiti', 'Jury-Rigging', 'Painting', 'Perfumery', 'Repair', 'Sculpting'],
            'investigation': ['Artifacts', 'Autopsy', 'Body Language', 'Crime Scenes', 'Cryptography', 'Dreams', 'Lab Work', 'Riddles'],
            'medicine': ['First Aid', 'Pathology', 'Pharmaceuticals', 'Physical Therapy', 'Surgery'],
            'occult': ['Angels', 'Alchemy', 'Mystic Places', 'Casting Lots', 'Phrenology', 'Sorcery', 'Supernatural Being (specify)', 'Superstition', 'Witchcraft'],
            'politics': ['Bureaucracy', 'Church', 'Democratic', 'Invictus', 'Local', 'Organized Crime', 'Scandals'],
            'science': ['Physics', 'Chemistry', 'Neuroscience', 'Virology', 'Alchemy', 'Genetics', 'Hematology'],
            # Physical Skills
            'athletics': ['Acrobatics', 'Archery', 'Climbing', 'Jumping', 'Parkour', 'Swimming', 'Throwing'],
            'brawl': ['Biting', 'Boxing', 'Dirty Fighting', 'Grappling', 'Martial Arts', 'Threats', 'Throws'],
            'drive': ['Defensive Driving', 'Evasion', 'Off-Road Driving', 'Motorcycles', 'Pursuit', 'Stunts'],
            'firearms': ['Handguns', 'Rifles', 'Shotguns', 'Trick Shots'],
            'larceny': ['Breaking and Entering', 'Concealment', 'Lockpicking', 'Pickpocketing', 'Safecracking', 'Security Systems', 'Sleight of Hand'],
            'stealth': ['Camouflage', 'Crowds', 'In Plain Sight', 'Rural', 'Shadowing', 'Stakeout', 'Staying Motionless'],
            'survival': ['Foraging', 'Hunting', 'Navigation', 'Shelter', 'Weather'],
            'weaponry': ['Chains', 'Clubs', 'Improvised Weapons', 'Spears', 'Swords'],
            # Social Skills
            'animal_ken': ['Animalism', 'Canines', 'Felines', 'Reptiles', 'Threatening', 'Training'],
            'empathy': ['Calming', 'Emotion', 'Lies', 'Motives', 'Personalities'],
            'expression': ['Dance', 'Drama', 'Journalism', 'Musical Instrument', 'Performance Art', 'Singing', 'Speeches'],
            'intimidation': ['Direct Threats', 'Interrogation', 'Stare Down', 'Torture', 'Veiled Threats'],
            'persuasion': ['Confidence Scam', 'Fast Talking', 'Inspiring', 'Sales Pitch', 'Seduction', 'Sermon'],
            'socialize': ['Bar Hopping', 'Church Lock-in', 'Dress Balls', 'Formal Events', 'Frat Parties', 'Political Fundraisers', 'the Club'],
            'streetwise': ['Black Market', 'Gangs', 'Navigation', 'Rumors', 'Undercover'],
            'subterfuge': ['Detecting Lies', 'Doublespeak', 'Hiding Emotion', 'Little White Lies', 'Misdirection']
        }
    
    def find_stat(self, stat_name):
        """Find a stat by name across all categories."""
        stat_name = stat_name.lower().replace(" ", "_")
        
        # Check attributes
        if stat_name in self.attributes:
            return ('attribute', self.attributes[stat_name])
        
        # Check skills
        if stat_name in self.skills:
            return ('skill', self.skills[stat_name])
        
        # Check advantages
        if stat_name in self.advantages:
            return ('advantage', self.advantages[stat_name])
        
        # Check anchors
        if stat_name in self.anchors:
            return ('anchor', self.anchors[stat_name])
        
        # Check merits
        for merit in self.all_merits:
            if merit.name.lower().replace(" ", "_") == stat_name:
                return ('merit', merit)
        
        return None
    
    def search_stats(self, search_term):
        """Search for stats containing the given term."""
        search_term = search_term.lower()
        results = []
        
        # Search attributes
        for name, attr in self.attributes.items():
            if search_term in name.lower():
                results.append(('attribute', name, attr))
        
        # Search skills
        for name, skill in self.skills.items():
            if search_term in name.lower():
                results.append(('skill', name, skill))
        
        # Search merits
        for merit in self.all_merits:
            if (search_term in merit.name.lower() or 
                search_term in merit.description.lower()):
                results.append(('merit', merit.name, merit))
        
        # Search disciplines
        for discipline in self.vampire_data['disciplines']:
            if search_term in discipline.lower():
                results.append(('discipline', discipline, None))
        
        # Search discipline powers
        for power_key, power_data in self.vampire_data['discipline_powers'].items():
            if (search_term in power_key.lower() or 
                search_term in power_data['name'].lower() or
                search_term in power_data['description'].lower()):
                results.append(('discipline_power', power_data['name'], power_data))
        
        # Search ritual powers (Scales, Theban, Cruac)
        for ritual_key, ritual_data in self.vampire_data['scales'].items():
            if (search_term in ritual_key.lower() or
                search_term in ritual_data['name'].lower() or
                search_term in ritual_data['description'].lower()):
                results.append(('ritual', ritual_data['name'], ritual_data))
        
        for miracle_key, miracle_data in self.vampire_data['theban'].items():
            if (search_term in miracle_key.lower() or
                search_term in miracle_data['name'].lower() or
                search_term in miracle_data['description'].lower()):
                results.append(('ritual', miracle_data['name'], miracle_data))
        
        for rite_key, rite_data in self.vampire_data['cruac'].items():
            if (search_term in rite_key.lower() or
                search_term in rite_data['name'].lower() or
                search_term in rite_data['description'].lower()):
                results.append(('ritual', rite_data['name'], rite_data))
        
        # Search werewolf gifts
        for gift_key, gift_data in self.werewolf_data['gifts'].items():
            if (search_term in gift_key.lower() or
                search_term in gift_data['name'].lower() or
                search_term in gift_data['description'].lower()):
                results.append(('gift', gift_data['name'], gift_data))
        
        # Search changeling contracts
        for contract_key, contract_data in self.changeling_data['contracts'].items():
            if (search_term in contract_key.lower() or
                search_term in contract_data['name'].lower() or
                search_term in contract_data['description'].lower()):
                results.append(('contract', contract_data['name'], contract_data))
        
        # Search geist keys
        for key_name, key_data in self.geist_data['keys_detailed'].items():
            if (search_term in key_name.lower() or
                search_term in key_data['name'].lower() or
                search_term in key_data['description'].lower()):
                results.append(('key', key_data['name'], key_data))
        
        # Search geist haunts
        for haunt_name, haunt_powers in self.geist_data['haunts_detailed'].items():
            for power_key, power_data in haunt_powers.items():
                if (search_term in haunt_name.lower() or
                    search_term in power_key.lower() or
                    search_term in power_data['name'].lower() or
                    search_term in power_data['description'].lower()):
                    results.append(('haunt', power_data['name'], power_data))
        
        # Search arcana
        for arcanum in self.mage_data['arcana']:
            if search_term in arcanum.lower():
                results.append(('arcanum', arcanum, None))
        
        # Search mummy affinities
        for affinity_key, affinity_data in self.mummy_data['affinities'].items():
            if (search_term in affinity_key.lower() or
                search_term in affinity_data['name'].lower() or
                search_term in affinity_data['description'].lower()):
                results.append(('affinity', affinity_data['name'], affinity_data))
        
        # Search mummy utterances
        for utterance_key, utterance_data in self.mummy_data['utterances'].items():
            if (search_term in utterance_key.lower() or
                search_term in utterance_data['name'].lower() or
                search_term in utterance_data['description'].lower()):
                results.append(('utterance', utterance_data['name'], utterance_data))
        
        # Search demon modifications
        for mod_key, mod_data in self.demon_data['modifications'].items():
            if (search_term in mod_key.lower() or
                search_term in mod_data['name'].lower() or
                search_term in mod_data['system'].lower() or
                search_term in mod_data['appearance'].lower()):
                results.append(('demon_modification', mod_data['name'], mod_data))
        
        # Search demon technologies
        for tech_key, tech_data in self.demon_data['technologies'].items():
            if (search_term in tech_key.lower() or
                search_term in tech_data['name'].lower() or
                search_term in tech_data['system'].lower() or
                search_term in tech_data['appearance'].lower()):
                results.append(('demon_technology', tech_data['name'], tech_data))
        
        # Search demon propulsions
        for prop_key, prop_data in self.demon_data['propulsions'].items():
            if (search_term in prop_key.lower() or
                search_term in prop_data['name'].lower() or
                search_term in prop_data['system'].lower() or
                search_term in prop_data['appearance'].lower()):
                results.append(('demon_propulsion', prop_data['name'], prop_data))
        
        # Search demon processes
        for proc_key, proc_data in self.demon_data['processes'].items():
            if (search_term in proc_key.lower() or
                search_term in proc_data['name'].lower() or
                search_term in proc_data['system'].lower() or
                search_term in proc_data['appearance'].lower()):
                results.append(('demon_process', proc_data['name'], proc_data))
        
        # Search demon embeds
        for embed_key, embed_data in self.demon_data['embeds'].items():
            if (search_term in embed_key.lower() or
                search_term in embed_data['name'].lower() or
                search_term in embed_data.get('description', '').lower() or
                search_term in embed_data.get('effect', '').lower()):
                results.append(('demon_embed', embed_data['name'], embed_data))
        
        # Search demon exploits
        for exploit_key, exploit_data in self.demon_data['exploits'].items():
            if (search_term in exploit_key.lower() or
                search_term in exploit_data['name'].lower() or
                search_term in exploit_data.get('description', '').lower() or
                search_term in exploit_data.get('effect', '').lower()):
                results.append(('demon_exploit', exploit_data['name'], exploit_data))
        
        return results
    
    def get_merits_by_type(self, merit_type=None, template=None):
        """Get merits filtered by type and/or template."""
        merits = []
        
        # Map template names to their merit lists
        template_map = {
            'vampire': self.vampire_merits,
            'mage': self.mage_merits,
            'werewolf': self.werewolf_merits,
            'changeling': self.changeling_merits,
            'geist': self.geist_merits,
            'demon': self.demon_merits,
            'deviant': self.deviant_merits,
            'hunter': self.hunter_merits,
            'mummy': self.mummy_merits,
            'promethean': self.promethean_merits,
            'mortal+': self.minor_template_merits,
            'mortal_plus': self.minor_template_merits,
            'general': self.general_merits,
            # Minor template types
            'ghoul': self.ghoul_merits,
            'dhampir': self.dhampir_merits,
            'atariya': self.atariya_merits,
            'psychic_vampire': self.psychic_vampire_merits,
            'psychic vampire': self.psychic_vampire_merits,
        }
        
        # Special handling for psychic merits - filter from general merits by name
        if template and template.lower() == 'psychic':
            merits = [m for m in self.general_merits if m.name in self.psychic_merit_names]
        elif template and template.lower() in template_map:
            merits = template_map[template.lower()]
        elif template is None:
            merits = self.general_merits
        else:
            merits = self.all_merits
        
        if merit_type:
            merits = [m for m in merits if m.merit_type == merit_type]
        
        return sorted(merits, key=lambda m: m.name)
    
    def parse_prerequisites(self, prereq_string):
        """Parse prerequisite string into structured data."""
        if not prereq_string:
            return []
        
        prereqs = []
        # Split on commas and clean up
        parts = [p.strip() for p in prereq_string.split(',')]
        
        for part in parts:
            if not part:
                continue
                
            # Handle negation
            negated = False
            if part.startswith('!'):
                negated = True
                part = part[1:]
            
            # Handle stat:value format
            if ':' in part:
                stat, value = part.split(':', 1)
                try:
                    value = int(value)
                    prereqs.append({
                        'type': 'stat',
                        'stat': stat.replace('_', ' ').title(),
                        'value': value,
                        'negated': negated
                    })
                except ValueError:
                    # Non-numeric value, treat as requirement
                    prereqs.append({
                        'type': 'requirement',
                        'requirement': f"{stat.replace('_', ' ').title()}: {value}",
                        'negated': negated
                    })
            # Handle bracketed OR conditions like [wits:3,dexterity:3]
            elif part.startswith('[') and part.endswith(']'):
                or_conditions = part[1:-1].split(',')
                or_prereqs = []
                for condition in or_conditions:
                    if ':' in condition:
                        stat, value = condition.split(':', 1)
                        try:
                            value = int(value)
                            or_prereqs.append(f"{stat.replace('_', ' ').title()} {value}")
                        except ValueError:
                            or_prereqs.append(condition.replace('_', ' ').title())
                    else:
                        or_prereqs.append(condition.replace('_', ' ').title())
                
                prereqs.append({
                    'type': 'or_condition',
                    'conditions': or_prereqs,
                    'negated': negated
                })
            else:
                # Simple requirement
                prereqs.append({
                    'type': 'requirement',
                    'requirement': part.replace('_', ' ').title(),
                    'negated': negated
                })
        
        return prereqs
    
    def format_prerequisites_display(self, prereq_string):
        """Format prerequisites for display."""
        if not prereq_string:
            return "None"
        
        prereqs = self.parse_prerequisites(prereq_string)
        if not prereqs:
            return "None"
        
        display_parts = []
        
        for prereq in prereqs:
            if prereq['type'] == 'stat':
                stat_display = f"{prereq['stat']} {prereq['value']}"
                if prereq['negated']:
                    stat_display = f"NOT {stat_display}"
                display_parts.append(stat_display)
            
            elif prereq['type'] == 'or_condition':
                or_display = " OR ".join(prereq['conditions'])
                if prereq['negated']:
                    or_display = f"NOT ({or_display})"
                else:
                    or_display = f"({or_display})"
                display_parts.append(or_display)
            
            elif prereq['type'] == 'requirement':
                req_display = prereq['requirement']
                if prereq['negated']:
                    req_display = f"NOT {req_display}"
                display_parts.append(req_display)
        
        return ", ".join(display_parts)


# Global instance for easy access
LOOKUP_DATA = LookupData()


def get_attribute_description(attr_name):
    """Get description for an attribute."""
    # Pull directly from the attribute dictionary
    if attr_name in attribute_dictionary:
        return attribute_dictionary[attr_name].description
    return "Core character attribute"


def get_skill_description(skill_name):
    """Get description for a skill."""
    # Pull directly from the skill dictionary
    if skill_name in skill_dictionary:
        return skill_dictionary[skill_name].description
    return "Character skill"


def get_discipline_description(discipline_name):
    """Get description for a vampire discipline."""
    descriptions = {
        # Standard clan disciplines
        "animalism": "Command and communicate with animals",
        "auspex": "Supernatural senses and perception",
        "celerity": "Supernatural speed and reflexes",
        "dominate": "Mental control and command",
        "majesty": "Supernatural presence and awe",
        "nightmare": "Inspire terror and fear",
        "obfuscate": "Concealment and stealth",
        "protean": "Shapechanging and transformation",
        "resilience": "Supernatural toughness",
        "vigor": "Supernatural strength",
        # Bloodline disciplines
        "bloodworking": "Manipulate and weaponize blood (bloodline)",
        "cachexy": "Inflict disease and decay (Morbus bloodline)",
        "crochan": "Blood healing and oaths (Bron bloodline)",
        "dead_signal": "God-Machine connection (Jharana bloodline)",
        "praestantia": "Enhanced physical capabilities (bloodline)",
        "chary": "Shadow manipulation (bloodline)",
        "vitiate": "Corruption and decay (bloodline)",
        # Covenant disciplines (rated 1-5)
        "cruac": "Circle of the Crone blood sorcery (rated 1-5)",
        "theban_sorcery": "Lancea et Sanctum divine magic (rated 1-5)",
        # Ordo Dracul (these shouldn't appear here but included for completeness)
        "coils of the dragon": "Ordo Dracul transcendence techniques",
        "coil_of_the_ascendant": "Overcome daysleep and sunlight (Ordo Dracul)",
        "coil_of_the_voivode": "Blood bond mastery (Ordo Dracul)",
        "coil_of_the_wyrm": "Frenzy mastery (Ordo Dracul)",
        "coil_of_zirnitra": "Supernatural merits (Ordo Dracul)",
        "coil_of_ziva": "Humanity transcendence (Ordo Dracul)"
    }
    return descriptions.get(discipline_name, "Vampire supernatural power")


def get_arcanum_description(arcanum_name):
    """Get description for a mage arcanum."""
    descriptions = {
        "death": "Decay, ghosts, and the underworld",
        "fate": "Luck, destiny, and probability",
        "forces": "Energy, motion, and physics",
        "life": "Biology, healing, and transformation",
        "matter": "Substances, alchemy, and transmutation",
        "mind": "Thoughts, emotions, and mental control",
        "prime": "Raw magic and the Supernal Realm",
        "space": "Distance, teleportation, and scrying",
        "spirit": "The Shadow Realm and ephemeral beings",
        "time": "Temporal manipulation and prophecy"
    }
    return descriptions.get(arcanum_name, "Sphere of magical influence")


def get_clan_description(clan_name):
    """Get description for a vampire clan."""
    descriptions = {
        "daeva": "Seductive predators driven by passion and desire",
        "gangrel": "Savage survivors who embrace their Beast",
        "mekhet": "Mysterious shadows who trade in secrets",
        "nosferatu": "Hideous monsters dwelling in the underground",
        "ventrue": "Noble lords who rule from positions of power"
    }
    return descriptions.get(clan_name, "Vampire bloodline")


def get_covenant_description(covenant_name):
    """Get description for a vampire covenant."""
    descriptions = {
        "carthian movement": "Revolutionary vampires seeking political change",
        "circle of the crone": "Pagan vampires who worship the dark goddess",
        "invictus": "Aristocratic vampires maintaining feudal traditions",
        "lancea et sanctum": "Religious vampires serving as God's predators",
        "ordo dracul": "Philosophical vampires transcending their curse",
        "unaligned": "Independent vampires avoiding covenant politics"
    }
    return descriptions.get(covenant_name, "Vampire political organization")


def get_path_info(path_name):
    """Get ruling arcana and description for a mage path."""
    path_info = {
        "acanthus": ("Time, Fate", "Enchanters who walk between worlds"),
        "mastigos": ("Mind, Space", "Warlocks who command demons and souls"),
        "moros": ("Death, Matter", "Necromancers who speak with the dead"),
        "obrimos": ("Forces, Prime", "Theurges who wield divine fire"),
        "thyrsus": ("Life, Spirit", "Shamans who commune with nature")
    }
    return path_info.get(path_name, ("Unknown", "Awakened magician"))


def get_order_description(order_name):
    """Get description for a mage order."""
    descriptions = {
        "adamantine arrow": "Warrior-philosophers who protect the Awakened",
        "guardians of the veil": "Secret agents maintaining the Masquerade",
        "mysterium": "Scholar-mages preserving magical knowledge",
        "silver ladder": "Political leaders guiding human destiny",
        "free council": "Democratic rebels embracing modern methods",
        "seers of the throne": "Servants of the Exarchs opposing Awakening",
        "unaligned": "Independent mages avoiding order politics"
    }
    return descriptions.get(order_name, "Mage political organization")


def get_template_description(template_name):
    """Get description for a character template."""
    descriptions = {
        "mortal": "Ordinary humans with no supernatural abilities",
        "mortal+": "Humans with minor supernatural abilities",
        "vampire": "Undead predators who feed on blood",
        "mage": "Awakened humans who manipulate reality",
        "werewolf": "Shapeshifters who guard the boundaries",
        "changeling": "Fae-touched humans who escaped Arcadia",
        "demon": "Fallen angels who escaped the God-Machine",
        "geist": "Humans bound to death-spirits",
        "promethean": "Artificial beings seeking humanity",
        "hunter": "Humans who hunt supernatural creatures",
        "mummy": "Immortal servants of ancient judges",
        "beast": "Incarnate nightmares who feed on fear",
        "deviant": "Humans transformed by conspiracy"
    }
    return descriptions.get(template_name, "Supernatural character type")
