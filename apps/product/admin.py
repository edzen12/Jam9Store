from django.contrib import admin
from apps.product.models import Category, Product, Slider, ProductReview


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku')
    list_display_links = ('name', 'sku')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name', 'sku')


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'created_at')
    list_display_links = ('id', 'name', 'product')
    search_fields = ('name', 'email')


admin.site.register(Slider)
