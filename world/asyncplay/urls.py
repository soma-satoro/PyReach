"""URL routes for asynchronous web play."""

from django.urls import path

from . import views

app_name = "asyncplay"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("api/characters/", views.api_my_characters, name="api_my_characters"),
    path("api/characters/<int:character_id>/sheet/", views.api_character_sheet, name="api_character_sheet"),
    path("api/actions/", views.api_my_actions, name="api_my_actions"),
    path("api/actions/submit/", views.api_submit_action, name="api_submit_action"),
]
