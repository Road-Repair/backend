from django_filters import FilterSet, ModelChoiceFilter, NumberFilter

from locations.models import FederationEntity, Region, Settlement


class RegionFilter(FilterSet):
    """
    Кастомный фильтр для районов.
    """

    federation_entity_title = ModelChoiceFilter(
        field_name="federation_entity__title",
        to_field_name="title",
        queryset=FederationEntity.objects.all(),
    )
    federation_entity = ModelChoiceFilter(
        queryset=FederationEntity.objects.all(),
    )
    federation_entity_index = NumberFilter(
        field_name="federation_entity__index", lookup_expr="exact"
    )

    class Meta:
        model = Region
        fields = [
            "federation_entity",
            "federation_entity_title",
            "federation_entity_index",
        ]


class SettlementFilter(FilterSet):
    """
    Кастомный фильтр для населенных пунктов.
    """

    region_title = ModelChoiceFilter(
        field_name="region__title",
        to_field_name="title",
        queryset=Region.objects.all(),
    )
    region = ModelChoiceFilter(
        queryset=Region.objects.all(),
    )

    class Meta:
        model = Settlement
        fields = [
            "region_title",
            "region",
        ]
