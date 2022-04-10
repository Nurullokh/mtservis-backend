from django.contrib import admin

from order.models import Order, OrderTime


class OrderTimeAdmin(admin.ModelAdmin):
    model = OrderTime
    list_display = ("id", "interval")
    search_fields = ("interval",)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = (
        "id",
        "user",
        "time",
        "date",
        "address",
        "description",
        "brand",
        "status",
        "technician",
    )
    search_fields = ("brand", "status")


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderTime, OrderTimeAdmin)
