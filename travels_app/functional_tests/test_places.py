from .base import FunctionalTest
from selenium import webdriver
from django.contrib.auth.models import User
from time import sleep
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from .setup import add_new_place, add_new_tag
from my_travels.models import Places, Tag

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

    def test_delete_place(self):
        place_id = add_new_place(self.user)

        self.log_in(self.username, self.password)

        self.browser.get(f'http://localhost:8000/{place_id}/')

        edit_button = self.browser.find_element_by_css_selector('.glyphicon-pencil')
        edit_button.click()

        delete_button = self.browser.find_element_by_css_selector('.glyphicon-minus')
        delete_button.click()

        delete_confirmation_button = self.browser.find_element_by_css_selector('.save')
        delete_confirmation_button.click()

        self.browser.find_element_by_id('map')
        sleep(5)

        pins = self.browser.find_elements_by_css_selector('#map .leaflet-marker-pane img:first-child')

        if len(pins) > 0:
            raise Exception('Place not deleted')

    def test_add_tag(self):
        place_id = add_new_place(self.user)

        self.log_in(self.username, self.password)

        self.browser.get(f'http://localhost:8000/{place_id}/')

        edit_button = self.browser.find_element_by_css_selector('.glyphicon-pencil')
        edit_button.click()

        add_tag_button = self.browser.find_element_by_css_selector('.glyphicon-plus')
        add_tag_button.click()

        tag_name = ''.join(random.choices(string.ascii_uppercase, k=10))
        tag = self.browser.find_element_by_id('id_tag')
        tag.send_keys(tag_name)

        save_tag_button = self.browser.find_element_by_css_selector('.glyphicon-ok')
        save_tag_button.click()

        tags_list_values = self.browser.find_elements_by_css_selector('#id_tag option')
        all_tags_names = [tag.text for tag in tags_list_values]
        if tag_name not in all_tags_names:
            raise Exception('New tag to available on the list')

    def test_search_place_by_name(self):
        search_place_id = add_new_place(self.user, "Search test")
        other_place_id = add_new_place(self.user)

        self.log_in(self.username, self.password)

        self.browser.get(f'http://localhost:8000/places')

        search_field = self.browser.find_element_by_css_selector('[type=search]')
        search_field.send_keys('Search', Keys.ENTER)

        search_results = self.browser.find_elements_by_css_selector('#id_places_table tr td:first-child')
        self.assertEqual(len(search_results), 1)

        search_result_name = self.browser.find_element_by_css_selector('#id_places_table tr:nth-child(2) td:first-child')
        self.assertEqual(search_result_name.text, 'Search test')

    def test_search_place_by_tag(self):
        tag_name = ''.join(random.choices(string.ascii_uppercase, k=10))
        tag = add_new_tag(self.user, tag_name)
        search_place_id = add_new_place(self.user, "Search test")
        search_place = Places.objects.get(pk=search_place_id)
        search_place.tag.set([tag])
        search_place.save()
        other_place_id = add_new_place(self.user)

        self.log_in(self.username, self.password)

        self.browser.get(f'http://localhost:8000/places')

        search_field = self.browser.find_element_by_css_selector('[type=search]')
        search_field.send_keys(tag_name, Keys.ENTER)

        search_results = self.browser.find_elements_by_css_selector('#id_places_table tr td:first-child')
        self.assertEqual(len(search_results), 1)

        search_result_name = self.browser.find_element_by_css_selector('#id_places_table tr:nth-child(2) td:first-child')
        self.assertEqual(search_result_name.text, 'Search test')

    def test_list_places_for_tag(self):
        tag_name = ''.join(random.choices(string.ascii_uppercase, k=10))
        tag = add_new_tag(self.user, tag_name)

        first_place_name = "First Place"
        first_place_id = add_new_place(self.user, first_place_name)
        first_place = Places.objects.get(pk=first_place_id)
        first_place.tag.set([tag])
        first_place.save()

        second_place_name = "Second Place"
        second_place_id = add_new_place(self.user, second_place_name)
        second_place = Places.objects.get(pk=second_place_id)
        second_place.tag.set([tag])
        second_place.save()

        no_tag_place_name = "No Tag"
        no_tag_place_id = add_new_place(self.user, no_tag_place_name)

        self.log_in(self.username, self.password)

        self.browser.get(f'http://localhost:8000/{first_place_id}/')

        tag_link = self.browser.find_element_by_css_selector('#id_tags_list a:first-child')
        tag_link.click()

        search_results = self.browser.find_elements_by_css_selector('#id_places_table tr td:first-child')
        self.assertEqual(len(search_results), 2)

        first_search_result_name = self.browser.find_element_by_css_selector('#id_places_table tr:nth-child(2) td:first-child')
        self.assertEqual(first_search_result_name.text, first_place_name)

        second_search_result_name = self.browser.find_element_by_css_selector('#id_places_table tr:nth-child(3) td:first-child')
        self.assertEqual(second_search_result_name.text, second_place_name)

        returned_places_names = [place_name.text for place_name in search_results]
        if no_tag_place_name in returned_places_names:
            raise Exception('Place without tag returned.')

    