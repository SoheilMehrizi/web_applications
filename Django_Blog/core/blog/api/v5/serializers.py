from rest_framework import serializers
from ...models import Post, category
from accounts.models import Profile
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)


class CategorySerializer(serializers.ModelSerializer):
    """
    Model Serializer for category objects
        # Inherit from ModelSerializer
    """
    class Meta:
        model = category
        fields = ['id', 'name']
   
class PostSerializer(serializers.ModelSerializer):
    """
    Serialize the object Model into json Object
        # inherit from ModelSerializer
    """
    # snippet gets a brief summary of posts content .
    snippet = serializers.ReadOnlyField(source='get_snippet')
    
    # we can get category field the way we want by slugrelatedfield or we can just inherite it from its serializer.
    # category=serializers.SlugRelatedField(many=False, queryset=category.objects.all(), slug_field='name')
    # category = 'CategorySerializer'
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    # its better to generate url inside serializer instead of model or view .
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'image','content', 'snippet', 'category', 'status', 'relative_url', 'absolute_url',
                  'published_date', 'created_date']
        read_only_fields = ['author','snippet', 'relative_url']
    def get_absolute_url(self, obj):
        """
        This Method generates an absolute_url for an object
        """
        request = self.context.get('request')
        
        return request.build_absolute_uri(obj.pk)
    def to_representation(self, instance):
        """
        This Method Will separate the showing representation style of some field and their creating time . 
        """
        # the objects that we want see in response JSONObject can be changed by rep object
        rep = super().to_representation(instance)
        # we should pass request , when we use another object in our representor.
        rep['category'] = CategorySerializer(instance.category, context={'request':request}).data
        # using request for determination of , showing some fields in list mode or single mode
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            # when the a single object requested
            rep['state'] = 'single'
            rep.pop('absolute_url', None)
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
        else:
            # When the list of all post objects requested
            rep['state'] = 'list'
            rep.pop('content', None)
        # the customization of Category
        return rep
    def create(self, validated_data):
        # get and setup the author of the post , it comes from authors Profile.
        #this way , the current autor will automatically use in posts author instance .
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)

        

