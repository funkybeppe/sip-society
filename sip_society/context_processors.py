from django.core.serializers import serialize
from newsletter.forms import AddSubscriber
from products.models import Product


def add_products_list_to_context(request):
    """Method to return a list of products as context"""
    return {
        'products_json': serialize('json', Product.objects.all())
    }


def add_subscription_form_to_context(request):
    """Method to return subscription form as context"""
    return {
        'add_subscriber_form': AddSubscriber
    }
