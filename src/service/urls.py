from django.urls import include, path

from rest_framework import routers

from service import views

router = routers.DefaultRouter()

router.register(r"service", views.ServiceViewSet, basename="service")


urlpatterns = [
    path("", include(router.urls)),
]
