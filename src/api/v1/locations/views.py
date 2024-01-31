from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import filters, generics

from api.v1.locations.filters import (
    MunicipalityFilter,
    RegionFilter,
    SettlementFilter,
)
from locations.models import FederationEntity, Municipality, Region, Settlement
from locations.serializers import (
    FederationEntitySerializer,
    MunicipalitySerializer,
    RegionSerializer,
    SettlementSerializer,
)


@extend_schema(tags=["Locations"])
@extend_schema_view(
    list=extend_schema(
        summary="Получение списка Субъектов Федерации.",
    ),
)
class FederationEntityView(generics.ListAPIView):
    """
    Вьюкласс для Субъектов Федерации.
    """

    serializer_class = FederationEntitySerializer
    queryset = FederationEntity.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["index", "title"]


@extend_schema(tags=["Locations"])
@extend_schema_view(
    list=extend_schema(
        summary="Получение списка районов.",
    ),
)
class RegionView(generics.ListAPIView):
    """
    Вьюкласс для районов.
    """

    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = RegionFilter
    search_fields = ["title"]


@extend_schema(tags=["Locations"])
@extend_schema_view(
    list=extend_schema(
        summary="Получение списка муниципалитетов.",
    ),
)
class MunicipalityView(generics.ListAPIView):
    """
    Вьюкласс для муниципалитетов.
    """

    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = MunicipalityFilter
    search_fields = ["title"]


@extend_schema(tags=["Locations"])
@extend_schema_view(
    list=extend_schema(
        summary="Получение списка населенных пунктов.",
    ),
)
class SettlementView(generics.ListAPIView):
    """
    Вьюкласс для населенных пунктов.
    """

    serializer_class = SettlementSerializer
    queryset = Settlement.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = SettlementFilter
    search_fields = ["title"]
