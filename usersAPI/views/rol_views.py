from rest_framework import status, views, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from usersAPI.models import Rol, Permission
from usersAPI.serializers import RolSerializer

class ListCreateRolView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class DeleteRolView(generics.DestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class AddPermissionToRolView(views.APIView):

    def post(self, request, *args, **kwargs):
        rol = get_object_or_404(Rol, id=self.kwargs.get('pk'))
        permission = get_object_or_404(Permission, id=request.data["permissionId"])
        rol.permissions.add(permission)
        rol.save()

        return Response({"detail": "Permission added to rol successfully"}, status=status.HTTP_200_OK)


class RemovePermissionFromRolView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        rol = get_object_or_404(Rol, id=self.kwargs.get('pk'))
        permission = get_object_or_404(Permission, id=request.data["permissionId"])
        rol.permissions.remove(permission)
        rol.save()

        return Response({"detail": "Permission removed from rol successfully"}, status=status.HTTP_200_OK)
