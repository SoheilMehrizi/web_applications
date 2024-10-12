from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    #  path for index function view, test function based view
    path('', views.index_fbView, name = "index_fbview"),
    path('Posts/', views.PostListView.as_view(), name="PostsList"),
    path('post/<int:id>/', views.PostDetailView.as_view(), name="PostDetail"),
    path('Post/create', views.PostCreateView.as_view(), name = "PostCreate"),
    path('api/v1/', include('blog.api.v1.urls')),
    path('api/v2/', include('blog.api.v2.urls')),
    path('api/v3/', include('blog.api.v3.urls')),
    path('api/v4/', include('blog.api.v4.urls')),
    path('api/v5/', include('blog.api.v5.urls')),
]