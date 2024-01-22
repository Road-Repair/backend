from http import HTTPStatus

from core.fixtures import TestUserFixtures


class TestUser(TestUserFixtures):
    def test_user_registry(self):
        email = "user@foo.com"
        phone = "+79999879887"
        username = "user"
        body = {
            "email": email,
            "phone": phone,
            "username": username
        }
        response = self.anon_client.post(
            "/api/v1/users/", data=body, format="json"
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
