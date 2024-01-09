from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core.choices_classes import Role, Sex
from core.enums import Limits


class CustomUser(AbstractUser):
    """Custom User model."""

    username = None
    account = models.OneToOneField(
        "Account",
        verbose_name="Профиль аккаунта",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        blank=True,
        unique=True,
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

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return (
            f"{self.account.last_name} {self.account.first_name[0].upper()}."
            f"{self.account.patronymic[0] + '.' if self.account.patronymic else ''} "
        )

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
    """Account model."""

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=Limits.MAX_LENGTH_FIRST_NAME.value,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=Limits.MAX_LENGTH_LAST_NAME.value,
        blank=False,
        null=False,
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

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name[0].upper()}."
