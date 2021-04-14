from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from time import sleep

class SearchElement:
	def __init__(self, locator):
		self.locator = locator

	def __call__(self, webdriver):
		print(f'searching {self.locator}')
		if webdriver.find_elements(*self.locator):
			return True
		else:
			return False


class EsperarElementoAtivo:
	def __init__(self, locator):
		self.locator = locator

	def __call__(self, webdriver):
		print(f'espernado {self.locator} ficar ativo')
		elementos = webdriver.find_elements(*self.locator)
		if elementos:
			return 'unclick' in elementos[0].get_attribute('class')
		else:
			return False


url = 'https://selenium.dunossauro.live/aula_09.html'

driver = Firefox()
driver_wait = WebDriverWait(driver, 10)
driver.get(url)

# first wait
locator = (By.CSS_SELECTOR, 'html')
driver_wait.until(
	SearchElement(locator),
	'Não carregou a página'
	)
print('carregou a página')

#waint to warning go away
locator = (By.CSS_SELECTOR, 'button')
driver_wait.until_not(
	EsperarElementoAtivo(locator),
	'não ficou aitvo'
	)
driver.find_element_by_tag_name('button').click()

sleep(10)
driver.close()
driver.quit()