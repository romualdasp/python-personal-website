from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import cv_preview
from cv.models import Skill

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

    def test_can_save_a_POST_request(self):
        response = self.client.post('/cv/', data={'skill_text': 'New skill text'})
        self.assertIn('New skill text', response.content.decode())
        self.assertTemplateUsed(response, 'cv/cv_preview.html')

class SkillModelTest(TestCase):

    def test_saving_and_retrieving_skills(self):
        first_skill = Skill()
        first_skill.text = 'The first skill'
        first_skill.save()

        second_skill = Skill()
        second_skill.text = 'The second skill'
        second_skill.save()

        saved_skills = Skill.objects.all()
        self.assertEqual(saved_skills.count(), 2)

        self.assertEqual(saved_skills[0].text, 'The first skill')
        self.assertEqual(saved_skills[1].text, 'The second skill')

