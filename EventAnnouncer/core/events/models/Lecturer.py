from django.db import models

"""
The Event App database models
"""


class Lecturer (models.Model):
    """
    Model for Programs Lecturer ,
    Contains the lecturer info instructions.
    # it can only add or create by superuser
    """
    name = models.CharField(max_length=50)
    Image = models.URLField(max_length=255, null= True, blank=True)
    Resume_link = models.URLField(max_length=255, null= True, blank=True)
    Bio = models.TextField(null=True, blank=True)
    
    Available = models.BooleanField(default=True)
    Created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Lecturer'
        verbose_name_plural = 'Lecturers'
    def __str__(self) :
        return f"{self.name}"
