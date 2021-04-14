from selenium.webdriver.support.expected_conditions import ...

w.until(
	element_to_be_clickable(element),
	'Elemento não é clicavel'
	)


url = driver.current_url
wdw.until(
	url_changes(url)
	)

wdw.until(
	url_contais(url)
	)

wdw.until(
	title_is('home page')
	)

wdw.until(
	title_contais('home')
	)