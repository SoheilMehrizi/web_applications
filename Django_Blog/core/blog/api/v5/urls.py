from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v5'
"""
Also can setup the router from SimpleRouter in this case we lose propertises like api_rout and ...
but we have this  ability to customize our own .
"""
router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')

# urlpatterns = [
     
# ]
urlpatterns = router.urls

