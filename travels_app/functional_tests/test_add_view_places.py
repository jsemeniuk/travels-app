from .base import FunctionalTest
from selenium import webdriver
from django.contrib.auth.models import User
from time import sleep
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from .helpers import add_new_place, add_new_user

class AddEditPlaceTest(FunctionalTest):
#TODO write helpers function to make code clearer (i.e type function)
#TODO move actions repeatable between test to separate function 
#TODO create test setup for each test: add new user and new place for user
    def test_add_place(self):
        user = User.objects.filter(username='TestUser')[0]
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        log_in = self.browser.find_element_by_css_selector('.top-menu a[href*=login]')
        log_in.click()
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('TestUser')
        username = self.browser.find_element_by_id('id_password')
        username.send_keys('T3stP4ss23')
        login_button = self.browser.find_element_by_css_selector('input[value=login]')
        login_button.click()

        self.browser.find_element_by_id('map')
        #TODO add better way to wait for map to load
        sleep(5)
 
        self.browser.get('http://localhost:8000/new&location=51.00,17.00')

        name = self.browser.find_element_by_id('id_name')
        name.send_keys('Test Place')

        description = self.browser.find_element_by_id('id_description')
        description.send_keys('Test description')

        save_button = self.browser.find_element_by_css_selector('.save')
        save_button.click()

        place_title = self.browser.find_element_by_css_selector('.place h2')
        self.assertEqual(place_title.text, 'Test Place')

    def test_view_place(self):
        
        user = User.objects.filter(username='TestUser')[0]
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        log_in = self.browser.find_element_by_css_selector('.top-menu a[href*=login]')
        log_in.click()
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('TestUser')
        username = self.browser.find_element_by_id('id_password')
        username.send_keys('T3stP4ss23')
        login_button = self.browser.find_element_by_css_selector('input[value=login]')
        login_button.click()

        self.browser.find_element_by_id('map')
        #TODO add better way to wait for map to load
        sleep(5)
 
        place = self.browser.find_element_by_css_selector('#map .leaflet-marker-pane img:first-child')
        place.click()
        popup_link = self.browser.find_element_by_css_selector('.leaflet-popup-content a')
        popup_link.click()

        place_title = self.browser.find_element_by_css_selector('.place h2')
        self.assertEqual(place_title.text, 'Borowa')

    def test_edit_place(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        log_in = self.browser.find_element_by_css_selector('.top-menu a[href*=login]')
        log_in.click()
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('TestUser')
        username = self.browser.find_element_by_id('id_password')
        username.send_keys('T3stP4ss23')
        login_button = self.browser.find_element_by_css_selector('input[value=login]')
        login_button.click()

        self.browser.get('http://localhost:8000/18/')

        edit_button = self.browser.find_element_by_css_selector('.glyphicon-pencil')
        edit_button.click()

        new_name = ''.join(random.choices(string.ascii_uppercase, k=10))
        name = self.browser.find_element_by_id('id_name')
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        name.send_keys(new_name)

        new_description = ''.join(random.choices(string.ascii_uppercase, k=20))
        description = self.browser.find_element_by_id('id_description')
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        description.send_keys(new_description)

        save_button = self.browser.find_element_by_css_selector('.save')
        save_button.click()

        place_title = self.browser.find_element_by_css_selector('.place h2')
        self.assertEqual(place_title.text, new_name)

        description_field = self.browser.find_element_by_id('description')
        self.assertEqual(description_field.text, new_description)



    