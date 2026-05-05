from django.views.generic import TemplateView 


class NewsView(TemplateView):
    template_name = 'pages/blog.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'
