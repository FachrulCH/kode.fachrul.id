import time
from selenium import webdriver

def test_default_state(browser: webdriver.Remote):
    browser.get('https://the-internet.herokuapp.com/checkboxes')
    
    first_checkbox = browser.find_element_by_xpath('//input[1]')
    second_checkbox = browser.find_element_by_xpath('//input[2]')
    assert not first_checkbox.is_selected()
    assert second_checkbox.is_selected()

def test_state_after_checked(browser: webdriver.Remote):
    browser.get('https://the-internet.herokuapp.com/checkboxes')
    
    first_checkbox = browser.find_element_by_xpath('//input[@type="checkbox"][1]')
    second_checkbox = browser.find_element_by_xpath('//input[@type="checkbox"][2]')
    first_checkbox.click()
    second_checkbox.click()
    assert first_checkbox.is_selected()
    assert not second_checkbox.is_selected()
    