from django.urls import path 
from apps.news.views import NewsView, AboutView, NewsDetailView


urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('about/', AboutView.as_view(), name='about'),
]
