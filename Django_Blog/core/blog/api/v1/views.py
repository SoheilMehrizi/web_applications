"""
    RestFrameWork Apis | 
"""
from ...models import Post
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    """
    Lists all of the bogs posts
    """
    if request.method == 'GET':
        posts = Post.objects.filter(status = False)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == "POST":
         
         serializer = PostSerializer(data = request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    """
    Extracts a single post 
    """
    post = get_object_or_404(Post, pk = id)
    if request.method == 'GET':
        """
        Returns the detail of an object in json form
        """
        SerializedPost = PostSerializer(post)
        response = SerializedPost.data
        Status = status.HTTP_200_OK
    elif request.method == 'PUT':
        """
        Update some fields of an object
        """
        SerializedUpdatedPost = PostSerializer(post, data = request.data)
        SerializedUpdatedPost.is_valid(raise_exception=True)
        SerializedUpdatedPost.save()
        response = SerializedUpdatedPost.data
        Status = status.HTTP_200_OK
    elif request.method == 'DELETE':
        """
        DELETE A Certain Post
        """
        post.delete()
        response = {'detail':"Item Not Found!"}
        Status = status.HTTP_204_NO_CONTENT
    return Response(response, status=Status)