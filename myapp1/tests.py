from django.test import TestCase
from django.urls import reverse


class MyApp1ViewsTests(TestCase):
    def test_blog_page(self):
        response = self.client.get(reverse('blog_posts'))
        self.assertEqual(response.status_code, 200)

# Create your tests here.
