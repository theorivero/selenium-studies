from functools import partial
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

def esperar_elemento(by, elemento, webdriver):
	elements = webdriver.find_elements(by, elemento)
	print(f'Tentando localizar pelo css o seletor "{elemento}"')
	return bool(elements)

url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()
wdw = WebDriverWait(driver, 10)
driver.get(url)
#driver.maximize_window()

esperar_botao = partial(esperar_elemento, By.CSS_SELECTOR,'button')
wdw.until(esperar_botao,'deu ruim')
driver.find_element_by_tag_name('button').click()

wdw.until(
	partial(esperar_elemento, By.ID,'finished'),
	'A msg de sucesso n apareceu')
print(driver.find_element_by_tag_name('#finished').text)

sleep(20)
driver.close()
driver.quit()