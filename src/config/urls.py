from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/account/", include("account.urls"), name="account"),
    path("v1/", include("document.urls")),
    path("v1/", include("service.urls")),
]
