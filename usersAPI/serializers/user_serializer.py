from usersAPI.models.user import User
from usersAPI.models.rol import Rol
from usersAPI.serializers.rol_serializer import RolSerializer

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    roles = RolSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'lastName', 'roles']

    def create(self, validated_data):
        roles = validated_data.pop('roles')
        user = User.objects.create(**validated_data)

        for rol in roles:
            Rol.objects.create(user=user, **rol)
            
        return user

    