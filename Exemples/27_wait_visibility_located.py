from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, invisibility_of_element_located

from time import sleep


url = 'https://selenium.dunossauro.live/aula_10_b.html'

driver = Firefox()
driver_wait = WebDriverWait(driver, 60)

driver.get(url)
driver.maximize_window()


locator = (By.TAG_NAME, 'h1')
driver_wait.until(
	visibility_of(driver.find_element_by(locator)),
	'H1 não foi encontrado, espera de 30 segundos'
	)
print('h1 disponivel')

locator = (By.TAG_NAME, 'h1')
driver_wait.until_not(
	invisibility_of_element(driver.find_element_by(locator)),
	'H1 não foi encontrado, espera de 30 segundos'
	)
print('h1 disponivel')

sleep(20)
driver.close()
driver.quit()