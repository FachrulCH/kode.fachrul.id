from selenium import webdriver
from selenium.webdriver.common.by import By

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