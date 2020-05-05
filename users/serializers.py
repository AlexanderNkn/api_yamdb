from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
#    password = serializers.CharField(min_length=8, write_only=True)

    def validate_role(self, value):
        '''
        Check if user's role is in ROLE_CHOICES('user' or 'moderator' or 'admin')
        '''
        if value not in ['admin', 'moderator', 'user']:
            raise ValidationError("Allowed value for role is 'user' or 'moderator' or 'admin'")
        return value

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
    
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            bio=validated_data.get('bio', ''),
            role=validated_data.get('role', 'user'),
        )
#        user.set_password(validated_data['password'])
        if validated_data.get('role') == 'admin':
            user.is_staff = True
            user.is_superuser = True
            user.save()
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio', 'role', 'id']  # 'password']
