from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=False,blank=False)
    email = models.EmailField(unique=False, blank=False)




