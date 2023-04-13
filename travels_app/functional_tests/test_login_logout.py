from .base import FunctionalTest
from selenium import webdriver

class LoginLogoutTest(FunctionalTest):

    def test_login_logout(self):
        self.log_in(self.username, self.password)

        log_out = self.browser.find_element_by_css_selector('a[href*=logout]')
        log_out.click()

        self.browser.find_element_by_css_selector('h2 [href*=login]')

    