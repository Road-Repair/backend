from django.db import models


class Role(models.IntegerChoices):
    ADMIN = 1
    MANAGER = 2
    USER = 3


class Sex(models.IntegerChoices):
    MALE = 1, "Мужчина"
    FEMALE = 2, "Женщина"
