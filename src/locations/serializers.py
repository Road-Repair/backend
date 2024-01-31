from rest_framework.serializers import ModelSerializer, StringRelatedField

from locations.models import (
    AbstractLocationModel,
    FederationEntity,
    Municipality,
    Region,
    Settlement,
)


class AbstractLocationSerializer(ModelSerializer):
    """
    Абстрактный Сериализатор для населенных пунктов.
    """

    class Meta:
        model = AbstractLocationModel
        fields = [
            "id",
            "title",
            "wiki_link",
            "projects_create",
            "has_subregions",
        ]
        abstract = True


class FederationEntitySerializer(AbstractLocationSerializer):
    """
    Сериализатор для Субъектов Федерации.
    """

    class Meta:
        model = FederationEntity
        fields = AbstractLocationSerializer.Meta.fields + [
            "index",
            "emblem",
        ]
        read_only_fields = AbstractLocationSerializer.Meta.fields + [
            "index",
            "emblem",
        ]


class RegionSerializer(ModelSerializer):
    """
    Сериализатор для районов.
    """

    federation_entity = StringRelatedField()

    class Meta:
        model = Region
        fields = AbstractLocationSerializer.Meta.fields + ["federation_entity"]
        read_only_fields = AbstractLocationSerializer.Meta.fields + [
            "federation_entity"
        ]


class MunicipalitySerializer(ModelSerializer):
    """
    Сериализатор для муниципалитетов.
    """

    region = StringRelatedField()

    class Meta:
        model = Municipality
        fields = AbstractLocationSerializer.Meta.fields + ["region"]
        read_only_fields = AbstractLocationSerializer.Meta.fields + ["region"]


class SettlementSerializer(ModelSerializer):
    """
    Сериализатор для населенных пунктов.
    """

    municipality = StringRelatedField()

    class Meta:
        model = Settlement
        fields = AbstractLocationSerializer.Meta.fields + ["municipality"]
        read_only_fields = AbstractLocationSerializer.Meta.fields + [
            "municipality"
        ]
