"""
Tests for Models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """
        Test creating a user with an email is successful
        """
        email = "test@email.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalized(self):
        """
        Test if email is normalized for new users
        """
        emails = [
            ["Test1@EXAMPLE.com", "Test1@example.com"],
            ["TEST2@EXAMPLE.COM", "TEST2@example.com"],
            ["tEST3@exaMPLE.cOM", "tEST3@example.com"],
            ["test4@EXAMPLE.COM", "test4@example.com"],
        ]

        for email, expected in emails:
            user = get_user_model().objects.create_user(email, "testpass123")
            self.assertEqual(user.email, expected)

    def test_new_email_without_email_raises_error(self):
        """Test that creating a new user without an email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "testpass123")

    def test_create_superuser(self):
        """Test creating a super user"""
        super_user = get_user_model().objects.create_superuser(
            "test123@example.com", "testpass123"
        )
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
