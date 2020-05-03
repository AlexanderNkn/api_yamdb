from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)
    role = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio', 'role']