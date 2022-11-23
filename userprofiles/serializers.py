from rest_framework import serializers
from userprofiles.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'username', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'} #To show dots not text while typing password
            }
        }