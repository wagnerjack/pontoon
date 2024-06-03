# Generated by Django 3.2.4 on 2021-11-29 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("insights", "0006_projectlocale_insights_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="localeinsightssnapshot",
            name="time_to_review_suggestions",
            field=models.DurationField(default=datetime.timedelta),
        ),
        migrations.AddField(
            model_name="projectinsightssnapshot",
            name="time_to_review_suggestions",
            field=models.DurationField(default=datetime.timedelta),
        ),
        migrations.AddField(
            model_name="projectlocaleinsightssnapshot",
            name="time_to_review_suggestions",
            field=models.DurationField(default=datetime.timedelta),
        ),
    ]
