from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.models import User


class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        User.objects.validate_user_status(attrs["email"])
        tokens = super().validate(attrs)
        attrs = {
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "tokens": tokens,
        }

        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "first_name",
            "last_name",
            "user_type",
            "password",
            "phone_number",
            "region",
            "city",
            "street",
            "zip_code",
        )

    def validate(self, attrs):
        if get_user_model().objects.filter(
            email=attrs["email"], is_active=True
        ):
            raise ValidationError("User with this email already exists.")

        return attrs
