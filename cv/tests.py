from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import cv_preview

# Create your tests here.

class HomePageTest(TestCase):

    # Manual way of testing

    def test_cv_url_resolves_to_cv_preview_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_preview)

    def test_cv_preview_returns_correct_html(self):
        response = self.client.get('/cv/')

        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>Rmlds | Personal Website | University Coursework</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'cv/cv_preview.html')

    # Testing using Django Test Client

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_preview.html')
