from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from time import sleep


url = 'https://selenium.dunossauro.live/aula_10_a.html'

driver = Firefox()
driver_wait = WebDriverWait(driver, 30)

driver.get(url)
driver.maximize_window()

locator = (By.CSS_SELECTOR, '#request')

driver_wait.until(
	presence_of_element_located(locator)
	)

driver.find_element(*locator).click()
sleep(10)
driver.close()
driver.quit()