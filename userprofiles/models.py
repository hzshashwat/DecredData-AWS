from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, username, profilepicture, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have an username')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, username=username, profilepicture=profilepicture)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, username, profilepicture, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, username, profilepicture, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, primary_key=True)
    profilepicture = models.ImageField(upload_to='profilepictures/')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.username

    def __str__(self):
        """Return string representation of user"""
        return self.username