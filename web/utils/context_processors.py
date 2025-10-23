"""
Custom context processors for adding variables to all templates.
"""

from django.conf import settings


def game_info(request):
    """
    Add game information to all template contexts.
    """
    return {
        'game_name': getattr(settings, 'SERVERNAME', 'Evennia'),
        'telnet_host': request.get_host().split(':')[0],
        'telnet_port': getattr(settings, 'TELNET_PORTS', [4000])[0] if hasattr(settings, 'TELNET_PORTS') else 4000,
    }

