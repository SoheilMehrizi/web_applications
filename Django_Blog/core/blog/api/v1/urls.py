from django.urls import path, include
from . import views

app_name = 'api_v1'

urlpatterns = [
    #  path for index function view, test function based view
 
    path('posts/', views.post_list, name="post_list"),
    path('post/<int:id>/', views.postDetail, name="post_Detail"),
 ]