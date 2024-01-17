from django.contrib import admin
from . import models


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "product_qty")
    search_fields = ("user__username", "product__name")
    date_hierarchy = "created_at"


class WishListAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
    )
    search_fields = ("user__username", "product__name")
    date_hierarchy = "created_at"


# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.WishList, WishListAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "fname",
        "lname",
        "email",
        "phone",
    )
    search_fields = (
        "user__username",
        "fname",
        "lname",
        "email",
        "phone",
    )
    date_hierarchy = "created_at"


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "price",
        "quantity",
    )
    search_fields = (
        "order__id",
        "product__name",
    )


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemsAdmin)

admin.site.register(models.Profile)


admin.site.site_header = "Admin BGMP"
# ?Configurar el título (Administración del sitio)
admin.site.index_title = "Panel"
admin.site.site_title = "Administration"
