from django.urls import path
from apps.product.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', GlobalSearchView.as_view(), name='global_search'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product_detail')
]
