from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from projects.models import Project
from projects.serializers import (
    ProjecListSerializer,
    ProjecRetrieveSerializer,
    ProjectCreateSerializer,
)


@extend_schema(tags=["Projects"])
@extend_schema_view(
    list=extend_schema(
        summary="Получение списка проектов",
    ),
    retrieve=extend_schema(
        summary="Получение информации об одном проекте",
    ),
    create=extend_schema(
        summary="Создание проекта",
    ),
)
class ProjectViewSet(
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    """
    Вьюсет для проектов.
    """

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProjecRetrieveSerializer
        if self.action == "create":
            return ProjectCreateSerializer
        return ProjecListSerializer
