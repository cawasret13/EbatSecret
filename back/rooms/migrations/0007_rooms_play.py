# Generated by Django 4.1.3 on 2022-12-04 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_rooms_endplay_rooms_listsant'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='play',
            field=models.BooleanField(null=True),
        ),
    ]