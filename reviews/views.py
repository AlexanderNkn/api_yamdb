from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from objects.models import Object
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer
from .permissions import IsOwnerAdminModeratorOrReadOnly


class NestedResourceMixin:
    """
    Mixin for ModelViewSet for nested resources. E.g., in /movies/<movie_id>/reviews/ 
    the 'Review.movie' field references 'Movie' objects identified by <movie_id>.
    Requires class attributes parent_object, parent_field, parent_url_id.
    """
    
    def _get_parent(self):
        return get_object_or_404(self.parent_object, id=self.kwargs[self.parent_url_id])

    def get_queryset(self):
        parent = self._get_parent()
        return super().get_queryset().filter(**{self.parent_field: parent})

    def perform_create(self, serializer):
        parent = self._get_parent()
        serializer.save(**{self.parent_field: parent}, **self.serializer_save_fields())


class ReviewViewSet(NestedResourceMixin, viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerAdminModeratorOrReadOnly,
    ]
    parent_object, parent_field, parent_url_id = Object, "object", "title_id"

    def serializer_save_fields(self):
        return {"author": self.request.user}


class CommentViewSet(NestedResourceMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerAdminModeratorOrReadOnly,
    ]
    parent_object, parent_field, parent_url_id = Review, "review", "review_id"

    def serializer_save_fields(self):
        return {"author": self.request.user}
