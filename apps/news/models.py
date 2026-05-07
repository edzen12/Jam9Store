from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    desc = CKEditor5Field('Описание', config_name='extends')
    slug = models.SlugField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='новость'
        verbose_name_plural='Новости'
        ordering = ['-id']


class NewsComment(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.news.title}"
    
    class Meta:
        verbose_name='комментарии'
        verbose_name_plural='Комментарии'