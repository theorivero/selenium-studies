from functools import partial
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

class EsperarElemento:
	def __init__(self, locator):
		self.locator = locator

	def __call__(self, webdriver):
		print('procurando')
		if webdriver.find_elements(*self.locator):
			return True
		return False

url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()
wdw = WebDriverWait(driver, 10)
driver.get(url)
#driver.maximize_window()
locator = (By.CSS_SELECTOR,'button')
esperar_botao = EsperarElemento(locator)

wdw.until(esperar_botao,'deu ruim')
wdw.until(EsperarElemento((By.CSS_SELECTOR,'button')),'deu ruim') # mesma coisa que a parte de cima
driver.find_element_by_tag_name('button').click()

wdw.until(
	EsperarElemento((By.ID,'finished')),
	'A msg de sucesso n apareceu')
print(driver.find_element_by_tag_name('#finished').text)

sleep(20)
driver.close()
driver.quit()