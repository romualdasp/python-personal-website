from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

geckodriver_path = r'C:\Users\Romas\geckodriver\geckodriver.exe'

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=geckodriver_path)

    def tearDown(self):
        self.browser.quit()

    def check_for_item_in_list(self, item, list):
        ul = self.browser.find_element_by_id(list)
        list_items = ul.find_elements_by_tag_name('li')
        self.assertIn(item, [li.text for li in list_items])

    def test_can_add_to_skill_list_and_retrieve_it_later(self):
        self.fail('URLs in this test require login. Please remove @login_required in views.py :)')

        # Open homepage
        self.browser.get(self.live_server_url + '/cv/')

        # Check the page title
        self.assertIn('Rmlds | Personal Website | University Coursework', self.browser.title)

        # Check all headers exist
        headers = self.browser.find_elements_by_class_name('cv-title')
        self.assertIn('Skills', [h.text for h in headers])
        self.assertIn('Education', [h.text for h in headers])
        self.assertIn('Achievements', [h.text for h in headers])
        self.assertIn('Courses', [h.text for h in headers])

        # We click a button to enter a new skill
        add_skill = self.browser.find_element_by_id('add-skill')
        add_skill.click()
        time.sleep(2)

        # We type 'Communication'
        inputbox = self.browser.find_element_by_id('id_title')
        inputbox.send_keys('Communication')

        # When we hit enter, the page redirects, and now it lists
        # 'Communication' as an item in a skill list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        self.check_for_item_in_list('Communication', 'skill-list')

        # We click a button to add another item
        add_skill = self.browser.find_element_by_id('add-skill')
        add_skill.click()
        time.sleep(2)

        # We type 'Presentation' and hit enter
        inputbox = self.browser.find_element_by_id('id_title')
        inputbox.send_keys('Presentation')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        # The page redirects, and now shows both items in the list
        self.check_for_item_in_list('Communication', 'skill-list')
        self.check_for_item_in_list('Presentation', 'skill-list')

        # self.fail('YAY everything works! :)')
