from rest_framework.views import APIView
from userprofiles import serializers, models
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

class ProfileApiViewSet(APIView):
    serializer_class = serializers.ProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format = None):
        try:
            profile = models.Profile.objects.get(user = self.request.user)
            profilejson = serializers.ProfileSerializer(profile)
            return Response({"message" : [profilejson.data]})

        except Exception as e:
            return Response({"error": str(e)})

    def put(self, request):
        try :
            profile = models.Profile.objects.get(user = self.request.user)
            profileobj = serializers.ProfileSerializer(profile, data=request.data)
            if profileobj.is_valid():
                profileobj.save()
                return Response({"message" : "Profile info updated."})
            else :
                return Response({"message": profileobj.errors,
                "status": "Failed"
                })
        except:
            profileobj = serializers.ProfileSerializer(data=request.data)
            if profileobj.is_valid():
                profileobj.validated_data['user'] = self.request.user
                profileobj.save()
                return Response({"message" : "Profile info updated."})
            else :
                return Response({"message": profileobj.errors,
                "status": "Failed"
                })