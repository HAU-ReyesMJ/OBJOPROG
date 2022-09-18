# Generated by Django 4.1.1 on 2022-09-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.CharField(default='none', max_length=120),
        ),
        migrations.AddField(
            model_name='item',
            name='markAsSold',
            field=models.BooleanField(default='False'),
        ),
    ]