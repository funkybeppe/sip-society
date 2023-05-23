from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Category(models.Model):
    """Category model"""
    class Meta:
        """Override Meta class"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """Method that returns category friendly_name"""
        return self.friendly_name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    is_premium = models.BooleanField()
    sku = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=False, blank=False)
    region = models.CharField(max_length=80, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    grapes = models.CharField(max_length=254, null=False, blank=False)
    year = models.PositiveIntegerField(null=False, blank=False)
    style = models.CharField(max_length=40, null=False, blank=False)
    code = models.CharField(max_length=6, unique=True)
    food_pairing = models.CharField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False,
                                blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.name)

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Override Meta method"""
        ordering = ["-created_at"]
