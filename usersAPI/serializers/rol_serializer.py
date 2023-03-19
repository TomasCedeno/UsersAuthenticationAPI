from usersAPI.models.rol import Rol
from usersAPI.models.permission import Permission
from usersAPI.serializers.permission_serializer import PermissionSerializer

from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Rol
        fields = ['id', 'name', 'permissions']

    def create(self, validated_data):
        permisssions = validated_data.pop('permissions')
        rol = Rol.objects.create(**validated_data)

        for permission in permisssions:
            Permission.objects.create(rol=rol, **permission)

        return rol