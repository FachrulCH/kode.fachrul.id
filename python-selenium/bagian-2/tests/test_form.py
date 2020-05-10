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
        form_page.input_date('05/09/2020')
        form_page.submit()

        thanks_page = Thanks(browser)
        thanks_page.verify_alert_is_green()
        assert thanks_page.title == 'Thanks for submitting your form'
        assert thanks_page.message == 'The form was successfully submitted!'