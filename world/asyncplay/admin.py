"""Admin registration for async play actions."""

from django.contrib import admin

from .models import AsyncAction


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
