from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from time import sleep

class SearchElement:
	def __init__(self, locator):
		self.locator = locator

	def __call__(self, webdriver):
		print(f'Searching for {self.locator}')
		if webdriver.find_elements(*self.locator):
			return True
		return False

driver = Firefox()
driver_wait = WebDriverWait(driver, 20, poll_frequency=0.2)
driver.get('https://selenium.dunossauro.live/exercicio_09.html')
driver.maximize_window()

#Searching Botton
locator = (By.CSS_SELECTOR, 'button')
driver_wait.until(SearchElement(locator), 'Não achou o botão')

locator = (By.CSS_SELECTOR, '.selenium')
driver_wait.until(SearchElement(locator), 'Não achou o .selenium')
btn = driver.find_element_by_css_selector('.selenium')
print(btn.__class__)

sleep(10)
driver.close()
driver.quit()
