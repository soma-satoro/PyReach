"""App config for asynchronous play web features."""

from django.apps import AppConfig


class AsyncPlayConfig(AppConfig):
    """Django app configuration for async play."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "world.asyncplay"
    verbose_name = "Async Play"
