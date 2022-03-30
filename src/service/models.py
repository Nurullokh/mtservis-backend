from django.db import models

from common.models import BaseModel
from document.models import ImageModel


class Service(BaseModel):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    icon = models.ForeignKey(
        ImageModel, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name_en


class ServiceType(BaseModel):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service_types"
    )

    def __str__(self):
        return self.name_en


class Brand(BaseModel):
    name = models.CharField(max_length=255)
    service_type = models.ForeignKey(
        ServiceType, on_delete=models.CASCADE, related_name="brands"
    )

    def __str__(self):
        return self.name
