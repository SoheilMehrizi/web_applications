from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework import status 
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
class PostList(APIView):
    """
    A Class Based View for Managing the GET and POST API Calls 
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(Self, request):
        """This Method will Handle the GET Requests
        This Method will return a list of all Posts 
        if their status were false"""
        posts = Post.objects.filter(status = False)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """This method will handle POST Methods and after 
        Validation will creates an new Post Object"""
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class PostDetail(APIView):
    """
    this is a class for handling api's that calls a single 
    post , such as api with get request , put request, delete 
    request.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request, id):
        """
        This method manages get requests and responds 
        with Extracted Object        """
        post = get_object_or_404(Post, pk = id)
        SerializedPost = self.serializer_class(post)
        response = SerializedPost.data
        Status = status.HTTP_200_OK
        return Response(response, status = Status)
    def put(self, request, id):
        """
        With this method , the post object becomes editable.
        """
        post = get_object_or_404(Post, pk = id)
        SerializedUpdatedPost = self.serializer_class(post, data = request.data)
        SerializedUpdatedPost.is_valid(raise_exception=True)
        SerializedUpdatedPost.save()
        response = SerializedUpdatedPost.data
        Status = status.HTTP_200_OK
        return Response(response, status = Status)
    
    def delete(self, request, id):
        """
        With this method a Particular Post can be deleted...
        """
        post = get_object_or_404(Post, pk = id)
        post.delete()
        response = {'detail':"Item Not Found!"}
        Status = status.HTTP_204_NO_CONTENT
        return Response(response, status = Status)