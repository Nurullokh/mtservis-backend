from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import PermissionDenied

from .constants import UserStatus, UserType
from .utils import send_email


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email field has to be given")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        email = extra_fields.pop("email")
        if self.all_with_deleted().filter(email=email).exists():
            self.all_with_deleted().get(email=email).delete()
        password = extra_fields.pop("password")
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", UserType.ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def delete_inactive_user(self, email):
        self.filter(email=email, is_active=False).delete()

    def register_user(self, data):
        self.delete_inactive_user(data["email"])
        data.setdefault("is_active", False)
        categories = data.pop("categories")
        user = self.create_user(**data)
        user.categories.set(categories)
        code = self.model.generate_code()
        self.model.set_cache(str(user.email), code)
        send_email.delay(user.email, code, "Your verification code is ")
        return user

    def validate_user_status(self, email):
        user = self.filter(email=email)
        if user.exists() and user.first().user_status == UserStatus.BLOCKED:
            raise PermissionDenied("You have been blocked!")
