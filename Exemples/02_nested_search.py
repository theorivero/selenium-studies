from selenium.webdriver import Firefox
from time import sleep

url = 'http://selenium.dunossauro.live/aula_04_a.html'

browser = Firefox()
browser.get(url)

lista_n_ordenada = browser.find_element_by_tag_name('ul') #1

lis = lista_n_ordenada.find_elements_by_tag_name('li') #2

duck = lis[0].find_element_by_tag_name('a').text #3

print(duck)

browser.quit()

"""
	1. We seek 'ul' (only the first one)  # unordered list
	2. We seek all 'li' # list item
	3. In the first 'li', we seek for the text of 'a' #anchor

"""