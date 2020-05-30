from django.test import TestCase
from django.urls import resolve
from cv.views import cv_preview

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/cv/')  
        self.assertEqual(found.func, cv_preview)
