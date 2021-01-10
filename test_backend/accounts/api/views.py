from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializers import UserListSerializer

User = get_user_model()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()