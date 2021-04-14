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
driver_wait = WebDriverWait(driver, 10, poll_frequency=0.5)
driver.get('https://selenium.dunossauro.live/exercicio_10.html')
driver.maximize_window()

# preencher formulario
driver.find_element_by_css_selector('input#todo-name').send_keys('Lavar o carro')
driver.find_element_by_css_selector('textarea#todo-desc').send_keys('Usando agua e sabão e fechando a tonerira para n gastar agua')
driver.find_element_by_css_selector('button#todo-submit').click()

# moving Todo to doing
locator = (By.CSS_SELECTOR, 'div.body_a fieldset div div')
driver_wait.until(
	SearchElement(locator),
	'Não achou a div'
	)
driver.find_element_by_css_selector('button.btn.btn-primary.btn-ghost.do').click()

#moving doing to done
locator = (By.CSS_SELECTOR, 'div.body_b fieldset div div')
driver_wait.until(
	SearchElement(locator),
	'Não achou a div'
	)
driver.find_element_by_css_selector('button.btn.btn-primary.btn-ghost.do').click()

# redo
locator = (By.CSS_SELECTOR, 'div.body_c fieldset div div')
driver_wait.until(
	SearchElement(locator),
	'Não achou a div'
	)
driver.find_element_by_css_selector('button.btn.btn-primary.btn-ghost.do').click()

# moving Todo to doing
locator = (By.CSS_SELECTOR, 'div.body_a fieldset div div')
driver_wait.until(
	SearchElement(locator),
	'Não achou a div'
	)
driver.find_element_by_css_selector('button.btn.btn-primary.btn-ghost.do').click()

#moving doing to todo
locator = (By.CSS_SELECTOR, 'div.body_b fieldset div div')
driver_wait.until(
	SearchElement(locator),
	'Não achou a div'
	)
driver.find_element_by_css_selector('button.btn.btn-error.btn-ghost.cancel').click()


sleep(10)
driver.close()
driver.quit()

