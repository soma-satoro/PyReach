"""
Custom website views for PyReach
"""

from django.views.generic import ListView
from evennia.utils.utils import class_from_module


class PublicCharacterListView(ListView):
    """
    Public character list (no login required).
    Only shows characters marked as publicly viewable.
    """
    template_name = "website/character_list.html"
    context_object_name = 'object_list'
    paginate_by = 50
    
    def get_queryset(self):
        """Get all characters"""
        # Get the Character typeclass
        Character = class_from_module("typeclasses.characters.Character")
        
        # Get all character objects
        characters = Character.objects.all()
        
        # Filter to only show approved characters (optional)
        approved_chars = [c for c in characters if getattr(c.db, 'approved', False)]
        
        # If you want to show all characters regardless of approval:
        # return characters.order_by('db_key')
        
        # To show only approved:
        return sorted(approved_chars, key=lambda x: x.db_key.lower()) if approved_chars else []

