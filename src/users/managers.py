from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet

from core.choices_classes import Role
from core.services import send_registry_email


class UserManager(BaseUserManager):
    """Кастомный менеджер для юзера."""

    def create_user(self, phone, email, password=None, **extra_fields):
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
                allowed_chars=settings.PASSWORD_SYMBOLS,
            )
        user.set_password(password)
        user.save(using=self._db)
        send_registry_email(email, password)
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


class AccountManager(models.Manager):
    """
    Пользовательсткий менеджер для Модели Аккаунт.
    """

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related("user")
