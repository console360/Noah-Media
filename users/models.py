from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


# Create your models here.
from noah import settings
from noah.models import CommonInfo


class UserManager(BaseUserManager):
    """
    User manager class to handle user creation
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates a new User
          - Normalizes the email
          - Also creates a new auth token for the user
        """

        # Check if email is provided
        if not email:
            raise ValueError('User must have a valid email')

        # Normalize the provided email
        email = self.normalize_email(email)

        # Creating user object
        # Default email isn't verified. To get it verified via email link
        user = self.model(email=email, is_deleted=False, **extra_fields)
        # # setting user password
        user.set_password(password)
        # # saving user in database
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates a superuser
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, CommonInfo, PermissionsMixin):
    """
    Maintain user and its attributes
    """
    class Meta:
        db_table = 'noah_users'

    name = models.CharField(_('name'), max_length=256, default='')
    email = models.EmailField(_('email'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_social = models.BooleanField(default=False)
    is_system_generated_password = models.BooleanField(default=False)
    # is_email_verified = models.BooleanField(default=False)  # Flag to verify user's email
    # user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, default=1)  # Define user role from the system

    # defines the user manager class for User
    objects = UserManager()

    # specifies the field that will be used as username by django
    # drf_auth_users framework
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        name = '%s' % self.name
        return name.strip()

    def get_email(self):
        """
        Returns email for the user.
        """
        return self.email


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
