from django.urls import path
from download.views import *

urlpatterns = [
    path('user/files', UserFilesApiView.as_view(), name='userfiles')
]
