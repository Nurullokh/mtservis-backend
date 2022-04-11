from django.utils.translation import get_language

from rest_framework import serializers

from document.serializers import ImageModelSerializer
from service.models import Brand, Service, ServiceType


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            "id",
            "name_uz",
            "name_ru",
            "name_en",
            "icon",
        )

    def __init__(self, *args, **kwargs):
        super(ServiceSerializer, self).__init__(*args, **kwargs)
        action = kwargs["context"]["view"].action
        if action == "retrieve":
            self.fields["icon"] = ImageModelSerializer()


class ServiceListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ("id", "name", "icon")

    def to_representation(self, instance):
        self.fields["icon"] = ImageModelSerializer()
        return super(ServiceListSerializer, self).to_representation(instance)

    def get_name(self, instance):
        return getattr(instance, f"name_{get_language()}")


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = (
            "id",
            "name_uz",
            "name_ru",
            "name_en",
            "service",
        )

    def __init__(self, *args, **kwargs):
        super(ServiceTypeSerializer, self).__init__(*args, **kwargs)
        action = kwargs["context"]["view"].action
        if action == "retrieve":
            self.fields["service"] = serializers.SerializerMethodField()

    def get_service(self, obj):
        if obj.service:
            return obj.service.name_en
        return None


class ServiceTypeListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceType
        fields = ("id", "name", "logo")

    def to_representation(self, instance):
        self.fields["logo"] = ImageModelSerializer()
        return super(ServiceTypeListSerializer, self).to_representation(
            instance
        )

    def get_name(self, instance):
        return getattr(instance, f"name_{get_language()}")


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "service_type",
        )

    def __init__(self, *args, **kwargs):
        super(BrandSerializer, self).__init__(*args, **kwargs)
        action = kwargs["context"]["view"].action
        if action == "retrieve":
            self.fields["service_type"] = serializers.SerializerMethodField()

    def get_service_type(self, obj):
        if obj.service_type:
            return obj.service_type.name_en
        return None


class BrandListSerializer(serializers.ModelSerializer):
    service_type = ServiceTypeListSerializer()

    class Meta:
        model = Brand
        fields = ("id", "name", "service_type")
