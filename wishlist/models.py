"""
Wishlist App - Models
----------------
Models for Wishlist App.
"""
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

from products.models import Product


class WishlistLine(models.Model):
    """Model for WishlistLine object"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
