from django.urls import path, include


urlpatterns = [
    path("", include("apps.authentications.rest.urls.auth")),
]
