import json

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.timezone import now

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ...models import UserDevice
from ..serializers.auth import UserSerializer

User = get_user_model()


# User Registration View
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = self.get_user(request)
            ip_address = self.get_client_ip(request)
            user_agent = request.headers.get("User-Agent", "Unknown Device")

            # Extracting device name from User-Agent
            device_name = self.extract_device_name(user_agent)

            # Save or update device info
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
