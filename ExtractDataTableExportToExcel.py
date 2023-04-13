# this script will extract data from Chrome and save the values in excel.

from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
import pandas as pd

# get browser that will use.
browser = seleniumOptions.Chrome()

# open rpa browser to get the data.
browser.get('https://rpachallengeocr.azurewebsites.net/')

# find xpath according table element.
tableElement = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

# extract rows and columns finding the tag.
rows = browser.find_elements(By.TAG_NAME, 'tr')
columns = browser.find_elements(By.TAG_NAME, 'td')
row = 1
dataFrameList = []

# for using to cycle through the data within the table and add value in dataFrameList.
for currentLine in rows:

    print(currentLine.text)
    dataFrameList.append(currentLine.text)
    row += 1

# create excel file extractdatachrome.xlsx and save workbook.
excelFile = pd.ExcelWriter('ExtractDataChrome.xlsx', engine='xlsxwriter')
excelFile._save()

# add column dados and values from dataFrameList.
dataFrame = pd.DataFrame(dataFrameList, columns=['Dados'])
excelFile = pd.ExcelWriter('ExtractDataChrome.xlsx', engine='xlsxwriter')

# convert the workboot to excel, add sheet and save.
dataFrame.to_excel(excelFile, sheet_name='Sheet1', index=False)
excelFile._save()
