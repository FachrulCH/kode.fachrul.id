from selenium import webdriver
from pages.form import Form


class TestForm():
    def test_submit_name(self, browser: webdriver.Remote):
        form_page = Form(browser)
        form_page.load()
        