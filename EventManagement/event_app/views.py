from datetime import datetime
from django.utils import timezone

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from event_app.models import Event, Participant


def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def eventreg(request):
    template = loader.get_template('EventRegister.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def participantreg(request):
    template = loader.get_template('ParticipantRegister.html')

    now = timezone.now()
    data = []

    for event in Event.objects.all():
        if event.EventRegDeadline > now:
            data.append(event)

    context = {
        "Events": data,
        "size": len(data)
    }
    return HttpResponse(template.render(context, request))


def create_event(request):
    template = loader.get_template('index.html')

    name = request.POST.get("Ename")
    desc = request.POST.get("Edesc")
    start = request.POST.get("Estart")
    end = request.POST.get("Eend")
    deadline = request.POST.get("ERegdead")
    Hemail = request.POST.get("EHmail")
    Hpwd = request.POST.get("EHpwd")

    event = Event(EventName=name, EventDescription=desc, EventFrom=start, EventTo=end, EventRegDeadline=deadline,
                  EventHostEmail=Hemail, EventHostPwd=Hpwd)

    event.save()
    context = {

    }
    return HttpResponse(template.render(context, request))


def create_participant_page(request, Event_Name):
    template = loader.get_template('CreateParticipant.html')

    context = {
        "InEvent": Event_Name
    }
    print("Reached: ",Event_Name)
    return HttpResponse(template.render(context, request))


def create_participant(request):

    template = loader.get_template('index.html')

    Ename = request.POST.get("PEName")
    name = request.POST.get("Pname")
    contact = request.POST.get("Pcontact")
    rmail = request.POST.get("Pmail")
    typr = request.POST.get("RegType")
    Ptotal = request.POST.get("Pnum")
    Pcount=1

    if typr == 'G' and Ptotal==1:
        return render(request, 'CreateParticipant.html', {"isgroup": True})
    else:
        Pcount=Ptotal

    EventInstance = Event.objects.get(EventName=Ename)

    EventID = EventInstance.id

    participant = Participant(ParticipantName=name, ParticipantContact=contact, ParticipantEvent=EventID,ParticipantEventName=Ename, ParticipantEmail=rmail, ParticipantCount=Pcount)
    participant.save()
    context = {

    }
    return HttpResponse(template.render(context, request))
