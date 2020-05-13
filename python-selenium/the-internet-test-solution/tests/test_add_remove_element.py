from selenium import webdriver
import random
import time

def test_adding(browser: webdriver.Remote):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    btn_add = browser.find_element_by_xpath('//button[text()="Add Element"]')
    
    # Check default state
    browser.implicitly_wait(0.3)      # before getting not found items, we should reduce implicit time to make selenium wait shorter
    btns_delete = browser.find_elements_by_css_selector('#elements button')
    assert len(btns_delete) == 0
    
    browser.implicitly_wait(5)     # restore it
    btn_add.click()
    btns_delete = browser.find_elements_by_css_selector('#elements button')
    assert len(btns_delete) > 0
    
def test_removing(browser: webdriver.Remote):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    btn_add = browser.find_element_by_xpath('//button[text()="Add Element"]')
    max_add = random.randint(2,15)
    print(f"will add button for {max_add} times ")
    for x in range(0, max_add):
         btn_add.click()
         time.sleep(0.1)    # make little bit visible ahaha :D believe me you wont see it, try to remark
    
    btns_delete = browser.find_elements_by_css_selector('#elements button')
    print('total btns_delete: ', len(btns_delete))
    print(btns_delete)
    
    for btn_delete in btns_delete:
        btn_delete.click()
        time.sleep(0.1)     # make little bit visible ahaha :D believe me you wont see it, try to remark
    
    # before getting not found items, we should reduce implicit time to make selenium wait shorter
    browser.implicitly_wait(1)
    btns_delete = browser.find_elements_by_css_selector('#elements button')
    assert len(btns_delete) == 0    