from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_v4'

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
urlpatterns = router.urls

# urlpatterns = [
#     #  path for index generic APIViews
 
#      path('post/', views.PostViewSet.as_view({'get':'list', 'post':'create'}), name="Post_List"),
#      path('post/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 
#                                                         'patch':'partial_update', 'delete':'destroy'}), name="Post_Detail"),
#  ]