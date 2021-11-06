from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_registered = models.DateTimeField(auto_now_add=True)

    #id_photo = models.ImageField()