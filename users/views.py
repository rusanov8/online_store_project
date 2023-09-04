from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
import secrets

from users.forms import UserRegisterForm, UserProfileForm
# Create your views here.
from users.models import User
from users.services import send_email_for_verify

from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView

# Функционал контроллеров LoginView и LogoutView не меняем


class RegisterView(CreateView):  # контроллер доя регистрации пользователя
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            verify_key = secrets.token_urlsafe(32)  # генерируем случайный ключ

            user = form.save(commit=False)
            user.verify_key = verify_key  # сохраняем ключ к пользователю
            user.save()  # сохраняем пользователя с ключом

            current_site = get_current_site(self.request)  # получаем сайт для формирования ссылки
            verify_link = f"http://{current_site.domain}{reverse('users:verify_email', args=[verify_key])}"
            send_email_for_verify(user, verify_link)  # отправляем сообщение
            return render(self.request, 'users/verify_email.html')  # перенаправляем на страницу с сообщением о проверке почты

        return super().form_valid(form)


class ProfileView(UpdateView):  # контроллер для изменения пользователя
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user


def verify_email(request, key):   # контроллер для верификации пользователя

    user = User.objects.filter(verify_key=key).first()   # получаем пользователя по ключу
    if user:    # проверяем, существует ли такой пользователь
        user.is_verified = True
        user.save()
        # Перенаправление на страницу с сообщением об успешной верификации
        return render(request, 'users/verification_success.html')
    else:
        # Перенаправление на страницу с сообщением об ошибке
        return render(request, 'users/verification_error.html')


class CustomPasswordResetView(PasswordResetView):   # контроллер для сброса пароля
    template_name = 'users/registration/password_reset_form.html'
    email_template_name = 'users/registration/password_reset_email.html'
    success_url = reverse_lazy("users:password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):  # контроллер для успешной страницы сброса пароля.
    template_name = 'users/registration/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):  # контроллер для подтверждения сброса пароля.
    template_name = 'users/registration/password_reset_confirm.html'
    success_url = reverse_lazy("users:password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):  # контроллер для страницы успешного завершения сброса пароля.
    template_name = 'users/registration/password_reset_complete.html'
