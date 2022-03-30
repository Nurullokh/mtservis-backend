from rest_framework import serializers

from service.models import Service


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
            self.fields["image"] = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return obj.image.thumbnail_150.url
        return None


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id",)
