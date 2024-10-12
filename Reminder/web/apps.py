from datetime import datetime
from django.apps import AppConfig

class WebConfig(AppConfig):
    """
    SetUp the Background Fuctionality
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
    def ready(self):
        from .reminder_scheduler import reminder_updator,  Reminder_Buffer_cleaner
        print("Start The Scout...")
        reminder_updator.start()
        Reminder_Buffer_cleaner.start()