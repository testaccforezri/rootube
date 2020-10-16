# Generated by Django 3.0.7 on 2020-10-11 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('backend', '0009_commentticket_ticket_videoticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='subs_notified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='from_channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='backend.Channel'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('CO', 'New Comment'), ('TA', 'Tagged User'), ('VI', 'New Video')], max_length=2)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('unread', models.BooleanField(default=True)),
                ('action_id', models.PositiveIntegerField()),
                ('target_id', models.PositiveIntegerField()),
                ('action_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='contenttypes.ContentType')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Channel')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('target_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
