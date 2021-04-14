from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/aula_09_a.html'
driver = Firefox()
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(30)


btn = driver.find_element_by_css_selector('button')
btn.click()


finished = driver.find_element_by_id('finished')
assert finished.text == "Carregamento concluído"


driver.find_element_by_css_selector('Fausto') 
"""
por conta do implicitly_wait(30) demora 30 segundos esperando a tag "Fausto  " 
aparecer antes de avisar
"""

sleep(20)
driver.close()
driver.quit()