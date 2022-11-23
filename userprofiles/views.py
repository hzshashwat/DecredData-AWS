from django.shortcuts import render
from rest_framework.views import APIView
from userprofiles import serializers, models
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES