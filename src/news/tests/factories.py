from factory import fuzzy
from factory.django import DjangoModelFactory

from core.enums import Limits
from news.models import News


class NewsFactory(DjangoModelFactory):
    """
    Класс для создания экземпляров модели Новостей.
    """

    class Meta:
        model = News

    title = fuzzy.FuzzyText(
        prefix="news_", length=Limits.MAX_LENGTH_NEWS_TITLE
    )
    content = fuzzy.FuzzyText(
        prefix="news_content_", length=Limits.MAX_LENGTH_NEWS_CONTENT
    )
