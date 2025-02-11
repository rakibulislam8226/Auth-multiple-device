from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from ..views.auth import RegisterUserView, CustomTokenObtainPairView

urlpatterns = [
    path("/register", RegisterUserView.as_view(), name="register"),
    path("/login", CustomTokenObtainPairView.as_view(), name="login"),
    path("/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
