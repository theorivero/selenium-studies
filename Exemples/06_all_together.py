from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep
from pprint import pprint


links = {}

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04.html')
sleep(2)


def get_links(browser, _element):
	links = {}

	element = browser.find_element_by_tag_name(_element)
	element_anchors = element.find_elements_by_tag_name('a')

	for anchor in element_anchors:
		links[anchor.text] = anchor.get_attribute('href')


	return links

main_links = get_links(browser, 'main')
pprint(main_links)
browser.get(main_links['Exercício 3'])
sleep(5)
browser.close()
browser.quit()
