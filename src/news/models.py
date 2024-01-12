from django.db import models
from django.utils import timezone

from core.enums import Limits


class News(models.Model):
    """
    Новость.
    """

    title = models.CharField(
        "Заголовок", max_length=Limits.MAX_LENGTH_NEWS_TITLE
    )
    content = models.TextField(
        "Содержание", max_length=Limits.MAX_LENGTH_NEWS_CONTENT
    )
    image = models.ImageField(
        "Фотография", upload_to="news_images", blank=True, null=True
    )
    created = models.DateTimeField(
        "Время создания", auto_now_add=True, db_index=True
    )
    published = models.DateTimeField("Время опубликования", null=True)
    is_shown = models.BooleanField("Новость размещена на сайте", default=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-published", "-created"]

    def publish(self):
        if not self.published:
            self.published = timezone.now()
            self.is_shown = True
            self.save()

    def __str__(self):
        return self.title
