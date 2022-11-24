from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from upload import models, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid

# Create your views here.
domain_name = 'decreddata.herokuapp.com'
class UploadFileApiView(APIView):
    serializer_class = serializers.FileUploadSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            fileobj = serializers.FileUploadSerializers(data=request.data)
            if fileobj.is_valid():
                fileobj.validated_data['owned_by'] = self.request.user

                for file, filename in request.FILES.items():
                    fileobj.validated_data['filename'] = filename
                    fileobj.validated_data['filetype'] = file
                
                fileobj.validated_data['file_id'] = uuid.uuid4()
                fileobj.validated_data['urltoken'] = uuid.uuid4()
                file_id = fileobj.validated_data['file_id']
                fileobj.save()
                downloadlink = f'{domain_name}/file/download/{file_id}/'
                return Response({"message" : "File uploaded successfully.", 'downloadlink' : downloadlink})
            else :
                return Response({"message": fileobj.errors,
                "status": "Failed"
                })
        except Exception as e:
            return Response({'error' : str(e)})