from django.views.generic import TemplateView, DetailView
from django.db.models import Q 
from django.db.models import Count, Prefetch
from apps.product.models import Category, Product, Slider
from apps.news.models import News


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('-id')[:10]
        context['products'] = Product.objects.all().order_by('-id')[:6]
        context['sliders'] = Slider.objects.all().order_by('-id')[:3]
        return context


class CategoryView(TemplateView):
    template_name = 'pages/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.annotate(
            products_count=Count('products')
        ).filter(products_count__gt=0).prefetch_related(
            Prefetch(
                'products',
                queryset=Product.objects.all(),
                to_attr='all_products'
            )
        )
        context['categories'] = categories
        return context


class GlobalSearchView(TemplateView):
    template_name = 'pages/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '').strip()

        products = Product.objects.none() 
        news_list = News.objects.none()

        if query:
            products = Product.objects.select_related(
                'category'
            ).filter(
                Q(name__icontains=query) |
                Q(sku__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )

            news_list = News.objects.filter(
                Q(title__icontains=query) |
                Q(desc__icontains=query), is_active=True
            ).distinct()
        context['query'] = query
        context['products'] = products 
        context['news_list'] = news_list
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'single_pages/shop-single.html'
    context_object_name = 'product'

    queryset = Product.objects.select_related('category')
    