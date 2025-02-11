from django.db import models
from django.contrib.auth import get_user_model

from common.models import BaseModelWithUID


User = get_user_model()


class UserDevice(BaseModelWithUID):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.device_name} ({self.ip_address})"
