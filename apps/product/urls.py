from django.urls import path
from apps.product.views import HomeView, ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]
