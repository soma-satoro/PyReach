"""Add public log fields for async scenes."""

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("asyncplay", "0002_asyncscene_asyncscenepost"),
    ]

    operations = [
        migrations.AddField(
            model_name="asyncscene",
            name="is_public_log",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="asyncscene",
            name="wiki_log_slug",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
