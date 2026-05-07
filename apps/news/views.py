from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import redirect
from django.db.models import Count

from apps.news.models import News, NewsComment


class NewsView(ListView):
    model = News
    template_name = 'pages/blog.html'
    context_object_name = 'news'
    paginate_by = 6

    def get_queryset(self):
        return News.objects.filter(
            is_active=True
        ).annotate(comments_count=Count('comments'))


class NewsDetailView(DetailView):
    model = News 
    template_name = 'single_pages/blog-single.html'
    context_object_name = 'news'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            NewsComment.objects.create(
                news=self.object,
                name = name,
                text = text
            )
        return redirect('news_detail', slug=self.object.slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-id')
        return context


class AboutView(TemplateView):
    template_name = 'pages/about.html'
