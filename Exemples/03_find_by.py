from selenium.webdriver import Firefox
from time import sleep

def find_by_text(browser, text, tag):
	""" Encoontrar o elemento com o texto 'text' 
	
	Args:
		- browser: Intancia do browser [Firefox, google]
		- texto: conteudo que deve estar na tag
		- tag: tag onde o texto será procurado
	"""
	elements = browser.find_elements_by_tag_name(tag)

	for element in elements:
		if element.text == text:
			return element

	return None

def find_by_href(browser, link):

	elements = browser.find_elements_by_tag_name('a')

	for element in elements:
		element_link = element.get_attribute('href')
		if link in element_link:
			return element

	return None


url = 'http://selenium.dunossauro.live/aula_04_a.html'

browser = Firefox()
browser.get(url)

#ddg_element = find_by_text(browser, "DuckDuckGo", "a")
ddg_element = find_by_href(browser, "ddg")

print(ddg_element.text)

