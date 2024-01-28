from rest_framework.test import APIClient, APITestCase

from users.tests.factories import CustomUserFactory


class TestUserFixtures(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = CustomUserFactory()
        cls.user_2 = CustomUserFactory()
        cls.user_3 = CustomUserFactory()

        cls.client_1 = APIClient()
        cls.client_1.force_authenticate(cls.user)
        cls.client_2 = APIClient()
        cls.client_2.force_authenticate(cls.user_2)
        cls.client_3 = APIClient()
        cls.client_3.force_authenticate(cls.user_3)
        cls.anon_client = APIClient()
