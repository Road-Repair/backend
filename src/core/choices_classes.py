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
    CREATED = 0, "Создан"
    CONFIRMED = 1, "Подтвержден"
    CANCELLED = 2, "Отменен"
    FUNDRASING = 3, "Сбор средств"
    AT_WORK = 4, "В работе"
    FINISHED = 5, "Завершен"
