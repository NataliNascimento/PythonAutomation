from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
import pyautogui as timeResponse
import pyautogui as keyboardFunctions

# get browser that will use.
browser = seleniumOptions.Chrome()

# open url to get the data
browser.get('https://www.magazineluiza.com.br/')

# find id from label search and type the name of the product.
browser.find_element(By.ID, 'input-search').send_keys('geladeira')

# wait computer response.
timeResponse.sleep(2)

# send hotkey enter.
keyboardFunctions.press('enter')

# wait computer response.
timeResponse.sleep(4)

# for and if to find all elements from the products.
productList = browser.find_elements(By.CLASS_NAME, 'fwviCj')

for item in productList:
    productName = ''
    produtPrice = ''
    productUrl = ''

    if productName == '':
        try:
            productName = item.find_element(By.CLASS_NAME, 'hQYVAI').text
        except Exception:
            pass
    elif productName == '':
        try:
            productName = item.find_element(By.CLASS_NAME, 'sc-hFVsQR').text
        except Exception:
            pass

    print(productName)
