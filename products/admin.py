from django.contrib import admin
from .models import Product, Category, SizeStock, RegularStock


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'has_sizes',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SizeStockAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'xs',
        's',
        'm',
        'l',
        'xl',
    )


class RegularStockAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'stock',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SizeStock, SizeStockAdmin)
admin.site.register(RegularStock, RegularStockAdmin)