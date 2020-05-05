from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer


class ApiUserViewSet(viewsets.ModelViewSet):
    '''
    List all users, or create a new user.
    Retrieve, update or delete selected user.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.kwargs.get('username', None)
        if username is not None:
            return User.objects.filter(username=username)
        return queryset


class UserProfile(generics.ListCreateAPIView):
    '''
    Get and patch your profile
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user.username)
        return queryset
