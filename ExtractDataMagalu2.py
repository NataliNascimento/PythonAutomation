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

    if produtPrice == '':
        try:
            productPrice = item.find_element(By.CLASS_NAME, 'sc-kDvujY').text
        except Exception:
            pass
    elif productPrice == '':
        try:
            productPrice = item.find_element(By.CLASS_NAME, 'jDmBNY').text
        except Exception:
            pass

    elif productPrice == '':
        try:
            produtPrice = item.find_element(By.CLASS_NAME, 'sc-hGglLj').text
        except Exception:
            pass

    elif productPrice == '':
        try:
            productPrice = item.find_element(By.CLASS_NAME, 'bQqJoc').text
        except Exception:
            pass

    else:
        productPrice = '0'

    if productUrl == '':
        try:
            productUrl = item. find_element(By.TAG_NAME, 'a').get_attribute('href')
        except Exception:
            pass

    else:
        productUrl = '-'

    print(productName + ' - ' + productPrice)
    print(productUrl)
        