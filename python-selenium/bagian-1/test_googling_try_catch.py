from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()                                    # 1. Buka Browser
browser.get('https://google.co.id')                             # 2. Menuju halaman
                                                                # 3. Pastikan browser berada pada “state” yang tepat
try:
                                                                # 4. Menemukan element yang diperlukan untuk interaksi
    search_box = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys('Fachrul Choliluddin' + Keys.ENTER)   # 5. Menjalankan suatu aksi pada element tersebut
    assert 'Fachrul Choliluddin' in browser.title              # 6. Melakukan pengujian dengan assertion
finally:
    browser.quit()                                       # 7. Menutup browser