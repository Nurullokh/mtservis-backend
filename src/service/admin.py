from django.contrib import admin

from service.models import Brand, Service, ServiceType


class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ("id", "name_uz", "name_en", "name_ru", "icon")
    search_fields = (
        "name_en",
        "name_uz",
        "name_ru",
    )


class ServiceTypeAdmin(admin.ModelAdmin):
    model = ServiceType
    list_display = ("id", "name_uz", "name_en", "name_ru", "service")
    search_fields = (
        "name_en",
        "name_uz",
        "name_ru",
    )
    list_filter = ("service",)


class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ("id", "name", "service_type")
    search_fields = ("name",)


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Brand, BrandAdmin)
