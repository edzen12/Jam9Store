from django.db import models



class Gallery(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title:
            return self.title
        return f"Фото: {self.id}"
    
    class Meta:
        verbose_name='галерея'
        verbose_name_plural='Галерея'