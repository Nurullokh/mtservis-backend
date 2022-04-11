import django_filters

from service.models import ServiceType


class ServiceTypeFilter(django_filters.FilterSet):
    class Meta:
        model = ServiceType
        fields = ("service",)
