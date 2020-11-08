from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://google.co.id')
search_box = browser.find_element_by_name('q')
search_box.send_keys('Fachrul Choliluddin' + Keys.ENTER)
assert 'Fachrul Choliluddin' in browser.title
browser.close()
