from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ....models import Lecturer

class LecturerSerializer(ModelSerializer):
    """
    Serializer for Lecturer Objects
    """
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Lecturer
        
        fields = ['id', 'absolute_url', 'name', 'Image', 'Resume_link', 'Bio',
                  'Available', 'Created_date', 'updated_date']
    def to_representation(self, instance):
        """
        Determine what should show and what shouldn't...
        """
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep['state'] = 'Single'
            rep.pop('absolute_url')
        else:
            rep['state'] = 'List'
        
        return rep
    def get_absolute_url(self, obj):
        """
        Returns the Absolute URL of an Object
        """
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
    