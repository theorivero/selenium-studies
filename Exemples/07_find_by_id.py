from selenium.webdriver import Firefox
from time import sleep

firefox = Firefox()
firefox.get('http://selenium.dunossauro.live/aula_05_a.html')


div_1 = firefox.find_element_by_id('python')
div_hk = firefox.find_element_by_id('haskell')

print(div_hk.text)


sleep(5)
firefox.close()
firefox.quit()