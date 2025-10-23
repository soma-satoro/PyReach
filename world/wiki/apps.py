"""
App configuration for the wiki module.
"""

from django.apps import AppConfig


class WikiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'world.wiki'
    label = 'wiki'
    verbose_name = 'Wiki System'

