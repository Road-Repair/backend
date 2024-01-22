from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

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
            "phone",
            "email",
            "username",
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
            "user",
            "patronymic",
            "sex",
            "date_birth",
        ]
