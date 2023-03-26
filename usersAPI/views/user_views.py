from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from usersAPI.serializers.user_serializer import UserSerializer
from usersAPI.models.user import User, Rol

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"email": request.data["email"],
                    "password": request.data["password"]}

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


class UserDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def isItself(self, request, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        return valid_data['user_id'] != kwargs['pk']

    def get(self, request, *args, **kwargs):
        if self.isItself(request, **kwargs):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if self.isItself(request, **kwargs):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().patch(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if self.isItself(request, **kwargs):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if self.isItself(request, **kwargs):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)


class AddRolToUserView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=self.kwargs.get('pk'))
        rol = get_object_or_404(Rol, id=request.data["rolId"])
        user.roles.add(rol)
        user.save()

        return Response({"detail": "Rol added to user successfully"}, status=status.HTTP_200_OK)


class RemoveRolFromUserView(views.APIView):
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=self.kwargs.get('pk'))
        rol = get_object_or_404(Rol, id=request.data["rolId"])
        user.roles.remove(rol)
        user.save()

        return Response({"detail": "Rol removed from user successfully"}, status=status.HTTP_200_OK)