from .base import FunctionalTest
from selenium import webdriver
from django.contrib.auth.models import User
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from .helpers import add_new_place, add_new_user

class AddEditPlaceTest(FunctionalTest):

    def test_add_place(self):
        #TODO create test setup: add new user and new place for user
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
 
        add_icon = self.browser.find_element_by_css_selector('.top-menu-add')
        add_icon.click()

        name = self.browser.find_element_by_id('id_name')
        name.send_keys('Test Place')

        description = self.browser.find_element_by_id('id_description')
        description.send_keys('Test description')

        #TODO find better way to click more specific place on map
        location_map = self.browser.find_element_by_css_selector('#id_location_map canvas')
        action = ActionChains(self.browser)
        action.move_to_element(location_map).click().perform()

        save_button = self.browser.find_element_by_css_selector('.save')
        save_button.click()

        place_title = self.browser.find_element_by_css_selector('.place h2')
        self.assertEqual(place_title.text, 'Test Place')

    def test_view_place(self):
        #TODO create test setup: add new user and new place for user
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



    