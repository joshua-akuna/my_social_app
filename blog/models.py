from django.db import models

# Create your models here.
# To extend django builtin User model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings #to reference the AUTH_USER_MODEL

class User(AbstractUser):
    '''Extends django's default User model to add custom fields.
        You can add more fields here as per your project app's requirement.
        e.g., profile picture, bio, website, etc.
    '''
    profile_picture = models.ImageField(
        upload_to = 'profile_pics/',
        blank = True,
        null = True,
        help_text = "User's profile picture"
    )
    bio = models.TextField(
        max_length = 200,
        blank = True,
        help_text = "A short biography of the User"
    )
    date_of_birth = models.DateField(
        blank = False,
        null = False,
        help_text = "User's date of birth"
    )
    location = models.CharField(
        max_length = 100,
        blank = True,
        help_text = "User's Location"
    )