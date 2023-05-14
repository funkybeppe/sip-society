from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
=======
    path('', views.Products.as_view(), name='products'),
    path('product_detail/<product_id>/', views.ProductDetail.as_view(),
         name='product_detail'),
>>>>>>> main
]
