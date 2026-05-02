from django.views.generic import TemplateView 
from django.shortcuts import get_object_or_404
from apps.product.models import Category, Product, Slider


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('-id')[:10]
        context['products'] = Product.objects.all().order_by('-id')[:6]
        context['sliders'] = Slider.objects.all().order_by('-id')[:3]
        return context


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class NewsView(TemplateView):
    template_name = 'pages/blog.html'


class TeamView(TemplateView):
    template_name = 'pages/team.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'