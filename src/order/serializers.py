from rest_framework import serializers

from order.models import OrderTime


class OrderTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTime
        fields = (
            "id",
            "interval",
        )
