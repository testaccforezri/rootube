# Generated by Django 3.0.7 on 2020-07-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_video_is_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]