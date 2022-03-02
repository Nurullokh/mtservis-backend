from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import UserLoginSerializer


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
