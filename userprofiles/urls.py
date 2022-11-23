from django.urls import path, include
from userprofiles.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('signup', UserViewSet, basename='signup')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view(), name='login')
]
