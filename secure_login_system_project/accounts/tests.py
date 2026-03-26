from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthenticationFlowTests(TestCase):
    def test_register_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_protected_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_user_can_login(self):
        User.objects.create_user(username='testuser', password='StrongPass123!')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'StrongPass123!'
        })
        self.assertEqual(response.status_code, 302)
