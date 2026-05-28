from django.urls import path
from apps.product.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', GlobalSearchView.as_view(), name='global_search'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path(
        'cart/remove/<int:product_id>/', 
        RemoveFromCartView.as_view(), name='remove_from_cart'
    ),
]
