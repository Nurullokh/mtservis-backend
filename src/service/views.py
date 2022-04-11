import django_filters
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from service.filter import ServiceTypeFilter
from service.models import Brand, Service, ServiceType
from service.serializers import (
    BrandListSerializer,
    BrandSerializer,
    ServiceListSerializer,
    ServiceSerializer,
    ServiceTypeListSerializer,
    ServiceTypeSerializer,
)


class ServiceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by("order_number")

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.permission_classes = (permissions.IsAdminUser,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceListSerializer
        return self.serializer_class


class ServiceTypeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all().order_by("order_number")
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ServiceTypeFilter

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.permission_classes = (permissions.IsAdminUser,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceTypeListSerializer
        return self.serializer_class


class BrandViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):

    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.permission_classes = (permissions.IsAdminUser,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return BrandListSerializer
        return self.serializer_class
