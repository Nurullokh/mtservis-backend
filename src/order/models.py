from django.db import models

from account.models import User
from common.models import BaseModel
from order.constants import OrderStatus
from service.models import Brand, ServiceType
from technician.models import Technician


class OrderTime(BaseModel):
    interval = models.CharField(max_length=50)

    def __str__(self):
        return self.interval


class Order(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders"
    )
    time = models.ForeignKey(
        OrderTime, on_delete=models.SET_NULL, related_name="orders", null=True
    )
    date = models.DateField()
    address = models.CharField(max_length=1024)
    description = models.TextField()
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="orders",
        null=True,
        blank=True,
    )
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.SET_NULL,
        related_name="orders",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=25, choices=OrderStatus.choices, default=OrderStatus.NEW
    )
    technician = models.ForeignKey(
        Technician,
        on_delete=models.SET_NULL,
        related_name="orders",
        null=True,
        blank=True,
    )
