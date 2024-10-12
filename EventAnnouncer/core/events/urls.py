from django.urls import path, include
app_name = 'events'
urlpatterns = [
    # All UrlRouts of Event App APIs Version 1.
    path(r'api/v1/', include('events.api.v1.urls')),
]
