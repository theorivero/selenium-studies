from selenium.webdriver import Firefox
from time import sleep


url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Firefox()

browser.get(url)
sleep(2)

ps = browser.find_elements_by_tag_name('p')
a = browser.find_element_by_tag_name('a')

expected_num = int(ps[1].text[-1])
num = None

while expected_num != num:
	a.click()
	ps = browser.find_elements_by_tag_name('p')
	num = int(ps[-1].text[-1])


	



