from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm


class VerificationRequiredMixin:
    """Миксин для предварительной проверки подтверждения пользователя"""

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_authenticated and request.user.is_verified):
            return HttpResponseForbidden("Доступ запрещен")
        return super().dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    """Контроллер для отображения списка товаров"""
    model = Product
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        for object in context['products']:
            try:
                active_version = Version.objects.get(product=object, current_version=True)
                object.current_version = active_version
            except Version.DoesNotExist:
                object.current_version = None

        return context


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


class ProductCreateView(VerificationRequiredMixin, CreateView):
    """Контроллер для создания нового товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(VerificationRequiredMixin, UpdateView):
    """Контроллер для редактирования товара"""
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:edit_product', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(VerificationRequiredMixin, DeleteView):
    """Контроллер для удаления товара"""
    model = Product
    fields = ('title', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:home')


