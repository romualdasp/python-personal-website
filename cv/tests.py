from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import cv_preview
from cv.models import Skill, Education, Achievement, Course

# Create your tests here.

class SkillPagesTest(TestCase):

    def test_uses_correct_template(self):
        response = self.client.get('/cv/skill/new/')
        self.assertTemplateUsed(response, 'cv/cv_new.html')

    def test_saves_POST_request(self):
        response = self.client.post('/cv/skill/new/', data={
            'title': 'saves_POST_request'
        })

        self.assertEqual(Skill.objects.count(), 1)
        self.assertEqual(Skill.objects.first().title, 'saves_POST_request')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/skill/new/', data={
            'title': 'redirects_after_POST'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/skill/new/')
        self.assertEqual(Skill.objects.count(), 0)

    def test_displays_all_items(self):
        Skill.objects.create(title='displays_all_items 1')
        Skill.objects.create(title='displays_all_items 2')

        response = self.client.get('/cv/')

        self.assertIn('displays_all_items 1', response.content.decode())
        self.assertIn('displays_all_items 2', response.content.decode())

class SkillModelTest(TestCase):

    def test_saving_and_retrieving_skills(self):
        Skill.objects.create(title='The first skill')
        Skill.objects.create(title='The second skill')

        saved_skills = Skill.objects.all()
        self.assertEqual(saved_skills.count(), 2)

        self.assertEqual(saved_skills[0].title, 'The first skill')
        self.assertEqual(saved_skills[1].title, 'The second skill')

class EducationPagesTest(TestCase):

    def test_uses_correct_template(self):
        response = self.client.get('/cv/education/new/')
        self.assertTemplateUsed(response, 'cv/cv_new.html')

    def test_saves_POST_request(self):
        response = self.client.post('/cv/education/new/', data={
            'title': 'saves_POST_request title',
            'date': 'saves_POST_request date',
            'description': 'saves_POST_request desc',
        })

        self.assertEqual(Education.objects.count(), 1)

        saved = Education.objects.first()
        self.assertEqual(saved.title, 'saves_POST_request title')
        self.assertEqual(saved.date, 'saves_POST_request date')
        self.assertEqual(saved.description, 'saves_POST_request desc')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/education/new/', data={
            'title': 'redirects_after_POST title',
            'date': 'redirects_after_POST date',
            'description': 'redirects_after_POST desc',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/education/new/')
        self.assertEqual(Education.objects.count(), 0)

    def test_displays_all_items(self):
        Education.objects.create(title='displays_all_items 1', date=2010, description='desc 1')
        Education.objects.create(title='displays_all_items 2', date=2012, description='desc 2')

        response = self.client.get('/cv/')

        self.assertIn('displays_all_items 1', response.content.decode())
        self.assertIn('displays_all_items 2', response.content.decode())

class EducationModelTest(TestCase):

    def test_saving_and_retrieving_educations(self):
        Education.objects.create(title='The first education', date='2018', description='first')
        Education.objects.create(title='The second education', date='2020', description='second')

        saved_educations = Education.objects.all()
        self.assertEqual(saved_educations.count(), 2)

        self.assertEqual(saved_educations[0].title, 'The first education')
        self.assertEqual(saved_educations[0].date, '2018')
        self.assertEqual(saved_educations[0].description, 'first')

        self.assertEqual(saved_educations[1].title, 'The second education')
        self.assertEqual(saved_educations[1].date, '2020')
        self.assertEqual(saved_educations[1].description, 'second')

class AchievementPagesTest(TestCase):

    def test_uses_correct_template(self):
        response = self.client.get('/cv/achievement/new/')
        self.assertTemplateUsed(response, 'cv/cv_new.html')

    def test_saves_POST_request(self):
        response = self.client.post('/cv/achievement/new/', data={
            'title': 'saves_POST_request title',
            'date': 'saves_POST_request date',
        })

        self.assertEqual(Achievement.objects.count(), 1)

        saved = Achievement.objects.first()
        self.assertEqual(saved.title, 'saves_POST_request title')
        self.assertEqual(saved.date, 'saves_POST_request date')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/achievement/new/', data={
            'title': 'redirects_after_POST title',
            'date': 'redirects_after_POST date',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/achievement/new/')
        self.assertEqual(Achievement.objects.count(), 0)

    def test_displays_all_items(self):
        Achievement.objects.create(title='displays_all_items 1', date=2015)
        Achievement.objects.create(title='displays_all_items 2', date=2016)

        response = self.client.get('/cv/')

        self.assertIn('displays_all_items 1', response.content.decode())
        self.assertIn('displays_all_items 2', response.content.decode())

class AchievementModelTest(TestCase):

    def test_saving_and_retrieving_achievements(self):
        Achievement.objects.create(title='The first achievement', date='2016')
        Achievement.objects.create(title='The second achievement', date='2019')

        saved_achievements = Achievement.objects.all()
        self.assertEqual(saved_achievements.count(), 2)

        self.assertEqual(saved_achievements[0].title, 'The first achievement')
        self.assertEqual(saved_achievements[0].date, '2016')

        self.assertEqual(saved_achievements[1].title, 'The second achievement')
        self.assertEqual(saved_achievements[1].date, '2019')

class CoursePagesTest(TestCase):

    def test_uses_correct_template(self):
        response = self.client.get('/cv/course/new/')
        self.assertTemplateUsed(response, 'cv/cv_new.html')

    def test_saves_POST_request(self):
        response = self.client.post('/cv/course/new/', data={
            'title': 'saves_POST_request title',
        })

        self.assertEqual(Course.objects.count(), 1)

        saved = Course.objects.first()
        self.assertEqual(saved.title, 'saves_POST_request title')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/course/new/', data={
            'title': 'redirects_after_POST title',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/course/new/')
        self.assertEqual(Course.objects.count(), 0)

    def test_displays_all_items(self):
        Course.objects.create(title='displays_all_items 1')
        Course.objects.create(title='displays_all_items 2')

        response = self.client.get('/cv/')

        self.assertIn('displays_all_items 1', response.content.decode())
        self.assertIn('displays_all_items 2', response.content.decode())

class CourseModelTest(TestCase):

    def test_saving_and_retrieving_achievements(self):
        Course.objects.create(title='The first course')
        Course.objects.create(title='The second course')

        saved_courses = Course.objects.all()
        self.assertEqual(saved_courses.count(), 2)

        self.assertEqual(saved_courses[0].title, 'The first course')
        self.assertEqual(saved_courses[1].title, 'The second course')
