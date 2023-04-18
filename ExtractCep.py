from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
import pyautogui as timeResponse

# get browser that will use.
browser = seleniumOptions.Chrome()

# open url to get the data
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

# wait computer response.
timeResponse.sleep(2)

# find element name to write CPF.
browser.find_element(By.NAME, 'endereco').send_keys('05527150')

# wait computer response.
timeResponse.sleep(2)

# press button "find".
browser.find_element(By.NAME, 'btn_pesquisar').click()

# wait computer response.
timeResponse.sleep(4)

# set variables values according web result.
address = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
district = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
state = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
cep = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text

print(address + '\n' +
      district + '\n' +
      state + '\n' +
      cep)
