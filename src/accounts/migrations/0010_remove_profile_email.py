# Generated by Django 4.1.1 on 2022-10-13 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_profile_avatar_profile_country_profile_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email",
        ),
    ]