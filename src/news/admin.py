from django.contrib import admin

from news.models import News, NewsImage


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "is_shown")
    list_filter = ("is_shown", "published")
    search_fields = ("title", "published", "content")


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_filter = ("news__is_shown", "news__published")
    search_fields = ("news__title", "news__published", "news__content")
