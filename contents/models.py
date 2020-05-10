from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(blank=True)
    description = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='title_category')
    genre = models.ManyToManyField(Genre, related_name='title_genres')
    