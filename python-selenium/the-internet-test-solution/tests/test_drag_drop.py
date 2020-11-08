import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def test_drag_a_to_b(browser: webdriver.Remote):
    browser.get('https://the-internet.herokuapp.com/drag_and_drop')
    browser.find_element_by_link_text('Drag and Drop').click()
    box_a = browser.find_element_by_id('column-a')
    box_b = browser.find_element_by_id('column-b')
    
    text_inside = box_a.find_element_by_tag_name('header').text
    print('text_inside: ', text_inside)
    assert text_inside == 'A'
    
    action = ActionChains(browser)
    action.drag_and_drop(box_a, box_b).perform()
    # text_inside = box_a.find_element_by_tag_name('header').text
    # print('after draging text_inside: ', text_inside)
    # assert text_inside == 'B'
    