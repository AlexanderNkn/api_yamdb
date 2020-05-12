from rest_framework import serializers
from django.db.models import Avg

from reviews.models import Review
from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["id"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ["id"]


class TitleSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="slug"
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field="slug", many=True
    )
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = "__all__"

    def get_rating(self, obj):
        return Review.objects.filter(title=obj).aggregate(Avg("score"))["score__avg"]
