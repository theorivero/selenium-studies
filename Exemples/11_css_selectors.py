def Basicss():
	id = browser.find_element_by_css_selector('#python')
	tag = browser.find_element_by_css_selector('div')
	tags = browser.find_elements_by_css_selector('div')
	_class = browser.find_element_by_css_selector('.form-group')
	tag_class = browser.find_elements_by_css_selector('div.form-group')
	atributo = browser.find_elements_by_css_selector('[atributo]') # pega todos os web elements que tem o atributo "atributo"
	atributo_operador_valor = browser.find_elements_by_css_selector('[class="form-group"]') # pega todos os web elements que tem o atributo "class" exatamente igual a "form-group"
	atributo_operador_valor = browser.find_elements_by_css_selector('[class*="group"]') # pega todos os WE que tem o "group" contido no atributo "class"
	universal = browser.find_elements_by_css_selector('*')
	combine = browser.find_elements_by_css_selector('input[type="text"]')