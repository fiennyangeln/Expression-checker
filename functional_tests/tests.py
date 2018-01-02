from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import os

class Checker(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_interface(self):
        #self.browser.get('http://localhost:8000')

        #check title and header
        self.assertIn('Math Checker',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Math Checker', header_text)

        #get the inputboxes and enter attribute
        input_box_1 = self.browser.find_element_by_id('value-1')
        input_box_1.send_keys('1+1')
        input_box_2 = self.browser.find_element_by_id('value-2')
        input_box_2.send_keys('2')

        #send the attribute entered
        input_box_1.send_keys(Keys.ENTER)
        time.sleep(1000)

        #check the result
        #result = self.browser.find_element_by_id('result')
        #self.assertEqual('True', result)


if __name__=='__main__':
    unittest.main(warnings='ignore')
