# Generated by Django 4.1.3 on 2022-11-06 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0014_alter_profile_image"),
        ("item", "0011_item_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="seller",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="seller",
                to="accounts.profile",
            ),
        ),
    ]
