from datetime import datetime
from django.utils import timezone

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from event_app.models import Event, Participant
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from twilio.rest import Client


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
    template = loader.get_template('RegisterReplyTemp.html')

    name = request.POST.get("Ename")
    desc = request.POST.get("Edesc")
    start = request.POST.get("Estart")
    end = request.POST.get("Eend")
    deadline = request.POST.get("ERegdead")
    Hemail = request.POST.get("EHmail")
    Hpwd = request.POST.get("EHpwd")
    venue = request.POST.get("Evenue")
    context = {
        "Rtype": "Event_Registration",
        "Bgcolor": "#e6a8a8",
        "Tcolor": "#4f0202",
        "Message": " Registration Unsuccessful!!",
        "Button_Text": "Try Again",
        "Destination": "event_registration",
        "name": name,
        "error": "",
        "error_color": "#8a0101",
        "cause": "Cause of Error:",
        "Type": "Event"
    }

    if end < start:
        context["error"] = "Event end time must be after start time !!"
        return HttpResponse(template.render(context, request))

    try:
        found = Event.objects.get(EventName=name)
        context["error"] = "Event with name '" + name + "' already exists. Change Event name"
        return HttpResponse(template.render(context, request))
    except:
        pass

    event = Event(EventName=name, EventDescription=desc, EventFrom=start, EventTo=end, EventRegDeadline=deadline,
                  EventHostEmail=Hemail, EventHostPwd=Hpwd, EventVenue=venue)
    event.save()

    mail_content = "Hello,\nYour Event '" + name + "' has been registered successfully.\nYour Event id is: " + str(
        event.id) + "\nYou can use this ID to view participant registrations in 'Dashboard' section of the website."
    subject = "Event Registered Successfully!!"

    send_mail(Hemail, subject, mail_content)

    context = {
        "Rtype": "Event_Registration",
        "Bgcolor": "#afedd3",
        "Tcolor": "#033813",
        "Message": " Registered successfully!!",
        "Button_Text": "Back",
        "Destination": "/index",
        "name": name,
        "Type": "Event"
    }
    return HttpResponse(template.render(context, request))


def create_participant_page(request, Event_Name):
    template = loader.get_template('CreateParticipant.html')

    context = {
        "InEvent": Event_Name
    }
    print("Reached: ", Event_Name)
    return HttpResponse(template.render(context, request))


def create_participant(request):
    template = loader.get_template('RegisterReplyTemp.html')

    Ename = request.POST.get("PEName")
    name = request.POST.get("Pname")
    contact = request.POST.get("Pcontact")
    rmail = request.POST.get("Pmail")
    typr = request.POST.get("RegType")
    Ptotal = request.POST.get("Pnum")
    Pcount = 1

    print("Ptotal: ", Ptotal)
    print("Ptyper: ", typr)

    if typr == 'G':
        Pcount = Ptotal

    context = {
        "Rtype": "Participant_Registration",
        "Bgcolor": "#e6a8a8",
        "Tcolor": "#4f0202",
        "Message": " Registration Unsuccessful!!",
        "Button_Text": "Try Again",
        "Destination": "handle_create_participant/" + Ename,
        "name": name,
        "error": "",
        "error_color": "#8a0101",
        "cause": "Cause of Error:",
        "Type": "Participant"
    }

    try:
        found = Participant.objects.get(ParticipantContact=contact)
        context["error"] = "Participant with this contact number already exists. One Participant is allowed to " \
                           "register only one time. "
        return HttpResponse(template.render(context, request))
    except:
        pass

    try:
        found = Participant.objects.get(ParticipantEmail=rmail)
        context["error"] = "Participant with this email number already exists.One Participant is allowed to register " \
                           "only one time. "
        return HttpResponse(template.render(context, request))
    except:
        pass

    EventInstance = Event.objects.get(EventName=Ename)

    EventID = EventInstance.id

    participant = Participant(ParticipantName=name, ParticipantContact=contact, ParticipantEventID=EventID,
                              ParticipantEventName=Ename, ParticipantEvent=EventInstance, ParticipantEmail=rmail,
                              ParticipantCount=Pcount)

    participant.save()

    message = "\n\n\n\nHello,\nYour Registration for event '" + Ename + "' is done successfully.\nYour Participant id is: " + str(
        participant.id) + "\nEvent Start:" + EventInstance.EventFrom.strftime("%m/%d/%Y, %H:%M:%S") + ".\n" + "Event End:" + EventInstance.EventTo.strftime("%m/%d/%Y, %H:%M:%S")+ ".\n" + "Event Venue:" + EventInstance.EventVenue + ".\n"

    subject = "About Registration in Event: " + Ename

    send_sms(message, contact)

    send_mail(rmail, subject, message)

    context = {
        "Rtype": "Participant_Registration",
        "Bgcolor": "#afedd3",
        "Tcolor": "#033813",
        "Message": " Registered successfully!!",
        "Button_Text": "Back",
        "Destination": "/index",
        "name": name,
        "Type": "Participant"
    }
    return HttpResponse(template.render(context, request))


def host_login(request):
    template = loader.get_template('HostLogIn.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def find_participant(request):
    template = loader.get_template('DisplayEvent.html')
    EID = request.POST.get("EId")
    password = request.POST.get("Hpassword")

    try:
        EventInstance = Event.objects.get(id=EID)
        if EventInstance.EventHostPwd != password:
            template = loader.get_template('HostLogIn.html')
            context = {
                "LoginFail": True,
            }
            return HttpResponse(template.render(context, request))


    except:
        template = loader.get_template('HostLogIn.html')
        context = {
            "LoginFail": True,
        }
        return HttpResponse(template.render(context, request))

    ParticipantsOfThisEvent = Participant.objects.filter(ParticipantEvent=int(EID))

    ZeroRegistration = False

    print("Number of Participants: ", len(ParticipantsOfThisEvent))
    if len(ParticipantsOfThisEvent) == 0:
        ZeroRegistration = True

    context = {
        "Event": Event.objects.get(id=EID).EventName,
        "participants": ParticipantsOfThisEvent,
        "isEmpty": ZeroRegistration
    }
    return HttpResponse(template.render(context, request))


def send_mail(receiver_address, subject, mail_content):
    sender_address = ''  # add sender's email address here
    sender_pass = ''  # add sender's passsword address here

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject

    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


def send_sms(message, reciever_number):
    account_sid = ''  # add account_sid here
    auth_token = ''  # add auth_token here

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='',  # add sender's number here
        body=message,
        to=str(reciever_number)
    )
