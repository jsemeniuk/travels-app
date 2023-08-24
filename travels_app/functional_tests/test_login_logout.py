from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginLogoutTest(FunctionalTest):

    def test_login_logout(self):
        self.log_in(self.username, self.password)

        menu_icon = self.browser.find_element(By.CSS_SELECTOR, '.btn-header')
        menu_icon.click()
        log_out = self.browser.find_element(By.CSS_SELECTOR, 'a[href*=logout]')
        log_out.click()

        self.browser.find_element(By.ID, 'id_username')

    