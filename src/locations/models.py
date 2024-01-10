from django.db import models

from core.enums import MAX_REGION_TITLE


class AbstractLocationModel(models.Mode):
    """
    Абстрактная модель для регионов.
    """

    projects_create = models.BooleanField(
        "Можно создавать авторские проекты", default=False
    )
    title = models.CharField("Наименование", max_length=MAX_REGION_TITLE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class FederationEntity(AbstractLocationModel):
    """
    Субъект Федерации.
    """

    title = models.CharField(
        "Наименование", max_length=MAX_REGION_TITLE, unique=True
    )
    index = models.ImageField("Номер Субъекта", unique=True, db_index=True)

    class Meta:
        verbose_name = "Субъект Федерации"
        verbose_name_plural = "Субъекты Федерации"
        ordering = ["index"]


class Region(AbstractLocationModel):
    """
    Район (а также муниципальный или городской округ).
    """

    federation_entity = models.ForeignKey(
        FederationEntity,
        on_delete=models.CASCADE,
        related_name="regions"
    )

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Municipality(AbstractLocationModel):
    """
    Муниципальное образование (а также городские или сельские послеления).
    """

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="municipalities"
    )

    class Meta:
        verbose_name = "Муниципальное образование"
        verbose_name_plural = "Муниципальные образования"


class Settlement(AbstractLocationModel):
    """
    Населенный пункт.
    """

    municipality = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="settlements"
    )

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенные пункты"
