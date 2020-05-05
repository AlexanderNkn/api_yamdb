from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class ApiUserViewSet(viewsets.ModelViewSet):
    '''
    List all users, or create a new user.
    Retrieve, update or delete selected user.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser]
    lookup_field = 'username'

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.kwargs.get('username', None)
        if username is not None:
            return User.objects.filter(username=username)
        return queryset


class UserProfile(APIView):
    '''
    Get and patch your profile
    '''
    def get(self, request, format=None):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, format=None):
        user = self.request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
