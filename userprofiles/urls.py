from django.urls import path, include
from userprofiles.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('signup', UserViewSet, basename='signup')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileApiViewSet.as_view(), name='profile')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)