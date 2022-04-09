from rest_framework import mixins, permissions
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet

from blog.models import Blog, BlogImages
from blog.serializers import (
    BlogImagesSerializer,
    BlogListSerializer,
    BlogSerializer,
)
from common.pagination import BlogPagination


class BlogViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all().order_by("-id")
    pagination_class = BlogPagination

    filter_backends = (SearchFilter,)
    search_fields = [
        "title",
    ]

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.permission_classes = (permissions.IsAdminUser,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return BlogListSerializer
        return self.serializer_class


class BlogImagesViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = BlogImagesSerializer
    queryset = BlogImages.objects.all()

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "delete"):
            self.permission_classes = (permissions.IsAdminUser,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()
