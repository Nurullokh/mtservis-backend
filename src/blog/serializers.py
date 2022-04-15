from django.conf import settings

from rest_framework import serializers

from blog.models import Blog, BlogImages
from document.serializers import ImageModelSerializer


class BlogImagesMiniSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source="image.file")

    class Meta:
        model = BlogImages
        fields = ("image",)


class BlogSerializer(serializers.ModelSerializer):
    share_url = serializers.CharField(read_only=True)

    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "description",
            "image",
            "blog_images",
            "share_url",
            "created_at",
        )
        read_only_fields = ("blog_images", "share_url")

    def __init__(self, *args, **kwargs):
        super(BlogSerializer, self).__init__(*args, **kwargs)
        action = kwargs["context"]["view"].action
        if action == "retrieve":
            self.fields["image"] = ImageModelSerializer()
            self.fields["blog_images"] = BlogImagesMiniSerializer(many=True)
            self.fields["share_url"] = serializers.SerializerMethodField()

    def get_share_url(self, obj):
        return settings.BLOG_SHORT_LINK + obj.title.replace(" ", "-")


class BlogImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImages
        fields = (
            "id",
            "blog",
            "image",
        )

    def __init__(self, *args, **kwargs):
        super(BlogImagesSerializer, self).__init__(*args, **kwargs)
        action = kwargs["context"]["view"].action
        if action in ["list", "retrieve"]:
            self.fields["image"] = ImageModelSerializer()


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "image",
            "created_at",
        )

    def __init__(self, *args, **kwargs):
        super(BlogListSerializer, self).__init__(*args, **kwargs)
        self.fields["image"] = ImageModelSerializer()
