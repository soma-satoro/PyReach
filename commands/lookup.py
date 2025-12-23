from evennia.commands.default.muxcommand import MuxCommand
from evennia.server.models import ServerConfig
from world.cofd.lookup_data import (
    LOOKUP_DATA, 
    get_attribute_description, get_skill_description,
    get_discipline_description, get_arcanum_description,
    get_clan_description, get_covenant_description,
    get_path_info, get_order_description, get_template_description
)
from world.utils.formatting import header, footer, divider, format_stat
import re


class CmdLookup(MuxCommand):
    """
    Look up character creation information and game statistics.
    
    Usage:
        +lookup                              - Show available lookup categories
        +lookup <category>                   - List all items in category
        +lookup <category> <name>            - Show details for specific item
        +lookup/search <term>                - Search for stats containing term
        
    Common Categories:
        attributes, skills, merits, disciplines, powers, clans, bloodlines, covenants,
        arcana, spells, paths, orders, legacies, auspices, tribes, lodges, gifts,
        kiths, entitlements, keys, haunts, variations, scars, adaptations, templates,
        lineages, guilds, tactics, compacts, conspiracies, etc.
        
    Category Filters:
        +lookup skills [mental|physical|social]
        +lookup merits [type|template]
        +lookup powers [discipline]
        +lookup spells [arcana]
        +lookup gifts [category]
        +lookup endowments [type]
        +lookup tactics [mental|physical|social]
        
        Examples:
        +lookup disciplines                  - List all vampire disciplines
        +lookup disciplines animalism        - Show Animalism discipline details
        +lookup clans daeva                  - Show Daeva clan details
        +lookup bloodlines morbus            - Show Morbus bloodline details
        +lookup paths acanthus               - Show Acanthus path details
        +lookup orders mysterium             - Show Mysterium order details
        +lookup legacies chronologue         - Show Chronologue legacy details
        +lookup auspices rahu                - Show Rahu auspice details
        +lookup tribes blood_talons          - Show Blood Talons tribe details
        +lookup lodges                       - List all werewolf lodges
        +lookup lodges eaters_of_the_dead    - Show Eaters of the Dead lodge
        +lookup kiths                        - List all changeling kiths
        +lookup kiths bright_one             - Show Bright One kith details
        +lookup entitlements                 - List all changeling entitlements
        +lookup entitlements master_of_keys  - Show Master of Keys entitlement
        +lookup tactics                      - List all hunter tactics
        +lookup tactics mental               - List mental tactics
        +lookup tactics sweep                - Show Sweep tactic details
        +lookup compacts                     - List all hunter compacts
        +lookup compacts ashwood_abbey       - Show Ashwood Abbey compact details
        +lookup conspiracies                 - List all hunter conspiracies
        +lookup conspiracies aegis_kai_doru  - Show Aegis Kai Doru conspiracy details
        +lookup keys beasts                  - Show Key of Beasts details
        +lookup lineages frankenstein        - Show Frankenstein lineage details
        +lookup guilds mesen-nebu            - Show Mesen-Nebu guild details
        +lookup incarnations destroyer       - Show Destroyer incarnation details
        +lookup origins cephalist            - Show Cephalist origin details
        +lookup powers animalism             - List all Animalism discipline powers
        +lookup spells forces                - List all Forces spells
        +lookup gifts cunning                - List all Cunning renown gifts
        +lookup merits mental                - List all mental merits
        +lookup alembics human_flesh         - Show Human Flesh alembic details
        +lookup/search "combat"              - Find all stats related to combat
        
    This command provides comprehensive information about character creation
    options including attributes, skills, merits, supernatural powers, and
    template-specific information like clans, covenants, paths, and orders.
    """
    
    key = "+lookup"
    aliases = ["+dict", "+dictionary", "+info", "+reference"]
    locks = "cmd:all()"
    help_category = "Chargen & Character Info"
    
    def get_theme_colors(self):
        """Get theme colors from server config or defaults."""
        theme_colors = ServerConfig.objects.conf("LOOKUP_THEME_COLORS")
        if theme_colors:
            colors = theme_colors.split(",")
            if len(colors) >= 3:
                return colors[0], colors[1], colors[2]
        # Default colors (cyan for informational)
        return 'c', 'c', 'c'
    
    def format_header(self, content):
        """
        Format a header for lookup displays.
        
        Format: ===> Content <===
        
        Args:
            content (str): The header text
            
        Returns:
            str: Formatted header string
        """
        header_color, text_color, divider_color = self.get_theme_colors()
        
        header_content = f" {content} "
        total_width = 80
        equals_per_side = (total_width - len(header_content) - 4) // 2  # -4 for the arrows
        
        header = f"|{header_color}" + "=" * equals_per_side + ">" + f"|{text_color}" + header_content + f"|{header_color}" + "<" + "=" * equals_per_side + "|n"
        
        return header
    
    def format_footer(self, content):
        """
        Format a footer for lookup displays.
        
        Format: ======> Content <======
        
        Args:
            content (str): The footer text
            
        Returns:
            str: Formatted footer string
        """
        header_color, text_color, divider_color = self.get_theme_colors()
        
        footer_content = f" {content} "
        total_width = 80
        equals_per_side = (total_width - len(footer_content) - 4) // 2  # -4 for the arrows
        
        footer = f"|{header_color}" + "=" * equals_per_side + ">" + f"|{text_color}" + footer_content + f"|{header_color}" + "<" + "=" * equals_per_side + "|n"
        
        return footer
    
    def func(self):
        if not self.args and not self.switches:
            self.show_categories()
            return
            
        if "search" in self.switches:
            self.search_stats()
            return
            
        args = self.args.strip().lower()
        
        # Handle specific lookups
        if args.startswith("attributes"):
            parts = args.split()
            if len(parts) > 1:
                # It's a stat name lookup with category filter
                stat_name = " ".join(parts[1:])
                self.show_stat_details(stat_name, category_filter="attributes")
            else:
                self.show_attributes()
        elif args.startswith("skills"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a filter or a stat name
                skill_filters = ["mental", "physical", "social"]
                if parts[1] in skill_filters:
                    self.show_skills(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="skills")
            else:
                self.show_skills(None)
        elif args.startswith("merits"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a filter or a stat name
                merit_filters = ["mental", "physical", "social", "supernatural", "fighting", "style",
                               "vampire", "mage", "werewolf", "changeling", "geist", "demon", 
                               "deviant", "hunter", "mummy", "promethean", "mortal+", "mortal_plus",
                               "psychic", "ghoul", "dhampir", "atariya", "psychic_vampire", "general",
                               "plain", "infected", "lost boy", "dreamer"]
                if parts[1] in merit_filters:
                    self.show_merits(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="merits")
            else:
                self.show_merits(None)
        elif args.startswith("disciplines") or args.startswith("discipline"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific discipline lookup
                discipline_name = " ".join(parts[1:])
                self.show_discipline_details(discipline_name)
            else:
                self.show_disciplines()
        elif args.startswith("discipline_powers") or args.startswith("powers"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a discipline filter or a stat name
                discipline_names = ["animalism", "auspex", "celerity", "dominate", "majesty", "nightmare", 
                                  "obfuscate", "protean", "resilience", "vigor", "cachexy", "crochan", "dead_signal"]
                if parts[1] in discipline_names:
                    self.show_discipline_powers(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="powers")
            else:
                self.show_discipline_powers(None)
        elif args.startswith("coils"):
            parts = args.split()
            mystery = parts[1] if len(parts) > 1 else None
            self.show_coils(mystery)
        elif args.startswith("bloodline"):
            parts = args.split()
            bloodline = parts[1] if len(parts) > 1 else None
            self.show_bloodline_disciplines(bloodline)
        elif args.startswith("devotions") or args.startswith("devotion"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a devotion type filter or a stat name
                devotion_types = ["general", "carthian", "invictus", "nereid"]
                if parts[1] in devotion_types:
                    self.show_devotions(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="devotions")
            else:
                self.show_devotions(None)
        elif args.startswith("scales"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a mystery filter or a stat name
                mystery_names = ["ascendant", "quintessence", "voivode", "wyrm", "zirnitra", "ziva", "other"]
                if parts[1] in mystery_names:
                    self.show_scales(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="scales")
            else:
                self.show_scales(None)
        elif args.startswith("theban"):
            parts = args.split()
            if len(parts) > 1:
                rank_arg = parts[1]
                if rank_arg.isdigit():
                    self.show_theban(int(rank_arg))
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="theban")
            else:
                self.show_theban(None)
        elif args.startswith("cruac"):
            parts = args.split()
            if len(parts) > 1:
                rank_arg = parts[1]
                if rank_arg.isdigit():
                    self.show_cruac(int(rank_arg))
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="cruac")
            else:
                self.show_cruac(None)
        elif args == "arcana":
            self.show_arcana()
        elif args.startswith("spells"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's an arcana filter or a stat name
                arcana_names = ["death", "fate", "forces", "life", "matter", "mind", "prime", "space", "spirit", "time"]
                if parts[1] in arcana_names:
                    self.show_spells(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="spells")
            else:
                self.show_spells(None)
        elif args.startswith("clans") or args.startswith("clan"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific clan lookup
                clan_name = " ".join(parts[1:])
                self.show_clan_details(clan_name)
            else:
                self.show_clans()
        elif args.startswith("bloodlines") or args.startswith("bloodline"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific bloodline lookup
                bloodline_name = " ".join(parts[1:])
                self.show_bloodline_details(bloodline_name)
            else:
                self.show_bloodlines()
        elif args.startswith("covenants") or args.startswith("covenant"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific covenant lookup
                covenant_name = " ".join(parts[1:])
                self.show_covenant_details(covenant_name)
            else:
                self.show_covenants()
        elif args.startswith("paths") or args.startswith("path"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific path lookup
                path_name = " ".join(parts[1:])
                self.show_path_details(path_name)
            else:
                self.show_paths()
        elif args.startswith("orders") or args.startswith("order"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific order lookup
                order_name = " ".join(parts[1:])
                self.show_order_details(order_name)
            else:
                self.show_orders()
        elif args.startswith("legacies") or args.startswith("legacy"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific legacy lookup
                legacy_name = " ".join(parts[1:])
                self.show_legacy_details(legacy_name)
            else:
                self.show_legacies()
        elif args.startswith("templates") or args.startswith("template"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific template lookup
                template_name = " ".join(parts[1:])
                self.show_template_details(template_name)
            else:
                self.show_templates()
        elif args.startswith("auspices") or args.startswith("auspice"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific auspice lookup
                auspice_name = " ".join(parts[1:])
                self.show_auspice_details(auspice_name)
            else:
                self.show_auspices()
        elif args.startswith("tribes") or args.startswith("tribe"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific tribe lookup
                tribe_name = " ".join(parts[1:])
                self.show_tribe_details(tribe_name)
            else:
                self.show_tribes()
        elif args.startswith("gifts"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a gift category filter or a stat name
                gift_categories = ["agony", "blood", "death", "disease", "dominance", "elementals",
                                 "evasion", "fervor", "hunger", "insight", "inspiration", "knowledge",
                                 "nature", "rage", "shaping", "stealth", "strength", "technology",
                                 "warding", "weather", "change", "hunting", "pack",
                                 "crescent_moon", "full_moon", "gibbous_moon", "half_moon", "new_moon",
                                 "cunning", "glory", "honor", "purity", "wisdom"]
                if parts[1] in gift_categories:
                    self.show_werewolf_gifts(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="gifts")
            else:
                self.show_werewolf_gifts(None)
        elif args.startswith("lodges") or args.startswith("lodge"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific lodge lookup
                lodge_name = " ".join(parts[1:])
                self.show_lodge_details(lodge_name)
            else:
                self.show_lodges()
        elif args.startswith("contracts"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a contract category filter or a stat name
                contract_categories = ["crown", "jewel", "mirror", "shield", "steed", "sword", 
                                     "chalice", "coin", "stars", "thorn", "goblin"]
                if parts[1] in contract_categories:
                    self.show_changeling_contracts(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="contracts")
            else:
                self.show_changeling_contracts(None)
        elif args.startswith("seemings") or args.startswith("seeming"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific seeming lookup
                seeming_name = " ".join(parts[1:])
                self.show_seeming_details(seeming_name)
            else:
                self.show_seemings()
        elif args.startswith("courts") or args.startswith("court"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific court lookup
                court_name = " ".join(parts[1:])
                self.show_court_details(court_name)
            else:
                self.show_courts()
        elif args.startswith("kiths") or args.startswith("kith"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific kith lookup
                kith_name = " ".join(parts[1:])
                self.show_kith_details(kith_name)
            else:
                self.show_kiths()
        elif args.startswith("entitlements") or args.startswith("entitlement"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific entitlement lookup
                entitlement_name = " ".join(parts[1:])
                self.show_entitlement_details(entitlement_name)
            else:
                self.show_entitlements()
        elif args.startswith("keys"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific key lookup
                key_name = " ".join(parts[1:])
                self.show_geist_key(key_name)
            else:
                self.show_geist_keys()
        elif args.startswith("haunts"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific haunt lookup
                haunt_name = " ".join(parts[1:])
                self.show_geist_haunt(haunt_name)
            else:
                self.show_geist_haunts()
        elif args.startswith("incarnations") or args.startswith("incarnation"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific incarnation lookup
                incarnation_name = " ".join(parts[1:])
                self.show_incarnation_details(incarnation_name)
            else:
                self.show_incarnations()
        elif args.startswith("agendas") or args.startswith("agenda"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific agenda lookup
                agenda_name = " ".join(parts[1:])
                self.show_agenda_details(agenda_name)
            else:
                self.show_agendas()
        elif args.startswith("embeds") or args.startswith("embed"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific embed lookup
                embed_name = " ".join(parts[1:])
                self.show_embed_details(embed_name)
            else:
                self.show_embeds()
        elif args.startswith("exploits") or args.startswith("exploit"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific exploit lookup
                exploit_name = " ".join(parts[1:])
                self.show_exploit_details(exploit_name)
            else:
                self.show_exploits()
        elif args.startswith("demon_modifications") or args.startswith("modifications") or args.startswith("modification"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific modification lookup
                modification_name = " ".join(parts[1:])
                self.show_demon_modification_details(modification_name)
            else:
                self.show_demon_modifications()
        elif args.startswith("demon_technologies") or args.startswith("technologies") or args.startswith("technology"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific technology lookup
                technology_name = " ".join(parts[1:])
                self.show_demon_technology_details(technology_name)
            else:
                self.show_demon_technologies()
        elif args.startswith("demon_propulsions") or args.startswith("propulsions") or args.startswith("propulsion"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific propulsion lookup
                propulsion_name = " ".join(parts[1:])
                self.show_demon_propulsion_details(propulsion_name)
            else:
                self.show_demon_propulsions()
        elif args.startswith("demon_processes") or args.startswith("processes") or args.startswith("process"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific process lookup
                process_name = " ".join(parts[1:])
                self.show_demon_process_details(process_name)
            else:
                self.show_demon_processes()
        elif args.startswith("transmutations") or args.startswith("transmutation"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific transmutation lookup
                transmutation_name = " ".join(parts[1:])
                self.show_transmutation_details(transmutation_name)
            else:
                self.show_transmutations()
        elif args.startswith("alembics"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific alembic lookup
                alembic_name = " ".join(parts[1:])
                self.show_alembic_details(alembic_name)
            else:
                self.show_alembics()
        elif args.startswith("bestowments") or args.startswith("bestowment"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific bestowment lookup
                bestowment_name = " ".join(parts[1:])
                self.show_bestowment_details(bestowment_name)
            else:
                self.show_bestowments()
        elif args.startswith("endowments"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's an endowment type filter or a stat name
                endowment_types = ["advanced_armory", "animal_control_kit", "benediction", "castigation", 
                                 "dreamscape", "elixir", "enkoimesis", "goetic_gospel", "horror_within", 
                                 "infusion", "ink", "inspiration", "lives_remembered", "perispiritism", 
                                 "relic", "rites_du_cheval", "rites_of_denial", "seitokuten", 
                                 "teleinformatics", "thaumatechnology", "xenotechnology"]
                if parts[1] in endowment_types:
                    self.show_endowments(parts[1])
                else:
                    # It's a stat name lookup with category filter (keep spaces for endowments)
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="endowments")
            else:
                self.show_endowments(None)
        elif args.startswith("tactics") or args.startswith("tactic"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a tactics category filter or a stat name
                tactic_categories = ["mental", "physical", "social"]
                if parts[1] in tactic_categories:
                    self.show_tactics(parts[1])
                else:
                    # It's a stat name lookup
                    tactic_name = " ".join(parts[1:])
                    self.show_tactic_details(tactic_name)
            else:
                self.show_tactics(None)
        elif args.startswith("compacts") or args.startswith("compact"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific compact lookup
                compact_name = " ".join(parts[1:])
                self.show_compact_details(compact_name)
            else:
                self.show_compacts()
        elif args.startswith("conspiracies") or args.startswith("conspiracy"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific conspiracy lookup
                conspiracy_name = " ".join(parts[1:])
                self.show_conspiracy_details(conspiracy_name)
            else:
                self.show_conspiracies()
        elif args.startswith("lineages") or args.startswith("lineage"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific lineage lookup
                lineage_name = " ".join(parts[1:])
                self.show_lineage_details(lineage_name)
            else:
                self.show_lineages()
        elif args.startswith("athanors") or args.startswith("athanor"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific athanor lookup
                athanor_name = " ".join(parts[1:])
                self.show_athanor_details(athanor_name)
            else:
                self.show_athanors()
        elif args.startswith("guilds") or args.startswith("guild"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific guild lookup
                guild_name = " ".join(parts[1:])
                self.show_guild_details(guild_name)
            else:
                self.show_guilds()
        elif args.startswith("decrees") or args.startswith("decree"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific decree lookup
                decree_name = " ".join(parts[1:])
                self.show_decree_details(decree_name)
            else:
                self.show_decrees()
        elif args.startswith("judges") or args.startswith("judge"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific judge lookup
                judge_name = " ".join(parts[1:])
                self.show_judge_details(judge_name)
            else:
                self.show_judges()
        elif args.startswith("utterances") or args.startswith("utterance"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific utterance lookup
                utterance_name = " ".join(parts[1:])
                self.show_utterance_details(utterance_name)
            else:
                self.show_utterances()
        elif args.startswith("affinities") or args.startswith("affinity"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific affinity lookup
                affinity_name = " ".join(parts[1:])
                self.show_affinity_details(affinity_name)
            else:
                self.show_affinities()
        elif args.startswith("burdens") or args.startswith("burden"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific burden lookup
                burden_name = " ".join(parts[1:])
                self.show_burden_details(burden_name)
            else:
                self.show_burdens()
        elif args.startswith("krewe"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific krewe type lookup
                krewe_name = " ".join(parts[1:])
                self.show_krewe_details(krewe_name)
            else:
                self.show_krewe_types()
        elif args.startswith("ceremonies") or args.startswith("ceremony"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific ceremony lookup
                ceremony_name = " ".join(parts[1:])
                self.show_ceremony_details(ceremony_name)
            else:
                self.show_ceremonies()
        elif args.startswith("origins") or args.startswith("origin"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific origin lookup
                origin_name = " ".join(parts[1:])
                self.show_origin_details(origin_name)
            else:
                self.show_origins()
        elif args.startswith("clades") or args.startswith("clade"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific clade lookup
                clade_name = " ".join(parts[1:])
                self.show_clade_details(clade_name)
            else:
                self.show_clades()
        elif args.startswith("variations"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific variation lookup
                variation_name = " ".join(parts[1:])
                self.show_deviant_variation(variation_name)
            else:
                self.show_variations()
        elif args.startswith("adaptations"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific adaptation lookup
                adaptation_name = " ".join(parts[1:])
                self.show_deviant_adaptation(adaptation_name)
            else:
                self.show_adaptations()
        elif args.startswith("scars"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific scar lookup
                scar_name = " ".join(parts[1:])
                self.show_deviant_scar(scar_name)
            else:
                self.show_scars()
        elif args == "mortal+" or args == "mortal_plus":
            self.show_mortal_plus_types()
        elif args == "psychic" or args == "psychic_powers":
            self.show_psychic_powers()
        elif args == "tells" or args == "wolf_blooded":
            self.show_wolf_blooded_tells()
        elif args == "specialties" or args.startswith("specialties"):
            parts = args.split()
            skill = parts[1] if len(parts) > 1 else None
            self.show_specialties(skill)
        else:
            # Try to find specific stat
            self.show_stat_details(args)
    
    def show_categories(self):
        """Show available lookup categories in a compact 4-column format."""
        msg = self.format_header("Chronicles of Darkness - Character Reference")
        msg += "\n\n"
        
        # Helper function to format items in 2 columns
        def format_two_columns(items):
            lines = []
            for i in range(0, len(items), 2):
                left = items[i] if i < len(items) else ""
                right = items[i + 1] if i + 1 < len(items) else ""
                lines.append((left, right))
            return lines
        
        # Define sections with items
        sections = [
            # Row 1: Core Stats | Vampire (4 columns total)
            {
                "left_title": "Core Stats:",
                "left_items": ["attributes", "skills [type]", "merits [filter]", "specialties", "templates"],
                "right_title": "Vampire:",
                "right_items": ["disciplines", "powers [disc]", "devotions [type]", "coils [mystery]",
                               "scales [mystery]", "theban [rank]", "cruac [rank]",
                               "clans", "bloodlines", "covenants"]
            },
            # Row 2: Mage | Werewolf
            {
                "left_title": "Mage:",
                "left_items": ["arcana", "spells [arcana]", "paths", "orders", "legacies"],
                "right_title": "Werewolf:",
                "right_items": ["auspices", "tribes", "lodges", "gifts [category]"]
            },
            # Row 3: Changeling | Geist
            {
                "left_title": "Changeling:",
                "left_items": ["seemings", "kiths", "courts", "entitlements", "contracts [type]"],
                "right_title": "Geist:",
                "right_items": ["burdens", "krewe", "haunts", "keys", "ceremonies"]
            },
            # Row 4: Demon | Promethean
            {
                "left_title": "Demon:",
                "left_items": ["incarnations", "agendas", "embeds", "exploits", "modifications", "technologies", "propulsions", "processes"],
                "right_title": "Promethean:",
                "right_items": ["transmutations", "alembics", "bestowments", "lineages", "athanors"]
            },
            # Row 5: Mummy | Deviant
            {
                "left_title": "Mummy:",
                "left_items": ["guilds", "decrees", "judges", "utterances", "affinities"],
                "right_title": "Deviant:",
                "right_items": ["origins", "clades", "variations", "scars", "adaptations"]
            },
            # Row 6: Hunter | Mortal+
            {
                "left_title": "Hunter:",
                "left_items": ["endowments [type]", "tactics [category]", "compacts", "conspiracies"],
                "right_title": "Mortal+:",
                "right_items": ["mortal+", "psychic", "tells"]
            }
        ]
        
        # Display each section pair side by side
        for i, section in enumerate(sections):
            # Format left and right items into 2-column layouts
            left_lines = format_two_columns(section["left_items"])
            right_lines = format_two_columns(section["right_items"])
            
            # Display section titles side by side (total width ~75 chars)
            msg += f"|c{section['left_title']:<41}|n|c{section['right_title']}|n\n"
            
            # Display items (4 columns: 2 for left section, 2 for right section)
            max_rows = max(len(left_lines), len(right_lines))
            for j in range(max_rows):
                # Left section (2 columns, 20 chars each)
                if j < len(left_lines):
                    left_col1 = f"|y{left_lines[j][0]:<20}|n" if left_lines[j][0] else " " * 20
                    left_col2 = f"|y{left_lines[j][1]:<20}|n" if left_lines[j][1] else " " * 20
                else:
                    left_col1 = " " * 20
                    left_col2 = " " * 20
                
                # Right section (2 columns, 20 chars each, but don't pad the last one)
                if j < len(right_lines):
                    right_col1 = f"|y{right_lines[j][0]:<20}|n" if right_lines[j][0] else " " * 20
                    # Last column - don't pad with trailing spaces
                    right_col2 = f"|y{right_lines[j][1]}|n" if right_lines[j][1] else ""
                else:
                    right_col1 = ""
                    right_col2 = ""
                
                # Build line - only add right columns if they have content
                line = f"  {left_col1}{left_col2}"
                if right_col1 or right_col2:
                    line += f"{right_col1}{right_col2}"
                msg += line.rstrip() + "\n"
            
            # Only add blank line if not the last section
            if i < len(sections) - 1:
                msg += "\n"
        
        msg += "\n|cSpecial Commands:|n\n"
        msg += "  |y+lookup <stat>|n                - Get details on any stat\n"
        msg += "  |y+lookup <category> <stat>|n    - Get details with category filter\n"
        msg += "  |y+lookup/search <term>|n        - Search for stats by keyword\n\n"
        
        msg += "|cExamples:|n\n"
        msg += "  |y+lookup attributes|n - List all attributes\n"
        msg += "  |y+lookup strength|n - View strength details\n"
        msg += "  |y+lookup orders mysterium|n - View Mysterium order details\n"
        msg += "  |y+lookup legacies chronologue|n - View Chronologue legacy details\n"
        msg += "  |y+lookup tribes blood_talons|n - View Blood Talons tribe details\n"
        msg += "  |y+lookup lodges eaters_of_the_dead|n - View Eaters of the Dead lodge\n"
        msg += "  |y+lookup kiths|n - List all changeling kiths\n"
        msg += "  |y+lookup kiths bright_one|n - View Bright One kith details\n"
        msg += "  |y+lookup tactics|n - List all hunter tactics\n"
        msg += "  |y+lookup tactics mental|n - List mental tactics\n"
        msg += "  |y+lookup tactics sweep|n - View Sweep tactic details\n"
        msg += "  |y+lookup compacts network_zero|n - View Network Zero compact details\n"
        msg += "  |y+lookup conspiracies aegis_kai_doru|n - View Aegis Kai Doru conspiracy\n"
        msg += "  |y+lookup embeds|n - List all demon embeds\n"
        msg += "  |y+lookup embeds authorized|n - View Authorized embed details\n"
        msg += "  |y+lookup processes|n - List all demon processes\n"
        msg += "  |y+lookup processes aegis_protocol|n - View Aegis Protocol process\n"
        msg += "  |y+lookup merits vampire|n - List vampire merits\n"
        msg += "  |y+lookup merits telekinesis|n - View telekinesis merit (not spell)\n"
        msg += "  |y+lookup spells telekinesis|n - View telekinesis spell (not merit)\n"
        msg += "  |y+lookup powers animalism|n - List Animalism discipline powers\n"
        msg += "  |y+lookup/search invisible|n - Find all invisibility-related powers\n\n"
        
        msg += self.format_footer("Use +lookup <category> to explore")
        
        self.caller.msg(msg)
    
    def show_attributes(self):
        """Show all attributes organized by type."""
        msg = self.format_header("Character Attributes")
        msg += "\n\n"
        
        # Organize by type
        power_attrs = []
        finesse_attrs = []
        resistance_attrs = []
        
        for name, attr in LOOKUP_DATA.attributes.items():
            if attr.att_type == "power":
                power_attrs.append((name.title(), attr))
            elif attr.att_type == "finesse":
                finesse_attrs.append((name.title(), attr))
            elif attr.att_type == "resistance":
                resistance_attrs.append((name.title(), attr))
        
        # Display Power attributes
        if power_attrs:
            msg += "|rPower Attributes:|n\n"
            for name, attr in sorted(power_attrs):
                desc = get_attribute_description(name.lower())
                msg += f"  |r{name:<15}|n ({attr.min_value}-{attr.max_value}) - {desc}\n"
            msg += "\n"
        
        # Display Finesse attributes
        if finesse_attrs:
            msg += "|gFinesse Attributes:|n\n"
            for name, attr in sorted(finesse_attrs):
                desc = get_attribute_description(name.lower())
                msg += f"  |g{name:<15}|n ({attr.min_value}-{attr.max_value}) - {desc}\n"
            msg += "\n"
        
        # Display Resistance attributes
        if resistance_attrs:
            msg += "|bResistance Attributes:|n\n"
            for name, attr in sorted(resistance_attrs):
                desc = get_attribute_description(name.lower())
                msg += f"  |b{name:<15}|n ({attr.min_value}-{attr.max_value}) - {desc}\n"
            msg += "\n"
        
        msg += "|cNote:|n All attributes start at 1 and can be raised to 5 during character creation.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_skills(self, category=None):
        """Show skills, optionally filtered by category."""
        if category and category not in ["mental", "physical", "social"]:
            self.caller.msg("Valid skill categories: mental, physical, social")
            return
        
        title = "Character Skills"
        if category:
            title += f" - {category.title()}"
        
        msg = self.format_header(title)
        msg += "\n\n"
        
        # Organize skills by type
        mental_skills = []
        physical_skills = []
        social_skills = []
        
        for name, skill in LOOKUP_DATA.skills.items():
            if category and skill.skill_type != category:
                continue
            
            if skill.skill_type == "mental":
                mental_skills.append((name, skill))
            elif skill.skill_type == "physical":
                physical_skills.append((name, skill))
            else:  # social
                social_skills.append((name, skill))
        
        # Display Mental skills
        if mental_skills and (not category or category == "mental"):
            msg += "|cMental Skills:|n\n"
            for name, skill in sorted(mental_skills):
                desc = get_skill_description(name)
                skill_name = name.title().replace('_', ' ')
                unskilled = f"(-{skill.unskilled})" if skill.unskilled else ""
                msg += f"  |c{skill_name:<20}|n {unskilled:<5} {desc}\n"
            msg += "\n"
        
        # Display Physical skills
        if physical_skills and (not category or category == "physical"):
            msg += "|yPhysical Skills:|n\n"
            for name, skill in sorted(physical_skills):
                desc = get_skill_description(name)
                skill_name = name.title().replace('_', ' ')
                unskilled = f"(-{skill.unskilled})" if skill.unskilled else ""
                msg += f"  |y{skill_name:<20}|n {unskilled:<5} {desc}\n"
            msg += "\n"
        
        # Display Social skills
        if social_skills and (not category or category == "social"):
            msg += "|mSocial Skills:|n\n"
            for name, skill in sorted(social_skills):
                desc = get_skill_description(name)
                skill_name = name.title().replace('_', ' ')
                unskilled = f"(-{skill.unskilled})" if skill.unskilled else ""
                msg += f"  |m{skill_name:<20}|n {unskilled:<5} {desc}\n"
            msg += "\n"
        
        msg += "|cNote:|n Skills start at 0 and can be raised to 5. Unskilled penalty applies when using a skill at 0 dots.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_merits(self, filter_arg=None):
        """Show merits, optionally filtered by type or template."""
        # Check if filter_arg is a merit type or template
        merit_types = ["mental", "physical", "social", "supernatural", "fighting", "style"]
        templates = ["vampire", "mage", "werewolf", "changeling", "geist", "demon", 
                    "deviant", "hunter", "mummy", "promethean", "mortal+", "mortal_plus", "general",
                    # Minor template types
                    "psychic", "ghoul", "dhampir", "atariya", "psychic_vampire", "psychic vampire",
                    "plain", "infected", "lost boy", "dreamer"]
        
        merit_type = None
        template = None
        
        if filter_arg:
            filter_lower = filter_arg.lower()
            if filter_lower in merit_types:
                merit_type = filter_lower
            elif filter_lower in templates:
                template = filter_lower
            else:
                self.caller.msg(f"Unknown filter: {filter_arg}")
                self.caller.msg("|cValid types:|n mental, physical, social, supernatural, fighting, style")
                self.caller.msg("|cValid templates:|n vampire, mage, werewolf, changeling, geist, demon, deviant, hunter, mummy, promethean, mortal+")
                self.caller.msg("|cMinor templates:|n psychic, ghoul, dhampir, atariya, psychic_vampire")
                return
        
        # Get filtered merits
        filtered_merits = LOOKUP_DATA.get_merits_by_type(merit_type, template if template else 'general')
        
        # Format title with proper capitalization
        if template:
            template_display = template.replace('_', ' ').title()
        else:
            template_display = "General"
        
        title = f"{template_display} Merits"
        if merit_type:
            title += f" - {merit_type.title()}"
        title += f" ({len(filtered_merits)} total)"
        
        msg = self.format_header(title)
        msg += "\n\n"
        
        # Type symbols and colors
        type_colors = {
            "mental": "|c", "physical": "|y", "social": "|m",
            "supernatural": "|r", "fighting": "|R", "style": "|g"
        }
        type_symbols = {
            "mental": "◆",      # Diamond for mental
            "physical": "■",    # Square for physical
            "social": "●",      # Circle for social
            "supernatural": "★", # Star for supernatural
            "fighting": "⚔",    # Swords for fighting
            "style": "◈"        # Diamond in square for style
        }
        
        # Display merits
        for merit in sorted(filtered_merits, key=lambda m: (m.merit_type, m.name)):
            color = type_colors.get(merit.merit_type, "|w")
            symbol = type_symbols.get(merit.merit_type, "○")
            
            if merit.min_value == merit.max_value:
                dots = f"({merit.min_value})"
            else:
                dots = f"({merit.min_value}-{merit.max_value})"
            
            prereq = LOOKUP_DATA.format_prerequisites_display(merit.prerequisite)
            prereq_display = f" - Prereq: {prereq}" if prereq and prereq != "None" else ""
            
            msg += f"{color}{symbol} {merit.name:<35}|n {dots:<8}{prereq_display}\n"
        
        msg += "\n"
        
        # Add legend for symbols and colors
        msg += "|wMerit Type Legend:|n\n"
        msg += "  |c◆ Mental|n (Cyan)        |y■ Physical|n (Yellow)      |m● Social|n (Magenta)\n"
        msg += "  |r★ Supernatural|n (Red)  |R⚔ Fighting|n (Bright Red)  |g◈ Style|n (Green)\n\n"
        
        msg += self.format_footer("Chronicles of Darkness Reference")
        self.caller.msg(msg)
        
        self.caller.msg(f"|cUse:|n |y+lookup <merit_name>|n for detailed information on any merit.")
        self.caller.msg(f"|cFilters:|n +lookup merits <type> or +lookup merits <template>")
        self.caller.msg(f"  |yTypes:|n mental, physical, social, supernatural, fighting, style")
        self.caller.msg(f"  |yMajor Templates:|n vampire, mage, werewolf, changeling, geist, demon, hunter, etc.")
        self.caller.msg(f"  |yMinor Templates:|n psychic, ghoul, dhampir, atariya, psychic_vampire, mortal+")
    
    def show_vampire_merits(self):
        """Show vampire-specific merits (backward compatibility wrapper)."""
        self.show_merits("vampire")
    
    def show_disciplines(self):
        """Show vampire disciplines."""
        from world.cofd.templates.vampire import VAMPIRE_PRIMARY_POWERS
        
        msg = self.format_header("Vampire Disciplines")
        msg += "\n\n"
        
        # Only show PRIMARY_POWERS (the rated disciplines), not secondary powers (individual rituals)
        for discipline in sorted(VAMPIRE_PRIMARY_POWERS):
            desc = get_discipline_description(discipline)
            msg += f"|r{discipline.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Disciplines are rated 1-5 dots and represent core vampiric powers.\n"
        msg += "|cView powers:|n Use |y+lookup powers <discipline>|n to see individual powers (e.g., +lookup powers animalism)\n"
        msg += "|cRitual Magic:|n Use |y+lookup cruac|n, |y+lookup theban|n, |y+lookup scales|n for covenant rituals\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_discipline_powers(self, discipline=None):
        """Show vampire discipline powers, optionally filtered by discipline."""
        from world.cofd.powers.vampire_disciplines import get_all_discipline_powers, get_powers_by_discipline
        
        if discipline:
            # Filter by discipline
            powers = get_powers_by_discipline(discipline)
            if not powers:
                self.caller.msg(f"No powers found for discipline: {discipline}")
                self.caller.msg("|cValid disciplines:|n animalism, auspex, celerity, dominate, majesty, nightmare, obfuscate, protean, resilience, vigor")
                return
            
            title = f"|wVampire Discipline Powers - {discipline.title()}|n"
        else:
            powers = get_all_discipline_powers()
            title = "|wAll Vampire Discipline Powers|n"
        
        # Group powers by level
        powers_by_level = {1: [], 2: [], 3: [], 4: [], 5: [], "rated": []}
        for power_key, power_data in powers.items():
            level = power_data['level']
            if isinstance(level, str) and '-' in level:
                powers_by_level["rated"].append((power_key, power_data))
            else:
                powers_by_level[level].append((power_key, power_data))
        
        output = [title, ""]
        
        # Display rated disciplines first (Celerity, Resilience, Vigor)
        if powers_by_level["rated"]:
            output.append("|rRated Disciplines (• to •••••)|n")
            for power_key, power_data in sorted(powers_by_level["rated"], key=lambda x: x[1]['name']):
                power_name = power_data['name']
                cost = power_data['cost']
                
                output.append(f"  |y{power_name}|n")
                output.append(f"    Cost: {cost}")
                if power_data.get('note'):
                    output.append(f"    {power_data['note']}")
                output.append(f"    |gUse:|n +stat {power_data['discipline']}=<1-5>")
            output.append("")
        
        # Display powers organized by level
        for level in range(1, 6):
            level_powers = powers_by_level[level]
            if level_powers:
                dots = "●" * level
                if discipline:
                    output.append(f"|r{discipline.title()} {dots}|n")
                else:
                    output.append(f"|rLevel {dots}|n")
                
                for power_key, power_data in sorted(level_powers, key=lambda x: x[1]['name']):
                    power_name = power_data['name']
                    cost = power_data['cost']
                    prereq = power_data.get('prerequisite', '')
                    
                    # Include discipline if showing all powers
                    if discipline:
                        output.append(f"  |y{power_name}|n - Cost: {cost}")
                    else:
                        power_discipline = power_data['discipline'].title()
                        output.append(f"  |y{power_name}|n ({power_discipline}) - Cost: {cost}")
                    
                    if prereq:
                        output.append(f"    Prerequisite: {prereq}")
                    
                    # Add usage hint
                    output.append(f"    |gUse:|n +lookup {power_key}")
                
                output.append("")
        
        self.caller.msg("\n".join(output))
        
        if not discipline:
            self.caller.msg("|cFilter by discipline:|n +lookup powers animalism, +lookup powers dominate, etc.")
        self.caller.msg("|cFor power details:|n +lookup <power_name> (e.g., +lookup mesmerize)")
    
    def show_discipline_power_details(self, power_key, power_data):
        """Show detailed information about a specific discipline power."""
        # Check type of power
        is_coil = 'mystery' in power_data
        is_bloodline = 'bloodline' in power_data and not is_coil
        is_devotion = power_data.get('type') == 'devotion'
        
        # Title
        if is_devotion:
            devotion_type = power_data.get('covenant', power_data.get('bloodline', 'General')).title()
            msg = f"|w{power_data['name']} ({devotion_type} Devotion)|n\n"
        elif is_coil:
            msg = f"|w{power_data['name']} (Coil of the Dragon)|n\n"
            mystery_name = power_data['mystery'].title()
            msg += f"|cMystery:|n {mystery_name}\n"
        elif is_bloodline:
            bloodline_name = power_data['bloodline'].title()
            msg = f"|w{power_data['name']} ({power_data['discipline'].title()} - {bloodline_name} Bloodline)|n\n"
        else:
            msg = f"|w{power_data['name']} (Vampire Discipline Power)|n\n"
        
        # For devotions, show prerequisites and XP cost
        if is_devotion:
            msg += f"|cPrerequisites:|n {power_data['prerequisites']}\n"
            xp_cost = power_data['xp_cost']
            msg += f"|cXP Cost:|n {xp_cost} XP\n"
        else:
            # Discipline and level for non-devotions
            if 'discipline' in power_data:
                discipline_name = power_data['discipline'].title()
                power_level = power_data.get('level')
                
                if not is_coil and power_level:  # Regular disciplines and bloodlines show discipline name
                    if isinstance(power_level, str) and '-' in str(power_level):
                        msg += f"|cDiscipline:|n {discipline_name} (Rated {power_level})\n"
                    else:
                        dots = "●" * power_level
                        msg += f"|cDiscipline:|n {discipline_name} {dots}\n"
            
            if is_coil:  # Coils just show level
                power_level = power_data.get('level')
                if power_level:
                    dots = "●" * power_level
                    msg += f"|cLevel:|n {dots}\n"
        
        # Cost (Vitae/Willpower)
        msg += f"|cCost:|n {power_data['cost']}\n"
        
        # Prerequisite for non-devotions
        if not is_devotion and power_data.get('prerequisite'):
            msg += f"|cPrerequisite:|n {power_data['prerequisite']}\n"
        
        # Dice Pool
        if power_data.get('dice_pool') and power_data['dice_pool'] != '-':
            msg += f"|cDice Pool:|n {power_data['dice_pool']}\n"
        
        # Description
        msg += f"|cDescription:|n {power_data['description']}\n"
        
        # Note (for rated disciplines)
        if power_data.get('note'):
            msg += f"|cNote:|n {power_data['note']}\n"
        
        # Source
        msg += f"|cSource:|n {power_data['book']}\n"
        
        # Usage
        if is_devotion:
            msg += f"\n|gTo add to character:|n +stat devotion={power_key}\n"
        elif isinstance(power_data.get('level'), str) and '-' in str(power_data.get('level', '')):
            msg += f"\n|gTo set on character:|n +stat {power_data['discipline']}=<1-5>\n"
        elif is_coil:
            msg += f"\n|gTo add to character:|n +stat coil={power_key}\n"
        else:
            msg += f"\n|gTo add to character:|n +stat discipline_power={power_key}\n"
        
        self.caller.msg(msg)
    
    def show_coils(self, mystery=None):
        """Show Coils of the Dragon, optionally filtered by mystery."""
        from world.cofd.powers.vampire_disciplines import get_all_coils, get_coils_by_mystery
        
        if mystery:
            # Filter by mystery
            coils = get_coils_by_mystery(mystery)
            if not coils:
                self.caller.msg(f"No coils found for mystery: {mystery}")
                self.caller.msg("|cValid mysteries:|n ascendant, quintessence, voivode, wyrm, zirnitra, ziva")
                return
            
            title = f"|wCoils of the Dragon - Mystery of the {mystery.title()}|n"
        else:
            coils = get_all_coils()
            title = "|wAll Coils of the Dragon|n"
        
        # Group coils by mystery if showing all
        if not mystery:
            mysteries = {}
            for coil_key, coil_data in coils.items():
                mystery_name = coil_data.get('mystery', 'unknown')
                if mystery_name not in mysteries:
                    mysteries[mystery_name] = []
                mysteries[mystery_name].append((coil_key, coil_data))
            
            output = [title, "", "|cOrdo Dracul Transcendent Powers|n", ""]
            
            for mystery_name in sorted(mysteries.keys()):
                mystery_coils = mysteries[mystery_name]
                output.append(f"|rMystery of the {mystery_name.title()}:|n")
                output.append(f"  {len(mystery_coils)} coils available")
                output.append(f"  |gView all:|n +lookup coils {mystery_name}")
                output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFilter by mystery:|n +lookup coils ascendant, +lookup coils wyrm, etc.")
            self.caller.msg("|cFor coil details:|n +lookup <coil_name> (e.g., +lookup conquer_the_red_fear)")
        else:
            # Show specific mystery's coils
            output = [title, ""]
            
            # Group by level
            coils_by_level = {1: [], 2: [], 3: [], 4: [], 5: []}
            for coil_key, coil_data in coils.items():
                level = coil_data['level']
                coils_by_level[level].append((coil_key, coil_data))
            
            # Display coils organized by level
            for level in range(1, 6):
                level_coils = coils_by_level[level]
                if level_coils:
                    dots = "●" * level
                    output.append(f"|r{mystery.title()} {dots}|n")
                    
                    for coil_key, coil_data in sorted(level_coils, key=lambda x: x[1]['name']):
                        coil_name = coil_data['name']
                        cost = coil_data['cost']
                        
                        output.append(f"  |y{coil_name}|n - Cost: {cost}")
                        output.append(f"    |gUse:|n +lookup {coil_key}")
                    
                    output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFor coil details:|n +lookup <coil_name> (e.g., +lookup peace_with_the_flame)")
    
    def show_bloodline_disciplines(self, bloodline=None):
        """Show bloodline disciplines, optionally filtered by bloodline."""
        from world.cofd.powers.vampire_disciplines import get_bloodline_discipline, ALL_BLOODLINE_DISCIPLINES
        
        if bloodline:
            # Filter by bloodline
            powers = get_bloodline_discipline(bloodline)
            if not powers:
                self.caller.msg(f"No bloodline discipline found for: {bloodline}")
                self.caller.msg("|cValid bloodlines:|n morbus (Cachexy), bron (Crochan), jharana (Dead Signal)")
                return
            
            # Get discipline name from first power
            first_power = next(iter(powers.values()))
            discipline_name = first_power['discipline'].title()
            
            title = f"|w{discipline_name} ({bloodline.title()} Bloodline)|n"
        else:
            # Show all bloodline disciplines organized by bloodline
            output = ["|wBloodline Disciplines|n", ""]
            
            bloodlines = {
                "morbus": {"discipline": "Cachexy", "description": "The disease-bearers"},
                "bron": {"discipline": "Crochan", "description": "The blood-healers"},
                "jharana": {"discipline": "Dead Signal", "description": "The God-Machine touched"}
            }
            
            for bloodline_name, info in sorted(bloodlines.items()):
                output.append(f"|r{info['discipline']}|n ({bloodline_name.title()} bloodline)")
                output.append(f"  {info['description']}")
                output.append(f"  |gView powers:|n +lookup bloodline {bloodline_name}")
                output.append("")
            
            self.caller.msg("\n".join(output))
            return
        
        # Show specific bloodline's powers
        output = [title, ""]
        
        # Group by level
        powers_by_level = {1: [], 2: [], 3: [], 4: [], 5: []}
        for power_key, power_data in powers.items():
            level = power_data['level']
            powers_by_level[level].append((power_key, power_data))
        
        # Display powers organized by level
        for level in range(1, 6):
            level_powers = powers_by_level[level]
            if level_powers:
                dots = "●" * level
                output.append(f"|r{discipline_name} {dots}|n")
                
                for power_key, power_data in sorted(level_powers, key=lambda x: x[1]['name']):
                    power_name = power_data['name']
                    cost = power_data['cost']
                    
                    output.append(f"  |y{power_name}|n - Cost: {cost}")
                    output.append(f"    |gUse:|n +lookup {power_key}")
                
                output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg("|cFor power details:|n +lookup <power_name> (e.g., +lookup diagnose)")
    
    def show_devotions(self, devotion_type=None):
        """Show devotions, optionally filtered by type."""
        from world.cofd.powers.vampire_disciplines import get_devotions_by_type, get_all_devotions
        
        if devotion_type:
            # Filter by type
            devotions = get_devotions_by_type(devotion_type)
            if not devotions:
                self.caller.msg(f"No devotions found for type: {devotion_type}")
                self.caller.msg("|cValid types:|n general, carthian, invictus, nereid")
                return
            
            title = f"|w{devotion_type.title()} Devotions|n"
        else:
            # Show all devotions organized by type
            output = ["|wDevotions|n", "", "|cCombination Discipline Powers|n", ""]
            
            devotion_types = {
                "general": ("General", "Available to all vampires"),
                "carthian": ("Carthian Movement", "Revolutionary covenant devotions"),
                "invictus": ("Invictus", "Aristocratic covenant devotions"),
                "nereid": ("Nereid", "Bloodline-specific devotions")
            }
            
            for type_key, (type_name, type_desc) in devotion_types.items():
                type_devotions = get_devotions_by_type(type_key)
                output.append(f"|r{type_name}|n")
                output.append(f"  {type_desc}")
                output.append(f"  {len(type_devotions)} devotions available")
                output.append(f"  |gView all:|n +lookup devotions {type_key}")
                output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFilter by type:|n +lookup devotions general, +lookup devotions carthian, etc.")
            self.caller.msg("|cFor devotion details:|n +lookup <devotion_name> (e.g., +lookup quicken_sight)")
            return
        
        # Show specific type's devotions
        output = [title, ""]
        
        # Sort devotions by XP cost, then alphabetically
        sorted_devotions = sorted(devotions.items(), key=lambda x: (x[1].get('xp_cost', 0), x[1]['name']))
        
        # Group by XP cost
        devotions_by_xp = {}
        for dev_key, dev_data in sorted_devotions:
            xp = dev_data.get('xp_cost', 0)
            if xp not in devotions_by_xp:
                devotions_by_xp[xp] = []
            devotions_by_xp[xp].append((dev_key, dev_data))
        
        # Display devotions organized by XP cost
        for xp_cost in sorted(devotions_by_xp.keys()):
            xp_devotions = devotions_by_xp[xp_cost]
            output.append(f"|r{xp_cost} XP|n")
            
            for dev_key, dev_data in xp_devotions:
                dev_name = dev_data['name']
                prereqs = dev_data['prerequisites']
                cost = dev_data['cost']
                
                output.append(f"  |y{dev_name}|n")
                output.append(f"    Prerequisites: {prereqs}")
                output.append(f"    Cost: {cost}")
                output.append(f"    |gUse:|n +lookup {dev_key}")
            
            output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg(f"|cTotal:|n {len(devotions)} devotions")
        self.caller.msg("|cFor devotion details:|n +lookup <devotion_name> (e.g., +lookup bend_space)")
    
    def show_scales(self, mystery=None):
        """Show Scales of the Dragon rituals, optionally filtered by mystery."""
        from world.cofd.powers.vampire_rituals import get_all_scales, get_scales_by_mystery
        
        if mystery:
            # Filter by mystery
            scales = get_scales_by_mystery(mystery)
            if not scales:
                self.caller.msg(f"No scales found for mystery: {mystery}")
                self.caller.msg("|cValid mysteries:|n ascendant, quintessence, voivode, wyrm, zirnitra, ziva, other")
                return
            
            title = f"|wScales of the Dragon - Mystery of the {mystery.title()}|n"
            output = [title, "", "|cOrdo Dracul Alchemical Rituals|n", ""]
            
            # Sort by rank
            sorted_scales = sorted(scales.items(), key=lambda x: (x[1].get('rank', 0) if isinstance(x[1].get('rank'), int) else 99, x[1]['name']))
            
            for scale_key, scale_data in sorted_scales:
                rank = scale_data.get('rank', '-')
                if isinstance(rank, int):
                    dots = "●" * rank
                    output.append(f"|y{scale_data['name']}|n - Rank: {dots}")
                else:
                    output.append(f"|y{scale_data['name']}|n - Rank: {rank}")
                output.append(f"  |gUse:|n +lookup {scale_key}")
            
            self.caller.msg("\n".join(output))
        else:
            # Show all mysteries
            output = ["|wScales of the Dragon|n", "", "|cOrdo Dracul Alchemical Rituals|n", ""]
            
            mysteries = {
                "ascendant": "Overcome vampiric weaknesses",
                "quintessence": "Domain-based rituals",
                "voivode": "Blood bond rituals",
                "wyrm": "Frenzy and vitae rituals",
                "zirnitra": "Supernatural merit rituals",
                "ziva": "Humanity transcendence rituals",
                "other": "Advanced spirit-walking scales"
            }
            
            for mystery_name, mystery_desc in mysteries.items():
                mystery_scales = get_scales_by_mystery(mystery_name)
                if mystery_scales:
                    output.append(f"|rMystery of the {mystery_name.title()}:|n")
                    output.append(f"  {mystery_desc}")
                    output.append(f"  {len(mystery_scales)} scales available")
                    output.append(f"  |gView all:|n +lookup scales {mystery_name}")
                    output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFor scale details:|n +lookup <scale_name> (e.g., +lookup flesh_graft_treatment)")
    
    def show_theban(self, rank=None):
        """Show Theban Sorcery miracles, optionally filtered by rank."""
        from world.cofd.powers.vampire_rituals import get_all_theban, get_theban_by_rank
        
        if rank:
            # Filter by rank
            miracles = get_theban_by_rank(rank)
            if not miracles:
                self.caller.msg(f"No Theban Sorcery miracles found for rank: {rank}")
                self.caller.msg("|cValid ranks:|n 1, 2, 3, 4, 5")
                return
            
            dots = "●" * rank
            title = f"|wTheban Sorcery - Rank {dots}|n"
            output = [title, "", "|cLancea et Sanctum Divine Miracles|n", ""]
            
            for miracle_key, miracle_data in sorted(miracles.items(), key=lambda x: x[1]['name']):
                output.append(f"|y{miracle_data['name']}|n")
                output.append(f"  Target Number: {miracle_data['target_number']}")
                if miracle_data.get('opposition') and miracle_data['opposition'] != '-':
                    output.append(f"  Opposition: {miracle_data['opposition']}")
                if miracle_data.get('sacrament'):
                    output.append(f"  Sacrament: {miracle_data['sacrament']}")
                output.append(f"  |gUse:|n +lookup {miracle_key}")
                output.append("")
            
            self.caller.msg("\n".join(output))
        else:
            # Show all ranks
            output = ["|wTheban Sorcery|n", "", "|cLancea et Sanctum Divine Miracles|n", ""]
            
            for rank_num in range(1, 6):
                rank_miracles = get_theban_by_rank(rank_num)
                if rank_miracles:
                    dots = "●" * rank_num
                    output.append(f"|rRank {dots}:|n")
                    output.append(f"  {len(rank_miracles)} miracles available")
                    output.append(f"  |gView all:|n +lookup theban {rank_num}")
                    output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFor miracle details:|n +lookup <miracle_name> (e.g., +lookup apple_of_eden)")
    
    def show_cruac(self, rank=None):
        """Show Cruac rites, optionally filtered by rank."""
        from world.cofd.powers.vampire_rituals import get_all_cruac, get_cruac_by_rank
        
        if rank:
            # Filter by rank
            rites = get_cruac_by_rank(rank)
            if not rites:
                self.caller.msg(f"No Cruac rites found for rank: {rank}")
                self.caller.msg("|cValid ranks:|n 1, 2, 3, 4, 5")
                return
            
            dots = "●" * rank
            title = f"|wCruac - Rank {dots}|n"
            output = [title, "", "|cCircle of the Crone Blood Sorcery|n", ""]
            
            for rite_key, rite_data in sorted(rites.items(), key=lambda x: x[1]['name']):
                output.append(f"|y{rite_data['name']}|n")
                output.append(f"  Target Number: {rite_data['target_number']}")
                if rite_data.get('opposition') and rite_data['opposition'] != '-':
                    output.append(f"  Opposition: {rite_data['opposition']}")
                output.append(f"  |gUse:|n +lookup {rite_key}")
                output.append("")
            
            self.caller.msg("\n".join(output))
        else:
            # Show all ranks
            output = ["|wCruac|n", "", "|cCircle of the Crone Blood Sorcery|n", ""]
            
            for rank_num in range(1, 6):
                rank_rites = get_cruac_by_rank(rank_num)
                if rank_rites:
                    dots = "●" * rank_num
                    output.append(f"|rRank {dots}:|n")
                    output.append(f"  {len(rank_rites)} rites available")
                    output.append(f"  |gView all:|n +lookup cruac {rank_num}")
                    output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFor rite details:|n +lookup <rite_name> (e.g., +lookup pangs_of_proserpina)")
    
    def show_ritual_power_details(self, power_key, power_data):
        """Show detailed information about a ritual power (Scale, Theban, or Cruac)."""
        ritual_type = power_data.get('type', 'ritual')
        
        # Determine title based on type
        if ritual_type == 'scale':
            mystery_name = power_data.get('mystery', 'Unknown').title()
            msg = f"|w{power_data['name']} (Scale of the Dragon - {mystery_name})|n\n"
        elif ritual_type == 'theban':
            msg = f"|w{power_data['name']} (Theban Sorcery Miracle)|n\n"
        elif ritual_type == 'cruac':
            if 'bloodline' in power_data:
                bloodline = power_data['bloodline'].title()
                msg = f"|w{power_data['name']} (Cruac - {bloodline} Bloodline)|n\n"
            else:
                msg = f"|w{power_data['name']} (Cruac Rite)|n\n"
        else:
            msg = f"|w{power_data['name']} (Ritual Power)|n\n"
        
        # Rank
        rank = power_data.get('rank', '-')
        if isinstance(rank, int):
            dots = "●" * rank
            msg += f"|cRank:|n {dots}\n"
        else:
            msg += f"|cRank:|n {rank}\n"
        
        # Target Number (for Theban and Cruac)
        if power_data.get('target_number'):
            msg += f"|cTarget Number:|n {power_data['target_number']}\n"
        
        # Opposition
        if power_data.get('opposition') and power_data['opposition'] != '-':
            msg += f"|cOpposition:|n {power_data['opposition']}\n"
        
        # Sacrament (for Theban)
        if power_data.get('sacrament'):
            msg += f"|cSacrament:|n {power_data['sacrament']}\n"
        
        # Prerequisites (for Scales)
        if power_data.get('prerequisites'):
            msg += f"|cPrerequisites:|n {power_data['prerequisites']}\n"
        
        # Description
        msg += f"|cDescription:|n {power_data['description']}\n"
        
        # Source
        msg += f"|cSource:|n {power_data['book']}\n"
        
        # Usage
        if ritual_type == 'scale':
            msg += f"\n|gTo add to character:|n +stat scale={power_key}\n"
        elif ritual_type == 'theban':
            msg += f"\n|gTo add to character:|n +stat theban={power_key}\n"
        elif ritual_type == 'cruac':
            msg += f"\n|gTo add to character:|n +stat cruac={power_key}\n"
        
        self.caller.msg(msg)
    
    def show_arcana(self):
        """Show mage arcana."""
        msg = self.format_header("Mage Arcana")
        msg += "\n\n"
        
        for arcanum in sorted(LOOKUP_DATA.mage_data['arcana']):
            desc = get_arcanum_description(arcanum)
            msg += f"|b{arcanum.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Arcana are the spheres of magical influence available to mages.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_spells(self, arcana=None):
        """Show mage spells, optionally filtered by arcana."""
        from world.cofd.powers.mage_spells import ALL_MAGE_SPELLS, get_spells_by_arcana, get_spells_by_level
        
        if arcana:
            # Filter by arcana
            spells = get_spells_by_arcana(arcana)
            if not spells:
                self.caller.msg(f"No spells found for arcana: {arcana}")
                self.caller.msg("Valid arcana: death, time, fate, forces, life, matter, mind, prime, space, spirit")
                return
            
            title = f"|wMage Spells - {arcana.title()} Arcanum|n"
        else:
            spells = ALL_MAGE_SPELLS
            title = "|wAll Mage Spells|n"
        
        # Group spells by level
        spells_by_level = {1: [], 2: [], 3: [], 4: [], 5: []}
        for spell_key, spell_data in spells.items():
            spells_by_level[spell_data['level']].append((spell_key, spell_data))
        
        output = [title, ""]
        
        # Display spells organized by level
        for level in range(1, 6):
            level_spells = spells_by_level[level]
            if level_spells:
                dots = "●" * level
                output.append(f"|c{arcana.title() if arcana else 'Level'} {dots}|n")
                
                for spell_key, spell_data in sorted(level_spells, key=lambda x: x[1]['name']):
                    spell_name = spell_data['name']
                    practice = spell_data['practice']
                    
                    # Include arcana if showing all spells
                    if arcana:
                        output.append(f"  |y{spell_name}|n - {practice}")
                    else:
                        spell_arcana = spell_data['arcana'].title()
                        output.append(f"  |y{spell_name}|n ({spell_arcana}) - {practice}")
                    
                    # Add usage hint
                    output.append(f"    |gUse:|n +stat spell={spell_key}")
                
                output.append("")
        
        self.caller.msg("\n".join(output))
        
        if not arcana:
            self.caller.msg("|cFilter by arcana:|n +lookup spells death, +lookup spells forces, etc.")
        self.caller.msg("|cFor spell details:|n +lookup <spell_name> (e.g., +lookup telekinesis)")
    
    def show_spell_details(self, spell_key, spell_data):
        """Show detailed information about a specific spell."""
        msg = f"|w{spell_data['name']} (Mage Spell)|n\n"
        
        # Arcana and level
        arcana_name = spell_data['arcana'].title()
        spell_level = spell_data['level']
        dots = "●" * spell_level
        msg += f"|cArcana:|n {arcana_name} {dots}\n"
        
        # Secondary arcana if present
        if 'secondary_arcana' in spell_data and spell_data['secondary_arcana']:
            msg += f"|cSecondary Arcana:|n {spell_data['secondary_arcana']}\n"
        
        # Practice
        msg += f"|cPractice:|n {spell_data['practice']}\n"
        
        # Primary Factor
        msg += f"|cPrimary Factor:|n {spell_data['primary_factor']}\n"
        
        # Withstand
        if 'withstand' in spell_data and spell_data['withstand']:
            msg += f"|cWithstand:|n {spell_data['withstand']}\n"
        
        # Rote Skills
        if 'rote_skills' in spell_data and spell_data['rote_skills']:
            msg += f"|cRote Skills:|n {', '.join(spell_data['rote_skills'])}\n"
        
        # Description
        msg += f"|cDescription:|n {spell_data['description']}\n"
        
        # Source
        msg += f"|cSource:|n {spell_data['source']}\n"
        
        # Usage
        msg += f"\n|gTo add to character:|n +stat spell={spell_key}\n"
        
        self.caller.msg(msg)
    
    def show_endowment_details(self, endowment_key, endowment_data):
        """Show detailed information about a specific endowment."""
        msg = f"|w{endowment_data['name']} (Hunter Endowment)|n\n"
        
        # Type and Conspiracy
        endow_type = endowment_data.get('endowment_type', 'unknown').replace('_', ' ').title()
        msg += f"|cType:|n {endow_type}\n"
        
        conspiracy = endowment_data.get('conspiracy', 'Unknown')
        msg += f"|cConspiracy:|n {conspiracy}\n"
        
        # Cost
        if endowment_data.get('cost'):
            msg += f"|cCost:|n {endowment_data['cost']}\n"
        else:
            msg += f"|cCost:|n None\n"
        
        # Dice Pool
        if endowment_data.get('dice_pool'):
            msg += f"|cDice Pool:|n {endowment_data['dice_pool']}\n"
        
        # Action Type
        if endowment_data.get('action'):
            msg += f"|cAction:|n {endowment_data['action']}\n"
        
        # Duration
        if endowment_data.get('duration'):
            msg += f"|cDuration:|n {endowment_data['duration']}\n"
        
        # Loadout
        if endowment_data.get('loadout'):
            msg += f"|cLoadout:|n {endowment_data['loadout']}\n"
        
        # Target Successes
        if endowment_data.get('target_successes'):
            msg += f"|cTarget Successes:|n {endowment_data['target_successes']}\n"
        
        # Prerequisite
        if endowment_data.get('prerequisite'):
            msg += f"|cPrerequisite:|n {endowment_data['prerequisite']}\n"
        
        # Description
        msg += f"|cDescription:|n {endowment_data['description']}\n"
        
        # Tags
        if endowment_data.get('tags'):
            msg += f"|cTags:|n {', '.join(endowment_data['tags'])}\n"
        
        # Source
        msg += f"|cSource:|n {endowment_data['book']}\n"
        
        # Usage - endowments use spaces in their keys
        msg += f"\n|gTo add to character:|n +stat endowment={endowment_key}\n"
        
        self.caller.msg(msg)
    
    def show_clans(self):
        """Show vampire clans."""
        msg = self.format_header("Vampire Clans")
        msg += "\n\n"
        
        for clan in sorted(LOOKUP_DATA.vampire_data['clans']):
            desc = get_clan_description(clan)
            msg += f"|r{clan.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Clans determine a vampire's supernatural heritage and favored disciplines.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_covenants(self):
        """Show vampire covenants."""
        msg = self.format_header("Vampire Covenants")
        msg += "\n\n"
        
        for covenant in sorted(LOOKUP_DATA.vampire_data['covenants']):
            desc = get_covenant_description(covenant)
            msg += f"|r{covenant.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Covenants are political and religious organizations that vampires join.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_paths(self):
        """Show mage paths."""
        msg = self.format_header("Mage Paths")
        msg += "\n\n"
        
        for path in sorted(LOOKUP_DATA.mage_data['paths']):
            arcana, desc = get_path_info(path)
            msg += f"|b{path.title():<20}|n |c({arcana})|n\n"
            msg += f"  {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Paths determine a mage's approach to magic and ruling arcana.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_orders(self):
        """Show mage orders."""
        msg = self.format_header("Mage Orders")
        msg += "\n\n"
        
        orders_detailed = LOOKUP_DATA.mage_data['orders_detailed']
        
        # Group orders
        contemporary = []
        ministry = []
        historical = []
        
        for order_key, order_data in orders_detailed.items():
            if order_key in ["hegemony", "horologian", "panopticon", "paternoster", "praetorian", "geryon"]:
                ministry.append((order_key, order_data))
            elif order_data.get('era') or order_data.get('region'):
                historical.append((order_key, order_data))
            else:
                contemporary.append((order_key, order_data))
        
        # Display Contemporary Orders
        if contemporary:
            msg += "|cContemporary Orders:|n\n"
            for order_key, order_data in sorted(contemporary, key=lambda x: x[1]['name']):
                name = order_data['name']
                creed = order_data.get('creed', '')
                rote_skills = ', '.join(order_data['rote_skills']) if isinstance(order_data['rote_skills'], list) else order_data['rote_skills']
                msg += f"|b{name:<30}|n (|c{rote_skills}|n)\n"
                msg += f"  {creed}\n"
                msg += f"  |gUse:|n +lookup orders {order_key}\n\n"
        
        # Display Ministry
        if ministry:
            msg += "|rMinistry (Seers of the Throne):|n\n"
            for order_key, order_data in sorted(ministry, key=lambda x: x[1]['name']):
                name = order_data['name']
                crown = order_data.get('crown', '')
                msg += f"|b{name:<30}|n ({crown})\n"
                msg += f"  |gUse:|n +lookup orders {order_key}\n\n"
        
        # Display Historical
        if historical:
            msg += "|yHistorical Orders:|n\n"
            for order_key, order_data in sorted(historical, key=lambda x: x[1]['name']):
                name = order_data['name']
                region_or_era = order_data.get('region', order_data.get('era', ''))
                msg += f"|b{name:<30}|n ({region_or_era})\n"
                msg += f"  |gUse:|n +lookup orders {order_key}\n\n"
        
        msg += f"|cTotal:|n {len(orders_detailed)} orders available\n"
        msg += "|cFor order details:|n +lookup orders <order_name> (e.g., +lookup orders mysterium)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_templates(self):
        """Show character templates."""
        msg = self.format_header("Character Templates")
        msg += "\n\n"
        
        templates = ["mortal", "mortal+", "vampire", "mage", "werewolf", "changeling", 
                    "demon", "geist", "promethean", "hunter", "mummy", "deviant"]
        
        for template in templates:
            desc = get_template_description(template)
            if template in ["mortal", "mortal+"]:
                color = "|w"
            else:
                color = "|y"
            msg += f"{color}{template.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Templates determine your character's supernatural nature and abilities.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_stat_details(self, stat_name, category_filter=None):
        """Show detailed information about a specific stat, optionally filtered by category."""
        # Collect all matches across categories
        matches = []
        
        # Check rituals (scales, theban, cruac) if not filtering or if filtering for these
        if not category_filter or category_filter in ["scales", "theban", "cruac", "rituals"]:
            from world.cofd.powers.vampire_rituals import get_ritual_power
            ritual_key = stat_name.lower().replace(" ", "_")
            ritual_data = get_ritual_power(ritual_key)
            if ritual_data:
                matches.append(("ritual", ritual_key, ritual_data))
        
        # Check discipline powers
        if not category_filter or category_filter in ["powers", "disciplines", "discipline_powers"]:
            from world.cofd.powers.vampire_disciplines import get_discipline_power
            power_key = stat_name.lower().replace(" ", "_")
            power_data = get_discipline_power(power_key)
            if power_data:
                matches.append(("discipline_power", power_key, power_data))
        
        # Check devotions
        if not category_filter or category_filter == "devotions":
            from world.cofd.powers.vampire_disciplines import ALL_DEVOTIONS
            devotion_key = stat_name.lower().replace(" ", "_")
            if devotion_key in ALL_DEVOTIONS:
                matches.append(("discipline_power", devotion_key, ALL_DEVOTIONS[devotion_key]))
        
        # Check werewolf gifts
        if not category_filter or category_filter == "gifts":
            from world.cofd.powers.werewolf_gifts import get_gift
            gift_key = stat_name.lower().replace(" ", "_")
            gift_data = get_gift(gift_key)
            if gift_data:
                matches.append(("gift", gift_key, gift_data))
        
        # Check changeling contracts
        if not category_filter or category_filter == "contracts":
            from world.cofd.powers.changeling_contracts import get_contract
            contract_key = stat_name.lower().replace(" ", "_")
            contract_data = get_contract(contract_key)
            if contract_data:
                matches.append(("contract", contract_key, contract_data))
        
        # Check geist keys
        if not category_filter or category_filter == "keys":
            key_name_normalized = stat_name.lower().replace(" ", " ")
            keys_data = LOOKUP_DATA.geist_data['keys_detailed']
            if key_name_normalized in keys_data:
                matches.append(("key", key_name_normalized, keys_data[key_name_normalized]))
        
        # Check geist haunts
        if not category_filter or category_filter == "haunts":
            haunt_name_normalized = stat_name.lower().replace(" ", "_")
            haunts_data = LOOKUP_DATA.geist_data['haunts_detailed']
            if haunt_name_normalized in haunts_data:
                matches.append(("haunt", haunt_name_normalized, haunts_data[haunt_name_normalized]))
        
        # Check spells
        if not category_filter or category_filter == "spells":
            from world.cofd.powers.mage_spells import get_spell
        spell_key = stat_name.lower().replace(" ", "_")
        spell_data = get_spell(spell_key)
        if spell_data:
                matches.append(("spell", spell_key, spell_data))
        
        # Check endowments
        if not category_filter or category_filter == "endowments":
            from world.cofd.powers.hunter_endowments import get_endowment
            endowment_key = stat_name.lower()  # Keep spaces for endowments
            endowment_data = get_endowment(endowment_key)
            if endowment_data:
                matches.append(("endowment", endowment_key, endowment_data))
        
        # Check general stats (attributes, skills, merits, etc.)
        if not category_filter or category_filter in ["attributes", "skills", "merits", "advantages", "anchors"]:
            result = LOOKUP_DATA.find_stat(stat_name)
            if result:
                stat_type, stat_data = result
                # Only include if category matches or no filter
                if not category_filter or category_filter == stat_type or category_filter == stat_type + "s":
                    matches.append((stat_type, stat_name, stat_data))
        
        # Handle results
        if len(matches) == 0:
            self.caller.msg(f"No stat found matching '{stat_name}'. Use |y+lookup|n to see available categories.")
            return
        
        elif len(matches) == 1:
            # Single match - show it
            stat_type, key, data = matches[0]
            if stat_type == "ritual":
                self.show_ritual_power_details(key, data)
            elif stat_type == "discipline_power":
                self.show_discipline_power_details(key, data)
            elif stat_type == "gift":
                self.show_gift_details(key, data)
            elif stat_type == "contract":
                self.show_contract_details(key, data)
            elif stat_type == "key":
                self.show_geist_key(key)
            elif stat_type == "haunt":
                self.show_geist_haunt(key)
            elif stat_type == "spell":
                self.show_spell_details(key, data)
            elif stat_type == "endowment":
                self.show_endowment_details(key, data)
            else:
                self._show_basic_stat_details(stat_type, data)
            return
        
        else:
            # Multiple matches - show them all with category indicators
            self.caller.msg(f"|wMultiple matches found for '{stat_name}':|n\n")
            for i, (stat_type, key, data) in enumerate(matches, 1):
                type_display = stat_type.replace("_", " ").title()
                if 'name' in data:
                    name = data['name']
                elif hasattr(data, 'name'):
                    name = data.name
                else:
                    name = stat_name.title()
                
                self.caller.msg(f"{i}. |y{name}|n ({type_display})")
            
            self.caller.msg(f"\n|cTo view a specific type:|n")
            self.caller.msg(f"  |y+lookup merits {stat_name}|n - View as merit")
            self.caller.msg(f"  |y+lookup spells {stat_name}|n - View as spell")
            self.caller.msg(f"  |y+lookup powers {stat_name}|n - View as discipline power")
            self.caller.msg(f"  |y+lookup gifts {stat_name}|n - View as werewolf gift")
            self.caller.msg(f"  |y+lookup contracts {stat_name}|n - View as changeling contract")
            self.caller.msg(f"  |y+lookup keys {stat_name}|n - View as geist key")
            self.caller.msg(f"  |y+lookup haunts {stat_name}|n - View as geist haunt")
            self.caller.msg(f"  |y+lookup endowments {stat_name}|n - View as endowment")
            return
    
    def _show_basic_stat_details(self, stat_type, stat_data):
        """Helper method to show basic stat details (attributes, skills, merits, etc.)."""
        if stat_type == 'attribute':
            msg = f"|w{stat_data.name.title()} (Attribute)|n\n"
            msg += f"|cType:|n {stat_data.att_type.title()}\n"
            msg += f"|cRange:|n {stat_data.min_value}-{stat_data.max_value}\n"
            msg += f"|cDescription:|n {get_attribute_description(stat_data.name)}\n"
            
        elif stat_type == 'skill':
            msg = f"|w{stat_data.name.title().replace('_', ' ')} (Skill)|n\n"
            msg += f"|cType:|n {stat_data.skill_type.title()}\n"
            msg += f"|cRange:|n {stat_data.min_value}-{stat_data.max_value}\n"
            if stat_data.unskilled:
                msg += f"|cUnskilled Penalty:|n {stat_data.unskilled}\n"
            msg += f"|cDescription:|n {get_skill_description(stat_data.name)}\n"
            
        elif stat_type == 'merit':
            msg = f"|w{stat_data.name} (Merit)|n\n"
            msg += f"|cType:|n {stat_data.merit_type.title()}\n"
            if stat_data.min_value == stat_data.max_value:
                msg += f"|cCost:|n {stat_data.min_value} dots\n"
            else:
                msg += f"|cCost:|n {stat_data.min_value}-{stat_data.max_value} dots\n"
            msg += f"|cPrerequisites:|n {LOOKUP_DATA.format_prerequisites_display(stat_data.prerequisite)}\n"
            msg += f"|cDescription:|n {stat_data.description}\n"
            
        elif stat_type == 'advantage':
            msg = f"|w{stat_data.name.title()} (Advantage)|n\n"
            msg += f"|cRange:|n {stat_data.min_value}-{stat_data.max_value}\n"
            msg += f"|cBase Calculation:|n {stat_data.adv_base}\n"
            msg += f"|cDescription:|n Derived stat calculated from other attributes\n"
            
        elif stat_type == 'anchor':
            msg = f"|w{stat_data.name.title()} (Anchor)|n\n"
            msg += f"|cDescription:|n Core personality trait that defines the character\n"
        else:
            msg = f"Unknown stat type: {stat_type}\n"
        
        self.caller.msg(msg)
    
    def show_transmutations(self):
        """Show promethean transmutations."""
        msg = self.format_header("Promethean Transmutations")
        msg += "\n\n"
        
        transmutation_descriptions = {
            "alchemicus": "Mastery over matter and transformation",
            "benefice": "Powers of the Throng - cooperative abilities",
            "contamination": "Powers of emotional and social corruption",
            "corporeum": "Physical enhancement and athletic prowess",
            "deception": "Powers of concealment and disguise",
            "disquietism": "Mastery over Disquiet and Flux",
            "electrification": "Control over electricity and lightning",
            "flux": "Dark powers of the Wasteland (dangerous)",
            "luciferus": "Powers of radiance and inspiration",
            "metamorphosis": "Shapeshifting and physical transformation",
            "mesmerism": "Powers of emotional manipulation",
            "saturninus": "Powers of Azothic memory and Pyros",
            "sensorium": "Enhanced senses and perception",
            "spiritus": "Powers against supernatural threats",
            "vitality": "Powers of endurance and strength",
            "vulcanus": "Powers of the Divine Fire"
        }
        
        for transmutation in sorted(LOOKUP_DATA.promethean_data['transmutations']):
            desc = transmutation_descriptions.get(transmutation, "Promethean supernatural power")
            msg += f"|g{transmutation.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Use |y+lookup alembics|n to see individual Alembics within each Transmutation.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_alembics(self):
        """Show promethean alembics organized by transmutation."""
        msg = f"|wPromethean Alembics (by Transmutation)|n\n\n"
        
        alembics_dict = LOOKUP_DATA.promethean_data['alembics']
        
        for transmutation in sorted(alembics_dict.keys()):
            alembics = sorted(alembics_dict[transmutation])
            msg += f"|g{transmutation.title()}:|n\n"
            msg += "  " + ", ".join([a.replace('_', ' ').title() for a in alembics]) + "\n\n"
        
        msg += f"|cTotal:|n {sum(len(a) for a in alembics_dict.values())} individual Alembics\n"
        msg += f"\n|cNote:|n Alembics are individual powers, not rated by dots. Set with:\n"
        msg += "|y+stat alembic=<alembic_name>|n (e.g., +stat alembic=human_flesh)\n"
        msg += f"|cDetailed lookup:|n |y+lookup alembics <name>|n"
        
        self.caller.msg(msg)
    
    def show_alembic_details(self, alembic_name):
        """Show detailed information about a specific Promethean alembic."""
        from world.cofd.powers.promethean_powers import get_alembic_details, get_transmutation_for_alembic
        
        # Normalize alembic name
        alembic_key = alembic_name.lower().replace(" ", "_")
        
        # Get detailed data
        alembic_data = get_alembic_details(alembic_key)
        
        if not alembic_data:
            # Check if alembic exists at all
            transmutation = get_transmutation_for_alembic(alembic_key)
            if transmutation:
                self.caller.msg(f"Alembic '{alembic_name}' found, but detailed data not yet available.")
                self.caller.msg(f"Transmutation: {transmutation.title()}")
                self.caller.msg(f"Use |y+lookup alembics|n to browse all alembics.")
            else:
                self.caller.msg(f"Alembic '{alembic_name}' not found.")
                self.caller.msg(f"Use |y+lookup alembics|n to see all available alembics.")
            return
        
        # Build detailed output
        msg = f"|wAlembic: {alembic_data['name']}|n\n"
        msg += f"|g{'=' * 78}|n\n\n"
        
        msg += f"|cTransmutation:|n {alembic_data['transmutation'].title()}\n"
        msg += f"|cDistillation:|n {alembic_data['distillation'].title()}\n"
        msg += f"|cRank:|n {alembic_data['rank']}\n"
        msg += f"|cCharge:|n {alembic_data['charge']}\n"
        msg += f"|cDice Pool:|n {alembic_data['dice_pool']}\n"
        msg += f"|cAction:|n {alembic_data['action']}\n"
        msg += f"|cBook:|n {alembic_data['book']}\n\n"
        
        msg += f"|wDescription:|n\n{alembic_data['description']}\n"
        
        msg += f"\n|cSet with:|n |y+stat alembic={alembic_key}|n"
        self.caller.msg(msg)
    
    def show_bestowments(self):
        """Show promethean bestowments."""
        msg = f"|wPromethean Bestowments|n\n\n"
        msg += "Bestowments are unique gifts tied to a Promethean's Lineage:\n\n"
        
        bestowments = sorted([b.lower().replace(" ", "_") for b in LOOKUP_DATA.promethean_data['bestowments']])
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
        for i in range(0, len(bestowments), 3):
            row = bestowments[i:i+3]
            msg += "  " + "".join([f"|y{b.replace('_', ' ').title():<{col_width}}|n" for b in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(bestowments)} Bestowments\n"
        msg += f"\n|cNote:|n Set with: |y+stat bestowment=<name>|n (e.g., +stat bestowment=spare_parts)"
        
        self.caller.msg(msg)
    
    def show_lineages(self):
        """Show promethean lineages."""
        msg = self.format_header("Promethean Lineages")
        msg += "\n\n"
        
        lineage_descriptions = {
            "frankenstein": "Created from corpses, the Wretched, driven by loneliness",
            "galatea": "Sculpted from unblemished forms, the Muses, seekers of beauty",
            "osiris": "Assembled from disparate parts, the Redeemed, guardians of the dead",
            "tammuz": "Formed from clay or earth, the Golem, seeking purpose",
            "ulgan": "Crafted from the remains of shamans, the Pilgrims, spiritual travelers",
            "extempore": "Spontaneously created Prometheans, rare and unpredictable",
            "unfleshed": "Prometheans without physical form, ethereal and strange",
            "zeka": "Created from metal and machine parts, the Manufactured"
        }
        
        for lineage in sorted(LOOKUP_DATA.promethean_data['lineages']):
            desc = lineage_descriptions.get(lineage, "Promethean lineage")
            msg += f"|g{lineage.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Set with: |y+stat lineage=<name>|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_athanors(self):
        """Show promethean athanors organized by lineage."""
        msg = f"|wPromethean Athanors (by Lineage)|n\n\n"
        msg += "Athanors are the spiritual engines that drive the Pilgrimage:\n\n"
        
        athanors_dict = LOOKUP_DATA.promethean_data['athanors']
        
        for lineage in sorted(athanors_dict.keys()):
            athanors = sorted(athanors_dict[lineage])
            msg += f"|g{lineage.title()}:|n\n"
            msg += "  " + ", ".join([a.replace('_', ' ').title() for a in athanors]) + "\n\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat athanor=<name>|n (requires matching Lineage)\n"
        msg += "Example: |y+stat lineage=Frankenstein|n then |y+stat athanor=Basilisk|n"
        
        self.caller.msg(msg)

    def show_endowments(self, endowment_type=None):
        """Show hunter endowments, optionally filtered by type."""
        from world.cofd.powers.hunter_endowments import get_all_endowments, get_endowments_by_type
        
        if endowment_type:
            # Filter by type
            endowments = get_endowments_by_type(endowment_type)
            if not endowments:
                self.caller.msg(f"No endowments found for type: {endowment_type}")
                self.caller.msg("|cValid types:|n advanced_armory, animal_control_kit, benediction, castigation, dreamscape, elixir, enkoimesis, goetic_gospel, horror_within, infusion, ink, inspiration, lives_remembered, perispiritism, relic, rites_du_cheval, rites_of_denial, seitokuten, teleinformatics, thaumatechnology, xenotechnology")
                return
            
            title = f"|wHunter Endowments - {endowment_type.replace('_', ' ').title()}|n"
        else:
            endowments = get_all_endowments()
            title = "|wAll Hunter Endowments|n"
        
        # Group endowments by type if showing all
        if endowment_type:
            output = [title, ""]
            for endow_key, endow_data in sorted(endowments.items(), key=lambda x: x[1]['name']):
                endow_name = endow_data['name']
                conspiracy = endow_data.get('conspiracy', 'Unknown')
                
                output.append(f"  |y{endow_name}|n")
                output.append(f"    Conspiracy: {conspiracy}")
                output.append(f"    |gUse:|n +stat endowment={endow_key}")
                output.append("")
        else:
            # Group by endowment type
            endowments_by_type = {}
            for endow_key, endow_data in endowments.items():
                e_type = endow_data.get('endowment_type', 'other')
                if e_type not in endowments_by_type:
                    endowments_by_type[e_type] = []
                endowments_by_type[e_type].append((endow_key, endow_data['name']))
            
            output = [title, ""]
            for e_type in sorted(endowments_by_type.keys()):
                output.append(f"|c{e_type.replace('_', ' ').title()}:|n")
                endow_list = sorted(endowments_by_type[e_type], key=lambda x: x[1])
                count = len(endow_list)
                output.append(f"  {count} endowments available")
                output.append(f"  |gView all:|n +lookup endowments {e_type}")
                output.append("")
        
        self.caller.msg("\n".join(output))
        
        if not endowment_type:
            self.caller.msg("|cFilter by type:|n +lookup endowments benediction, +lookup endowments castigation, etc.")
        self.caller.msg("|cFor endowment details:|n +lookup <endowment_name> (e.g., +lookup hellfire)")
    
    def show_tactics(self, category=None):
        """Show hunter tactics, optionally filtered by category."""
        if category:
            # Show specific category
            if category == "mental":
                tactics = LOOKUP_DATA.hunter_data['mental_tactics']
                title = "Hunter Tactics - Mental"
            elif category == "physical":
                tactics = LOOKUP_DATA.hunter_data['physical_tactics']
                title = "Hunter Tactics - Physical"
            elif category == "social":
                tactics = LOOKUP_DATA.hunter_data['social_tactics']
                title = "Hunter Tactics - Social"
            else:
                self.caller.msg(f"Invalid tactics category: {category}")
                self.caller.msg("|cValid categories:|n mental, physical, social")
                return
            
            msg = self.format_header(title)
            msg += "\n\n"
            
            for tactic_key in sorted(tactics.keys()):
                tactic_data = tactics[tactic_key]
                name = tactic_data['name']
                desc = tactic_data['description']
                
                msg += f"|y{name:<25}|n {desc}\n"
                msg += f"  |gUse:|n +lookup tactics {tactic_key}\n\n"
            
            msg += f"|cTotal:|n {len(tactics)} {category} tactics\n"
            msg += "|cFor tactic details:|n +lookup tactics <tactic_name> (e.g., +lookup tactics identification)\n\n"
            msg += self.format_footer("Chronicles of Darkness Reference")
            
            self.caller.msg(msg)
        else:
            # Show all categories
            msg = self.format_header("Hunter Tactics")
            msg += "\n\n"
            msg += "|cTactics are coordinated group actions that hunters use in the Vigil:|n\n\n"
            
            msg += "|cMental Tactics:|n (Investigation and knowledge)\n"
            mental = LOOKUP_DATA.hunter_data['mental_tactics']
            msg += f"  {len(mental)} tactics available\n"
            msg += "  |gView all:|n +lookup tactics mental\n\n"
            
            msg += "|yPhysical Tactics:|n (Combat and action)\n"
            physical = LOOKUP_DATA.hunter_data['physical_tactics']
            msg += f"  {len(physical)} tactics available\n"
            msg += "  |gView all:|n +lookup tactics physical\n\n"
            
            msg += "|mSocial Tactics:|n (Influence and interaction)\n"
            social = LOOKUP_DATA.hunter_data['social_tactics']
            msg += f"  {len(social)} tactics available\n"
            msg += "  |gView all:|n +lookup tactics social\n\n"
            
            msg += "|cFilter by category:|n +lookup tactics mental, +lookup tactics physical, +lookup tactics social\n"
            msg += "|cFor tactic details:|n +lookup tactics <tactic_name> (e.g., +lookup tactics sweep)\n\n"
            msg += self.format_footer("Chronicles of Darkness Reference")
            
            self.caller.msg(msg)
    
    def show_tactic_details(self, tactic_name):
        """Show detailed information about a specific hunter tactic."""
        from world.cofd.powers.hunter_tactics import get_tactic
        
        # Normalize tactic name
        tactic_key = tactic_name.lower().replace(" ", "_")
        
        # Get tactic data
        tactic_data = get_tactic(tactic_key)
        
        if not tactic_data:
            # Try with spaces
            tactic_data = get_tactic(tactic_name.lower())
        
        if not tactic_data:
            self.caller.msg(f"Tactic '{tactic_name}' not found.")
            self.caller.msg("|cUse:|n +lookup tactics - to see all available tactics")
            return
        
        msg = self.format_header(f"{tactic_data['name']} - Hunter Tactic")
        msg += "\n\n"
        
        msg += f"|cCategory:|n {tactic_data['category'].title()}\n"
        
        # Requirements
        requirements = tactic_data.get('requirements', {})
        if requirements:
            msg += f"|cRequirements:|n\n"
            if 'primary' in requirements:
                msg += f"  Primary: {requirements['primary']}\n"
            if 'secondary' in requirements:
                msg += f"  Secondary: {requirements['secondary']}\n"
            if 'any' in requirements:
                msg += f"  Any: {requirements['any']}\n"
            if 'special' in requirements:
                msg += f"  Special: {requirements['special']}\n"
        else:
            msg += f"|cRequirements:|n None\n"
        
        msg += f"\n|cPrimary Pool:|n {tactic_data['primary_pool']}\n"
        
        # Secondary pools
        secondary_pools = tactic_data.get('secondary_pools', [])
        if secondary_pools:
            msg += f"\n|cSecondary Actor Pools:|n\n"
            for pool_data in secondary_pools:
                actors = f"({pool_data['min_actors']}-{pool_data['max_actors']} actors)"
                note = f" [{pool_data['note']}]" if 'note' in pool_data else ""
                msg += f"  • {pool_data['pool']} {actors}{note}\n"
        
        # Special notes
        if tactic_data.get('special'):
            msg += f"\n|rSpecial:|n {tactic_data['special']}\n"
        
        msg += f"\n|wDescription:|n\n{tactic_data['description']}\n"
        
        # Tags
        if tactic_data.get('tags'):
            msg += f"\n|cTags:|n {', '.join(tactic_data['tags'])}\n"
        
        msg += f"\n|cSource:|n {tactic_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat tactic={tactic_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_compacts(self):
        """Show hunter compacts."""
        msg = self.format_header("Hunter Compacts")
        msg += "\n\n"
        msg += "|cCompacts are small, grassroots hunter organizations:|n\n\n"
        
        compacts = LOOKUP_DATA.hunter_data['compacts_detailed']
        
        for compact_key in sorted(compacts.keys()):
            compact_data = compacts[compact_key]
            name = compact_data['name']
            desc = compact_data['description']
            
            msg += f"|y{name:<30}|n\n"
            msg += f"  {desc}\n"
            msg += f"  |gUse:|n +lookup compacts {compact_key}\n\n"
        
        msg += f"|cTotal:|n {len(compacts)} compacts available\n"
        msg += "|cFor compact details:|n +lookup compacts <compact_name> (e.g., +lookup compacts ashwood_abbey)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_compact_details(self, compact_name):
        """Show detailed information about a specific hunter compact."""
        from world.cofd.powers.hunter_organizations import get_organization
        
        # Normalize compact name
        compact_key = compact_name.lower().replace(" ", "_")
        
        # Get compact data
        compact_data = get_organization(compact_key)
        
        if not compact_data or compact_data.get('type') != 'compact':
            self.caller.msg(f"Compact '{compact_name}' not found.")
            self.caller.msg("|cUse:|n +lookup compacts - to see all available compacts")
            return
        
        msg = self.format_header(f"{compact_data['name']} - Hunter Compact")
        msg += "\n\n"
        
        msg += f"|cDescription:|n\n{compact_data['description']}\n\n"
        
        msg += "|wStatus Benefits:|n\n"
        for level in sorted(compact_data['status_benefits'].keys()):
            dots = "•" * level
            benefit = compact_data['status_benefits'][level]
            msg += f"  |y{dots}|n - {benefit}\n"
        
        msg += f"\n|cSource:|n {compact_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat organization={compact_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_conspiracies(self):
        """Show hunter conspiracies."""
        msg = self.format_header("Hunter Conspiracies")
        msg += "\n\n"
        msg += "|cConspiracies are well-funded hunter organizations with supernatural endowments:|n\n\n"
        
        conspiracies = LOOKUP_DATA.hunter_data['conspiracies_detailed']
        
        for conspiracy_key in sorted(conspiracies.keys()):
            conspiracy_data = conspiracies[conspiracy_key]
            name = conspiracy_data['name']
            endowments = conspiracy_data['endowments']
            desc = conspiracy_data['description']
            
            msg += f"|y{name:<30}|n (|c{endowments}|n)\n"
            msg += f"  {desc}\n"
            msg += f"  |gUse:|n +lookup conspiracies {conspiracy_key}\n\n"
        
        msg += f"|cTotal:|n {len(conspiracies)} conspiracies available\n"
        msg += "|cFor conspiracy details:|n +lookup conspiracies <conspiracy_name> (e.g., +lookup conspiracies aegis_kai_doru)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_conspiracy_details(self, conspiracy_name):
        """Show detailed information about a specific hunter conspiracy."""
        from world.cofd.powers.hunter_organizations import get_organization
        
        # Normalize conspiracy name
        conspiracy_key = conspiracy_name.lower().replace(" ", "_").replace(":", "")
        
        # Get conspiracy data
        conspiracy_data = get_organization(conspiracy_key)
        
        if not conspiracy_data or conspiracy_data.get('type') != 'conspiracy':
            self.caller.msg(f"Conspiracy '{conspiracy_name}' not found.")
            self.caller.msg("|cUse:|n +lookup conspiracies - to see all available conspiracies")
            return
        
        msg = self.format_header(f"{conspiracy_data['name']} - Hunter Conspiracy")
        msg += "\n\n"
        
        msg += f"|cEndowments:|n {conspiracy_data['endowments']}\n"
        msg += f"|cDescription:|n\n{conspiracy_data['description']}\n\n"
        
        msg += "|wStatus Benefits:|n\n"
        for level in sorted(conspiracy_data['status_benefits'].keys()):
            dots = "•" * level
            benefit = conspiracy_data['status_benefits'][level]
            msg += f"  |y{dots}|n - {benefit}\n"
        
        msg += f"\n|cSource:|n {conspiracy_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat organization={conspiracy_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_auspices(self):
        """Show werewolf auspices."""
        msg = self.format_header("Werewolf Auspices")
        msg += "\n\n"
        
        auspice_descriptions = {
            "cahalith": "The Gibbous Moon, visionaries and lorekeepers",
            "elodoth": "The Half Moon, judges and mediators",
            "irraka": "The New Moon, scouts and tricksters",
            "ithaeur": "The Crescent Moon, spirit-talkers and shamans",
            "rahu": "The Full Moon, warriors and protectors"
        }
        
        for auspice in sorted(LOOKUP_DATA.werewolf_data['auspices']):
            desc = auspice_descriptions.get(auspice, "Werewolf moon-sign")
            msg += f"|y{auspice.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Auspices determine a werewolf's role and moon-gifts.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_tribes(self):
        """Show werewolf tribes."""
        msg = self.format_header("Werewolf Tribes")
        msg += "\n\n"
        
        tribe_descriptions = {
            "blood talons": "Warriors who glory in battle and honor",
            "bone shadows": "Death-speakers who police the spirit world",
            "hunters in darkness": "Territorial guardians of sacred places",
            "iron masters": "Adaptable survivors who embrace civilization",
            "storm lords": "Noble leaders who command respect",
            "ghost wolves": "Tribal outcasts who follow no pack"
        }
        
        for tribe in sorted(LOOKUP_DATA.werewolf_data['tribes']):
            desc = tribe_descriptions.get(tribe, "Werewolf tribe")
            msg += f"|y{tribe.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Tribes determine a werewolf's culture and tribal gifts.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_lodges(self):
        """Show werewolf lodges."""
        msg = self.format_header("Werewolf Lodges")
        msg += "\n\n"
        msg += "|cLodges are specialized groups within werewolf society:|n\n\n"
        
        lodges = LOOKUP_DATA.werewolf_data['lodges_detailed']
        
        for lodge_key in sorted(lodges.keys()):
            lodge_data = lodges[lodge_key]
            name = lodge_data['name']
            desc = lodge_data['description']
            
            msg += f"|y{name:<30}|n\n"
            msg += f"  {desc}\n"
            msg += f"  |gUse:|n +lookup lodges {lodge_key}\n\n"
        
        msg += f"|cTotal:|n {len(lodges)} lodges available\n"
        msg += "|cFor lodge details:|n +lookup lodges <lodge_name> (e.g., +lookup lodges eaters_of_the_dead)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_lodge_details(self, lodge_name):
        """Show detailed information about a specific werewolf lodge."""
        from world.cofd.powers.werewolf_tribes import get_lodge
        
        # Normalize lodge name
        lodge_key = lodge_name.lower().replace(" ", "_")
        
        # Get lodge data
        lodge_data = get_lodge(lodge_key)
        
        if not lodge_data:
            self.caller.msg(f"Lodge '{lodge_name}' not found.")
            self.caller.msg("|cUse:|n +lookup lodges - to see all available lodges")
            return
        
        msg = self.format_header(f"{lodge_data['name']} - Werewolf Lodge")
        msg += "\n\n"
        
        msg += f"|cDescription:|n\n{lodge_data['description']}\n\n"
        
        # Show blessing, ban, sacred hunt, and access if available
        if lodge_data.get('blessing'):
            msg += f"|wLodge Blessing:|n\n{lodge_data['blessing']}\n\n"
        
        if lodge_data.get('ban'):
            msg += f"|rLodge Ban:|n\n{lodge_data['ban']}\n\n"
        
        if lodge_data.get('sacred_hunt'):
            msg += f"|gSacred Hunt:|n\n{lodge_data['sacred_hunt']}\n\n"
        
        if lodge_data.get('access'):
            msg += f"|cAccess:|n {lodge_data['access']}\n\n"
        
        msg += f"|cSource:|n {lodge_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat lodge={lodge_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_werewolf_gifts(self, filter_arg=None):
        """Show werewolf gifts, optionally filtered by category, renown, or auspice."""
        from world.cofd.powers.werewolf_gifts import (
            get_all_gifts, get_gifts_by_type, get_gifts_by_renown, GIFT_CATEGORIES
        )
        
        if not filter_arg:
            # Show all gift categories
            output = ["|wWerewolf Gifts (Facets)|n", "", "|cAvailable Gift Categories:|n", ""]
            
            # Moon Gifts
            output.append("|yMoon Gifts (Auspice-Specific):|n")
            output.append("  crescent_moon (Ithaeur), full_moon (Rahu), gibbous_moon (Cahalith)")
            output.append("  half_moon (Elodoth), new_moon (Irraka)")
            output.append("")
            
            # Shadow Gift Categories
            output.append("|yShadow Gifts (General):|n")
            shadow_cats = ["agony", "blood", "death", "disease", "dominance", "elementals",
                          "evasion", "fervor", "hunger", "insight", "inspiration", "knowledge",
                          "nature", "rage", "shaping", "stealth", "strength", "technology",
                          "warding", "weather", "change", "hunting", "pack"]
            
            # Display in 3 columns
            for i in range(0, len(shadow_cats), 3):
                row = shadow_cats[i:i+3]
                row_text = "  " + ", ".join([f"{cat}" for cat in row])
                output.append(row_text)
            
            output.append("")
            output.append("|cBy Renown:|n")
            output.append("  cunning, glory, honor, purity, wisdom")
            output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFilter by category:|n +lookup gifts agony, +lookup gifts crescent_moon, etc.")
            self.caller.msg("|cFilter by renown:|n +lookup gifts cunning, +lookup gifts glory, etc.")
            self.caller.msg("|cFor gift details:|n +lookup <gift_name> (e.g., +lookup shadow_gaze)")
            return
        
        # Check if it's a renown filter
        if filter_arg in ["cunning", "glory", "honor", "purity", "wisdom"]:
            gifts = get_gifts_by_renown(filter_arg)
            title = f"|wWerewolf Gifts - {filter_arg.title()} Renown|n"
        else:
            # It's a category filter
            gifts = get_gifts_by_type(filter_arg)
            if not gifts:
                self.caller.msg(f"No gifts found for category: {filter_arg}")
                self.caller.msg("|cValid categories:|n Use |y+lookup gifts|n to see all categories")
                return
            
            title = f"|wWerewolf Gifts - {filter_arg.replace('_', ' ').title()}|n"
        
        # Group by rank
        gifts_by_rank = {1: [], 2: [], 3: [], 4: [], 5: []}
        for gift_key, gift_data in gifts.items():
            rank = gift_data.get('rank', 1)
            gifts_by_rank[rank].append((gift_key, gift_data))
        
        output = [title, ""]
        
        # Display gifts by rank
        for rank in range(1, 6):
            rank_gifts = gifts_by_rank[rank]
            if rank_gifts:
                dots = "●" * rank
                output.append(f"|yRank {dots}|n")
                
                for gift_key, gift_data in sorted(rank_gifts, key=lambda x: x[1]['name']):
                    gift_name = gift_data['name']
                    renown = gift_data['renown'].title()
                    cost = gift_data['cost']
                    
                    output.append(f"  |g{gift_name}|n ({renown}) - Cost: {cost}")
                    output.append(f"    |gUse:|n +lookup {gift_key}")
                
                output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg(f"|cTotal:|n {len(gifts)} gifts")
        self.caller.msg("|cFor gift details:|n +lookup <gift_name> (e.g., +lookup shadow_gaze)")
    
    def show_gift_details(self, gift_key, gift_data):
        """Show detailed information about a specific werewolf gift."""
        msg = f"|w{gift_data['name']} (Werewolf Gift)|n\n"
        
        # Category and Renown
        gift_type = gift_data['gift_type'].replace('_', ' ').title()
        renown = gift_data['renown'].title()
        msg += f"|cGift Type:|n {gift_type}\n"
        msg += f"|cRenown:|n {renown}\n"
        
        # Rank
        rank = gift_data['rank']
        dots = "●" * rank if isinstance(rank, int) else rank
        msg += f"|cRank:|n {dots}\n"
        
        # Cost
        msg += f"|cCost:|n {gift_data['cost']}\n"
        
        # Dice Pool
        if gift_data.get('dice_pool') and gift_data['dice_pool'] != '-':
            msg += f"|cDice Pool:|n {gift_data['dice_pool']}\n"
        
        # Action
        msg += f"|cAction:|n {gift_data['action']}\n"
        
        # Duration
        if gift_data.get('duration') and gift_data['duration'] != '-':
            msg += f"|cDuration:|n {gift_data['duration']}\n"
        
        # Description
        msg += f"|cDescription:|n {gift_data['description']}\n"
        
        # Source
        msg += f"|cSource:|n {gift_data['book']}\n"
        
        # Usage
        msg += f"\n|gTo add to character:|n +stat gift={gift_key}\n"
        
        self.caller.msg(msg)
    
    def show_contract_details(self, contract_key, contract_data):
        """Show detailed information about a specific changeling contract."""
        msg = f"|w{contract_data['name']} (Changeling Contract)|n\n"
        
        # Contract Type
        contract_type = contract_data['contract_type'].replace('_', ' ').title()
        msg += f"|cContract Type:|n {contract_type}\n"
        
        # Cost
        msg += f"|cCost:|n {contract_data['cost']}\n"
        
        # Dice Pool
        if contract_data.get('dice_pool') and contract_data['dice_pool'] != 'None':
            msg += f"|cDice Pool:|n {contract_data['dice_pool']}\n"
        
        # Loopholes
        if contract_data.get('loopholes'):
            msg += f"|cLoopholes:|n {contract_data['loopholes']}\n"
        
        # Description
        msg += f"|cDescription:|n {contract_data['description']}\n"
        
        # Seeming Benefits
        if contract_data.get('seeming_benefits'):
            msg += f"\n|cSeeming Benefits:|n\n"
            for seeming, benefit in contract_data['seeming_benefits'].items():
                if benefit:  # Only show non-empty benefits
                    seeming_title = seeming.title()
                    msg += f"  |y{seeming_title}:|n {benefit}\n"
        
        # Source
        msg += f"\n|cSource:|n {contract_data['book']}\n"
        
        # Usage
        msg += f"\n|gTo add to character:|n +stat contract={contract_key}\n"
        
        self.caller.msg(msg)
    
    def show_changeling_contracts(self, filter_arg=None):
        """Show changeling contracts, optionally filtered by category."""
        from world.cofd.powers.changeling_contracts import (
            get_contracts_by_category, get_all_contracts
        )
        
        if not filter_arg:
            # Show all contract categories
            output = ["|wChangeling Contracts|n", "", "|cAvailable Contract Categories:|n", ""]
            
            # Main contract categories
            main_cats = ["crown", "jewel", "mirror", "shield", "steed", "sword", 
                        "chalice", "coin", "stars", "thorn"]
            
            output.append("|yMain Contracts:|n")
            # Display in 2 columns
            for i in range(0, len(main_cats), 2):
                row = main_cats[i:i+2]
                row_text = "  " + ", ".join([f"{cat}" for cat in row])
                output.append(row_text)
            
            output.append("")
            output.append("|yOther Contracts:|n")
            output.append("  goblin (Independent Contracts)")
            output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFilter by category:|n +lookup contracts crown, +lookup contracts goblin, etc.")
            self.caller.msg("|cFor contract details:|n +lookup <contract_name> (e.g., +lookup hostile_takeover)")
            return
        
        # Get contracts by category
        contracts = get_contracts_by_category(filter_arg)
        if not contracts:
            self.caller.msg(f"No contracts found for category: {filter_arg}")
            self.caller.msg("|cValid categories:|n Use |y+lookup contracts|n to see all categories")
            return
        
        # Display contracts
        title = f"|wChangeling Contracts - {filter_arg.title()}|n"
        self.caller.msg(title)
        self.caller.msg("=" * len(title.replace("|w", "").replace("|n", "")))
        
        for contract_key, contract_data in contracts.items():
            name = contract_data['name']
            cost = contract_data['cost']
            contract_type = contract_data['contract_type']
            
            # Format contract type for display
            type_display = contract_type.replace('_', ' ').title()
            if 'royal' in contract_type:
                type_display = type_display.replace(' Royal', ' (Royal)')
            
            msg = f"\n|y{name}|n ({type_display})\n"
            msg += f"|cCost:|n {cost}\n"
            
            # Show dice pool if present
            if contract_data.get('dice_pool') and contract_data['dice_pool'] != 'None':
                msg += f"|cDice Pool:|n {contract_data['dice_pool']}\n"
            
            # Show loopholes if present
            if contract_data.get('loopholes'):
                msg += f"|cLoopholes:|n {contract_data['loopholes']}\n"
            
            # Show description (truncated)
            description = contract_data['description']
            if len(description) > 150:
                description = description[:147] + "..."
            msg += f"|cDescription:|n {description}\n"
            
            # Show source
            msg += f"|cSource:|n {contract_data['book']}\n"
            
            self.caller.msg(msg)
        
        self.caller.msg(f"\n|cTotal:|n {len(contracts)} contracts in {filter_arg.title()} category")
        self.caller.msg(f"\n|cNote:|n Set with: |y+stat contract=<name>|n")
    
    def show_geist_keys(self):
        """Show all Geist keys."""
        msg = self.format_header("Geist Keys")
        msg += "\n\n"
        
        keys_data = LOOKUP_DATA.geist_data['keys_detailed']
        
        msg += "|cAll nine Keys unlock specific types of Haunts based on associated Attributes:|n\n\n"
        
        # Show all keys with their attributes
        for key_name in sorted(keys_data.keys()):
            key_data = keys_data[key_name]
            full_name = key_data['full_name']
            attribute = key_data['attribute']
            description = key_data['description']
            
            msg += f"|g{full_name:<30}|n |c({attribute})|n\n"
            msg += f"  {description}\n"
            msg += f"  |gUse:|n +lookup keys {key_name}\n\n"
        
        msg += "|cFor key details:|n +lookup keys <key_name> (e.g., +lookup keys beasts)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_geist_key(self, key_name):
        """Show detailed information about a specific Geist key."""
        keys_data = LOOKUP_DATA.geist_data['keys_detailed']
        
        # Normalize key name
        key_name = key_name.lower().replace(" ", " ")
        
        # Try to find the key
        key_data = keys_data.get(key_name)
        
        if not key_data:
            self.caller.msg(f"Key '{key_name}' not found.")
            self.caller.msg("|cUse:|n +lookup keys - to see all available keys")
            return
        
        msg = f"|w{key_data['full_name']}|n\n"
        msg += f"|cAttribute:|n {key_data['attribute']}\n"
        
        if key_data.get('alternate_names'):
            msg += f"|cAlso Known As:|n {key_data['alternate_names']}\n"
        
        msg += f"\n|cDescription:|n {key_data['description']}\n"
        msg += f"\n|rDoom:|n {key_data['doom']}\n"
        msg += f"\n|cSource:|n {key_data['book']}\n"
        
        self.caller.msg(msg)
    
    def show_geist_haunts(self):
        """Show all Geist haunts."""
        haunts_data = LOOKUP_DATA.geist_data['haunts_detailed']
        
        output = ["|wGeist Haunts|n", ""]
        output.append("|cHaunts are the supernatural powers of the Bound, rated from 1 to 5 dots:|n")
        output.append("")
        
        # List all haunts
        for haunt_name in sorted(haunts_data.keys()):
            haunt_display = haunt_name.replace("_", " ").title()
            output.append(f"|g{haunt_display}|n")
            output.append(f"  |gUse:|n +lookup haunts {haunt_name}")
        
        output.append("")
        self.caller.msg("\n".join(output))
        self.caller.msg("|cFor haunt details:|n +lookup haunts <haunt_name> (e.g., +lookup haunts boneyard)")
    
    def show_geist_haunt(self, haunt_name):
        """Show detailed information about a specific Geist haunt."""
        haunts_data = LOOKUP_DATA.geist_data['haunts_detailed']
        
        # Normalize haunt name
        haunt_name = haunt_name.lower().replace(" ", "_")
        
        # Try to find the haunt
        haunt_powers = haunts_data.get(haunt_name)
        
        if not haunt_powers:
            self.caller.msg(f"Haunt '{haunt_name}' not found.")
            self.caller.msg("|cUse:|n +lookup haunts - to see all available haunts")
            return
        
        haunt_display = haunt_name.replace("_", " ").title()
        output = [f"|wThe {haunt_display}|n", ""]
        
        # Group powers by rank
        powers_by_rank = {1: [], 2: [], 3: [], 4: [], 5: []}
        for power_key, power_data in haunt_powers.items():
            rank = power_data.get('rank', 1)
            powers_by_rank[rank].append((power_key, power_data))
        
        # Display powers by rank
        for rank in range(1, 6):
            rank_powers = powers_by_rank[rank]
            if rank_powers:
                dots = "●" * rank
                output.append(f"|yRank {dots}|n")
                
                for power_key, power_data in rank_powers:
                    power_name = power_data['name']
                    cost = power_data['cost']
                    description = power_data['description']
                    
                    output.append(f"  |g{power_name}|n - Cost: {cost}")
                    output.append(f"    {description}")
                    
                    if power_data.get('additional'):
                        output.append(f"    |cAdditional:|n {power_data['additional']}")
                    
                    output.append(f"    |cSource:|n {power_data['book']}")
                    output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg(f"|cTotal:|n {len(haunt_powers)} powers in {haunt_display}")
        self.caller.msg(f"|cNote:|n Set haunt rating with: |y+stat {haunt_name}=<dots>|n")
    
    def show_seemings(self):
        """Show changeling seemings."""
        msg = self.format_header("Changeling Seemings")
        msg += "\n\n"
        
        seeming_descriptions = {
            "beast": "Animal-like changelings with feral instincts",
            "darkling": "Shadow-touched changelings who lurk in darkness",
            "elemental": "Changelings infused with primal forces",
            "fairest": "Beautiful changelings of devastating presence",
            "ogre": "Brutal changelings of terrifying strength",
            "wizened": "Crafty changelings of supernatural skill"
        }
        
        for seeming in sorted(LOOKUP_DATA.changeling_data['seemings']):
            desc = seeming_descriptions.get(seeming, "Changeling seeming")
            msg += f"|m{seeming.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Seemings reflect how the Fae transformed a changeling.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_courts(self):
        """Show changeling courts."""
        msg = self.format_header("Changeling Courts")
        msg += "\n\n"
        
        court_descriptions = {
            "spring": "The Emerald Court of desire and new beginnings",
            "summer": "The Crimson Court of wrath and iron resolve",
            "autumn": "The Leaden Court of fear and sorcerous power",
            "winter": "The Onyx Court of sorrow and cold logic",
            "courtless": "Independent changelings who reject court politics"
        }
        
        for court in sorted(LOOKUP_DATA.changeling_data['courts']):
            desc = court_descriptions.get(court, "Changeling court")
            msg += f"|m{court.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Courts are seasonal political factions among the Lost.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_kiths(self):
        """Show changeling kiths."""
        msg = self.format_header("Changeling Kiths")
        msg += "\n\n"
        
        kiths_data = LOOKUP_DATA.changeling_data['kiths_detailed']
        
        # Organize kiths alphabetically
        for kith_key in sorted(kiths_data.keys()):
            kith_data = kiths_data[kith_key]
            name = kith_data['name']
            skill = kith_data['skill']
            desc = kith_data['description']
            
            msg += f"|m{name:<20}|n (|c{skill}|n)\n"
            msg += f"  {desc}\n"
            msg += f"  |gUse:|n +lookup kiths {kith_key}\n\n"
        
        msg += f"|cTotal:|n {len(kiths_data)} Kiths available\n"
        msg += "|cFor kith details:|n +lookup kiths <kith_name> (e.g., +lookup kiths bright_one)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_kith_details(self, kith_name):
        """Show detailed information about a specific changeling kith."""
        from world.cofd.powers.changeling_kiths import get_kith
        
        # Normalize kith name
        kith_key = kith_name.lower().replace(" ", "_")
        
        # Get kith data
        kith_data = get_kith(kith_key)
        
        if not kith_data:
            self.caller.msg(f"Kith '{kith_name}' not found.")
            self.caller.msg("|cUse:|n +lookup kiths - to see all available kiths")
            return
        
        msg = self.format_header(f"{kith_data['name']} - Changeling Kith")
        msg += "\n\n"
        
        msg += f"|cAssociated Skill:|n {kith_data['skill']}\n"
        msg += f"|cDescription:|n {kith_data['description']}\n\n"
        msg += f"|wKith Blessing:|n\n{kith_data['blessing']}\n\n"
        msg += f"|cSource:|n {kith_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat kith={kith_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_entitlements(self):
        """Show changeling entitlements."""
        msg = self.format_header("Changeling Entitlements")
        msg += "\n\n"
        msg += "|cEntitlements are prestigious positions and organizations among the Lost:|n\n\n"
        
        entitlements = LOOKUP_DATA.changeling_data['entitlements_detailed']
        
        for entitlement_key in sorted(entitlements.keys()):
            entitlement_data = entitlements[entitlement_key]
            name = entitlement_data['name']
            desc = entitlement_data['description']
            
            msg += f"|m{name:<40}|n\n"
            msg += f"  {desc}\n"
            msg += f"  |gUse:|n +lookup entitlements {entitlement_key}\n\n"
        
        msg += f"|cTotal:|n {len(entitlements)} entitlements available\n"
        msg += "|cFor entitlement details:|n +lookup entitlements <entitlement_name>\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_entitlement_details(self, entitlement_name):
        """Show detailed information about a specific changeling entitlement."""
        from world.cofd.powers.changeling_seemings import get_entitlement
        
        # Normalize entitlement name
        entitlement_key = entitlement_name.lower().replace(" ", "_")
        
        # Get entitlement data
        entitlement_data = get_entitlement(entitlement_key)
        
        if not entitlement_data:
            self.caller.msg(f"Entitlement '{entitlement_name}' not found.")
            self.caller.msg("|cUse:|n +lookup entitlements - to see all available entitlements")
            return
        
        msg = self.format_header(f"{entitlement_data['name']} - Changeling Entitlement")
        msg += "\n\n"
        
        msg += f"|cDescription:|n {entitlement_data['description']}\n\n"
        
        # Prerequisites (can be string or dict)
        prereqs = entitlement_data['prerequisites']
        if isinstance(prereqs, dict):
            msg += f"|cPrerequisites:|n\n"
            for role, req in prereqs.items():
                msg += f"  |y{role}:|n {req}\n"
        else:
            msg += f"|cPrerequisites:|n {prereqs}\n"
        
        msg += f"\n|rEntitlement Curse:|n\n{entitlement_data['curse']}\n\n"
        
        msg += f"|wEntitlement Token:|n\n{entitlement_data['token']}\n\n"
        
        msg += f"|wEntitlement Blessings:|n\n"
        for blessing in entitlement_data['blessings']:
            msg += f"  • {blessing}\n"
        
        msg += f"\n|cSource:|n {entitlement_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat entitlement={entitlement_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_incarnations(self):
        """Show demon incarnations."""
        msg = self.format_header("Demon Incarnations")
        msg += "\n\n"
        
        incarnation_descriptions = {
            "destroyer": "Angels of destruction and apocalypse",
            "guardian": "Angels of protection and defense",
            "messenger": "Angels of communication and knowledge",
            "psychopomp": "Angels of death and transition"
        }
        
        for incarnation in sorted(LOOKUP_DATA.demon_data['incarnations']):
            desc = incarnation_descriptions.get(incarnation, "Demon incarnation")
            msg += f"|r{incarnation.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Incarnations reflect a demon's original angelic function.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_agendas(self):
        """Show demon agendas."""
        msg = self.format_header("Demon Agendas")
        msg += "\n\n"
        
        agenda_descriptions = {
            "inquisitor": "Seeking to understand the God-Machine",
            "integrator": "Attempting to live among humans",
            "saboteur": "Working to destroy the God-Machine",
            "tempter": "Corrupting humans for their own ends"
        }
        
        for agenda in sorted(LOOKUP_DATA.demon_data['agendas']):
            desc = agenda_descriptions.get(agenda, "Demon agenda")
            msg += f"|r{agenda.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Agendas define a demon's goals in their new existence.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_embeds(self):
        """Show demon embeds."""
        msg = f"|wDemon Embeds|n\n\n"
        msg += "Embeds are intrinsic demonic powers tied to their former nature:\n\n"
        
        embeds = sorted([e.lower().replace(" ", "_") for e in LOOKUP_DATA.demon_data['embeds']])
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
        for i in range(0, len(embeds), 3):
            row = embeds[i:i+3]
            msg += "  " + "".join([f"|r{e.replace('_', ' ').title():<{col_width}}|n" for e in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(embeds)} Embeds\n"
        msg += f"\n|cNote:|n Set with: |y+stat embed=<name>|n"
        
        self.caller.msg(msg)
    
    def show_exploits(self):
        """Show demon exploits."""
        msg = f"|wDemon Exploits|n\n\n"
        msg += "Exploits are learned demonic powers that manipulate reality:\n\n"
        
        exploits = sorted([e.lower().replace(" ", "_") for e in LOOKUP_DATA.demon_data['exploits']])
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
        for i in range(0, len(exploits), 3):
            row = exploits[i:i+3]
            msg += "  " + "".join([f"|r{e.replace('_', ' ').title():<{col_width}}|n" for e in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(exploits)} Exploits\n"
        msg += f"\n|cNote:|n Set with: |y+stat exploit=<name>|n"
        
        self.caller.msg(msg)

    def show_guilds(self):
        """Show mummy guilds."""
        msg = self.format_header("Mummy Guilds")
        msg += "\n\n"
        
        guild_descriptions = {
            "mesen-nebu": "The Watchers, prophets and scholars who preserve knowledge",
            "sesha-hebsu": "The Scribes, ritualists and spellcasters who wield utterances",
            "su-menent": "The Shepherds, leaders and guides who protect the living",
            "tef-aabhi": "The Judges, warriors and executioners who enforce ma'at",
            "amenti": "Independent mummies with no guild affiliation"
        }
        
        for guild in sorted(LOOKUP_DATA.mummy_data['guilds']):
            desc = guild_descriptions.get(guild, "Mummy guild")
            msg += f"|y{guild.title().replace('-', ' '):<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Guilds determine a mummy's role and abilities.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_decrees(self):
        """Show mummy decrees."""
        msg = self.format_header("Mummy Decrees")
        msg += "\n\n"
        
        decree_descriptions = {
            "balance": "Maintain ma'at and cosmic equilibrium",
            "fortune": "Bring prosperity and good fortune to the cult",
            "knowledge": "Preserve and protect ancient wisdom",
            "protection": "Shield the cult from supernatural threats",
            "vengeance": "Strike down enemies of the Judges"
        }
        
        for decree in sorted(LOOKUP_DATA.mummy_data['decrees']):
            desc = decree_descriptions.get(decree, "Mummy decree")
            msg += f"|y{decree.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Decrees define a mummy's mission from the Judges.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_judges(self):
        """Show mummy judges."""
        msg = self.format_header("Mummy Judges")
        msg += "\n\n"
        
        judge_descriptions = {
            "djehuty": "The Ibis-Headed, god of wisdom and magic (Thoth)",
            "duamutef": "The Jackal-Headed, son of Horus, protector of the stomach",
            "hapi": "The Baboon-Headed, son of Horus, protector of the lungs",
            "imsety": "The Human-Headed, son of Horus, protector of the liver",
            "kebehsenuf": "The Falcon-Headed, son of Horus, protector of intestines",
            "nehebkau": "The Serpent, primordial guardian of the gates",
            "neith": "The Weaver, goddess of war and wisdom",
            "ptah": "The Craftsman, god of creation and artisans",
            "sobek": "The Crocodile, god of the Nile and military prowess"
        }
        
        for judge in sorted(LOOKUP_DATA.mummy_data['judges']):
            desc = judge_descriptions.get(judge, "Mummy judge")
            msg += f"|y{judge.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Judges are the gods who command mummies in Duat.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_utterances(self):
        """Show mummy utterances."""
        msg = f"|wMummy Utterances|n\n\n"
        msg += "Utterances are supernatural powers granted by Sekhem:\n\n"
        
        utterance_descriptions = {
            "afire": "Powers of flame and destruction",
            "bone": "Powers over death and the dead",
            "elements": "Control over the natural elements",
            "flesh": "Mastery of the body and healing",
            "guidance": "Insight and foresight",
            "glory": "Commanding presence and authority",
            "reign": "Leadership and dominion",
            "vision": "Enhanced perception and awareness",
            "word": "Power of command and compulsion"
        }
        
        for utterance in sorted(LOOKUP_DATA.mummy_data['utterances']):
            desc = utterance_descriptions.get(utterance, "Mummy utterance")
            msg += f"  |y{utterance.title():<15}|n - {desc}\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat utterance=<name>|n (rated 1-5 dots)"
        self.caller.msg(msg)
    
    def show_affinities(self):
        """Show mummy affinities."""
        msg = f"|wMummy Affinities|n\n\n"
        msg += "Affinities represent the nine souls of Egyptian belief:\n\n"
        
        affinity_descriptions = {
            "ab": "The heart, seat of emotion and will",
            "ba": "The personality and individuality",
            "ka": "The life force and vital essence",
            "khaibit": "The shadow, darker aspects",
            "khat": "The physical body",
            "ren": "The secret name and identity",
            "sahu": "The spiritual body",
            "sekhem": "The power and life energy",
            "sheut": "The shadow-self in the underworld"
        }
        
        for affinity in sorted(LOOKUP_DATA.mummy_data['affinities']):
            desc = affinity_descriptions.get(affinity, "Mummy affinity")
            msg += f"  |y{affinity.title():<15}|n - {desc}\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat affinity=<name>|n (rated 1-5 dots)"
        self.caller.msg(msg)
    
    def show_burdens(self):
        """Show geist burdens."""
        msg = self.format_header("Geist Burdens")
        msg += "\n\n"
        
        burden_descriptions = {
            "abiding": "Died lingering, unable to let go",
            "bereaved": "Died mourning, with unfinished grief",
            "hungry": "Died starving or craving",
            "kindly": "Died peacefully, accepting death",
            "vengeful": "Died angry, with unfinished business"
        }
        
        for burden in sorted(LOOKUP_DATA.geist_data['burdens']):
            desc = burden_descriptions.get(burden, "Geist burden")
            msg += f"|m{burden.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Burdens define how a Sin-Eater died.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_krewe_types(self):
        """Show geist krewe types."""
        msg = self.format_header("Geist Krewe Types")
        msg += "\n\n"
        
        krewe_descriptions = {
            "family": "Close-knit group bound by personal ties",
            "industrial": "Organized like a corporation or business",
            "network": "Loose association of independent agents",
            "military": "Hierarchical command structure",
            "academic": "Focused on research and knowledge"
        }
        
        for krewe in sorted(LOOKUP_DATA.geist_data['krewe_types']):
            desc = krewe_descriptions.get(krewe, "Krewe type")
            msg += f"|m{krewe.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Krewes are groups of Sin-Eaters working together.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_haunts(self):
        """Show geist haunts (manifestations)."""
        msg = f"|wGeist Haunts (Manifestations)|n\n\n"
        msg += "Haunts are supernatural powers rated 1-5 dots:\n\n"
        
        haunt_descriptions = {
            "boneyard": "Control over death and decay",
            "caul": "Protection and defensive abilities",
            "curse": "Inflicting misfortune and harm",
            "dirge": "Manipulating emotion and perception",
            "marionette": "Controlling bodies and actions",
            "memoria": "Accessing memories and the past",
            "oracle": "Perceiving the future and hidden truths",
            "rage": "Destructive and offensive power",
            "shroud": "Concealment and stealth",
            "tomb": "Manipulating the physical world"
        }
        
        for haunt in sorted(LOOKUP_DATA.geist_data['haunts']):
            desc = haunt_descriptions.get(haunt, "Geist haunt")
            msg += f"  |m{haunt.title():<15}|n - {desc}\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat <haunt>=<1-5>|n (e.g., +stat boneyard=3)"
        self.caller.msg(msg)
    
    def show_keys(self):
        """Show geist keys."""
        msg = f"|wGeist Keys|n\n\n"
        msg += "Keys unlock and enhance manifestations in specific situations:\n\n"
        
        for key in sorted(LOOKUP_DATA.geist_data['keys']):
            msg += f"  |m{key.title().replace('_', ' '):<15}|n - The Key of {key.title().replace('_', ' ')}\n"
        
        msg += f"\n|cTotal:|n {len(LOOKUP_DATA.geist_data['keys'])} Keys\n"
        msg += f"\n|cNote:|n Set with: |y+stat key=<name>|n (e.g., +stat key=cold_wind)"
        self.caller.msg(msg)
    
    def show_ceremonies(self):
        """Show geist ceremonies."""
        msg = f"|wGeist Ceremonies|n\n\n"
        msg += "Ceremonies are rituals Sin-Eaters can perform:\n\n"
        
        ceremonies = sorted([c.replace('_', ' ').title() for c in LOOKUP_DATA.geist_data['ceremonies']])
        
        # Display in columns
        col_width = 30
        for i in range(0, len(ceremonies), 2):
            row = ceremonies[i:i+2]
            msg += "  " + "".join([f"|m{c:<{col_width}}|n" for c in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(ceremonies)} Ceremonies\n"
        msg += f"\n|cNote:|n Set with: |y+stat ceremony=<name>|n"
        self.caller.msg(msg)
    
    def show_origins(self):
        """Show deviant origins."""
        msg = self.format_header("Deviant Origins")
        msg += "\n\n"
        
        origin_descriptions = {
            "cephalist": "Created by mad scientists and reality hackers",
            "cheiron group": "Experimented on by the supernatural hunting corporation",
            "government": "Products of black ops and secret military programs",
            "pentex": "Created by the corrupt megacorporation",
            "seers of the throne": "Twisted by servants of the Exarchs",
            "technocracy": "Remade by reality engineers and techno-mages"
        }
        
        for origin in sorted(LOOKUP_DATA.deviant_data['origins']):
            desc = origin_descriptions.get(origin, "Deviant origin")
            msg += f"|c{origin.title():<25}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Origins define who created or transformed the Deviant.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_clades(self):
        """Show deviant clades."""
        msg = self.format_header("Deviant Clades")
        msg += "\n\n"
        
        clade_descriptions = {
            "coactive": "Multiple beings merged into one",
            "devoted": "Transformed through sacrifice and dedication",
            "genotypal": "Genetically engineered or mutated",
            "invasive": "Invaded by foreign elements",
            "mutant": "Spontaneously evolved or changed",
            "pelagic": "Transformed by deep and alien forces",
            "remnant": "Rebuilt from death or destruction"
        }
        
        for clade in sorted(LOOKUP_DATA.deviant_data['clades']):
            desc = clade_descriptions.get(clade, "Deviant clade")
            msg += f"|c{clade.title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Clades define how a Deviant was transformed.\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_variations(self):
        """Show deviant variations."""
        from world.cofd.powers.deviant_data import ALL_VARIATIONS, VARIATION_CATEGORIES
        
        msg = f"|wDeviant Variations|n\n\n"
        msg += "Variations are the supernatural powers of Deviants:\n\n"
        
        # Group by category
        universal_variations = []
        clade_variations = {}
        
        for var_name, var_data in sorted(ALL_VARIATIONS.items()):
            category = var_data.get("category", "Unknown")
            name = var_data.get("name", var_name.replace("_", " ").title())
            keywords = ", ".join(var_data.get("keywords", []))
            
            var_line = f"  |c{name:<30}|n |w({keywords})|n"
            
            if category == "Universal":
                universal_variations.append(var_line)
            else:
                if category not in clade_variations:
                    clade_variations[category] = []
                clade_variations[category].append(var_line)
        
        if universal_variations:
            msg += "|yUniversal Variations:|n (available to all Deviants)\n"
            msg += "\n".join(universal_variations) + "\n\n"
        
        for clade, variations in sorted(clade_variations.items()):
            msg += f"|y{clade} Clade Variations:|n\n"
            msg += "\n".join(variations) + "\n\n"
        
        msg += f"|cTotal:|n {len(ALL_VARIATIONS)} Variations\n"
        msg += f"\n|cNote:|n Set with: |y+stat <variation_name>=<magnitude>|n"
        msg += f"\n|cDetailed lookup:|n |y+lookup variations <name>|n"
        self.caller.msg(msg)
    
    def show_adaptations(self):
        """Show deviant adaptations."""
        from world.cofd.powers.deviant_data import DEVIANT_ADAPTATIONS
        
        msg = f"|wDeviant Adaptations|n\n\n"
        msg += "Adaptations are special abilities that help Deviants manage their powers:\n\n"
        
        # Group by category
        universal_adaptations = []
        clade_adaptations = {}
        
        for adapt_name, adapt_data in sorted(DEVIANT_ADAPTATIONS.items()):
            category = adapt_data.get("category", "Unknown")
            name = adapt_data.get("name", adapt_name.replace("_", " ").title())
            desc = adapt_data.get("description", "")
            
            if category == "Universal":
                universal_adaptations.append(f"  |y{name:<25}|n - {desc}")
            else:
                if category not in clade_adaptations:
                    clade_adaptations[category] = []
                clade_adaptations[category].append(f"  |y{name:<25}|n - {desc}")
        
        if universal_adaptations:
            msg += "|cUniversal Adaptations:|n\n"
            msg += "\n".join(universal_adaptations) + "\n\n"
        
        for clade, adaptations in sorted(clade_adaptations.items()):
            msg += f"|c{clade} Clade Adaptations:|n\n"
            msg += "\n".join(adaptations) + "\n\n"
        
        msg += f"|cTotal:|n {len(DEVIANT_ADAPTATIONS)} Adaptations\n"
        msg += f"\n|cNote:|n Set with: |y+stat adaptation=<name>|n"
        msg += f"\n|cDetailed lookup:|n |y+lookup adaptations <name>|n"
        self.caller.msg(msg)
    
    def show_scars(self):
        """Show all deviant scars."""
        from world.cofd.powers.deviant_data import ALL_SCARS
        
        msg = f"|wDeviant Scars|n\n\n"
        msg += "Scars are the drawbacks and complications of a Deviant's transformation:\n\n"
        
        # Group by activation type
        controlled = []
        involuntary = []
        persistent = []
        
        for scar_name, scar_data in sorted(ALL_SCARS.items()):
            activation = scar_data.get("activation", "Unknown")
            name = scar_data.get("name", scar_name.replace("_", " ").title())
            keywords = ", ".join(scar_data.get("keywords", []))
            
            scar_line = f"  |r{name:<30}|n |w({keywords})|n"
            
            if activation == "Controlled":
                controlled.append(scar_line)
            elif activation == "Involuntary":
                involuntary.append(scar_line)
            elif activation == "Persistent":
                persistent.append(scar_line)
        
        if controlled:
            msg += f"|cControlled Scars:|n (player-activated)\n"
            msg += "\n".join(controlled) + "\n\n"
        
        if involuntary:
            msg += f"|cInvoluntary Scars:|n (triggered by circumstances)\n"
            msg += "\n".join(involuntary) + "\n\n"
        
        if persistent:
            msg += f"|cPersistent Scars:|n (always active)\n"
            msg += "\n".join(persistent) + "\n\n"
        
        msg += f"|cTotal:|n {len(ALL_SCARS)} Scars\n"
        msg += f"\n|cNote:|n Set with: |y+stat <scar_name>=<magnitude>|n"
        msg += f"\n|cDetailed lookup:|n |y+lookup scars <name>|n"
        self.caller.msg(msg)
    
    def show_deviant_variation(self, variation_name):
        """Show detailed information about a specific Deviant variation."""
        from world.cofd.powers.deviant_data import ALL_VARIATIONS
        
        # Normalize variation name
        variation_key = variation_name.lower().replace(" ", "_")
        
        # Look up variation
        variation_data = ALL_VARIATIONS.get(variation_key)
        if not variation_data:
            self.caller.msg(f"Variation '{variation_name}' not found.")
            self.caller.msg(f"Use |y+lookup variations|n to see all available variations.")
            return
        
        # Build detailed output
        msg = f"|wVariation: {variation_data['name']}|n\n"
        msg += f"|g{'=' * 78}|n\n\n"
        
        msg += f"|cCategory:|n {variation_data.get('category', 'Unknown')}\n"
        msg += f"|cKeywords:|n {', '.join(variation_data.get('keywords', []))}\n"
        msg += f"|cBook:|n {variation_data.get('book', 'Unknown')}\n\n"
        
        # Show magnitude effects
        magnitude_effects = variation_data.get("magnitude_effects", {})
        if magnitude_effects:
            msg += f"|wMagnitude Effects:|n\n"
            for magnitude in sorted(magnitude_effects.keys()):
                msg += f"  |y{'●' * magnitude}{'○' * (5 - magnitude)}|n {magnitude_effects[magnitude]}\n"
            msg += "\n"
        
        # Show deviations if any
        deviations = variation_data.get("deviations", {})
        if deviations:
            msg += f"|wDeviations:|n\n"
            for dev_name, dev_data in sorted(deviations.items()):
                cost = dev_data.get("cost", 0)
                cost_str = f"+{cost}" if cost > 0 else f"{cost}"
                msg += f"  |c{dev_name}|n ({cost_str} cost): {dev_data.get('effect', '')}\n"
            msg += "\n"
        
        msg += f"\n|cSet with:|n |y+stat {variation_key}=<magnitude>|n"
        self.caller.msg(msg)
    
    def show_deviant_scar(self, scar_name):
        """Show detailed information about a specific Deviant scar."""
        from world.cofd.powers.deviant_data import ALL_SCARS
        
        # Normalize scar name
        scar_key = scar_name.lower().replace(" ", "_")
        
        # Look up scar
        scar_data = ALL_SCARS.get(scar_key)
        if not scar_data:
            self.caller.msg(f"Scar '{scar_name}' not found.")
            self.caller.msg(f"Use |y+lookup scars|n to see all available scars.")
            return
        
        # Build detailed output
        msg = f"|wScar: {scar_data['name']}|n\n"
        msg += f"|g{'=' * 78}|n\n\n"
        
        msg += f"|cActivation:|n {scar_data.get('activation', 'Unknown')}\n"
        msg += f"|cCategory:|n {scar_data.get('category', 'Unknown')}\n"
        msg += f"|cKeywords:|n {', '.join(scar_data.get('keywords', []))}\n"
        msg += f"|cBook:|n {scar_data.get('book', 'Unknown')}\n\n"
        
        # Show magnitude effects
        magnitude_effects = scar_data.get("magnitude_effects", {})
        if magnitude_effects:
            msg += f"|wMagnitude Effects:|n\n"
            for magnitude in sorted(magnitude_effects.keys()):
                msg += f"  |r{'●' * magnitude}{'○' * (5 - magnitude)}|n {magnitude_effects[magnitude]}\n"
            msg += "\n"
        
        # Show deviations if any
        deviations = scar_data.get("deviations", {})
        if deviations:
            msg += f"|wDeviations (Scar Modifiers):|n\n"
            for dev_name, dev_data in sorted(deviations.items()):
                cost = dev_data.get("cost", 0)
                cost_str = f"+{cost}" if cost > 0 else f"{cost}"
                msg += f"  |c{dev_name}|n ({cost_str} cost): {dev_data.get('effect', '')}\n"
            msg += "\n"
        
        msg += f"\n|cSet with:|n |y+stat {scar_key}=<magnitude>|n"
        self.caller.msg(msg)
    
    def show_deviant_adaptation(self, adaptation_name):
        """Show detailed information about a specific Deviant adaptation."""
        from world.cofd.powers.deviant_data import DEVIANT_ADAPTATIONS
        
        # Normalize adaptation name
        adaptation_key = adaptation_name.lower().replace(" ", "_")
        
        # Look up adaptation
        adaptation_data = DEVIANT_ADAPTATIONS.get(adaptation_key)
        if not adaptation_data:
            self.caller.msg(f"Adaptation '{adaptation_name}' not found.")
            self.caller.msg(f"Use |y+lookup adaptations|n to see all available adaptations.")
            return
        
        # Build detailed output
        msg = f"|wAdaptation: {adaptation_data['name']}|n\n"
        msg += f"|g{'=' * 78}|n\n\n"
        
        msg += f"|cCategory:|n {adaptation_data.get('category', 'Unknown')}\n"
        msg += f"|cFrequency:|n {adaptation_data.get('frequency', 'Unknown')}\n"
        
        cost = adaptation_data.get('cost')
        if cost:
            msg += f"|cCost:|n {cost}\n"
        else:
            msg += f"|cCost:|n None\n"
        
        msg += f"|cBook:|n {adaptation_data.get('book', 'Unknown')}\n\n"
        
        msg += f"|wDescription:|n\n{adaptation_data.get('description', 'No description available.')}\n"
        
        msg += f"\n|cSet with:|n |y+stat adaptation={adaptation_key}|n"
        self.caller.msg(msg)
    
    def show_mortal_plus_types(self):
        """Show mortal+ types."""
        msg = f"|wMortal+ Types|n\n\n"
        msg += "Mortal+ includes all minor supernatural templates:\n\n"
        
        types = sorted(LOOKUP_DATA.mortal_plus_data['types'])
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
        for i in range(0, len(types), 3):
            row = types[i:i+3]
            msg += "  " + "".join([f"|w{t:<{col_width}}|n" for t in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(types)} Mortal+ Types\n"
        msg += f"\n|cNote:|n Use |y+stat template_type=<type>|n to set your mortal+ type"
        self.caller.msg(msg)
    
    def show_psychic_powers(self):
        """Show psychic powers."""
        msg = f"|wPsychic Powers|n\n\n"
        msg += "Psychic powers available to mortal+ psychics:\n\n"
        
        powers = sorted([p.title() for p in LOOKUP_DATA.mortal_plus_data['psychic_powers']])
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
        for i in range(0, len(powers), 3):
            row = powers[i:i+3]
            msg += "  " + "".join([f"|c{p:<{col_width}}|n" for p in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(powers)} Psychic Powers\n"
        msg += f"\n|cNote:|n Set with: |y+stat psychic=<power>|n (e.g., +stat psychic=telepathy)"
        self.caller.msg(msg)
    
    def show_wolf_blooded_tells(self):
        """Show wolf-blooded tells (2e)."""
        msg = self.format_header("Wolf-Blooded Tells (2e)")
        msg += "\n\n"
        
        tell_descriptions = {
            "moon_gift": "Powers that manifest based on moon phase",
            "pack_awareness": "Sense other Wolf-Blooded and werewolves",
            "territorial": "Enhanced abilities in claimed territory",
            "spirit_sight": "Ability to perceive the Shadow Realm",
            "primal": "Enhanced physical traits and instincts"
        }
        
        for tell in sorted(LOOKUP_DATA.mortal_plus_data['wolf_blooded_tells']):
            desc = tell_descriptions.get(tell, "Wolf-Blooded tell")
            msg += f"|y{tell.replace('_', ' ').title():<20}|n {desc}\n"
        
        msg += "\n"
        msg += "|cNote:|n Tells are inherited traits from werewolf ancestry.\n"
        msg += "Set with: |y+stat tell=<name>|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_specialties(self, skill=None):
        """Show skill specialties, optionally filtered by skill."""
        if skill:
            # Show specialties for a specific skill
            skill = skill.lower().replace(" ", "_")
            if skill not in LOOKUP_DATA.specialties:
                self.caller.msg(f"No specialties found for '{skill}'.")
                self.caller.msg(f"Use |y+lookup specialties|n to see all available skills with specialties.")
                return
            
            specialties = LOOKUP_DATA.specialties[skill]
            msg = f"|w{skill.title().replace('_', ' ')} Specialties|n\n\n"
            msg += f"|cSuggested Specialties:|n\n"
            msg += "  " + ", ".join(specialties) + "\n\n"
            msg += f"|cUsage:|n |y+stat specialty/{skill}=<specialty name>|n\n"
            msg += f"|cExample:|n |y+stat specialty/{skill}={specialties[0]}|n"
            
            self.caller.msg(msg)
        else:
            # Show all specialties organized by skill type
            msg = f"|wSkill Specialties|n\n\n"
            msg += "Specialties add depth and focus to your skills. Set them with:\n"
            msg += "|y+stat specialty/<skill>=<specialty name>|n\n\n"
            
            # Organize by skill type
            mental_skills = ['academics', 'computer', 'crafts', 'investigation', 'medicine', 'occult', 'politics', 'science']
            physical_skills = ['athletics', 'brawl', 'drive', 'firearms', 'larceny', 'stealth', 'survival', 'weaponry']
            social_skills = ['animal_ken', 'empathy', 'expression', 'intimidation', 'persuasion', 'socialize', 'streetwise', 'subterfuge']
            
            msg += "|cMental Skills:|n\n"
            for skill in mental_skills:
                if skill in LOOKUP_DATA.specialties:
                    specialties = LOOKUP_DATA.specialties[skill]
                    msg += f"  |y{skill.title().replace('_', ' ')}:|n {', '.join(specialties[:3])}"
                    if len(specialties) > 3:
                        msg += f", ... ({len(specialties)} total)"
                    msg += "\n"
            
            msg += "\n|cPhysical Skills:|n\n"
            for skill in physical_skills:
                if skill in LOOKUP_DATA.specialties:
                    specialties = LOOKUP_DATA.specialties[skill]
                    msg += f"  |y{skill.title().replace('_', ' ')}:|n {', '.join(specialties[:3])}"
                    if len(specialties) > 3:
                        msg += f", ... ({len(specialties)} total)"
                    msg += "\n"
            
            msg += "\n|cSocial Skills:|n\n"
            for skill in social_skills:
                if skill in LOOKUP_DATA.specialties:
                    specialties = LOOKUP_DATA.specialties[skill]
                    msg += f"  |y{skill.title().replace('_', ' ')}:|n {', '.join(specialties[:3])}"
                    if len(specialties) > 3:
                        msg += f", ... ({len(specialties)} total)"
                    msg += "\n"
            
            msg += f"\n|cUse:|n |y+lookup specialties <skill>|n to see all specialties for a specific skill\n"
            msg += f"|cExample:|n |y+lookup specialties athletics|n"
            
            self.caller.msg(msg)
    
    def search_stats(self):
        """Search for stats containing the given term."""
        if not self.args:
            self.caller.msg("Usage: +lookup/search <search term>")
            return
        
        search_results = LOOKUP_DATA.search_stats(self.args)
        
        if search_results:
            msg = f"|wSearch results for '{self.args}':|n\n"
            formatted_results = []
            
            for stat_type, name, data in search_results[:20]:  # Limit to 20 results
                if stat_type == 'attribute':
                    formatted_results.append(f"|wAttribute:|n {name.title()} ({data.att_type})")
                elif stat_type == 'skill':
                    formatted_results.append(f"|wSkill:|n {name.title().replace('_', ' ')} ({data.skill_type})")
                elif stat_type == 'merit':
                    formatted_results.append(f"|wMerit:|n {name} ({data.merit_type})")
                elif stat_type == 'discipline':
                    formatted_results.append(f"|wDiscipline:|n {name.title()}")
                elif stat_type == 'discipline_power':
                    formatted_results.append(f"|wDiscipline Power:|n {name} ({data['discipline'].title()})")
                elif stat_type == 'gift':
                    gift_type = data.get('gift_type', 'gift').replace('_', ' ').title()
                    formatted_results.append(f"|wWerewolf Gift:|n {name} ({gift_type})")
                elif stat_type == 'ritual':
                    ritual_type = data.get('type', 'ritual').title()
                    formatted_results.append(f"|w{ritual_type.title()}:|n {name}")
                elif stat_type == 'arcanum':
                    formatted_results.append(f"|wArcanum:|n {name.title()}")
            
            msg += "\n".join(formatted_results)
            if len(search_results) > 20:
                msg += f"\n\n|y... and {len(search_results) - 20} more results.|n"
            msg += f"\n\n|cUse:|n |y+lookup <stat_name>|n for detailed information."
        else:
            msg = f"No results found for '{self.args}'."
        
        self.caller.msg(msg)
    
    def show_discipline_details(self, discipline_name):
        """Show detailed information about a specific discipline."""
        discipline_key = discipline_name.lower().replace(" ", "_")
        
        # Check if it's a valid discipline
        from world.cofd.templates.vampire import VAMPIRE_PRIMARY_POWERS
        if discipline_key not in [d.lower() for d in VAMPIRE_PRIMARY_POWERS]:
            self.caller.msg(f"Discipline '{discipline_name}' not found.")
            self.caller.msg("|cUse:|n +lookup disciplines - to see all available disciplines")
            return
        
        desc = get_discipline_description(discipline_key)
        msg = self.format_header(f"{discipline_key.title()} - Vampire Discipline")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n\n"
        msg += f"|cView Powers:|n Use |y+lookup powers {discipline_key}|n to see individual powers\n"
        msg += f"|cSet on Character:|n |y+stat {discipline_key}=<1-5>|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_clan_details(self, clan_name):
        """Show detailed information about a specific clan."""
        from world.cofd.powers.vampire_clans import get_clan
        
        clan_key = clan_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
        
        # Get detailed clan data
        clan_data = get_clan(clan_key)
        
        if not clan_data:
            self.caller.msg(f"Clan '{clan_name}' not found.")
            self.caller.msg("|cUse:|n +lookup clans - to see all available clans")
            return
        
        msg = self.format_header(f"{clan_data['name']} - Vampire Clan")
        msg += "\n\n"
        
        msg += f"|cNickname:|n {clan_data['nickname']}\n"
        msg += f"|cClan Disciplines:|n {', '.join(clan_data['disciplines'])}\n"
        msg += f"|cBonus Trait:|n {clan_data['bonus_trait']}\n"
        msg += f"|cDescription:|n {clan_data['description']}\n\n"
        
        msg += f"|rClan Weakness:|n\n{clan_data['weakness']}\n\n"
        
        msg += f"|cSource:|n {clan_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat clan={clan_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_bloodlines(self):
        """Show vampire bloodlines."""
        msg = self.format_header("Vampire Bloodlines")
        msg += "\n\n"
        msg += "|cBloodlines are specialized vampiric lineages with unique disciplines and banes:|n\n\n"
        
        bloodlines = LOOKUP_DATA.vampire_data['bloodlines_detailed']
        
        for bloodline_key in sorted(bloodlines.keys()):
            bloodline_data = bloodlines[bloodline_key]
            name = bloodline_data['name']
            parent = bloodline_data['parent_clan']
            desc = bloodline_data['description']
            
            msg += f"|r{name:<30}|n (|y{parent}|n)\n"
            msg += f"  {desc}\n"
            msg += f"  |gUse:|n +lookup bloodlines {bloodline_key}\n\n"
        
        msg += f"|cTotal:|n {len(bloodlines)} bloodlines available\n"
        msg += "|cFor bloodline details:|n +lookup bloodlines <bloodline_name> (e.g., +lookup bloodlines morbus)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_bloodline_details(self, bloodline_name):
        """Show detailed information about a specific vampire bloodline."""
        from world.cofd.powers.vampire_clans import get_bloodline
        
        # Normalize bloodline name
        bloodline_key = bloodline_name.lower().replace(" ", "_")
        
        # Get bloodline data
        bloodline_data = get_bloodline(bloodline_key)
        
        if not bloodline_data:
            self.caller.msg(f"Bloodline '{bloodline_name}' not found.")
            self.caller.msg("|cUse:|n +lookup bloodlines - to see all available bloodlines")
            return
        
        msg = self.format_header(f"{bloodline_data['name']} - Vampire Bloodline")
        msg += "\n\n"
        
        msg += f"|cParent Clan:|n {bloodline_data['parent_clan']}\n"
        
        # Handle disciplines (can be string or list)
        if isinstance(bloodline_data['disciplines'], list):
            msg += f"|cDisciplines:|n {', '.join(bloodline_data['disciplines'])}\n"
        else:
            msg += f"|cDisciplines:|n {bloodline_data['disciplines']}\n"
        
        msg += f"|cGifts:|n {bloodline_data['gifts']}\n"
        msg += f"|cDescription:|n {bloodline_data['description']}\n\n"
        
        msg += f"|rBloodline Bane:|n\n{bloodline_data['bane']}\n\n"
        
        msg += f"|cSource:|n {bloodline_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat bloodline={bloodline_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_covenant_details(self, covenant_name):
        """Show detailed information about a specific covenant."""
        from world.cofd.powers.vampire_covenants import get_covenant
        
        covenant_key = covenant_name.lower().replace(" ", "_")
        
        # Get detailed covenant data
        covenant_data = get_covenant(covenant_key)
        
        if not covenant_data:
            self.caller.msg(f"Covenant '{covenant_name}' not found.")
            self.caller.msg("|cUse:|n +lookup covenants - to see all available covenants")
            return
        
        msg = self.format_header(f"{covenant_data['name']} - Vampire Covenant")
        msg += "\n\n"
        
        if covenant_data.get('nickname'):
            msg += f"|cNickname:|n {covenant_data['nickname']}\n"
        
        if covenant_data.get('region'):
            msg += f"|cRegion:|n {covenant_data['region']}\n"
        
        if covenant_data.get('era'):
            msg += f"|cEra:|n {covenant_data['era']}\n"
        
        msg += f"|cAdvantage:|n {covenant_data['advantage']}\n"
        
        # Use full_description if available, otherwise use description
        desc = covenant_data.get('full_description', covenant_data['description'])
        msg += f"|cDescription:|n {desc}\n\n"
        
        msg += f"|cSource:|n {covenant_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat covenant={covenant_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_path_details(self, path_name):
        """Show detailed information about a specific mage path."""
        from world.cofd.powers.mage_paths import get_path
        
        path_key = path_name.lower().replace(" ", "_")
        
        # Get detailed path data
        path_data = get_path(path_key)
        
        if not path_data:
            self.caller.msg(f"Path '{path_name}' not found.")
            self.caller.msg("|cUse:|n +lookup paths - to see all available paths")
            return
        
        msg = self.format_header(f"{path_data['name']} - Mage Path")
        msg += "\n\n"
        
        msg += f"|cNickname:|n {path_data['nickname']}\n"
        msg += f"|cRuling Arcana:|n {', '.join(path_data['ruling_arcana'])}\n"
        msg += f"|cInferior Arcanum:|n {path_data['inferior_arcanum']}\n"
        msg += f"|cMaterials:|n {path_data['materials']}\n"
        msg += f"|cPath Tools:|n {path_data['path_tools']}\n"
        msg += f"|cDescription:|n {path_data['description']}\n\n"
        
        msg += f"|cSource:|n {path_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat path={path_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_order_details(self, order_name):
        """Show detailed information about a specific mage order."""
        from world.cofd.powers.mage_orders_detailed import get_order
        
        order_key = order_name.lower().replace(" ", "_")
        
        # Get detailed order data
        order_data = get_order(order_key)
        
        if not order_data:
            self.caller.msg(f"Order '{order_name}' not found.")
            self.caller.msg("|cUse:|n +lookup orders - to see all available orders")
            return
        
        msg = self.format_header(f"{order_data['name']} - Mage Order")
        msg += "\n\n"
        
        if order_data.get('nickname'):
            msg += f"|cNickname:|n {order_data['nickname']}\n"
        
        # Handle different order types
        if order_data.get('creed'):
            msg += f"|cCreed:|n {order_data['creed']}\n"
        elif order_data.get('ethos'):
            msg += f"|cEthos:|n {order_data['ethos']}\n"
        
        if order_data.get('symbolism'):
            msg += f"|cSymbolism:|n {order_data['symbolism']}\n"
        
        if order_data.get('rote_skills'):
            if isinstance(order_data['rote_skills'], list):
                msg += f"|cRote Skills:|n {', '.join(order_data['rote_skills'])}\n"
            else:
                msg += f"|cRote Skills:|n {order_data['rote_skills']}\n"
        
        # Ministry-specific fields
        if order_data.get('crown'):
            msg += f"|cCrown:|n {order_data['crown']}\n"
        if order_data.get('iron_seal'):
            msg += f"|cIron Seal:|n {order_data['iron_seal']}\n"
        
        # Historical order fields
        if order_data.get('greek_name'):
            msg += f"|cGreek Name:|n {order_data['greek_name']}\n"
        if order_data.get('region'):
            msg += f"|cRegion:|n {order_data['region']}\n"
        if order_data.get('era'):
            msg += f"|cEra:|n {order_data['era']}\n"
        
        msg += f"|cDescription:|n {order_data['description']}\n\n"
        
        msg += f"|cSource:|n {order_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat order={order_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_legacies(self):
        """Show mage legacies."""
        msg = self.format_header("Mage Legacies")
        msg += "\n\n"
        msg += "|cLegacies are specialized magical traditions that refine a mage's practice:|n\n\n"
        
        legacies = LOOKUP_DATA.mage_data['legacies_detailed']
        
        # Group by primary arcanum
        by_arcanum = {}
        for legacy_key, legacy_data in legacies.items():
            arcanum = legacy_data.get('primary_arcanum', 'Unknown')
            if arcanum not in by_arcanum:
                by_arcanum[arcanum] = []
            by_arcanum[arcanum].append((legacy_key, legacy_data))
        
        # Display by arcanum
        for arcanum in sorted(by_arcanum.keys()):
            msg += f"|c{arcanum} Legacies:|n\n"
            for legacy_key, legacy_data in sorted(by_arcanum[arcanum], key=lambda x: x[1]['name']):
                name = legacy_data['name']
                desc = legacy_data['description']
                msg += f"  |b{name:<35}|n - {desc}\n"
                msg += f"    |gUse:|n +lookup legacies {legacy_key}\n"
            msg += "\n"
        
        msg += f"|cTotal:|n {len(legacies)} legacies available\n"
        msg += "|cFor legacy details:|n +lookup legacies <legacy_name> (e.g., +lookup legacies chronologue)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_legacy_details(self, legacy_name):
        """Show detailed information about a specific mage legacy."""
        from world.cofd.powers.mage_legacies_detailed import get_legacy
        
        # Normalize legacy name
        legacy_key = legacy_name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
        
        # Get legacy data
        legacy_data = get_legacy(legacy_key)
        
        if not legacy_data:
            self.caller.msg(f"Legacy '{legacy_name}' not found.")
            self.caller.msg("|cUse:|n +lookup legacies - to see all available legacies")
            return
        
        msg = self.format_header(f"{legacy_data['name']} - Mage Legacy")
        msg += "\n\n"
        
        msg += f"|cDescription:|n {legacy_data['description']}\n\n"
        
        msg += f"|cPrimary Arcanum:|n {legacy_data['primary_arcanum']}\n"
        
        if legacy_data.get('conjunctional_arcanum'):
            msg += f"|cConjunctional Arcanum:|n {legacy_data['conjunctional_arcanum']}\n"
        
        if legacy_data.get('optional_arcanum'):
            msg += f"|cOptional Arcanum:|n {legacy_data['optional_arcanum']}\n"
        
        if legacy_data.get('path'):
            msg += f"|cAssociated Path(s):|n {legacy_data['path']}\n"
        
        if legacy_data.get('order'):
            msg += f"|cAssociated Order(s):|n {legacy_data['order']}\n"
        
        msg += f"\n|cSource:|n {legacy_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat legacy={legacy_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_template_details(self, template_name):
        """Show detailed information about a specific character template."""
        template_key = template_name.lower().replace(" ", "_").replace("+", "_plus")
        
        templates = ["mortal", "mortal_plus", "vampire", "mage", "werewolf", "changeling", 
                    "demon", "geist", "promethean", "hunter", "mummy", "deviant"]
        
        if template_key not in templates:
            self.caller.msg(f"Template '{template_name}' not found.")
            self.caller.msg("|cUse:|n +lookup templates - to see all available templates")
            return
        
        desc = get_template_description(template_key)
        msg = self.format_header(f"{template_key.replace('_', ' ').title()} - Character Template")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat template={template_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_auspice_details(self, auspice_name):
        """Show detailed information about a specific werewolf auspice."""
        from world.cofd.powers.werewolf_auspices import get_auspice
        
        auspice_key = auspice_name.lower().replace(" ", "_")
        
        # Get detailed auspice data
        auspice_data = get_auspice(auspice_key)
        
        if not auspice_data:
            self.caller.msg(f"Auspice '{auspice_name}' not found.")
            self.caller.msg("|cUse:|n +lookup auspices - to see all available auspices")
            return
        
        msg = self.format_header(f"{auspice_data['name']} - Werewolf Auspice")
        msg += "\n\n"
        
        msg += f"|cMoon Phase:|n {auspice_data['moon_phase']}\n"
        msg += f"|cHunt Role:|n {auspice_data['hunt_role']}\n"
        msg += f"|cPrimary Renown:|n {auspice_data['primary_renown']}\n"
        msg += f"|cAuspice Skills:|n {', '.join(auspice_data['auspice_skills'])}\n"
        msg += f"|cAuspice Gifts:|n {', '.join(auspice_data['auspice_gifts'])}\n"
        msg += f"|cDescription:|n {auspice_data['description']}\n\n"
        
        msg += f"|wHunter's Aspect:|n {auspice_data['hunters_aspect']}\n\n"
        
        benefit = auspice_data['auspice_benefit']
        msg += f"|wAuspice Benefit: {benefit['name']}|n\n"
        msg += f"{benefit['description']}\n"
        msg += f"|cFrequency:|n {benefit['frequency']}\n\n"
        
        msg += f"|cSource:|n {auspice_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat auspice={auspice_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_tribe_details(self, tribe_name):
        """Show detailed information about a specific werewolf tribe."""
        from world.cofd.powers.werewolf_tribes import get_tribe
        
        tribe_key = tribe_name.lower().replace(" ", "_")
        
        # Get detailed tribe data
        tribe_data = get_tribe(tribe_key)
        
        if not tribe_data:
            self.caller.msg(f"Tribe '{tribe_name}' not found.")
            self.caller.msg("|cUse:|n +lookup tribes - to see all available tribes")
            return
        
        msg = self.format_header(f"{tribe_data['name']} - Werewolf Tribe")
        msg += "\n\n"
        
        msg += f"|cFirst Tongue:|n {tribe_data['first_tongue']}\n"
        msg += f"|cHunt Focus:|n {tribe_data['hunt_focus']}\n"
        msg += f"|cPrimary Renown:|n {tribe_data['primary_renown']}\n"
        
        if tribe_data.get('secondary_renown'):
            msg += f"|cSecondary Renown:|n {tribe_data['secondary_renown']}\n"
        
        if tribe_data.get('tribal_gifts'):
            msg += f"|cTribal Gifts:|n {', '.join(tribe_data['tribal_gifts'])}\n"
        
        msg += f"|cDescription:|n {tribe_data['description']}\n\n"
        
        if tribe_data.get('tribal_oath') and tribe_data['tribal_oath'] != "None":
            msg += f"|wTribal Oath Obligation:|n\n{tribe_data['tribal_oath']}\n\n"
        
        msg += f"|cSource:|n {tribe_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat tribe={tribe_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_seeming_details(self, seeming_name):
        """Show detailed information about a specific changeling seeming."""
        from world.cofd.powers.changeling_seemings import get_seeming
        
        seeming_key = seeming_name.lower().replace(" ", "_")
        
        # Get detailed seeming data
        seeming_data = get_seeming(seeming_key)
        
        if not seeming_data:
            self.caller.msg(f"Seeming '{seeming_name}' not found.")
            self.caller.msg("|cUse:|n +lookup seemings - to see all available seemings")
            return
        
        msg = self.format_header(f"{seeming_data['name']} - Changeling Seeming")
        msg += "\n\n"
        
        msg += f"|cRegalia:|n {seeming_data['regalia']}\n"
        msg += f"|cBonus Attribute:|n {seeming_data['bonus_attribute']}\n"
        msg += f"|cDescription:|n {seeming_data['description']}\n\n"
        
        msg += f"|wSeeming Blessing:|n\n{seeming_data['blessing']}\n\n"
        msg += f"|rSeeming Curse:|n\n{seeming_data['curse']}\n\n"
        
        msg += f"|cSource:|n {seeming_data['book']}\n"
        msg += f"|cSet on Character:|n |y+stat seeming={seeming_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_court_details(self, court_name):
        """Show detailed information about a specific changeling court."""
        court_key = court_name.lower().replace(" ", "_")
        
        court_descriptions = {
            "spring": "The Emerald Court of desire and new beginnings",
            "summer": "The Crimson Court of wrath and iron resolve",
            "autumn": "The Leaden Court of fear and sorcerous power",
            "winter": "The Onyx Court of sorrow and cold logic",
            "courtless": "Independent changelings who reject court politics"
        }
        
        if court_key not in LOOKUP_DATA.changeling_data['courts']:
            self.caller.msg(f"Court '{court_name}' not found.")
            self.caller.msg("|cUse:|n +lookup courts - to see all available courts")
            return
        
        desc = court_descriptions.get(court_key, "Changeling court")
        msg = self.format_header(f"{court_key.title()} - Changeling Court")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat court={court_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_incarnation_details(self, incarnation_name):
        """Show detailed information about a specific demon incarnation."""
        incarnation_key = incarnation_name.lower().replace(" ", "_")
        
        incarnation_descriptions = {
            "destroyer": "Angels of destruction and apocalypse",
            "guardian": "Angels of protection and defense",
            "messenger": "Angels of communication and knowledge",
            "psychopomp": "Angels of death and transition"
        }
        
        if incarnation_key not in LOOKUP_DATA.demon_data['incarnations']:
            self.caller.msg(f"Incarnation '{incarnation_name}' not found.")
            self.caller.msg("|cUse:|n +lookup incarnations - to see all available incarnations")
            return
        
        desc = incarnation_descriptions.get(incarnation_key, "Demon incarnation")
        msg = self.format_header(f"{incarnation_key.title()} - Demon Incarnation")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat incarnation={incarnation_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_agenda_details(self, agenda_name):
        """Show detailed information about a specific demon agenda."""
        agenda_key = agenda_name.lower().replace(" ", "_")
        
        agenda_descriptions = {
            "inquisitor": "Seeking to understand the God-Machine",
            "integrator": "Attempting to live among humans",
            "saboteur": "Working to destroy the God-Machine",
            "tempter": "Corrupting humans for their own ends"
        }
        
        if agenda_key not in LOOKUP_DATA.demon_data['agendas']:
            self.caller.msg(f"Agenda '{agenda_name}' not found.")
            self.caller.msg("|cUse:|n +lookup agendas - to see all available agendas")
            return
        
        desc = agenda_descriptions.get(agenda_key, "Demon agenda")
        msg = self.format_header(f"{agenda_key.title()} - Demon Agenda")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat agenda={agenda_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_embed_details(self, embed_name):
        """Show detailed information about a specific demon embed."""
        embed_key = embed_name.lower().replace(" ", "_")
        
        # Get embed data
        embed_data = LOOKUP_DATA.demon_data['embeds'].get(embed_key)
        
        if not embed_data:
            self.caller.msg(f"Embed '{embed_name}' not found.")
            self.caller.msg("|cUse:|n +lookup embeds - to see all available embeds")
            return
        
        # Determine incarnation
        incarnation = "Unknown"
        if embed_key in LOOKUP_DATA.demon_data['embeds_cacophony']:
            incarnation = "Destroyer (Cacophony)"
        elif embed_key in LOOKUP_DATA.demon_data['embeds_instrumental']:
            incarnation = "Guardian (Instrumental)"
        elif embed_key in LOOKUP_DATA.demon_data['embeds_mundane']:
            incarnation = "Psychopomp (Mundane)"
        elif embed_key in LOOKUP_DATA.demon_data['embeds_vocal']:
            incarnation = "Messenger (Vocal)"
        
        msg = self.format_header(f"{embed_data['name']} - Demon Embed")
        msg += "\n\n"
        msg += f"|cIncarnation:|n {incarnation}\n"
        msg += f"|cDice Pool:|n {embed_data.get('pool', 'None')}\n"
        msg += f"|cDescription:|n {embed_data.get('description', 'Intrinsic demonic power')}\n"
        msg += f"|cSource:|n {embed_data.get('source', 'Unknown')}\n"
        msg += f"\n|gSet on Character:|n |y+stat embed={embed_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_exploit_details(self, exploit_name):
        """Show detailed information about a specific demon exploit."""
        exploit_key = exploit_name.lower().replace(" ", "_")
        
        # Get exploit data
        exploit_data = LOOKUP_DATA.demon_data['exploits'].get(exploit_key)
        
        if not exploit_data:
            self.caller.msg(f"Exploit '{exploit_name}' not found.")
            self.caller.msg("|cUse:|n +lookup exploits - to see all available exploits")
            return
        
        msg = self.format_header(f"{exploit_data['name']} - Demon Exploit")
        msg += "\n\n"
        msg += f"|cCost:|n {exploit_data.get('cost', 'Varies')} Aether\n"
        msg += f"|cDice Pool:|n {exploit_data.get('pool', 'None')}\n"
        
        if exploit_data.get('prerequisite'):
            msg += f"|cPrerequisite:|n {exploit_data['prerequisite']}\n"
        
        msg += f"|cDescription:|n {exploit_data.get('description', 'Learned demonic power that manipulates reality.')}\n"
        msg += f"|cSource:|n {exploit_data.get('source', 'Unknown')}\n"
        msg += f"\n|gSet on Character:|n |y+stat exploit={exploit_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_demon_modifications(self):
        """Show all demon modifications."""
        msg = self.format_header("Demon Modifications")
        msg += "\n\n"
        msg += "|cModifications are permanent alterations to the demonic form:|n\n"
        msg += "|cAt Character Creation:|n Choose 3 modifications\n\n"
        
        modifications = sorted(LOOKUP_DATA.demon_data['modifications'].keys())
        
        # Display in columns
        col_width = 25
        for i in range(0, len(modifications), 3):
            row = modifications[i:i+3]
            msg += "  " + "".join([f"|c{m.replace('_', ' ').title():<{col_width}}|n" for m in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(modifications)} Modifications\n"
        msg += f"\n|cNote:|n Set with: |y+stat/demon modification=<name>|n"
        msg += f"\n|cExample:|n |y+stat/demon modification=armored_plates|n"
        msg += f"\n|cFor details:|n |y+lookup modifications <name>|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_demon_modification_details(self, modification_name):
        """Show detailed information about a specific demon modification."""
        modification_key = modification_name.lower().replace(" ", "_")
        
        # Get modification data
        modification_data = LOOKUP_DATA.demon_data['modifications'].get(modification_key)
        
        if not modification_data:
            self.caller.msg(f"Modification '{modification_name}' not found.")
            self.caller.msg("|cUse:|n +lookup modifications - to see all available modifications")
            return
        
        msg = self.format_header(f"{modification_data['name']} - Demon Modification")
        msg += "\n\n"
        msg += f"|cType:|n Permanent Alteration\n"
        msg += f"|cAppearance:|n {modification_data.get('appearance', 'Physical change to demonic form')}\n"
        msg += f"|cSystem:|n {modification_data.get('system', 'See book for details')}\n"
        msg += f"|cSource:|n {modification_data.get('source', 'Unknown')}\n"
        msg += f"\n|gSet on Character:|n |y+stat/demon modification={modification_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_demon_technologies(self):
        """Show all demon technologies."""
        msg = self.format_header("Demon Technologies")
        msg += "\n\n"
        msg += "|cTechnologies are activated abilities in demonic form:|n\n"
        msg += "|cAt Character Creation:|n Choose 2 technologies\n\n"
        
        technologies = sorted(LOOKUP_DATA.demon_data['technologies'].keys())
        
        # Display in columns
        col_width = 25
        for i in range(0, len(technologies), 3):
            row = technologies[i:i+3]
            msg += "  " + "".join([f"|y{t.replace('_', ' ').title():<{col_width}}|n" for t in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(technologies)} Technologies\n"
        msg += f"\n|cNote:|n Set with: |y+stat/demon technology=<name>|n"
        msg += f"\n|cExample:|n |y+stat/demon technology=electric_jolt|n"
        msg += f"\n|cFor details:|n |y+lookup technologies <name>|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_demon_technology_details(self, technology_name):
        """Show detailed information about a specific demon technology."""
        technology_key = technology_name.lower().replace(" ", "_")
        
        # Get technology data
        technology_data = LOOKUP_DATA.demon_data['technologies'].get(technology_key)
        
        if not technology_data:
            self.caller.msg(f"Technology '{technology_name}' not found.")
            self.caller.msg("|cUse:|n +lookup technologies - to see all available technologies")
            return
        
        msg = self.format_header(f"{technology_data['name']} - Demon Technology")
        msg += "\n\n"
        msg += f"|cType:|n Activated Ability\n"
        msg += f"|cAppearance:|n {technology_data.get('appearance', 'Physical feature on demonic form')}\n"
        msg += f"|cSystem:|n {technology_data.get('system', 'See book for details')}\n"
        msg += f"|cSource:|n {technology_data.get('source', 'Unknown')}\n"
        msg += f"\n|gSet on Character:|n |y+stat/demon technology={technology_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_demon_propulsions(self):
        """Show all demon propulsions."""
        msg = self.format_header("Demon Propulsions")
        msg += "\n\n"
        msg += "|cPropulsions are movement abilities for demonic form:|n\n"
        msg += "|cAt Character Creation:|n Choose 1 propulsion\n\n"
        
        propulsions = sorted(LOOKUP_DATA.demon_data['propulsions'].keys())
        
        # Display in columns
        col_width = 25
        for i in range(0, len(propulsions), 3):
            row = propulsions[i:i+3]
            msg += "  " + "".join([f"|g{p.replace('_', ' ').title():<{col_width}}|n" for p in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(propulsions)} Propulsions\n"
        msg += f"\n|cNote:|n Set with: |y+stat/demon propulsion=<name>|n"
        msg += f"\n|cExample:|n |y+stat/demon propulsion=wings|n"
        msg += f"\n|cFor details:|n |y+lookup propulsions <name>|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_demon_propulsion_details(self, propulsion_name):
        """Show detailed information about a specific demon propulsion."""
        propulsion_key = propulsion_name.lower().replace(" ", "_")
        
        # Get propulsion data
        propulsion_data = LOOKUP_DATA.demon_data['propulsions'].get(propulsion_key)
        
        if not propulsion_data:
            self.caller.msg(f"Propulsion '{propulsion_name}' not found.")
            self.caller.msg("|cUse:|n +lookup propulsions - to see all available propulsions")
            return
        
        msg = self.format_header(f"{propulsion_data['name']} - Demon Propulsion")
        msg += "\n\n"
        msg += f"|cType:|n Movement Ability\n"
        msg += f"|cAppearance:|n {propulsion_data.get('appearance', 'Physical feature enabling movement')}\n"
        msg += f"|cSystem:|n {propulsion_data.get('system', 'See book for details')}\n"
        msg += f"|cSource:|n {propulsion_data.get('source', 'Unknown')}\n"
        msg += f"\n|gSet on Character:|n |y+stat/demon propulsion={propulsion_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_demon_processes(self):
        """Show all demon processes."""
        msg = self.format_header("Demon Processes")
        msg += "\n\n"
        msg += "|cProcesses are complex activated abilities for demonic form:|n\n"
        msg += "|cAt Character Creation:|n Choose 1 process\n\n"
        
        processes = sorted(LOOKUP_DATA.demon_data['processes'].keys())
        
        # Display in columns
        col_width = 25
        for i in range(0, len(processes), 3):
            row = processes[i:i+3]
            msg += "  " + "".join([f"|r{p.replace('_', ' ').title():<{col_width}}|n" for p in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(processes)} Processes\n"
        msg += f"\n|cNote:|n Set with: |y+stat/demon process=<name>|n"
        msg += f"\n|cExample:|n |y+stat/demon process=aegis_protocol|n"
        msg += f"\n|cFor details:|n |y+lookup processes <name>|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_demon_process_details(self, process_name):
        """Show detailed information about a specific demon process."""
        process_key = process_name.lower().replace(" ", "_")
        
        # Get process data
        process_data = LOOKUP_DATA.demon_data['processes'].get(process_key)
        
        if not process_data:
            self.caller.msg(f"Process '{process_name}' not found.")
            self.caller.msg("|cUse:|n +lookup processes - to see all available processes")
            return
        
        msg = self.format_header(f"{process_data['name']} - Demon Process")
        msg += "\n\n"
        msg += f"|cType:|n Complex Activated Ability\n"
        msg += f"|cAppearance:|n {process_data.get('appearance', 'Physical feature on demonic form')}\n"
        msg += f"|cSystem:|n {process_data.get('system', 'See book for details')}\n"
        msg += f"|cSource:|n {process_data.get('source', 'Unknown')}\n"
        msg += f"\n|gSet on Character:|n |y+stat/demon process={process_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_transmutation_details(self, transmutation_name):
        """Show detailed information about a specific promethean transmutation."""
        transmutation_key = transmutation_name.lower().replace(" ", "_")
        
        transmutation_descriptions = {
            "alchemicus": "Mastery over matter and transformation",
            "benefice": "Powers of the Throng - cooperative abilities",
            "contamination": "Powers of emotional and social corruption",
            "corporeum": "Physical enhancement and athletic prowess",
            "deception": "Powers of concealment and disguise",
            "disquietism": "Mastery over Disquiet and Flux",
            "electrification": "Control over electricity and lightning",
            "flux": "Dark powers of the Wasteland (dangerous)",
            "luciferus": "Powers of radiance and inspiration",
            "metamorphosis": "Shapeshifting and physical transformation",
            "mesmerism": "Powers of emotional manipulation",
            "saturninus": "Powers of Azothic memory and Pyros",
            "sensorium": "Enhanced senses and perception",
            "spiritus": "Powers against supernatural threats",
            "vitality": "Powers of endurance and strength",
            "vulcanus": "Powers of the Divine Fire"
        }
        
        if transmutation_key not in LOOKUP_DATA.promethean_data['transmutations']:
            self.caller.msg(f"Transmutation '{transmutation_name}' not found.")
            self.caller.msg("|cUse:|n +lookup transmutations - to see all available transmutations")
            return
        
        desc = transmutation_descriptions.get(transmutation_key, "Promethean supernatural power")
        msg = self.format_header(f"{transmutation_key.title()} - Promethean Transmutation")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cView Alembics:|n Use |y+lookup alembics|n to see individual powers\n"
        msg += f"|cSet on Character:|n |y+stat {transmutation_key}=<1-5>|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_bestowment_details(self, bestowment_name):
        """Show detailed information about a specific promethean bestowment."""
        bestowment_key = bestowment_name.lower().replace(" ", "_")
        
        if bestowment_key not in [b.lower().replace(" ", "_") for b in LOOKUP_DATA.promethean_data['bestowments']]:
            self.caller.msg(f"Bestowment '{bestowment_name}' not found.")
            self.caller.msg("|cUse:|n +lookup bestowments - to see all available bestowments")
            return
        
        msg = self.format_header(f"{bestowment_key.replace('_', ' ').title()} - Promethean Bestowment")
        msg += "\n\n"
        msg += f"|cDescription:|n Unique gift tied to your Lineage.\n"
        msg += f"|cSet on Character:|n |y+stat bestowment={bestowment_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_lineage_details(self, lineage_name):
        """Show detailed information about a specific promethean lineage."""
        lineage_key = lineage_name.lower().replace(" ", "_")
        
        lineage_descriptions = {
            "frankenstein": "Created from corpses, the Wretched, driven by loneliness",
            "galatea": "Sculpted from unblemished forms, the Muses, seekers of beauty",
            "osiris": "Assembled from disparate parts, the Redeemed, guardians of the dead",
            "tammuz": "Formed from clay or earth, the Golem, seeking purpose",
            "ulgan": "Crafted from the remains of shamans, the Pilgrims, spiritual travelers",
            "extempore": "Spontaneously created Prometheans, rare and unpredictable",
            "unfleshed": "Prometheans without physical form, ethereal and strange",
            "zeka": "Created from metal and machine parts, the Manufactured"
        }
        
        if lineage_key not in LOOKUP_DATA.promethean_data['lineages']:
            self.caller.msg(f"Lineage '{lineage_name}' not found.")
            self.caller.msg("|cUse:|n +lookup lineages - to see all available lineages")
            return
        
        desc = lineage_descriptions.get(lineage_key, "Promethean lineage")
        msg = self.format_header(f"{lineage_key.title()} - Promethean Lineage")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat lineage={lineage_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_athanor_details(self, athanor_name):
        """Show detailed information about a specific promethean athanor."""
        athanor_key = athanor_name.lower().replace(" ", "_")
        
        # Search through all lineages for this athanor
        found = False
        for lineage, athanors in LOOKUP_DATA.promethean_data['athanors'].items():
            if athanor_key in athanors:
                found = True
                msg = self.format_header(f"{athanor_key.replace('_', ' ').title()} - Promethean Athanor")
        msg += "\n\n"
        msg += f"|cLineage:|n {lineage.title()}\n"
        msg += f"|cDescription:|n The spiritual engine that drives your Pilgrimage.\n"
        msg += f"|cSet on Character:|n |y+stat athanor={athanor_key}|n (requires {lineage.title()} lineage)\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_guild_details(self, guild_name):
        """Show detailed information about a specific mummy guild."""
        guild_key = guild_name.lower().replace(" ", "_").replace("-", "_")
        
        guild_descriptions = {
            "mesen_nebu": "The Watchers, prophets and scholars who preserve knowledge",
            "sesha_hebsu": "The Scribes, ritualists and spellcasters who wield utterances",
            "su_menent": "The Shepherds, leaders and guides who protect the living",
            "tef_aabhi": "The Judges, warriors and executioners who enforce ma'at",
            "amenti": "Independent mummies with no guild affiliation"
        }
        
        if guild_key not in LOOKUP_DATA.mummy_data['guilds']:
            self.caller.msg(f"Guild '{guild_name}' not found.")
            self.caller.msg("|cUse:|n +lookup guilds - to see all available guilds")
            return
        
        desc = guild_descriptions.get(guild_key, "Mummy guild")
        msg = self.format_header(f"{guild_key.replace('_', '-').title()} - Mummy Guild")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat guild={guild_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_decree_details(self, decree_name):
        """Show detailed information about a specific mummy decree."""
        decree_key = decree_name.lower().replace(" ", "_")
        
        decree_descriptions = {
            "balance": "Maintain ma'at and cosmic equilibrium",
            "fortune": "Bring prosperity and good fortune to the cult",
            "knowledge": "Preserve and protect ancient wisdom",
            "protection": "Shield the cult from supernatural threats",
            "vengeance": "Strike down enemies of the Judges"
        }
        
        if decree_key not in LOOKUP_DATA.mummy_data['decrees']:
            self.caller.msg(f"Decree '{decree_name}' not found.")
            self.caller.msg("|cUse:|n +lookup decrees - to see all available decrees")
            return
        
        desc = decree_descriptions.get(decree_key, "Mummy decree")
        msg = self.format_header(f"{decree_key.title()} - Mummy Decree")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat decree={decree_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_judge_details(self, judge_name):
        """Show detailed information about a specific mummy judge."""
        judge_key = judge_name.lower().replace(" ", "_")
        
        judge_descriptions = {
            "djehuty": "The Ibis-Headed, god of wisdom and magic (Thoth)",
            "duamutef": "The Jackal-Headed, son of Horus, protector of the stomach",
            "hapi": "The Baboon-Headed, son of Horus, protector of the lungs",
            "imsety": "The Human-Headed, son of Horus, protector of the liver",
            "kebehsenuf": "The Falcon-Headed, son of Horus, protector of intestines",
            "nehebkau": "The Serpent, primordial guardian of the gates",
            "neith": "The Weaver, goddess of war and wisdom",
            "ptah": "The Craftsman, god of creation and artisans",
            "sobek": "The Crocodile, god of the Nile and military prowess"
        }
        
        if judge_key not in LOOKUP_DATA.mummy_data['judges']:
            self.caller.msg(f"Judge '{judge_name}' not found.")
            self.caller.msg("|cUse:|n +lookup judges - to see all available judges")
            return
        
        desc = judge_descriptions.get(judge_key, "Mummy judge")
        msg = self.format_header(f"{judge_key.title()} - Mummy Judge")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat judge={judge_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_utterance_details(self, utterance_name):
        """Show detailed information about a specific mummy utterance."""
        utterance_key = utterance_name.lower().replace(" ", "_")
        
        utterance_descriptions = {
            "afire": "Powers of flame and destruction",
            "bone": "Powers over death and the dead",
            "elements": "Control over the natural elements",
            "flesh": "Mastery of the body and healing",
            "guidance": "Insight and foresight",
            "glory": "Commanding presence and authority",
            "reign": "Leadership and dominion",
            "vision": "Enhanced perception and awareness",
            "word": "Power of command and compulsion"
        }
        
        if utterance_key not in LOOKUP_DATA.mummy_data['utterances']:
            self.caller.msg(f"Utterance '{utterance_name}' not found.")
            self.caller.msg("|cUse:|n +lookup utterances - to see all available utterances")
            return
        
        desc = utterance_descriptions.get(utterance_key, "Mummy utterance")
        msg = self.format_header(f"{utterance_key.title()} - Mummy Utterance")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat utterance={utterance_key}|n (rated 1-5 dots)\n"
        
        self.caller.msg(msg)
    
    def show_affinity_details(self, affinity_name):
        """Show detailed information about a specific mummy affinity."""
        affinity_key = affinity_name.lower().replace(" ", "_")
        
        affinity_descriptions = {
            "ab": "The heart, seat of emotion and will",
            "ba": "The personality and individuality",
            "ka": "The life force and vital essence",
            "khaibit": "The shadow, darker aspects",
            "khat": "The physical body",
            "ren": "The secret name and identity",
            "sahu": "The spiritual body",
            "sekhem": "The power and life energy",
            "sheut": "The shadow-self in the underworld"
        }
        
        if affinity_key not in LOOKUP_DATA.mummy_data['affinities']:
            self.caller.msg(f"Affinity '{affinity_name}' not found.")
            self.caller.msg("|cUse:|n +lookup affinities - to see all available affinities")
            return
        
        desc = affinity_descriptions.get(affinity_key, "Mummy affinity")
        msg = self.format_header(f"{affinity_key.title()} - Mummy Affinity")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat affinity={affinity_key}|n (rated 1-5 dots)\n"
        
        self.caller.msg(msg)
    
    def show_burden_details(self, burden_name):
        """Show detailed information about a specific geist burden."""
        burden_key = burden_name.lower().replace(" ", "_")
        
        burden_descriptions = {
            "abiding": "Died lingering, unable to let go",
            "bereaved": "Died mourning, with unfinished grief",
            "hungry": "Died starving or craving",
            "kindly": "Died peacefully, accepting death",
            "vengeful": "Died angry, with unfinished business"
        }
        
        if burden_key not in LOOKUP_DATA.geist_data['burdens']:
            self.caller.msg(f"Burden '{burden_name}' not found.")
            self.caller.msg("|cUse:|n +lookup burdens - to see all available burdens")
            return
        
        desc = burden_descriptions.get(burden_key, "Geist burden")
        msg = self.format_header(f"{burden_key.title()} - Geist Burden")
        msg += "\n\n"
        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat burden={burden_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_krewe_details(self, krewe_name):
        """Show detailed information about a specific geist krewe type."""
        krewe_key = krewe_name.lower().replace(" ", "_")
        
        krewe_descriptions = {
            "family": "Close-knit group bound by personal ties",
            "industrial": "Organized like a corporation or business",
            "network": "Loose association of independent agents",
            "military": "Hierarchical command structure",
            "academic": "Focused on research and knowledge"
        }
        
        if krewe_key not in LOOKUP_DATA.geist_data['krewe_types']:
            self.caller.msg(f"Krewe type '{krewe_name}' not found.")
            self.caller.msg("|cUse:|n +lookup krewe - to see all available krewe types")
            return
        
        desc = krewe_descriptions.get(krewe_key, "Krewe type")
        msg = self.format_header(f"{krewe_key.title()} - Geist Krewe Type")
        msg += "\n\n"

        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat krewe_type={krewe_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_ceremony_details(self, ceremony_name):
        """Show detailed information about a specific geist ceremony."""
        ceremony_key = ceremony_name.lower().replace(" ", "_")
        
        if ceremony_key not in LOOKUP_DATA.geist_data['ceremonies']:
            self.caller.msg(f"Ceremony '{ceremony_name}' not found.")
            self.caller.msg("|cUse:|n +lookup ceremonies - to see all available ceremonies")
            return
        
        msg = self.format_header(f"{ceremony_key.replace('_', ' ').title()} - Geist Ceremony")
        msg += "\n\n"

        msg += f"|cDescription:|n Ritual that Sin-Eaters can perform.\n"
        msg += f"|cSet on Character:|n |y+stat ceremony={ceremony_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_origin_details(self, origin_name):
        """Show detailed information about a specific deviant origin."""
        origin_key = origin_name.lower().replace(" ", "_")
        
        origin_descriptions = {
            "cephalist": "Created by mad scientists and reality hackers",
            "cheiron_group": "Experimented on by the supernatural hunting corporation",
            "government": "Products of black ops and secret military programs",
            "pentex": "Created by the corrupt megacorporation",
            "seers_of_the_throne": "Twisted by servants of the Exarchs",
            "technocracy": "Remade by reality engineers and techno-mages"
        }
        
        if origin_key not in LOOKUP_DATA.deviant_data['origins']:
            self.caller.msg(f"Origin '{origin_name}' not found.")
            self.caller.msg("|cUse:|n +lookup origins - to see all available origins")
            return
        
        desc = origin_descriptions.get(origin_key, "Deviant origin")
        msg = self.format_header(f"{origin_key.replace('_', ' ').title()} - Deviant Origin")
        msg += "\n\n"

        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cSet on Character:|n |y+stat origin={origin_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)
    
    def show_clade_details(self, clade_name):
        """Show detailed information about a specific deviant clade."""
        clade_key = clade_name.lower().replace(" ", "_")
        
        clade_descriptions = {
            "coactive": "Multiple beings merged into one",
            "devoted": "Transformed through sacrifice and dedication",
            "genotypal": "Genetically engineered or mutated",
            "invasive": "Invaded by foreign elements",
            "mutant": "Spontaneously evolved or changed",
            "pelagic": "Transformed by deep and alien forces",
            "remnant": "Rebuilt from death or destruction"
        }
        
        if clade_key not in LOOKUP_DATA.deviant_data['clades']:
            self.caller.msg(f"Clade '{clade_name}' not found.")
            self.caller.msg("|cUse:|n +lookup clades - to see all available clades")
            return
        
        desc = clade_descriptions.get(clade_key, "Deviant clade")
        msg = self.format_header(f"{clade_key.title()} - Deviant Clade")
        msg += "\n\n"

        msg += f"|cDescription:|n {desc}\n"
        msg += f"|cView Variations:|n Use |y+lookup variations|n to see clade-specific powers\n"
        msg += f"|cSet on Character:|n |y+stat clade={clade_key}|n\n\n"
        msg += self.format_footer("Chronicles of Darkness Reference")
        
        self.caller.msg(msg)

