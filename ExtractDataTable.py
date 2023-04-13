# this script will open Chrome browser and extract a datatable.

from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By

# get browser that will use.
browser = seleniumOptions.Chrome()

# open url to get the data
browser.get('https://rpachallengeocr.azurewebsites.net/')

# find xpath according table element
tableElement = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

# extract rows and columns finding the tag.
rows = tableElement.find_elements(By.TAG_NAME, 'tr')
columns = tableElement.find_elements(By.TAG_NAME, 'td')
row = 1

# for using to cycle through the data within the table.
for currentLine in rows:

    print(currentLine.text)

    row += 1
