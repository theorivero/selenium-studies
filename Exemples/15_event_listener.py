from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from time import sleep

class Escuta(AbstractEventListener):
	def before_click(self, elemento, webdriver):
		if elemento.tag_name == 'input':	
			print(wraper.find_element_by_tag_name('span').text)
		print(f'antes do click {elemento.tag_name}')

	def after_click(self, elemento, webdriver):
		print('depois do click')
		print(wraper.find_element_by_tag_name('span').text)


browser = Firefox()
wraper = EventFiringWebDriver(browser, Escuta())
wraper.get('http://selenium.dunossauro.live/aula_07_d .html')



sleep(5)


_input = wraper.find_element_by_tag_name('input')
span = wraper.find_element_by_tag_name('span')
p = wraper.find_element_by_tag_name('p')

_input.click()



sleep(5)
wraper.close()
wraper.quit()
