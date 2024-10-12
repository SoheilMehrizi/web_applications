from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permisions import IsOwnerOrReadOnly
from rest_framework import status 
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, category
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import DefaultPagination

# Example for Model ViewSet in CBV
class PostModelViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Post Object
    """
    Model = Post
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = DefaultPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # Some Applied Filters on this View .
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Fields to sort.
    filterset_fields = {'category':['exact', 'in'], 'author':['exact', 'in'], 'status':['exact', 'in']}
    # Search among post based on their exact title and content. 
    search_fields = ['=title', 'content']
    # Sorts the list of posts in order by their ordering_field
    ordering_fields = ['published_date']
    """
    We use @action decorator when we want to use extra methods .
    """    
    @action(['get'], detail=False)
    def get_ok(self, request):
        """
        Returns a response that clarifies the extraaction's functionality 
        """
        return Response({'detail':'OK'})



class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Category Object
    """
    Model = category
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = category.objects.all()