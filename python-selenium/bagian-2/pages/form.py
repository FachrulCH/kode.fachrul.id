from selenium import webdriver
from selenium.webdriver.common.by import By

class Form():
    URL = 'https://formy-project.herokuapp.com/form'
    #locators
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    SUBMIT = (By.LINK_TEXT, 'Submit')

    def __init__(self, browser: webdriver.Remote):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def input_name(self, first_name, last_name):
        self.browser.find_elements(*self.FIRST_NAME).send_keys(first_name)
        self.browser.find_elements(*self.LAST_NAME).send_keys(last_name)

    def submit_form(self):
        self.browser.find_element(*self.SUBMIT).click()