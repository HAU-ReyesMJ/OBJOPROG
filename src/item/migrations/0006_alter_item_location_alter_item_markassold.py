# Generated by Django 4.1.1 on 2022-09-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_item_location_item_markassold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='markAsSold',
            field=models.BooleanField(),
        ),
    ]
