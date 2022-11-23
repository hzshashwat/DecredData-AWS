from django.db import models
import os
from userprofiles.models import User

# Create your models here.
def create_path(instance, filename):
    return os.path.join('files',
        instance.owned_by.username,
        filename
    )

class File(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to=create_path)
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file_id = models.CharField(max_length=100, primary_key=True)
    urltoken = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    description = models.CharField(max_length=500)