from django.db import models
from .Events import Events
from .Lecturer import Lecturer



class Event_programs(models.Model):
    """
    Model for creating Event Programs objects that is subset for Events Object
    it can not be used with out a lecturer instance
    # its relation is CASCADE
    """
    Event = models.ForeignKey("Events", on_delete=models.CASCADE)
    Lecturer = models.ForeignKey("Lecturer", on_delete=models.CASCADE)
    Topic = models.CharField(max_length=55)
    Description = models.TextField(blank=True, null=True)
    Session_link = models.URLField(max_length=255, blank=True, null=True)
    
    Available = models.BooleanField(default=True)

    Session_date = models.DateTimeField()
    Created_date = models.DateTimeField(auto_now=True)
    Updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Event_Programs'
        verbose_name_plural = 'Event_Programs'
    
    def get_snippet(self):
        """
        Makes a summery from Description Field.
        """
        snippet = 'Hello'
        # try:
        #     snippet = self.Description[0:5]
        #     return snippet
        # except IndexError:
        #     return snippet
        return snippet

    def __str__(self):
        return f"{self.Event.Title}, {self.Topic}"
