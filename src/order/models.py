from django.db import models

from common.models import BaseModel


class OrderTime(BaseModel):
    interval = models.CharField(max_length=50)

    def __str__(self):
        return self.interval
