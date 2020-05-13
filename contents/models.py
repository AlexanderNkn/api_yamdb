from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

RAING_CHOICES = (("1", "1"), ("2", "2"), ("3", "3"),("4", "4"),("5", "5"),
                ("6", "6"),("7", "7"),("8", "8"),("9", "9"),("10", "10"),)

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="title_category",
    )
    genre = models.ManyToManyField(Genre, related_name="title_genres")
    rating = models.IntegerField(default=0, choices=RAING_CHOICES, blank=True)

    def __str__(self):
        return self.name
