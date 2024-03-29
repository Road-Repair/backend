import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from rest_framework.test import APIClient, APITestCase

from locations.tests.factories import (
    FederationEntityFactory,
    RegionFactory,
    SettlementFactory,
)
from users.tests.factories import CustomUserFactory

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class BaseTestCase(APITestCase):
    """
    Базовый класс для тестирования моделей.
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
        cls.file_name = "small_1.gif"
        cls.uploaded = SimpleUploadedFile(
            name=cls.file_name, content=small_gif, content_type="image/gif"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)


class TestUserFixtures(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.phone = "+71000000001"
        cls.password = "super_password"
        cls.new_password = "new_super_password"
        cls.user = CustomUserFactory()
        cls.user_2 = CustomUserFactory()
        cls.user_3 = CustomUserFactory()
        cls.user_4 = CustomUserFactory(phone=cls.phone, password=cls.password)

        cls.client_1 = APIClient()
        cls.client_1.force_authenticate(cls.user)
        cls.client_2 = APIClient()
        cls.client_2.force_authenticate(cls.user_2)
        cls.client_3 = APIClient()
        cls.client_3.force_authenticate(cls.user_3)
        cls.client_4 = APIClient()
        cls.client_4.force_authenticate(cls.user_4)
        cls.anon_client = APIClient()


class LocationsFixtures(TestUserFixtures):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.federation_entity_1 = FederationEntityFactory()
        cls.federation_entity_2 = FederationEntityFactory()
        cls.region_1_1 = RegionFactory(
            federation_entity=cls.federation_entity_1
        )
        cls.region_1_1 = RegionFactory(
            federation_entity=cls.federation_entity_1
        )
        cls.region_2_1 = RegionFactory(
            federation_entity=cls.federation_entity_2
        )
        cls.region_2_2 = RegionFactory(
            federation_entity=cls.federation_entity_2
        )
        cls.settlement_1 = SettlementFactory(region=cls.region_2_1)
        cls.settlement_2 = SettlementFactory(region=cls.region_1_1)
