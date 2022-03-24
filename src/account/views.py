import uuid

from django.contrib.auth import get_user_model
from django.core.cache import cache

from rest_framework import permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    get_object_or_404,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import (
    ChangePasswordSerializer,
    ConfirmResgistrationSerializer,
    ForgotPasswordSerializer,
    RegisterSerializer,
    ResetPasswordSerializer,
    UserLoginSerializer,
    VerifyEmailSerializer,
)
from account.utils import send_email
from common.utils import ApiErrorsMixin


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class RegisterView(ApiErrorsMixin, CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.instance = get_user_model().objects.register_user(
            serializer.validated_data
        )


class ConfirmRegistrationView(APIView):
    serializer_class = ConfirmResgistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        instance = get_object_or_404(get_user_model(), email=data["email"])
        cache_code = cache.get(data["email"])
        if cache_code != data["code"]:
            return Response(
                {"status": "Code is not matching!"},
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )
        instance.is_active = True
        instance.save()
        return Response({"status": "Confirmed!"}, status=status.HTTP_200_OK)


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        instance = get_object_or_404(
            get_user_model(), email=validated_data["email"]
        )
        code = get_user_model().generate_code()
        get_user_model().set_cache(str(instance.email), code)
        send_email.delay(
            instance.email,
            code,
            "Your reset password code is ",
            instance.first_name,
        )
        return Response(serializer.validated_data)


class VerifyResetPasswordView(APIView):
    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        instance = get_object_or_404(
            get_user_model(), email=validated_data["email"]
        )
        cache_code = cache.get(instance.email)
        if cache_code != validated_data["code"]:
            raise ValidationError("Code expired or invalid")
        guid = uuid.uuid4()
        get_user_model().set_cache(key=guid, val=instance.email, ttl=86400)
        return Response(
            data={"verification_key": guid}, status=status.HTTP_200_OK
        )


class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = cache.get(data["verification_key"])
        if email is None:
            raise ValidationError("Guid expired or invalid")
        instance = get_user_model().objects.get(email=email)
        instance.set_password(data["password"])
        instance.save()
        OutstandingToken.objects.filter(user=instance).delete()
        cache.expire(data["verification_key"], timeout=1)
        return Response(status=status.HTTP_201_CREATED)


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        instance = self.request.user
        instance.set_password(serializer.validated_data["password"])
        instance.save()
        return Response(status=status.HTTP_201_CREATED)
