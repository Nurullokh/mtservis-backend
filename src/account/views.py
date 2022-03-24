from django.contrib.auth import get_user_model
from django.core.cache import cache

from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import (
    ConfirmResgistrationSerializer,
    RegisterSerializer,
    UserLoginSerializer,
)
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
