from selenium import webdriver
import unittest

class Checker(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_interface(self):
        browser.get('http://localhost:8000')

        self.assertIn('Math Checker',self.browser.title)

if __name__=='__main__':
    unittest.main(warnings='ignore')
