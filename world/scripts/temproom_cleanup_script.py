"""
Temporary room cleanup script.

Destroys expired TempRoom instances that have been inactive for 24 hours.
"""

from evennia.scripts.scripts import DefaultScript
from evennia import create_script, search_object, search_script
from evennia.utils import logger


class TempRoomCleanupScript(DefaultScript):
    """Periodic cleanup worker for temporary rooms."""

    def at_script_creation(self):
        self.key = "temproom_cleanup_script"
        self.desc = "Cleans up expired temporary rooms"
        self.interval = 900  # 15 minutes
        self.persistent = True
        self.start_delay = True

    def at_repeat(self):
        expired = 0
        errored = 0
        temprooms = search_object(typeclass="typeclasses.rooms.TempRoom")

        for room in temprooms:
            try:
                if room.is_expired():
                    room.cleanup_temproom(reason="expired")
                    expired += 1
            except Exception as err:
                errored += 1
                logger.log_err(f"TempRoom cleanup error in #{room.id}: {err}")

        if expired or errored:
            logger.log_info(
                f"TempRoom cleanup run complete: expired={expired}, errors={errored}"
            )


def start_temproom_cleanup_script():
    """Create script if it does not already exist."""
    existing = search_script("temproom_cleanup_script")
    if existing:
        return existing[0]
    return create_script(TempRoomCleanupScript, key="temproom_cleanup_script")

