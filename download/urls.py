from django.urls import path
from download.views import *

urlpatterns = [
    path('user/files/', UserFilesApiView.as_view(), name='userfiles'),
    path('file/download/<str:id>/', FileDownloadDescription.as_view(), name='filedownload'),
    path('file/download/<str:id>/securitycheck/', FileSecurityCheck.as_view(), name='filesecuritycheck'),
    path('file/decrypt/<str:urltoken>/download/', FinalDownload.as_view(), name='finaldownload')
]