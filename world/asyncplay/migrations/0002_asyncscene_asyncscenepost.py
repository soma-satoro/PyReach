"""Add async scene and scene post models."""

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "__first__"),
        ("asyncplay", "0001_initial"),
        ("objects", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="AsyncScene",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=140)),
                ("notes", models.TextField(blank=True)),
                ("location", models.CharField(blank=True, max_length=140)),
                ("ic_date", models.DateField(default=django.utils.timezone.localdate)),
                (
                    "scene_type",
                    models.CharField(
                        choices=[("social", "Social"), ("event", "Event"), ("vignette", "Vignette")],
                        default="social",
                        max_length=20,
                    ),
                ),
                (
                    "pacing",
                    models.CharField(
                        choices=[
                            ("traditional", "Traditional"),
                            ("distracted", "Distracted"),
                            ("asynchronous", "Asynchronous"),
                        ],
                        default="traditional",
                        max_length=20,
                    ),
                ),
                (
                    "privacy",
                    models.CharField(
                        choices=[("private", "Private"), ("open", "Open")],
                        default="private",
                        max_length=20,
                    ),
                ),
                ("is_completed", models.BooleanField(default=False)),
                ("plot", models.CharField(blank=True, max_length=140)),
                ("tags", models.CharField(blank=True, max_length=240)),
                ("summary", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("last_activity_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_async_scenes",
                        to="accounts.accountdb",
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(blank=True, related_name="async_scenes", to="objects.objectdb"),
                ),
                ("related_scenes", models.ManyToManyField(blank=True, symmetrical=False, to="asyncplay.asyncscene")),
            ],
            options={
                "ordering": ["-last_activity_at", "-created_at"],
            },
        ),
        migrations.CreateModel(
            name="AsyncScenePost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "post_type",
                    models.CharField(
                        choices=[
                            ("pose", "Pose"),
                            ("ooc", "OOC"),
                            ("gm_emit", "GM Emit"),
                            ("scene_set", "Scene Set"),
                        ],
                        default="pose",
                        max_length=20,
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="async_scene_posts",
                        to="accounts.accountdb",
                    ),
                ),
                (
                    "character",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="async_scene_posts",
                        to="objects.objectdb",
                    ),
                ),
                (
                    "scene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="asyncplay.asyncscene",
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
    ]
