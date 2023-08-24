from .base import FunctionalTest
from .setup import add_new_user, add_new_place, delete_user, add_new_list, add_item_to_list
from selenium import webdriver
from django.contrib.auth.models import User
from time import sleep
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class AddEditListsTest(FunctionalTest):
#TODO write helpers function to make code clearer (i.e type function)

    def add_list(self, list_name: str):
        list_name_field = self.browser.find_element(By.ID, 'id_name')
        list_name_field.clear()
        list_name_field.send_keys(list_name)

        save_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-primary')
        save_button.click()

        list_name_header = self.browser.find_element(By.CSS_SELECTOR, '.header h2')
        self.assertEqual(list_name_header.text, list_name)

    def add_item(self, item_name: str, item_done: bool, item_no: int):
        item_name_field = self.browser.find_element(By.ID, 'id_name')
        item_name_field.send_keys(item_name)
        if item_done:
            item_checkobox = self.browser.find_element(By.ID, 'id_item_done')
            item_checkobox.click()
        save_button = self.browser.find_element(By.CSS_SELECTOR, '.save')
        save_button.click()

        item_added_name = self.browser.find_element(By.CSS_SELECTOR, f'label[for="item_{item_no}"]')
        self.assertEqual(item_added_name.text, item_name)
        item_added_checkobox = self.browser.find_element(By.ID, f'item_{item_no}')
        if item_done:
            self.assertEqual(item_added_checkobox.get_attribute("checked"), "true")
        else:
            self.assertEqual(item_added_checkobox.get_attribute("checked"), None)

    def test_add_list(self):
        self.log_in(self.username, self.password)

        menu_icon = self.browser.find_element(By.CSS_SELECTOR, '.btn-header')
        menu_icon.click()
        lists_link = self.browser.find_element(By.CSS_SELECTOR, 'a[href*=lists]')
        lists_link.click()

        add_list_button = self.browser.find_element(By.CSS_SELECTOR, '.bi-plus-lg')
        add_list_button.click()

        self.add_list('New list test')
        self.add_item('Checked item', True, 1)
        self.add_item('Unchecked item', False, 2)

    @unittest.skip("Functionality temporary removed")
    def test_add_list_for_place(self):
        place_id = add_new_place(self.user)

        self.log_in(self.username, self.password)
        self.browser.get(f'http://localhost:8000/{place_id}')
        edit_button = self.browser.find_element(By.CSS_SELECTOR, '.bi-pencil')
        edit_button.click()

        add_list_button = self.browser.find_element(By.CSS_SELECTOR, "[href*='list/']")
        add_list_button.click()

        self.add_list('New list test')

    def test_edit_list(self):
        new_list = add_new_list(self.user, 'New List')
        new_list_id = new_list.pk

        self.log_in(self.username, self.password)
        self.browser.get(f'http://localhost:8000/list/{new_list_id}')

        edit_list_button = self.browser.find_element(By.CSS_SELECTOR, ".header .bi-pencil")
        edit_list_button.click()

        self.add_list('Very new list name')

    def test_delete_list(self):
        new_list = add_new_list(self.user, 'New List')
        new_list_id = new_list.pk

        self.log_in(self.username, self.password)
        self.browser.get(f'http://localhost:8000/list/{new_list_id}')

        delete_list_button = self.browser.find_element(By.CSS_SELECTOR, ".header .delete-button")
        delete_list_button.click()

        delete_confirmation_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-primary')
        delete_confirmation_button.click()

        lists_search_result = self.browser.find_element(By.CSS_SELECTOR, '.details p')
        self.assertEqual(lists_search_result.text, 'No lists found')

    def test_edit_item(self):
        new_list = add_new_list(self.user, 'New List')
        new_list_id = new_list.pk

        add_item_to_list(new_list, 'First item')
        add_item_to_list(new_list, 'Second item')

        self.log_in(self.username, self.password)
        self.browser.get(f'http://localhost:8000/list/{new_list_id}')

        first_item_edit_button = self.browser.find_element(By.CSS_SELECTOR, '.list .row:first-child .bi-pencil')
        first_item_edit_button.click()
        first_item_name_edit = self.browser.find_element(By.CSS_SELECTOR, '.list .row:first-child #id_name')
        first_item_name_edit.clear()
        first_item_name_edit.send_keys('New name for first item')
        save_edit_button = self.browser.find_element(By.CSS_SELECTOR, '[name=edit-button]')
        save_edit_button.click()
        new_first_item_name = self.browser.find_element(By.CSS_SELECTOR, 'label[for="item_2"]')
        self.assertEqual(new_first_item_name.text, 'New name for first item')

        second_item_edit_button = self.browser.find_element(By.CSS_SELECTOR, '.list .row:first-child .bi-pencil')
        second_item_edit_button.click()
        second_item_checkbox_edit = self.browser.find_element(By.CSS_SELECTOR, '.list .row:first-child #id_item_done')
        second_item_checkbox_edit.click()
        save_edit_button = self.browser.find_element(By.CSS_SELECTOR, '[name=edit-button]')
        save_edit_button.click()
        new_second_item_checkbox = self.browser.find_element(By.CSS_SELECTOR, '#item_2')
        self.assertEqual(new_second_item_checkbox.get_attribute("checked"), "true")

    def test_delete_item(self):
        new_list = add_new_list(self.user, 'New List')
        new_list_id = new_list.pk

        add_item_to_list(new_list, 'This will be deleted')
        add_item_to_list(new_list, 'This should stay')

        self.log_in(self.username, self.password)
        self.browser.get(f'http://localhost:8000/list/{new_list_id}')

        delete_item_button = self.browser.find_element(By.CSS_SELECTOR, ".list .row:first-child .bi-trash")
        delete_item_button.click()

        delete_confirmation_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-primary')
        delete_confirmation_button.click()

        first_item_name = self.browser.find_element(By.CSS_SELECTOR, 'label[for="item_1"]')
        self.assertEqual(first_item_name.text, 'This should stay')



