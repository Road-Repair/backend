from django.contrib.auth import get_user_model
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
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
)
class UserViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для создания пользователя.
    """

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return ReadUserSerializer
