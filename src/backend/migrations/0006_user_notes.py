# Generated by Django 3.0.7 on 2020-08-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_uploaded_file_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]