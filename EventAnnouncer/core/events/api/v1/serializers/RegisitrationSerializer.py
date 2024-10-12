from rest_framework.serializers import ModelSerializer
from ..models import Registrations

class RegistrationSerializer(ModelSerializer):
    """
    Serializer for Registrations objects
    """
    class Meta:
        model = Registrations
        fields = ['id', 'Event', 'Event_threshold', 'Programs_threshold', 
                  'Created_date', 'Updated_date']