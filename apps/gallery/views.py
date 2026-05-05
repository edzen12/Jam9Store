from django.views.generic import TemplateView 


class GalleryView(TemplateView):
    template_name = 'pages/gallery.html'