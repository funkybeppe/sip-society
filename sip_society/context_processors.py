from django.core.serializers import serialize
from products.models import Product


def add_products_list_to_context(request):
    """Method to return a list of products as context"""
    return {
        'products_json': serialize('json', Product.objects.all())
    }
