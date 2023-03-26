from usersAPI.models.user import User
from usersAPI.models.rol import Rol
from usersAPI.serializers.rol_serializer import RolSerializer

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    roles = RolSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'lastName', 'roles']

    