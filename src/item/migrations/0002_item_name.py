# Generated by Django 4.1.1 on 2022-09-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
