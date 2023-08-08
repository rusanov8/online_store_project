from django.urls import path
from catalog.views import get_home, get_contacts

urlpatterns = [
    path('', get_home),
    path('contacts/', get_contacts)
]
