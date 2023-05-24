from django.contrib import admin

# Register your models here.
"""
Wishlist App - Admin
----------------
Admin Configuration for Wishlist App.
"""
from django.contrib import admin

from wishlist.models import WishlistLine


class WishlistLineAdmin(admin.ModelAdmin):
    """Class for displaying wishlist lines in admin panel"""
    list_display = (
        'user',
        'product',
    )


admin.site.register(WishlistLine, WishlistLineAdmin)
