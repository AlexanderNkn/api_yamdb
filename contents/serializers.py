from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="title")
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field="name")
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(), slug_field="name", many=True)

    class Meta:
        model = Title
        fields = '__all__'
        # fields = ("id", "name", "year", "description", "genre", "category")
