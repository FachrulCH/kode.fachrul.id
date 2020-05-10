from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Form():
    URL = 'https://formy-project.herokuapp.com/form'
    #locators
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    SUBMIT = (By.LINK_TEXT, 'Submit')
    JOB_TITLE = (By.ID, 'job-title')
    EDUCATION = (By.ID, 'radio-button-{}')
    GENDER = (By.ID, 'checkbox-{}')
    EXPERIENCE = (By.ID, 'select-menu')


    def __init__(self, browser: webdriver.Remote):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def input_name(self, first_name, last_name):
        self.browser.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.browser.find_element(*self.LAST_NAME).send_keys(last_name)

    def submit_form(self):
        self.browser.find_element(*self.SUBMIT).click()
        time.sleep(3)

    def input_job_title(self, job_title):
        self.browser.find_element(*self.JOB_TITLE).send_keys(job_title)

    def choose_education(self, education_level: str):
        level = {'high school': 1, 'college': 2, 'grad school': 3}
        edu_level = level.get(education_level.lower(), 1)
        locator = list(self.EDUCATION)
        locator[1] = locator[1].format(edu_level)
        self.browser.find_element(*locator).click()

    def choose_gender(self, user_gender: str):
        gender_option = {'male': 1, 'female': 2}
        gender = gender_option.get(user_gender.lower(), 3)
        _by, _val = self.GENDER
        _val = _val.format(gender)
        self.browser.find_element(_by, _val).click()

    def choose_experience(self, user_experience: str):
        print('user experience: ', user_experience)
        select = Select(self.browser.find_element(*self.EXPERIENCE))
        select.select_by_visible_text(user_experience)
