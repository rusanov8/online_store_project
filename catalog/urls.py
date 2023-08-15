from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import get_home, get_contacts, product_detail, create_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', get_home, name='home'),
    path('contacts/', get_contacts, name='contacts'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('create_product/', create_product, name='create_product')
]
