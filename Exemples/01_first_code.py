from selenium.webdriver import Firefox
from time import sleep

url='https://curso-python-selenium.netlify.app/aula_03.html'

browser = Firefox()
browser.get(url)
sleep(3)
a = browser.find_element_by_tag_name('a')
p = browser.find_element_by_tag_name('p')

for i in range(10):
	ps = browser.find_elements_by_tag_name('p')
	a.click()
	print(f'Valor de p: {ps[-1].text}, click: {i}')

print(f'a value: {a.text}')
print(f'p value: {ps[-1].text}')

browser.quit()