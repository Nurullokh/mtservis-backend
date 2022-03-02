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
