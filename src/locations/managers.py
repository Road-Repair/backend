from django.db import models
from django.db.models.query import QuerySet


class FederationEntityManager(models.Manager):
    """
    Пользовательстки менеджер для модели Субъекта Федерации.
    """

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related(
            "region",
            "region__municipality",
            "region__municipality__settlement",
        )


class RegionManager(models.Manager):
    """
    Пользовательстки менеджер для модели Регионов.
    """

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related(
            "municipality",
            "municipality__settlement",
        )


class MunicipalityManager(models.Manager):
    """
    Пользовательстки менеджер для модели Муниципалитетов.
    """

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related(
            "settlement",
        )
