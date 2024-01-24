from django.contrib.auth import get_user_model
from django.middleware import csrf
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
)
from rest_framework import mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib.auth import authenticate
from django.conf import settings

from core.enums import Limits
from users.models import Account
from users.permissions import IsOwner
from users.serializers import (
    AccountSerializer,
    CookieTokenRefreshSerializer,
    CreateUserSerializer,
    ReadUserSerializer,
    UpdateAccountSerializer,
)

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
class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Вьюсет для создания пользователя.
    """

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return ReadUserSerializer


@extend_schema(
    tags=["Users"],
    summary="Логин",
    examples=[
        OpenApiExample(
            "Пример входа пользователя в систему.",
            value={
                "phone": "+79123456789",
                "password": "password"
            },
            status_codes=[str(status.HTTP_200_OK)],
        ),
    ]
)
class CookieTokenObtainPairView(TokenObtainPairView):
    """
    Сохранение токена в Cookie.
    """

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                "refresh_token",
                response.data["refresh"],
                max_age=Limits.COOKIE_MAX_AGE,
                httponly=True,
            )
            response.set_cookie(
                "access_token",
                response.data["access"],
                max_age=Limits.COOKIE_MAX_AGE,
                httponly=True,
            )
            del response.data["refresh"]
            del response.data["access"]
            response.data = {"Success": "Login successfully"}
        return super().finalize_response(request, response, *args, **kwargs)


@extend_schema(
    tags=["Users"],
    summary="Обновление refresh токена.",
)
class CookieTokenRefreshView(TokenRefreshView):
    """
    Обновление refresh токена.
    """

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                "refresh_token",
                response.data["refresh"],
                max_age=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
                httponly=True,
            )
            response.set_cookie(
                "access_token",
                response.data["access"],
                max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                httponly=True,
            )
            del response.data["refresh"]
            del response.data["access"]
            response.data = {"Success": "Token refreshed"}
        return super().finalize_response(request, response, *args, **kwargs)

    serializer_class = CookieTokenRefreshSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@extend_schema(
    tags=["Users"],
    summary="Логин",
    examples=[
        OpenApiExample(
            "Пример входа пользователя в систему.",
            value={
                "phone": "+79123456789",
                "password": "password"
            },
            status_codes=[str(status.HTTP_200_OK)],
        ),
    ]
)
class LoginView(APIView):
    """
    Вход пользователя в систему.
    """
    def post(self, request, format=None):
        data = request.data
        response = Response()
        phone = data.get("phone", None)
        password = data.get("password", None)
        user = authenticate(phone=phone, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                    value=data["access"],
                    expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                    samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                )
                response.set_cookie(
                    key=settings.SIMPLE_JWT["AUTH_REFRESH"],
                    value=data["refresh"],
                    expires=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                    samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                )
                csrf.get_token(request)
                response.data = {"Success": "Login successfully"}
                return response
            else:
                return Response(
                    {"No active": "This account is not active!!"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"Invalid": "Invalid phone or password!!"},
                status=status.HTTP_404_NOT_FOUND,
            )


@extend_schema(tags=["Users"])
@extend_schema_view(
    update=extend_schema(
        summary="Изменение сведений о пользователе.",
        examples=[
            OpenApiExample(
                "Пример создания пользователя.",
                value={
                    "user": {
                        "last_name": "Иванов",
                        "first_name": "Иван"
                    },
                    "patronymic": "Иванович",
                    "date_birth": "2024-01-01",
                    "sex": 1
                },
                status_codes=[str(status.HTTP_200_OK)],
            ),
        ]
    ),
    partial_update=extend_schema(
        summary="Изменение сведений о пользователе.",
        examples=[
            OpenApiExample(
                "Пример создания пользователя.",
                value={
                    "user": {
                        "last_name": "Иванов"
                    },
                    "patronymic": "Иванович",
                    "date_birth": "2024-01-01"
                },
                status_codes=[str(status.HTTP_200_OK)],
            ),
        ]
    ),
    retrieve=extend_schema(
        summary="Просмотр сведений о пользователе.",
    ),
)
class AccountViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    Вьюсет для аккаута.
    """

    permission_classes = (IsOwner,)

    def get_queryset(self):
        return Account.objects.all()

    def get_object(self):
        if self.kwargs.get("pk", None) == "me":
            self.kwargs["pk"] = self.request.user.pk
        return super(AccountViewSet, self).get_object()

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return UpdateAccountSerializer
        return AccountSerializer
