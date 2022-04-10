from django.db import models

from account.models import User
from common.models import BaseModel
from document.models import DocumentModel
from service.models import Service


class Technician(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="technician"
    )
    services = models.ManyToManyField(Service, related_name="technicians")
    experience = models.PositiveIntegerField()
    resume = models.ForeignKey(
        DocumentModel,
        on_delete=models.SET_NULL,
        related_name="technicians",
        null=True,
        blank=True,
    )
