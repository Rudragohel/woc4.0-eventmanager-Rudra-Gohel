from django.contrib import admin

# Register your models here.
from event_app.models import Event, Participant

admin.site.register(Event)
admin.site.register(Participant)

