from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import RegisterSerializer, UserLoginSerializer
from common.utils import ApiErrorsMixin


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class RegisterView(ApiErrorsMixin, CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.instance = get_user_model().objects.register_user(
            serializer.validated_data
        )
