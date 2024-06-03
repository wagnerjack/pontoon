# Generated by Django 3.2.15 on 2022-11-30 20:32
from django.db import migrations


system_user_emails = [
    "pontoon-sync@example.com",
    "pontoon-gt@example.com",
    "pontoon-tm@example.com",
]


def mark_system_users(apps, schema_editor):
    UserProfile = apps.get_model("base", "UserProfile")
    UserProfile.objects.filter(user__email__in=system_user_emails).update(
        system_user=True
    )


def revert_mark_system_users(apps, schema_editor):
    UserProfile = apps.get_model("base", "UserProfile")
    UserProfile.objects.filter(user__email__in=system_user_emails).update(
        system_user=False
    )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("base", "0038_userprofile_system_user"),
    ]

    operations = [
        migrations.RunPython(
            code=mark_system_users,
            reverse_code=revert_mark_system_users,
        ),
    ]
