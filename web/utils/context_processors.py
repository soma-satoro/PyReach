"""
Custom context processors for adding variables to all templates.
"""

from django.conf import settings


def game_info(request):
    """
    Add game information to all template contexts.
    """
    async_play_url = getattr(settings, "ASYNC_PLAY_PUBLIC_URL", "/async/")
    if not async_play_url:
        async_play_url = "/async/"
    game_name = (
        getattr(settings, "SERVERNAME", None)
        or getattr(settings, "server_name", None)
        or "Evennia"
    )
    return {
        'game_name': game_name,
        'telnet_host': request.get_host().split(':')[0],
        'telnet_port': getattr(settings, 'TELNET_PORTS', [4000])[0] if hasattr(settings, 'TELNET_PORTS') else 4000,
        'async_play_url': async_play_url,
    }

