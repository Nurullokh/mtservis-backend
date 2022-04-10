from django.utils.translation import get_language

from rest_framework import serializers

from order.models import Order, OrderTime


class OrderTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTime
        fields = (
            "id",
            "interval",
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "time",
            "date",
            "address",
            "description",
            "brand",
            "service_type",
            "status",
        )
        read_only_fields = ("user",)

    def to_representation(self, instance):
        self.fields["time"] = serializers.CharField(source="time.interval")
        self.fields["brand"] = serializers.SerializerMethodField()
        self.fields["service_type"] = serializers.SerializerMethodField()
        self.fields["service"] = serializers.SerializerMethodField()
        return super(OrderSerializer, self).to_representation(instance)

    def get_brand(self, instance):
        if instance.brand:
            return getattr(instance.brand.name)
        return

    def get_service_type(self, instance):
        return getattr(instance.service_type, f"name_{get_language()}")

    def get_service(self, instance):
        return getattr(instance.service_type.service, f"name_{get_language()}")
