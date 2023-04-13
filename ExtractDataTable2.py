# this script will open Chrome browser and extract all datas from datatable.

from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
import pyautogui as timeResponse

# get browser that will use.
browser = seleniumOptions.Chrome()

# open url to get the data.
browser.get('https://rpachallengeocr.azurewebsites.net/')

i = 1
row = 1

while i < 4:
    # find xpath according table element
    tableElement = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    # extract rows and columns finding the tag.
    rows = browser.find_elements(By.TAG_NAME, 'tr')
    columns = browser.find_elements(By.TAG_NAME, 'td')

    # for using to cycle through the data within the table.
    for currentLine in rows:
        print(currentLine.text)
        row += 1
    i += 1

    # wait computer response.
    timeResponse.sleep(2)

    # find xpath according Next button element.
    browser.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    # wait computer response.
    timeResponse.sleep(2)

else:
    print('End of process.')
