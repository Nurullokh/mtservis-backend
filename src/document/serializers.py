from rest_framework import serializers

from document.models import ImageModel


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = (
            "id",
            "file",
            "thumbnail_150",
        )
        read_only_fields = ("thumbnail_150",)


class ImageModelMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = (
            "id",
            "file",
        )


class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = (
            "id",
            "file",
        )
