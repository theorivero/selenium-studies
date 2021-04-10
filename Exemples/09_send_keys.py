from selenium.webdriver import Firefox
from time import sleep

def send_keys_by_name(browser, name, keys):
	web_element = browser.find_element_by_name(name)
	web_element.send_keys(keys)

def click_button_by_name(browser, name):
	button = browser.find_element_by_name(name).click()


firefox = Firefox()
firefox.get('http://selenium.dunossauro.live/aula_05_c.html')
sleep(10)


send_keys_by_name(firefox, 'filme', 'A festa da salsicha')
send_keys_by_name(firefox, 'email', 'theo@gmail.com')
send_keys_by_name(firefox, 'telefone', '(048)991020756')


click_button_by_name(firefox, 'enviar')

sleep(20)
firefox.close()
firefox.quit()