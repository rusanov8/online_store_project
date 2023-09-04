from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verify_email, CustomPasswordResetView, \
    CustomPasswordResetCompleteView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView .as_view(), name='logout'),
    path('register/', RegisterView .as_view(), name='register'),
    path('profile/', ProfileView .as_view(), name='profile'),
    path('confirm_email/<str:key>/', verify_email, name='verify_email'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

