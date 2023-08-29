from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'category', )
    list_filter = ('category', )

    search_fields = ('title', 'description', )

@admin.register(Version)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_title',)
    list_filter = ('current_version',)
