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
            "created_at",
        )

    def __init__(self, *args, **kwargs):
        super(ServiceSerializer, self).__init__(*args, **kwargs)
        action = kwargs["context"]["view"].action
        if action == "retrieve":
            self.fields["icon"] = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return obj.image.thumbnail_150.url
        return None


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id",)


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = (
            "id",
            "name_uz",
            "name_ru",
            "name_en",
            "service",
            "created_at",
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
    class Meta:
        model = ServiceType
        fields = ("id",)


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
    class Meta:
        model = Brand
        fields = ("id",)
