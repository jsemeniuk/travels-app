from .base import FunctionalTest
from .setup import add_new_user, add_new_place, delete_user, add_new_list, add_item_to_list
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

    def add_list(self, list_name: str):
        list_name_field = self.browser.find_element_by_id('id_name')
        list_name_field.clear()
        list_name_field.send_keys(list_name)

        save_button = self.browser.find_element_by_css_selector('.save-button')
        save_button.click()

        list_name_header = self.browser.find_element_by_css_selector('.header h2')
        self.assertEqual(list_name_header.text, list_name)

    def add_item(self, item_name: str, item_done: bool, item_no: int):
        item_name_field = self.browser.find_element_by_id('id_name')
        item_name_field.send_keys(item_name)
        if item_done:
            item_checkobox = self.browser.find_element_by_id('id_item_done')
            item_checkobox.click()
        save_button = self.browser.find_element_by_css_selector('.save-button')
        save_button.click()

        item_added_name = self.browser.find_element_by_css_selector(f'#id_list_table tr:nth-child({item_no}) td:first-child text')
        self.assertEqual(item_added_name.text, item_name)
        item_added_checkobox = self.browser.find_element_by_id(f'item_{item_no}')
        if item_done:
            self.assertEqual(item_added_checkobox.get_attribute("checked"), "true")
        else:
            self.assertEqual(item_added_checkobox.get_attribute("checked"), None)

    def test_add_list(self):
        user_details = add_new_user()
        username = user_details[0]
        password = user_details[1]
        user = user_details[2]

        self.log_in(username, password)

        lists_link = self.browser.find_element_by_css_selector('a[href*=lists]')
        lists_link.click()

        add_list_button = self.browser.find_element_by_css_selector('.glyphicon-plus')
        add_list_button.click()

        self.add_list('New list test')
        self.add_item('Checked item', True, 1)
        self.add_item('Unchecked item', False, 2)

        delete_user(user)

    def test_add_list_for_place(self):
        user_details = add_new_user()
        username = user_details[0]
        password = user_details[1]
        user = user_details[2]

        place_id = add_new_place(user)

        self.log_in(username, password)
        self.browser.get(f'http://localhost:8000/{place_id}')
        edit_button = self.browser.find_element_by_css_selector('.glyphicon-pencil')
        edit_button.click()

        add_list_button = self.browser.find_element_by_css_selector("[href*='list/']")
        add_list_button.click()

        self.add_list('New list test')

        delete_user(user)

    def test_edit_list(self):
        user_details = add_new_user()
        username = user_details[0]
        password = user_details[1]
        user = user_details[2]

        new_list = add_new_list(user, 'New List')
        new_list_id = new_list.pk

        self.log_in(username, password)
        self.browser.get(f'http://localhost:8000/list/{new_list_id}')

        edit_list_button = self.browser.find_element_by_css_selector(".header .edit-button")
        edit_list_button.click()

        self.add_list('Very new list name')

        delete_user(user)

    def test_delete_list(self):
        user_details = add_new_user()
        username = user_details[0]
        password = user_details[1]
        user = user_details[2]

        new_list = add_new_list(user, 'New List')
        new_list_id = new_list.pk

        self.log_in(username, password)
        self.browser.get(f'http://localhost:8000/list/{new_list_id}')

        delete_list_button = self.browser.find_element_by_css_selector(".header .delete-button")
        delete_list_button.click()

        delete_confirmation_button = self.browser.find_element_by_css_selector('.save')
        delete_confirmation_button.click()

        lists_search_result = self.browser.find_element_by_css_selector('.list p')
        self.assertEqual(lists_search_result.text, 'No lists found')

        delete_user(user)

    def test_edit_item(self):
        user_details = add_new_user()
        username = user_details[0]
        password = user_details[1]
        user = user_details[2]

        new_list = add_new_list(user, 'New List')
        new_list_id = new_list.pk

        add_item_to_list(new_list, 'First item')
        add_item_to_list(new_list, 'Second item')

        self.log_in(username, password)
        self.browser.get(f'http://localhost:8000/list/{new_list_id}')

        first_item_edit_button = self.browser.find_element_by_css_selector('#id_list_table tr:first-child .glyphicon-pencil')
        first_item_edit_button.click()
        first_item_name_edit = self.browser.find_element_by_css_selector('#id_list_table tr:first-child #id_name')
        first_item_name_edit.clear()
        first_item_name_edit.send_keys('New name for first item')
        save_edit_button = self.browser.find_element_by_css_selector('[name=edit-button]')
        save_edit_button.click()
        new_first_item_name = self.browser.find_element_by_css_selector('#id_list_table tr:nth-child(2) text')
        self.assertEqual(new_first_item_name.text, 'New name for first item')

        second_item_edit_button = self.browser.find_element_by_css_selector('#id_list_table tr:first-child .glyphicon-pencil')
        second_item_edit_button.click()
        second_item_checkbox_edit = self.browser.find_element_by_css_selector('#id_list_table tr:first-child #id_item_done')
        second_item_checkbox_edit.click()
        save_edit_button = self.browser.find_element_by_css_selector('[name=edit-button]')
        save_edit_button.click()
        new_second_item_checkbox = self.browser.find_element_by_css_selector('#item_2')
        self.assertEqual(new_second_item_checkbox.get_attribute("checked"), "true")

        delete_user(user)

    def test_delete_item(self):
        user_details = add_new_user()
        username = user_details[0]
        password = user_details[1]
        user = user_details[2]

        new_list = add_new_list(user, 'New List')
        new_list_id = new_list.pk

        add_item_to_list(new_list, 'This will be deleted')
        add_item_to_list(new_list, 'This should stay')

        self.log_in(username, password)
        self.browser.get(f'http://localhost:8000/list/{new_list_id}')

        delete_item_button = self.browser.find_element_by_css_selector("#id_list_table tr:first-child .glyphicon-minus")
        delete_item_button.click()

        delete_confirmation_button = self.browser.find_element_by_css_selector('.save')
        delete_confirmation_button.click()

        first_item_name = self.browser.find_element_by_css_selector('#id_list_table tr:first-child text')
        self.assertEqual(first_item_name.text, 'This should stay')

        delete_user(user)




