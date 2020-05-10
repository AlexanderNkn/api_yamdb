from rest_framework import permissions

from .models import User


class IsAdnminRoleOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author
        
        # return request.user.is_superuser 

        return User.objects.filter(username=request.user, groups__name = 'admin').exists()
        
    