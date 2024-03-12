from core.fixtures import BaseTestCase
from news.models import News, NewsImage
from news.tests.factories import NewsFactory


class NewsModelsTest(BaseTestCase):
    """
    Класс для тестирования моделей приложения news.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.news_1 = NewsFactory()
        cls.image_1 = NewsImage.objects.create(
            news=cls.news_1, image=cls.uploaded
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_news_image_creation(self):
        self.assertEqual(self.image_1.image, f"news_images/{self.file_name}")

    def test_models_have_correct_object_names(self):
        self.assertEqual(str(self.news_1), self.news_1.title)

    def test_models_default_values(self):
        self.assertFalse(self.news_1.is_shown)

    def test_models_methods(self):
        self.news_1.publish()
        self.assertTrue(News.objects.get(id=self.news_1.id).is_shown)
