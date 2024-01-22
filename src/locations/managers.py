from django.db import models
from django.db.models.query import QuerySet


class SettlementManager(models.Manager):
    """
    Пользовательстки менеджер для модели населенных пунктов.
    """

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related(
            "municipality",
            "municipality__region",
            "municipality__region__federation_entity",
        )


class RegionManager(models.Manager):
    """
    Пользовательстки менеджер для модели Регионов.
    """

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related(
            "federation_entity",
        )


class MunicipalityManager(models.Manager):
    """
    Пользовательстки менеджер для модели Муниципалитетов.
    """

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related("region", "region__federation_entity")
