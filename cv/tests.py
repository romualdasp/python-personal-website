from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import cv_preview

# Create your tests here.

class HomePageTest(TestCase):

    def test_cv_url_resolves_to_cv_preview_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_preview)

    def test_cv_preview_returns_correct_html(self):
        request = HttpRequest()
        response = cv_preview(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>Rmlds | Personal Website | University Coursework</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
