from .base import FunctionalTest
from selenium import webdriver
from django.contrib.auth.models import User
from time import sleep
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from .setup import add_new_place

class AddEditPlaceTest(FunctionalTest):
#TODO write helpers function to make code clearer (i.e type function)

    def test_add_place(self):
        self.log_in(self.username, self.password)
 
        self.browser.get('http://localhost:8000/new/location=51.00,17.00')

        name = self.browser.find_element_by_id('id_name')
        name.send_keys('Test Place')

        description = self.browser.find_element_by_id('id_description')
        description.send_keys('Test description')

        save_button = self.browser.find_element_by_css_selector('.save')
        save_button.click()

        place_title = self.browser.find_element_by_css_selector('.header h2')
        self.assertEqual(place_title.text, 'Test Place')

    def test_view_place(self):
        place_id = add_new_place(self.user)
        
        self.log_in(self.username, self.password)
 
        place = self.browser.find_element_by_css_selector('#map .leaflet-marker-pane img:first-child')
        place.click()
        popup_link = self.browser.find_element_by_css_selector('.leaflet-popup-content a')
        popup_link.click()

        place_title = self.browser.find_element_by_css_selector('.header h2')
        self.assertEqual(place_title.text, 'Test Place')

    def test_edit_place(self):
        place_id = add_new_place(self.user)

        self.log_in(self.username, self.password)

        self.browser.get(f'http://localhost:8000/{place_id}/')

        edit_button = self.browser.find_element_by_css_selector('.glyphicon-pencil')
        edit_button.click()

        new_name = ''.join(random.choices(string.ascii_uppercase, k=10))
        name = self.browser.find_element_by_id('id_name')
        name.clear()
        name.send_keys(new_name)

        new_description = ''.join(random.choices(string.ascii_uppercase, k=20))
        description = self.browser.find_element_by_id('id_description')
        description.clear()
        description.send_keys(new_description)

        save_button = self.browser.find_element_by_css_selector('.save')
        save_button.click()

        place_title = self.browser.find_element_by_css_selector('.header h2')
        self.assertEqual(place_title.text, new_name)

        description_field = self.browser.find_element_by_id('description')
        self.assertEqual(description_field.text, new_description)



    