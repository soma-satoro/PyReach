"""Add scene-scoped initiative state storage."""

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("asyncplay", "0003_asyncscene_public_log_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="asyncscene",
            name="initiative_state",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
