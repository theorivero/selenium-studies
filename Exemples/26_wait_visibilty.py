from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of, invisibility_of_element

from time import sleep


url = 'https://selenium.dunossauro.live/aula_10_b.html'

driver = Firefox()
driver_wait = WebDriverWait(driver, 60)

driver.get(url)
driver.maximize_window()

driver_wait.until(
	visibility_of(driver.find_element_by_tag_name('h1')),
	'H1 não foi encontrado, espera de 30 segundos'
	)
print('h1 disponivel')

driver_wait.until_not(
	invisibility_of_element(driver.find_element_by_tag_name('h1')),
	'H1 não foi encontrado, espera de 30 segundos'
	)
print('h1 disponivel')

sleep(20)
driver.close()
driver.quit()