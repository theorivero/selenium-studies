from selenium.webdriver import Firefox
from time import sleep


browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'

browser.get(url)
sleep(2)

def att_type():
	browser.find_element_by_css_selector('[type="text"]').send_keys('theo') #nome
	browser.find_element_by_css_selector('[type="password"]').send_keys('senha123') #senha
	browser.find_element_by_css_selector('[type="submit"]').click() #botao

def att_name():
	browser.find_element_by_css_selector('[name="nome"]').send_keys('theo')  #nome
	browser.find_element_by_css_selector('[name="senha"]').send_keys('senha123') #senha
	browser.find_element_by_css_selector('[name="l0c0"]').click() #botao

def att_valor():
	browser.find_element_by_css_selector('[name*="ome"]').send_keys('theo')  #nome
	browser.find_element_by_css_selector('[name*="nha"]').send_keys('senha123') #senha
	browser.find_element_by_css_selector('[name*="l0"]').click() #botao


att_valor()

sleep(10)
browser.close()
browser.quit()
