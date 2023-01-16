from .base import FunctionalTest
from selenium import webdriver

class LoginLogoutTest(FunctionalTest):

    def test_login_logout(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        log_in = self.browser.find_element_by_css_selector('.top-menu a[href*=login]')
        log_in.click()
        # TODO add new user as setup
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('TestUser')
        username = self.browser.find_element_by_id('id_password')
        username.send_keys('T3stP4ss23')
        login_button = self.browser.find_element_by_css_selector('input[value=login]')
        login_button.click()

        self.browser.find_element_by_id('map')

        log_out = self.browser.find_element_by_css_selector('.top-menu a[href*=logout]')
        log_out.click()

        self.browser.find_element_by_css_selector('h2 [href*=login]')

    