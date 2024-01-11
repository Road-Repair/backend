from rest_framework.test import APIClient, APITestCase

from users.models import CustomUser as User


class TestUserFixture(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User(
            email="vasya@vasya.ru",
            first_name="Vasya",
            last_name="Vasya",
            phone_number="+71110000000",
            password="vasya123",
        )
        cls.user.set_password("vasya123")
        cls.user.save()
        cls.user2 = User(
            email="petya@petya.ru",
            first_name="Petya",
            password="petya123",
            phone_number="+71110000001",
            last_name="Petya",
        )
        cls.user2.set_password("petya123")
        cls.user2.save()
        cls.user3 = User(
            email="vanya@vanya.ru",
            first_name="Vanya",
            last_name="Vanya",
            phone_number="+71110000002",
            password="vanya123",
        )
        cls.user3.set_password("vanya123")
        cls.user3.save()

        cls.user_client = APIClient()
        cls.user_client.force_authenticate(cls.user)
        cls.user2_client = APIClient()
        cls.user2_client.force_authenticate(cls.user2)
