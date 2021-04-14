from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from time import sleep

url = 'https://selenium.dunossauro.live/caixinha'
browser = Firefox()
browser.get(url)
browser.maximize_window()



caixa = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')

ac = ActionChains(browser)
def clicks(key1, key2=None):
	ac.pause(1)
	ac.key_down(key1)
	if key2:
		ac.key_down(key2)
	ac.move_to_element(caixa)
	ac.pause(1)
	ac.click()
	ac.pause(1)
	ac.double_click()
	ac.pause(1)
	ac.move_to_element(span)
	ac.key_up(key1)
	if key2:
		ac.key_up(key2)

clicks(Keys.SHIFT)
clicks(Keys.CONTROL)
clicks(Keys.CONTROL,Keys.SHIFT)
ac.pause(1)


ac.context_click()
ac.perform()







sleep(10)
#browser.close()
#browser.quit()