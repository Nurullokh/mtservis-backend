from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.models import User
from account.utils import validate_password
from document.serializers import ImageModelSerializer


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
            "profile_image",
        )

    def validate(self, attrs):
        if get_user_model().objects.filter(
            email=attrs["email"], is_active=True
        ):
            raise ValidationError("User with this email already exists.")

        return attrs

    def to_representation(self, instance):
        self.fields["profile_image"] = ImageModelSerializer()
        return super(RegisterSerializer, self).to_representation(instance)


class ConfirmResgistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.IntegerField()

    def validate_code(self, code):
        if code not in range(100000, 1000000):
            raise ValidationError("Invalid code!")
        return code


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs["email"]
        if not get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError("Email not registered")
        return attrs


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.IntegerField()

    def validate_code(self, code):
        if code not in range(100000, 1000000):
            raise ValidationError("Invalid Code")
        return code


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    verification_key = serializers.UUIDField()

    def validate(self, attrs):
        password = attrs["password"]
        validate_password(password)
        confirm_password = attrs["confirm_password"]
        if password != confirm_password:
            raise serializers.ValidationError("passwords do not match")
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    current_password = serializers.CharField()

    def validate(self, attrs):
        password = attrs["password"]
        confirm_password = attrs["confirm_password"]
        current_password = attrs["current_password"]
        user = self.context["request"].user
        if not user.check_password(current_password):
            raise serializers.ValidationError("Password is wrong")
        if password == current_password:
            raise serializers.ValidationError(
                "Password is similar with old one, "
                "please choose another password"
            )
        validate_password(password)
        if password != confirm_password:
            raise serializers.ValidationError("passwords did not match")
        return attrs


class LogOutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "region",
            "city",
            "street",
            "zip_code",
            "user_type",
            "email",
        )

        extra_kwargs = {
            "first_name": {
                "required": False,
                "allow_null": False,
            },
            "last_name": {
                "required": False,
                "allow_null": False,
            },
            "email": {"read_only": True},
            "user_type": {"read_only": True},
        }

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        action = kwargs["context"]["view"].action
        if action in ["list", "detail", "get_profile"]:
            self.fields["profile_image"] = ImageModelSerializer()
