from rest_framework import routers
from . import views
app_name='api-v1'


Router = routers.DefaultRouter()

Router.register(r'event', views.EventModelViewSet, basename="EventModelViewSet")
Router.register(r'program', views.EventProgramModelViewSet, basename="EventProgramModelViewSet")
Router.register(r'lecturer', views.LecturerModelViewSet, basename="LecturerModelViewSet")
urlpatterns = Router.urls
