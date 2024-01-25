from django.contrib.auth import get_user_model
from drf_spectacular.utils import (
    OpenApiExample,
    extend_schema,
    extend_schema_view,
)
from rest_framework import mixins, status, viewsets

from users.serializers import CreateUserSerializer, ReadUserSerializer

User = get_user_model()


@extend_schema(tags=["Users"])
@extend_schema_view(
    create=extend_schema(
        summary="Создание нового пользователя",
        examples=[
            OpenApiExample(
                "Пример создания пользователя",
                value={
                    "phone": "+79451234567",
                    "email": "user@example.com",
                    "username": "superUser",
                },
                status_codes=[str(status.HTTP_201_CREATED)],
            ),
        ],
    ),
    retrieve=extend_schema(summary="Конкретный пользователь"),
    update=extend_schema(summary="Изменение данных пользователя"),
    partial_update=extend_schema(
        summary="Изменение данных пользователя",
        examples=[
            OpenApiExample(
                "Пример изменения данных пользователя",
                value={
                    "first_name": "Пётр",
                    "last_name": "Иванов",
                    "organization_name": "AMR",
                    "inn": "123456789112",
                },
                status_codes=[str(status.HTTP_200_OK)],
            ),
        ],
    ),
)
class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Вьюсет для пользователей.
    """

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "partial_update"]:
            return CreateUserSerializer
        return ReadUserSerializer
