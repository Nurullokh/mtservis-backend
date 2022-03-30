from django.contrib import admin

from service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ("id", "name_uz", "name_en", "name_ru", "icon")
    search_fields = (
        "name_en",
        "name_uz",
        "name_ru",
    )


admin.site.register(Service, ServiceAdmin)
