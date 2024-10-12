from django.db import models
from accounts.models import User
"""
The Event App database models
"""


class Events (models.Model):
    """
    Model for objects in Events Table
    Contains the information about Events
    # only Superuser can add or change the objects.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Category = models.ForeignKey("Category", on_delete=models.CASCADE, default=None)
    Title = models.CharField(max_length=50)
    Image = models.URLField(max_length=255, null= True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Capacity = models.IntegerField(blank=True, null=True)
    Registration_onset = models.DateTimeField()
    Registration_end = models.DateTimeField()
    Event_onset = models.DateTimeField()
    Event_end = models.DateTimeField()
    Is_published = models.BooleanField(default=False)
    Expired = models.BooleanField(default=False)
    Published_date = models.DateTimeField()
    Created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    def get_snippet(self):
        """
        Makes A Summery from Object Description to show on List Mode.
        """
        return self.Description[0:2]
    def __str__(self):
        return f"{self.Category.Name}:{self.Title}"


class Category(models.Model):
    """
    The Categories of Events
    # only Superuser can add or change the objects.
    """
    Name = models.CharField(max_length=55)

    Created_date = models.DateTimeField(auto_now=True)
    Updated_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.Name