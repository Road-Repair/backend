from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, generics

from api.v1.locations.filters import RegionFilter, SettlementFilter
from locations.models import FederationEntity, Region, Settlement
from locations.serializers import (
    FederationEntitySerializer,
    RegionSerializer,
    SettlementSerializer,
)


@extend_schema(
    tags=["Locations"],
    summary="Получение списка Субъектов Федерации.",
)
class FederationEntityView(generics.ListAPIView):
    """
    Вьюкласс для Субъектов Федерации.
    """

    serializer_class = FederationEntitySerializer
    queryset = FederationEntity.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["index", "title"]


@extend_schema(
    tags=["Locations"],
    summary="Получение списка районов.",
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


@extend_schema(
    tags=["Locations"],
    summary="Получение списка населенных пунктов.",
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
