from django.contrib import admin
from django.contrib.auth.models import(
    User,
)
from .models import (
                    Event,
                    )

class EventAdmin(admin.ModelAdmin):#Customize the Django Admin Panel
    list_display = ['Title', 'Upcoming_DateTime', 'treshold',
                    'Repeat_all_Day','Repeat','created', 'updated']
admin.site.register(Event, EventAdmin)
