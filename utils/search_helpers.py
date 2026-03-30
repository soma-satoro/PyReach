"""
Utility functions for searching and validating characters.
"""
from evennia.utils.search import search_object
from typeclasses.characters import Character

def search_character(searcher, search_string, global_search=True, quiet=False):
    """
    Search for a character, ensuring only Character objects are returned.
    
    This function searches globally by default, meaning it will find characters
    anywhere in the game world, not just in the searcher's current location.
    
    IMPORTANT: This function finds characters regardless of whether they are
    currently logged in or offline. Use this for commands that need to access
    character data (like +finger, +stat, +sheet) even when the player is offline.
    
    The search prioritizes:
    1. Exact character name matches
    2. Case-insensitive character name matches
    3. Character alias matches (exact and case-insensitive)
    
    Args:
        searcher (Object): The object performing the search
        search_string (str): The string to search for (name or alias)
        global_search (bool): Whether to search globally (default: True) or just local location
        quiet (bool): Whether to suppress error messages (default: False)
        
    Returns:
        Character or None: The found character object, or None if not found
        
    Note:
        This function does NOT check if the character is online. If you need to
        send messages or notifications, check target.sessions.all() separately.
    """
    # Handle local vs global search
    if not global_search:
        # Local search - only in current location
        if not searcher.location:
            if not quiet:
                searcher.msg("You are not in a location to search locally.")
            return None
        
        # Search in current location only
        candidates = [obj for obj in searcher.location.contents 
                     if isinstance(obj, Character)]
        
        # Try exact match first
        for char in candidates:
            if char.key == search_string:
                return char
        
        # Try case-insensitive match
        for char in candidates:
            if char.key.lower() == search_string.lower():
                return char
        
        # Try alias match
        for char in candidates:
            alias = char.attributes.get('alias')
            if alias and alias.lower() == search_string.lower():
                return char
        
        # Not found locally
        if not quiet:
            searcher.msg(f"Could not find a character named '{search_string}' here.")
        return None
    
    # Global search (default behavior)
    # First try exact match with Character typeclass
    matches = search_object(search_string, typeclass=Character, exact=True)
    
    if matches:
        return matches[0]
        
    # If no exact match, try case-insensitive search
    chars = search_object(search_string, typeclass=Character)
    matching_chars = [char for char in chars if char.key.lower() == search_string.lower()]
    if matching_chars:
        return matching_chars[0]
        
    # If still no match, try alias as last resort
    # First try using the Character's class method if it exists
    if hasattr(Character, 'get_by_alias'):
        target = Character.get_by_alias(search_string.lower())
        if target:
            return target
        
    # Fallback to case-insensitive attribute search as a last resort.
    # NOTE: Evennia's search_object does not support `attribute_value` in all
    # versions, so we avoid passing unsupported kwargs here.
    all_chars = search_object("*", typeclass=Character)
    for char in all_chars:
        if hasattr(char, 'attributes') and char.attributes.has('alias'):
            alias = char.attributes.get('alias')
            if alias and alias.lower() == search_string.lower():
                return char
        
    # If we get here, no valid character was found
    if not quiet:
        searcher.msg(f"Could not find a character named '{search_string}'.")
    return None 