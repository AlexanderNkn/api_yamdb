from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Genre, Title
from .permissions import IsAdnminRoleOrReadOnly
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title',)
    lookup_field = 'slug'
    # permission_classes = [IsAdnminRoleOrReadOnly]
    

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title',)
    lookup_field = 'slug'
    # permission_classes = [IsAdnminRoleOrReadOnly]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # permission_classes = [IsAdnminRoleOrReadOnly]
