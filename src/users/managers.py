from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings
from django.core.mail import EmailMessage

from core.choices_classes import Role


class UserManager(BaseUserManager):
    """Кастомный менеджер для юзера."""

    def create_user(
            self, phone, email, password=None, **extra_fields
    ):
        if not phone:
            raise ValueError("Телефон обязателен")
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(
            phone=phone,
            email=email,
            **extra_fields,
        )
        if not password:
            password = self.make_random_password(
                length=int(settings.PASSWORD_LENGTH),
                allowed_chars=settings.PASSWORD_SYMBOLS
            )
        print(password)
        print(email)
        user.set_password(password)
        send_to = EmailMessage(
            "Приветствуем Вас на сайте Желтый грейдер",
            f"Ваш временный пароль для входа в личный кабинет: {password}",
            to=[email],
        )
        send_to.send()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, email=None):
        email = input("Введите почту: ")
        first_name = input("Введите Имя: ")
        last_name = input("Введите Фамилию: ")
        user = self.create_user(
            phone=phone,
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_superuser = True
        user.is_active = True
        user.role = Role.ADMIN
        user.save(using=self._db)
        return user
