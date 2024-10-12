from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ....models import Events
class Event_Serializer(ModelSerializer):
    """
    Serializer for Event objects
    """
    snippet = serializers.ReadOnlyField(source="get_snippet")
    absolute_url = serializers.SerializerMethodField()
    """
    Getting a Summery for Object Description
    """

    class Meta:
        model = Events
        fields = ['id', 'absolute_url', 'author','Category', 'Title', 'Image', 'snippet', 'Description',
                  'Capacity', 'Registration_onset', 'Registration_end',
                  'Event_onset', 'Event_end','Published_date', 'Created_date',
                  'updated_date',  'Is_published', 'Expired']
        read_only_fields = ['snippet', 'author']
    def get_absolute_url(self, obj):
        """
        This Function returns the absolute url of an object .
        """
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
    def to_representation(self, instance):
        """
        Whats going to send to client .
        """
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep['state'] = 'single'
            rep.pop('snippet')
            rep.pop('absolute_url')
        else:
            rep['state'] = 'List'
        return rep
    def create(self, validated_data):
        """
        Set The Current session User as the Author of the event 
        """
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user
        return super().create(validated_data)
