from selenium.webdriver.support.ui import WebDriverWait

web_driver_wait = WebDriverWait(
	driver, # WebDriver
	timeout, # Tempo de espera até o erro
	poll_frequency=0.5, # Tempo emtre uma tentativa e outra
	ignored_exceptions=None # Lista de coisas que vamos ignorar

	)

#chamando 

wdw = WebDriverWait(driver, 10)

wdw.until(
	Callable, # Operação que vai ser executada
	mensage # mensagem caso o erro ocorra
	)