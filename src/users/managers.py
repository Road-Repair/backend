from django.contrib.auth.base_user import BaseUserManager

from core.choices_classes import Role


class UserManager(BaseUserManager):
    """Кастомный менеджер для юзера."""

    def create_user(self, phone, email, password, **extra_fields):
        if not phone:
            raise ValueError("Телефон обязателен")
        email = self.normalize_email(email) if email else None
        user = self.model(
            phone=phone,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
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
