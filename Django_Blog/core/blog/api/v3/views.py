from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from  rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework import status 
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404


class PostList_Create_APIView(ListAPIView, CreateAPIView):
    """
    This is a generic API View that returns a list of all posts.
    # Also You can Create new Posts.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail_Destroy_Update_ApiView(RetrieveUpdateDestroyAPIView, RetrieveModelMixin):
    """
    This View returns the detail of a particular post and also
    its able to delete or update a Post.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()