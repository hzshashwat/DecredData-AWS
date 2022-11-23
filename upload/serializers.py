from rest_framework import serializers
from upload.models import File

class FileUploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('filename', 'file', 'owned_by', 'file_id', 'urltoken', 'password', 'description', 'filetype')
        extra_kwargs = {
            'filename' : {'read_only' : True},
            'owned_by' : {'read_only' : True},
            'file_id' : {'read_only' : True},
            'urltoken' : {'read_only' : True},
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'} #To show dots not text while typing password
            },
            'filetype' : {'read_only' : True}
            }