from django.contrib import admin

from .models import Post, category

class Post_Custom_Admin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'created_date', 'published_date']
    search_fields = ('author', 'title')

admin.site.register(Post, Post_Custom_Admin)
admin.site.register(category)