from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path("admin", admin.site.urls),
    path("api/v1", include("apps.authentications.rest.urls")),
]


urlpatterns += (
    re_path(
        r"^(?!api|media|static/).*", TemplateView.as_view(template_name="index.html")
    ),
)
