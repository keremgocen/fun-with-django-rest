from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    pin_code = models.CharField(
        max_length=5, editable=True, unique=True, validators=[MinLengthValidator(5)]
    )
