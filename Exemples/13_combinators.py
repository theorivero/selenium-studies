from selenium.webdriver import Firefox
from time import sleep


browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'

browser.get(url)

browser.find_elements_by_css_selector('div.form-group')

browser.find_elements_by_css_selector('div.form-group + br' #br irmão de div com class form-group
	)[1].get_attribute('id')

# da tag div com a classe form-group pegue o filho com id "dentro-nome"
b.find_element_by_css_selector('div.form-group > #dentro-nome')

sleep(10)
browser.close()
browser.quit()
