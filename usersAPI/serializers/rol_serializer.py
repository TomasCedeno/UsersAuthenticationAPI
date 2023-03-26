from usersAPI.models.rol import Rol
from usersAPI.models.permission import Permission
from usersAPI.serializers.permission_serializer import PermissionSerializer

from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Rol
        fields = ['id', 'name', 'permissions']