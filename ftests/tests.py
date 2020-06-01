from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

geckodriver_path = r'C:\Users\Romas\geckodriver\geckodriver.exe'

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        # self.fail('URLs in this class require login. Please remove @login_required in views.py :)')
        self.browser = webdriver.Firefox(executable_path=geckodriver_path)

    def tearDown(self):
        self.browser.quit()

    def item_in_list(self, item, list):
        ul = self.browser.find_element_by_id(list)
        list_items = ul.find_elements_by_tag_name('li')
        return (item in [li.text for li in list_items])

    def check_item_in_list(self, item, list):
        self.assertTrue(self.item_in_list(item, list))

    def check_item_not_in_list(self, item, list):
        self.assertFalse(self.item_in_list(item, list))

    def click_button(self, id):
        button = self.browser.find_element_by_id(id)
        button.click()
        time.sleep(2)

    def populate_field(self, id, text):
        inputbox = self.browser.find_element_by_id(id)
        inputbox.send_keys(text)

    def hit_enter(self):
        inputbox = self.browser.find_element_by_tag_name('body')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

    def check_header_exists(self, header):
        headers = self.browser.find_elements_by_class_name('cv-title')
        self.assertIn(header, [h.text for h in headers])

    def delete_item_in_list(self, item, list):
        ul = self.browser.find_element_by_id(list)
        list_items = ul.find_elements_by_tag_name('li')
        for i in list_items:
            if i.text == item:
                i.find_element_by_tag_name('a').click()
                break
        time.sleep(2)

    def test_can_add_to_skill_list_and_retrieve_it_later(self):
        # Open homepage
        self.browser.get(self.live_server_url + '/cv/')

        # Check the page title
        self.assertIn('Rmlds | Personal Website | University Coursework', self.browser.title)

        # Check the header exists
        self.check_header_exists('Skills') # Education, Achievements, Courses

        # We click a button to enter a new skill
        self.click_button('add-skill')

        # We type 'Communication'
        self.populate_field('id_title', 'Communication')

        # When we hit enter, the page redirects, and now it lists
        # 'Communication' as an item in a skill list
        self.hit_enter()

        self.check_item_in_list('Communication', 'skill-list')

        # We click a button to add another item
        self.click_button('add-skill')

        # We type 'Presentation' and hit enter
        self.populate_field('id_title', 'Presentation')
        self.hit_enter()

        # The page redirects, and now shows both items in the list
        self.check_item_in_list('Communication', 'skill-list')
        self.check_item_in_list('Presentation', 'skill-list')

        # We click delete next to 'Communication'
        self.delete_item_in_list('Communication', 'skill-list')

        # The item is deleted and no longer in the list
        self.check_item_not_in_list('Communication', 'skill-list')
        self.check_item_in_list('Presentation', 'skill-list')

        self.fail('YAY everything works! :)')
