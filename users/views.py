from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class ApiUserViewSet(viewsets.ModelViewSet):
    '''
    List all userss, or create a new user.
    Retrieve, update or delete selected user.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
