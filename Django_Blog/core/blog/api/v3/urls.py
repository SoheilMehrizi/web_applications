from django.urls import path, include
from . import views

app_name = 'api_v3'

urlpatterns = [
    #  path for index Class Based APIViews
 
    path('posts/', views.PostList_Create_APIView.as_view(), name="PostList_Create"),
    path('post/<int:pk>/', views.PostDetail_Destroy_Update_ApiView.as_view(), name="PostDetails_Destroy_Update"),
 ]