from rest_framework import serializers
from rest_framework.serializers import ValidationError

from technician.models import Technician


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = (
            "id",
            "user",
            "services",
            "experience",
            "resume",
        )
        read_only_fields = ("user",)

    def validate(self, attrs):
        user = self.context["request"].user
        if Technician.objects.filter(user=user).exists():
            raise ValidationError("You have already submitted!")
        return attrs
