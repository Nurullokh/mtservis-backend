from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/account/", include("account.urls"), name="account"),
    path("v1/", include("document.urls")),
    path("v1/", include("service.urls")),
    path("v1/", include("order.urls")),
    path("v1/", include("technician.urls")),
    path("v1/", include("blog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
