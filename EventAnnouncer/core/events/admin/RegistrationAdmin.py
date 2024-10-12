from django.contrib import admin
from events.models import Registrations

@admin.register(Registrations)
class RegistrationAdmin(admin.ModelAdmin):
    """
    Specify how admin access of the Registrations Object should look.
    # the Ordinary users has the CRUD Permissions for these objects 
    """
    list_display = ('Event', 'Event_threshold', 'Programs_threshold', 'Created_date', 'Updated_date')
    
    list_filter = ('Event',)
    
    search_fields = ('Event',)