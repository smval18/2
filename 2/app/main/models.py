from django.contrib.auth.models import AbstractUser
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=150)
    disc = models.TextField(max_length=255)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

