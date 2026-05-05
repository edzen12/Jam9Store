from django.urls import path 
from apps.news.views import NewsView, AboutView


urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('about/', AboutView.as_view(), name='about'),
]
