from django.contrib import admin

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "is_shown")
    list_filter = ("is_shown",)
    search_fields = ("title", "published", "content")
