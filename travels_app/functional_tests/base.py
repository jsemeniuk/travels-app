from selenium import webdriver
from django.test import TestCase
import unittest
from time import sleep
from datetime import datetime
from my_travels.models import Places

from django.contrib.auth.models import User

MAX_WAIT = 10

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        
    def tearDown(self):
        self.browser.quit()

    def log_in(self, username, password):
        login_link = self.browser.find_element_by_css_selector('li a[href*=login]')
        login_link.click()

        username_field = self.browser.find_element_by_id('id_username')
        username_field.send_keys(username)
        password_field = self.browser.find_element_by_id('id_password')
        password_field.send_keys(password)
        login_button = self.browser.find_element_by_css_selector('input[value=login]')
        login_button.click()

        self.browser.find_element_by_id('map')
        #TODO add better way to wait for map to load
        sleep(5)
    
        