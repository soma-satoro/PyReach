"""
Account

The Account represents the game "account" and each login has only one
Account object. An Account is what chats on default channels but has no
other in-game-world existence. Rather the Account puppets Objects (such
as Characters) in order to actually participate in the game world.


Guest

Guest accounts are simple low-level accounts that are created/deleted
on the fly and allows users to test the game without the commitment
of a full registration. Guest accounts are deactivated by default; to
activate them, add the following line to your settings file:

    GUEST_ENABLED = True

You will also need to modify the connection screen to reflect the
possibility to connect with a guest account. The setting file accepts
several more options for customizing the Guest account system.

"""

from evennia.accounts.accounts import DefaultAccount, DefaultGuest
from evennia.accounts.models import AccountDB
from evennia.utils import logger


# Monkey-patch AccountDB to add missing methods that Evennia's shutdown expects
# This fixes AttributeError issues when server tries to shutdown/reload
# These patches are applied at module import time to ensure they're always available

def _accountdb_unpuppet_all(self):
    """
    Disconnect all puppets. Called by server before reset/shutdown.
    This is a compatibility patch for AccountDB instances.
    """
    try:
        # Get the typeclass wrapper and call its method if it exists
        if hasattr(self, 'typeclass'):
            typeclass = self.typeclass
            if hasattr(typeclass, 'unpuppet_all') and callable(typeclass.unpuppet_all):
                return typeclass.unpuppet_all()
            # Fallback: manually unpuppet
            if hasattr(typeclass, 'sessions') and hasattr(typeclass, 'unpuppet_object'):
                sessions = typeclass.sessions.all()
                if sessions:
                    typeclass.unpuppet_object(sessions)
    except Exception as e:
        logger.log_err(f"Error in AccountDB.unpuppet_all() for account {self.id}: {e}")


def _accountdb_at_server_shutdown(self):
    """
    Called just before server shutdown.
    This is a compatibility patch for AccountDB instances.
    """
    try:
        # Call unpuppet_all if available
        if hasattr(self, 'unpuppet_all'):
            self.unpuppet_all()
        # Also try the typeclass version
        elif hasattr(self, 'typeclass'):
            typeclass = self.typeclass
            if hasattr(typeclass, 'at_server_shutdown') and callable(typeclass.at_server_shutdown):
                typeclass.at_server_shutdown()
    except Exception as e:
        logger.log_err(f"Error in AccountDB.at_server_shutdown() for account {self.id}: {e}")


def _accountdb_at_server_reload(self):
    """
    Called when server reloads.
    This is a compatibility patch for AccountDB instances.
    """
    try:
        # Get the typeclass wrapper and call its method if it exists
        if hasattr(self, 'typeclass'):
            typeclass = self.typeclass
            if hasattr(typeclass, 'at_server_reload') and callable(typeclass.at_server_reload):
                return typeclass.at_server_reload()
    except Exception as e:
        logger.log_err(f"Error in AccountDB.at_server_reload() for account {self.id}: {e}")


# Apply the patches if they don't already exist
if not hasattr(AccountDB, 'unpuppet_all'):
    AccountDB.unpuppet_all = _accountdb_unpuppet_all

if not hasattr(AccountDB, 'at_server_shutdown'):
    AccountDB.at_server_shutdown = _accountdb_at_server_shutdown

if not hasattr(AccountDB, 'at_server_reload'):
    AccountDB.at_server_reload = _accountdb_at_server_reload


