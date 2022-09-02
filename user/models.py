from django.contrib.auth.models import AbstractUser
from django.db import models

from user.manager import CustomUserManager
from enumoration import UserType


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=45, unique=True)
    user_type = models.CharField(max_length=10, choices=UserType.choices())
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.username
