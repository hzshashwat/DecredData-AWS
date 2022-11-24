from django.shortcuts import render
from rest_framework.views import APIView
from download.serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from upload.models import File
from rest_framework.response import Response

# Create your views here.
domain_name = 'decreddata.herokuapp.com'
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

class FileDownloadDescription(APIView):
    serializers_class = FileDownloadSerializer

    def get(self, request, id, format = None):
        try:
            file = File.objects.get(file_id = id)
            filejson = UserFilesSerializer(file)
            securitychecklink = f'{domain_name}/file/download/{id}/securitycheck/'
            return Response({'file' : [filejson.data], 'securitychecklink' : securitychecklink})
        except Exception as e:
            return Response({'error' : str(e)})

class FileSecurityCheck(APIView):
    serializers_class = FileSecurityCheckSerializer

    def post(self, request, id):
        try:
            fileobj = FileSecurityCheckSerializer(data=request.data)
            file = File.objects.get(file_id = id)
            if fileobj.is_valid():
                if fileobj.validated_data['password'] == file.password :
                    urltoken = file.urltoken
                    filejson = FileSecurityCheckPassSerializer(file)
                    downloadlinkpage = f'{domain_name}/file/decrypt/{urltoken}/download/'
                    return Response({'file' : [filejson.data], 'downloadlinkpage' : downloadlinkpage})
                else:
                    return Response({'message' : 'Incorrect password'})
        except Exception as e:
            return Response({'error' : str(e)})

class FinalDownload(APIView):
    serializers_class = FinalDownloadSerializer
    def get(self, request, urltoken):
        try:
            file = File.objects.get(urltoken = urltoken)
            filejson = UserFilesSerializer(file)
            fileurl = filejson.data['file']
            downloadlink = f'{domain_name}{fileurl}'
            return Response({'file' : [filejson.data], 'downloadlink' : downloadlink})
        except Exception as e:
            return Response({'error' : str(e)})