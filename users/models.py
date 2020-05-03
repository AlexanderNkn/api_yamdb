from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    '''
    A custom user model to customize it if the need arises.
    '''
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
