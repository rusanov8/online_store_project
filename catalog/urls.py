from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import get_contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', get_contacts, name='contacts'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('create_product/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product')
]
