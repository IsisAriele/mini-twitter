from django.test import TestCase
from users.models import CustomUser
from rest_framework.test import APIClient


class TestAuthRegister(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_should_register_user_successfully(self):
        user = CustomUser.objects.filter(username="testuser").first()
        self.assertIsNone(user)
        
        response = self.client.post(
            "/auth/register/",
            {
                "username": "testuser",
                "password": "testuserpassword",
                "name": "Test User",
                "email": "test@user.com"
            }
        )

        self.assertEqual(response.status_code, 201)
