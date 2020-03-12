from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name','venue','date','time','details','details_html','cover_pic','icon','email','flag','year','created_at','modified_at')