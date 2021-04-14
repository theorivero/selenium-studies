from selenium.webdriver import Firefox
from time import sleep

def fill_form(browser, form_class):
	form = browser.find_element_by_css_selector(f'form.{form_class}')
	form.find_element_by_css_selector('input[name="nome"]').send_keys('theo')
	form.find_element_by_css_selector('input[name="senha"]').send_keys('senha')
	form.find_element_by_css_selector('input[type="submit"]').click()

def get_form_class(browser):
	form_class_loc = browser.find_element_by_css_selector('body div header p span').text
	form_class = f"form-{form_class_loc}"
	print(form_class)
	return form_class


browser = Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_05.html')

for i in range(4):
	sleep(5)
	form_class = get_form_class(browser)
	fill_form(browser, form_class)


sleep(10)
browser.close()
browser.quit()





