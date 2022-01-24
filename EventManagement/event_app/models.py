from django.db import models
from datetime import datetime


class Event(models.Model):
    EventName = models.CharField(max_length=70)
    EventDescription = models.TextField()
    EventFrom = models.DateTimeField(default=datetime.now())
    EventTo = models.DateTimeField(default=datetime.now())
    EventRegDeadline = models.DateTimeField(default=datetime.now())
    # EventPoster = models.ImageField(default='poster.jpg')
    EventHostEmail = models.EmailField(default="", max_length=254)
    EventHostPwd = models.CharField(default="", max_length=70)

    def __str__(self):
        return self.EventName


class Participant(models.Model):
    ParticipantName = models.CharField(max_length=70)
    ParticipantContact = models.CharField(max_length=10)
    ParticipantEvent = models.ForeignKey(Event, on_delete=models.CASCADE)
    ParticipantEventID = models.IntegerField()
    ParticipantEventName = models.CharField(default="", max_length=70)
    ParticipantEmail = models.EmailField(default="", max_length=254)
    ParticipantCount = models.IntegerField(default=1)

    def __str__(self):
        return self.ParticipantName
