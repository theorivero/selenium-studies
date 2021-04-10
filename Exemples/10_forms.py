from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse

def send_keys_by_name(browser, name, keys):
	web_element = browser.find_element_by_name(name)
	web_element.send_keys(keys)

def click_btn_by_name(browser, name):
	btn = browser.find_element_by_name(name).click()

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_05.html')
sleep(2)

send_keys_by_name(browser, 'nome', 'theo')
send_keys_by_name(browser, 'email', 'th@gmail.com')
send_keys_by_name(browser, 'senha', 'senha123')
send_keys_by_name(browser, 'telefone', '888888888')
click_btn_by_name(browser, 'btn')

sleep(20)
firefox.close()
firefox.quit()
