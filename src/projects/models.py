from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.choices_classes import ProjectImageTypes, StatusOfProject, WorkTypes
from core.enums import Limits
from projects.managers import ProjectManager, ProjectStatusImageManager
from projects.utils import path_to_save_project_photo

User = get_user_model()


class Project(models.Model):
    """
    Модель проектов.
    """

    initiator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Инициатор проекта"
    )
    limit = (
        models.Q(app_label="locations", model="region")
        | models.Q(app_label="locations", model="federationentity")
        | models.Q(app_label="locations", model="settlement")
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name="Модель приложения locations",
        limit_choices_to=limit,
    )
    object_id = models.PositiveIntegerField("ID объекта")
    location = GenericForeignKey("content_type", "object_id")
    number = models.CharField(
        "Номер проекта",
        max_length=Limits.MAX_LENGTH_PROJECT_NUMBER.value,
        unique=True,
    )
    address = models.CharField(
        "Адрес", max_length=Limits.MAX_LENGTH_PROJECT_ADDRESS.value
    )
    work_type = models.IntegerField("Вид работ", choices=WorkTypes.choices)
    description = models.TextField(
        "Описание проекта",
        max_length=Limits.MAX_LENGTH_PROJECT_DESCRIPTION.value,
    )
    actual_status = models.IntegerField(
        "Текущий статус",
        choices=StatusOfProject.choices,
        default=StatusOfProject.CREATED,
    )
    cost_of_works = models.DecimalField(
        "Стоимость работ",
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
    )
    needed_promotion = models.BooleanField("Нужно продвижение", default=False)

    objects = ProjectManager()

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        default_related_name = "projects"

    def __str__(self) -> str:
        return self.number

    def promote(self) -> None:
        self.needed_promotion = True
        self.save()

    def change_status(self, new_status: int) -> None:
        if self.actual_status != 0:
            self.actual_status = new_status
            self.save()
            ProjectStatus.objects.create(status=new_status, project=self)


class ProjectImage(models.Model):
    """
    Фотографии для проектов.
    """

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        "Фотография",
        upload_to=path_to_save_project_photo,
        blank=True,
        null=True,
    )
    type = models.CharField(
        "До или после",
        choices=ProjectImageTypes.choices,
        default=ProjectImageTypes.BEFORE,
        max_length=Limits.MAX_LENGTH_IMAGE_TYPE,
    )

    objects = ProjectStatusImageManager()

    class Meta:
        verbose_name = "Фотография для проекта"
        verbose_name_plural = "Фотографии для проектов"

    def __str__(self):
        return f"Фото для {self.project}"


class ProjectStatus(models.Model):
    """
    История изменения статуса проекта.
    """

    status = models.IntegerField(
        "Статус",
        choices=StatusOfProject.choices,
        default=StatusOfProject.CREATED,
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="statuses"
    )
    created_at = models.DateField("Дата присваивания", auto_now=True)

    objects = ProjectStatusImageManager()

    class Meta:
        verbose_name = "Статус проекта"
        verbose_name_plural = "Статусы проектов"

    def __str__(self):
        return f"Проект {self.project}, статус {self.status}"
