from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


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
            "username",
            "phone",
            "email",
            "last_name",
            "first_name",
        ]
