from django.utils.translation import get_language

from rest_framework import serializers

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
            self.fields["icon"] = serializers.SerializerMethodField()

    def get_icon(self, obj):
        if obj.image:
            return obj.image.thumbnail_150.url
        return None


class ServiceListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ("id", "name", "icon")

    def to_representation(self, instance):
        self.fields["icon"] = serializers.SerializerMethodField()
        return super(ServiceListSerializer, self).to_representation(instance)

    def get_icon(self, instance):
        if instance.icon:
            return instance.icon.thumbnail_150.url
        return None

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
        self.fields["logo"] = serializers.SerializerMethodField()
        return super(ServiceTypeListSerializer, self).to_representation(
            instance
        )

    def get_logo(self, instance):
        if instance.logo:
            return instance.logo.thumbnail_150.url
        return None

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
