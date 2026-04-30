from django.urls import path
from apps.product.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('news/', NewsView.as_view(), name='news'),
    path('team/', TeamView.as_view(), name='team'),
]
