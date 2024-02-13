from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework.serializers import (
    ChoiceField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    ValidationError,
)

from core.choices_classes import LocationLevel
from projects.models import Project, ProjectImage


class ProjectImageSerializer(ModelSerializer):
    """
    Сериализатор для фото проекта.
    """

    class Meta:
        model = ProjectImage
        fields = ["image"]


class ProjectCreateSerializer(ModelSerializer):
    """
    Сериализатор для создания проекта.
    """

    content_type = ChoiceField(choices=LocationLevel.choices, write_only=True)
    location = StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = [
            "content_type",
            "object_id",
            "number",
            "description",
            "work_type",
            "location",
        ]

    def validate(self, attrs):
        content_type = attrs.get("content_type", None)
        model = ContentType.objects.get(
            app_label="locations", model=content_type
        )
        if (
            not model.model_class()
            .objects.filter(id=attrs.get("object_id", None))
            .exists()
        ):
            raise ValidationError("Выбран неверный идентификатор объекта")

        return attrs

    def create(self, validated_data):
        self.validate(validated_data)
        content_type_data = validated_data.pop("content_type")
        content_type = get_object_or_404(
            ContentType, app_label="locations", model=content_type_data
        )
        project = Project.objects.create(
            **validated_data, content_type=content_type
        )
        return project


class ProjecListSerializer(ModelSerializer):
    """
    Сериализатор для вывода списка проектов.
    """

    location = StringRelatedField()
    description = SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "location",
            "number",
            "description",
            "actual_status",
        ]

    def get_description(self, obj):
        return obj.description[:30]


class ProjecRetrieveSerializer(ProjecListSerializer):
    """
    Сериализатор для вывода информации об одном проекте.
    """

    initiator = StringRelatedField(read_only=True)
    images = SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "initiator",
            "address",
            "work_type",
            "needed_promotion",
            "images",
            "cost_of_works",
        ]

    def get_images(self, obj):
        return obj.images.all()
