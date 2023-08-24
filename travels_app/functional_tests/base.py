from selenium import webdriver
from django.test import TestCase
import unittest
from time import sleep

from .setup import add_new_user, delete_user

from django.contrib.auth.models import User
from selenium.webdriver.common.by import By

MAX_WAIT = 10

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.get('http://localhost:8000')
        user_details = add_new_user()
        self.username = user_details[0]
        self.password = user_details[1]
        self.user = user_details[2]
        
    def tearDown(self):
        self.browser.quit()
        delete_user(self.user)

    def log_in(self, username, password):
        menu_icon = self.browser.find_element(By.CSS_SELECTOR, '.btn-header')
        menu_icon.click()
        login_link = self.browser.find_element(By.CSS_SELECTOR, 'li a[href*=login]')
        login_link.click()

        username_field = self.browser.find_element(By.ID, 'id_username')
        username_field.send_keys(username)
        password_field = self.browser.find_element(By.ID, 'id_password')
        password_field.send_keys(password)
        login_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-primary')
        login_button.click()

        self.browser.find_element(By.ID, 'map')
        #TODO add better way to wait for map to load
        sleep(5)
    
        