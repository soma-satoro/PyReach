"""
Mystery investigation handler for characters.

Provides a consistent interface for accessing character's discovered clues,
following the same handler pattern used by ConditionHandler and TiltHandler.
"""


class MysteryHandler:
    """
    Handler for managing a character's mystery clue discoveries.

    Data is stored on character.db.mystery_clues as:
        {mystery_id: [clue_id, clue_id, ...]}

    Clue discovery is performed via Mystery.discover_clue() which updates
    both the mystery script and the character's mystery_clues. This handler
    provides read access and a consistent API for commands.
    """

    def __init__(self, obj):
        """
        Initialize the handler.

        Args:
            obj: The character object (or any object with mystery_clues attribute)
        """
        self.obj = obj

    @property
    def _clues(self):
        """Get the underlying mystery_clues dict, initializing if needed."""
        clues = self.obj.attributes.get('mystery_clues', default=None)
        if clues is None:
            self.obj.attributes.add('mystery_clues', {})
            return {}
        return clues or {}

    def get_all(self):
        """
        Get all discovered clues for this character.

        Returns:
            dict: {mystery_id: [clue_id, ...]}
        """
        return dict(self._clues)

    def get_for_mystery(self, mystery_id):
        """
        Get clue IDs discovered by this character for a specific mystery.

        Args:
            mystery_id: The mystery's database ID (int or str)

        Returns:
            list: List of clue_ids the character has discovered
        """
        if mystery_id is None:
            return []
        # Try both int and str keys (storage may use either)
        clues = self._clues.get(mystery_id) or self._clues.get(str(mystery_id))
        return list(clues) if clues else []

    def has_clue(self, mystery_id, clue_id):
        """
        Check if the character has discovered a specific clue.

        Args:
            mystery_id: The mystery's database ID
            clue_id: The clue ID within the mystery

        Returns:
            bool: True if the character has discovered this clue
        """
        return clue_id in self.get_for_mystery(mystery_id)

    def mystery_count(self):
        """
        Get the number of mysteries this character has clues in.

        Returns:
            int: Count of mysteries with at least one discovered clue
        """
        return len([m for m, clues in self._clues.items() if clues])

    def total_clue_count(self):
        """
        Get total number of clues discovered across all mysteries.

        Returns:
            int: Total count of discovered clues
        """
        return sum(len(clues) for clues in self._clues.values())
