from django.test import TestCase
from django.urls import reverse


class MyAppViewsTests(TestCase):
    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_home_requires_login(self):
        response = self.client.get(reverse('home'))
        # unauthenticated users should be redirected to login
        self.assertEqual(response.status_code, 302)

# Create your tests here.
