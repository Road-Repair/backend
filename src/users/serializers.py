from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken

from users.models import Account


User = get_user_model()


class CreateUserSerializer(ModelSerializer):
    """
    Сериализатор для создания пользователя.
    """

    class Meta:
        model = User
        fields = [
            "phone",
            "email",
            "username",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ReadUserSerializer(ModelSerializer):
    """
    Сериализатор для создания пользователя.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "phone",
            "email",
            "username",
            "last_name",
            "first_name",
        ]


class UpdateUserSerializer(ModelSerializer):
    """
    Сериализатор для создания пользователя.
    """

    class Meta:
        model = User
        fields = [
            "last_name",
            "first_name",
        ]


class AccountSerializer(ModelSerializer):
    """
    Сериализатор для аккаунта пользователя.
    """

    user = ReadUserSerializer()

    class Meta:
        model = Account
        fields = [
            "id",
            "user",
            "patronymic",
            "sex",
            "date_birth",
        ]


class UpdateAccountSerializer(ModelSerializer):
    """
    Сериализатор для изменения аккаунта пользователя.
    """

    user = UpdateUserSerializer()

    class Meta:
        model = Account
        fields = [
            "user",
            "patronymic",
            "sex",
            "date_birth",
        ]

    def update(self, instance, validated_data):
        user = instance.user
        user_info = validated_data.pop("user")
        if user_info.get("first_name", None):
            user.first_name = user_info["first_name"]
        if user_info.get("last_name", None):
            user.last_name = user_info["last_name"]
        user.save()
        return super().update(instance, validated_data)


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get("refresh_token")
        if attrs["refresh"]:
            return super().validate(attrs)
        else:
            raise InvalidToken(
                "No valid token found in cookie 'refresh_token'"
            )
