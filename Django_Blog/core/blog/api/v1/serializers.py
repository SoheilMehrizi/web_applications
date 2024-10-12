from rest_framework import serializers
from ...models import Post
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)


class PostSerializer(serializers.ModelSerializer):
    """
    Serialize the object Model into json Object
        # inherit from ModelSerializer
    """
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'status', 'published_date', 'created_date']
