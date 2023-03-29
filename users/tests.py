from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='testuser@example.com'
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        superuser = self.User.objects.create_superuser(
            username='adminuser',
            password='adminpass123',
            email='adminuser@example.com'
        )
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertEqual(str(superuser), 'adminuser')

    def test_username_max_length(self):
        max_length = self.user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150)

    def test_email_max_length(self):
        max_length = self.user._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)
