from django.db import models
from django.utils import timezone

from core.enums import Limits
from news.managers import NewsImageManager


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
    created = models.DateTimeField(
        "Время создания", auto_now_add=True, db_index=True
    )
    published = models.DateTimeField(
        "Время опубликования", blank=True, null=True
    )
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


class NewsImage(models.Model):
    """
    Фотографии для новостей.
    """

    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        "Фотография", upload_to="news_images", blank=True, null=True
    )

    objects = NewsImageManager()

    class Meta:
        verbose_name = "Фотография для новости"
        verbose_name_plural = "Фотографии для новостей"

    def __str__(self):
        return f"Фото для {self.news}"
