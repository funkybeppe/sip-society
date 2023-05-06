from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products.as_view(), name='products'),
    path('product_detail/<product_id>/', views.ProductDetail.as_view(),
         name='product_detail'),
]
