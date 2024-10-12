from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where Email is the unique identifier 
    for authentication instead of username
    """
    def create_user(self, Email, password, **kwargs):
        """
        Create and save a user with the given Email and password.
        """

        if not Email:
            raise ValueError(_("The Email must be set"))

        Email = self.normalize_email(Email)
        user = self.model(Email= Email, **kwargs)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, Email, password, **kwargs):
        """
        Create and save a SuperUser with the given email and password.
        """

        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)


        if kwargs.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(Email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Contains the User Objects Model Structure
    """

    Email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    Created_date = models.DateTimeField(auto_now=True)
    Updated_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "Email"

    objects = CustomUserManager()

    def __str__(self):
        return self.Email