from selenium import webdriver
from pages.form import Form
import time
from pages.thanks import Thanks


class TestForm():
    def test_submit_name(self, browser: webdriver.Remote):
        form_page = Form(browser)
        form_page.load()
        form_page.input_name('Fachrul', 'Choliluddin')
        form_page.choose_education('Grad School')
        form_page.choose_gender('Female')
        form_page.choose_experience('2-4')
        time.sleep(3)
        # form_page.submit_form()

        # thanks_page = Thanks(browser)
        # assert thanks_page.title == 'Thanks for submitting your form'
        # assert thanks_page.message == 'The form was successfully submitted!'