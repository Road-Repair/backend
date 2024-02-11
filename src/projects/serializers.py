from rest_framework.serializers import (
    ChoiceField,
    ModelSerializer,
    StringRelatedField,
    SerializerMethodField
)

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

    location_type = ChoiceField(
        choices={}
    )

    class Meta:
        model = Project
        fields = [
            "location_type",
            "object_id",
            "number",
            "description",
            "work_type",
        ]


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
            "images"
        ]

    def get_images(self, obj):
        return obj.images.all()
