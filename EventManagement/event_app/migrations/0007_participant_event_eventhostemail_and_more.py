# Generated by Django 4.0.1 on 2022-01-22 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0006_alter_event_eventfrom_alter_event_eventposter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ParticipantName', models.CharField(max_length=70)),
                ('ParticipantContact', models.CharField(max_length=10)),
                ('ParticipantEvent', models.CharField(max_length=2)),
                ('ParticipantEmail', models.EmailField(max_length=254)),
                ('Participantpwd', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='EventHostEmail',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventFrom',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 22, 22, 2, 22, 175445)),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventRegDeadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 22, 22, 2, 22, 175445)),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventTo',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 22, 22, 2, 22, 175445)),
        ),
    ]