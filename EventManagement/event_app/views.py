from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


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
    context = {

    }
    return HttpResponse(template.render(context, request))
