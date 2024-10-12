from django.urls import path, include
from . import views

app_name = 'api_v2'

urlpatterns = [
    #  path for index Class Based APIViews
 
    path('posts/', views.PostList.as_view(), name="PostList"),
    path('post/<int:id>/', views.PostDetail.as_view(), name="PostDetail"),
 ]