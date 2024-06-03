# Generated by Django 2.2.13 on 2020-07-03 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("actionlog", "0001_squashed_0002_auto_20200123_1843"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actionlog",
            name="performed_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="actions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
