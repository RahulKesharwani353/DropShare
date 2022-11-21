from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', HandleFileUpload.as_view()),
    path('share/', HandelShare.as_view()),
    path('my-uploads/', HandleFileUpload.as_view()),
]