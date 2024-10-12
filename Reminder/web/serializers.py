
from dataclasses import fields
from rest_framework import(
    serializers
)

from .models import(
    Event,

)

class Event_Serializer(serializers.ModelSerializer):
    """
    Serialize the Event Model for Rest API
    """
    class Meta:
        model = Event
        fields = ["Title", "description", "logo", "treshold",
                  "Repeat","Repeat_all_Day","disabled","Upcoming_DateTime", "created", "updated"]