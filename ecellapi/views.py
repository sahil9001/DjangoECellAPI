from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
# Create your views here.

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer