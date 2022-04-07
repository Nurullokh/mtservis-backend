from django.contrib import admin

from technician.models import Technician


class TechnicianAdmin(admin.ModelAdmin):
    model = Technician
    fields = (
        "user",
        "experience",
        "services",
        "resume",
    )
    search_fields = ("user", "service")


admin.site.register(Technician, TechnicianAdmin)
