from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .serializers.Event_Serializer import Event_Serializer
from .serializers.EventProgramsSerializer import EventProgramsSerializer
from .serializers.LecturerSerializer import LecturerSerializer
from ...models import Events, Event_programs, Lecturer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
class EventModelViewSet(ModelViewSet):
    """
    ModelViewSet For Event Model that handles the 
    CRUD Operations for Events Object .
    """
    
    queryset = Events.objects.all()
    serializer_class = Event_Serializer


    permission_classes = [IsAuthenticatedOrReadOnly]
    # Some Applied Filters On this View .
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    # Fields to Filter
    filterset_fields = {'Category':['exact', 'in'], 'Capacity':['exact', 'in']}
    # Fields to Search
    search_fields = ['Category', 'Title', 'Registration_onset',
                     'Event_onset']
    # Ordering By these fields .
    ordering_fields=['Registration_onset']

class EventProgramModelViewSet(ModelViewSet):
    """
    ModelViewSet For Event Model that handles the 
    CRUD Operations for Events Object .
    """
    
    queryset = Event_programs.objects.all()
    serializer_class = EventProgramsSerializer


    permission_classes = [IsAuthenticatedOrReadOnly]
    # Some Applied Filters On this View .
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    # Fields to Filter
    filterset_fields = {'Event':['exact', 'in'], 'Available':['exact','in']}
    # Fields to Search
    search_fields = ['Topic', 'Lecturer','Event']
    # Ordering By these fields .
    ordering_fields=['Session_date']

class LecturerModelViewSet(ModelViewSet):
    """
    Processes the CRUD Operation for Lecturer DataBase Model.
    """

    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, 
                        filters.OrderingFilter]
    # Fields to Search
    search_fields = ['name']
    # Ordering By these fields .
    ordering_fields=['Created_date']
