from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that

class Thanks():
    TITLE = (By.TAG_NAME, 'h1')
    MESSAGE = (By.CSS_SELECTOR, '.alert')

    def __init__(self, browser: webdriver.Remote):
        self.browser = browser

    @property
    def title(self):
        return self.browser.find_element(*self.TITLE).text
    
    @property
    def message(self):
        return str(self.browser.find_element(*self.MESSAGE).text).strip()

    def verify_alert_is_green(self):
        el_class = self.browser.find_element(*self.MESSAGE).get_attribute('class')
        # assert 'success' in el_class
        assert_that(el_class).contains('successs')