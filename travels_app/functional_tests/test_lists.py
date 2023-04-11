from .base import FunctionalTest
from selenium import webdriver
from django.contrib.auth.models import User
from time import sleep
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class AddEditListsTest(FunctionalTest):
#TODO write helpers function to make code clearer (i.e type function)
#TODO move actions repeatable between test to separate function 
#TODO create test setup for each test: add new user / new place / new list
    def test_add_list(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        log_in = self.browser.find_element_by_css_selector('li a[href*=login]')
        log_in.click()
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('TestUser')
        username = self.browser.find_element_by_id('id_password')
        username.send_keys('T3stP4ss23')
        login_button = self.browser.find_element_by_css_selector('input[value=login]')
        login_button.click()

        lists_link = self.browser.find_element_by_css_selector('a[href*=lists]')
        lists_link.click()

        add_list_button = self.browser.find_element_by_css_selector('.glyphicon-plus')
        add_list_button.click()

        list_name = self.browser.find_element_by_id('id_name')
        list_name.send_keys('New list test')

        save_button = self.browser.find_element_by_css_selector('.save')
        save_button.click()

        list_name = self.browser.find_element_by_css_selector('.header h2')
        self.assertEqual(list_name.text, 'New list test')

        item_name = self.browser.find_element_by_id('id_name')
        item_name.send_keys('Checked item')
        item_checkobox = self.browser.find_element_by_id('id_item_done')
        item_checkobox.click()
        save_button = self.browser.find_element_by_css_selector('.save-button')
        save_button.click()

        first_item = self.browser.find_element_by_css_selector('#id_list_table tr:first-child td:first-child text')
        self.assertEqual(first_item.text, 'Checked item')
        first_item_checkobox = self.browser.find_element_by_id('item_1')
        self.assertEqual(first_item_checkobox.get_attribute("checked"), "true")

        item_name = self.browser.find_element_by_id('id_name')
        item_name.send_keys('Unchecked item')

        save_button = self.browser.find_element_by_css_selector('.save-button')
        save_button.click()

        second_item = self.browser.find_element_by_css_selector('#id_list_table tr:nth-child(2) td:first-child text')
        self.assertEqual(second_item.text, 'Unchecked item')
        second_item_checkobox = self.browser.find_element_by_id('item_2')
        self.assertEqual(second_item_checkobox.get_attribute("checked"), None)

    def test_add_list_for_place(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        log_in = self.browser.find_element_by_css_selector('li a[href*=login]')
        log_in.click()
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('TestUser')
        username = self.browser.find_element_by_id('id_password')
        username.send_keys('T3stP4ss23')
        login_button = self.browser.find_element_by_css_selector('input[value=login]')
        login_button.click()
        
        #TODO This should be part of setup
        self.browser.get('http://localhost:8000/new/location=51.00,17.00')

        name = self.browser.find_element_by_id('id_name')
        name.send_keys('Test Place')

        description = self.browser.find_element_by_id('id_description')
        description.send_keys('Test description')

        save_button = self.browser.find_element_by_css_selector('.save')
        save_button.click()

        edit_button = self.browser.find_element_by_css_selector('.glyphicon-pencil')
        edit_button.click()

        add_list_button = self.browser.find_element_by_css_selector("[href*='list/']")
        add_list_button.click()

        list_name = self.browser.find_element_by_id('id_name')
        list_name.send_keys('New list for place')

        save_button = self.browser.find_element_by_css_selector('.save')
        save_button.click()

        list_name = self.browser.find_element_by_css_selector('.header h2')
        self.assertEqual(list_name.text, 'New list for place')

