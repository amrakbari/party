# Generated by Django 4.0.6 on 2022-07-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_room_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