class Account(DefaultAccount):
    """
    An Account is the actual OOC player entity. It doesn't exist in the game,
    but puppets characters.

    This is the base Typeclass for all Accounts. Accounts represent
    the person playing the game and tracks account info, password
    etc. They are OOC entities without presence in-game. An Account
    can connect to a Character Object in order to "enter" the
    game.

    Account Typeclass API:

    * Available properties (only available on initiated typeclass objects)

     - key (string) - name of account
     - name (string)- wrapper for user.username
     - aliases (list of strings) - aliases to the object. Will be saved to
            database as AliasDB entries but returned as strings.
     - dbref (int, read-only) - unique #id-number. Also "id" can be used.
     - date_created (string) - time stamp of object creation
     - permissions (list of strings) - list of permission strings
     - user (User, read-only) - django User authorization object
     - obj (Object) - game object controlled by account. 'character' can also
                     be used.
     - is_superuser (bool, read-only) - if the connected user is a superuser

    * Handlers

     - locks - lock-handler: use locks.add() to add new lock strings
     - db - attribute-handler: store/retrieve database attributes on this
                              self.db.myattr=val, val=self.db.myattr
     - ndb - non-persistent attribute handler: same as db but does not
                                  create a database entry when storing data
     - scripts - script-handler. Add new scripts to object with scripts.add()
     - cmdset - cmdset-handler. Use cmdset.add() to add new cmdsets to object
     - nicks - nick-handler. New nicks with nicks.add().
     - sessions - session-handler. Use session.get() to see all sessions connected, if any
     - options - option-handler. Defaults are taken from settings.OPTIONS_ACCOUNT_DEFAULT
     - characters - handler for listing the account's playable characters

    * Helper methods (check autodocs for full updated listing)

     - msg(text=None, from_obj=None, session=None, options=None, **kwargs)
     - execute_cmd(raw_string)
     - search(searchdata, return_puppet=False, search_object=False, typeclass=None,
                      nofound_string=None, multimatch_string=None, use_nicks=True,
                      quiet=False, **kwargs)
     - is_typeclass(typeclass, exact=False)
     - swap_typeclass(new_typeclass, clean_attributes=False, no_default=True)
     - access(accessing_obj, access_type='read', default=False, no_superuser_bypass=False, **kwargs)
     - check_permstring(permstring)
     - get_cmdsets(caller, current, **kwargs)
     - get_cmdset_providers()
     - uses_screenreader(session=None)
     - get_display_name(looker, **kwargs)
     - get_extra_display_name_info(looker, **kwargs)
     - disconnect_session_from_account()
     - puppet_object(session, obj)
     - unpuppet_object(session)
     - unpuppet_all()
     - get_puppet(session)
     - get_all_puppets()
     - is_banned(**kwargs)
     - get_username_validators(validator_config=settings.AUTH_USERNAME_VALIDATORS)
     - authenticate(username, password, ip="", **kwargs)
     - normalize_username(username)
     - validate_username(username)
     - validate_password(password, account=None)
     - set_password(password, **kwargs)
     - get_character_slots()
     - get_available_character_slots()
     - create_character(*args, **kwargs)
     - create(*args, **kwargs)
     - delete(*args, **kwargs)
     - channel_msg(message, channel, senders=None, **kwargs)
     - idle_time()
     - connection_time()

    * Hook methods

     basetype_setup()
     at_account_creation()

     > note that the following hooks are also found on Objects and are
       usually handled on the character level:

     - at_init()
     - at_first_save()
     - at_access()
     - at_cmdset_get(**kwargs)
     - at_password_change(**kwargs)
     - at_first_login()
     - at_pre_login()
     - at_post_login(session=None)
     - at_failed_login(session, **kwargs)
     - at_disconnect(reason=None, **kwargs)
     - at_post_disconnect(**kwargs)
     - at_message_receive()
     - at_message_send()
     - at_server_reload()
     - at_server_shutdown()
     - at_look(target=None, session=None, **kwargs)
     - at_post_create_character(character, **kwargs)
     - at_post_add_character(char)
     - at_post_remove_character(char)
     - at_pre_channel_msg(message, channel, senders=None, **kwargs)
     - at_post_chnnel_msg(message, channel, senders=None, **kwargs)

    """

    def unpuppet_all(self):
        """
        Disconnect all puppets. This is called by server before a
        reset/shutdown.
        
        This method ensures compatibility during server shutdown by
        safely unpuppeting all connected sessions.
        """
        try:
            # Get all sessions and unpuppet them
            if hasattr(self, 'sessions'):
                sessions = self.sessions.all()
                if sessions:
                    self.unpuppet_object(sessions)
        except Exception as e:
            # Log but don't raise - we want shutdown to continue
            from evennia.utils import logger
            logger.log_err(f"Error during unpuppet_all for account {self.id}: {e}")
    
    def at_server_shutdown(self):
        """
        Called just before the server shuts down.
        
        This hook ensures proper cleanup before shutdown.
        """
        try:
            # Make sure all puppets are disconnected
            self.unpuppet_all()
        except Exception as e:
            # Log but don't raise - we want shutdown to continue
            from evennia.utils import logger
            logger.log_err(f"Error during at_server_shutdown for account {self.id}: {e}")
    
    def at_server_reload(self):
        """
        Called when the server reloads.
        
        This hook is called on all connected accounts when the server reloads.
        """
        # Default behavior is to do nothing, but this ensures the method exists
        pass


class Guest(DefaultGuest):
    """
    This class is used for guest logins. Unlike Accounts, Guests and their
    characters are deleted after disconnection.
    """

    def unpuppet_all(self):
        """
        Disconnect all puppets. This is called by server before a
        reset/shutdown.
        
        This method ensures compatibility during server shutdown by
        safely unpuppeting all connected sessions.
        """
        try:
            # Get all sessions and unpuppet them
            if hasattr(self, 'sessions'):
                sessions = self.sessions.all()
                if sessions:
                    self.unpuppet_object(sessions)
        except Exception as e:
            # Log but don't raise - we want shutdown to continue
            from evennia.utils import logger
            logger.log_err(f"Error during unpuppet_all for guest account {self.id}: {e}")
    
    def at_server_shutdown(self):
        """
        Called just before the server shuts down.
        
        This hook ensures proper cleanup before shutdown.
        """
        try:
            # Make sure all puppets are disconnected
            self.unpuppet_all()
        except Exception as e:
            # Log but don't raise - we want shutdown to continue
            from evennia.utils import logger
            logger.log_err(f"Error during at_server_shutdown for guest account {self.id}: {e}")
    
    def at_server_reload(self):
        """
        Called when the server reloads.
        
        This hook is called on all connected accounts when the server reloads.
        """
        # Default behavior is to do nothing, but this ensures the method exists
        pass
