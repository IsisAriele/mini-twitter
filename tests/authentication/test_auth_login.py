from django.test import TestCase
from rest_framework.test import APIClient
from tests.utils.get_user_data import get_default_user_data
from users.models import UserModel


class TestAuthLogin(TestCase):
    def setUp(self):
        self.client = APIClient()
        UserModel.objects.create_user(**get_default_user_data())

    def test_should_login_user_successfully(self):
        response = self.client.post(
            "/auth/login/", {"username": "testuser", "password": "testuserpassword"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_should_return_error_when_username_or_password_is_incorrect(self):
        response = self.client.post(
            "/auth/login/", {"username": "wronguser", "password": "wrongpassword"}
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data["detail"],
            "No active account found with the given credentials",
        )
