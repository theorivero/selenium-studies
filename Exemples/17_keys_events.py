from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from time import sleep

url = 'https://selenium.dunossauro.live/aula_08_a'
browser = Firefox()
browser.get(url)
sleep(5)

texto = 'Selenium'

# hi-level
element = browser.find_element_by_name('texto')#.send_keys(texto)

# low-level
ac = ActionChains(browser)
ac.move_to_element(element)
ac.click(element)

def digita_com(key):
	ac.key_down(key)

	for letra in texto:
		ac.key_down(letra)
		ac.key_up(letra)

	ac.key_up(key)

digita_com(Keys.SHIFT)



sleep(5)
browser.close()
browser.quit()