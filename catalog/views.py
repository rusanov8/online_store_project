from django.shortcuts import render

from catalog.models import Product


def get_home(request):
    """Контроллер, который отвечает за отображение домашней страницы"""

    # Выборка последних 5 товаров в консоль
    latest_products = Product.objects.order_by('-create_date')[:5]
    print('Последние 5 товаров:')
    for product in latest_products:
        print(product.title)

    return render(request, 'catalog/home.html')


def get_contacts(request):
    """Контроллер, который отвечает за отображение контактной информации и обрабатывает POST запрос"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}')

    return render(request, 'catalog/contacts.html')
