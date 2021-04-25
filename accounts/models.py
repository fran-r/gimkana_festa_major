from django.contrib.auth.models import AbstractUser
from django.db import models

from gimkana.models import UserQrs


class User(AbstractUser):
    qrs = models.ManyToManyField(UserQrs, blank=True, null=True)

    # REQUIRED_FIELDS = ['email']
    # USERNAME_FIELD = 'email'
