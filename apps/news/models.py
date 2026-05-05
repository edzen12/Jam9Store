from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='news/')
    desc = CKEditor5Field('Описание', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='новость'
        verbose_name_plural='Новости'

