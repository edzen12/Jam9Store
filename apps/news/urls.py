from django.urls import path 
from apps.news.views import NewsView, AboutView, NewsDetailView, NewsSearchView


urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('search/', NewsSearchView.as_view(), name='news_search'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('about/', AboutView.as_view(), name='about'),
]
