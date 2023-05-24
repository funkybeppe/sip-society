from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, View
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from products.models import Category, Product

from wishlist.forms import SetWishlistRelation

from wishlist.models import WishlistLine


# Create your views here.
class WishList(LoginRequiredMixin, ListView):
    """
    A view that provides the wishlist of products
    """
    template_name = "wishlist/wishlist.html"
    model = WishlistLine

    def get(self, request):
        wishlist = Product.objects.filter(
            pk__in=WishlistLine.objects.filter(
                user=self.request.user).values_list('product'))
        categories = None
        is_premium = None
        sort = None
        direction = None
        # GET EVERY PRODUCT COUNT OF APPEARENCE IN WISHLISTLINE DATABASE
        wishlist_product_count = []
        products = Product.objects.filter(
            pk__in=WishlistLine.objects.filter(
                user=self.request.user).values_list(
                    'product'))

        for product in products:
            wishlist_product_count.append(
                {
                    'id': product.pk,
                    'count': WishlistLine.objects.filter(
                            product=product).count(),
                })

        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    products = products.annotate(lower_name=Lower('name'))
                if sortkey == 'category':
                    sortkey = 'category__name'
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)

            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('products'))

                queries = Q(name__icontains=query) | Q(region__icontains=query) | \
                    Q(country__icontains=query) | Q(grapes__icontains=query) | \
                    Q(style__icontains=query)
                products = products.filter(queries)

        current_sorting = f'{sort}_{direction}'

        context = {
            'wishlist': wishlist,
            'current_categories': categories,
            'is_premium': is_premium,
            'categories': categories,
            'current_sorting': current_sorting,
            'wishlist_product_count': wishlist_product_count
            }
        return render(request, 'wishlist/wishlist.html', context)


class AddProductToWishList(View):
    """
    A view that provides a form for creating a new entry in
    WishlistLine
    """
    def post(self, request, product_id):
        """Override post method"""
        redirect_url = request.POST.get('redirect_url')
        wishlist_form = SetWishlistRelation(data=request.POST)

        if wishlist_form.is_valid():
            user = request.user
            product = get_object_or_404(Product, pk=product_id)
            wishlist_form = WishlistLine(user=user, product=product)
            wishlist_form.save()

        return redirect(redirect_url)

    def get(self, request, product_id, *args, **kwargs):
        """Override get method to redirect to product details page"""
        return redirect('/products/product_detail/' + str(product_id))


class RemoveProductFromWishList(LoginRequiredMixin, DeleteView):
    """
    A view that deletes a WishlistLine entry from the database.
    The action is performed only if the authenticated user
    is the author of WishlistLine entry.
    """

    model = WishlistLine
    template_name = 'menu.html'

    def get_success_url(self):
        id_key = self.get_object().id
        return redirect('/products/product_detail/' + str(id_key))

    def get_object(self):
        return WishlistLine.objects.get(pk=self.kwargs.get('wishlist_id'))

    def get(self, request, *args, **kwargs):
        """Override get method to redirect to product details page"""
        id_key = self.get_object().id
        return redirect('/products/product_detail/' + str(id_key))

    def test_func(self):
        item = self.get_object()
        return self.request.user == item.user

    def delete(self, request, *args, **kwargs):
        wishlist_id = self.kwargs['wishlist_id']
        redirect_url = request.POST.get('redirect_url')
        wishlist = WishlistLine.objects.get(pk=wishlist_id)
        wishlist.delete()

        return redirect(redirect_url)
