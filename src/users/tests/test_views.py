from http import HTTPStatus

from django.conf import settings
from django.urls import reverse

from core.fixtures import TestUserFixtures


class TestUser(TestUserFixtures):
    def setUp(self):
        self.old_email_backend = settings.EMAIL_BACKEND
        settings.EMAIL_BACKEND = (
            "django.core.mail.backends.locmem.EmailBackend"
        )

    def tearDown(self):
        settings.NUM_LATEST = self.old_email_backend

    def test_user_registry(self):
        email = "user@foo.com"
        phone = "+79999879887"
        username = "user"
        body = {"email": email, "phone": phone, "username": username}
        response = self.anon_client.post(
            reverse("users-list"), data=body, format="json"
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
