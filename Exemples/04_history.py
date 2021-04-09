from selenium.webdriver import Firefox
from time import sleep

def find_by_text(browser, text, tag):
	
	elements = browser.find_elements_by_tag_name(tag)

	for element in elements:
		if element.text == text:
			return element

	return None

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_b.html')

divs = browser.find_elements_by_tag_name('div')

boxs_texts = ['um', 'dois', 'tres', 'quatro']

for i in range(10):
	for text in boxs_texts:
		find_by_text(browser, text, 'div').click()
		sleep(0.5)

	for nome in boxs_texts:
		browser.back()
		sleep(0.5)

	for nome in boxs_texts:
		browser.forward()
		sleep(0.5)


