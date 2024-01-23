from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core.choices_classes import Role, Sex
from core.enums import Limits
from users.managers import AccountManager, UserManager
from users.validators import unique_email


class CustomUser(AbstractUser):
    """Кастомный юзер."""

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=Limits.MAX_LENGTH_PATRONYMIC.value,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=Limits.MAX_LENGTH_PATRONYMIC.value,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        blank=True,
        null=True,
        unique=False,
        validators=(unique_email,),
    )
    phone = PhoneNumberField(
        verbose_name="Номер телефона",
        max_length=Limits.MAX_LENGTH_PHONE_NUMBER.value,
        blank=False,
        null=False,
        unique=True,
    )
    role = models.IntegerField(
        verbose_name="Роль",
        choices=Role.choices,
        default=Role.USER,
    )

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ()

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        default_related_name = "user"

    def __str__(self) -> str:
        return self.username

    @property
    def is_admin(self):
        return self.role == Role.ADMIN

    @property
    def is_manager(self):
        return self.role == Role.MANAGER

    @property
    def is_staff(self):
        return self.role == Role.MANAGER or self.role == Role.ADMIN


class Account(models.Model):
    """Аккаунт пользователя."""

    user = models.OneToOneField(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    patronymic = models.CharField(
        verbose_name="Отчество",
        max_length=Limits.MAX_LENGTH_PATRONYMIC.value,
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name="Пол",
        choices=Sex.choices,
        blank=True,
        null=True,
    )
    date_birth = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True,
    )

    objects = AccountManager()

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
        default_related_name = "account"

    def __str__(self) -> str:
        return self.user.username
