from django.test import TestCase
from rest_framework.test import APIClient

from users.models import UserModel


class TestAuthRegister(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_should_register_user_successfully(self):
        user = UserModel.objects.filter(
            username="testuser", email="test@user.com"
        ).first()
        self.assertIsNone(user)

        response = self.client.post(
            "/auth/register/",
            {
                "username": "testuser",
                "password": "testuserpassword",
                "name": "Test User",
                "email": "test@user.com",
            },
        )

        self.assertEqual(response.status_code, 201)
        user = UserModel.objects.filter(
            username="testuser", email="test@user.com"
        ).first()
        self.assertIsNotNone(user)

    def test_should_return_error_when_mandatory_fields_are_missing(self):
        response = self.client.post(
            "/auth/register/", {"username": "", "password": "", "name": "", "email": ""}
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["username"][0], "This field may not be blank."),
        self.assertEqual(response.data["password"][0], "This field may not be blank."),
        self.assertEqual(response.data["name"][0], "This field may not be blank."),
        self.assertEqual(response.data["email"][0], "This field may not be blank."),

    def test_should_return_error_when_email_is_invalid(self):
        response = self.client.post(
            "/auth/register/",
            {
                "username": "testuser",
                "password": "testuserpassword",
                "name": "Test User",
                "email": "test",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["email"][0], "Enter a valid email address.")

    def test_should_return_error_when_username_and_email_already_exists(self):
        UserModel.objects.create(
            username="testuser",
            password="testuserpassword",
            name="Test User",
            email="test@user.com",
        )

        response = self.client.post(
            "/auth/register/",
            {
                "username": "testuser",
                "password": "testuserpassword",
                "name": "Test User",
                "email": "test@user.com",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data["username"][0], "A user with that username already exists."
        )
        self.assertEqual(
            response.data["email"][0], "User Model with this email already exists."
        )
