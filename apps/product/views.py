from django.views import View
from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q 
from django.db.models import Count, Prefetch
from django.shortcuts import redirect
from apps.product.models import Category, Product, Slider, ProductReview
from apps.news.models import News
from apps.testimonials.models import Review


class AddToCartView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', {})
        product_id = str(product.id)
        if product_id in cart:
            cart[product_id]['quantity'] += 1
        else:
            cart[product_id] = {
                'id': product.id,
                'name': product.name,
                'price': float(product.price),
                'image': product.image.url if product.image else '',
                'quantity': 1,
                'slug': product.slug,
            }
        request.session['cart'] = cart 
        return redirect(request.META.get('HTTP_REFERER'))
    

class RemoveFromCartView(View):
    def get(self, request, product_id):
        cart = request.session.get('cart', {})
        product_id = str(product_id)
        if product_id in cart:
            del cart[product_id]
        request.session['cart'] = cart 
        return redirect(request.META.get('HTTP_REFERER'))
    

class CartView(TemplateView):
    template_name = 'pages/cart.html'


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('-id')[:10]
        context['products'] = Product.objects.all().order_by('-id')[:6]
        context['reviews'] = Review.objects.all().order_by('-id')[:6]
        context['news'] = News.objects.all().order_by('-id')[:8]
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        if name and email and text:
            ProductReview.objects.create(
                product=self.object,
                name=name,
                email=email,
                text=text,
            )
        return redirect('product_detail', slug=self.object.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        return context 
    