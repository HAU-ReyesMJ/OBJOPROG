# Generated by Django 4.1.1 on 2022-11-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0010_alter_item_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="marketplace_pics"
            ),
        ),
    ]
