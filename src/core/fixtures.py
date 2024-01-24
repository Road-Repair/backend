from rest_framework.test import APITestCase, APIClient

from users.tests.factories import CustomUserFactory


class TestUserFixtures(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = CustomUserFactory()

        cls.user_client = APIClient()
        cls.user_client.force_authenticate(cls.user)
        cls.anon_client = APIClient()
