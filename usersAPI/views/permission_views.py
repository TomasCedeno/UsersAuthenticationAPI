from rest_framework import generics

from usersAPI.models import Permission
from usersAPI.serializers import PermissionSerializer

class ListCreatePermissionView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class DeletePermissionView(generics.DestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer