from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

geckodriver_path = r'C:\Users\Romas\geckodriver\geckodriver.exe'

class NewVisitorTest(unittest.TestCase):  
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=geckodriver_path)

    def tearDown(self):
        self.browser.quit()

    def check_for_li_in_skill_list(self, li_text):
        ul = self.browser.find_element_by_id('skill-list')
        list_items = ul.find_elements_by_tag_name('li')
        self.assertIn(li_text, [li.text for li in list_items])

    def test_can_add_to_skill_list_and_retrieve_it_later(self):
        # Open homepage
        self.browser.get('http://127.0.0.1:8000/cv/')

        # Check the page title
        self.assertIn('Rmlds | Personal Website | University Coursework', self.browser.title)

        # Check the header
        header_text = self.browser.find_element_by_class_name('cv-title').text
        self.assertIn('Personal CV', header_text)

        # We are invited to enter a skill straight away
        inputbox = self.browser.find_element_by_id('new-skill')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a new skill'
        )

        # We type 'Communication'
        inputbox.send_keys('Communication')

        # When we hit enter, the page updates, and now the page lists
        # 'Communication' as an item in a skill list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        self.check_for_li_in_skill_list('Communication')

        # We see a text box inviting us to add another item.
        # We enter 'Presentation'
        inputbox = self.browser.find_element_by_id('new-skill')
        inputbox.send_keys('Presentation')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        # The page updates again, and now shows both items in the list
        self.check_for_li_in_skill_list('Communication')
        self.check_for_li_in_skill_list('Presentation')

        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
