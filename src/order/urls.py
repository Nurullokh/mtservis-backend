from django.urls import include, path

from rest_framework import routers

from order import views

routers = routers.DefaultRouter()

routers.register(r"order-time", views.OrderTimeViewSet, basename="order-time")

urlpatterns = [
    path("", include(routers.urls)),
]
