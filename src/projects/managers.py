from django.db import models
from django.db.models.query import QuerySet


class ProjectStatusImageManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related("project")


class ProjectManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return (
            super()
            .get_queryset()
            .select_related("initiator")
            .prefetch_related("images", "statuses")
        )
