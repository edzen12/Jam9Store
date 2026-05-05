from django.views.generic import TemplateView, ListView, DetailView
from apps.news.models import News


class NewsView(ListView):
    model = News
    template_name = 'pages/blog.html'
    context_object_name = 'news'


class AboutView(TemplateView):
    template_name = 'pages/about.html'
