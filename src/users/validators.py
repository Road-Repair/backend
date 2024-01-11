from django.core.exceptions import ValidationError


def unique_email(value):
    """Валидатор уникальности почты."""

    from users.models import CustomUser

    existing_users = CustomUser.objects.filter(email=value)
    if existing_users.exists():
        raise ValidationError("Пользователь с таким email уже существует")
