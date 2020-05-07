from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core import mail
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (MyTokenObtainPairSerializer, SignUpSerializer,
                          UserSerializer)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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

#    def patch(self, request, format=None):
#        user = self.request.user
#        serializer = UserSerializer(user, data=request.data, partial=True)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def get_queryset(self):
#        queryset = User.objects.all()
#        username = self.kwargs.get('username', None)
#        if username is not None:
#            return User.objects.filter(username=username)
#        return queryset
    def partial_update(self, request, username):
        user = User.objects.get(username=username)
        role = request.data.get('role', None)
        if role is not None:
            if role == 'admin':
                user.is_staff = True
                user.is_superuser = True
            else:
                user.is_staff = False
                user.is_superuser = False
            user.save() 
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            # do not allow to change role in profile
            serializer.save(role=user.role)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpEmail(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            confirmation_code = make_password(
                password=email, 
                salt='settings.SECRET_KEY', 
                hasher='default'
            ).split('$')[-1]
            mail.send_mail(
                'Sign up new user', 
                f'Your confirmation code is {confirmation_code}',
                'yatube@mail.ru', 
                [email],
                fail_silently=False, 
            )        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
