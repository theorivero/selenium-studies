from functools import partial
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver import Firefox

def esperar_elemento(elemento, webdriver):
	elements = webdriver.find_element_by_css_selector(elemento)
	print(f'Tentando localizar pelo css o seletor "{elemento}"')
	return bool(elements)

url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()
wdw = WebDriverWait(driver, 10)
driver.get(url)
#driver.maximize_window()

esperar_botao = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')
wdw.until(esperar_botao,'deu ruim')
driver.find_element_by_tag_name('button').click()

wdw.until(esperar_sucesso,'A msg de sucesso n apareceu')
print(driver.find_element_by_tag_name('#finished').text)

sleep(20)
driver.close()
driver.quit()