from django.urls import include, path

from rest_framework import routers

from account import views
from account.views import (
    ChangePasswordView,
    ConfirmRegistrationView,
    ForgotPasswordView,
    LogOutView,
    RegisterView,
    ResetPasswordView,
    UserLoginView,
    VerifyResetPasswordView,
)

routers = routers.DefaultRouter()
routers.register(r"user", views.UserViewSet, basename="user")

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "confirm-registration/",
        ConfirmRegistrationView.as_view(),
        name="confirm-registration",
    ),
    path(
        "forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot-password",
    ),
    path(
        "verify-reset-password/",
        VerifyResetPasswordView.as_view(),
        name="verify-reset-password",
    ),
    path(
        "reset-password/", ResetPasswordView.as_view(), name="reset-password"
    ),
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("", include(routers.urls)),
]
