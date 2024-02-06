from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.choices_classes import ProjectImageTypes, StatusOfProject, WorkTypes
from core.enums import Limits
from projects.utils import path_to_save_project_photo


class Project(models.Model):
    """
    Модель проектов.
    """

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name="Модель приложения locations"
    )
    object_id = models.IntegerField(
        "ID объекта"
    )
    location = GenericForeignKey("content_type", "object_id")
    number = models.CharField(
        "Номер проекта",
        max_length=Limits.MAX_LENGTH_PROJECT_NUMBER
    )
    address = models.CharField(
        "Адрес",
        max_length=Limits.MAX_LENGTH_PROJECT_ADDRESS
    )
    work_type = models.IntegerField(
        "Вид работ",
        choices=WorkTypes.choices
    )
    decription = models.TextField(
        "Описание проекта",
        max_length=Limits.MAX_LENGTH_PROJECT_DESCRIPTION
    )
    actual_status = models.IntegerField(
        "Текущий статус",
        choices=StatusOfProject.choices,
        default=StatusOfProject.CREATED
    )
    needed_promotion = models.BooleanField(
        "Нужно продвижение",
        default=False
    )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        default_related_name = "projects"

    def __str__(self):
        return self.number


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
        null=True
    )
    type = models.CharField(
        "До или после",
        choices=ProjectImageTypes.choices,
        default=ProjectImageTypes.BEFORE,
        max_length=Limits.MAX_LENGTH_IMAGE_TYPE
    )

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
        default=StatusOfProject.CREATED
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="statuses"
    )
    created_at = models.DateField(
        "Дата присваивания",
        auto_now=True
    )

    class Meta:
        verbose_name = "Статус проекта"
        verbose_name_plural = "Статусы проектов"

    def __str__(self):
        return f"{self.project} {self.status}"
