# Async Play External URL Notes

The async portal is mounted at `/async/` inside Django/Evennia.

To expose it under a dedicated public URL (for example from MediaWiki):

1. Set `ASYNC_PLAY_PUBLIC_URL` in `server/conf/settings.py` to the public URL.
   - Example: `ASYNC_PLAY_PUBLIC_URL = "https://play.pyreach.com/async/"`
2. Keep the route mounted in `web/urls.py` as `path("async/", include("world.asyncplay.urls"))`.
3. Add a normal hyperlink on MediaWiki to the public URL.

This is a link-out flow only (no MediaWiki integration required).

## Reverse Proxy Pattern

If using Nginx/Caddy/Apache, route public `/async/` traffic to your Evennia web endpoint.
This keeps one auth/session system and avoids cross-origin API complications.
