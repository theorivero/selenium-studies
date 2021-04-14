"""
TODO:
	fazer a função get_colors ser realmente uma list de dicionarios
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import ast
from time import sleep

url = 'https://selenium.dunossauro.live/caixinha'
browser = Firefox()
browser.get(url)
browser.maximize_window()

box = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')

ac = ActionChains(browser)

def get_colors(browser):
	text = browser.find_element_by_tag_name('textarea').text
	text = text.replace('}', '};')
	text = text.replace('evento', '"event"')
	text = text.replace('cor', '"color"')
	text = text.replace('shift', '"shift"')
	text = text.replace('ctrl', '"ctrl"')
	text = "["+ text + "]"
	texts_list = text.split(";")

	for _text in texts_list:
		dicionario = dict(_text)
		print(dicionario)

def clicks(key1=None, key2=None):
	ac.pause(1)
	if key1:
		ac.key_down(key1)
	if key2:
		ac.key_down(key2)
	ac.move_to_element(box)
	ac.pause(1)
	ac.double_click()
	ac.move_to_element(span)
	if key1:
		ac.key_up(key1)
	if key2:
		ac.key_up(key2)

clicks()
clicks(Keys.SHIFT) # tudo certo
clicks(Keys.CONTROL) # não consigo pegar o dbclick
clicks(Keys.CONTROL, Keys.SHIFT)
ac.perform()



sleep(3)
get_colors(browser)


sleep(20)
browser.close()
browser.quit()