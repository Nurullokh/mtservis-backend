from django.urls import path

from account.views import ConfirmRegistrationView, RegisterView, UserLoginView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "confirm-registration/",
        ConfirmRegistrationView.as_view(),
        name="confirm-registration",
    ),
]
