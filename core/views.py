from django.contrib.auth import login, logout
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from core.models import User
from core.serializers import UserSerializer, CreateUserSerializer, LoginUserSerializer, UpdatePasswordSerializer


class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class LoginAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginUserSerializer

    def perform_create(self, serializer):
        login(request=self.request, user=serializer.save())

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)

        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordAPIView(UpdateAPIView):
    model = User
    serializer_class = UpdatePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
