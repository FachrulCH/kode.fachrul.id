import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # _browser = webdriver.Chrome(options=chrome_options)
    _browser = webdriver.Chrome()
    _browser.implicitly_wait(10)
    _browser.get('https://the-internet.herokuapp.com/')
    yield _browser
    _browser.quit()