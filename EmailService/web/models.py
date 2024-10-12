from django.db import models

# Create your models here.

class API_KEYs(models.Model):
    platform_name     = models.CharField(
                                        verbose_name="platform",
                                        blank=True, max_length=50)
    Location          = models.URLField(verbose_name="Service_Address",
                                        blank=True)
    API_KEY           = models.CharField(verbose_name="API_KEY",
                                        max_length=300,
                                        blank=True)
    CLIENT_SECRET     = models.CharField(verbose_name="secret_key",
                                        blank=True,
                                        max_length=200)
    CLIENT_ID         = models.CharField(verbose_name="CLIENT_ID",
                                        blank=True,
                                        max_length=200)
    ACCESS_TOKEN      = models.CharField(verbose_name="AccessToken",
                                        blank=True,
                                        max_length=200)
    
    def __str__(self):
        return f"{self.Location} {self.platform_name}"