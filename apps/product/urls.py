from django.urls import path
from apps.product.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoryView.as_view(), name='categories'),
]
