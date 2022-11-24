from django.urls import path
from upload.views import UploadFileApiView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('upload/', UploadFileApiView.as_view(), name='upload')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)