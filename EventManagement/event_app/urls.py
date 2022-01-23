"""EventManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from event_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event_registration', views.eventreg, name='eventregister'),
    path('participant_registration', views.participantreg, name='participantregister'),
    path('event_creation', views.create_event, name='event_creation'),
    path('handle_create_participant/<str:Event_Name>', views.create_participant_page, name="handle_create_participant"),
    path('participant_creation', views.create_participant, name='create participant'),
]
