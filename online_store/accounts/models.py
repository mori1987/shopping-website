from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True,null=True)
