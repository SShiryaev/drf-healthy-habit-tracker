from django.urls import path
from rest_framework_simplejwt import views

from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path(
        'login/',
        views.TokenObtainPairView.as_view(),
        name='login'
    ),
    path(
        'token/refresh/',
        views.TokenRefreshView.as_view(),
        name='token-refresh'
    ),
    path(
        'registration/',
        UserCreateAPIView.as_view(),
        name='user-registration'
    ),
]
