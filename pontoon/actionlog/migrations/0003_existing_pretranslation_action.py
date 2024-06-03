# Generated by Django 3.2.15 on 2023-01-24 10:40

from django.db import migrations


def create_action_logs_for_pretranslations(apps, schema_editor):
    Translation = apps.get_model("base", "Translation")
    ActionLog = apps.get_model("actionlog", "ActionLog")

    translations = Translation.objects.filter(
        user__email__in=["pontoon-sync@example.com", "pontoon-tm@example.com"]
    )

    actions_to_log = [
        ActionLog(
            action_type="translation:created",
            performed_by=t.user,
            translation=t,
            created_at=t.date,
        )
        for t in translations
    ]

    ActionLog.objects.bulk_create(actions_to_log)


def delete_action_logs_for_pretranslations(apps, schema_editor):
    ActionLog = apps.get_model("actionlog", "ActionLog")

    ActionLog.objects.filter(
        translation__user__email__in=[
            "pontoon-sync@example.com",
            "pontoon-tm@example.com",
        ],
        action_type="translation:created",
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("actionlog", "0002_auto_20200703_0709"),
    ]

    operations = [
        migrations.RunPython(
            code=create_action_logs_for_pretranslations,
            reverse_code=delete_action_logs_for_pretranslations,
        ),
    ]
