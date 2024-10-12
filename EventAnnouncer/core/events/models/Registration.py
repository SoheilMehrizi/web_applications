from django.db import models
import datetime
from .Events import Events

class Registration_Manager(models.Manager):
    """
    The Method in this class will do validations before 
    Creating registration object.
    """
    pass
    def list(self, request, kwargs):
        pass

class Registrations(models.Model):
    """
    Model for Registration objects
    # It can be created by normal User
    # this objects contains the threshold for reminding the Event and its PRograms to user 
    """

    #User = models.ForeignKey('User', on_delete=models.CASCADE)
    Event = models.ForeignKey('Events', on_delete=models.CASCADE)
    # RegistrationSerial=models.
    Event_threshold = models.DurationField(default=datetime.timedelta(minutes = 5))
    Programs_threshold =  models.DurationField(default=datetime.timedelta(minutes = 5))

    Created_date = models.DateTimeField(auto_now=True)
    Updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'

    def __str__ (self):
        return f"Registered for {self.Event.Title}"
