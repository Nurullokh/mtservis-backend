import random
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.cache import cache
from django.core.mail import send_mail
from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.tokens import RefreshToken
from softdelete.models import SoftDeleteObject

from account.constants import Regions, UserStatus, UserType
from account.managers import UserManager
from document.models import ImageModel


class User(SoftDeleteObject, AbstractBaseUser, PermissionsMixin):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    region = models.CharField(choices=Regions.choices, max_length=20)
    city = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    user_type = models.CharField(choices=UserType.choices, max_length=15)
    profile_image = models.ForeignKey(
        ImageModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    user_status = models.CharField(
        choices=UserStatus.choices,
        default=UserStatus.ACTIVE,
        max_length=15,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}

    @classmethod
    def generate_code(cls):
        return random.randint(100000, 999999)

    @classmethod
    def set_cache(cls, key, val, ttl=300):
        cache.set(f"{key}", val, timeout=ttl)

    def update_user(self, data):
        with transaction.atomic():
            for key, val in data.items():
                setattr(self, key, val)
            self.save()
