from factory import Sequence, fuzzy, SubFactory
from factory.django import DjangoModelFactory

from core.enums import Limits
from locations.models import FederationEntity, Municipality, Region, Settlement


class FederationEntityFactory(DjangoModelFactory):
    """
    Фабрика для создания экземпляров модели Субъекта Федерации.
    """

    class Meta:
        model = FederationEntity

    index = Sequence(lambda num: num)
    title = fuzzy.FuzzyText(
        prefix="fed_entity_", length=Limits.MAX_LENGTH_REGION_TITLE
    )


class RegionFactory(DjangoModelFactory):
    """
    Фабрика для создания экземпляров модели Регионов.
    """

    class Meta:
        model = Region

    federation_entity = SubFactory(FederationEntityFactory)
    title = fuzzy.FuzzyText(
        prefix="region_", length=Limits.MAX_LENGTH_REGION_TITLE
    )


class MunicipalityFactory(DjangoModelFactory):
    """
    Фабрика для создания экземпляров модели Муниципалитетов.
    """

    class Meta:
        model = Municipality

    region = SubFactory(RegionFactory)
    title = fuzzy.FuzzyText(
        prefix="municipality_", length=Limits.MAX_LENGTH_REGION_TITLE
    )


class SettlementFactory(DjangoModelFactory):
    """
    Фабрика для создания экземпляров модели Населенных пунктов.
    """

    class Meta:
        model = Settlement

    municipality = SubFactory(MunicipalityFactory)
    title = fuzzy.FuzzyText(
        prefix="settlement_", length=Limits.MAX_LENGTH_REGION_TITLE
    )