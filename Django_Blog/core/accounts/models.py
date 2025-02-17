from django.contrib.auth.models import(
                                       BaseUserManager,
                                       AbstractBaseUser,
                                       PermissionsMixin
                                       )
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        create and save a UserObject as a ordinary user
        with the given email and password and extra data. 
        """
        if not email :
            raise ValueError(_('The Email must be set.'))
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    

    def create_superuser(self, email, password, **extra_fields):
        """
        create and save a User object as a superuser 
        with given email and password and extra data.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)
        
class User(AbstractBaseUser, PermissionsMixin):
    """
    its a class to define users for accounts app
    """
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

@receiver(post_save, sender=User)
def save_Profile(sender, instance, created, **kwargs):
    # a signal function , will create a Profile object  in the times that
    # a new user added
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):

    """
    stores the user's additional data 
    """
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length= 255)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(_("Bio"))

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.email}, {self.first_name} {self.last_name}"