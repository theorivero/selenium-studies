from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/keyboard'
browser = Firefox()
browser.get(url)
sleep(5)
browser.find_element_by_tag_name('html').send_keys('youtube')

sleep(5)
browser.close()
browser.quit()