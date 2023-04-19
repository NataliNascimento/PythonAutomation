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
browser.find_element(By.NAME, 'endereco').send_keys('06764040')

# wait computer response.
timeResponse.sleep(2)

# press button "find".
browser.find_element(By.NAME, 'btn_pesquisar').click()

# wait computer response.
timeResponse.sleep(4)

# find xpath from table.
elementTable = browser.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

for tableRow in elementTable.find_elements(By.TAG_NAME, 'tr'):
    address = ''
    for columnTable in tableRow.find_elements(By.TAG_NAME, 'td'):
        address = address + '\n' + columnTable.text

print(address)
