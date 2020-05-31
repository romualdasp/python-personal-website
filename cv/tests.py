from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import cv_preview
from cv.models import Skill

# Create your tests here.

class HomePageTest(TestCase):

    # Testing using Django Test Client

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_preview.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/cv/', data={'skill_text': 'New skill text'})

        self.assertEqual(Skill.objects.count(), 1)
        new_skill = Skill.objects.first()
        self.assertEqual(new_skill.text, 'New skill text')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/', data={'skill_text': 'New skill text'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/')
        self.assertEqual(Skill.objects.count(), 0)

    def test_displays_all_items(self):
        Skill.objects.create(text='itemey 1')
        Skill.objects.create(text='itemey 2')

        response = self.client.get('/cv/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

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

