from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.close()

class TestGoogling():
    def test_searching_name(self, browser: webdriver.Remote):
        browser.get('https://google.co.id')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('Fachrul Choliluddin' + Keys.ENTER)
        assert 'Fachrul Choliluddin' in browser.title