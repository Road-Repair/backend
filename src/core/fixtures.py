from rest_framework.test import APIClient, APITestCase

from users.tests.factories import CustomUserFactory


class TestUserFixtures(APITestCase):
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
