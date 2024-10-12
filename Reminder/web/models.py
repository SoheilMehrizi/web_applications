from logging import disable
from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class Event(models.Model):
    """
    Storing the Events
    """
    Title = models.CharField("Title", max_length=100, blank=True)
    description = models.TextField("Description")
    logo = models.URLField("Logo", max_length=200)
    treshold = models.PositiveIntegerField("Treshold", blank=True)
    #Event_Time = models.TimeField("Event_Time", auto_now=False, auto_now_add=False)
    Repeat_all_Day = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    Repeat = models.PositiveIntegerField("Repaet('Day')", blank=True, default=0)
    Upcoming_DateTime = models.DateTimeField("Upcoming_DateTime", auto_now=False, auto_now_add=False)
    created = models.DateTimeField("Created_Date", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now=True)
