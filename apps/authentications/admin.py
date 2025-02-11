from django.contrib import admin
from .models import UserDevice

# Register your models here.


@admin.register(UserDevice)
class UserDeviceAdmin(admin.ModelAdmin):
    list_display = ["user", "device_name", "ip_address", "user_agent"]
    ordering = ("-created_at", "user")
    readonly_fields = ["created_at", "updated_at", "uid"]
