from selenium import webdriver
from django.test import TestCase
import unittest

MAX_WAIT = 10

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def tearDown(self):
        self.browser.quit()
