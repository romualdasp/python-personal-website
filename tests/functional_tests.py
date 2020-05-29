from selenium import webdriver
import unittest

geckodriver_path = r'C:\Users\Romas\geckodriver\geckodriver.exe'

class NewVisitorTest(unittest.TestCase):  
    def setUp(self):  
        self.browser = webdriver.Firefox(executable_path=geckodriver_path)

    def tearDown(self):  
        self.browser.quit()

    def test_title(self):  
        # Go to homepage
        self.browser.get('http://127.0.0.1:8000')

        # Check the title
        self.assertIn('Rmlds | Personal Website | University Coursework', self.browser.title)  
        self.fail('Finished the test!')  

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
