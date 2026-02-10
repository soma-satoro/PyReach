"""
This is the base model file for Chronicles of Darkness, it contains
the base statistics and attributes for all the characters. It includes the following:
- stat: any base statistic (attributes, abilities, merits)
- power: gnosis in mage, blood potency in vampire, wyrd for changeling, etc.
- pool: health levels, glamour, essence, blood points, etc.
- advantage: advantages that are calculated based on certain stats (speed, willpower, initiative, etc.)
- anchor: virtue, vice, thread, root, bloom, etc.
"""

from django.db import models
from evennia.utils.idmapper.models import SharedMemoryModel
from evennia.typeclasses.models import TypedObject
from evennia.objects.models import ObjectDB

# Import template models
from .template_models import TemplateDefinition, TemplatePackage, TemplateUsage

# Equipment Models
class Equipment(SharedMemoryModel):
    """Model for storing equipment information."""
    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=50, choices=[
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('gear', 'Gear'),
        ('vehicle', 'Vehicle'),
    ])
    availability = models.IntegerField(default=1)
    damage = models.IntegerField(null=True, blank=True)
    armor_rating = models.IntegerField(null=True, blank=True)
    defense_modifier = models.IntegerField(default=0)
    speed_modifier = models.IntegerField(default=0)
    initiative_modifier = models.IntegerField(default=0)
    size = models.IntegerField(default=1)
    durability = models.IntegerField(default=1)
    structure = models.IntegerField(default=1)
    cost = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class CharacterEquipment(SharedMemoryModel):
    """Link between characters and their equipment."""
    character = models.ForeignKey('objects.ObjectDB', on_delete=models.CASCADE, related_name='equipment_set')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    equipped = models.BooleanField(default=False)
    condition = models.CharField(max_length=50, default='Good')
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('character', 'equipment')

# Condition Models
class ConditionTemplate(SharedMemoryModel):
    """Template for conditions that can be applied to characters."""
    name = models.CharField(max_length=100, unique=True)
    condition_type = models.CharField(max_length=50, choices=[
        ('persistent', 'Persistent'),
        ('temporary', 'Temporary'),
    ])
    description = models.TextField()
    resolution = models.TextField(blank=True)
    beat_on_resolution = models.BooleanField(default=True)
    effects = models.JSONField(default=dict)
    
    def __str__(self):
        return self.name

class CharacterCondition(SharedMemoryModel):
    """Active conditions on a character."""
    character = models.ForeignKey('objects.ObjectDB', on_delete=models.CASCADE, related_name='conditions_set')
    condition = models.ForeignKey(ConditionTemplate, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('character', 'condition')

# Combat Models
class CombatInstance(SharedMemoryModel):
    """Represents an active combat scene."""
    name = models.CharField(max_length=100)
    location = models.ForeignKey('objects.ObjectDB', on_delete=models.SET_NULL, null=True, related_name='combats')
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    current_turn = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Combat: {self.name}"

class CombatParticipant(SharedMemoryModel):
    """Tracks participants in combat."""
    combat = models.ForeignKey(CombatInstance, on_delete=models.CASCADE, related_name='participants')
    character = models.ForeignKey('objects.ObjectDB', on_delete=models.CASCADE)
    initiative = models.IntegerField(default=0)
    has_acted = models.BooleanField(default=False)
    defense_applied = models.IntegerField(default=0)
    conditions = models.JSONField(default=list)
    
    class Meta:
        unique_together = ('combat', 'character')
        ordering = ['-initiative']

# Investigation Models
class Investigation(SharedMemoryModel):
    """Represents an ongoing investigation."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey('objects.ObjectDB', on_delete=models.SET_NULL, null=True, related_name='investigations_created')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    participants = models.ManyToManyField('objects.ObjectDB', related_name='investigations')
    
    def __str__(self):
        return self.name

class Clue(SharedMemoryModel):
    """Represents a clue in an investigation."""
    investigation = models.ForeignKey(Investigation, on_delete=models.CASCADE, related_name='clues')
    name = models.CharField(max_length=100)
    description = models.TextField()
    discovered_by = models.ForeignKey('objects.ObjectDB', on_delete=models.SET_NULL, null=True)
    discovered_at = models.DateTimeField(auto_now_add=True)
    tags = models.JSONField(default=list)
    elements = models.JSONField(default=list)
    spent_elements = models.JSONField(default=list)
    
    def __str__(self):
        return f"{self.name} ({self.investigation.name})"

# Social Models
class SocialManeuvering(SharedMemoryModel):
    """Tracks social maneuvering between characters."""
    actor = models.ForeignKey('objects.ObjectDB', on_delete=models.CASCADE, related_name='social_maneuvers_initiated')
    target = models.ForeignKey('objects.ObjectDB', on_delete=models.CASCADE, related_name='social_maneuvers_targeted')
    goal = models.TextField()
    impression_level = models.CharField(max_length=20, choices=[
        ('hostile', 'Hostile'),
        ('average', 'Average'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
        ('perfect', 'Perfect'),
    ], default='average')
    doors = models.IntegerField(default=0)
    doors_opened = models.IntegerField(default=0)
    leverage = models.JSONField(default=list)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('actor', 'target', 'goal')

# Group Models
class Group(SharedMemoryModel):
    """Model for storing in-game group information."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    group_type = models.CharField(max_length=50, choices=[
        ('sphere', 'Sphere'),
        ('coterie', 'Coterie'),
        ('pack', 'Pack'),
        ('cabal', 'Cabal'),
        ('motley', 'Motley'),
        ('conspiracy', 'Conspiracy'),
        ('agency', 'Agency'),
        ('cult', 'Cult'),
        ('other', 'Other'),
    ], default='other')
    leader = models.ForeignKey('objects.ObjectDB', on_delete=models.SET_NULL, null=True, related_name='led_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    group_id = models.PositiveIntegerField(unique=True, null=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Override save to handle group ID assignment."""
        if self.group_id is None:
            used_ids = list(Group.objects.exclude(id=self.id).values_list('group_id', flat=True))
            used_ids = [id for id in used_ids if id is not None]
            
            if used_ids:
                all_ids = set(range(1, max(used_ids) + 2))
                available_ids = all_ids - set(used_ids)
                if available_ids:
                    self.group_id = min(available_ids)
            else:
                self.group_id = 1
        
        super().save(*args, **kwargs)
    
    @property
    def channel_name(self):
        """Returns the channel name for this group."""
        return ''.join(c for c in self.name if c.isalnum())

class GroupRole(SharedMemoryModel):
    """Roles within a group."""
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='roles')
    can_invite = models.BooleanField(default=False)
    can_kick = models.BooleanField(default=False)
    can_promote = models.BooleanField(default=False)
    can_edit_info = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.group.name}"

class GroupMembership(SharedMemoryModel):
    """Membership in a group."""
    character = models.ForeignKey('objects.ObjectDB', on_delete=models.CASCADE, related_name='group_memberships')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members')
    role = models.ForeignKey(GroupRole, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('character', 'group')
    
    def __str__(self):
        return f"{self.character.name} - {self.group.name}"
