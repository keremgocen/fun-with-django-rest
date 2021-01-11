from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    pin_code = models.CharField(
        max_length=5, default='00000', editable=True, unique=True)
