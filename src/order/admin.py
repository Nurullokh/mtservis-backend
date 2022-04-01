from django.contrib import admin

from order.models import OrderTime


class OrderTimeAdmin(admin.ModelAdmin):
    model = OrderTime
    list_display = ("id", "interval")
    search_fields = ("interval",)


admin.site.register(OrderTime, OrderTimeAdmin)
