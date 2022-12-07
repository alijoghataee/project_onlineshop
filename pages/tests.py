from django.test import TestCase
from django.urls import reverse


class PagesTest(TestCase):

    def test_home_page_view_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_view(self):
        self.client.get(reverse('home'))
        self.assertTemplateUsed('pages/home_page.html')
