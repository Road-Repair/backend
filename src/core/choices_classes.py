from django.db import models


class Role(models.IntegerChoices):
    ADMIN = 1
    MANAGER = 2
    USER = 3


class Sex(models.IntegerChoices):
    MALE = 1, "Мужчина"
    FEMALE = 2, "Женщина"


class ProjectImageTypes(models.TextChoices):
    AFTER = "После"
    BEFORE = "До"


class WorkTypes(models.IntegerChoices):
    LANDSCAPING = 1, "Благоустройство"
    REPAIR = 2, "Ремонт"


class StatusOfProject(models.IntegerChoices):
    CANCELLED = 0, "Отменен"
    CREATED = 1, "Создан"
    CONFIRMED = 2, "Подтвержден"
    FUNDRASING = 4, "Сбор средств"
    AT_WORK = 5, "В работе"
    FINISHED = 6, "Завершен"
