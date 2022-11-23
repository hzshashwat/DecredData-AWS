from django.urls import path
from upload.views import UploadFileApiView

urlpatterns = [
    path('upload/', UploadFileApiView.as_view(), name='upload')
]
