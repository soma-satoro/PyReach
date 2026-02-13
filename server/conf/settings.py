r"""
Evennia settings file.

The available options are found in the default settings file found
here:

https://www.evennia.com/docs/latest/Setup/Settings-Default.html

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *
from evennia.contrib.base_systems import color_markups

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "PyReach"
# Use the below if you set up a domain with ssl.
# Best suggestion for this is to use letsencrypt. Just change the domain to your own.
# The Evennia site has information on this. https://www.evennia.com/docs/latest/Setup/Websocket.html
WEBSOCKET_CLIENT_URL = "wss://pyreach.com/ws"

# Force 80-character width for help files and formatted output
CLIENT_DEFAULT_WIDTH = 80

# Text formatting settings
# Enable special character substitutions (%r for newlines, %t for tabs)
ENABLE_SPECIAL_CHAR_SUBSTITUTIONS = True

# Define custom substitutions (can be extended by admins)
SPECIAL_CHAR_SUBSTITUTIONS = {
    '%r%r': '\n\n',  # Paragraph break (must be processed first)
    '%r': '\n',      # Newline/carriage return
    '%t': '     ',   # Tab (5 spaces)
}

# Add game_name to all template contexts (for Jobs web UI, etc.)
if "TEMPLATES" in dir() and TEMPLATES:
    for template_config in TEMPLATES:
        if "OPTIONS" in template_config and "context_processors" in template_config["OPTIONS"]:
            template_config["OPTIONS"]["context_processors"].append(
                "web.utils.context_processors.game_info"
            )
            break

# Add your custom apps to the existing INSTALLED_APPS
INSTALLED_APPS += [
    'world.cofd',
    'world.jobs',
    'world.wiki',
]
"""
BASE ANSI MARKUP CONFIGURATION
See below for more specific color markup configurations.

Note that this is not the only place to set %r/%t replacements, as that needs to also be done
within each file that uses the MUX carriage return or tab style.
"""
# Enable both default pipe-based (|r, |n, |b) AND MUX (%cr, %cn, %cb) color systems
COLOR_NO_DEFAULT = False

COLOR_ANSI_EXTRA_MAP = color_markups.MUX_COLOR_ANSI_EXTRA_MAP
COLOR_XTERM256_EXTRA_FG = color_markups.MUX_COLOR_XTERM256_EXTRA_FG
COLOR_XTERM256_EXTRA_BG = color_markups.MUX_COLOR_XTERM256_EXTRA_BG
COLOR_XTERM256_EXTRA_GFG = color_markups.MUX_COLOR_XTERM256_EXTRA_GFG
COLOR_XTERM256_EXTRA_GBG = color_markups.MUX_COLOR_XTERM256_EXTRA_GBG
COLOR_ANSI_XTERM256_BRIGHT_BG_EXTRA_MAP = color_markups.MUX_COLOR_ANSI_XTERM256_BRIGHT_BG_EXTRA_MAP

######################################################################
# Account Creation Settings (for testing)
######################################################################

# Disable account creation throttling for testing purposes
# Set to None to disable, or increase the limit for more accounts
CREATION_THROTTLE_LIMIT = None  # Disable limit (default: 2)
# CREATION_THROTTLE_TIMEOUT = 10 * 60  # 10 minutes (default)

######################################################################
# Account Options
######################################################################

# Extensible options available to players via the @option command
from evennia.settings_default import OPTIONS_ACCOUNT_DEFAULT as _DEFAULT_OPTIONS
OPTIONS_ACCOUNT_DEFAULT = _DEFAULT_OPTIONS.copy()
OPTIONS_ACCOUNT_DEFAULT.update({
    "UNICODE_DOTS": (
        "Display character sheet stats as Unicode dots (●●●○○) instead of numbers",
        "Boolean",  # Option class type
        False       # Default value (numeric display)
    ),
})

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
