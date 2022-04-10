import os
import pathlib
import uuid

from django.db import models

from common.models import BaseModel


def original_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f"{new_fname}/original{fpath.suffix}"


def thumbnail_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f"{new_fname}/150x150{fpath.suffix}"


class DocumentModel(BaseModel):
    file = models.FileField(upload_to="documents/")

    class Meta:
        ordering = ("-created_at",)

    @property
    def file_url(self):
        return self.file.url if self.file else None

    @property
    def file_name(self):
        return os.path.basename(self.file.name) if self.file else None


class ImageModel(BaseModel):
    file = models.ImageField(upload_to=original_upload_handler)
    thumbnail_150 = models.ImageField(
        upload_to=thumbnail_upload_handler, blank=True, null=True
    )

    class Meta:
        ordering = ("-created_at",)

    @property
    def image_url(self):
        return self.file.url if self.file else None


class VideoModel(BaseModel):
    file = models.FileField(upload_to=original_upload_handler)

    class Meta:
        ordering = ("-created_at",)

    @property
    def image_url(self):
        return self.file.url if self.file else None
