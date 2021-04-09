"""-Pegar todos os links de aulas"""
	
from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep
from pprint import pprint


links = {}

browser = Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_03.html')
sleep(2)

#página 1
btn = browser.find_elements_by_tag_name('a')[-1]
btn.click()

sleep(2)
p = browser.find_elements_by_tag_name('p')[-1].text
res = int(p[0]) * int(p[4])

lis = browser.find_elements_by_tag_name('li')[-2:]

i = 0
while int(lis[i].text) == res:
	print(lis[i].text)
	i +=1

a = lis[i].find_element_by_tag_name('a')
a.click()

#pagina 2
print('começou')
sleep(60)
print('acabou')

title = browser.title
lis = browser.find_elements_by_tag_name('li')[-2:]

i = 0
while lis[i].text != title:
	i +=1

a = lis[i].find_element_by_tag_name('a')
a.click()

#pagina 3
sleep(5)

url_end = urlparse(browser.current_url).path

lis = browser.find_elements_by_tag_name('li')[-2:]

i = 0
while lis[i].text not in url_end:
	i +=1

a = lis[i].find_element_by_tag_name('a')
a.click()

#
sleep(5)
browser.refresh()

#browser.close()
#browser.quit()
