from django.db import models
from users.models import User

# Константа для обозначения необязательных полей
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    change_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=150, verbose_name='Номер версии')
    version_title = models.CharField(max_length=150, verbose_name='Название версии')
    current_version = models.BooleanField(default=False, verbose_name='Текущая версия')

    def __str__(self):
        return f'Версия {self.version_number} {self.version_title}'

    def save(self, *args, **kwargs):
        if self.current_version:
            Version.objects.filter(product=self.product, current_version=True).update(current_version=False)
        super(Version, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        db_table = 'versions'




