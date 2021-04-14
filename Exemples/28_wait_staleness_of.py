from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

from time import sleep


url = 'https://selenium.dunossauro.live/aula_10_b.html'

driver = Firefox()
driver_wait = WebDriverWait(driver, 60)

driver.get(url)
driver.maximize_window()


driver_wait.until(
	staleness_of(driver.find_element_by_tag_name('button ')),
	'button não está disponivel, espera de 30 segundos'
	)

driver.find_element_by_tag_name('button ').click()


sleep(20)
driver.close()
driver.quit()