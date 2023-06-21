from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=255,null=True,blank=True)#the null mean if user didnt input any thing in field the field still empty

    def __str__(self):
        return self.email