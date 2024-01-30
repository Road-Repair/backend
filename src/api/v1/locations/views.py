from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework import mixins, viewsets

from locations.models import FederationEntity
from locations.serializers import FederationEntitySerializer


@extend_schema(tags=["Locations"])
@extend_schema_view(
    list=extend_schema(
        summary="Получение списка Субъектов Федерации.",
    ),
)
class FederationEntityViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для Субъектов Федерации.
    """

    serializer_class = FederationEntitySerializer
    queryset = FederationEntity.objects.all()
