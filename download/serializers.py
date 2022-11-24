from rest_framework import serializers
from upload.models import File

class UserFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'file', 'file_id', 'password', 'description', 'filetype']

class FileDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'description', 'filetype']

class FileSecurityCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['password',]

class FileSecurityCheckPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'file_id', 'filetype']