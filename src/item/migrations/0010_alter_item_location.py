# Generated by Django 4.1.1 on 2022-09-18 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_alter_item_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]
