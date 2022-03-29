from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        "guid",
        "id",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "region",
        "city",
        "street",
        "zip_code",
        "is_staff",
        "user_type",
    )
    list_filter = (
        "is_active",
        "is_staff",
        "user_type",
    )
    list_editable = ("user_type",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "region",
                    "city",
                    "street",
                    "zip_code",
                    "user_type",
                    "user_status",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "groups",
                    "is_superuser",
                    "user_permissions",
                    "is_active",
                ),
            },
        ),
        (
            _("Important dates of user"),
            {"fields": ("last_login", "date_joined")},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "user_type",
                    "password1",
                    "password2",
                )
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
