from django.test import TestCase
from users.models import UserModel
from rest_framework.test import APIClient

class TestAuthRefresh(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserModel.objects.create_user(
            username="testuser",
            password="testuserpassword",
            name="Test User",
            email="test@user.com"
        )
        login_response = self.client.post(
            "/auth/login/",
            {
                "username": "testuser", 
                "password": "testuserpassword"
            }
        )
        self.refresh_token = login_response.data["refresh"]

    def test_should_refresh_token_successfully(self):
        response = self.client.post(
            "/auth/refresh/",
            {"refresh": self.refresh_token}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_should_return_error_with_invalid_refresh_token(self):
        response = self.client.post(
            "/auth/refresh/",
            {"refresh": "invalid.token.here"}
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data["code"], "token_not_valid")
        self.assertEqual(response.data["detail"], "Token is invalid")
