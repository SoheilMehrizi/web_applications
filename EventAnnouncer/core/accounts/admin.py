from django.contrib import admin
from .models import User
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """
    This is a Custom structure for the users admin panel .
    # This Admin model inherit from ModelAdmin
    """

    list_display = ('Email', 'is_staff', 'is_active', 'Created_date', 'Updated_date')

    list_filter = ('is_staff', 'is_active', 'Created_date')

    search_fields = ('Email',)