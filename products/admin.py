from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """Class for displaying products in admin panel"""
    list_display = (
        'sku',
        'name',
        'category',
        'country',
        'year',
        'price',
        'rating',
        'image',
    )
    readonly_fields = ('rating', )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Class for displaying categories in admin panel"""
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """Class for displaying reviews in admin panel"""
    list_display = (
        'product',
        'rating',
        'content',
        'created_by',
        'created_at',
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
