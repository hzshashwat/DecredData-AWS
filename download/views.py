from django.shortcuts import render
from rest_framework.views import APIView
from download.serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from upload.models import File
from rest_framework.response import Response

# Create your views here.
class UserFilesApiView(APIView):
    serializer_class = UserFilesSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format = None):
        try:
            file = File.objects.filter(owned_by = self.request.user)
            filejson = UserFilesSerializer(file, many=True)
            return Response({'files' : [filejson.data]})
        except Exception as e:
            return Response({'error' : str(e)})