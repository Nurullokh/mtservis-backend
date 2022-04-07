from django.urls import path

from technician.views import TechnicianView

urlpatterns = [
    path(
        "technician-create/",
        TechnicianView.as_view(),
        name="technician-create",
    ),
]
