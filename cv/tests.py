from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import cv_preview
from cv.models import Skill, Education, Achievement, Course

# Create your tests here.

# This class wont be executed by the test runner
# It is used to share tests
class SharedPagesTest(object):

    # these variables must be overridden by the child classes
    _ModelUsed = None

    create_url = '/unset/'
    delete_url = '/unset/'

    data = []
    
    def test_uses_correct_template(self):
        response = self.client.get(self.create_url)
        self.assertTemplateUsed(response, 'cv/cv_new.html')

    def test_saves_POST_request(self):
        data = self.data

        response = self.client.post(self.create_url, data[0])

        self.assertEqual(self._ModelUsed.objects.count(), 1)
        for key in data[0]:
            actual = getattr(self._ModelUsed.objects.first(), key)
            expected = data[0][key]
            self.assertEqual(actual, expected)

    def test_redirects_after_POST(self):
        data = self.data

        response = self.client.post(self.create_url, data[0])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_only_saves_items_when_necessary(self):
        self.client.get(self.create_url)
        self.assertEqual(self._ModelUsed.objects.count(), 0)

    def test_displays_all_items(self):
        data = self.data

        self._ModelUsed.objects.create(**data[0])
        self._ModelUsed.objects.create(**data[1])

        response = self.client.get('/cv/')

        self.assertIn(data[0]['title'], response.content.decode())
        self.assertIn(data[1]['title'], response.content.decode())

    def test_deletes_items_correctly(self):
        data = self.data

        self._ModelUsed.objects.create(**data[0])
        self._ModelUsed.objects.create(**data[1])

        response = self.client.get(self.delete_url + '1/')
        response = self.client.get('/cv/')

        self.assertNotIn(data[0]['title'], response.content.decode())
        self.assertIn(data[1]['title'], response.content.decode())

class SkillPagesTest(TestCase, SharedPagesTest):

    _ModelUsed = Skill

    create_url = '/cv/skill/new/'
    delete_url = '/cv/skill/remove/'

    data = [
        {'title': 'GreatSkill1'},
        {'title': 'GreatSkill2'}]

class EducationPagesTest(TestCase, SharedPagesTest):

    _ModelUsed = Education

    create_url = '/cv/education/new/'
    delete_url = '/cv/education/remove/'

    data = [
        {'title': 'TheEducation1', 'date': '2019', 'description': 'education1'},
        {'title': 'TheEducation2', 'date': '2018', 'description': 'education2'}]

class AchievementPagesTest(TestCase, SharedPagesTest):

    _ModelUsed = Achievement

    create_url = '/cv/achievement/new/'
    delete_url = '/cv/achievement/remove/'

    data = [
        {'title': 'NiceAchievement1', 'date': '2020'},
        {'title': 'NiceAchievement2', 'date': '2019'}]

class CoursePagesTest(TestCase, SharedPagesTest):

    _ModelUsed = Course

    create_url = '/cv/course/new/'
    delete_url = '/cv/course/remove/'

    data = [
        {'title': 'NiceCourse1'},
        {'title': 'NiceCourse2'}]


class SharedModelTest(object):

    # these variables must be overridden by the child classes
    _ModelUsed = None
    data = []
    
    def test_saving_and_retrieving(self):
        data = self.data

        for i in range(len(data)):
            self._ModelUsed.objects.create(**data[i])

        saved = self._ModelUsed.objects.all()
        self.assertEqual(saved.count(), len(data))

        for i in range(len(data)):
            for key in data[i]:
                actual = getattr(saved[i], key)
                expected = data[i][key]
                self.assertEqual(actual, expected)

class SkillModelTest(TestCase, SharedModelTest):

    _ModelUsed = Skill
    data = [{'title': 'The first skill'}, {'title': 'The second skill'}]

class EducationModelTest(TestCase, SharedModelTest):

    _ModelUsed = Education
    data = [
        {'title': 'The first education', 'date': '2018', 'description': 'first'},
        {'title': 'The second education', 'date': '2020', 'description': 'second'}]


class AchievementModelTest(TestCase, SharedModelTest):

    _ModelUsed = Achievement
    data = [
        {'title': 'The first achievement', 'date': '2016'},
        {'title': 'The second achievement', 'date': '2019'}]

class CourseModelTest(TestCase, SharedModelTest):

    _ModelUsed = Course
    data = [{'title': 'The first course'}, {'title': 'The second course'}]
