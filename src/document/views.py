import os

from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from document.models import DocumentModel, ImageModel, VideoModel
from document.serializers import (
    DocumentModelSerializer,
    ImageModelSerializer,
    VideoModelSerializer,
)
from document.tasks import create_thumbnail_images


class UploadImageViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet
):
    serializer_class = ImageModelSerializer
    queryset = ImageModel.objects.all().order_by("-created_at")

    def create(self, request, *args, **kwargs):
        error_list = list()
        if request.FILES and request.FILES.getlist("images"):
            objs = list()
            for file in request.FILES.getlist("images"):
                ct = os.path.splitext(file.name.lower())[1]
                if ct not in (".jpg", ".jpeg", ".png", ".svg"):
                    raise ValidationError(
                        "available format (.jpg, .jpeg, .png)"
                    )
                image = ImageModel(file=file)
                objs.append(image)
            images = ImageModel.objects.bulk_create(objs)
            serializer = self.serializer_class(images, many=True)
            obj_ids = [i.id for i in images]
            create_thumbnail_images.delay(obj_ids)
            return Response(serializer.data)
        error_list.append("images can not be null")
        if error_list:
            raise ValidationError(error_list)


class UploadVideoViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet
):
    serializer_class = VideoModelSerializer
    queryset = VideoModel.objects.all().order_by("-created_at")

    def create(self, request, *args, **kwargs):
        error_list = list()
        if request.FILES and request.FILES.getlist("videos"):
            objs = list()
            for file in request.FILES.getlist("videos"):
                ct = os.path.splitext(file.name.lower())[1]
                if ct not in (".mp4", ".mov", ".wmv", ".avi", ".mkv"):
                    raise ValidationError(
                        "available format (.jpg, .jpeg, .png)"
                    )
                video = VideoModel(file=file)
                objs.append(video)
            videos = VideoModel.objects.bulk_create(objs)
            serializer = self.serializer_class(videos, many=True)
            return Response(serializer.data)
        error_list.append("images can not be null")
        if error_list:
            raise ValidationError(error_list)


class UploadDocumentViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet
):
    serializer_class = DocumentModelSerializer
    queryset = DocumentModel.objects.all()
    permission_classes = (IsAuthenticated,)
