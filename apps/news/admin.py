from django.contrib import admin
from apps.news.models import News, NewsComment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'created_at')
    prepopulated_fields = {'slug':('title',)}


@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'news', 'created_at')
