from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cached_categories():
    try:
        if settings.CACHE_ENABLED:
            key = 'categories'
            categories = cache.get(key)
            if categories is None:
                categories = Category.objects.all()
                cache.set(key, categories)

        else:
            categories = Category.objects.all()

        return categories

    except Category.DoesNotExist:
        return []


