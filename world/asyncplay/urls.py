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
    path("api/scenes/", views.api_scene_list, name="api_scene_list"),
    path("api/scenes/locations/", views.api_scene_locations, name="api_scene_locations"),
    path("api/scenes/create/", views.api_scene_create, name="api_scene_create"),
    path("api/scenes/<int:scene_id>/", views.api_scene_detail, name="api_scene_detail"),
    path("api/scenes/<int:scene_id>/join/", views.api_scene_join, name="api_scene_join"),
    path("api/scenes/<int:scene_id>/update/", views.api_scene_update, name="api_scene_update"),
    path("api/scenes/<int:scene_id>/complete/", views.api_scene_complete, name="api_scene_complete"),
    path("api/scenes/<int:scene_id>/reopen/", views.api_scene_reopen, name="api_scene_reopen"),
    path("api/scenes/<int:scene_id>/post/", views.api_scene_post, name="api_scene_post"),
]
