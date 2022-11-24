from rest_framework import serializers
from upload.models import File

class UserFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'file', 'file_id', 'password', 'description', 'filetype']