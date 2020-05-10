from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'slug')
        # fields = '__all__'
        model = Category


    def to_representation(self, value):
        return {
            "name": value.title,
            "slug": value.slug
            }

    def to_internal_value(self, data):
        return {
            "title": data["name"],
            "slug": data["slug"]
        }


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'slug')
        # fields = '__all__'
        model = Genre

    def to_representation(self, value):
        return {
            "name": value.title,
            "slug": value.slug
            }

    def to_internal_value(self, data):
        return {
            "title": data["name"],
            "slug": data["slug"]
        }

class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    genre = serializers.SlugRelatedField(slug_field='slug', queryset=Genre.objects.all(), many=True)

    class Meta:
        fields = "__all__"
        model = Title




            