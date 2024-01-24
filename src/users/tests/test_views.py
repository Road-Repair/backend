from http import HTTPStatus

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

from core.fixtures import TestUserFixtures
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
        response = self.user_client.get(reverse("accounts"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_user_logout(self):
        response = self.user_client.post(reverse("logout"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
