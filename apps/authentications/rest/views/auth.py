import json

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.timezone import now

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from common.permissions import IsUnauthenticated
from common.utils import create_response

from ..serializers.auth import UserSerializer

from ...models import UserDevice

User = get_user_model()


# User Registration View
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [IsUnauthenticated]

    def post(self, request, *args, **kwargs):
        """
        During login, save user device details
        """
        try:
            response = super().post(request, *args, **kwargs)
            if response.status_code == 200:
                user = self.get_user(request)
                ip_address = self.get_client_ip(request)
                user_agent = request.headers.get("User-Agent", "Unknown Device")
                device_name = self.extract_device_name(user_agent)
                device, created = UserDevice.objects.get_or_create(
                    user=user,
                    ip_address=ip_address,
                    user_agent=user_agent,
                    defaults={"device_name": device_name},
                )
                if not created:
                    device.last_active = now()
                    device.save()

            return response
        except Exception as e:
            return create_response(
                status_bool=False,
                message="Invalid username or password",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    def get_user(self, request):
        """Get user from login request"""
        data = request.data
        return authenticate(
            username=data.get("username"), password=data.get("password")
        )

    def get_client_ip(self, request):
        """Get IP address of the user"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")

    def extract_device_name(self, user_agent):
        """Extract device name from User-Agent string"""
        if "Windows" in user_agent:
            return "Windows PC"
        elif "Macintosh" in user_agent:
            return "MacBook / iMac"
        elif "iPhone" in user_agent:
            return "iPhone"
        elif "Android" in user_agent:
            return "Android Device"
        elif "iPad" in user_agent:
            return "iPad"
        elif "Linux" in user_agent:
            return "Linux PC"
        elif "Bot" in user_agent:
            return "Bot"
        return "Unknown Device"
