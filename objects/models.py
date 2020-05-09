from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Object(models.Model):
    name = models.TextField()
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.IntegerField(null=True, blank=True)  # temp
    genre = models.IntegerField(null=True, blank=True)  # temp
