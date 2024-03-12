from django.db import models
from django.db.models.query import QuerySet


class NewsImageManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs.select_related("news")
