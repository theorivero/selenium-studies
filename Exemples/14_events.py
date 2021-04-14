from selenium.webdriver import Firefox
from time import sleep
browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_07_d .html')
sleep(5)
_input = browser.find_element_by_tag_name('input')
span = browser.find_element_by_tag_name('span')
p = browser.find_element_by_tag_name('p')

_input.click()

assert 'está com foco' == span.text
span.click() # saindo do foco do input
assert 'está sem foco' == span.text


assert p.text == '0'
_input.send_keys('theozin')
assert 'está com foco' == span.text
span.click() # saindo do foco do input
assert 'está sem foco' == span.text
assert p.text == '1'

sleep(5)
browser.close()
browser.quit()
