from web import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.PRV, name="PRV")
]
