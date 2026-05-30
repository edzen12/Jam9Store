from django.db import models


class Review(models.Model):
    full_name = models.CharField(
        max_length=100, 
        verbose_name="ФИО"
    )
    image = models.ImageField(
        upload_to='Фото лица', 
        blank=True, null=True
    )
    position = models.CharField(
        max_length=100, 
        verbose_name="Должность"
    )
    text = models.TextField(verbose_name="Текст (отзыв)")

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name="отзыв"
        verbose_name_plural="Отзывы"
