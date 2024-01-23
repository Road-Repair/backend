from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_registry_email(mail_to: str, password: str):
    """
    Отправка временного пароля для входа в ЛК.
    """

    html_body = render_to_string(
        "email/user_registry.html", {"password": password}
    )
    message = EmailMultiAlternatives(
        subject="Регистрация на сервисе Желтый Грейдер", to=[mail_to]
    )
    message.attach_alternative(html_body, "text/html")
    message.send()
