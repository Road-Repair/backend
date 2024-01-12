import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from news.models import News
from news.tests.factories import NewsFactory

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class NewssModelsTest(TestCase):
    """
    Класс для тестирования моделей приложения news.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        small_gif = (
            b"\x47\x49\x46\x38\x39\x61\x02\x00"
            b"\x01\x00\x80\x00\x00\x00\x00\x00"
            b"\xFF\xFF\xFF\x21\xF9\x04\x00\x00"
            b"\x00\x00\x00\x2C\x00\x00\x00\x00"
            b"\x02\x00\x01\x00\x00\x02\x02\x0C"
            b"\x0A\x00\x3B"
        )
        uploaded = SimpleUploadedFile(
            name="small.gif", content=small_gif, content_type="image/gif"
        )
        cls.news_1 = NewsFactory(image=uploaded)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_news_creation(self):
        self.assertEqual(self.news_1.image, "news_images/small.gif")

    def test_models_have_correct_object_names(self):
        self.assertEqual(str(self.news_1), self.news_1.title)

    def test_models_default_values(self):
        self.assertFalse(self.news_1.is_shown)

    def test_models_methods(self):
        self.news_1.publish()
        self.assertTrue(News.objects.get(id=self.news_1.id).is_shown)
