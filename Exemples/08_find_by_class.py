from selenium.webdriver import Firefox
from time import sleep

firefox = Firefox()
firefox.get('http://selenium.dunossauro.live/aula_05_b.html')


topico = firefox.find_element_by_class_name('topico')
lng_divs = firefox.find_elements_by_class_name('linguagens')

for lng_div in lng_divs:
	print((
		lng_div.find_element_by_tag_name('h2').text,
		lng_div.find_element_by_tag_name('p').text))

sleep(5)
firefox.close()
firefox.quit()