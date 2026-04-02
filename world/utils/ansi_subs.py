"""
ANSI substitution compatibility helpers.

Some Evennia versions expose `ANSI_REPLACEMENTS` while others do not.
This module should never crash command imports; it applies replacements
only when the target mapping is available.
"""

try:
    from evennia.utils.ansi import ANSI_REPLACEMENTS  # type: ignore
except Exception:
    ANSI_REPLACEMENTS = None


def _apply_substitutions():
    """Apply custom replacements when Evennia exposes a mutable mapping."""
    if ANSI_REPLACEMENTS and hasattr(ANSI_REPLACEMENTS, "update"):
        ANSI_REPLACEMENTS.update({
            "|r": "\n",  # Carriage return (newline)
            "|t": "\t",  # Tab
        })


_apply_substitutions()
