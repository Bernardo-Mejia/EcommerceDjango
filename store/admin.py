from django.contrib import admin
from . import models

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', "product", 'product_qty')
    search_fields = ("user__username", "product__name")
    date_hierarchy = ('created_at')

class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', "product",)
    search_fields = ("user__username", "product__name")
    date_hierarchy = ('created_at')

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.WishList, WishListAdmin)


admin.site.site_header = "Admin BGMP"
# ?Configurar el título (Administración del sitio)
admin.site.index_title = "Panel"
admin.site.site_title = "Administration"