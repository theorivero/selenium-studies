from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')

url_parsed = urlparse(browser.current_url)

print(url_parsed)

sleep(4)
browser.close()
browser.quit()