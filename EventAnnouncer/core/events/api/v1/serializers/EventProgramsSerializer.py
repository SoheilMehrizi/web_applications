from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ....models import Event_programs
class EventProgramsSerializer(ModelSerializer):
    """
    the serializer for EventProgram Objects .
    """
    snippet = serializers.ReadOnlyField(source='get_snippet')
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model=Event_programs
        fields = ['id', 'absolute_url', 'Event', 'Lecturer', 'Topic', 'Description', 'snippet',
                  'Session_link', 'Available', 'Session_date',
                  'Created_date', 'Updated_date']
        read_only_fields = ['snippet', 'absolute_url', 'Created_date',
                            'Updated_date']

    def to_representation(self, instance):
        """
        what the client should see.
        """
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep['state'] = 'Single'
            rep.pop('snippet')
            rep.pop('absolute_url')
        else:
            rep['state'] = 'List'
        return rep
    def get_lecturer(self, instance):
        """
        The List of Lecturers
        """
        pass
    def get_absolute_url(self, obj):
        """
        This Function returns the absolute url of an object .
        """
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
        