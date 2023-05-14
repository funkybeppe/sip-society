import urllib
import json
from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Sum
from django_countries.data import COUNTRIES
from django.contrib import messages
from django.core.serializers import serialize

from products.models import Product, Category


class Products(ListView):
    """ A view to show all products, including sorting and search queries """
    template_name = "products/products.html"
    model = Product
    paginate_by = 12
    context_object_name = "products"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all().order_by('style')
        return context

    def get(self, request):
        products = Product.objects.all().order_by('style')
        query = None
        category = None
        is_premium = None
        premium_style = None
        filters = {}
        remove_filter = None
        sort = None
        direction = None

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            if sortkey != 'best_sellers' and 'rating' not in sortkey:
                products = products.order_by(sortkey)
            elif sortkey == 'best_sellers':
                # SORT PRODUCTS BY SUM OF PRODUCTS QUANTITY IN ORDERLINES
                products = products.annotate(orders_products=Sum(
                    ('orderline__quantity'))).order_by('-orders_products')
            elif 'rating' in sortkey:
                if direction == 'asc':
                    products = products.order_by(
                        F('rating').asc(nulls_last=True))
                elif direction == 'desc':
                    products = products.order_by(
                        F('rating').desc(nulls_last=True))

        if sort == 'best_sellers':
            current_sorting = sort
        else:
            current_sorting = f'{sort}_{direction}'

        # CREATE DINAMIC QUERY FOR FILTERING PRODUCTS
        filter_options = ['category', 'style', 'grapes', 'year',
                          'country', 'region', 'food_pairing', 'is_premium']
        filter_clauses = {}
        for key, value in request.GET.items():
            if key in filter_options:
                if key not in ('category', 'country', 'grapes',
                               'food_pairing'):
                    filter_clauses[key] = value
                else:
                    if key == 'category':
                        category = get_object_or_404(
                            Category, name=value)
                        filter_clauses[key] = category
                    if key == 'country':
                        country_value = None
                        for c_key, c_value in COUNTRIES.items():
                            if c_value == value:
                                country_value = c_key
                        filter_clauses[key] = country_value
                    if key in ('grapes', 'food_pairing'):
                        filter_clauses[key+"__contains"] = value

        if filter_clauses:
            products = products.filter(**filter_clauses)
            for key, value in filter_clauses.items():
                if key == 'category':
                    category_name = request.GET['category']
                    category = get_object_or_404(Category, name=category_name)
                    # ADD CATEGORY FILTER TO FILTER CONTEXT
                    if 'filter' in request.GET and\
                        request.get_full_path().find('filter') < \
                       request.get_full_path().find('category'):
                        filters['category'] = 'CATEGORY - ' + \
                                              category.get_friendly_name()
                        category = None
                # ADD STYLE FILTER TO FILTER CONTEXT
                elif key == 'style':
                    deluxe_style = request.GET['style']
                    filters['style'] = 'STYLE OF WINE - ' + premium_style
                # ADD GRAPE VARIETY FILTER TO FILTER CONTEXT
                elif 'grapes' in key:
                    grape = request.GET['grapes']
                    filters['grapes'] = 'GRAPE VARIETY - ' + grape
                # ADD YEAR FILTER TO FILTER CONTEXT
                elif key == 'year':
                    year = request.GET['year']
                    filters['year'] = 'YEAR - ' + year
                # ADD COUNTRY FILTER TO FILTER CONTEXT
                elif key == 'country':
                    country = request.GET['country']
                    filters['country'] = 'COUNTRY - ' + country
                # ADD REGION FILTER TO FILTER CONTEXT
                elif key == 'region':
                    region = request.GET['region']
                    filters['region'] = 'REGION - ' + region
                # ADD FOOD FILTER TO FILTER CONTEXT
                elif 'food_pairing' in key:
                    food = request.GET['food_pairing']
                    filters['food_pairing'] = 'FOOD PAIRING - ' + food

        # HANDLE SEARCH QUERIES
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You did not enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(region__icontains=query) | \
                Q(country__icontains=query) | Q(grapes__icontains=query) | \
                Q(style__icontains=query)
            products = products.filter(queries)

        # ADD IS_DELUXE VALUE TO CONTEXT
        if 'is_premium' in request.GET:
            premium = request.GET['is_premium']
            is_premium = premium

        # ADD FILTERS LISTS TO CONTEXT FOR FILTERS DROPDOWNS
        categories = Category.objects.filter(
            id__in=products.values_list(
                'category', flat=True).distinct()).order_by('name')

        premium_styles = products.values_list(
            'style', flat=True).distinct().order_by('style')

        grapes_list = []
        for grapes in products.values_list('grapes', flat=True):
            grapes_values = grapes.split(', ')
            grapes_list.extend(grapes_values)
        grapes_list = [*set(grapes_list)]
        grapes_list.sort()

        years_list = products.values_list(
            'year', flat=True).distinct().order_by('-year')

        regions_list = products.values_list(
            'region', flat=True).distinct().order_by('region')

        countries_list = [COUNTRIES[country_code] for country_code
                          in products.values_list(
                              'country', flat=True).distinct().order_by(
                                  'country')]

        food_pairings_list = []
        for food in products.values_list('food_pairing', flat=True):
            food_values = food.split(', ')
            food_pairings_list.extend(food_values)
        food_pairings_list = [*set(food_pairings_list)]
        food_pairings_list.sort()

        # ADD FILTER PARAMETER TO CURRENT URL ONLY ONCE
        current_url = request.get_full_path()
        if '?' in current_url:
            current_url += '&'
        else:
            current_url += '?'
        if 'filter' not in current_url:
            current_url += 'filter=True&'

        # REMOVE FILTERS FROM URL TO BE USED IN TEMPLATE HREFS WHEN
        # 'CLEAR ALL' BUTTON IS ACTIVE
        current_url_no_filters = request.path_info
        parameters = request.GET.copy()
        parameters_list = json.loads(json.dumps(request.GET)).items()
        is_filter = False
        for key, value in parameters_list:
            if key == 'filter':
                is_filter = True
                del parameters['filter']
            if is_filter is True and key in filter_options:
                del parameters[key]
        if parameters:
            current_url_no_filters += '?' + urllib.parse.urlencode(parameters)

        # CHECK IF THERE IS ONLY ONE FILTER APPLIED AND CREATE BOOLEAN VALUE
        # TO BE ADDED TO CONTEXT
        parameters = []
        for key, value in request.GET.items():
            parameters.append(key)
        if parameters:
            if parameters[len(parameters)-2] == 'filter' and \
               parameters[len(parameters)-1] in filter_options:
                remove_filter = True
            else:
                for i in range(0, len(parameters)-2):
                    if parameters[i] == 'filter' and \
                       parameters[i+1] in filter_options:
                        one_filter = True
                        for j in range(i+2, len(parameters)):
                            if parameters[j] in filter_options:
                                one_filter = False
                                break
                        if one_filter is True:
                            remove_filter = True

        context = {
            'products': products,
            'search_term': query,
            'current_category': category,
            'is_premium': is_premium,
            'categories': categories,
            'premium_styles': premium_styles,
            'premium_style': premium_style,
            'filters_list': filters,
            'grapes_list': grapes_list,
            'years_list': years_list,
            'regions_list': regions_list,
            'countries_list': countries_list,
            'food_pairing_list': food_pairings_list,
            'current_url': current_url,
            'current_url_no_filters': current_url_no_filters,
            'remove_filter': remove_filter,
            'current_sorting': current_sorting,
            }
        return render(request, 'products/products.html', context)


class ProductDetail(ListView):
    """ A view to show a product details including reviews """
    template_name = "products/product_detail.html"

    def get(self, request, product_id):
        """Override get method"""
        product = get_object_or_404(Product, pk=product_id)
        current_review = None
        current_wishlist_line = None

        # if request.user.is_authenticated and len(
        #     ReviewModel.objects.filter(
        #         Q(author=request.user) & Q(product=product))) == 1:
        #     current_review = ReviewModel.objects.get(
        #         author=self.request.user, product=product)
        if product.is_premium is True:
            update_product_form = AddUpdateProductForm(
                is_premium=True, initial={
                    'country': product.country
                    },
                instance=product, prefix='UPDATE')
    
        context = {
            'product': product,
            'product_json': serialize('json', Product.objects.filter(pk=product.pk)),
        }

        return render(request, 'products/product_detail.html', context)
