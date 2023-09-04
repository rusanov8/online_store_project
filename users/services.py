from django.core.mail import send_mail


def send_email_for_verify(user, verify_link):  # функция для отправки сообщения

    subject = 'Подтверждение email на Skystore'
    message = f'Пройдите по ссылке для подтверждения вашего email: {verify_link}'
    from_email = 'rusanov.egor@bk.ru'
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)

