from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):  # переопределяем модель для пользователя

    username = None
    email = models.EmailField(verbose_name='Почта', unique=True)

    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='Страна', blank=True, null=True)

    verify_key = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ключ верификации')
    is_verified = models.BooleanField(default=False, verbose_name='верифицирован')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'
