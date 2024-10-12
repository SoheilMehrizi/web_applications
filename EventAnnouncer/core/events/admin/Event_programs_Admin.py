from django.contrib import admin
from events.models import Event_programs
@admin.register(Event_programs)
class Event_programs_Admin(admin.ModelAdmin):
    """
    specify how Event_programs Objects should look on admin panel
    """
    list_display = ('Topic', 'Event', 'Lecturer', 'Available', 'Session_date',
                    'Created_date', 'Updated_date')

    list_filter = ('Event', 'Lecturer', 'Available', 'Session_date')

    search_fields = ('Topic', 'Events', 'Lecturer', 'Session_date')