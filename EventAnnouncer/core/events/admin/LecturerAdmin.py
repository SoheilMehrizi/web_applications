from django.contrib import admin
from events.models import Lecturer
@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    """
    Specify how lecturer objects should look in admin panel
    """
    fields = ('name', 'Image', 'Resume_link', 'Bio', 'Available')
    list_display = ('name', 'Available', 'Created_date', 'updated_date')
    list_filter = ('Available',)
    search_fields = ('name',)

