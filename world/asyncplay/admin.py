"""Admin registration for async play actions."""

from django.contrib import admin

from .models import AsyncAction, AsyncScene, AsyncScenePost


@admin.register(AsyncAction)
class AsyncActionAdmin(admin.ModelAdmin):
    """Admin UI for staff to review async submissions."""

    list_display = (
        "id",
        "account",
        "character",
        "title",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("title", "content", "account__username", "character__db_key")


@admin.register(AsyncScene)
class AsyncSceneAdmin(admin.ModelAdmin):
    """Admin UI for async scene management."""

    list_display = (
        "id",
        "title",
        "creator",
        "privacy",
        "scene_type",
        "pacing",
        "is_completed",
        "last_activity_at",
    )
    list_filter = ("privacy", "scene_type", "pacing", "is_completed", "created_at")
    search_fields = ("title", "notes", "summary", "creator__username", "location", "tags")
    filter_horizontal = ("participants", "related_scenes")


@admin.register(AsyncScenePost)
class AsyncScenePostAdmin(admin.ModelAdmin):
    """Admin UI for scene posts."""

    list_display = ("id", "scene", "account", "character", "post_type", "created_at")
    list_filter = ("post_type", "created_at")
    search_fields = ("content", "account__username", "character__db_key", "scene__title")
