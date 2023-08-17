from django.shortcuts import render, redirect


from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView


class ProductListView(ListView):
    """Контроллер для отображения списка товаров"""
    model = Product


def get_contacts(request):
    """Контроллер, который отвечает за отображение контактной информации и обрабатывает POST запрос"""
    context = {
        'title': 'Контакты'
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}')

    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    """Контроллер для отображения страницы с товаром"""
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:home')

