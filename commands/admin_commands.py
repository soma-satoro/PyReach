from evennia.commands.default.muxcommand import MuxCommand

class CmdMigrate(MuxCommand):
    """
    Migrate legacy stats to new format.
    """
    key = "+migrate"
    aliases = ["migrate"]
    help_category = "Admin Commands"
    
    def func(self):
        """
        Migrate legacy stats to new format."""

        if self.args:
            self.migrate_legacy_stats(self.caller.search(self.args.strip(), global_search=True), silent=False)
        else:
            self.migrate_legacy_stats(self.caller, silent=False)

    def migrate_legacy_stats(self, target=None, silent=False):
        """
        Migrate legacy stats from individual attributes to new stats dictionary format.
        Also cleans up old data to prevent database bloat.
        
        Args:
            target: Character object to migrate (if None, uses command args)
            silent: If True, don't send migration messages
            
        Returns:
            bool: True if migration was performed, False if no legacy data found
        """
        # If called as command switch, determine target from args
        if target is None:
            if self.args:
                # Migrating someone else - requires staff
                if not self.caller.check_permstring("Builder"):
                    self.caller.msg("Only staff can migrate stats for other characters.")
                    return False
                
                target = self.caller.search(self.args.strip(), global_search=True)
                if not target:
                    return False
            else:
                # Migrating self
                target = self.caller
        
        migrated_data = {}
        cleaned_attrs = []
        
        # Define all possible legacy attribute names
        legacy_attrs = [
            # Attributes
            "strength", "dexterity", "stamina", "presence", "manipulation", 
            "composure", "intelligence", "wits", "resolve",
            
            # Skills  
            "crafts", "investigation", "medicine", "occult", "politics", "science",
            "athletics", "brawl", "drive", "firearms", "larceny", "stealth", 
            "survival", "weaponry", "animal_ken", "empathy", "expression", 
            "intimidation", "persuasion", "socialize", "streetwise", "subterfuge",
            
            # Advantages
            "health", "willpower", "speed", "defense", "initiative",
            
            # Bio fields (old format)
            "fullname", "full_name", "birthdate", "concept", "virtue", "vice",
            
            # Other common legacy fields
            "integrity", "size", "beats", "experience", "template",
            
            # template-specific bio fields
            "path", "order", "mask", "dirge", "clan", "covenant", "bone", "blood", 
            "auspice", "tribe", "seeming", "court", "kith", "burden", "archetype", 
            "krewe", "lineage", "refinement", "profession", "organization", "creed", 
            "incarnation", "agenda", "agency", "hunger", "family", "inheritance", 
            "origin", "clade", "divergence", "needle", "thread", "legend", "life",
            
            # Anchors
            "anchors",
            
            # Power stats that might be stored individually
            "gnosis", "blood_potency", "primal_urge", "wyrd", "synergy", "azoth", 
            "primum", "satiety", "deviation"
        ]
        
        # Check for legacy data
        has_legacy_data = False
        for attr_name in legacy_attrs:
            if hasattr(target.db, attr_name):
                value = getattr(target.db, attr_name)
                if value is not None:
                    migrated_data[attr_name] = value
                    has_legacy_data = True
        
        # If no legacy data found, return early
        if not has_legacy_data:
            if not silent:
                self.caller.msg(f"No legacy stats found for {target.name}.")
            return False
        
        # Initialize modern stats structure if needed
        if not target.db.stats:
            target.db.stats = {
                "attributes": {},
                "skills": {},
                "advantages": {},
                "anchors": {},
                "bio": {},
                "merits": {},
                "other": {}
            }
        
        # Migrate data to appropriate categories
        attributes = ["strength", "dexterity", "stamina", "presence", "manipulation", 
                     "composure", "intelligence", "wits", "resolve"]
        skills = ["crafts", "investigation", "medicine", "occult", "politics", "science",
                 "athletics", "brawl", "drive", "firearms", "larceny", "stealth", 
                 "survival", "weaponry", "animal_ken", "empathy", "expression", 
                 "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]
        advantages = ["health", "willpower", "speed", "defense", "initiative",
                     "gnosis", "blood_potency", "primal_urge", "wyrd", "synergy", 
                     "azoth", "primum", "satiety", "deviation"]
        bio_fields = ["fullname", "full_name", "birthdate", "concept", "virtue", "vice",
                     "path", "order", "mask", "dirge", "clan", "covenant", "bone", "blood", 
                     "auspice", "tribe", "seeming", "court", "kith", "burden", "archetype", 
                     "krewe", "lineage", "refinement", "profession", "organization", "creed", 
                     "incarnation", "agenda", "agency", "hunger", "family", "inheritance", 
                     "origin", "clade", "divergence", "needle", "thread", "legend", "life"]
        other_fields = ["integrity", "size", "beats", "experience", "template"]
        
        migration_log = []
        
        for attr_name, value in migrated_data.items():
            # Migrate to appropriate category
            if attr_name in attributes:
                target.db.stats["attributes"][attr_name] = value
                migration_log.append(f"Attribute: {attr_name}")
                
            elif attr_name in skills:
                target.db.stats["skills"][attr_name] = value
                migration_log.append(f"Skill: {attr_name}")
                
            elif attr_name in advantages:
                target.db.stats["advantages"][attr_name] = value
                migration_log.append(f"Advantage: {attr_name}")
                
            elif attr_name in bio_fields:
                # Handle fullname variations
                bio_key = "full_name" if attr_name in ["fullname", "full_name"] else attr_name
                target.db.stats["bio"][bio_key] = value
                migration_log.append(f"Bio: {attr_name}")
                
                # Also migrate virtue/vice to anchors for backward compatibility
                if attr_name in ["virtue", "vice"]:
                    target.db.stats["anchors"][attr_name] = value
                    
            elif attr_name in other_fields:
                target.db.stats["other"][attr_name] = value
                migration_log.append(f"Other: {attr_name}")
                
            elif attr_name == "anchors" and isinstance(value, dict):
                # Migrate entire anchors dict
                target.db.stats["anchors"].update(value)
                migration_log.append("Anchors dictionary")
                
            else:
                # Put unknown stats in 'other' category
                target.db.stats["other"][attr_name] = value
                migration_log.append(f"Unknown: {attr_name}")
            
            # Clean up the old attribute
            try:
                delattr(target.db, attr_name)
                cleaned_attrs.append(attr_name)
            except AttributeError:
                pass  # Attribute didn't exist or already deleted
        
        # Clean up other common legacy attributes that might exist
        legacy_cleanup_attrs = [
            # Old character sheet storage methods
            "stats_dict", "character_stats", "stat_data",
            # Old bio storage
            "bio_data", "biography", "char_bio",
            # Old pool tracking
            "current_health", "current_willpower", "temp_willpower",
            # Old derived stats storage
            "derived_stats", "calculated_stats",
            # Old experience tracking
            "xp", "exp_points", "character_xp"
        ]
        
        for cleanup_attr in legacy_cleanup_attrs:
            if hasattr(target.db, cleanup_attr):
                try:
                    delattr(target.db, cleanup_attr)
                    cleaned_attrs.append(cleanup_attr)
                except AttributeError:
                    pass
        
        # Report migration results
        if not silent and migration_log:
            if target == self.caller:
                self.caller.msg(f"|gLegacy stats migration completed!|n")
                self.caller.msg(f"Migrated: {', '.join(migration_log)}")
                if cleaned_attrs:
                    self.caller.msg(f"Cleaned up {len(cleaned_attrs)} old database attributes.")
            else:
                self.caller.msg(f"|gMigrated legacy stats for {target.name}|n")
                self.caller.msg(f"Migrated: {', '.join(migration_log)}")
                if cleaned_attrs:
                    self.caller.msg(f"Cleaned up {len(cleaned_attrs)} old database attributes.")
        
        return True
    
    def mass_migrate_all_characters(self):
        """
        Mass migrate legacy stats for all characters in the database.
        Staff-only command to clean up the entire database.
        """
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can perform mass migration.")
            return
        
        from evennia import search_object
        from typeclasses.characters import Character
        
        # Find all character objects
        all_characters = search_object(typeclass=Character)
        
        if not all_characters:
            self.caller.msg("No characters found in the database.")
            return
        
        migrated_count = 0
        total_count = len(all_characters)
        
        self.caller.msg(f"Starting mass migration for {total_count} characters...")
        self.caller.msg("This may take a moment...")
        
        for char in all_characters:
            try:
                # Try to migrate each character
                was_migrated = self.migrate_legacy_stats(char, silent=True)
                if was_migrated:
                    migrated_count += 1
            except Exception as e:
                self.caller.msg(f"Error migrating {char.name}: {e}")
                continue
        
        # Report results
        self.caller.msg(f"|gMass migration completed!|n")
        self.caller.msg(f"Total characters: {total_count}")
        self.caller.msg(f"Characters migrated: {migrated_count}")
        self.caller.msg(f"Characters with no legacy data: {total_count - migrated_count}")
        
        if migrated_count > 0:
            self.caller.msg(f"|gSuccessfully cleaned up legacy data for {migrated_count} characters.|n")
        else:
            self.caller.msg("No characters had legacy stats to migrate.")