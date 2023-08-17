from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', )
    list_filter = ('is_published', 'publication_date')

    search_fields = ('title', 'content', )
