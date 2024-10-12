from django.contrib import admin
from events.models import  Events, Category


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    """
    specify how the admin panel should look for Events
    """
    date_hierarchy = 'Published_date'
    empty_value_display = '-empty-'

    fields = ("Title", "Category", "Image", "Description", "Capacity", "Registration_onset",
              "Registration_end", "Event_onset", "Event_end", "Is_published", "Expired", "Published_date"
              )
    list_display = ("Title", "Category", "Capacity", "Registration_onset", "Registration_end",
                    "Event_onset", "Event_end", "Is_published", "Published_date", "Created_date", "updated_date")
    search_fields=("Title", "Published_date")

    list_filter = ("Is_published", "Category", "Capacity")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    specify how Category objects should look in admin panel
    """
    date_hierarchy = "Created_date"

    list_display = ("Name", "Created_date", "Updated_date")

    search_fields = ("Name",)
    
