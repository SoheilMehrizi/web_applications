from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework import status 
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404


# Example for ViewSet in CBV
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def list(self, request):

        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):

        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    def create(self, request):
        pass
    def update(self, request, pk=None):
        pass
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass