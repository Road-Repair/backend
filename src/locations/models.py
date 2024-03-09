from django.db import models

from core.enums import Limits
from locations.managers import RegionManager, SettlementManager


class AbstractLocationModel(models.Model):
    """
    Абстрактная модель для регионов.
    """

    projects_create = models.BooleanField(
        "Можно создавать авторские проекты", default=False
    )
    title = models.CharField(
        "Наименование", max_length=Limits.MAX_LENGTH_REGION_TITLE
    )
    wiki_link = models.URLField(
        "Ссылка на статью на Википедии",
        max_length=Limits.MAX_LENGTH_LINK,
        blank=True,
        null=True,
    )
    has_subregions = models.BooleanField("Имеет субрегионы", default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class FederationEntity(AbstractLocationModel):
    """
    Субъект Федерации.
    """

    title = models.CharField(
        "Наименование", max_length=Limits.MAX_LENGTH_REGION_TITLE, unique=True
    )
    index = models.IntegerField("Номер Субъекта", unique=True, db_index=True)
    emblem = models.ImageField(
        "Герб региона", upload_to="f_entities_emblems", blank=True, null=True
    )

    class Meta:
        verbose_name = "Субъект Федерации"
        verbose_name_plural = "Субъекты Федерации"
        ordering = ["index"]


class Region(AbstractLocationModel):
    """
    Район (а также муниципальный или городской округ).
    """

    federation_entity = models.ForeignKey(
        FederationEntity, on_delete=models.CASCADE, related_name="regions"
    )

    objects = RegionManager()

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Settlement(AbstractLocationModel):
    """
    Населенный пункт.
    """

    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="settlements"
    )
    projects_create = models.BooleanField(
        "Можно создавать авторские проекты", default=True
    )

    objects = SettlementManager()

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенные пункты"
