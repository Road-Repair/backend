from datetime import timedelta
from http import HTTPStatus

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from core.fixtures import TestUserFixtures
from users.models import Account
from users.tests.factories import CustomUserFactory

User = get_user_model()


class TestUser(TestUserFixtures):
    def setUp(self):
        self.old_email_backend = settings.EMAIL_BACKEND
        settings.EMAIL_BACKEND = (
            "django.core.mail.backends.locmem.EmailBackend"
        )

    def tearDown(self):
        settings.EMAIL_BACKEND = self.old_email_backend

    def test_user_registry(self):
        email = "user@foo.com"
        phone = "+79999879887"
        username = "user"
        body = {"email": email, "phone": phone, "username": username}
        response = self.anon_client.post(
            reverse("users-list"), data=body, format="json"
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(
            User.objects.filter(
                email=email, phone=phone, username=username
            ).exists()
        )

    def test_get_account(self):
        response = self.client_1.get(reverse("accounts"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_change_account(self):
        patronymic = "some_name"
        date_birth = timezone.now().date() - timedelta(weeks=55 * 18)
        last_name = "last_name"
        first_name = "first_name"
        data = {
            "user": {"last_name": last_name, "first_name": first_name},
            "patronymic": patronymic,
            "date_birth": date_birth,
            "sex": 1,
        }
        response = self.client_1.put(
            reverse("accounts"), data=data, format="json"
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        user_account = Account.objects.filter(user=self.user).first()
        self.assertEqual(user_account.patronymic, patronymic)
        self.assertEqual(user_account.date_birth, date_birth)
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        response_2 = self.anon_client.put(
            reverse("accounts"), data=data, format="json"
        )
        self.assertEqual(response_2.status_code, HTTPStatus.UNAUTHORIZED)

    def test_partially_change_account(self):
        patronymic = "another_name"
        data = {
            "patronymic": patronymic,
        }
        response = self.client_1.patch(
            reverse("accounts"), data=data, format="json"
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        user_account = Account.objects.filter(user=self.user).first()
        self.assertEqual(user_account.patronymic, patronymic)
        response_2 = self.anon_client.put(
            reverse("accounts"), data=data, format="json"
        )
        self.assertEqual(response_2.status_code, HTTPStatus.UNAUTHORIZED)

    def test_user_logout(self):
        response = self.client_1.post(reverse("logout"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_user_login(self):
        phone = "+71000000000"
        password = "super_password"
        CustomUserFactory(phone=phone, password=password)
        data = {"phone": phone, "password": password}
        response = self.client_1.post(reverse("login"), data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data, {"Success": "Login successfully"})

    def test_anon_client_does_not_have_access(self):
        response = self.anon_client.get(reverse("accounts"))
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_refresh_tokens(self):
        response = self.anon_client.post(reverse("token_refresh"))
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
