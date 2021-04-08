from selenium.webdriver import Firefox
from time import sleep

res = {'h1' : {}}

browser = Firefox()
browser.get('https://curso-python-selenium.netlify.app/exercicio_01.html')
sleep(2)
ps = browser.find_elements_by_tag_name('p')

for p in ps:
	attribute = p.get_attribute("atributo")

	res['h1'][attribute] = p.text


sleep(5)
browser.quit()
print(res)
