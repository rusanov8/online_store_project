from django.shortcuts import render, redirect

from catalog.forms import ProductForm
from catalog.models import Product


def get_home(request):
    """Контроллер, который отвечает за отображение домашней страницы"""
    products_list = Product.objects.all()  # Список продуктов

    context = {
        'object_list': products_list,
        'title': 'Главная'
    }

    return render(request, 'catalog/home.html', context)


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


def product_detail(request, product_id):
    """Контроллер для отображения страницы с товаром"""

    product = Product.objects.get(pk=product_id)
    context = {
        'object': product,
        'title': product.title
    }
    return render(request, 'catalog/product.html', context)


def create_product(request):
    """Контроллер для добавления нового товара"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')

    else:
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, 'catalog/create_product.html', context)


